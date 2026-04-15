from __future__ import annotations

import json
import logging
import re
import time
from typing import Any

import requests
from tenacity import retry, stop_after_attempt, wait_fixed

from ..models import EpisodeDraft
from ..settings import load_settings
from .validate import assemble_script

logger = logging.getLogger(__name__)


def _word_count(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text or ""))


def _build_user_prompt(manifest: dict, settings, force_length: bool = False) -> str:
    compact_sources = []
    for src in manifest.get("sources", [])[:120]:
        compact_sources.append(
            {
                "title": src.get("title"),
                "domain": src.get("domain"),
                "url": src.get("url"),
                "published_at": src.get("published_at"),
                "summary": src.get("summary"),
                "content_text": (src.get("content_text") or "")[:2200],
                "relevance_score": src.get("relevance_score", 0.0),
            }
        )

    target_words = max(settings.min_script_words + 400, 2500)

    schema = {
        "episode_title": "string — short, factual, no clickbait",
        "episode_summary": "string — 2-3 sentence summary of the episode",
        "opening_news_title": "string — the most impactful headline of the day",
        "highlights_label": "1-2 words summarizing the day's theme",
        "tomorrow_pedagogical_concept": "one short sentence fragment, no more than 12 words, announcing a concept to explain tomorrow",
        "sections": {
            # IMPORTANT: variable paragraph count per section. One paragraph = ONE
            # distinct story/fact. Do NOT pad. Do NOT write synthesis paragraphs
            # that recombine facts already stated elsewhere. If a fact only fills
            # 60 words cleanly, write 60 and move on — never stretch to hit a quota.
            "ai_news": [
                "5 to 8 paragraphs of 80-110 words each. ONE story per paragraph: launch, partnership, funding, or major corporate move. Lead with the biggest of the day. No transitions between stories inside this section — end one, start the next.",
            ],
            "use_cases_and_deployments": [
                "4 to 6 paragraphs of 80-110 words each. ONE deployment per paragraph — who deployed what, on what scale, with what measurable result. Prefer numbers (revenue %, latency ms, users, cost delta).",
            ],
            "tools_and_practice": [
                "3 to 5 paragraphs of 80-110 words each. ONE tool or technique per paragraph — what a practitioner can now do that they couldn't yesterday, with the name of the tool and the concrete capability.",
            ],
            "weak_signals_and_trends": [
                "1 to 2 paragraphs of 80-110 words each. ONE concrete signal per paragraph, each grounded in AT LEAST TWO distinct cited facts (different companies, different domains, or different papers). NEVER a synthesis of what you already said in the previous sections. If you have no genuine signal, write only one paragraph and keep it tight.",
            ],
            "research_and_breakthroughs": [
                "2 to 4 paragraphs of 80-110 words each. ONE result per paragraph — paper title or lab, what was achieved (one concrete number or comparison), and why it matters in one sentence. No method explanation unless a finance exec could not otherwise understand the result.",
            ],
            "education_and_pedagogy": [
                "exactly 2 paragraphs of 80-110 words each. Paragraph 1: one concept introduced with a concrete analogy. Paragraph 2: why the concept matters in practice today — tie to ONE of the stories covered earlier. No third paragraph.",
            ],
        },
    }

    length_instructions = (
        f"Your script MUST contain at least {settings.min_script_words} words total across all paragraphs. "
        f"Target {target_words} words. The range you are aiming for is 14 to 18 spoken minutes. "
        "Each paragraph MUST be between 80 and 110 words. Never shorter than 80. Never longer than 110. "
        "Each paragraph covers ONE distinct story or fact — one story per paragraph, never merge two into one, never split one across two. "
        "If a story only carries 60 words of actual substance, DO NOT stretch it. Pick another story from the manifest instead. "
        "Produce between 18 and 28 paragraphs total across all sections, distributed per the schema ranges. "
        "Hitting the word target comes from COVERING MORE STORIES, not from inflating paragraphs. "
    )

    if force_length:
        length_instructions += (
            "CRITICAL: Your previous output was TOO SHORT. You MUST cover MORE distinct stories "
            "from the source manifest. Do NOT lengthen existing paragraphs. Do NOT add synthesis "
            "paragraphs. Add NEW paragraphs each covering a NEW story with its own facts: company "
            "name, number, product name, or result. Dig deeper into the manifest — there are 120 "
            "sources there, use them. "
        )

    # Weekly recap context
    if settings.profile_name == 'weekly_recap':
        length_instructions += (
            "This is a WEEKLY RECAP covering the entire past week. "
            "Prioritize the biggest stories that generated buzz. "
            "Also highlight important news that may have been missed in daily episodes. "
            "Sources with higher relevance_score are more likely to be unused — prioritize them. "
            "Use natural time references when covering stories from different days. "
        )

    payload = {
        "constraints": {
            "title": settings.podcast_title,
            "subtitle": settings.podcast_subtitle,
            "target_duration_min": settings.target_duration_min,
            "target_duration_max": settings.target_duration_max,
            "minimum_script_words": settings.min_script_words,
            "target_script_words": target_words,
            "min_source_count": settings.min_source_count,
            "required_output": schema,
        },
        "instructions": (
            "Return JSON only. Do not include markdown fences or any text outside the JSON. "
            "TONE: You are a press analyst writing for busy senior professionals, in the register of "
            "Stratechery or Les Echos Briefing — NOT a radio host. Fact → number → concrete consequence "
            "in one action verb. The listener draws the lesson; you never draw it for them. "
            "No bullet points. No headings inside paragraphs. "
            "DENSITY (hard rule): Every paragraph must contain at least TWO distinct numbers OR at least "
            "TWO distinct proper nouns (company, product, researcher, country, dataset, paper). "
            "If a story cannot carry that density, pick another story from the manifest. "
            "FORBIDDEN: meta-commentary ('this matters because', 'this shows that', 'pour les entreprises, "
            "ça signifie que'), generic management lessons ('don't bet on one horse', 'without adoption, "
            "the best model stays unused'), forward-looking platitudes ('this opens the way to', 'it's a "
            "key step', 'ça ouvre la voie à'), synthesis paragraphs that recombine earlier facts without "
            "adding new ones, and restating a story in a later section. "
            "NO RECYCLING: A fact, company, product, or study may be cited in ONE paragraph only across "
            "the entire script. Callbacks by single-name reference ('as Meta showed') are allowed only "
            "in the education section, never elsewhere. "
            "NUMBERS: Round aggressively ('about 1.2 billion' not '1,247,000,000'). Skip model version "
            "numbers ('the latest GPT' not 'GPT-4o-2024-05-13'). "
            "ACRONYMS: Write them so the TTS reads them naturally. If the acronym is pronounced as a word "
            "in its native language (SOLARIS, NASA, RADAR, LASER), keep it uppercase as-is. If it is spelled "
            "out letter by letter (GPU, CPU, API, LLM, LCA, RPRA, IA), keep it uppercase as-is — the voice "
            "will read the letters. NEVER expand an acronym mid-sentence ('les unités de traitement graphique "
            "— ou GPU'); introduce it once at first occurrence with a short parenthetical only if strictly "
            "needed for comprehension, then reuse the bare acronym. "
            "FLOW: Within a pillar, no transitions between stories — end one paragraph, start the next with "
            "the next story's subject. "
            "PILLAR SIGNPOSTS: The first paragraph of every pillar after AI News opens with a SHORT factual "
            "signpost of 3 to 6 words, then a period, then the first fact. Examples (FR): 'Côté déploiements.' / "
            "'Côté outils.' / 'Un signal à surveiller.' / 'Côté recherche.' / 'Un concept à retenir.' (EN: "
            "'Turning to deployments.' / 'On tools.' / 'One signal to watch.' / 'On the research front.' / "
            "'One concept to keep.'). Never speak the pillar name itself. Never use pontificating bridges "
            "like 'Pulling back from the day's news, a few patterns are worth flagging' — this is dead air. "
            "RHYTHM: Vary sentence length. Short sentences are allowed and encouraged. Use dashes and commas "
            "for pauses. Use contractions (it's, they've, ca, c'est, on). Write for the ear, not the eye. "
            "Prioritize sources with the highest relevance_score. Cross-reference multiple sources on the "
            "same topic to sharpen a single paragraph's facts, not to create extra paragraphs. "
            + length_instructions
        ).strip(),
        "source_manifest": compact_sources,
    }
    return json.dumps(payload, ensure_ascii=False)


