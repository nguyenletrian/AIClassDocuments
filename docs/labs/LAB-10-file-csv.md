# LAB-10-file-csv — nguyên đề Anh, toàn bộ dịch Việt, hướng giải và code có note

**Nguồn:** `Lab Session 10.docx` đã được chuyển sang `labs/pythoclass/LAB-10-file-csv/LAB.md`; code nguyên chương trình từ bản chú thích `SOLUTION_ANNOTATED.py` lưu trong lịch sử repo, xây trên `labs/pythoclass/LAB-10-file-csv/SOLUTION.py`, đối chiếu `DEMO.py`. Không thay thuật toán. Tài liệu này không chia lời giải ra từng câu.

---

## PART 1 — COMPLETE ORIGINAL ENGLISH ASSIGNMENT

# LAB Session 10

## Objective
Develop a Python program to manage student grades using **File I/O, Functions, and Error Handling**.

## Requirements
Create a menu-driven program with these functions:

1. **Display All Students:** Read/display student data from `students.csv`.
2. **Add a New Student:** Enter student information and grades. Validate input and prevent duplicate Student IDs.
3. **Search Student by ID:** Search/display a student's information.
4. **Calculate Average Grade:** Display each student's average grade.
5. **Save Students to File:** Save current student data to `students.csv`.
6. **Exit:** Exit the program.

## Error Handling
Handle file-not-found errors, invalid numeric input, grades outside **0–100**, and duplicate student IDs.

## Sample `students.csv`

```csv
student_id,name,class_name,Python,Math,ML
S001,Learner 01,AI01,85,78,90
S002,Learner 02,AI01,72,85,80
S003,Learner 03,AI01,90,88,95
S004,Learner 04,AI02,65,70,68
S005,Learner 05,AI02,82,75,85
S006,Learner 06,AI02,78,80,72
S007,Learner 07,AI03,95,92,94
S008,Learner 08,AI03,70,68,75
S009,Learner 09,AI03,88,85,82
S010,Learner 10,AI03,76,90,88
```

---

## PHẦN 2 — BẢN DỊCH TIẾNG VIỆT TOÀN BỘ ĐỀ

# LAB SESSION 10 — Quản lý điểm sinh viên bằng file CSV

## Mục tiêu
Xây dựng chương trình Python quản lý điểm sinh viên bằng thao tác **File I/O**, các **hàm** và **xử lý lỗi**.

## Các yêu cầu
Tạo chương trình có menu với sáu chức năng:

1. **Hiển thị tất cả sinh viên:** Đọc dữ liệu sinh viên từ `students.csv` và hiển thị thông tin.
2. **Thêm sinh viên:** Nhập thông tin cá nhân và điểm của từng môn; kiểm tra dữ liệu hợp lệ và chống mã sinh viên trùng.
3. **Tìm theo mã sinh viên:** Nhập mã và hiển thị thông tin của sinh viên cần tìm.
4. **Tính điểm trung bình:** In điểm trung bình từng sinh viên.
5. **Lưu vào file:** Ghi dữ liệu đang quản lý vào `students.csv`.
6. **Thoát:** Kết thúc chương trình.

## Xử lý lỗi
Cần xử lý **không tìm thấy file**, **nhập số không hợp lệ**, **điểm ngoài phạm vi 0–100** và **mã sinh viên trùng**.

## Dữ liệu mẫu students.csv
Dùng bảng CSV gồm mã sinh viên, tên, lớp, điểm Python, Math và ML. Bảng được giữ nguyên số liệu, tên đã được thay bằng mã/tên giả lập để bảo vệ danh tính:

```csv
student_id,name,class_name,Python,Math,ML
S001,Learner 01,AI01,85,78,90
S002,Learner 02,AI01,72,85,80
S003,Learner 03,AI01,90,88,95
S004,Learner 04,AI02,65,70,68
S005,Learner 05,AI02,82,75,85
S006,Learner 06,AI02,78,80,72
S007,Learner 07,AI03,95,92,94
S008,Learner 08,AI03,70,68,75
S009,Learner 09,AI03,88,85,82
S010,Learner 10,AI03,76,90,88
```

