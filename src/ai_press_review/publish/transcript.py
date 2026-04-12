"""Transcript + per-episode HTML page generation.

Produces two artifacts per published episode:

- `docs/episodes/{slug}/transcript.vtt` — WebVTT with paragraph-level
  timestamps. Without word-level alignment from Cartesia (which would
  require the SSE endpoint), we estimate each paragraph's duration from
  its word share of the total audio. This is coarse but accurate enough
  for podcast apps to display a scrolling transcript in sync with
  playback.
- `docs/episodes/{slug}/index.html` — a standalone, SEO-friendly HTML
  page with the full transcript, per-paragraph anchors, OG/Twitter/JSON-LD
  `PodcastEpisode` schema, and a link back to the RSS feed. Indexable
  by Google — this is where per-episode SEO actually comes from.
"""
from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path
from xml.sax.saxutils import escape


def _split_paragraphs(script: str) -> list[str]:
    parts = [p.strip() for p in re.split(r"\n{2,}", script) if p.strip()]
    if not parts:
        parts = [p.strip() for p in script.split('\n') if p.strip()]
    return parts


def _vtt_timestamp(ms: int) -> str:
    h = ms // 3_600_000
    m = (ms % 3_600_000) // 60_000
    s = (ms % 60_000) // 1000
    ms_rem = ms % 1000
    return f"{h:02d}:{m:02d}:{s:02d}.{ms_rem:03d}"


def estimate_paragraph_timings(paragraphs: list[str], total_duration_s: int) -> list[tuple[int, int]]:
    """Return [(start_ms, end_ms), ...] aligned to each paragraph,
    distributed proportionally to word count. Always covers [0, total]."""
    if not paragraphs or total_duration_s <= 0:
        return [(0, (total_duration_s or 0) * 1000) for _ in paragraphs]

    word_counts = [max(len(p.split()), 1) for p in paragraphs]
    total_words = sum(word_counts)
    total_ms = total_duration_s * 1000

    timings: list[tuple[int, int]] = []
    cursor = 0
    for idx, wc in enumerate(word_counts):
        if idx == len(word_counts) - 1:
            timings.append((cursor, total_ms))
        else:
            span = int(total_ms * wc / total_words)
            timings.append((cursor, cursor + span))
            cursor += span
    return timings


def render_vtt(paragraphs: list[str], timings: list[tuple[int, int]]) -> str:
    lines = ['WEBVTT', '']
    for idx, (para, (start_ms, end_ms)) in enumerate(zip(paragraphs, timings), start=1):
        lines.append(f'{idx}')
        lines.append(f'{_vtt_timestamp(start_ms)} --> {_vtt_timestamp(end_ms)}')
        # Collapse internal newlines — VTT cues should be self-contained.
        lines.append(para.replace('\n', ' '))
        lines.append('')
    return '\n'.join(lines)


