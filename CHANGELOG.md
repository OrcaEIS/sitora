# Changelog

All notable changes to SITORA are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project
adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

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
