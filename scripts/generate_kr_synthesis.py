#!/usr/bin/env python3
"""Generate AX (AI Transformation) synthesis briefing for a Korean research firm.

Filters the past N days of the AI Press Review corpus on four interview themes
(strategic objectives, investment decisions, organizational structures, KPIs &
management processes), then calls the editorial LLM with a dedicated long-form
prompt that produces a dense, structured markdown briefing similar in spirit
to the weekend press review but expanded for a 1-hour expert interview.

Usage:
    python scripts/generate_kr_synthesis.py --lang en
    python scripts/generate_kr_synthesis.py --lang ko --days 60
    python scripts/generate_kr_synthesis.py --lang both --mode synthesis
    python scripts/generate_kr_synthesis.py --mode filter-only

Outputs land in `output/kr-synthesis/<run-date>-<lang>.md` plus a
`<run-date>-manifest.json` snapshot of the filtered corpus.

Environment: reuses the existing LLM_* env vars (LLM_BASE_URL, LLM_API_KEY,
LLM_EDITOR_MODEL, ...) so the script honours the same cascade configuration
as the daily pipeline. No additional secret is required.
"""
from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

# Ensure local src/ is importable when run as a plain script
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import requests  # noqa: E402

from ai_press_review.editorial.generator import (  # noqa: E402
    _create_completion_data,
    _extract_message_content,
    _resolve_endpoint,
)
from ai_press_review.settings import load_settings  # noqa: E402

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("kr_synthesis")


# ─────────────────────────────────────────────────────────────────────────────
# Keyword universe — built per interview theme
# ─────────────────────────────────────────────────────────────────────────────