def render_transcript_html(
    *,
    title: str,
    slug: str,
    summary: str,
    published_at: str,
    duration_seconds: int,
    audio_url: str,
    feed_url: str,
    site_base_url: str,
    cover_url: str,
    author: str,
    language: str,
    paragraphs: list[str],
    timings: list[tuple[int, int]],
    key_claims: list[dict] | None = None,
    source_count: int = 0,
    domain_count: int = 0,
    grounding_coverage: float | None = None,
) -> str:
    """Full standalone HTML page for one episode with transcript."""
    episode_url = f"{site_base_url.rstrip('/')}/episodes/{slug}/"
    iso_duration = _iso8601_duration(duration_seconds)

    json_ld = json.dumps({
        '@context': 'https://schema.org',
        '@type': 'PodcastEpisode',
        'name': title,
        'description': summary,
        'datePublished': published_at,
        'url': episode_url,
        'duration': iso_duration,
        'inLanguage': language,
        'author': {'@type': 'Person', 'name': author},
        'image': cover_url,
        'associatedMedia': {
            '@type': 'MediaObject',
            'contentUrl': audio_url,
            'encodingFormat': 'audio/mpeg',
        },
        'partOfSeries': {
            '@type': 'PodcastSeries',
            'name': 'AI Press Review',
            'url': site_base_url,
            'webFeed': feed_url,
        },
    }, ensure_ascii=False)

    transcript_blocks = []
    for idx, (para, (start_ms, _end)) in enumerate(zip(paragraphs, timings), start=1):
        ts = _vtt_timestamp(start_ms)[:-4]  # HH:MM:SS
        anchor = f"t-{idx}"
        transcript_blocks.append(
            f"<p id='{anchor}'><a class='tstamp' href='#{anchor}' aria-label='jump to {ts}'>{ts}</a> {escape(para)}</p>"
        )

    claims_block = ''
    if key_claims:
        items = []
        for claim in key_claims[:25]:
            text = escape(claim.get('claim', ''))
            src = escape(claim.get('source_url', ''))
            if text and src:
                items.append(f"<li>{text} <a class='src' href='{src}' rel='nofollow'>source</a></li>")
        if items:
            claims_block = (
                "<section class='claims'><h2>Key claims with sources</h2>"
                f"<ul>{''.join(items)}</ul></section>"
            )

    coverage_line = ''
    if grounding_coverage is not None:
        pct = round(grounding_coverage * 100)
        coverage_line = (
            f"<p class='coverage'>Grounding coverage: <strong>{pct}%</strong> of cited "
            f"claims verified against the source manifest."
            f" Sources: <strong>{source_count}</strong> articles from <strong>{domain_count}</strong> domains.</p>"
        )

    return (
        "<!doctype html>"
        f"<html lang='{escape(language)}'>"
        "<head>"
        "<meta charset='utf-8'>"
        "<meta name='viewport' content='width=device-width,initial-scale=1'>"
        f"<title>{escape(title)} — AI Press Review</title>"
        f"<meta name='description' content='{escape(summary)}'>"
        "<meta name='robots' content='index,follow,max-image-preview:large'>"
        f"<link rel='canonical' href='{escape(episode_url)}'>"
        f"<link rel='alternate' type='application/rss+xml' title='AI Press Review RSS' href='{escape(feed_url)}'>"
        f"<link rel='icon' type='image/png' href='{escape(site_base_url)}/assets/podcast-cover.png'>"
        # Open Graph / Twitter
        "<meta property='og:type' content='article'>"
        f"<meta property='og:title' content='{escape(title)}'>"
        f"<meta property='og:description' content='{escape(summary)}'>"
        f"<meta property='og:url' content='{escape(episode_url)}'>"
        f"<meta property='og:image' content='{escape(cover_url)}'>"
        "<meta name='twitter:card' content='summary_large_image'>"
        f"<meta name='twitter:title' content='{escape(title)}'>"
        f"<meta name='twitter:description' content='{escape(summary)}'>"
        f"<meta name='twitter:image' content='{escape(cover_url)}'>"
        f"<script type='application/ld+json'>{json_ld}</script>"
        "<style>"
        "body{font-family:-apple-system,BlinkMacSystemFont,sans-serif;max-width:760px;"
        "margin:2rem auto;padding:0 1rem;line-height:1.65;color:#111}"
        "header{margin-bottom:1.5rem}"
        "h1{margin-bottom:.25rem;font-size:1.6rem}"
        ".meta{color:#555;font-size:.9rem}"
        "audio{width:100%;margin:1.25rem 0}"
        ".transcript p{margin:.9rem 0}"
        ".tstamp{color:#888;font-variant-numeric:tabular-nums;font-size:.85rem;"
        "margin-right:.35rem;text-decoration:none}"
        ".tstamp:hover{color:#0b5fff}"
        ".claims{margin-top:2rem;padding-top:1rem;border-top:1px solid #ddd}"
        ".claims li{margin:.4rem 0}"
        ".claims a.src{font-size:.85rem;color:#0b5fff;margin-left:.35rem}"
        ".coverage{color:#444;font-size:.9rem}"
        "nav.return{margin-top:2rem;font-size:.9rem}"
        "a{color:#0b5fff}"
        "</style>"
        "</head>"
        "<body>"
        "<header>"
        f"<p class='meta'><a href='{escape(site_base_url)}/'>AI Press Review</a> "
        f"· {escape(published_at[:10])} · {duration_seconds // 60} min</p>"
        f"<h1>{escape(title)}</h1>"
        f"<p class='summary'>{escape(summary)}</p>"
        f"{coverage_line}"
        f"<audio controls preload='metadata' src='{escape(audio_url)}'></audio>"
        "</header>"
        "<section class='transcript'>"
        "<h2>Transcript</h2>"
        f"{''.join(transcript_blocks)}"
        "</section>"
        f"{claims_block}"
        "<nav class='return'>"
        f"<a href='{escape(site_base_url)}/'>← All episodes</a> · "
        f"<a href='{escape(feed_url)}'>RSS feed</a>"
        "</nav>"
        "</body></html>"
    )


def _iso8601_duration(seconds: int) -> str:
    """Render seconds as ISO 8601 duration (PT15M30S)."""
    seconds = max(int(seconds or 0), 0)
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    parts = ['PT']
    if h:
        parts.append(f'{h}H')
    if m or h:
        parts.append(f'{m}M')
    parts.append(f'{s}S')
    return ''.join(parts)


def write_transcript_artifacts(
    *,
    docs_dir: Path,
    slug: str,
    script: str,
    duration_seconds: int,
    episode_meta: dict,
    site_base_url: str,
    feed_url: str,
    cover_url: str,
    author: str,
    language: str,
    key_claims: list[dict] | None = None,
    grounding_coverage: float | None = None,
    source_count: int = 0,
    domain_count: int = 0,
) -> dict:
    """Write both VTT and HTML artifacts for an episode. Returns the
    public URLs so the RSS generator can reference them."""
    episode_dir = docs_dir / 'episodes' / slug
    episode_dir.mkdir(parents=True, exist_ok=True)

    paragraphs = _split_paragraphs(script)
    timings = estimate_paragraph_timings(paragraphs, duration_seconds)

    vtt = render_vtt(paragraphs, timings)
    (episode_dir / 'transcript.vtt').write_text(vtt, encoding='utf-8')

    html = render_transcript_html(
        title=episode_meta['title'],
        slug=slug,
        summary=episode_meta.get('summary', ''),
        published_at=episode_meta.get('published_at', ''),
        duration_seconds=duration_seconds,
        audio_url=episode_meta.get('audio_url', ''),
        feed_url=feed_url,
        site_base_url=site_base_url,
        cover_url=cover_url,
        author=author,
        language=language,
        paragraphs=paragraphs,
        timings=timings,
        key_claims=key_claims,
        source_count=source_count,
        domain_count=domain_count,
        grounding_coverage=grounding_coverage,
    )
    (episode_dir / 'index.html').write_text(html, encoding='utf-8')

    base = site_base_url.rstrip('/')
    return {
        'vtt_url': f'{base}/episodes/{slug}/transcript.vtt',
        'html_url': f'{base}/episodes/{slug}/',
    }
