# SITORA Reference Evaluator

A minimal, deterministic implementation of the SITORA v0.1-alpha control loop:

```
Intent → Evidence → Deterministic Evaluation → Explainable Finding
```

This is a **reference** implementation. It proves the loop is coherent and
inspectable. It is **not** the commercial OrcaEIS control plane — no live
connectors, no credentials, no sensitive evidence, no governance workflows.
See [../COMMERCIAL_BOUNDARY.md](../COMMERCIAL_BOUNDARY.md).

## Requirements

- Python 3.10+
- No third-party dependencies for the core evaluator.
- Optional schema validation uses `jsonschema` (`pip install jsonschema`).

## Quickstart

Run the bundled synthetic example (no setup required):

```bash
python -m evaluator --demo
```

Run against your own files:

```bash
python -m evaluator \
  --intent   examples/training-obligation-alignment/input/intent.json \
  --evidence examples/training-obligation-alignment/input/evidence.json \
  --rules    examples/training-obligation-alignment/input/rules.json \
  --roster   examples/training-obligation-alignment/input/roster.json
```

Include `--roster` so subjects with no evidence (the **Incomplete** case)
are evaluated. Without it, only subjects that have evidence are evaluated.

Emit findings as JSON:

```bash
python -m evaluator --demo --json --out examples/training-obligation-alignment/output/findings.json
```

## What the demo proves

The synthetic data is designed to exercise all five SITORA statuses:

| Subject | Evidence | Result |
|---|---|---|
| emp-001 | Completed, current, attributable | **Aligned** |
| emp-002 | Completed but expired (2025) | **Drifting** |
| emp-003 | No evidence | **Incomplete** |
| emp-004 | LMS says complete, HRIS says not | **Conflicting** |
| emp-005 | Evidence present but no provenance | **Unverifiable** |

> "Unverifiable" is never treated as "Aligned," and "Incomplete" preserves the
> possibility that the underlying obligation may be satisfied but not
> adequately evidenced.

## Deterministic evaluation

Rules apply declared predicates to defined evidence and produce traceable
results. AI may assist extraction, classification, and explanation elsewhere in
the stack, but the material finding produced here is inspectable and
reproducible: same input + same rules → same result.

## Tests

```bash
python -m pytest -q
```

See [../conformance](../conformance) for conformance-suite requirements.
