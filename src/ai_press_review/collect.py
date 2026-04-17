from __future__ import annotations

import logging
from collections import OrderedDict
from concurrent.futures import ThreadPoolExecutor
from typing import Iterable
from urllib.parse import urlparse
from xml.sax.saxutils import escape, quoteattr

from .collectors.newsapi import fetch_newsapi_articles
from .collectors.rss import fetch_rss_entries
from .extractors.web_content import batch_extract
from .models import SourceItem
from .settings import DATA_DIR, ScoringConfig, load_settings, load_sources_config
from .state import load_episode_history, load_used_sources, save_used_sources
from .utils import fingerprint, iso_now, title_similarity, within_hours, write_json

logger = logging.getLogger(__name__)

# ── Paywall domain filter ────────────────────────────────────────────────────
# Hard exclusion list: articles from these domains sit behind a paywall.
# Listeners cannot verify them, and reproducing their content raises
# copyright / plagiarism risk.  This list is intentionally conservative;
# add new domains as they are confirmed paywalled.
_PAYWALL_DOMAINS: frozenset[str] = frozenset({
    'wsj.com',
    'ft.com',
    'economist.com',
    'nytimes.com',
    'technologyreview.com',
    'bloomberg.com',
    'theinformation.com',
    'hbr.org',
    'barrons.com',
    'marketwatch.com',
    'seekingalpha.com',
    'lemonde.fr',
    'lefigaro.fr',
    'lesechos.fr',
    'thetimes.co.uk',
    'telegraph.co.uk',
})


def _is_paywalled(domain: str) -> bool:
    """Return True if *domain* (or any parent domain) is on the paywall list."""
    d = (domain or '').lower().removeprefix('www.')
    return any(d == pw or d.endswith('.' + pw) for pw in _PAYWALL_DOMAINS)


def _is_safe_http_url(url: str) -> bool:
    """Whitelist http(s) schemes for rendered links.

    Prevents `javascript:`, `data:`, `vbscript:` URIs from slipping into public
    HTML via a poisoned feed. Any malformed URL (parse error, wrong type) is
    treated as unsafe. Relative URLs with no scheme are rejected too — all
    source URLs in the manifest are absolute by construction.
    """
    try:
        return urlparse(url).scheme in ('http', 'https')
    except (ValueError, TypeError):
        return False


def _previous_episode_memory() -> tuple[set[str], list[str]]:
    history = load_episode_history()
    episodes = history.get("episodes", [])
    if not episodes:
        return set(), []
    latest = episodes[0]
    return set(latest.get("source_fingerprints", [])), list(latest.get("source_titles", []))


def _all_used_this_week() -> tuple[set[str], list[str]]:
    """Fingerprints and titles from all recent episodes (for weekly recap)."""
    history = load_episode_history()
    fps: set[str] = set()
    titles: list[str] = []
    for ep in history.get("episodes", [])[:7]:
        fps.update(ep.get("source_fingerprints", []))
        titles.extend(ep.get("source_titles", []))
    used = load_used_sources()
    titles.extend(item.get("title", "") for item in used.get("items", []))
    return fps, titles


def _recent_used_titles() -> list[str]:
    payload = load_used_sources()
    return [item.get("title", "") for item in payload.get("items", [])]


def _contains_banned_topic(text: str, scoring: ScoringConfig) -> bool:
    value = (text or "").lower()
    return any(term in value for term in scoring.banned_terms)


def _ai_relevance_score(texts: Iterable[str], scoring: ScoringConfig) -> float:
    joined = " ".join(text or "" for text in texts).lower()
    score = 0.0
    for term in scoring.ai_terms_high:
        if term in joined:
            score += 3.0
    for term in scoring.ai_terms_mid:
        if term in joined:
            score += 1.5
    for term in scoring.ai_terms_low:
        if term in joined:
            score += 0.5
    return score


