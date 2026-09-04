"""Feature flag evaluation and safe single-customer enablement."""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

HERE = Path(__file__).parent


@dataclass(frozen=True)
class Evaluation:
    value: Any
    variation_index: int
    reason: str            # "OFF", "TARGET_MATCH", "RULE_MATCH:<rule id>", "FALLTHROUGH", ...


def evaluate(flag: dict[str, Any], context: dict[str, Any]) -> Evaluation:
    # TODO
    raise NotImplementedError


def plan_enable(flag: dict[str, Any], org_key: str) -> tuple[list[str], dict[str, Any]]:
    """
    Return (ordered_steps, resulting_flag) such that, after applying the steps
    in order, evaluate() returns True for exactly this org and False for
    every other org. Each intermediate state must also be safe.
    """
    # TODO
    raise NotImplementedError


if __name__ == "__main__":
    flags = {f["key"]: f for f in json.loads((HERE / "flags.json").read_text())}
    contexts = json.loads((HERE / "contexts.json").read_text())
    for flag in flags.values():
        for ctx in contexts:
            e = evaluate(flag, ctx)
            print(f"{flag['key']:20s} {ctx['key'][:24]:24s} -> {e.value!s:5s} {e.reason}")
    steps, new_flag = plan_enable(flags["workgraph-enabled"], contexts[0]["key"])
    print("\n".join(steps))