THEME_KEYWORDS: dict[str, list[str]] = {
    # Q1 — Strategic objectives & long-term AX direction
    "strategy": [
        r"\bAI strategy\b",
        r"\bAI roadmap\b",
        r"\bAI transformation\b",
        r"\bAX\b",
        r"\bAI-first\b",
        r"\bAI vision\b",
        r"\bAI agenda\b",
        r"\bdigital transformation\b",
        r"\benterprise AI\b",
        r"\bagentic\b",
        r"\bAI strategy\b",
        r"\bgenerative AI strategy\b",
        r"\bAI thesis\b",
        r"\bAI platform\b",
        r"\bAI-native\b",
        r"\bAI moat\b",
    ],
    # Q2 — Investment magnitude, decision authority, prioritization
    "investment": [
        r"\bcapex\b",
        r"\bAI capex\b",
        r"\binvest(?:ment|ed|ing)\b.{0,40}\bAI\b",
        r"\bAI\b.{0,40}\binvest(?:ment|ed|ing)\b",
        r"\$\s*\d+(?:\.\d+)?\s*billion",
        r"\$\s*\d+(?:\.\d+)?\s*trillion",
        r"\d+\s*billion\s*(?:dollar|won|yen|euro)",
        r"\bfunding round\b",
        r"\bSeries\s*[A-Z]\b",
        r"\bvaluation\b",
        r"\bdata center\b.{0,40}\b(invest|build|spend|commit)",
        r"\bspending\b.{0,40}\bAI\b",
        r"\bAI\b.{0,40}\bspending\b",
        r"\bcommitted\b.{0,40}\b(billion|trillion)",
        r"\bcapital allocation\b",
        r"\bAI infrastructure\b",
        r"\bStargate\b",
        r"\bsovereign AI\b",
    ],
    # Q3 — Organizational structures, CAIO, AI orgs
    "organization": [
        r"\bChief AI Officer\b",
        r"\bCAIO\b",
        r"\bChief Artificial Intelligence Officer\b",
        r"\bhead of AI\b",
        r"\bAI center of excellence\b",
        r"\bAI CoE\b",
        r"\bAI factory\b",
        r"\bAI hub\b",
        r"\bAI office\b",
        r"\bAI lab\b",
        r"\bAI council\b",
        r"\bAI steering committee\b",
        r"\bappointed\b.{0,40}\bAI\b",
        r"\bAI organization\b",
        r"\bAI team\b",
        r"\bAI division\b",
        r"\bAI unit\b",
        r"\bAI research lab\b",
        r"\bcross-functional\b.{0,40}\bAI\b",
        r"\bAI governance\b",
        r"\bgroup AI\b",
        r"\bcenter of AI\b",
    ],
    # Q3 — KPIs, ROI, management processes
    "kpi": [
        r"\bAI ROI\b",
        r"\breturn on (?:AI|investment)\b",
        r"\bAI adoption\b",
        r"\bAI productivity\b",
        r"\bAI metrics?\b",
        r"\bKPIs?\b",
        r"\bdeveloper productivity\b",
        r"\bhours saved\b",
        r"\btime saved\b",
        r"\bcost savings?\b",
        r"\bcontact deflection\b",
        r"\bdeflection rate\b",
        r"\bhallucination\b",
        r"\binference cost\b",
        r"\bAI scorecard\b",
        r"\bAI dashboard\b",
        r"\bbeyond pilots?\b",
        r"\bmoving past pilots?\b",
        r"\bpilot to production\b",
        r"\bAI maturity\b",
    ],
    # Korean companies & Asia context (boosts geographic relevance)
    "korea": [
        r"\bSamsung\b",
        r"\bSK Hynix\b",
        r"\bSK Group\b",
        r"\bSK Telecom\b",
        r"\bLG\b",
        r"\bLG AI\b",
        r"\bLG CNS\b",
        r"\bNaver\b",
        r"\bKakao\b",
        r"\bHyundai\b",
        r"\bKia\b",
        r"\bPosco\b",
        r"\bKT Corp\b",
        r"\bKorea\b",
        r"\bKorean\b",
        r"\bSeoul\b",
        r"\bHBM\b",
        r"\bHigh Bandwidth Memory\b",
        r"\bchaebol\b",
        r"\bSamsung SDS\b",
        r"\bSamsung SDI\b",
        r"\bKB Financial\b",
        r"\bKookmin Bank\b",
        r"\bShinhan\b",
        r"\bWoori\b",
        r"\bHana Bank\b",
    ],
    # Banking, financial services, fintech — first-class theme because
    # the client is consulting a senior expert with a JPMorgan background.
    "finance": [
        r"\bJPMorgan\b",
        r"\bJ\.?P\.? Morgan\b",
        r"\bJPMC\b",
        r"\bJamie Dimon\b",
        r"\bMary Erdoes\b",
        r"\bLori Beer\b",
        r"\bMarco Pistoia\b",
        r"\bDerek Waldron\b",
        r"\bGoldman Sachs\b",
        r"\bMorgan Stanley\b",
        r"\bBank of America\b",
        r"\bBofA\b",
        r"\bCitigroup\b",
        r"\bCitibank\b",
        r"\bWells Fargo\b",
        r"\bHSBC\b",
        r"\bBarclays\b",
        r"\bBNP Paribas\b",
        r"\bDeutsche Bank\b",
        r"\bUBS\b",
        r"\bCredit Suisse\b",
        r"\bSantander\b",
        r"\bSocGen\b",
        r"\bMUFG\b",
        r"\bSumitomo\b",
        r"\bMizuho\b",
        r"\bICBC\b",
        r"\bDBS\b",
        r"\bWall Street\b",
        r"\bbanking\b.{0,40}\bAI\b",
        r"\bAI\b.{0,40}\bbank(?:ing|s)\b",
        r"\bfinancial services\b.{0,40}\bAI\b",
        r"\bAI\b.{0,40}\bfinancial services\b",
        r"\bfintech\b",
        r"\bcapital markets\b.{0,40}\bAI\b",
        r"\binvestment bank\b",
        r"\basset management\b.{0,40}\bAI\b",
        r"\bwealth management\b.{0,40}\bAI\b",
        r"\binsurance\b.{0,40}\bAI\b",
        r"\bAllianz\b",
        r"\bAXA\b",
        r"\bAIG\b",
        r"\bBlackRock\b",
        r"\bFidelity\b",
        r"\bBridgewater\b",
        r"\bTwo Sigma\b",
        r"\bRenaissance Technologies\b",
        r"\bPayPal\b",
        r"\bStripe\b",
        r"\bAdyen\b",
        r"\bSquare\b",
        r"\bBlock Inc\b",
        r"\bIntuit\b",
        r"\bAmerican Express\b",
        r"\bAmex\b",
        r"\bMastercard\b",
        r"\bVisa\b",
        r"\bcompliance\b.{0,40}\bAI\b",
        r"\bAI\b.{0,40}\b(?:KYC|AML|fraud)\b",
        r"\b(?:KYC|AML|fraud)\b.{0,40}\bAI\b",
        r"\balgorithmic trading\b",
        r"\bquant\b.{0,40}\bAI\b",
        r"\bAI\b.{0,40}\bquant\b",
    ],
    # Anchor companies (Big Tech / labs) — keep prominent
    "anchors": [
        r"\bMicrosoft\b",
        r"\bGoogle\b",
        r"\bAlphabet\b",
        r"\bMeta\b",
        r"\bAmazon\b",
        r"\bApple\b",
        r"\bNvidia\b",
        r"\bAMD\b",
        r"\bOpenAI\b",
        r"\bAnthropic\b",
        r"\bxAI\b",
        r"\bMistral\b",
        r"\bCohere\b",
        r"\bDeepMind\b",
        r"\bSoftBank\b",
        r"\bAlibaba\b",
        r"\bTencent\b",
        r"\bBaidu\b",
        r"\bDeepSeek\b",
        r"\bByteDance\b",
        r"\bSiemens\b",
        r"\bSAP\b",
        r"\bSalesforce\b",
        r"\bIBM\b",
        r"\bOracle\b",
    ],
}

