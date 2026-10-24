# Chuẩn biên soạn bắt buộc — Curriculum v1

**Áp dụng cho mọi bài mới và khi chỉnh bài cũ.** Mỗi lần tạo bài, agent **phải đọc tệp này và `templates/lesson.md` trước khi viết**, sau đó chạy checklist bên dưới. Không chỉ suy từ một ví dụ PCA hoặc tin rằng ghi nhớ lịch sử là đủ.

## Kết cấu dành cho sinh viên
1. **Bài đang ở đâu trong chuỗi kiến thức?** Trình bày các bài trước → bài hiện tại → bài liên quan, dễ theo dõi.
2. **Từ vựng trong mục:** trước từng mục và tiểu mục, 2–5 thuật ngữ `English — tiếng Việt`; đoạn văn phía sau viết tự nhiên, **không** thêm `(Vietnamese)` sau mỗi lần nhắc. Những bảng thuật ngữ chỉ ghi từ thật sự dùng trong mục.
3. **Thư viện và hàm:** cú pháp, mục đích, các tham số được giải thích cùng hàm (`dtype=float` trong `np.array`, `axis=0` trong các phép thống kê...), không rải quá nhiều chú thích tham số khắp code.
4. **Khái niệm và khái niệm liên quan:** giải thích trước bằng tiếng Việt phổ thông → một ví dụ nhỏ có dữ liệu và đơn vị → code Python → giải thích kết quả → câu tự kiểm tra với đáp án. Không có mục chứng minh toán học, mục tiêu dành cho giảng viên hoặc chữ “Subconcept”.
5. **5 tình huống thực tế:** mỗi tình huống có hoàn cảnh, vấn đề, vì sao chọn cách giải này (so với phương án khác), trình tự xử lý, dữ liệu (mỗi hàng, cột, đơn vị, giả lập hay thật), chương trình chạy được với comment giải thích lý do từng bước, đầu ra/cách tự kiểm chứng và giới hạn sử dụng.
6. **20 câu trắc nghiệm Anh–Việt** với mỗi câu và **bản dịch trên CÙNG MỘT DÒNG**, ví dụ: `**Q1. What is a vector? — Vector là gì?**`. Mỗi phương án nằm trên **một dòng**: `A. A sequence of numbers — Một dãy số`. Đủ 4 lựa chọn cho một câu. Phần answer key là bảng 4 cột: `Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt)`. Không viết một dòng dịch tách dưới câu hỏi/phương án.
7. **Nối sang bài kế tiếp:** giải thích mối liên hệ trong chuỗi kiến thức, không ép hiểu thuật toán nâng cao trước khi học nền.
8. Hình minh họa khi có ích phải là file SVG/PNG có thật, đường dẫn tương đối **đúng chính xác** với file Markdown và kiểm tra tồn tại. Không chỉnh tên file trong quá trình dịch thuật. Nếu ảnh được tạo từ dữ liệu thì phải khớp tọa độ/số liệu.
9. **Markdown là bản gốc**. PDF sau này phát hành riêng ở `exports/pdf/`, bảo toàn bảng/hình/code/dấu tiếng Việt và được render kiểm tra trước khi công bố.

## Nguồn nội bộ, coverage và chất lượng
- Chỉ sử dụng nội dung kiến thức có căn cứ từ source code/notebook/bài tập đã đọc. **Không nhắc tên repository ghi chép trong bài dành cho sinh viên.** Nguồn từng mục, source commit và vấn đề chỉnh sửa được ghi tại `sources/` và bản đồ coverage nội bộ.
- Không sao chép nguyên ví dụ sai ở ghi chép; tái tạo tình huống đúng cú pháp và logic.
- Khi nguồn DOCX/PPTX/XLSX/binary chưa trích xuất được: ghi `SOURCE_UNREAD` trong coverage, không khẳng định đã bao phủ nội dung bên trong. Phân biệt `DRAFT`, `CODE_VERIFIED`, `EDITOR_REVIEWED`, `APPROVED`.
- Agent kiểm tra cấu trúc và syntax của từng đoạn code; chỉ công bố `CODE_VERIFIED` khi thực sự chạy và kiểm tra kết quả. Tất cả lệnh cần thư viện cài ngoài phải ghi rõ điều kiện cài đặt.
- 20 câu phải liên quan trực tiếp bài, không chèn trắc nghiệm chung chung về chủ đề khác. Đáp án đúng có giải thích kỹ thuật.

## Quy trình vận hành không phụ thuộc bộ nhớ hội thoại
Trước mỗi bài: mở `docs/CURRICULUM-STYLE-GUIDE.md` → `templates/lesson.md` → coverage ledger của nguồn → lên cấu trúc và viết → kiểm tra hình/code/20 QA → cập nhật ledger và trạng thái. Tuyệt đối không bỏ bước guide khi tác vụ được giao tự động cho worker mới.

## Về việc mở rộng toàn giáo trình
Chủ dự án **đã trực tiếp yêu cầu tạo tất cả bài còn lại ngày 2026-10-24**, không còn giữ cổng chờ phê duyệt cho việc tạo các bản thảo. Tuy nhiên, **cho phép tạo ≠ coi là đã kiểm định**: cần phân biệt bản thảo với bài được chạy unit test và review. Không tự kích hoạt Bridge hoặc restart worker chỉ vì tài liệu này được cập nhật.
