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
from .locales import ALL_LOCALES, DEFAULT_LOCALE, LOCALES, get_locale


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
    # Generate site for every locale (EN, FR, ...). Episodes themselves
    # are EN-only for now; the FR site renders the same shell with French
    # UI strings and an empty episode list until a FR pipeline is wired.
    for locale in ALL_LOCALES:
        episodes_for_locale = kept if locale == DEFAULT_LOCALE else []
        _write_feed(episodes_for_locale, locale=locale)
        _write_index(episodes_for_locale, locale=locale)
        _write_how_it_works(locale=locale)
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


def _locale_path(loc: dict) -> str:
    """Return the URL prefix for a locale: '' for default, '/fr' otherwise."""
    site_path = loc.get('site_path', '').strip('/')
    return f"/{site_path}" if site_path else ''


def _locale_dir(loc: dict):
    """Return the docs sub-directory where this locale's files live."""
    site_path = loc.get('site_path', '').strip('/')
    out = DOCS_DIR / site_path if site_path else DOCS_DIR
    out.mkdir(parents=True, exist_ok=True)
    return out


def _feed_url(settings, loc: dict | None = None) -> str:
    if loc is None:
        return settings.rss_feed_url or f"{_base_url(settings)}/podcast-feed.xml"
    prefix = _locale_path(loc)
    return f"{_base_url(settings)}{prefix}/{loc.get('feed_filename', 'podcast-feed.xml')}"


def _home_url(settings, loc: dict) -> str:
    prefix = _locale_path(loc)
    return f"{_base_url(settings)}{prefix}/"


def _how_url(settings, loc: dict) -> str:
    prefix = _locale_path(loc)
    return f"{_base_url(settings)}{prefix}/how-it-works.html"


def _secondary_category_xml(settings) -> str:
    if not settings.category_secondary:
        return ''
    if settings.category_secondary.strip().lower() == 'artificial intelligence':
        return '<itunes:category text="Technology"><itunes:category text="Artificial Intelligence" /></itunes:category>'
    return f'<itunes:category text="{escape(settings.category_secondary)}" />'


# ── RSS feed ─────────────────────────────────────────────────────────────────

_PODCAST_NS = 'https://podcastindex.org/namespace/1.0'


def _channel_guid(settings, loc: dict | None = None) -> str:
    """Stable channel GUID per Podcasting 2.0 spec. Deterministic UUIDv5
    derived from the locale-specific feed URL so each locale has its
    own stable identifier (Apple/Spotify treat them as distinct shows)."""
    import uuid
    return str(uuid.uuid5(uuid.NAMESPACE_URL, _feed_url(settings, loc)))


def _podcast_person_xml(settings) -> str:
    return (
        f'<podcast:person role="host" group="cast">'
        f'{escape(settings.podcast_author)}'
        '</podcast:person>'
    )


def _write_feed(episodes: list[dict], locale: str = DEFAULT_LOCALE) -> None:
    settings = load_settings()
    loc = get_locale(locale)
    feed_url = _feed_url(settings, loc)
    cover_url = _absolute(settings, settings.cover_image_path)
    description = loc['intro_paragraph']
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
        f"<title>{escape(loc['title'])}</title>"
        f"<link>{escape(_home_url(settings, loc))}</link>"
        f'<atom:link href="{escape(feed_url)}" rel="self" type="application/rss+xml" />'
        f"<language>{escape(loc['lang'])}</language>"
        f"<lastBuildDate>{last_build}</lastBuildDate>"
        '<generator>ai-press-review</generator>'
        f'<podcast:guid>{_channel_guid(settings, loc)}</podcast:guid>'
        '<podcast:medium>podcast</podcast:medium>'
        '<podcast:locked>no</podcast:locked>'
        f'{_podcast_person_xml(settings)}'
        f"<itunes:author>{escape(settings.podcast_author)}</itunes:author>"
        f"<itunes:subtitle>{escape(loc['subtitle'])}</itunes:subtitle>"
        f"<itunes:summary>{escape(loc['description_short'])}</itunes:summary>"
        f"<description>{escape(description)}</description>"
        '<itunes:type>episodic</itunes:type>'
        f"<itunes:explicit>{'true' if settings.explicit else 'false'}</itunes:explicit>"
        '<itunes:owner>'
        f"<itunes:name>{escape(settings.podcast_author)}</itunes:name>"
        f"<itunes:email>{escape(settings.podcast_email)}</itunes:email>"
        '</itunes:owner>'
        f'<itunes:image href="{escape(cover_url)}" />'
        f'<image><url>{escape(cover_url)}</url>'
        f"<title>{escape(loc['title'])}</title>"
        f"<link>{escape(_home_url(settings, loc))}</link></image>"
        f'<itunes:category text="{escape(settings.category_primary)}" />'
        f'{_secondary_category_xml(settings)}'
        f"{''.join(items)}"
        '</channel></rss>'
    )
    (_locale_dir(loc) / loc.get('feed_filename', 'podcast-feed.xml')).write_text(xml, encoding='utf-8')


