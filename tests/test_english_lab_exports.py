"""QA cho toàn bộ 8 đề Word: Anh → Việt → giải thích, code có chú thích cuối dòng.

Bài học không sử dụng assert. Phần test dùng unittest để kiểm tra kết quả thực tế.
"""
import ast
import io
import json
import re
import subprocess
import sys
import tempfile
import tokenize
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC_ROOT = ROOT / "docs" / "labs"
LEDGER = ROOT / "docs" / "WORD-LAB-WHOLE-BRIEF-PROGRESS.json"
EXPECTED = {
    "ASSIGNMENT-01-student-dictionary": 10,
    "LAB-04-conditions-loops": 14,
    "LAB-05-student-list": 7,
    "LAB-05-06-gradient-descent": 5,
    "LAB-07-probability": 5,
    "LAB-08-statistics": 5,
    "LAB-10-file-csv": 6,
    "PRETEST": 3,
}
HEADING = "## TOÀN BỘ CODE PYTHON — CHÚ THÍCH NGAY SAU TỪNG DÒNG"
TASK_RE = re.compile(r"^### Câu (\d+) — English → Tiếng Việt → Giải thích$", re.M)
CODE_RE = re.compile(r"^" + r"\x60" * 3 + r"python\n([\s\S]*?)^" + r"\x60" * 3 + r"$", re.M)


def source_and_questions(slug):
    document = (DOC_ROOT / (slug + ".md")).read_text(encoding="utf-8")
    heading, sep, end = document.partition(HEADING)
    if not sep:
        raise ValueError("Missing complete code section: " + slug)
    tasks = list(TASK_RE.finditer(heading))
    matches = CODE_RE.findall(end)
    if len(matches) != 1:
        raise ValueError("Expected ONE complete script in " + slug)
    return document, heading, tasks, matches[0]


class BilingualInlineWordLabQA(unittest.TestCase):
    def test_all_eight_word_documents_have_paired_english_vietnamese_and_methods(self):
        progress = json.loads(LEDGER.read_text(encoding="utf-8"))
        self.assertEqual(progress["expected_word_documents"], 8)
        self.assertEqual(progress["completed_word_documents"], 8)
        self.assertEqual(progress["status"], "COMPLETED")
        self.assertEqual(set(EXPECTED), set(progress["final_manifest"][i].split("/")[-1].replace(".md", "") for i in range(8)))
        for slug, count in EXPECTED.items():
            with self.subTest(lab=slug):
                document, intro, questions, script = source_and_questions(slug)
                self.assertIn("SONG NGỮ", intro)
                self.assertGreater(len(document), 1500)
                self.assertEqual(len(questions), count)
                self.assertEqual([int(m.group(1)) for m in questions], list(range(1, count+1)))
                for index, match in enumerate(questions):
                    stop = questions[index + 1].start() if index + 1 < len(questions) else len(intro)
                    part = intro[match.start():stop]
                    # Match section labels, not the word "Ví dụ" inside the original question.
                    en_pos = part.find("**English —")
                    vi_pos = part.find("**Tiếng Việt —", en_pos + 1)
                    guide_pos = part.find("**Giải thích", vi_pos + 1)
                    example_pos = part.find("**Ví dụ", guide_pos + 1)
                    vocab_pos = part.find("**Thuật ngữ", example_pos + 1)
                    if vocab_pos < 0:
                        vocab_pos = part.find("**Từ vựng", example_pos + 1)
                    positions = [en_pos, vi_pos, guide_pos, example_pos, vocab_pos]
                    self.assertTrue(all(x >= 0 for x in positions), slug + ": missing EN/VI/guide/glossary")
                    self.assertEqual(positions, sorted(positions), slug + ": incorrect order")
                    self.assertRegex(part, r"\([^)]+\)")  # explain English terms in parentheses
                self.assertTrue(script.endswith("\n"))
                syntax = ast.parse(script, filename=slug + ".py")
                self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(syntax)),
                                 slug + ": educational script must not use assert")
                # A comment must be on the same physical line as code, never above it.
                comment_rows = set()
                code_rows = set()
                for tok in tokenize.generate_tokens(io.StringIO(script).readline):
                    if tok.type == tokenize.COMMENT:
                        comment_rows.add(tok.start[0])
                        self.assertGreater(tok.start[1], 0, slug + ": standalone comment")
                    elif tok.type not in (
                        tokenize.NL, tokenize.NEWLINE, tokenize.INDENT,
                        tokenize.DEDENT, tokenize.ENDMARKER, tokenize.ENCODING,
                    ):
                        code_rows.add(tok.start[0])
                self.assertTrue(code_rows, slug + ": no executable lines")
                self.assertTrue(code_rows.issubset(comment_rows),
                                slug + ": some code lines lack inline explanation")

    def test_every_standalone_solution_runs(self):
        for slug in EXPECTED:
            with self.subTest(lab=slug):
                document, _, _, script = source_and_questions(slug)
                with tempfile.TemporaryDirectory() as tmp:
                    file = Path(tmp) / "lab_solution.py"
                    file.write_text(script, encoding="utf-8")
                    # Lab10 reads students.csv next to the program in interactive mode.
                    # Demo mode uses known synthetic student records and does not overwrite it.
                    if slug == "LAB-10-file-csv":
                        csv = re.search(r"(?m)^" + r"\x60" * 3 + r"csv\n([\s\S]*?)^" + r"\x60" * 3,
                                        document)
                        if csv:
                            (Path(tmp) / "students.csv").write_text(csv.group(1), encoding="utf-8")
                    args = [sys.executable, "-B", str(file)]
                    if slug in {"ASSIGNMENT-01-student-dictionary", "LAB-05-student-list",
                                "LAB-10-file-csv"}:
                        args.append("--demo")
                    elif slug in {"LAB-05-06-gradient-descent", "LAB-07-probability",
                                  "LAB-08-statistics"}:
                        args.append("--no-plot")
                    result = subprocess.run(
                        args, cwd=tmp, capture_output=True, text=True,
                        encoding="utf-8", timeout=85
                    )
                    self.assertEqual(result.returncode, 0, slug + ": " + result.stderr)
                    if slug == "PRETEST":
                        for expected in (
                            "Actual-score mean: 66.00",
                            "Student A | 50 | 32",
                            "P(actual score >= 70): 0.400000",
                            "P(actual score >= 70 | hours >= 4): 0.666667",
                            "Updated w after one step: 2.40",
                        ):
                            self.assertIn(expected, result.stdout)

    def test_pretest_source_table_still_intact(self):
        document, intro, _, code = source_and_questions("PRETEST")
        for name, hours, attendance, score in (
            ("Student A", 2, 60, 50),
            ("Student B", 3, 65, 55),
            ("Student C", 4, 75, 65),
            ("Student D", 5, 80, 70),
            ("Student E", 6, 95, 90),
        ):
            self.assertIn(f"| {name} | {hours} | {attendance} | {score} |", intro)
        self.assertIn("L(w) = (w - 4)^2", intro)
        self.assertIn("student_data = np.array", code)


if __name__ == "__main__":
    unittest.main()