Các cột của file là `student_id,name,class_name,Python,Math,ML`; tên `Learner 01..10` là dữ liệu minh họa đã được ẩn danh.

---

## Quy trình giải chi tiết và các công thức liên quan

**Luồng giải chung:** Mở `students.csv` → kiểm tra đủ sáu cột → đọc từng bản ghi → xác thực dữ liệu và số điểm → thao tác trên danh sách trong bộ nhớ → tính điểm hoặc ghi file khi người dùng chọn → báo lỗi dễ hiểu nếu sai hoặc thiếu file. Đây là cách làm đã có trong DEMO / lời giải tham khảo, không đổi sang bài toán khác.

### Bài 1 — Hướng giải và công thức

`csv.DictReader` đọc bảng dựa trên tên cột. `Path` trỏ đúng file cạnh chương trình; kiểm tra header và kiểm tra từng record trước khi in qua `display()`. Nếu thiếu file, dừng có thông báo thay vì trả dữ liệu bịa.

**Công thức / quy tắc:** Định dạng cột cố định: `student_id,name,class_name,Python,Math,ML`. Không có công thức.

**Chi tiết kiểm tra:** Đọc tệp bằng `csv.DictReader`; đối chiếu tiêu đề phải đủ sáu cột; mỗi hàng được chuyển thành dict, cần xử lý `FileNotFoundError` rõ ràng.

### Bài 2 — Hướng giải và công thức

`validate()` buộc ba trường ID/tên/lớp không rỗng, chuyển ba điểm sang `float`, kiểm tra 0–100. `add_student()` chỉ thêm nếu mã không nằm trong danh sách. Đó là code tham khảo đã có, từ phần thực hành CSV và kiểm tra dữ liệu.

**Công thức / quy tắc:** Với mỗi môn: 0 ≤ score ≤ 100; điều kiện ID mới: không tồn tại trong các bản ghi hiện tại.

**Chi tiết kiểm tra:** `validate` loại bỏ chuỗi rỗng, chuyển 3 điểm thành `float` và kiểm tra `0 ≤ score ≤ 100`. Kiểm tra `student_id` mới không trùng trước khi thêm.

### Bài 3 — Hướng giải và công thức

Dùng ID đã được `.strip()` để tìm bản ghi đúng. `next(...,None)` trả kết quả đầu tiên, hoặc None nếu không tìm thấy; không dùng tìm tên để thay cho tìm mã.

**Công thức / quy tắc:** Quy tắc tìm kiếm: `record['student_id'] == student_id` (khớp chính xác sau khi bỏ dấu cách đầu/cuối).

**Chi tiết kiểm tra:** Tìm ID sau khi `strip()` qua các dòng, trả bản ghi trùng mã hoặc `None` nếu không có; tránh tìm bằng tên thay cho mã.

### Bài 4 — Hướng giải và công thức

Đọc ba điểm đã xác thực của cùng một người, cộng và chia cho ba. Không cộng điểm của tất cả sinh viên rồi mới chia.

**Công thức / quy tắc:** Điểm trung bình = (Python + Math + ML) / 3.

**Chi tiết kiểm tra:** Điểm trung bình sinh viên = (điểm Python + điểm Math + điểm ML)/3. Chỉ tính trên các môn của cùng một sinh viên.

### Bài 5 — Hướng giải và công thức

Dùng `csv.DictWriter` tạo header, lần lượt ghi các dòng. Script tham khảo ghi sang tệp tạm rồi `os.replace` tệp đích nếu thành công, hạn chế hỏng file khi ghi dở. Không ghi file trong chế độ `--demo`.

**Công thức / quy tắc:** Số dòng sau khi thêm = số dòng trước + 1 nếu mã duy nhất và dữ liệu hợp lệ; việc ghi không làm mất sáu cột nguồn.

