"""Contract tests for the sequential five-lesson curriculum workstream.

This test validates state integrity and completed-batch structure.
It does not claim code execution, educational accuracy, or Windows verification.
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs" / "CURRICULUM-5-LESSON-PROGRESS.json"
CHAPTERS = ROOT / "lessons" / "chapters"
STATUSES = {"PENDING", "IN_PROGRESS", "QA_PASSED", "BLOCKED", "MERGED"}
SIZES = (10, 12, 15, 18, 20)


class FiveLessonBatchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
        cls.index = {}
        for file in CHAPTERS.glob("PY-*.vi.md"):
            match = re.search(r"PY-(\d{2})-", file.name)
            if match:
                cls.index[f"PY-{match.group(1)}"] = file

    def test_exact_fixed_buckets_and_no_parallel_bursts(self):
        data = self.ledger
        self.assertEqual(data["batch_limit"], 5)
        self.assertEqual(data["expected_lessons"], 46)
        self.assertEqual(data["expected_scenarios"], 230)
        self.assertEqual(data["record_sizes_by_level"], list(SIZES))
        batches = data["batches"]
        self.assertEqual(len(batches), 10)
        self.assertEqual(
            [lesson for batch in batches for lesson in batch["lesson_ids"]],
            [f"PY-{i:02d}" for i in range(1, 47)],
        )
        self.assertEqual(len(self.index), 46)
        active = [b for b in batches if b["status"] in {"IN_PROGRESS", "QA_PASSED"}]
        self.assertLessEqual(len(active), 1, "Never run several batches at once")
        seen_unmerged = False
        count_merged = 0
        for index, batch in enumerate(batches, 1):
            self.assertEqual(batch["batch_id"], f"{index:02d}")
            self.assertLessEqual(len(batch["lesson_ids"]), 5)
            self.assertIn(batch["status"], STATUSES)
            if batch["status"] == "MERGED":
                self.assertFalse(seen_unmerged, "Batches must merge sequentially")
                count_merged += 1
                self.assertIsInstance(batch["pr_number"], int)
                self.assertRegex(batch["merged_commit"], r"^[0-9a-f]{40}$")
                self.assertIsNotNone(batch["ci_run"])
            else:
                seen_unmerged = True
        self.assertEqual(data["last_completed_batch"], count_merged)

    def test_merged_lessons_have_five_rising_levels(self):
        for batch in self.ledger["batches"]:
            if batch["status"] != "MERGED":
                continue
            for chapter_id in batch["lesson_ids"]:
                with self.subTest(chapter=chapter_id):
                    text = self.index[chapter_id].read_text(encoding="utf-8")
                    part = text.split("## 5.", 1)[1].split("## 6.", 1)[0]
                    cases = re.split(r"(?=^### Tình huống [1-5]\b)", part, flags=re.M)[1:]
                    self.assertEqual(len(cases), 5)
                    for i, section in enumerate(cases, 1):
                        self.assertTrue(re.search(rf"^### Tình huống {i}\b", section))
                        self.assertRegex(section, rf"\bCấp\s*{i}\b")
                        self.assertIn("**Tình huống thực tế:**", section)
                        self.assertIn("**Vì sao chọn cách", section)
                        self.assertIn("**Quy trình", section)
                        self.assertTrue(
                            ("\x60\x60\x60python" in section or "\x60\x60\x60bash" in section),
                            f"{chapter_id} case {i}: executable example required",
                        )
                        self.assertIn(str(SIZES[i - 1]), section,
                                      f"{chapter_id} case {i}: explain input data count")


if __name__ == "__main__":
    unittest.main()