# ── HTML landing page ────────────────────────────────────────────────────────

def _json_ld(settings, episodes: list[dict], loc: dict | None = None) -> str:
    if loc is None:
        loc = get_locale(DEFAULT_LOCALE)
    cover_url = _absolute(settings, settings.cover_image_path)

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
        'name': loc['title'],
        'url': _home_url(settings, loc),
        'description': loc['description_short'],
        'image': cover_url,
        'inLanguage': loc['lang'],
        'author': {'@type': 'Person', 'name': settings.podcast_author},
        'webFeed': _feed_url(settings, loc),
    }
    if episode_nodes:
        data['episode'] = episode_nodes

    return json.dumps(data, ensure_ascii=False)


def _subscribe_buttons_html(settings, feed_url: str) -> str:
    """Inline subscribe links. RSS always shown; other platforms hidden
    until the operator adds a URL in config/podcast.yaml."""
    parts: list[str] = []
    if settings.apple_podcasts_url:
        parts.append(f"<a href='{escape(settings.apple_podcasts_url)}' rel='noopener' target='_blank'>Apple Podcasts</a>")
    if settings.spotify_url:
        parts.append(f"<a href='{escape(settings.spotify_url)}' rel='noopener' target='_blank'>Spotify</a>")
    if settings.youtube_url:
        parts.append(f"<a href='{escape(settings.youtube_url)}' rel='noopener' target='_blank'>YouTube</a>")
    parts.append(f"<a href='{escape(feed_url)}'>RSS</a>")
    return "<span class='dot'>&middot;</span>".join(parts)


def _arch_bars_svg(n: int = 30, width: int = 320, baseline: int = 78,
                   max_h: int = 70, min_h: int = 8) -> str:
    """Render the waveform-arch SVG used inside the banner. Bars get
    progressively taller toward the center then back down, evoking a
    podcast waveform shaped as an arch."""
    bars = []
    center = (n - 1) / 2
    for i in range(n):
        normalized = abs(i - center) / center
        height = min_h + (max_h - min_h) * (1 - normalized ** 1.4)
        x = (i + 0.5) * (width / n)
        y_top = baseline - height
        bars.append(f'<line x1="{x:.1f}" y1="{baseline}" x2="{x:.1f}" y2="{y_top:.1f}" />')
    return (
        f'<svg class="banner-arch" viewBox="0 0 {width} {baseline + 4}" '
        'aria-hidden="true" role="presentation">'
        '<g stroke="#BF8520" stroke-width="2.4" stroke-linecap="round" fill="none">'
        f'{"".join(bars)}'
        '</g>'
        '</svg>'
    )


def _shared_css() -> str:
    """Single source of truth for the dark editorial palette + Garamond
    typography. Used by both the landing page and the methodology page
    so they look like one site."""
    return (
        ":root{"
        # Unified midnight navy — same hex for body, sections, and cards.
        # Differentiation comes from borders (gold) only, not from
        # background variations.
        "--bg:#01040F;"
        "--bg-soft:#01040F;"
        "--bg-card:#01040F;"
        "--ink:#F4ECDC;"
        "--ink-soft:#C5BAA0;"
        "--ink-muted:#8E8470;"
        "--rule:rgba(217,162,74,.25);"
        "--rule-strong:rgba(217,162,74,.5);"
        "--gold:#D9A24A;"
        "--gold-soft:#BF8520;"
        "--gold-dark:#8C601A;"
        "}"
        "*{box-sizing:border-box}"
        "html,body{margin:0;padding:0}"
        "body{font-family:'EB Garamond','Garamond','Cormorant Garamond',Georgia,serif;"
        "background:var(--bg);color:var(--ink);line-height:1.65;"
        "font-size:21px;-webkit-font-smoothing:antialiased}"
        "a{color:var(--gold);text-decoration:none;border-bottom:1px solid transparent;"
        "transition:border-color .15s,color .15s,background .15s}"
        "a:hover{color:#EBC172;border-bottom-color:var(--gold)}"
        # Banner (shared)
        ".banner{background:var(--bg);padding:3.6rem 1.25rem 2.6rem;text-align:center;"
        "position:relative;overflow:hidden}"
        ".banner::before{content:'';position:absolute;inset:0;pointer-events:none;"
        "background:radial-gradient(circle at 50% 60%,rgba(217,162,74,.10) 0%,rgba(1,4,15,0) 60%)}"
        ".banner::after{content:'';position:absolute;inset:0;pointer-events:none;"
        "background:repeating-radial-gradient(circle at 50% 110%,transparent 0,transparent 80px,"
        "rgba(217,162,74,.04) 81px,rgba(217,162,74,.04) 82px)}"
        ".banner-inner{position:relative;z-index:1;max-width:760px;margin:0 auto}"
        ".banner-arch{display:block;width:min(360px,58vw);height:auto;margin:0 auto 1.2rem;opacity:.95}"
        ".banner-title{font-family:'EB Garamond',Garamond,Georgia,serif;font-weight:700;"
        "font-variant:small-caps;letter-spacing:.32em;color:var(--gold);"
        "font-size:clamp(2rem,5vw,3.2rem);margin:0;padding-left:.32em;line-height:1.1}"
        ".banner-rule{width:100px;height:1px;background:var(--gold);border:0;"
        "margin:1rem auto .65rem;opacity:.55}"
        ".banner-author{font-family:'EB Garamond',Garamond,Georgia,serif;font-variant:small-caps;"
        "letter-spacing:.32em;color:var(--gold);font-size:.95rem;margin:0;padding-left:.32em;opacity:.85}"
        ".banner-title a{color:var(--gold);border-bottom:none}"
        ".banner-title a:hover{color:#EBC172;border-bottom:none}"
        # Page nav
        ".pagenav{position:relative;z-index:1;text-align:center;padding:1rem 1rem 0;"
        "background:var(--bg);border-bottom:1px solid var(--rule)}"
        ".pagenav a{display:inline-block;margin:0 1rem;padding-bottom:1rem;"
        "font-variant:small-caps;letter-spacing:.18em;font-size:.92rem;color:var(--ink-soft)}"
        ".pagenav a:hover{color:var(--gold);border-bottom:1px solid var(--gold)}"
        ".pagenav a.active{color:var(--gold)}"
        # Footer (shared)
        "footer{margin-top:3.5rem;padding:1.6rem 1rem 1.8rem;border-top:1px solid var(--rule);"
        "text-align:center;color:var(--ink-muted);font-size:.95rem}"
        "footer .sep{margin:0 .5rem;color:var(--gold);opacity:.6}"
        "footer a{color:var(--gold)}"
    )