**Chi tiết kiểm tra:** Ghi header bằng `csv.DictWriter`, tạo file tạm và `os.replace` khi hoàn tất để tránh ghi dở; chỉ lưu khi chọn chức năng 5.

### Bài 6 — Hướng giải và công thức

`main()` đọc CSV, mở menu lặp và gọi đúng hàm theo lựa chọn. Người dùng chọn 0 thì kết thúc; thao tác Save ở lựa chọn 5 được thực hiện riêng để không tự ý ghi.

**Công thức / quy tắc:** Không có công thức: điều kiện dừng là lựa chọn menu Exit. Biến `dirty` theo dõi dữ liệu chưa lưu.

**Chi tiết kiểm tra:** Menu chạy trong `while True`; lựa chọn Exit sẽ dừng mà không ghi file ngoài ý muốn; kiểm tra và thông báo khi người dùng có thay đổi chưa lưu.

**Lưu ý chạy thực tế:** Code đọc `students.csv` bên cạnh file Python. Nếu dùng tài liệu một-file-này để học, sao chép nguyên bảng CSV bên trên vào file `students.csv` trước khi chạy menu. Không có file CSV xuất bản riêng trong `docs/labs`, đúng yêu cầu một lab = một tài liệu.

---

## PHẦN 4 — TOÀN BỘ CODE PYTHON CÙNG CHÚ THÍCH

**Code đã có đầy đủ các import, hằng số, hàm xử lý file, validate, add/search/average/save, menu và demo**, cùng comment giải thích. Tạo `lab_solution.py` và dữ liệu `students.csv` từ chính đề ở trên, chạy `python lab_solution.py --demo` để kiểm tra không tương tác, hoặc `python lab_solution.py` để dùng menu. **Demo không tự ghi đè CSV**, thao tác Save riêng trong menu có thể thay đổi file đã sao chép.

