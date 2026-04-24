"""Cartesia voice mixing utility.

Steps:
  1. List available EN voices from Cartesia library
  2. Create a mixed voice from your clone + a chosen library voice
  3. Print the new voice ID to use as CARTESIA_VOICE_ID

Usage:
    # List available EN voices
    python scripts/cartesia_voice_mix.py --list

    # Create a mix: 70% your clone + 30% a library voice
    python scripts/cartesia_voice_mix.py --mix <library_voice_id> --ratio 0.7

    # Dry-run (print payload without calling API)
    python scripts/cartesia_voice_mix.py --mix <library_voice_id> --ratio 0.7 --dry-run

Environment variables required:
    CARTESIA_API_KEY      - your Cartesia API key
    CARTESIA_VOICE_ID     - your current EN clone voice ID
    CARTESIA_VERSION      - optional, defaults to 2026-03-01
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.request
import urllib.error

API_BASE = 'https://api.cartesia.ai'


def _headers(api_key: str, version: str) -> dict:
    return {
        'X-API-Key': api_key,
        'Cartesia-Version': version,
        'Content-Type': 'application/json',
    }


def _get(path: str, api_key: str, version: str) -> dict:
    req = urllib.request.Request(
        f'{API_BASE}{path}',
        headers=_headers(api_key, version),
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def _post(path: str, payload: dict, api_key: str, version: str) -> dict:
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        f'{API_BASE}{path}',
        data=data,
        headers=_headers(api_key, version),
        method='POST',
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def list_voices(api_key: str, version: str) -> None:
    print('Fetching Cartesia voice library...\n')
    result = _get('/voices', api_key, version)
    voices = result if isinstance(result, list) else result.get('voices', [])

    # Filter English voices, exclude clones (user-created)
    en_voices = [
        v for v in voices
        if (v.get('language') or '').startswith('en')
        and not v.get('is_owner', False)
    ]

    if not en_voices:
        print('No public English voices found. Showing all voices:\n')
        en_voices = voices

    print(f'{"ID":<38} {"Name":<35} {"Gender":<8} {"Description"}')
    print('-' * 110)
    for v in sorted(en_voices, key=lambda x: x.get('name', '')):
        vid = v.get('id', '')
        name = (v.get('name') or '')[:34]
        gender = (v.get('gender') or v.get('features', {}).get('gender', '?'))[:7]
        desc = (v.get('description') or '')[:50]
        print(f'{vid:<38} {name:<35} {gender:<8} {desc}')

    print(f'\nTotal: {len(en_voices)} voices')


def create_mix(clone_id: str, partner_id: str, ratio: float,
               name: str, api_key: str, version: str, dry_run: bool) -> None:
    """Mix clone_id (ratio) with partner_id (1-ratio)."""
    payload = {
        'name': name,
        'description': f'Mixed voice: {ratio*100:.0f}% clone + {(1-ratio)*100:.0f}% EN library',
        'voices': [
            {'id': clone_id,   'weight': ratio},
            {'id': partner_id, 'weight': round(1.0 - ratio, 4)},
        ],
    }

    print('Payload:')
    print(json.dumps(payload, indent=2))

    if dry_run:
        print('\n[dry-run] Not calling API.')
        return

    print('\nCreating mixed voice...')
    try:
        result = _post('/voices/mix', payload, api_key, version)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode()
        print(f'API error {exc.code}: {body}', file=sys.stderr)
        sys.exit(1)

    new_id = result.get('id', '')
    print(f'\nMixed voice created!')
    print(f'  ID   : {new_id}')
    print(f'  Name : {result.get("name")}')
    print(f'\nUpdate your GitHub secret CARTESIA_VOICE_ID to: {new_id}')


def main() -> None:
    parser = argparse.ArgumentParser(description='Cartesia voice mixing utility')
    parser.add_argument('--list', action='store_true', help='List available EN voices')
    parser.add_argument('--mix', metavar='PARTNER_VOICE_ID', help='Library voice ID to mix with your clone')
    parser.add_argument('--ratio', type=float, default=0.7,
                        help='Weight of YOUR clone (0.0-1.0, default 0.7)')
    parser.add_argument('--name', default='AI Press Review EN (mixed)',
                        help='Name for the new mixed voice')
    parser.add_argument('--dry-run', action='store_true', help='Print payload only, no API call')
    args = parser.parse_args()

    api_key = os.environ.get('CARTESIA_API_KEY', '').strip()
    clone_id = os.environ.get('CARTESIA_VOICE_ID', '').strip()
    version = os.environ.get('CARTESIA_VERSION', '2026-03-01').strip()

    if not api_key and not args.dry_run:
        print('Error: CARTESIA_API_KEY not set', file=sys.stderr)
        sys.exit(1)

    if args.list:
        list_voices(api_key, version)
        return

    if args.mix:
        if not clone_id and not args.dry_run:
            print('Error: CARTESIA_VOICE_ID not set', file=sys.stderr)
            sys.exit(1)
        if not 0.0 < args.ratio < 1.0:
            print('Error: --ratio must be between 0 and 1 exclusive', file=sys.stderr)
            sys.exit(1)
        create_mix(clone_id, args.mix, args.ratio, args.name, api_key, version, args.dry_run)
        return

    parser.print_help()


if __name__ == '__main__':
    main()
