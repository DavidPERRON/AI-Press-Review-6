from __future__ import annotations

import re
from html import escape
from pathlib import Path

from ..settings import DOCS_DIR

TEMPLATE_PATH = Path(__file__).parent / 'templates' / 'episode-brief-template.html'


def generate_episode_brief(episode_data: dict) -> str:
    """Render an episode brief HTML page from template + episode_data dict.

    Returns the path (relative to docs/) of the generated file.
    """
    template = TEMPLATE_PATH.read_text(encoding='utf-8')
    html = template

    # ── Simple placeholders ──
    replacements = {
        '{{EPISODE_TITLE}}': escape(episode_data.get('title', '')),
        '{{EPISODE_DATE_ISO}}': escape(episode_data.get('date_iso', '')),
        '{{EPISODE_DATE_HUMAN}}': escape(episode_data.get('date_human', '')),
        '{{EPISODE_NUMBER}}': escape(str(episode_data.get('number', ''))),
        '{{EPISODE_DURATION}}': escape(episode_data.get('duration', '')),
        '{{EPISODE_AUDIO_URL}}': escape(episode_data.get('audio_url', '')),
        '{{EPISODE_SPOTIFY_URL}}': escape(episode_data.get('spotify_url', '')),
        '{{EPISODE_APPLE_URL}}': escape(episode_data.get('apple_url', '')),
        '{{EPISODE_SUMMARY}}': escape(episode_data.get('summary', '')),
        '{{PREV_EPISODE_URL}}': escape(episode_data.get('prev_url', '')),
        '{{PREV_EPISODE_TITLE}}': escape(episode_data.get('prev_title', '')),
        '{{NEXT_EPISODE_URL}}': escape(episode_data.get('next_url', '')),
        '{{NEXT_EPISODE_TITLE}}': escape(episode_data.get('next_title', '')),
    }
    for placeholder, value in replacements.items():
        html = html.replace(placeholder, value)

    # ── Key claims ──
    claims_html = []
    for claim in episode_data.get('key_claims', []):
        claims_html.append(
            f'<div class="claim-item">'
            f'<p class="claim-text">{escape(claim["claim"])}</p>'
            f'<p class="claim-source">Source: <a href="{escape(claim["source_url"])}" '
            f'target="_blank" rel="noopener">{escape(claim["source_label"])}</a> '
            f'({escape(claim["source_domain"])})</p>'
            f'</div>'
        )
    html = html.replace(
        '<!-- Rendered by pipeline from KEY_CLAIMS JSON array -->\n'
        '        <!-- Example item structure (repeat for each claim):\n'
        '        <div class="claim-item">\n'
        '          <p class="claim-text">OpenAI released o4 with a reported 40% improvement on math benchmarks.</p>\n'
        '          <p class="claim-source">Source: <a href="https://openai.com/..." target="_blank" rel="noopener">OpenAI Blog</a> (openai.com)</p>\n'
        '        </div>\n'
        '        -->',
        '\n'.join(claims_html),
    )

    # ── Source manifest ──
    total_articles = sum(s.get('articles', 0) for s in episode_data.get('source_manifest', []))
    unique_domains = len({s.get('domain', '') for s in episode_data.get('source_manifest', [])})
    html = html.replace('{{SOURCE_COUNT}}', str(total_articles))
    html = html.replace('{{DOMAIN_COUNT}}', str(unique_domains))

    source_html = []
    for src in episode_data.get('source_manifest', []):
        weight = src.get('weight', 1)
        if weight >= 3:
            badge_class = 'w-high'
        elif weight >= 2:
            badge_class = 'w-med'
        else:
            badge_class = 'w-base'
        articles = src.get('articles', 0)
        plural = 's' if articles > 1 else ''
        source_html.append(
            f'<div class="source-row">'
            f'<span class="source-domain">{escape(src["domain"])}</span>'
            f'<span class="source-label">{escape(src.get("label", src["domain"]))}</span>'
            f'<span class="source-weight {badge_class}">\u00d7{weight}</span>'
            f'<span class="source-count">{articles} article{plural}</span>'
            f'</div>'
        )
    html = html.replace(
        '<!-- Rendered by pipeline from SOURCE_MANIFEST JSON array -->\n'
        '        <!-- Example row structure:\n'
        '        <div class="source-row">\n'
        '          <span class="source-domain">openai.com</span>\n'
        '          <span class="source-label">OpenAI Blog</span>\n'
        '          <span class="source-weight w-high">2.0\u00d7</span>\n'
        '          <span class="source-count">2 articles</span>\n'
        '        </div>\n'
        '        -->',
        '\n'.join(source_html),
    )

    # ── Conditional removal of optional buttons ──
    if not episode_data.get('spotify_url'):
        html = re.sub(
            r'<!-- SPOTIFY button:.*?-->\s*<a[^>]*>.*?Listen on Spotify.*?</a>',
            '',
            html,
            flags=re.DOTALL,
        )

    if not episode_data.get('apple_url'):
        html = re.sub(
            r'<!-- APPLE button:.*?-->\s*<a[^>]*>.*?Apple Podcasts.*?</a>',
            '',
            html,
            flags=re.DOTALL,
        )

    # ── Conditional removal of nav blocks ──
    if not episode_data.get('prev_url'):
        html = re.sub(
            r'<!-- Rendered only if PREV_EPISODE_URL is non-empty -->\s*<div class="nav-block">.*?</div>',
            '',
            html,
            flags=re.DOTALL,
        )

    if not episode_data.get('next_url'):
        html = re.sub(
            r'<!-- Rendered only if NEXT_EPISODE_URL is non-empty -->\s*<div class="nav-block right">.*?</div>',
            '',
            html,
            flags=re.DOTALL,
        )

    # ── Write output ──
    date_iso = episode_data.get('date_iso', 'unknown')
    episodes_dir = DOCS_DIR / 'episodes'
    episodes_dir.mkdir(parents=True, exist_ok=True)
    out_path = episodes_dir / f'{date_iso}.html'
    out_path.write_text(html, encoding='utf-8')

    return f'episodes/{date_iso}.html'
