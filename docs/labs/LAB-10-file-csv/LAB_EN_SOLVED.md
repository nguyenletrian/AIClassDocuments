# Lab Session 10 — CSV Student Grade Management (English + annotated answers)

**Source:** English transcription of `Lab Session 10.docx` at `labs/pythoclass/LAB-10-file-csv/LAB.md` and the owner's File I/O demo scripts. The brief includes six menu features and explicit error-handling requirements, all retained here. Synthetic learner names protect private identities.

**Run:** `python SOLUTION_ANNOTATED.py --demo` (non-interactive; never overwrites the example data), or `python SOLUTION_ANNOTATED.py` to use the menu.

**Example CSV columns and data:** `student_id,name,class_name,Python,Math,ML`; a 10-record [students.csv](students.csv) is included in this folder. Grades are interpreted on a 0–100 scale.

## Task 1 — Display All Students

**English lab requirement:** Load the supplied `students.csv` with the columns student_id, name, class_name, Python, Math, ML; display the learner records.

**Annotated solution:**

```python
from SOLUTION_ANNOTATED import load_students, display

# csv.DictReader reads columns by their header names.
rows = load_students()
display(rows)
```

**Explanation:** `Path(__file__).resolve().parent` locates the sample beside the script. Each row is validated before display. The full function implementation, all parameters and file error cases are documented in [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 2 — Add a New Student

**English lab requirement:** Input an ID, name, class and three numeric subject grades (Python, Math, ML). Reject empty fields, scores outside 0–100 and duplicate IDs.

**Annotated solution:**

```python
from SOLUTION_ANNOTATED import load_students, add_student

# Add only to in-memory rows; do not overwrite the sample CSV.
rows = load_students()
add_student(rows, {'student_id': 'S011', 'name': 'Learner 11',
                   'class_name': 'AI04', 'Python': 90,
                   'Math': 88, 'ML': 91})
print('After add:', len(rows))
```

**Explanation:** `float()` converts each grade from input text, and `any()` checks existing student IDs before appending. The full function implementation, all parameters and file error cases are documented in [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 3 — Search Student by ID

**English lab requirement:** Input a student ID, search existing records, and display the matching student or a not-found message.

**Annotated solution:**

```python
from SOLUTION_ANNOTATED import load_students, search_by_id

# The ID is stripped before matching to prevent accidental spaces.
rows = load_students()
print(search_by_id(rows, 'S003'))
print(search_by_id(rows, 'S999'))  # None: record not found.
```

**Explanation:** `next(iterator, None)` returns the first match or None without raising StopIteration. The full function implementation, all parameters and file error cases are documented in [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 4 — Calculate Average Grade

**English lab requirement:** Calculate and display the average of each student's Python, Math and ML grades.

**Annotated solution:**

```python
from SOLUTION_ANNOTATED import load_students, average_grade

# Every subject contributes equally to the arithmetic mean.
for record in load_students():
    print(record['student_id'], round(average_grade(record), 2))
```

**Explanation:** Sum the three validated numeric fields and divide by the number of subjects (3), not by student count. The full function implementation, all parameters and file error cases are documented in [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 5 — Save Students to File

**English lab requirement:** Save all current students to a CSV file with the original six columns, preserving data integrity on write failures.

**Annotated solution:**

```python
from tempfile import TemporaryDirectory
from pathlib import Path
from SOLUTION_ANNOTATED import load_students, save_students

# Use a temporary directory so the distributed sample CSV is not modified.
with TemporaryDirectory() as folder:
    destination = Path(folder) / 'students.csv'
    save_students(load_students(), destination)
    print(destination.exists())
```

**Explanation:** `csv.DictWriter` preserves column names. Save writes to a temporary file first, then replaces the destination atomically. The full function implementation, all parameters and file error cases are documented in [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 6 — Exit the Menu

**English lab requirement:** Display a menu for tasks 1–5 and allow exiting without unintended file writes.

**Annotated solution:**

```python
from SOLUTION_ANNOTATED import main

# Interactive menu exits when 0 is selected. Save is a separate action.
# Run this in a terminal; use --demo for automatic tests.
if __name__ == '__main__':
    main()
```

**Explanation:** The `dirty` flag warns about unsaved changes; exiting does not silently write the original students.csv. The full function implementation, all parameters and file error cases are documented in [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Error handling — applies to every relevant task

- **Missing file:** `load_students()` raises `FileNotFoundError`; the interactive menu catches and explains the error.
- **Non-numeric grade / missing column:** `validate()` raises a clear `ValueError` instead of silently accepting the data.
- **Out-of-range grade:** reject scores below 0 or above 100.
- **Duplicate ID:** reject IDs already present in CSV or current in-memory rows.
- **Malformed header:** require the exact six column names listed above.
- **File integrity:** write to a temporary file in the destination directory, then call `os.replace()`; the demo reads but never saves to the original example CSV.

The source notebook's product-management CSV demo is consulted for file and menu mechanics; the Word lab specifically requires **student grades**, so these solutions use student records rather than changing the assignment to products.
