# AIClassDocuments — Tài liệu tự học Python và AI

**Định hướng:** Tài liệu giúp sinh viên hệ thống hóa kiến thức Python, xử lý dữ liệu và AI, đặt mỗi khái niệm đúng vị trí trong chuỗi học, có ví dụ code và bài toán thực tế. Nguồn phục vụ biên tập được quản lý riêng ở tài liệu dự án.

Bài học đi theo thứ tự: **chuỗi kiến thức → từ vựng Anh–Việt theo từng mục → thư viện và hàm Python → các khái niệm với ví dụ → năm tình huống thực tế → 20 câu trắc nghiệm song ngữ và đáp án**. Các phép tính được thể hiện ngay trong Python; không có phần chứng minh toán học hoặc mục tiêu giáo án.

## Bài mẫu chờ góp ý
**[AI-MATH-01 — PCA: Phân tích thành phần chính](lessons/pilot/AI-MATH-01-pca.vi.md)**

Bài thử có hình minh họa PCA trước/sau từ dữ liệu chạy thật, câu tự kiểm tra ngay sau các nhóm khái niệm, năm tình huống thực tế bằng Python có chú thích lý do, và 20 câu trắc nghiệm Anh–Việt kèm đáp án song ngữ. Các thuật toán mở rộng được đánh dấu để sinh viên đọc sau. Đây chỉ là **pilot**; chưa nhân rộng toàn bộ giáo trình trước khi duyệt.

## Cấu trúc
- `AGENTS.md`: quy tắc cho Architect/Document Author và giữ tính an toàn Bridge.
- `docs/PYTHOCLASS-CURRICULUM.md`: quy trình chuẩn hóa bài học, quyền hạn và cổng nghiệm thu.
- `sources/pythoclass-file-inventory.csv`: inventory 65 file được ghim theo source commit.
- `sources/pythoclass-topic-map.md`: bản đồ chủ đề ban đầu — **chưa coi là bao phủ hoàn tất**.
- `templates/lesson.md`: mẫu mỗi bài.
- `exports/pdf/`: thư mục dành cho PDF phát hành (khác nơi lưu Markdown); chưa xuất PDF ở giai đoạn này.
- `lessons/pilot/`: bài mẫu cần góp ý; chỉ chuyển sang bài chính sau nghiệm thu.
- `docs/JETKING-*`, `sources/lesson-index.csv`: lịch sử Jetking được giữ để truy vết; **không phải nguồn giáo trình hiện tại**.

## Trình tự triển khai
1. Đọc đầy đủ PythoClass, lập bảng khái niệm từ tất cả file nguồn.
2. Biên soạn + kiểm thử **một bài PCA** và nhận góp ý owner.
3. Khi pilot được duyệt: phân chia toàn bộ thành các bài có prereq và coverage, triển khai theo chủ đề, có kiểm thử code.
4. Review bài trong Markdown; khi cần, xuất PDF riêng vào `exports/pdf/` và kiểm tra các hình, bảng, code, dấu tiếng Việt trước khi phát hành.

Không sửa PythoClass; không truy cập lại Jetking chỉ vì nhiệm vụ mới; không tự kích hoạt task Bridge khi chưa có việc đủ điều kiện.
