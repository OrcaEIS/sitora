# SITORA Specification — v0.1-alpha

**SITORA** = **S**trategic **I**ntent **T**o **O**perational **R**eality
**A**lignment.

SITORA is the open-core alignment framework behind OrcaEIS. It defines how
to represent and evaluate whether an organization's operational reality
remains aligned with its strategic intent, using attributable evidence and
deterministic checks.

## 1. The control loop

SITORA evaluates a single alignment question through a deterministic loop:

```
Intent → Evidence → Deterministic Evaluation → Explainable Finding → Governed Action → Auditable Outcome
```

- **Intent** is represented as a versioned, attributable, scoped requirement —
  not prose in a policy document.
- **Evidence** retains source, provenance, time, access context, and relevance.
- **Deterministic evaluation** applies declared rules to defined evidence and
  produces traceable results. AI may assist with extraction, classification,
  explanation, and recommendations, but material findings remain inspectable and
  reproducible.
- **Explainable findings** show why the system reached a conclusion, including
  the evidence considered and the rules applied.
- **Governed action** creates ownership, escalation, approvals, exception
  handling, and remediation.
- **Auditable outcomes** capture what happened after the finding, including
  resolution evidence and historical traceability.

> AI can assist the alignment process. SITORA makes the alignment conclusion
> inspectable.

## 2. Status taxonomy (v0.1)

Every finding has exactly one status:

| Status | Meaning |
|---|---|
| **Aligned** | Available attributable evidence satisfies the configured condition. |
| **Drifting** | Evidence indicates a condition is no longer being met, or is trending toward nonconformance. |
| **Incomplete** | Required evidence, obligation data, ownership information, or other material inputs are missing. |
| **Conflicting** | Relevant evidence sources materially contradict one another. |
| **Unverifiable** | There is insufficient attributable evidence to determine whether the condition is met. |

> "Unverifiable" must never be treated as "Aligned." "Incomplete" preserves the
> possibility that the underlying obligation may be satisfied but not
> adequately evidenced.

## 3. Evaluation precedence

When multiple conditions apply to a single scope, the worst (most severe)
status governs, in this precedence order:

1. Unverifiable
2. Conflicting
3. Incomplete
4. Drifting
5. Aligned

Rationale: a finding cannot be "Aligned" if the evidence is missing,
contradictory, or unverifiable. See `/conformance` for codified tests.

## 4. Future dimensions (v0.2+)

Planned, not yet in v0.1:

- **Alignment status** — aligned, drifting, conflicting.
- **Evidence sufficiency** — sufficient, incomplete, unverifiable.
- **Materiality** — informational, moderate, high, critical.
- **Confidence** — deterministic, corroborated, provisional.

This will let SITORA express findings like:

> The control is provisionally aligned, but evidence coverage is incomplete
> and confidence is insufficient for audit reliance.

## 5. Artifacts

| Artifact | Schema | Location |
|---|---|---|
| Intent | `schemas/intent.schema.json` | `/schemas` |
| Evidence | `schemas/evidence.schema.json` | `/schemas` |
| Evaluation rule | `schemas/evaluation-rule.schema.json` | `/schemas` |
| Finding | `schemas/finding.schema.json` | `/schemas` |
| Governed action | `schemas/governed-action.schema.json` | `/schemas` |
| Audit outcome | `schemas/audit-outcome.schema.json` | `/schemas` |

## 6. Normative references

- [Semantic Versioning 2.0.0](https://semver.org/)
- [JSON Schema](https://json-schema.org/)
- [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## 7. Conformance

An implementation conforms to SITORA v0.1-alpha if it:

1. Accepts input conforming to the intent and evidence schemas.
2. Applies evaluation rules deterministically (same input + same rules → same
   result).
3. Produces findings using exactly the five statuses above, with precedence
   per §3.
4. Emits evidence provenance for every finding.
5. Passes the conformance suite in `/conformance`.

## 8. Versioning and stability

SITORA is v0.1-alpha. Breaking changes are allowed between minor versions
with a documented migration note. Stability commitments apply from v1.0.
