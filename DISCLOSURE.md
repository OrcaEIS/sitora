# SITORA Disclosures and Intended Use

> **Version:** 0.2 — DRAFT for OrcaEIS counsel review. Not yet in force.
> **Status:** This file is placeholder content until ratified. Do not publish
> this repository publicly until this document is countersigned by OrcaEIS
> counsel and its version marker is changed to `1.0` (or later).
>
> **STATUS: SCAFFOLD / DRAFT — NOT AN EXTERNAL COMMITMENT.**
> Specific engineering commitments below require reconciliation and
> founder ratification before they may be quoted in customer contracts,
> marketing pages, warranties, or public statements.

This document consolidates disclosures that apply to the open-core SITORA
framework distributed in this repository. It is intended to be read alongside,
not in place of:

- [`LICENSE`](LICENSE) — the Apache-2.0 license under which this code is
  distributed.
- [`NOTICE`](NOTICE) — attributions and trademark notice.
- [`TRADEMARKS.md`](TRADEMARKS.md) — the full trademark usage policy.
- [`COMMERCIAL_BOUNDARY.md`](COMMERCIAL_BOUNDARY.md) — what is open in SITORA
  and what is delivered commercially by OrcaEIS.
- [`SANDBOX.md`](SANDBOX.md) — the controlled-evaluation trust guarantee for
  the open reference evaluator.
- [`OPERATING_SAFETY.md`](OPERATING_SAFETY.md) — the Governed Production
  Autonomy Doctrine and the buyer-facing Operating Safety Trust Guarantee
  that govern how the OrcaEIS commercial runtime treats production
  environments beyond the open-core boundary.
- [`SECURITY.md`](SECURITY.md) — vulnerability reporting.

If any statement here conflicts with the Apache-2.0 license text, the license
governs the copyright and patent grants. The clarifications below describe how
OrcaEIS intends the framework to be used, understood, and not misrepresented —
they do not enlarge or diminish the license.

---

## 1. What SITORA is

SITORA is an **open-core framework and specification** for representing and
evaluating whether an organization's operational reality remains aligned with
its strategic intent, using attributable evidence and deterministic checks. It
defines:

- schemas for intent, evidence, evaluation, finding, action, and outcome;
- an alignment status taxonomy (Aligned / Drifting / Incomplete / Conflicting /
  Unverifiable) with a defined precedence order;
- a reference evaluator that operates on file-based exported evidence in a
  controlled environment;
- conformance tests and example Alignment Packs.

SITORA is designed for **modeling, testing, extending, and controlled
evaluation** of alignment conditions. It is intended to make alignment
conclusions inspectable and reproducible.

## 2. What SITORA is not

SITORA is **not**:

- an audit opinion, audit report, or substitute for a licensed audit performed
  by a qualified auditor;
- legal, regulatory, compliance, tax, medical, or professional advice;
- a certified GRC platform or a substitute for one;
- a certified compliance solution for any regulatory obligation, including but
  not limited to SOX, HIPAA, GDPR, CCPA, SOC 2, ISO/IEC 27001, ISO/IEC 42001,
  the EU AI Act, the NIST AI Risk Management Framework, or similar frameworks;
- an enterprise production runtime for operating alignment evaluation against
  live systems, credentials, or sensitive evidence at scale.

Findings produced by the open-core SITORA reference evaluator are engineering
outputs computed by deterministic rules from the evidence provided. They are
**not attestations, certifications, or opinions of any kind**, and no party
should represent them as such to auditors, regulators, customers, boards, or
courts without independent professional review.

Enterprise use cases that require credential handling, sensitive-evidence
management, organizational governance workflows, operational deployment at
scale, or scalable remediation orchestration are addressed by the OrcaEIS
commercial runtime, not by this open-core repository. See
[`COMMERCIAL_BOUNDARY.md`](COMMERCIAL_BOUNDARY.md).

## 3. No warranty; no fitness for regulatory reliance

The Apache-2.0 license disclaims warranties in Section 7 and limits liability
in Section 8. Those provisions govern. In addition, and for clarity:

- SITORA is provided **"AS IS,"** without warranty of any kind, express or
  implied, including without limitation any warranty of merchantability,
  fitness for a particular purpose, non-infringement, accuracy, completeness,
  or reliability.
- OrcaEIS does not warrant that SITORA is fit for reliance in connection with
  any specific regulatory, statutory, contractual, or professional obligation.
  Users who rely on SITORA in connection with any such obligation do so at
  their own risk and are solely responsible for validating that reliance with
  qualified counsel, auditors, and other appropriate professionals.
