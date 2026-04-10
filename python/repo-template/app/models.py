from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Job:
    job_id: str
    payload: dict[str, Any] = field(default_factory=dict)
    max_retries: int = 0


@dataclass
class JobState:
    job_id: str
    state: str
    attempts: int = 0
    last_error: str | None = None


TERMINAL_STATES = {"success", "failed"}
