# LAB-10-file-csv — nguyên đề Anh, toàn bộ dịch Việt, hướng giải và code có note

**Nguồn:** `Lab Session 10.docx` đã được chuyển sang `labs/pythoclass/LAB-10-file-csv/LAB.md`; code nguyên chương trình từ bản chú thích `SOLUTION_ANNOTATED.py` lưu trong lịch sử repo, xây trên `labs/pythoclass/LAB-10-file-csv/SOLUTION.py`, đối chiếu `DEMO.py`. Không thay thuật toán. Tài liệu này không chia lời giải ra từng câu.

---

## ĐỀ BÀI SONG NGỮ — MỖI CÂU ENGLISH / TIẾNG VIỆT / GIẢI THÍCH

**Cách học:** Đọc yêu cầu tiếng Anh (English: tiếng Anh), xem bản dịch tiếng Việt ngay bên dưới, rồi tới giải thích/công thức. Các thuật ngữ quan trọng có nghĩa tiếng Việt trong ngoặc.

### Bối cảnh và dữ liệu — Original English

# LAB Session 10

## Objective
Develop a Python program to manage student grades using **File I/O, Functions, and Error Handling**.

## Requirements
Create a menu-driven program with these functions:

### Bối cảnh và dữ liệu — Tiếng Việt

# LAB SESSION 10 — Quản lý điểm sinh viên bằng file CSV (tệp phân cách bằng dấu phẩy)

## Mục tiêu
Xây dựng chương trình Python quản lý điểm sinh viên bằng thao tác **File I/O**, các **hàm** và **xử lý lỗi**.

## Các yêu cầu
Tạo chương trình có menu với sáu chức năng:

### Câu 1 — English → Tiếng Việt → Giải thích

**English — Nguyên đề:**

1. **Display All Students:** Read/display student data from `students.csv`.

**Tiếng Việt — Dịch ngay dưới đề Anh:**

1. **Hiển thị tất cả sinh viên:** Đọc dữ liệu sinh viên từ `students.csv` và hiển thị thông tin.

**Giải thích từng bước và công thức:**

`csv.DictReader` đọc bảng dựa trên tên cột. `Path` trỏ đúng file cạnh chương trình; kiểm tra header và kiểm tra từng record trước khi in qua `display()`. Nếu thiếu file, dừng có thông báo thay vì trả dữ liệu bịa.

**Công thức / quy tắc:** Định dạng cột cố định: `student_id,name,class_name,Python,Math,ML`. Không có công thức.

**Chi tiết kiểm tra:** Đọc tệp bằng `csv.DictReader`; đối chiếu tiêu đề phải đủ sáu cột; mỗi hàng được chuyển thành dict, cần xử lý `FileNotFoundError` rõ ràng.

**Ví dụ/lỗi thường gặp:** DictReader đọc từng hàng dựa vào tên cột, cần kiểm tra đủ sáu cột và xử lý file không tồn tại.

**Từ vựng chính:** Display (hiển thị).

### Câu 2 — English → Tiếng Việt → Giải thích

**English — Nguyên đề:**

2. **Add a New Student:** Enter student information and grades. Validate input and prevent duplicate Student IDs.

**Tiếng Việt — Dịch ngay dưới đề Anh:**

2. **Thêm sinh viên:** Nhập thông tin cá nhân và điểm của từng môn; kiểm tra dữ liệu hợp lệ và chống mã sinh viên trùng.

**Giải thích từng bước và công thức:**

`validate()` buộc ba trường ID/tên/lớp không rỗng, chuyển ba điểm sang `float`, kiểm tra 0–100. `add_student()` chỉ thêm nếu mã không nằm trong danh sách. Đó là code tham khảo đã có, từ phần thực hành CSV (tệp phân cách bằng dấu phẩy) và kiểm tra dữ liệu.

**Công thức / quy tắc:** Với mỗi môn: 0 ≤ score (điểm số) ≤ 100; điều kiện ID mới: không tồn tại trong các bản ghi hiện tại.

**Chi tiết kiểm tra:** `validate` loại bỏ chuỗi rỗng, chuyển 3 điểm thành `float` và kiểm tra `0 ≤ score ≤ 100`. Kiểm tra `student_id` mới không trùng trước khi thêm.

