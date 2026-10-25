"""LAB SESSION 5 — Student management using a LIST as principal storage."""
import sys

def validate(student_id,name,score):
    sid=student_id.strip()
    name=name.strip()
    if not sid or not name: raise ValueError("ID and name are required")
    try: score=float(score)
    except ValueError as e: raise ValueError("Score must be numeric") from e
    if not 0<=score<=10: raise ValueError("Score must be in 0..10")
    return {"id":sid,"name":name,"score":score}

def add(students,student_id,name,score):
    data=validate(student_id,name,score)
    if any(item["id"]==data["id"] for item in students):
        raise ValueError("Duplicate student ID")
    students.append(data)

def find_by_name(students,name):
    query=name.strip().casefold()
    if not query: return []
    return [s for s in students if query in s["name"].casefold()]

def delete_by_id(students,student_id):
    for index,s in enumerate(students):
        if s["id"]==student_id:
            return students.pop(index)
    raise KeyError(student_id)

def sorted_by_score(students,descending=False):
    return sorted(students,key=lambda s:s["score"],reverse=descending)

def statistics(students):
    if not students: return None
    return {"highest":max(students,key=lambda s:s["score"]),
            "lowest":min(students,key=lambda s:s["score"]),
            "average":sum(s["score"] for s in students)/len(students)}

def show(students):
    for s in students:
        print(f'{s["id"]} | {s["name"]} | {s["score"]:g}/10')

def sample():
    students=[]
    grades=[5,6,7,8,9,10,5.5,6.5,7.5,8.5,9.5,4]
    for i,score in enumerate(grades,1):
        add(students,f"S{i:03}",f"Learner {i:02}",score)
    return students

def run_demo():
    students=sample()
    assert len(students)==12
    add(students,"S013","Learner 13",7)
    assert len(find_by_name(students,"learner"))==13
    removed=delete_by_id(students,"S013")
    assert removed["id"]=="S013" and len(students)==12
    print("Sorted:",[(s["id"],s["score"]) for s in sorted_by_score(students)])
    print("Statistics:",statistics(students))
    show(students)

def interactive():
    students=sample()
    while True:
        print("\n1.Add 2.Display 3.Search 4.Delete 5.Sort 6.Statistics 0.Exit")
        c=input("Choice: ").strip()
        try:
            if c=="0":break
            elif c=="1": add(students,input("ID: "),input("Name: "),input("Score: "))
            elif c=="2":show(students)
            elif c=="3":show(find_by_name(students,input("Name to search: ")))
            elif c=="4":delete_by_id(students,input("ID: ").strip())
            elif c=="5":
                show(sorted_by_score(students,input("Descending? [y/N] ").lower()=="y"))
            elif c=="6":print(statistics(students))
            else:print("Unknown menu option")
        except (ValueError,KeyError) as exc:
            print("Error:",exc)
if __name__=="__main__":
    run_demo() if "--demo" in sys.argv else interactive()
