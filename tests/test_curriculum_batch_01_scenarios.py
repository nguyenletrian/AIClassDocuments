"""Executable QA for PY-01..PY-05, five progressive case studies per chapter.

Runs each code sample in a fresh isolated Python process and compares
stdout to the adjacent expected text block. Tests validate examples,
not pedagogical review or a Windows environment.
"""
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

CHAPTERS = Path(__file__).resolve().parents[1] / "lessons" / "chapters"
EXPECTED_ROWS = (10, 12, 15, 18, 20)


class FirstBatchScenarios(unittest.TestCase):
    def test_all_25_scenarios_execute_and_match_documented_output(self):
        for number in range(1, 6):
            chapter_id = f"PY-{number:02d}"
            matches = list(CHAPTERS.glob(f"{chapter_id}-*.vi.md"))
            self.assertEqual(len(matches), 1, chapter_id)
            text = matches[0].read_text(encoding="utf-8")
            part = text.split("## 5.", 1)[1].split("## 6.", 1)[0]
            sections = re.split(
                r"(?=^### Tình huống [1-5] — Cấp [1-5]: )",
                part,
                flags=re.MULTILINE,
            )[1:]
            self.assertEqual(len(sections), 5, chapter_id)
            for case_id, section in enumerate(sections, 1):
                with self.subTest(chapter=chapter_id, case=case_id):
                    self.assertRegex(
                        section, rf"^### Tình huống {case_id} — Cấp {case_id}:"
                    )
                    self.assertIn("**Từ vựng trong mục:**", section)
                    self.assertIn("**Tình huống thực tế:**", section)
                    self.assertIn("**Vì sao chọn cách này?**", section)
                    self.assertIn("**Quy trình:**", section)
                    self.assertIn("**Kết quả khi chạy:**", section)
                    self.assertRegex(section, rf"\b{EXPECTED_ROWS[case_id-1]}\b")
                    codes = re.findall(
                        r"^\x60\x60\x60python\n(.*?)^\x60\x60\x60$",
                        section, flags=re.MULTILINE | re.DOTALL
                    )
                    expecteds = re.findall(
                        r"^\x60\x60\x60text\n(.*?)^\x60\x60\x60$",
                        section, flags=re.MULTILINE | re.DOTALL
                    )
                    self.assertEqual(len(codes), 2, 'No Note + original annotated code')
                    self.assertEqual(len(expecteds), 1)
                    # Deliberately isolated and bounded. Code is repository-authored.
                    with tempfile.TemporaryDirectory() as cwd:
                        run = subprocess.run(
                            [sys.executable, "-I", "-B", "-c", codes[1]],
                            cwd=cwd, capture_output=True, text=True,
                            encoding="utf-8", timeout=15,
                        )
                    self.assertEqual(
                        run.returncode, 0,
                        f"{chapter_id} case {case_id}: {run.stderr}",
                    )
                    self.assertEqual(
                        run.stdout.strip(), expecteds[0].strip(),
                        f"{chapter_id} case {case_id}: output does not match"
                    )


if __name__ == "__main__":
    unittest.main()
