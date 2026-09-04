# Staged rollout planner

Acme ships a desktop agent to thousands of laptops. Releases are published on GitHub. An operator controls who gets what through a rollout config. Write the planner that decides, for every device, which version it should be on and why.

## Inputs

- Release catalog: `GET https://api.github.com/repos/{owner}/{repo}/releases`. Each release has `tag_name`, `prerelease`, `draft`, `published_at` and `assets[].name`. Docs: https://docs.github.com/en/rest/releases/releases. Use `cli/cli`. A `GITHUB_TOKEN` in `.env` is optional for this one.
- `fleet.csv`: `device_id, org_id, os, arch, current_version, ring`
- `rollout.yaml`:

```yaml
channel: stable            # stable excludes prereleases; beta includes them
security_floor: v2.98.0    # every device must be at least here, whatever its ring says
rings:
  canary: {release: v2.100.0, percent: 100}
  early:  {release: v2.100.0, percent: 25}
  broad:  {release: v2.99.0,  percent: 100}
paused: [broad]
```

## Rules

- A device only ever moves to a release that has an asset for its os and arch.
- Cohort membership for a percentage is a pure function of the device and the ring. Raising 25 to 50 must keep every device that was already in.
- Never plan a downgrade. Never plan a move for a paused ring unless the floor requires it.
- Every decision carries a reason.

`starter.py` has the types. Run it with `python starter.py`.

## Follow-ups

- Devices report `APPLIED` or `FAILED` after each move. Design the health rule that pauses a ring automatically. What does a 100% failure rate on one device mean?
- The operator sets `security_floor` to the same release the canary ring is on. Walk through your planner. Is that what the operator wanted?
- When is the planner allowed to promote a ring to the next stage?
- What does the device verify before applying what you planned?
