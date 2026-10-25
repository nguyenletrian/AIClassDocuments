# Bộ LAB gốc — PythoClass

Mỗi folder tương ứng với **một đề Word cụ thể** trong repository PythoClass, được tách thành các tệp:

| File | Nội dung |
|---|---|
| `LAB.md` | Đề gốc từ Word chuyển sang Markdown, bao gồm dữ liệu, câu hỏi và bảng; ghi rõ các sai lệch của đề nếu có |
| `DEMO.py` | **Code do chủ dự án đã viết** trong notebook/script PythoClass tương ứng, giữ các phần thử nghiệm và comment để truy nguyên; **không phải lời giải chuẩn** |
| `KNOWLEDGE.md` | Kiến thức cần có, giải thích, lỗi hay gặp và liên kết sang các chương giáo trình |
| `SOLUTION.py` | Lời giải tham khảo đầy đủ, tách khỏi bản Demo |
| `students.csv` | Riêng Lab 10: 10 dòng dữ liệu học viên giả lập để thử file I/O |

## Danh sách

| Lab gốc | Thư mục | Bài học liên quan |
|---|---|---|
| `Ass 1.docx` | [Assignment 1](ASSIGNMENT-01-student-dictionary/LAB.md) | PY-08, PY-09, PY-44 |
| `LAB Session 4.docx` | [Lab Session 4](LAB-04-conditions-loops/LAB.md) | PY-03 đến PY-05 |
| `Lab Session 5.docx` | [Lab Session 5](LAB-05-student-list/LAB.md) | PY-05, PY-06, PY-09 |
| `LAB SESSION 5_6.docx` | [Lab Session 5 & 6](LAB-05-06-gradient-descent/LAB.md) | PY-24, PY-28 đến PY-33 |
| `LAB SESSION 7.docx` | [Lab Session 7](LAB-07-probability/LAB.md) | PY-34 đến PY-36 |
| `LAB SESSION 8.docx` | [Lab Session 8](LAB-08-statistics/LAB.md) | PY-37 đến PY-40 |
| `Lab Session 10.docx` | [Lab Session 10](LAB-10-file-csv/LAB.md) | PY-12, PY-44 |

## Phân biệt 4 file

**LAB.md** là yêu cầu bài gốc; **DEMO.py** là code học viên từng làm (có thể chưa đúng, chưa đủ, cần chạy từng đoạn); **KNOWLEDGE.md** diễn giải cách làm; **SOLUTION.py** là lời giải tham khảo có kiểm tra.

## Nguồn và quyền riêng tư

Nguồn: `nguyenletrian/PythoClass`, 7 tệp DOCX và các notebook/script tương ứng. Repository nguồn được giữ nguyên. Vì AIClassDocuments công khai, tên học viên trong ví dụ và code được thay bằng mã/tên giả khi có nguy cơ lộ danh tính. **Đề Lab 4 có một ví dụ tiền điện không khớp bảng giá**, đã được chú thích thay vì sửa âm thầm. `LAB SESSION 5_6.docx` có một bản trùng dưới `MON 2/`; chỉ lập một bộ lab.

Không chèn trực tiếp 13 bộ bài tập tự sinh của đợt trước vào bộ này. Mục tiêu là **đối chiếu từng lab Word với code thực tế bạn đã viết**.
