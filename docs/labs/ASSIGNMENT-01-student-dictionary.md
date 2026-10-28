# ASSIGNMENT-01-student-dictionary — English brief, Vietnamese brief, method and full commented script

**Nguồn đề:** `PythoClass` Word (bản chép ở `labs/pythoclass/ASSIGNMENT-01-student-dictionary/LAB.md`). **Nguồn code:** bản giải/annotated có sẵn từ repo AIClassDocuments (không nhận là nguyên văn code demo nếu demo chưa đủ), đối chiếu `labs/pythoclass/ASSIGNMENT-01-student-dictionary/DEMO.py` và `SOLUTION.py`. **Một tài liệu duy nhất**, không chia đề/đáp án xen kẽ.

---

## ĐỀ VÀ HƯỚNG GIẢI SONG NGỮ — TỪNG CÂU ENGLISH / TIẾNG VIỆT

**Cách đọc:** Mỗi câu có nguyên đề tiếng Anh (English: tiếng Anh) ngay trước bản dịch tiếng Việt, tiếp đến phần giải thích và công thức. Mọi giá trị, bảng và biểu thức gốc được giữ nguyên.

### Bối cảnh, dữ liệu — Original English

# ASSIGNMENT 1

## Objective
Develop a menu-driven Python program to manage student information using a dictionary data structure and functions.

## Requirements
Write a Python program that implements the following features:

### Bối cảnh, dữ liệu — Tiếng Việt

# BÀI TẬP 1 — Quản lý sinh viên bằng Dictionary (từ điển)

## Mục tiêu
Xây dựng chương trình Python có menu quản lý thông tin sinh viên, sử dụng cấu trúc dữ liệu **dictionary** và các hàm.

## Yêu cầu
Viết chương trình có đầy đủ các chức năng sau:

### Câu 1 — English → Tiếng Việt → Giải thích

**English — Đề gốc:**

1. **Data Structure:** Store students in a dictionary. Each student includes: `id`, `name`, `score`.

**Tiếng Việt — Bản dịch của câu ngay trên:**

1. **Cấu trúc dữ liệu:** Lưu sinh viên bằng dictionary (từ điển), mỗi bản ghi có `id`, `name`, `score`.

**Giải thích từng bước và công thức liên quan:**

Dùng `dict` lồng nhau: khóa ngoài là ID duy nhất, giá trị là đối tượng có `name` và `score`. Hàm tạo dữ liệu giả lập để tránh thông tin cá nhân.

**Công thức / quy tắc:** Không có công thức; truy cập theo `students[id]` có độ phức tạp trung bình O(1).

**Điểm cần kiểm tra:** dictionary (từ điển) là cấu trúc lưu trữ chính; ID là khóa.

**Ví dụ, cách kiểm tra và lỗi dễ gặp:** ID là khóa duy nhất của từ điển; mỗi khóa dẫn tới thông tin người học. Dùng tên làm khóa dễ ghi đè khi trùng tên.

**Thuật ngữ cần nhớ:** Dictionary (từ điển).

### Câu 2 — English → Tiếng Việt → Giải thích

**English — Đề gốc:**

2. **Create (Add student):** Input student information. Check for duplicate ID before adding.

**Tiếng Việt — Bản dịch của câu ngay trên:**

2. **Thêm sinh viên (Create):** Nhập thông tin, kiểm tra mã ID trùng trước khi thêm.

**Giải thích từng bước và công thức liên quan:**

Đọc các trường, chuẩn hóa bằng `.strip()`, đổi điểm bằng `float()`, kiểm tra miền 0–10, rồi kiểm tra ID chưa có trước khi thêm.

**Công thức / quy tắc:** Điểm hợp lệ: 0 ≤ score (điểm số) ≤ 10; điều kiện tồn tại ID: `id in students`.

**Điểm cần kiểm tra:** xác thực `id`, `name`, `score` và chặn trùng ID.

**Ví dụ, cách kiểm tra và lỗi dễ gặp:** Kiểm tra ID đã có hay chưa trước khi gán dữ liệu, rồi xác thực tên, điểm. Nhập sai cần báo lỗi thay vì ghi nhầm.

**Thuật ngữ cần nhớ:** Create (thêm mới).

### Câu 3 — English → Tiếng Việt → Giải thích

**English — Đề gốc:**

