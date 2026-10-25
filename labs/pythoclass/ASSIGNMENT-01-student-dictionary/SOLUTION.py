"""ASSIGNMENT 1 — Dictionary CRUD with validation and score statistics.

Run with --demo for reproducible example (12 synthetic learners).
Run without arguments for an interactive terminal menu.
"""
from collections import Counter
import sys

def validate(student_id, name, score):
    student_id, name = student_id.strip(), name.strip()
    if not student_id or not name:
        raise ValueError("ID and name are required")
    try:
        value = float(score)
    except (TypeError, ValueError) as exc:
        raise ValueError("Score must be numeric") from exc
    if not 0 <= value <= 10:
        raise ValueError("Score must be between 0 and 10")
    return student_id, name, value

def add(students, student_id, name, score):
    student_id, name, score = validate(student_id, name, score)
    if student_id in students:
        raise ValueError("Duplicate student ID")
    students[student_id] = {"name": name, "score": score}

def update(students, student_id, name, score):
    if student_id not in students:
        raise KeyError(student_id)
    _, name, score = validate(student_id, name, score)
    students[student_id] = {"name": name, "score": score}

def delete(students, student_id, confirmed=False):
    if student_id not in students:
        raise KeyError(student_id)
    if not confirmed:
        return False
    del students[student_id]
    return True

def classify(score):
    if score >= 9: return "Excellent"
    if score >= 7: return "Good"
    if score >= 5: return "Average"
    return "Poor"

def sorted_students(students, descending=False):
    return sorted(students.items(), key=lambda pair: pair[1]["score"], reverse=descending)

def statistics(students):
    if not students:
        return None
    grades = [item["score"] for item in students.values()]
    return {
        "highest": max(grades),
        "lowest": min(grades),
        "average": sum(grades) / len(grades),
        "classification_counts": dict(Counter(classify(s) for s in grades)),
    }

def show(students):
    for student_id, data in students.items():
        print(f'{student_id} | {data["name"]} | {data["score"]:g}/10 | {classify(data["score"])}')

def sample():
    students = {}
    scores = [9.5, 8, 7.5, 6, 5.5, 4.5, 7, 9, 8.5, 6.5, 10, 5]
    for i, score in enumerate(scores, 1):
        add(students, f"S{i:03}", f"Learner {i:02}", score)
    return students

def run_demo():
    students = sample()
    assert len(students) == 12
    add(students, "S013", "Learner 13", 8)
    update(students, "S013", "Updated Learner", 8.5)
    assert delete(students, "S013", confirmed=False) is False
    assert delete(students, "S013", confirmed=True) is True
    assert len(students) == 12
    print("Sorted ascending:")
    print(sorted_students(students)[:4])
    print("Statistics:", statistics(students))
    show(students)

def interactive():
    students = sample()
    menu = "\n1.Display 2.Add 3.Update 4.Delete 5.Sort 6.Statistics 0.Exit"
    while True:
        print(menu)
        choice = input("Choose: ").strip()
        try:
            if choice == "0": break
            if choice == "1": show(students)
            elif choice == "2":
                add(students, input("ID: "), input("Name: "), input("Score [0,10]: "))
            elif choice == "3":
                sid = input("ID to update: ").strip()
                update(students, sid, input("New name: "), input("New score: "))
            elif choice == "4":
                sid = input("ID to delete: ").strip()
                if not delete(students, sid, input("Confirm delete [y/N]: ").strip().lower() == "y"):
                    print("Cancelled")
            elif choice == "5":
                desc = input("Descending? [y/N]: ").strip().lower() == "y"
                for sid, data in sorted_students(students, desc): print(sid, data)
            elif choice == "6": print(statistics(students))
            else: print("Unknown option")
        except (ValueError, KeyError) as exc:
            print("Input error:", exc)

if __name__ == "__main__":
    run_demo() if "--demo" in sys.argv else interactive()
