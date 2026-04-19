from __future__ import annotations

import asyncio
import logging
import os
from dataclasses import dataclass
from functools import lru_cache
from typing import Optional
from urllib.parse import quote

import httpx
import trafilatura
from bs4 import BeautifulSoup

from ..utils import clean_text

logger = logging.getLogger(__name__)

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)

MAX_CONTENT_LENGTH = 6000
MIN_CONTENT_LENGTH = 400

# Number of concurrent HTTP requests in batch_extract (Layer 1).
# httpx async client opens connections in parallel — no browser, no JS engine.
# 20 concurrent requests on a 2-vCPU GitHub-hosted runner is comfortably safe
# and keeps Phase 3 under 3 minutes even on 100-URL batches.
BATCH_CONCURRENCY = 20

# Hard per-URL timeout (seconds). News articles load in <2s on good days;
# 8s gives a generous buffer while bounding the worst-case tail.
HTTP_TIMEOUT = 8.0

# ─── Layer 2: Jina Reader fallback ──────────────────────────────────────────
# Free JS-rendering reader at https://r.jina.ai/<url>. Used for URLs that
# Layer 1 couldn't extract — typically SPAs, JS-paywalled articles, and
# Asian/Chinese sites that geo-throttle direct datacenter traffic but serve
# Jina's residential/egress fleet cleanly.
#
# - No API key required (anonymous ~20 req/min, typically enough for the
#   fallback subset after Layer 1). Setting JINA_API_KEY bumps the rate to
#   ~200 req/min (free tier of reader.jina.ai).
# - Returns plain markdown/text; no HTML parsing needed.
# - Timeout is 2.5x Layer 1 because Jina runs a headless browser server-side.
JINA_READER_BASE = "https://r.jina.ai/"
JINA_CONCURRENCY = 6          # conservative: anonymous free tier is ~20 RPM
JINA_TIMEOUT = 20.0           # Jina renders JS; give it room
JINA_MIN_CHARS = MIN_CONTENT_LENGTH

# Feature flags — can be turned off via env without code change.
#   JINA_READER_ENABLED=false  → skip Layer 2 entirely
#   JINA_API_KEY=<key>         → optional, raises rate limit
#
# NB: GitHub Actions `${{ vars.FOO }}` expands to "" when the Variable is
# unset, not to None. Treat empty string as "not configured" → default ON.
# Only explicit falsy tokens disable the fallback.
_FALSY_TOKENS = {"0", "false", "no", "off", "disabled"}

def _jina_enabled() -> bool:
    v = os.getenv("JINA_READER_ENABLED")
    if v is None or not v.strip():
        return True
    return v.strip().lower() not in _FALSY_TOKENS


def _jina_api_key() -> Optional[str]:
    v = os.getenv("JINA_API_KEY")
    return v.strip() if v and v.strip() else None


@dataclass
class ExtractedContent:
    url: str
    text: str
    method: str


def _extract_with_trafilatura(url: str, html: str) -> Optional[str]:
    try:
        text = trafilatura.extract(
            html,
            url=url,
            include_links=False,
            include_images=False,
            include_comments=False,
            include_tables=False,
            favor_recall=True,
        )
        text = clean_text(text or "")
        if len(text) >= MIN_CONTENT_LENGTH:
            return text
    except Exception:
        pass
    return None


def _extract_with_beautifulsoup(html: str) -> Optional[str]:
    try:
        soup = BeautifulSoup(html, 'lxml')
        paragraphs = [clean_text(p.get_text(' ', strip=True)) for p in soup.find_all('p')]
        text = ' '.join(part for part in paragraphs if part)
        text = clean_text(text)
        if len(text) >= MIN_CONTENT_LENGTH:
            return text
    except Exception:
        pass
    return None


def _parse_html(url: str, html: str) -> Optional[ExtractedContent]:
    """Try trafilatura then BS4 on already-fetched HTML."""
    text = _extract_with_trafilatura(url, html)
    if text:
        return ExtractedContent(url=url, text=text[:MAX_CONTENT_LENGTH], method="trafilatura")

    text = _extract_with_beautifulsoup(html)
    if text:
        return ExtractedContent(url=url, text=text[:MAX_CONTENT_LENGTH], method="beautifulsoup")

    return None


# ── Async batch path — Layer 1 (direct httpx) ────────────────────────────────