def _render_banner_html(settings, loc: dict) -> str:
    """Banner header reused on every page (locale-aware title + home link)."""
    home_href = _locale_path(loc) + '/' if _locale_path(loc) else '/'
    return (
        "<header class='banner'>"
        "<div class='banner-inner'>"
        f"{_arch_bars_svg()}"
        f"<h1 class='banner-title'><a href='{escape(home_href)}'>{escape(loc['title'])}</a></h1>"
        "<hr class='banner-rule' />"
        f"<p class='banner-author'>{escape(settings.podcast_author)}</p>"
        "</div>"
        "</header>"
    )


def _render_pagenav(active: str, loc: dict, feed_url: str) -> str:
    """Small navigation bar with locale-aware labels and cross-locale link."""
    def cls(name: str) -> str:
        return " class='active'" if name == active else ""
    home_href = _locale_path(loc) + '/' if _locale_path(loc) else '/'
    how_href = _locale_path(loc) + '/how-it-works.html' if _locale_path(loc) else '/how-it-works.html'
    return (
        "<nav class='pagenav'>"
        f"<a href='{escape(home_href)}'{cls('home')}>{escape(loc['nav_home'])}</a>"
        f"<a href='{escape(how_href)}'{cls('how')}>{escape(loc['nav_how'])}</a>"
        f"<a href='{escape(loc['nav_other_path'])}' class='other-locale'>{escape(loc['nav_other_label'])}</a>"
        f"<a href='{escape(feed_url)}'>{escape(loc['nav_rss'])}</a>"
        "</nav>"
    )


def _render_footer(settings, loc: dict, feed_url: str) -> str:
    how_href = _locale_path(loc) + '/how-it-works.html' if _locale_path(loc) else '/how-it-works.html'
    return (
        "<footer>"
        f"{escape(loc['footer_hosted_by'])} {escape(settings.podcast_author)}"
        f"<span class='sep'>&middot;</span><a href='{escape(feed_url)}'>{escape(loc['footer_rss'])}</a>"
        f"<span class='sep'>&middot;</span><a href='{escape(how_href)}'>{escape(loc['nav_how'])}</a>"
        "</footer>"
    )


