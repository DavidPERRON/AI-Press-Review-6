"""Settings tests — per-locale LLM model resolution.

Context: the daily/weekly pipeline runs the same Python code for both EN and
FR jobs. Until 2026-04-16 it used a single LLM_EDITOR_MODEL shared across
locales. This file verifies the new per-locale override mechanism added in
settings._apply_locale():

    LLM_EDITOR_MODEL_EN  → wins for EN runs
    LLM_EDITOR_MODEL_FR  → wins for FR runs
    LLM_EDITOR_MODEL     → falls back to this when the per-locale var is unset

Same logic for LLM_FALLBACK_MODEL_* and LLM_EMERGENCY_MODEL_*.

The motivation is editorial register: FR uses Mistral Large 2411 (French-native,
sophisticated register), EN uses Claude Sonnet 4.5 (journalism tone). Both
through OpenRouter with one shared API key — the per-locale split happens
purely client-side via env-var resolution.

Backward compatibility is mandatory: pipelines that only set the generic
LLM_EDITOR_MODEL must keep working unchanged. That's the most important
property to guard against — the production pipeline depends on it.
"""

from __future__ import annotations

import pytest

from ai_press_review.settings import load_settings


# ─── Per-locale override beats the generic var ────────────────────────────────

def test_per_locale_editor_model_overrides_generic_for_en(monkeypatch):
    monkeypatch.setenv('LLM_EDITOR_MODEL', 'generic-editor')
    monkeypatch.setenv('LLM_EDITOR_MODEL_EN', 'anthropic/claude-sonnet-4.5')
    monkeypatch.setenv('LLM_EDITOR_MODEL_FR', 'mistralai/mistral-large-2411')
    settings = load_settings(locale='en')
    assert settings.llm_editor_model == 'anthropic/claude-sonnet-4.5'


def test_per_locale_editor_model_overrides_generic_for_fr(monkeypatch):
    monkeypatch.setenv('LLM_EDITOR_MODEL', 'generic-editor')
    monkeypatch.setenv('LLM_EDITOR_MODEL_EN', 'anthropic/claude-sonnet-4.5')
    monkeypatch.setenv('LLM_EDITOR_MODEL_FR', 'mistralai/mistral-large-2411')
    settings = load_settings(locale='fr')
    assert settings.llm_editor_model == 'mistralai/mistral-large-2411'


def test_per_locale_fallback_model_overrides_generic(monkeypatch):
    monkeypatch.setenv('LLM_FALLBACK_MODEL', 'generic-fallback')
    monkeypatch.setenv('LLM_FALLBACK_MODEL_EN', 'google/gemini-2.5-pro')
    settings = load_settings(locale='en')
    assert settings.llm_fallback_model == 'google/gemini-2.5-pro'


def test_per_locale_emergency_model_overrides_generic(monkeypatch):
    monkeypatch.setenv('LLM_EMERGENCY_MODEL', 'generic-emergency')
    monkeypatch.setenv('LLM_EMERGENCY_MODEL_FR', 'openai/gpt-4o-mini')
    settings = load_settings(locale='fr')
    assert settings.llm_emergency_model == 'openai/gpt-4o-mini'


# ─── Backward compatibility: generic-only setup still works ──────────────────

def test_falls_back_to_generic_when_per_locale_unset(monkeypatch):
    """The most critical property: a pipeline that only sets the generic
    LLM_EDITOR_MODEL must continue working with both EN and FR jobs."""
    monkeypatch.setenv('LLM_EDITOR_MODEL', 'shared-editor')
    monkeypatch.delenv('LLM_EDITOR_MODEL_EN', raising=False)
    monkeypatch.delenv('LLM_EDITOR_MODEL_FR', raising=False)
    en_settings = load_settings(locale='en')
    fr_settings = load_settings(locale='fr')
    assert en_settings.llm_editor_model == 'shared-editor'
    assert fr_settings.llm_editor_model == 'shared-editor'


def test_falls_back_per_field_independently(monkeypatch):
    """Mixed config: per-locale editor set, but per-locale fallback not.
    Each tier resolves independently; one missing override shouldn't blank
    out the others."""
    monkeypatch.setenv('LLM_EDITOR_MODEL', 'generic-editor')
    monkeypatch.setenv('LLM_FALLBACK_MODEL', 'generic-fallback')
    monkeypatch.setenv('LLM_EDITOR_MODEL_EN', 'anthropic/claude-sonnet-4.5')
    monkeypatch.delenv('LLM_FALLBACK_MODEL_EN', raising=False)
    settings = load_settings(locale='en')
    assert settings.llm_editor_model == 'anthropic/claude-sonnet-4.5'
    assert settings.llm_fallback_model == 'generic-fallback'


def test_empty_per_locale_var_falls_through_to_generic(monkeypatch):
    """An empty string (e.g. unset GitHub Variable interpolated as '') should
    behave the same as missing — the generic value wins. This matches GitHub
    Actions behavior where ${{ vars.UNDEFINED }} expands to empty string."""
    monkeypatch.setenv('LLM_EDITOR_MODEL', 'generic-editor')
    monkeypatch.setenv('LLM_EDITOR_MODEL_EN', '')
    settings = load_settings(locale='en')
    assert settings.llm_editor_model == 'generic-editor'


