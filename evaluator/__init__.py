"""SITORA reference evaluator package."""

from .evaluator import (
    EvidenceRecord,
    Finding,
    Rule,
    RuleResult,
    STATUS_PRECEDENCE,
    evaluate_predicate,
    evaluate_subject,
    run,
)
from .cli import main

__all__ = [
    "EvidenceRecord",
    "Finding",
    "Rule",
    "RuleResult",
    "STATUS_PRECEDENCE",
    "evaluate_predicate",
    "evaluate_subject",
    "run",
    "main",
]

__version__ = "0.1.0"
