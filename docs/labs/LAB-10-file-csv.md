# Lab 10 — Quản lý điểm sinh viên bằng CSV

## Đề bài tiếng Anh

### LAB Session 10

#### Objective
Develop a Python program to manage student grades using **File I/O, Functions, and Error Handling**.

#### Requirements
Create a menu-driven program with these functions:

1. **Display All Students:** Read/display student data from `students.csv`.
2. **Add a New Student:** Enter student information and grades. Validate input and prevent duplicate Student IDs.
3. **Search Student by ID:** Search/display a student's information.
4. **Calculate Average Grade:** Display each student's average grade.
5. **Save Students to File:** Save current student data to `students.csv`.
6. **Exit:** Exit the program.

#### Error Handling
Handle file-not-found errors, invalid numeric input, grades outside **0–100**, and duplicate student IDs.

#### Sample `students.csv`

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

*Chuyển từ `Lab Session 10.docx` sang Markdown. Tên học viên trong dữ liệu ví dụ đã được thay bằng mã minh họa nhằm tránh công khai thông tin định danh; điểm số, lớp và cấu trúc bảng được giữ nguyên.*

## Đề bài tiếng Việt

### LAB SESSION 10 — Quản lý điểm sinh viên bằng file CSV (tệp phân cách bằng dấu phẩy)

#### Mục tiêu
Xây dựng chương trình Python quản lý điểm sinh viên bằng thao tác **File I/O**, các **hàm** và **xử lý lỗi**.

#### Các yêu cầu
Tạo chương trình có menu với sáu chức năng:

1. **Hiển thị tất cả sinh viên:** Đọc dữ liệu sinh viên từ `students.csv` và hiển thị thông tin.

2. **Thêm sinh viên:** Nhập thông tin cá nhân và điểm của từng môn; kiểm tra dữ liệu hợp lệ và chống mã sinh viên trùng.

3. **Tìm theo mã sinh viên:** Nhập mã và hiển thị thông tin của sinh viên cần tìm.

4. **Tính điểm trung bình:** In điểm trung bình từng sinh viên.

5. **Lưu vào file:** Ghi dữ liệu đang quản lý vào `students.csv`.

6. **Thoát:** Kết thúc chương trình.

#### Xử lý lỗi
Cần xử lý **không tìm thấy file**, **nhập số không hợp lệ**, **điểm ngoài phạm vi 0–100** và **mã sinh viên trùng**.

#### Dữ liệu mẫu students.csv (tệp phân cách bằng dấu phẩy)
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

## Giải thích từng câu

### Câu 1

`csv.DictReader` đọc bảng dựa trên tên cột. `Path` trỏ đúng file cạnh chương trình; kiểm tra header và kiểm tra từng record trước khi in qua `display()`. Nếu thiếu file, dừng có thông báo thay vì trả dữ liệu bịa.

**Vì sao đọc theo tên cột?** Bảng điểm có sáu trường; dùng `DictReader` giúp mỗi dòng mang tên trường rõ ràng, tránh hiểu sai vị trí cột.

**Các bước:** (1) Xác định đường dẫn CSV ở cạnh script. (2) Mở file với mã hóa phù hợp. (3) Đọc header, kiểm tra đủ tên cột. (4) Đọc từng dòng và kiểm tra dữ liệu trước khi in.
~~~python
import csv
from pathlib import Path
path = Path("students.csv")
with path.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    required = {"student_id", "name", "class_name", "Python", "Math", "ML"}
    if not required.issubset(reader.fieldnames or []):
        raise ValueError("Thiếu cột CSV")
    rows = list(reader)
~~~
**Tham số và cú pháp:** `"r"` là chế độ đọc; `encoding="utf-8"` đọc tiếng Việt; `newline=""` cho thư viện CSV tự xử lý xuống dòng; `DictReader` tạo từng dictionary theo tên cột; `issubset` kiểm tra đủ trường bắt buộc; `list(reader)` gom các hàng. Nếu thiếu file, cần báo `FileNotFoundError` thay vì tự tạo dữ liệu không có trong nguồn.

**Chi tiết kiểm tra:** Đọc tệp bằng `csv.DictReader`; đối chiếu tiêu đề phải đủ sáu cột; mỗi hàng được chuyển thành dict, cần xử lý `FileNotFoundError` rõ ràng.

**Ví dụ/lỗi thường gặp:** DictReader đọc từng hàng dựa vào tên cột, cần kiểm tra đủ sáu cột và xử lý file không tồn tại.

**Từ vựng chính:** Display (hiển thị).

### Câu 2

`validate()` buộc ba trường ID/tên/lớp không rỗng, chuyển ba điểm sang `float`, kiểm tra 0–100. `add_student()` chỉ thêm nếu mã không nằm trong danh sách. Đó là code tham khảo đã có, từ phần thực hành CSV (tệp phân cách bằng dấu phẩy) và kiểm tra dữ liệu.

