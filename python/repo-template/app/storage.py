from __future__ import annotations

import json
from pathlib import Path


def append_event(log_path: Path, event: dict) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")


def read_events(log_path: Path) -> list[dict]:
    if not log_path.exists():
        return []
    items: list[dict] = []
    with log_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            items.append(json.loads(line))
    return items


def rebuild_state(events: list[dict]) -> dict[str, dict]:
    states: dict[str, dict] = {}
    for event in events:
        job_id = event["job_id"]
        states[job_id] = {
            "state": event["type"],
            "attempts": event.get("attempt", 0),
            "last_error": event.get("error"),
        }
    return states
