from __future__ import annotations

from pathlib import Path

from app.metrics import summarize
from app.queue import enqueue_jobs
from app.storage import rebuild_state
from app.worker import run_once


def test_rebuild_state_with_retry_scheduled_keeps_latest_event():
    events = [
        {"job_id": "a", "type": "failed", "attempt": 1, "error": "boom"},
        {"job_id": "a", "type": "retry_scheduled", "attempt": 1},
    ]
    state = rebuild_state(events)
    assert state["a"]["state"] == "retry_scheduled"


def test_run_once_only_processes_single_job(tmp_path: Path):
    log = tmp_path / "events.log"
    jobs = enqueue_jobs([
        {"job_id": "a", "payload": {"action": "success"}},
        {"job_id": "b", "payload": {"action": "success"}},
    ])
    states = run_once(log, jobs)
    summary = summarize(states)
    assert summary["total"] == 1


def test_failed_job_records_error_message(tmp_path: Path):
    log = tmp_path / "events.log"
    jobs = enqueue_jobs([
        {"job_id": "x", "payload": {"action": "fail", "message": "nope"}, "max_retries": 0},
    ])
    states = run_once(log, jobs)
    assert states["x"]["last_error"] == "nope"