def _score_source(item: SourceItem, scoring: ScoringConfig) -> float:
    score = 0.0
    combined = " ".join(filter(None, [item.title, item.summary, item.content_text])).lower()

    # Content depth
    content_len = len(item.content_text or "")
    if content_len >= 2000:
        score += 4.0
    elif content_len >= 1200:
        score += 3.0
    elif content_len >= 700:
        score += 2.0
    elif item.summary and len(item.summary) >= 180:
        score += 1.0

    # Numerical data density
    digit_count = sum(1 for char in combined if char.isdigit())
    if digit_count >= 10:
        score += 2.0
    elif digit_count >= 3:
        score += 1.0

    # Strong signal words
    strong_matches = sum(1 for w in scoring.signal_words_strong if w in combined)
    score += min(strong_matches * 1.0, 4.0)

    # Medium signal words
    medium_matches = sum(1 for w in scoring.signal_words_medium if w in combined)
    score += min(medium_matches * 0.5, 2.0)

    # Domain authority
    domain = (item.domain or "").lower()
    for auth_domain, bonus in scoring.domain_authority.items():
        if domain.endswith(auth_domain):
            score += bonus
            break

    # AI relevance
    ai_score = _ai_relevance_score([item.title, item.summary, item.content_text or ""], scoring)
    score += min(ai_score, 5.0)

    return round(score, 2)


def _is_editorially_valid(item: SourceItem, settings) -> bool:
    scoring = settings.scoring

    if not item.url or not item.title or not item.domain:
        return False

    # Hard exclusion: never cite sources that are behind a paywall.
    if _is_paywalled(item.domain):
        return False

    if not within_hours(item.published_at, settings.freshness_hours):
        return False

    combined = " ".join(filter(None, [item.title, item.summary, item.content_text]))
    if _contains_banned_topic(combined, scoring):
        return False

    ai_score = _ai_relevance_score([item.title, item.summary, item.content_text or ""], scoring)
    if ai_score < 1.0:
        return False

    effective_text = (item.content_text or item.summary or "").strip()
    if len(effective_text) < scoring.min_text_length:
        return False

    item.relevance_score = _score_source(item, scoring)
    return item.relevance_score >= scoring.min_relevance


def _is_duplicate_of_previous(
    item: SourceItem,
    previous_fingerprints: set[str],
    previous_titles: list[str],
    recent_titles: list[str],
    threshold: float,
) -> bool:
    fp = fingerprint(item.title, item.url)
    if fp in previous_fingerprints:
        return True

    for prior_title in previous_titles + recent_titles:
        if title_similarity(item.title, prior_title) >= threshold:
            return True

    return False


def _apply_weekly_bonus(
    sources: list[SourceItem],
    used_fps: set[str],
    used_titles: list[str],
    settings,
) -> list[SourceItem]:
    """For weekly recap: boost unused sources, penalize reused ones."""
    threshold = settings.scoring.similarity_threshold
    kept: list[SourceItem] = []
    for item in sources:
        fp = fingerprint(item.title, item.url)
        is_reused = fp in used_fps or any(
            title_similarity(item.title, t) >= threshold for t in used_titles
        )
        if is_reused:
            if item.relevance_score < settings.reuse_min_score:
                continue
            item.relevance_score = round(item.relevance_score - 1.0, 2)
        else:
            item.relevance_score = round(item.relevance_score + settings.unused_score_bonus, 2)
        kept.append(item)
    kept.sort(key=lambda s: (s.relevance_score, s.published_at or ""), reverse=True)
    return kept


USED_SOURCES_RETENTION_DAYS = 10
USED_SOURCES_HARD_CAP = 400


