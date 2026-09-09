# OPERATING_SAFETY.md — Governed Production Autonomy Doctrine

> **Version:** 0.2 — CTO-ratified engineering commitment for Level 4
> (Human-Approved Execution). Not yet counsel-ratified for external
> publication.
> **Status:** As of v0.2 the six engineering properties of a well-built
> Level 4 are a ratified OrcaEIS commitment and every commercial-runtime
> SOW must be defensible against them. Counsel review still pending before
> the version marker is advanced to `1.0` and this document is published
> or referenced in a public artifact.
>
> **STATUS: SCAFFOLD / DRAFT — NOT AN EXTERNAL COMMITMENT.**
> Specific engineering commitments below require reconciliation and
> founder ratification before they may be quoted in customer contracts,
> marketing pages, warranties, or public statements.

This document defines how the OrcaEIS commercial runtime treats live
production environments. It is the operating-safety companion to:

- [`SANDBOX.md`](SANDBOX.md) — the controlled-evaluation trust guarantee
  for the open reference evaluator, which never touches production;
- [`DISCLOSURE.md`](DISCLOSURE.md) §5.5 — which references this document
  and states its relationship to open-core SITORA;
- [`COMMERCIAL_BOUNDARY.md`](COMMERCIAL_BOUNDARY.md) — which defines what
  is open in SITORA and what is delivered commercially by OrcaEIS.

The open-core SITORA framework in this repository does **not** execute
actions against live systems. The doctrine below applies to the OrcaEIS
commercial runtime, which enterprise adopters engage under a separate
agreement.

---

## 1. Anchor sentence

The following sentence is load-bearing and appears verbatim in every
OrcaEIS artifact that touches production autonomy:

> **OrcaEIS is not autonomous by default. OrcaEIS is governed by default,
> and autonomy is earned through evidence, approval, auditability, and
> verified outcomes.**

---

## 2. Core operating statement

*Observe by default. Recommend with evidence. Execute only by governed
authorization. Escalate when uncertain. Verify after action.*

---

## 3. The Governed Production Autonomy Doctrine

**CTO-ratified interpretation (v0.2).** The doctrine is not the claim
that a human must click every button forever. It is the claim that **no
production authority exists inside OrcaEIS without human-governed
approval, accountability, auditability, and revocation.** Approval may
be delivered as an explicit human decision on a specific action, or as a
pre-approved, narrow, auditable, revocable autonomy envelope for defined
low-risk action classes — but in either case the accountability chain
terminates in a named human, and the authority is revocable.

OrcaEIS does not modify live production environments by default. All
production engagements begin with controlled evaluation or read-only
observation. OrcaEIS may evaluate alignment, detect drift, generate
findings, recommend corrective actions, and prepare remediation plans
without write access.

Any production write, modification, rollback, policy deployment, permission
adjustment, workflow change, configuration change, agent constraint
update, or remediation execution requires **governed authorization**.

Governed authorization may take exactly one of the following forms:

1. **Explicit human-in-the-loop approval** for a specific action.
2. **Multi-party approval** for high-risk or regulated action classes.
3. **Staged approval** through a non-production or shadow environment.
4. **A pre-approved, policy-bounded autonomy envelope** for low-risk,
   reversible, high-frequency actions.
5. **Human-directed execution** where OrcaEIS provides evidence and
   instructions but a human or customer-controlled system performs the
   change.

Production autonomy is earned, bounded, auditable, reversible where
applicable, and revocable. If evidence freshness, dependency impact,
readiness, approval authority, rollback safety, or governance status
cannot be verified, OrcaEIS defaults to **HOLD** rather than ALLOW.

The HOLD-default rule maps to the ALLOW / HOLD / RESTRICT / ESCALATE /
QUARANTINE / DEFER gate decisions defined in the second OrcaEIS
provisional patent application.

---

## 4. The Graduated Authority Ladder

The doctrine is implemented as a seven-level ladder. Each level defines
exactly what OrcaEIS may do to a production environment. Levels 0–4 are
offered today. Levels 5–6 are documented as future capability and are
not part of any current commitment.

