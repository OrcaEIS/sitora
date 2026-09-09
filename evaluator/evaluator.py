"""SITORA reference evaluator.

A minimal, deterministic implementation of the SITORA v0.1-alpha control loop:

    Intent -> Evidence -> Deterministic Evaluation -> Explainable Finding

This is a reference implementation: it proves the loop is coherent and
inspectable. It is NOT the commercial OrcaEIS control plane (no live
connectors, no credentials, no sensitive evidence, no governance workflows).

Run:  python -m evaluator --intent ... --evidence ... --rules ...
      python -m evaluator --demo
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Iterable

STATUS_PRECEDENCE = [
    "unverifiable",
    "conflicting",
    "incomplete",
    "drifting",
    "aligned",
]

VALID_STATUSES = set(STATUS_PRECEDENCE)


def _resolve(path: str, obj: Any) -> Any:
    """Resolve a dotted path against a (possibly nested) object."""
    cur = obj
    for part in path.split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            return None
    return cur


def _coerce_date(v: Any) -> date | None:
    if v is None:
        return None
    if isinstance(v, date) and not isinstance(v, datetime):
        return v
    if isinstance(v, datetime):
        return v.date()
    try:
        return date.fromisoformat(str(v)[:10])
    except ValueError:
        return None


@dataclass
class EvidenceRecord:
    id: str
    intent_id: str
    subject: str
    source: dict
    value: Any
    retrieved_at: str | None = None
    as_of: str | None = None
    provenance: str | None = None

    @property
    def is_attributable(self) -> bool:
        """An evidence record is attributable if it has a source system and provenance."""
        return bool(self.source and self.source.get("system") and self.provenance)


def evaluate_predicate(predicate: dict, value: Any) -> bool:
    """Evaluate a structured predicate against an evidence value. Pure and deterministic."""
    op = predicate.get("op")
    path = predicate.get("path")
    target = _resolve(path, value) if path else value
    cmp_val = predicate.get("value")

    if op == "exists":
        return target is not None
    if op == "equals":
        return target == cmp_val
    if op == "gte":
        try:
            return float(target) >= float(cmp_val)
        except (TypeError, ValueError):
            return False
    if op == "lte":
        try:
            return float(target) <= float(cmp_val)
        except (TypeError, ValueError):
            return False
    if op == "before":
        t, c = _coerce_date(target), _coerce_date(cmp_val)
        return bool(t and c and t < c)
    if op == "after":
        t, c = _coerce_date(target), _coerce_date(cmp_val)
        return bool(t and c and t > c)
    if op == "matches":
        try:
            return bool(re.fullmatch(str(cmp_val), str(target)))
        except re.error:
            return False
    if op in ("all", "any", "none"):
        items = target if isinstance(target, list) else []
        sub = predicate.get("rule")
        if not sub:
            return op == "none" and not items
        results = [evaluate_predicate(sub, i) for i in items]
        if op == "all":
            return bool(items) and all(results)
        if op == "any":
            return any(results)
        if op == "none":
            return not any(results)
    raise ValueError(f"Unsupported predicate op: {op!r}")


@dataclass
class Rule:
    id: str
    intent_id: str
    description: str
    predicate: dict
    pass_status: str = "aligned"
    fail_status: str = "drifting"
    requires_evidence: bool = True


@dataclass
class RuleResult:
    rule_id: str
    status: str
    evidence_ids: list[str] = field(default_factory=list)
    detail: str = ""


@dataclass
class Finding:
    id: str
    intent_id: str
    subject: str
    status: str
    evaluated_at: str
    rule_results: list[RuleResult]
    summary: str = ""

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "intentId": self.intent_id,
            "subject": self.subject,
            "status": self.status,
            "evaluatedAt": self.evaluated_at,
            "ruleResults": [
                {
                    "ruleId": r.rule_id,
                    "status": r.status,
                    "evidenceIds": r.evidence_ids,
                    "detail": r.detail,
                }
                for r in self.rule_results
            ],
            "summary": self.summary,
        }


def _worst(statuses: Iterable[str]) -> str:
    order = {s: i for i, s in enumerate(STATUS_PRECEDENCE)}
    present = [s for s in statuses if s in order]
    if not present:
        return "aligned"
    return min(present, key=lambda s: order[s])


def evaluate_subject(
    intent: dict,
    subject: str,
    evidence: list[EvidenceRecord],
    rules: list[Rule],
) -> Finding:
    """Evaluate all rules for one subject and aggregate to a single finding."""
    subject_evidence = [e for e in evidence if e.subject == subject and e.intent_id == intent["id"]]
    results: list[RuleResult] = []

    for rule in rules:
        if rule.requires_evidence and not subject_evidence:
            results.append(RuleResult(rule.id, "incomplete", detail="No evidence present."))
            continue

        # Detect conflicting evidence among multiple attributable sources.
        attributable = [e for e in subject_evidence if e.is_attributable]
        if not attributable:
            # Non-attributable evidence was considered but is insufficient to
            # support a finding. Reference it so the conclusion stays explainable.
            considered = [e.id for e in subject_evidence]
            results.append(
                RuleResult(
                    rule.id,
                    "unverifiable",
                    considered,
                    "Evidence present but lacks attributable provenance.",
                )
            )
            continue

        if len(attributable) > 1:
            outcomes = {evaluate_predicate(rule.predicate, e.value) for e in attributable}
            if len(outcomes) > 1:
                results.append(
                    RuleResult(
                        rule.id,
                        "conflicting",
                        [e.id for e in attributable],
                        "Attributable evidence sources disagree.",
                    )
                )
                continue

        passed = evaluate_predicate(rule.predicate, attributable[0].value)
        status = rule.pass_status if passed else rule.fail_status
        results.append(
            RuleResult(rule.id, status, [e.id for e in attributable], "Predicate held." if passed else "Predicate did not hold.")
        )

    overall = _worst([r.status for r in results])
    summary = f"Subject '{subject}' evaluated as {overall.upper()} across {len(results)} rule(s)."
    return Finding(
        id=f"finding-{intent['id']}-{subject}",
        intent_id=intent["id"],
        subject=subject,
        status=overall,
        evaluated_at=datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        rule_results=results,
        summary=summary,
    )


# ---------- Loading helpers ----------


def _load_json(path: Path) -> dict | list:
    with path.open() as fh:
        return json.load(fh)


def load_intent(path: Path) -> dict:
    return _load_json(path)


def load_evidence(path: Path) -> list[EvidenceRecord]:
    raw = _load_json(path)
    if isinstance(raw, dict):
        raw = raw.get("evidence", [raw])
    return [
        EvidenceRecord(
            id=e["id"],
            intent_id=e["intentId"],
            subject=e["subject"],
            source=e.get("source", {}),
            value=e.get("value"),
            retrieved_at=e.get("retrievedAt"),
            as_of=e.get("asOf"),
            provenance=e.get("provenance"),
        )
        for e in raw
    ]


def load_rules(path: Path) -> list[Rule]:
    raw = _load_json(path)
    if isinstance(raw, dict):
        raw = raw.get("rules", [raw])
    return [
        Rule(
            id=r["id"],
            intent_id=r["intentId"],
            description=r["description"],
            predicate=r["predicate"],
            pass_status=r.get("passStatus", "aligned"),
            fail_status=r.get("failStatus", "drifting"),
            requires_evidence=r.get("requiresEvidence", True),
        )
        for r in raw
    ]


def run(
    intent_path: Path,
    evidence_path: Path,
    rules_path: Path,
    roster_path: Path | None = None,
) -> list[Finding]:
    intent = load_intent(intent_path)
    evidence = load_evidence(evidence_path)
    rules = load_rules(rules_path)
    rules = [r for r in rules if r.intent_id == intent["id"]]

    if roster_path is not None:
        roster = _load_json(roster_path)
        subjects = roster.get("subjects", []) if isinstance(roster, dict) else []
    else:
        # Without a roster, only subjects with evidence can be evaluated.
        subjects = sorted({e.subject for e in evidence if e.intent_id == intent["id"]})

    if not subjects:
        raise SystemExit("No subjects in scope for intent %s" % intent["id"])
    return [evaluate_subject(intent, s, evidence, rules) for s in subjects]
