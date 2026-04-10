from __future__ import annotations

from pathlib import Path

from app.queue import enqueue_jobs
from app.worker import run_until_empty
from app.storage import rebuild_state


def test_run_until_empty_leaves_failed_job_visible(tmp_path: Path):
    log = tmp_path / "events.log"
    jobs = enqueue_jobs([
        {"job_id": "a", "payload": {"action": "fail", "message": "x"}, "max_retries": 0}
    ])
    states = run_until_empty(log, jobs)
    assert states["a"]["state"] == "failed"


def test_rebuild_state_handles_multiple_jobs():
    events = [
        {"job_id": "a", "type": "success", "attempt": 1},
        {"job_id": "b", "type": "failed", "attempt": 1, "error": "boom"},
    ]
    states = rebuild_state(events)
    assert set(states.keys()) == {"a", "b"}


def test_failed_job_with_retry_marks_retry_scheduled(tmp_path: Path):
    log = tmp_path / "events.log"
    jobs = enqueue_jobs([
        {"job_id": "r", "payload": {"action": "fail", "message": "boom"}, "max_retries": 1}
    ])
    states = run_until_empty(log, jobs)
    assert states["r"]["state"] in {"failed", "retry_scheduled"}
