"""Enrich the bare CycloneDX SBOM produced by `cyclonedx-py requirements`.

The bare SBOM lists the 10 dependency components with purls but no license
data and no primary (sitora) metadata component. This script reads SPDX
licenses from installed package metadata (PEP 639 License-Expression, falling
back to the License field and License classifiers), adds the sitora primary
component, and writes the enriched sbom.cdx.json back.

Run after:
    cyclonedx-py requirements requirements.lock --output-format json --output-file sbom.cdx.json
"""
import json, uuid, datetime
from pathlib import Path
import importlib.metadata as md

REPO = Path(__file__).resolve().parent
bom = json.loads((REPO / "sbom.cdx.json").read_text())

KNOWN_SPDX = {"MIT","ISC","Apache-2.0","BSD-2-Clause","BSD-3-Clause",
              "MPL-2.0","Python-2.0","LGPL-2.0-or-later"}
SPDX_FROM_CLASSIFIER = {
    "MIT License":"MIT","Apache Software License":"Apache-2.0",
    "BSD License":"BSD-3-Clause","ISC License":"ISC",
    "Python Software Foundation License":"Python-2.0",
    "Mozilla Public License 2.0 (MPL 2.0)":"MPL-2.0",
    "GNU Lesser General Public License v2 or later (LGPLv2+)":"LGPL-2.0-or-later",
}
def norm(n): return n.lower().replace("-", "_")
lookup = {norm(d.metadata["Name"]): d for d in md.distributions() if d.metadata["Name"]}

def license_for(meta):
    lex = (meta.get("License-Expression") or "").strip()
    if lex:
        return ("id", lex)
    lic = (meta.get("License") or "").strip()
    if lic and not lic.startswith("License ::") and len(lic) < 80:
        return ("name", lic)
    for c in (meta.get_all("Classifier") or []):
        if c.startswith("License ::"):
            for k, spdx in SPDX_FROM_CLASSIFIER.items():
                if k in c:
                    return ("id", spdx)
    return None

def homepage(meta):
    for u in (meta.get_all("Project-URL") or []):
        if u.lower().startswith("homepage,"):
            return u.split(",", 1)[-1].strip()
    return None

for c in bom.get("components", []):
    d = lookup.get(norm(c["name"]))
    if not d:
        continue
    meta = d.metadata
    lic = license_for(meta)
    if lic:
        kind, val = lic
        if " OR " in val or " AND " in val:
            c["licenses"] = [{"expression": val}]
        elif val in KNOWN_SPDX and kind == "name":
            c["licenses"] = [{"license": {"id": val}}]
        else:
            c["licenses"] = [{"license": {kind: val}}]
    hp = homepage(meta)
    if hp and "externalReferences" not in c:
        c["externalReferences"] = [{"type": "website", "url": hp}]
    # ensure purl / bom-ref
    if "purl" not in c:
        c["purl"] = f"pkg:pypi/{c['name'].lower()}@{c['version']}"
    if "bom-ref" not in c:
        c["bom-ref"] = c["purl"]

# Primary metadata component: sitora
bom.setdefault("metadata", {})
bom["metadata"]["component"] = {
    "type": "application",
    "name": "sitora",
    "version": "0.1.0",
    "licenses": [{"license": {"id": "Apache-2.0"}}],
    "purl": "pkg:generic/sitora@0.1.0",
    "bom-ref": "pkg:generic/sitora@0.1.0",
    "externalReferences": [{"type": "website", "url": "https://github.com/OrcaEIS/sitora"}],
}
bom["metadata"].setdefault("timestamp", datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z"))
bom["metadata"]["tools"] = [{"vendor": "OrcaEIS", "name": "sitora-sbom-generator", "version": "0.1.0"}]
bom["metadata"]["properties"] = [
    {"name": "sitora:scope", "value": "declared + transitive dependencies of optional dev/schema extras"},
    {"name": "sitora:license", "value": "Apache-2.0"},
    {"name": "sitora:python", "value": ">=3.10"},
    {"name": "sitora:runtime-deps", "value": "none (standard library only)"},
]

(REPO / "sbom.cdx.json").write_text(json.dumps(bom, indent=2))
print(f"Enriched sbom.cdx.json — {len(bom['components'])} components + sitora metadata")