- OrcaEIS does not warrant that outputs of the reference evaluator are
  suitable for submission to any regulator, auditor, court, standards body, or
  contractual counterparty.

Nothing in this document is intended to reduce the protections OrcaEIS enjoys
under the Apache-2.0 license.

## 4. Evidence, data, and legal responsibility of users

Users are **solely responsible** for:

- the lawful collection, handling, storage, transmission, redaction,
  minimization, retention, and disposal of any evidence, records, personal
  data, or other information they load into a SITORA implementation;
- compliance with all applicable data-protection, privacy, sectoral, export
  control, sanctions, employment, and confidentiality laws and regulations,
  including without limitation the GDPR, the UK Data Protection Act, the CCPA
  and CPRA, HIPAA, PIPEDA, LGPD, and any equivalent regime in their
  jurisdiction;
- obtaining any consents, disclosures, contractual rights, and legal bases
  required to process the evidence they choose to use with SITORA;
- ensuring that the deployment environment in which SITORA is operated is
  appropriate for the sensitivity of the evidence being processed.

When the open reference evaluator is executed locally, OrcaEIS does not
receive, transmit, or process user evidence. See [`SANDBOX.md`](SANDBOX.md)
for the controlled-evaluation trust guarantee.

## 5. Intended-use scope

SITORA's open reference evaluator is intended for:

- exploratory modeling of alignment obligations against exported evidence;
- research, teaching, and academic work;
- evaluation of the framework by prospective adopters, contributors, and
  partners;
- internal proof-of-concept work by organizations considering the OrcaEIS
  commercial runtime;
- authoring, testing, and extending Alignment Packs.

SITORA's open reference evaluator is **not intended for**:

- direct enterprise production use against live systems, credentials, or
  regulated data flows;
- automated regulatory submissions or automated audit workflows without
  independent professional review;
- decisions affecting individuals' legal rights, employment, credit, health,
  safety, or access to services, without human review by an appropriately
  qualified decision-maker;
- any use prohibited by applicable law, including Article 5 of the EU AI Act
  or equivalent prohibitions in other jurisdictions.

Users who intend to deploy SITORA-derived work in high-stakes or regulated
contexts should evaluate the OrcaEIS commercial runtime and engage qualified
counsel.

## 5.5 OrcaEIS commercial-runtime safety contract

This section describes the operating boundary that governs how the OrcaEIS
commercial runtime — which is outside the scope of this open-core repository
— treats live production environments. It is included here so that adopters
considering the commercial runtime can understand its safety contract, and so
that the boundary between open-core SITORA (which produces findings only) and
the commercial runtime (which may execute actions under governance) is
documented in a single place.

**Governed Production Autonomy Doctrine.**

> **OrcaEIS is not autonomous by default. OrcaEIS is governed by default, and
> autonomy is earned through evidence, approval, auditability, and verified
> outcomes.**

The OrcaEIS commercial runtime does not modify live production environments
by default. All production engagements begin with controlled evaluation or
read-only observation. Any production write, modification, rollback, policy
deployment, permission adjustment, workflow change, configuration change,
agent constraint update, or remediation execution requires **governed
authorization**, which may take the form of explicit human-in-the-loop
approval, multi-party approval for high-risk action classes, staged approval
through a non-production or shadow environment, a pre-approved and
policy-bounded autonomy envelope for low-risk reversible actions, or
human-directed execution where the runtime provides evidence and instructions
and a human or customer-controlled system performs the change. Production
autonomy is earned, bounded, auditable, reversible where applicable, and
revocable. If evidence freshness, dependency impact, readiness, approval
authority, rollback safety, or governance status cannot be verified, the
runtime defaults to HOLD rather than ALLOW.

**Graduated authority ladder.** The commercial runtime operates on a
graduated authority ladder. The current commercial ceiling is
**Human-Approved Execution**: the runtime may execute production actions
only after explicit named-human approval per action, with independently
auditable approval records, refusal on any unverified action, and post-action
verification against intended state. Broader autonomy modes are documented
as future capability, are not currently offered, and are not part of any
commitment made by OrcaEIS in this document, in the license, in any SITORA
repository, or in any current OrcaEIS commercial-runtime engagement.

