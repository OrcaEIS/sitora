# ADR 0001 — License, CLA, and Governance Foundation

- **Date:** 2026-08-28
- **Status:** Accepted
- **Deciders:** OrcaEIS steward
- **Related:** COMMERCIAL_BOUNDARY.md, TRADEMARKS.md, CONTRIBUTING.md

## Context

SITORA is the open-core alignment framework behind OrcaEIS. Before accepting
any outside contribution, the project needed an explicit license, a
contributor agreement, and a governance model so the open/commercial boundary
is unambiguous and contributed work can be reused in commercial OrcaEIS
distributions.

## Decision

- **License:** Apache-2.0 for all code and specification artifacts.
- **Contributor agreement:** lightweight individual + corporate CLA, with DCO
  sign-off layered on as an internal traceability convention (not a separate
  contributor hurdle).
- **CLA scope:** explicitly covers patent grants, proprietary
  redistribution, and relicensing by OrcaEIS.
- **Governance:** OrcaEIS-stewarded for v0.x, with public RFCs and a path to
  a technical advisory council once real contributors and adopters exist.
- **Trademarks:** "OrcaEIS," "SITORA," and "OrcaTrain" are governed by a
  separate trademark policy; no third party may claim "certified" status
  until a formal certification program exists.

## Rationale

Apache-2.0 is the most enterprise-friendly, patent-granting permissive license
and avoids the adoption friction of copyleft for an enterprise audience. A CLA
(rather than DCO alone) preserves the right to ship contributed schemas,
evaluator extensions, and Alignment Packs in paid OrcaEIS builds without a
future re-licensing campaign.

## Consequences

- Positive: clear open/commercial boundary; commercial flexibility preserved;
  enterprise-friendly posture.
- Negative: slightly more contributor friction than DCO alone; counsel review
  required for the CLA and trademark policy.
- Neutral: governance will need to evolve toward participatory models as the
  project grows.

## Compliance

The Phase 1 IP/dependency gate (license scan, SBOM, attribution review, no
real customer data) must pass before any public release. The conformance suite
in `/conformance` does not cover licensing; licensing compliance is checked at
release time by the steward.
