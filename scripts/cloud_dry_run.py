from __future__ import annotations

import argparse
import json
import logging
from datetime import date
from pathlib import Path

from ai_press_review.pipeline import run_pipeline

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
    datefmt="%H:%M:%S",
)


def _dump_collected_sources(run_date: str) -> Path | None:
    """Write a slim collected_sources.json (url, title, date, domain) next to the
    full manifest. Read from data/sources/<locale>/<run_date>.json (per-locale)
    or data/sources/<run_date>.json (legacy single-locale)."""
    import os

    locale = os.environ.get("APR_LOCALE", "").strip()
    candidates = []
    if locale:
        candidates.append(Path("data/sources") / locale / f"{run_date}.json")
    candidates.append(Path("data/sources") / f"{run_date}.json")

    manifest_path = next((p for p in candidates if p.exists()), None)
    if manifest_path is None:
        logging.getLogger(__name__).warning(
            "collected_sources.json: no manifest found at %s",
            ", ".join(str(p) for p in candidates),
        )
        return None

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    slim = []
    for src in manifest.get("sources", []):
        slim.append(
            {
                "url": src.get("url"),
                "title": src.get("title"),
                "published_at": src.get("published_at"),
                "domain": src.get("domain"),
            }
        )

    outputs_dir = Path("output") / run_date
    outputs_dir.mkdir(parents=True, exist_ok=True)
    out_path = outputs_dir / "collected_sources.json"
    out_path.write_text(
        json.dumps(
            {
                "run_date": run_date,
                "source_count": len(slim),
                "profile": manifest.get("profile"),
                "sources": slim,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    # Console recap: total + by domain + top 10
    logger = logging.getLogger(__name__)
    by_domain: dict[str, int] = {}
    for s in slim:
        d = (s.get("domain") or "unknown").lower()
        by_domain[d] = by_domain.get(d, 0) + 1
    logger.info("=" * 60)
    logger.info("COLLECTED SOURCES RECAP — %s", run_date)
    logger.info("=" * 60)
    logger.info("Total sources: %d", len(slim))
    logger.info("Distinct domains: %d", len(by_domain))
    logger.info("Top domains:")
    for dom, n in sorted(by_domain.items(), key=lambda kv: kv[1], reverse=True)[:10]:
        logger.info("  %4d  %s", n, dom)
    logger.info("Top 10 sources:")
    for i, s in enumerate(slim[:10], start=1):
        logger.info("  %2d. %s", i, s.get("title") or "(no title)")
        logger.info("      %s", s.get("url") or "")
    logger.info("=" * 60)
    return out_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Cloud dry run: remote LLM + (optionally) Cartesia, no upload/publish'
    )
    parser.add_argument('--date', default=date.today().isoformat())
    parser.add_argument('--profile', default='daily', help='Editorial profile: daily, weekly_recap')
    parser.add_argument(
        '--no-audio',
        action='store_true',
        help='Run Collect + Editorial only — skip TTS, upload and feed publication',
    )
    args = parser.parse_args()
    result = run_pipeline(
        run_date=args.date,
        local_preview=False,
        render_audio=not args.no_audio,
        upload_audio=False,
        publish_feed=False,
        profile=args.profile,
    )
    print(result)

    if args.no_audio:
        _dump_collected_sources(args.date)


if __name__ == '__main__':
    main()
