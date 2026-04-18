import re
from datetime import datetime

REQUIRED_SECTION_KEYS = [
    "ai_news",
    "use_cases_and_deployments",
    "tools_and_practice",
    "weak_signals_and_trends",
    "research_and_breakthroughs",
    "education_and_pedagogy",
]

# Weekly recap uses a 2-part structure: intro + news/use-cases (Part 1) +
# what-to-watch (Part 2). Separate key list so validate_section_payload can
# enforce the right order for each format.
REQUIRED_SECTION_KEYS_WEEKLY = [
    "weekly_intro",       # 1-2 §: introduces the 3-part format naturally
    "weekly_news",        # Part 1: the week's biggest news stories
    "weekly_use_cases",   # Part 1: concrete deployments this week
    "weekly_offradar",    # Part 1b: signals absent from mainstream media
    "weekly_next_week",   # Part 2: what to watch next week (news only)
]

# Closing sentence appended to every script. Each locale has its own — both EN
# and FR prompts tell the LLM NOT to include the closing, so the pipeline
# appends the locale-appropriate text here. Passing an English closing into a
# French TTS voice would make the voice drift mid-sentence (observed on
# 2026-04-15 FR audio).
CLOSING_SENTENCES_BY_LOCALE = {
    'en': (
        "This podcast has a daily production cost. "
        "If you enjoy it, support it — the link is on the podcast page. Thank you."
    ),
    'fr': (
        "Ce podcast a un coût de production quotidien. "
        "Pour le soutenir, le lien est sur la page du podcast. Merci."
    ),
}
# Backward-compat alias for code / tests that imported the EN-only constant.
CLOSING_SENTENCE = CLOSING_SENTENCES_BY_LOCALE['en']

# Opening line prefixes per locale. The prompts for each locale reference the
# exact string in their "INJECTÉE AUTOMATIQUEMENT" instruction so the LLM never
# duplicates the opening. Keep these in sync with config/podcast.yaml
# (locales.*.opening_line_daily / opening_line_weekly).
OPENING_PREFIXES_BY_LOCALE = {
    'en': {
        'daily': 'Your Daily AI Press Review',
        'weekly': 'Your Weekly AI Press Review',
    },
    'fr': {
        'daily': 'Votre Revue de Presse IA du jour',
        'weekly': 'Votre Revue de Presse IA hebdo',
    },
}

# Month names in French (strftime('%B') depends on the runner locale, which
# isn't guaranteed; inline table avoids a system-locale dependency).
_MONTHS_FR = [
    'janvier', 'février', 'mars', 'avril', 'mai', 'juin',
    'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre',
]


def _format_date_for_locale(dt: datetime, intro_format: str, locale: str) -> str:
    """Human-readable date for the intro line. FR → '15 avril 2026' / 'semaine du 15 avril 2026'."""
    if locale == 'fr':
        base = f"{dt.day} {_MONTHS_FR[dt.month - 1]} {dt.year}"
        return f"semaine du {base}" if intro_format == 'weekly' else base
    base = dt.strftime("%B %d, %Y")
    return f"Week of {base}" if intro_format == 'weekly' else base


def _intro_pattern(intro_format: str, locale: str) -> str:
    """Regex matching a correctly-formed intro line for (format, locale)."""
    prefix = re.escape(OPENING_PREFIXES_BY_LOCALE[locale][intro_format])
    if locale == 'fr':
        # '15 avril 2026' / 'semaine du 15 avril 2026'
        months = '|'.join(_MONTHS_FR)
        date_re = rf"(?:semaine du )?\d{{1,2}} (?:{months}) \d{{4}}"
    else:
        # 'April 15, 2026' / 'Week of April 15, 2026'
        date_re = r"(?:Week of )?[A-Za-z]+ \d{1,2}, \d{4}"
    return rf"{prefix} — {date_re}: .+\."


def _normalize_locale(locale: str | None) -> str:
    """Map empty/unknown locales to 'en' (default keeps legacy single-locale behavior)."""
    if not locale:
        return 'en'
    loc = locale.strip().lower()
    return loc if loc in OPENING_PREFIXES_BY_LOCALE else 'en'


def build_intro_line(
    run_date: str,
    highlights_label: str,
    intro_format: str = 'daily',
    locale: str | None = None,
) -> str:
    """Build the opening sentence the pipeline injects as the first paragraph.

    Locale drives both the prefix ('Your Daily…' vs 'Votre Revue de Presse IA…')
    and the date wording. Passing the wrong locale here is how a FR TTS voice
    ends up reading 'April fifteenth, two thousand twenty-six' in English.
    """
    loc = _normalize_locale(locale)
    dt = datetime.fromisoformat(run_date)
    label = " ".join((highlights_label or "").split())[:32].strip() or "Highlights"
    prefix = OPENING_PREFIXES_BY_LOCALE[loc][intro_format]
    formatted = _format_date_for_locale(dt, intro_format, loc)
    return f"{prefix} — {formatted}: {label}."


