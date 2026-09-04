"""Attribute desktop heartbeats to employees and build the reporting tree."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

HERE = Path(__file__).parent


@dataclass(frozen=True)
class Attribution:
    user_id: str
    employee_email: str | None     # None when unmatched or ambiguous
    tier: str | None               # which policy tier matched
    reason: str | None             # "ambiguous:2", "no_match", "deleted_employee", ...


@dataclass
class Report:
    roots: list[str]
    reachable_active: int
    roster_active: int
    depth_by_email: dict[str, int]              # 0 for a root; only employees reachable from a root
    attributions: list[Attribution]
    coverage_by_domain: dict[str, dict[str, int]] = field(default_factory=dict)
    anomalies: list[str] = field(default_factory=list)   # cycles, self-loops, dangling managers


def build_report(employees_csv: str, heartbeats_jsonl: str, policy_yaml: str) -> Report:
    # TODO
    raise NotImplementedError


if __name__ == "__main__":
    report = build_report(
        str(HERE / "data" / "employees.csv"),
        str(HERE / "data" / "heartbeats.jsonl"),
        str(HERE / "policy.yaml"),
    )
    print(f"roots={len(report.roots)} reachable={report.reachable_active} roster={report.roster_active}")
    print(report.coverage_by_domain)
    for a in report.anomalies:
        print("anomaly:", a)