**Relationship to open-core SITORA.** SITORA in this repository is a
deterministic evaluation framework that produces findings and
governed-action recommendations. It does **not** execute actions against
live systems. Enterprise adopters who require production-side execution
engage the OrcaEIS commercial runtime under a separate agreement that
incorporates the Governed Production Autonomy Doctrine.

This section is descriptive of the commercial runtime's operating boundary
and does not create warranties or obligations under this open-core license.
See [`OPERATING_SAFETY.md`](OPERATING_SAFETY.md) for the full doctrine text
and for the buyer-facing Operating Safety Trust Guarantee that a customer
CISO, auditor, or regulator may verify against.

## 6. Trademarks

"OrcaEIS," "SITORA," and "OrcaTrain" are trademarks of OrcaEIS. The
Apache-2.0 license grants copyright and patent rights to the code in this
repository — it does **not** grant trademark rights. Permitted and prohibited
uses of the marks are governed by [`TRADEMARKS.md`](TRADEMARKS.md). In
particular, no third party may claim to be "SITORA-certified," "OrcaEIS-
certified," or "official" until a formal certification program is published.

## 7. Patent notice

OrcaEIS holds or is prosecuting patents and patent applications relating to
alignment evaluation, evidence attribution, and related methods. Users should
understand the following:

- **Apache-2.0 patent grant.** Section 3 of the Apache-2.0 license grants a
  patent license from each contributor to the code they contribute, on the
  terms stated in the license. That grant applies to the code in this
  repository as contributed.
- **Commercial-runtime claims.** OrcaEIS retains all patent rights not
  expressly granted by Apache-2.0, including without limitation patent claims
  that read on the OrcaEIS commercial runtime, on enterprise credential and
  sensitive-evidence handling, on organizational governance workflows, on
  scalable remediation orchestration, and on other capabilities outside the
  open-core boundary defined in [`COMMERCIAL_BOUNDARY.md`](COMMERCIAL_BOUNDARY.md).
- **No implied license.** Nothing in this repository, in OrcaEIS marketing or
  documentation, or in any statement by OrcaEIS personnel grants any patent
  license by implication, estoppel, or otherwise beyond what Apache-2.0
  Section 3 expressly grants.
- **Defensive termination.** As stated in Apache-2.0 Section 3, if a user
  initiates patent litigation alleging that SITORA or a contribution
  constitutes direct or contributory patent infringement, that user's patent
  licenses under Apache-2.0 terminate as of the date such litigation is filed.

This notice is provided so users and contributors can make informed decisions.
It is not a threat, and OrcaEIS's default posture toward good-faith adopters,
contributors, and researchers is welcoming.

## 8. AI-assisted use of SITORA

SITORA is designed to make alignment conclusions inspectable even when AI
tools are used elsewhere in an organization's workflow. Users who employ AI
tools (including large language models, agents, or automation platforms) to
generate intent statements, curate evidence, interpret findings, or draft
governed-action recommendations retain full responsibility for:

- the accuracy and lawfulness of AI-generated inputs and outputs used with
  SITORA;
- ensuring that AI-assisted use complies with the user's own AI-governance
  policy, applicable law, and any applicable professional standards;
- human review of any high-stakes decision informed by SITORA outputs.

SITORA's determinism applies to its own evaluation step. It does not extend
determinism or reliability to any AI-assisted step performed by the user.

## 9. Export, sanctions, and jurisdictional matters

Users are responsible for compliance with all applicable export control laws
and economic sanctions in connection with their download, use, modification,
or redistribution of SITORA. OrcaEIS makes no representation that SITORA is
appropriate or available for use in any particular jurisdiction. Users who
access SITORA from other jurisdictions do so on their own initiative and are
responsible for compliance with local law.

## 10. Changes to this document

OrcaEIS may revise this document from time to time. Material changes will be
recorded in [`CHANGELOG.md`](CHANGELOG.md) with the version and date. Users
should consult the version of this document distributed with the release they
are using.

## 11. Contact

Questions about this document may be directed to `legal@orcaeis.com`.
Security vulnerability reports are governed by [`SECURITY.md`](SECURITY.md)
and should be sent to the address listed there, not to the legal address.

---

## Draft-review notes for OrcaEIS counsel

*This section is not part of the disclosure and must be removed before the
version marker is changed to `1.0`.*

Intended coverage of this draft:

1. **§1–2 Intended use and non-use.** Defines what SITORA is and is not so
   downstream users cannot point to OrcaEIS marketing ("audit-ready,"
   "deterministic," "inspectable") to argue the open-core version carries
   commercial-runtime assurances.
