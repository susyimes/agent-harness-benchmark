from __future__ import annotations

from app.storage import rebuild_state


def test_rebuild_state_prefers_latest_event():
    events = [
        {"job_id": "a", "type": "running", "attempt": 1},
        {"job_id": "a", "type": "failed", "attempt": 1, "error": "boom"},
        {"job_id": "a", "type": "success", "attempt": 2},
    ]
    state = rebuild_state(events)
    assert state["a"]["state"] == "success"
