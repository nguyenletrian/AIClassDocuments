"""End-to-end syntax, structure and five practical PCA scenarios from the lesson."""
import ast
import contextlib
import io
import os
import re
import unittest
from pathlib import Path
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
                         "## 5. Năm tình huống", "## 7. English multiple-choice"):
            self.assertIn(expected, self.text)
        self.assertEqual(len(re.findall(r"^### Tình huống [1-5]", self.text, re.M)), 5)
        self.assertEqual(len(re.findall(r"^\*\*Q\d+\.", self.text, re.M)), 20)
        for forbidden in ("PythoClass", "PythonClass", "Toán học đằng sau", "Sau bài học"):
            self.assertNotIn(forbidden, self.text)
        self.assertEqual(len(self.blocks), 11)
        # Each of the five cases must justify its choice, not only give steps.
        self.assertEqual(self.text.count("**Vì sao chọn cách này?**"), 5)
        self.assertEqual(len(re.findall(r"^\| Q\d+ \|", self.text, re.M)), 20)
        self.assertNotIn("Subconcept", self.text)
        # Feature/Vector/Matrix are defined in prose before the first code sample.
        concepts = self.text.split("### 4.2.", 1)[1].split("### 4.3.", 1)[0]
        for concept in ("**Feature là gì?**", "**Vector là gì?**", "**Matrix là gì?**"):
            self.assertIn(concept, concepts)
        self.assertLess(concepts.index("**Feature là gì?**"), concepts.index("```python"))
        self.assertLess(concepts.index("**Vector là gì?**"), concepts.index("```python"))


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
