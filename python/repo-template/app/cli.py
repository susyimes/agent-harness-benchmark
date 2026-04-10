from __future__ import annotations

import argparse
import json
from pathlib import Path

from .metrics import summarize
from .queue import enqueue_jobs
from .storage import read_events, rebuild_state
from .worker import run_once, run_until_empty


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["run-once", "run-until-empty", "status"])
    parser.add_argument("--seed", default="data/seed_jobs.json")
    parser.add_argument("--log", default="data/events.log")
    args = parser.parse_args()

    seed_path = Path(args.seed)
    log_path = Path(args.log)

    if args.command == "status":
        states = rebuild_state(read_events(log_path))
        print(json.dumps(summarize(states), ensure_ascii=False, sort_keys=True))
        return 0

    jobs = enqueue_jobs(json.loads(seed_path.read_text(encoding="utf-8")))
    if args.command == "run-once":
        states = run_once(log_path, jobs)
    else:
        states = run_until_empty(log_path, jobs)
    print(json.dumps(summarize(states), ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
