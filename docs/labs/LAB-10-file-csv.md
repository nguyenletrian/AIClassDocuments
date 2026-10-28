# Lab Session 10 — Quản lý điểm sinh viên qua file CSV

**Tương ứng duy nhất Word gốc:** `Lab Session 10.docx`. Đề Anh dưới đây là bản chép từ `labs/pythoclass/LAB-10-file-csv/LAB.md`; mỗi câu có bản dịch Việt, đoạn code **đã tồn tại trong repo**, rồi mới đến giải thích quy trình và công thức. Đối chiếu `DEMO.py` của bài File I/O, `SOLUTION.py` được kiểm tra, bản thêm comment `docs/labs/LAB-10-file-csv/SOLUTION_ANNOTATED.py`, giáo trình PY-12 và PY-44. Bài Word yêu cầu quản lý **điểm sinh viên**, không thay bằng quản lý sản phẩm trong notebook demo.

### English — Original objective

Develop a Python program to manage student grades using **File I/O, Functions, and Error Handling**.

### Tiếng Việt — Dịch mục tiêu

Tạo chương trình Python quản lý điểm sinh viên thông qua thao tác file, tổ chức hàm, xử lý lỗi và menu console.

**Dữ liệu mẫu trong Word (bản chép, 10 người dùng tên giả):**

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

**Mã khởi tạo chung:** `SOLUTION.py` sử dụng `csv`, `os`, `pathlib.Path`, `sys`, `tempfile`, và quy ước `FIELDS=['student_id','name','class_name','Python','Math','ML']` cùng `SUBJECTS=['Python','Math','ML']`. Các hàm dưới đây được trích từ cùng một script nên phải giữ các import, hằng và hàm phụ trợ khi chạy đầy đủ. Dữ liệu CSV mẫu đã được đưa **trong chính tài liệu này**, không xuất file thứ hai.

## Bài 1

### English — Original Word requirement

**Display All Students:** Read/display student data from `students.csv`.

### Tiếng Việt — Bản dịch

**Hiển thị tất cả sinh viên:** Đọc file `students.csv` và hiển thị thông tin sinh viên theo các cột mã, tên, lớp và điểm các môn.

### Bài giải — Code đã có trong demo/giáo trình

**Nguồn:** `labs/pythoclass/LAB-10-file-csv/SOLUTION.py` / phiên bản comment `docs/labs/LAB-10-file-csv/SOLUTION_ANNOTATED.py`, hàm `load_students()`, `display()`. `DEMO.py` là code thực hành để đối chiếu, không mặc nhiên là lời giải chuẩn của Word.

```python
# Hàm nguồn load_students() từ code lời giải tham khảo hiện có.
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

# Hàm nguồn display() từ code lời giải tham khảo hiện có.
def display(rows):
    # Process each element of the input collection in order.
    for item in rows:
        # Show a human-readable result to the learner.
        print(f"{item['student_id']} | {item['name']} | {item['class_name']} | average={average_grade(item):.2f}/100")

# Function: Write a well-formed temporary CSV then atomically replace the destination.
```

### Giải thích quy trình giải và công thức

`csv.DictReader` đọc bảng dựa trên tên cột. `Path` trỏ đúng file cạnh chương trình; kiểm tra header và kiểm tra từng record trước khi in qua `display()`. Nếu thiếu file, dừng có thông báo thay vì trả dữ liệu bịa.

**Công thức / quy tắc:** Định dạng cột cố định: `student_id,name,class_name,Python,Math,ML`. Không có công thức.

## Bài 2

### English — Original Word requirement

**Add a New Student:** Enter student information and grades. Validate input and prevent duplicate Student IDs.

### Tiếng Việt — Bản dịch

**Thêm sinh viên:** Nhập mã, tên, lớp và điểm từng môn; kiểm tra đầu vào hợp lệ, từ chối mã trùng hoặc điểm ngoài khoảng 0–100 trước khi thêm dữ liệu vào bộ nhớ.

