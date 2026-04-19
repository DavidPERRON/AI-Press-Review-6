from __future__ import annotations

import json
import logging
import random
import re
import sys
import time
from pathlib import Path
from typing import Any

import requests

from ..models import EpisodeDraft
from ..settings import load_settings
from ..utils import atomic_write_text, write_json
from .validate import assemble_script

logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────────────────────────────────────
# Typed exception hierarchy
# ─────────────────────────────────────────────────────────────────────────────
#
# 2026-04-16: production crashed because the retry loop treated every failure
# the same. Quota exhaustion (HTTP 429) burned all 4 attempts in ~5 seconds
# because we used `wait_fixed(3)` instead of respecting `Retry-After`. Then
# the misleading message "Script too short: 0 words" hid the real cause.
#
# Splitting the failure modes lets the loop:
#   • Pause appropriately on quota — long, jittered, capped wait.
#   • Pause briefly on transient 5xx — exponential backoff.
#   • Switch model immediately on quota that won't recover within budget.
#   • Skip retry entirely on validation errors that will never get better
#     by waiting (malformed JSON from same prompt, etc.).
class LLMError(Exception):
    """Base class for editorial LLM call failures."""


class LLMQuotaError(LLMError):
    """HTTP 429 / explicit quota signal. Carries Retry-After hint when present."""

    def __init__(self, message: str, retry_after_s: float | None = None) -> None:
        super().__init__(message)
        self.retry_after_s = retry_after_s


class LLMTransientError(LLMError):
    """HTTP 5xx, connection drop, or timeout. Worth a backed-off retry."""


class LLMInvalidResponseError(LLMError):
    """Model returned malformed JSON or empty content. A single retry only."""


class LLMShortScriptError(LLMError):
    """Script came back under min_script_words. Retry with force_length=True."""

    def __init__(self, message: str, word_count: int) -> None:
        super().__init__(message)
        self.word_count = word_count


# HTTP status code groups
_QUOTA_HTTP_CODES = (429,)
_TRANSIENT_HTTP_CODES = (500, 502, 503, 504)


