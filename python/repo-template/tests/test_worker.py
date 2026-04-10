from __future__ import annotations

from pathlib import Path

from app.queue import enqueue_jobs
from app.worker import run_until_empty


def test_run_until_empty_creates_terminal_states(tmp_path: Path):
    log = tmp_path / "events.log"
    jobs = enqueue_jobs([
        {"job_id": "a", "payload": {"action": "success"}},
        {"job_id": "b", "payload": {"action": "fail", "message": "boom"}, "max_retries": 1},
    ])
    states = run_until_empty(log, jobs)
    assert states["a"]["state"] == "success"
    assert states["b"]["state"] == "failed"
