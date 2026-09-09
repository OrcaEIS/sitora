# SITORA SBOM Summary

### Human-readable summary of the SITORA software bill of materials

**Project:** sitora 0.1.0  
**Project license:** Apache-2.0  
**SBOM formats:** CycloneDX 1.6 (`sbom.cdx.json`) and SPDX 2.3 (`sbom.spdx.json`)  
**Generated:** 2026-09-09 00:04 UTC

> This document is a human-readable summary of the machine-readable SBOMs committed to the repository. The machine-readable files are authoritative; this summary exists to make them reviewable by humans.

---

## 1. Key facts

- **No runtime dependencies.** The SITORA reference evaluator uses only the Python standard library.
- **10 third-party packages**, all optional (schema validation and testing).
- **All licenses are OSI-approved** and compatible with Apache-2.0 redistribution.
- **No copyleft (GPL/AGPL/LGPL) dependencies.**
- **The SBOM itself does not assert vulnerability status.** Run `pip-audit` before each release.
- **Primary component:** `sitora` 0.1.0 (Apache-2.0).

## 2. Dependency inventory

| # | Package | Version | License | Role |
|---:|---|---|---|---|
| 1 | jsonschema | 4.26.0 | MIT | JSON Schema validation (optional: schema validation + CI) |
| 2 | pytest | 9.1.1 | MIT | Test framework (optional: conformance suite) |
| 3 | attrs | 26.1.0 | MIT | Data classes (transitive of jsonschema) |
| 4 | referencing | 0.37.0 | MIT | JSON reference resolution (transitive of jsonschema) |
| 5 | rpds-py | 2026.6.3 | MIT | Persistent data structures (transitive of jsonschema) |
| 6 | jsonschema-specifications | 2025.9.1 | MIT | Standard JSON Schema vocabularies (transitive of jsonschema) |
| 7 | iniconfig | 2.3.0 | MIT | INI file parsing (transitive of pytest) |
| 8 | packaging | 26.3 | Apache-2.0 OR BSD-2-Clause | Version/spec parsing (transitive of pytest) |
| 9 | pluggy | 1.6.0 | MIT | Plugin management (transitive of pytest) |
| 10 | Pygments | 2.21.0 | BSD-2-Clause | Syntax highlighting (transitive of pytest) |

All packages are available on PyPI and carry a Package URL (purl) in the machine-readable SBOMs.

## 3. License summary

| License | Packages | Count |
|---|---|---:|
| MIT | jsonschema, pytest, attrs, referencing, rpds-py, jsonschema-specifications, iniconfig, pluggy | 8 |
| Apache-2.0 OR BSD-2-Clause | packaging | 1 |
| BSD-2-Clause | Pygments | 1 |

Every license in this SBOM is permissive and compatible with distribution under Apache-2.0.

## 4. Dependency graph

```
sitora
├── jsonschema
│   ├── attrs
│   ├── jsonschema-specifications
│   │   └── referencing
│   │       ├── attrs
│   │       └── rpds-py
│   ├── referencing
│   └── rpds-py
└── pytest
    ├── Pygments
    ├── iniconfig
    ├── packaging
    └── pluggy
```

Relationships are encoded as `DEPENDS_ON` edges in `sbom.spdx.json`. Extras-only (optional/test) dependencies are excluded so the graph reflects runtime dependency truth. Diamond dependencies (e.g., `attrs`) are shown once per path.

## 5. Scope and exclusions

**In scope:** the declared optional dependencies of the SITORA reference evaluator (`jsonschema`, `pytest`) and their full transitive dependency trees.
**Out of scope:** the Python standard library, the Python interpreter itself, and build/SBOM tooling (e.g., `cyclonedx-bom`, `spdx-tools`). The SBOM is generated from a clean virtualenv containing only the declared optional dependencies, so it reflects the true dependency surface without tooling noise.

## 6. Supply-chain and security notes

- The SBOM is regenerated and validated on every push via GitHub Actions (CycloneDX against the 1.6 schema; SPDX via `pyspdxtools`).
- Run `pip-audit -r requirements.lock` before each release to check for known vulnerabilities.
- No proprietary customer code, real evidence data, or customer configurations are present in the repository.
- All synthetic data is unmistakably synthetic and contains no real PII.
- The pre-release IP gate checklist in `DEPENDENCIES.md` requires SBOM review before any public release.

## 7. How to regenerate

The pipeline keeps the dependency virtualenv and the SBOM tooling separate so the SBOM reflects only the true dependency tree (no build-tooling noise).

```bash
# 1. Clean dependency venv (jsonschema + pytest only)
python -m venv .dep-venv
.dep-venv/bin/pip install jsonschema pytest
.dep-venv/bin/pip freeze > requirements.lock

# 2. CycloneDX SBOM (tooling installed in the main environment)
pip install cyclonedx-bom
cyclonedx-py requirements requirements.lock --output-format json --output-file sbom.cdx.json

# 3. Enrich with SPDX licenses + sitora metadata (reads .dep-venv metadata)
.dep-venv/bin/python generate_cdx.py

# 4. SPDX 2.3 (reads enriched sbom.cdx.json + .dep-venv metadata)
.dep-venv/bin/python generate_spdx.py

# 5. This summary (reads both SBOMs)
python generate_sbom_summary.py

# 6. validate
pip install spdx-tools jsonschema
pyspdxtools --infile sbom.spdx.json
```

## 8. Files

| File | Format | Purpose |
|---|---|---|
| `sbom.cdx.json` | CycloneDX 1.6 JSON | Machine-readable SBOM (primary) |
| `sbom.spdx.json` | SPDX 2.3 JSON | Machine-readable SBOM with relationships |
| `SBOM-SUMMARY.md` | Markdown | This human-readable summary |
| `generate_cdx.py` | Python | CycloneDX enrichment (licenses + sitora metadata) |
| `generate_spdx.py` | Python | SPDX generator |
| `generate_sbom_summary.py` | Python | This summary generator |

## 9. Validation status

- CycloneDX: validates against the CycloneDX 1.6 schema.
- SPDX: validates with `pyspdxtools` (exit 0) and against the official SPDX SPDX-2.3 JSON schema.
- Conformance suite + controlled-evaluation trust guard pass (`python -m pytest -q`).

---

*This summary is informational. The machine-readable SBOM files are authoritative. Generated from the committed SBOMs; do not edit by hand.*
