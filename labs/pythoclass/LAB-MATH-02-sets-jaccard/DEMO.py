# Teacher notebook code cells copied into one Python file for reference only.
# Some cells prompt for user input or depend on earlier cells; this is not
# the polished solution. Use SOLUTION.py or docs/labs/<folder> instead.
# Source at 2026-10-27 snapshot: 2. Math/labs2.ipynb

from itertools import combinations

# ----- Next notebook cell -----

# DATASET
students = {
    "An": {"Python", "AI", "Math"},
    "Binh": {"Python", "AI", "SQL"},
    "Chi": {"Python", "SQL"},
    "Dung": {"Java", "Web"},
    "Lan": {"Python", "AI", "Math"},
    "Hoa": {"AI", "Math", "Python"}
}

# ----- Next notebook cell -----

# Find all unique subjects
all_subjects = set()

for interests in students.values():
    all_subjects = all_subjects | interests

print("All subjects:")
print(all_subjects)

# ----- Next notebook cell -----

# Students interested in Python AND AI
python_and_ai = []

for name, interests in students.items():

    if "Python" in interests and "AI" in interests:
        python_and_ai.append(name)

print("Students interested in Python AND AI:")
print(python_and_ai)

# ----- Next notebook cell -----

# Students interested in Python OR Math
python_or_math = []

for name, interests in students.items():

    if "Python" in interests or "Math" in interests:
        python_or_math.append(name)

print("Students interested in Python OR Math:")
print(python_or_math)

# ----- Next notebook cell -----

student1 = input("Enter first student: ").strip()
student2 = input("Enter second student: ").strip()

if student1 not in students or student2 not in students:
    print("Invalid student name.")
elif student1 == student2:
    print("Please enter two different students.")
else:
    set1 = students[student1]
    set2 = students[student2]

    # Subjects that both students have
    common_subjects = set1 & set2
    
    # All subjects from both students
    all_student_subjects = set1 | set2

    # Subjects of student1 but not student2
    only_student1 = set1 - set2

    print(f"Common subjects between {student1} and {student2}: {common_subjects}")
    print(f"All subjects: {all_student_subjects}")
    print(f"Subjects that {student1} has but {student2} does not have: {only_student1}")

# ----- Next notebook cell -----

def jaccard_similarity(set_a, set_b):

    intersection = set_a & set_b
    union = set_a | set_b

    if len(union) == 0:
        return 0

    return len(intersection) / len(union)

# Calculate similarity for the two students entered above
if (student1 in students
    and student2 in students
    and student1 != student2 ):

    similarity = jaccard_similarity(
        students[student1],
        students[student2]
    )

    print(f"Jaccard Similarity between {student1} and {student2}: {similarity:.2f}")

# ----- Next notebook cell -----

most_similar_pair = None
highest_similarity = -1

# combinations() generates each pair only once
for student_a, student_b in combinations(students.keys(), 2):

    similarity = jaccard_similarity(students[student_a],students[student_b])

    print(f"{student_a} - {student_b}: {similarity:.2f}")

    if similarity > highest_similarity:

        highest_similarity = similarity
        most_similar_pair = (student_a,student_b)

print(f"Most similar students: {most_similar_pair[0]} and {most_similar_pair[1]}")
print(f"Similarity: {highest_similarity:.2f}")

# ----- Next notebook cell -----

recommendation_student = input("Enter a student name: ").strip()

THRESHOLD = 0.5

if recommendation_student not in students:
    print("Invalid student name.")
else:
    recommendations = []
    for other_student in students:
        # Do not compare the student with themselves
        if other_student == recommendation_student:
            continue

        similarity = jaccard_similarity(
            students[recommendation_student],
            students[other_student]
        )

        if similarity >= THRESHOLD:
            recommendations.append((other_student, similarity))

    print(f"Student: {recommendation_student}")

    if len(recommendations) == 0:
        print("No suitable study partner found.")
    else:
        print("Recommended study partners:")

        for name, similarity in recommendations:
            print(f"- {name} (Similarity = {similarity:.2f})")

# ----- Next notebook cell -----

graph = {}

# Add every student as a node
for student in students:
    graph[student] = []

# Create connections
for student_a, student_b in combinations(students.keys(), 2):
    similarity = jaccard_similarity(students[student_a],students[student_b])

    if similarity >= THRESHOLD:
        graph[student_a].append(student_b)
        graph[student_b].append(student_a)

print("Student Graph (Adjacency List):")
for student, connections in graph.items():
    if len(connections) == 0:
        print(f"{student} -> No connections")
    else:
        print(f"{student} -> {', '.join(connections)}")
