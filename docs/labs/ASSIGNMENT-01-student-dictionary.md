# Assignment 01 — Quản lý sinh viên bằng Dictionary

**Tương ứng một file Word:** `Ass 1.docx`. Đây là **một tài liệu duy nhất** kết hợp đề gốc tiếng Anh, bản dịch tiếng Việt, mã đã có và giải thích dưới mã. Đề lấy từ bản chép `labs/pythoclass/ASSIGNMENT-01-student-dictionary/LAB.md`. Code dưới đây trích từ `docs/labs/ASSIGNMENT-01-student-dictionary/SOLUTION_ANNOTATED.py` (bản chú thích của `labs/pythoclass/ASSIGNMENT-01-student-dictionary/SOLUTION.py`), đối chiếu `DEMO.py` và giáo trình **PY-08 / PY-09 / PY-44**. Những hàm là các phần cùng một chương trình: cần đặt chung trong một file Python để chạy hoàn chỉnh.

**English objective (from Word transcription):** Develop a menu-driven Python program to manage student information using a dictionary data structure and functions.

**Dịch tiếng Việt:** Xây dựng chương trình Python có menu quản lý sinh viên, sử dụng từ điển và các hàm để tổ chức thao tác.

**Quy ước:** Điểm từ 0 đến 10 và dữ liệu tên giả lập là cách triển khai của code tham khảo; không coi đây là các quy định mới trong đề Word.

## Bài 1

### English — Original requirement

**Data Structure:** Store students in a dictionary. Each student includes: `id`, `name`, `score`.

### Tiếng Việt — Bản dịch

**Cấu trúc dữ liệu:** Tạo chương trình lưu sinh viên bằng `dictionary`; mỗi sinh viên có mã `id`, tên `name`, điểm `score`.

### Bài giải — Code từ tài liệu đã có

Code thực hành gốc: `labs/pythoclass/ASSIGNMENT-01-student-dictionary/DEMO.py`; hàm hoàn chỉnh: `docs/labs/ASSIGNMENT-01-student-dictionary/SOLUTION_ANNOTATED.py`. Hàm áp dụng: `sample_students()`.

```python
def sample_students():
    """Generate synthetic demo names rather than real student identities."""
    scores = [9.5, 8, 7.5, 6, 5.5, 4.5, 7, 9, 8.5, 6.5, 10, 5]
    students = {}
    for number, score in enumerate(scores, start=1):
        add(students, f"S{number:03d}", f"Learner {number:02d}", score)
    return students
```

### Giải thích quy trình giải và công thức

Dùng `dict` lồng nhau: khóa ngoài là ID duy nhất, giá trị là đối tượng có `name` và `score`. Hàm tạo dữ liệu giả lập để tránh thông tin cá nhân.

**Công thức / quy tắc:** Không có công thức; truy cập theo `students[id]` có độ phức tạp trung bình O(1).

## Bài 2

### English — Original requirement

**Create (Add student):** Input student information. Check for duplicate ID before adding.

### Tiếng Việt — Bản dịch

**Thêm sinh viên:** Nhập thông tin; trước khi thêm phải kiểm tra mã sinh viên đã tồn tại hay chưa.

### Bài giải — Code từ tài liệu đã có

Code thực hành gốc: `labs/pythoclass/ASSIGNMENT-01-student-dictionary/DEMO.py`; hàm hoàn chỉnh: `docs/labs/ASSIGNMENT-01-student-dictionary/SOLUTION_ANNOTATED.py`. Hàm áp dụng: `add()`.

```python
def add(students, student_id, name, score):
    """Create a dictionary entry while preventing duplicate IDs."""
    student_id, name, score = validate(student_id, name, score)
    if student_id in students:  # Dictionary keys are unique identifiers.
        raise ValueError(f"Duplicate student ID: {student_id}")
    # Nested dictionary gives named fields instead of brittle list offsets.
    students[student_id] = {"name": name, "score": score}
```

### Giải thích quy trình giải và công thức

