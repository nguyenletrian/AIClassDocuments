"""Fully annotated English solution for LAB-05-student-list.
Source methods and executable statements are preserved from the reviewed
labs/pythoclass reference implementation; explanatory comments are added.
"""

"""LAB SESSION 5 — Student management using a LIST as principal storage."""
# Use sys.argv to choose an unattended demo instead of interactive prompts.
import sys

# Function: Validate required ID and name and convert the 0–10 score to a float.
def validate(student_id,name,score):
    # Prepare this intermediate value for the next calculation or validation.
    sid=student_id.strip()
    # Prepare this intermediate value for the next calculation or validation.
    name=name.strip()
    # Reject out-of-range or missing inputs early instead of silently accepting them.
    if not sid or not name: raise ValueError("ID and name are required")
    # Catch expected user/file errors without terminating the whole interactive workflow.
    try: score=float(score)
    # Handle expected exceptions while preserving diagnostics.
    except ValueError as e: raise ValueError("Score must be numeric") from e
    # Reject out-of-range or missing inputs early instead of silently accepting them.
    if not 0<=score<=10: raise ValueError("Score must be in 0..10")
    # Return the result for later reuse or testing instead of only printing it.
    return {"id":sid,"name":name,"score":score}

# Function: Append a dictionary record to a LIST, rejecting an ID already in that list.
def add(students,student_id,name,score):
    # Prepare this intermediate value for the next calculation or validation.
    data=validate(student_id,name,score)
    # Branch when this validated condition is true.
    if any(item["id"]==data["id"] for item in students):
        raise ValueError("Duplicate student ID")
    # Add the new element to a list while retaining insertion order.
    students.append(data)

# Function: Find students by a case-insensitive substring of their name.
def find_by_name(students,name):
    # Prepare this intermediate value for the next calculation or validation.
    query=name.strip().casefold()
    # Branch when this validated condition is true.
    if not query: return []
    # Return the result for later reuse or testing instead of only printing it.
    return [s for s in students if query in s["name"].casefold()]

# Function: Find a matching ID, remove that list element with pop(), or reject missing IDs.
def delete_by_id(students,student_id):
    # Keep the list index while inspecting each student record.
    for index,s in enumerate(students):
        # Branch when this validated condition is true.
        if s["id"]==student_id:
            # Return the result for later reuse or testing instead of only printing it.
            return students.pop(index)
    raise KeyError(student_id)

# Function: Return a new sorted list by numeric scores without mutating the source list.
def sorted_by_score(students,descending=False):
    # Return the result for later reuse or testing instead of only printing it.
    return sorted(students,key=lambda s:s["score"],reverse=descending)

# Function: Compute highest-scoring record, lowest-scoring record and arithmetic mean.
def statistics(students):
    # Branch when this validated condition is true.
    if not students: return None
    # Return the result for later reuse or testing instead of only printing it.
    return {"highest":max(students,key=lambda s:s["score"]),
            "lowest":min(students,key=lambda s:s["score"]),
            "average":sum(s["score"] for s in students)/len(students)}

# Function: Display every list entry in ID, name, score order.
def show(students):
    # Process each element of the input collection in order.
    for s in students:
        # Show a human-readable result to the learner.
        print(f'{s["id"]} | {s["name"]} | {s["score"]:g}/10')

# Function: Generate twelve synthetic student records for reproducible demonstrations.
def sample():
    # Prepare this intermediate value for the next calculation or validation.
    students=[]
    # Prepare this intermediate value for the next calculation or validation.
    grades=[5,6,7,8,9,10,5.5,6.5,7.5,8.5,9.5,4]
    # Keep the list index while inspecting each student record.
    for i,score in enumerate(grades,1):
        add(students,f"S{i:03}",f"Learner {i:02}",score)
    # Return the result for later reuse or testing instead of only printing it.
    return students

# Function: Exercise creating, searching, deleting, sorting and statistics with assertions.
def run_demo():
    # Prepare this intermediate value for the next calculation or validation.
    students=sample()
    # Verify the expected outcome and fail the demo if a regression occurs.
    assert len(students)==12
    add(students,"S013","Learner 13",7)
    # Verify the expected outcome and fail the demo if a regression occurs.
    assert len(find_by_name(students,"learner"))==13
    # Prepare this intermediate value for the next calculation or validation.
    removed=delete_by_id(students,"S013")
    # Verify the expected outcome and fail the demo if a regression occurs.
    assert removed["id"]=="S013" and len(students)==12
    # Show a human-readable result to the learner.
    print("Sorted:",[(s["id"],s["score"]) for s in sorted_by_score(students)])
    # Show a human-readable result to the learner.
    print("Statistics:",statistics(students))
    show(students)

# Function: Loop over user menu options until the exit command is selected.
def interactive():
    # Prepare this intermediate value for the next calculation or validation.
    students=sample()
    # Repeat this operation until the stopping condition becomes false.
    while True:
        # Show a human-readable result to the learner.
        print("\n1.Add 2.Display 3.Search 4.Delete 5.Sort 6.Statistics 0.Exit")
        # Prepare this intermediate value for the next calculation or validation.
        c=input("Choice: ").strip()
        # Catch expected user/file errors without terminating the whole interactive workflow.
        try:
            # Branch when this validated condition is true.
            if c=="0":break
            # Handle an alternative choice only when earlier tests did not match.
            elif c=="1": add(students,input("ID: "),input("Name: "),input("Score: "))
            # Handle an alternative choice only when earlier tests did not match.
            elif c=="2":show(students)
            # Handle an alternative choice only when earlier tests did not match.
            elif c=="3":show(find_by_name(students,input("Name to search: ")))
            # Handle an alternative choice only when earlier tests did not match.
            elif c=="4":delete_by_id(students,input("ID: ").strip())
            # Handle an alternative choice only when earlier tests did not match.
            elif c=="5":
                show(sorted_by_score(students,input("Descending? [y/N] ").lower()=="y"))
            # Handle an alternative choice only when earlier tests did not match.
            elif c=="6":print(statistics(students))
            # Run the fallback branch when no earlier condition applies.
            else:print("Unknown menu option")
        # Handle expected exceptions while preserving diagnostics.
        except (ValueError,KeyError) as exc:
            # Show a human-readable result to the learner.
            print("Error:",exc)
if __name__=="__main__":
    run_demo() if "--demo" in sys.argv else interactive()
