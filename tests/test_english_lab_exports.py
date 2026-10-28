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
HEADING = "## Code Python"
TASK_RE = re.compile(r"^### Câu (\d+)$", re.M)
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
                self.assertGreater(len(document), 1500)
                sections = (
                    "## Đề bài tiếng Anh",
                    "## Đề bài tiếng Việt",
                    "## Giải thích từng câu",
                )
                positions = [intro.find(section) for section in sections]
                self.assertTrue(all(pos >= 0 for pos in positions), slug + ": missing section")
                self.assertEqual(positions, sorted(positions), slug + ": wrong section order")
                self.assertTrue(all(intro.count(section) == 1 for section in sections))
                english = intro[positions[0] + len(sections[0]):positions[1]].strip()
                vietnamese = intro[positions[1] + len(sections[1]):positions[2]].strip()
                explanations = intro[positions[2] + len(sections[2]):].strip()
                self.assertGreater(len(english), 100, slug + ": incomplete English brief")
                self.assertGreater(len(vietnamese), 100, slug + ": incomplete Vietnamese brief")
                self.assertGreater(len(explanations), 100, slug + ": incomplete explanations")
                if slug != "PRETEST":
                    original = (ROOT / "labs" / "pythoclass" / slug / "LAB.md").read_text(
                        encoding="utf-8"
                    ).strip()
                    original = re.sub(
                        r"^(#{1,3})(?=\s)",
                        lambda match: "#" * (len(match.group(1)) + 2),
                        original,
                        flags=re.M,
                    )
                    self.assertEqual(english, original, slug + ": English differs from Word")
                self.assertEqual(len(questions), count)
                self.assertEqual([int(m.group(1)) for m in questions], list(range(1, count + 1)))
                for index, match in enumerate(questions):
                    stop = questions[index + 1].start() if index + 1 < len(questions) else len(intro)
                    part = intro[match.start():stop]
                    self.assertTrue(part.strip(), slug + ": empty explanation")
                    self.assertNotIn("**English —", part)
                    self.assertNotIn("**Tiếng Việt —", part)
                    self.assertRegex(part, r"\([^)]+\)")  # define English technical terms
                    self.assertTrue("**Ví dụ" in part, slug + ": missing example")
                    self.assertTrue(
                        "**Thuật ngữ" in part or "**Từ vựng" in part,
                        slug + ": missing glossary",
                    )
                for boilerplate in (
                    "**Nguồn:**", "**Nguồn đề:**", "**Cách đọc:**", "**Cách học:**",
                    "## ĐỀ VÀ HƯỚNG GIẢI SONG NGỮ", "## ĐỀ BÀI SONG NGỮ",
                ):
                    self.assertNotIn(boilerplate, document)
                if slug == "LAB-04-conditions-loops":
                    self.assertIn("PHẦN 2: VÒNG LẶP", vietnamese)
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
