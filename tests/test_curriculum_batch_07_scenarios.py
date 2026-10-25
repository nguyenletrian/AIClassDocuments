"""Run all 25 PY-31..PY-35 examples and compare their exact documented output.

GitHub CI installs NumPy and SymPy. Each sample runs in an isolated Python
subprocess; Linux CI passing must not be called Windows Bridge verification.
"""
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "lessons" / "chapters"
EXPECTED_RECORDS = (10, 12, 15, 18, 20)


class Batch07ExecutableCases(unittest.TestCase):
    def test_25_examples_execute_with_exact_documented_stdout(self):
        for number in range(31, 36):
            name = f"PY-{number:02d}"
            paths = list(ROOT.glob(f"{name}-*.vi.md"))
            self.assertEqual(len(paths), 1, name)
            text = paths[0].read_text(encoding="utf-8")
            section = text.split("## 5.", 1)[1].split("## 6.", 1)[0]
            cases = re.split(
                r"(?=^### Tình huống [1-5] — Cấp [1-5]: )",
                section, flags=re.MULTILINE,
            )[1:]
            self.assertEqual(len(cases), 5, name)
            for level, case in enumerate(cases, 1):
                with self.subTest(chapter=name, level=level):
                    self.assertRegex(case, rf"^### Tình huống {level} — Cấp {level}:")
                    for phrase in (
                        "**Từ vựng trong mục:**", "**Tình huống thực tế:**",
                        "**Vì sao chọn cách này?**", "**Quy trình:**",
                        "**Kết quả khi chạy:**",
                    ):
                        self.assertIn(phrase, case)
                    self.assertRegex(case, rf"\b{EXPECTED_RECORDS[level-1]}\b")
                    blocks = re.findall(
                        r"^\x60\x60\x60python\n(.*?)^\x60\x60\x60$",
                        case, flags=re.MULTILINE | re.DOTALL,
                    )
                    outputs = re.findall(
                        r"^\x60\x60\x60text\n(.*?)^\x60\x60\x60$",
                        case, flags=re.MULTILINE | re.DOTALL,
                    )
                    self.assertEqual(len(blocks), 1)
                    self.assertEqual(len(outputs), 1)
                    with tempfile.TemporaryDirectory() as cwd:
                        proc = subprocess.run(
                            [sys.executable, "-I", "-B", "-c", blocks[0]],
                            cwd=cwd, text=True, capture_output=True,
                            encoding="utf-8", timeout=25,
                        )
                    self.assertEqual(
                        proc.returncode, 0,
                        f"{name} case {level}: {proc.stderr}",
                    )
                    self.assertEqual(
                        proc.stdout.strip(), outputs[0].strip(),
                        f"{name} case {level}: stdout differs from guide",
                    )


if __name__ == "__main__":
    unittest.main()
