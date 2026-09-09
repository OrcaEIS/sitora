# SITORA Governance

This document defines how decisions are made in the SITORA open-core
project. SITORA is stewarded by OrcaEIS. The project is not a neutral
foundation; OrcaEIS acts as steward and final decision authority for all
v0.x releases. Governance will evolve toward a more participatory model
only after real contributors, design partners, and enterprise adopters
exist (see §7).

## 1. Roles

| Role | Who | Authority |
|---|---|---|
| Steward | OrcaEIS | Final decision authority for v0.x; roadmap owner |
| Maintainer | Trusted contributors appointed by the steward | Merge rights, issue triage, release cuts in their area |
| Contributor | Anyone with a signed CLA and accepted contributions | Propose changes, open RFCs, review |
| Participant | Anyone using or discussing SITORA | File issues, comment on RFCs |

## 2. Decision rights

| Change type | Decision path |
|---|---|
| Typo, doc fix, non-breaking minor change | Maintainer approval via PR |
| New schema field, new status value, non-breaking addition | RFC → maintainer review → steward approval |
| Breaking change to a released schema or the taxonomy | RFC → advisory review → steward approval |
| Governance, license, or trademark change | Steward decision, documented in an ADR |

## 3. RFC process

Schema and specification changes flow through the [RFC process](./rfcs/0000-template.md):

1. **Propose:** author opens an RFC document in `/rfcs`.
2. **Review:** community and maintainers provide feedback.
3. **Decision:** the steward (or delegated maintainer) accepts, rejects, or
   defers. The decision and rationale are recorded in the RFC.
4. **Implement:** once accepted, implementation proceeds via PR.
5. **Document:** the outcome is reflected in the spec and CHANGELOG.

## 4. Issue triage

- Issues are triaged by the steward based on severity, impact, relevance,
  and available maintainer capacity. No fixed response or review cadence is
  committed at this stage of the project.
- Labels: `bug`, `enhancement`, `schema`, `spec`, `security`, `question`,
  `good first issue`.
- A maintainer is assigned per issue when capacity allows.

## 5. Security disclosure

See [SECURITY.md](./SECURITY.md). Security issues are handled privately and are
never tracked as public issues until a fix is released.

## 6. Releases

- SITORA follows [semantic versioning](https://semver.org/).
  - **0.x:** pre-1.0; breaking changes allowed with a minor version bump and a
    migration note.
  - **1.0+:** stability commitments apply (see ROADMAP.md).
- Target cadence: one minor release every 6–8 weeks during active development.
- Each release is tagged, includes a CHANGELOG entry, and is announced in
  GitHub Discussions.

## 7. Governance evolution

SITORA will move toward a more participatory model in phases:

- **Phase 1–4 (now):** OrcaEIS-stewarded. The steward owns the roadmap and
  final decisions. RFCs are public for transparency.
- **Phase 5:** a **technical advisory council** is convened from design
  partners and credible external practitioners. A maintainer nomination
  process is published.
- **Year 2:** if adoption and contributor base justify it, scope whether
  SITORA should move toward a vendor-neutral foundation. This is earned, not
  declared.

## 8. Code of conduct

All participants are bound by the [Code of Conduct](./CODE_OF_CONDUCT.md).
Governance decisions are made independently of enforcement, but violations
may affect participation.
