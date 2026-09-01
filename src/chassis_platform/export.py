from __future__ import annotations

import csv
import json
from pathlib import Path

from .models import SyncAction


def export_plan(actions: list[SyncAction], output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    rows = [action.to_dict() for action in actions]
    with (output / "sync_plan.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=["action", "vehicle_id", "reason"])
        writer.writeheader()
        writer.writerows(rows)
    (output / "sync_plan.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")
