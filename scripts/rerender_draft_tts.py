"""Re-render TTS for the current pending draft using the latest TTS config.

Reads the script from a file (usually downloaded from a daily-generate artifact),
synthesizes audio with the current Cartesia settings, uploads it to R2 using the
SAME key as the original draft (so the old URL still works — it just points at the
new audio), and updates data/state/pending_draft_{locale}.json with the refreshed
audio metadata (bytes, duration).

Usage (called from tts-rerender-draft.yml):
    python scripts/rerender_draft_tts.py --script /tmp/script.txt [--locale fr]
"""
from __future__ import annotations

import argparse
import json
import logging
from datetime import datetime, timezone
from pathlib import Path

from ai_press_review.settings import load_settings
from ai_press_review.state import load_pending_draft, save_pending_draft
from ai_press_review.storage.r2 import upload_file
from ai_press_review.tts.cartesia import synthesize_script

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def main() -> None:
    parser = argparse.ArgumentParser(description="Re-render TTS for the pending draft")
    parser.add_argument("--script", required=True, help="Path to script.txt")
    parser.add_argument("--locale", default="", help="Locale override (en|fr)")
    args = parser.parse_args()

    script_path = Path(args.script)
    if not script_path.exists():
        raise FileNotFoundError(f"Script not found: {script_path}")

    script = script_path.read_text(encoding="utf-8")
    logger.info("Script loaded: %d words, %d chars", len(script.split()), len(script))

    # Load settings — APR_LOCALE env var also accepted if --locale not passed
    settings = load_settings()
    logger.info(
        "TTS config — locale=%s voice=%s speed=%s mode=%s",
        settings.locale or "(default)",
        settings.cartesia_voice_id[:8] + "..." if settings.cartesia_voice_id else "(unset)",
        settings.cartesia_speed,
        getattr(settings, "tts_mode", "websocket"),
    )

    # Load the pending draft to get the original audio_name / R2 key
    draft = load_pending_draft()
    if not draft:
        raise ValueError("No pending draft found — run daily-generate first")
    if draft.get("status") not in ("pending", "rejected"):
        raise ValueError(
            f"Pending draft status is '{draft.get('status')}' — "
            "expected 'pending' or 'rejected'. Cannot re-render a released episode."
        )

    audio_name = draft.get("audio_name")
    if not audio_name:
        # Reconstruct from audio_url if audio_name was not stored
        base = settings.public_audio_base_url.rstrip("/") + "/"
        audio_url_orig = draft.get("audio_url", "")
        audio_name = audio_url_orig.replace(base, "").lstrip("/").split("/")[-1]
    if not audio_name:
        raise ValueError("Cannot determine audio filename from pending draft")

    logger.info("Target audio name: %s", audio_name)

    # Render to a temp output path
    out_dir = Path("output") / "rerender"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / audio_name

    audio_meta = synthesize_script(script, out_path)
    logger.info(
        "TTS done — chunks=%d duration=%ds bytes=%d auto_spelled=%s",
        audio_meta["chunk_count"],
        audio_meta["duration_seconds"],
        audio_meta["bytes"],
        audio_meta.get("auto_spelled_acronyms", []),
    )

    # Upload to R2 using the same key — overwrites the old audio at the same URL
    remote_key = f"{settings.r2_audio_prefix.rstrip('/')}/{audio_name}"
    audio_url = upload_file(out_path, remote_key)
    logger.info("Uploaded: %s → %s", remote_key, audio_url)

    # Update the pending draft with the new audio metadata
    draft["audio_bytes"] = audio_meta["bytes"]
    draft["duration_seconds"] = audio_meta["duration_seconds"]
    draft["audio_url"] = audio_url
    draft["audio_name"] = audio_name
    draft["status"] = "pending"  # re-open if it was rejected
    draft["rerendered_at"] = datetime.now(timezone.utc).isoformat()
    save_pending_draft(draft)
    logger.info("Pending draft updated — ready for approve-release")

    print(json.dumps({
        "title": draft.get("title"),
        "audio_url": audio_url,
        "duration_seconds": audio_meta["duration_seconds"],
        "bytes": audio_meta["bytes"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
