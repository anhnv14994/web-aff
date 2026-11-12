"""Unit tests for decision_engine.py; standard library only."""
import unittest
from decision_engine import CandidateEvaluation, DecisionProfile, evaluate_candidate, rank_candidates

class DecisionEngineTests(unittest.TestCase):
    def setUp(self):
        self.profile = DecisionProfile(("max_width", "required_compatibility"),
                                       {"portability": 5, "battery": 3})

    def test_all_hard_pass_then_score(self):
        r = evaluate_candidate(self.profile, CandidateEvaluation(
            "a", {"max_width": "pass", "required_compatibility": "pass"},
            {"portability": 2, "battery": 1}))
        self.assertEqual(r.eligibility_status, "eligible")
        self.assertEqual(r.fit_score, 87.5)
        self.assertEqual(r.evidence_coverage, 1.0)

    def test_hard_fail_excludes(self):
        r = evaluate_candidate(self.profile, CandidateEvaluation(
            "b", {"max_width": "fail", "required_compatibility": "pass"},
            {"portability": 2, "battery": 2}))
        self.assertEqual(r.eligibility_status, "excluded")
        self.assertEqual(r.hard_failures, ("max_width",))

    def test_unknown_hard_check_needs_verification(self):
        r = evaluate_candidate(self.profile, CandidateEvaluation(
            "c", {"max_width": "pass", "required_compatibility": "unknown"},
            {"portability": 2, "battery": 2}))
        self.assertEqual(r.eligibility_status, "verification_required")
        self.assertEqual(r.hard_unknowns, ("required_compatibility",))

    def test_missing_hard_check_defaults_unknown(self):
        r = evaluate_candidate(self.profile, CandidateEvaluation(
            "d", {"max_width": "pass"}, {"portability": 2, "battery": 2}))
        self.assertEqual(r.eligibility_status, "verification_required")

    def test_unknown_soft_preference_is_not_zero(self):
        r = evaluate_candidate(self.profile, CandidateEvaluation(
            "e", {"max_width": "pass", "required_compatibility": "pass"},
            {"portability": 2, "battery": None}))
        self.assertEqual(r.fit_score, 100.0)
        self.assertEqual(r.evidence_coverage, 0.625)

    def test_missing_preference_is_unknown(self):
        r = evaluate_candidate(self.profile, CandidateEvaluation(
            "f", {"max_width": "pass", "required_compatibility": "pass"},
            {"portability": 1}))
        self.assertEqual(r.fit_score, 50.0)
        self.assertEqual(r.evidence_coverage, 0.625)

    def test_zero_is_known_low_fit(self):
        r = evaluate_candidate(self.profile, CandidateEvaluation(
            "g", {"max_width": "pass", "required_compatibility": "pass"},
            {"portability": 0, "battery": 0}))
        self.assertEqual(r.fit_score, 0.0)
        self.assertEqual(r.evidence_coverage, 1.0)

    def test_no_known_preference_has_null_score(self):
        r = evaluate_candidate(self.profile, CandidateEvaluation(
            "h", {"max_width": "pass", "required_compatibility": "pass"}, {}))
        self.assertIsNone(r.fit_score)
        self.assertEqual(r.evidence_coverage, 0.0)

    def test_deterministic_order_and_separate_buckets(self):
        out = rank_candidates(self.profile, [
            CandidateEvaluation("z-low", {"max_width": "pass", "required_compatibility": "pass"},
                                {"portability": 1, "battery": 1}),
            CandidateEvaluation("b-high", {"max_width": "pass", "required_compatibility": "pass"},
                                {"portability": 2, "battery": 2}),
            CandidateEvaluation("a-tie", {"max_width": "pass", "required_compatibility": "pass"},
                                {"portability": 2, "battery": 2}),
            CandidateEvaluation("needs-check", {"max_width": "pass"}, {"portability": 2, "battery": 2}),
            CandidateEvaluation("excluded", {"max_width": "fail", "required_compatibility": "pass"},
                                {"portability": 2, "battery": 2}),
        ])
        self.assertEqual([x.candidate_id for x in out.ranked], ["a-tie", "b-high", "z-low"])
        self.assertEqual([x.candidate_id for x in out.verification_required], ["needs-check"])
        self.assertEqual([x.candidate_id for x in out.excluded], ["excluded"])

    def test_duplicate_ids_rejected(self):
        c = CandidateEvaluation("same", {}, {})
        with self.assertRaises(ValueError):
            rank_candidates(self.profile, [c, c])

    def test_unknown_keys_rejected(self):
        c = CandidateEvaluation("bad", {"misspelled": "pass"}, {"portability": 1})
        with self.assertRaises(ValueError):
            evaluate_candidate(self.profile, c)

    def test_invalid_fit_rejected(self):
        c = CandidateEvaluation("bad", {}, {"portability": True})
        with self.assertRaises(ValueError):
            evaluate_candidate(self.profile, c)

    def test_invalid_weight_rejected(self):
        p = DecisionProfile((), {"portability": 0})
        with self.assertRaises(ValueError):
            evaluate_candidate(p, CandidateEvaluation("x", {}, {"portability": 1}))

    def test_commission_is_not_an_engine_input(self):
        with self.assertRaises(TypeError):
            CandidateEvaluation("no-commission", {}, {}, commission=99.0)

if __name__ == "__main__":
    unittest.main()
