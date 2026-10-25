"""Detect broken Markdown table cells and visibly leaked pipe entities.

Only the current five-lesson batch and previously fixed batches are checked.
Expand coverage by advancing the 10-batch progress ledger, not by mutating
all 46 lessons at once.
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "lessons" / "chapters"
PROGRESS = ROOT / "docs" / "CURRICULUM-MARKDOWN-RENDER-PROGRESS.json"
PIPE_ENTITY = re.compile(r"&#(?:0*124|x0*7c);|&(?:vert|VerticalLine);", re.IGNORECASE)
DELIMITER = re.compile(r"(?<!\\)\|")


def markdown_errors(source):
    """Return (line, description) for known GitHub Markdown display errors."""
    errors = []
    table_columns = None
    in_fence = False
    for number, line in enumerate(source.splitlines(), 1):
        if re.match(r"^\s*(?:\x60{3,}|~{3,})", line):
            in_fence = not in_fence
            table_columns = None
            continue
        if in_fence:
            continue
        if PIPE_ENTITY.search(line):
            errors.append((number, "pipe HTML entity appears literally in inline code"))
        if not line.lstrip().startswith("|"):
            table_columns = None
            continue
        # A table row has one opening and closing delimiter plus its cell separators.
        # A literal pipe in table-cell inline code must be escaped as \|.
        cells = len(DELIMITER.split(line)) - 2
        if table_columns is None:
            table_columns = cells
        elif cells != table_columns:
            errors.append((number, f"table has {cells} cells, expected {table_columns}"))
    return errors


class MarkdownRenderingRegression(unittest.TestCase):
    def test_examples_reject_split_cells_and_undecoded_entities(self):
        bad = (
            "| A | B |\n|---|---|\n| \x60a | b\x60 | explanation |\n"
            "Explanation: \x60&#124;\x60\n"
        )
        self.assertEqual(len(markdown_errors(bad)), 2)
        corrected = (
            "| A | B |\n|---|---|\n| \x60a \\| b\x60 | explanation |\n"
            "Explanation: \x60a | b\x60\n"
        )
        self.assertEqual(markdown_errors(corrected), [])

    def test_only_reviewed_batches_and_active_batch_are_clean(self):
        progress = json.loads(PROGRESS.read_text(encoding="utf-8"))
        self.assertEqual(len(progress["batches"]), 10)
        self.assertLessEqual(progress["last_completed_batch"], 10)
        expected_ids = [f"PY-{i:02d}" for i in range(1, 47)]
        ids = [lesson for batch in progress["batches"] for lesson in batch["lessons"]]
        self.assertEqual(ids, expected_ids)
        for batch in progress["batches"]:
            self.assertLessEqual(len(batch["lessons"]), 5)
            if batch["status"] == "PENDING":
                continue
            for lesson_id in batch["lessons"]:
                with self.subTest(lesson=lesson_id):
                    files = list(CHAPTERS.glob(f"{lesson_id}-*.vi.md"))
                    self.assertEqual(len(files), 1)
                    issues = markdown_errors(files[0].read_text(encoding="utf-8"))
                    self.assertEqual(issues, [], f"{lesson_id} formatting: {issues}")


if __name__ == "__main__":
    unittest.main()
