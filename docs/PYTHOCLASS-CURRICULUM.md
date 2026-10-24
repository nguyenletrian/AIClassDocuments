# PythoClass → AIClassDocuments — Hướng dẫn biên soạn giáo trình (2026-10-24)

## Nhiệm vụ mới
**Nguồn chính:** [nguyenletrian/PythoClass](https://github.com/nguyenletrian/PythoClass) (đúng tên repo là *PythoClass*). Đây là kho ghi bài, notebook, code, bài tập, lab của chủ dự án. **Đầu ra:** giáo trình Python ứng dụng AI có cấu trúc, bắt đầu bằng tiếng Việt, giải thích cặn kẽ và minh họa code có thể chạy độc lập.

**Không còn phụ thuộc Jetking**. Hồ sơ Jetking vẫn được lưu để tra cứu lịch sử nhưng không được khởi động lại để tạo bài trong mục tiêu mới.

## Nguyên tắc bao phủ không bỏ sót
1. Tạo danh sách tất cả file ở commit nguồn ổn định. Đọc `.py`, cell `source` của `.ipynb`, nội dung bảng `.csv`; xử lý `.docx`/`.pptx`/`.xlsx` qua bộ đọc phù hợp; xem riêng file chứa hình/đồ thị khi cần. Notebook output không phải nguồn chân lý nếu output cũ hoặc bị cắt.
2. Mỗi định nghĩa, thuật toán, API, hàm, toán tử, kỹ thuật toán và ví dụ thực tế **dù xuất hiện rất ít** đều được ghi một hàng trong sổ `topic-map`, cùng tên file, cell/phần nếu có, trạng thái và bài dự kiến.
3. Hợp nhất các mục trùng lặp vào **một bài chuẩn**; vẫn lưu tất cả liên kết nguồn. Mỗi khái niệm nhỏ có mục con rõ ràng; nếu quá sâu hoặc độc lập thì tách bài.
4. Ghi chép gốc có thể chứa typo, code thiếu ngoặc, sai định nghĩa, tên hàm hoặc khái niệm chưa hoàn chỉnh. **Không sao chép sai**; viết phần hiệu đính, giải thích tại sao và kiểm tra bằng code/toán.
5. Không tuyên bố bao phủ toàn bộ repo khi còn file binary, notebook, code hoặc comment chưa duyệt. Đối chiếu trước và sau bằng số file đã review, số concept đã lập chỉ mục, số bài đã xuất, số mục chưa xử lý.

## Cấu trúc bắt buộc cho mỗi bài
- Tên bài, trình độ, kiến thức cần có, mục tiêu đầu ra
- **Khái niệm** chính xác và trực giác
- **Mục đích**/lý do sử dụng và khi không nên sử dụng
- **Công thức** và giải thích từng ký hiệu/nếu không có ghi *không áp dụng*
- **Thư viện** Python, cài đặt, các API và thao tác liên quan
- **Cách dùng trong Python**: ví dụ độc lập và kết quả kiểm tra
- **Ứng dụng thực tế trong lập trình AI**: pipeline, xử lý dữ liệu, bài toán tương ứng; không vẽ ra lợi ích không chứng minh
- **Khoảng năm bài tập** lập trình theo cấp độ, có đề bài, mã mẫu/lời giải, cách kiểm tra, thử thách mở rộng
- Các lỗi điển hình, FAQ/ôn tập, thuật ngữ, nguồn chi tiết, phần AI tự bổ sung

Với chủ đề toán: ký hiệu, giả định, kích thước mảng và các bẫy tính toán quan trọng. Với chủ đề không có công thức: không ép thêm công thức vô nghĩa.

## Truy nguyên nguồn
- Có ít nhất một dẫn nguồn `PythoClass` từ đường dẫn file cụ thể, khuyến khích kèm commit SHA và cell hoặc đoạn code.
- Ghi: **Có trong ghi chép / Đã sửa lỗi / Mở rộng do AI biên soạn**.
- Có thể tham chiếu tài liệu API chính thức để chuẩn hóa nếu cần, nhưng vẫn giữ mối liên hệ với ghi chép gốc.
- Không sửa hoặc ghi đè `PythoClass`. Không đưa thông tin bí mật, file cá nhân hoặc nội dung bên thứ ba không được phép lên GitHub.

## Test và nghiệm thu
- Code của năm bài tập phải chạy hoặc được kiểm tra rõ điều kiện cài đặt và dữ liệu. Đoạn cần UI/biểu đồ có thể chạy headless bằng việc kiểm tra dữ liệu trước `show()`.
- Đối chiếu con số xuất ra, shape, đơn vị đo, `random_state` và tránh data leakage với ML.
- Ghi trạng thái: `SOURCE_MAPPED → DRAFT → SELF_REVIEW → PILOT_REVIEW → OWNER_APPROVED`.
- Bài thử đầu: `lessons/pilot/AI-MATH-01-pca.vi.md`. **Chỉ sau khi owner duyệt bố cục** mới mở rộng ra toàn repo. Trước đó không tạo hàng loạt, không tự queue task làm tài liệu mới và không tự bật `goal_review.enabled`.

## Quy trình tự chủ (không đẩy việc thô cho chủ dự án)
1. Kiểm kê và đọc tài liệu trực tiếp qua GitHub/Bridge của nguồn `PythoClass`.
2. Chủ động dùng mã nguồn và công cụ đọc notebook/office/file Python phù hợp, không yêu cầu chủ dự án chụp ảnh hay copy từng đoạn nếu dữ liệu đã tồn tại trong repo.
3. Tách concept, sinh outline, soạn, kiểm thử code, review nội bộ, commit bài vào `AIClassDocuments`.
4. Owner chỉ góp ý bản nháp mẫu hoặc kiểm tra học liệu đã hoàn thiện. Nếu nguồn không đọc được vì hạn chế kỹ thuật, trước tiên tìm cách xử lý bằng công cụ và ghi blocker cụ thể; không bịa nội dung.

## Trạng thái triển khai hiện tại
- Pilot: **PCA (Principal Component Analysis)**, từ `MON 2/3. Eigens_PCA.py`, `MON 2/LabSession3_4.py`, `MON 2/Linear Algebra.py`.
- Đã kiểm tra các khối tính toán mẫu với NumPy 2.3.5 và scikit-learn 1.8.0.
- Đây chưa phải đánh giá hoàn tất mọi `.docx`/`.pptx`/`.xlsx` hoặc toàn bộ 60+ file nguồn.
- Mọi thử nghiệm Bridge cho Jetking cũ **không thuộc** chương trình mới. Nhánh AIBridge nghiên cứu asset discovery trước đó vẫn độc lập, không merge hoặc kích hoạt chỉ vì goal thay đổi.
