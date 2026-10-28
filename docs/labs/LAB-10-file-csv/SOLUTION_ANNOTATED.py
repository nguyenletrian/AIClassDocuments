"""Fully annotated English solution for LAB-10-file-csv.
Source methods and executable statements are preserved from the reviewed
labs/pythoclass reference implementation; explanatory comments are added.
"""

"""LAB SESSION 10 — CSV-based interactive student grade management.

Run: python SOLUTION.py           # interactive CLI
     python SOLUTION.py --demo    # safe in-memory tests, never writes students.csv
"""
# The csv standard-library module handles quoted fields and header names correctly.
import csv
# Use os.replace() for an atomic replacement after writing a temporary file.
import os
# Path constructs filesystem paths portably and makes adjacent data files discoverable.
from pathlib import Path
# Use sys.argv to choose an unattended demo instead of interactive prompts.
import sys
# Use tempfile to avoid corrupting an existing CSV if a write fails.
import tempfile

# Prepare this intermediate value for the next calculation or validation.
CSV_PATH=Path(__file__).resolve().parent/"students.csv"
# Prepare this intermediate value for the next calculation or validation.
FIELDS=["student_id","name","class_name","Python","Math","ML"]
# Prepare this intermediate value for the next calculation or validation.
SUBJECTS=["Python","Math","ML"]

# Function: Check all required CSV fields and convert three subject grades to numbers in the 0–100 range.
def validate(student):
    # Prepare this intermediate value for the next calculation or validation.
    sid=str(student.get("student_id","")).strip()
    # Prepare this intermediate value for the next calculation or validation.
    name=str(student.get("name","")).strip()
    # Prepare this intermediate value for the next calculation or validation.
    cls=str(student.get("class_name","")).strip()
    # Reject out-of-range or missing inputs early instead of silently accepting them.
    if not sid or not name or not cls: raise ValueError("ID, name and class are required")
    # Prepare this intermediate value for the next calculation or validation.
    result={"student_id":sid,"name":name,"class_name":cls}
    # Process each element of the input collection in order.
    for sub in SUBJECTS:
        # Catch expected user/file errors without terminating the whole interactive workflow.
        try: score=float(student[sub])
        # Handle expected exceptions while preserving diagnostics.
        except (ValueError,KeyError,TypeError) as exc: raise ValueError(f"{sub} grade must be numeric") from exc
        # Reject out-of-range or missing inputs early instead of silently accepting them.
        if not 0<=score<=100: raise ValueError(f"{sub} grade outside 0..100")
        result[sub]=score
    # Return the result for later reuse or testing instead of only printing it.
    return result

# Function: Read rows using csv.DictReader; check exact columns and unique student IDs.
def load_students(path=CSV_PATH):
    # Branch when this validated condition is true.
    if not Path(path).exists():
        raise FileNotFoundError(f"Missing data file: {path}")
    # Open the file using a context manager so it closes after reading/writing.
    with Path(path).open("r",encoding="utf-8",newline="") as f:
        # Map each row to column-name keys instead of fragile positional indexing.
        reader=csv.DictReader(f)
        # Branch when this validated condition is true.
        if reader.fieldnames != FIELDS:
            raise ValueError(f"Unexpected columns, expected {FIELDS}")
        # Prepare this intermediate value for the next calculation or validation.
        rows=[validate(r) for r in reader]
    # Prepare this intermediate value for the next calculation or validation.
    ids=[r["student_id"] for r in rows]
    # Reject out-of-range or missing inputs early instead of silently accepting them.
    if len(ids)!=len(set(ids)): raise ValueError("Duplicate student IDs already in CSV")
    # Return the result for later reuse or testing instead of only printing it.
    return rows

# Function: Append one validated record, only after rejecting a duplicate student ID.
def add_student(rows, student):
    # Prepare this intermediate value for the next calculation or validation.
    item=validate(student)
    # Branch when this validated condition is true.
    if any(r["student_id"]==item["student_id"] for r in rows):
        raise ValueError("Duplicate student ID")
    # Add the new element to a list while retaining insertion order.
    rows.append(item)

# Function: Return the matching student record or None using an ID comparison.
def search_by_id(rows, student_id):
    # Return the result for later reuse or testing instead of only printing it.
    return next((r for r in rows if r["student_id"]==student_id.strip()),None)

# Function: Compute the average of Python, Math and ML scores for one student.
def average_grade(student):
    # Return the result for later reuse or testing instead of only printing it.
    return sum(student[sub] for sub in SUBJECTS)/len(SUBJECTS)

# Function: Print identity and averaged score for every student record.
def display(rows):
    # Process each element of the input collection in order.
    for item in rows:
        # Show a human-readable result to the learner.
        print(f"{item['student_id']} | {item['name']} | {item['class_name']} | average={average_grade(item):.2f}/100")

