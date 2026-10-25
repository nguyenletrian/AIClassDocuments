"""12 student records: variables, types, averages (synthetic data)."""
import csv
from pathlib import Path
DATA = Path(__file__).resolve().parents[1] / "data/students_sample.csv"
def main():
    with DATA.open(encoding="utf-8", newline="") as f:
        students = list(csv.DictReader(f))
    assert len(students) == 12
    for item in students:
        scores = [float(item[k]) for k in ("python_score", "math_score", "english_score")]
        if not all(0 <= s <= 10 for s in scores):
            raise ValueError("Invalid score")
        average = sum(scores) / len(scores)
        label = "Dat" if average >= 8 else "Can ren luyen"
        print(f"{item['student_id']} | {item['age']} tuoi | TB={average:.2f} | {label}")
if __name__ == "__main__":
    main()
