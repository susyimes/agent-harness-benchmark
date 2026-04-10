from __future__ import annotations

from pathlib import Path

from .models import Job
from .retry import should_retry
from .storage import append_event, read_events, rebuild_state


def execute_job(job: Job) -> None:
    action = job.payload.get("action", "success")
    if action == "fail":
        raise RuntimeError(job.payload.get("message", "job failed"))


def run_once(log_path: Path, jobs: list[Job]) -> dict[str, dict]:
    states = rebuild_state(read_events(log_path))
    for job in jobs:
        state = states.get(job.job_id)
        attempt = (state or {}).get("attempts", 0) + 1
        append_event(log_path, {"job_id": job.job_id, "type": "running", "attempt": attempt})
        try:
            execute_job(job)
        except Exception as exc:
            append_event(log_path, {"job_id": job.job_id, "type": "failed", "attempt": attempt, "error": str(exc)})
            if should_retry(attempt, job.max_retries):
                append_event(log_path, {"job_id": job.job_id, "type": "retry_scheduled", "attempt": attempt})
        else:
            append_event(log_path, {"job_id": job.job_id, "type": "success", "attempt": attempt})
        break
    return rebuild_state(read_events(log_path))


def run_until_empty(log_path: Path, jobs: list[Job], max_steps: int = 100) -> dict[str, dict]:
    states = {}
    for _ in range(max_steps):
        states = run_once(log_path, jobs)
        pending = [j for j in jobs if states.get(j.job_id, {}).get("state") not in {"success", "failed"}]
        if not pending:
            return states
    return states