def _word_count(text: str) -> int:
    r"""Honest spoken-word count: whitespace-separated tokens.

    Earlier used re.findall(r"\b\w+\b", ...) which inflated French counts
    by ~10-15% because apostrophes split "c'est"/"l'IA"/"d'Anthropic" into
    two matches each. That made the min_script_words gate pass on scripts
    that spoke for far less than target_duration_min — observed 2026-04-17
    FR weekly: 2174 split-words (~11m54s audio) sailed past a 2200 regex-
    gate while the audio was 6 minutes short of the 18-min minimum.
    Using split() aligns the count with what the TTS will actually speak.
    """
    return len((text or "").split())


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

    # Target well above the minimum so the LLM aims for the middle of the
    # target duration band. At ~180 WPM, 22 min = 3960 words, 25 min = 4500.
    # Overshoot the minimum by 500 words to leave room for TTS variance and
    # avoid dancing on the gate.
    target_words = max(settings.min_script_words + 500, 3500)

    if settings.profile_name == 'weekly_recap':
        schema = {
            "episode_title": "string — short weekly recap title, factual, no clickbait",
            "episode_summary": (
                "string — exactly 3 sentences: "
                "(1) the biggest story of the week with key actor and outcome; "
                "(2) the most concrete deployment or use case of the week; "
                "(3) one concrete item to watch in the coming week. "
                "No filler. Pure facts."
            ),
            "highlights_label": "1-2 words summarizing the week's dominant theme",
            "sections": {
                # PART 1 (~15 min): intro + this week's news + this week's use cases
                # PART 2 (~5 min): what to watch next week (news only)
                # One paragraph = ONE distinct story/fact. No padding.
                "weekly_intro": [
                    "KEY NAME IS 'weekly_intro' — do not rename. "
                    "EXACTLY 1 paragraph of 60-70 words. No more. "
                    "Straight to the point: name the top story of the week, state what's in this episode "
                    "(Friday news + off-radar signals + week ahead), tease the off-radar segment in one punchy sentence. "
                    "No filler, no 'Welcome back', no paragraph numbering. "
                    "Reference Friday explicitly ('this Friday' / 'hier vendredi' in FR).",
                ],
                "weekly_news": [
                    "KEY NAME IS 'weekly_news' — do not rename. "
                    "12 to 22 paragraphs of 80-110 words each. "
                    "IMPORTANT: use ONLY sources published on the most recent Friday in the manifest — "
                    "do NOT include news from earlier in the week. "
                    "Also include any post-NYSE-close developments or overnight signals (Asian markets, "
                    "after-hours moves, late-breaking announcements) if present in the manifest. "
                    "Friday's biggest AI news stories in order of impact. ONE story per paragraph — launch, funding, "
                    "partnership, major corporate move, or market reaction. "
                    "FINANCIAL ANGLE: when a story moved a stock or triggered a market reaction, include "
                    "the % move and ticker. Funding rounds must state valuation and lead investor. "
                    "Lead with the most impactful Friday story. "
                    "You may use 'yesterday', 'this Friday', or 'after the close' as time references. "
                    "No transitions between stories — end one paragraph, start the next with the next story's subject. "
                    "No signpost needed: the intro already set the context.",
                ],
                "weekly_use_cases": [
                    "KEY NAME IS 'weekly_use_cases' — do not rename. "
                    "7 to 10 paragraphs of 80-110 words each. "
                    "IMPORTANT: use ONLY deployment news published on the most recent Friday in the manifest. "
                    "Friday's most concrete AI deployments. ONE deployment per paragraph. "
                    "Prefer numbers: revenue %, latency ms, users, cost delta, headcount. "
                    "First paragraph opens with a short signpost — "
                    "FR: 'Côté déploiements.' | EN: 'On deployments.' "
                    "— then a period, then the first fact.",
                ],
                "weekly_offradar": [
                    "KEY NAME IS 'weekly_offradar' — do not rename. "
                    "3 to 5 paragraphs of 80-110 words each. "
                    "Signals absent from mainstream tech media but material for AI business strategy. "
                    "Draw from: specialized AI research blogs, non-anglophone sources (Asian markets, "
                    "European labs, government filings), academic preprints not yet covered, "
                    "niche industry verticals, open-source releases from non-famous actors, "
                    "hiring patterns, quiet acquisitions, regulatory moves outside the US. "
                    "ONE signal per paragraph — novelty and forward-looking relevance over volume. "
                    "Never repeat a story already covered in weekly_news or weekly_use_cases. "
                    "First paragraph opens with a short signpost — "
                    "FR: 'Sous le radar.' | EN: 'Off the radar.' "
                    "— then a period, then the first signal.",
                ],
                "weekly_next_week": [
                    "KEY NAME IS 'weekly_next_week' — do not rename. "
                    "3 to 5 paragraphs of 80-110 words each. "
                    "What to watch in the coming week: announced product launches, earnings calls, regulatory "
                    "decisions, policy hearings, IPOs, investor days, or research papers about to drop. "
                    "FINANCIAL ANGLE: prioritize events with market implications — earnings calls (name the company "
                    "and consensus estimate if known), IPOs, central bank decisions affecting tech spending. "
                    "Also flag any overnight or Asian market signal from Friday that could set the tone for Monday. "
                    "ONE item per paragraph. News and announced facts only — no tools, no research, no pedagogy. "
                    "First paragraph opens with a short signpost — "
                    "FR: 'Ce qu'il faut surveiller la semaine prochaine.' | EN: 'Looking ahead to next week.' "
                    "— then a period, then the first item. "
                    "Ground each item in a concrete signal from this week's news.",
                ],
            },
        }
    else:
        schema = {
            "episode_title": "string — short, factual, no clickbait",
            "episode_summary": (
                "string — exactly 3 sentences: "
                "(1) the top news finding of the day with the key actor and outcome; "
                "(2) one concrete use-case or deployment highlighted in this episode; "
                "(3) what practitioners or professionals can act on or watch. "
                "No filler. No 'this episode covers'. Pure facts."
            ),
            "opening_news_title": "string — the most impactful headline of the day",
            "highlights_label": "1-2 words summarizing the day's theme",
            "sections": {
                # IMPORTANT: variable paragraph count per section. One paragraph = ONE
                # distinct story/fact. Do NOT pad. Do NOT write synthesis paragraphs
                # that recombine facts already stated elsewhere. If a fact only fills
                # 60 words cleanly, write 60 and move on — never stretch to hit a quota.
                "daily_intro": [
                    "KEY NAME IS 'daily_intro' — do not rename. "
                    "EXACTLY 1 paragraph of 50-70 words. "
                    "Very brief spoken opening: name the 2-3 biggest stories in one tight sentence each, "
                    "then close with ONE sentence teasing the off-radar segment — "
                    "FR: something like 'Et sous le radar, [1 fact/signal that Bloomberg hasn't covered].' "
                    "EN: 'Off the radar, [1 fact/signal the mainstream missed].' "
                    "No greeting. No 'welcome'. No 'today we cover'. Start directly with the first story.",
                ],
                "ai_news": [
                    "6 to 10 paragraphs of 80-110 words each. ONE story per paragraph: launch, partnership, funding, or major corporate move. Lead with the biggest of the day. No transitions between stories inside this section — end one, start the next.",
                ],
                "use_cases_and_deployments": [
                    "5 to 8 paragraphs of 80-110 words each. ONE deployment per paragraph — who deployed what, on what scale, with what measurable result. Prefer numbers (revenue %, latency ms, users, cost delta).",
                ],
                "tools_and_practice": [
                    "4 to 6 paragraphs of 80-110 words each. ONE tool or technique per paragraph — what a practitioner can now do that they couldn't yesterday, with the name of the tool and the concrete capability.",
                ],
                "weak_signals_and_trends": [
                    "2 to 3 paragraphs of 80-110 words each. ONE concrete signal per paragraph, each grounded in AT LEAST TWO distinct cited facts (different companies, different domains, or different papers). NEVER a synthesis of what you already said in the previous sections. If you have no genuine signal, write only two paragraphs and keep them tight.",
                ],
                "daily_offradar": [
                    "KEY NAME IS 'daily_offradar' — do not rename. "
                    "2 to 4 paragraphs of 80-110 words each. "
                    "Signals absent from mainstream tech media but material for AI business strategy. "
                    "Draw from: specialized AI research blogs, non-anglophone sources (Asian markets, "
                    "European labs, government filings), academic preprints not yet covered, "
                    "niche industry verticals, open-source releases from non-famous actors, "
                    "hiring patterns, quiet acquisitions, regulatory moves outside the US. "
                    "ONE signal per paragraph — novelty and forward-looking relevance over volume. "
                    "Never repeat a story already covered earlier in this script. "
                    "First paragraph opens with: FR 'Sous le radar.' | EN 'Off the radar.' "
                    "— then a period, then the first signal.",
                ],
                "research_and_breakthroughs": [
                    "3 to 5 paragraphs of 80-110 words each. ONE result per paragraph — paper title or lab, what was achieved (one concrete number or comparison), and why it matters in one sentence. No method explanation unless a finance exec could not otherwise understand the result.",
                ],
            },
        }

    if settings.profile_name == 'weekly_recap':
        length_instructions = (
            f"Your script MUST contain at least {settings.min_script_words} words total across all paragraphs. "
            f"Target {target_words} words (~21 spoken minutes total: ~16 min for Friday news + deployments, ~5 min for next week). "
            "weekly_intro: exactly 1 paragraph of 60-70 words. All other paragraphs: 80-110 words each. Never shorter, never longer. "
            "One paragraph = one distinct story or fact. Never merge two stories. Never split one story across two paragraphs. "
            "weekly_news and weekly_use_cases MUST use ONLY sources from Friday — ignore earlier days. "
            "weekly_next_week may reference any recent signals to ground its forward-looking items. "
            "Sources with higher relevance_score should be prioritized. "
            f"Produce between 38 and 46 paragraphs total across all sections. "
            "Hitting the word target comes from COVERING MORE STORIES, not from inflating paragraphs. "
        )
        if force_length:
            length_instructions += (
                f"STRICT FLOOR: you MUST produce AT LEAST {settings.min_script_words} words and "
                "AT LEAST 40 paragraphs total. "
                "Expand weekly_news to at least 16 paragraphs and weekly_use_cases to at least 8. "
                "Each added paragraph must cover a NEW story with a company name, number, or concrete fact."
            )
    else:
        length_instructions = (
            f"Your script MUST contain at least {settings.min_script_words} words total across all paragraphs. "
            f"Target {target_words} words. The range you are aiming for is 14 to 18 spoken minutes. "
            "Each paragraph MUST be between 80 and 110 words. Never shorter than 80. Never longer than 110. "
            "Each paragraph covers ONE distinct story or fact — one story per paragraph, never merge two into one, never split one across two. "
            "If a story only carries 60 words of actual substance, DO NOT stretch it. Pick another story from the manifest instead. "
            "Produce between 24 and 36 paragraphs total across all sections, distributed per the schema ranges. "
            "Hitting the word target comes from COVERING MORE STORIES, not from inflating paragraphs. "
        )
        if force_length:
            # Same rationale as weekly: stateless API, no "previous output".
            length_instructions += (
                "CRITICAL REMINDER: this script MUST hit the word minimum above. "
                "You MUST cover MORE distinct stories from the source manifest. "
                "Do NOT lengthen existing paragraphs. Do NOT add synthesis "
                "paragraphs. Add NEW paragraphs each covering a NEW story with its own facts: company "
                "name, number, product name, or result. Dig deeper into the manifest — there are 120 "
                "sources there, use them. "
            )

    if settings.profile_name == 'weekly_recap':
        key_names_instruction = (
            "CRITICAL — WEEKLY SECTION KEYS (read this first): "
            "Your JSON response MUST contain a \"sections\" object with EXACTLY these five keys "
            "in EXACTLY this order: "
            "\"weekly_intro\", \"weekly_news\", \"weekly_use_cases\", \"weekly_offradar\", \"weekly_next_week\". "
            "Any other key name — including ai_news, use_cases_and_deployments, tools_and_practice, "
            "weak_signals_and_trends, research_and_breakthroughs, education_and_pedagogy, "
            "news, deployments, next_week, intro, off_radar, offradar, or ANY variation — will cause an immediate "
            "validation failure and your output will be discarded. "
            "There are exactly FIVE sections. No more, no less. "
        )
    else:
        key_names_instruction = ""

    if settings.profile_name == 'weekly_recap':
        signpost_instructions = (
            "SECTION SIGNPOSTS (weekly only): "
            "weekly_news has NO signpost — the intro sets the context. "
            "weekly_use_cases first paragraph opens with: FR 'Côté déploiements.' | EN 'On deployments.' "
            "weekly_offradar first paragraph opens with: FR 'Sous le radar.' | EN 'Off the radar.' "
            "weekly_next_week first paragraph opens with: FR 'Ce qu'il faut surveiller la semaine prochaine.' | EN 'Looking ahead to next week.' "
            "Never use pontificating bridges — no 'Pulling back from the week's news...' or equivalent. "
        )
        recycling_rule = (
            "NO RECYCLING: A fact, company, product, or study may be cited in ONE paragraph only across "
            "the entire script. Callbacks are never allowed in any section. "
        )
    else:
        signpost_instructions = (
            "SECTION SIGNPOSTS (daily): "
            "daily_intro has NO signpost — it IS the teaser. "
            "ai_news has NO signpost — it follows directly after the intro. "
            "Every section after ai_news opens with a SHORT factual signpost of 3 to 6 words, a period, then the first fact. "
            "Examples (FR): 'Côté déploiements.' / 'Côté outils.' / 'Un signal à surveiller.' / 'Sous le radar.' / 'Côté recherche.' "
            "(EN: 'On deployments.' / 'On tools.' / 'One signal to watch.' / 'Off the radar.' / 'On the research front.'). "
            "Never speak the section name itself. Never use pontificating bridges — dead air. "
        )
        recycling_rule = (
            "NO RECYCLING: A fact, company, product, or study may be cited in ONE paragraph only across "
            "the entire script. No callbacks of any kind in any section. "
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
            key_names_instruction +
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
            + recycling_rule +
            "NUMBERS: Round aggressively ('about 1.2 billion' not '1,247,000,000'). Skip model version "
            "numbers ('the latest GPT' not 'GPT-4o-2024-05-13'). "
            "ACRONYMS: Write them in their canonical uppercase form (TSMC, GPT, API, LLM, IA, PDG, IPO, USA). "
            "The TTS layer normalizes them to the correct spoken form, so DO NOT pre-spell them out, DO NOT "
            "expand them mid-sentence ('graphics processing units — or GPUs'), and DO NOT add letter-by-letter "
            "hints. Just write the acronym once in its canonical form and reuse it. "
            "FLOW: Within a section, no transitions between stories — end one paragraph, start the next with "
            "the next story's subject. "
            + signpost_instructions +
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


def _parse_retry_after(response: requests.Response) -> float | None:
    """Parse Retry-After header. Returns seconds-to-wait, or None if absent/invalid.

    Per RFC 7231 the value is either delta-seconds (an integer) or an HTTP-date.
    Most LLM gateways send seconds; we cap at 120s so a stuck retry doesn't
    block a daily run forever.
    """
    raw = response.headers.get('Retry-After') or response.headers.get('retry-after')
    if not raw:
        return None
    try:
        seconds = float(raw.strip())
    except (TypeError, ValueError):
        # HTTP-date format — rare from LLM APIs; treat as "no hint"
        return None
    if seconds < 0:
        return None
    return min(seconds, 120.0)


def _extract_message_content(data: dict[str, Any]) -> str:
    try:
        message = data["choices"][0]["message"]["content"]
    except Exception as exc:
        raise LLMInvalidResponseError(f"Malformed LLM response: {data}") from exc

    if isinstance(message, str):
        return message

    if isinstance(message, list):
        parts: list[str] = []
        for item in message:
            if isinstance(item, dict) and item.get("type") == "text":
                parts.append(item.get("text", ""))
        return "\n".join(parts).strip()

    return str(message).strip()


def _resolve_endpoint(model: str, settings) -> tuple[str, str]:
    """Resolve (base_url, api_key) for `model` based on which cascade tier it sits in.

    Per-tier overrides (LLM_<TIER>_BASE_URL[_<LOCALE>] / _API_KEY[_<LOCALE>])
    win over the generic LLM_BASE_URL / LLM_API_KEY. Empty per-tier values
    fall through to the generic pair, so single-provider deployments keep
    working unchanged.

    Why this exists: the 2026-04-19 weekly run failed when both editor (Claude)
    and fallback (GPT-5.1) on OpenRouter produced unusable output (one short,
    one wrong-schema). The emergency tier needs to be on a different provider
    so a single OpenRouter incident doesn't take down all three slots.
    """
    # getattr with defaults keeps unit tests using SimpleNamespace mocks happy
    # — they only set the model fields, not the per-tier endpoint fields.
    base = getattr(settings, 'llm_base_url', '') or ''
    key = getattr(settings, 'llm_api_key', '') or ''
    tier_prefix: str | None = None
    if model and model == getattr(settings, 'llm_emergency_model', None):
        tier_prefix = 'llm_emergency'
    elif model and model == getattr(settings, 'llm_fallback_model', None):
        tier_prefix = 'llm_fallback'
    elif model and model == getattr(settings, 'llm_editor_model', None):
        tier_prefix = 'llm_editor'
    if tier_prefix:
        per_base = getattr(settings, f'{tier_prefix}_base_url', '') or ''
        per_key = getattr(settings, f'{tier_prefix}_api_key', '') or ''
        env_prefix = tier_prefix.upper().replace('LLM_', '')
        if per_base:
            base = per_base
            if per_key:
                key = per_key
            else:
                # Per-tier base URL set but no matching key — fall through to the
                # generic LLM_API_KEY with a warning.
                logger.warning(
                    "LLM_%s_BASE_URL is set (%s) but LLM_%s_API_KEY[_<LOCALE>] is empty "
                    "— falling back to generic LLM_API_KEY. "
                    "If the target provider needs its own key, set LLM_%s_API_KEY.",
                    env_prefix, per_base, env_prefix, env_prefix,
                )
        elif per_key:
            # Per-tier key set WITHOUT a per-tier base URL: applying a provider-specific
            # key (e.g. DEEPINFRA_API_KEY) to the generic endpoint (e.g. OpenRouter)
            # sends the wrong credentials and causes HTTP 401. Ignore the stray key and
            # keep using the generic LLM_API_KEY for the generic endpoint.
            # Fix: set LLM_{TIER}_BASE_URL[_<LOCALE>] to point at the correct provider.
            logger.warning(
                "LLM_%s_API_KEY[_<LOCALE>] is set but LLM_%s_BASE_URL is empty "
                "— ignoring per-tier key to avoid sending wrong credentials to %r. "
                "Set LLM_%s_BASE_URL[_<LOCALE>] to route this tier to its own endpoint.",
                env_prefix, env_prefix, base, env_prefix,
            )
    return base, key


def _post_chat_completion(
    settings,
    payload: dict[str, Any],
    base_url_override: str | None = None,
    api_key_override: str | None = None,
) -> dict[str, Any]:
    base_url_raw = base_url_override if base_url_override else settings.llm_base_url
    api_key = api_key_override if api_key_override is not None else settings.llm_api_key

    base_url = (base_url_raw or "").strip().rstrip("/")
    if not base_url.startswith("http"):
        raise ValueError(f"Invalid LLM base URL: {base_url!r}")
    from urllib.parse import urlparse
    parsed = urlparse(base_url)
    hostname = parsed.hostname or ""
    if hostname in ("localhost", "127.0.0.1", "0.0.0.0") or hostname.startswith("169.254.") or hostname.startswith("10.") or hostname.startswith("192.168."):
        raise ValueError(f"LLM base URL points to a private/internal address: {base_url!r}")

    url = f"{base_url}/chat/completions"
    if not api_key:
        raise ValueError(
            f"No API key configured for LLM endpoint {parsed.hostname!r}. "
            "Set LLM_API_KEY, or for a per-tier provider endpoint also set "
            "LLM_<TIER>_BASE_URL[_<LOCALE>] and LLM_<TIER>_API_KEY[_<LOCALE>] "
            "(e.g. LLM_EMERGENCY_BASE_URL_EN + LLM_EMERGENCY_API_KEY_EN)."
        )
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

    try:
        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=max(settings.llm_timeout_seconds, 180),
        )
    except requests.RequestException as exc:
        raise LLMTransientError(f"LLM connection error to {parsed.hostname}: {exc}") from exc

    status = response.status_code
    if status in _QUOTA_HTTP_CODES:
        retry_after = _parse_retry_after(response)
        raise LLMQuotaError(
            f"LLM HTTP {status} (quota exhausted): {_response_error_text(response)}",
            retry_after_s=retry_after,
        )
    if status in _TRANSIENT_HTTP_CODES:
        raise LLMTransientError(
            f"LLM HTTP {status} (transient): {_response_error_text(response)}"
        )
    if status >= 400:
        # Permanent client error (400/401/403/404/422/etc.) — do not retry
        raise ValueError(f"LLM HTTP {status}: {_response_error_text(response)}")

    try:
        return response.json()
    except Exception as exc:
        raise LLMInvalidResponseError(
            f"LLM returned non-JSON response: {response.text[:500]}"
        ) from exc


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

    base_url, api_key = _resolve_endpoint(model, settings)

    try:
        return _post_chat_completion(
            settings, payload,
            base_url_override=base_url, api_key_override=api_key,
        )
    except ValueError as exc:
        # Permanent client errors only — re-attempt without response_format
        # if the model rejects that field (common with older OpenAI-compatible
        # endpoints). LLMQuota / Transient / Invalid errors fall through.
        message = str(exc).lower()
        if "json_object" in message or "response format" in message or "405" in message:
            logger.info("Model does not support response_format, retrying without it")
            payload.pop("response_format", None)
            return _post_chat_completion(
                settings, payload,
                base_url_override=base_url, api_key_override=api_key,
            )
        raise