**Ví dụ/lỗi thường gặp:** Trước khi thêm, phải kiểm tra mã duy nhất, trường tên/lớp không rỗng và ba điểm nằm trong [0,100].

**Từ vựng chính:** Add (thêm).

### Câu 3 — English → Tiếng Việt → Giải thích

**English — Nguyên đề:**

3. **Search Student by ID:** Search/display a student's information.

**Tiếng Việt — Dịch ngay dưới đề Anh:**

3. **Tìm theo mã sinh viên:** Nhập mã và hiển thị thông tin của sinh viên cần tìm.

**Giải thích từng bước và công thức:**

Dùng ID đã được `.strip()` để tìm bản ghi đúng. `next(...,None)` trả kết quả đầu tiên, hoặc None nếu không tìm thấy; không dùng tìm tên để thay cho tìm mã.

**Công thức / quy tắc:** Quy tắc tìm kiếm: `record['student_id'] == student_id` (khớp chính xác sau khi bỏ dấu cách đầu/cuối).

**Chi tiết kiểm tra:** Tìm ID sau khi `strip()` qua các dòng, trả bản ghi trùng mã hoặc `None` nếu không có; tránh tìm bằng tên thay cho mã.

**Ví dụ/lỗi thường gặp:** strip() xóa khoảng trắng không cần thiết; tìm theo student_id, trả None nếu không có sinh viên phù hợp.

**Từ vựng chính:** Search (tìm kiếm).

### Câu 4 — English → Tiếng Việt → Giải thích

**English — Nguyên đề:**

4. **Calculate Average Grade:** Display each student's average grade.

**Tiếng Việt — Dịch ngay dưới đề Anh:**

4. **Tính điểm trung bình:** In điểm trung bình từng sinh viên.

**Giải thích từng bước và công thức:**

Đọc ba điểm đã xác thực của cùng một người, cộng và chia cho ba. Không cộng điểm của tất cả sinh viên rồi mới chia.

**Công thức / quy tắc:** Điểm trung bình = (Python + Math + ML) / 3.

**Chi tiết kiểm tra:** Điểm trung bình sinh viên = (điểm Python + điểm Math + điểm ML)/3. Chỉ tính trên các môn của cùng một sinh viên.

**Ví dụ/lỗi thường gặp:** Điểm trung bình mỗi người bằng (Python+Math+ML)/3. Không nhầm tổng điểm lớp với trung bình một người.

**Từ vựng chính:** Average (trung bình).

### Câu 5 — English → Tiếng Việt → Giải thích

**English — Nguyên đề:**

5. **Save Students to File:** Save current student data to `students.csv`.

**Tiếng Việt — Dịch ngay dưới đề Anh:**

5. **Lưu vào file:** Ghi dữ liệu đang quản lý vào `students.csv`.

**Giải thích từng bước và công thức:**

Dùng `csv.DictWriter` tạo header, lần lượt ghi các dòng. Script tham khảo ghi sang tệp tạm rồi `os.replace` tệp đích nếu thành công, hạn chế hỏng file khi ghi dở. Không ghi file trong chế độ `--demo`.

**Công thức / quy tắc:** Số dòng sau khi thêm = số dòng trước + 1 nếu mã duy nhất và dữ liệu hợp lệ; việc ghi không làm mất sáu cột nguồn.

**Chi tiết kiểm tra:** Ghi header bằng `csv.DictWriter`, tạo file tạm và `os.replace` khi hoàn tất để tránh ghi dở; chỉ lưu khi chọn chức năng 5.

**Ví dụ/lỗi thường gặp:** DictWriter giữ đúng các cột nguồn; ghi vào file tạm xong mới thay file đích bằng os.replace().

**Từ vựng chính:** Save (lưu).

### Câu 6 — English → Tiếng Việt → Giải thích

**English — Nguyên đề:**

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

**Tiếng Việt — Dịch ngay dưới đề Anh:**

6. **Thoát:** Kết thúc chương trình.

## Xử lý lỗi
Cần xử lý **không tìm thấy file**, **nhập số không hợp lệ**, **điểm ngoài phạm vi 0–100** và **mã sinh viên trùng**.

## Dữ liệu mẫu students.csv (tệp phân cách bằng dấu phẩy)
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

**Giải thích từng bước và công thức:**

