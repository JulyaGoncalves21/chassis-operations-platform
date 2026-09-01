from __future__ import annotations

import csv
from pathlib import Path

from .models import Vehicle
from .normalization import normalize_text, normalize_vehicle_id


def read_vehicles(path: Path) -> list[Vehicle]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return [
            Vehicle(
                vehicle_id=normalize_vehicle_id(row["vehicle_id"]),
                location=normalize_text(row["location"]),
                status=normalize_text(row["status"]),
                updated_at=row["updated_at"].strip(),
            )
            for row in csv.DictReader(stream)
        ]
