# Lab Session 5 — Student Management with a List (English + solutions)

**English source:** Existing transcription of `Lab Session 5.docx` at `labs/pythoclass/LAB-05-student-list/LAB.md`. The original sample notebook used a list of lists, sometimes mixed text and numeric scores, and left sorting unfinished. This corrected solution keeps a **list** as its primary storage and stores structured dictionaries inside it to avoid index mistakes; identifiers and names are synthetic.

**Run:** `python SOLUTION_ANNOTATED.py --demo`; for the console interface, run `python SOLUTION_ANNOTATED.py`.

## Task 1 — Add a student

**English lab requirement:** Input a student ID, name and numeric score (0–10), validate the fields, and append a record to a **list**. Prevent duplicate IDs.

**Annotated solution:**

```python
from SOLUTION_ANNOTATED import sample, add

# Build twelve synthetic records and append one new student.
students = sample()
add(students, 'S013', 'Learner 13', 7)
print(students[-1])
```

**Explanation:** The list is the primary container. `append()` adds a dictionary record; `any()` rejects an existing ID. See the fully commented function and its parameters in [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 2 — Display the student list

**English lab requirement:** Display every student in the list, including ID, name and score.

**Annotated solution:**

```python
from SOLUTION_ANNOTATED import sample, show

# Traverse all list entries in insertion order.
show(sample())
```

**Explanation:** Loop through the list and access each record's three named fields. See the fully commented function and its parameters in [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 3 — Search by name

**English lab requirement:** Accept a name and display matching students. Search is case-insensitive and supports partial matches.

**Annotated solution:**

```python
from SOLUTION_ANNOTATED import sample, find_by_name, show

# casefold() allows matching learner / Learner identically.
results = find_by_name(sample(), 'learner 03')
show(results)
```

**Explanation:** The list comprehension keeps records whose lowercase-normalized name contains the search text. See the fully commented function and its parameters in [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 4 — Delete by student ID

**English lab requirement:** Input a student ID, find its index in the list and remove that record. Report missing IDs rather than deleting an unrelated record.

**Annotated solution:**

```python
from SOLUTION_ANNOTATED import sample, delete_by_id

# enumerate() provides the index for pop().
students = sample()
removed = delete_by_id(students, 'S003')
print('Removed:', removed)
print('Remaining:', len(students))
```

**Explanation:** `pop(index)` removes only the identified record and returns it. An unknown ID raises `KeyError`. See the fully commented function and its parameters in [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 5 — Sort students by score

**English lab requirement:** Sort students by numeric score in ascending or descending order.

**Annotated solution:**

```python
from SOLUTION_ANNOTATED import sample, sorted_by_score

# key=... selects score, and reverse determines direction.
students = sample()
print([(s['id'], s['score']) for s in sorted_by_score(students)])
print([(s['id'], s['score']) for s in sorted_by_score(students, descending=True)])
```

**Explanation:** Unlike sorting names, `sorted()` compares `float` scores; it returns a separate list and does not overwrite original insertion order. See the fully commented function and its parameters in [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 6 — Score statistics

**English lab requirement:** Find the student with the highest score, the student with the lowest score, and the arithmetic mean of all student scores.

**Annotated solution:**

```python
from SOLUTION_ANNOTATED import sample, statistics

# max/min select whole records; sum/len computes mean.
report = statistics(sample())
print(report)
```

**Explanation:** The function returns None on an empty list to avoid dividing by zero. See the fully commented function and its parameters in [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 7 — Exit the program

**English lab requirement:** Provide a text menu so the user can select actions and leave by choosing Exit.

**Annotated solution:**

```python
from SOLUTION_ANNOTATED import interactive

# Interactive mode loops until the user enters 0.
# Run this code in a terminal; use --demo for unattended tests.
if __name__ == '__main__':
    interactive()
```

**Explanation:** `while True` repeats the menu; choosing 0 breaks the loop. Each input error is caught so the menu remains usable. See the fully commented function and its parameters in [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Validation and source comparison

All seven requests from the Word-derived English transcription appear above, in order. The owner's previous notebook attempted addition, search, removal and high/low scores; it used mixed strings/numbers and did not complete sorting. The solution adds input validation, duplicate detection and stable numeric sorting. No changes were made to the original `DEMO.py` or `SOLUTION.py`.
