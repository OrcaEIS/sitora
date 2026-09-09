# SITORA Controlled Evaluation Trust Guarantee

> You do not have to install OrcaEIS in production to test SITORA. You also do
> not need a formal enterprise sandbox.
>
> You can run the open SITORA evaluator against exported evidence in any
> controlled environment you choose — a local machine, virtual machine, offline
> container, private cloud instance, secure internal folder, or formal sandbox.
>
> The SITORA open-core reference evaluator is non-invasive by design. It is
> file-based, deterministic, offline-capable, and inspectable.

## The guarantee

The open SITORA reference evaluator:

1. Never connects to a live enterprise system.
2. Accepts no credentials, tokens, secrets, or API keys.
3. Performs no network I/O of any kind.
4. Does not spawn subprocesses or shells.
5. Contains no live or behind-the-login connector code.
6. Never writes to, mutates, or calls back into any evidence source.
7. Reads only user-provided local files, such as intent, evidence, rules, and
   roster files.
8. Writes only to an explicit, user-selected output path.
9. Runs fully offline with bundled synthetic data.
10. Produces deterministic, inspectable findings with traceable rule results and
    evidence references.

## What this means in practice

A technical buyer, partner, or reviewer can:

- export a small sample of evidence from their own systems,
- place it in a controlled local or isolated workspace,
- run the SITORA evaluator with no network access,
- inspect every finding, rule result, and evidence reference.

The framework never touches production, never holds credentials, never calls
external systems, and never writes back to any evidence source.

## What counts as a controlled environment

A controlled evaluation environment may be:

- a developer laptop,
- a workstation,
- a virtual machine,
- an offline container,
- a temporary private cloud instance,
- a secure internal folder,
- a formal enterprise sandbox,
- or another customer-approved isolated workspace.

A formal sandbox is helpful, but it is not required.

## Why this is a trust boundary

Sandbox-safe evaluation is open. Production integration is commercial.

The open SITORA evaluator is the local, file-based, deterministic,
non-invasive side of the boundary.

Live evidence collection, behind-the-login connectors, credential vaulting,
production integration, governance workflows, evidence management, and
remediation orchestration belong to the commercial OrcaEIS platform.

## Enforcement

This guarantee is mechanically enforced, not merely stated.
`conformance/test_sandbox_safety.py` fails if the evaluator imports or uses any
network, subprocess, connector, cloud-SDK, or credential/secret module; if it
uses `os` for process execution or env/secret access; or if it writes anywhere
except the single allowed output path (`Path(args.out).write_text(...)` in
`cli.py`). It runs on every push via CI:

```bash
python -m pytest -q
```

## See also

- [COMMERCIAL_BOUNDARY.md](COMMERCIAL_BOUNDARY.md) — open vs. commercial matrix
- [docs/open-core-architecture.md](docs/open-core-architecture.md) — open vs. commercial architecture diagram
- [README.md](README.md) — repository overview
