# LAB-05-student-list — English brief, Vietnamese brief, method and full commented script

**Nguồn đề:** `PythoClass` Word (bản chép ở `labs/pythoclass/LAB-05-student-list/LAB.md`). **Nguồn code:** bản giải/annotated có sẵn từ repo AIClassDocuments (không nhận là nguyên văn code demo nếu demo chưa đủ), đối chiếu `labs/pythoclass/LAB-05-student-list/DEMO.py` và `SOLUTION.py`. **Một tài liệu duy nhất**, không chia đề/đáp án xen kẽ.

---

## PART 1 — COMPLETE ORIGINAL ENGLISH ASSIGNMENT

# LAB Session 5

## Objective
Develop a console-based Student Management System in Python using a **list** as the main data structure.

## Requirements
Write a Python program that implements the following features:

1. **Add a student:** Input student information (ID, name, score). Store the student in a list.
2. **Display student list:** Show all students in the list.
3. **Search student by name:** Input a name. Display matching students.
4. **Delete a student:** Input student ID. Remove the student from the list.
5. **Sort students by score:** Sort the list in ascending or descending order based on score.
6. **Statistics:** Find the student with the highest score; find the student with the lowest score; calculate the average score.
7. **Exit program.**

---

## PHẦN 2 — BẢN DỊCH TIẾNG VIỆT TOÀN BỘ ĐỀ

# LAB SESSION 5 — Quản lý sinh viên bằng List

## Mục tiêu
Xây dựng hệ thống quản lý sinh viên trên console bằng Python, sử dụng **list** làm cấu trúc lưu trữ chính.

## Yêu cầu
Viết chương trình Python có các chức năng:

1. **Thêm sinh viên:** Nhập ID, tên, điểm; lưu vào một danh sách.
2. **Hiển thị danh sách sinh viên:** In toàn bộ sinh viên trong list.
3. **Tìm sinh viên theo tên:** Nhập tên, hiển thị sinh viên khớp.
4. **Xóa sinh viên:** Nhập ID, xóa sinh viên tương ứng khỏi danh sách.
5. **Sắp xếp theo điểm:** Sắp xếp danh sách tăng dần hoặc giảm dần theo điểm.
6. **Thống kê:** Tìm sinh viên có điểm cao nhất, thấp nhất và tính điểm trung bình.
7. **Thoát chương trình:** Cho phép người dùng kết thúc menu.

---

## Quy trình giải chi tiết và các công thức liên quan

**Luồng giải chung:** Đọc yêu cầu và dữ liệu đầu vào → xác thực kiểu và miền giá trị → chọn cấu trúc dữ liệu/điều kiện/vòng lặp đã học → tính toán hoặc cập nhật → kiểm tra kết quả bằng ví dụ đề → xử lý trường hợp rỗng/sai. Các hàm trong phần code bên dưới là một chương trình hoàn chỉnh và có thể chạy cùng nhau.

### Bài 1 — Cách thực hiện

Đầu tiên dùng `validate()` từ code nguồn để làm sạch ID/tên và đổi điểm về `float`. Sau đó kiểm tra trùng ID bằng `any` và dùng `append` thêm bản ghi vào list. Các ví dụ DEMO ban đầu đưa thông tin sinh viên vào list nhưng chưa thống nhất kiểu dữ liệu, nên bản tham chiếu kiểm tra kỹ hơn.

**Công thức / lưu ý:** Điểm hợp lệ được code tham khảo dùng là 0–10 (đây là quy ước của code, không phải ngưỡng ghi trực tiếp trong Word).

**Điểm cần kiểm tra:** list là cấu trúc chứa chính; mỗi phần tử dùng dictionary có ID/tên/điểm.

### Bài 2 — Cách thực hiện

Dùng vòng lặp duyệt từng phần tử của list và truy cập các khóa `id`, `name`, `score` của từng phần tử. Không dùng dictionary làm cấu trúc chứa danh sách chính.

**Công thức / lưu ý:** Không có công thức; độ dài danh sách `len(students)` cho biết số bản ghi.

**Điểm cần kiểm tra:** thêm qua `append` và kiểm tra trùng mã nếu code tham khảo có hỗ trợ.

### Bài 3 — Cách thực hiện

Chuẩn hóa tên bằng `.strip().casefold()` rồi lọc phần tử chứa chuỗi tìm kiếm. Khác với DEMO so sánh tên chính xác, cách này thuận tiện với dữ liệu thực tế.

**Công thức / lưu ý:** So sánh `query in student_name.casefold()`; kết quả là một list sinh viên khớp.

**Điểm cần kiểm tra:** tìm tên bằng `casefold()`; duyệt và xóa theo ID bằng `enumerate()/pop()`.

### Bài 4 — Cách thực hiện

Dùng `enumerate` lấy cặp chỉ số và bản ghi, sau đó `pop(index)` xóa đúng sinh viên có mã cần tìm. Nếu không thấy ID, báo lỗi.

**Công thức / lưu ý:** Duyệt tối đa n phần tử, độ phức tạp tìm ID là O(n).

**Điểm cần kiểm tra:** sắp xếp bằng `sorted(..., key=...)`; không so sánh điểm như chuỗi.

### Bài 5 — Cách thực hiện

Dùng `sorted(students, key=..., reverse=...)` để tạo kết quả có thứ tự theo điểm số; không sắp chuỗi điểm thay cho số.

**Công thức / lưu ý:** Sắp xếp trung bình O(n log n); `reverse=True` đảo sang điểm giảm dần.

**Điểm cần kiểm tra:** điểm trung bình = tổng điểm/số sinh viên; xử lý list rỗng.

### Bài 6 — Cách thực hiện

Với list không rỗng, dùng `max` và `min` theo khóa điểm để tìm toàn bộ bản ghi đứng đầu/cuối, rồi cộng điểm chia số sinh viên.

**Công thức / lưu ý:** Trung bình = tổng điểm / n. Khi n=0, hàm trả `None` thay vì chia cho 0.

**Điểm cần kiểm tra:** menu `while True` thoát khi chọn 0.

### Bài 7 — Cách thực hiện

Dùng vòng `while True` hiển thị menu, chọn tác vụ theo `if/elif`, xử lý lỗi đầu vào, và `break` khi chọn Exit. Đây là chương trình đã có, không tạo menu mới.

**Công thức / lưu ý:** Không dùng công thức toán; điều kiện kết thúc menu là lựa chọn 0 trong code tham khảo.

**Điểm cần kiểm tra:** menu `while True` thoát khi chọn 0.


---

## PHẦN 4 — TOÀN BỘ CODE PYTHON CÙNG CHÚ THÍCH

**Nguồn code:** `labs/pythoclass/LAB-05-student-list/SOLUTION.py` và phiên bản chú thích đã có trong lịch sử dự án. Code giữ nguyên logic thực hành; `#` trong file dùng để giải thích từng đoạn. Sao chép **nguyên khối** sau vào một file `lab_solution.py` trong môi trường Python; chạy bằng `python lab_solution.py --demo` nếu là lab menu, hoặc `python lab_solution.py` để thực hiện lệnh tương tác/kiểm thử. Các đường dẫn, nguồn dữ liệu đi kèm vẫn cần tuân theo hướng dẫn trong script.

```python
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
```

**Lưu ý:** Nếu demo gốc chỉ thể hiện một phần, code đầy đủ được lấy từ lời giải tham khảo đã được lưu/kiểm tra, không phải phần tự sáng tác ở tài liệu này.
