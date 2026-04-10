from __future__ import annotations


def summarize(states: dict[str, dict]) -> dict[str, int]:
    result = {"total": len(states), "success": 0, "failed": 0, "running": 0, "retry_scheduled": 0}
    for state in states.values():
        name = state["state"]
        if name in result:
            result[name] += 1
    return result
