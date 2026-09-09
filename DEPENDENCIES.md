# Dependencies and Third-Party Attribution

This inventory supports the SITORA Phase 1 IP/dependency gate: every
third-party dependency's license must be verified compatible with Apache-2.0
redistribution, and no proprietary or customer data may enter the repository.

## Runtime dependencies

The SITORA reference evaluator has **no required third-party runtime
dependencies**. It runs on Python 3.10+ using only the standard library.

## Optional dependencies

| Dependency | Purpose | License | Compatible with Apache-2.0? |
|---|---|---|---|
| jsonschema | Schema validation (conformance + CI) | MIT | Yes |
| pytest | Conformance test runner | MIT | Yes |

## SBOM / dependency inventory

Machine-readable SBOMs are committed in two formats:

- [`sbom.cdx.json`](./sbom.cdx.json) — **CycloneDX 1.6** JSON
- [`sbom.spdx.json`](./sbom.spdx.json) — **SPDX 2.3** JSON (with `DEPENDS_ON` relationships)
- [`SBOM-SUMMARY.md`](./SBOM-SUMMARY.md) — human-readable summary of both SBOMs

Both are generated from a clean virtualenv containing only the project's
declared optional dependencies (`jsonschema`, `pytest`) and their transitive
dependencies, so they reflect the true dependency tree without build-tooling
noise. The SPDX variant additionally encodes `DEPENDS_ON` relationships
between packages.

- **Primary package:** `sitora` 0.1.0 (Apache-2.0)
- **10 third-party components**, all OSI-approved and compatible with
  Apache-2.0 redistribution (MIT, BSD-2-Clause, Apache-2.0 OR BSD-2-Clause).
- **No runtime dependencies** — the reference evaluator uses only the Python
  standard library; `jsonschema` and `pytest` are optional (schema validation
  and testing).

Regenerate the SBOMs:

```bash
# 1. Clean dependency venv (jsonschema + pytest only — true dep tree, no tooling)
python -m venv .dep-venv
.dep-venv/bin/pip install jsonschema pytest
.dep-venv/bin/pip freeze > requirements.lock
# 2. CycloneDX (tooling in the main environment)
pip install cyclonedx-bom
cyclonedx-py requirements requirements.lock --output-format json --output-file sbom.cdx.json
# 3. Enrich with SPDX licenses + sitora metadata
.dep-venv/bin/python generate_cdx.py
# 4. SPDX 2.3 (reads enriched sbom.cdx.json + .dep-venv metadata)
.dep-venv/bin/python generate_spdx.py
# 5. human-readable summary
python generate_sbom_summary.py
# 6. validate
pip install spdx-tools jsonschema
pyspdxtools --infile sbom.spdx.json
```

GitHub Actions regenerates and validates both SBOMs (and the summary) on every
push (see `.github/workflows/ci.yml`).

## Pre-release IP gate checklist

Before any public release, confirm:

- [ ] Dependency and license scan of all third-party code and libraries.
- [ ] No proprietary customer code, real evidence data, or customer
      configurations present in the repository.
- [ ] Third-party attribution review (every dependency's license compatible
      with Apache-2.0 redistribution).
- [ ] SBOMs (`sbom.cdx.json`, `sbom.spdx.json`) regenerated and reviewed,
      and every component license verified compatible with Apache-2.0
      redistribution.
- [ ] No copied code, schemas, or content lacking a compatible license or
      attribution.
- [ ] All synthetic data is unmistakably synthetic and contains no real PII
      or customer artifacts.

## Placeholder notice

Domains and URLs in this repository resolved to their canonical values in the
v0.1-alpha release-candidate pass: `orcaeis.com` for OrcaEIS-hosted resources,
`sitora.orcaeis.com` for schema `$id` identifiers, and
`github.com/OrcaEIS/sitora` for the canonical repository. Contact addresses
(`legal@orcaeis.com`, `security@orcaeis.com`, `trademarks@orcaeis.com`,
`conduct@orcaeis.com`) are the real reporting channels. CLA signing URLs
remain manual until a CLA-signing service is adopted (see `CONTRIBUTING.md`).
