# SITORA Roadmap

This roadmap is indicative, not a commitment. Items may be reordered based on
design-partner and community feedback. Versions follow semantic versioning.

## Current

### v0.1-alpha (Phase 1)

- Intent, evidence, evaluation-rule, finding, governed-action, audit-outcome
  JSON schemas
- SITORA status taxonomy: Aligned / Drifting / Incomplete / Conflicting /
  Unverifiable
- Reference evaluator (Python) with local quickstart
- Synthetic demo data + input→output walkthrough
- Sample executive alignment report
- Connector interface contract (interface only)
- Full governance and legal scaffolding (LICENSE, CLA, SECURITY, TRADEMARKS,
  COMMERCIAL_BOUNDARY)

## Next

### v0.2 (Phase 3–4)

- Refined taxonomy with separate dimensions: alignment status, evidence
  sufficiency, materiality, confidence
- Conformance test suite for evaluators and Alignment Packs
- First community-contributed schema extensions
- Improved reference evaluator (rule composition, evidence provenance)

### v0.5 (Phase 5)

- Stabilized schemas (breaking changes require deprecation path)
- Contributor and maintainer model formalized
- Formal security advisory process
- Alignment Pack packaging format

## Future

### v1.0 (Year 2)

- Stability commitments and deprecation policy
- Technical advisory council
- Optional vendor-neutral foundation evaluation

## How to influence the roadmap

Open an [RFC](./rfcs/0000-template.md) describing the problem and proposed
direction. Roadmap changes are discussed in GitHub Discussions and decided by
the steward per [GOVERNANCE.md](./GOVERNANCE.md).
