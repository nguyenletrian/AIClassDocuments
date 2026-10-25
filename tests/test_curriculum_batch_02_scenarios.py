"""Run every PY-06..PY-10 scenario in isolation and compare documented output.

Each lesson preserves its own 20 multiple-choice questions and outer sections.
These tests exercise real examples, not just parse their syntax.
"""
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

CHAPTERS = Path(__file__).resolve().parents[1] / "lessons" / "chapters"
RECORD_SIZES = (10, 12, 15, 18, 20)


class Batch02ScenarioTests(unittest.TestCase):
    def test_all_25_scenarios_execute_and_match_expected_stdout(self):
        for n in range(6, 11):
            chapter = f"PY-{n:02d}"
            files = list(CHAPTERS.glob(f"{chapter}-*.vi.md"))
            self.assertEqual(len(files), 1, chapter)
            text = files[0].read_text(encoding="utf-8")
            section = text.split("## 5.", 1)[1].split("## 6.", 1)[0]
            scenarios = re.split(r"(?=^### Tình huống [1-5] — Cấp [1-5]: )",
                                 section, flags=re.MULTILINE)[1:]
            self.assertEqual(len(scenarios), 5, chapter)
            for level, part in enumerate(scenarios, 1):
                with self.subTest(chapter=chapter, level=level):
                    self.assertRegex(part, rf"^### Tình huống {level} — Cấp {level}:")
                    for item in ("**Từ vựng trong mục:**", "**Tình huống thực tế:**",
                                 "**Vì sao chọn cách này?**", "**Quy trình:**",
                                 "**Kết quả khi chạy:**"):
                        self.assertIn(item, part)
                    self.assertRegex(part, rf"\b{RECORD_SIZES[level - 1]}\b")
                    codes = re.findall(r"^\x60\x60\x60python\n(.*?)^\x60\x60\x60$",
                                       part, flags=re.MULTILINE | re.DOTALL)
                    outputs = re.findall(r"^\x60\x60\x60text\n(.*?)^\x60\x60\x60$",
                                         part, flags=re.MULTILINE | re.DOTALL)
                    self.assertEqual(len(codes), 1)
                    self.assertEqual(len(outputs), 1)
                    with tempfile.TemporaryDirectory() as wd:
                        run = subprocess.run(
                            [sys.executable, "-I", "-B", "-c", codes[0]],
                            cwd=wd, capture_output=True, text=True,
                            encoding="utf-8", timeout=15,
                        )
                    self.assertEqual(run.returncode, 0,
                                     f"{chapter}, level {level}: {run.stderr}")
                    self.assertEqual(run.stdout.strip(), outputs[0].strip(),
                                     f"{chapter}, level {level}: printed answer mismatch")


if __name__ == "__main__":
    unittest.main()
