# Chuẩn biên soạn bắt buộc — Curriculum v2 (biên tập tinh gọn)

**Áp dụng cho mọi bài mới và khi chỉnh bài cũ.** Mỗi lần tạo bài, agent **phải đọc tệp này và `templates/lesson.md` trước khi viết**, sau đó chạy checklist bên dưới. Không chỉ suy từ một ví dụ PCA hoặc tin rằng ghi nhớ lịch sử là đủ.

## Kết cấu dành cho sinh viên
1. **Bài đang ở đâu trong chuỗi kiến thức?** Trình bày các bài trước → bài hiện tại → bài liên quan, dễ theo dõi.
2. **Từ vựng:** giải thích thuật ngữ Anh–Việt một lần trong bảng đầu bài. Chỉ nhắc lại tại mục con nếu có nghĩa mới hoặc cần phân biệt; không tạo một dòng `Từ vựng trong mục` lặp lại cùng một từ ở mọi mục/tình huống.
3. **Thư viện và hàm:** cú pháp, mục đích, các tham số được giải thích cùng hàm (`dtype=float` trong `np.array`, `axis=0` trong các phép thống kê...), không rải quá nhiều chú thích tham số khắp code.
4. **Khái niệm:** giải thích ngắn bằng tiếng Việt dễ hiểu → code minh họa → đầu ra/kết luận cụ thể khi có ích. Chỉ dùng tự kiểm tra nếu thực sự vận dụng kiến thức, **không hỏi lại định nghĩa y hệt vừa nêu**. Không có mục chứng minh toán học, mục tiêu dành cho giảng viên hoặc chữ “Subconcept”.
5. **5 tình huống thực tế:** tên vấn đề nằm trong tiêu đề, không viết lại ngay dưới tiêu đề; ghi **lý do kỹ thuật cụ thể**, dữ liệu thiết yếu và code. Chỉ thêm quy trình, cách kiểm chứng hoặc giới hạn khi có thông tin **riêng của tình huống** (ví dụ kết quả kỳ vọng, rủi ro rò rỉ train/test), không lặp một câu chung cho cả 5 tình huống.
6. **20 câu trắc nghiệm Anh–Việt** với mỗi câu và **bản dịch trên CÙNG MỘT DÒNG**, ví dụ: `**Q1. What is a vector? — Vector là gì?**`. Mỗi phương án nằm trên **một dòng**: `A. A sequence of numbers — Một dãy số`. Đủ 4 lựa chọn cho một câu. Phần answer key là bảng 4 cột: `Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt)`. Không viết một dòng dịch tách dưới câu hỏi/phương án.
7. **Kiến thức tiếp theo:** nếu có nội dung mới thì nêu một câu ngắn. **Không lặp lại đúng sơ đồ chuỗi kiến thức ở cuối bài** chỉ để lấp mục.
8. Hình minh họa khi có ích phải là file SVG/PNG có thật, đường dẫn tương đối **đúng chính xác** với file Markdown và kiểm tra tồn tại. Không chỉnh tên file trong quá trình dịch thuật. Nếu ảnh được tạo từ dữ liệu thì phải khớp tọa độ/số liệu.
9. **Markdown là bản gốc**. PDF sau này phát hành riêng ở `exports/pdf/`, bảo toàn bảng/hình/code/dấu tiếng Việt và được render kiểm tra trước khi công bố.

## Quy tắc biên tập tinh gọn — áp dụng cho **mọi** bài

- **Tài liệu dành cho sinh viên chỉ chứa nội dung học.** Không đưa nhãn `DRAFT`, `Trạng thái:`, `chưa xác nhận chạy Windows`, tên phiên bản góp ý, cảnh báo nội bộ hoặc ghi chú về tiến độ vào đầu hay giữa bài. Giữ trạng thái và kết quả kiểm thử ở `docs/CURRICULUM-QA-STATUS.md`, `sources/` hoặc metadata quản lý.
- **Xóa câu không thêm tri thức**, chẳng hạn: “Các tham số được giải thích ngay cạnh hàm, không chèn quá nhiều comment vào ví dụ.”, “Không dùng thuật toán phức tạp hơn khi quy tắc đơn giản đã đủ.”, “Mỗi giá trị mang ý nghĩa và đơn vị đã nêu.”, “Không phải hồ sơ thật.”. Nếu cần cho biết dữ liệu giả lập, ghi **một lần**, chỉ ở nơi nguồn dữ liệu quan trọng để hiểu kết luận.
- **Rút cụm dẫn không cần thiết**, ví dụ “Trước khi chạy ví dụ, ”, “Đây là một bước nhỏ...”, “Hãy xem ví dụ...”, “Dưới đây là đoạn code...”, khi bỏ đi **không thay đổi ý nghĩa**. Nếu phần còn lại không có thông tin độc lập thì xóa luôn câu.
- **Không lặp nội dung trong cùng một khối**: tiêu đề đã nêu vấn đề thì không thêm `**Vấn đề:**` lặp lại; bảng thuật ngữ đã định nghĩa từ thì không lặp nguyên văn câu hỏi “X nghĩa là gì?” rồi chép cùng một định nghĩa làm đáp án. Tránh lặp sơ đồ tiên quyết ở cuối bài.
- **Giữ nguyên thông tin cần thiết:** định nghĩa/thuật ngữ mới, giải thích quan hệ nhân quả, tham số và công dụng cụ thể, nguồn dữ liệu có ý nghĩa (ví dụ Iris là dataset công khai thay vì bảng giả lập), shape, cột/hàng/đơn vị quan trọng, code, kết quả thật, cảnh báo kỹ thuật cụ thể (chia cho 0, leakage, kiểu dữ liệu) và nội dung 20 câu trắc nghiệm song ngữ.
- **Không lạm dụng nhãn.** Chỉ dùng các nhãn như “Dữ liệu”, “Vì sao”, “Lưu ý” khi người đọc cần tra cứu; đoạn văn tự nhiên ngắn gọn được ưu tiên hơn các nhãn trình bày hình thức. Không biến quy trình kiểm định hoặc hướng dẫn tác giả thành đoạn văn giải thích cho sinh viên.
- **Tự rà câu:** thử bỏ từng câu/mệnh đề; nếu nghĩa kỹ thuật, dữ kiện, kết luận và hành động của người học không đổi, **bỏ**. Một ý chỉ cần xuất hiện một lần ở vị trí giúp hiểu tốt nhất.
- Với code: **không tự động sửa xóa dòng code hoặc comment có mục đích thật** trong lúc biên tập prose. Trắc nghiệm 20 câu, 80 lựa chọn, bảng đáp án và link/hình phải giữ toàn vẹn.
- Checklist: không có `DRAFT` hay “Trạng thái” trong bài; không có 5 câu mô tả quy trình y hệt nhau; không có disclaimer giả lập lặp lại; không có câu meta hướng dẫn người soạn; đủ nội dung chuyên môn, code, bài tập và 20 MCQ.

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
