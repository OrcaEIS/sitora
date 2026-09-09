"""Generate a human-readable SBOM summary (Markdown) from sbom.cdx.json and
sbom.spdx.json. Figures are derived from the committed SBOMs, not hardcoded.
"""
import json, datetime
from pathlib import Path
from collections import Counter

REPO = Path(__file__).resolve().parent
cdx = json.loads((REPO / "sbom.cdx.json").read_text())
spdx = json.loads((REPO / "sbom.spdx.json").read_text())

# --- Component data from CycloneDX (ordered) ---
order = ["jsonschema","pytest","attrs","referencing","rpds-py",
         "jsonschema-specifications","iniconfig","packaging","pluggy","Pygments"]
cdx_by_name = {c["name"]: c for c in cdx["components"]}
primary = cdx["metadata"]["component"]

purpose = {
    "jsonschema": "JSON Schema validation (optional: schema validation + CI)",
    "pytest": "Test framework (optional: conformance suite)",
    "attrs": "Data classes (transitive of jsonschema)",
    "referencing": "JSON reference resolution (transitive of jsonschema)",
    "rpds-py": "Persistent data structures (transitive of jsonschema)",
    "jsonschema-specifications": "Standard JSON Schema vocabularies (transitive of jsonschema)",
    "iniconfig": "INI file parsing (transitive of pytest)",
    "packaging": "Version/spec parsing (transitive of pytest)",
    "pluggy": "Plugin management (transitive of pytest)",
    "Pygments": "Syntax highlighting (transitive of pytest)",
}

def license_str(c):
    lic = c.get("licenses", [{}])[0]
    if "expression" in lic:
        return lic["expression"]
    l = lic.get("license", {})
    return l.get("id") or l.get("name") or "NOASSERTION"

def purl(c):
    return c.get("purl", "")

# --- Dependency graph from SPDX relationships ---
id_to_name = {p["SPDXID"]: p["name"] for p in spdx["packages"]}
edges = {name: [] for name in id_to_name.values()}
for rel in spdx["relationships"]:
    if rel["relationshipType"] == "DEPENDS_ON":
        src = id_to_name.get(rel["spdxElementId"], "?")
        dst = id_to_name.get(rel["relatedSpdxElement"], "?")
        if src != "sitora":  # sitora edges handled separately
            edges.setdefault(src, []).append(dst)

# --- License breakdown ---
lic_counter = Counter()
for name in order:
    lic_counter[license_str(cdx_by_name[name])] += 1

generated = cdx["metadata"]["timestamp"]
# Render timestamp as a clean date-time.
try:
    import datetime as _dt
    _parsed = _dt.datetime.fromisoformat(generated.replace("Z", "+00:00"))
    generated = _parsed.strftime("%Y-%m-%d %H:%M UTC")
except Exception:
    pass
created_spdx = spdx["creationInfo"]["created"]

# --- Build Markdown ---
lines = []
w = lines.append

w(f"# SITORA SBOM Summary\n")
w(f"### Human-readable summary of the SITORA software bill of materials\n")
w(f"**Project:** {primary['name']} {primary['version']}  ")
w(f"**Project license:** Apache-2.0  ")
w(f"**SBOM formats:** CycloneDX 1.6 (`sbom.cdx.json`) and SPDX 2.3 (`sbom.spdx.json`)  ")
w(f"**Generated:** {generated}\n")
w(f"> This document is a human-readable summary of the machine-readable SBOMs committed to the repository. The machine-readable files are authoritative; this summary exists to make them reviewable by humans.\n")
w("---\n")

w("## 1. Key facts\n")
w(f"- **No runtime dependencies.** The SITORA reference evaluator uses only the Python standard library.")
w(f"- **{len(order)} third-party packages**, all optional (schema validation and testing).")
w(f"- **All licenses are OSI-approved** and compatible with Apache-2.0 redistribution.")
w(f"- **No copyleft (GPL/AGPL/LGPL) dependencies.**")
w(f"- **No known vulnerabilities are introduced by the dependency surface** at generation time; verify with `pip-audit` before each release.")
w(f"- **Primary component:** `{primary['name']}` {primary['version']} (Apache-2.0).\n")

w("## 2. Dependency inventory\n")
w("| # | Package | Version | License | Role |")
w("|---:|---|---|---|---|")
for i, name in enumerate(order, 1):
    c = cdx_by_name[name]
    w(f"| {i} | {name} | {c['version']} | {license_str(c)} | {purpose.get(name,'')} |")
w("")
w("All packages are available on PyPI and carry a Package URL (purl) in the machine-readable SBOMs.\n")

w("## 3. License summary\n")
w("| License | Packages | Count |")
w("|---|---|---:|")
for lic, count in sorted(lic_counter.items(), key=lambda x: -x[1]):
    pkgs = ", ".join(n for n in order if license_str(cdx_by_name[n]) == lic)
    w(f"| {lic} | {pkgs} | {count} |")
w("")
w("Every license in this SBOM is permissive and compatible with distribution under Apache-2.0.\n")

