from __future__ import annotations

from .models import SyncAction


def event_rows(actions: list[SyncAction], event_time: str) -> list[dict[str, str]]:
    return [
        {
            "vehicle_id": action.vehicle_id,
            "event": action.action,
            "reason": action.reason,
            "event_time": event_time,
        }
        for action in actions
        if action.action != "keep"
    ]
