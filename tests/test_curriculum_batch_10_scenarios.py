"""Verify PY-46 end-to-end mini-project and final 46-lesson curriculum coverage.

All five examples execute in isolated subprocesses, including JSON report
creation in a temporary directory. CI evidence is not Windows Bridge evidence.
"""
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

CHAPTERS = Path(__file__).resolve().parents[1] / "lessons" / "chapters"
SIZES = (10, 12, 15, 18, 20)


class Batch10ExecutableScenarios(unittest.TestCase):
    def test_five_cases_execute_and_match_exact_stdout(self):
        paths = list(CHAPTERS.glob("PY-46-*.vi.md"))
        self.assertEqual(len(paths), 1)
        content = paths[0].read_text(encoding="utf-8")
        section = content.split("## 5.", 1)[1].split("## 6.", 1)[0]
        cases = re.split(
            r"(?=^### Tình huống [1-5] — Cấp [1-5]: )",
            section, flags=re.MULTILINE,
        )[1:]
        self.assertEqual(len(cases), 5)
        for level, case in enumerate(cases, 1):
            with self.subTest(lesson="PY-46", level=level):
                self.assertRegex(case, rf"^### Tình huống {level} — Cấp {level}:")
                for marker in (
                    "**Từ vựng trong mục:**", "**Tình huống thực tế:**",
                    "**Vì sao chọn cách này?**", "**Quy trình:**",
                    "**Kết quả khi chạy:**",
                ):
                    self.assertIn(marker, case)
                self.assertRegex(case, rf"\b{SIZES[level-1]}\b")
                snippets = re.findall(
                    r"^\x60\x60\x60python\n(.*?)^\x60\x60\x60$",
                    case, flags=re.MULTILINE | re.DOTALL,
                )
                expected = re.findall(
                    r"^\x60\x60\x60text\n(.*?)^\x60\x60\x60$",
                    case, flags=re.MULTILINE | re.DOTALL,
                )
                self.assertEqual(len(snippets), 2, 'Require exactly one No Note and one annotated example')
                self.assertEqual(len(expected), 1)
                with tempfile.TemporaryDirectory() as cwd:
                    completed = subprocess.run(
                        [sys.executable, "-I", "-B", "-c", snippets[1]],
                        cwd=cwd, capture_output=True, text=True,
                        encoding="utf-8", timeout=45,
                    )
                self.assertEqual(
                    completed.returncode, 0,
                    f"PY-46 level {level}: {completed.stderr}",
                )
                self.assertEqual(
                    completed.stdout.strip(), expected[0].strip(),
                    f"PY-46 level {level}: documented output differs",
                )

    def test_all_chapters_have_230_scenarios_and_920_mcqs(self):
        chapters = sorted(CHAPTERS.glob("PY-*.vi.md"))
        self.assertEqual(len(chapters), 46)
        scenario_total = 0
        question_total = 0
        for lesson in chapters:
            body = lesson.read_text(encoding="utf-8")
            cases = re.findall(r"^### Tình huống [1-5]\b", body, re.MULTILINE)
            questions = re.findall(r"^\*\*Q\d+\..+ \| .+\*\*$", body, re.MULTILINE)
            with self.subTest(lesson=lesson.name):
                self.assertEqual(len(cases), 5)
                self.assertEqual(len(questions), 20)
            scenario_total += len(cases)
            question_total += len(questions)
        self.assertEqual(scenario_total, 230)
        self.assertEqual(question_total, 920)


if __name__ == "__main__":
    unittest.main()
