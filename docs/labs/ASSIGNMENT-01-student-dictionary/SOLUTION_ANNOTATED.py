"""Assignment 01 — Student dictionary manager, explained step by step.

Reference: labs/pythoclass/ASSIGNMENT-01-student-dictionary/SOLUTION.py
Run the deterministic example: python SOLUTION_ANNOTATED.py --demo
Run the text menu: python SOLUTION_ANNOTATED.py
"""
from collections import Counter  # Count learners in each performance category.
import sys  # Read command-line arguments without a third-party library.


def validate(student_id, name, score):
    """Accept ID, student name and score; reject malformed records."""
    # .strip() removes accidental leading or trailing spaces from text input.
    student_id = student_id.strip()
    name = name.strip()
    if not student_id or not name:  # Empty ID/name is not allowed.
        raise ValueError("Student ID and name are required.")
    try:
        score = float(score)  # Input from input() is text; convert to a number.
    except (ValueError, TypeError) as error:
        raise ValueError("Score must be numeric.") from error
    if not 0 <= score <= 10:  # Require points within the 0–10 grading scale.
        raise ValueError("Score must be between 0 and 10.")
    return student_id, name, score


def add(students, student_id, name, score):
    """Create a dictionary entry while preventing duplicate IDs."""
    student_id, name, score = validate(student_id, name, score)
    if student_id in students:  # Dictionary keys are unique identifiers.
        raise ValueError(f"Duplicate student ID: {student_id}")
    # Nested dictionary gives named fields instead of brittle list offsets.
    students[student_id] = {"name": name, "score": score}


def display(students):
    """Read: list all records including score and academic category."""
    if not students:
        print("No students stored.")  # Handle an empty dataset gracefully.
    for student_id, record in students.items():  # Traverse key/value pairs.
        print(f"{student_id} | {record['name']} | "
              f"{record['score']:g}/10 | {classify(record['score'])}")


def update(students, student_id, new_name, new_score):
    """Update a student by ID without silently creating new records."""
    if student_id not in students:
        raise KeyError(f"Unknown student ID: {student_id}")
    _, name, score = validate(student_id, new_name, new_score)
    students[student_id] = {"name": name, "score": score}


def delete(students, student_id, confirmed=False):
    """Delete only if the key exists and the user confirms the operation."""
    if student_id not in students:
        raise KeyError(f"Unknown student ID: {student_id}")
    if not confirmed:
        return False  # Cancellation must leave dictionary untouched.
    del students[student_id]  # Remove exactly the selected dictionary key.
    return True


def classify(score):
    """Map scores to four documented, mutually exclusive categories."""
    if score >= 9:
        return "Excellent"
    if score >= 7:
        return "Good"
    if score >= 5:
        return "Average"
    return "Poor"


def sort_by_score(students, descending=False):
    """Return a sorted view without modifying the source dictionary."""
    # Each 'pair' contains the dictionary key and its nested student record.
    return sorted(
        students.items(),
        key=lambda pair: pair[1]["score"],  # Compare numeric score fields.
        reverse=descending,  # True sorts from high score to low score.
    )


def statistics(students):
    """Summarize scores and classification counts; handle zero students."""
    if not students:
        return None
    scores = [item["score"] for item in students.values()]
    counts = Counter(classify(score) for score in scores)
    return {
        "highest": max(scores),
        "lowest": min(scores),
        "average": sum(scores) / len(scores),  # No /0: empty case handled.
        "classification_counts": dict(counts),
    }


def sample_students():
    """Generate synthetic demo names rather than real student identities."""
    scores = [9.5, 8, 7.5, 6, 5.5, 4.5, 7, 9, 8.5, 6.5, 10, 5]
    students = {}
    for number, score in enumerate(scores, start=1):
        add(students, f"S{number:03d}", f"Learner {number:02d}", score)
    return students


def run_demo():
    """Exercise create, update, cancel/delete, sort and numeric statistics."""
    students = sample_students()
    assert len(students) == 12  # Base fixture contains twelve test records.
    add(students, "S013", "New Learner", 8)
    update(students, "S013", "Updated Learner", 8.5)
    assert delete(students, "S013", confirmed=False) is False
    assert "S013" in students  # Cancelled deletion did not change the record.
    assert delete(students, "S013", confirmed=True) is True
    assert "S013" not in students
    assert len(students) == 12

    print("Ascending scores (first 4):", sort_by_score(students)[:4])
    print("Descending scores (first 4):",
          sort_by_score(students, descending=True)[:4])
    print("Statistics:", statistics(students))
    print("Student list:")
    display(students)


def interactive_menu():
    """Keep the terminal menu running until the user explicitly exits."""
    students = sample_students()
    menu = "\n1.Display 2.Add 3.Update 4.Delete 5.Sort 6.Statistics 0.Exit"
    while True:
        print(menu)
        action = input("Choose: ").strip()
        try:  # Catch user errors; do not terminate the whole menu.
            if action == "0":
                break
            elif action == "1":
                display(students)
            elif action == "2":
                add(students, input("ID: "), input("Name: "),
                    input("Score [0,10]: "))
            elif action == "3":
                key = input("ID to update: ").strip()
                update(students, key, input("New name: "), input("New score: "))
            elif action == "4":
                key = input("ID to delete: ").strip()
                answer = input("Confirm deletion? [y/N]: ").strip().lower()
                if not delete(students, key, confirmed=(answer == "y")):
                    print("Deletion cancelled.")
            elif action == "5":
                descending = input("Descending? [y/N]: ").strip().lower() == "y"
                for key, item in sort_by_score(students, descending):
                    print(key, item)
            elif action == "6":
                print(statistics(students))
            else:
                print("Unknown menu option.")
        except (ValueError, KeyError) as error:
            print("Input error:", error)


if __name__ == "__main__":
    # '--demo' avoids interactive input in automated tests or tutorials.
    if "--demo" in sys.argv:
        run_demo()
    else:
        interactive_menu()