# Per-theme weight when scoring articles
THEME_WEIGHTS: dict[str, float] = {
    "strategy": 3.0,
    "investment": 3.0,
    "organization": 3.5,
    "kpi": 3.5,
    "korea": 2.0,
    "finance": 3.5,
    "anchors": 0.8,
}

COMPILED_PATTERNS: dict[str, list[re.Pattern[str]]] = {
    theme: [re.compile(p, re.IGNORECASE) for p in patterns]
    for theme, patterns in THEME_KEYWORDS.items()
}


# ─────────────────────────────────────────────────────────────────────────────
# Source loading and filtering
# ─────────────────────────────────────────────────────────────────────────────


def _parse_published(raw: str | None) -> datetime | None:
    """Best-effort parse of the various published_at strings the collectors emit."""
    if not raw:
        return None
    raw = raw.strip()
    # RFC 822 (RSS): "Mon, 11 May 2026 14:15:14 +0000"
    for fmt in (
        "%a, %d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S GMT",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d",
    ):
        try:
            dt = datetime.strptime(raw, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except ValueError:
            continue
    # Fall back: try fromisoformat
    try:
        dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except ValueError:
        return None


def _load_corpus(window_days: int, today: date) -> tuple[list[dict[str, Any]], list[Path]]:
    """Load every source JSON in data/sources/en/ whose run-date is within `window_days`.

    The corpus already de-duplicates within a single day; we de-dup across
    days by URL so a story that recurs in three daily manifests is counted once.
    """
    sources_dir = ROOT / "data" / "sources" / "en"
    if not sources_dir.exists():
        raise FileNotFoundError(f"Source corpus not found: {sources_dir}")

    cutoff = today - timedelta(days=window_days)
    loaded_files: list[Path] = []
    seen_urls: set[str] = set()
    seen_titles: set[str] = set()
    merged: list[dict[str, Any]] = []

    for path in sorted(sources_dir.glob("2026-*.json")):
        try:
            run_date = datetime.strptime(path.stem, "%Y-%m-%d").date()
        except ValueError:
            continue
        if run_date < cutoff or run_date > today:
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            logger.warning("Skipping unreadable manifest %s: %s", path.name, exc)
            continue
        loaded_files.append(path)
        for src in data.get("sources", []):
            url = (src.get("url") or "").strip()
            title = (src.get("title") or "").strip().lower()
            if url and url in seen_urls:
                continue
            if title and title in seen_titles:
                continue
            if url:
                seen_urls.add(url)
            if title:
                seen_titles.add(title)
            merged.append(src)

    logger.info(
        "Loaded %d unique sources from %d daily manifests (window=%d days, cutoff=%s)",
        len(merged), len(loaded_files), window_days, cutoff.isoformat(),
    )
    return merged, loaded_files


def _score_source(src: dict[str, Any]) -> tuple[float, dict[str, int]]:
    """Return (score, hits-per-theme) for one source.

    Score is the sum of THEME_WEIGHTS[theme] × matches-in-theme, capped at 4
    matches per theme so a single article saturated on Korea or Anchors does
    not crowd out a more balanced one. Also factors in the original
    relevance_score from the collector (light multiplier).
    """
    text_parts = [
        src.get("title") or "",
        src.get("summary") or "",
        src.get("content_text") or "",
    ]
    blob = " \n ".join(text_parts)
    if len(blob.strip()) < 80:
        return 0.0, {}

    hits: dict[str, int] = defaultdict(int)
    score = 0.0
    for theme, patterns in COMPILED_PATTERNS.items():
        theme_hits = 0
        for pat in patterns:
            if pat.search(blob):
                theme_hits += 1
                if theme_hits >= 4:
                    break
        if theme_hits:
            hits[theme] = theme_hits
            score += theme_hits * THEME_WEIGHTS[theme]

    # Require at least one of the core interview themes; Korea/anchors alone
    # is not enough. Finance counts as a core theme because the consulting
    # firm explicitly probes JPMorgan-related experience.
    core_themes = {"strategy", "investment", "organization", "kpi", "finance"}
    if not any(t in hits for t in core_themes):
        return 0.0, {}

    base = float(src.get("relevance_score") or 0.0)
    score += min(base, 25.0) * 0.1
    return score, dict(hits)


def _filter_and_rank(
    sources: list[dict[str, Any]],
    max_keep: int,
) -> list[dict[str, Any]]:
    """Score every source, keep the top-K, balance themes."""
    scored: list[tuple[float, dict[str, int], dict[str, Any]]] = []
    for src in sources:
        score, hits = _score_source(src)
        if score <= 0:
            continue
        enriched = dict(src)
        enriched["_themes"] = hits
        enriched["_theme_score"] = round(score, 2)
        scored.append((score, hits, enriched))

    scored.sort(key=lambda t: t[0], reverse=True)

    # Theme balancing — make sure no single theme cluster dominates.
    # Cap each core theme at 40% of the kept corpus.
    cap_per_theme = max(8, int(max_keep * 0.5))
    counts: dict[str, int] = defaultdict(int)
    kept: list[dict[str, Any]] = []
    for _score, hits, enriched in scored:
        # Primary theme = most hits, tie-broken by highest theme weight so a
        # 2-hits-on-strategy + 2-hits-on-anchors article counts as strategy
        # (the heavier interview theme) rather than anchors.
        primary = max(hits.items(), key=lambda kv: (kv[1], THEME_WEIGHTS[kv[0]]))[0]
        if counts[primary] >= cap_per_theme and len(kept) >= max_keep * 0.6:
            continue
        kept.append(enriched)
        counts[primary] += 1
        if len(kept) >= max_keep:
            break

    logger.info(
        "Filter kept %d sources of %d candidates (theme distribution: %s)",
        len(kept), len(scored),
        ", ".join(f"{t}={c}" for t, c in sorted(counts.items())),
    )
    return kept


# ─────────────────────────────────────────────────────────────────────────────
# Manifest packaging for the LLM
# ─────────────────────────────────────────────────────────────────────────────


def _compact_for_prompt(src: dict[str, Any], extract_chars: int = 2400) -> dict[str, Any]:
    text = src.get("content_text") or src.get("summary") or ""
    # Strip HTML tags coarsely — the manifest stores HTML summaries from RSS.
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return {
        "title": src.get("title"),
        "domain": src.get("domain"),
        "url": src.get("url"),
        "published_at": src.get("published_at"),
        "themes": list((src.get("_themes") or {}).keys()),
        "theme_score": src.get("_theme_score"),
        "relevance_score": src.get("relevance_score"),
        "content_text": text[:extract_chars],
    }


def _build_user_payload(
    kept: list[dict[str, Any]],
    today: date,
    window_days: int,
    lang: str,
) -> str:
    """Build the JSON user message the LLM will see."""
    payload = {
        "briefing_date": today.isoformat(),
        "language": lang,
        "window_days": window_days,
        "source_count": len(kept),
        "instructions": (
            "Use the source_manifest below as the ONLY factual ground truth. "
            "Follow the system-prompt section structure exactly. Return markdown, not JSON."
        ),
        "source_manifest": [_compact_for_prompt(s) for s in kept],
    }
    return json.dumps(payload, ensure_ascii=False)


# ─────────────────────────────────────────────────────────────────────────────
# LLM call (reuses existing endpoint helpers)
# ─────────────────────────────────────────────────────────────────────────────


def _call_llm(prompt_path: Path, user_payload: str, max_tokens: int) -> str:
    """Call the LLM and return the markdown synthesis.

    Routing:
      • Anthropic-direct endpoints (api.anthropic.com) → native /v1/messages
        API. The OpenAI-compat /chat/completions adapter at api.anthropic.com
        rejects response_format + temperature combinations for Opus 4.x, so
        we bypass it and speak the Messages protocol directly. Markdown
        output means we don't need response_format anyway.
      • Anything else (OpenRouter, DeepInfra, ...) → OpenAI-compat path via
        _create_completion_data, which already handles the response_format
        cascade for those providers.
    """
    settings = load_settings()
    if not settings.llm_editor_model:
        raise RuntimeError(
            "LLM_EDITOR_MODEL is not configured — set LLM_BASE_URL, LLM_API_KEY, "
            "and LLM_EDITOR_MODEL in your .env to call the synthesis LLM."
        )

    base_url, api_key = _resolve_endpoint(settings.llm_editor_model, settings)
    if not api_key:
        raise RuntimeError(
            f"No API key resolved for endpoint {base_url!r}. "
            "Set LLM_API_KEY (or per-tier LLM_*_API_KEY) before running."
        )

    system_prompt = prompt_path.read_text(encoding="utf-8")
    logger.info(
        "Calling LLM model=%s base=%s tokens<=%d user_payload=%d chars",
        settings.llm_editor_model, base_url, max_tokens, len(user_payload),
    )

    if "anthropic.com" in (base_url or ""):
        return _call_anthropic_messages(
            base_url=base_url,
            api_key=api_key,
            model=settings.llm_editor_model,
            system_prompt=system_prompt,
            user_payload=user_payload,
            max_tokens=max_tokens,
        )

    # OpenAI-compatible endpoint (OpenRouter, DeepInfra, etc.)
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_payload},
    ]
    data = _create_completion_data(
        settings=settings,
        model=settings.llm_editor_model,
        messages=messages,
        temperature=0.25,
        max_tokens=max_tokens,
    )
    content = _extract_message_content(data)
    if not content.strip():
        raise RuntimeError("LLM returned empty content")
    return content.strip()


