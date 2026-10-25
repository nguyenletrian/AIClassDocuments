# coding: utf-8
# DEMO.py — original student practice code aligned with LAB-05-student-list.
# Source: nguyenletrian/PythoClass (private). This is notebook/code provenance, NOT a complete tested solution.
# Read and run sections independently; interactive cells and exploratory snippets may not run sequentially.
# Original example student names (if present) are anonymized before entering the public destination.


# ========= BEGIN SOURCE: LAB Session 5.ipynb =========

# === Notebook cell 1 ===
studenList = [
    [1,"Nguyen Van A",5],
    [2,"Nguyen Van B",6],
    [3,"Nguyen Van C",7]
]
newStudent = str(input("Please input studend info"))
studentInfo = newStudent.split(" ")
studenList.append(studentInfo)
for index,val in enumerate(studenList):
    print(f"Sinh vien thu {index}: MSSV {val[0]}, Ten {val[1]}, Diem {val[2]}")

# === Notebook cell 2 ===
searchName = str(input("Please input student name"))
for index , val in enumerate(studenList):
    if searchName == val[1]:
        print(f"Sinh vien thu {index}: MSSV {val[0]}, Ten {val[1]}, Diem {val[2]}")

# === Notebook cell 3 ===
id = input("Please input student id")
for index , val in enumerate(studenList):
    if int(id) == int(val[0]):
        print(id)
        studenList.pop(index)
print(studenList)

# === Notebook cell 4 ===
# Sort list
    


# === Notebook cell 5 ===
maxScore = 0
indexMaxScore = None
for index , val in enumerate(studenList):
    if val[2] > maxScore:
        maxScore = val[2]
        indexMaxScore = index
print(studenList[indexMaxScore])

# === Notebook cell 6 ===
minScore = 10
indexMinScore = None
for index , val in enumerate(studenList):
    if val[2] < minScore:
        minScore = val[2]
        indexMinScore = index
print(studenList[indexMinScore])

# === Notebook cell 7 ===
#

# ========= END SOURCE: LAB Session 5.ipynb =========


# ========= BEGIN SOURCE: Demo/5_list.ipynb =========

# === Notebook cell 1 ===
# tao list rong
empty_list = []
# tao list chua cac phan tu co kieu du lieu giong nhau
student_list = ["Van", "Tuan", "Khoi"]
# tao list chua cac phan tu co kieu du lieu khac nhau
mixed_list = [1, "Apple", 20.5]
# tao list bang list()
numbers = list((1, 2, 3))
print("Empty list: ", empty_list)
print("Student list: ", student_list)
print("Mixed_list: ", mixed_list)
print("Number: ", numbers)

# === Notebook cell 2 ===
print("student_list[0]: ",student_list[0])
print("student_list[2]: ",student_list[2])
print("student_list[-1]: ",student_list[-1])
print("student_list[-2]: ",student_list[-2])

# === Notebook cell 3 ===
for item in student_list:
    print(item)

# === Notebook cell 4 ===
for index in range(len(student_list)):
    print(student_list[index])

# === Notebook cell 5 ===
for index, item in enumerate(student_list):
    print(index, ":", item)

# === Notebook cell 6 ===
# kiem tra xem co ton tai trong danh sach hay ko
if "Tuan" in student_list:
    print("La sinh vien cua lop")
else:
    print("Ko la sinh vien cua lop")

# === Notebook cell 7 ===
# trich xuat 1 phan cua danh sach
print("student_list[0:2]: ", student_list[0:2])
print("student_list[1:]: ", student_list[1:])
print("reverse: ", student_list[::-1])

# === Notebook cell 8 ===
# thay the gia tri phan tu o 1 vi tri bat ky
student_list[1] = "Hoang Tuan"
print("student_list: ", student_list)

# === Notebook cell 9 ===
# thay the bang slice
student_list[1:2] = ["An", "Nam"]
print("student_list: ", student_list)

# === Notebook cell 10 ===
# them 1 phan tu vao vi tri cuoi cung cua danh sach
student_list.append("Tuan")
print("student_list: ", student_list)

# === Notebook cell 11 ===
# them 1 phan tu vao vi tri bat ky theo index
student_list.insert(1, "Nhi")
print("student_list: ", student_list)

# === Notebook cell 12 ===
# them 1 mang vao cuoi danh sach
sub_list = ["Diem", "Vy"]
student_list.extend(sub_list)
print("student_list: ", student_list)

# === Notebook cell 13 ===
# xoa phan tu theo value
student_list.remove("Van")
print("student_list: ", student_list)

# === Notebook cell 14 ===
# xoa phan tu theo index
student_list.pop(2)
print("student_list: ", student_list)

# === Notebook cell 15 ===
# xoa phan tu theo index (ko the hien index) thi se xoa phan tu cuoi cung
student_list.pop()
print("student_list: ", student_list)

# === Notebook cell 16 ===
# xoa phan tu dung del
del student_list[1]
print("student_list: ", student_list)

# === Notebook cell 17 ===
# xoa phan tu dung del, slice
del student_list[1:2]
print("student_list: ", student_list)

# === Notebook cell 18 ===
# xoa het tat ca phan tu trong danh sach
student_list.clear()
print("student_list: ", student_list)

# === Notebook cell 19 ===
students = ['Van', 'Nhi', 'An', 'Nam', 'Khoi', 'Tuan', 'Diem', 'Vy']
students.sort()
print("students: ", students)

# === Notebook cell 20 ===
students.sort(reverse=True)
print("students: ", students)

# ========= END SOURCE: Demo/5_list.ipynb =========
