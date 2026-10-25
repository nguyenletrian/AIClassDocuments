"""Run PY-11..15 scenarios and check their exact documented output.

NumPy is installed by the associated CI workflow. Each code sample runs in an
isolated Python subprocess. The assertions do not imply Windows verification.
"""
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

CHAPTERS = Path(__file__).resolve().parents[1] / "lessons" / "chapters"
SIZES = (10, 12, 15, 18, 20)


class ThirdBatchExamples(unittest.TestCase):
    def test_25_examples_execute_and_match_printed_answers(self):
        for number in range(11, 16):
            chapter = f"PY-{number:02d}"
            matches = list(CHAPTERS.glob(f"{chapter}-*.vi.md"))
            self.assertEqual(len(matches), 1, chapter)
            content = matches[0].read_text(encoding="utf-8")
            section = content.split("## 5.", 1)[1].split("## 6.", 1)[0]
            parts = re.split(
                r"(?=^### Tình huống [1-5] — Cấp [1-5]: )",
                section, flags=re.MULTILINE,
            )[1:]
            self.assertEqual(len(parts), 5, chapter)
            for level, case in enumerate(parts, 1):
                with self.subTest(chapter=chapter, level=level):
                    self.assertRegex(case, rf"^### Tình huống {level} — Cấp {level}:")
                    for field in (
                        "**Từ vựng trong mục:**", "**Tình huống thực tế:**",
                        "**Vì sao chọn cách này?**", "**Quy trình:**",
                        "**Kết quả khi chạy:**",
                    ):
                        self.assertIn(field, case)
                    self.assertRegex(case, rf"\b{SIZES[level - 1]}\b")
                    code_blocks = re.findall(
                        r"^\x60\x60\x60python\n(.*?)^\x60\x60\x60$",
                        case, flags=re.MULTILINE | re.DOTALL,
                    )
                    outputs = re.findall(
                        r"^\x60\x60\x60text\n(.*?)^\x60\x60\x60$",
                        case, flags=re.MULTILINE | re.DOTALL,
                    )
                    self.assertEqual(len(code_blocks), 1)
                    self.assertEqual(len(outputs), 1)
                    with tempfile.TemporaryDirectory() as cwd:
                        completed = subprocess.run(
                            [sys.executable, "-I", "-B", "-c", code_blocks[0]],
                            cwd=cwd, capture_output=True, text=True,
                            encoding="utf-8", timeout=15,
                        )
                    self.assertEqual(
                        completed.returncode, 0,
                        f"{chapter} case {level}: {completed.stderr}",
                    )
                    self.assertEqual(
                        completed.stdout.strip(), outputs[0].strip(),
                        f"{chapter} case {level}: result differs from docs",
                    )


if __name__ == "__main__":
    unittest.main()
