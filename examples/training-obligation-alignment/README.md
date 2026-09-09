# Training Obligation Alignment — Synthetic Walkthrough

This is a **reference example** of the SITORA alignment framework applied to a
training-and-compliance obligation. It is unmistakably synthetic — no real
customer data, no real employee identifiers, no credentials. It exists so a
technical buyer can run the reference evaluator and inspect how a SITORA
finding is produced.

> **Open-core boundary:** SITORA is the open-core alignment framework and
> specification. **OrcaTrain** is a commercial application built on SITORA and
> is not open-sourced in this repository. This example is a generic,
> domain-neutral illustration of the framework — it is not the OrcaTrain product.

## The alignment question

> For the privileged-access workforce in 2026-Q1, are required Security
> Awareness Training obligations completed, current, and evidenced in
> authoritative systems?

## Files

| File | Role |
|---|---|
| `input/intent.json` | The strategic intent / obligation |
| `input/evidence.json` | Attributable operational evidence from LMS/HRIS |
| `input/rules.json` | Deterministic evaluation rules |
| `output/findings.json` | Generated findings (run the evaluator to produce) |

## Run it

```bash
# from the repository root
python -m evaluator --demo

# or write findings to the output directory
python -m evaluator --demo --json --out examples/training-obligation-alignment/output/findings.json
```

## Expected outcome

Five subjects, one per SITORA status, so the full taxonomy is exercised:

- **emp-001 → Aligned**: attributable LMS record, completed, current.
- **emp-002 → Drifting**: attributable record, completed but expired (2025).
- **emp-003 → Incomplete**: no evidence present for the obligation.
- **emp-004 → Conflicting**: LMS and HRIS attributable records disagree.
- **emp-005 → Unverifiable**: evidence present but lacks attributable provenance.

## What this proves

The output is not a dashboard. It is an **evidence-backed alignment finding**
with a governed conclusion, traceable rule results, and the evidence
considered for each. That is the core SITORA differentiator.
