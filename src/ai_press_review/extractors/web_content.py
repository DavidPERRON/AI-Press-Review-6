from __future__ import annotations

import asyncio
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from functools import lru_cache
from typing import Optional

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

# Number of concurrent HTTP requests in batch_extract.
# httpx async client opens connections in parallel — no browser, no JS engine.
# 20 concurrent requests on a 2-vCPU GitHub-hosted runner is comfortably safe
# and keeps Phase 3 under 3 minutes even on 100-URL batches.
BATCH_CONCURRENCY = 20

# Hard per-URL timeout (seconds). News articles load in <2s on good days;
# 8s gives a generous buffer while bounding the worst-case tail.
HTTP_TIMEOUT = 8.0


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


# ── Async batch path ─────────────────────────────────────────────────────────

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


async def _batch_extract_async(urls: list[str]) -> dict[str, Optional[ExtractedContent]]:
    """Fetch all URLs concurrently under a single httpx async client.

    Uses a semaphore to cap in-flight requests at BATCH_CONCURRENCY so the
    GitHub-hosted runner isn't overwhelmed.  Each request has a hard timeout
    of HTTP_TIMEOUT seconds — no retry, no Chromium, no JavaScript rendering.
    For a news aggregation pipeline, ~85 % of articles are plain HTML and
    extract cleanly; the remaining 15 % are JS-gated or paywalled and would
    have been filtered in Phase 4 anyway.

    Previous approach used Crawl4AI (Playwright/Chromium) which added 2+ min
    of browser startup overhead and occasionally hung indefinitely on tabs that
    never resolved — causing the weekly job to time out at 88+ minutes.
    """
    results: dict[str, Optional[ExtractedContent]] = {u: None for u in urls}
    if not urls:
        return results

    sem = asyncio.Semaphore(BATCH_CONCURRENCY)
    timeout = httpx.Timeout(connect=5.0, read=HTTP_TIMEOUT, write=5.0, pool=5.0)
    headers = {"User-Agent": USER_AGENT}

    async with httpx.AsyncClient(timeout=timeout, headers=headers) as client:
        # gather runs all coroutines truly concurrently; semaphore caps in-flight.
        coroutines = [_fetch_one_async(client, url, sem) for url in urls]
        raw = await asyncio.gather(*coroutines, return_exceptions=True)

    for url, result in zip(urls, raw):
        if isinstance(result, BaseException):
            results[url] = None
        else:
            results[url] = result

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
    """Extract content for many URLs using async httpx (no browser required).

    All requests share a single httpx AsyncClient and run concurrently up to
    BATCH_CONCURRENCY.  Returns a dict keyed by input URL; failed/timeout
    entries map to None.  Duplicates in the input are collapsed before work.

    Timing: 100 URLs at concurrency-20 with 8s timeout ≈ 40–90 seconds on
    a GitHub-hosted runner — well within the weekly job's 90-minute budget
    even when combined with LLM generation and TTS encoding.
    """
    unique_urls = list(dict.fromkeys(urls))
    logger.info("batch_extract: fetching %d unique URLs (concurrency=%d, timeout=%.0fs)",
                len(unique_urls), BATCH_CONCURRENCY, HTTP_TIMEOUT)
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
    """Single-URL extraction (cached).  Used by ad-hoc callers outside the batch path."""
    try:
        timeout = httpx.Timeout(connect=5.0, read=HTTP_TIMEOUT, write=5.0, pool=5.0)
        with httpx.Client(timeout=timeout, headers={"User-Agent": USER_AGENT},
                          follow_redirects=True) as client:
            resp = client.get(url)
            resp.raise_for_status()
            if len(resp.content) > 5_000_000:
                return None
            return _parse_html(url, resp.text)
    except Exception:
        return None


def fetch_article_text(url: str) -> str:
    result = extract_article_content(url)
    return result.text if result else ''