def _render_head(settings, loc: dict, *, page_title: str, page_description: str,
                 canonical_subpath: str, extra_css: str = '') -> str:
    """Render the <head> for a localized page.

    canonical_subpath: path WITHIN the locale (e.g. '/' for the locale
    home, '/how-it-works.html' for the methodology page). The locale
    site_path is prepended automatically.
    """
    base = _base_url(settings)
    cover_url = _absolute(settings, settings.cover_image_path)
    cover_rel = settings.cover_image_path
    feed_url = _feed_url(settings, loc)
    keywords = (
        'AI podcast, artificial intelligence, generative AI, LLM, '
        'AI news, AI research, AI use cases, AI tools, weak signals, '
        'AI for business, daily AI briefing'
    )
    canonical = f"{base}{_locale_path(loc)}{canonical_subpath}"

    # hreflang alternates: emit one <link> per locale + x-default = English.
    alts: list[str] = []
    for code, other in LOCALES.items():
        other_path = f"/{other.get('site_path','').strip('/')}/" if other.get('site_path') else '/'
        # For the methodology page, suffix stays the same across locales.
        if canonical_subpath != '/' and not canonical_subpath.startswith('/episodes/'):
            other_path = other_path.rstrip('/') + canonical_subpath
        alts.append(
            f"<link rel='alternate' hreflang='{escape(code)}' href='{escape(base)}{escape(other_path)}'>"
        )
    # x-default points to English root version.
    default_loc = LOCALES[DEFAULT_LOCALE]
    default_path = f"/{default_loc.get('site_path','').strip('/')}/" if default_loc.get('site_path') else '/'
    if canonical_subpath != '/' and not canonical_subpath.startswith('/episodes/'):
        default_path = default_path.rstrip('/') + canonical_subpath
    alts.append(
        f"<link rel='alternate' hreflang='x-default' href='{escape(base)}{escape(default_path)}'>"
    )

    return (
        "<head>"
        "<meta charset='utf-8'>"
        "<meta name='viewport' content='width=device-width,initial-scale=1'>"
        f"<title>{escape(page_title)}</title>"
        f"<meta name='description' content='{escape(page_description)}'>"
        f"<meta name='keywords' content='{escape(keywords)}'>"
        f"<meta name='author' content='{escape(settings.podcast_author)}'>"
        "<meta name='robots' content='index,follow,max-image-preview:large'>"
        "<meta name='theme-color' content='#071028'>"
        f"<link rel='canonical' href='{escape(canonical)}'>"
        f"{''.join(alts)}"
        f"<link rel='alternate' type='application/rss+xml' title='{escape(loc['title'])} RSS' href='{escape(feed_url)}'>"
        f"<link rel='icon' type='image/png' href='{escape(_absolute(settings, cover_rel))}'>"
        f"<link rel='apple-touch-icon' href='{escape(_absolute(settings, cover_rel))}'>"
        "<meta property='og:type' content='website'>"
        f"<meta property='og:site_name' content='{escape(loc['title'])}'>"
        f"<meta property='og:title' content='{escape(page_title)}'>"
        f"<meta property='og:description' content='{escape(page_description)}'>"
        f"<meta property='og:url' content='{escape(canonical)}'>"
        f"<meta property='og:image' content='{escape(cover_url)}'>"
        f"<meta property='og:image:alt' content='{escape(loc['title'])} cover'>"
        f"<meta property='og:locale' content='{escape(loc['lang'])}'>"
        "<meta name='twitter:card' content='summary_large_image'>"
        f"<meta name='twitter:title' content='{escape(page_title)}'>"
        f"<meta name='twitter:description' content='{escape(page_description)}'>"
        f"<meta name='twitter:image' content='{escape(cover_url)}'>"
        "<link rel='preconnect' href='https://fonts.googleapis.com'>"
        "<link rel='preconnect' href='https://fonts.gstatic.com' crossorigin>"
        "<link rel='stylesheet' href='https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap'>"
        f"<style>{_shared_css()}{extra_css}</style>"
        "</head>"
    )


def _episode_card(ep: dict, base: str, loc: dict) -> str:
    episode_link = ep.get('episode_page_url') or f"{base}/episodes/{ep.get('slug', '')}/"
    pub_label = (ep.get('published_at') or '')[:10]
    duration = ''
    if ep.get('duration_seconds'):
        duration = f" &nbsp;&middot;&nbsp; {int(ep['duration_seconds']) // 60} {escape(loc['min_label'])}"
    return (
        f"<article class='card'>"
        f"<p class='card-meta'>{escape(pub_label)}{duration}</p>"
        f"<h3><a href='{escape(episode_link)}'>{escape(ep['title'])}</a></h3>"
        f"<p class='card-summary'>{escape(ep['summary'])}</p>"
        f"<p class='card-links'>"
        f"<a href='{escape(episode_link)}'>{escape(loc['transcript_link_label'])}</a> "
        f"<span class='dot'>&middot;</span> "
        f"<a href='{escape(ep['audio_url'])}'>{escape(loc['listen_label'])}</a> "
        f"<span class='dot'>&middot;</span> "
        f"<a href='{escape(ep['source_manifest_url'])}'>{escape(loc['sources_label'])}</a>"
        f"</p>"
        f"</article>"
    )


