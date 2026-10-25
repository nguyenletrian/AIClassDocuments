"""LAB SESSION 10 — CSV-based interactive student grade management.

Run: python SOLUTION.py           # interactive CLI
     python SOLUTION.py --demo    # safe in-memory tests, never writes students.csv
"""
import csv
import os
from pathlib import Path
import sys
import tempfile

CSV_PATH=Path(__file__).resolve().parent/"students.csv"
FIELDS=["student_id","name","class_name","Python","Math","ML"]
SUBJECTS=["Python","Math","ML"]

def validate(student):
    sid=str(student.get("student_id","")).strip()
    name=str(student.get("name","")).strip()
    cls=str(student.get("class_name","")).strip()
    if not sid or not name or not cls: raise ValueError("ID, name and class are required")
    result={"student_id":sid,"name":name,"class_name":cls}
    for sub in SUBJECTS:
        try: score=float(student[sub])
        except (ValueError,KeyError,TypeError) as exc: raise ValueError(f"{sub} grade must be numeric") from exc
        if not 0<=score<=100: raise ValueError(f"{sub} grade outside 0..100")
        result[sub]=score
    return result

def load_students(path=CSV_PATH):
    if not Path(path).exists():
        raise FileNotFoundError(f"Missing data file: {path}")
    with Path(path).open("r",encoding="utf-8",newline="") as f:
        reader=csv.DictReader(f)
        if reader.fieldnames != FIELDS:
            raise ValueError(f"Unexpected columns, expected {FIELDS}")
        rows=[validate(r) for r in reader]
    ids=[r["student_id"] for r in rows]
    if len(ids)!=len(set(ids)): raise ValueError("Duplicate student IDs already in CSV")
    return rows

def add_student(rows, student):
    item=validate(student)
    if any(r["student_id"]==item["student_id"] for r in rows):
        raise ValueError("Duplicate student ID")
    rows.append(item)

def search_by_id(rows, student_id):
    return next((r for r in rows if r["student_id"]==student_id.strip()),None)

def average_grade(student):
    return sum(student[sub] for sub in SUBJECTS)/len(SUBJECTS)

def display(rows):
    for item in rows:
        print(f"{item['student_id']} | {item['name']} | {item['class_name']} | average={average_grade(item):.2f}/100")

def save_students(rows, path=CSV_PATH):
    """Write a temporary CSV first, then atomically replace target if successful."""
    path=Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    tmp=None
    try:
        with tempfile.NamedTemporaryFile(mode="w",encoding="utf-8",newline="",dir=path.parent,
                                         prefix=".students-",suffix=".csv",delete=False) as out:
            tmp=Path(out.name)
            writer=csv.DictWriter(out,fieldnames=FIELDS)
            writer.writeheader()
            for row in rows: writer.writerow(validate(row))
        os.replace(tmp,path)
    finally:
        if tmp is not None and tmp.exists(): tmp.unlink()

def run_demo():
    rows=load_students()
    assert len(rows)==10
    add_student(rows,{"student_id":"S011","name":"Learner 11","class_name":"AI04",
                      "Python":90,"Math":88,"ML":91})
    assert len(rows)==11
    assert abs(average_grade(search_by_id(rows,"S011"))-269/3)<1e-9
    try:
        add_student(rows,{"student_id":"S011","name":"Duplicate","class_name":"AI04",
                          "Python":90,"Math":88,"ML":91})
        raise AssertionError("Duplicate check failed")
    except ValueError: pass
    print("PASS: CSV read, search, add, duplicate detection and average")
    display(rows[:3])
    print("(Demo does not overwrite students.csv)")

def main():
    try: rows=load_students()
    except (OSError,ValueError,csv.Error) as exc:
        print("Cannot open students.csv:",exc)
        return
    dirty=False
    while True:
        print("\n1.Display 2.Add 3.Search ID 4.Averages 5.Save 0.Exit")
        choice=input("Choose: ").strip()
        try:
            if choice=="0":
                if dirty: print("Unsaved changes are discarded. Select 5 to save next time.")
                break
            if choice=="1": display(rows)
            elif choice=="2":
                record={"student_id":input("ID: "),"name":input("Name: "),
                        "class_name":input("Class: ")}
                for subject in SUBJECTS: record[subject]=input(f"{subject} grade [0,100]: ")
                add_student(rows,record)
                dirty=True
                print("Student added (not yet saved).")
            elif choice=="3":
                print(search_by_id(rows,input("Student ID: ")) or "Not found")
            elif choice=="4":
                for row in rows:print(row["student_id"],round(average_grade(row),2))
            elif choice=="5":
                save_students(rows)
                dirty=False
                print("Saved",CSV_PATH)
            else: print("Unknown option")
        except (OSError,ValueError,KeyError) as exc:
            print("Error:",exc)
if __name__=="__main__":
    run_demo() if "--demo" in sys.argv else main()