async def _fetch_one_async(
    client: httpx.AsyncClient,
    url: str,
    sem: asyncio.Semaphore,
) -> Optional[ExtractedContent]:
    """Fetch a single URL inside a shared client, bounded by a semaphore."""
    async with sem:
        try:
            resp = await client.get(url, follow_redirects=True)
            resp.raise_for_status()
            # Skip excessively large pages (> 5 MB) — unlikely to be articles.
            if len(resp.content) > 5_000_000:
                return None
            html = resp.text
        except Exception:
            return None
        return _parse_html(url, html)


# ── Layer 2: Jina Reader fallback ────────────────────────────────────────────

async def _jina_fetch_one(
    client: httpx.AsyncClient,
    url: str,
    sem: asyncio.Semaphore,
    api_key: Optional[str],
) -> Optional[ExtractedContent]:
    """Fetch article text via Jina Reader (https://r.jina.ai/<url>).

    Jina returns pre-extracted, markdown-ish plain text — no HTML parsing.
    Response structure is typically a short title/URL header followed by the
    article body, so we keep the full payload and let the caller's length
    cap + downstream scoring filter noise.
    """
    reader_url = JINA_READER_BASE + url  # Jina accepts raw or percent-encoded
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/plain",
        # Ask Jina for markdown-plain content (less boilerplate than html).
        "X-Return-Format": "markdown",
    }
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    async with sem:
        try:
            resp = await client.get(reader_url, headers=headers, follow_redirects=True)
            resp.raise_for_status()
            body = clean_text(resp.text or "")
            if len(body) >= JINA_MIN_CHARS:
                return ExtractedContent(
                    url=url,
                    text=body[:MAX_CONTENT_LENGTH],
                    method="jina-reader",
                )
        except Exception as exc:
            logger.debug("jina-reader failed for %s: %s", url, exc)
    return None


async def _batch_extract_async(urls: list[str]) -> dict[str, Optional[ExtractedContent]]:
    """Fetch all URLs via a two-layer free pipeline.

    Layer 1 — httpx + trafilatura/BS4 (fast, free, ~85 % hit rate):
        Single httpx AsyncClient, semaphore-capped concurrency, hard timeout.
        No browser, no JS engine. This is the ONLY path that runs for most
        articles.

    Layer 2 — Jina Reader (https://r.jina.ai/<url>):
        Only invoked for URLs that Layer 1 couldn't extract. Jina runs a
        headless browser server-side for us — free, no API key required,
        globally distributed (meaningfully better than our runner for
        Chinese/Japanese/Korean outlets and geo-fenced SPAs). Concurrency
        is deliberately lower (6 vs 20) to respect the anonymous rate limit.
        Can be disabled with JINA_READER_ENABLED=false; rate-lifted with
        JINA_API_KEY=<free-tier-key>.

    Previous approach used Crawl4AI (Playwright/Chromium) which added 2+ min
    of browser startup overhead and occasionally hung indefinitely on tabs
    that never resolved — causing the weekly job to time out at 88+ minutes.
    Jina replaces that capability without the infra cost.
    """
    results: dict[str, Optional[ExtractedContent]] = {u: None for u in urls}
    if not urls:
        return results

    # ── Layer 1 ──────────────────────────────────────────────────────────
    sem_l1 = asyncio.Semaphore(BATCH_CONCURRENCY)
    timeout_l1 = httpx.Timeout(connect=5.0, read=HTTP_TIMEOUT, write=5.0, pool=5.0)
    headers_l1 = {"User-Agent": USER_AGENT}

    async with httpx.AsyncClient(timeout=timeout_l1, headers=headers_l1) as client:
        coroutines = [_fetch_one_async(client, url, sem_l1) for url in urls]
        raw = await asyncio.gather(*coroutines, return_exceptions=True)

    for url, result in zip(urls, raw):
        if isinstance(result, BaseException):
            results[url] = None
        else:
            results[url] = result

    layer1_hits = sum(1 for v in results.values() if v is not None)

    # ── Layer 2: Jina Reader fallback ───────────────────────────────────
    if not _jina_enabled():
        logger.info("batch_extract: Layer 1 %d/%d; Jina fallback disabled",
                    layer1_hits, len(urls))
        return results

    failed_urls = [u for u, v in results.items() if v is None]
    if not failed_urls:
        logger.info("batch_extract: Layer 1 %d/%d (no fallback needed)",
                    layer1_hits, len(urls))
        return results

    api_key = _jina_api_key()
    logger.info(
        "batch_extract: Layer 1 %d/%d; invoking Jina fallback on %d URLs "
        "(concurrency=%d, timeout=%.0fs, api_key=%s)",
        layer1_hits, len(urls), len(failed_urls),
        JINA_CONCURRENCY, JINA_TIMEOUT, "yes" if api_key else "anonymous",
    )

    sem_l2 = asyncio.Semaphore(JINA_CONCURRENCY)
    timeout_l2 = httpx.Timeout(connect=10.0, read=JINA_TIMEOUT, write=10.0, pool=10.0)

    async with httpx.AsyncClient(timeout=timeout_l2) as client:
        coroutines = [
            _jina_fetch_one(client, url, sem_l2, api_key) for url in failed_urls
        ]
        raw = await asyncio.gather(*coroutines, return_exceptions=True)

    l2_hits = 0
    for url, result in zip(failed_urls, raw):
        if isinstance(result, BaseException):
            continue
        if result is not None:
            results[url] = result
            l2_hits += 1

    logger.info(
        "batch_extract: Layer 2 recovered %d/%d URLs (%d total hits of %d)",
        l2_hits, len(failed_urls), layer1_hits + l2_hits, len(urls),
    )
    return results


