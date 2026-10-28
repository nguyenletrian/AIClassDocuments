# Assignment 01 — Student Dictionary Management (English)

**Source:** `Ass 1.docx` → existing verified `labs/pythoclass/ASSIGNMENT-01-student-dictionary/LAB.md`. This assignment is already presented in English in the repository; the requirements below retain its meaning while adding a complete, fully commented solution immediately below **each** task. The data and names used in the solution are synthetic.

**Run the full solution:** `python SOLUTION_ANNOTATED.py --demo` (non-interactive) or `python SOLUTION_ANNOTATED.py` (menu).

## Task 1 — Data Structure

**English lab requirement:** Store students in a dictionary. Every entry contains an ID, a name and a score.

**Annotated solution:**

```python
from SOLUTION_ANNOTATED import sample_students

# The outer dictionary key is the unique student ID.
students = sample_students()
print(students['S001'])
```

**Explanation:** Each record is a nested dictionary containing `name` and numeric `score`. The implementation and inputs are further explained inside [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 2 — Create — Add a Student

**English lab requirement:** Prompt for ID, name and score; create a new record only if the ID does not already exist.

**Annotated solution:**

```python
from SOLUTION_ANNOTATED import add

# add() also validates score range and mandatory fields.
add(students, 'S013', 'New Learner', 8.0)
```

**Explanation:** An existing ID raises `ValueError`, so data is never silently overwritten. The implementation and inputs are further explained inside [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 3 — Read — Display All Students

**English lab requirement:** Print every stored student, including their score and academic category.

**Annotated solution:**

```python
from SOLUTION_ANNOTATED import display

# Print nested dictionary values in a readable table-like format.
display(students)
```

**Explanation:** The program displays a clear message when no record exists. The implementation and inputs are further explained inside [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 4 — Update a Student

**English lab requirement:** Locate an existing student by ID and change name/score while validating the new values.

**Annotated solution:**

```python
from SOLUTION_ANNOTATED import update

# Update uses the ID as a stable dictionary key.
update(students, 'S013', 'Updated Learner', 8.5)
```

**Explanation:** Unknown IDs raise `KeyError` rather than creating accidental new entries. The implementation and inputs are further explained inside [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 5 — Delete a Student

**English lab requirement:** Find the student by ID, request confirmation, and delete only after the user confirms.

**Annotated solution:**

```python
from SOLUTION_ANNOTATED import delete

# False preserves the record; True removes it.
assert delete(students, 'S013', confirmed=False) is False
assert delete(students, 'S013', confirmed=True) is True
```

**Explanation:** The confirmation flag protects against accidental deletion. The implementation and inputs are further explained inside [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 6 — Validate Data

**English lab requirement:** Reject missing ID/name, non-numeric score and any score outside the range 0–10.

**Annotated solution:**

```python
from SOLUTION_ANNOTATED import validate

# Conversion from text to float happens inside validate().
print(validate('S014', 'Learner 14', '9.5'))
```

**Explanation:** Use `float()` and explicit range checks; user input is initially a string. The implementation and inputs are further explained inside [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 7 — Check Duplicate IDs

**English lab requirement:** Do not add a second student whose ID is already used.

**Annotated solution:**

```python
from SOLUTION_ANNOTATED import add

# A dictionary cannot contain two distinct values for the same key.
try:
    add(students, 'S001', 'Duplicate', 7)
except ValueError as error:
    print(error)
```

**Explanation:** Check for an existing key before the assignment statement. The implementation and inputs are further explained inside [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 8 — Sort Students by Score

**English lab requirement:** Sort student records in ascending or descending score order.

**Annotated solution:**

```python
from SOLUTION_ANNOTATED import sort_by_score

# reverse=True inside sorted() reverses numeric ranking.
print(sort_by_score(students, descending=True)[:3])
```

**Explanation:** Sorting returns a new list of key/value pairs; the original dictionary stays intact. The implementation and inputs are further explained inside [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 9 — Advanced Statistics

**English lab requirement:** Show highest score, lowest score, average score and the number of students in each performance category.

**Annotated solution:**

```python
from SOLUTION_ANNOTATED import statistics

# Counter() inside statistics() groups equal class labels.
print(statistics(students))
```

**Explanation:** The function returns `None` on an empty collection to avoid division by zero. The implementation and inputs are further explained inside [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 10 — Academic Classification

**English lab requirement:** Classify scores as Excellent (9–10), Good (7–<9), Average (5–<7) or Poor (<5).

**Annotated solution:**

```python
from SOLUTION_ANNOTATED import classify

# Highest threshold must be checked first.
print(classify(9.5))
print(classify(6.5))
```

**Explanation:** The order of conditional branches guarantees exactly one category. The implementation and inputs are further explained inside [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Sample data and correctness

The `--demo` option generates 12 synthetic students, adds a 13th, updates the record, verifies that cancelled deletion keeps the record, deletes after confirmation, and prints sorted results and statistics. `SOLUTION_ANNOTATED.py` implements all ten requirements in one reusable program. Validation and duplicate-ID errors are demonstrated without requiring real personal information.

**Source-code lineage:** This edition derives from the user's existing `labs/pythoclass/ASSIGNMENT-01-student-dictionary/SOLUTION.py`, based on their earlier dictionary/CRUD examples. The original `DEMO.py`, `LAB.md` and `SOLUTION.py` have not been modified.
