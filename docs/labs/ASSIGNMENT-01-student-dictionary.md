# ASSIGNMENT-01-student-dictionary — English brief, Vietnamese brief, method and full commented script

**Nguồn đề:** `PythoClass` Word (bản chép ở `labs/pythoclass/ASSIGNMENT-01-student-dictionary/LAB.md`). **Nguồn code:** bản giải/annotated có sẵn từ repo AIClassDocuments (không nhận là nguyên văn code demo nếu demo chưa đủ), đối chiếu `labs/pythoclass/ASSIGNMENT-01-student-dictionary/DEMO.py` và `SOLUTION.py`. **Một tài liệu duy nhất**, không chia đề/đáp án xen kẽ.

---

## PART 1 — COMPLETE ORIGINAL ENGLISH ASSIGNMENT

# ASSIGNMENT 1

## Objective
Develop a menu-driven Python program to manage student information using a dictionary data structure and functions.

## Requirements
Write a Python program that implements the following features:

1. **Data Structure:** Store students in a dictionary. Each student includes: `id`, `name`, `score`.
2. **Create (Add student):** Input student information. Check for duplicate ID before adding.
3. **Read (Display students):** Show all students in the system.
4. **Update student:** Update student information based on ID.
5. **Delete student:** Delete a student by ID. Require confirmation before deletion.
6. **Validate data:** Ensure valid input (non-empty name, valid score range, correct format).
7. **Check duplicate ID:** Do not allow adding students with existing IDs.
8. **Sorting:** Sort students by score (ascending/descending).
9. **Advanced statistics:** Highest score student, lowest score student, average score, count students by performance level.
10. **Academic classification:** Classify students based on score (e.g., Excellent, Good, Average, Poor).

---

## PHẦN 2 — BẢN DỊCH TIẾNG VIỆT TOÀN BỘ ĐỀ

# BÀI TẬP 1 — Quản lý sinh viên bằng Dictionary

## Mục tiêu
Xây dựng chương trình Python có menu quản lý thông tin sinh viên, sử dụng cấu trúc dữ liệu **dictionary** và các hàm.

## Yêu cầu
Viết chương trình có đầy đủ các chức năng sau:

1. **Cấu trúc dữ liệu:** Lưu sinh viên bằng dictionary, mỗi bản ghi có `id`, `name`, `score`.
2. **Thêm sinh viên (Create):** Nhập thông tin, kiểm tra mã ID trùng trước khi thêm.
3. **Hiển thị (Read):** Xuất toàn bộ sinh viên hiện có.
4. **Cập nhật (Update):** Sửa thông tin sinh viên dựa trên ID.
5. **Xóa (Delete):** Xóa theo ID và **phải có xác nhận** trước khi xóa.
6. **Kiểm tra dữ liệu:** Không cho phép tên rỗng, điểm ngoài khoảng hợp lệ hoặc sai định dạng.
7. **Chống trùng mã:** Không thêm được sinh viên có ID đã tồn tại.
8. **Sắp xếp:** Sắp xếp theo điểm tăng dần hoặc giảm dần.
9. **Thống kê nâng cao:** Tìm sinh viên có điểm cao nhất, thấp nhất, tính điểm trung bình và đếm sinh viên theo mức học lực.
10. **Phân loại học lực:** Dựa trên điểm, chia thành Xuất sắc (Excellent), Khá (Good), Trung bình (Average) và Yếu (Poor).

*Lưu ý:* Đề Word chỉ nêu ví dụ các mức học lực, **không quy định ngưỡng điểm cụ thể**. Các ngưỡng của code tham khảo phải được trình bày như quy ước triển khai, không phải dữ liệu gốc.

---

## Quy trình giải chi tiết và các công thức liên quan

**Luồng giải chung:** Đọc yêu cầu và dữ liệu đầu vào → xác thực kiểu và miền giá trị → chọn cấu trúc dữ liệu/điều kiện/vòng lặp đã học → tính toán hoặc cập nhật → kiểm tra kết quả bằng ví dụ đề → xử lý trường hợp rỗng/sai. Các hàm trong phần code bên dưới là một chương trình hoàn chỉnh và có thể chạy cùng nhau.

### Bài 1 — Cách thực hiện

Dùng `dict` lồng nhau: khóa ngoài là ID duy nhất, giá trị là đối tượng có `name` và `score`. Hàm tạo dữ liệu giả lập để tránh thông tin cá nhân.

**Công thức / quy tắc:** Không có công thức; truy cập theo `students[id]` có độ phức tạp trung bình O(1).

**Điểm cần kiểm tra:** dictionary là cấu trúc lưu trữ chính; ID là khóa.

### Bài 2 — Cách thực hiện

Đọc các trường, chuẩn hóa bằng `.strip()`, đổi điểm bằng `float()`, kiểm tra miền 0–10, rồi kiểm tra ID chưa có trước khi thêm.

