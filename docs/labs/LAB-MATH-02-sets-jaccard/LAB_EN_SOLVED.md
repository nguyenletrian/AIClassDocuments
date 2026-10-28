# Lab Math 02 — Sets, Jaccard Similarity and Study Partners

> **English teaching edition.** The source is a worked notebook, not a formal Word assignment. The following English tasks are reconstructed faithfully from its six section headings, data and code. Student names are anonymized. Each task is followed immediately by its solution.

**Prerequisites:** Python 3.10+, sets, dictionaries, loops, functions and `itertools.combinations`. **Run all tasks:** `python SOLUTION_ANNOTATED.py` in this folder.

## Task 1. Analyze Student Interests

**English lab requirement:** Find all distinct subjects in the six-student dictionary. List students taking **Python AND AI** and students taking **Python OR Math**.

**Annotated solution (runnable in this folder):**

```python
from SOLUTION_ANNOTATED import STUDENTS, analyse_interests

# Three results: distinct subjects, both-course filter, either-course filter.
subjects, both, either = analyse_interests(STUDENTS)
print(subjects)
print(both)
print(either)
```

**Explanation:** A set removes duplicate subject names. Intersection-style membership uses `and`; the inclusive filter uses `or`. The full implementation, its function arguments, special cases and intermediate statements are commented in [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 2. Compare Two Students

**English lab requirement:** For two different, valid student names, display common interests, all interests, and subjects only the first student takes. Handle invalid names and identical selections.

**Annotated solution (runnable in this folder):**

```python
from SOLUTION_ANNOTATED import STUDENTS, compare_students

# Student A and B share Python/AI, and A alone studies Math.
print(compare_students(STUDENTS, 'Student A', 'Student B'))
```

**Explanation:** The set operators `&`, `|` and `-` mean intersection, union and directional difference. The full implementation, its function arguments, special cases and intermediate statements are commented in [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 3. Calculate Jaccard Similarity

**English lab requirement:** Calculate Jaccard similarity as shared-subject count divided by the distinct combined-subject count. Avoid division by zero for empty sets.

**Annotated solution (runnable in this folder):**

```python
from SOLUTION_ANNOTATED import STUDENTS, jaccard_similarity

# Both students have exactly the same subjects, so the score is 1.
print(jaccard_similarity(STUDENTS['Student A'], STUDENTS['Student E']))
```

**Explanation:** A score of 0 means no common subjects; 1 means exactly matching interests. The full implementation, its function arguments, special cases and intermediate statements are commented in [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 4. Find the Most Similar Pair

**English lab requirement:** Evaluate each unordered pair once, identify the highest-scoring pair and show its similarity.

**Annotated solution (runnable in this folder):**

```python
from SOLUTION_ANNOTATED import STUDENTS, most_similar_pair

# combinations() excludes pairing one student with themselves.
print(most_similar_pair(STUDENTS))
```

**Explanation:** Ties retain the first matching pair in insertion order; this makes results reproducible. The full implementation, its function arguments, special cases and intermediate statements are commented in [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 5. Recommend Study Partners

**English lab requirement:** For a selected student, recommend different students whose Jaccard similarity is **at least 0.5**; show the score.

**Annotated solution (runnable in this folder):**

```python
from SOLUTION_ANNOTATED import STUDENTS, recommend_partners

# Exclude the chosen student; sort by similarity descending.
print(recommend_partners(STUDENTS, 'Student A', threshold=0.5))
```

**Explanation:** The threshold is inclusive (`>= 0.5`); a student is never paired with themselves. The full implementation, its function arguments, special cases and intermediate statements are commented in [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Task 6. Build a Simple Student Graph

**English lab requirement:** Represent students as nodes and connect two different students whenever their similarity is at least 0.5. Print a symmetric adjacency list, including isolated students.

**Annotated solution (runnable in this folder):**

```python
from SOLUTION_ANNOTATED import STUDENTS, build_graph

# Each edge is stored in both endpoints' neighbor lists.
for name, neighbors in build_graph(STUDENTS).items():
    print(name, '->', neighbors)
```

**Explanation:** Student D remains in the graph even though Java/Web shares no subjects with the other students. The full implementation, its function arguments, special cases and intermediate statements are commented in [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py).

## Source and verification

Source (private teacher repository): `2. Math/labs2.ipynb` at commit `851d67d`. It has six named sections. The solution follows the original set operations, `combinations()`, Jaccard computation, inclusive `0.5` recommendation threshold and undirected graph construction; differences are input validation, deterministic ordering and synthetic identifiers. Use `python SOLUTION_ANNOTATED.py` to run the examples and assertions. Do not mislabel these reconstructed questions as a verbatim Word translation.
