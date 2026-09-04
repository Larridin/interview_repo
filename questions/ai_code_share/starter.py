"""AI Code Share: weekly AI-assisted share of a GitHub repository."""
from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class WeekStats:
    week_start: str      # ISO date of the week's first day, UTC
    commits: int         # commits you chose to count
    ai_assisted: int     # commits with at least one AI co-author trailer
    excluded: int        # commits you chose not to count; why is up to you
    share: float | None  # ai_assisted / commits, None when commits == 0


def ai_code_share(
    owner: str,
    repo: str,
    weeks: int,
    ai_identities: list[str],
    token: str | None = None,
) -> dict[str, Any]:
    """
    Returns:
    {
      "weeks": [WeekStats, ...],                       # oldest first
      "by_author": {"login-or-email": {"commits": int, "ai_assisted": int}},
      "ai_identities_seen": {"Copilot": 41, ...},
      "unmatched_coauthors": ["Some Person <p@example.com>", ...],
    }
    """
    # TODO
    return {}


if __name__ == "__main__":
    owner, repo, weeks = sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 8
    result = ai_code_share(
        owner, repo, weeks,
        ai_identities=["Copilot", "Claude", "Cursor Agent"],
        token=os.environ.get("GITHUB_TOKEN") or None,
    )
    print(result)
