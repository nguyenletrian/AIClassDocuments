"""Execute PY-16..PY-20 code and compare outputs in each independent case.

Needs NumPy and Pandas provided by the associated CI workflow.
No Windows Bridge execution is implied by passing these tests.
"""
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

CHAPTERS = Path(__file__).resolve().parents[1] / "lessons" / "chapters"
ROWS = (10, 12, 15, 18, 20)


class Batch04ExecutableExamples(unittest.TestCase):
    def test_25_examples_execute_and_match_printed_answers(self):
        for number in range(16, 21):
            cid = f"PY-{number:02d}"
            paths = list(CHAPTERS.glob(f"{cid}-*.vi.md"))
            self.assertEqual(len(paths), 1, cid)
            src = paths[0].read_text(encoding="utf-8")
            part = src.split("## 5.", 1)[1].split("## 6.", 1)[0]
            cases = re.split(
                r"(?=^### Tình huống [1-5] — Cấp [1-5]: )",
                part, flags=re.MULTILINE,
            )[1:]
            self.assertEqual(len(cases), 5, cid)
            for level, case in enumerate(cases, 1):
                with self.subTest(chapter=cid, level=level):
                    self.assertRegex(case, rf"^### Tình huống {level} — Cấp {level}:")
                    for field in (
                        "**Từ vựng trong mục:**", "**Tình huống thực tế:**",
                        "**Vì sao chọn cách này?**", "**Quy trình:**",
                        "**Kết quả khi chạy:**",
                    ):
                        self.assertIn(field, case)
                    self.assertRegex(case, rf"\b{ROWS[level - 1]}\b")
                    codes = re.findall(
                        r"^\x60\x60\x60python\n(.*?)^\x60\x60\x60$",
                        case, flags=re.MULTILINE | re.DOTALL,
                    )
                    answers = re.findall(
                        r"^\x60\x60\x60text\n(.*?)^\x60\x60\x60$",
                        case, flags=re.MULTILINE | re.DOTALL,
                    )
                    self.assertEqual(len(codes), 2, 'Exactly one No Note and one annotated code')
                    self.assertEqual(len(answers), 1)
                    with tempfile.TemporaryDirectory() as cwd:
                        done = subprocess.run(
                            [sys.executable, "-I", "-B", "-c", codes[1]],
                            cwd=cwd, text=True, capture_output=True,
                            encoding="utf-8", timeout=20,
                        )
                    self.assertEqual(done.returncode, 0,
                                     f"{cid} case {level}: {done.stderr}")
                    self.assertEqual(done.stdout.strip(), answers[0].strip(),
                                     f"{cid} case {level}: stdout mismatch")


if __name__ == "__main__":
    unittest.main()
