import pathlib
import unittest


SOURCE = pathlib.Path(__file__).resolve().parents[1] / "MilestoneJury.py"


class MilestoneJurySourceTests(unittest.TestCase):
    def setUp(self):
        self.source = SOURCE.read_text(encoding="utf-8")

    def test_has_studio_runner_header_and_contract_class(self):
        self.assertTrue(self.source.startswith("# v0.2.16\n"))
        self.assertIn("class MilestoneJury(gl.Contract):", self.source)

    def test_exposes_distinct_milestone_workflow(self):
        self.assertIn("def define_milestone", self.source)
        self.assertIn("def adjudicate_delivery", self.source)
        self.assertIn("def get_status", self.source)
        self.assertNotIn("review_public_collateral_evidence", self.source)

    def test_uses_web_llm_and_validator_consensus(self):
        self.assertIn("gl.nondet.web.get", self.source)
        self.assertIn("gl.nondet.exec_prompt", self.source)
        self.assertIn("gl.vm.run_nondet_unsafe", self.source)
        self.assertIn("AWARD_ELIGIBLE", self.source)


if __name__ == "__main__":
    unittest.main()
