from __future__ import annotations

import argparse
from pathlib import Path

from .export import export_plan
from .local_source import read_vehicles
from .sync_plan import build_sync_plan, guardrail_errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build a local dry-run vehicle synchronization plan."
    )
    parser.add_argument("--incoming", type=Path, default=Path("sample-data/incoming_vehicles.csv"))
    parser.add_argument("--current", type=Path, default=Path("sample-data/current_registry.csv"))
    parser.add_argument("--output", type=Path, default=Path("output"))
    args = parser.parse_args()
    actions = build_sync_plan(read_vehicles(args.incoming), read_vehicles(args.current))
    errors = guardrail_errors(actions)
    if errors:
        print("blocked: " + "; ".join(errors))
        return 2
    export_plan(actions, args.output)
    print(f"dry_run_actions={len(actions)} external_writes=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
