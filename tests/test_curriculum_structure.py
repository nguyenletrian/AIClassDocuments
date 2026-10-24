"""Structural and Python-syntax gates for the 46 self-study chapters.

These tests deliberately do NOT claim educational content review or execution.
Run: python -m unittest tests.test_curriculum_structure -v
"""
import ast
import re
import unittest
from pathlib import Path

CHAPTERS = Path(__file__).resolve().parents[1] / "lessons" / "chapters"
EXPECTED = 46


class CurriculumStructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.paths = sorted(CHAPTERS.glob("PY-*.vi.md"))

    def test_exact_unique_chapter_ids(self):
        self.assertEqual(len(self.paths), EXPECTED)
        ids = [int(re.search(r"PY-(\d{2})-", p.name).group(1))
               for p in self.paths]
        self.assertEqual(sorted(ids), list(range(1, EXPECTED + 1)))

    def test_chapter_structure_and_bilingual_layout(self):
        for path in self.paths:
            with self.subTest(chapter=path.name):
                text = path.read_text(encoding="utf-8")
                self.assertNotRegex(text, r"(?im)^\s*\*{0,2}(?:Trạng thái:\s*)?DRAFT\b")
                self.assertIn("## 1.", text)
                self.assertIn("## 2.", text)
                self.assertIn("## 3.", text)
                self.assertIn("## 4.", text)
                self.assertIn("## 5.", text)
                self.assertIn("## 6.", text)
                self.assertIn("## 7.", text)
                self.assertIn("## 8.", text)
                self.assertNotIn("PythoClass", text)
                self.assertNotIn("PythonClass", text)

                cases = re.findall(r"^### Tình huống ([1-5])", text, re.M)
                self.assertEqual(cases, list("12345"))
                qs = [int(x) for x in re.findall(
                    r"^\*\*Q(\d+)\..+ — .+\*\*$", text, re.M)]
                self.assertEqual(qs, list(range(1, 21)))
                options = re.findall(r"^([A-D])\. .+ — .+$", text, re.M)
                self.assertEqual(options, list("ABCD") * 20)
                qa_text = text.split("## 7.", 1)[1].split("## 8.", 1)[0]
                blocks = re.findall(
                    r"(?ms)^\*\*Q(\d+)\..*?\*\*$"
                    r"(.*?)(?=^\*\*Q\d+\.|\Z)", qa_text)
                self.assertEqual([int(q) for q, _ in blocks], list(range(1, 21)))
                for q, block in blocks:
                    answers = re.findall(r"^\*\*Đáp án: ([A-D])\*\*$", block, re.M)
                    notes = re.findall(r"^\*\*Giải thích:\*\* (.+)$", block, re.M)
                    self.assertEqual(len(answers), 1, f"Q{q}: exactly one answer")
                    self.assertEqual(len(notes), 1, f"Q{q}: one Vietnamese explanation")
                    self.assertNotIn("Explanation (English)", block)
                self.assertNotIn("### Answer key", qa_text)
                self.assertIn("**Học xong dùng để làm gì?**", text)
                self.assertIn("**Kết nối kiến thức tiếp theo:**", text)
                self.assertIn("**Từ vựng trong mục:**", text)
                cases_text = text.split("## 5.", 1)[1].split("## 6.", 1)[0]
                self.assertEqual(cases_text.count("**Tình huống thực tế:**"), 5)
                self.assertNotIn("**Vấn đề:**", cases_text)
                self.assertNotIn("**Dữ liệu:**", cases_text)
                for i in range(1, 5):
                    section = re.search(
                        rf"^### 4\.{i}\..+\n\n\*\*Từ vựng trong mục:",
                        text, re.M)
                    self.assertIsNotNone(section, f"4.{i} in {path.name}")

    def test_python_code_blocks_parse(self):
        for path in self.paths:
            with self.subTest(chapter=path.name):
                text = path.read_text(encoding="utf-8")
                py_blocks = re.findall(
                    r"^\x60\x60\x60python\n(.*?)^\x60\x60\x60$", text,
                    re.M | re.S)
                bash_blocks = re.findall(
                    r"^\x60\x60\x60bash\n(.*?)^\x60\x60\x60$", text,
                    re.M | re.S)
                if "PY-43-" in path.name:
                    self.assertEqual(len(bash_blocks), 9)
                else:
                    self.assertEqual(len(py_blocks), 9)
                for i, code in enumerate(py_blocks):
                    with self.subTest(block=i + 1):
                        ast.parse(code, filename=f"{path.name}:{i+1}")

    def test_markdown_images_exist(self):
        for path in self.paths:
            body = path.read_text(encoding="utf-8")
            refs = re.findall(r"!\[[^\n]*\]\(([^)\n]+)\)", body)
            for ref in refs:
                with self.subTest(file=path.name, image=ref):
                    self.assertFalse(ref.startswith(("http:", "https:")))
                    self.assertTrue((path.parent / ref).is_file())

    def test_style_guide_has_the_exact_line_contract(self):
        root = CHAPTERS.parents[1]
        guide = (root / "docs" / "CURRICULUM-STYLE-GUIDE.md").read_text("utf-8")
        self.assertIn("CÙNG MỘT DÒNG", guide)
        self.assertIn("5 tình huống", guide)
        self.assertIn("20 câu", guide)


if __name__ == "__main__":
    unittest.main()
