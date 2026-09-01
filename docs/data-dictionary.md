# Synthetic data dictionary

All example values are fictional and use identifiers that cannot be mistaken for valid VINs.

## Vehicle registry and incoming snapshot

| Field | Type | Example | Purpose | Validation |
| --- | --- | --- | --- | --- |
| `vehicle_id` | string | `DEMO00000001` | Synthetic record key | Must start with `DEMO`; not a VIN |
| `location` | string | `North Yard` | Fictional current zone | Required, free-text demo value |
| `status` | string | `Available` | Conceptual operating state | Required, demo vocabulary |
| `updated_at` | ISO 8601 timestamp | `2026-06-01T08:00:00Z` | Synthetic state timestamp | Must be parseable |

## Transfer requests

| Field | Type | Example | Purpose | Validation |
| --- | --- | --- | --- | --- |
| `request_id` | string | `TR-001` | Synthetic request key | Required and unique in sample |
| `vehicle_id` | string | `DEMO00000002` | Links to the synthetic vehicle | Must use `DEMO` prefix |
| `origin` | string | `Inspection Bay` | Fictional origin | Required |
| `destination` | string | `Dispatch Zone` | Fictional destination | Required and different from origin |
| `status` | string | `Planned` | Conceptual request state | Demo vocabulary only |

The public model intentionally excludes customer, employee, document, financial and corporate-system fields.

