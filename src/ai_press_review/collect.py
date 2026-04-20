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
from .utils import (
    atomic_write_text,
    fingerprint,
    iso_now,
    title_similarity,
    within_hours,
    write_json,
)

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


# ── Cross-check entity extraction ────────────────────────────────────────────
# Tokens that capitalize in English/French titles but carry no identifying
# signal. Kept lowercase — comparison is case-insensitive.
_ENTITY_STOPWORDS: frozenset[str] = frozenset({
    'the', 'and', 'for', 'with', 'from', 'into', 'that', 'this', 'what',
    'why', 'how', 'when', 'where', 'who', 'will', 'after', 'before', 'over',
    'under', 'new', 'news', 'says', 'said', 'says', 'can', 'could', 'should',
    'would', 'may', 'might', 'just', 'also', 'about', 'amid', 'against',
    'le', 'la', 'les', 'des', 'une', 'sur', 'sous', 'dans', 'pour', 'avec',
    'sans', 'plus', 'moins', 'avant', 'apres', 'apr\u00e8s', 'entre', 'chez',
    'ai', 'ia', 'it',
})


def _title_entities(title: str) -> set[str]:
    """Extract a coarse set of 'named entities' from a title.

    We don't need a real NER model — we just need a cheap signal of whether
    two headlines are talking about the same story.  A 3+ char token that
    starts with an uppercase letter (or is ALL CAPS, catching tickers like
    TSMC, ASML, GPU) and isn't a stopword is treated as an entity.
    """
    if not title:
        return set()
    out: set[str] = set()
    for raw in title.split():
        token = ''.join(c for c in raw if c.isalnum())
        if len(token) < 3:
            continue
        lower = token.lower()
        if lower in _ENTITY_STOPWORDS:
            continue
        # Uppercase-initial (Apple, OpenAI) OR all-caps (TSMC, NYSE, GPU, LLM)
        if token[0].isupper() or token.isupper():
            out.add(lower)
    return out


def _cross_check_dedupe(
    sources: list[SourceItem],
    min_shared_entities: int = 2,
) -> list[SourceItem]:
    """Drop near-duplicate stories that share >=N named entities with a
    higher-scoring item already kept.

    User instruction 2026-04-18 (1.96): "analyse croisee" before selection —
    avoid featuring the same story under different angles when two outlets
    cover the same acquisition / launch / earnings release.

    Inputs MUST be sorted by relevance_score descending so the best-scoring
    variant is kept and its near-duplicates dropped.  Two items collide when
    their title-entity sets share at least *min_shared_entities* tokens.

    Complexity is O(n*k) where k is the size of the running 'kept' set.
    For n=300 candidates this stays well under 50 ms.
    """
    kept: list[SourceItem] = []
    kept_entities: list[set[str]] = []
    dropped = 0
    for item in sources:
        ents = _title_entities(item.title)
        # Items without at least 2 entities can't collide under this rule;
        # keep them unconditionally (they'll be judged by other filters).
        if len(ents) < min_shared_entities:
            kept.append(item)
            kept_entities.append(ents)
            continue
        collision = False
        for prior in kept_entities:
            if len(ents & prior) >= min_shared_entities:
                collision = True
                break
        if collision:
            dropped += 1
            continue
        kept.append(item)
        kept_entities.append(ents)
    if dropped:
        logger.info(
            "Cross-check dedupe: dropped %d near-duplicate stories "
            "(shared >=%d named entities with a higher-scored item)",
            dropped, min_shared_entities,
        )
    return kept


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

    # Content depth — reweighted 2026-04-18 (user instruction 1.96: "pondertion
    # du contenu profond pour evaluer ce qui ressort"). The top bucket is
    # raised so a 3 000-char deep-dive dominates a 1 500-char press note,
    # and a new 300-char floor rewards summaries-only items with at least
    # some substance over one-line wire items.
    content_len = len(item.content_text or "")
    if content_len >= 3000:
        score += 6.0
    elif content_len >= 2000:
        score += 5.0
    elif content_len >= 1200:
        score += 3.5
    elif content_len >= 700:
        score += 2.0
    elif content_len >= 300:
        score += 1.0
    elif item.summary and len(item.summary) >= 180:
        score += 0.5

    # Numerical data density
    digit_count = sum(1 for char in combined if char.isdigit())
    if digit_count >= 10:
        score += 2.0
    elif digit_count >= 3:
        score += 1.0

    # Strong signal words
    strong_matches = sum(1 for w in scoring.signal_words_strong if w in combined)
    score += min(strong_matches * 1.0, 4.0)

    # Medium signal words — cap raised to 3.0 on 2026-04-18 so the expanded
    # medium list (24 terms vs. 10 before) can actually influence ranking
    # rather than saturating at 2.0 after 4 matches.
    medium_matches = sum(1 for w in scoring.signal_words_medium if w in combined)
    score += min(medium_matches * 0.5, 3.0)

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