Đọc các trường, chuẩn hóa bằng `.strip()`, đổi điểm bằng `float()`, kiểm tra miền 0–10, rồi kiểm tra ID chưa có trước khi thêm.

**Công thức / quy tắc:** Điểm hợp lệ: 0 ≤ score ≤ 10; điều kiện tồn tại ID: `id in students`.

## Bài 3

### English — Original requirement

**Read (Display students):** Show all students in the system.

### Tiếng Việt — Bản dịch

**Hiển thị:** Xuất toàn bộ sinh viên đang được quản lý.

### Bài giải — Code từ tài liệu đã có

Code thực hành gốc: `labs/pythoclass/ASSIGNMENT-01-student-dictionary/DEMO.py`; hàm hoàn chỉnh: `docs/labs/ASSIGNMENT-01-student-dictionary/SOLUTION_ANNOTATED.py`. Hàm áp dụng: `display()`.

```python
def display(students):
    """Read: list all records including score and academic category."""
    if not students:
        print("No students stored.")  # Handle an empty dataset gracefully.
    for student_id, record in students.items():  # Traverse key/value pairs.
        print(f"{student_id} | {record['name']} | "
              f"{record['score']:g}/10 | {classify(record['score'])}")
```

### Giải thích quy trình giải và công thức

Duyệt `.items()` để lấy cặp ID–thông tin và in nội dung. Giữ nguyên thứ tự thêm vào của từ điển.

**Công thức / quy tắc:** Không có công thức; dùng lặp `for` thay vì ép người học tự hình dung cấu trúc.

## Bài 4

### English — Original requirement

**Update student:** Update student information based on ID.

### Tiếng Việt — Bản dịch

**Cập nhật:** Tìm sinh viên theo mã và sửa thông tin.

### Bài giải — Code từ tài liệu đã có

Code thực hành gốc: `labs/pythoclass/ASSIGNMENT-01-student-dictionary/DEMO.py`; hàm hoàn chỉnh: `docs/labs/ASSIGNMENT-01-student-dictionary/SOLUTION_ANNOTATED.py`. Hàm áp dụng: `update()`.

```python
def update(students, student_id, new_name, new_score):
    """Update a student by ID without silently creating new records."""
    if student_id not in students:
        raise KeyError(f"Unknown student ID: {student_id}")
    _, name, score = validate(student_id, new_name, new_score)
    students[student_id] = {"name": name, "score": score}
```

### Giải thích quy trình giải và công thức

Từ ID đầu vào, tìm đúng khóa; từ chối ID không tồn tại, xác thực giá trị mới trước khi thay thế.

**Công thức / quy tắc:** Điểm chỉ được cập nhật nếu `0 ≤ score ≤ 10`.

## Bài 5

### English — Original requirement

**Delete student:** Delete a student by ID. Require confirmation before deletion.

### Tiếng Việt — Bản dịch

**Xóa:** Xác định sinh viên theo mã, chỉ xóa sau khi người dùng xác nhận.

### Bài giải — Code từ tài liệu đã có

Code thực hành gốc: `labs/pythoclass/ASSIGNMENT-01-student-dictionary/DEMO.py`; hàm hoàn chỉnh: `docs/labs/ASSIGNMENT-01-student-dictionary/SOLUTION_ANNOTATED.py`. Hàm áp dụng: `delete()`.

```python
def delete(students, student_id, confirmed=False):
    """Delete only if the key exists and the user confirms the operation."""
    if student_id not in students:
        raise KeyError(f"Unknown student ID: {student_id}")
    if not confirmed:
        return False  # Cancellation must leave dictionary untouched.
    del students[student_id]  # Remove exactly the selected dictionary key.
    return True
```

### Giải thích quy trình giải và công thức

Tìm ID rồi kiểm tra `confirmed`; khi người dùng từ chối thì không đụng đến dữ liệu. Khi đồng ý mới `del students[id]`.

**Công thức / quy tắc:** Quy tắc xóa: `exists(id) AND confirmed`.

