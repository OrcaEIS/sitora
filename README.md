# SITORA

Strategic Intent → Operational Reality Alignment.

SITORA is the open-core alignment framework behind
[OrcaEIS](https://orcaeis.com), which provides Continuous Enterprise Alignment
Infrastructure for the AI-operated enterprise. SITORA defines how to represent
and evaluate whether an
organization's operational reality remains aligned with its strategic intent,
using attributable evidence and deterministic checks.

> **Open the alignment framework. Protect the enterprise control plane.**

## The control loop

```
Intent → Evidence → Deterministic Evaluation → Explainable Finding → Governed Action → Auditable Outcome
```

> AI can assist the alignment process. SITORA makes the alignment conclusion
> inspectable.

## Status taxonomy

| Status | Meaning |
|---|---|
| **Aligned** | Available attributable evidence satisfies the configured condition. |
| **Drifting** | Evidence indicates a condition is no longer being met. |
| **Incomplete** | Required evidence or obligation data is missing. |
| **Conflicting** | Relevant evidence sources materially contradict one another. |
| **Unverifiable** | Insufficient attributable evidence to determine the condition. |

## Quickstart

```bash
# Run the bundled synthetic example (Python 3.10+, no dependencies)
python -m evaluator --demo

# Emit findings as JSON
python -m evaluator --demo --json
```

See [examples/training-obligation-alignment/README.md](examples/training-obligation-alignment/README.md)
for the input→output walkthrough. The demo exercises all five statuses.

## Controlled evaluation by design

SITORA's open reference evaluator is non-invasive by design: it reads local
files, writes only to an explicit output path, uses no network access or
credentials, and never writes back to evidence sources. You do not have to
install OrcaEIS in production to test SITORA — and you do not need a formal
sandbox. Run the open evaluator against exported evidence in any controlled
environment you choose. See [SANDBOX.md](SANDBOX.md).

## Repository layout

```
sitora/
├── LICENSE                 # Apache-2.0
├── NOTICE                  # Attributions + trademark notice
├── CONTRIBUTING.md         # CLA + DCO + how to contribute
├── CODE_OF_CONDUCT.md      # Contributor Covenant 2.1
├── SECURITY.md             # Responsible disclosure
├── GOVERNANCE.md           # Decision rights, RFC process, releases
├── ROADMAP.md              # v0.1-alpha → v1.0
├── TRADEMARKS.md           # Mark usage policy
├── COMMERCIAL_BOUNDARY.md  # What is open vs. paid
├── SANDBOX.md              # Controlled evaluation trust guarantee
├── spec/                   # SITORA specification
├── schemas/                # JSON Schemas (intent, evidence, rule, finding, action, outcome)
├── evaluator/              # Reference evaluator (Python)
├── examples/training-obligation-alignment/  # Synthetic demo data + walkthrough
├── alignment-pack-template/ # Reusable generic Alignment Pack structure
├── conformance/            # Conformance tests + sandbox-safety guard
├── connector-contracts/    # Open connector interface contracts
├── rfcs/                   # RFC template + proposals
├── adr/                     # Architecture decision records
└── docs/                    # Documentation index
```

## What is open vs. paid

See [COMMERCIAL_BOUNDARY.md](COMMERCIAL_BOUNDARY.md). In short:

- **Open:** schemas, taxonomy, reference evaluator, synthetic data, connector
  interface contracts, documentation, community extensions.
- **Paid (OrcaEIS):** live enterprise connectors, credential handling,
  behind-login evidence collection, governance workflows, audit-evidence
  management, deployment orchestration, partner certification, and managed
  implementation.

## Contributing

Contributions require a signed CLA under the contribution process. DCO
sign-off is optional and may be requested by maintainers for traceability.
See [CONTRIBUTING.md](CONTRIBUTING.md). Schema and spec changes follow the
[RFC process](rfcs/0000-template.md).

## License

Apache-2.0. See [LICENSE](LICENSE). The project marks "OrcaEIS," "SITORA,"
and "OrcaTrain" are governed by [TRADEMARKS.md](TRADEMARKS.md) and are not
licensed under the Apache-2.0 copyright license.

## Status

v0.1-alpha. Pre-1.0; breaking changes are allowed between minor versions with
a documented migration note. See [ROADMAP.md](ROADMAP.md).
