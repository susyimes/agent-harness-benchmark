from __future__ import annotations

from app.queue import enqueue_jobs


def test_enqueue_jobs_count():
    jobs = enqueue_jobs([{"job_id": "a"}, {"job_id": "b"}])
    assert len(jobs) == 2
