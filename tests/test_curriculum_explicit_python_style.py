"""Enforce beginner-readable executable examples for reviewed lesson batches.

Tests only the active or merged batches from the explicitly approved ledger.
Use Python AST (not regex) to catch assert, all comprehension variants,
generator expressions, and condensed conditional expressions.
"""
import ast
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs" / "CURRICULUM-EXPLICIT-PYTHON-PROGRESS.json"
CHAPTERS = ROOT / "lessons" / "chapters"
DISALLOWED = (
    ast.Assert, ast.ListComp, ast.SetComp, ast.DictComp,
    ast.GeneratorExp, ast.IfExp,
)


def shortcut_nodes(code):
    """Return (line, syntax) for discouraged shorthand in a Python snippet."""
    tree = ast.parse(code)
    return sorted(
        [(node.lineno, type(node).__name__)
         for node in ast.walk(tree) if isinstance(node, DISALLOWED)]
    )


class ExplicitPythonStyleTests(unittest.TestCase):
    def test_shortcut_fixtures(self):
        invalid = (
            "assert len(items) == 10\n"
            "selected = [x for x in items if x > 0]\n"
            "total = sum(x for x in items)\n"
            "label = 'yes' if selected else 'no'\n"
        )
        issues = shortcut_nodes(invalid)
        self.assertEqual(
            {name for _, name in issues},
            {"Assert", "ListComp", "GeneratorExp", "IfExp"},
        )
        explicit = (
            "if len(items) != 10:\n"
            "    raise ValueError('Cần 10 bản ghi')\n"
            "selected = []\n"
            "total = 0\n"
            "for x in items:\n"
            "    if x > 0:\n"
            "        selected.append(x)\n"
            "    total += x\n"
            "if selected:\n"
            "    label = 'yes'\n"
            "else:\n"
            "    label = 'no'\n"
        )
        self.assertEqual(shortcut_nodes(explicit), [])

    def test_only_approved_active_or_merged_batches(self):
        ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
        self.assertEqual(len(ledger["batches"]), 10)
        lessons = [lid for batch in ledger["batches"] for lid in batch["lessons"]]
        self.assertEqual(lessons, [f"PY-{i:02d}" for i in range(1, 47)])
        for batch in ledger["batches"]:
            self.assertLessEqual(len(batch["lessons"]), 5)
            if batch["status"] == "PENDING":
                continue
            for chapter_id in batch["lessons"]:
                files = list(CHAPTERS.glob(f"{chapter_id}-*.vi.md"))
                self.assertEqual(len(files), 1, chapter_id)
                content = files[0].read_text(encoding="utf-8")
                snippets = re.findall(
                    r"^\x60\x60\x60python\n(.*?)^\x60\x60\x60$",
                    content, flags=re.MULTILINE | re.DOTALL,
                )
                # PY-43 teaches Git primarily through shell fences; it has five
                # complete executable Python Git integration examples.
                expected = 5 if chapter_id == "PY-43" else 9
                self.assertGreaterEqual(len(snippets), expected, chapter_id)
                for index, code in enumerate(snippets, 1):
                    with self.subTest(chapter=chapter_id, snippet=index):
                        self.assertEqual(
                            shortcut_nodes(code), [],
                            f"{chapter_id} snippet {index}: shortened syntax still used",
                        )


if __name__ == "__main__":
    unittest.main()