`main()` đọc CSV (tệp phân cách bằng dấu phẩy), mở menu lặp và gọi đúng hàm theo lựa chọn. Người dùng chọn 0 thì kết thúc; thao tác Save ở lựa chọn 5 được thực hiện riêng để không tự ý ghi.

**Công thức / quy tắc:** Không có công thức: điều kiện dừng là lựa chọn menu Exit. Biến `dirty` theo dõi dữ liệu chưa lưu.

**Chi tiết kiểm tra:** Menu chạy trong `while True`; lựa chọn Exit sẽ dừng mà không ghi file ngoài ý muốn; kiểm tra và thông báo khi người dùng có thay đổi chưa lưu.

**Lưu ý chạy thực tế:** Code đọc `students.csv` bên cạnh file Python. Nếu dùng tài liệu một-file-này để học, sao chép nguyên bảng CSV bên trên vào file `students.csv` trước khi chạy menu. Không có file CSV xuất bản riêng trong `docs/labs`, đúng yêu cầu một lab = một tài liệu.

**Ví dụ/lỗi thường gặp:** Menu (bảng chọn) hoạt động đến Exit. Phân biệt dữ liệu trong bộ nhớ và file đã lưu để tránh mất thay đổi.

**Từ vựng chính:** Exit (thoát).

---

## TOÀN BỘ CODE PYTHON — CHÚ THÍCH NGAY SAU TỪNG DÒNG

**Hướng dẫn:** Chú thích nằm cùng dòng, sau câu lệnh và dấu `#`; không đặt comment riêng trên dòng phía trước. Các câu lệnh kiểm tra dùng `if` (nếu) và `raise ValueError` (báo lỗi dữ liệu), không dùng `assert`. Thuật toán và số liệu giữ như code đã học, các dòng trắng chỉ chia nhóm lệnh.

