# Quy trình biên soạn tài liệu

## 1. Nhận bài
Đầu vào tối thiểu: `course_url`, `lesson_id`, nguồn thực tế (transcript, nội dung văn bản, ghi chú, hoặc trang truy cập được).

Nếu chỉ có URL nhưng chưa đọc được nội dung, dừng ở `AWAITING_SOURCE` và không tạo tài liệu như thể đã học xong.

## 2. Phân tích nguồn
Tách các ý chính, thuật ngữ, quy trình, ví dụ, bài tập. Gắn nhãn thông tin thiếu hoặc không rõ. Lưu metadata ở `sources/lesson-index.csv`.

## 3. Soạn thảo
Dùng `templates/lesson.md` và lưu `lessons/<lessonId>-<slug>.md`.
Mỗi bài cần có mục tiêu, bối cảnh, giải thích chi tiết, ví dụ tự xây dựng, thực hành, ôn tập và liên kết nguồn.

## 4. Kiểm tra
Đối chiếu với nguồn, phát hiện bịa đặt, kiểm tra cách dùng thuật ngữ và chất lượng tiếng Việt; chạy thử code mẫu nếu có môi trường phù hợp.
Không sao chép nguyên chương/video/học liệu có bản quyền.

## 5. Git & nghiệm thu
Commit tài liệu đã review, cập nhật index, đánh dấu `READY_FOR_OWNER_TEST`; chủ dự án chỉ cần đọc, góp ý, nghiệm thu.
Sau khi duyệt, đánh dấu `APPROVED`.

## 6. Xuất tài liệu
Markdown là nguồn gốc. DOCX/PDF là bản phát hành xuất từ Markdown; không sửa hai bản độc lập.
Ưu tiên lưu bản xuất có phiên bản và ghi rõ thời điểm.

## Tích hợp AI Bridge (giai đoạn tiếp theo)
Chỉ kết nối Bridge sau khi xác định executor và quyền truy cập nội dung phù hợp. Bridge thực thi theo task JSON có `task_id`, `lesson_id`, `source_uri`, `output_path`, `status`, `evidence`.
Bridge không cần giữ credentials Jetking trong repo; không nhận lệnh shell tùy ý từ tài liệu nguồn.