_HOME_EXTRA_CSS = (
    # Intro block (zone visible sous le banner) — flat unified bg
    ".intro{padding:2.8rem 1.25rem 2.4rem;text-align:center;"
    "border-bottom:1px solid var(--rule)}"
    ".intro-inner{max-width:720px;margin:0 auto}"
    ".intro .tagline{font-family:'EB Garamond',serif;font-style:italic;"
    "font-size:clamp(1.6rem,3.5vw,2.1rem);color:var(--ink);"
    "margin:0 0 .8rem;line-height:1.35;font-weight:500}"
    ".intro .description{color:var(--ink-soft);font-size:1.18rem;line-height:1.6;"
    "margin:0 auto 1.8rem;max-width:620px}"
    ".intro .tagline-note{font-size:.92rem;color:var(--gold);text-align:center;"
    "margin:0 0 1.8rem;font-variant:small-caps;letter-spacing:.28em;opacity:.85}"
    # Subscribe pills
    ".intro .subscribe{display:flex;flex-wrap:wrap;justify-content:center;"
    "gap:.65rem;margin:0 0 1.6rem}"
    ".intro .subscribe .label{display:none}"
    ".intro .subscribe a{display:inline-flex;align-items:center;padding:.7rem 1.4rem;"
    "border:1px solid var(--rule-strong);border-radius:999px;color:var(--gold);"
    "font-size:1.05rem;font-weight:500;letter-spacing:.02em;background:rgba(217,162,74,.04);"
    "border-bottom:1px solid var(--rule-strong)}"
    ".intro .subscribe a:hover{background:rgba(217,162,74,.12);"
    "color:#EBC172;border-color:var(--gold)}"
    ".intro .subscribe .dot{display:none}"
    ".intro .hiw-link{display:inline-block;margin:0;font-size:.95rem;"
    "font-variant:small-caps;letter-spacing:.22em;color:var(--ink-soft);"
    "padding:.5rem 1rem;border-bottom:1px solid var(--rule)}"
    ".intro .hiw-link:hover{color:var(--gold);border-bottom-color:var(--gold)}"
    # Six pillars block on home — flat unified bg, distinguished by border
    ".pillars-home{padding:2.6rem 1.25rem 2.4rem;border-bottom:1px solid var(--rule)}"
    ".pillars-home-inner{max-width:880px;margin:0 auto}"
    ".pillars-home h2{font-family:'EB Garamond',serif;font-weight:700;"
    "font-variant:small-caps;letter-spacing:.24em;color:var(--gold);"
    "font-size:1.05rem;text-align:center;margin:0 0 .4rem}"
    ".pillars-home .subhead{text-align:center;color:var(--ink-soft);"
    "font-style:italic;font-size:1.05rem;margin:0 0 1.8rem}"
    ".pillars-grid{display:grid;grid-template-columns:repeat(3,1fr);"
    "gap:1rem;margin:0 auto}"
    ".pillar-tile{padding:1.2rem 1.25rem;background:var(--bg-card);"
    "border:1px solid var(--rule);border-radius:4px;"
    "transition:border-color .2s,transform .2s}"
    ".pillar-tile:hover{border-color:var(--gold-soft);transform:translateY(-2px)}"
    ".pillar-tile .pillar-num{font-variant:small-caps;letter-spacing:.22em;"
    "font-size:.78rem;color:var(--gold);display:block;margin-bottom:.4rem;opacity:.9}"
    ".pillar-tile .pillar-name{font-family:'EB Garamond',serif;font-weight:700;"
    "color:var(--ink);font-size:1.2rem;display:block;margin-bottom:.5rem;line-height:1.2}"
    ".pillar-tile .pillar-desc{color:var(--ink-soft);font-size:.98rem;"
    "line-height:1.5;display:block}"
    # Page wrap
    ".wrap{max-width:760px;margin:0 auto;padding:2.8rem 1.25rem 3rem}"
    ".sect-head{font-family:'EB Garamond',serif;font-weight:700;font-variant:small-caps;"
    "letter-spacing:.24em;color:var(--gold);font-size:1.1rem;text-align:center;"
    "margin:0 0 1.8rem}"
    # Episode cards
    ".card{background:var(--bg-card);border:1px solid var(--rule);border-radius:4px;"
    "padding:1.6rem 1.8rem;margin:0 0 1.2rem;"
    "transition:border-color .2s,box-shadow .2s,transform .2s}"
    ".card:hover{border-color:var(--gold-soft);box-shadow:0 8px 28px rgba(0,0,0,.35);"
    "transform:translateY(-1px)}"
    ".card.empty{text-align:center;border-style:dashed;background:transparent}"
    ".card-meta{font-variant:small-caps;letter-spacing:.18em;font-size:.9rem;"
    "color:var(--gold);margin:0 0 .4rem;opacity:.9}"
    ".card h3{font-family:'EB Garamond',serif;font-weight:700;color:var(--ink);"
    "font-size:1.7rem;line-height:1.25;margin:0 0 .6rem}"
    ".card h3 a{color:var(--ink);border-bottom:none}"
    ".card h3 a:hover{color:var(--gold);border-bottom:none}"
    ".card-summary{margin:0 0 .9rem;color:var(--ink-soft);font-size:1.1rem;line-height:1.55}"
    ".card-links{margin:0;font-size:.98rem;color:var(--ink-muted)}"
    ".card-links a{color:var(--gold)}"
    ".card-links .dot{margin:0 .4rem;color:var(--gold);opacity:.55}"
    # Mobile
    "@media (max-width:780px){"
    ".pillars-grid{grid-template-columns:repeat(2,1fr)}"
    "}"
    "@media (max-width:560px){"
    ".intro{padding:2.2rem 1rem 1.8rem}"
    ".intro .tagline{font-size:1.45rem}"
    ".intro .description{font-size:1.08rem}"
    ".intro .subscribe a{font-size:.95rem;padding:.55rem 1.1rem}"
    ".pillars-home{padding:2rem 1rem 1.8rem}"
    ".pillars-grid{grid-template-columns:1fr}"
    ".wrap{padding:2.2rem 1rem 2rem}"
    ".card{padding:1.3rem 1.3rem}"
    ".card h3{font-size:1.4rem}"
    ".card-summary{font-size:1.02rem}"
    "}"
)


