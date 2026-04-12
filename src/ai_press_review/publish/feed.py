from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from xml.sax.saxutils import escape

from ..models import PublishedEpisode
from ..settings import DOCS_DIR, load_settings
from ..state import load_episode_history, save_episode_history
from ..storage.r2 import delete_key
from ..utils import utcnow


def publish_episode(episode: PublishedEpisode, source_fingerprints: list[str], source_titles: list[str]) -> None:
    history = load_episode_history()
    episodes = history.get('episodes', [])
    payload = episode.to_dict()
    payload['source_fingerprints'] = source_fingerprints
    payload['source_titles'] = source_titles
    episodes.insert(0, payload)

    settings = load_settings()
    cutoff = utcnow() - timedelta(days=settings.retention_days)

    kept = []
    for item in episodes:
        published_at = datetime.fromisoformat(item['published_at'])
        if published_at >= cutoff:
            kept.append(item)
        else:
            try:
                key = item['audio_url'].replace(settings.public_audio_base_url.rstrip('/') + '/', '')
                delete_key(key)
            except Exception:
                pass

    history['episodes'] = kept
    save_episode_history(history)
    _write_feed(kept)
    _write_index(kept)
    _write_sitemap(kept)
    _write_robots()


# ── helpers ──────────────────────────────────────────────────────────────────

def _base_url(settings) -> str:
    return settings.site_base_url.rstrip('/')


def _absolute(settings, path: str) -> str:
    if path.startswith('http://') or path.startswith('https://'):
        return path
    return f"{_base_url(settings)}/{path.lstrip('/')}"


def _feed_url(settings) -> str:
    return settings.rss_feed_url or f"{_base_url(settings)}/podcast-feed.xml"


def _secondary_category_xml(settings) -> str:
    if not settings.category_secondary:
        return ''
    if settings.category_secondary.strip().lower() == 'artificial intelligence':
        return '<itunes:category text="Technology"><itunes:category text="Artificial Intelligence" /></itunes:category>'
    return f'<itunes:category text="{escape(settings.category_secondary)}" />'


# ── RSS feed ─────────────────────────────────────────────────────────────────

def _write_feed(episodes: list[dict]) -> None:
    settings = load_settings()
    feed_url = _feed_url(settings)
    cover_url = _absolute(settings, settings.cover_image_path)
    description = settings.podcast_description_long or settings.podcast_description_short
    last_build = format_datetime(utcnow())

    items = []
    for ep in episodes:
        pub_date = format_datetime(datetime.fromisoformat(ep['published_at']))
        items.append(
            f"<item><title>{escape(ep['title'])}</title>"
            f"<description>{escape(ep['summary'])}</description>"
            f"<guid isPermaLink=\"false\">{escape(ep['audio_url'])}</guid>"
            f"<pubDate>{pub_date}</pubDate>"
            f'<enclosure url="{escape(ep["audio_url"])}" length="{ep["audio_bytes"]}" type="audio/mpeg" />'
            f"<itunes:summary>{escape(ep['summary'])}</itunes:summary>"
            f'<itunes:image href="{escape(cover_url)}" />'
            f"<itunes:explicit>{'true' if settings.explicit else 'false'}</itunes:explicit>"
            f"<link>{escape(ep['source_manifest_url'])}</link></item>"
        )

    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<rss version="2.0" '
        'xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" '
        'xmlns:content="http://purl.org/rss/1.0/modules/content/" '
        'xmlns:atom="http://www.w3.org/2005/Atom">'
        '<channel>'
        f"<title>{escape(settings.podcast_title)}</title>"
        f"<link>{escape(_base_url(settings))}</link>"
        f'<atom:link href="{escape(feed_url)}" rel="self" type="application/rss+xml" />'
        f"<language>{escape(settings.podcast_language)}</language>"
        f"<lastBuildDate>{last_build}</lastBuildDate>"
        '<generator>ai-press-review</generator>'
        f"<itunes:author>{escape(settings.podcast_author)}</itunes:author>"
        f"<itunes:subtitle>{escape(settings.podcast_subtitle)}</itunes:subtitle>"
        f"<itunes:summary>{escape(settings.podcast_description_short)}</itunes:summary>"
        f"<description>{escape(description)}</description>"
        '<itunes:type>episodic</itunes:type>'
        f"<itunes:explicit>{'true' if settings.explicit else 'false'}</itunes:explicit>"
        '<itunes:owner>'
        f"<itunes:name>{escape(settings.podcast_author)}</itunes:name>"
        f"<itunes:email>{escape(settings.podcast_email)}</itunes:email>"
        '</itunes:owner>'
        f'<itunes:image href="{escape(cover_url)}" />'
        f'<image><url>{escape(cover_url)}</url>'
        f"<title>{escape(settings.podcast_title)}</title>"
        f"<link>{escape(_base_url(settings))}</link></image>"
        f'<itunes:category text="{escape(settings.category_primary)}" />'
        f'{_secondary_category_xml(settings)}'
        f"{''.join(items)}"
        '</channel></rss>'
    )
    (DOCS_DIR / 'podcast-feed.xml').write_text(xml, encoding='utf-8')