def _extract_json(content: str) -> dict[str, Any]:
    cleaned = content.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
        cleaned = re.sub(r"\s*```$", "", cleaned)

    # Python's pure-Python JSON decoder is recursive. Very long arrays (e.g.
    # 40+ paragraphs × long strings) can overflow the default limit of 1000
    # frames. We temporarily raise the limit for the parse call only; the
    # previous value is restored in the finally block so we don't change the
    # process-wide default permanently.
    prev_limit = sys.getrecursionlimit()
    try:
        sys.setrecursionlimit(max(prev_limit, 5000))
        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            pass
        except RecursionError:
            raise LLMInvalidResponseError(
                "Model returned JSON too deeply nested to parse (RecursionError). "
                f"Response length: {len(content)} chars."
            )

        # Find the outermost JSON object by matching braces
        start = cleaned.find("{")
        if start == -1:
            raise LLMInvalidResponseError(
                f"Model did not return valid JSON. First 500 chars: {content[:500]}"
            )
        depth = 0
        for i, ch in enumerate(cleaned[start:], start):
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(cleaned[start:i + 1])
                    except (json.JSONDecodeError, RecursionError):
                        break
        raise LLMInvalidResponseError(
            f"Model did not return valid JSON. First 500 chars: {content[:500]}"
        )
    finally:
        sys.setrecursionlimit(prev_limit)


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

    # OpenRouter (and some other gateways) return HTTP 200 with an error
    # payload instead of a proper 4xx/5xx when the upstream rejects the
    # request (e.g. context overflow). Detect this before calling
    # _extract_message_content so we can raise the right exception class.
    if isinstance(data, dict) and "error" in data and "choices" not in data:
        err = data["error"]
        msg = str(err.get("message", err) if isinstance(err, dict) else err)
        # Context overflow is permanent — the same prompt will never fit.
        if any(kw in msg for kw in ("max_num_tokens", "prompt length", "context_length", "maximum context", "context window")):
            raise ValueError(f"LLM context overflow (permanent — prompt too large for this model): {msg[:300]}")
        raise LLMTransientError(f"LLM gateway error (upstream rejection): {msg[:300]}")

    content = _extract_message_content(data)
    if not content.strip():
        raise LLMInvalidResponseError("Model returned empty content")

    usage = data.get("usage", {})
    logger.info(
        "LLM call completed: model=%s elapsed=%.1fs prompt_tokens=%s completion_tokens=%s",
        model, elapsed,
        usage.get("prompt_tokens", "?"),
        usage.get("completion_tokens", "?"),
    )

    return _extract_json(content)


