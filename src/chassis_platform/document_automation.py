from __future__ import annotations

from string import Template

DOCUMENT_TEMPLATE = Template(
    "Transfer request $request_id\nVehicle: $vehicle_id\nOrigin: $origin\nDestination: $destination\nStatus: DEMO ONLY\n"
)


def render_transfer_document(fields: dict[str, str]) -> str:
    required = {"request_id", "vehicle_id", "origin", "destination"}
    missing = required - fields.keys()
    if missing:
        raise ValueError(f"missing document fields: {', '.join(sorted(missing))}")
    return DOCUMENT_TEMPLATE.substitute(fields)
