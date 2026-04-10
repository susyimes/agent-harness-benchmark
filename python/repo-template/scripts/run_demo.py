from __future__ import annotations

from pathlib import Path

from app.cli import main


if __name__ == "__main__":
    log = Path("data/events.log")
    if log.exists():
        log.unlink()
    raise SystemExit(main())