def _update_used_sources(sources: list[SourceItem]) -> None:
    """Record the sources cited in today's episode and trim old entries.

    Retention policy:
    - Time-based: drop entries older than USED_SOURCES_RETENTION_DAYS (default 10).
      This is the primary dedup window — an article that aired 11 days ago is
      fair game again and shouldn't permanently block its own domain.
    - Size-based: hard-cap at USED_SOURCES_HARD_CAP as a safety net against
      runaway growth (e.g. weekly recaps that mark 200+ sources in one run).

    Entries without a parseable `used_at` timestamp are conservatively kept
    under the hard cap so a legacy file with bare {title, url} items won't
    be silently wiped on first write.
    """
    from datetime import datetime, timedelta, timezone

    payload = load_used_sources()
    items = payload.get("items", [])
    fresh = [{"title": src.title, "url": src.url, "used_at": iso_now()} for src in sources[:80]]

    cutoff = datetime.now(timezone.utc) - timedelta(days=USED_SOURCES_RETENTION_DAYS)
    kept: list[dict] = []
    for it in items:
        ts = it.get("used_at")
        if not ts:
            kept.append(it)  # legacy entry, hard-cap will catch it
            continue
        try:
            used_at = datetime.fromisoformat(ts)
        except ValueError:
            kept.append(it)
            continue
        if used_at >= cutoff:
            kept.append(it)

    merged = (fresh + kept)[:USED_SOURCES_HARD_CAP]
    payload["items"] = merged
    save_used_sources(payload)


