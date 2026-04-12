"""Structured observability for the podcast pipeline.

Writes JSONL metrics to `data/metrics/runs.jsonl`. One line per event.
Events are typed: 'run' (end-to-end summary), 'phase' (pipeline phase
duration), 'llm' (per-LLM-call token + cost stats).

Rotation is handled by `retention_days` at the call site (we don't
delete past history here — cheap storage, useful for trends).
"""
from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

from ..settings import DATA_DIR
from ..utils import iso_now

logger = logging.getLogger(__name__)

METRICS_DIR = DATA_DIR / 'metrics'
RUNS_PATH = METRICS_DIR / 'runs.jsonl'


# ── Cost table (USD per 1M tokens). Extend as new models are used. ──
# Values reflect publicly listed prices; set to None when unknown so the
# metric is still captured without a false cost.
MODEL_PRICING: dict[str, dict[str, float]] = {
    # Anthropic
    'claude-opus-4-6': {'input': 15.0, 'output': 75.0, 'cached_input': 1.5},
    'claude-sonnet-4-6': {'input': 3.0, 'output': 15.0, 'cached_input': 0.3},
    'claude-haiku-4-5': {'input': 1.0, 'output': 5.0, 'cached_input': 0.1},
    # OpenAI
    'gpt-4o': {'input': 2.5, 'output': 10.0, 'cached_input': 1.25},
    'gpt-4o-mini': {'input': 0.15, 'output': 0.6, 'cached_input': 0.075},
    # Groq / OSS
    'llama-3.3-70b-versatile': {'input': 0.59, 'output': 0.79},
    'mixtral-8x7b-32768': {'input': 0.24, 'output': 0.24},
}


def _estimate_cost_usd(model: str, prompt_tokens: int, completion_tokens: int, cached_tokens: int = 0) -> float | None:
    key = (model or '').lower()
    pricing = None
    for candidate in (key, key.split(':')[0], key.split('@')[0]):
        if candidate in MODEL_PRICING:
            pricing = MODEL_PRICING[candidate]
            break
    if not pricing:
        return None
    fresh_input = max(prompt_tokens - cached_tokens, 0)
    cost = (
        fresh_input * pricing['input']
        + cached_tokens * pricing.get('cached_input', pricing['input'])
        + completion_tokens * pricing['output']
    ) / 1_000_000
    return round(cost, 6)


def _append_event(event: dict[str, Any]) -> None:
    try:
        METRICS_DIR.mkdir(parents=True, exist_ok=True)
        event.setdefault('at', iso_now())
        with RUNS_PATH.open('a', encoding='utf-8') as handle:
            handle.write(json.dumps(event, ensure_ascii=False) + '\n')
    except Exception as exc:
        # Observability never breaks the pipeline.
        logger.warning("Failed to persist metric event: %s", exc)


def record_phase(run_date: str, phase: str, duration_s: float, **meta: Any) -> None:
    """Record a pipeline phase (collect, editorial, tts, upload, publish)."""
    _append_event({
        'type': 'phase',
        'run_date': run_date,
        'phase': phase,
        'duration_s': round(duration_s, 2),
        **meta,
    })


def record_llm_call(
    run_date: str,
    model: str,
    prompt_tokens: int,
    completion_tokens: int,
    duration_s: float,
    *,
    phase: str = 'editorial',
    cached_tokens: int = 0,
    retries: int = 0,
    success: bool = True,
    **meta: Any,
) -> None:
    cost = _estimate_cost_usd(model, prompt_tokens, completion_tokens, cached_tokens)
    _append_event({
        'type': 'llm',
        'run_date': run_date,
        'phase': phase,
        'model': model,
        'prompt_tokens': prompt_tokens,
        'completion_tokens': completion_tokens,
        'cached_tokens': cached_tokens,
        'duration_s': round(duration_s, 2),
        'retries': retries,
        'success': success,
        'cost_usd': cost,
        **meta,
    })


def record_run(run_date: str, **data: Any) -> None:
    """Record the end-to-end run summary."""
    _append_event({
        'type': 'run',
        'run_date': run_date,
        **data,
    })


def read_runs(limit: int | None = None) -> list[dict[str, Any]]:
    """Read recent events (most recent last). Returns an empty list if
    the metrics file does not yet exist."""
    if not RUNS_PATH.exists():
        return []
    events: list[dict[str, Any]] = []
    with RUNS_PATH.open('r', encoding='utf-8') as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    if limit is not None:
        return events[-limit:]
    return events
