from __future__ import annotations

from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path
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
        if published_at.tzinfo is None:
            published_at = published_at.replace(tzinfo=timezone.utc)
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


def _secondary_category_xml(settings) -> str:
    if not settings.category_secondary:
        return ''
    if settings.category_secondary.strip().lower() == 'artificial intelligence':
        return '<itunes:category text="Technology"><itunes:category text="Artificial Intelligence" /></itunes:category>'
    return f'<itunes:category text="{escape(settings.category_secondary)}" />'


def _write_feed(episodes: list[dict]) -> None:
    settings = load_settings()
    items = []
    for ep in episodes:
        pub_date = format_datetime(datetime.fromisoformat(ep['published_at']))
        duration_secs = ep.get('duration_seconds', 0)
        duration_str = f"{duration_secs // 3600}:{(duration_secs % 3600) // 60:02d}:{duration_secs % 60:02d}"
        items.append(
            f"<item><title>{escape(ep['title'])}</title>"
            f"<description>{escape(ep['summary'])}</description>"
            f"<guid isPermaLink=\"false\">{escape(ep.get('date', '') + '-' + ep.get('slug', ''))}</guid>"
            f"<pubDate>{pub_date}</pubDate>"
            f'<enclosure url="{escape(ep["audio_url"])}" length="{ep["audio_bytes"]}" type="audio/mpeg" />'
            f"<itunes:summary>{escape(ep['summary'])}</itunes:summary>"
            f"<itunes:duration>{escape(duration_str)}</itunes:duration>"
            f"<link>{escape(ep['source_manifest_url'])}</link></item>"
        )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<?xml-stylesheet type="text/xsl" href="/feed.xsl"?>\n'
        '<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:atom="http://www.w3.org/2005/Atom">'
        '<channel>'
        f"<title>{escape(settings.podcast_title)}</title>"
        f"<link>{escape(settings.site_base_url)}</link>"
        f'<atom:link href="{escape(settings.rss_feed_url)}" rel="self" type="application/rss+xml" />'
        f"<language>{escape(settings.podcast_language)}</language>"
        f"<itunes:author>{escape(settings.podcast_author)}</itunes:author>"
        f"<itunes:subtitle>{escape(settings.podcast_subtitle)}</itunes:subtitle>"
        f"<itunes:summary>{escape(settings.podcast_description_short)}</itunes:summary>"
        f"<description>{escape(settings.podcast_description_long or settings.podcast_description_short)}</description>"
        f"<itunes:explicit>{'true' if settings.explicit else 'false'}</itunes:explicit>"
        '<itunes:owner>'
        f"<itunes:name>{escape(settings.podcast_author)}</itunes:name>"
        f"<itunes:email>{escape(settings.podcast_email)}</itunes:email>"
        '</itunes:owner>'
        f'<itunes:image href="{escape(settings.site_base_url)}/{escape(settings.cover_image_path)}" />'
        f'<itunes:category text="{escape(settings.category_primary)}" />'
        f'{_secondary_category_xml(settings)}'
        f"{''.join(items)}"
        '</channel></rss>'
    )
    (DOCS_DIR / 'podcast-feed.xml').write_text(xml, encoding='utf-8')


_INDEX_TEMPLATE_PATH = Path(__file__).parent / 'templates' / 'index-template.html'


def _write_index(episodes: list[dict]) -> None:
    template = _INDEX_TEMPLATE_PATH.read_text(encoding='utf-8')
    cards = []
    for ep in episodes:
        pub_dt = datetime.fromisoformat(ep['published_at'])
        date_str = pub_dt.strftime('%b %d, %Y')
        dur = ep.get('duration_seconds') or 0
        dur_str = f'{dur // 60} min' if dur else ''
        cards.append(
            f'<div class="episode-item">'
            f'<div>'
            f'<a href="{escape(ep["audio_url"])}" class="episode-title">{escape(ep["title"])}</a>'
            f'<div class="episode-meta">{date_str}</div>'
            f'<p class="episode-summary">{escape(ep["summary"])}</p>'
            f'<a href="{escape(ep["audio_url"])}" class="episode-listen">Listen &rarr;</a>'
            f'</div>'
            f'<span class="episode-duration">{dur_str}</span>'
            f'</div>'
        )
    episodes_html = '\n'.join(cards) if cards else '<div class="empty-state">First episode coming soon.</div>'
    html = template.replace('{{EPISODES}}', episodes_html)
    (DOCS_DIR / 'index.html').write_text(html, encoding='utf-8')