def record_used_sources(entries: list[tuple[str, str]]) -> None:
    """Record sources cited in a PUBLISHED episode and trim old entries.

    Only called from `release_pending_draft` — **not** from `collect_sources`.
    Before this refactor, collect_sources wrote used_sources on every draft,
    so a rejected or re-generated draft still "consumed" its sources in the
    dedup pool for 10 days. That quietly blocked those stories from any
    future run, even though they never actually aired. Moving the write to
    release means:

      - Drafts that get rejected leave zero footprint.
      - Re-generating a draft on the same day is idempotent.
      - `used_sources.json` now truly means "published in the last N days".

    *entries* is a list of (title, url) tuples — the function is deliberately
    ignorant of the wider SourceItem shape so it can be called from the
    release pipeline where only the pending-draft dict is available.

    Retention policy (unchanged from the old implementation):
      - Time-based: drop entries older than USED_SOURCES_RETENTION_DAYS (10).
      - Size-based: hard-cap at USED_SOURCES_HARD_CAP as a safety net.
      - Legacy entries without `used_at` are kept under the hard cap so a
        pre-refactor state file isn't silently wiped on first write.
    """
    from datetime import datetime, timedelta, timezone

    payload = load_used_sources()
    items = payload.get("items", [])
    fresh = [
        {"title": title, "url": url, "used_at": iso_now()}
        for title, url in entries[:80]
    ]

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

    # Phase 2b: Pre-score on RSS metadata to cap the crawl budget.
    #
    # The content-extraction crawl (Phase 3) is the pipeline's biggest time sink:
    # ~22-25 min for 700 URLs on a weekly run. But scoring in Phase 4 only needs
    # a content_text boost for items that would otherwise be borderline — items
    # with strong domain authority + high AI-term density in their title/summary
    # will rank high regardless. So we:
    #   1. Score every candidate on title + summary + domain alone (no content).
    #   2. Sort by pre-score, take the top PRE_CRAWL_KEEP for full extraction.
    #   3. Keep the rest in a separate pool — they enter Phase 4 on summary only
    #      and can still pass the relevance gate if their summary is strong enough.
    #
    # Effect: crawl drops from ~700 to ~200 items → ~2-4 min with httpx async.
    # Trade-off: a few articles with weak summaries but rich content may be missed.
    # Mitigation: domain-authority items are pre-scored high and always crawled.
    # 2026-04-18: user re-validated 200 (not 100) to keep a wider extraction pool
    # feeding Phase 4 with full-content data. 200 stays within the 25-30 min
    # pipeline budget at concurrency-20 + 8s timeout.
    PRE_CRAWL_KEEP = 200
    if len(candidates) > PRE_CRAWL_KEEP:
        for item in candidates:
            item.relevance_score = _score_source(item, settings.scoring)
        candidates.sort(key=lambda i: (i.relevance_score, i.published_at or ""), reverse=True)
        crawl_pool = candidates[:PRE_CRAWL_KEEP]
        rss_only_pool = candidates[PRE_CRAWL_KEEP:]
        logger.info(
            "Phase 2b: pre-scored %d candidates — crawling top %d, "
            "%d enter Phase 4 on RSS summary only",
            len(candidates), len(crawl_pool), len(rss_only_pool),
        )
    else:
        crawl_pool = candidates
        rss_only_pool = []

    # Phase 3: Batch extract content in parallel for items missing content
    # Skip extraction for:
    #   - arxiv.org        — RSS abstract is sufficient for scoring
    #   - news.google.com  — the URL is a Google News redirect wrapper that
    #                        either 404s our crawler or serves a JS-only page;
    #                        trafilatura discards it and we're just wasting a
    #                        Chromium tab. The 2026-04-18 weekly run spent
    #                        several minutes pointlessly crawling 272 of these.
    # Two lists, two reasons:
    #   SKIP_EXTRACT_DOMAINS: matched against item.domain (the real publisher,
    #       captured from the RSS <source> tag for Google News items).
    #   SKIP_EXTRACT_URL_HOSTS: matched against the URL's own hostname. This
    #       is the one that catches news.google.com — the Google News item's
    #       domain field has already been rewritten to the real publisher
    #       (e.g. "techcrunch.com"), so a domain-only check misses it. The
    #       earlier version used domain only, and "news.google.com" never
    #       matched a Google News item's rewritten domain — silent waste.
    SKIP_EXTRACT_DOMAINS = {"arxiv.org"}
    SKIP_EXTRACT_URL_HOSTS = {"news.google.com"}

    def _should_extract(item: SourceItem) -> bool:
        if (item.content_text or "").strip():
            return False
        if any(d in (item.domain or "") for d in SKIP_EXTRACT_DOMAINS):
            return False
        try:
            host = urlparse(item.url or "").hostname or ""
        except ValueError:
            return False
        if host in SKIP_EXTRACT_URL_HOSTS:
            return False
        return True

    urls_to_extract = [item.url for item in crawl_pool if _should_extract(item)]
    if urls_to_extract:
        logger.info("Phase 3: Extracting content for %d articles...", len(urls_to_extract))
        extracted_map = batch_extract(urls_to_extract)
        for item in crawl_pool:
            if not (item.content_text or "").strip() and item.url in extracted_map:
                result = extracted_map[item.url]
                if result:
                    item.content_text = result.text
    else:
        logger.info("Phase 3: All candidates already have content")

    # Phase 4: Score and filter — crawled pool (full content) + RSS-only pool
    all_candidates = crawl_pool + rss_only_pool
    deduped: OrderedDict[str, SourceItem] = OrderedDict()
    for item in all_candidates:
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

    # Phase 4b.5: Cross-check dedupe — drop same-story variants. This runs
    # AFTER scoring and weekly bonuses so the kept variant is the highest-
    # scoring one. See _cross_check_dedupe() for the rationale.
    sources = _cross_check_dedupe(sources)

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

    # NOTE: used_sources.json is NO LONGER updated here. Only a successfully
    # RELEASED episode should consume its sources for dedup. See
    # `pipeline.release_pending_draft` which calls record_used_sources at
    # that point.

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

    # atomic_write_text to guard against partial writes — the manifest
    # pages are served from GitHub Pages, so half-written HTML would be
    # visible to visitors and crawlers between the truncate and the flush.
    atomic_write_text(data_sources_dir / f"{run_date}.md", md)
    atomic_write_text(data_sources_dir / "latest.md", md)
    atomic_write_text(docs_sources_dir / f"{run_date}.html", html)
    atomic_write_text(docs_sources_dir / "latest.html", html)

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


