"""SITORA sandbox-safety trust guarantee guard.

Enforces that the open SITORA reference evaluator is non-invasive by design.
The guarantee (see SANDBOX.md) is mechanical, not merely stated: this test
fails if any evaluator source file imports a network, subprocess, connector,
cloud-SDK, or credential/secret module, or uses ``os`` for process execution or
env/secret access, or writes anywhere except the single allowed output path
(``Path(args.out).write_text(...)`` in ``cli.py``).

Scope: this guard covers every Python file under ``evaluator/``. It does not
inspect SBOM generators, conformance tests, or other repository scripts — the
guarranty applies to the open reference evaluator a buyer actually runs.
"""
from __future__ import annotations

import ast
from pathlib import Path

import pytest

EVAL_DIR = Path(__file__).resolve().parent.parent / "evaluator"

# Top-level modules that would violate the sandbox-safety guarantee. Covers the
# explicit denylist (socket, http.client, urllib, requests, subprocess,
# ftplib, smtplib) plus cloud SDKs, credential/secret SDKs, file/process
# side-effect modules, and common network/protocol libraries.
DISALLOWED_TOPLEVEL: frozenset[str] = frozenset(
    {
        # network / protocols
        "socket", "ssl", "http", "urllib", "urllib3", "requests", "httpx",
        "aiohttp", "websocket", "websockets", "telnetlib", "ftplib", "smtplib",
        "poplib", "imaplib", "nntplib", "xmlrpc", "paho",
        # process execution
        "subprocess",
        # cloud SDKs
        "boto3", "botocore", "azure", "google", "googleapiclient", "oci",
        "kubernetes", "docker", "paramiko", "fabric", "asyncssh", "pysftp",
        # credential / secret / env SDKs
        "keyring", "hvac", "secrets", "jwt", "pyjwt", "getpass", "netrc",
        "dotenv",
        # file / process side-effect modules
        "shutil", "pickle",
        # dynamic import bypass
        "importlib",
    }
)

# Substrings that indicate a connector module even when the top-level name is
# not in the denylist above.
DISALLOWED_SUBSTRINGS: tuple[str, ...] = ("connector",)

# os.* attributes that perform process execution, env/secret access, or writes.
DANGEROUS_OS_ATTRS: frozenset[str] = frozenset(
    {
        "system", "popen", "popen2", "popen3", "popen4",
        "spawnl", "spawnle", "spawnlp", "spawnlpe", "spawnv", "spawnve",
        "spawnvp", "spawnvpe",
        "execl", "execle", "execlp", "execlpe", "execv", "execve", "execvp",
        "execvpe", "fork",
        "environ", "getenv",
        "replace", "rename", "remove", "unlink", "rmdir", "mkdir", "makedirs",
    }
)

WRITE_METHODS: frozenset[str] = frozenset({"write_text", "write_bytes", "write"})
SHUTIL_WRITE: frozenset[str] = frozenset(
    {"copy", "copy2", "copyfile", "copytree", "move", "rmtree"}
)
CLI_FILE_NAME = "cli.py"
ALLOWED_WRITE_ATTR = "write_text"  # only this write primitive, to args.out, in cli.py


def _top_level(module: str | None) -> str | None:
    return module.split(".")[0] if module else None


def _import_violations(tree: ast.AST) -> list[str]:
    """Disallowed imports (top-level denylist or connector-like substrings)."""
    violations: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                name = alias.name
                top = _top_level(name)
                if top in DISALLOWED_TOPLEVEL:
                    violations.append(f"disallowed import '{name}'")
                elif any(sub in name.lower() for sub in DISALLOWED_SUBSTRINGS):
                    violations.append(f"connector-like import '{name}'")
        elif isinstance(node, ast.ImportFrom):
            # Skip relative (intra-package) imports — level > 0.
            if node.level and node.level > 0:
                continue
            module = node.module or ""
            top = _top_level(module)
            if top in DISALLOWED_TOPLEVEL:
                violations.append(f"disallowed import '{module}'")
            elif any(sub in module.lower() for sub in DISALLOWED_SUBSTRINGS):
                violations.append(f"connector-like import '{module}'")
            for alias in node.names:
                full = f"{module}.{alias.name}" if module else alias.name
                if any(sub in full.lower() for sub in DISALLOWED_SUBSTRINGS):
                    violations.append(f"connector-like import '{full}'")
    return violations