# Function: Write a well-formed temporary CSV then atomically replace the destination.
def save_students(rows, path=CSV_PATH):
    """Write a temporary CSV first, then atomically replace target if successful."""
    # Prepare this intermediate value for the next calculation or validation.
    path=Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    # Prepare this intermediate value for the next calculation or validation.
    tmp=None
    # Catch expected user/file errors without terminating the whole interactive workflow.
    try:
        with tempfile.NamedTemporaryFile(mode="w",encoding="utf-8",newline="",dir=path.parent,
                                         # Prepare this intermediate value for the next calculation or validation.
                                         prefix=".students-",suffix=".csv",delete=False) as out:
            # Prepare this intermediate value for the next calculation or validation.
            tmp=Path(out.name)
            # Write rows using explicit column names, retaining stable CSV order.
            writer=csv.DictWriter(out,fieldnames=FIELDS)
            # Write the CSV header once before writing student records.
            writer.writeheader()
            # Process each element of the input collection in order.
            for row in rows: writer.writerow(validate(row))
        # Replace the destination only after all temporary rows were written.
        os.replace(tmp,path)
    # Clean up temporary resources whether execution succeeds or fails.
    finally:
        # Branch when this validated condition is true.
        if tmp is not None and tmp.exists(): tmp.unlink()

# Function: Run an in-memory ten-row example without modifying source students.csv.
def run_demo():
    # Prepare this intermediate value for the next calculation or validation.
    rows=load_students()
    # Verify the expected outcome and fail the demo if a regression occurs.
    assert len(rows)==10
    add_student(rows,{"student_id":"S011","name":"Learner 11","class_name":"AI04",
                      "Python":90,"Math":88,"ML":91})
    # Verify the expected outcome and fail the demo if a regression occurs.
    assert len(rows)==11
    # Verify the expected outcome and fail the demo if a regression occurs.
    assert abs(average_grade(search_by_id(rows,"S011"))-269/3)<1e-9
    # Catch expected user/file errors without terminating the whole interactive workflow.
    try:
        add_student(rows,{"student_id":"S011","name":"Duplicate","class_name":"AI04",
                          "Python":90,"Math":88,"ML":91})
        raise AssertionError("Duplicate check failed")
    # Handle expected exceptions while preserving diagnostics.
    except ValueError: pass
    # Show a human-readable result to the learner.
    print("PASS: CSV read, search, add, duplicate detection and average")
    display(rows[:3])
    # Show a human-readable result to the learner.
    print("(Demo does not overwrite students.csv)")

# Function: Run the six-option menu; retain changes in memory until Save is explicitly selected.
def main():
    # Catch expected user/file errors without terminating the whole interactive workflow.
    try: rows=load_students()
    # Handle expected exceptions while preserving diagnostics.
    except (OSError,ValueError,csv.Error) as exc:
        # Show a human-readable result to the learner.
        print("Cannot open students.csv:",exc)
        return
    # Prepare this intermediate value for the next calculation or validation.
    dirty=False
    # Repeat this operation until the stopping condition becomes false.
    while True:
        # Show a human-readable result to the learner.
        print("\n1.Display 2.Add 3.Search ID 4.Averages 5.Save 0.Exit")
        # Prepare this intermediate value for the next calculation or validation.
        choice=input("Choose: ").strip()
        # Catch expected user/file errors without terminating the whole interactive workflow.
        try:
            # Branch when this validated condition is true.
            if choice=="0":
                # Branch when this validated condition is true.
                if dirty: print("Unsaved changes are discarded. Select 5 to save next time.")
                # Exit the active loop after meeting the termination condition.
                break
            # Branch when this validated condition is true.
            if choice=="1": display(rows)
            # Handle an alternative choice only when earlier tests did not match.
            elif choice=="2":
                # Prepare this intermediate value for the next calculation or validation.
                record={"student_id":input("ID: "),"name":input("Name: "),
                        "class_name":input("Class: ")}
                # Process each element of the input collection in order.
                for subject in SUBJECTS: record[subject]=input(f"{subject} grade [0,100]: ")
                add_student(rows,record)
                # Prepare this intermediate value for the next calculation or validation.
                dirty=True
                # Show a human-readable result to the learner.
                print("Student added (not yet saved).")
            # Handle an alternative choice only when earlier tests did not match.
            elif choice=="3":
                # Show a human-readable result to the learner.
                print(search_by_id(rows,input("Student ID: ")) or "Not found")
            # Handle an alternative choice only when earlier tests did not match.
            elif choice=="4":
                # Process each element of the input collection in order.
                for row in rows:print(row["student_id"],round(average_grade(row),2))
            # Handle an alternative choice only when earlier tests did not match.
            elif choice=="5":
                save_students(rows)
                # Prepare this intermediate value for the next calculation or validation.
                dirty=False
                # Show a human-readable result to the learner.
                print("Saved",CSV_PATH)
            # Run the fallback branch when no earlier condition applies.
            else: print("Unknown option")
        # Handle expected exceptions while preserving diagnostics.
        except (OSError,ValueError,KeyError) as exc:
            # Show a human-readable result to the learner.
            print("Error:",exc)
if __name__=="__main__":
    run_demo() if "--demo" in sys.argv else main()