```python
import csv  # Nạp thư viện (import: nạp vào) để có các hàm đã học.
import os  # Nạp thư viện (import: nạp vào) để có các hàm đã học.
from pathlib import Path  # Nạp thư viện (import: nạp vào) để có các hàm đã học.
import sys  # Nạp thư viện (import: nạp vào) để có các hàm đã học.
import tempfile  # Nạp thư viện (import: nạp vào) để có các hàm đã học.

CSV_PATH=Path(__file__).resolve().parent/"students.csv"  # Tính hoặc cập nhật biến CSV_PATH từ công thức bên phải.
FIELDS=["student_id","name","class_name","Python","Math","ML"]  # Tính hoặc cập nhật biến FIELDS từ công thức bên phải.
SUBJECTS=["Python","Math","ML"]  # Tính hoặc cập nhật biến SUBJECTS từ công thức bên phải.

def validate(student):  # Định nghĩa hàm (function: hàm) để gom và gọi lại các bước.
    sid=str(student.get("student_id","")).strip()  # Loại bỏ khoảng trắng đầu và cuối.
    name=str(student.get("name","")).strip()  # Loại bỏ khoảng trắng đầu và cuối.
    cls=str(student.get("class_name","")).strip()  # Loại bỏ khoảng trắng đầu và cuối.
    if not sid or not name or not cls: raise ValueError("ID, name and class are required")  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
    result={"student_id":sid,"name":name,"class_name":cls}  # Tính hoặc cập nhật biến result từ công thức bên phải.
    for sub in SUBJECTS:  # Duyệt từng phần tử qua vòng lặp (loop: vòng lặp).
        try: score=float(student[sub])  # Thử thao tác có khả năng gây lỗi.
        except (ValueError,KeyError,TypeError) as exc: raise ValueError(f"{sub} grade must be numeric") from exc  # Bắt lỗi ngoại lệ (exception: lỗi) để báo rõ.
        if not 0<=score<=100: raise ValueError(f"{sub} grade outside 0..100")  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
        result[sub]=score  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
    return result  # Trả kết quả (return: trả về) cho nơi gọi hàm.

def load_students(path=CSV_PATH):  # Định nghĩa hàm (function: hàm) để gom và gọi lại các bước.
    if not Path(path).exists():  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
        raise FileNotFoundError(f"Missing data file: {path}")  # Báo lỗi khi đầu vào không hợp lệ.
    with Path(path).open("r",encoding="utf-8",newline="") as f:  # Quản lý file an toàn và tự đóng sau khi sử dụng.
        reader=csv.DictReader(f)  # Đọc file theo tên cột hoặc nội dung.
        if reader.fieldnames != FIELDS:  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
            raise ValueError(f"Unexpected columns, expected {FIELDS}")  # Báo lỗi khi đầu vào không hợp lệ.
        rows=[validate(r) for r in reader]  # Tính hoặc cập nhật biến rows từ công thức bên phải.
    ids=[r["student_id"] for r in rows]  # Tính hoặc cập nhật biến ids từ công thức bên phải.
    if len(ids)!=len(set(ids)): raise ValueError("Duplicate student IDs already in CSV")  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
    return rows  # Trả kết quả (return: trả về) cho nơi gọi hàm.

def add_student(rows, student):  # Định nghĩa hàm (function: hàm) để gom và gọi lại các bước.
    item=validate(student)  # Tính hoặc cập nhật biến item từ công thức bên phải.
    if any(r["student_id"]==item["student_id"] for r in rows):  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
        raise ValueError("Duplicate student ID")  # Báo lỗi khi đầu vào không hợp lệ.
    rows.append(item)  # Thêm phần tử vào cuối danh sách.

def search_by_id(rows, student_id):  # Định nghĩa hàm (function: hàm) để gom và gọi lại các bước.
    return next((r for r in rows if r["student_id"]==student_id.strip()),None)  # Trả kết quả (return: trả về) cho nơi gọi hàm.

def average_grade(student):  # Định nghĩa hàm (function: hàm) để gom và gọi lại các bước.
    return sum(student[sub] for sub in SUBJECTS)/len(SUBJECTS)  # Trả kết quả (return: trả về) cho nơi gọi hàm.

def display(rows):  # Định nghĩa hàm (function: hàm) để gom và gọi lại các bước.
    for item in rows:  # Duyệt từng phần tử qua vòng lặp (loop: vòng lặp).
        print(f"{item['student_id']} | {item['name']} | {item['class_name']} | average={average_grade(item):.2f}/100")  # In kết quả (output: kết quả) để đối chiếu với đề.

def save_students(rows, path=CSV_PATH):  # Định nghĩa hàm (function: hàm) để gom và gọi lại các bước.
    path=Path(path)  # Tính hoặc cập nhật biến path từ công thức bên phải.
    path.parent.mkdir(parents=True,exist_ok=True)  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
    tmp=None  # Tính hoặc cập nhật biến tmp từ công thức bên phải.
    try:  # Thử thao tác có khả năng gây lỗi.
        with tempfile.NamedTemporaryFile(mode="w",encoding="utf-8",newline="",dir=path.parent,  # Quản lý file an toàn và tự đóng sau khi sử dụng.
                                         prefix=".students-",suffix=".csv",delete=False) as out:  # Tính hoặc cập nhật biến prefix từ công thức bên phải.
            tmp=Path(out.name)  # Tính hoặc cập nhật biến tmp từ công thức bên phải.
            writer=csv.DictWriter(out,fieldnames=FIELDS)  # Tính hoặc cập nhật biến writer từ công thức bên phải.
            writer.writeheader()  # Ghi dữ liệu và lưu file (save: lưu) an toàn.
            for row in rows: writer.writerow(validate(row))  # Duyệt từng phần tử qua vòng lặp (loop: vòng lặp).
        os.replace(tmp,path)  # Ghi dữ liệu và lưu file (save: lưu) an toàn.
    finally:  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
        if tmp is not None and tmp.exists(): tmp.unlink()  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.

def run_demo():  # Định nghĩa hàm (function: hàm) để gom và gọi lại các bước.
    rows=load_students()  # Tính hoặc cập nhật biến rows từ công thức bên phải.
    if not (len(rows)==10): raise ValueError("Kiểm tra không đạt")  # Kiểm tra bằng if (nếu), báo lỗi nếu kết quả không phù hợp.
    add_student(rows,{"student_id":"S011","name":"Learner 11","class_name":"AI04",  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
                      "Python":90,"Math":88,"ML":91})  # Gắn khóa (key: tên trường) với giá trị trong từ điển.
    if not (len(rows)==11): raise ValueError("Kiểm tra không đạt")  # Kiểm tra bằng if (nếu), báo lỗi nếu kết quả không phù hợp.
    if not (abs(average_grade(search_by_id(rows,"S011"))-269/3)<1e-9): raise ValueError("Kiểm tra không đạt")  # Kiểm tra bằng if (nếu), báo lỗi nếu kết quả không phù hợp.
    try:  # Thử thao tác có khả năng gây lỗi.
        add_student(rows,{"student_id":"S011","name":"Duplicate","class_name":"AI04",  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
                          "Python":90,"Math":88,"ML":91})  # Gắn khóa (key: tên trường) với giá trị trong từ điển.
        raise AssertionError("Duplicate check failed")  # Báo lỗi khi đầu vào không hợp lệ.
    except ValueError: pass  # Bắt lỗi ngoại lệ (exception: lỗi) để báo rõ.
    print("PASS: CSV read, search, add, duplicate detection and average")  # In kết quả (output: kết quả) để đối chiếu với đề.
    display(rows[:3])  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
    print("(Demo does not overwrite students.csv)")  # In kết quả (output: kết quả) để đối chiếu với đề.

def main():  # Định nghĩa hàm (function: hàm) để gom và gọi lại các bước.
    try: rows=load_students()  # Thử thao tác có khả năng gây lỗi.
    except (OSError,ValueError,csv.Error) as exc:  # Bắt lỗi ngoại lệ (exception: lỗi) để báo rõ.
        print("Cannot open students.csv:",exc)  # In kết quả (output: kết quả) để đối chiếu với đề.
        return  # Trả kết quả (return: trả về) cho nơi gọi hàm.
    dirty=False  # Tính hoặc cập nhật biến dirty từ công thức bên phải.
    while True:  # Tiếp tục lặp cho đến khi điều kiện dừng.
        print("\n1.Display 2.Add 3.Search ID 4.Averages 5.Save 0.Exit")  # In kết quả (output: kết quả) để đối chiếu với đề.
        choice=input("Choose: ").strip()  # Loại bỏ khoảng trắng đầu và cuối.
        try:  # Thử thao tác có khả năng gây lỗi.
            if choice=="0":  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
                if dirty: print("Unsaved changes are discarded. Select 5 to save next time.")  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
                break  # Thoát vòng lặp tại đây.
            if choice=="1": display(rows)  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
            elif choice=="2":  # Kiểm tra điều kiện thay thế khi nhánh trước không đúng.
                record={"student_id":input("ID: "),"name":input("Name: "),  # Nhận input (dữ liệu nhập) từ người dùng.
                        "class_name":input("Class: ")}  # Gắn khóa (key: tên trường) với giá trị trong từ điển.
                for subject in SUBJECTS: record[subject]=input(f"{subject} grade [0,100]: ")  # Duyệt từng phần tử qua vòng lặp (loop: vòng lặp).
                add_student(rows,record)  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
                dirty=True  # Tính hoặc cập nhật biến dirty từ công thức bên phải.
                print("Student added (not yet saved).")  # In kết quả (output: kết quả) để đối chiếu với đề.
            elif choice=="3":  # Kiểm tra điều kiện thay thế khi nhánh trước không đúng.
                print(search_by_id(rows,input("Student ID: ")) or "Not found")  # In kết quả (output: kết quả) để đối chiếu với đề.
            elif choice=="4":  # Kiểm tra điều kiện thay thế khi nhánh trước không đúng.
                for row in rows:print(row["student_id"],round(average_grade(row),2))  # Duyệt từng phần tử qua vòng lặp (loop: vòng lặp).
            elif choice=="5":  # Kiểm tra điều kiện thay thế khi nhánh trước không đúng.
                save_students(rows)  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
                dirty=False  # Tính hoặc cập nhật biến dirty từ công thức bên phải.
                print("Saved",CSV_PATH)  # In kết quả (output: kết quả) để đối chiếu với đề.
            else: print("Unknown option")  # Thực hiện trường hợp còn lại.
        except (OSError,ValueError,KeyError) as exc:  # Bắt lỗi ngoại lệ (exception: lỗi) để báo rõ.
            print("Error:",exc)  # In kết quả (output: kết quả) để đối chiếu với đề.
if __name__=="__main__":  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
    run_demo() if "--demo" in sys.argv else main()  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
```
