# Who is this desktop user?

Acme installs a desktop agent on every laptop. The agent reports usage under whatever username the operating system gives it. HR gives us a roster. Your job is to connect the two, and to build the reporting tree the numbers roll up through.

## Inputs

- `data/employees.csv`: `email, display_name, desktop_user_id, manager_email, department, deleted_at`. `desktop_user_id` and `deleted_at` may be empty.
- `data/heartbeats.jsonl`: one object per line, `{"device_id", "os", "user_id", "ts"}`.
- `policy.yaml`: the ordered list of matching tiers you must apply. Treat it as configuration you may extend, not a spec you may ignore.

```yaml
case_insensitive: true
tiers:                       # applied in order; first tier with exactly one match wins
  - desktop_user_id_exact
  - email_exact
  - email_local_part         # "jsmith" matches employee jsmith@acme.com by the part before @
  - strip_domain_prefix      # "CORP\jsmith" is treated as "jsmith"
  - punctuation_fold         # ignore . _ - when comparing
refuse_if_ambiguous: true    # a tier that matches two employees matches none
```

## Deliverables

1. The org chart: every root, each employee's depth, and how many active employees are reachable from the roots versus how many are on the roster.
2. Attribution of every distinct heartbeat `user_id` to an employee, with the tier that matched, or a reason it did not.
3. A coverage report per email domain: matched, unmatched, ambiguous.

`starter.py` has the return shape. Run it with `python starter.py`.

## Follow-ups

- Which tiers would you refuse to ship to production, and why?
- Coverage drops from 92% to 40% overnight while every laptop is still checking in. How would you have caught it?
- Tomorrow the agent can be told the user's email at install time. What changes in your code, and what still cannot be fixed that way?
- 50,000 employees and 10 million heartbeats a day. What breaks first?
