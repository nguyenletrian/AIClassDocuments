"""Verify owner-corrected export: one Markdown document per original Word lab.

A task must contain EN brief, VI translation, sourced code and explanation.
Historical multi-file output is not counted as completion.
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPORT_ROOT = ROOT / "docs" / "labs"
LEDGER = ROOT / "docs" / "LAB-EN-SOLUTIONS-PROGRESS.json"
GOAL = ROOT / "docs" / "LAB-EN-SOLUTIONS-GOAL.json"
COUNTS = {
    "ASSIGNMENT-01-student-dictionary": 10,
    "LAB-04-conditions-loops": 14,
    "LAB-05-student-list": 7,
    "LAB-05-06-gradient-descent": 5,
    "LAB-07-probability": 5,
    "LAB-08-statistics": 5,
    "LAB-10-file-csv": 6,
}


class OriginalWordSingleFileLabTests(unittest.TestCase):
    def test_exactly_seven_word_lab_units_in_authorized_scope(self):
        goal = json.loads(GOAL.read_text(encoding="utf-8"))
        progress = json.loads(LEDGER.read_text(encoding="utf-8"))
        self.assertTrue(goal["scope"]["one_document_per_original_word_file"])
        self.assertEqual(goal["scope"]["total_unique_lab_units"], 7)
        self.assertEqual(progress["expected_lab_units"], 7)
        self.assertEqual(progress["expected_batches"], 3)
        self.assertEqual(set(COUNTS), {x for batch in progress["batches"] for x in batch["labs"]})
        self.assertLessEqual(sum(b["status"] == "IN_PROGRESS" for b in progress["batches"]), 1)

    def test_english_vietnamese_sourced_solution_explanation_per_exercise(self):
        progress = json.loads(LEDGER.read_text(encoding="utf-8"))
        for batch in progress["batches"]:
            if batch["status"] == "PENDING":
                continue
            for slug in batch["labs"]:
                with self.subTest(original_word_lab=slug):
                    path = EXPORT_ROOT / (slug + ".md")
                    self.assertTrue(path.is_file(), f"Missing consolidated Word lab: {path}")
                    text = path.read_text(encoding="utf-8")
                    tasks = list(re.finditer(r"^## Bài (\d+)(?:\s|$)", text, flags=re.MULTILINE))
                    self.assertEqual(len(tasks), COUNTS[slug])
                    self.assertEqual([int(m[1]) for m in tasks], list(range(1, COUNTS[slug]+1)))
                    for i, m in enumerate(tasks):
                        end = tasks[i+1].start() if i+1 < len(tasks) else len(text)
                        section = text[m.start():end]
                        markers = [
                            "### English",
                            "### Tiếng Việt",
                            "### Bài giải",
                            "### Giải thích",
                        ]
                        positions = [section.find(q) for q in markers]
                        self.assertTrue(all(p >= 0 for p in positions), f"Missing required section: {slug} task {i+1}")
                        self.assertEqual(positions, sorted(positions))
                        self.assertIn("```python", section)
                        snippets = re.findall(r"```python\n([\s\S]*?)^```", section, flags=re.MULTILINE)
                        self.assertTrue(snippets, f"No Python from source for {slug} task {i+1}")
                        for snippet in snippets:
                            compile(snippet, f"{path}:task{i+1}", "exec")
                        # Do not accept only a call without implementation or source.
                        self.assertIn("def ", section)
                        self.assertRegex(section, r"SOLUTION\.py|SOLUTION_ANNOTATED\.py|DEMO\.py")
                    self.assertNotIn("LAB-MATH-02", path.name)

    def test_one_file_contract_in_final_export(self):
        # Replacing old output must be checked in PR, not only post-merge.
        paths = sorted(p.name for p in EXPORT_ROOT.iterdir())
        expected = sorted([slug + ".md" for slug in COUNTS] + ["README.md"])
        self.assertEqual(paths, expected, "Only 7 Word lab documents and index should remain")
        for slug in COUNTS:
            self.assertTrue((EXPORT_ROOT / (slug + ".md")).is_file())
            self.assertFalse((EXPORT_ROOT / slug).exists(), "Legacy multi-file lab remains")


if __name__ == "__main__":
    unittest.main()
