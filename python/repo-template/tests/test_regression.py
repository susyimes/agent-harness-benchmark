from __future__ import annotations

from pathlib import Path

from app.storage import append_event, read_events, rebuild_state


def test_corrupted_tail_should_be_tolerated(tmp_path: Path):
    log = tmp_path / "events.log"
    append_event(log, {"job_id": "a", "type": "running", "attempt": 1})
    with log.open("a", encoding="utf-8") as f:
        f.write('{"job_id": "a", "type": "failed"')
    events = read_events(log)
    state = rebuild_state(events)
    assert state["a"]["state"] == "running"
