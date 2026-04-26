"""Fix common TTS script artefacts before synthesis.

Applies three corrections in-place on a script file:

1. Duplicate standalone title line — the LLM sometimes emits the episode title
   as a bare first line AND repeats it verbatim at the start of the intro
   paragraph.  The duplicate causes TTS to read the show name twice before any
   content.  Detected when the first paragraph is a strict prefix of the second
   paragraph's opening.

2. Em dashes (U+2014) — Cartesia treats them as long pause markers.  Replace
   with a comma so the prosody stays natural without the dead air.

3. Markdown link syntax — the LLM occasionally slips in [text](url) notation
   which Cartesia reads aloud as bracket, text, bracket, parenthesis, URL,
   parenthesis.  Strip to plain text.

Usage:
    python scripts/fix_tts_script.py /tmp/script.txt
"""
from __future__ import annotations

import re
import sys


def _normalize(s: str) -> str:
    """Collapse whitespace and punctuation differences for loose comparison."""
    s = re.sub(r'[—\-–]', '', s)       # strip all dash variants
    s = re.sub(r'[:.!?]', '', s)        # strip sentence punctuation
    s = re.sub(r'\s+', ' ', s)          # collapse whitespace
    return s.strip().lower()


def fix(text: str) -> tuple[str, list[str]]:
    changes: list[str] = []

    # 1. Remove duplicate standalone title line.
    # Split on the first blank line; if the second paragraph opens with the
    # same words as the first (ignoring punctuation/spacing differences), the
    # first line is a bare title that TTS would read twice.  Drop it.
    parts = text.split('\n\n', 1)
    if len(parts) == 2:
        first = _normalize(parts[0].strip())
        rest = parts[1].strip()
        if first and _normalize(rest).startswith(first):
            text = rest
            changes.append(f"removed duplicate title line ({len(parts[0].strip())} chars)")

    # 2. Em dashes → comma-space.
    # Use a regex to absorb surrounding whitespace so " — " → ", " not " ,  ".
    count = len(re.findall('—', text))
    if count:
        text = re.sub(r'\s*—\s*', ', ', text)
        changes.append(f"replaced {count} em dash(es) with ', '")

    # 3. Strip Markdown link syntax [label](url) → label.
    text, n = re.subn(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    if n:
        changes.append(f"stripped {n} markdown link(s)")

    return text, changes


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: fix_tts_script.py <script_path>", file=sys.stderr)
        sys.exit(1)

    path = sys.argv[1]
    original = open(path, encoding='utf-8').read()
    fixed, changes = fix(original)

    if not changes:
        print(f"No changes needed — {len(original.split())} words")
        return

    with open(path, 'w', encoding='utf-8') as f:
        f.write(fixed)

    delta = len(fixed.split()) - len(original.split())
    sign = '+' if delta >= 0 else ''
    print(f"Fixed ({'; '.join(changes)}) — {len(fixed.split())} words ({sign}{delta})")


if __name__ == '__main__':
    main()
