"""End-to-end pipeline test with all external services mocked.

Validates that collect → editorial → tts → upload → publish flows through
cleanly, that the RSS feed and HTML landing page are regenerated, that
the episode history is updated, and that observability metrics are
persisted.
"""
from __future__ import annotations

import json
from unittest.mock import patch

import pytest

from ai_press_review.models import EpisodeDraft


# ── Fixture manifests / drafts returned by mocks ─────────────────────────────

SAMPLE_SCRIPT = (
    "Your Daily AI Press Review — April 12: Signal Day. "
    "Today we look at three stories that matter. OpenAI shipped a new model "
    "that outperforms prior systems on reasoning benchmarks. A major European "
    "bank deployed an internal agent cutting onboarding review time by about "
    "forty percent. And a quiet research result from a university lab shows "
    "that smaller models can match larger ones when trained on cleaner data. "
    "This podcast has a daily production cost. If you'd like to support me, "
    "my latest book, The Last Heaven, is available on Amazon and at "
    "ashcroftedition.com — link on the podcast page. Thank you. "
    "Tomorrow: why context windows are finally catching up."
)


def _fake_manifest(run_date: str) -> dict:
    return {
        'run_date': run_date,
        'source_count': 45,
        'sources': [
            {'title': f'Sample article {i}', 'url': f'https://example.com/a{i}',
             'domain': 'example.com', 'content_text': 'content', 'relevance_score': 5.0}
            for i in range(45)
        ],
        'generated_at': '2026-04-12T06:00:00+00:00',
    }


def _fake_draft() -> EpisodeDraft:
    return EpisodeDraft(
        episode_title='OpenAI ships o4: what enterprise should know — Apr 12',
        episode_summary='Today: OpenAI ships o4, a European bank cuts onboarding time with an agent, and a small-model result from academia.',
        opening_news_title='OpenAI ships o4',
        script=SAMPLE_SCRIPT,
        tomorrow_concept='why context windows are finally catching up',
        highlights_label='Signal Day',
    )


def _fake_synthesize(script, output_path, local_preview=False):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write a minimal fake MP3 (just bytes — we don't decode it).
    output_path.write_bytes(b'\xff\xfb\x90\x00' + b'\x00' * 1024)
    return {
        'chunk_count': 2,
        'duration_seconds': 900,
        'bytes': output_path.stat().st_size,
    }


def _fake_upload(path, remote_key, local_preview=False):
    return f'https://audio.example.test/{remote_key}'


# ── Tests ────────────────────────────────────────────────────────────────────

def test_pipeline_publishes_episode_end_to_end(isolated_dirs):
    from ai_press_review import pipeline as pipeline_mod

    with patch.object(pipeline_mod, 'collect_sources', side_effect=lambda **kw: _fake_manifest(kw['run_date'])), \
         patch.object(pipeline_mod, 'generate_episode_script', return_value=_fake_draft()), \
         patch.object(pipeline_mod, 'synthesize_script', side_effect=_fake_synthesize), \
         patch.object(pipeline_mod, 'upload_file', side_effect=_fake_upload):

        result = pipeline_mod.run_pipeline(
            run_date='2026-04-12',
            render_audio=True,
            upload_audio=True,
            publish_feed=True,
        )

    assert result['published'] is True
    assert result['rendered_audio'] is True
    assert result['uploaded_audio'] is True
    assert result['script_words'] > 50
    assert 'audio_url' in result

    # RSS feed and landing page regenerated with the episode.
    feed_xml = (isolated_dirs['docs'] / 'podcast-feed.xml').read_text(encoding='utf-8')
    assert '<item>' in feed_xml
    assert 'OpenAI ships o4' in feed_xml
    assert 'rel="self"' in feed_xml  # atom:self from SEO patch
    assert '<itunes:type>episodic</itunes:type>' in feed_xml

    index_html = (isolated_dirs['docs'] / 'index.html').read_text(encoding='utf-8')
    assert 'OpenAI ships o4' in index_html
    assert 'application/ld+json' in index_html

    # Episode history and sitemap persisted.
    history = json.loads((isolated_dirs['data'] / 'state' / 'episode_history.json').read_text())
    assert len(history['episodes']) == 1
    assert history['episodes'][0]['title'].startswith('OpenAI ships o4')

    sitemap = (isolated_dirs['docs'] / 'sitemap.xml').read_text(encoding='utf-8')
    assert 'https://podcast.example.test/' in sitemap

    # Observability metrics recorded for each phase + run summary.
    metrics_path = isolated_dirs['metrics']
    assert metrics_path.exists(), 'metrics runs.jsonl was not created'
    events = [json.loads(line) for line in metrics_path.read_text().splitlines() if line.strip()]
    phases = {e['phase'] for e in events if e.get('type') == 'phase'}
    assert {'collect', 'editorial', 'tts', 'upload', 'publish'}.issubset(phases)
    runs = [e for e in events if e.get('type') == 'run']
    assert len(runs) == 1
    assert runs[0]['published'] is True


def test_pipeline_without_publish_skips_feed_regeneration(isolated_dirs):
    from ai_press_review import pipeline as pipeline_mod

    with patch.object(pipeline_mod, 'collect_sources', side_effect=lambda **kw: _fake_manifest(kw['run_date'])), \
         patch.object(pipeline_mod, 'generate_episode_script', return_value=_fake_draft()), \
         patch.object(pipeline_mod, 'synthesize_script', side_effect=_fake_synthesize), \
         patch.object(pipeline_mod, 'upload_file', side_effect=_fake_upload):

        result = pipeline_mod.run_pipeline(
            run_date='2026-04-12',
            render_audio=True,
            upload_audio=False,
            publish_feed=False,
        )

    assert result['published'] is False
    assert result['uploaded_audio'] is False
    assert not (isolated_dirs['docs'] / 'podcast-feed.xml').exists()


def test_pipeline_raises_when_publish_requested_without_upload(isolated_dirs):
    from ai_press_review import pipeline as pipeline_mod

    with patch.object(pipeline_mod, 'collect_sources', side_effect=lambda **kw: _fake_manifest(kw['run_date'])), \
         patch.object(pipeline_mod, 'generate_episode_script', return_value=_fake_draft()), \
         patch.object(pipeline_mod, 'synthesize_script', side_effect=_fake_synthesize):

        with pytest.raises(ValueError, match='upload is required'):
            pipeline_mod.run_pipeline(
                run_date='2026-04-12',
                render_audio=True,
                upload_audio=False,
                publish_feed=True,
            )
