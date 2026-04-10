from __future__ import annotations

from app.retry import should_retry


def test_retry_zero_allows_no_retry():
    assert should_retry(1, 0) is False