def _pillars_grid_html(loc: dict) -> str:
    tiles = []
    for num, name, desc in loc['pillars']:
        tiles.append(
            "<div class='pillar-tile'>"
            f"<span class='pillar-num'>{escape(num)}</span>"
            f"<span class='pillar-name'>{escape(name)}</span>"
            f"<span class='pillar-desc'>{escape(desc)}</span>"
            "</div>"
        )
    return f"<div class='pillars-grid'>{''.join(tiles)}</div>"


def _write_index(episodes: list[dict], locale: str = DEFAULT_LOCALE) -> None:
    settings = load_settings()
    loc = get_locale(locale)
    base = _base_url(settings)
    feed_url = _feed_url(settings, loc)
    how_href = _locale_path(loc) + '/how-it-works.html' if _locale_path(loc) else '/how-it-works.html'

    cards = [_episode_card(ep, base, loc) for ep in episodes]
    empty = (
        "<div class='card empty'>"
        f"<p class='card-meta'>{escape(loc['first_episode_meta'])}</p>"
        f"<h3>{escape(loc['first_episode_h'])}</h3>"
        f"<p class='card-summary'>{escape(loc['subscribe_invite'])}</p>"
        "</div>"
    )
    subscribe_html = _subscribe_buttons_html(settings, feed_url)
    json_ld = _json_ld(settings, episodes, loc)
    page_title = f"{loc['title']} — {loc['subtitle']}"

    head = _render_head(
        settings, loc,
        page_title=page_title,
        page_description=loc['description_short'],
        canonical_subpath='/',
        extra_css=_HOME_EXTRA_CSS,
    )

    html = (
        "<!doctype html>"
        f"<html lang='{escape(loc['lang'])}'>"
        + head
        + f"<script type='application/ld+json'>{json_ld}</script>"
        + "<body>"
        + _render_banner_html(settings, loc)
        + _render_pagenav('home', loc, feed_url)
        + "<section class='intro'>"
        + "<div class='intro-inner'>"
        + f"<p class='tagline'>{escape(loc['subtitle'])}</p>"
        + f"<p class='description'>{loc['intro_paragraph']}</p>"
        + f"<p class='tagline-note'>{loc['tagline_note']}</p>"
        + f"<div class='subscribe'>{subscribe_html}</div>"
        + f"<a class='hiw-link' href='{escape(how_href)}'>{escape(loc['how_link_label'])}</a>"
        + "</div>"
        + "</section>"
        + "<section class='pillars-home'>"
        + "<div class='pillars-home-inner'>"
        + f"<h2>{escape(loc['pillars_heading'])}</h2>"
        + f"<p class='subhead'>{escape(loc['pillars_subhead'])}</p>"
        + _pillars_grid_html(loc)
        + "</div>"
        + "</section>"
        + "<div class='wrap'>"
        + f"<h2 class='sect-head'>{escape(loc['latest_episodes'])}</h2>"
        + "<main>"
        + (''.join(cards) if cards else empty)
        + "</main>"
        + "</div>"
        + _render_footer(settings, loc, feed_url)
        + "</body></html>"
    )
    (_locale_dir(loc) / 'index.html').write_text(html, encoding='utf-8')