**Vì sao phải kiểm tra trước khi thêm?** ID là định danh duy nhất. Nếu thêm ID đã tồn tại hoặc điểm không hợp lệ, kết quả tìm kiếm và thống kê sẽ sai.

**Các bước:** (1) Nhập ID, tên, lớp, ba điểm. (2) Bỏ khoảng trắng đầu/cuối, chuyển điểm sang số thực. (3) Kiểm tra điểm trong khoảng 0–100. (4) Tìm ID cũ trước khi chèn; nếu đã có thì báo lỗi.
~~~python
student_id = "S011".strip()
scores = {"Python": 85.0, "Math": 90.0, "ML": 88.0}
valid_scores = all(0 <= grade <= 100 for grade in scores.values())
duplicate = any(row["student_id"] == student_id for row in rows)
if not student_id or not valid_scores or duplicate:
    raise ValueError("ID hoặc điểm không hợp lệ, hoặc ID bị trùng")
~~~
**Cú pháp và toán tử:** `.strip()` bỏ khoảng trắng; `float(...)` chuyển chuỗi điểm thành số; `all(...)` chỉ đúng nếu **mọi** điểm hợp lệ; `any(...)` đúng nếu có **ít nhất một** bản ghi trùng; `<=` so sánh biên; `or` là hoặc, `not` là phủ định. Đây là quy tắc dữ liệu của code, không phải tự phát sinh từ CSV.

**Chi tiết kiểm tra:** `validate` loại bỏ chuỗi rỗng, chuyển 3 điểm thành `float` và kiểm tra `0 ≤ score ≤ 100`. Kiểm tra `student_id` mới không trùng trước khi thêm.

**Ví dụ/lỗi thường gặp:** Trước khi thêm, phải kiểm tra mã duy nhất, trường tên/lớp không rỗng và ba điểm nằm trong [0,100].

**Từ vựng chính:** Add (thêm).

### Câu 3

Dùng ID đã được `.strip()` để tìm bản ghi đúng. `next(...,None)` trả kết quả đầu tiên, hoặc None nếu không tìm thấy; không dùng tìm tên để thay cho tìm mã.

**Vì sao tìm đúng ID thay vì tìm gần giống?** ID là khóa duy nhất, nên tìm chính xác giúp tránh nhầm S01 với S010 hoặc hai sinh viên có cùng tên.

**Các bước:** (1) Nhận ID cần tìm và bỏ khoảng trắng. (2) Duyệt các dòng. (3) So sánh chuỗi ID bằng `==`. (4) Trả bản ghi đầu tiên khớp hoặc trả `None` nếu không có.
~~~python
query = "S003".strip()
found = next((row for row in rows if row["student_id"] == query), None)
~~~
**Cú pháp:** `==` so sánh bằng, không phải gán; `next(iterator, None)` lấy phần tử đầu thỏa điều kiện, trả `None` khi không có; `row["student_id"]` truy cập cột theo tên. Trước khi tìm phải thống nhất cách lưu ID (hoa/thường theo yêu cầu), không tự suy đoán bản ghi.

**Chi tiết kiểm tra:** Tìm ID sau khi `strip()` qua các dòng, trả bản ghi trùng mã hoặc `None` nếu không có; tránh tìm bằng tên thay cho mã.

**Ví dụ/lỗi thường gặp:** strip() xóa khoảng trắng không cần thiết; tìm theo student_id, trả None nếu không có sinh viên phù hợp.

**Từ vựng chính:** Search (tìm kiếm).

### Câu 4

Đọc ba điểm đã xác thực của cùng một người, cộng và chia cho ba. Không cộng điểm của tất cả sinh viên rồi mới chia.

**Vì sao tính trung bình từng sinh viên?** Đề yêu cầu tổng hợp ba môn của **mỗi người**, nên không cộng điểm của mọi sinh viên với nhau.

**Các bước:** (1) Lấy ba điểm Python, Math, ML của cùng một hàng. (2) Đổi về số thực khi đọc CSV. (3) Cộng ba điểm, chia số môn. (4) In trung bình với số chữ số thập phân phù hợp.
~~~python
subject_names = ["Python", "Math", "ML"]
grades = [float(student[name]) for name in subject_names]
average = sum(grades) / len(subject_names)
print(f"{average:.2f}")
~~~
**Cú pháp và flag:** `sum` cộng điểm; `len` đếm số môn (3); `/` chia thực; `float` tránh cộng chuỗi. `:.2f` trong f-string chỉ **hiển thị hai chữ số thập phân**, không làm thay đổi giá trị `average` dùng ở các phép tính khác.

**Chi tiết kiểm tra:** Điểm trung bình sinh viên = (điểm Python + điểm Math + điểm ML)/3. Chỉ tính trên các môn của cùng một sinh viên.

