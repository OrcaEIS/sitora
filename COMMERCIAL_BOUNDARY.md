# SITORA Commercial Boundary

This document defines what is open in the SITORA project and what is
delivered commercially by the OrcaEIS enterprise platform. It exists so
contributors, adopters, and buyers can tell, unambiguously, what they can
inspect, extend, and rely on for free — and what is paid.

## 1. The boundary rule

> **SITORA is the open-core alignment framework and specification. OrcaTrain
> is a commercial application built on SITORA and is not open-sourced in this
> repository.**

> If it helps people understand, model, test, or extend alignment, it can be
> open. If it handles enterprise credentials, sensitive evidence,
> organizational governance, operational deployment, or scalable remediation,
> it belongs in OrcaEIS.

## 2. Open (this repository)

The SITORA foundation is open under Apache-2.0:

- Intent, evidence, evaluation, finding, action, and outcome schemas
- Alignment status taxonomy (Aligned / Drifting / Incomplete / Conflicting /
  Unverifiable)
- Connector interface contracts (the interface; not the enterprise
  implementation)
- Reference evaluator
- Alignment Pack template (generic, reusable structure)
- Synthetic example data
- Sample reports and test fixtures
- Documentation and implementation patterns
- Community extensions

## 3. Protected (OrcaEIS enterprise control plane)

The following are delivered commercially by OrcaEIS and are **not** part of
this repository. Contributions implementing these are out of scope and will
be declined:

- Secure enterprise connectors and credential management
- Behind-the-login evidence collection
- Enterprise knowledge graph orchestration
- Policy mapping and cross-system normalization
- Governance workflows, routing, approvals, and escalations
- Audit-evidence management and retention controls
- Deployment orchestration, enterprise reporting, and administration
- AI-assisted explanations, recommendations, and partner certification
- Verified, supported Alignment Packs and managed implementation services

## 4. Why this boundary

The open project explains and validates the method. The commercial product
handles the difficult enterprise work: secure access, sensitive evidence,
workflow governance, auditability, deployment, and continuous operation.

### Controlled evaluation is open; production integration is commercial

The open SITORA reference evaluator is local, file-based, deterministic, and
non-invasive: it reads only user-provided local files, writes only to an
explicit user-selected output path, uses no network access or credentials, and
never writes back to evidence sources (see [SANDBOX.md](SANDBOX.md)). A buyer
can test SITORA against exported evidence in any controlled environment they
choose — a laptop, VM, offline container, secure internal folder, or formal
sandbox — without installing anything in production.

Live evidence collection, behind-the-login connectors, credential vaulting,
production integration, governance workflows, and write-back / remediation
orchestration belong to the **commercial OrcaEIS platform**. OrcaTrain is a
commercial application built on SITORA.

A public repository alone is not open source; this project ships an explicit
license (Apache-2.0), a contributor agreement (CLA), separate trademark
protection (TRADEMARKS.md), and this boundary document so the open/commercial
line is clear.

## 5. Contributor guidance

- Do **not** submit PRs that implement live enterprise connectors, credential
  handling, or behind-login evidence collection.
- Do submit improvements to schemas, the reference evaluator, synthetic data,
  conformance tests, and documentation.
- If a contribution is on the boundary and you are unsure, open a
  [discussion](https://github.com/OrcaEIS/sitora/discussions) before writing
  code.

## 6. Component classification summary

The OrcaEIS platform includes a set of internal components whose names
are **not** exposed in this open-core repository. This section publishes
the boundary decision for those components in aggregate, so the open/
commercial line is inspectable at the component level as well as at the
feature level.

| Classification | Count | What it means | Where it lives |
|---|---:|---|---|
| **OPEN implementation** | 0 | OrcaEIS-named components with implementations in this repository | — (none) |
| **OPEN-IFC** | 7 | Behavior expressed as a neutral interface contract only (schemas, conformance contracts) | `schemas/`, `connector-contracts/`, `spec/SITORA.md` |
| **BOUNDARY-EXAMPLE** | 5 | Names that may appear in prose in boundary, trademark, or roadmap contexts — not as implemented components | `TRADEMARKS.md`, `COMMERCIAL_BOUNDARY.md`, `ROADMAP.md`, `NOTICE`, `LICENSE`, sample report prose |
| **COMMERCIAL** | 42 | OrcaEIS-named components whose names and implementations remain closed | The commercial OrcaEIS platform |

Counts above reflect the current classification of OrcaEIS Primary Agents,
Global Cross-Layer Agents, and Intelligence Engines against the boundary
rule stated in Section 3.

**Practical rule for contributors:** if an OrcaEIS-named component is not
listed in `spec/SITORA.md` as an open interface or example, treat it as
commercial and out of scope for this repository. See
[`CONTRIBUTING.md`](./CONTRIBUTING.md) §1.1 for the naming discipline
that enforces this rule at contribution time.

## 7. Disclaimer

This document is a strategic and technical boundary statement, not legal
advice or a contract. OrcaEIS reserves the right to evolve the open/commercial
boundary in future versions. Material changes will be documented in the
CHANGELOG and discussed under the RFC process in GOVERNANCE.md.