def _response_error_text(response: requests.Response) -> str:
    try:
        data = response.json()
        if isinstance(data, dict):
            if isinstance(data.get("error"), dict):
                return str(data["error"].get("message") or data["error"])
            return str(data)
    except Exception:
        pass
    return response.text.strip()[:500]


def _extract_message_content(data: dict[str, Any]) -> str:
    try:
        message = data["choices"][0]["message"]["content"]
    except Exception as exc:
        raise ValueError(f"Malformed LLM response: {data}") from exc

    if isinstance(message, str):
        return message

    if isinstance(message, list):
        parts: list[str] = []
        for item in message:
            if isinstance(item, dict) and item.get("type") == "text":
                parts.append(item.get("text", ""))
        return "\n".join(parts).strip()

    return str(message).strip()


def _post_chat_completion(settings, payload: dict[str, Any]) -> dict[str, Any]:
    base_url = (settings.llm_base_url or "").strip().rstrip("/")
    if not base_url.startswith("http"):
        raise ValueError(f"Invalid LLM_BASE_URL: {base_url!r}")
    from urllib.parse import urlparse
    parsed = urlparse(base_url)
    hostname = parsed.hostname or ""
    if hostname in ("localhost", "127.0.0.1", "0.0.0.0") or hostname.startswith("169.254.") or hostname.startswith("10.") or hostname.startswith("192.168."):
        raise ValueError(f"LLM_BASE_URL points to a private/internal address: {base_url!r}")

    url = f"{base_url}/chat/completions"
    headers = {"Content-Type": "application/json"}
    if settings.llm_api_key:
        headers["Authorization"] = f"Bearer {settings.llm_api_key}"

    try:
        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=max(settings.llm_timeout_seconds, 180),
        )
    except requests.RequestException as exc:
        raise ValueError(f"LLM connection error to {parsed.hostname}") from exc

    if response.status_code >= 400:
        raise ValueError(f"LLM HTTP {response.status_code}: {_response_error_text(response)}")

    try:
        return response.json()
    except Exception as exc:
        raise ValueError(f"LLM returned non-JSON response: {response.text[:500]}") from exc


