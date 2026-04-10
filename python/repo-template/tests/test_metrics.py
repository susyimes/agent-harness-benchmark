from __future__ import annotations

from app.metrics import summarize


def test_summarize_counts_known_states():
    summary = summarize({
        "a": {"state": "success"},
        "b": {"state": "failed"},
        "c": {"state": "retry_scheduled"},
    })
    assert summary == {"total": 3, "success": 1, "failed": 1, "running": 0, "retry_scheduled": 1}
