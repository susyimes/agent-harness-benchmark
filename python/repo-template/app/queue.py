from __future__ import annotations

from .models import Job


def enqueue_jobs(raw_jobs: list[dict]) -> list[Job]:
    return [
        Job(
            job_id=item["job_id"],
            payload=item.get("payload", {}),
            max_retries=item.get("max_retries", 0),
        )
        for item in raw_jobs
    ]


def pick_next(states: dict[str, dict], jobs: list[Job]) -> Job | None:
    for job in jobs:
        if job.job_id not in states or states[job.job_id]["state"] not in {"success", "failed"}:
            return job
    return None