def collect_sources(run_date: str, local_preview: bool = False, profile: str | None = None) -> dict:
    settings = load_settings(local_preview=local_preview, profile=profile)
    cfg = load_sources_config()

    # Phase 1: Collect metadata in parallel (RSS feeds + NewsAPI)
    logger.info("Phase 1: Collecting metadata from RSS and NewsAPI...")
    with ThreadPoolExecutor(max_workers=2) as executor:
        rss_future = executor.submit(
            fetch_rss_entries,
            list(cfg.get("google_news_rss", [])) + list(cfg.get("curated_rss", [])),
            settings.freshness_hours,
        )
        newsapi_future = executor.submit(
            fetch_newsapi_articles,
            settings.newsapi_api_key,
            settings.newsapi_query,
            settings.newsapi_page_size,
            settings.freshness_hours,
        )
        rss_items = rss_future.result()
        newsapi_items = newsapi_future.result()

    logger.info("Collected %d RSS + %d NewsAPI items", len(rss_items), len(newsapi_items))

    # Phase 2: Pre-filter and deduplicate before expensive extraction
    if settings.exclude_previous_episode:
        previous_fingerprints, previous_titles = _previous_episode_memory()
        recent_titles = _recent_used_titles()
    else:
        previous_fingerprints, previous_titles, recent_titles = set(), [], []

    # For weekly recap: load all used data even though we don't pre-filter
    weekly_used_fps: set[str] = set()
    weekly_used_titles: list[str] = []
    if settings.prefer_unused:
        weekly_used_fps, weekly_used_titles = _all_used_this_week()

    candidates: list[SourceItem] = []
    seen_urls: set[str] = set()

    google_news_kept = 0
    for item in rss_items + newsapi_items:
        if item.url in seen_urls:
            continue
        seen_urls.add(item.url)

        if settings.exclude_previous_episode and _is_duplicate_of_previous(
            item, previous_fingerprints, previous_titles, recent_titles, settings.scoring.similarity_threshold
        ):
            continue

        if _contains_banned_topic(" ".join(filter(None, [item.title, item.summary])), settings.scoring):
            continue

        if "news.google.com" in (item.url or ""):
            google_news_kept += 1

        candidates.append(item)

    if google_news_kept:
        logger.info("Kept %d Google News items (unresolved URLs use RSS summary)", google_news_kept)

    logger.info("Phase 2: %d candidates after pre-filtering", len(candidates))

    # Phase 3: Batch extract content in parallel for items missing content
    # Skip extraction for arxiv.org — RSS abstract is sufficient for scoring
    SKIP_EXTRACT_DOMAINS = {"arxiv.org", "news.google.com"}
    urls_to_extract = [
        item.url for item in candidates
        if not (item.content_text or "").strip()
        and not any(d in (item.domain or "") for d in SKIP_EXTRACT_DOMAINS)
    ]
    if urls_to_extract:
        logger.info("Phase 3: Extracting content for %d articles...", len(urls_to_extract))
        extracted_map = batch_extract(urls_to_extract)
        for item in candidates:
            if not (item.content_text or "").strip() and item.url in extracted_map:
                result = extracted_map[item.url]
                if result:
                    item.content_text = result.text
    else:
        logger.info("Phase 3: All candidates already have content")

    # Phase 4: Score and filter
    deduped: OrderedDict[str, SourceItem] = OrderedDict()
    for item in candidates:
        if not _is_editorially_valid(item, settings):
            continue

        fp = fingerprint(item.title, item.url)
        existing = deduped.get(fp)
        if existing is None or item.relevance_score > existing.relevance_score:
            deduped[fp] = item

    sources = list(deduped.values())
    sources.sort(key=lambda s: (s.relevance_score, s.published_at or ""), reverse=True)

    # Phase 4b: Weekly bonus/penalty for unused vs reused sources
    if settings.prefer_unused and weekly_used_fps:
        sources = _apply_weekly_bonus(sources, weekly_used_fps, weekly_used_titles, settings)

    # Phase 4c: Cap per domain to ensure source diversity
    max_per_domain = settings.scoring.max_per_domain
    if max_per_domain > 0:
        domain_counts: dict[str, int] = {}
        capped: list[SourceItem] = []
        for item in sources:
            d = (item.domain or "").lower()
            count = domain_counts.get(d, 0)
            if count >= max_per_domain:
                continue
            domain_counts[d] = count + 1
            capped.append(item)
        if len(capped) < len(sources):
            logger.info("Domain cap applied: %d → %d sources (max %d per domain)", len(sources), len(capped), max_per_domain)
        sources = capped

    logger.info(
        "Phase 4: %d sources selected (min required: %d)",
        len(sources), settings.min_source_count,
    )

    _update_used_sources(sources)

    manifest = {
        "run_date": run_date,
        "generated_at": iso_now(),
        "source_count": len(sources),
        "profile": settings.profile_name,
        "sources": [s.to_dict() for s in sources],
    }

    # Per-locale manifest storage prevents EN and FR matrix jobs from
    # clobbering each other's data/sources/latest.json on the same run date.
    # Legacy single-locale mode (no APR_LOCALE) keeps writing to data/sources/.
    if settings.locale:
        data_sources_dir = DATA_DIR / "sources" / settings.locale
    else:
        data_sources_dir = DATA_DIR / "sources"
    # docs/sources/ for EN, docs/fr/sources/ for FR — driven by APR_LOCALE.
    docs_sources_dir = settings.docs_output_dir / "sources"
    data_sources_dir.mkdir(parents=True, exist_ok=True)
    docs_sources_dir.mkdir(parents=True, exist_ok=True)

    write_json(data_sources_dir / f"{run_date}.json", manifest)
    write_json(data_sources_dir / "latest.json", manifest)

    md = _manifest_to_markdown(manifest)
    html = _manifest_to_html(manifest)

    (data_sources_dir / f"{run_date}.md").write_text(md, encoding="utf-8")
    (data_sources_dir / "latest.md").write_text(md, encoding="utf-8")
    (docs_sources_dir / f"{run_date}.html").write_text(html, encoding="utf-8")
    (docs_sources_dir / "latest.html").write_text(html, encoding="utf-8")

    return manifest


def _manifest_to_markdown(manifest: dict) -> str:
    lines = [
        f"# Source manifest — {manifest['run_date']}",
        "",
        f"Generated at: {manifest['generated_at']}",
        f"Profile: {manifest.get('profile', 'daily')}",
        f"Relevant source count: {manifest['source_count']}",
        "",
    ]

    for idx, src in enumerate(manifest["sources"], start=1):
        lines.extend(
            [
                f"## {idx}. {src['title']}",
                f"- Domain: {src['domain']}",
                f"- URL: {src['url']}",
                f"- Relevance score: {src.get('relevance_score', 0.0)}",
            ]
        )

        if src.get("published_at"):
            lines.append(f"- Published: {src['published_at']}")
        if src.get("summary"):
            lines.append(f"- Summary: {src['summary']}")
        if src.get("content_text"):
            lines.append(f"- Extract: {src['content_text'][:800]}")

        lines.append("")

    return "\n".join(lines)


