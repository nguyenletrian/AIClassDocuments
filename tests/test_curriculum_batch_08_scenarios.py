"""Execute 25 PY-36..PY-40 code examples, verify exact documented outputs.

GitHub CI installs NumPy/Pandas/SymPy/SciPy. Runs each scenario in a separate
Python subprocess. CI passes do not constitute Windows Bridge verification.
"""
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

CHAPTERS = Path(__file__).resolve().parents[1] / "lessons" / "chapters"
SIZES = (10, 12, 15, 18, 20)


class Batch08ExecutableCases(unittest.TestCase):
    def test_25_cases_execute_and_match_documented_stdout(self):
        for number in range(36, 41):
            cid = f"PY-{number:02d}"
            paths = list(CHAPTERS.glob(f"{cid}-*.vi.md"))
            self.assertEqual(len(paths), 1, cid)
            source = paths[0].read_text(encoding="utf-8")
            section = source.split("## 5.", 1)[1].split("## 6.", 1)[0]
            cases = re.split(
                r"(?=^### Tình huống [1-5] — Cấp [1-5]: )",
                section, flags=re.MULTILINE,
            )[1:]
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
                    self.assertRegex(case, rf"\b{SIZES[level-1]}\b")
                    code = re.findall(
                        r"^\x60\x60\x60python\n(.*?)^\x60\x60\x60$",
                        case, flags=re.MULTILINE | re.DOTALL,
                    )
                    expected = re.findall(
                        r"^\x60\x60\x60text\n(.*?)^\x60\x60\x60$",
                        case, flags=re.MULTILINE | re.DOTALL,
                    )
                    self.assertEqual(len(code), 1)
                    self.assertEqual(len(expected), 1)
                    with tempfile.TemporaryDirectory() as cwd:
                        proc = subprocess.run(
                            [sys.executable, "-I", "-B", "-c", code[0]],
                            cwd=cwd, capture_output=True, text=True,
                            encoding="utf-8", timeout=25,
                        )
                    self.assertEqual(
                        proc.returncode, 0,
                        f"{cid} scenario {level}: {proc.stderr}",
                    )
                    self.assertEqual(
                        proc.stdout.strip(), expected[0].strip(),
                        f"{cid} scenario {level}: stdout mismatch",
                    )


if __name__ == "__main__":
    unittest.main()
