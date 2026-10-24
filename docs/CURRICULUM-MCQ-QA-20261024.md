# Rà soát trắc nghiệm song ngữ — 24/10/2026

## Phạm vi rà soát

- Đọc và đối chiếu câu hỏi với **phương án được khoanh** ở tất cả 46 bài PY-01–PY-46: tổng 920 câu, 3.680 lựa chọn, 920 dòng đáp án.
- Soát cấu trúc bốn lựa chọn Anh–Việt/câu, đánh số, chữ cái A–D, trùng nguyên văn, tham chiếu tình huống đánh số và dấu phân cột Markdown. Đây là **QA cấu trúc**, không phải bằng chứng tự động rằng mọi lựa chọn sai về mặt ngữ nghĩa.
- Với PY-41–PY-46: viết mới 120 câu lý thuyết có đáp án liên quan trực tiếp nội dung bài; kiểm tra lại key/choices và mở rộng 120 lời giải thích thành tối thiểu hai ý bằng mỗi ngôn ngữ, nêu nguyên lý và nhầm lẫn gần.
- Với PY-01–PY-40: rà tính phù hợp của phương án được chọn với câu hỏi; những lời giải thích còn ngắn **chưa được biên tập đồng loạt thành hai ý**. Rà toàn bộ ba phương án nhiễu về ngữ nghĩa và chất lượng sư phạm vẫn cần vòng độc lập trước phát hành.

## Phát hiện và sửa chữa có bằng chứng

| Bài | Phát hiện | Khắc phục |
|---|---|---|
| PY-07 Q9 (PR #102) | Dấu `&#124;` trong bảng đáp án tạo các cột Markdown sai | Escape bằng entity `&#124;`, giải thích rõ hợp so với giao |
| PY-20 Q4 (PR QA) | Từ "independent choices" ở nguyên lý nhân đếm dễ bị hiểu nhầm là độc lập xác suất | Sửa điều kiện đếm theo số lựa chọn nối tiếp hợp lệ, nêu rõ không cần độc lập xác suất |
| PY-41 Q13 và Q19 | Cách hỏi chưa khớp chính xác với kiểu đáp án | Viết lại câu hỏi để chỉ có một cách hiểu |
| PY-42 | Biểu thức Jaccard gốc bị thiếu cú pháp/mẫu số | Sửa `len(a & b) / len(a | b)`, xử lý hợp rỗng bằng quy ước rõ |
| PY-41–46 | Giải thích đáp án quá ngắn theo chuẩn mới | Thêm phân biệt, ví dụ hoặc hệ quả riêng cho từng câu Anh–Việt |

## Những thay đổi đồng thời

Guide kiểm tra tính đúng theo nghĩa đã được merge riêng tại **PR #101**. Bản sửa bảng đáp án PY-07 Q9 đã merge tại **PR #102**. Nhánh rà soát này giữ nguyên hai kết quả trên và chỉ bổ sung bản ghi QA cùng sửa khái niệm đếm ở PY-20.

## Chuẩn duyệt trước khi phát hành

1. Không coi kiểm tra đủ số câu là đã xác nhận đáp án đúng. Mỗi câu cần người duyệt độc lập kiểm tra phát biểu, ba distractor và đáp án; câu có điều kiện thiếu phải sửa trước khi phát hành.
2. Đối với câu tính toán/output, chạy code hoặc phép tính độc lập; không đoán kết quả từ tên hàm.
3. Kiểm bảng Markdown bốn cột và kết quả Python ngay dưới mỗi khối; code cần được thử trên môi trường đích khi phát hành.
4. Các bản sửa hiện tại được thực hiện qua GitHub; **chưa phải chứng nhận QA runtime trên Windows**, và chưa phải duyệt học thuật độc lập toàn bộ 920 câu.