**Công thức / quy tắc:** Điểm hợp lệ: 0 ≤ score ≤ 10; điều kiện tồn tại ID: `id in students`.

**Điểm cần kiểm tra:** xác thực `id`, `name`, `score` và chặn trùng ID.

### Bài 3 — Cách thực hiện

Duyệt `.items()` để lấy cặp ID–thông tin và in nội dung. Giữ nguyên thứ tự thêm vào của từ điển.

**Công thức / quy tắc:** Không có công thức; dùng lặp `for` thay vì ép người học tự hình dung cấu trúc.

**Điểm cần kiểm tra:** thao tác CRUD thêm, đọc, sửa và xóa sau khi xác nhận.

### Bài 4 — Cách thực hiện

Từ ID đầu vào, tìm đúng khóa; từ chối ID không tồn tại, xác thực giá trị mới trước khi thay thế.

**Công thức / quy tắc:** Điểm chỉ được cập nhật nếu `0 ≤ score ≤ 10`.

**Điểm cần kiểm tra:** sắp xếp điểm và tổng hợp bằng `Counter`.

### Bài 5 — Cách thực hiện

Tìm ID rồi kiểm tra `confirmed`; khi người dùng từ chối thì không đụng đến dữ liệu. Khi đồng ý mới `del students[id]`.

**Công thức / quy tắc:** Quy tắc xóa: `exists(id) AND confirmed`.

**Điểm cần kiểm tra:** phân loại mức học lực từ cao xuống thấp; đây là ngưỡng do lời giải tham khảo chọn.

### Bài 6 — Cách thực hiện

Phân biệt kiểm tra kiểu dữ liệu và kiểm tra khoảng giá trị; nêu rõ vì sao `input()` tạo chuỗi, vì sao cần bắt `ValueError`.

**Công thức / quy tắc:** 0 ≤ score ≤ 10; ID và name không được rỗng.

**Điểm cần kiểm tra:** phân loại mức học lực từ cao xuống thấp; đây là ngưỡng do lời giải tham khảo chọn.

### Bài 7 — Cách thực hiện

Dùng cùng hàm `add` trong code nguồn để chống trùng trước thao tác gán: nếu `id in students` thì báo lỗi.

**Công thức / quy tắc:** ID đóng vai trò khóa duy nhất (unique key).

**Điểm cần kiểm tra:** phân loại mức học lực từ cao xuống thấp; đây là ngưỡng do lời giải tham khảo chọn.

### Bài 8 — Cách thực hiện

Sắp theo khóa `score`, dùng `reverse=True/False` để đổi chiều; chương trình không làm biến đổi dữ liệu đang lưu.

**Công thức / quy tắc:** Sắp xếp có độ phức tạp điển hình O(n log n).

**Điểm cần kiểm tra:** phân loại mức học lực từ cao xuống thấp; đây là ngưỡng do lời giải tham khảo chọn.

### Bài 9 — Cách thực hiện

Lấy danh sách điểm; tính `max`, `min`, trung bình, rồi đếm nhãn phân loại bằng `Counter`. Cần xử lý trường hợp không có sinh viên để tránh chia 0.

**Công thức / quy tắc:** Điểm trung bình = tổng điểm / số sinh viên; mỗi nhãn được đếm bằng số bản ghi thuộc mức đó.

**Điểm cần kiểm tra:** phân loại mức học lực từ cao xuống thấp; đây là ngưỡng do lời giải tham khảo chọn.

### Bài 10 — Cách thực hiện

Kiểm tra ngưỡng từ cao xuống thấp để không có hai mức cùng đúng; các mốc lấy từ code tham khảo đã tồn tại, **không giả nhận là đề Word quy định**.

**Công thức / quy tắc:** `score ≥ 9`: Excellent; `7 ≤ score < 9`: Good; `5 ≤ score < 7`: Average; `score < 5`: Poor.

**Điểm cần kiểm tra:** phân loại mức học lực từ cao xuống thấp; đây là ngưỡng do lời giải tham khảo chọn.


---

## PHẦN 4 — TOÀN BỘ CODE PYTHON CÙNG CHÚ THÍCH

**Nguồn code:** `labs/pythoclass/ASSIGNMENT-01-student-dictionary/SOLUTION.py` và phiên bản chú thích đã có trong lịch sử dự án. Code giữ nguyên logic thực hành; `#` trong file dùng để giải thích từng đoạn. Sao chép **nguyên khối** sau vào một file `lab_solution.py` trong môi trường Python; chạy bằng `python lab_solution.py --demo` nếu là lab menu, hoặc `python lab_solution.py` để thực hiện lệnh tương tác/kiểm thử. Các đường dẫn, nguồn dữ liệu đi kèm vẫn cần tuân theo hướng dẫn trong script.