def _manifest_to_html(manifest: dict) -> str:
    # Article excerpts are intentionally omitted from the public source page
    # to avoid reproducing copyrighted content without explicit permission.
    # Only title, author (if available), publication, date, and link are shown.
    # Paywalled sources are silently excluded even from older manifests that
    # were collected before the domain filter was added to the pipeline.
    cards = []

    for src in manifest["sources"]:
        if _is_paywalled(src.get("domain", "")):
            continue

        # Refuse to render non-http(s) URLs. `javascript:` in a feed would
        # otherwise be emitted verbatim into the public sources page — small
        # attack surface, trivial fix. `lstrip` was also replaced by
        # `removeprefix` below because lstrip takes a *character set*, so
        # "wow.example.com".lstrip("www.") drops the w+o, not the "www.".
        url = src.get("url", "")
        if not _is_safe_http_url(url):
            continue

        pub = src.get("published_at", "")[:10] if src.get("published_at") else ""
        author = (src.get("author") or "").strip()

        # Publication name: clean domain, strip literal "www." prefix only.
        domain_raw = src.get("domain", "") or ""
        publication = domain_raw.removeprefix("www.")

        # Build the by-line: "by Author · Publication · Date" (omit missing parts)
        byline_parts: list[str] = []
        if author:
            byline_parts.append(f"by {escape(author)}")
        if publication:
            byline_parts.append(escape(publication))
        if pub:
            byline_parts.append(escape(pub))
        byline = " · ".join(byline_parts)

        # quoteattr emits the surrounding quotes and escapes both " and '.
        cards.append(
            "<article class='source-card'>"
            f"<h3><a href={quoteattr(url)} target='_blank' rel='noopener'>{escape(src['title'])} ↗</a></h3>"
            + (f"<p class='source-byline'>{byline}</p>" if byline else "")
            + "</article>"
        )

    run_date = escape(manifest['run_date'])

    return (
        "<!doctype html>"
        "<html lang='en'>"
        "<head>"
        "<meta charset='utf-8'>"
        "<meta name='viewport' content='width=device-width,initial-scale=1'>"
        f"<title>Sources — {run_date} · AI Press Review</title>"
        "<style>"
        ":root{--bg:#09090b;--surface:#111113;--border:#1f1f23;--text:#e8e8ed;"
        "--text-secondary:#8a8a9a;--accent:#c8a96e;--font:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}"
        "body{background:var(--bg);color:var(--text);font-family:var(--font);"
        "max-width:760px;margin:0 auto;padding:2rem 1.5rem;line-height:1.6}"
        "h1{font-size:1.4rem;font-weight:600;margin-bottom:.25rem;color:var(--text)}"
        ".page-meta{font-size:.8rem;color:var(--text-secondary);margin-bottom:2rem}"
        ".page-meta a{color:var(--accent);text-decoration:none}"
        ".source-card{border-bottom:1px solid var(--border);padding:1rem 0}"
        ".source-card:last-child{border-bottom:none}"
        ".source-card h3{margin:0 0 .3rem;font-size:.95rem;font-weight:500;line-height:1.4}"
        ".source-card h3 a{color:var(--text);text-decoration:none}"
        ".source-card h3 a:hover{color:var(--accent)}"
        ".source-byline{margin:0;font-size:.78rem;color:var(--text-secondary)}"
        "</style>"
        "</head>"
        "<body>"
        f"<h1>Sources — {run_date}</h1>"
        f"<p class='page-meta'><a href='/'>← AI Press Review</a> &nbsp;·&nbsp; {len(manifest['sources'])} sources</p>"
        f"{''.join(cards)}"
        "</body>"
        "</html>"
    )
