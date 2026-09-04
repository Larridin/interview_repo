# Feature flag evaluator

Acme's flag service exports flags in the JSON shape in `flags.json`. Write the evaluator, then write the tool that safely turns a flag on for one customer.

## Evaluation semantics

1. If `on` is false, serve `offVariation`.
2. Else if the context's key appears in a `contextTargets` entry of the same `contextKind`, serve that variation.
3. Else walk `rules` in order. A rule matches when all of its clauses match. A clause compares the context attribute named by `attribute` against `values` using `op` (`in`, `startsWith`, `endsWith`, `contains`), inverted when `negate` is true. A missing attribute never matches. The first matching rule serves its `variation` or its `rollout`.
4. Else serve `fallthrough`, which is also a variation or a rollout.

A rollout splits contexts deterministically. Weights sum to 100,000. Compute

```
bucket = int(sha1(f"{flag_key}.{salt}.{context_key}").hexdigest()[:15], 16) / 0xFFFFFFFFFFFFFFF * 100000
```

then walk the weights cumulatively. The same context must land in the same variation on every call.

Contexts look like `{"kind": "org", "key": "b6b1c0e2-...", "plan": "enterprise", "workos_id": "org_01J7YTKQ2M"}`. A sample set is in `contexts.json`.

## Deliverables

1. `evaluate(flag, context)` returning the value, the variation index and a reason.
2. `plan_enable(flag, org_key)` returning the ordered steps and the resulting flag such that, after the steps, `evaluate` returns True for exactly that org and False for every other org. Each intermediate state must also be safe.

`starter.py` has both signatures. Run it with `python starter.py`.

## Follow-ups

- The `contextTargets` list on `capture-enabled` never matches anything in production. Why might that be, and how would your evaluator make it visible?
- Write the test that proves your rollout is fair and stable.
- The client cannot reach the flag service and gets a 429. Your feature is a kill switch for data capture. What does the client do, and who decided?
- How would you lint every flag in the export for the `workgraph-enabled` problem before anyone touches it?
