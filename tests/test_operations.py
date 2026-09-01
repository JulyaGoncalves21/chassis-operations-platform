import pytest

from chassis_platform.document_automation import render_transfer_document
from chassis_platform.models import Vehicle
from chassis_platform.normalization import normalize_vehicle_id
from chassis_platform.sync_plan import build_sync_plan, guardrail_errors


def vehicle(identifier: str, location: str, status: str = "Available") -> Vehicle:
    return Vehicle(identifier, location, status, "2026-01-01T10:00:00Z")


def test_vehicle_id_normalization() -> None:
    assert normalize_vehicle_id("demo-ab12-3456") == "DEMOAB123456"
    with pytest.raises(ValueError):
        normalize_vehicle_id("short")


def test_plan_describes_create_update_keep_and_deactivate() -> None:
    current = [
        vehicle("DEMO00000001", "Yard A"),
        vehicle("DEMO00000002", "Yard B"),
        vehicle("DEMO00000003", "Yard C"),
    ]
    incoming = [
        vehicle("DEMO00000001", "Yard A"),
        vehicle("DEMO00000002", "Dispatch"),
        vehicle("DEMO00000004", "Yard D"),
    ]
    assert [item.action for item in build_sync_plan(incoming, current)] == [
        "keep",
        "update",
        "deactivate",
        "create",
    ]


def test_guardrail_blocks_large_deactivation() -> None:
    actions = build_sync_plan([], [vehicle("DEMO00000001", "A")])
    assert guardrail_errors(actions) == ["deactivation ratio exceeds public demo guardrail"]


def test_document_is_marked_as_demo() -> None:
    text = render_transfer_document(
        {
            "request_id": "TR-001",
            "vehicle_id": "DEMO00000001",
            "origin": "Yard A",
            "destination": "Yard B",
        }
    )
    assert "DEMO ONLY" in text