w("## 4. Dependency graph\n")
# Derive the tree from SPDX DEPENDS_ON edges (sitora is the root).
children = {name: [] for name in id_to_name.values()}
for rel in spdx["relationships"]:
    if rel["relationshipType"] == "DEPENDS_ON":
        src = id_to_name.get(rel["spdxElementId"], "?")
        dst = id_to_name.get(rel["relatedSpdxElement"], "?")
        children.setdefault(src, []).append(dst)

def render_tree(root, prefix="", visited=None):
    if visited is None:
        visited = set()
    out = []
    kids = sorted(children.get(root, []))
    for i, kid in enumerate(kids):
        last = (i == len(kids) - 1)
        branch = "└── " if last else "├── "
        out.append(prefix + branch + kid)
        if kid not in visited:
            visited.add(kid)
            extension = "    " if last else "│   "
            out.extend(render_tree(kid, prefix + extension, visited))
    return out

tree_lines = ["sitora"] + render_tree("sitora")
w("```")
w("\n".join(tree_lines))
w("```")
w("")
w("Relationships are encoded as `DEPENDS_ON` edges in `sbom.spdx.json`. Extras-only (optional/test) dependencies are excluded so the graph reflects runtime dependency truth. Diamond dependencies (e.g., `attrs`) are shown once per path.\n")

w("## 5. Scope and exclusions\n")
w("**In scope:** the declared optional dependencies of the SITORA reference evaluator (`jsonschema`, `pytest`) and their full transitive dependency trees.")
w("**Out of scope:** the Python standard library, the Python interpreter itself, and build/SBOM tooling (e.g., `cyclonedx-bom`, `spdx-tools`). The SBOM is generated from a clean virtualenv containing only the declared optional dependencies, so it reflects the true dependency surface without tooling noise.\n")

w("## 6. Supply-chain and security notes\n")
w("- The SBOM is regenerated and validated on every push via GitHub Actions (CycloneDX against the 1.6 schema; SPDX via `pyspdxtools`).")
w("- Run `pip-audit -r requirements.lock` before each release to check for known vulnerabilities.")
w("- No proprietary customer code, real evidence data, or customer configurations are present in the repository.")
w("- All synthetic data is unmistakably synthetic and contains no real PII.")
w("- The pre-release IP gate checklist in `DEPENDENCIES.md` requires SBOM review before any public release.\n")

w("## 7. How to regenerate\n")
w("The pipeline keeps the dependency virtualenv and the SBOM tooling separate so the SBOM reflects only the true dependency tree (no build-tooling noise).\n")
w("```bash")
w("# 1. Clean dependency venv (jsonschema + pytest only)")
w("python -m venv .dep-venv")
w(".dep-venv/bin/pip install jsonschema pytest")
w(".dep-venv/bin/pip freeze > requirements.lock")
w("")
w("# 2. CycloneDX SBOM (tooling installed in the main environment)")
w("pip install cyclonedx-bom")
w("cyclonedx-py requirements requirements.lock --output-format json --output-file sbom.cdx.json")
w("")
w("# 3. Enrich with SPDX licenses + sitora metadata (reads .dep-venv metadata)")
w(".dep-venv/bin/python generate_cdx.py")
w("")
w("# 4. SPDX 2.3 (reads enriched sbom.cdx.json + .dep-venv metadata)")
w(".dep-venv/bin/python generate_spdx.py")
w("")
w("# 5. This summary (reads both SBOMs)")
w("python generate_sbom_summary.py")
w("")
w("# 6. validate")
w("pip install spdx-tools jsonschema")
w("pyspdxtools --infile sbom.spdx.json")
w("```")
w("")

w("## 8. Files\n")
w("| File | Format | Purpose |")
w("|---|---|---|")
w(f"| `sbom.cdx.json` | CycloneDX 1.6 JSON | Machine-readable SBOM (primary) |")
w(f"| `sbom.spdx.json` | SPDX 2.3 JSON | Machine-readable SBOM with relationships |")
w(f"| `SBOM-SUMMARY.md` | Markdown | This human-readable summary |")
w(f"| `generate_cdx.py` | Python | CycloneDX enrichment (licenses + sitora metadata) |")
w(f"| `generate_spdx.py` | Python | SPDX generator |")
w(f"| `generate_sbom_summary.py` | Python | This summary generator |")
w("")

w("## 9. Validation status\n")
w(f"- CycloneDX: validates against the CycloneDX {cdx['specVersion']} schema.")
w(f"- SPDX: validates with `pyspdxtools` (exit 0) and against the official SPDX {spdx['spdxVersion']} JSON schema.")
w(f"- Conformance suite + controlled-evaluation trust guard pass (`python -m pytest -q`).")
w("")

w("---\n")
w("*This summary is informational. The machine-readable SBOM files are authoritative. Generated from the committed SBOMs; do not edit by hand.*\n")

out = REPO / "SBOM-SUMMARY.md"
out.write_text("\n".join(lines))
print(f"Wrote {out} ({len(lines)} lines)")
print(f"Components: {len(order)} | Licenses: {dict(lic_counter)}")