# ─────────────────────────────────────────────────────────────────────────────
# Backoff helpers
# ─────────────────────────────────────────────────────────────────────────────

def _sleep_with_backoff(attempt: int, base: float = 2.0, cap: float = 60.0) -> None:
    """Sleep for `min(cap, base * 2^attempt) + jitter` seconds.

    Used between transient-error retries within the same model. Jitter avoids
    synchronized thundering-herd across parallel matrix jobs that share a
    free-tier quota.
    """
    delay = min(cap, base * (2 ** attempt))
    delay += random.uniform(0, min(delay * 0.25, 2.0))
    logger.info("Backing off %.1fs before retry (attempt=%d)", delay, attempt)
    time.sleep(delay)


def _sleep_for_quota(retry_after_s: float | None, attempt: int) -> None:
    """Honor server-supplied Retry-After when present, else exponential.

    Floors at 8s because free-tier quotas typically reset on minute boundaries
    and a 1s wait is just going to bounce off 429 again.
    """
    floor = 8.0
    if retry_after_s is not None and retry_after_s > 0:
        delay = max(retry_after_s + random.uniform(0, 2.0), floor)
    else:
        delay = max(min(60.0, 5.0 * (2 ** attempt)) + random.uniform(0, 3.0), floor)
    logger.warning("Quota hit — sleeping %.1fs before next attempt", delay)
    time.sleep(delay)


