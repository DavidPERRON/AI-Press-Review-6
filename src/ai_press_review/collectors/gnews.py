from __future__ import annotations

import logging
from datetime import timedelta

import requests

from ..models import SourceItem
from ..utils import clean_text, domain_from_url, normalize_url, utcnow, within_hours

logger = logging.getLogger(__name__)

GNEWS_URL = "https://gnews.io/api/v4/search"


def fetch_gnews_articles(
    api_key: str,
    query: str,
    max_results: int = 50,
    freshness_hours: int = 48,
) -> list[SourceItem]:
    """Fetch articles from GNews.io API."""
    if not api_key:
        logger.info("GNews API key not set, skipping")
        return []

    since = (utcnow() - timedelta(hours=freshness_hours)).strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        response = requests.get(
            GNEWS_URL,
            params={
                "q": query,
                "lang": "en",
                "max": min(max_results, 100),
                "from": since,
                "sortby": "publishedAt",
                "token": api_key,
            },
            timeout=30,
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        logger.warning("GNews request failed: %s", exc)
        return []

    payload = response.json()
    items: list[SourceItem] = []

    for article in payload.get("articles", []):
        url = normalize_url(article.get("url", ""))
        if not url:
            continue
        published = article.get("publishedAt")
        if not within_hours(published, freshness_hours):
            continue
        title = clean_text(article.get("title", "Untitled"))
        summary = clean_text(article.get("description", "") or article.get("content", ""))[:1200]
        items.append(
            SourceItem(
                url=url,
                title=title,
                domain=domain_from_url(url),
                published_at=published,
                summary=summary,
                queries=[query],
                sections=[],
            )
        )

    logger.info("GNews: %d articles collected", len(items))
    return items
