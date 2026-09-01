from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class Vehicle:
    vehicle_id: str
    location: str
    status: str
    updated_at: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


@dataclass(frozen=True)
class SyncAction:
    action: str
    vehicle_id: str
    reason: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)