# ── HTML landing page ────────────────────────────────────────────────────────

def _json_ld(settings, episodes: list[dict]) -> str:
    base = _base_url(settings)
    cover_url = _absolute(settings, settings.cover_image_path)
    description = settings.podcast_description_long or settings.podcast_description_short

    episode_nodes = []
    for ep in episodes[:10]:
        episode_nodes.append({
            '@type': 'PodcastEpisode',
            'name': ep['title'],
            'description': ep['summary'],
            'datePublished': ep['published_at'],
            'url': ep['audio_url'],
            'associatedMedia': {
                '@type': 'MediaObject',
                'contentUrl': ep['audio_url'],
                'encodingFormat': 'audio/mpeg',
            },
        })

    data = {
        '@context': 'https://schema.org',
        '@type': 'PodcastSeries',
        'name': settings.podcast_title,
        'url': base,
        'description': description,
        'image': cover_url,
        'inLanguage': settings.podcast_language,
        'author': {'@type': 'Person', 'name': settings.podcast_author},
        'webFeed': _feed_url(settings),
    }
    if episode_nodes:
        data['episode'] = episode_nodes

    return json.dumps(data, ensure_ascii=False)


def _write_index(episodes: list[dict]) -> None:
    settings = load_settings()
    base = _base_url(settings)
    cover_rel = settings.cover_image_path
    cover_url = _absolute(settings, cover_rel)
    description = settings.podcast_description_short or settings.podcast_description_long
    feed_url = _feed_url(settings)

    keywords = (
        'AI podcast, artificial intelligence, generative AI, LLM, '
        'AI news, AI research, AI use cases, AI tools, weak signals, '
        'AI for business, daily AI briefing'
    )

    cards = []
    for ep in episodes:
        cards.append(
            f"<article class='card'>"
            f"<h3>{escape(ep['title'])}</h3>"
            f"<p>{escape(ep['summary'])}</p>"
            f"<p><a href='{escape(ep['audio_url'])}'>Listen</a> &middot; "
            f"<a href='{escape(ep['source_manifest_url'])}'>Sources</a></p>"
            f"</article>"
        )
    empty = "<div class='card'><strong>No episodes published yet.</strong></div>"

    json_ld = _json_ld(settings, episodes)

    html = (
        "<!doctype html>"
        f"<html lang='{escape(settings.podcast_language)}'>"
        "<head>"
        "<meta charset='utf-8'>"
        "<meta name='viewport' content='width=device-width,initial-scale=1'>"
        f"<title>{escape(settings.podcast_title)} &mdash; {escape(settings.podcast_subtitle)}</title>"
        f"<meta name='description' content='{escape(description)}'>"
        f"<meta name='keywords' content='{escape(keywords)}'>"
        f"<meta name='author' content='{escape(settings.podcast_author)}'>"
        "<meta name='robots' content='index,follow,max-image-preview:large'>"
        "<meta name='theme-color' content='#111111'>"
        f"<link rel='canonical' href='{escape(base)}/'>"
        f"<link rel='alternate' type='application/rss+xml' title='{escape(settings.podcast_title)} RSS' href='{escape(feed_url)}'>"
        f"<link rel='icon' type='image/png' href='{escape(cover_rel)}'>"
        f"<link rel='apple-touch-icon' href='{escape(cover_rel)}'>"
        # Open Graph
        "<meta property='og:type' content='website'>"
        f"<meta property='og:site_name' content='{escape(settings.podcast_title)}'>"
        f"<meta property='og:title' content='{escape(settings.podcast_title)} &mdash; {escape(settings.podcast_subtitle)}'>"
        f"<meta property='og:description' content='{escape(description)}'>"
        f"<meta property='og:url' content='{escape(base)}/'>"
        f"<meta property='og:image' content='{escape(cover_url)}'>"
        "<meta property='og:image:alt' content='AI Press Review cover'>"
        f"<meta property='og:locale' content='{escape(settings.podcast_language)}'>"
        # Twitter
        "<meta name='twitter:card' content='summary_large_image'>"
        f"<meta name='twitter:title' content='{escape(settings.podcast_title)}'>"
        f"<meta name='twitter:description' content='{escape(description)}'>"
        f"<meta name='twitter:image' content='{escape(cover_url)}'>"
        # JSON-LD
        f"<script type='application/ld+json'>{json_ld}</script>"
        "<style>"
        "body{font-family:-apple-system,BlinkMacSystemFont,sans-serif;max-width:760px;"
        "margin:2rem auto;padding:0 1rem;line-height:1.55;color:#111}"
        "img.cover{max-width:240px;border-radius:20px}"
        ".card{border:1px solid #ddd;border-radius:16px;padding:1rem 1.25rem;margin:1rem 0}"
        "h1{margin-bottom:.25rem}.subtitle{color:#555;margin-top:0}"
        "a{color:#0b5fff}"
        "</style>"
        "</head>"
        "<body>"
        f"<img class='cover' src='{escape(cover_rel)}' alt='{escape(settings.podcast_title)} cover'>"
        f"<h1>{escape(settings.podcast_title)}</h1>"
        f"<p class='subtitle'>{escape(settings.podcast_subtitle)}</p>"
        f"<p>{escape(description)}</p>"
        f"<p><a href='{escape(feed_url)}'>Podcast RSS feed</a></p>"
        "<main>"
        f"{''.join(cards) if cards else empty}"
        "</main>"
        "</body></html>"
    )
    (DOCS_DIR / 'index.html').write_text(html, encoding='utf-8')


