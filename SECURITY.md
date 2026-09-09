# Security Policy

## Supported versions

SITORA is in early alpha. Only the latest released version receives security
fixes.

| Version | Supported |
|---|---|
| 0.1.x | Yes |
| < 0.1 | No |

## Reporting a vulnerability

**Do not open a public GitHub issue for security vulnerabilities.**

Report vulnerabilities privately:

- Email: security@orcaeis.com
- Subject line: `[SECURITY] SITORA — <short description>`

Please include:

- A description of the vulnerability and its impact
- Steps to reproduce (proof of concept if possible)
- Affected version / commit
- Any suggested remediation

## Response process

SITORA is an early-alpha, solo-founder-stewarded project. OrcaEIS does not
commit to fixed acknowledgement or triage SLAs at this stage.

1. **Acknowledgement.** OrcaEIS will acknowledge reports as promptly as
   practicable.
2. **Triage and confirmation.** Reports are triaged based on severity,
   impact, and available maintainer capacity.
3. **Remediation and status.** A remediation approach and status updates
   are communicated to the reporter based on severity.
4. Coordinated **public disclosure** after a fix is released, crediting the
   reporter (unless they prefer to remain anonymous).

## Scope

This policy covers the open SITORA repository: schemas, the reference
evaluator, synthetic data, connector interface contracts, and documentation.

The following are **out of scope** for this repository and handled under
the commercial OrcaEIS security program:

- Live enterprise connectors and credential handling
- Behind-the-login evidence collection
- Production evidence storage, retention, or audit trails
- Enterprise deployment infrastructure

If a report touches any out-of-scope area, we will route it to the OrcaEIS
enterprise security team and confirm receipt.

## Security advisory channel

Confirmed vulnerabilities and fixes are published as GitHub Security Advisories
and, where applicable, requested CVE assignment.
