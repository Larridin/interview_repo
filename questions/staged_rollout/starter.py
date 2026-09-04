"""Plan a staged rollout of a desktop agent from a GitHub release catalog."""
from __future__ import annotations

import os
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

HERE = Path(__file__).parent

Reason = Literal[
    "up_to_date", "ring_update", "security_floor",
    "hold_not_in_cohort", "hold_paused", "hold_no_asset", "hold_ahead_of_catalog",
]


@dataclass(frozen=True)
class Release:
    tag: str
    version: tuple[int, ...]                 # parsed, comparable
    prerelease: bool
    platforms: frozenset[tuple[str, str]]    # (os, arch) pairs that have an asset


@dataclass(frozen=True)
class Decision:
    device_id: str
    current: str
    target: str | None
    reason: Reason


def build_catalog(owner: str, repo: str, token: str | None = None) -> list[Release]:
    # TODO
    raise NotImplementedError


def plan_rollout(fleet_csv: str, catalog: list[Release], rollout_yaml: str) -> list[Decision]:
    # TODO
    raise NotImplementedError


if __name__ == "__main__":
    catalog = build_catalog("cli", "cli", token=os.environ.get("GITHUB_TOKEN") or None)
    decisions = plan_rollout(str(HERE / "fleet.csv"), catalog, str(HERE / "rollout.yaml"))
    print(Counter(d.reason for d in decisions))
    print(Counter((d.reason, d.target) for d in decisions))
