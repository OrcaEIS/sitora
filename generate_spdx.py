"""Generate an SPDX 2.3 JSON SBOM for the SITORA repository.

Reads component data from the CycloneDX sbom.cdx.json and package metadata from
the installed optional dependencies, builds an SPDX 2.3 JSON document with
accurate DEPENDS_ON relationships, and writes sbom.spdx.json.
"""
import json, uuid, re, datetime
from pathlib import Path
import importlib.metadata as md

REPO = Path(__file__).resolve().parent
CDX = json.loads((REPO / "sbom.cdx.json").read_text())

# Component data from the CycloneDX SBOM
components = {c["name"]: c for c in CDX["components"]}

# Derive runtime dependency edges (exclude extras-only markers)
def norm(n): return n.lower().replace("-", "_")
lookup = {norm(d.metadata["Name"]): d for d in md.distributions() if d.metadata["Name"]}
edges = {}
for name in components:
    d = lookup.get(norm(name))
    if not d:
        edges[name] = []
        continue
    deps = []
    for r in (d.metadata.get_all("Requires-Dist") or []):
        if "extra ==" in r or "extra==" in r:
            continue  # optional/test dependency, not a runtime edge
        pkg = re.split(r"[<>=!~;\s]", r, maxsplit=1)[0].strip()
        if norm(pkg) in lookup and lookup[norm(pkg)].metadata["Name"] in components:
            deps.append(lookup[norm(pkg)].metadata["Name"])
    # de-duplicate, preserve order
    edges[name] = list(dict.fromkeys(deps))

def lic_for(c):
    lic = c.get("licenses", [{}])[0]
    if "expression" in lic:
        return lic["expression"]
    l = lic.get("license", {})
    return l.get("id") or l.get("name") or "NOASSERTION"

def purl_for(c):
    return c.get("purl", "")

def download_for(c):
    return f"https://pypi.org/project/{c['name'].lower()}/{c['version']}/"

def spdx_id(name):
    return "SPDXRef-Package-" + re.sub(r"[^A-Za-z0-9.-]", "-", name)

created = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")

packages = []
# Primary package: sitora
packages.append({
    "SPDXID": "SPDXRef-Package-sitora",
    "name": "sitora",
    "versionInfo": "0.1.0",
    "downloadLocation": "https://github.com/OrcaEIS/sitora",
    "filesAnalyzed": False,
    "licenseConcluded": "Apache-2.0",
    "licenseDeclared": "Apache-2.0",
    "copyrightText": "NOASSERTION",
    "supplier": "Organization: OrcaEIS",
    "externalRefs": [{
        "referenceCategory": "PACKAGE-MANAGER",
        "referenceType": "purl",
        "referenceLocator": "pkg:generic/sitora@0.1.0",
    }],
})
# Dependency packages
for name, c in components.items():
    packages.append({
        "SPDXID": spdx_id(name),
        "name": name,
        "versionInfo": c["version"],
        "downloadLocation": download_for(c),
        "filesAnalyzed": False,
        "licenseConcluded": lic_for(c),
        "licenseDeclared": lic_for(c),
        "copyrightText": "NOASSERTION",
        "supplier": "NOASSERTION",
        "externalRefs": [{
            "referenceCategory": "PACKAGE-MANAGER",
            "referenceType": "purl",
            "referenceLocator": purl_for(c),
        }],
    })

relationships = [
    {"spdxElementId": "SPDXRef-DOCUMENT", "relationshipType": "DESCRIBES", "relatedSpdxElement": "SPDXRef-Package-sitora"},
]
# sitora depends on its declared optional deps (jsonschema, pytest)
for dep in ["jsonschema", "pytest"]:
    relationships.append({
        "spdxElementId": "SPDXRef-Package-sitora",
        "relationshipType": "DEPENDS_ON",
        "relatedSpdxElement": spdx_id(dep),
    })
# transitive edges
for name, deps in edges.items():
    for dep in deps:
        relationships.append({
            "spdxElementId": spdx_id(name),
            "relationshipType": "DEPENDS_ON",
            "relatedSpdxElement": spdx_id(dep),
        })

doc = {
    "spdxVersion": "SPDX-2.3",
    "dataLicense": "CC0-1.0",
    "SPDXID": "SPDXRef-DOCUMENT",
    "name": "sitora-0.1.0",
    "documentNamespace": f"https://orcaeis.com/spdx/sitora-0.1.0-{uuid.uuid4()}",
    "creationInfo": {
        "created": created,
        "creators": ["Tool: sitora-sbom-generator-0.1.0", "Organization: OrcaEIS"],
        "licenseListVersion": "3.21",
    },
    "packages": packages,
    "relationships": relationships,
}

(REPO / "sbom.spdx.json").write_text(json.dumps(doc, indent=2))
print(f"Wrote sbom.spdx.json — {len(packages)} packages, {len(relationships)} relationships")
print("Edges:")
for name, deps in edges.items():
    print(f"  {name} -> {deps}")