def validate_section_payload(payload: dict, intro_format: str = 'daily') -> None:
    required_keys = (
        REQUIRED_SECTION_KEYS_WEEKLY if intro_format == 'weekly' else REQUIRED_SECTION_KEYS
    )
    sections = payload.get("sections") or {}
    actual_keys = list(sections.keys())

    # Better error surfacing: first call out missing / extra keys by name so a
    # prompt-drift (e.g. the LLM returning `ai_news` instead of `weekly_news`)
    # yields an actionable message, not a generic "order does not match".
    missing = [k for k in required_keys if k not in sections]
    extra = [k for k in actual_keys if k not in required_keys]
    if missing or extra:
        raise ValueError(
            f"Section keys mismatch — missing={missing!r}, unexpected={extra!r}, "
            f"expected={required_keys!r}"
        )
    if actual_keys != required_keys:
        raise ValueError(
            f"Section order does not match the editorial line: got {actual_keys!r}, "
            f"expected {required_keys!r}"
        )

    for key in required_keys:
        paragraphs = sections.get(key)
        if not isinstance(paragraphs, list) or not paragraphs:
            raise ValueError(f"Missing section content for {key}")
        for paragraph in paragraphs:
            _validate_paragraph(paragraph)

    # tomorrow_pedagogical_concept is a daily concept — not applicable to weekly.
    if intro_format != 'weekly':
        raw_concept = payload.get("tomorrow_pedagogical_concept") or ""
        if not isinstance(raw_concept, str):
            raise ValueError(
                f"tomorrow_pedagogical_concept must be a string, got {type(raw_concept).__name__}"
            )
        tomorrow_concept = raw_concept.strip()
        if not tomorrow_concept:
            raise ValueError("Tomorrow pedagogical concept is missing")
        if len(tomorrow_concept.split()) > 12:
            raise ValueError("Tomorrow pedagogical concept is too long")


def assemble_script(
    run_date: str,
    payload: dict,
    intro_format: str = 'daily',
    locale: str | None = None,
) -> str:
    """Assemble the final TTS-ready script with locale-aware intro & closing."""
    validate_section_payload(payload, intro_format=intro_format)
    loc = _normalize_locale(locale)

    intro = build_intro_line(
        run_date, payload.get("highlights_label", "Highlights"), intro_format, locale=loc,
    )
    sections = payload["sections"]

    section_keys = (
        REQUIRED_SECTION_KEYS_WEEKLY if intro_format == 'weekly' else REQUIRED_SECTION_KEYS
    )
    ordered_paragraphs = [intro]
    for key in section_keys:
        ordered_paragraphs.extend([p.strip() for p in sections[key] if p.strip()])

    ordered_paragraphs.append(CLOSING_SENTENCES_BY_LOCALE[loc])
    # tomorrow_pedagogical_concept is kept in the JSON payload (for the episode
    # brief page) but is NOT appended to the TTS script — the teaser was removed
    # from the audio by user request.

    script = "\n\n".join(ordered_paragraphs)
    validate_final_script(script, intro_format, locale=loc)
    return script


def validate_final_script(
    script: str,
    intro_format: str = 'daily',
    locale: str | None = None,
) -> None:
    loc = _normalize_locale(locale)
    lines = [line.strip() for line in script.splitlines() if line.strip()]
    if not lines:
        raise ValueError("Script is empty")

    pattern = _intro_pattern(intro_format, loc)
    if not re.fullmatch(pattern, lines[0]):
        raise ValueError(f"Opening line does not match the required format for locale={loc!r}")

    if len(lines) < 4:
        raise ValueError("Script has too few paragraphs")

    expected_closing = CLOSING_SENTENCES_BY_LOCALE[loc]
    if lines[-1] != expected_closing:
        raise ValueError(f"Closing sentence does not exactly match the required line for locale={loc!r}")

    for line in lines:
        _validate_paragraph(line)


def _validate_paragraph(text) -> None:
    # Explicit type check so a malformed JSON payload (e.g. the LLM returning
    # `sections.ai_news = [{"text": "…"}, "…"]`) surfaces a readable error
    # instead of a raw AttributeError deep inside `text.strip()`.
    if not isinstance(text, str):
        raise ValueError(
            f"Paragraph must be a string, got {type(text).__name__}: {text!r}"
        )
    stripped = text.strip()
    if not stripped:
        raise ValueError("Empty paragraph found")
    if re.match(r"^[\-\*\u2022]\s+", stripped):
        raise ValueError("Bullet points are forbidden in the final script")
    if re.match(r"^\d+[\.)]\s+", stripped):
        raise ValueError("Enumerated lists are forbidden in the final script")
    if stripped.endswith(":"):
        raise ValueError("Heading-style paragraphs are forbidden in the final script")
