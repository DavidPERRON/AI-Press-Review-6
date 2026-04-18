from __future__ import annotations

import asyncio
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from functools import lru_cache
from typing import Optional

import requests
import trafilatura
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

from ..utils import clean_text

logger = logging.getLogger(__name__)

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)

MAX_CONTENT_LENGTH = 6000
MIN_CONTENT_LENGTH = 400
MAX_EXTRACTION_WORKERS = 3

# ── Crawl4AI concurrency ────────────────────────────────────────────────────
# arun_many opens one tab per URL under a single shared browser process.
# Too many tabs at once starves the runner's 2-vCPU GitHub-hosted Ubuntu
# box and each tab times out; too few and the batch serialises. 8 is the
# sweet spot observed on the weekly (770-URL) run. Tune here if you move
# to a larger runner.
CRAWL4AI_CONCURRENCY = 8


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


@retry(
    stop=stop_after_attempt(2),
    wait=wait_exponential(multiplier=1, min=1, max=5),
    retry=retry_if_exception_type((requests.ConnectionError, requests.Timeout)),
    reraise=True,
)
def _fetch_html(url: str, timeout: int = 25) -> Optional[str]:
    response = requests.get(url, timeout=timeout, headers={"User-Agent": USER_AGENT})
    response.raise_for_status()
    # Reject excessively large pages (> 10 MB)
    content_length = response.headers.get('Content-Length')
    if content_length and int(content_length) > 10_000_000:
        logger.warning("Skipping oversized page (%s bytes): %s", content_length, url[:80])
        return None
    return response.text


def _fetch_and_extract(url: str) -> Optional[ExtractedContent]:
    try:
        html = _fetch_html(url)
    except Exception:
        return None

    if not html:
        return None

    text = _extract_with_trafilatura(url, html)
    if text:
        return ExtractedContent(url=url, text=text[:MAX_CONTENT_LENGTH], method="trafilatura")

    text = _extract_with_beautifulsoup(html)
    if text:
        return ExtractedContent(url=url, text=text[:MAX_CONTENT_LENGTH], method="beautifulsoup")

    return None


async def _crawl4ai_extract_async(url: str) -> Optional[ExtractedContent]:
    """Single-URL crawl. Only used by the per-URL `extract_article_content`
    entry point below; batch_extract goes through the shared-session path.
    """
    try:
        from crawl4ai import AsyncWebCrawler
        async with AsyncWebCrawler(verbose=False) as crawler:
            result = await crawler.arun(url=url)
            markdown = clean_text(getattr(result, "markdown", "") or "")
            if len(markdown) >= MIN_CONTENT_LENGTH:
                return ExtractedContent(url=url, text=markdown[:MAX_CONTENT_LENGTH], method="crawl4ai")
    except Exception:
        pass
    return None


def _extract_with_crawl4ai(url: str) -> Optional[ExtractedContent]:
    try:
        return asyncio.run(_crawl4ai_extract_async(url))
    except RuntimeError:
        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(_crawl4ai_extract_async(url))
        finally:
            loop.close()
    except Exception:
        return None


@lru_cache(maxsize=512)
def extract_article_content(url: str) -> Optional[ExtractedContent]:
    extracted = _extract_with_crawl4ai(url)
    if extracted:
        return extracted

    extracted = _fetch_and_extract(url)
    if extracted:
        return extracted

    logger.debug("All extraction methods failed for %s", url)
    return None


def fetch_article_text(url: str) -> str:
    result = extract_article_content(url)
    return result.text if result else ''