def _create_completion_data(
    settings,
    model: str,
    messages: list[dict[str, str]],
    temperature: float,
    max_tokens: int,
) -> dict[str, Any]:
    payload = {
        "model": model,
        "temperature": temperature,
        "messages": messages,
        "max_tokens": max_tokens,
        "response_format": {"type": "json_object"},
    }

    try:
        return _post_chat_completion(settings, payload)
    except Exception as exc:
        message = str(exc).lower()
        if "json_object" in message or "response format" in message or "405" in message:
            logger.info("Model does not support response_format, retrying without it")
            payload.pop("response_format", None)
            return _post_chat_completion(settings, payload)
        raise


def _extract_json(content: str) -> dict[str, Any]:
    cleaned = content.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
        cleaned = re.sub(r"\s*```$", "", cleaned)
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        # Find the outermost JSON object by matching braces
        start = cleaned.find("{")
        if start == -1:
            raise ValueError(f"Model did not return valid JSON. First 500 chars: {content[:500]}")
        depth = 0
        for i, ch in enumerate(cleaned[start:], start):
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(cleaned[start:i + 1])
                    except json.JSONDecodeError:
                        break
        raise ValueError(f"Model did not return valid JSON. First 500 chars: {content[:500]}")


def _generate_with_model(model: str, manifest: dict, settings, force_length: bool) -> dict[str, Any]:
    messages = [
        {"role": "system", "content": settings.prompt_path.read_text(encoding="utf-8")},
        {"role": "user", "content": _build_user_prompt(manifest, settings, force_length=force_length)},
    ]

    start = time.monotonic()
    data = _create_completion_data(
        settings=settings,
        model=model,
        messages=messages,
        temperature=settings.llm_temperature,
        max_tokens=settings.llm_max_tokens,
    )
    elapsed = time.monotonic() - start

    content = _extract_message_content(data)
    if not content.strip():
        raise ValueError("Model returned empty content")

    usage = data.get("usage", {})
    logger.info(
        "LLM call completed: model=%s elapsed=%.1fs prompt_tokens=%s completion_tokens=%s",
        model, elapsed,
        usage.get("prompt_tokens", "?"),
        usage.get("completion_tokens", "?"),
    )

    return _extract_json(content)


