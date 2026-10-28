# Hiệu chuẩn câu hỏi trắc nghiệm theo mẫu 16 câu của giảng viên

**Ngày:** 28/10/2026  
**Nguồn so sánh:** 16 câu trắc nghiệm do người học cung cấp, được cho biết là tài liệu giảng viên FPT Jetking phát. **Không khẳng định đây là cấu trúc đề thi chính thức hoặc câu sẽ xuất hiện trong kỳ thi.**

## Mức độ tư duy mục tiêu

- Mỗi câu thường có thể xử lý trong khoảng **30–45 giây**; số lớn vừa phải, đủ để tính nhẩm hoặc tính nhanh trên giấy.
- Ưu tiên: hiểu nghĩa khái niệm; một đến hai phép toán vector, ma trận, đạo hàm, xác suất, thống kê; nhận biết kết luận sai/đúng (định thức bằng 0, learning rate quá lớn, p-value và Bayes).
- Bốn đáp án có cùng kiểu trả lời, chỉ một đáp án đúng; đáp án sai phải là sai lầm hợp lý (nhầm phép cộng với nhân, quên chia tổng số, đảo điều kiện Bayes).
- Giải thích ngắn nhưng nêu rõ **tại sao** và bước tính hoặc lập luận; giữ câu hỏi Anh–Việt và mỗi lựa chọn Anh–Việt.
- **Không xóa kiến thức API NumPy, Pandas, SymPy** khỏi phần lý thuyết, demo hoặc các câu trắc nghiệm khác: mục tiêu là nâng tỷ lệ bài kiểm tra tư duy, không làm mất chương trình Python tự học.

## Phạm vi đã điều chỉnh

Chỉ cập nhật mục **7. Trắc nghiệm** của **17 lesson PY-24–PY-40** (Toán/AI):

- Thay nội dung **Q5, Q6, Q7, Q8** ở mỗi bài bằng câu vận dụng cùng mức độ với mẫu: **68 câu**.
- Sắp xếp lại thứ tự bốn lựa chọn của cả 20 câu/bài (**340 câu**) để tránh quy luật đáp án A–B–C–D lặp; cập nhật ký tự đáp án nhưng giữ nguyên nội dung lựa chọn đúng.
- Giữ **20 câu/lesson, 4 lựa chọn, 1 đáp án, 1 giải thích**, và nguyên các phần 1–6, 8 cùng toàn bộ code, hình ảnh, tình huống và lý thuyết.
- Các lesson **PY-01–PY-23 và PY-41–PY-46** giữ nguyên, vì nguồn 16 câu mẫu tập trung vào kiến thức Toán–Xác suất–Thống kê nền tảng.
- 16 câu giảng viên cung cấp vẫn nằm riêng trong `exports/markdown/AIClassDocuments-16-CauBoSung-20261028.vi.md`; không tự nhận câu được biên soạn là đề thật.

## Kiểm tra

- `python -m unittest tests.test_curriculum_structure tests.test_jetking_mcq_level -v` xác nhận số câu, cách trình bày song ngữ, cú pháp Markdown đáp án và **đúng nội dung đáp án của cả 68 câu mới**, bất kể chữ A–D sau khi đảo.
- Workflow `export_quiz_pdf.yml` xuất lại **920 câu trong 46 lesson**, sau đó **936 câu có 16 câu mẫu**, và **10 đề luyện 160 câu** trong cùng một lần chạy để tránh PDF bị lệch phiên bản.

**Nguyên tắc bảo trì:** Khi nhận thêm đề mẫu từ giảng viên, kiểm tra logic đáp án rồi chỉ cập nhật những câu lệch mức độ. Không tự suy đoán đề thi thật.
