# Changelog

All notable changes to SITORA are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project
adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.1.0-alpha-rc2] — 2026-09-09

Public-release cleanup pass on RC1. No architecture, evaluator, schema,
example, taxonomy, or commercial-boundary changes. Dependency inventory and
both SBOMs (CycloneDX 1.6 and SPDX 2.3) are unchanged.

### Removed

- `DISCLOSURE.md` and `OPERATING_SAFETY.md` removed from the public tree.
  Their substantive commercial-runtime content is not relocated elsewhere in
  this repository.

### Changed

- `CONTRIBUTING.md`: removed the statement implying the CLA text has already
  been reviewed by counsel. Preserved the existing statement that the CLA
  templates in `/cla` are starter/provisional text pending legal review.
  Kept the CLA required under the intended contribution process; kept DCO
  sign-off optional (maintainers may request it for traceability).
- `README.md`: corrected the contribution sentence so DCO sign-off is not
  described as mandatory. Contributions require a signed CLA under the
  contribution process; DCO sign-off is optional and may be requested by
  maintainers for traceability.
- `SECURITY.md`: removed the hard commitments to acknowledgement within 2
  business days and triage within 5 business days. Replaced with non-SLA
  language appropriate for a solo-founder alpha project (acknowledge as
  promptly as practicable; triage and remediation based on severity, impact,
  and available maintainer capacity). Private vulnerability-reporting
  requirement and `security@orcaeis.com` preserved.
- `GOVERNANCE.md`: removed the commitment that every issue receives a first
  response within 3 business days and the commitment to review stale issues
  every 30 days. Replaced with steward-based triage keyed to severity,
  impact, relevance, and available maintainer capacity.
- `SBOM-SUMMARY.md`: replaced the assertion that no known vulnerabilities
  are introduced by the dependency surface at generation time with: "The
  SBOM itself does not assert vulnerability status. Run `pip-audit` before
  each release." Dependency inventory unchanged.
- `generate_sbom_summary.py`: updated the corresponding line so future
  regenerations produce the corrected summary.
- `cla/CORPORATE_CLA.md` and `cla/INDIVIDUAL_CLA.md`: reworded the
  consumer-facing `TODO (placeholder)` marker on the legal-entity
  replacement note to `Note (before use)`. Substantive warning and
  legal-review requirement unchanged.

### Validation

- Conformance suite: 16 / 16 passing.
- Sandbox-safety guard: 8 / 8 passing.
- Offline demo emits all five statuses
  (aligned / drifting / incomplete / conflicting / unverifiable).
- Schema and fixture validation: 7 / 7 passing.
- CycloneDX 1.6 schema validation: passing.
- SPDX 2.3 validation (`pyspdxtools`): passing.
- Naming-discipline check: passing (only `OrcaEIS` / `OrcaTrain`).
- Open-core boundary scrub: passing.

## [0.1.0-alpha-rc1] — 2026-09-09

First release candidate for `v0.1.0-alpha`. Frozen as annotated tag
`v0.1.0-alpha-rc1` on commit `370d2273dd14b2ec86425272d98446a1200b11c5`.
Superseded by `v0.1.0-alpha-rc2` for public release cleanup; RC1 is
preserved unchanged for reference.

### Added

- **SITORA Controlled Evaluation Trust Guarantee.** New [`SANDBOX.md`](SANDBOX.md)
  formally states that the open reference evaluator is non-invasive by design:
  never connects to a live enterprise system, accepts no credentials, tokens,
  secrets, or API keys, performs no network I/O, spawns no subprocesses or
  shells, contains no live or behind-the-login connector code, never writes to,
  mutates, or calls back into any evidence source, reads only user-provided
  local files, writes only to an explicit user-selected output path, runs fully
  offline with bundled synthetic data, and produces deterministic, inspectable
  findings. Defines what counts as a controlled environment (laptop, VM,
  offline container, private cloud instance, secure internal folder, or formal
  sandbox — a formal sandbox is helpful but not required).
- **Mechanically enforced guard.** `conformance/test_sandbox_safety.py` fails
  if the evaluator imports or uses any network, subprocess, connector,
  cloud-SDK, or credential/secret module (socket, http, urllib, requests,
  subprocess, ftplib, smtplib, boto3/azure/google, keyring/hvac/secrets,
  importlib, shutil, pickle, etc.); if it uses `os` for process execution or
  env/secret access (`os.system`, `os.environ`, `os.exec*`, `os.spawn*`); or if
  it writes anywhere except the single allowed output path
  (`Path(args.out).write_text(...)` in `cli.py`). Wired as a dedicated CI step.
- README "Controlled evaluation by design" section with the enterprise-adoption
  line: you do not have to install OrcaEIS in production to test SITORA, and you
  do not need a formal sandbox.

### Changed

- [`COMMERCIAL_BOUNDARY.md`](COMMERCIAL_BOUNDARY.md) now makes the boundary
  explicit: the open evaluator is local, file-based, deterministic, and
  non-invasive; live collection, behind-login connectors, credential vaulting,
  production integration, governance workflows, and write-back / remediation
  orchestration belong to commercial OrcaEIS. OrcaTrain remains commercial.
- [`docs/open-core-architecture.md`](docs/open-core-architecture.md) diagram
  expanded: open side (local file-based evaluator, schemas, synthetic data,
  reference alignment packs, conformance tests, sandbox-safety guard) vs.
  commercial side (live connectors, credential vaulting, behind-login
  observation, governance workflows, production evidence management,
  remediation orchestration, enterprise audit controls).
- CI runs the sandbox-safety guard as a named step.
- Renamed `examples/orcatrain-synthetic/` →
  `examples/training-obligation-alignment/` so the open repository does not
  carry the commercial OrcaTrain brand. The synthetic data is unchanged; it is
  now a domain-neutral reference example.
- Removed OrcaTrain branding from the open example, demo help text,
  conformance docs, CI paths, and architecture diagram. OrcaTrain is now noted
  only as a commercial application built on SITORA.
- Regenerated the sample executive alignment report with neutral language and an
  open-core boundary note.
- `COMMERCIAL_BOUNDARY.md` now states explicitly: "SITORA is the open-core
  alignment framework and specification. OrcaTrain is a commercial application
  built on SITORA and is not open-sourced in this repository."

### Added
- `alignment-pack-template/` — a reusable, generic Alignment Pack structure
  (`README.md` + `pack.schema.json`) for configuring repeatable, auditable
  assessments on top of the open SITORA framework.

## [0.1.0] — 2026-08-28

### Added
- SITORA v0.1-alpha specification (control loop, status taxonomy, precedence).
- JSON Schemas: intent, evidence, evaluation-rule, finding, governed-action,
  audit-outcome.
- Reference evaluator (Python 3.10+) with CLI and `--demo` mode.
- Synthetic example data exercising all five SITORA statuses.
- Connector interface contracts (open interface; commercial implementation).
- Conformance test suite (pytest).
- Machine-readable SBOMs in two formats: CycloneDX 1.6 (`sbom.cdx.json`) and
  SPDX 2.3 (`sbom.spdx.json`), with `DEPENDS_ON` relationships in the SPDX
  variant, plus a human-readable `SBOM-SUMMARY.md`.
- Governance docs: LICENSE (Apache-2.0), NOTICE, CONTRIBUTING (CLA + DCO),
  CODE_OF_CONDUCT, SECURITY, GOVERNANCE, ROADMAP, TRADEMARKS,
  COMMERCIAL_BOUNDARY.
- CLA templates (individual + corporate).
- Sample executive alignment report and open-core architecture diagram.
- GitHub Actions CI.
