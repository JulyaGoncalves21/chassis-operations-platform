from __future__ import annotations

import re


def normalize_vehicle_id(value: object) -> str:
    normalized = re.sub(r"[^A-Z0-9]", "", str(value).upper())
    if not 8 <= len(normalized) <= 17:
        raise ValueError("vehicle identifier must contain 8 to 17 letters or digits")
    return normalized


def normalize_text(value: object) -> str:
    return " ".join(str(value).strip().split())
