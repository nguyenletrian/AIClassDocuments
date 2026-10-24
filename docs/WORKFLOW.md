# Workflow — PythoClass → Giáo trình Python/AI

## 1. Kiểm kê
Chốt source commit và kiểm tra **68 file** tại `sources/curriculum-source-coverage.csv` ở phiên bản nguồn ngày 24/10/2026. Bảng 65 file ban đầu được lưu lại để đối chiếu lịch sử. Phải đọc code và comments, notebook cells, DOCX/PPTX/XLSX nếu có nội dung học; phân biệt file dữ liệu, bài tập và tài liệu lịch.

## 2. Tách khái niệm
Với **mỗi chủ đề nhỏ**: ghi `concept_id`, khái niệm, file/cell nguồn, chương dự kiến, prerequisite, trạng thái. Không bỏ qua đề mục chỉ nhắc một câu. Đánh dấu trùng nội dung giữa các file, tránh viết lặp.

## 3. Biên soạn
**Bắt buộc đọc `docs/CURRICULUM-STYLE-GUIDE.md` và `templates/lesson.md` trước mỗi bài.** Phần yêu cầu:
- Khái niệm và trực giác
- Mục đích và giới hạn
- Công thức (khi có) + đơn vị/ký hiệu
- Thư viện và cách dùng Python
- Ứng dụng AI thực tế
- Khoảng năm bài tập chương trình, có đề, lời giải/check, nâng cấp
- Lỗi phổ biến, self-test, nguồn, phần hiệu đính và phần mở rộng

## 4. Tự kiểm
Rà nguồn/logic/toán; chạy code trong môi trường được phép, kiểm chứng kết quả, đường dẫn và bản quyền; ghi hạn chế. Không coi output notebook cũ là bằng chứng code đúng.

## 5. Tạo bản thảo toàn bộ chương trình
Theo yêu cầu trực tiếp của chủ dự án ngày 24/10/2026, **đã tạo 46 bài DRAFT ngoài bài PCA tham chiếu**. Bản thảo chưa phải bài học đã thử code/đã kiểm định từng câu hỏi. Có thể tiếp tục hiệu đính theo guide mà không cần chờ phê duyệt mẫu nữa. `goal_review.enabled=false` tiếp tục được giữ để tránh nhắc vô ích; không có task Bridge tự phát từ heartbeat.

## 6. Kiểm định và phát hành
Hoàn thiện concept index, đọc các nguồn binary chưa phân tích, rà từng ví dụ và câu hỏi; các bài mới đi từ `DRAFT` → `CODE_VERIFIED` → `EDITOR_REVIEWED` → `APPROVED`. Mỗi bài cập nhật coverage và commit riêng để có thể trace lại nguồn.

## Hệ thống cũ
Jetking được giữ dưới dạng tài liệu/hồ sơ lịch sử, không xóa và không dùng làm nguồn giảng dạy PythoClass khi chưa được yêu cầu riêng.
