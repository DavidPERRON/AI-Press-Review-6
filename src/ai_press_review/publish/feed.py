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


def publish_episode(
    episode: PublishedEpisode,
    source_fingerprints: list[str],
    source_titles: list[str],
    *,
    script: str | None = None,
    key_claims: list[dict] | None = None,
    grounding_report: dict | None = None,
) -> None:
    history = load_episode_history()
    episodes = history.get('episodes', [])
    payload = episode.to_dict()
    payload['source_fingerprints'] = source_fingerprints
    payload['source_titles'] = source_titles
    if script is not None:
        payload['script'] = script
    if key_claims is not None:
        payload['key_claims'] = key_claims
    if grounding_report is not None:
        payload['grounding_report'] = grounding_report
    payload['source_count'] = len(source_fingerprints)
    payload['domain_count'] = _count_domains(source_titles)
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
            # Remove stale per-episode transcript pages as well.
            _remove_episode_artifacts(item.get('slug', ''))

    history['episodes'] = kept
    save_episode_history(history)
    _write_transcripts(kept)
    _write_feed(kept)
    _write_index(kept)
    _write_sitemap(kept)
    _write_robots()


def _count_domains(source_titles: list[str]) -> int:
    """Best-effort domain count — if only titles are available, we can't
    compute it exactly, so we leave this as a placeholder the pipeline
    may override later."""
    return 0


def _remove_episode_artifacts(slug: str) -> None:
    if not slug:
        return
    episode_dir = DOCS_DIR / 'episodes' / slug
    if episode_dir.exists():
        for child in episode_dir.iterdir():
            try:
                child.unlink()
            except Exception:
                pass
        try:
            episode_dir.rmdir()
        except Exception:
            pass


def _write_transcripts(episodes: list[dict]) -> None:
    """Regenerate per-episode transcript artifacts (VTT + HTML) for
    every retained episode. Cheap enough at our scale (≤10 episodes)."""
    from .transcript import write_transcript_artifacts

    settings = load_settings()
    for ep in episodes:
        script = ep.get('script') or ''
        if not script:
            continue
        try:
            urls = write_transcript_artifacts(
                docs_dir=DOCS_DIR,
                slug=ep['slug'],
                script=script,
                duration_seconds=int(ep.get('duration_seconds') or 0),
                episode_meta={
                    'title': ep['title'],
                    'summary': ep.get('summary', ''),
                    'published_at': ep.get('published_at', ''),
                    'audio_url': ep.get('audio_url', ''),
                },
                site_base_url=_base_url(settings),
                feed_url=_feed_url(settings),
                cover_url=_absolute(settings, settings.cover_image_path),
                author=settings.podcast_author,
                language=settings.podcast_language,
                key_claims=ep.get('key_claims') or [],
                grounding_coverage=(ep.get('grounding_report') or {}).get('coverage_ratio'),
                source_count=ep.get('source_count', 0),
                domain_count=ep.get('domain_count', 0),
            )
            ep['transcript_vtt_url'] = urls['vtt_url']
            ep['episode_page_url'] = urls['html_url']
        except Exception:
            # Transcript generation is best-effort — never block publish.
            pass


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

_PODCAST_NS = 'https://podcastindex.org/namespace/1.0'


def _channel_guid(settings) -> str:
    """Stable channel GUID per Podcasting 2.0 spec. Deterministic UUIDv5
    derived from the podcast feed URL so it stays identical across
    regenerations but changes if the operator forks/moves the feed."""
    import uuid
    return str(uuid.uuid5(uuid.NAMESPACE_URL, _feed_url(settings)))


def _podcast_person_xml(settings) -> str:
    return (
        f'<podcast:person role="host" group="cast">'
        f'{escape(settings.podcast_author)}'
        '</podcast:person>'
    )


