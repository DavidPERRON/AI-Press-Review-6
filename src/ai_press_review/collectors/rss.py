from __future__ import annotations

import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Iterable

import feedparser
import requests

from ..models import SourceItem
from ..utils import clean_text, domain_from_url, normalize_url, within_hours

logger = logging.getLogger(__name__)

MAX_FEED_WORKERS = 6
MAX_RESOLVE_WORKERS = 12

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)


def _parse_single_feed(feed_url: str, freshness_hours: int) -> list[SourceItem]:
    items: list[SourceItem] = []
    try:
        parsed = feedparser.parse(feed_url)
    except Exception:
        logger.warning("Failed to parse RSS feed: %s", feed_url)
        return items

    for entry in parsed.entries:
        link = normalize_url(entry.get('link', ''))
        if not link:
            continue
        published = entry.get('published') or entry.get('updated')
        if not within_hours(published, freshness_hours):
            continue

        # Use source metadata for domain attribution (Google News)
        source_url = None
        if hasattr(entry, 'source'):
            source_url = getattr(entry.source, 'href', None) or entry.source.get('url')

        domain = domain_from_url(source_url) if source_url else domain_from_url(link)
        summary = clean_text(entry.get('summary', ''))[:1200]
        # Author: prefer entry.author_detail.name, fall back to entry.author
        author_raw = ''
        if hasattr(entry, 'author_detail') and entry.author_detail:
            author_raw = entry.author_detail.get('name', '') or ''
        if not author_raw:
            author_raw = entry.get('author', '') or ''
        author = clean_text(author_raw)[:120] if author_raw else None

        items.append(
            SourceItem(
                url=link,
                title=clean_text(entry.get('title', 'Untitled')),
                domain=domain,
                published_at=published,
                author=author,
                summary=summary,
                queries=[feed_url],
                sections=[],
            )
        )
    return items


def _resolve_redirect(url: str) -> str:
    """Follow Google News redirect to get the actual article URL."""
    if 'news.google.com' not in url:
        return url
    try:
        resp = requests.head(
            url, allow_redirects=True, timeout=8,
            headers={"User-Agent": USER_AGENT},
        )
        if 'news.google.com' not in resp.url:
            return resp.url
        # HEAD didn't resolve, try GET with stream
        resp = requests.get(
            url, allow_redirects=True, timeout=8,
            headers={"User-Agent": USER_AGENT}, stream=True,
        )
        final = resp.url
        resp.close()
        return final
    except Exception:
        return url


def _resolve_google_news_urls(items: list[SourceItem]) -> list[SourceItem]:
    """Resolve Google News redirect URLs to actual article URLs in parallel."""
    google_items = [i for i in items if 'news.google.com' in i.url]
    if not google_items:
        return items

    logger.info("Resolving %d Google News redirect URLs...", len(google_items))
    resolved = 0

    with ThreadPoolExecutor(max_workers=MAX_RESOLVE_WORKERS) as executor:
        futures = {executor.submit(_resolve_redirect, item.url): item for item in google_items}
        for future in as_completed(futures):
            item = futures[future]
            try:
                real_url = future.result()
                if real_url != item.url and 'news.google.com' not in real_url:
                    item.url = normalize_url(real_url)
                    item.domain = domain_from_url(real_url)
                    resolved += 1
            except Exception:
                pass

    logger.info("Resolved %d/%d Google News URLs to actual sources", resolved, len(google_items))
    return items


def fetch_rss_entries(feed_urls: Iterable[str], freshness_hours: int) -> list[SourceItem]:
    feed_list = list(feed_urls)
    all_items: list[SourceItem] = []

    with ThreadPoolExecutor(max_workers=MAX_FEED_WORKERS) as executor:
        futures = {
            executor.submit(_parse_single_feed, url, freshness_hours): url
            for url in feed_list
        }
        for future in as_completed(futures):
            feed_url = futures[future]
            try:
                items = future.result()
                all_items.extend(items)
                logger.info("RSS feed %s: %d entries", feed_url[:80], len(items))
            except Exception:
                logger.warning("RSS feed failed: %s", feed_url)

    # Resolve Google News redirects to actual article URLs
    all_items = _resolve_google_news_urls(all_items)

    return all_items