**Ví dụ/lỗi thường gặp:** Điểm trung bình mỗi người bằng (Python+Math+ML)/3. Không nhầm tổng điểm lớp với trung bình một người.

**Từ vựng chính:** Average (trung bình).

### Câu 5

Dùng `csv.DictWriter` tạo header, lần lượt ghi các dòng. Script tham khảo ghi sang tệp tạm rồi `os.replace` tệp đích nếu thành công, hạn chế hỏng file khi ghi dở. Không ghi file trong chế độ `--demo`.

**Vì sao lưu qua file tạm?** Nếu đang ghi mà xảy ra lỗi, ghi trực tiếp có nguy cơ làm hỏng dữ liệu cũ. Ghi file tạm trước rồi thay thế khi hoàn tất là cách giảm rủi ro.

**Các bước:** (1) Xác thực toàn bộ các dòng. (2) Tạo file tạm trong cùng thư mục đích. (3) Ghi đúng sáu tên cột và từng bản ghi bằng `DictWriter`. (4) Đóng file, dùng `os.replace` thay file đích; xử lý lỗi và xóa file tạm chưa dùng.
~~~python
with open("students_example.csv", "w", encoding="utf-8", newline="") as out:
    writer = csv.DictWriter(out, fieldnames=FIELDS)
    writer.writeheader()
    for row in rows:
        writer.writerow(validate(row))
# Code cuối bài dùng file tạm và os.replace thay vì ghi trực tiếp như ví dụ nhỏ này.
~~~
**Flag và tham số quan trọng của code cuối bài:** `fieldnames=FIELDS` bắt buộc thứ tự cột; `writeheader()` ghi dòng tiêu đề; `writerow` ghi một hàng. `NamedTemporaryFile(mode="w", encoding="utf-8", newline="", dir=path.parent, delete=False)` tạo file tạm trong cùng thư mục; `delete=False` để file còn tồn tại cho `os.replace` sau khi đóng. `path.parent.mkdir(parents=True, exist_ok=True)` tạo thư mục thiếu, không báo lỗi khi đã tồn tại. Chỉ lưu khi người dùng chọn chức năng Save.

**Chi tiết kiểm tra:** Ghi header bằng `csv.DictWriter`, tạo file tạm và `os.replace` khi hoàn tất để tránh ghi dở; chỉ lưu khi chọn chức năng 5.

**Ví dụ/lỗi thường gặp:** DictWriter giữ đúng các cột nguồn; ghi vào file tạm xong mới thay file đích bằng os.replace().

**Từ vựng chính:** Save (lưu).

### Câu 6

`main()` đọc CSV (tệp phân cách bằng dấu phẩy), mở menu lặp và gọi đúng hàm theo lựa chọn. Người dùng chọn 0 thì kết thúc; thao tác Save ở lựa chọn 5 được thực hiện riêng để không tự ý ghi.

**Vì sao tách Exit khỏi Save?** Người dùng có thể đang xem hoặc chỉnh dữ liệu; thoát không đồng nghĩa tự ý ghi đè file. Menu phải kiểm soát trạng thái thay đổi và cho người dùng quyết định.

**Các bước:** (1) Hiển thị menu trong vòng lặp. (2) Dựa vào lựa chọn để gọi hàm tương ứng. (3) Khi thêm/sửa thì đánh dấu `dirty=True`. (4) Khi Save thành công đặt lại `dirty=False`. (5) Khi Exit, cảnh báo nếu còn dữ liệu chưa lưu rồi dừng.
~~~python
dirty = True
choice = "0"
if choice == "0":
    if dirty:
        print("Có thay đổi chưa lưu")
    print("Chọn Exit từ menu")
~~~
**Cú pháp:** `==` là so sánh lựa chọn; `if` chỉ chạy khi điều kiện đúng; `dirty` là biến Boolean (đúng/sai) cho biết đã thay đổi dữ liệu trong bộ nhớ chưa được ghi xuống CSV. `break` dừng vòng lặp `while True` trong hàm menu. Không dùng phép tính trung bình để quyết định Exit.

**Chi tiết kiểm tra:** Menu chạy trong `while True`; lựa chọn Exit sẽ dừng mà không ghi file ngoài ý muốn; kiểm tra và thông báo khi người dùng có thay đổi chưa lưu.

**Lưu ý chạy thực tế:** Code đọc `students.csv` bên cạnh file Python. Nếu dùng tài liệu một-file-này để học, sao chép nguyên bảng CSV bên trên vào file `students.csv` trước khi chạy menu. Không có file CSV xuất bản riêng trong `docs/labs`, đúng yêu cầu một lab = một tài liệu.

**Ví dụ/lỗi thường gặp:** Menu (bảng chọn) hoạt động đến Exit. Phân biệt dữ liệu trong bộ nhớ và file đã lưu để tránh mất thay đổi.

**Từ vựng chính:** Exit (thoát).


## Code Python

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
