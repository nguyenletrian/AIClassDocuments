"""Validate English lab export folders and execute their annotated solutions.

This test does not infer that private Word documents were directly reparsed.
"""
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPORTS = ROOT / "docs" / "labs"
LEDGER = ROOT / "docs" / "LAB-EN-SOLUTIONS-PROGRESS.json"
TASK_COUNTS = {
    "LAB-MATH-02-sets-jaccard": 6,
    "LAB-MATH-03-04-matrix-pca": 4,
    "ASSIGNMENT-01-student-dictionary": 10,
    "LAB-04-conditions-loops": 14,
    "LAB-05-student-list": 7,
    "LAB-10-file-csv": 0,
    "LAB-05-06-gradient-descent": 5,
    "LAB-07-probability": 5,
    "LAB-08-statistics": 5,
}
# Minimum output substrings for the first owner-approved batch.
SMOKE = {
    "LAB-MATH-02-sets-jaccard": ("Task 3 - Jaccard(A, E): 1.00", "Student D: No connections"),
    "LAB-MATH-03-04-matrix-pca": ("Task 1 - Store matrix shape: (8, 4)", "PCA projected shape: (8, 2)"),
    "ASSIGNMENT-01-student-dictionary": ("Ascending scores", "Statistics:", "Student list:"),
}


class LabEnglishExports(unittest.TestCase):
    def test_current_batch_has_complete_folders_and_valid_english_code(self):
        progress = json.loads(LEDGER.read_text(encoding="utf-8"))
        self.assertEqual(progress["expected_lab_units"], 9)
        self.assertEqual(progress["expected_batches"], 3)
        self.assertEqual(len(progress["batches"]), 3)
        self.assertLessEqual(
            sum(b["status"] == "IN_PROGRESS" for b in progress["batches"]), 1
        )
        for batch in progress["batches"]:
            if batch["status"] == "PENDING":
                continue
            for slug in batch["labs"]:
                with self.subTest(lab=slug):
                    folder = EXPORTS / slug
                    english = (folder / "LAB_EN_SOLVED.md").read_text(encoding="utf-8")
                    code = (folder / "SOLUTION_ANNOTATED.py").read_text(encoding="utf-8")
                    self.assertTrue((folder / "README.md").is_file())
                    self.assertIn("English lab requirement:", english)
                    self.assertIn("Annotated solution", english)
                    self.assertIn("def ", code)
                    self.assertIn("# ", code, "Source code must teach step by step")
                    compile(code, str(folder / "SOLUTION_ANNOTATED.py"), "exec")
                    count = len(re.findall(r"^## Task \d+\b", english, re.MULTILINE))
                    expected = TASK_COUNTS[slug]
                    if expected:
                        self.assertEqual(count, expected)
                    self.assertEqual(english.count("**English lab requirement:**"), count)
                    self.assertEqual(english.count("**Annotated solution"), count)
                    # Within each task block, the requirement must occur before a code fence.
                    for section in re.split(r"(?=^## Task \d+\b)", english, flags=re.MULTILINE)[1:]:
                        self.assertLess(section.index("**English lab requirement:**"), section.index("**Annotated solution"))
                        self.assertIn("```python", section)

    def test_batch_one_scripts_run_noninteractive(self):
        for slug, terms in SMOKE.items():
            with self.subTest(lab=slug):
                folder = EXPORTS / slug
                source = folder / "SOLUTION_ANNOTATED.py"
                self.assertTrue(source.exists())
                args = [sys.executable, "-B", str(source)]
                if slug.startswith("ASSIGNMENT"):
                    args.append("--demo")
                result = subprocess.run(
                    args, cwd=folder, capture_output=True, text=True,
                    encoding="utf-8", timeout=45
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                for term in terms:
                    self.assertIn(term, result.stdout)


if __name__ == "__main__":
    unittest.main()
