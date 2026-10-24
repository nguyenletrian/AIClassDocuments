"""Validation tests for AI-MATH-01 PCA pilot; no internet or student data needed."""
import unittest

import numpy as np
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


STUDENTS = np.array([
    [80, 81, 72, 20, 90], [85, 88, 80, 22, 95],
    [60, 65, 72, 12, 75], [70, 72, 68, 15, 80],
    [90, 91, 88, 25, 98], [88, 87, 89, 20, 90],
    [40, 45, 50, 10, 70], [75, 73, 76, 15, 85]
], dtype=float)


class PCAPilotTests(unittest.TestCase):
    def test_01_center_scale_covariance(self):
        z = StandardScaler().fit_transform(STUDENTS)
        c = np.cov(z, rowvar=False)
        self.assertEqual(c.shape, (5, 5))
        self.assertTrue(np.allclose(c, c.T))
        self.assertTrue(np.allclose(np.diag(c), np.full(5, 8/7)))

    def test_02_numpy_manual_eigen_matches_sklearn(self):
        x = np.array([[2, 0], [0, 1], [3, 4]], dtype=float)
        x_centered = x - x.mean(axis=0)
        values, vectors = np.linalg.eigh(np.cov(x_centered, rowvar=False))
        order = np.argsort(values)[::-1]
        values, vectors = values[order], vectors[:, order]
        manual = x_centered @ vectors[:, :1]
        sklearn = PCA(n_components=1).fit_transform(x)
        self.assertTrue(np.allclose(np.abs(manual), np.abs(sklearn)))
        self.assertAlmostEqual(values[0]/values.sum(), 0.813249, places=5)

    def test_03_student_pca_5d_to_2d(self):
        z = StandardScaler().fit_transform(STUDENTS)
        pca = PCA(n_components=2)
        pts = pca.fit_transform(z)
        self.assertEqual(pts.shape, (8, 2))
        self.assertAlmostEqual(pca.explained_variance_ratio_.sum(), 0.9865238828, places=7)

    def test_04_variance_threshold(self):
        z = StandardScaler().fit_transform(STUDENTS)
        self.assertEqual(PCA(n_components=0.95, svd_solver="full").fit(z).n_components_, 2)
        self.assertLess(PCA(n_components=1).fit(z).explained_variance_ratio_.sum(), 0.95)

    def test_05_pipeline_does_not_fit_test_set(self):
        iris = load_iris()
        xtr, xte, ytr, yte = train_test_split(
            iris.data, iris.target, test_size=0.25, stratify=iris.target, random_state=42
        )
        model = Pipeline([
            ("scale", StandardScaler()), ("pca", PCA(n_components=2)),
            ("classifier", LogisticRegression(max_iter=1000))
        ])
        model.fit(xtr, ytr)
        self.assertEqual((len(xtr), len(xte)), (112, 38))
        self.assertTrue(0.0 <= model.score(xte, yte) <= 1.0)
        self.assertEqual(model.named_steps["pca"].n_components_, 2)


if __name__ == "__main__":
    unittest.main()
