# AIClassDocuments — Tài liệu tự học Python và AI

**Định hướng:** Tài liệu giúp sinh viên hệ thống hóa kiến thức Python, xử lý dữ liệu và AI, đặt mỗi khái niệm đúng vị trí trong chuỗi học, có ví dụ code và bài toán thực tế. Nguồn phục vụ biên tập được quản lý riêng ở tài liệu dự án.

Bài học đi theo thứ tự: **chuỗi kiến thức → từ vựng Anh–Việt theo từng mục → thư viện và hàm Python → các khái niệm với ví dụ → năm tình huống thực tế → 20 câu trắc nghiệm song ngữ và đáp án**. Các phép tính được thể hiện ngay trong Python; không có phần chứng minh toán học hoặc mục tiêu giáo án.

## Giáo trình đã có bản thảo
**[AI-MATH-01 — PCA: Phân tích thành phần chính](lessons/pilot/AI-MATH-01-pca.vi.md)**

Bài PCA là mẫu được dùng để định hình quy chuẩn. **46 chương khác** đã được tạo ở [mục lục giáo trình](lessons/chapters/README.md). Những chương mới được đánh dấu **DRAFT** để phân biệt với học liệu đã kiểm định code và nội dung.

## Cấu trúc
- `AGENTS.md`: quy tắc cho Architect/Document Author và giữ tính an toàn Bridge.
- `docs/PYTHOCLASS-CURRICULUM.md`: quy trình chuẩn hóa bài học, quyền hạn và cổng nghiệm thu.
- `sources/pythoclass-file-inventory.csv`: bảng nguồn ban đầu 65 file (lịch sử).
- `sources/curriculum-source-coverage.csv`: bảng nguồn mới 68 file, có trạng thái phần nào đã xem, chưa đọc sâu hoặc là binary chưa phân tích.
- `sources/pythoclass-topic-map.md`: bản đồ chủ đề ban đầu — **chưa coi là bao phủ hoàn tất**.
- `templates/lesson.md`: mẫu mỗi bài.
- `docs/CURRICULUM-STYLE-GUIDE.md`: **phải đọc trước mỗi lần tạo bài**; có hợp đồng trắc nghiệm song ngữ trên cùng một dòng.
- `docs/CURRICULUM-QA-STATUS.md`: bằng chứng kiểm tra cấu trúc và giới hạn kiểm định.
- `lessons/chapters/README.md`: mục lục 46 chương bản thảo.
- `exports/pdf/`: thư mục dành cho PDF phát hành (khác nơi lưu Markdown); chưa xuất PDF ở giai đoạn này.
- `lessons/pilot/`: bài PCA tham chiếu cách trình bày.
- `lessons/chapters/`: 46 chương khác ở trạng thái DRAFT, chưa coi là kiểm định.
- `docs/JETKING-*`, `sources/lesson-index.csv`: lịch sử Jetking được giữ để truy vết; **không phải nguồn giáo trình hiện tại**.

## Trình tự triển khai
1. Bắt buộc đọc `docs/CURRICULUM-STYLE-GUIDE.md` và mẫu bài trước khi tạo/chỉnh giáo trình.
2. Dùng [mục lục 46 bài](lessons/chapters/README.md) và [coverage ledger](sources/curriculum-source-coverage.csv) để tránh bỏ sót khái niệm nhỏ.
3. **Rà các bài DRAFT**: tiếp tục đọc file nguồn chưa trích xuất, kiểm tra cú pháp/đầu ra code, kiến thức và câu trắc nghiệm; chỉ chuyển sang trạng thái đã kiểm định khi có bằng chứng.
4. Khi cần, xuất PDF riêng vào `exports/pdf/` và kiểm tra hình, bảng, code và dấu tiếng Việt trước khi phát hành.

Không sửa PythoClass; không truy cập lại Jetking chỉ vì nhiệm vụ mới; không tự kích hoạt task Bridge khi chưa có việc đủ điều kiện.