def _run_async(coro):
    try:
        return asyncio.run(coro)
    except RuntimeError:
        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(coro)
        finally:
            loop.close()


def batch_extract(urls: list[str]) -> dict[str, Optional[ExtractedContent]]:
    """Extract content for many URLs using the two-layer free pipeline.

    Layer 1 (httpx + trafilatura/BS4) runs first; Jina Reader picks up the
    URLs that Layer 1 couldn't crack. Returns a dict keyed by input URL;
    entries that neither layer could recover map to None. Duplicates in the
    input are collapsed before work.

    Typical timing on 100 URLs:
      - Layer 1: 40–90 s (80–85 % hit)
      - Layer 2: 30–80 s on the ~15–20 remaining URLs
      - Total: well under 3 min, fits comfortably in the daily 25-min budget.
    """
    unique_urls = list(dict.fromkeys(urls))
    logger.info(
        "batch_extract: fetching %d unique URLs (L1 concurrency=%d, timeout=%.0fs; "
        "L2 jina enabled=%s)",
        len(unique_urls), BATCH_CONCURRENCY, HTTP_TIMEOUT, _jina_enabled(),
    )
    try:
        results = _run_async(_batch_extract_async(unique_urls))
    except Exception as exc:
        logger.warning("batch_extract async pass failed (%s) — all URLs yield None", exc)
        results = {u: None for u in unique_urls}

    success = sum(1 for v in results.values() if v is not None)
    logger.info("batch_extract: %d/%d URLs yielded content", success, len(unique_urls))
    return results


@lru_cache(maxsize=512)
def extract_article_content(url: str) -> Optional[ExtractedContent]:
    """Single-URL extraction (cached). Tries Layer 1 then Jina Reader fallback.

    Used by ad-hoc callers outside the batch path. Respects the same
    JINA_READER_ENABLED / JINA_API_KEY toggles as batch_extract.
    """
    # Layer 1
    try:
        timeout = httpx.Timeout(connect=5.0, read=HTTP_TIMEOUT, write=5.0, pool=5.0)
        with httpx.Client(timeout=timeout, headers={"User-Agent": USER_AGENT},
                          follow_redirects=True) as client:
            resp = client.get(url)
            resp.raise_for_status()
            if len(resp.content) > 5_000_000:
                return None
            parsed = _parse_html(url, resp.text)
            if parsed is not None:
                return parsed
    except Exception:
        pass

    # Layer 2 — Jina Reader
    if not _jina_enabled():
        return None
    api_key = _jina_api_key()
    try:
        timeout = httpx.Timeout(connect=10.0, read=JINA_TIMEOUT, write=10.0, pool=10.0)
        headers = {
            "User-Agent": USER_AGENT,
            "Accept": "text/plain",
            "X-Return-Format": "markdown",
        }
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"
        with httpx.Client(timeout=timeout, follow_redirects=True) as client:
            resp = client.get(JINA_READER_BASE + url, headers=headers)
            resp.raise_for_status()
            body = clean_text(resp.text or "")
            if len(body) >= JINA_MIN_CHARS:
                return ExtractedContent(
                    url=url, text=body[:MAX_CONTENT_LENGTH], method="jina-reader",
                )
    except Exception:
        return None
    return None


def fetch_article_text(url: str) -> str:
    result = extract_article_content(url)
    return result.text if result else ''