# ─── Locale isolation: setting EN doesn't pollute FR ─────────────────────────

def test_setting_en_does_not_affect_fr(monkeypatch):
    monkeypatch.setenv('LLM_EDITOR_MODEL', 'generic-editor')
    monkeypatch.setenv('LLM_EDITOR_MODEL_EN', 'anthropic/claude-sonnet-4.5')
    monkeypatch.delenv('LLM_EDITOR_MODEL_FR', raising=False)
    fr_settings = load_settings(locale='fr')
    # FR sees no FR-specific override, so it gets the generic — NOT the EN one.
    assert fr_settings.llm_editor_model == 'generic-editor'


def test_setting_fr_does_not_affect_en(monkeypatch):
    monkeypatch.setenv('LLM_EDITOR_MODEL', 'generic-editor')
    monkeypatch.setenv('LLM_EDITOR_MODEL_FR', 'mistralai/mistral-large-2411')
    monkeypatch.delenv('LLM_EDITOR_MODEL_EN', raising=False)
    en_settings = load_settings(locale='en')
    assert en_settings.llm_editor_model == 'generic-editor'


# ─── Locale resolved from APR_LOCALE env (matrix workflow path) ──────────────

def test_apr_locale_env_var_drives_resolution(monkeypatch):
    """The matrix workflow sets APR_LOCALE once per job. Downstream calls to
    load_settings() with locale=None must read that env to pick the right
    per-locale model — otherwise the cascade would silently use the generic
    one even when per-locale vars are configured."""
    monkeypatch.setenv('APR_LOCALE', 'fr')
    monkeypatch.setenv('LLM_EDITOR_MODEL', 'generic-editor')
    monkeypatch.setenv('LLM_EDITOR_MODEL_FR', 'mistralai/mistral-large-2411')
    settings = load_settings()  # no explicit locale arg
    assert settings.llm_editor_model == 'mistralai/mistral-large-2411'


def test_no_locale_means_generic_only(monkeypatch):
    """When neither APR_LOCALE nor an explicit locale is passed, _apply_locale
    is never called and the generic vars are used as-is. This is the legacy
    single-locale code path."""
    monkeypatch.delenv('APR_LOCALE', raising=False)
    monkeypatch.setenv('LLM_EDITOR_MODEL', 'generic-editor')
    monkeypatch.setenv('LLM_EDITOR_MODEL_EN', 'should-be-ignored')
    settings = load_settings()  # no locale, no APR_LOCALE
    assert settings.llm_editor_model == 'generic-editor'


# ─── Three-tier sanity: all three tiers work together ────────────────────────

def test_all_three_tiers_resolve_per_locale(monkeypatch):
    """Realistic FR config: editor + fallback + emergency all locale-specific."""
    monkeypatch.setenv('LLM_EDITOR_MODEL', 'generic-editor')
    monkeypatch.setenv('LLM_FALLBACK_MODEL', 'generic-fallback')
    monkeypatch.setenv('LLM_EMERGENCY_MODEL', 'generic-emergency')
    monkeypatch.setenv('LLM_EDITOR_MODEL_FR', 'mistralai/mistral-large-2411')
    monkeypatch.setenv('LLM_FALLBACK_MODEL_FR', 'google/gemini-2.5-pro')
    monkeypatch.setenv('LLM_EMERGENCY_MODEL_FR', 'openai/gpt-4o')
    settings = load_settings(locale='fr')
    assert settings.llm_editor_model == 'mistralai/mistral-large-2411'
    assert settings.llm_fallback_model == 'google/gemini-2.5-pro'
    assert settings.llm_emergency_model == 'openai/gpt-4o'


def test_realistic_en_config_resolves(monkeypatch):
    """Realistic EN config: Claude Sonnet 4.5 editor, Gemini 2.5 Pro fallback,
    no emergency tier."""
    monkeypatch.setenv('LLM_EDITOR_MODEL_EN', 'anthropic/claude-sonnet-4.5')
    monkeypatch.setenv('LLM_FALLBACK_MODEL_EN', 'google/gemini-2.5-pro')
    monkeypatch.delenv('LLM_EMERGENCY_MODEL_EN', raising=False)
    monkeypatch.delenv('LLM_EMERGENCY_MODEL', raising=False)
    settings = load_settings(locale='en')
    assert settings.llm_editor_model == 'anthropic/claude-sonnet-4.5'
    assert settings.llm_fallback_model == 'google/gemini-2.5-pro'
    assert settings.llm_emergency_model == ''  # no emergency configured


# ─── Other locale-dependent fields aren't broken by the new resolution ───────

def test_per_locale_resolution_does_not_break_other_locale_fields(monkeypatch):
    """Smoke test: adding the model resolution block to _apply_locale must
    not regress existing locale overrides like prompt_file, docs_subdir,
    or podcast_language."""
    monkeypatch.setenv('LLM_EDITOR_MODEL_FR', 'mistralai/mistral-large-2411')
    settings = load_settings(locale='fr')
    # Locale machinery still wires up the FR side as before.
    assert settings.locale == 'fr'
    assert 'fr' in settings.prompt_file.lower() or settings.prompt_file == 'prompt_system_fr.txt'
    assert settings.docs_subdir == 'fr'
