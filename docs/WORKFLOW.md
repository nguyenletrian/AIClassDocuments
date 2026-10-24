# Workflow — PythoClass → Giáo trình Python/AI

## 1. Kiểm kê
Chốt source commit PythoClass và kiểm tra danh sách **65 file** tại `sources/pythoclass-file-inventory.csv`. Phải đọc code và comments, notebook cells, DOCX/PPTX/XLSX nếu có nội dung học; phân biệt file dữ liệu, bài tập và tài liệu lịch.

## 2. Tách khái niệm
Với **mỗi chủ đề nhỏ**: ghi `concept_id`, khái niệm, file/cell nguồn, chương dự kiến, prerequisite, trạng thái. Không bỏ qua đề mục chỉ nhắc một câu. Đánh dấu trùng nội dung giữa các file, tránh viết lặp.

## 3. Biên soạn
Dùng `templates/lesson.md`. Phần yêu cầu:
- Khái niệm và trực giác
- Mục đích và giới hạn
- Công thức (khi có) + đơn vị/ký hiệu
- Thư viện và cách dùng Python
- Ứng dụng AI thực tế
- Khoảng năm bài tập chương trình, có đề, lời giải/check, nâng cấp
- Lỗi phổ biến, self-test, nguồn, phần hiệu đính và phần mở rộng

## 4. Tự kiểm
Rà nguồn/logic/toán; chạy code trong môi trường được phép, kiểm chứng kết quả, đường dẫn và bản quyền; ghi hạn chế. Không coi output notebook cũ là bằng chứng code đúng.

## 5. Pilot gate
Lúc này **chỉ có PCA pilot**. Cập nhật từ góp ý owner trước khi làm 64/65 file còn lại. `goal_review.enabled=false`; Bridge không tự khởi động viết hàng loạt từ idle reminder.

## 6. Sau khi nghiệm thu
Hoàn thiện concept index, lập thứ tự prerequisite, chia việc theo lô; các bài mới từ `DRAFT` → `SELF_REVIEW` → `READY_FOR_OWNER_TEST` → `APPROVED`. Mỗi bài cập nhật coverage và commit riêng để có thể trace lại nguồn.

## Hệ thống cũ
Jetking được giữ dưới dạng tài liệu/hồ sơ lịch sử, không xóa và không dùng làm nguồn giảng dạy PythoClass khi chưa được yêu cầu riêng.
