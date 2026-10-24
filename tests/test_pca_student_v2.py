"""End-to-end syntax, structure and five practical PCA scenarios from the lesson."""
import ast
import contextlib
import io
import os
import re
import unittest
from pathlib import Path
from xml.etree import ElementTree as ET
from unittest.mock import patch

os.environ.setdefault("MPLBACKEND", "Agg")
LESSON = Path(__file__).resolve().parents[1] / "lessons" / "pilot" / "AI-MATH-01-pca.vi.md"


class StudentPcaLessonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = LESSON.read_text(encoding="utf-8")
        cls.blocks = re.findall(r"```python\n(.*?)\n```", cls.text, re.S)

    def test_student_first_layout_and_no_internal_sources(self):
        for expected in ("## 1. PCA nằm ở đâu", "## 2. English vocabulary",
                         "## 3. Thư viện và hàm Python", "## 4. PCA và các khái niệm liên quan",
                         "## 5. Năm tình huống", "## 7. English–Vietnamese multiple-choice"):
            self.assertIn(expected, self.text)
        self.assertEqual(len(re.findall(r"^### Tình huống [1-5]", self.text, re.M)), 5)
        self.assertEqual(len(re.findall(r"^\*\*Q\d+\.", self.text, re.M)), 20)
        for forbidden in ("PythoClass", "PythonClass", "Toán học đằng sau", "Sau bài học"):
            self.assertNotIn(forbidden, self.text)
        self.assertEqual(len(self.blocks), 11)
        # Each of the five cases must justify its choice, not only give steps.
        self.assertEqual(self.text.count("**Vì sao chọn cách này?**"), 5)
        # Terms and dataset structure are reiterated before calculations.
        self.assertEqual(self.text.count("**Nhắc lại kiến thức liên quan:**"), 4)
        self.assertEqual(self.text.count("**Nhắc lại kiến thức để giải bài:**"), 5)
        self.assertEqual(self.text.count("**Dữ liệu sử dụng:**"), 5)
        self.assertEqual(len(re.findall(r"^### Tình huống [1-5]", self.text, re.M)), 5)
        self.assertEqual(len(re.findall(r"^\| Q\d+ \|", self.text, re.M)), 20)
        self.assertNotIn("Subconcept", self.text)
        # Feature/Vector/Matrix are defined in prose before the first code sample.
        concepts = self.text.split("### 4.2.", 1)[1].split("### 4.3.", 1)[0]
        for concept in ("**Feature:**", "**Vector:**", "**Matrix:**"):
            self.assertIn(concept, concepts)
        self.assertLess(concepts.index("**Feature:**"), concepts.index("```python"))
        self.assertLess(concepts.index("**Vector:**"), concepts.index("```python"))


    def test_explanations_progress_from_vectors_to_matrix(self):
        # The concept example must construct five profiles, then stack them.
        section = self.text.split("### 4.2.", 1)[1].split("### 4.3.", 1)[0]
        for expected in (
            "**Nhắc lại các khái niệm", "5 khách hàng → 5 vector → 1 ma trận",
            "**5 khách → 5 vector:**", "**5 vector → 1 matrix:**",
            "customer_1 =", "customer_5 =", "np.vstack(customer_vectors)",
            "print(\"Shape:\", X.shape)  # (5, 5)",
        ):
            self.assertIn(expected, section)
        self.assertLess(section.index("**Nhắc lại"), section.index("customer_1 ="))
        self.assertLess(section.index("customer_1 ="), section.index("np.vstack"))

        # Run the small example by itself. Rows correspond to 5 customers,
        # columns to the declared five features in the same fixed order.
        block = re.search(r"```python\n(.*?)\n```", section, re.S)
        self.assertIsNotNone(block)
        scope = {}
        with contextlib.redirect_stdout(io.StringIO()):
            exec(compile(block.group(1), "concept-4.2.py", "exec"), scope)
        self.assertEqual(scope["X"].shape, (5, 5))
        self.assertEqual(len(scope["customer_vectors"]), 5)
        self.assertEqual(scope["X"][:, 2].tolist(), [950, 1200, 500, 1600, 220])

    def test_each_scenario_labels_rows_columns_and_units(self):
        scenario_code = [
            re.search(
                r"^### Tình huống " + str(i) + r" —.*?^```python\n(.*?)\n```",
                self.text, re.M | re.S
            ).group(1)
            for i in range(1, 6)
        ]
        for i, block in enumerate(scenario_code, start=1):
            with self.subTest(scenario=i):
                self.assertRegex(block, r"(?i)HÀNG|hàng")
                self.assertRegex(block, r"(?i)CỘT|cột")
                self.assertRegex(block, r"(?i)BƯỚC 1")
                self.assertRegex(block, r"(?i)giờ|phút|đơn|đồng|cm|đơn vị")
        self.assertIn("iris.target là NHÃN loài hoa", scenario_code[4])
        self.assertIn("profiles.shape", scenario_code[0])

    def test_named_arguments_are_grouped_with_their_functions(self):
        library = self.text.split('## 3.', 1)[1].split('## 4.', 1)[0]
        self.assertNotIn('### 3.3.', library)  # No separate flag catalog.
        examples = (
            ('np.array(data, dtype=float)', 'dtype=float'),
            ('X.mean(axis=0)', 'axis=0'),
            ('np.cov(X, rowvar=False)', 'rowvar=False'),
            ('PCA(n_components=2)', 'n_components=2'),
            ('PCA(n_components=1)', 'n_components=1'),
            ('PCA(n_components=0.95, svd_solver="full")', 'svd_solver="full"'),
            ('KMeans(n_clusters=2, random_state=42, n_init=10)', 'n_init=10'),
            ('LogisticRegression(max_iter=1000)', 'max_iter=1000'),
            ('train_test_split(..., test_size=0.25, stratify=iris.target, random_state=42)', 'test_size=0.25'),
        )
        for signature, argument in examples:
            with self.subTest(signature=signature):
                matches = [line for line in library.splitlines() if line.startswith('| ') and signature in line]
                self.assertEqual(len(matches), 1, signature)
                self.assertIn(argument, matches[0])
                self.assertIn(' | ', matches[0])  # Explanation co-located in API table.
        self.assertIn('số thực', library)  # dtype=float is explained alongside np.array.
        code_blocks = '\n'.join(self.blocks)
        for flag in ('dtype=float', 'axis=0', 'rowvar=False', 'random_state=42', 'n_init=10'):
            with self.subTest(no_redundant_note=flag):
                self.assertNotRegex(code_blocks, r'(?m)^\s*#\s*' + re.escape(flag) + r'\s*:')

    def test_each_section_has_a_small_term_glossary(self):
        parts = [
            '## 1.', '## 3.', '## 4.',
            *[f'### 4.{i}.' for i in range(1, 7)],
            '## 5.', *[f'### Tình huống {i}' for i in range(1, 6)],
            '## 6.', '## 8.',
        ]
        lines = self.text.splitlines()
        for heading in parts:
            with self.subTest(heading=heading):
                matches = [i for i, line in enumerate(lines) if line.startswith(heading)]
                self.assertEqual(len(matches), 1, heading)
                # A short glossary must come immediately after the section heading.
                follow = '\n'.join(lines[matches[0]+1:matches[0]+4])
                self.assertIn('**Từ vựng trong mục:**', follow)
        eigen = self.text.split('### 4.4.', 1)[1].split('### 4.5.', 1)[0]
        self.assertIn('**Eigenvector** — vector riêng', eigen)
        self.assertIn('**Eigenvalue** — giá trị riêng', eigen)
        self.assertIn('**Covariance** — hiệp phương sai', eigen)
        self.assertNotIn('Eigenvector (vector riêng)', eigen)

    def test_bilingual_quiz_includes_every_option_and_key(self):
        quiz = self.text.split('## 7. English–Vietnamese', 1)[1].split('## 8.', 1)[0]
        self.assertEqual(len(re.findall(r'^\*\*Q\d+\.', quiz, re.M)), 20)
        self.assertEqual(quiz.count('*Tiếng Việt: '), 0)
        self.assertEqual(len(re.findall(r'^\*\*Q\d+\..+ — .+\*\*
        self.assertEqual(len(re.findall(r'^\| Q\d+ \|', quiz, re.M)), 20)
        # English and Vietnamese must be on the same line for every option.
        items = re.findall(r'^[A-D]\. .+ — .+
        self.assertEqual(len(items), 80)
        self.assertIn('Explanation (English)', quiz)
        self.assertIn('Giải thích (Tiếng Việt)', quiz)
        self.assertNotIn('scatter plot (biểu đồ phân tán)', quiz)

    def test_all_markdown_images_exist_at_relative_paths(self):
        refs = re.findall(r'!\[[^\n]*\]\(([^)\n]+)\)', self.text)
        self.assertEqual(sorted(refs), sorted([
            'assets/pca-before-after.svg', 'assets/pca-direction-intuition.svg',
        ]))
        for ref in refs:
            self.assertTrue((LESSON.parent / ref).is_file(), ref)
            self.assertNotIn('(', ref)  # Previous automatic translation broke paths.

    def test_five_immediate_self_checks_and_advanced_labels(self):
        sections = [
            self.text.split(f"### 4.{i}.", 1)[1].split(f"### 4.{i+1}.", 1)[0]
            for i in range(2, 6)
        ]
        sections.append(
            self.text.split("### 4.6.", 1)[1].split("## 5.", 1)[0]
        )
        for i, section in enumerate(sections, start=2):
            with self.subTest(concept=i):
                self.assertIn(f"**Tự kiểm tra nhanh — 4.{i}:**", section)
                self.assertIn("**Đáp án gợi ý:**", section)
        self.assertGreaterEqual(self.text.count("**Phần mở rộng — có thể đọc sau:**"), 2)
        self.assertIn("KMeans", self.text)
        self.assertIn("LogisticRegression", self.text)

    def test_before_after_table_matches_real_pca_values(self):
        # Exact synthetic student data from the lesson, NOT a screenshot guess.
        import numpy as np
        from sklearn.preprocessing import StandardScaler
        from sklearn.decomposition import PCA

        data = np.array([
            [80, 81, 72, 20, 90], [85, 88, 80, 22, 95],
            [60, 65, 72, 12, 75], [70, 72, 68, 15, 80],
            [90, 91, 88, 25, 98], [88, 87, 89, 20, 90],
            [40, 45, 50, 10, 70], [75, 73, 76, 15, 85],
        ], dtype=float)
        pca = PCA(n_components=2)
        points = pca.fit_transform(StandardScaler().fit_transform(data))
        expected = (
            ("SV1", "0.75", "-0.54"),
            ("SV2", "1.85", "-0.40"),
            ("SV3", "-1.81", "0.71"),
        )
        section = self.text.split("### 4.5.", 1)[1].split("### 4.6.", 1)[0]
        self.assertIn("![Bảng dữ liệu gốc", section)
        for n, (label, x, y) in enumerate(expected):
            self.assertEqual(label, f"SV{n+1}")
            self.assertAlmostEqual(points[n, 0], float(x), delta=.006)
            self.assertAlmostEqual(points[n, 1], float(y), delta=.006)
            self.assertRegex(section, rf"\| {label} \| .* \| {re.escape(x)} \| {re.escape(y)} \|")
        self.assertAlmostEqual(pca.explained_variance_ratio_.sum(), .9865238828, places=7)
        self.assertIn("98,65%", section)

    def test_source_figures_are_local_svg_and_pca_coordinates_match(self):
        assets = LESSON.parent / "assets"
        paths = [
            assets / "pca-before-after.svg",
            assets / "pca-direction-intuition.svg",
        ]
        for path in paths:
            self.assertTrue(path.is_file(), str(path))
            root = ET.parse(path).getroot()
            self.assertTrue(root.tag.endswith("svg"))
            self.assertFalse(any(
                key.lower().endswith("href") and ("http://" in val or "https://" in val)
                for element in root.iter()
                for key, val in element.attrib.items()
            ))
        before = ET.parse(paths[0]).getroot()
        nodes = [
            element for element in before.iter()
            if element.attrib.get("data-student", "").startswith("SV")
        ]
        self.assertEqual(len(nodes), 8)
        import numpy as np
        from sklearn.preprocessing import StandardScaler
        from sklearn.decomposition import PCA
        profiles = np.array([
            [80, 81, 72, 20, 90], [85, 88, 80, 22, 95],
            [60, 65, 72, 12, 75], [70, 72, 68, 15, 80],
            [90, 91, 88, 25, 98], [88, 87, 89, 20, 90],
            [40, 45, 50, 10, 70], [75, 73, 76, 15, 85],
        ], dtype=float)
        coords = PCA(n_components=2).fit_transform(StandardScaler().fit_transform(profiles))
        for i, node in enumerate(nodes):
            self.assertEqual(node.attrib["data-student"], f"SV{i+1}")
            self.assertAlmostEqual(float(node.attrib["data-pc1"]), coords[i, 0], delta=.0001)
            self.assertAlmostEqual(float(node.attrib["data-pc2"]), coords[i, 1], delta=.0001)

    def test_all_python_snippets_have_valid_syntax(self):
        for number, block in enumerate(self.blocks, 1):
            with self.subTest(number=number):
                ast.parse(block)

    def run_scenario(self, number):
        match = re.search(r"^### Tình huống " + str(number) + r" —.*?^```python\n(.*?)\n```",
                          self.text, re.M | re.S)
        self.assertIsNotNone(match)
        ns, printed = {"__name__": "__main__"}, io.StringIO()
        with contextlib.redirect_stdout(printed), patch("matplotlib.pyplot.show"):
            exec(compile(match.group(1), "scenario-" + str(number) + ".py", "exec"), ns)
        return ns, printed.getvalue()

    def test_scenario_1_school_profiles(self):
        ns, output = self.run_scenario(1)
        self.assertEqual(ns["map_2d"].shape, (8, 2))
        self.assertAlmostEqual(ns["pca"].explained_variance_ratio_.sum(), .9865238828, places=6)
        self.assertIn("98.65", output)

    def test_scenario_2_sensor_redundancy(self):
        ns, output = self.run_scenario(2)
        self.assertEqual(ns["compressed"].shape, (8, 1))
        self.assertGreater(ns["pca"].explained_variance_ratio_.sum(), .999)

    def test_scenario_3_customers(self):
        ns, output = self.run_scenario(3)
        self.assertEqual(ns["locations"].shape, (10, 2))
        self.assertEqual(sorted(ns["np"].bincount(ns["labels"]).tolist()), [5, 5])

    def test_scenario_4_auto_variance_threshold(self):
        ns, output = self.run_scenario(4)
        self.assertEqual(ns["compressed"].shape[0], 8)
        self.assertGreaterEqual(ns["pca"].explained_variance_ratio_.sum(), .95)

    def test_scenario_5_no_data_leakage(self):
        ns, output = self.run_scenario(5)
        self.assertEqual((len(ns["X_train"]), len(ns["X_test"])), (112, 38))
        self.assertEqual(ns["with_pca"].named_steps["reduce"].n_components_, 2)
        self.assertTrue(0 <= ns["with_pca"].score(ns["X_test"], ns["y_test"]) <= 1)
        self.assertTrue(0 <= ns["without_pca"].score(ns["X_test"], ns["y_test"]) <= 1)


if __name__ == "__main__":
    unittest.main()
, quiz, re.M)), 20)
        self.assertEqual(len(re.findall(r'^\| Q\d+ \|', quiz, re.M)), 20)
        # Each English option is followed by a Vietnamese translation line.
        items = re.findall(r'^[A-D]\. [^\n]+\n\*[^\n]+\*', quiz, re.M)
        self.assertEqual(len(items), 80)
        self.assertIn('Explanation (English)', quiz)
        self.assertIn('Giải thích (Tiếng Việt)', quiz)
        self.assertNotIn('scatter plot (biểu đồ phân tán)', quiz)

    def test_all_markdown_images_exist_at_relative_paths(self):
        refs = re.findall(r'!\[[^\n]*\]\(([^)\n]+)\)', self.text)
        self.assertEqual(sorted(refs), sorted([
            'assets/pca-before-after.svg', 'assets/pca-direction-intuition.svg',
        ]))
        for ref in refs:
            self.assertTrue((LESSON.parent / ref).is_file(), ref)
            self.assertNotIn('(', ref)  # Previous automatic translation broke paths.

    def test_five_immediate_self_checks_and_advanced_labels(self):
        sections = [
            self.text.split(f"### 4.{i}.", 1)[1].split(f"### 4.{i+1}.", 1)[0]
            for i in range(2, 6)
        ]
        sections.append(
            self.text.split("### 4.6.", 1)[1].split("## 5.", 1)[0]
        )
        for i, section in enumerate(sections, start=2):
            with self.subTest(concept=i):
                self.assertIn(f"**Tự kiểm tra nhanh — 4.{i}:**", section)
                self.assertIn("**Đáp án gợi ý:**", section)
        self.assertGreaterEqual(self.text.count("**Phần mở rộng — có thể đọc sau:**"), 2)
        self.assertIn("KMeans", self.text)
        self.assertIn("LogisticRegression", self.text)

    def test_before_after_table_matches_real_pca_values(self):
        # Exact synthetic student data from the lesson, NOT a screenshot guess.
        import numpy as np
        from sklearn.preprocessing import StandardScaler
        from sklearn.decomposition import PCA

        data = np.array([
            [80, 81, 72, 20, 90], [85, 88, 80, 22, 95],
            [60, 65, 72, 12, 75], [70, 72, 68, 15, 80],
            [90, 91, 88, 25, 98], [88, 87, 89, 20, 90],
            [40, 45, 50, 10, 70], [75, 73, 76, 15, 85],
        ], dtype=float)
        pca = PCA(n_components=2)
        points = pca.fit_transform(StandardScaler().fit_transform(data))
        expected = (
            ("SV1", "0.75", "-0.54"),
            ("SV2", "1.85", "-0.40"),
            ("SV3", "-1.81", "0.71"),
        )
        section = self.text.split("### 4.5.", 1)[1].split("### 4.6.", 1)[0]
        self.assertIn("![Bảng dữ liệu gốc", section)
        for n, (label, x, y) in enumerate(expected):
            self.assertEqual(label, f"SV{n+1}")
            self.assertAlmostEqual(points[n, 0], float(x), delta=.006)
            self.assertAlmostEqual(points[n, 1], float(y), delta=.006)
            self.assertRegex(section, rf"\| {label} \| .* \| {re.escape(x)} \| {re.escape(y)} \|")
        self.assertAlmostEqual(pca.explained_variance_ratio_.sum(), .9865238828, places=7)
        self.assertIn("98,65%", section)

    def test_source_figures_are_local_svg_and_pca_coordinates_match(self):
        assets = LESSON.parent / "assets"
        paths = [
            assets / "pca-before-after.svg",
            assets / "pca-direction-intuition.svg",
        ]
        for path in paths:
            self.assertTrue(path.is_file(), str(path))
            root = ET.parse(path).getroot()
            self.assertTrue(root.tag.endswith("svg"))
            self.assertFalse(any(
                key.lower().endswith("href") and ("http://" in val or "https://" in val)
                for element in root.iter()
                for key, val in element.attrib.items()
            ))
        before = ET.parse(paths[0]).getroot()
        nodes = [
            element for element in before.iter()
            if element.attrib.get("data-student", "").startswith("SV")
        ]
        self.assertEqual(len(nodes), 8)
        import numpy as np
        from sklearn.preprocessing import StandardScaler
        from sklearn.decomposition import PCA
        profiles = np.array([
            [80, 81, 72, 20, 90], [85, 88, 80, 22, 95],
            [60, 65, 72, 12, 75], [70, 72, 68, 15, 80],
            [90, 91, 88, 25, 98], [88, 87, 89, 20, 90],
            [40, 45, 50, 10, 70], [75, 73, 76, 15, 85],
        ], dtype=float)
        coords = PCA(n_components=2).fit_transform(StandardScaler().fit_transform(profiles))
        for i, node in enumerate(nodes):
            self.assertEqual(node.attrib["data-student"], f"SV{i+1}")
            self.assertAlmostEqual(float(node.attrib["data-pc1"]), coords[i, 0], delta=.0001)
            self.assertAlmostEqual(float(node.attrib["data-pc2"]), coords[i, 1], delta=.0001)

    def test_all_python_snippets_have_valid_syntax(self):
        for number, block in enumerate(self.blocks, 1):
            with self.subTest(number=number):
                ast.parse(block)

    def run_scenario(self, number):
        match = re.search(r"^### Tình huống " + str(number) + r" —.*?^```python\n(.*?)\n```",
                          self.text, re.M | re.S)
        self.assertIsNotNone(match)
        ns, printed = {"__name__": "__main__"}, io.StringIO()
        with contextlib.redirect_stdout(printed), patch("matplotlib.pyplot.show"):
            exec(compile(match.group(1), "scenario-" + str(number) + ".py", "exec"), ns)
        return ns, printed.getvalue()

    def test_scenario_1_school_profiles(self):
        ns, output = self.run_scenario(1)
        self.assertEqual(ns["map_2d"].shape, (8, 2))
        self.assertAlmostEqual(ns["pca"].explained_variance_ratio_.sum(), .9865238828, places=6)
        self.assertIn("98.65", output)

    def test_scenario_2_sensor_redundancy(self):
        ns, output = self.run_scenario(2)
        self.assertEqual(ns["compressed"].shape, (8, 1))
        self.assertGreater(ns["pca"].explained_variance_ratio_.sum(), .999)

    def test_scenario_3_customers(self):
        ns, output = self.run_scenario(3)
        self.assertEqual(ns["locations"].shape, (10, 2))
        self.assertEqual(sorted(ns["np"].bincount(ns["labels"]).tolist()), [5, 5])

    def test_scenario_4_auto_variance_threshold(self):
        ns, output = self.run_scenario(4)
        self.assertEqual(ns["compressed"].shape[0], 8)
        self.assertGreaterEqual(ns["pca"].explained_variance_ratio_.sum(), .95)

    def test_scenario_5_no_data_leakage(self):
        ns, output = self.run_scenario(5)
        self.assertEqual((len(ns["X_train"]), len(ns["X_test"])), (112, 38))
        self.assertEqual(ns["with_pca"].named_steps["reduce"].n_components_, 2)
        self.assertTrue(0 <= ns["with_pca"].score(ns["X_test"], ns["y_test"]) <= 1)
        self.assertTrue(0 <= ns["without_pca"].score(ns["X_test"], ns["y_test"]) <= 1)


if __name__ == "__main__":
    unittest.main()
, quiz, re.M)
        self.assertEqual(len(items), 80)
        self.assertIn('Explanation (English)', quiz)
        self.assertIn('Giải thích (Tiếng Việt)', quiz)
        self.assertNotIn('scatter plot (biểu đồ phân tán)', quiz)

    def test_all_markdown_images_exist_at_relative_paths(self):
        refs = re.findall(r'!\[[^\n]*\]\(([^)\n]+)\)', self.text)
        self.assertEqual(sorted(refs), sorted([
            'assets/pca-before-after.svg', 'assets/pca-direction-intuition.svg',
        ]))
        for ref in refs:
            self.assertTrue((LESSON.parent / ref).is_file(), ref)
            self.assertNotIn('(', ref)  # Previous automatic translation broke paths.

    def test_five_immediate_self_checks_and_advanced_labels(self):
        sections = [
            self.text.split(f"### 4.{i}.", 1)[1].split(f"### 4.{i+1}.", 1)[0]
            for i in range(2, 6)
        ]
        sections.append(
            self.text.split("### 4.6.", 1)[1].split("## 5.", 1)[0]
        )
        for i, section in enumerate(sections, start=2):
            with self.subTest(concept=i):
                self.assertIn(f"**Tự kiểm tra nhanh — 4.{i}:**", section)
                self.assertIn("**Đáp án gợi ý:**", section)
        self.assertGreaterEqual(self.text.count("**Phần mở rộng — có thể đọc sau:**"), 2)
        self.assertIn("KMeans", self.text)
        self.assertIn("LogisticRegression", self.text)

    def test_before_after_table_matches_real_pca_values(self):
        # Exact synthetic student data from the lesson, NOT a screenshot guess.
        import numpy as np
        from sklearn.preprocessing import StandardScaler
        from sklearn.decomposition import PCA

        data = np.array([
            [80, 81, 72, 20, 90], [85, 88, 80, 22, 95],
            [60, 65, 72, 12, 75], [70, 72, 68, 15, 80],
            [90, 91, 88, 25, 98], [88, 87, 89, 20, 90],
            [40, 45, 50, 10, 70], [75, 73, 76, 15, 85],
        ], dtype=float)
        pca = PCA(n_components=2)
        points = pca.fit_transform(StandardScaler().fit_transform(data))
        expected = (
            ("SV1", "0.75", "-0.54"),
            ("SV2", "1.85", "-0.40"),
            ("SV3", "-1.81", "0.71"),
        )
        section = self.text.split("### 4.5.", 1)[1].split("### 4.6.", 1)[0]
        self.assertIn("![Bảng dữ liệu gốc", section)
        for n, (label, x, y) in enumerate(expected):
            self.assertEqual(label, f"SV{n+1}")
            self.assertAlmostEqual(points[n, 0], float(x), delta=.006)
            self.assertAlmostEqual(points[n, 1], float(y), delta=.006)
            self.assertRegex(section, rf"\| {label} \| .* \| {re.escape(x)} \| {re.escape(y)} \|")
        self.assertAlmostEqual(pca.explained_variance_ratio_.sum(), .9865238828, places=7)
        self.assertIn("98,65%", section)

    def test_source_figures_are_local_svg_and_pca_coordinates_match(self):
        assets = LESSON.parent / "assets"
        paths = [
            assets / "pca-before-after.svg",
            assets / "pca-direction-intuition.svg",
        ]
        for path in paths:
            self.assertTrue(path.is_file(), str(path))
            root = ET.parse(path).getroot()
            self.assertTrue(root.tag.endswith("svg"))
            self.assertFalse(any(
                key.lower().endswith("href") and ("http://" in val or "https://" in val)
                for element in root.iter()
                for key, val in element.attrib.items()
            ))
        before = ET.parse(paths[0]).getroot()
        nodes = [
            element for element in before.iter()
            if element.attrib.get("data-student", "").startswith("SV")
        ]
        self.assertEqual(len(nodes), 8)
        import numpy as np
        from sklearn.preprocessing import StandardScaler
        from sklearn.decomposition import PCA
        profiles = np.array([
            [80, 81, 72, 20, 90], [85, 88, 80, 22, 95],
            [60, 65, 72, 12, 75], [70, 72, 68, 15, 80],
            [90, 91, 88, 25, 98], [88, 87, 89, 20, 90],
            [40, 45, 50, 10, 70], [75, 73, 76, 15, 85],
        ], dtype=float)
        coords = PCA(n_components=2).fit_transform(StandardScaler().fit_transform(profiles))
        for i, node in enumerate(nodes):
            self.assertEqual(node.attrib["data-student"], f"SV{i+1}")
            self.assertAlmostEqual(float(node.attrib["data-pc1"]), coords[i, 0], delta=.0001)
            self.assertAlmostEqual(float(node.attrib["data-pc2"]), coords[i, 1], delta=.0001)

    def test_all_python_snippets_have_valid_syntax(self):
        for number, block in enumerate(self.blocks, 1):
            with self.subTest(number=number):
                ast.parse(block)

    def run_scenario(self, number):
        match = re.search(r"^### Tình huống " + str(number) + r" —.*?^```python\n(.*?)\n```",
                          self.text, re.M | re.S)
        self.assertIsNotNone(match)
        ns, printed = {"__name__": "__main__"}, io.StringIO()
        with contextlib.redirect_stdout(printed), patch("matplotlib.pyplot.show"):
            exec(compile(match.group(1), "scenario-" + str(number) + ".py", "exec"), ns)
        return ns, printed.getvalue()

    def test_scenario_1_school_profiles(self):
        ns, output = self.run_scenario(1)
        self.assertEqual(ns["map_2d"].shape, (8, 2))
        self.assertAlmostEqual(ns["pca"].explained_variance_ratio_.sum(), .9865238828, places=6)
        self.assertIn("98.65", output)

    def test_scenario_2_sensor_redundancy(self):
        ns, output = self.run_scenario(2)
        self.assertEqual(ns["compressed"].shape, (8, 1))
        self.assertGreater(ns["pca"].explained_variance_ratio_.sum(), .999)

    def test_scenario_3_customers(self):
        ns, output = self.run_scenario(3)
        self.assertEqual(ns["locations"].shape, (10, 2))
        self.assertEqual(sorted(ns["np"].bincount(ns["labels"]).tolist()), [5, 5])

    def test_scenario_4_auto_variance_threshold(self):
        ns, output = self.run_scenario(4)
        self.assertEqual(ns["compressed"].shape[0], 8)
        self.assertGreaterEqual(ns["pca"].explained_variance_ratio_.sum(), .95)

    def test_scenario_5_no_data_leakage(self):
        ns, output = self.run_scenario(5)
        self.assertEqual((len(ns["X_train"]), len(ns["X_test"])), (112, 38))
        self.assertEqual(ns["with_pca"].named_steps["reduce"].n_components_, 2)
        self.assertTrue(0 <= ns["with_pca"].score(ns["X_test"], ns["y_test"]) <= 1)
        self.assertTrue(0 <= ns["without_pca"].score(ns["X_test"], ns["y_test"]) <= 1)


