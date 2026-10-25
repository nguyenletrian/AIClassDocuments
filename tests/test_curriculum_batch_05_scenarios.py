"""Execute and compare all 25 PY-21..PY-25 scenarios against printed answers.

Python 3.12 and NumPy are installed by the workflow. Each example executes
in its own subprocess; CI evidence is not Windows Bridge verification.
"""
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

CHAPTERS = Path(__file__).resolve().parents[1] / "lessons" / "chapters"
ROWS = (10, 12, 15, 18, 20)


class Batch05RunnableExamples(unittest.TestCase):
    def test_25_examples_execute_and_match_documented_stdout(self):
        for number in range(21, 26):
            cid = f"PY-{number:02d}"
            paths = list(CHAPTERS.glob(f"{cid}-*.vi.md"))
            self.assertEqual(len(paths), 1, cid)
            src = paths[0].read_text(encoding="utf-8")
            section = src.split("## 5.", 1)[1].split("## 6.", 1)[0]
            cases = re.split(r"(?=^### Tình huống [1-5] — Cấp [1-5]: )",
                             section, flags=re.MULTILINE)[1:]
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
                    self.assertRegex(case, rf"\b{ROWS[level-1]}\b")
                    snippets = re.findall(r"^\x60\x60\x60python\n(.*?)^\x60\x60\x60$",
                                          case, flags=re.MULTILINE | re.DOTALL)
                    answers = re.findall(r"^\x60\x60\x60text\n(.*?)^\x60\x60\x60$",
                                         case, flags=re.MULTILINE | re.DOTALL)
                    self.assertEqual(len(snippets), 2, 'One No Note and one annotated snippet')
                    self.assertEqual(len(answers), 1)
                    with tempfile.TemporaryDirectory() as folder:
                        completed = subprocess.run(
                            [sys.executable, "-I", "-B", "-c", snippets[1]],
                            cwd=folder, text=True, capture_output=True,
                            encoding="utf-8", timeout=20,
                        )
                    self.assertEqual(completed.returncode, 0,
                                     f"{cid} level {level}: {completed.stderr}")
                    self.assertEqual(completed.stdout.strip(), answers[0].strip(),
                                     f"{cid} level {level}: printed output mismatch")


if __name__ == "__main__":
    unittest.main()