3. **Read (Display students):** Show all students in the system.

**Tiếng Việt — Bản dịch của câu ngay trên:**

3. **Hiển thị (Read):** Xuất toàn bộ sinh viên hiện có.

**Giải thích từng bước và công thức liên quan:**

Duyệt `.items()` để lấy cặp ID–thông tin và in nội dung. Giữ nguyên thứ tự thêm vào của từ điển.

**Công thức / quy tắc:** Không có công thức; dùng lặp `for` thay vì ép người học tự hình dung cấu trúc.

**Điểm cần kiểm tra:** thao tác CRUD thêm, đọc, sửa và xóa sau khi xác nhận.

**Ví dụ, cách kiểm tra và lỗi dễ gặp:** items() cho phép lấy cả mã và thông tin; in đủ ID, tên và điểm. Danh sách rỗng cần trả thông báo dễ hiểu.

**Thuật ngữ cần nhớ:** Read (đọc dữ liệu).

### Câu 4 — English → Tiếng Việt → Giải thích

**English — Đề gốc:**

4. **Update student:** Update student information based on ID.

**Tiếng Việt — Bản dịch của câu ngay trên:**

4. **Cập nhật (Update):** Sửa thông tin sinh viên dựa trên ID.

**Giải thích từng bước và công thức liên quan:**

Từ ID đầu vào, tìm đúng khóa; từ chối ID không tồn tại, xác thực giá trị mới trước khi thay thế.

**Công thức / quy tắc:** Điểm chỉ được cập nhật nếu `0 ≤ score ≤ 10`.

**Điểm cần kiểm tra:** sắp xếp điểm và tổng hợp bằng `Counter`.

**Ví dụ, cách kiểm tra và lỗi dễ gặp:** Chỉ thay đổi bản ghi có đúng ID; nếu không tìm thấy mã phải xử lý chứ không tự tạo người mới.

**Thuật ngữ cần nhớ:** Update (cập nhật).

### Câu 5 — English → Tiếng Việt → Giải thích

**English — Đề gốc:**

5. **Delete student:** Delete a student by ID. Require confirmation before deletion.

**Tiếng Việt — Bản dịch của câu ngay trên:**

5. **Xóa (Delete):** Xóa theo ID và **phải có xác nhận** trước khi xóa.

**Giải thích từng bước và công thức liên quan:**

Tìm ID rồi kiểm tra `confirmed`; khi người dùng từ chối thì không đụng đến dữ liệu. Khi đồng ý mới `del students[id]`.

**Công thức / quy tắc:** Quy tắc xóa: `exists(id) AND confirmed`.

**Điểm cần kiểm tra:** phân loại mức học lực từ cao xuống thấp; đây là ngưỡng do lời giải tham khảo chọn.

**Ví dụ, cách kiểm tra và lỗi dễ gặp:** Chỉ xóa khi tìm thấy mã và người dùng đã xác nhận; thử hủy xóa để chứng minh dữ liệu giữ nguyên.

**Thuật ngữ cần nhớ:** Delete (xóa).

### Câu 6 — English → Tiếng Việt → Giải thích

**English — Đề gốc:**

6. **Validate data:** Ensure valid input (non-empty name, valid score range, correct format).

**Tiếng Việt — Bản dịch của câu ngay trên:**

6. **Kiểm tra dữ liệu:** Không cho phép tên rỗng, điểm ngoài khoảng hợp lệ hoặc sai định dạng.

**Giải thích từng bước và công thức liên quan:**

Phân biệt kiểm tra kiểu dữ liệu và kiểm tra khoảng giá trị; nêu rõ vì sao `input()` tạo chuỗi, vì sao cần bắt `ValueError`.

**Công thức / quy tắc:** 0 ≤ score (điểm số) ≤ 10; ID và name không được rỗng.

**Điểm cần kiểm tra:** phân loại mức học lực từ cao xuống thấp; đây là ngưỡng do lời giải tham khảo chọn.

**Ví dụ, cách kiểm tra và lỗi dễ gặp:** strip() bỏ khoảng trắng ở tên; float() chuyển điểm sang số; kiểm tra miền điểm của code nguồn.

**Thuật ngữ cần nhớ:** Validate (xác thực dữ liệu).

### Câu 7 — English → Tiếng Việt → Giải thích

**English — Đề gốc:**

