from __future__ import annotations

import re
from html import escape
from pathlib import Path

from ..settings import load_settings
from ..utils import atomic_write_text

TEMPLATE_PATH = Path(__file__).parent / 'templates' / 'episode-brief-template.html'

_VOICE_NOTE_ENDINGS = [
    "The algorithm had opinions.",
    "Vos retours m'intéressent.",
]


def _render_summary_html(summary: str) -> str:
    """Render episode summary as HTML, separating the voice note from the intro.

    New format: summary contains '\n\n' between voice note and intro.
    Legacy format (space-concatenated): detect by known voice note endings.
    """
    summary = summary.strip()
    if not summary:
        return ''

    voice_note, intro = '', ''
    if '\n\n' in summary:
        voice_note, intro = summary.split('\n\n', 1)
    else:
        for ending in _VOICE_NOTE_ENDINGS:
            idx = summary.find(ending)
            if idx != -1:
                split_pos = idx + len(ending)
                voice_note = summary[:split_pos].strip()
                intro = summary[split_pos:].strip()
                break

    if voice_note and intro:
        return (
            f'<p class="episode-voice-note">{escape(voice_note)}</p>\n'
            f'      <p class="episode-summary">{escape(intro)}</p>'
        )
    return f'<p class="episode-summary">{escape(summary)}</p>'


def generate_episode_brief(episode_data: dict) -> str:
    """Render an episode brief HTML page from template + episode_data dict.

    Writes to settings.docs_output_dir / 'episodes/' so EN goes to docs/episodes/
    and FR goes to docs/fr/episodes/ (driven by APR_LOCALE via settings).

    Returns the path (relative to the locale's docs subdir) of the generated
    file — e.g. 'episodes/2026-04-20.html' for both EN and FR. The site_url
    already carries the locale prefix, so concatenating site_url + return value
    gives the correct absolute URL.
    """
    template = TEMPLATE_PATH.read_text(encoding='utf-8')
    html = template

    # Locale-derived fields. Before the 2026-04-18 fix, FR episode briefs
    # rendered with <html lang="en">, canonical URLs pointing to /episodes/
    # (not /fr/episodes/), inLanguage=en in JSON-LD, and the EN series name
    # in <title>. Google treated FR pages as duplicates of EN and skipped
    # them from the FR index. We now pull the locale-specific site base,
    # HTML lang attribute, and series title from Settings so a FR render
    # produces correct hreflang-consistent metadata.
    settings = load_settings()
    site_base = (settings.site_base_url or '').rstrip('/')
    html_lang = (settings.locale or 'en').strip().lower() or 'en'
    series_title = settings.podcast_title or 'AI Press Review'

    # ── Locale-aware labels ──
    is_fr = html_lang == 'fr'
    brief_button_label = 'Lire le brief complet' if is_fr else 'Read full brief'

    # ── Simple placeholders ──
    replacements = {
        '{{EPISODE_TITLE}}': escape(episode_data.get('title', '')),
        '{{EPISODE_DATE_ISO}}': escape(episode_data.get('date_iso', '')),
        '{{EPISODE_DATE_HUMAN}}': escape(episode_data.get('date_human', '')),
        '{{EPISODE_NUMBER}}': escape(str(episode_data.get('number', ''))),
        '{{EPISODE_DURATION}}': escape(episode_data.get('duration', '')),
        '{{EPISODE_DURATION_ISO}}': escape(episode_data.get('duration_iso', 'PT0S')),
        '{{EPISODE_AUDIO_URL}}': escape(episode_data.get('audio_url', '')),
        '{{EPISODE_SPOTIFY_URL}}': escape(episode_data.get('spotify_url', '')),
        '{{EPISODE_APPLE_URL}}': escape(episode_data.get('apple_url', '')),
        '{{EPISODE_SUMMARY}}': escape(episode_data.get('summary', '').replace('\n\n', ' ')),
        '{{EPISODE_SUMMARY_HTML}}': _render_summary_html(episode_data.get('summary', '')),
        '{{PREV_EPISODE_URL}}': escape(episode_data.get('prev_url', '')),
        '{{PREV_EPISODE_TITLE}}': escape(episode_data.get('prev_title', '')),
        '{{NEXT_EPISODE_URL}}': escape(episode_data.get('next_url', '')),
        '{{NEXT_EPISODE_TITLE}}': escape(episode_data.get('next_title', '')),
        '{{HTML_LANG}}': escape(html_lang),
        '{{SITE_BASE_URL}}': escape(site_base),
        '{{SERIES_TITLE}}': escape(series_title),
        '{{BRIEF_BUTTON_LABEL}}': escape(brief_button_label),
    }
    for placeholder, value in replacements.items():
        html = html.replace(placeholder, value)

    # ── Episode script (full transcript) ──
    raw_script = episode_data.get('script', '').strip()
    if raw_script:
        paras = [p.strip() for p in raw_script.split('\n\n') if p.strip()]
        duration_s = float(episode_data.get('duration_seconds', 0) or 0)
        total_words = sum(len(p.split()) for p in paras)
        wps = total_words / duration_s if duration_s > 0 and total_words > 0 else 0
        cumulative = 0
        para_tags = []
        for p in paras:
            start_s = round(cumulative / wps, 1) if wps > 0 else 0
            para_tags.append(f'<p class="script-para" data-start="{start_s}">{escape(p)}</p>')
            cumulative += len(p.split())
        script_html = '\n'.join(para_tags)
        empty_notice = ''
    else:
        script_html = ''
        empty_notice = (
            '<p class="script-empty">'
            + (
                'Le texte intégral de cet épisode n\'est pas encore disponible. '
                'Utilisez le lecteur audio ci-dessus pour écouter.'
                if is_fr else
                'The full transcript for this episode is not yet available. '
                'Use the audio player above to listen.'
            )
            + '</p>'
        )
    html = html.replace('{{EPISODE_SCRIPT_HTML}}', script_html)
    html = html.replace('<!-- EMPTY_NOTICE_PLACEHOLDER -->', empty_notice)

    # ── Conditional removal of optional platform links in compact listen bar ──
    # Each link has a preceding separator <span class="listen-sep">·</span>.
    # Remove both the separator and the link when the URL is empty.
    if not episode_data.get('spotify_url'):
        html = re.sub(
            r'<!-- SPOTIFY button:.*?-->\s*<span class="listen-sep">[^<]*</span>\s*<a[^>]*>.*?</a>',
            '',
            html,
            flags=re.DOTALL,
        )

    if not episode_data.get('apple_url'):
        html = re.sub(
            r'<!-- APPLE button:.*?-->\s*<span class="listen-sep">[^<]*</span>\s*<a[^>]*>.*?</a>',
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
    # `settings` was loaded at the top of the function for locale-aware
    # placeholder resolution — reuse it here rather than paying for a
    # second YAML/env parse.
    episodes_dir = settings.docs_output_dir / 'episodes'
    episodes_dir.mkdir(parents=True, exist_ok=True)
    out_path = episodes_dir / f'{date_iso}.html'
    atomic_write_text(out_path, html)

    return f'episodes/{date_iso}.html'
