# Lab Session 5 — Hệ thống sinh viên bằng List

**File Word gốc:** `Lab Session 5.docx`. Mỗi yêu cầu sau đây xuất hiện đúng một lần, theo thứ tự **English → Tiếng Việt → bài giải trích code đã có → giải thích quy trình và công thức**. Đề Anh lấy từ `labs/pythoclass/LAB-05-student-list/LAB.md`; mã thực hành đối chiếu `DEMO.py`, code đã tổng hợp ở `SOLUTION.py` và phiên bản có chú thích ở `docs/labs/LAB-05-student-list/SOLUTION_ANNOTATED.py`. Các chức năng cơ bản liên hệ PY-05, PY-06, PY-09. **List** là đối tượng lưu trữ chính, mỗi phần tử có thể là một dictionary mô tả sinh viên.

### English — Original objective

Develop a console-based Student Management System in Python using a **list** as the main data structure.

### Tiếng Việt — Dịch mục tiêu

Xây dựng hệ thống quản lý sinh viên chạy trên terminal bằng Python; sử dụng **danh sách** làm cấu trúc chứa dữ liệu chính.

## Bài 1

### English — Original Word requirement

**Add a student:** Input student information (ID, name, score). Store the student in a list.

### Tiếng Việt — Dịch đề

**Thêm sinh viên:** Nhập mã số, tên và điểm; thêm bản ghi vào danh sách (**List**) làm cấu trúc lưu trữ chính. Code đã học thêm kiểm tra mã trùng.

### Bài giải — Trích mã đã có

**Nguồn:** `labs/pythoclass/LAB-05-student-list/SOLUTION.py` và bản code giải thích `docs/labs/LAB-05-student-list/SOLUTION_ANNOTATED.py`, hàm `add()`. Đối chiếu với `DEMO.py` (code thực hành, chưa hoàn chỉnh).

```python
def add(students,student_id,name,score):
    # Prepare this intermediate value for the next calculation or validation.
    data=validate(student_id,name,score)
    # Branch when this validated condition is true.
    if any(item["id"]==data["id"] for item in students):
        raise ValueError("Duplicate student ID")
    # Add the new element to a list while retaining insertion order.
    students.append(data)

# Function: Find students by a case-insensitive substring of their name.
```

### Giải thích quy trình giải và công thức

Đầu tiên dùng `validate()` từ code nguồn để làm sạch ID/tên và đổi điểm về `float`. Sau đó kiểm tra trùng ID bằng `any` và dùng `append` thêm bản ghi vào list. Các ví dụ DEMO ban đầu đưa thông tin sinh viên vào list nhưng chưa thống nhất kiểu dữ liệu, nên bản tham chiếu kiểm tra kỹ hơn.

**Công thức / lưu ý:** Điểm hợp lệ được code tham khảo dùng là 0–10 (đây là quy ước của code, không phải ngưỡng ghi trực tiếp trong Word).

## Bài 2

### English — Original Word requirement

**Display student list:** Show all students in the list.

### Tiếng Việt — Dịch đề

**Hiển thị:** In tất cả sinh viên có trong danh sách cùng mã, tên và điểm.

### Bài giải — Trích mã đã có

**Nguồn:** `labs/pythoclass/LAB-05-student-list/SOLUTION.py` và bản code giải thích `docs/labs/LAB-05-student-list/SOLUTION_ANNOTATED.py`, hàm `show()`. Đối chiếu với `DEMO.py` (code thực hành, chưa hoàn chỉnh).

```python
def show(students):
    # Process each element of the input collection in order.
    for s in students:
        # Show a human-readable result to the learner.
        print(f'{s["id"]} | {s["name"]} | {s["score"]:g}/10')

# Function: Generate twelve synthetic student records for reproducible demonstrations.
```

### Giải thích quy trình giải và công thức

Dùng vòng lặp duyệt từng phần tử của list và truy cập các khóa `id`, `name`, `score` của từng phần tử. Không dùng dictionary làm cấu trúc chứa danh sách chính.

**Công thức / lưu ý:** Không có công thức; độ dài danh sách `len(students)` cho biết số bản ghi.

## Bài 3

### English — Original Word requirement

**Search student by name:** Input a name. Display matching students.

### Tiếng Việt — Dịch đề

**Tìm theo tên:** Nhập tên rồi hiện các sinh viên có tên khớp; bản code tham khảo hỗ trợ tìm một phần tên không phân biệt chữ hoa/thường.

### Bài giải — Trích mã đã có

**Nguồn:** `labs/pythoclass/LAB-05-student-list/SOLUTION.py` và bản code giải thích `docs/labs/LAB-05-student-list/SOLUTION_ANNOTATED.py`, hàm `find_by_name()`. Đối chiếu với `DEMO.py` (code thực hành, chưa hoàn chỉnh).

```python
def find_by_name(students,name):
    # Prepare this intermediate value for the next calculation or validation.
    query=name.strip().casefold()
    # Branch when this validated condition is true.
    if not query: return []
    # Return the result for later reuse or testing instead of only printing it.
    return [s for s in students if query in s["name"].casefold()]

# Function: Find a matching ID, remove that list element with pop(), or reject missing IDs.
```

### Giải thích quy trình giải và công thức

Chuẩn hóa tên bằng `.strip().casefold()` rồi lọc phần tử chứa chuỗi tìm kiếm. Khác với DEMO so sánh tên chính xác, cách này thuận tiện với dữ liệu thực tế.

**Công thức / lưu ý:** So sánh `query in student_name.casefold()`; kết quả là một list sinh viên khớp.

## Bài 4

### English — Original Word requirement