7. **Check duplicate ID:** Do not allow adding students with existing IDs.

**Tiếng Việt — Bản dịch của câu ngay trên:**

7. **Chống trùng mã:** Không thêm được sinh viên có ID đã tồn tại.

**Giải thích từng bước và công thức liên quan:**

Dùng cùng hàm `add` trong code nguồn để chống trùng trước thao tác gán: nếu `id in students` thì báo lỗi.

**Công thức / quy tắc:** ID đóng vai trò khóa duy nhất (unique key).

**Điểm cần kiểm tra:** phân loại mức học lực từ cao xuống thấp; đây là ngưỡng do lời giải tham khảo chọn.

**Ví dụ, cách kiểm tra và lỗi dễ gặp:** Không kiểm tra trùng bằng tên, bởi hai sinh viên có thể có tên giống nhau; cần kiểm tra khóa ID.

**Thuật ngữ cần nhớ:** duplicate ID (trùng mã).

### Câu 8 — English → Tiếng Việt → Giải thích

**English — Đề gốc:**

8. **Sorting:** Sort students by score (ascending/descending).

**Tiếng Việt — Bản dịch của câu ngay trên:**

8. **Sắp xếp:** Sắp xếp theo điểm tăng dần hoặc giảm dần.

**Giải thích từng bước và công thức liên quan:**

Sắp theo khóa `score`, dùng `reverse=True/False` để đổi chiều; chương trình không làm biến đổi dữ liệu đang lưu.

**Công thức / quy tắc:** Sắp xếp có độ phức tạp điển hình O(n log n).

**Điểm cần kiểm tra:** phân loại mức học lực từ cao xuống thấp; đây là ngưỡng do lời giải tham khảo chọn.

**Ví dụ, cách kiểm tra và lỗi dễ gặp:** sorted() sắp điểm số tăng/giảm; điểm là float chứ không phải chuỗi chữ, tránh thứ tự sai.

**Thuật ngữ cần nhớ:** Sorting (sắp xếp).

### Câu 9 — English → Tiếng Việt → Giải thích

**English — Đề gốc:**

9. **Advanced statistics:** Highest score student, lowest score student, average score, count students by performance level.

**Tiếng Việt — Bản dịch của câu ngay trên:**

9. **Thống kê nâng cao:** Tìm sinh viên có điểm cao nhất, thấp nhất, tính điểm trung bình và đếm sinh viên theo mức học lực.

**Giải thích từng bước và công thức liên quan:**

Lấy danh sách điểm; tính `max`, `min`, trung bình, rồi đếm nhãn phân loại bằng `Counter`. Cần xử lý trường hợp không có sinh viên để tránh chia 0.

**Công thức / quy tắc:** Điểm trung bình = tổng điểm / số sinh viên; mỗi nhãn được đếm bằng số bản ghi thuộc mức đó.

**Điểm cần kiểm tra:** phân loại mức học lực từ cao xuống thấp; đây là ngưỡng do lời giải tham khảo chọn.

**Ví dụ, cách kiểm tra và lỗi dễ gặp:** Trung bình bằng tổng điểm/số người; cần xử lý n=0 để tránh chia cho 0; Counter đếm mức học lực.

**Thuật ngữ cần nhớ:** Statistics (thống kê).

### Câu 10 — English → Tiếng Việt → Giải thích

**English — Đề gốc:**

10. **Academic classification:** Classify students based on score (e.g., Excellent, Good, Average, Poor).

**Tiếng Việt — Bản dịch của câu ngay trên:**

10. **Phân loại học lực:** Dựa trên điểm, chia thành Xuất sắc (Excellent), Khá (Good), Trung bình (Average) và Yếu (Poor).

*Lưu ý:* Đề Word chỉ nêu ví dụ các mức học lực, **không quy định ngưỡng điểm cụ thể**. Các ngưỡng của code tham khảo phải được trình bày như quy ước triển khai, không phải dữ liệu gốc.

**Giải thích từng bước và công thức liên quan:**

Kiểm tra ngưỡng từ cao xuống thấp để không có hai mức cùng đúng; các mốc lấy từ code tham khảo đã tồn tại, **không giả nhận là đề Word quy định**.

**Công thức / quy tắc:** `score ≥ 9`: Excellent; `7 ≤ score < 9`: Good; `5 ≤ score < 7`: Average; `score < 5`: Poor.