def _references_args_out(node: ast.AST) -> bool:
    """True if the subtree contains an ``args.out`` attribute reference."""
    for n in ast.walk(node):
        if (
            isinstance(n, ast.Attribute)
            and n.attr == "out"
            and isinstance(n.value, ast.Name)
            and n.value.id == "args"
        ):
            return True
    return False


def _is_whitelisted_write(func: ast.Attribute, file_name: str) -> bool:
    """The only allowed write: ``write_text`` to ``args.out`` in ``cli.py``."""
    return (
        file_name == CLI_FILE_NAME
        and func.attr == ALLOWED_WRITE_ATTR
        and _references_args_out(func.value)
    )


def _usage_violations(tree: ast.AST, file_name: str) -> list[str]:
    """Dangerous os.* usage, dynamic import, and non-whitelisted writes."""
    violations: list[str] = []
    for node in ast.walk(tree):
        # os.<dangerous> access (read or call) — process exec, env/secret, writes
        if isinstance(node, ast.Attribute):
            if (
                isinstance(node.value, ast.Name)
                and node.value.id == "os"
                and node.attr in DANGEROUS_OS_ATTRS
            ):
                violations.append(f"os.{node.attr} access")
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        # open(path, mode) in a write mode (w / a / x / +)
        if isinstance(func, ast.Name) and func.id == "open":
            if len(node.args) >= 2 and isinstance(node.args[1], ast.Constant):
                mode = node.args[1].value
                if isinstance(mode, str) and any(
                    c in mode for c in ("w", "a", "x", "+")
                ):
                    violations.append("open() in a write/append/create mode")
        # json.dump / pickle.dump write to a file object
        if isinstance(func, ast.Attribute) and func.attr == "dump":
            if isinstance(func.value, ast.Name) and func.value.id in ("json", "pickle"):
                violations.append(f"{func.value.id}.dump() writes to a file object")
        # shutil write/remove functions
        if isinstance(func, ast.Attribute) and func.attr in SHUTIL_WRITE:
            if isinstance(func.value, ast.Name) and func.value.id == "shutil":
                violations.append(f"shutil.{func.attr}()")
        # method writes: .write_text / .write_bytes / .write
        if isinstance(func, ast.Attribute) and func.attr in WRITE_METHODS:
            if _is_whitelisted_write(func, file_name):
                continue
            violations.append(f".{func.attr}() write outside the allowed output path")
        # dynamic import bypass
        if isinstance(func, ast.Name) and func.id == "__import__":
            violations.append("dynamic __import__() call")
        if (
            isinstance(func, ast.Attribute)
            and isinstance(func.value, ast.Name)
            and func.value.id == "importlib"
        ):
            violations.append("importlib dynamic import")
    return violations


def _eval_source_files() -> list[Path]:
    """Every Python file under evaluator/ (recursive)."""
    return sorted(EVAL_DIR.rglob("*.py"))


@pytest.mark.parametrize("source_file", _eval_source_files(), ids=lambda p: p.name)
def test_evaluator_imports_no_disallowed_modules(source_file: Path) -> None:
    """No network/subprocess/connector/cloud/credential/secret imports."""
    tree = ast.parse(source_file.read_text(), filename=str(source_file))
    violations = _import_violations(tree)
    assert not violations, (
        f"{source_file.name} violates the SITORA sandbox-safety guarantee "
        f"(see SANDBOX.md): {violations}"
    )


@pytest.mark.parametrize("source_file", _eval_source_files(), ids=lambda p: p.name)
def test_evaluator_has_no_dangerous_usage(source_file: Path) -> None:
    """No os.* process/env access, no dynamic import, no writes except args.out."""
    tree = ast.parse(source_file.read_text(), filename=str(source_file))
    violations = _usage_violations(tree, source_file.name)
    assert not violations, (
        f"{source_file.name} violates the SITORA sandbox-safety guarantee "
        f"(see SANDBOX.md): {violations}"
    )