async def _batch_extract_crawl4ai_async(urls: list[str]) -> dict[str, Optional[ExtractedContent]]:
    """Extract content for many URLs sharing a single AsyncWebCrawler.

    Why this exists: the previous `batch_extract` spawned a ThreadPoolExecutor
    and each thread ran `asyncio.run(_crawl4ai_extract_async(url))`, which
    opened its own `async with AsyncWebCrawler(...)` block. Every entry to
    that context spins up a fresh Playwright Chromium — ~0.5s of pure init
    per URL. On the 2026-04-18 weekly run that was 770 inits (visible in
    the log as 770 `[INIT].... → Crawl4AI 0.8.6` lines), burning roughly
    6 minutes of wallclock on nothing but browser startup, on top of the
    actual fetch time.

    Sharing a single context means one browser process; `arun_many` then
    opens tabs concurrently under it. CRAWL4AI_CONCURRENCY caps concurrent
    tabs so the 2-vCPU hosted runner doesn't thrash.

    Returns a dict keyed by input URL; missing/failed entries map to None
    so the caller can fall back per-URL without re-running the whole batch.
    """
    results: dict[str, Optional[ExtractedContent]] = {u: None for u in urls}
    if not urls:
        return results

    try:
        from crawl4ai import AsyncWebCrawler
    except ImportError:
        logger.warning("crawl4ai not installed — skipping shared crawl pass")
        return results

    try:
        async with AsyncWebCrawler(verbose=False) as crawler:
            # Prefer arun_many when available (crawl4ai ≥0.8 exposes it).
            # Guarded with hasattr so a surprise API change doesn't hard-fail
            # the whole pipeline — we degrade to sequential arun in the
            # same shared context, which still avoids per-URL browser init.
            if hasattr(crawler, 'arun_many'):
                try:
                    # Older crawl4ai signatures don't accept concurrency=;
                    # try the rich signature first, then fall back.
                    batch = await crawler.arun_many(
                        urls=urls,
                        concurrency=CRAWL4AI_CONCURRENCY,
                    )
                except TypeError:
                    batch = await crawler.arun_many(urls=urls)
                for result in batch:
                    url = getattr(result, 'url', None)
                    if not url or url not in results:
                        continue
                    markdown = clean_text(getattr(result, "markdown", "") or "")
                    if len(markdown) >= MIN_CONTENT_LENGTH:
                        results[url] = ExtractedContent(
                            url=url,
                            text=markdown[:MAX_CONTENT_LENGTH],
                            method="crawl4ai",
                        )
            else:
                for url in urls:
                    try:
                        result = await crawler.arun(url=url)
                        markdown = clean_text(getattr(result, "markdown", "") or "")
                        if len(markdown) >= MIN_CONTENT_LENGTH:
                            results[url] = ExtractedContent(
                                url=url,
                                text=markdown[:MAX_CONTENT_LENGTH],
                                method="crawl4ai",
                            )
                    except Exception:
                        continue
    except Exception as exc:
        # Entire shared session blew up (e.g. Playwright install borked).
        # Leave results untouched — the requests-based pass in batch_extract
        # will still get a shot at every URL.
        logger.warning("Shared crawl4ai session failed (%s) — falling back to requests", exc)

    return results


def _run_async(coro):
    """Run an async coroutine whether or not a loop already exists.

    Matches the try/except pattern used elsewhere in this module so the
    function works both in CLI scripts and inside pipelines that happen
    to already own an event loop.
    """
    try:
        return asyncio.run(coro)
    except RuntimeError:
        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(coro)
        finally:
            loop.close()


def batch_extract(urls: list[str], max_workers: int = MAX_EXTRACTION_WORKERS) -> dict[str, Optional[ExtractedContent]]:
    """Extract content for many URLs, two passes.

    Pass 1: single shared crawl4ai session (one browser, many tabs). Fast
    for JS-heavy sites; handles most of the traffic. See
    `_batch_extract_crawl4ai_async` for the rationale on sharing the
    context instead of per-URL instances.

    Pass 2: requests-based trafilatura/BeautifulSoup fallback for URLs
    crawl4ai returned nothing for. Runs in a ThreadPoolExecutor (small
    pool — these are IO-bound but cheap).

    Returns a dict keyed by input URL; URLs that failed both passes map
    to None. Duplicates in the input are collapsed before work starts.
    """
    unique_urls = list(dict.fromkeys(urls))
    results: dict[str, Optional[ExtractedContent]] = {}

    # Pass 1 — shared crawl4ai browser
    try:
        results = _run_async(_batch_extract_crawl4ai_async(unique_urls))
    except Exception as exc:
        logger.warning("batch_extract crawl4ai pass failed (%s) — skipping to requests pass", exc)
        results = {u: None for u in unique_urls}

    # Pass 2 — requests fallback for URLs crawl4ai didn't yield content for
    remaining = [u for u in unique_urls if results.get(u) is None]
    if remaining:
        logger.info(
            "batch_extract: crawl4ai got %d/%d; requests fallback running for %d",
            len(unique_urls) - len(remaining), len(unique_urls), len(remaining),
        )
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_url = {executor.submit(_fetch_and_extract, url): url for url in remaining}
            for future in as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    results[url] = future.result()
                except Exception:
                    logger.warning("Extraction failed for %s", url)
                    results[url] = None

    return results
