"""Lab Math 02 — set operations, Jaccard similarity and student graphs.

Reconstructed and improved from PythoClass/2. Math/labs2.ipynb.
Run: python SOLUTION_ANNOTATED.py
All example names are synthetic; no user input is required.
"""
from itertools import combinations  # Generate unordered pairs without repetition.

# Map each synthetic student to a SET of subjects: duplicates are impossible.
# The subject choices reproduce the patterns in the owner's six-row demo.
STUDENTS = {
    "Student A": {"Python", "AI", "Math"},
    "Student B": {"Python", "AI", "SQL"},
    "Student C": {"Python", "SQL"},
    "Student D": {"Java", "Web"},
    "Student E": {"Python", "AI", "Math"},
    "Student F": {"AI", "Math", "Python"},
}


def analyse_interests(students):
    """Task 1: compute unique subjects and the two requested filters."""
    # set().union(*iterable) joins every subject set into one unique collection.
    all_subjects = set().union(*students.values())
    # 'and' keeps people who study BOTH Python and AI.
    python_and_ai = [name for name, subjects in students.items()
                     if "Python" in subjects and "AI" in subjects]
    # 'or' keeps people who study AT LEAST ONE of Python and Math.
    python_or_math = [name for name, subjects in students.items()
                      if "Python" in subjects or "Math" in subjects]
    # Sorting gives reproducible output even though sets have no fixed order.
    return sorted(all_subjects), python_and_ai, python_or_math


def compare_students(students, first, second):
    """Task 2: inspect intersection, union and directional difference."""
    # Reject unknown identifiers before attempting dictionary indexing.
    if first not in students or second not in students:
        raise ValueError("Both student names must exist.")
    if first == second:
        raise ValueError("Choose two distinct students.")
    left, right = students[first], students[second]
    return {
        "shared": sorted(left & right),  # Subjects common to BOTH students.
        "combined": sorted(left | right),  # Subjects studied by EITHER student.
        "only_first": sorted(left - right),  # Subjects absent from second.
    }


def jaccard_similarity(left, right):
    """Task 3: fraction of unique shared subjects among unique subjects."""
    both = left & right  # Set intersection.
    either = left | right  # Set union.
    # Two empty sets have no shared subjects here; choose 0 rather than /0.
    return len(both) / len(either) if either else 0.0


def most_similar_pair(students):
    """Task 4: compare all unordered pairs, preserving first winning tie."""
    best_pair = None
    best_score = -1.0  # Lower than every legal Jaccard value [0, 1].
    for first, second in combinations(students, 2):
        score = jaccard_similarity(students[first], students[second])
        if score > best_score:
            best_pair, best_score = (first, second), score
    return best_pair, best_score


def recommend_partners(students, student, threshold=0.5):
    """Task 5: return everyone other than student with similarity >= limit."""
    if student not in students:
        raise ValueError("Unknown student.")
    if not 0.0 <= threshold <= 1.0:
        raise ValueError("Threshold must be between 0 and 1.")
    matches = []
    for other, subjects in students.items():
        if other == student:  # Never recommend a student to themselves.
            continue
        score = jaccard_similarity(students[student], subjects)
        if score >= threshold:  # Inclusive as in the original notebook.
            matches.append((other, score))
    # Rank by similarity, then alphabetically when scores are identical.
    return sorted(matches, key=lambda item: (-item[1], item[0]))


def build_graph(students, threshold=0.5):
    """Task 6: symmetric adjacency list; isolated vertices remain visible."""
    if not 0.0 <= threshold <= 1.0:
        raise ValueError("Threshold must be between 0 and 1.")
    graph = {name: [] for name in students}  # Every student becomes a node.
    for first, second in combinations(students, 2):
        score = jaccard_similarity(students[first], students[second])
        if score >= threshold:
            graph[first].append(second)  # Undirected edge in both directions.
            graph[second].append(first)
    return {name: sorted(neighbors) for name, neighbors in graph.items()}


def main():
    """Show each result and assert easy-to-check reference expectations."""
    subjects, both, either = analyse_interests(STUDENTS)
    print("Task 1 - All subjects:", ", ".join(subjects))
    print("Python AND AI:", ", ".join(both))
    print("Python OR Math:", ", ".join(either))

    compared = compare_students(STUDENTS, "Student A", "Student B")
    print("Task 2 - Common:", compared["shared"])
    print("Union:", compared["combined"])
    print("Only Student A:", compared["only_first"])

    score = jaccard_similarity(STUDENTS["Student A"], STUDENTS["Student E"])
    print("Task 3 - Jaccard(A, E):", f"{score:.2f}")
    assert score == 1.0  # These two students have identical interest sets.

    pair, highest = most_similar_pair(STUDENTS)
    print("Task 4 - Best pair:", pair, "score", f"{highest:.2f}")
    assert highest == 1.0  # Duplicate interest sets give perfect similarity.

    matches = recommend_partners(STUDENTS, "Student A", threshold=0.5)
    print("Task 5 - Partners:", matches)
    assert all(s >= 0.5 for _, s in matches)

    graph = build_graph(STUDENTS, threshold=0.5)
    print("Task 6 - Student graph:")
    for name, neighbors in graph.items():
        print(f"  {name}: {', '.join(neighbors) if neighbors else 'No connections'}")
    assert graph["Student D"] == []  # Java/Web shares none of these subjects.


if __name__ == "__main__":
    main()  # Do not run the sample automatically when imported.