if __name__ == "__main__":
    unittest.main()
, quiz, re.M)), 20)
        self.assertEqual(len(re.findall(r'^\| Q\d+ \|', quiz, re.M)), 20)
        # Each English option is followed by a Vietnamese translation line.
        items = re.findall(r'^[A-D]\. [^\n]+\n\*[^\n]+\*', quiz, re.M)
        self.assertEqual(len(items), 80)
        self.assertIn('Explanation (English)', quiz)
        self.assertIn('Giải thích (Tiếng Việt)', quiz)
        self.assertNotIn('scatter plot (biểu đồ phân tán)', quiz)

    def test_all_markdown_images_exist_at_relative_paths(self):
        refs = re.findall(r'!\[[^\n]*\]\(([^)\n]+)\)', self.text)
        self.assertEqual(sorted(refs), sorted([
            'assets/pca-before-after.svg', 'assets/pca-direction-intuition.svg',
        ]))
        for ref in refs:
            self.assertTrue((LESSON.parent / ref).is_file(), ref)
            self.assertNotIn('(', ref)  # Previous automatic translation broke paths.

    def test_five_immediate_self_checks_and_advanced_labels(self):
        sections = [
            self.text.split(f"### 4.{i}.", 1)[1].split(f"### 4.{i+1}.", 1)[0]
            for i in range(2, 6)
        ]
        sections.append(
            self.text.split("### 4.6.", 1)[1].split("## 5.", 1)[0]
        )
        for i, section in enumerate(sections, start=2):
            with self.subTest(concept=i):
                self.assertIn(f"**Tự kiểm tra nhanh — 4.{i}:**", section)
                self.assertIn("**Đáp án gợi ý:**", section)
        self.assertGreaterEqual(self.text.count("**Phần mở rộng — có thể đọc sau:**"), 2)
        self.assertIn("KMeans", self.text)
        self.assertIn("LogisticRegression", self.text)

    def test_before_after_table_matches_real_pca_values(self):
        # Exact synthetic student data from the lesson, NOT a screenshot guess.
        import numpy as np
        from sklearn.preprocessing import StandardScaler
        from sklearn.decomposition import PCA

        data = np.array([
            [80, 81, 72, 20, 90], [85, 88, 80, 22, 95],
            [60, 65, 72, 12, 75], [70, 72, 68, 15, 80],
            [90, 91, 88, 25, 98], [88, 87, 89, 20, 90],
            [40, 45, 50, 10, 70], [75, 73, 76, 15, 85],
        ], dtype=float)
        pca = PCA(n_components=2)
        points = pca.fit_transform(StandardScaler().fit_transform(data))
        expected = (
            ("SV1", "0.75", "-0.54"),
            ("SV2", "1.85", "-0.40"),
            ("SV3", "-1.81", "0.71"),
        )
        section = self.text.split("### 4.5.", 1)[1].split("### 4.6.", 1)[0]
        self.assertIn("![Bảng dữ liệu gốc", section)
        for n, (label, x, y) in enumerate(expected):
            self.assertEqual(label, f"SV{n+1}")
            self.assertAlmostEqual(points[n, 0], float(x), delta=.006)
            self.assertAlmostEqual(points[n, 1], float(y), delta=.006)
            self.assertRegex(section, rf"\| {label} \| .* \| {re.escape(x)} \| {re.escape(y)} \|")
        self.assertAlmostEqual(pca.explained_variance_ratio_.sum(), .9865238828, places=7)
        self.assertIn("98,65%", section)

    def test_source_figures_are_local_svg_and_pca_coordinates_match(self):
        assets = LESSON.parent / "assets"
        paths = [
            assets / "pca-before-after.svg",
            assets / "pca-direction-intuition.svg",
        ]
        for path in paths:
            self.assertTrue(path.is_file(), str(path))
            root = ET.parse(path).getroot()
            self.assertTrue(root.tag.endswith("svg"))
            self.assertFalse(any(
                key.lower().endswith("href") and ("http://" in val or "https://" in val)
                for element in root.iter()
                for key, val in element.attrib.items()
            ))
        before = ET.parse(paths[0]).getroot()
        nodes = [
            element for element in before.iter()
            if element.attrib.get("data-student", "").startswith("SV")
        ]
        self.assertEqual(len(nodes), 8)
        import numpy as np
        from sklearn.preprocessing import StandardScaler
        from sklearn.decomposition import PCA
        profiles = np.array([
            [80, 81, 72, 20, 90], [85, 88, 80, 22, 95],
            [60, 65, 72, 12, 75], [70, 72, 68, 15, 80],
            [90, 91, 88, 25, 98], [88, 87, 89, 20, 90],
            [40, 45, 50, 10, 70], [75, 73, 76, 15, 85],
        ], dtype=float)
        coords = PCA(n_components=2).fit_transform(StandardScaler().fit_transform(profiles))
        for i, node in enumerate(nodes):
            self.assertEqual(node.attrib["data-student"], f"SV{i+1}")
            self.assertAlmostEqual(float(node.attrib["data-pc1"]), coords[i, 0], delta=.0001)
            self.assertAlmostEqual(float(node.attrib["data-pc2"]), coords[i, 1], delta=.0001)

    def test_all_python_snippets_have_valid_syntax(self):
        for number, block in enumerate(self.blocks, 1):
            with self.subTest(number=number):
                ast.parse(block)

    def run_scenario(self, number):
        match = re.search(r"^### Tình huống " + str(number) + r" —.*?^```python\n(.*?)\n```",
                          self.text, re.M | re.S)
        self.assertIsNotNone(match)
        ns, printed = {"__name__": "__main__"}, io.StringIO()
        with contextlib.redirect_stdout(printed), patch("matplotlib.pyplot.show"):
            exec(compile(match.group(1), "scenario-" + str(number) + ".py", "exec"), ns)
        return ns, printed.getvalue()

    def test_scenario_1_school_profiles(self):
        ns, output = self.run_scenario(1)
        self.assertEqual(ns["map_2d"].shape, (8, 2))
        self.assertAlmostEqual(ns["pca"].explained_variance_ratio_.sum(), .9865238828, places=6)
        self.assertIn("98.65", output)

    def test_scenario_2_sensor_redundancy(self):
        ns, output = self.run_scenario(2)
        self.assertEqual(ns["compressed"].shape, (8, 1))
        self.assertGreater(ns["pca"].explained_variance_ratio_.sum(), .999)

    def test_scenario_3_customers(self):
        ns, output = self.run_scenario(3)
        self.assertEqual(ns["locations"].shape, (10, 2))
        self.assertEqual(sorted(ns["np"].bincount(ns["labels"]).tolist()), [5, 5])

    def test_scenario_4_auto_variance_threshold(self):
        ns, output = self.run_scenario(4)
        self.assertEqual(ns["compressed"].shape[0], 8)
        self.assertGreaterEqual(ns["pca"].explained_variance_ratio_.sum(), .95)

    def test_scenario_5_no_data_leakage(self):
        ns, output = self.run_scenario(5)
        self.assertEqual((len(ns["X_train"]), len(ns["X_test"])), (112, 38))
        self.assertEqual(ns["with_pca"].named_steps["reduce"].n_components_, 2)
        self.assertTrue(0 <= ns["with_pca"].score(ns["X_test"], ns["y_test"]) <= 1)
        self.assertTrue(0 <= ns["without_pca"].score(ns["X_test"], ns["y_test"]) <= 1)


if __name__ == "__main__":
    unittest.main()
