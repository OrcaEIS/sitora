# Alignment Pack Template

An **Alignment Pack** is a versioned, governed configuration that defines one
specific enterprise alignment question. It is the reusable unit that turns the
open SITORA framework into a repeatable, auditable assessment.

> SITORA is the open-core alignment framework. An Alignment Pack is what you
> configure on top of it. Verified, supported packs and managed implementation
> are commercial (see [COMMERCIAL_BOUNDARY.md](../COMMERCIAL_BOUNDARY.md)); this
> template is the open, generic structure.

## What a pack defines

| Field | Purpose |
|---|---|
| `id`, `version` | Stable pack identifier and semantic version |
| `alignmentQuestion` | The single question this pack answers |
| `intent` | Intent source, authoritative source, obligation id + version |
| `scope` | In-scope population, period, and boundaries |
| `evidenceSources` | Named evidence sources and system-of-record designation |
| `fieldMapping` | How source fields map to SITORA evidence attributes |
| `evaluationRules` | Deterministic rules applied to evidence (references `schemas/evaluation-rule.schema.json`) |
| `thresholds` | Finding thresholds and severity guidance |
| `ownership` | Finding owner, review SLA, exception process |
| `remediationActions` | Remediation action templates per status |
| `evidenceRetention` | Retention and audit-output expectations |
| `reportOutputs` | Executive and audit report formats |

## How to use

1. Copy this directory: `cp -r alignment-pack-template/ my-pack/`
2. Edit `pack.json` — fill the `TODO` placeholders.
3. Add concrete `intent.json`, `evidence.json`, `rules.json` (see
   [`../schemas/`](../schemas/) and the worked example in
   [`../examples/training-obligation-alignment/`](../examples/training-obligation-alignment/)).
4. Run the evaluator against your pack files:

```bash
python -m evaluator \
  --intent   my-pack/intent.json \
  --evidence my-pack/evidence.json \
  --rules    my-pack/rules.json \
  --roster   my-pack/roster.json
```

## Conformance

A pack is well-formed when its `intent`, `evidence`, `rules`, `findings`,
`governed-actions`, and `audit-outcomes` all validate against the corresponding
schemas in [`../schemas/`](../schemas/). Run the conformance suite to verify:

```bash
python -m pytest -q
```