| Level | Name | Production authority |
|---|---|---|
| **0** | Sandbox Evaluation | No production access; exported evidence only. |
| **1** | Read-Only Observation | May observe production evidence; no write-back. |
| **2** | Recommendation | May generate findings and recommended actions; no execution. |
| **3** | Staged Change Preparation | May prepare change packages in non-production or shadow review. |
| **4** | Human-Approved Execution | May execute production actions only after explicit named-human approval per action, with independently auditable approval records, refusal on any unverified action, and post-action verification against intended state. |
| 5 | Policy-Bounded Execution (future) | May execute low-risk, reversible actions inside a pre-approved autonomy envelope. |
| 6 | Governed Autonomous Operation (future) | Broader autonomy for narrow reversible action classes with continuous verification, audit, revocation, and named human accountability. |

Levels 5–6 are documented for architectural completeness. They are not
currently offered, not part of any warranty, and not part of any current
customer commitment.

---

## 5. Engineering properties of a well-built Level 4

**[CTO-RATIFIED v0.2 — operating commitment.]**

Level 4 (Human-Approved Execution) is the near-term commercial ceiling.
OrcaEIS builds it to a standard that leaves no question about whether the
system is autonomous. Every OrcaEIS commercial-runtime SOW that operates
at Level 4 must be defensible against all six properties below.

The **six properties** are the ratified vocabulary and the surface a
customer, auditor, or regulator sees. The lettered **acceptance criteria**
under each property are the enforceable engineering detail that every
implementation of the property must satisfy.

---

### Property 1 — Named human approver

Every production action taken by OrcaEIS must identify the specific human
who approved it. Approval is a per-action, non-repudiable record; there
is no anonymous, service-account, or system-of-record approval path.

**Acceptance criteria:**

