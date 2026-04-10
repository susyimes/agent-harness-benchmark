from __future__ import annotations

import json
import random
from pathlib import Path


def main() -> None:
    random.seed(42)
    jobs = []
    for i in range(100):
        jobs.append({
            "job_id": f"job-{i}",
            "payload": {"action": "fail" if i % 10 == 0 else "success", "message": "boom"},
            "max_retries": 1 if i % 10 == 0 else 0,
        })
    out = Path("data/generated_seed_100.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