# ─────────────────────────────────────────────────────────────────────────────
# Per-model attempt loop
# ─────────────────────────────────────────────────────────────────────────────
#
# Per-model budget:
#   • Up to MAX_LENGTH_RETRIES content attempts (force_length on retry).
#   • MAX_QUOTA_HITS quota errors before we stop wasting time and cascade to
#     the next model — quota usually doesn't recover within one daily run.
#   • MAX_TRANSIENT_RETRIES backed-off retries on 5xx / connection errors.
#   • One retry on malformed JSON (might be a transient glitch, never worth
#     more than one extra spin).

MAX_LENGTH_RETRIES = 3
MAX_QUOTA_HITS = 2
MAX_TRANSIENT_RETRIES = 3
MAX_INVALID_JSON_RETRIES = 1


def _try_generate_one(
    model: str,
    manifest: dict,
    settings,
    force_length: bool,
) -> tuple[dict[str, Any], str, int]:
    """One outer attempt: generate, assemble script, count words.

    Internally retries on transient/quota/JSON failures with appropriate
    backoff. Raises LLMQuotaError or LLMTransientError if the per-attempt
    budgets for those classes are exhausted, so the outer caller can decide
    to cascade to the next model.
    """
    quota_hits = 0
    transient_hits = 0
    invalid_json_hits = 0

    while True:
        try:
            payload = _generate_with_model(model, manifest, settings, force_length=force_length)
            script = assemble_script(
                manifest["run_date"],
                payload,
                intro_format=settings.intro_format,
                locale=settings.locale,
            )
            wc = _word_count(script)
            return payload, script, wc

        except LLMQuotaError as exc:
            quota_hits += 1
            if quota_hits > MAX_QUOTA_HITS:
                logger.warning(
                    "Quota budget exhausted for model %s (%d hits) — cascading",
                    model, quota_hits,
                )
                raise
            _sleep_for_quota(exc.retry_after_s, quota_hits)

        except LLMTransientError as exc:
            transient_hits += 1
            if transient_hits > MAX_TRANSIENT_RETRIES:
                logger.warning(
                    "Transient budget exhausted for model %s (%d hits): %s — cascading",
                    model, transient_hits, exc,
                )
                raise
            _sleep_with_backoff(transient_hits)

        except LLMInvalidResponseError as exc:
            invalid_json_hits += 1
            if invalid_json_hits > MAX_INVALID_JSON_RETRIES:
                logger.warning(
                    "Invalid-JSON budget exhausted for model %s — cascading: %s",
                    model, exc,
                )
                # Re-raise as transient so the outer caller treats this as a
                # cascade trigger rather than a hard stop.
                raise LLMTransientError(str(exc)) from exc
            # Brief pause on JSON glitch — usually a sampling artefact.
            time.sleep(2.0)