**Điểm cần kiểm tra:** phân loại mức học lực từ cao xuống thấp; đây là ngưỡng do lời giải tham khảo chọn.

**Ví dụ, cách kiểm tra và lỗi dễ gặp:** Các ngưỡng học lực là quy ước của code tham khảo, không mặc định là quy định từ đề Word.

**Thuật ngữ cần nhớ:** classification (phân loại).

---

## TOÀN BỘ CODE PYTHON — CHÚ THÍCH NGAY SAU TỪNG DÒNG

**Hướng dẫn:** Các dòng lệnh có lời giải thích tiếng Việt **sau cùng dòng**, đi sau dấu `#`. Các dòng trắng chỉ tách nhóm code. Không dùng `assert`; các phép kiểm tra của script cũ được diễn đạt thành `if` (nếu) và `raise ValueError` (báo lỗi dữ liệu) để giữ khả năng phát hiện kết quả sai. Dữ liệu và thuật toán đều bám theo code mẫu, không thay bài toán.

```python
from collections import Counter  # Nạp thư viện (import: nạp vào) để sử dụng hàm có sẵn.
import sys  # Nạp thư viện (import: nạp vào) để sử dụng hàm có sẵn.


def validate(student_id, name, score):  # Khai báo hàm (function: hàm), nhóm các bước và cho phép gọi lại.
    student_id = student_id.strip()  # Bỏ khoảng trắng thừa (strip: cắt khoảng trắng).
    name = name.strip()  # Bỏ khoảng trắng thừa (strip: cắt khoảng trắng).
    if not student_id or not name:  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
        raise ValueError("Student ID and name are required.")  # Thông báo lỗi khi dữ liệu không hợp lệ.
    try:  # Thử thao tác có thể phát sinh lỗi.
        score = float(score)  # Tính hoặc cập nhật biến score từ biểu thức, giữ đúng công thức của bài.
    except (ValueError, TypeError) as error:  # Bắt ngoại lệ (exception: lỗi) để thông báo rõ.
        raise ValueError("Score must be numeric.") from error  # Thông báo lỗi khi dữ liệu không hợp lệ.
    if not 0 <= score <= 10:  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
        raise ValueError("Score must be between 0 and 10.")  # Thông báo lỗi khi dữ liệu không hợp lệ.
    return student_id, name, score  # Trả kết quả (return: trả về) cho hàm gọi.


def add(students, student_id, name, score):  # Khai báo hàm (function: hàm), nhóm các bước và cho phép gọi lại.
    student_id, name, score = validate(student_id, name, score)  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.
    if student_id in students:  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
        raise ValueError(f"Duplicate student ID: {student_id}")  # Thông báo lỗi khi dữ liệu không hợp lệ.
    students[student_id] = {"name": name, "score": score}  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.


def display(students):  # Khai báo hàm (function: hàm), nhóm các bước và cho phép gọi lại.
    if not students:  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
        print("No students stored.")  # In kết quả (output: kết quả) để đối chiếu với đề.
    for student_id, record in students.items():  # Duyệt lần lượt dữ liệu bằng vòng lặp (loop: lặp).
        print(f"{student_id} | {record['name']} | "  # In kết quả (output: kết quả) để đối chiếu với đề.
              f"{record['score']:g}/10 | {classify(record['score'])}")  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.


def update(students, student_id, new_name, new_score):  # Khai báo hàm (function: hàm), nhóm các bước và cho phép gọi lại.
    if student_id not in students:  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
        raise KeyError(f"Unknown student ID: {student_id}")  # Thông báo lỗi khi dữ liệu không hợp lệ.
    _, name, score = validate(student_id, new_name, new_score)  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.
    students[student_id] = {"name": name, "score": score}  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.


def delete(students, student_id, confirmed=False):  # Khai báo hàm (function: hàm), nhóm các bước và cho phép gọi lại.
    if student_id not in students:  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
        raise KeyError(f"Unknown student ID: {student_id}")  # Thông báo lỗi khi dữ liệu không hợp lệ.
    if not confirmed:  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
        return False  # Trả kết quả (return: trả về) cho hàm gọi.
    del students[student_id]  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.
    return True  # Trả kết quả (return: trả về) cho hàm gọi.


def classify(score):  # Khai báo hàm (function: hàm), nhóm các bước và cho phép gọi lại.
    if score >= 9:  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
        return "Excellent"  # Trả kết quả (return: trả về) cho hàm gọi.
    if score >= 7:  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
        return "Good"  # Trả kết quả (return: trả về) cho hàm gọi.
    if score >= 5:  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
        return "Average"  # Trả kết quả (return: trả về) cho hàm gọi.
    return "Poor"  # Trả kết quả (return: trả về) cho hàm gọi.


def sort_by_score(students, descending=False):  # Khai báo hàm (function: hàm), nhóm các bước và cho phép gọi lại.
    return sorted(  # Trả kết quả (return: trả về) cho hàm gọi.
        students.items(),  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.
        key=lambda pair: pair[1]["score"],  # Tính hoặc cập nhật biến key từ biểu thức, giữ đúng công thức của bài.
        reverse=descending,  # Tính hoặc cập nhật biến reverse từ biểu thức, giữ đúng công thức của bài.
    )  # Đóng danh sách, biểu thức hoặc tập giá trị đang tạo.


def statistics(students):  # Khai báo hàm (function: hàm), nhóm các bước và cho phép gọi lại.
    if not students:  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
        return None  # Trả kết quả (return: trả về) cho hàm gọi.
    scores = [item["score"] for item in students.values()]  # Tính hoặc cập nhật biến scores từ biểu thức, giữ đúng công thức của bài.
    counts = Counter(classify(score) for score in scores)  # Tính hoặc cập nhật biến counts từ biểu thức, giữ đúng công thức của bài.
    return {  # Trả kết quả (return: trả về) cho hàm gọi.
        "highest": max(scores),  # Lưu trường tên khóa (key: khóa) và kết quả vào từ điển.
        "lowest": min(scores),  # Lưu trường tên khóa (key: khóa) và kết quả vào từ điển.
        "average": sum(scores) / len(scores),  # Lưu trường tên khóa (key: khóa) và kết quả vào từ điển.
        "classification_counts": dict(counts),  # Lưu trường tên khóa (key: khóa) và kết quả vào từ điển.
    }  # Đóng danh sách, biểu thức hoặc tập giá trị đang tạo.


def sample_students():  # Khai báo hàm (function: hàm), nhóm các bước và cho phép gọi lại.
    scores = [9.5, 8, 7.5, 6, 5.5, 4.5, 7, 9, 8.5, 6.5, 10, 5]  # Tính hoặc cập nhật biến scores từ biểu thức, giữ đúng công thức của bài.
    students = {}  # Tính hoặc cập nhật biến students từ biểu thức, giữ đúng công thức của bài.
    for number, score in enumerate(scores, start=1):  # Duyệt lần lượt dữ liệu bằng vòng lặp (loop: lặp).
        add(students, f"S{number:03d}", f"Learner {number:02d}", score)  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.
    return students  # Trả kết quả (return: trả về) cho hàm gọi.


def run_demo():  # Khai báo hàm (function: hàm), nhóm các bước và cho phép gọi lại.
    students = sample_students()  # Tính hoặc cập nhật biến students từ biểu thức, giữ đúng công thức của bài.
    if not (len(students) == 12): raise ValueError("Kết quả kiểm tra không đúng")  # Dùng if (nếu) thay lệnh kiểm tra assert trước đây; báo lỗi khi dữ liệu không đạt.
    add(students, "S013", "New Learner", 8)  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.
    update(students, "S013", "Updated Learner", 8.5)  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.
    if not (delete(students, "S013", confirmed=False) is False): raise ValueError("Kết quả kiểm tra không đúng")  # Dùng if (nếu) thay lệnh kiểm tra assert trước đây; báo lỗi khi dữ liệu không đạt.
    if not ("S013" in students): raise ValueError("Kết quả kiểm tra không đúng")  # Dùng if (nếu) thay lệnh kiểm tra assert trước đây; báo lỗi khi dữ liệu không đạt.
    if not (delete(students, "S013", confirmed=True) is True): raise ValueError("Kết quả kiểm tra không đúng")  # Dùng if (nếu) thay lệnh kiểm tra assert trước đây; báo lỗi khi dữ liệu không đạt.
    if not ("S013" not in students): raise ValueError("Kết quả kiểm tra không đúng")  # Dùng if (nếu) thay lệnh kiểm tra assert trước đây; báo lỗi khi dữ liệu không đạt.
    if not (len(students) == 12): raise ValueError("Kết quả kiểm tra không đúng")  # Dùng if (nếu) thay lệnh kiểm tra assert trước đây; báo lỗi khi dữ liệu không đạt.

    print("Ascending scores (first 4):", sort_by_score(students)[:4])  # In kết quả (output: kết quả) để đối chiếu với đề.
    print("Descending scores (first 4):",  # In kết quả (output: kết quả) để đối chiếu với đề.
          sort_by_score(students, descending=True)[:4])  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.
    print("Statistics:", statistics(students))  # In kết quả (output: kết quả) để đối chiếu với đề.
    print("Student list:")  # In kết quả (output: kết quả) để đối chiếu với đề.
    display(students)  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.


def interactive_menu():  # Khai báo hàm (function: hàm), nhóm các bước và cho phép gọi lại.
    students = sample_students()  # Tính hoặc cập nhật biến students từ biểu thức, giữ đúng công thức của bài.
    menu = "\n1.Display 2.Add 3.Update 4.Delete 5.Sort 6.Statistics 0.Exit"  # Tính hoặc cập nhật biến menu từ biểu thức, giữ đúng công thức của bài.
    while True:  # Lặp khi điều kiện còn đúng, dừng khi sai.
        print(menu)  # In kết quả (output: kết quả) để đối chiếu với đề.
        action = input("Choose: ").strip()  # Bỏ khoảng trắng thừa (strip: cắt khoảng trắng).
        try:  # Thử thao tác có thể phát sinh lỗi.
            if action == "0":  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
                break  # Thoát vòng lặp tại vị trí này.
            elif action == "1":  # Kiểm tra trường hợp thay thế sau nhánh trước.
                display(students)  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.
            elif action == "2":  # Kiểm tra trường hợp thay thế sau nhánh trước.
                add(students, input("ID: "), input("Name: "),  # Nhận input (dữ liệu nhập) rồi kiểm tra trước khi dùng.
                    input("Score [0,10]: "))  # Nhận input (dữ liệu nhập) rồi kiểm tra trước khi dùng.
            elif action == "3":  # Kiểm tra trường hợp thay thế sau nhánh trước.
                key = input("ID to update: ").strip()  # Bỏ khoảng trắng thừa (strip: cắt khoảng trắng).
                update(students, key, input("New name: "), input("New score: "))  # Nhận input (dữ liệu nhập) rồi kiểm tra trước khi dùng.
            elif action == "4":  # Kiểm tra trường hợp thay thế sau nhánh trước.
                key = input("ID to delete: ").strip()  # Bỏ khoảng trắng thừa (strip: cắt khoảng trắng).
                answer = input("Confirm deletion? [y/N]: ").strip().lower()  # Bỏ khoảng trắng thừa (strip: cắt khoảng trắng).
                if not delete(students, key, confirmed=(answer == "y")):  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
                    print("Deletion cancelled.")  # In kết quả (output: kết quả) để đối chiếu với đề.
            elif action == "5":  # Kiểm tra trường hợp thay thế sau nhánh trước.
                descending = input("Descending? [y/N]: ").strip().lower() == "y"  # Bỏ khoảng trắng thừa (strip: cắt khoảng trắng).
                for key, item in sort_by_score(students, descending):  # Duyệt lần lượt dữ liệu bằng vòng lặp (loop: lặp).
                    print(key, item)  # In kết quả (output: kết quả) để đối chiếu với đề.
            elif action == "6":  # Kiểm tra trường hợp thay thế sau nhánh trước.
                print(statistics(students))  # In kết quả (output: kết quả) để đối chiếu với đề.
            else:  # Xử lý trường hợp còn lại.
                print("Unknown menu option.")  # In kết quả (output: kết quả) để đối chiếu với đề.
        except (ValueError, KeyError) as error:  # Bắt ngoại lệ (exception: lỗi) để thông báo rõ.
            print("Input error:", error)  # In kết quả (output: kết quả) để đối chiếu với đề.


if __name__ == "__main__":  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
    if "--demo" in sys.argv:  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
        run_demo()  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.
    else:  # Xử lý trường hợp còn lại.
        interactive_menu()  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.
```