@retry(wait=wait_fixed(3), stop=stop_after_attempt(2))
def generate_episode_script(manifest: dict, local_preview: bool = False, profile: str | None = None) -> EpisodeDraft:
    settings = load_settings(local_preview=local_preview, profile=profile)

    source_count = manifest.get("source_count", 0)
    if source_count < settings.min_source_count:
        raise ValueError(
            f"Not enough relevant sources: {source_count} < {settings.min_source_count}"
        )

    errors: list[str] = []

    models = [settings.llm_editor_model]
    if settings.llm_fallback_model:
        models.append(settings.llm_fallback_model)

    max_length_retries = 4  # nombre de tentatives par modele si trop court

    for model in models:
        try:
            logger.info("Generating script with model: %s (profile=%s)", model, settings.profile_name)

            best_payload = None
            best_script = None
            best_wc = 0

            for attempt in range(max_length_retries):
                force = attempt > 0
                logger.info("Attempt %d/%d (force_length=%s)", attempt + 1, max_length_retries, force)

                try:
                    payload = _generate_with_model(model, manifest, settings, force_length=force)
                    script = assemble_script(
                        manifest["run_date"],
                        payload,
                        intro_format=settings.intro_format,
                        locale=settings.locale,
                    )
                    wc = _word_count(script)
                except Exception as inner_exc:
                    logger.warning("Attempt %d failed: %s", attempt + 1, inner_exc)
                    continue

                logger.info("Attempt %d produced %d words", attempt + 1, wc)

                if wc > best_wc:
                    best_payload = payload
                    best_script = script
                    best_wc = wc

                if wc >= settings.min_script_words:
                    break

                logger.warning(
                    "Script too short: %d words < %d minimum, retrying...",
                    wc, settings.min_script_words,
                )

            if best_wc < settings.min_script_words:
                raise ValueError(
                    f"Script too short after {max_length_retries} attempts: "
                    f"{best_wc} words < {settings.min_script_words} minimum"
                )

            logger.info("Script generated successfully: %d words, model=%s", best_wc, model)
            return EpisodeDraft(
                episode_title=best_payload.get("episode_title", settings.podcast_title),
                episode_summary=best_payload.get("episode_summary", settings.podcast_description_short),
                opening_news_title=best_payload.get("opening_news_title", ""),
                script=best_script,
                tomorrow_concept=best_payload.get("tomorrow_pedagogical_concept", ""),
                highlights_label=best_payload.get("highlights_label", "Highlights"),
            )
        except Exception as exc:
            logger.error("Model %s failed: %s", model, exc)
            errors.append(f"{model}: {exc}")

    raise ValueError("All editorial generation attempts failed: " + " | ".join(errors))
