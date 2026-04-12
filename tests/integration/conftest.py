"""Shared fixtures for integration tests.

Isolates DATA_DIR / DOCS_DIR / output dir under a tmp path so tests
don't pollute the real repo state, and pre-seeds env vars required by
settings.py (site URL, feed URL, etc.).
"""
from __future__ import annotations

import os
from pathlib import Path

import pytest


REQUIRED_ENV = {
    'SITE_BASE_URL': 'https://podcast.example.test',
    'RSS_FEED_URL': 'https://podcast.example.test/podcast-feed.xml',
    'PUBLIC_AUDIO_BASE_URL': 'https://audio.example.test',
    'LLM_BASE_URL': 'https://api.llm.example.test/v1',
    'LLM_EDITOR_MODEL': 'test-editor-model',
    'LLM_API_KEY': 'test-key',
    'CARTESIA_API_KEY': 'test-cartesia-key',
    'CARTESIA_VOICE_ID': 'test-voice-id',
    'R2_ENDPOINT': 'https://r2.example.test',
    'R2_ACCESS_KEY_ID': 'test-access',
    'R2_SECRET_ACCESS_KEY': 'test-secret',
    'NEWSAPI_API_KEY': 'test-newsapi',
}


@pytest.fixture
def isolated_dirs(tmp_path, monkeypatch):
    """Redirect DATA_DIR and DOCS_DIR to tmp paths, and chdir for output/."""
    data_dir = tmp_path / 'data'
    docs_dir = tmp_path / 'docs'
    data_dir.mkdir()
    docs_dir.mkdir()
    (tmp_path / 'output').mkdir()
    (data_dir / 'state').mkdir()
    (data_dir / 'metrics').mkdir()

    # Redirect all modules that captured DATA_DIR / DOCS_DIR at import time.
    import ai_press_review.settings as settings_mod
    import ai_press_review.publish.feed as feed_mod
    import ai_press_review.state as state_mod
    import ai_press_review.observability.metrics as metrics_mod

    monkeypatch.setattr(settings_mod, 'DATA_DIR', data_dir)
    monkeypatch.setattr(settings_mod, 'DOCS_DIR', docs_dir)
    monkeypatch.setattr(feed_mod, 'DOCS_DIR', docs_dir)
    monkeypatch.setattr(state_mod, 'DATA_DIR', data_dir)
    # state.py binds its path constants at import time — repoint them explicitly.
    monkeypatch.setattr(state_mod, 'USED_SOURCES_PATH', data_dir / 'state' / 'used_sources.json')
    monkeypatch.setattr(state_mod, 'EPISODE_HISTORY_PATH', data_dir / 'state' / 'episode_history.json')
    monkeypatch.setattr(state_mod, 'PENDING_DRAFT_PATH', data_dir / 'state' / 'pending_draft.json')
    monkeypatch.setattr(metrics_mod, 'METRICS_DIR', data_dir / 'metrics')
    monkeypatch.setattr(metrics_mod, 'RUNS_PATH', data_dir / 'metrics' / 'runs.jsonl')

    # Seed required env vars (some may already be set by CI — override safely).
    for key, value in REQUIRED_ENV.items():
        monkeypatch.setenv(key, value)

    # Run in the tmp directory so `output/` is local to the test.
    monkeypatch.chdir(tmp_path)

    return {
        'root': tmp_path,
        'data': data_dir,
        'docs': docs_dir,
        'metrics': data_dir / 'metrics' / 'runs.jsonl',
    }