def _generate_for_model(
    model: str,
    manifest: dict,
    settings,
) -> tuple[dict[str, Any] | None, str | None, int]:
    """Multi-attempt loop for a single model: get the longest script under budget.

    Returns (best_payload, best_script, best_wc). Caller decides whether
    best_wc >= min_script_words is acceptable or it's time to cascade.
    Raises if the model itself is unusable (quota / transient budget).
    """
    best_payload = None
    best_script = None
    best_wc = 0

    last_exc: Exception | None = None

    for attempt in range(MAX_LENGTH_RETRIES):
        force = attempt > 0
        logger.info(
            "Model %s, attempt %d/%d (force_length=%s)",
            model, attempt + 1, MAX_LENGTH_RETRIES, force,
        )
        try:
            payload, script, wc = _try_generate_one(model, manifest, settings, force_length=force)
        except (LLMQuotaError, LLMTransientError) as exc:
            # Per-attempt budget for retryable errors blew up — give up on this model.
            last_exc = exc
            break

        logger.info("Model %s attempt %d produced %d words", model, attempt + 1, wc)

        if wc > best_wc:
            best_payload = payload
            best_script = script
            best_wc = wc

        if wc >= settings.min_script_words:
            return best_payload, best_script, best_wc

        logger.warning(
            "Script too short on model %s: %d words < %d minimum, retrying with force_length",
            model, wc, settings.min_script_words,
        )

    if last_exc is not None and best_wc == 0:
        # Model produced nothing usable AND blew its retryable budget. Surface
        # the underlying class so the cascade caller can log it cleanly.
        raise last_exc

    return best_payload, best_script, best_wc