_HOW_EXTRA_CSS = (
    ".wrap{max-width:760px;margin:0 auto;padding:2.8rem 1.25rem 3rem}"
    ".page-lead{text-align:center;font-style:italic;color:var(--ink-soft);"
    "font-size:1.3rem;margin:0 0 2.6rem;line-height:1.5}"
    ".section{margin-bottom:2.8rem}"
    ".section .num{font-variant:small-caps;letter-spacing:.28em;font-size:.92rem;"
    "color:var(--gold);margin:0 0 .55rem;display:block}"
    ".section h2{font-family:'EB Garamond',serif;font-weight:700;color:var(--ink);"
    "font-size:1.85rem;margin:0 0 1.1rem;line-height:1.25}"
    ".section p{margin:0 0 1rem;color:var(--ink-soft);font-size:1.15rem;"
    "line-height:1.7}"
    ".section p strong{color:var(--ink);font-weight:600}"
    "table.tiers{width:100%;border-collapse:collapse;margin:1.1rem 0 .6rem;"
    "font-size:1.05rem;background:var(--bg-card);border:1px solid var(--rule)}"
    "table.tiers th,table.tiers td{padding:.85rem 1rem;text-align:left;"
    "border-bottom:1px solid var(--rule);vertical-align:top}"
    "table.tiers th{font-variant:small-caps;letter-spacing:.18em;color:var(--gold);"
    "font-weight:600;font-size:.88rem;background:var(--bg-soft)}"
    "table.tiers td.weight{color:var(--gold);font-variant:small-caps;letter-spacing:.1em;"
    "white-space:nowrap;font-weight:600}"
    "table.tiers td.examples{color:var(--ink-soft);font-size:1rem;font-style:italic}"
    "ul.exclusions{margin:0 0 1rem;padding-left:1.4rem;color:var(--ink-soft);"
    "font-size:1.15rem;line-height:1.65}"
    "ul.exclusions li{margin:.5rem 0}"
    ".pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));"
    "gap:1rem;margin:1.2rem 0}"
    ".pillars .pillar{padding:1.1rem 1.25rem;background:var(--bg-card);"
    "border:1px solid var(--rule);border-radius:4px;font-size:1.05rem;"
    "color:var(--ink-soft);line-height:1.5}"
    ".pillars .pillar strong{display:block;color:var(--gold);font-size:.95rem;"
    "font-variant:small-caps;letter-spacing:.16em;margin-bottom:.4rem}"
    ".author-card{padding:1.6rem 1.8rem;background:var(--bg-card);"
    "border:1px solid var(--rule);border-radius:4px;margin:1.1rem 0;"
    "display:flex;gap:1.6rem;align-items:flex-start}"
    ".author-card .avatar{position:relative;flex-shrink:0;width:112px;height:112px;"
    "border-radius:50%;overflow:hidden;border:1px solid var(--rule-strong);"
    "background:var(--bg-soft);display:flex;align-items:center;justify-content:center}"
    ".author-card .avatar img{position:absolute;inset:0;width:100%;height:100%;"
    "object-fit:cover;z-index:2}"
    ".author-card .avatar-fallback{font-family:'EB Garamond',serif;font-weight:700;"
    "font-size:2.6rem;color:var(--gold);font-variant:small-caps;letter-spacing:.05em;"
    "z-index:1}"
    ".author-card .author-text{flex:1;min-width:0}"
    ".author-card .name{font-family:'EB Garamond',serif;font-weight:700;color:var(--ink);"
    "font-size:1.4rem;margin:0 0 .3rem}"
    ".author-card .tag{font-variant:small-caps;letter-spacing:.18em;font-size:.88rem;"
    "color:var(--gold);margin:0 0 .9rem}"
    ".author-card .author-links{margin:.9rem 0 0;font-size:1rem;color:var(--ink-muted)}"
    ".author-card .author-links a{color:var(--gold)}"
    ".author-card .author-links .sep{margin:0 .55rem;color:var(--gold);opacity:.55}"
    ".section-rule{display:block;width:60px;height:1px;background:var(--gold-soft);"
    "border:0;margin:0 0 1.4rem;opacity:.5}"
    "@media (max-width:560px){"
    ".wrap{padding:2.2rem 1rem 2rem}"
    ".page-lead{font-size:1.15rem}"
    ".section h2{font-size:1.5rem}"
    ".section p{font-size:1.05rem}"
    "table.tiers{font-size:.95rem}"
    "table.tiers th,table.tiers td{padding:.6rem .65rem}"
    ".author-card{flex-direction:column;align-items:center;text-align:center;gap:1.1rem}"
    ".author-card .author-text{text-align:left}"
    "}"
)


