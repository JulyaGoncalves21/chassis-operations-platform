from __future__ import annotations

from .models import SyncAction, Vehicle


def build_sync_plan(incoming: list[Vehicle], current: list[Vehicle]) -> list[SyncAction]:
    """Create an auditable plan; this function performs no external writes."""
    incoming_by_id = {item.vehicle_id: item for item in incoming}
    current_by_id = {item.vehicle_id: item for item in current}
    actions: list[SyncAction] = []
    for vehicle_id, item in incoming_by_id.items():
        previous = current_by_id.get(vehicle_id)
        if previous is None:
            actions.append(SyncAction("create", vehicle_id, "not present in current registry"))
        elif (item.location, item.status) != (previous.location, previous.status):
            actions.append(SyncAction("update", vehicle_id, "location or status changed"))
        else:
            actions.append(SyncAction("keep", vehicle_id, "no relevant change"))
    for vehicle_id in current_by_id.keys() - incoming_by_id.keys():
        actions.append(SyncAction("deactivate", vehicle_id, "absent from incoming snapshot"))
    return sorted(actions, key=lambda action: action.vehicle_id)


def guardrail_errors(
    actions: list[SyncAction], maximum_deactivation_ratio: float = 0.25
) -> list[str]:
    if not actions:
        return ["empty synchronization plan"]
    deactivations = sum(action.action == "deactivate" for action in actions)
    if deactivations / len(actions) > maximum_deactivation_ratio:
        return ["deactivation ratio exceeds public demo guardrail"]
    return []