# ── sitemap.xml & robots.txt ─────────────────────────────────────────────────

def _write_sitemap(episodes: list[dict]) -> None:
    settings = load_settings()
    base = _base_url(settings)
    feed_url = _feed_url(settings)

    if episodes:
        last_pub = max(ep['published_at'] for ep in episodes)
        lastmod = datetime.fromisoformat(last_pub).astimezone(timezone.utc).date().isoformat()
    else:
        lastmod = utcnow().date().isoformat()

    urls = [
        ('', 'daily', '1.0', lastmod),
        ('podcast-feed.xml', 'daily', '0.9', lastmod),
    ]
    url_nodes = ''.join(
        f'<url><loc>{escape(base)}/{escape(path)}</loc>'
        f'<lastmod>{lastmod}</lastmod>'
        f'<changefreq>{freq}</changefreq>'
        f'<priority>{prio}</priority></url>'
        for path, freq, prio, lastmod in urls
    )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f'{url_nodes}'
        '</urlset>'
    )
    (DOCS_DIR / 'sitemap.xml').write_text(xml, encoding='utf-8')


def _write_robots() -> None:
    settings = load_settings()
    base = _base_url(settings)
    content = (
        "User-agent: *\n"
        "Allow: /\n"
        f"Sitemap: {base}/sitemap.xml\n"
    )
    (DOCS_DIR / 'robots.txt').write_text(content, encoding='utf-8')