```python
"""Fully annotated English solution for LAB-10-file-csv.
Source methods and executable statements are preserved from the reviewed
labs/pythoclass reference implementation; explanatory comments are added.
"""

"""LAB SESSION 10 — CSV-based interactive student grade management.

Run: python SOLUTION.py           # interactive CLI
     python SOLUTION.py --demo    # safe in-memory tests, never writes students.csv
"""
# The csv standard-library module handles quoted fields and header names correctly.
import csv
# Use os.replace() for an atomic replacement after writing a temporary file.
import os
# Path constructs filesystem paths portably and makes adjacent data files discoverable.
from pathlib import Path
# Use sys.argv to choose an unattended demo instead of interactive prompts.
import sys
# Use tempfile to avoid corrupting an existing CSV if a write fails.
import tempfile

# Prepare this intermediate value for the next calculation or validation.
CSV_PATH=Path(__file__).resolve().parent/"students.csv"
# Prepare this intermediate value for the next calculation or validation.
FIELDS=["student_id","name","class_name","Python","Math","ML"]
# Prepare this intermediate value for the next calculation or validation.
SUBJECTS=["Python","Math","ML"]

# Function: Check all required CSV fields and convert three subject grades to numbers in the 0–100 range.
def validate(student):
    # Prepare this intermediate value for the next calculation or validation.
    sid=str(student.get("student_id","")).strip()
    # Prepare this intermediate value for the next calculation or validation.
    name=str(student.get("name","")).strip()
    # Prepare this intermediate value for the next calculation or validation.
    cls=str(student.get("class_name","")).strip()
    # Reject out-of-range or missing inputs early instead of silently accepting them.
    if not sid or not name or not cls: raise ValueError("ID, name and class are required")
    # Prepare this intermediate value for the next calculation or validation.
    result={"student_id":sid,"name":name,"class_name":cls}
    # Process each element of the input collection in order.
    for sub in SUBJECTS:
        # Catch expected user/file errors without terminating the whole interactive workflow.
        try: score=float(student[sub])
        # Handle expected exceptions while preserving diagnostics.
        except (ValueError,KeyError,TypeError) as exc: raise ValueError(f"{sub} grade must be numeric") from exc
        # Reject out-of-range or missing inputs early instead of silently accepting them.
        if not 0<=score<=100: raise ValueError(f"{sub} grade outside 0..100")
        result[sub]=score
    # Return the result for later reuse or testing instead of only printing it.
    return result

# Function: Read rows using csv.DictReader; check exact columns and unique student IDs.
def load_students(path=CSV_PATH):
    # Branch when this validated condition is true.
    if not Path(path).exists():
        raise FileNotFoundError(f"Missing data file: {path}")
    # Open the file using a context manager so it closes after reading/writing.
    with Path(path).open("r",encoding="utf-8",newline="") as f:
        # Map each row to column-name keys instead of fragile positional indexing.
        reader=csv.DictReader(f)
        # Branch when this validated condition is true.
        if reader.fieldnames != FIELDS:
            raise ValueError(f"Unexpected columns, expected {FIELDS}")
        # Prepare this intermediate value for the next calculation or validation.
        rows=[validate(r) for r in reader]
    # Prepare this intermediate value for the next calculation or validation.
    ids=[r["student_id"] for r in rows]
    # Reject out-of-range or missing inputs early instead of silently accepting them.
    if len(ids)!=len(set(ids)): raise ValueError("Duplicate student IDs already in CSV")
    # Return the result for later reuse or testing instead of only printing it.
    return rows

# Function: Append one validated record, only after rejecting a duplicate student ID.
def add_student(rows, student):
    # Prepare this intermediate value for the next calculation or validation.
    item=validate(student)
    # Branch when this validated condition is true.
    if any(r["student_id"]==item["student_id"] for r in rows):
        raise ValueError("Duplicate student ID")
    # Add the new element to a list while retaining insertion order.
    rows.append(item)

# Function: Return the matching student record or None using an ID comparison.
def search_by_id(rows, student_id):
    # Return the result for later reuse or testing instead of only printing it.
    return next((r for r in rows if r["student_id"]==student_id.strip()),None)

# Function: Compute the average of Python, Math and ML scores for one student.
def average_grade(student):
    # Return the result for later reuse or testing instead of only printing it.
    return sum(student[sub] for sub in SUBJECTS)/len(SUBJECTS)

# Function: Print identity and averaged score for every student record.
def display(rows):
    # Process each element of the input collection in order.
    for item in rows:
        # Show a human-readable result to the learner.
        print(f"{item['student_id']} | {item['name']} | {item['class_name']} | average={average_grade(item):.2f}/100")

# Function: Write a well-formed temporary CSV then atomically replace the destination.
def save_students(rows, path=CSV_PATH):
    """Write a temporary CSV first, then atomically replace target if successful."""
    # Prepare this intermediate value for the next calculation or validation.
    path=Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    # Prepare this intermediate value for the next calculation or validation.
    tmp=None
    # Catch expected user/file errors without terminating the whole interactive workflow.
    try:
        with tempfile.NamedTemporaryFile(mode="w",encoding="utf-8",newline="",dir=path.parent,
                                         # Prepare this intermediate value for the next calculation or validation.
                                         prefix=".students-",suffix=".csv",delete=False) as out:
            # Prepare this intermediate value for the next calculation or validation.
            tmp=Path(out.name)
            # Write rows using explicit column names, retaining stable CSV order.
            writer=csv.DictWriter(out,fieldnames=FIELDS)
            # Write the CSV header once before writing student records.
            writer.writeheader()
            # Process each element of the input collection in order.
            for row in rows: writer.writerow(validate(row))
        # Replace the destination only after all temporary rows were written.
        os.replace(tmp,path)
    # Clean up temporary resources whether execution succeeds or fails.
    finally:
        # Branch when this validated condition is true.
        if tmp is not None and tmp.exists(): tmp.unlink()

# Function: Run an in-memory ten-row example without modifying source students.csv.
def run_demo():
    # Prepare this intermediate value for the next calculation or validation.
    rows=load_students()
    # Verify the expected outcome and fail the demo if a regression occurs.
    assert len(rows)==10
    add_student(rows,{"student_id":"S011","name":"Learner 11","class_name":"AI04",
                      "Python":90,"Math":88,"ML":91})
    # Verify the expected outcome and fail the demo if a regression occurs.
    assert len(rows)==11
    # Verify the expected outcome and fail the demo if a regression occurs.
    assert abs(average_grade(search_by_id(rows,"S011"))-269/3)<1e-9
    # Catch expected user/file errors without terminating the whole interactive workflow.
    try:
        add_student(rows,{"student_id":"S011","name":"Duplicate","class_name":"AI04",
                          "Python":90,"Math":88,"ML":91})
        raise AssertionError("Duplicate check failed")
    # Handle expected exceptions while preserving diagnostics.
    except ValueError: pass
    # Show a human-readable result to the learner.
    print("PASS: CSV read, search, add, duplicate detection and average")
    display(rows[:3])
    # Show a human-readable result to the learner.
    print("(Demo does not overwrite students.csv)")

# Function: Run the six-option menu; retain changes in memory until Save is explicitly selected.
def main():
    # Catch expected user/file errors without terminating the whole interactive workflow.
    try: rows=load_students()
    # Handle expected exceptions while preserving diagnostics.
    except (OSError,ValueError,csv.Error) as exc:
        # Show a human-readable result to the learner.
        print("Cannot open students.csv:",exc)
        return
    # Prepare this intermediate value for the next calculation or validation.
    dirty=False
    # Repeat this operation until the stopping condition becomes false.
    while True:
        # Show a human-readable result to the learner.
        print("\n1.Display 2.Add 3.Search ID 4.Averages 5.Save 0.Exit")
        # Prepare this intermediate value for the next calculation or validation.
        choice=input("Choose: ").strip()
        # Catch expected user/file errors without terminating the whole interactive workflow.
        try:
            # Branch when this validated condition is true.
            if choice=="0":
                # Branch when this validated condition is true.
                if dirty: print("Unsaved changes are discarded. Select 5 to save next time.")
                # Exit the active loop after meeting the termination condition.
                break
            # Branch when this validated condition is true.
            if choice=="1": display(rows)
            # Handle an alternative choice only when earlier tests did not match.
            elif choice=="2":
                # Prepare this intermediate value for the next calculation or validation.
                record={"student_id":input("ID: "),"name":input("Name: "),
                        "class_name":input("Class: ")}
                # Process each element of the input collection in order.
                for subject in SUBJECTS: record[subject]=input(f"{subject} grade [0,100]: ")
                add_student(rows,record)
                # Prepare this intermediate value for the next calculation or validation.
                dirty=True
                # Show a human-readable result to the learner.
                print("Student added (not yet saved).")
            # Handle an alternative choice only when earlier tests did not match.
            elif choice=="3":
                # Show a human-readable result to the learner.
                print(search_by_id(rows,input("Student ID: ")) or "Not found")
            # Handle an alternative choice only when earlier tests did not match.
            elif choice=="4":
                # Process each element of the input collection in order.
                for row in rows:print(row["student_id"],round(average_grade(row),2))
            # Handle an alternative choice only when earlier tests did not match.
            elif choice=="5":
                save_students(rows)
                # Prepare this intermediate value for the next calculation or validation.
                dirty=False
                # Show a human-readable result to the learner.
                print("Saved",CSV_PATH)
            # Run the fallback branch when no earlier condition applies.
            else: print("Unknown option")
        # Handle expected exceptions while preserving diagnostics.
        except (OSError,ValueError,KeyError) as exc:
            # Show a human-readable result to the learner.
            print("Error:",exc)
if __name__=="__main__":
    run_demo() if "--demo" in sys.argv else main()
```

**Ghi chú nguồn:** Hàm mã giải là bản tham khảo đã lưu chứ không nhất thiết là từng dòng code demo của học viên. Không tự viết thuật toán mới trong bản tài liệu này.