def _write_how_it_works(locale: str = DEFAULT_LOCALE) -> None:
    settings = load_settings()
    loc = get_locale(locale)
    feed_url = _feed_url(settings, loc)

    head = _render_head(
        settings, loc,
        page_title=loc['how_page_title'],
        page_description=loc['how_page_desc'],
        canonical_subpath='/how-it-works.html',
        extra_css=_HOW_EXTRA_CSS,
    )

    th = loc['how_s02_th']
    rows = ''.join(
        f"<tr><td>{escape(t)}</td>"
        f"<td class='weight'>{escape(w)}</td>"
        f"<td class='examples'>{escape(ex)}</td>"
        f"<td>{escape(rat)}</td></tr>"
        for t, w, ex, rat in loc['how_s02_rows']
    )
    s03_items = ''.join(
        f"<li><strong>{escape(s)}</strong>{escape(rest)}</li>"
        for s, rest in loc['how_s03_items']
    )
    s04_items = ''.join(
        f"<li><strong>{escape(s)}</strong>{escape(rest)}</li>"
        for s, rest in loc['how_s04_items']
    )

    body = (
        _render_banner_html(settings, loc)
        + _render_pagenav('how', loc, feed_url)
        + "<div class='wrap'>"
        + f"<p class='page-lead'>{escape(loc['how_lead'])}</p>"
        # 01 — Structure
        + "<section class='section'>"
        + "<hr class='section-rule' />"
        + f"<span class='num'>{loc['how_s01_num']}</span>"
        + f"<h2>{escape(loc['how_s01_h'])}</h2>"
        + f"<p>{escape(loc['how_s01_p1'])}</p>"
        + f"<p><strong>{escape(loc['how_s01_p2_strong'])}</strong>{escape(loc['how_s01_p2'])}</p>"
        + "</section>"
        # 02 — Sources & weighting
        + "<section class='section'>"
        + "<hr class='section-rule' />"
        + f"<span class='num'>{loc['how_s02_num']}</span>"
        + f"<h2>{escape(loc['how_s02_h'])}</h2>"
        + f"<p><strong>{escape(loc['how_s02_p1_strong'])}</strong>{escape(loc['how_s02_p1'])}</p>"
        + "<table class='tiers'>"
        + f"<thead><tr><th>{escape(th[0])}</th><th>{escape(th[1])}</th><th>{escape(th[2])}</th><th>{escape(th[3])}</th></tr></thead>"
        + f"<tbody>{rows}</tbody>"
        + "</table>"
        + f"<p>{escape(loc['how_s02_p2'])}</p>"
        + "</section>"
        # 03 — Topics covered
        + "<section class='section'>"
        + "<hr class='section-rule' />"
        + f"<span class='num'>{loc['how_s03_num']}</span>"
        + f"<h2>{escape(loc['how_s03_h'])}</h2>"
        + f"<p>{escape(loc['how_s03_lead'])}</p>"
        + f"<ul class='exclusions'>{s03_items}</ul>"
        + "</section>"
        # 04 — Exclusions
        + "<section class='section'>"
        + "<hr class='section-rule' />"
        + f"<span class='num'>{loc['how_s04_num']}</span>"
        + f"<ul class='exclusions'>{s04_items}</ul>"
        + "</section>"
        # 05 — About the host
        + "<section class='section'>"
        + "<hr class='section-rule' />"
        + f"<span class='num'>{loc['how_s05_num']}</span>"
        + "<div class='author-card'>"
        + "<div class='avatar'>"
        + f"<img src='{escape(_absolute(settings, 'assets/david-perron.jpg'))}' alt='{escape(settings.podcast_author)}' "
          "onerror=\"this.style.display='none'\">"
        + "<span class='avatar-fallback'>DP</span>"
        + "</div>"
        + "<div class='author-text'>"
        + f"<p class='name'>{escape(settings.podcast_author)}</p>"
        + f"<p class='tag'>{loc['how_s05_tag']}</p>"
        + f"<p>{escape(loc['how_s05_bio'])}</p>"
        + "<p class='author-links'>"
          "<a href='https://www.linkedin.com/in/davidperron/' "
          "rel='noopener' target='_blank'>LinkedIn</a>"
          f"<span class='sep'>&middot;</span><a href='mailto:{escape(settings.podcast_email)}'>{escape(settings.podcast_email)}</a>"
          "</p>"
        + "</div>"
        + "</div>"
        + "</section>"
        # 06 — Feedback
        + "<section class='section'>"
        + "<hr class='section-rule' />"
        + f"<span class='num'>{loc['how_s06_num']}</span>"
        + f"<h2>{escape(loc['how_s06_h'])}</h2>"
        + f"<p>{loc['how_s06_p_template'].format(email=escape(settings.podcast_email))}</p>"
        + "</section>"
        + "</div>"
        + _render_footer(settings, loc, feed_url)
    )

    html = (
        "<!doctype html>"
        f"<html lang='{escape(loc['lang'])}'>"
        + head
        + "<body>"
        + body
        + "</body></html>"
    )
    (_locale_dir(loc) / 'how-it-works.html').write_text(html, encoding='utf-8')

# ── sitemap.xml & robots.txt ─────────────────────────────────────────────────

def _write_sitemap(episodes: list[dict]) -> None:
    settings = load_settings()
    base = _base_url(settings)

    if episodes:
        last_pub = max(ep['published_at'] for ep in episodes)
        lastmod = datetime.fromisoformat(last_pub).astimezone(timezone.utc).date().isoformat()
    else:
        lastmod = utcnow().date().isoformat()

    urls: list[tuple[str, str, str, str]] = []
    # One entry per locale: home, how-it-works, RSS feed
    for code in ALL_LOCALES:
        loc = get_locale(code)
        prefix = (loc.get('site_path', '').strip('/') + '/') if loc.get('site_path') else ''
        urls.append((prefix, 'daily', '1.0', lastmod))
        urls.append((prefix + 'how-it-works.html', 'monthly', '0.7', lastmod))
        urls.append((prefix + 'podcast-feed.xml', 'daily', '0.9', lastmod))
    # Per-episode transcript pages (EN only for now — FR pipeline will add later)
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
