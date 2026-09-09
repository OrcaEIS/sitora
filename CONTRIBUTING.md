# Contributing to SITORA

Thank you for your interest in contributing to SITORA — the open-core
alignment framework behind OrcaEIS. This document explains how to
contribute and the agreement every contributor must accept.

> **Open the alignment framework. Protect the enterprise control plane.**
> If it helps people understand, model, test, or extend alignment, it can
> be open. If it handles enterprise credentials, sensitive evidence,
> organizational governance, operational deployment, or scalable
> remediation, it belongs in OrcaEIS and is out of scope for this repo.

## 1. Before you start

- Read [`COMMERCIAL_BOUNDARY.md`](./COMMERCIAL_BOUNDARY.md) so you understand what belongs here versus in the commercial OrcaEIS platform.
- Read [`GOVERNANCE.md`](./GOVERNANCE.md) for decision rights and the RFC process.
- Read [`SECURITY.md`](./SECURITY.md) before any contribution touching secrets, credentials, or evidence handling.

### 1.1 Naming discipline (mandatory)

SITORA uses the neutral vocabulary defined in the SITORA specification
(`spec/SITORA.md`) — for example, *Alignment Engine*, *Governance Engine*,
*Reconciliation Engine*, *Verification Engine*, *Strategic Intent Model*,
*Operational Reality Model*, and the five-status taxonomy (Aligned /
Drifting / Incomplete / Conflicting / Unverifiable).

Contributions must **not** introduce Orca-prefixed component or agent names
into implementation code, module names, class names, function names,
test identifiers, schemas, fixtures, or documentation. Names such as (for
example) *OrcaIdentity*, *OrcaRoles*, *OrcaPermissions*, *OrcaHxM*,
*OrcaGovernance*, *OrcaCompliance*, *OrcaValidate*, or any other
Orca-prefixed component name belong to the commercial OrcaEIS platform
and are out of scope for this repository.

The only Orca-prefixed strings permitted in this repository are:

- **`OrcaEIS`** — the company / trademarked platform, used in trademark,
  attribution, boundary, and license contexts (e.g. `TRADEMARKS.md`,
  `LICENSE`, `NOTICE`, `COMMERCIAL_BOUNDARY.md`).
- **`OrcaTrain`** — the commercial application referenced in trademark
  and boundary contexts and in the ROADMAP as a commercial example. It
  must not appear as an implemented component in this repository.

Contributions that introduce disallowed Orca-prefixed names will be
rejected. The CI naming-discipline check enforces this automatically.

If you believe a specific Orca-prefixed name legitimately belongs in the
open repo (for instance, because the boundary shifted), open an RFC under
`rfcs/` before writing code.

## 2. Contributor License Agreement (CLA)

A signed CLA is required for contributions under the intended contribution
process. SITORA uses a lightweight **individual + corporate CLA** so that
contributed schemas, evaluator extensions, and Alignment Packs can be reused
inside commercial OrcaEIS distributions.

1. Open a pull request. Sign the [Individual CLA](./cla/INDIVIDUAL_CLA.md) or, if contributing on behalf of an employer, the [Corporate CLA](./cla/CORPORATE_CLA.md). CLA templates are included in this repository (`/cla`) as starter text.
2. If your contribution is made on behalf of an employer, a corporate CLA covering the contributing entity is required.
3. The CLA explicitly covers **patent grants**, **proprietary redistribution**, and **relicensing** by OrcaEIS. Review the full text before signing.

> **Provisional templates.** CLA signing is currently manual; a CLA bot or
> signing service is a future improvement. The templates in `/cla` are
> starter/provisional text pending legal review and are not legal advice.
> If you have questions about the agreement, contact legal@orcaeis.com
> before contributing.

## 3. Developer Certificate of Origin (DCO) — optional

In addition to the CLA, maintainers *may* request a `Signed-off-by` line on
commits for internal traceability:

```bash
git commit -s -m "your commit message"
```

DCO sign-off is **optional** and is not a separate contributor hurdle. The
CLA is the required agreement; DCO is an optional traceability convention
maintainers can use at their discretion.

## 4. How to propose a change

- **Small fixes** (typos, docs, minor schema corrections): open a pull
  request directly.
- **Schema or spec changes, new status taxonomy, or breaking changes:**
  follow the [RFC process](./rfcs/0000-template.md). Open an RFC, gather
  feedback, and reach a decision before implementing.
- **Architecture decisions:** record an [ADR](./adr/0000-template.md).

## 5. Pull request checklist

- [ ] CLA signed
- [ ] Commits signed off with `-s` (optional; maintainers may request for traceability)
- [ ] Tests pass: `cd evaluator && python -m pytest`
- [ ] Schemas validate: `python -m jsonschema` (if schemas changed)
- [ ] No real customer data, credentials, or PII
- [ ] Synthetic data is unmistakably synthetic
- [ ] Documentation updated
- [ ] CHANGELOG entry added (if user-facing)

## 6. Code of conduct

Participation in this project is governed by the
[Contributor Covenant Code of Conduct](./CODE_OF_CONDUCT.md). By
participating, you agree to abide by its terms.

## 7. Reporting issues

- Bugs and feature requests: [GitHub Issues](https://github.com/OrcaEIS/sitora/issues)
- Security vulnerabilities: see [SECURITY.md](./SECURITY.md) (do **not**
  open a public issue for security reports).

## 8. Release process

Releases follow [semantic versioning](https://semver.org/). See
[GOVERNANCE.md](./GOVERNANCE.md) §6 for the release cadence and the
maintainer who cuts each release.