## Bài 6

### English — Original requirement

**Validate data:** Ensure valid input (non-empty name, valid score range, correct format).

### Tiếng Việt — Bản dịch

**Kiểm tra dữ liệu:** Không cho phép tên rỗng, điểm ngoài phạm vi, hoặc định dạng không hợp lệ.

### Bài giải — Code từ tài liệu đã có

Code thực hành gốc: `labs/pythoclass/ASSIGNMENT-01-student-dictionary/DEMO.py`; hàm hoàn chỉnh: `docs/labs/ASSIGNMENT-01-student-dictionary/SOLUTION_ANNOTATED.py`. Hàm áp dụng: `validate()`.

```python
def validate(student_id, name, score):
    """Accept ID, student name and score; reject malformed records."""
    # .strip() removes accidental leading or trailing spaces from text input.
    student_id = student_id.strip()
    name = name.strip()
    if not student_id or not name:  # Empty ID/name is not allowed.
        raise ValueError("Student ID and name are required.")
    try:
        score = float(score)  # Input from input() is text; convert to a number.
    except (ValueError, TypeError) as error:
        raise ValueError("Score must be numeric.") from error
    if not 0 <= score <= 10:  # Require points within the 0–10 grading scale.
        raise ValueError("Score must be between 0 and 10.")
    return student_id, name, score
```

### Giải thích quy trình giải và công thức

Phân biệt kiểm tra kiểu dữ liệu và kiểm tra khoảng giá trị; nêu rõ vì sao `input()` tạo chuỗi, vì sao cần bắt `ValueError`.

**Công thức / quy tắc:** 0 ≤ score ≤ 10; ID và name không được rỗng.

## Bài 7

### English — Original requirement

**Check duplicate ID:** Do not allow adding students with existing IDs.

### Tiếng Việt — Bản dịch

**Trùng mã:** Một mã sinh viên chỉ được xuất hiện một lần.

### Bài giải — Code từ tài liệu đã có

Code thực hành gốc: `labs/pythoclass/ASSIGNMENT-01-student-dictionary/DEMO.py`; hàm hoàn chỉnh: `docs/labs/ASSIGNMENT-01-student-dictionary/SOLUTION_ANNOTATED.py`. Hàm áp dụng: `add()`.

```python
def add(students, student_id, name, score):
    """Create a dictionary entry while preventing duplicate IDs."""
    student_id, name, score = validate(student_id, name, score)
    if student_id in students:  # Dictionary keys are unique identifiers.
        raise ValueError(f"Duplicate student ID: {student_id}")
    # Nested dictionary gives named fields instead of brittle list offsets.
    students[student_id] = {"name": name, "score": score}
```

### Giải thích quy trình giải và công thức

Dùng cùng hàm `add` trong code nguồn để chống trùng trước thao tác gán: nếu `id in students` thì báo lỗi.

**Công thức / quy tắc:** ID đóng vai trò khóa duy nhất (unique key).

## Bài 8

### English — Original requirement

**Sorting:** Sort students by score (ascending/descending).

### Tiếng Việt — Bản dịch

**Sắp xếp:** Xếp sinh viên tăng dần hoặc giảm dần theo điểm.

### Bài giải — Code từ tài liệu đã có

Code thực hành gốc: `labs/pythoclass/ASSIGNMENT-01-student-dictionary/DEMO.py`; hàm hoàn chỉnh: `docs/labs/ASSIGNMENT-01-student-dictionary/SOLUTION_ANNOTATED.py`. Hàm áp dụng: `sort_by_score()`.

```python
def sort_by_score(students, descending=False):
    """Return a sorted view without modifying the source dictionary."""
    # Each 'pair' contains the dictionary key and its nested student record.
    return sorted(
        students.items(),
        key=lambda pair: pair[1]["score"],  # Compare numeric score fields.
        reverse=descending,  # True sorts from high score to low score.
    )
```

### Giải thích quy trình giải và công thức