### Bài giải — Code đã có trong demo/giáo trình

**Nguồn:** `labs/pythoclass/LAB-10-file-csv/SOLUTION.py` / phiên bản comment `docs/labs/LAB-10-file-csv/SOLUTION_ANNOTATED.py`, hàm `validate()`, `add_student()`. `DEMO.py` là code thực hành để đối chiếu, không mặc nhiên là lời giải chuẩn của Word.

```python
# Hàm nguồn validate() từ code lời giải tham khảo hiện có.
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

# Hàm nguồn add_student() từ code lời giải tham khảo hiện có.
def add_student(rows, student):
    # Prepare this intermediate value for the next calculation or validation.
    item=validate(student)
    # Branch when this validated condition is true.
    if any(r["student_id"]==item["student_id"] for r in rows):
        raise ValueError("Duplicate student ID")
    # Add the new element to a list while retaining insertion order.
    rows.append(item)

# Function: Return the matching student record or None using an ID comparison.
```

### Giải thích quy trình giải và công thức

`validate()` buộc ba trường ID/tên/lớp không rỗng, chuyển ba điểm sang `float`, kiểm tra 0–100. `add_student()` chỉ thêm nếu mã không nằm trong danh sách. Đó là code tham khảo đã có, từ phần thực hành CSV và kiểm tra dữ liệu.

**Công thức / quy tắc:** Với mỗi môn: 0 ≤ score ≤ 100; điều kiện ID mới: không tồn tại trong các bản ghi hiện tại.

## Bài 3

### English — Original Word requirement

**Search Student by ID:** Search/display a student's information.

### Tiếng Việt — Bản dịch

**Tìm sinh viên theo mã:** Người dùng nhập ID, chương trình tìm và hiển thị bản ghi tương ứng; khi không có thì thông báo không tìm thấy.

### Bài giải — Code đã có trong demo/giáo trình

**Nguồn:** `labs/pythoclass/LAB-10-file-csv/SOLUTION.py` / phiên bản comment `docs/labs/LAB-10-file-csv/SOLUTION_ANNOTATED.py`, hàm `search_by_id()`. `DEMO.py` là code thực hành để đối chiếu, không mặc nhiên là lời giải chuẩn của Word.

```python
# Hàm nguồn search_by_id() từ code lời giải tham khảo hiện có.
def search_by_id(rows, student_id):
    # Return the result for later reuse or testing instead of only printing it.
    return next((r for r in rows if r["student_id"]==student_id.strip()),None)

# Function: Compute the average of Python, Math and ML scores for one student.
```

### Giải thích quy trình giải và công thức

Dùng ID đã được `.strip()` để tìm bản ghi đúng. `next(...,None)` trả kết quả đầu tiên, hoặc None nếu không tìm thấy; không dùng tìm tên để thay cho tìm mã.

**Công thức / quy tắc:** Quy tắc tìm kiếm: `record['student_id'] == student_id` (khớp chính xác sau khi bỏ dấu cách đầu/cuối).

## Bài 4

### English — Original Word requirement

**Calculate Average Grade:** Display each student's average grade.

### Tiếng Việt — Bản dịch

**Tính điểm trung bình:** Với mỗi sinh viên, lấy trung bình cộng các môn Python, Math và ML và hiển thị kết quả.

### Bài giải — Code đã có trong demo/giáo trình

**Nguồn:** `labs/pythoclass/LAB-10-file-csv/SOLUTION.py` / phiên bản comment `docs/labs/LAB-10-file-csv/SOLUTION_ANNOTATED.py`, hàm `average_grade()`. `DEMO.py` là code thực hành để đối chiếu, không mặc nhiên là lời giải chuẩn của Word.

```python
# Hàm nguồn average_grade() từ code lời giải tham khảo hiện có.
def average_grade(student):
    # Return the result for later reuse or testing instead of only printing it.
    return sum(student[sub] for sub in SUBJECTS)/len(SUBJECTS)

# Function: Print identity and averaged score for every student record.
```

