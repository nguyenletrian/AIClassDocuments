"""Vector, matrix, PCA on 12 learners x 3 numerical features."""
import csv
from pathlib import Path
import numpy as np
from sklearn.decomposition import PCA
DATA=Path(__file__).resolve().parents[1]/"data/students_sample.csv"
def main():
    with DATA.open(encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
    X=np.array([[float(r[k]) for k in ("python_score","math_score","english_score")] for r in rows])
    assert X.shape==(12,3)
    print("Vector norm:",np.linalg.norm(X[0]).round(3))
    print("Dot product:",(X[0]@X[1]).round(3))
    mean=X.mean(axis=0)
    print("Column means:",mean.round(2),"centered first row:",(X[0]-mean).round(2))
    model=PCA(n_components=2)
    projected=model.fit_transform(X)
    assert projected.shape==(12,2)
    print("Before/after shapes:",X.shape,projected.shape)
    print("Explained variance ratio:",model.explained_variance_ratio_.round(3))
    print("Projected first rows:",projected[:2].round(3))
if __name__ == "__main__":
    main()
