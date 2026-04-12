"""Tests for transcript generation (VTT + HTML)."""
from __future__ import annotations

from ai_press_review.publish.transcript import (
    _iso8601_duration,
    _split_paragraphs,
    _vtt_timestamp,
    estimate_paragraph_timings,
    render_transcript_html,
    render_vtt,
    write_transcript_artifacts,
)


def test_iso8601_duration():
    assert _iso8601_duration(0) == 'PT0S'
    assert _iso8601_duration(42) == 'PT42S'
    assert _iso8601_duration(125) == 'PT2M5S'
    assert _iso8601_duration(3723) == 'PT1H2M3S'


def test_vtt_timestamp_formats():
    assert _vtt_timestamp(0) == '00:00:00.000'
    assert _vtt_timestamp(1500) == '00:00:01.500'
    assert _vtt_timestamp(3_725_420) == '01:02:05.420'


def test_split_paragraphs_handles_double_newlines():
    script = "Para one.\n\nPara two.\n\nPara three."
    paras = _split_paragraphs(script)
    assert paras == ['Para one.', 'Para two.', 'Para three.']


def test_estimate_paragraph_timings_distributes_proportionally():
    paragraphs = [
        'short one.',  # 2 words
        'a much longer paragraph containing many more words here please.',  # 10 words
    ]
    timings = estimate_paragraph_timings(paragraphs, total_duration_s=60)
    assert len(timings) == 2
    assert timings[0][0] == 0
    assert timings[-1][1] == 60_000
    # First paragraph should cover proportionally less time.
    assert timings[0][1] < timings[1][1] - timings[1][0]


def test_estimate_paragraph_timings_handles_zero_duration():
    paragraphs = ['a', 'b']
    timings = estimate_paragraph_timings(paragraphs, total_duration_s=0)
    assert all(t == (0, 0) for t in timings)


def test_render_vtt_well_formed():
    paragraphs = ['Hello world.', 'Second cue.']
    timings = [(0, 1000), (1000, 2500)]
    out = render_vtt(paragraphs, timings)
    assert out.startswith('WEBVTT')
    assert '00:00:00.000 --> 00:00:01.000' in out
    assert '00:00:01.000 --> 00:00:02.500' in out
    assert 'Hello world.' in out


def test_render_transcript_html_contains_structural_elements():
    html = render_transcript_html(
        title='Test episode — Apr 12',
        slug='test-episode',
        summary='A short summary.',
        published_at='2026-04-12T07:00:00+00:00',
        duration_seconds=900,
        audio_url='https://cdn.example/ep.mp3',
        feed_url='https://site.example/feed.xml',
        site_base_url='https://site.example',
        cover_url='https://site.example/cover.png',
        author='David Perron',
        language='en',
        paragraphs=['First paragraph.', 'Second paragraph.'],
        timings=[(0, 450_000), (450_000, 900_000)],
        key_claims=[{'claim': 'A claim', 'source_url': 'https://s.example/'}],
        source_count=45,
        domain_count=30,
        grounding_coverage=0.93,
    )
    assert '<h1>Test episode — Apr 12</h1>' in html
    assert 'PodcastEpisode' in html  # JSON-LD
    assert 'PT15M0S' in html  # ISO duration
    assert 'https://cdn.example/ep.mp3' in html
    assert 'Key claims with sources' in html
    assert '93%' in html  # grounding coverage rendered
    assert '45' in html and '30' in html
    # Canonical URL
    assert "<link rel='canonical' href='https://site.example/episodes/test-episode/'>" in html
    # Per-paragraph anchors
    assert "id='t-1'" in html
    assert "id='t-2'" in html


def test_write_transcript_artifacts_creates_both_files(tmp_path):
    urls = write_transcript_artifacts(
        docs_dir=tmp_path,
        slug='ep-slug',
        script='Intro sentence.\n\nBody sentence.\n\nOutro sentence.',
        duration_seconds=120,
        episode_meta={
            'title': 'Ep title',
            'summary': 'sum',
            'published_at': '2026-04-12T07:00:00+00:00',
            'audio_url': 'https://a/x.mp3',
        },
        site_base_url='https://site/',
        feed_url='https://site/feed.xml',
        cover_url='https://site/cover.png',
        author='DP',
        language='en',
    )
    episode_dir = tmp_path / 'episodes' / 'ep-slug'
    assert (episode_dir / 'transcript.vtt').exists()
    assert (episode_dir / 'index.html').exists()
    assert urls['vtt_url'] == 'https://site/episodes/ep-slug/transcript.vtt'
    assert urls['html_url'] == 'https://site/episodes/ep-slug/'

    vtt = (episode_dir / 'transcript.vtt').read_text(encoding='utf-8')
    assert vtt.startswith('WEBVTT')
    # Three paragraphs → three cues
    assert vtt.count('-->') == 3
