"""A+ generic decision-engine reference core; no product-specific rules or commission input."""
from __future__ import annotations
from dataclasses import dataclass
from math import isfinite
from typing import Literal, Mapping, Sequence

CheckStatus = Literal["pass", "fail", "unknown"]
EligibilityStatus = Literal["eligible", "verification_required", "excluded"]
FitLevel = int | None

@dataclass(frozen=True)
class DecisionProfile:
    hard_constraints: tuple[str, ...]
    preference_weights: Mapping[str, float]

@dataclass(frozen=True)
class CandidateEvaluation:
    candidate_id: str
    hard_checks: Mapping[str, CheckStatus]
    fit_by_preference: Mapping[str, FitLevel]

@dataclass(frozen=True)
class CandidateResult:
    candidate_id: str
    eligibility_status: EligibilityStatus
    hard_failures: tuple[str, ...]
    hard_unknowns: tuple[str, ...]
    fit_score: float | None
    evidence_coverage: float | None

@dataclass(frozen=True)
class RankingResult:
    ranked: tuple[CandidateResult, ...]
    verification_required: tuple[CandidateResult, ...]
    excluded: tuple[CandidateResult, ...]

def _validate_profile(profile: DecisionProfile) -> None:
    if len(set(profile.hard_constraints)) != len(profile.hard_constraints):
        raise ValueError("hard_constraints must not contain duplicates")
    for key, weight in profile.preference_weights.items():
        if not isinstance(key, str) or not key.strip():
            raise ValueError("preference keys must be non-empty strings")
        if isinstance(weight, bool) or not isinstance(weight, (int, float)):
            raise ValueError(f"weight for {key!r} must be numeric")
        if not isfinite(float(weight)) or weight <= 0:
            raise ValueError(f"weight for {key!r} must be finite and > 0")

def _validate_candidate(profile: DecisionProfile, candidate: CandidateEvaluation) -> None:
    if not candidate.candidate_id or not candidate.candidate_id.strip():
        raise ValueError("candidate_id must be non-empty")
    extra_checks = set(candidate.hard_checks) - set(profile.hard_constraints)
    if extra_checks:
        raise ValueError("unknown hard-check keys: " + ", ".join(sorted(extra_checks)))
    for key, status in candidate.hard_checks.items():
        if status not in ("pass", "fail", "unknown"):
            raise ValueError(f"invalid hard-check status for {key!r}: {status!r}")
    extra_preferences = set(candidate.fit_by_preference) - set(profile.preference_weights)
    if extra_preferences:
        raise ValueError("unknown preference keys: " + ", ".join(sorted(extra_preferences)))
    for key, fit in candidate.fit_by_preference.items():
        if fit is None:
            continue
        if isinstance(fit, bool) or not isinstance(fit, int) or fit not in (0, 1, 2):
            raise ValueError(f"fit for {key!r} must be 0, 1, 2, or None")

def evaluate_candidate(profile: DecisionProfile, candidate: CandidateEvaluation) -> CandidateResult:
    """Apply hard gates, then score only known soft-preference evaluations."""
    _validate_profile(profile)
    _validate_candidate(profile, candidate)
    failures = tuple(k for k in profile.hard_constraints if candidate.hard_checks.get(k, "unknown") == "fail")
    unknowns = tuple(k for k in profile.hard_constraints if candidate.hard_checks.get(k, "unknown") == "unknown")
    if failures:
        status: EligibilityStatus = "excluded"
    elif unknowns:
        status = "verification_required"
    else:
        status = "eligible"
    total_weight = sum(float(w) for w in profile.preference_weights.values())
    known_weight = 0.0
    weighted_fit = 0.0
    for key, raw_weight in profile.preference_weights.items():
        fit = candidate.fit_by_preference.get(key)
        if fit is not None:
            weight = float(raw_weight)
            known_weight += weight
            weighted_fit += weight * fit
    score = round(100.0 * weighted_fit / (2.0 * known_weight), 6) if known_weight else None
    coverage = round(known_weight / total_weight, 6) if total_weight else None
    return CandidateResult(candidate.candidate_id, status, failures, unknowns, score, coverage)

def rank_candidates(profile: DecisionProfile, candidates: Sequence[CandidateEvaluation]) -> RankingResult:
    """Split candidates into eligible, verification-needed and excluded groups."""
    _validate_profile(profile)
    ids = [c.candidate_id for c in candidates]
    if len(set(ids)) != len(ids):
        raise ValueError("candidate_id values must be unique within one ranking run")
    results = [evaluate_candidate(profile, c) for c in candidates]
    ranked = [r for r in results if r.eligibility_status == "eligible"]
    verify = [r for r in results if r.eligibility_status == "verification_required"]
    excluded = [r for r in results if r.eligibility_status == "excluded"]
    ranked.sort(key=lambda r: (r.fit_score is None, -(r.fit_score or 0.0), r.candidate_id))
    verify.sort(key=lambda r: r.candidate_id)
    excluded.sort(key=lambda r: r.candidate_id)
    return RankingResult(tuple(ranked), tuple(verify), tuple(excluded))