def _call_anthropic_messages(
    base_url: str,
    api_key: str,
    model: str,
    system_prompt: str,
    user_payload: str,
    max_tokens: int,
    max_continuations: int = 4,
) -> str:
    """POST to Anthropic's native /v1/messages with auto-continuation.

    No response_format, no temperature — Opus 4.7 rejects both. The model
    returns markdown directly per the system-prompt contract.

    If the first response stops on `max_tokens` (truncation), we re-issue the
    request with the partial output as an assistant turn and ask the model
    to continue exactly where it left off. We accumulate up to
    `max_continuations` additional rounds before giving up. This guarantees
    the long-form synthesis is not silently cut off at the Opus 32K output
    ceiling.
    """
    url = base_url.rstrip("/") + "/messages"
    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }

    messages: list[dict[str, str]] = [{"role": "user", "content": user_payload}]
    accumulated = ""
    total_in = 0
    total_out = 0

    for attempt in range(max_continuations + 1):
        payload = {
            "model": model,
            "max_tokens": max_tokens,
            "system": system_prompt,
            "messages": messages,
        }
        # Retry transient API-side errors (overloaded 529, gateway 502/503/504,
        # quota 429). Anthropic 529s are common during peak hours and clear
        # within a minute; without this loop the entire run is wasted.
        import time as _time
        data = None
        for retry in range(6):
            response = requests.post(url, headers=headers, json=payload, timeout=900)
            if response.status_code in (429, 502, 503, 504, 529):
                wait = min(60, 5 * (2 ** retry))
                logger.warning(
                    "Anthropic HTTP %s (transient, attempt %d/6) — sleeping %ds",
                    response.status_code, retry + 1, wait,
                )
                _time.sleep(wait)
                continue
            if response.status_code >= 400:
                snippet = response.text[:500]
                raise RuntimeError(
                    f"Anthropic /v1/messages HTTP {response.status_code}: {snippet}"
                )
            data = response.json()
            break
        if data is None:
            raise RuntimeError(
                "Anthropic /v1/messages: 6 transient retries exhausted "
                f"(last status {response.status_code})"
            )
        blocks = data.get("content") or []
        parts = [b.get("text", "") for b in blocks if isinstance(b, dict) and b.get("type") == "text"]
        chunk = "\n".join(parts)
        if not chunk.strip() and attempt == 0:
            raise RuntimeError(f"Anthropic returned no text blocks: {data}")

        accumulated += chunk
        usage = data.get("usage") or {}
        in_t = int(usage.get("input_tokens", 0) or 0)
        out_t = int(usage.get("output_tokens", 0) or 0)
        total_in += in_t
        total_out += out_t
        stop_reason = data.get("stop_reason", "?")
        logger.info(
            "Anthropic call %d OK — input=%s output=%s stop=%s (cumulative output=%d)",
            attempt + 1, in_t, out_t, stop_reason, total_out,
        )

        if stop_reason != "max_tokens":
            break
        if attempt >= max_continuations:
            logger.warning(
                "Hit max_continuations=%d with stop=max_tokens; returning accumulated output (%d tokens). "
                "Consider raising --max-tokens or splitting the synthesis manually.",
                max_continuations, total_out,
            )
            break

        # Re-issue with the partial as an assistant turn, plus a continue directive.
        messages = [
            {"role": "user", "content": user_payload},
            {"role": "assistant", "content": accumulated},
            {
                "role": "user",
                "content": (
                    "Continue the markdown synthesis exactly from where you stopped. "
                    "Do not repeat any prior text. Do not summarize what came before. "
                    "Do not write a header that already exists. Pick up mid-sentence if "
                    "that is where you left off, and continue through Section 9 (Source "
                    "Inventory). Maintain the same source-discipline rules and density rule."
                ),
            },
        ]

    logger.info(
        "Anthropic synthesis complete — total_input=%d total_output=%d (across %d calls)",
        total_in, total_out, attempt + 1,
    )
    return accumulated.strip()


