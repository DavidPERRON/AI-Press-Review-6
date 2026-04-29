"""Quick TTS voice test — renders a short text and uploads to R2 under audio-test/.

Usage (from tts-voice-test.yml):
    TEST_TEXT="..." APR_LOCALE=fr python scripts/tts_voice_test.py
"""
from __future__ import annotations

import logging
import os
import re
import sys
from pathlib import Path

from ai_press_review.settings import load_settings
from ai_press_review.storage.r2 import upload_file
from ai_press_review.tts.cartesia import synthesize_script

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
    datefmt="%H:%M:%S",
)

text = os.environ.get('TEST_TEXT', '').strip()
if not text:
    print("TEST_TEXT is empty — nothing to render")
    sys.exit(1)

suffix = os.environ.get('TTS_OUTPUT_SUFFIX', '')
emotion_override = os.environ.get('TTS_EMOTION_OVERRIDE', '').strip()
if not suffix and emotion_override:
    # Derive a filesystem/R2-safe suffix from the emotion string so two
    # back-to-back runs (e.g. "excited" then "positivity:high") don't
    # overwrite each other's artifacts.
    suffix = '-' + re.sub(r'[^a-zA-Z0-9]+', '-', emotion_override).strip('-')
output_dir = Path('output/tts-test')
output_dir.mkdir(parents=True, exist_ok=True)
audio_path = output_dir / f'test{suffix}.mp3'

settings = load_settings()
speed_override = os.environ.get('TTS_SPEED_OVERRIDE', '').strip()
if speed_override:
    settings.cartesia_speed = float(speed_override)
if emotion_override:
    settings.cartesia_emotion = emotion_override

print(f"Locale  : {settings.locale or '(default)'}")
print(f"Voice   : {settings.cartesia_voice_id}")
print(f"Speed   : {settings.cartesia_speed}{' (override)' if speed_override else ''}")
print(f"Emotion : {settings.cartesia_emotion}{' (override)' if emotion_override else ''}")
print(f"Mode    : {settings.tts_mode}")
print(f"Text    : {len(text)} chars")

meta = synthesize_script(text, audio_path)
print(f"Rendered: {meta['duration_seconds']}s  {meta['bytes'] / 1024:.0f} KB")

locale_tag = settings.locale or 'en'
remote_key = f"audio-test/voice-test-{locale_tag}{suffix}.mp3"
url = upload_file(audio_path, remote_key)
print(f"\nAudio URL: {url}")
(output_dir / 'url.txt').write_text(url + '\n', encoding='utf-8')
