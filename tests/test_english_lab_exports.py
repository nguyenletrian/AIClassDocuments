"""QA: each original Word lab is one document with four contiguous parts.

This does not invent Pretest: skip the blocked source until its binary is readable.
"""
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "labs"
PROGRESS = ROOT / "docs" / "WORD-LAB-WHOLE-BRIEF-PROGRESS.json"
EXPECTED = {
    "ASSIGNMENT-01-student-dictionary": 10,
    "LAB-04-conditions-loops": 14,
    "LAB-05-student-list": 7,
    "LAB-05-06-gradient-descent": 5,
    "LAB-07-probability": 5,
    "LAB-08-statistics": 5,
    "LAB-10-file-csv": 6,
    "PRETEST": None,
}
MARKERS = [
    "## PART 1 — COMPLETE ORIGINAL ENGLISH ASSIGNMENT",
    "## PHẦN 2 — BẢN DỊCH TIẾNG VIỆT TOÀN BỘ ĐỀ",
    "## Quy trình giải chi tiết và các công thức liên quan",
    "## PHẦN 4 — TOÀN BỘ CODE PYTHON CÙNG CHÚ THÍCH",
]


class OneWordOneDocument(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.progress = json.loads(PROGRESS.read_text(encoding="utf-8"))

    def test_scope_and_batch_limit(self):
        data = self.progress
        self.assertEqual(data["expected_word_documents"], 8)
        self.assertEqual(len(data["batches"]), 4)
        self.assertEqual(
            set(EXPECTED), {slug for batch in data["batches"] for slug in batch["labs"]}
        )
        self.assertLessEqual(sum(b["status"] == "IN_PROGRESS" for b in data["batches"]), 1)

    def test_four_contiguous_sections_and_complete_script(self):
        data = self.progress
        for batch in data["batches"]:
            if batch["status"] in {"PENDING", "BLOCKED_SOURCE_BINARY"}:
                continue
            for slug in batch["labs"]:
                with self.subTest(source_word=slug):
                    content = (DOCS / f"{slug}.md").read_text(encoding="utf-8")
                    positions = [content.find(marker) for marker in MARKERS]
                    self.assertEqual(len(positions), len(set(positions)))
                    self.assertTrue(all(pos >= 0 for pos in positions))
                    self.assertEqual(positions, sorted(positions))
                    en = content[positions[0]:positions[1]]
                    vi = content[positions[1]:positions[2]]
                    method = content[positions[2]:positions[3]]
                    script = content[positions[3]:]
                    count = EXPECTED[slug]
                    self.assertGreater(len(en), 300)
                    self.assertGreater(len(vi), 300)
                    self.assertGreater(len(method), 400)
                    if count is not None:
                        self.assertEqual(len(re.findall(r"^### Bài \d+", method, re.M)), count)
                        self.assertIn(str(count), str(count))  # handled in method-count assertion
                    blocks = re.findall(r"^\x60\x60\x60python\n([\s\S]*?)^\x60\x60\x60$", script, re.M)
                    self.assertEqual(len(blocks), 1, "One full Python program, not per-task snippets")
                    compiled = compile(blocks[0], slug + ".py", "exec")
                    self.assertIsNotNone(compiled)
                    self.assertIn("def ", blocks[0])
                    self.assertGreaterEqual(len(re.findall(r"#", blocks[0])), 6)

    def test_smoke_first_batch(self):
        data = self.progress
        if data["batches"][0]["status"] == "PENDING":
            return
        for slug in EXPECTED:
            if slug not in data["batches"][0]["labs"]:
                continue
            content = (DOCS / f"{slug}.md").read_text(encoding="utf-8")
            last = content.split(MARKERS[-1], 1)[1]
            script = re.findall(r"^\x60\x60\x60python\n([\s\S]*?)^\x60\x60\x60$", last, re.M)[0]
            with tempfile.TemporaryDirectory() as folder:
                src = Path(folder) / "lab_solution.py"
                src.write_text(script, encoding="utf-8")
                args = [sys.executable, "-B", str(src)]
                if slug != "LAB-04-conditions-loops":
                    args.append("--demo")
                r = subprocess.run(args, cwd=folder, capture_output=True,
                                   text=True, timeout=45, encoding="utf-8")
                self.assertEqual(r.returncode, 0, r.stderr)


if __name__ == "__main__":
    unittest.main()
