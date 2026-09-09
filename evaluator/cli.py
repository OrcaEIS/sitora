"""Command-line interface for the SITORA reference evaluator."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .evaluator import run, STATUS_PRECEDENCE

DEMO_DIR = Path(__file__).resolve().parent.parent / "examples" / "training-obligation-alignment"


def _render_report(findings) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("SITORA ALIGNMENT REPORT (reference evaluator)")
    lines.append("=" * 72)
    counts = {s: 0 for s in STATUS_PRECEDENCE}
    for f in findings:
        counts[f.status] = counts.get(f.status, 0) + 1
    lines.append("")
    lines.append("Summary")
    lines.append("-" * 72)
    for s in STATUS_PRECEDENCE:
        lines.append(f"  {s:<14} {counts.get(s, 0)}")
    lines.append("")
    lines.append("Findings")
    lines.append("-" * 72)
    for f in findings:
        lines.append(f"  [{f.status.upper():<12}] subject={f.subject}")
        lines.append(f"    finding id: {f.id}")
        lines.append(f"    {f.summary}")
        for r in f.rule_results:
            lines.append(f"      - rule={r.rule_id} status={r.status} evidence={r.evidence_ids}")
            if r.detail:
                lines.append(f"        {r.detail}")
        lines.append("")
    lines.append("=" * 72)
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="sitora-eval", description="SITORA v0.1-alpha reference evaluator.")
    parser.add_argument("--intent", help="Path to intent JSON.")
    parser.add_argument("--evidence", help="Path to evidence JSON (array or single).")
    parser.add_argument("--rules", help="Path to evaluation-rule JSON (array or single).")
    parser.add_argument("--roster", help="Path to roster JSON (subjects in scope; enables 'incomplete' status).")
    parser.add_argument("--demo", action="store_true", help="Run the bundled synthetic training-obligation-alignment example.")
    parser.add_argument("--json", action="store_true", help="Emit findings as JSON instead of a text report.")
    parser.add_argument("--out", help="Write output to this path instead of stdout.")
    args = parser.parse_args(argv)

    if args.demo:
        intent_path = DEMO_DIR / "input" / "intent.json"
        evidence_path = DEMO_DIR / "input" / "evidence.json"
        rules_path = DEMO_DIR / "input" / "rules.json"
        roster_path = DEMO_DIR / "input" / "roster.json"
    else:
        if not (args.intent and args.evidence and args.rules):
            parser.error("Provide --intent, --evidence, --rules, or use --demo.")
        intent_path = Path(args.intent)
        evidence_path = Path(args.evidence)
        rules_path = Path(args.rules)
        roster_path = Path(args.roster) if args.roster else None

    findings = run(intent_path, evidence_path, rules_path, roster_path)

    if args.json:
        payload = [f.to_dict() for f in findings]
        text = json.dumps(payload, indent=2)
    else:
        text = _render_report(findings)

    if args.out:
        Path(args.out).write_text(text)
        print(f"Wrote {len(findings)} finding(s) to {args.out}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