Sắp theo khóa `score`, dùng `reverse=True/False` để đổi chiều; chương trình không làm biến đổi dữ liệu đang lưu.

**Công thức / quy tắc:** Sắp xếp có độ phức tạp điển hình O(n log n).

## Bài 9

### English — Original requirement

**Advanced statistics:** Highest score student, lowest score student, average score, count students by performance level.

### Tiếng Việt — Bản dịch

**Thống kê nâng cao:** Tìm điểm cao nhất, thấp nhất, điểm trung bình và số sinh viên ở từng mức học lực.

### Bài giải — Code từ tài liệu đã có

Code thực hành gốc: `labs/pythoclass/ASSIGNMENT-01-student-dictionary/DEMO.py`; hàm hoàn chỉnh: `docs/labs/ASSIGNMENT-01-student-dictionary/SOLUTION_ANNOTATED.py`. Hàm áp dụng: `statistics()`.

```python
def statistics(students):
    """Summarize scores and classification counts; handle zero students."""
    if not students:
        return None
    scores = [item["score"] for item in students.values()]
    counts = Counter(classify(score) for score in scores)
    return {
        "highest": max(scores),
        "lowest": min(scores),
        "average": sum(scores) / len(scores),  # No /0: empty case handled.
        "classification_counts": dict(counts),
    }
```

### Giải thích quy trình giải và công thức

Lấy danh sách điểm; tính `max`, `min`, trung bình, rồi đếm nhãn phân loại bằng `Counter`. Cần xử lý trường hợp không có sinh viên để tránh chia 0.

**Công thức / quy tắc:** Điểm trung bình = tổng điểm / số sinh viên; mỗi nhãn được đếm bằng số bản ghi thuộc mức đó.

## Bài 10

### English — Original requirement

**Academic classification:** Classify students based on score (e.g., Excellent, Good, Average, Poor).

### Tiếng Việt — Bản dịch

**Phân loại học lực:** Dựa trên điểm, gán Excellent (Xuất sắc), Good (Khá), Average (Trung bình), Poor (Yếu). Đề không ấn định ngưỡng; dùng quy tắc của file code tham khảo và ghi rõ.

### Bài giải — Code từ tài liệu đã có

Code thực hành gốc: `labs/pythoclass/ASSIGNMENT-01-student-dictionary/DEMO.py`; hàm hoàn chỉnh: `docs/labs/ASSIGNMENT-01-student-dictionary/SOLUTION_ANNOTATED.py`. Hàm áp dụng: `classify()`.

```python
def classify(score):
    """Map scores to four documented, mutually exclusive categories."""
    if score >= 9:
        return "Excellent"
    if score >= 7:
        return "Good"
    if score >= 5:
        return "Average"
    return "Poor"
```

### Giải thích quy trình giải và công thức

Kiểm tra ngưỡng từ cao xuống thấp để không có hai mức cùng đúng; các mốc lấy từ code tham khảo đã tồn tại, **không giả nhận là đề Word quy định**.

**Công thức / quy tắc:** `score ≥ 9`: Excellent; `7 ≤ score < 9`: Good; `5 ≤ score < 7`: Average; `score < 5`: Poor.

## Ghi chú nguồn và cách chạy

- Các đoạn code trên là **trích hàm từ script đã có**, không phải bài giải thuật toán mới tự nghĩ. Khi chạy cả chương trình cần giữ chung các import/hàm phụ thuộc (`from collections import Counter`, `import sys`, `validate`, `classify`, `add`) như trong file tham chiếu.
- Những ví dụ DEMO ban đầu có thể chưa hoàn chỉnh; bản code trích ở trên lấy từ tài liệu giải đã kiểm tra, không giả nhận tất cả đều là code đã tự viết trong notebook. Xem tiến trình học ở PY-08, PY-09 và PY-44.
- **Không cần file thứ hai**: mọi đề, bản dịch, code và giải thích của Lab này nằm trong tài liệu Markdown này.