def generate_episode_script(manifest: dict, local_preview: bool = False, profile: str | None = None) -> EpisodeDraft:
    """Generate the daily/weekly episode script with model cascade and graceful retry.

    Cascade order (configured via env / settings):
        1. settings.llm_editor_model      (LLM_EDITOR_MODEL)
        2. settings.llm_fallback_model    (LLM_FALLBACK_MODEL)   — optional
        3. settings.llm_emergency_model   (LLM_EMERGENCY_MODEL)  — optional

    A model is dropped from cascade as soon as it exhausts its quota or
    transient-retry budget. This is what saves the daily run from the
    2026-04-16 incident: previously a single 429 on Gemini 2.5 Pro burned
    every retry slot in 5 seconds, the misleading 'Script too short: 0 words'
    error was raised, and the FR run cascaded to the same exhausted quota
    on Flash and crashed the same way.

    Raises ValueError if every cascade slot fails. The caller (the daily
    pipeline) will surface that as a workflow-level failure, which is the
    correct outcome — better to skip the day cleanly than ship a broken
    or empty episode.
    """
    settings = load_settings(local_preview=local_preview, profile=profile)

    source_count = manifest.get("source_count", 0)
    if source_count < settings.min_source_count:
        raise ValueError(
            f"Not enough relevant sources: {source_count} < {settings.min_source_count}"
        )

    models: list[str] = [settings.llm_editor_model]
    if settings.llm_fallback_model:
        models.append(settings.llm_fallback_model)
    if settings.llm_emergency_model:
        models.append(settings.llm_emergency_model)
    # De-dup while preserving order in case the caller misconfigures emergency=editor
    seen: set[str] = set()
    cascade = [m for m in models if m and not (m in seen or seen.add(m))]

    errors: list[str] = []
    best_overall_payload: dict[str, Any] | None = None
    best_overall_script: str | None = None
    best_overall_wc = 0
    best_overall_model: str | None = None

    for model in cascade:
        ep_base, ep_key = _resolve_endpoint(model, settings)
        from urllib.parse import urlparse as _u
        ep_host = _u(ep_base or '').hostname or '(none)'
        logger.info(
            "Generating script with model: %s (profile=%s, endpoint=%s, key=%s)",
            model, settings.profile_name, ep_host, 'set' if ep_key else 'unset',
        )
        try:
            payload, script, wc = _generate_for_model(model, manifest, settings)
        except LLMError as exc:
            logger.error("Model %s exhausted retry budget: %s", model, exc)
            errors.append(f"{model}: {exc}")
            continue
        except Exception as exc:
            # Any non-LLM exception (assemble_script validation error, etc.)
            # is permanent — the same prompt won't suddenly produce a valid
            # schema. Skip cascade silently for the model, log loudly.
            logger.error("Model %s failed with permanent error: %s", model, exc)
            errors.append(f"{model}: {exc}")
            continue

        if wc > best_overall_wc:
            best_overall_payload = payload
            best_overall_script = script
            best_overall_wc = wc
            best_overall_model = model

        if wc >= settings.min_script_words and payload is not None and script is not None:
            logger.info(
                "Script generated successfully: %d words, model=%s", wc, model,
            )
            return EpisodeDraft(
                episode_title=payload.get("episode_title", settings.podcast_title),
                episode_summary=payload.get("episode_summary", settings.podcast_description_short),
                opening_news_title=payload.get("opening_news_title", ""),
                script=script,
                tomorrow_concept=payload.get("tomorrow_pedagogical_concept", ""),
                highlights_label=payload.get("highlights_label", "Highlights"),
            )

        # Did produce something, but under the minimum — record and move on
        # to the next model in the cascade. We never silently ship a too-short
        # script, but we DO keep the best draft for the error report so an
        # operator can re-run manually with the partial output if they choose.
        if payload is not None:
            errors.append(
                f"{model}: short script ({wc} < {settings.min_script_words})"
            )

    if best_overall_payload is not None and best_overall_script is not None:
        logger.error(
            "All models exhausted — best draft was %d words from %s "
            "(min %d). Errors: %s",
            best_overall_wc, best_overall_model, settings.min_script_words,
            " | ".join(errors),
        )
        # Preserve the best-effort draft on disk so an operator can inspect
        # it, or — at their discretion — re-run the pipeline from the saved
        # artifact. Before this change, the draft was simply discarded when
        # the raise fired, which meant an operator had to pay the full LLM
        # cost again just to see what came out of the last attempt.
        _persist_short_draft(
            run_date=manifest.get('run_date', 'unknown'),
            payload=best_overall_payload,
            script=best_overall_script,
            word_count=best_overall_wc,
            model=best_overall_model,
            min_words=settings.min_script_words,
            errors=errors,
        )
    raise ValueError("All editorial generation attempts failed: " + " | ".join(errors))


def _persist_short_draft(
    run_date: str,
    payload: dict[str, Any],
    script: str,
    word_count: int,
    model: str | None,
    min_words: int,
    errors: list[str],
) -> None:
    """Write the best-effort draft + metadata to output/<run_date>/short_draft.*.

    Best-effort: never masks the original cascade failure. If the write itself
    raises (disk full, permission denied, weird CI path), we log and move on
    so the ValueError in the caller is what surfaces to the pipeline.
    """
    try:
        out_dir = Path('output') / run_date
        out_dir.mkdir(parents=True, exist_ok=True)
        atomic_write_text(out_dir / 'short_draft.txt', script)
        write_json(out_dir / 'short_draft.json', {
            'run_date': run_date,
            'model': model,
            'word_count': word_count,
            'min_words': min_words,
            'deficit': max(0, min_words - word_count),
            'errors': errors,
            'payload': payload,
        })
        logger.info(
            "Short draft preserved at %s (%d words; min was %d)",
            out_dir, word_count, min_words,
        )
    except Exception as exc:
        logger.warning("Could not persist short draft: %s", exc)
