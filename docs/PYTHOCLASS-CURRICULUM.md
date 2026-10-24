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

## Cấu trúc bắt buộc cho mỗi bài (bản đọc của sinh viên)
1. Bản đồ **vị trí trong chuỗi kiến thức**, cho thấy kiến thức trước/sau và quan hệ giữa các khái niệm.
2. **English vocabulary** liên quan đến toàn bài, đi trước tất cả các API và định nghĩa.
3. **Thư viện, hàm, API Python**, bảng ngắn giải thích từng tên và cách dùng, ví dụ đầu vào/đầu ra.
   - **Gộp giải thích đối số (keyword arguments/flags) vào đúng hàm trong bảng thư viện/API**: ví dụ `np.array(...,dtype=float)` giải thích số thực; `X.mean(axis=0)` giải thích tính theo cột; `np.cov(X,rowvar=False)` giải thích cột là biến; `PCA(n_components=2)` giải thích số thành phần. Mỗi hàm ghi mục đích, ý nghĩa/lý do chọn tham số, ảnh hưởng khi thay giá trị. **Không lập một chương/bảng flags riêng** và không lặp lại lời giải thích flags ở mọi code demo. Comment trong code ưu tiên bối cảnh dữ liệu, lý do xử lý, đọc kết quả.
3a. **Ngôn ngữ sinh viên:** khi nhắc lại khái niệm tiếng Anh trong câu tiếng Việt phải có bản dịch ngay trong ngoặc, ví dụ eigenvector (vector riêng), eigenvalue (giá trị riêng), feature (đặc trưng), vector (véc-tơ), matrix (ma trận). Không dịch tên biến, tên hàm, keyword argument trong code/backticks; cột English của glossary đã được dịch ở cột bên cạnh và trắc nghiệm tiếng Anh giữ nguyên.
4. **Khái niệm và các khái niệm liên quan**: giải thích bằng lời dễ hiểu, ví dụ gần gũi trước rồi đến công thức tính thể hiện bằng **code Python nhỏ**. Mỗi nhóm Feature / Vector / Matrix, Mean / Variance... đều cần định nghĩa riêng; không dùng tiêu đề “Subconcept”; bỏ chứng minh toán học dài.
   - Nhắc lại các khái niệm được sử dụng **ngay tại từng tiểu mục** rồi tạo một ví dụ tăng tiến: nhiều đối tượng → mỗi đối tượng một vector → xếp vector thành một matrix → phép tính → đọc shape/kết quả. Không yêu cầu sinh viên tự suy đoán dữ liệu từ một dãy số trần.
   - Mọi bảng/`np.array`/`DataFrame`/dataset đều phải chú thích **mỗi hàng là mẫu gì, mỗi cột là feature nào, đơn vị đo gì, bao nhiêu hàng/cột, dữ liệu thật hay minh họa**. Với dữ liệu có nhãn, phân biệt nhãn mục tiêu với cột đầu vào. Chú thích bước xử lý `BƯỚC 1/2/3...` và giải thích tại sao code như vậy.
4a. **Kiểm tra hiểu ngay tại mỗi khái niệm:** một câu ngắn và đáp án gợi ý ngay sau đoạn ví dụ. Với khái niệm trừu tượng, ưu tiên **tình huống đời thường và hình trực giác** trước số liệu/công thức. Với các phép biến đổi dữ liệu, phải có bảng **trước / sau** (ít nhất vài hàng) và hình được tạo từ **kết quả chạy thật** khi trực quan hóa giúp ích; kiểm tra tương ứng với chương trình tạo hình. Hình minh họa giả lập phải ghi nguồn và giới hạn; không dùng tranh trang trí thay cho dữ liệu đúng.
5. **Khoảng 5 vấn đề thực tiễn**: bối cảnh và nhu cầu → khái niệm phù hợp → **vì sao chọn phương pháp này thay vì phương pháp khác, lợi ích/giới hạn** → quy trình giải → code có chú thích **vì sao viết như vậy** → cách kiểm tra và hạn chế.
   - Trước code mỗi tình huống, công bố metadata của dataset: đơn vị, ý nghĩa từng cột, ý nghĩa từng hàng, số mẫu và provenance. Trong code khởi tạo nhiều vector rõ ràng khi sinh viên cần hiểu quá trình hình thành matrix.
5a. **Tải nhận thức:** các bài thực tiễn kết hợp thuật toán chưa được học (như clustering/classification khi bài chính là PCA) phải mang nhãn **Phần mở rộng — có thể đọc sau** và giải thích ngắn vai trò của thuật toán, không ép sinh viên phải hiểu toàn bộ trước khi nắm bài chính.
6. **20 English multiple-choice questions** với bốn đáp án mỗi câu, đủ bảng đáp án và giải thích bằng tiếng Anh, bao quát thuật ngữ, Python, khái niệm và các quyết định thực tiễn.
7. **Liên hệ bài tiếp theo**, duy trì sơ đồ logic tiến trình.

Không dùng mục "mục tiêu học tập", "sau bài học bạn sẽ làm được gì", không xưng hô như giảng viên, không yêu cầu học sinh chứng minh công thức toán. Sinh viên phải có thể tự đọc để hệ thống hóa những gì từng học. Không chỉ biến bài toán thuần túy thành một câu chuyện giả: tình huống cần có quyết định, dữ liệu và thao tác Python hợp lý.

## Truy nguyên nguồn
- Có ít nhất một dẫn nguồn repo gốc từ đường dẫn file cụ thể trong **hồ sơ nội bộ** `sources/`/docs, khuyến khích kèm commit SHA và cell hoặc đoạn code.
- Ghi nội bộ: **Có trong ghi chép / Đã sửa lỗi / Mở rộng do AI biên soạn**. **Tuyệt đối không đưa nguồn biên tập/tên repo PythoClass hoặc PythonClass vào bài học phát hành cho sinh viên**, không đưa nhãn nguồn nội bộ, không chèn dẫn chiếu lịch sử ghi chú.
- Có thể tham chiếu tài liệu API chính thức để chuẩn hóa nếu cần, nhưng vẫn giữ mối liên hệ với ghi chép gốc.
- Không sửa hoặc ghi đè `PythoClass`. Không đưa thông tin bí mật, file cá nhân hoặc nội dung bên thứ ba không được phép lên GitHub.

## Test và nghiệm thu
- Code của năm tình huống thực tế phải chạy hoặc được kiểm tra rõ điều kiện cài đặt và dữ liệu. Comment giải thích lý do chọn biến đổi/hàm, không chỉ mô tả câu lệnh. Đoạn cần UI/biểu đồ có thể chạy headless bằng việc kiểm tra dữ liệu trước `show()`.
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
