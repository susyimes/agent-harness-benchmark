from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def test_status_command_outputs_json(tmp_path: Path):
    log = tmp_path / "events.log"
    seed = tmp_path / "seed.json"
    seed.write_text("[]", encoding="utf-8")
    result = subprocess.run(
        [sys.executable, "-m", "app.cli", "status", "--seed", str(seed), "--log", str(log)],
        capture_output=True,
        text=True,
        cwd=Path(__file__).resolve().parents[1],
        check=False,
    )
    assert result.returncode == 0
    data = json.loads(result.stdout)
    assert data["total"] == 0
