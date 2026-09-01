# Public data model

| Entity | Key fields | Purpose |
|---|---|---|
| Vehicle Location | `vehicle_id`, `location`, `status`, `updated_at` | Current lookup state |
| Vehicle Event | `vehicle_id`, `event`, `reason`, `event_time` | Chronological audit context |
| Transfer Request | `request_id`, `vehicle_id`, `origin`, `destination`, `status` | Movement context |
| Dispatch Document | synthetic reference only | Document availability |

All identifiers in samples are invented and are not valid chassis numbers.