# ─────────────────────────────────────────────────────────────────────────────
# Output writers
# ─────────────────────────────────────────────────────────────────────────────


def _write_filter_report(
    out_dir: Path,
    today: date,
    window_days: int,
    kept: list[dict[str, Any]],
    loaded_files: list[Path],
) -> Path:
    """Dump the filtered manifest as JSON + a human-readable markdown index."""
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = out_dir / f"{today.isoformat()}-manifest.json"
    manifest_path.write_text(
        json.dumps(
            {
                "briefing_date": today.isoformat(),
                "window_days": window_days,
                "source_count": len(kept),
                "files_scanned": [p.name for p in loaded_files],
                "sources": kept,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    index_path = out_dir / f"{today.isoformat()}-index.md"
    by_theme: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for src in kept:
        for theme in (src.get("_themes") or {}).keys():
            by_theme[theme].append(src)

    lines: list[str] = []
    lines.append(f"# AX synthesis — filtered corpus index")
    lines.append("")
    lines.append(f"- Briefing date: {today.isoformat()}")
    lines.append(f"- Window: last {window_days} days")
    lines.append(f"- Unique sources kept: {len(kept)}")
    lines.append(f"- Daily manifests scanned: {len(loaded_files)}")
    lines.append("")
    for theme in ("strategy", "investment", "organization", "kpi", "finance", "korea", "anchors"):
        items = by_theme.get(theme, [])
        if not items:
            continue
        lines.append(f"## Theme: {theme} ({len(items)} sources)")
        for src in sorted(items, key=lambda s: s.get("_theme_score", 0), reverse=True)[:40]:
            lines.append(
                f"- [{src.get('domain')}] {src.get('title')} "
                f"— {src.get('published_at')} — score {src.get('_theme_score')}"
            )
            lines.append(f"  - {src.get('url')}")
        lines.append("")
    index_path.write_text("\n".join(lines), encoding="utf-8")

    logger.info("Wrote filter report: %s and %s", manifest_path.name, index_path.name)
    return manifest_path


def _write_synthesis(out_dir: Path, today: date, lang: str, markdown: str) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{today.isoformat()}-{lang}.md"
    out_path.write_text(markdown, encoding="utf-8")
    logger.info("Wrote synthesis: %s (%d chars, ~%d words)",
                out_path.name, len(markdown), len(markdown.split()))
    return out_path


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate AX (AI Transformation) synthesis for a Korean research firm interview.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--lang",
        choices=("en", "ko", "both"),
        default="en",
        help="Output language for the synthesis (default: en).",
    )
    parser.add_argument(
        "--days",
        type=int,
        default=60,
        help="Look-back window in days (default: 60).",
    )
    parser.add_argument(
        "--max-sources",
        type=int,
        default=200,
        help="Max sources to keep after filtering (default: 200). Set to a "
             "very large value (e.g. 9999) for an effectively unlimited corpus.",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=16000,
        help="Max output tokens for the LLM call (default: 16000).",
    )
    parser.add_argument(
        "--mode",
        choices=("filter-only", "synthesis"),
        default="synthesis",
        help="`filter-only` skips the LLM and writes only the filtered corpus.",
    )
    parser.add_argument(
        "--today",
        default=None,
        help="Override the run date (YYYY-MM-DD). Defaults to today.",
    )
    parser.add_argument(
        "--out-dir",
        default=str(ROOT / "output" / "kr-synthesis"),
        help="Output directory (default: output/kr-synthesis/).",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()

    today = (
        datetime.strptime(args.today, "%Y-%m-%d").date()
        if args.today
        else date.today()
    )
    out_dir = Path(args.out_dir)

    sources, loaded_files = _load_corpus(window_days=args.days, today=today)
    if not sources:
        raise SystemExit(
            f"No sources found in window of {args.days} days ending {today.isoformat()}. "
            f"Check data/sources/en/ for daily manifests."
        )

    kept = _filter_and_rank(sources, max_keep=args.max_sources)
    if not kept:
        raise SystemExit(
            "Filter kept zero sources — the AX/Korea/investment themes did not match. "
            "Try increasing --days or relaxing THEME_KEYWORDS."
        )

    _write_filter_report(out_dir, today, args.days, kept, loaded_files)

    if args.mode == "filter-only":
        logger.info("filter-only mode — skipping LLM call. Done.")
        return

    en_payload = _build_user_payload(kept, today, args.days, "en")

    # EN is generated from the manifest. KR is a TRANSLATION of the EN output —
    # the KR prompt is a translator role, not a generator. This guarantees the
    # two languages share identical content and that the KR memo respects
    # Korean business writing conventions instead of being a parallel
    # generation that drifts from the EN.
    languages = ("en", "ko") if args.lang == "both" else (args.lang,)
    en_markdown: str | None = None

    if "en" in languages:
        en_prompt = ROOT / "config" / "prompt_kr_ax_synthesis_en.txt"
        if not en_prompt.exists():
            raise FileNotFoundError(f"Prompt not found: {en_prompt}")
        en_markdown = _call_llm(en_prompt, en_payload, max_tokens=args.max_tokens)
        _write_synthesis(out_dir, today, "en", en_markdown)

    if "ko" in languages:
        # Load EN from the just-generated output, or the most recent prior
        # EN memo on disk if --lang ko was invoked standalone.
        if en_markdown is None:
            en_path = out_dir / f"{today.isoformat()}-en.md"
            if not en_path.exists():
                raise FileNotFoundError(
                    f"--lang ko requires an EN memo to translate. "
                    f"Expected {en_path} not found — run --lang en first."
                )
            en_markdown = en_path.read_text(encoding="utf-8")
            logger.info("Loaded EN memo for translation: %s (%d chars)",
                        en_path.name, len(en_markdown))

        ko_prompt = ROOT / "config" / "prompt_kr_ax_synthesis_kr.txt"
        if not ko_prompt.exists():
            raise FileNotFoundError(f"Prompt not found: {ko_prompt}")
        ko_markdown = _call_llm(ko_prompt, en_markdown, max_tokens=args.max_tokens)
        _write_synthesis(out_dir, today, "ko", ko_markdown)

    logger.info("Done. Output in %s", out_dir)


if __name__ == "__main__":
    main()
