# AIClassDocuments — Giáo trình Python ứng dụng AI từ PythoClass

**Mục tiêu mới (24/10/2026):** Dựa trên toàn bộ ghi chép, lab, bài tập và code tại [PythoClass](https://github.com/nguyenletrian/PythoClass), biên soạn thành bài học Python + Toán + AI chính xác, dễ đọc, có tính thực hành và truy nguyên nguồn.

Không chỉ viết lại ghi chép: dự án phải giải thích **khái niệm, mục đích, công thức (nếu có), thư viện, cách sử dụng trong Python, ứng dụng thực tế trong AI và khoảng 5 bài tập lập trình** cho mỗi bài. Mọi khái niệm trong nguồn, kể cả chỉ được nhắc ngắn, đều có vị trí trong bản đồ giáo trình.

## Bài mẫu chờ góp ý
**[AI-MATH-01 — PCA: Phân tích thành phần chính](lessons/pilot/AI-MATH-01-pca.vi.md)**

Bài thử này dùng ba script PythoClass, trình bày toán nền tảng và năm bài tập Python đã được chạy đối chiếu. Đây chỉ là **pilot**; chưa nhân rộng toàn repo trước khi owner duyệt.

## Cấu trúc
- `AGENTS.md`: quy tắc cho Architect/Document Author và giữ tính an toàn Bridge.
- `docs/PYTHOCLASS-CURRICULUM.md`: quy trình chuẩn hóa bài học, quyền hạn và cổng nghiệm thu.
- `sources/pythoclass-file-inventory.csv`: inventory 65 file được ghim theo source commit.
- `sources/pythoclass-topic-map.md`: bản đồ chủ đề ban đầu — **chưa coi là bao phủ hoàn tất**.
- `templates/lesson.md`: mẫu mỗi bài.
- `lessons/pilot/`: bài mẫu cần góp ý; chỉ chuyển sang bài chính sau nghiệm thu.
- `docs/JETKING-*`, `sources/lesson-index.csv`: lịch sử Jetking được giữ để truy vết; **không phải nguồn giáo trình hiện tại**.

## Trình tự triển khai
1. Đọc đầy đủ PythoClass, lập bảng khái niệm từ tất cả file nguồn.
2. Biên soạn + kiểm thử **một bài PCA** và nhận góp ý owner.
3. Khi pilot được duyệt: phân chia toàn bộ thành các bài có prereq và coverage, triển khai theo chủ đề, có kiểm thử code.
4. Review bài và cung cấp phiên bản Markdown; xuất DOCX/PDF khi cần.

Không sửa PythoClass; không truy cập lại Jetking chỉ vì nhiệm vụ mới; không tự kích hoạt task Bridge khi chưa có việc đủ điều kiện.
