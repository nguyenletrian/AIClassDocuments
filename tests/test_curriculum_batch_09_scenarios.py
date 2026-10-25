"""Run PY-41..PY-45 scripts independently with exact expected outputs.

Requires scikit-learn, NumPy, Matplotlib, a local Git executable and the
dependencies from earlier lessons. Matplotlib uses Agg and writes to temp CWD.
Passing Linux GitHub Actions does not verify Windows AIBridge execution.
"""
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

CHAPTERS = Path(__file__).resolve().parents[1] / "lessons" / "chapters"
ROWS = (10, 12, 15, 18, 20)


class Batch09Scenarios(unittest.TestCase):
    def test_25_cases_execute_and_match_exact_stdout(self):
        for number in range(41, 46):
            cid = f"PY-{number:02d}"
            files = list(CHAPTERS.glob(f"{cid}-*.vi.md"))
            self.assertEqual(len(files), 1, cid)
            content = files[0].read_text(encoding="utf-8")
            chapter = content.split("## 5.", 1)[1].split("## 6.", 1)[0]
            cases = re.split(
                r"(?=^### Tình huống [1-5] — Cấp [1-5]: )",
                chapter, flags=re.MULTILINE,
            )[1:]
            self.assertEqual(len(cases), 5, cid)
            for level, case in enumerate(cases, 1):
                with self.subTest(chapter=cid, level=level):
                    self.assertRegex(case, rf"^### Tình huống {level} — Cấp {level}:")
                    for phrase in (
                        "**Từ vựng trong mục:**", "**Tình huống thực tế:**",
                        "**Vì sao chọn cách này?**", "**Quy trình:**",
                        "**Kết quả khi chạy:**",
                    ):
                        self.assertIn(phrase, case)
                    self.assertRegex(case, rf"\b{ROWS[level-1]}\b")
                    code = re.findall(
                        r"^\x60\x60\x60python\n(.*?)^\x60\x60\x60$",
                        case, flags=re.MULTILINE | re.DOTALL,
                    )
                    output = re.findall(
                        r"^\x60\x60\x60text\n(.*?)^\x60\x60\x60$",
                        case, flags=re.MULTILINE | re.DOTALL,
                    )
                    self.assertEqual(len(code), 2, 'No Note and annotated Python copy required')
                    self.assertEqual(len(output), 1)
                    with tempfile.TemporaryDirectory() as cwd:
                        result = subprocess.run(
                            [sys.executable, "-I", "-B", "-c", code[1]],
                            cwd=cwd, text=True, capture_output=True,
                            encoding="utf-8", timeout=40,
                        )
                    self.assertEqual(
                        result.returncode, 0,
                        f"{cid} scenario {level}: {result.stderr}",
                    )
                    self.assertEqual(
                        result.stdout.strip(), output[0].strip(),
                        f"{cid} scenario {level}: output differs",
                    )


if __name__ == "__main__":
    unittest.main()
