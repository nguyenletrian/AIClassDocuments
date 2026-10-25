"""No Note pairing checks for the owner-approved sequential curriculum batches.

Baseline fingerprints represent the exact annotated lesson before paired layout.
Tests verify original material is recoverable byte-for-byte (Unicode codepoints),
Python ASTs are equal, and No Note contains no tokenizer COMMENT tokens.
"""
import ast
import io
import json
import re
import tokenize
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "lessons" / "chapters"
LEDGER = ROOT / "docs" / "CURRICULUM-NO-NOTE-PROGRESS.json"
PAIR = re.compile(
    r"(?m)^\*\*No Note — Không chú thích\*\*\n\n"
    r"^\x60{3}(?P<language>python|bash|sh|shell)\n(?P<clean>.*?)^\x60{3}\n\n"
    r"^\*\*Code có chú thích — Giải thích từng bước\*\*\n\n"
    r"^\x60{3}(?P=language)\n(?P<annotated>.*?)^\x60{3}$",
    re.MULTILINE | re.DOTALL,
)
SOURCE_FENCE = re.compile(r"(?m)^\x60{3}(python|bash|sh|shell)\n")
HEAD_NO_NOTE = "**No Note — Không chú thích**"
HEAD_ANNOTATED = "**Code có chú thích — Giải thích từng bước**"


def fnv64(text):
    """Stable 64-bit fingerprint of the exact Unicode source text."""
    value = 0xCBF29CE484222325
    for char in text:
        value ^= ord(char)
        value = (value * 0x100000001B3) & 0xFFFFFFFFFFFFFFFF
    return f"{value:016x}"


def remove_pair_layout(pair):
    """Return only the previously annotated fence, unchanged."""
    return "\x60\x60\x60" + pair.group("language") + "\n" + pair.group("annotated") + "\x60\x60\x60"


class NoNotePairTests(unittest.TestCase):
    def test_only_one_sequential_batch_active(self):
        ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
        batches = ledger["batches"]
        self.assertEqual(len(batches), 10)
        self.assertEqual(
            [lesson for batch in batches for lesson in batch["lessons"]],
            [f"PY-{i:02d}" for i in range(1, 47)],
        )
        self.assertLessEqual(
            sum(batch["status"] == "IN_PROGRESS" for batch in batches), 1,
        )
        saw_pending = False
        for batch in batches:
            self.assertLessEqual(len(batch["lessons"]), 5)
            if batch["status"] == "COMPLETED":
                self.assertFalse(saw_pending, "Completed batches must be contiguous")
            else:
                saw_pending = True

    def test_adjacency_original_fidelity_and_ast(self):
        ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
        checked = 0
        for batch in ledger["batches"]:
            if batch["status"] not in {"IN_PROGRESS", "COMPLETED"}:
                continue
            fingerprints = batch["original_source_fingerprints"]
            for lesson in batch["lessons"]:
                with self.subTest(lesson=lesson):
                    files = list(CHAPTERS.glob(f"{lesson}-*.vi.md"))
                    self.assertEqual(len(files), 1)
                    text = files[0].read_text(encoding="utf-8")
                    pairs = list(PAIR.finditer(text))
                    self.assertGreater(len(pairs), 0)
                    self.assertEqual(text.count(HEAD_NO_NOTE), len(pairs))
                    self.assertEqual(text.count(HEAD_ANNOTATED), len(pairs))
                    self.assertEqual(len(SOURCE_FENCE.findall(text)), len(pairs) * 2)
                    restored = PAIR.sub(remove_pair_layout, text)
                    self.assertEqual(
                        fnv64(restored), fingerprints[lesson],
                        f"{lesson}: original source/prose/MCQs not preserved",
                    )
                    self.assertEqual(
                        len(re.findall(r"(?m)^\*\*Q\d+\.", text)), 20,
                        f"{lesson}: preserve all 20 bilingual questions",
                    )
                    for idx, pair in enumerate(pairs, 1):
                        clean, annotated = pair.group("clean"), pair.group("annotated")
                        self.assertTrue(clean.strip())
                        if pair.group("language") == "python":
                            comments = [
                                token for token in tokenize.generate_tokens(
                                    io.StringIO(clean).readline
                                )
                                if token.type == tokenize.COMMENT
                            ]
                            self.assertEqual(comments, [], f"{lesson} pair {idx} contains comments")
                            self.assertEqual(
                                ast.dump(ast.parse(clean), include_attributes=False),
                                ast.dump(ast.parse(annotated), include_attributes=False),
                                f"{lesson} pair {idx}: source AST changed",
                            )
                        else:
                            # Bash syntax and quoting require a separate reviewed
                            # command-preservation check, not a Python AST.
                            self.assertFalse(re.search(r"(?m)^\s*#(?!\!)", clean))
                    checked += 1
        self.assertGreater(checked, 0, "At least the first batch must be in progress")


if __name__ == "__main__":
    unittest.main()