2. **§3 No warranty and no regulatory-reliance fitness.** Layers a plain-
   language warranty disclaimer on top of Apache-2.0 §7–8. Counsel to confirm
   the layering does not inadvertently create an implied warranty by
   specifying regulations by name.
3. **§4 Evidence handling responsibility.** Places data-protection compliance
   on the user. Counsel to confirm the list of regimes is representative
   without being exhaustive (LGPD, PIPEDA included; consider adding APPI,
   PDPA, or replacing the list with a generic "applicable data-protection
   regime" formulation).
4. **§5 Intended-use scope.** Names both intended and non-intended uses.
   Counsel to review the "not intended for" list against EU AI Act Article 5
   language and any state-level (Colorado AI Act, NYC Local Law 144)
   obligations that may warrant explicit call-out.
5. **§6 Trademarks.** Cross-references `TRADEMARKS.md`. No new claims here.
6. **§7 Patent notice.** Discloses that OrcaEIS holds/prosecutes patents,
   restates Apache-2.0 §3 grant, reserves claims on commercial runtime,
   restates defensive termination. Counsel to confirm this disclosure is
   consistent with patent-prosecution strategy and does not prejudice pending
   applications. Counsel to confirm whether specific patent or application
   numbers should be listed.
7. **§5.5 OrcaEIS commercial-runtime safety contract.** New in v0.2. States
   the Governed Production Autonomy Doctrine and the near-term commercial
   ceiling (Human-Approved Execution) so open-core adopters understand the
   commercial runtime's operating boundary. Counsel to confirm: (a) that
   describing the commercial runtime's safety contract in this open-core
   disclosure does not inadvertently extend the Apache-2.0 warranty
   disclaimer's coverage in a way that binds the commercial runtime; (b) that
   naming "Human-Approved Execution" as the current commercial ceiling and
   describing broader autonomy modes as "future capability not currently
   offered" is consistent with the marketing and prosecution posture; (c)
   that the six engineering properties of a well-built Level 4 (Human-
   Approved Execution) belong in `OPERATING_SAFETY.md` rather than here.
8. **§8 AI-assisted use.** Novel section. Addresses the case where a user
   employs LLMs or agents around SITORA. Counsel to confirm this framing does
   not create unintended obligations for OrcaEIS's own commercial-runtime AI
   features.
9. **§9 Export and sanctions.** Standard clause. Counsel to confirm scope.
10. **§10–11 Changes and contact.** Placeholder for real contact.

**Placeholders to resolve before ratification:**

- ~~`orcaeis.example` domain references throughout the repository.~~ Resolved: replaced with `orcaeis.com` in the v0.1-alpha release-candidate pass.
- ~~`legal@orcaeis.example` contact.~~ Resolved: `legal@orcaeis.com` set in §11.
- Confirm the correct legal entity name for the copyright notice in `NOTICE`.
- Confirm whether the "SITORA is not a certified…" list in §2 should name any
  additional frameworks that OrcaEIS marketing frequently references.
- Confirm the version marker convention: `0.x` for pre-ratification drafts,
  `1.0` for the first counsel-ratified public version, with material changes
  incrementing appropriately.

**Related repository files this disclosure depends on being current:**

- `TRADEMARKS.md` — must be published in final form.
- `COMMERCIAL_BOUNDARY.md` — must match the current product boundary.
- `SANDBOX.md` — must match the current reference-evaluator behavior.
- `OPERATING_SAFETY.md` — must exist and must contain the full Governed
  Production Autonomy Doctrine, the graduated authority ladder, and the
  buyer-facing Operating Safety Trust Guarantee (currently a v0.1 scaffold;
  engineering properties of a well-built Level 4 pending CTO ratification
  before v0.2).
- `NOTICE` — trademark and attribution block must match.
- `SECURITY.md` — contact must be real.
- `CHANGELOG.md` — must reference DISCLOSURE.md version bumps going forward.

**Not covered here, by design:**

- CLA and DCO — governed by `CONTRIBUTING.md` and `cla/`.
- Governance and stewardship — governed by `GOVERNANCE.md`.
- Vulnerability disclosure — governed by `SECURITY.md`.
- Positive trust guarantees (what SITORA does do) — governed by `SANDBOX.md`
  and the separate Controlled-Evaluation and Sandbox-Safety trust guarantee
  documents.