- **1a. Independently auditable approval record.** The approval record is
  auditable independently of OrcaEIS — a third party (customer auditor,
  regulator, customer's own SIEM) can verify the approval chain without
  OrcaEIS's cooperation. Records are timestamped, non-repudiable, and
  retained at least as long as the action's effects persist.
- **1b. Refuse-on-missing-approval, refusal logged.** Any production
  action attempted without a matching approval record is refused. The
  refusal itself is logged as a first-class audit event and is visible
  to the customer and to OrcaEIS internal review, with the reason for
  refusal recorded.

### Property 2 — Action-class authorization

Approval is tied to a defined action class — a bounded, named set of
specific operations against specific target systems — not to a session,
a user context, or a blanket permission. Batch approvals are permitted
only when the batch is bounded by explicit named criteria and the batch
approval itself is a single reviewable artifact.

**Acceptance criteria:**

- **2a. Approver authority verified at approval time.** At the moment of
  approval, the approver's authority to authorize this action class
  against this target system is verified against the customer's current
  role/authority state, not assumed from prior sessions or cached
  entitlements. Approvals from users whose authority has been revoked,
  suspended, downgraded, or expired are refused.

### Property 3 — Evidence-linked recommendation

Every proposed action links back to (a) the specific SITORA finding that
motivated it, (b) the source evidence underlying that finding, and (c)
the alignment rule the finding was evaluated against. Actions that
cannot produce this three-part link are not eligible for approval.

**Acceptance criteria:**

- **3a. Independently auditable evidence-to-action chain.** The
  finding-evidence-rule linkage attached to each action is auditable
  independently of OrcaEIS. A third party can reconstruct why the
  action was recommended without OrcaEIS's cooperation.

### Property 4 — Pre-execution impact check

Before an approved action executes, OrcaEIS evaluates likely
dependencies, affected systems, cross-system risk, and readiness state.
If the impact check surfaces conditions the original approval did not
contemplate (unexpected downstream systems, changed evidence freshness,
changed dependency graph), the action does not execute; it is returned
to the approver as a re-approval request.

### Property 5 — Rollback or recovery path

Where technically possible, every action defines how it can be reversed
or remediated. For actions where technical rollback is not possible
(irreversible operations against systems that do not support it),
OrcaEIS must define a compensating recovery path (manual runbook,
escalation, forward-fix procedure) and the approver must acknowledge the
irreversibility at approval time.

### Property 6 — Post-action verification

After execution, OrcaEIS verifies whether the action restored alignment
and did not create secondary drift. Verification is required and logged.
If verification fails or cannot be performed, the action's outcome is
flagged as **Unverifiable** under the SITORA precedence taxonomy and
escalated to the approver.

---

**Implementation note.** The six properties are the ratified vocabulary
for v0.2. The five lettered acceptance criteria (1a, 1b, 2a, 3a, plus the
irreversibility acknowledgment in Property 5) are enforceable engineering
detail that every implementation must satisfy; they are not additional
properties in their own right. Any SOW, engagement letter, or trust
assessment that operates at Level 4 is written against the six
properties and audited against both the properties and the criteria.

---

## 6. Relationship to open-core SITORA

SITORA in this repository is a deterministic evaluation framework that
produces findings and governed-action recommendations. SITORA does **not**
execute actions against live systems. The doctrine above applies to the
OrcaEIS commercial runtime, which is delivered under a separate agreement
outside the Apache-2.0 license.

Nothing in this document creates warranties or obligations under the
Apache-2.0 license governing this repository. This document is a
description of the commercial-runtime operating boundary provided for
adopter clarity.

---

## 7. Changes to this document

Material changes to this document will be recorded in
[`CHANGELOG.md`](CHANGELOG.md) with the version and date. Adopters and
customers should consult the version of this document distributed or
referenced in their engagement.

---

## Draft-review notes for OrcaEIS CTO and counsel

*This section is not part of the trust guarantee and must be removed before
the version marker is changed to `1.0`.*

**CTO ratification complete for v0.2 (2026-08-30).**

The six engineering properties and five acceptance criteria in §5 are
ratified as the OrcaEIS Level 4 operating commitment. Ratification
specifically confirmed:

- **Property vocabulary.** Six properties are the customer-facing surface;
  the five acceptance criteria (1a, 1b, 2a, 3a, plus Property 5
  irreversibility acknowledgment) are enforceable engineering detail
  under those properties, not additional top-level properties.
- **Doctrine interpretation.** The "human clicks every button" reading
  is explicitly not the doctrine. The doctrine is: no production
  authority exists without human-governed approval, accountability,
  auditability, and revocation. Approval may be delivered as explicit
  per-action approval or as a pre-approved, narrow, auditable,
  revocable autonomy envelope for defined low-risk action classes.
- **Level 4 as commercial ceiling.** Levels 0–4 are the near-term
  sellable surface. Levels 5–6 are internal roadmap only and are not
  externalized in customer artifacts.

**Follow-up engineering questions carried forward (not blockers for v0.2
commitment, but must be resolved before the first Level 4 SOW is signed):**

- Precise implementation of "independently auditable" (criteria 1a and
  3a): must approval records and evidence-to-action chains land in a
  customer-controlled log store, or is a customer-inspectable
  OrcaEIS-hosted log store sufficient? Default direction: customer-
  controlled or dual-write is the trust-safer answer for CISO buyers.
- Precise implementation of "refusal logged" (criterion 1b): does the
  refusal event land in the customer's system, in OrcaEIS's audit trail,
  or in both? Default direction: both, with the customer copy authoritative.
- Precise implementation of "approver authority verified at approval
  time" (criterion 2a): SSO authority check at the moment of approval,
  role-attestation cadence, or stronger? Default direction: SSO authority
  check at the moment of approval, with a documented staleness bound.
- Post-action verification cadence (Property 6): what counts as
  verification, and how long does OrcaEIS hold the Unverifiable status
  open before escalating?
- Architectural forward-compatibility: v0.2 assumes Level 4 built to
  this standard is architecturally most of the substrate a future Level 5
  (policy-bounded execution) will require. Confirm during Level 5 spike.

**Counsel ratification pending for v1.0:**

- Confirm this document does not, by describing the commercial runtime's
  safety contract, create warranties under the Apache-2.0 license that
  binds the open-core repository.
- Confirm the language "not currently offered, not part of any warranty,
  not part of any current customer commitment" is sufficient to preclude
  a customer or third party from arguing that Levels 5–6 are implicitly
  offered.
- Confirm the anchor sentence and the doctrine are consistent with
  patent-prosecution strategy (particularly the second provisional).
  Both the anchor sentence and the doctrine may themselves be
  patentable governance mechanisms and should be reviewed against the
  patent claims before this document is published in final form.
- Confirm whether this document should include an express reservation
  that the commercial runtime's safety contract is not a substitute for
  the customer's own governance program.
