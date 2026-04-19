"""Extract the script from the current pending draft and write it to /tmp/script.txt.

Called by tts-rerender-draft.yml when no source_run_id is provided.
"""
from __future__ import annotations

import json
import os
import pathlib
import sys

locale = os.environ.get('LOCALE', 'en')
candidates = [
    pathlib.Path(f'data/state/pending_draft_{locale}.json'),
    pathlib.Path('data/state/pending_draft.json'),
]

data = None
found_path = None
for p in candidates:
    if p.exists():
        data = json.loads(p.read_text(encoding='utf-8'))
        found_path = p
        break

if data is None:
    print('ERROR: no pending draft found in data/state/', file=sys.stderr)
    sys.exit(1)

script = data.get('script', '').strip()
if not script:
    print('ERROR: pending draft has no script field', file=sys.stderr)
    sys.exit(1)

out = pathlib.Path('/tmp/script.txt')
out.write_text(script, encoding='utf-8')
print(f'Extracted {len(script.split())} words from {found_path}')