def _write_feed(episodes: list[dict]) -> None:
    settings = load_settings()
    feed_url = _feed_url(settings)
    cover_url = _absolute(settings, settings.cover_image_path)
    description = settings.podcast_description_long or settings.podcast_description_short
    last_build = format_datetime(utcnow())

    items = []
    for ep in episodes:
        pub_date = format_datetime(datetime.fromisoformat(ep['published_at']))
        transcript_tag = ''
        if ep.get('transcript_vtt_url'):
            transcript_tag = (
                f'<podcast:transcript url="{escape(ep["transcript_vtt_url"])}" '
                f'type="text/vtt" rel="captions" />'
            )
        episode_page = ep.get('episode_page_url') or ep.get('source_manifest_url')
        duration_tag = ''
        if ep.get('duration_seconds'):
            duration_tag = f'<itunes:duration>{int(ep["duration_seconds"])}</itunes:duration>'
        items.append(
            f"<item><title>{escape(ep['title'])}</title>"
            f"<description>{escape(ep['summary'])}</description>"
            f"<guid isPermaLink=\"false\">{escape(ep['audio_url'])}</guid>"
            f"<pubDate>{pub_date}</pubDate>"
            f'<enclosure url="{escape(ep["audio_url"])}" length="{ep["audio_bytes"]}" type="audio/mpeg" />'
            f"<itunes:summary>{escape(ep['summary'])}</itunes:summary>"
            f'<itunes:image href="{escape(cover_url)}" />'
            f"<itunes:explicit>{'true' if settings.explicit else 'false'}</itunes:explicit>"
            f"{duration_tag}"
            f"{transcript_tag}"
            f"{_podcast_person_xml(settings)}"
            f"<link>{escape(episode_page)}</link></item>"
        )

    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<rss version="2.0" '
        'xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" '
        'xmlns:content="http://purl.org/rss/1.0/modules/content/" '
        'xmlns:atom="http://www.w3.org/2005/Atom" '
        f'xmlns:podcast="{_PODCAST_NS}">'
        '<channel>'
        f"<title>{escape(settings.podcast_title)}</title>"
        f"<link>{escape(_base_url(settings))}</link>"
        f'<atom:link href="{escape(feed_url)}" rel="self" type="application/rss+xml" />'
        f"<language>{escape(settings.podcast_language)}</language>"
        f"<lastBuildDate>{last_build}</lastBuildDate>"
        '<generator>ai-press-review</generator>'
        # Podcasting 2.0 channel-level
        f'<podcast:guid>{_channel_guid(settings)}</podcast:guid>'
        '<podcast:medium>podcast</podcast:medium>'
        '<podcast:locked>no</podcast:locked>'
        f'{_podcast_person_xml(settings)}'
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


def _subscribe_buttons_html(settings, feed_url: str) -> str:
    """Render Subscribe row. Each platform button is hidden if URL is
    empty in config — RSS is always shown as the always-on fallback."""
    buttons: list[str] = []

    if settings.apple_podcasts_url:
        buttons.append(
            f"<a class='sub apple' href='{escape(settings.apple_podcasts_url)}' "
            "rel='noopener' target='_blank' aria-label='Listen on Apple Podcasts'>"
            "<svg viewBox='0 0 24 24' aria-hidden='true' width='18' height='18'>"
            "<path fill='currentColor' d='M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm0 4a3 3 0 1 1 0 6 3 3 0 0 1 0-6zm-3 9c0-1.1.9-2 2-2h2c1.1 0 2 .9 2 2v3a3 3 0 0 1-6 0v-3z'/>"
            "</svg>Apple Podcasts</a>"
        )
    if settings.spotify_url:
        buttons.append(
            f"<a class='sub spotify' href='{escape(settings.spotify_url)}' "
            "rel='noopener' target='_blank' aria-label='Listen on Spotify'>"
            "<svg viewBox='0 0 24 24' aria-hidden='true' width='18' height='18'>"
            "<circle cx='12' cy='12' r='10' fill='currentColor'/>"
            "<path fill='#fff' d='M7.3 9.5c3.3-.9 7.6-.7 11 1 .5.3.7 1 .4 1.5-.3.5-1 .7-1.5.4-2.9-1.5-6.7-1.7-9.5-.9-.6.2-1.1-.2-1.3-.7-.1-.6.3-1.2.9-1.3zm-.2 3.4c2.7-.7 6.6-.4 9.3 1.2.4.2.6.8.3 1.2-.2.4-.8.6-1.2.3-2.3-1.4-5.7-1.6-7.9-1-.5.1-.9-.2-1-.6-.1-.5.2-1 .5-1.1zm.4 3.2c2.2-.5 5.1-.3 7.2.9.3.2.4.6.2.9-.2.3-.6.4-.9.2-1.7-1-4.3-1.2-6.2-.7-.4.1-.7-.1-.8-.5-.1-.3.1-.7.5-.8z'/>"
            "</svg>Spotify</a>"
        )
    if settings.youtube_url:
        buttons.append(
            f"<a class='sub youtube' href='{escape(settings.youtube_url)}' "
            "rel='noopener' target='_blank' aria-label='Watch on YouTube'>"
            "<svg viewBox='0 0 24 24' aria-hidden='true' width='18' height='18'>"
            "<path fill='currentColor' d='M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2C.5 9.1.5 12 .5 12s0 2.9.5 4.8a3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1c.5-1.9.5-4.8.5-4.8s0-2.9-.5-4.8z'/>"
            "<path fill='#fff' d='M9.6 15.6V8.4l6.2 3.6z'/>"
            "</svg>YouTube</a>"
        )
    # RSS — always available
    buttons.append(
        f"<a class='sub rss' href='{escape(feed_url)}' "
        "aria-label='Subscribe via RSS'>"
        "<svg viewBox='0 0 24 24' aria-hidden='true' width='16' height='16'>"
        "<path fill='currentColor' d='M4 4a16 16 0 0 1 16 16h-3A13 13 0 0 0 4 7V4zm0 6a10 10 0 0 1 10 10h-3a7 7 0 0 0-7-7v-3zm2 7a2 2 0 1 1 0 4 2 2 0 0 1 0-4z'/>"
        "</svg>RSS</a>"
    )
    return f"<div class='subscribe'>{''.join(buttons)}</div>"


