"""Run 25 PY-26..PY-30 examples in independent Python 3.12 subprocesses.

NumPy dependency is installed by the curriculum workflow.
Checks exact printed output, not merely Python syntax; Windows Bridge tests
require separate runtime evidence.
"""
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

CHAPTERS = Path(__file__).resolve().parents[1] / "lessons" / "chapters"
ROWS = (10, 12, 15, 18, 20)


class Batch06ExecutableScenarios(unittest.TestCase):
    def test_each_case_executes_and_matches_documented_answer(self):
        for number in range(26, 31):
            cid = f"PY-{number:02d}"
            files = list(CHAPTERS.glob(f"{cid}-*.vi.md"))
            self.assertEqual(len(files), 1, cid)
            content = files[0].read_text(encoding="utf-8")
            section = content.split("## 5.", 1)[1].split("## 6.", 1)[0]
            cases = re.split(r"(?=^### Tình huống [1-5] — Cấp [1-5]: )",
                             section, flags=re.MULTILINE)[1:]
            self.assertEqual(len(cases), 5, cid)
            for level, case in enumerate(cases, 1):
                with self.subTest(chapter=cid, level=level):
                    self.assertRegex(case, rf"^### Tình huống {level} — Cấp {level}:")
                    for heading in (
                        "**Từ vựng trong mục:**", "**Tình huống thực tế:**",
                        "**Vì sao chọn cách này?**", "**Quy trình:**",
                        "**Kết quả khi chạy:**",
                    ):
                        self.assertIn(heading, case)
                    self.assertRegex(case, rf"\b{ROWS[level-1]}\b")
                    code = re.findall(r"^\x60\x60\x60python\n(.*?)^\x60\x60\x60$",
                                      case, flags=re.MULTILINE | re.DOTALL)
                    answers = re.findall(r"^\x60\x60\x60text\n(.*?)^\x60\x60\x60$",
                                         case, flags=re.MULTILINE | re.DOTALL)
                    self.assertEqual(len(code), 1)
                    self.assertEqual(len(answers), 1)
                    with tempfile.TemporaryDirectory() as folder:
                        result = subprocess.run(
                            [sys.executable, "-I", "-B", "-c", code[0]],
                            cwd=folder, capture_output=True, text=True,
                            encoding="utf-8", timeout=20,
                        )
                    self.assertEqual(result.returncode, 0,
                                     f"{cid} case {level}: {result.stderr}")
                    self.assertEqual(result.stdout.strip(), answers[0].strip(),
                                     f"{cid} case {level}: stdout mismatch")


if __name__ == "__main__":
    unittest.main()
