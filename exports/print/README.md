# Bộ tài liệu Lab và bài tập để in

Bộ soạn **10 tài liệu độc lập**, một file Markdown cho mỗi bài, dựa trên đề và bài giải đã có, ưu tiên đối chiếu nguồn gốc tại [PythoClass](https://github.com/nguyenletrian/PythoClass) và kho [AIClassDocuments](https://github.com/nguyenletrian/AIClassDocuments).

## File nguồn có thể chỉnh sửa

- **[Toàn bộ 10 Lab trong một file Markdown](AIClassDocuments-TongHop-10-Lab-BaiTap.md)** — file chữ gốc, có đầy đủ năm phần từng bài, chỉnh sửa trong VS Code hoặc trình soạn thảo Markdown.
- **[Toàn bộ 10 Lab trong một file Word](source/AIClassDocuments-TongHop-10-Lab-BaiTap.docx)** — bản `.docx` A4 ngang, có thể sửa bằng Microsoft Word/LibreOffice; được xuất tự động từ file Markdown tổng hợp.

## Tải một file PDF tổng hợp

**[AIClassDocuments - Tổng hợp 10 Lab và Bài tập, A4 ngang](pdf/AIClassDocuments-TongHop-10-Lab-BaiTap-A4-Ngang.pdf)** — một file **75 trang** để in toàn bộ, có mục lục, khoảng trang của từng bài và **61 dấu trang PDF** cho cả năm phần trong mỗi bài. Bản tổng hợp ghép nguyên các trang từ 10 file PDF riêng, không làm thay đổi code, lời giải hoặc định nghĩa.

Để xuất lại cả bộ từ nội dung Markdown mới nhất:

```bash
python scripts/export_lab_print_pdf.py
python scripts/combine_lab_print_pdfs.py
```

## Thứ tự cố định trong mỗi file

1. **Đề bài tiếng Anh** — toàn bộ nội dung đề; không tự cắt bớt các câu hỏi.
2. **Đề bài tiếng Việt** — dịch cùng thứ tự, giải thích các thuật ngữ khó ở ngữ cảnh phù hợp.
3. **Code Python có chú thích chọn lọc** — **một khối code duy nhất** cho cả bài (không còn snippet code lặp ở phần giải thích), chỉ ghi chú cạnh những thuật toán, thư viện/hàm và tham số dễ nhầm; không dùng `assert` trong bản in.
4. **Giải thích nội dung và cách giải** — sau code, diễn giải kỹ từng bước bằng lời và phép tính số cụ thể; không chèn thêm code rời.
5. **Giải thích các định nghĩa** — cuối cùng, mỗi khái niệm/hàm/thuật ngữ có lời giải thích bình dân và ví dụ để học viên tự tính; giải nghĩa các ký hiệu như `n`, `i`, `Σ`, `y`, `ŷ`, `ddof`, PCA, Bayes và Jaccard khi xuất hiện.

Từng file là nguồn Markdown sẵn để kết xuất ra PDF A4. Bản gốc trong `docs/labs/`, `labs/pythoclass/` và kho `PythoClass` **không bị chỉnh sửa**.

## Danh mục

| Nhóm | Bài | File để in |
|---|---|---|
| Bài tập | Assignment 1 — Dictionary | [ASSIGNMENT-01](exercises/ASSIGNMENT-01.md) |
| Lab | Lab 04 — Điều kiện, vòng lặp | [LAB-04](labs/LAB-04.md) |
| Lab | Lab 05 — List và sinh viên | [LAB-05](labs/LAB-05.md) |
| Lab | Lab 05–06 — Hồi quy và Gradient Descent | [LAB-05-06](labs/LAB-05-06.md) |
| Lab | Lab 07 — Xác suất | [LAB-07](labs/LAB-07.md) |
| Lab | Lab 08 — Thống kê | [LAB-08](labs/LAB-08.md) |
| Lab | Lab 10 — CSV và phân tích điểm | [LAB-10](labs/LAB-10.md) |
| Bài tập | Pretest — Điểm, xác suất, Gradient Descent | [PRETEST](exercises/PRETEST.md) |
| Bài tập Toán | Math 02 — Set, Jaccard, graph | [LAB-MATH-02](exercises/LAB-MATH-02.md) |
| Bài tập Toán | Math 03–04 — Matrix, PCA | [LAB-MATH-03-04](exercises/LAB-MATH-03-04.md) |

## Đối chiếu với nguồn từ PythoClass

| Bài | Đề/dữ liệu nguồn | Nguồn code trong bản in |
|---|---|---|
| Assignment 1 | `PythoClass/Ass 1.docx` | Bản hoàn chỉnh trong `docs/labs/ASSIGNMENT-01-student-dictionary.md` |
| Lab 04 | `PythoClass/LAB Session 4.docx` | Bản hoàn chỉnh trong `docs/labs/LAB-04-conditions-loops.md` |
| Lab 05 | `PythoClass/Lab Session 5.docx` | Bản hoàn chỉnh trong `docs/labs/LAB-05-student-list.md` |
| Lab 05–06 | `PythoClass/LAB SESSION 5_6.docx` | Bản hoàn chỉnh trong `docs/labs/LAB-05-06-gradient-descent.md` |
| Lab 07 | `PythoClass/LAB SESSION 7.docx` | Bản hoàn chỉnh trong `docs/labs/LAB-07-probability.md` |
| Lab 08 | `PythoClass/LAB SESSION 8.docx` | Bản hoàn chỉnh trong `docs/labs/LAB-08-statistics.md` |
| **Lab 10** | `PythoClass/Lab Session 10.docx` | **`PythoClass/main.py`** (SHA `13357fe148ed82a8ac73812f627de749ceedf9e4`), giữ logic mã nguồn và bổ sung chú thích |
| Pretest | `PythoClass/Pretest.docx` | Bản hoàn chỉnh trong `docs/labs/PRETEST.md` |
| Math 02 | `PythoClass/2. Math/labs2.ipynb` | `labs/pythoclass/LAB-MATH-02-sets-jaccard/SOLUTION.py`, tái cấu trúc từ notebook |
| Math 03–04 | `PythoClass/2. Math/labs3_4.ipynb` | `labs/pythoclass/LAB-MATH-03-04-matrix-pca/SOLUTION.py`, tái cấu trúc từ notebook |

**Phân biệt rõ:** Đề Word Lab 10 yêu cầu *thêm và lưu sinh viên*, trong khi `main.py` có các chức năng *phân tích theo môn/lớp và top 3*. Tài liệu [LAB-10](labs/LAB-10.md) giải thích khác biệt này ở cuối và ghi chú rằng code cần `students.csv` gốc với cột `" name"` có dấu cách đầu. Không tuyên bố code đó đáp ứng toàn bộ đề Word.

**Hai bài Math:** Notebook gốc có tiêu đề các nhiệm vụ và cell code, không có đề Word song ngữ đầy đủ; phần diễn giải đề Anh–Việt là bản tái dựng bám theo notebook, không ghi là dịch nguyên văn đề gốc. Tên học viên trong các bộ code tham khảo được thay bằng tên minh họa.

## In thành PDF

Có thể xuất tự động các file trong danh mục bằng lệnh:

```bash
python scripts/export_lab_print_pdf.py
```

Tệp PDF tương ứng nằm trong `exports/print/pdf/`; kích thước trang **A4 nằm ngang, đúng MỘT cột trên toàn chiều ngang trang** để dễ đọc code, có tiêu đề bài và số trang. Bài có dữ liệu đầu vào dạng bảng/CSV có thể giữ khối dữ liệu minh họa, nhưng chỉ có **một chương trình Python hoàn chỉnh**. Không cần sửa file nguồn để đổi bố cục PDF.

**Nếu bạn cập nhật `PythoClass/main.py` về sau:** so sánh nội dung nguồn trước khi cập nhật bản in; không ghi đè tự động những chỉnh sửa có ý nghĩa mà chưa đối chiếu.

## Quy tắc trình bày công thức

Trong mọi file in, **không để nguyên mã LaTeX** như `$$`, `\\frac`, `\\sum`, `\\hat` hoặc các khối `\\[ ... \\]`. Thay bằng phép tính có từ ngữ bình dân và một ví dụ số: *bắt đầu từ dữ liệu nào, thực hiện các phép tính nào, chia cho số lượng nào, ý nghĩa kết quả là gì*. Phần ký hiệu toán học cần thiết được giải nghĩa ở mục 5 thay vì giả định người học đã biết.

Các bài vẫn giữ **đề Anh–Việt, một khối code Python, A4 ngang một cột**, và mã nguồn bài giải gốc không bị thay đổi.
