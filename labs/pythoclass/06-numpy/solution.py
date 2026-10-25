"""12x3 score matrix: indexing, axis, broadcasting."""
import csv
import numpy as np
from pathlib import Path
DATA=Path(__file__).resolve().parents[1]/"data/students_sample.csv"
def main():
    with DATA.open(encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
    X=np.array([[float(r[k]) for k in ("python_score","math_score","english_score")] for r in rows])
    assert X.shape==(12,3)
    print("Shape:",X.shape,"ndim:",X.ndim,"dtype:",X.dtype)
    print("First student:",X[0],"Python column:",X[:,0])
    print("Subject means:",X.mean(axis=0).round(2))
    print("Student means:",X.mean(axis=1).round(2))
    adjusted=np.minimum(X+np.array([0.5,0.0,0.0]),10.0)
    print("Before/after first row:",X[0],adjusted[0])
    assert adjusted.shape==X.shape
if __name__ == "__main__":
    main()
