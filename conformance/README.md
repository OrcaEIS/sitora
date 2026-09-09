# SITORA Conformance Suite

An implementation conforms to SITORA v0.1-alpha if it passes the checks below.
The reference evaluator (`/evaluator`) is the canonical passing implementation.

## Conformance requirements

1. **Schema conformance** — inputs and outputs validate against the JSON
   Schemas in `/schemas`.
2. **Determinism** — same input + same rules → same result, every run.
3. **Taxonomy completeness** — uses exactly the five statuses (Aligned,
   Drifting, Incomplete, Conflicting, Unverifiable) and no others.
4. **Precedence** — the worst-case status governs, in order: unverifiable >
   conflicting > incomplete > drifting > aligned.
5. **Provenance** — every finding references the evidence considered.
6. **No unverifiable-as-aligned** — a finding with no attributable evidence is
   never reported as Aligned.

## Test cases

The pytest cases in `test_conformance.py` cover each status and the precedence
rule using the synthetic example data. Run:

```bash
python -m pytest -q
```

## Adding a conformance case

Add a fixture under `fixtures/` and a test in `test_conformance.py` that
asserts the expected status and that the output validates against
`finding.schema.json`.