```python
"""Assignment 01 — Student dictionary manager, explained step by step.

Reference: labs/pythoclass/ASSIGNMENT-01-student-dictionary/SOLUTION.py
Run the deterministic example: python lab_solution.py --demo
Run the text menu: python lab_solution.py
"""
from collections import Counter  # Count learners in each performance category.
import sys  # Read command-line arguments without a third-party library.


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


def add(students, student_id, name, score):
    """Create a dictionary entry while preventing duplicate IDs."""
    student_id, name, score = validate(student_id, name, score)
    if student_id in students:  # Dictionary keys are unique identifiers.
        raise ValueError(f"Duplicate student ID: {student_id}")
    # Nested dictionary gives named fields instead of brittle list offsets.
    students[student_id] = {"name": name, "score": score}


def display(students):
    """Read: list all records including score and academic category."""
    if not students:
        print("No students stored.")  # Handle an empty dataset gracefully.
    for student_id, record in students.items():  # Traverse key/value pairs.
        print(f"{student_id} | {record['name']} | "
              f"{record['score']:g}/10 | {classify(record['score'])}")


def update(students, student_id, new_name, new_score):
    """Update a student by ID without silently creating new records."""
    if student_id not in students:
        raise KeyError(f"Unknown student ID: {student_id}")
    _, name, score = validate(student_id, new_name, new_score)
    students[student_id] = {"name": name, "score": score}


def delete(students, student_id, confirmed=False):
    """Delete only if the key exists and the user confirms the operation."""
    if student_id not in students:
        raise KeyError(f"Unknown student ID: {student_id}")
    if not confirmed:
        return False  # Cancellation must leave dictionary untouched.
    del students[student_id]  # Remove exactly the selected dictionary key.
    return True


def classify(score):
    """Map scores to four documented, mutually exclusive categories."""
    if score >= 9:
        return "Excellent"
    if score >= 7:
        return "Good"
    if score >= 5:
        return "Average"
    return "Poor"


def sort_by_score(students, descending=False):
    """Return a sorted view without modifying the source dictionary."""
    # Each 'pair' contains the dictionary key and its nested student record.
    return sorted(
        students.items(),
        key=lambda pair: pair[1]["score"],  # Compare numeric score fields.
        reverse=descending,  # True sorts from high score to low score.
    )


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


def sample_students():
    """Generate synthetic demo names rather than real student identities."""
    scores = [9.5, 8, 7.5, 6, 5.5, 4.5, 7, 9, 8.5, 6.5, 10, 5]
    students = {}
    for number, score in enumerate(scores, start=1):
        add(students, f"S{number:03d}", f"Learner {number:02d}", score)
    return students


def run_demo():
    """Exercise create, update, cancel/delete, sort and numeric statistics."""
    students = sample_students()
    assert len(students) == 12  # Base fixture contains twelve test records.
    add(students, "S013", "New Learner", 8)
    update(students, "S013", "Updated Learner", 8.5)
    assert delete(students, "S013", confirmed=False) is False
    assert "S013" in students  # Cancelled deletion did not change the record.
    assert delete(students, "S013", confirmed=True) is True
    assert "S013" not in students
    assert len(students) == 12

    print("Ascending scores (first 4):", sort_by_score(students)[:4])
    print("Descending scores (first 4):",
          sort_by_score(students, descending=True)[:4])
    print("Statistics:", statistics(students))
    print("Student list:")
    display(students)


def interactive_menu():
    """Keep the terminal menu running until the user explicitly exits."""
    students = sample_students()
    menu = "\n1.Display 2.Add 3.Update 4.Delete 5.Sort 6.Statistics 0.Exit"
    while True:
        print(menu)
        action = input("Choose: ").strip()
        try:  # Catch user errors; do not terminate the whole menu.
            if action == "0":
                break
            elif action == "1":
                display(students)
            elif action == "2":
                add(students, input("ID: "), input("Name: "),
                    input("Score [0,10]: "))
            elif action == "3":
                key = input("ID to update: ").strip()
                update(students, key, input("New name: "), input("New score: "))
            elif action == "4":
                key = input("ID to delete: ").strip()
                answer = input("Confirm deletion? [y/N]: ").strip().lower()
                if not delete(students, key, confirmed=(answer == "y")):
                    print("Deletion cancelled.")
            elif action == "5":
                descending = input("Descending? [y/N]: ").strip().lower() == "y"
                for key, item in sort_by_score(students, descending):
                    print(key, item)
            elif action == "6":
                print(statistics(students))
            else:
                print("Unknown menu option.")
        except (ValueError, KeyError) as error:
            print("Input error:", error)


if __name__ == "__main__":
    # '--demo' avoids interactive input in automated tests or tutorials.
    if "--demo" in sys.argv:
        run_demo()
    else:
        interactive_menu()
```

**Lưu ý:** Nếu demo gốc chỉ thể hiện một phần, code đầy đủ được lấy từ lời giải tham khảo đã được lưu/kiểm tra, không phải phần tự sáng tác ở tài liệu này.
