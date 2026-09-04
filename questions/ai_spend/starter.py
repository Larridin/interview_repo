"""Monthly AI spend by person and team, reconciled to the vendor's own accounting."""
from __future__ import annotations

import os
import sys
from dataclasses import dataclass, field
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).parent


@dataclass
class SpendReport:
    month: str                                      # "2026-08"
    total_usd: Decimal
    by_tool: dict[str, Decimal]
    by_person: dict[str, Decimal]                   # roster email, lowercased
    by_manager: dict[str, Decimal]                  # manager's subtree including themselves
    untracked_usd: Decimal                          # spend with no user
    unassigned_usd: Decimal                         # spend by users not on the roster
    adoption: dict[str, float | int]                # active_users, headcount, pct_of_headcount, pct_of_active
    reconciles: bool                                # sum of buckets == total_usd
    vendor_check: dict[str, dict[str, Decimal]]     # per model: computed, vendor, delta, for rows with a generation_id
    missing_generations: list[str]                  # generation ids the vendor could not find
    warnings: list[str] = field(default_factory=list)


def compute_spend(usage_jsonl: str, employees_csv: str, tools_yaml: str, month: str,
                  openrouter_key: str | None = None) -> SpendReport:
    # TODO
    raise NotImplementedError


if __name__ == "__main__":
    month = sys.argv[1] if len(sys.argv) > 1 else "2026-08"
    report = compute_spend(
        str(HERE / "data" / "usage.jsonl"),
        str(HERE / "data" / "employees.csv"),
        str(HERE / "tools.yaml"),
        month,
        openrouter_key=os.environ.get("OPENROUTER_API_KEY") or None,
    )
    print(f"{report.month}: total ${report.total_usd}  reconciles={report.reconciles}")
    print("by_tool:", report.by_tool)
    print("untracked:", report.untracked_usd, "unassigned:", report.unassigned_usd)
    print("adoption:", report.adoption)
    print("vendor_check:", report.vendor_check)
    for w in report.warnings:
        print("warning:", w)
