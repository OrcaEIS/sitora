"""Conformance tests for the SITORA reference evaluator.

These tests double as the v0.1-alpha conformance suite. They assert:
  - schema-adjacent shape of findings,
  - determinism (same input -> same result),
  - the five-status taxonomy,
  - precedence (worst-case status governs),
  - no unverifiable-as-aligned.

Run:  python -m pytest -q
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from evaluator.evaluator import (
    STATUS_PRECEDENCE,
    run,
    evaluate_predicate,
)

REPO = Path(__file__).resolve().parent.parent
DEMO = REPO / "examples" / "training-obligation-alignment" / "input"


@pytest.fixture(scope="module")
def findings():
    return run(
        DEMO / "intent.json",
        DEMO / "evidence.json",
        DEMO / "rules.json",
        DEMO / "roster.json",
    )


def test_five_statuses_exercised(findings):
    statuses = {f.status for f in findings}
    assert statuses == set(STATUS_PRECEDENCE), f"Expected all five statuses, got {statuses}"


def test_status_by_subject(findings):
    by_subject = {f.subject: f.status for f in findings}
    assert by_subject == {
        "emp-001": "aligned",
        "emp-002": "drifting",
        "emp-003": "incomplete",
        "emp-004": "conflicting",
        "emp-005": "unverifiable",
    }


def test_determinism(findings):
    again = run(
        DEMO / "intent.json",
        DEMO / "evidence.json",
        DEMO / "rules.json",
        DEMO / "roster.json",
    )
    # evaluatedAt may differ; compare everything else
    for a, b in zip(findings, again):
        a2 = a.to_dict()
        b2 = b.to_dict()
        a2.pop("evaluatedAt")
        b2.pop("evaluatedAt")
        assert a2 == b2


def test_precedence_rule():
    # 'aligned' is the best (lowest precedence index); 'unverifiable' is worst.
    assert STATUS_PRECEDENCE[0] == "unverifiable"
    assert STATUS_PRECEDENCE[-1] == "aligned"


def test_no_unverifiable_as_aligned(findings):
    for f in findings:
        if f.status == "unverifiable":
            assert f.status != "aligned"


def test_unverifiable_references_considered_evidence(findings):
    # emp-005 has non-attributable evidence (ev-emp-005-lms). The finding is
    # Unverifiable, but the considered evidence must still be referenced so
    # the conclusion is explainable.
    emp005 = next(f for f in findings if f.subject == "emp-005")
    assert emp005.status == "unverifiable"
    for r in emp005.rule_results:
        assert "ev-emp-005-lms" in r.evidence_ids


def test_predicate_purity():
    assert evaluate_predicate({"op": "equals", "path": "completed", "value": True}, {"completed": True})
    assert not evaluate_predicate({"op": "equals", "path": "completed", "value": True}, {"completed": False})
    assert evaluate_predicate({"op": "exists", "path": "completionDate"}, {"completionDate": "2026-02-14"})
    assert evaluate_predicate({"op": "after", "path": "completionDate", "value": "2026-01-01"}, {"completionDate": "2026-02-14"})


def test_finding_output_shape(findings):
    out = findings[0].to_dict()
    for key in ("id", "intentId", "subject", "status", "evaluatedAt", "ruleResults", "summary"):
        assert key in out