### Giải thích quy trình giải và công thức

Đọc ba điểm đã xác thực của cùng một người, cộng và chia cho ba. Không cộng điểm của tất cả sinh viên rồi mới chia.

**Công thức / quy tắc:** Điểm trung bình = (Python + Math + ML) / 3.

## Bài 5

### English — Original Word requirement

**Save Students to File:** Save current student data to `students.csv`.

### Tiếng Việt — Bản dịch

**Lưu dữ liệu:** Ghi danh sách sinh viên hiện tại vào `students.csv` theo đúng thứ tự cột nguồn, chỉ khi người dùng chọn lưu.

### Bài giải — Code đã có trong demo/giáo trình

**Nguồn:** `labs/pythoclass/LAB-10-file-csv/SOLUTION.py` / phiên bản comment `docs/labs/LAB-10-file-csv/SOLUTION_ANNOTATED.py`, hàm `save_students()`. `DEMO.py` là code thực hành để đối chiếu, không mặc nhiên là lời giải chuẩn của Word.

```python
# Hàm nguồn save_students() từ code lời giải tham khảo hiện có.
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
```

### Giải thích quy trình giải và công thức

Dùng `csv.DictWriter` tạo header, lần lượt ghi các dòng. Script tham khảo ghi sang tệp tạm rồi `os.replace` tệp đích nếu thành công, hạn chế hỏng file khi ghi dở. Không ghi file trong chế độ `--demo`.

**Công thức / quy tắc:** Số dòng sau khi thêm = số dòng trước + 1 nếu mã duy nhất và dữ liệu hợp lệ; việc ghi không làm mất sáu cột nguồn.

## Bài 6

### English — Original Word requirement

**Exit:** Exit the program.

### Tiếng Việt — Bản dịch

**Thoát:** Cho phép rời menu của chương trình; nếu có dữ liệu thay đổi mà chưa lưu thì không âm thầm ghi ra tệp.

### Bài giải — Code đã có trong demo/giáo trình

**Nguồn:** `labs/pythoclass/LAB-10-file-csv/SOLUTION.py` / phiên bản comment `docs/labs/LAB-10-file-csv/SOLUTION_ANNOTATED.py`, hàm `main()`. `DEMO.py` là code thực hành để đối chiếu, không mặc nhiên là lời giải chuẩn của Word.

```python
# Hàm nguồn main() từ code lời giải tham khảo hiện có.
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
```

### Giải thích quy trình giải và công thức

`main()` đọc CSV, mở menu lặp và gọi đúng hàm theo lựa chọn. Người dùng chọn 0 thì kết thúc; thao tác Save ở lựa chọn 5 được thực hiện riêng để không tự ý ghi.

**Công thức / quy tắc:** Không có công thức: điều kiện dừng là lựa chọn menu Exit. Biến `dirty` theo dõi dữ liệu chưa lưu.

## Error Handling — Yêu cầu Word và bản dịch Việt

**English (original):** Handle file-not-found errors, invalid numeric input, grades outside **0–100**, and duplicate student IDs.

**Tiếng Việt:** Xử lý các lỗi không tìm thấy file, nhập điểm không phải số, điểm vượt khỏi khoảng 0–100 và mã sinh viên bị trùng. Ngoài ra file phải có đúng sáu cột như bảng nguồn, nếu thiếu cột phải báo lỗi thay vì đọc sai dữ liệu.

**Quy trình đã có trong code:** `load_students()` kiểm tra file/header, `validate()` kiểm tra điểm/chuỗi rỗng, `add_student()` chống mã trùng, `save_students()` ghi tệp tạm rồi thay thế. Vì đề cung cấp bảng 10 dòng, số liệu CSV được đặt trong tài liệu này cho người học có thể tự lưu vào `students.csv` khi luyện tập; **chỉ xuất một file Markdown cho Lab 10**.
