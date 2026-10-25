"""Check beginner-readable Python in only current and merged batches.

AST catches assert, list/set/dict comprehensions, generator expressions, and
inline ternaries in Python snippets, even when text searches miss them.
Previous lessons remain in scope as the 10 sequential batches progress.
"""
import ast
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "lessons" / "chapters"
LEDGER = ROOT / "docs" / "CURRICULUM-EXPLICIT-PYTHON-PROGRESS.json"
SHORTHAND = (ast.Assert, ast.ListComp, ast.SetComp, ast.DictComp,
             ast.GeneratorExp, ast.IfExp)


class ExplicitPythonSyntaxQA(unittest.TestCase):
    def test_only_reviewed_or_active_lessons_have_explicit_code(self):
        ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
        self.assertEqual(len(ledger["batches"]), 10)
        self.assertEqual(
            [c for b in ledger["batches"] for c in b["lessons"]],
            [f"PY-{i:02d}" for i in range(1, 47)],
        )
        for batch in ledger["batches"]:
            self.assertLessEqual(len(batch["lessons"]), 5)
            if batch["status"] == "PENDING":
                continue
            for chapter_id in batch["lessons"]:
                with self.subTest(chapter=chapter_id):
                    matches = list(CHAPTERS.glob(f"{chapter_id}-*.vi.md"))
                    self.assertEqual(len(matches), 1, chapter_id)
                    source = matches[0].read_text(encoding="utf-8")
                    blocks = re.findall(
                        r"^\x60\x60\x60python\n(.*?)^\x60\x60\x60$",
                        source, flags=re.MULTILINE | re.DOTALL,
                    )
                    self.assertGreater(len(blocks), 0, chapter_id)
                    for block_id, code in enumerate(blocks, 1):
                        with self.subTest(block=block_id):
                            tree = ast.parse(code)
                            violations = [
                                f"{type(node).__name__}@{node.lineno}"
                                for node in ast.walk(tree)
                                if isinstance(node, SHORTHAND)
                            ]
                            self.assertEqual(
                                violations, [],
                                f"{chapter_id} code block {block_id}: {violations}",
                            )


if __name__ == "__main__":
    unittest.main()