**Delete a student:** Input student ID. Remove the student from the list.

### Tiếng Việt — Dịch đề

**Xóa:** Nhập mã sinh viên và xóa bản ghi tương ứng trong danh sách.

### Bài giải — Trích mã đã có

**Nguồn:** `labs/pythoclass/LAB-05-student-list/SOLUTION.py` và bản code giải thích `docs/labs/LAB-05-student-list/SOLUTION_ANNOTATED.py`, hàm `delete_by_id()`. Đối chiếu với `DEMO.py` (code thực hành, chưa hoàn chỉnh).

```python
def delete_by_id(students,student_id):
    # Keep the list index while inspecting each student record.
    for index,s in enumerate(students):
        # Branch when this validated condition is true.
        if s["id"]==student_id:
            # Return the result for later reuse or testing instead of only printing it.
            return students.pop(index)
    raise KeyError(student_id)

# Function: Return a new sorted list by numeric scores without mutating the source list.
```

### Giải thích quy trình giải và công thức

Dùng `enumerate` lấy cặp chỉ số và bản ghi, sau đó `pop(index)` xóa đúng sinh viên có mã cần tìm. Nếu không thấy ID, báo lỗi.

**Công thức / lưu ý:** Duyệt tối đa n phần tử, độ phức tạp tìm ID là O(n).

## Bài 5

### English — Original Word requirement

**Sort students by score:** Sort the list in ascending or descending order based on score.

### Tiếng Việt — Dịch đề

**Sắp xếp:** Sắp xếp theo điểm tăng dần hoặc giảm dần.

### Bài giải — Trích mã đã có

**Nguồn:** `labs/pythoclass/LAB-05-student-list/SOLUTION.py` và bản code giải thích `docs/labs/LAB-05-student-list/SOLUTION_ANNOTATED.py`, hàm `sorted_by_score()`. Đối chiếu với `DEMO.py` (code thực hành, chưa hoàn chỉnh).

```python
def sorted_by_score(students,descending=False):
    # Return the result for later reuse or testing instead of only printing it.
    return sorted(students,key=lambda s:s["score"],reverse=descending)

# Function: Compute highest-scoring record, lowest-scoring record and arithmetic mean.
```

### Giải thích quy trình giải và công thức

Dùng `sorted(students, key=..., reverse=...)` để tạo kết quả có thứ tự theo điểm số; không sắp chuỗi điểm thay cho số.

**Công thức / lưu ý:** Sắp xếp trung bình O(n log n); `reverse=True` đảo sang điểm giảm dần.

## Bài 6

### English — Original Word requirement

**Statistics:** Find the student with the highest score; find the student with the lowest score; calculate the average score.

### Tiếng Việt — Dịch đề

**Thống kê:** Tìm sinh viên điểm cao nhất, thấp nhất và tính điểm trung bình của các sinh viên.

### Bài giải — Trích mã đã có

**Nguồn:** `labs/pythoclass/LAB-05-student-list/SOLUTION.py` và bản code giải thích `docs/labs/LAB-05-student-list/SOLUTION_ANNOTATED.py`, hàm `statistics()`. Đối chiếu với `DEMO.py` (code thực hành, chưa hoàn chỉnh).

```python
def statistics(students):
    # Branch when this validated condition is true.
    if not students: return None
    # Return the result for later reuse or testing instead of only printing it.
    return {"highest":max(students,key=lambda s:s["score"]),
            "lowest":min(students,key=lambda s:s["score"]),
            "average":sum(s["score"] for s in students)/len(students)}

# Function: Display every list entry in ID, name, score order.
```

### Giải thích quy trình giải và công thức

Với list không rỗng, dùng `max` và `min` theo khóa điểm để tìm toàn bộ bản ghi đứng đầu/cuối, rồi cộng điểm chia số sinh viên.

**Công thức / lưu ý:** Trung bình = tổng điểm / n. Khi n=0, hàm trả `None` thay vì chia cho 0.

## Bài 7

### English — Original Word requirement

**Exit program.**

### Tiếng Việt — Dịch đề

**Thoát:** Cung cấp lựa chọn thoát khỏi chương trình quản lý sinh viên dạng menu.

### Bài giải — Trích mã đã có

**Nguồn:** `labs/pythoclass/LAB-05-student-list/SOLUTION.py` và bản code giải thích `docs/labs/LAB-05-student-list/SOLUTION_ANNOTATED.py`, hàm `interactive()`. Đối chiếu với `DEMO.py` (code thực hành, chưa hoàn chỉnh).

```python
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
```

### Giải thích quy trình giải và công thức

Dùng vòng `while True` hiển thị menu, chọn tác vụ theo `if/elif`, xử lý lỗi đầu vào, và `break` khi chọn Exit. Đây là chương trình đã có, không tạo menu mới.

**Công thức / lưu ý:** Không dùng công thức toán; điều kiện kết thúc menu là lựa chọn 0 trong code tham khảo.

## Phần dùng chung và giới hạn

- Các hàm `add()`, `show()`, `find_by_name()`, `delete_by_id()`, `sorted_by_score()`, `statistics()`, `interactive()` là hàm trong một ứng dụng; cần giữ thêm `validate()`, `sample()`, và `import sys` như ở file tham khảo khi chạy toàn chương trình.
- Không viết lời giải mới: những hàm được trích từ code đã có; nếu demo ban đầu bỏ trống Sort hoặc có dữ liệu lẫn kiểu, điều đó đã được ghi nhận thay vì giả nhận demo giải đủ.
- Lab này chỉ xuất **một file Markdown duy nhất**, không phát hành file Python hoặc README tách riêng.