def _episode_card(ep: dict, base: str, *, featured: bool = False) -> str:
    episode_link = ep.get('episode_page_url') or f"{base}/episodes/{ep.get('slug', '')}/"
    duration_min = ''
    if ep.get('duration_seconds'):
        duration_min = f" &middot; {int(ep['duration_seconds']) // 60} min"
    pub_label = (ep.get('published_at') or '')[:10]
    cls = 'card featured' if featured else 'card'
    return (
        f"<article class='{cls}'>"
        f"<p class='ep-meta'>{escape(pub_label)}{duration_min}</p>"
        f"<h3><a href='{escape(episode_link)}'>{escape(ep['title'])}</a></h3>"
        f"<p>{escape(ep['summary'])}</p>"
        f"<p class='ep-links'>"
        f"<a href='{escape(episode_link)}'>Transcript &amp; episode page</a> &middot; "
        f"<a href='{escape(ep['audio_url'])}'>Listen</a> &middot; "
        f"<a href='{escape(ep['source_manifest_url'])}'>Sources</a>"
        f"</p>"
        f"</article>"
    )


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

    if episodes:
        first = _episode_card(episodes[0], base, featured=True)
        rest = ''.join(_episode_card(ep, base) for ep in episodes[1:])
        episodes_html = first + rest
    else:
        episodes_html = "<div class='card empty'><strong>First episode publishing soon.</strong> Subscribe via the buttons above to be notified.</div>"

    subscribe_html = _subscribe_buttons_html(settings, feed_url)
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
        # Reset & base
        "*{box-sizing:border-box}"
        "body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;"
        "margin:0;padding:0;line-height:1.55;color:#111;background:#fff}"
        ".wrap{max-width:880px;margin:0 auto;padding:1.5rem 1.25rem 3rem}"
        # Hero — horizontal layout, compact so first episode is above the fold
        ".hero{display:flex;align-items:center;gap:1.4rem;padding:1rem 0 1.4rem;"
        "border-bottom:1px solid #eee;margin-bottom:1.5rem}"
        ".hero img.logo{width:140px;height:140px;border-radius:22px;flex-shrink:0;"
        "box-shadow:0 4px 18px rgba(0,0,0,.10)}"
        ".hero-content{min-width:0;flex:1}"
        ".hero h1{margin:0;font-size:1.7rem;letter-spacing:-.01em}"
        ".hero .tagline{margin:.25rem 0 .65rem;color:#444;font-size:1rem}"
        # Subscribe row
        ".subscribe{display:flex;flex-wrap:wrap;gap:.5rem;align-items:center}"
        ".sub{display:inline-flex;align-items:center;gap:.4rem;padding:.45rem .8rem;"
        "border-radius:999px;border:1px solid #ddd;font-size:.85rem;font-weight:500;"
        "text-decoration:none;transition:all .15s}"
        ".sub svg{flex-shrink:0}"
        ".sub.apple{color:#a437dc;border-color:#e4c8f5}"
        ".sub.apple:hover{background:#f7eefc}"
        ".sub.spotify{color:#1db954;border-color:#bfeac9}"
        ".sub.spotify:hover{background:#e8f8ed}"
        ".sub.youtube{color:#ff0033;border-color:#ffc8d1}"
        ".sub.youtube:hover{background:#fff0f3}"
        ".sub.rss{color:#e69200;border-color:#ffe1b3}"
        ".sub.rss:hover{background:#fff5e3}"
        # How-it-works prominent CTA in hero
        ".hiw-cta{display:inline-flex;align-items:center;gap:.35rem;margin-left:.5rem;"
        "padding:.45rem .85rem;border-radius:999px;background:#111;color:#fff;"
        "font-size:.85rem;font-weight:500;text-decoration:none;transition:opacity .15s}"
        ".hiw-cta:hover{opacity:.85}"
        # Episodes section
        ".section-head{display:flex;align-items:baseline;justify-content:space-between;"
        "margin:0 0 .8rem;gap:1rem}"
        ".section-head h2{margin:0;font-size:1.15rem;letter-spacing:.02em;"
        "text-transform:uppercase;color:#555}"
        ".section-head .small-link{font-size:.85rem;color:#0b5fff;text-decoration:none}"
        ".card{border:1px solid #e5e5e5;border-radius:16px;padding:1rem 1.25rem;"
        "margin:.85rem 0;background:#fff;transition:border-color .15s}"
        ".card:hover{border-color:#bbb}"
        ".card.featured{border:2px solid #111;padding:1.25rem 1.4rem}"
        ".card.empty{text-align:center;color:#555;padding:2rem;border-style:dashed}"
        ".card h3{margin:.15rem 0 .4rem;font-size:1.15rem;line-height:1.3}"
        ".card h3 a{color:#111;text-decoration:none}"
        ".card h3 a:hover{color:#0b5fff}"
        ".card p{margin:.35rem 0}"
        ".ep-meta{font-size:.8rem;color:#888;text-transform:uppercase;"
        "letter-spacing:.05em;margin:0 0 .3rem}"
        ".ep-links{font-size:.85rem;color:#666}"
        ".ep-links a{color:#0b5fff;text-decoration:none}"
        ".ep-links a:hover{text-decoration:underline}"
        # How-it-works inline section
        "#how-it-works{margin-top:3rem;padding-top:1.5rem;border-top:1px solid #eee}"
        "#how-it-works h2{font-size:1.3rem;margin:0 0 .25rem}"
        "#how-it-works .lead{color:#555;margin:.25rem 0 1.25rem;font-size:.95rem}"
        ".hiw-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));"
        "gap:1rem;margin-bottom:1rem}"
        ".hiw-grid .step{padding:1rem;background:#f7f7f8;border-radius:12px}"
        ".hiw-grid .step strong{display:block;font-size:.95rem;margin-bottom:.3rem}"
        ".hiw-grid .step span{color:#555;font-size:.88rem}"
        # Footer
        "footer{margin-top:3rem;padding-top:1rem;border-top:1px solid #eee;"
        "color:#888;font-size:.85rem;text-align:center}"
        "footer a{color:#888}"
        "a{color:#0b5fff}"
        # Mobile
        "@media (max-width:560px){"
        ".hero{flex-direction:column;align-items:flex-start;gap:1rem;text-align:left}"
        ".hero img.logo{width:96px;height:96px;border-radius:18px}"
        ".hero h1{font-size:1.4rem}"
        ".hiw-cta{margin-left:0}"
        "}"
        "</style>"
        "</head>"
        "<body>"
        "<div class='wrap'>"
        # ── HERO ──
        "<header class='hero'>"
        f"<img class='logo' src='{escape(cover_rel)}' alt='{escape(settings.podcast_title)} cover'>"
        "<div class='hero-content'>"
        f"<h1>{escape(settings.podcast_title)}</h1>"
        f"<p class='tagline'>{escape(settings.podcast_subtitle)}</p>"
        f"{subscribe_html}"
        " <a class='hiw-cta' href='#how-it-works'>How it works &rarr;</a>"
        "</div>"
        "</header>"
        # ── EPISODES (above the fold) ──
        "<main>"
        "<section aria-label='Latest episodes'>"
        "<div class='section-head'>"
        "<h2>Latest episodes</h2>"
        f"<a class='small-link' href='{escape(feed_url)}'>RSS &rarr;</a>"
        "</div>"
        f"{episodes_html}"
        "</section>"
        # ── HOW IT WORKS (inline anchor) ──
        "<section id='how-it-works'>"
        "<h2>How it works</h2>"
        f"<p class='lead'>{escape(description)}</p>"
        "<div class='hiw-grid'>"
        "<div class='step'><strong>40+ sources, weighted</strong>"
        "<span>Primary labs (OpenAI, DeepMind, Anthropic, arXiv) carry more weight than aggregators. Regulatory speculation and unverified rumors are excluded.</span></div>"
        "<div class='step'><strong>Semantic clustering</strong>"
        "<span>Sources reporting the same story are grouped before the editorial pass. Single-source claims are flagged as weak signals.</span></div>"
        "<div class='step'><strong>Claim &rarr; source grounding</strong>"
        "<span>Every factual claim in the script is verified against the cited source. Per-episode coverage is published on the transcript page.</span></div>"
        "<div class='step'><strong>14&ndash;18 minute briefing</strong>"
        "<span>Six pillars: AI News, Use Cases, Tools &amp; Practice, Weak Signals, Research, Education. Every Saturday: a weekly recap.</span></div>"
        "</div>"
        "</section>"
        "</main>"
        "<footer>"
        f"Hosted by {escape(settings.podcast_author)} &middot; "
        f"<a href='{escape(feed_url)}'>RSS feed</a>"
        "</footer>"
        "</div>"
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
    # Per-episode transcript pages — indexable content is the real SEO lever.
    for ep in episodes:
        slug = ep.get('slug')
        if not slug:
            continue
        ep_date = (ep.get('published_at') or lastmod)[:10]
        urls.append((f'episodes/{slug}/', 'weekly', '0.8', ep_date))
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