_SECTION_LABELS = {
    'ai_news': 'AI News',
    'use_cases': 'Use Cases',
    'tools_practice': 'Tools & Practice',
    'weak_signals': 'Weak Signals',
    'off_radar': 'Off the Radar',
    'research': 'Research',
    'weekly_news': 'Weekly News',
    'weekly_use_cases': 'Weekly Use Cases',
    'weekly_tools': 'Weekly Tools',
    'weekly_signals': 'Weekly Signals',
    'weekly_research': 'Weekly Research',
    'weekly_next_week': 'Next Week',
    'intro': 'Intro',
    'outro': 'Outro',
}


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

        author = (src.get("author") or "").strip()

        # Publication name: clean domain, strip literal "www." prefix only.
        domain_raw = src.get("domain", "") or ""
        domain = domain_raw.removeprefix("www.")

        # Short date for display (e.g. "Apr 14")
        pub_short = ""
        pub_raw = src.get("published_at", "") or ""
        if pub_raw:
            try:
                from datetime import datetime as _dt
                pub_short = _dt.fromisoformat(pub_raw[:19]).strftime("%b %-d")
            except Exception:
                pass

        # Sections this source was used in
        sections = src.get("sections", []) or []
        section_labels = [
            _SECTION_LABELS.get(s, s.replace("_", " ").title())
            for s in sections
        ]

        # Meta line: domain · date
        meta_parts = []
        if domain:
            meta_parts.append(escape(domain))
        if pub_short:
            meta_parts.append(escape(pub_short))
        meta_line = " · ".join(meta_parts)

        # Build the by-line: "by Author" (omit if no author)
        byline = f"by {escape(author)}" if author else ""

        # Section tags HTML
        sections_html = ""
        if section_labels:
            tags = "".join(
                f"<span class='source-section-tag'>{escape(lbl)}</span>"
                for lbl in section_labels
            )
            sections_html = f"<div class='source-sections'>{tags}</div>"

        # quoteattr emits the surrounding quotes and escapes both " and '.
        cards.append(
            "<article class='source-card'>"
            f"<h3><a href={quoteattr(url)} target='_blank' rel='noopener'>{escape(src['title'])} ↗</a></h3>"
            + (f"<p class='source-meta'>{meta_line}</p>" if meta_line else "")
            + (f"<p class='source-byline'>{byline}</p>" if byline else "")
            + sections_html
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
        ".source-meta{margin:.15rem 0 .2rem;font-size:.75rem;color:#8a8a9a}"
        ".source-sections{display:inline-flex;gap:.35rem;flex-wrap:wrap;margin-top:.3rem}"
        ".source-section-tag{font-size:.65rem;padding:.1rem .45rem;border-radius:999px;background:rgba(200,169,110,.08);border:1px solid rgba(200,169,110,.2);color:#c8a96e}"
        "</style>"
        "</head>"
        "<body>"
        f"<h1>Sources — {run_date}</h1>"
        f"<p class='page-meta'><a href='/'>← AI Press Review</a> &nbsp;·&nbsp; {len(manifest['sources'])} sources</p>"
        f"{''.join(cards)}"
        "</body>"
        "</html>"
    )
