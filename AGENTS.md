# AIClassDocuments — Hướng dẫn agent (PythoClass-first)

## Mục đích được chủ dự án đổi ngày 2026-10-24
Tài liệu tham chiếu **chính** là repository [nguyenletrian/PythoClass](https://github.com/nguyenletrian/PythoClass), chứa bài ghi chép, lab, scripts và notebooks của chủ dự án. Nhiệm vụ mới là **biên soạn lại thành giáo trình Python ứng dụng AI chuẩn xác và có thể thực hành**, không phải chép lại nguyên văn hay dịch khóa Jetking. Các ghi nhận Jetking cũ chỉ còn là hồ sơ lịch sử, không được tự ý tái kích hoạt.

Mọi công việc biên soạn **PHẢI đọc** [docs/CURRICULUM-STYLE-GUIDE.md](docs/CURRICULUM-STYLE-GUIDE.md) và [templates/lesson.md](templates/lesson.md) **trước khi viết bất kỳ bài nào**. Quy trình nguồn chi tiết ở [docs/PYTHOCLASS-CURRICULUM.md](docs/PYTHOCLASS-CURRICULUM.md).

## Nguyên tắc biên soạn
1. Kiểm kê nguồn tại `sources/curriculum-source-coverage.csv` (68 file trong phiên bản nguồn 24/10/2026), bóc tách mọi khái niệm **dù chỉ nhắc ngắn**. Bảng `sources/pythoclass-file-inventory.csv` chỉ là snapshot 65 file trước đó. Không công bố bao phủ toàn bộ nếu còn nguồn chưa đọc.
2. Tài liệu dành cho sinh viên đi theo thứ tự: **vị trí kiến thức → English vocabulary → thư viện/hàm Python → các khái niệm được giải thích bằng lời rồi minh họa bằng ví dụ Python nhỏ → 5 tình huống thực tế có lý do chọn phương pháp, quy trình và code → 20 câu trắc nghiệm song ngữ Anh–Việt với lựa chọn và giải thích → bài tiếp theo**. Các từ như Feature/Vector/Matrix phải được định nghĩa riêng bằng ngôn ngữ phổ thông trước khi xuất hiện trong phép tính; không dùng nhãn tiêu đề “Subconcept”, không có mục tiêu học tập/chứng minh toán học hoặc ngôn ngữ giáo án.
3. Dùng tiếng Việt rõ ràng; có bảng thuật ngữ tiếng Anh đặt trước thư viện và khái niệm. Mỗi bài phải có sơ đồ chuỗi kiến thức (ví dụ Vector → Matrix → Features → PCA → ML) để sinh viên biết nội dung đang ở đâu trong hệ thống.
3a. Ở mỗi mục khái niệm liên quan (4.2, 4.3...), **nhắc lại bằng lời khái niệm xuất hiện trong mục**, rồi trình bày **một ví dụ nhỏ tăng tiến từng bước**: đối tượng → vector → matrix → phép xử lý → đọc kết quả. Bất cứ khối dữ liệu nào cũng phải chú thích: số hàng, **mỗi hàng biểu diễn ai/cái gì**, tên & ý nghĩa từng cột, đơn vị đo, nguồn dữ liệu (giả lập/công khai). Không đưa array số trần mà thiếu nghĩa dữ liệu. Mỗi code block gắn bước và lý do chọn thao tác.
3b. Thiết kế cho sinh viên năng lực học bình thường: **mỗi tiểu mục có tự kiểm tra ngắn và đáp án ngay bên dưới**; khái niệm trừu tượng như Eigenvector cần **ẩn dụ/thí dụ đời thường trước code**. Với phép biến đổi như PCA/scale/clustering, hiển thị dữ liệu **trước và sau**, tọa độ thật và hình trực quan khớp chính dữ liệu/thuật toán đã chạy (không dùng minh họa vô căn cứ). Đánh dấu rõ **phần mở rộng — có thể đọc sau** cho API/thuật toán vượt quá kiến thức tiên quyết. Duy trì 20 câu hỏi trắc nghiệm song ngữ Anh–Việt cuối bài; tự kiểm tra ngắn không thay thế trắc nghiệm.
3c. **Gộp đối số/flags vào từng hàm ở phần thư viện**: giải thích `dtype=float` bên cạnh `np.array`, `axis=0` bên cạnh `mean`, `rowvar=False` bên cạnh `np.cov`, `n_components` bên cạnh `PCA`... nêu tham số có nghĩa gì, vì sao chọn và hệ quả nếu đổi. **KHÔNG tạo một bảng tham số chung tách khỏi hàm.** Trong code demo chỉ chú thích nguồn dữ liệu, số hàng/cột, mục đích và lý do thực hiện từng bước; tránh lặp lại ý nghĩa cờ ở từng dòng. Giữ code minh họa ngắn, có cấu trúc.
3d. **Bảng thuật ngữ gọn trước mỗi mục:** Trước **mỗi mục, tiểu mục và tình huống** có một dòng `Từ vựng trong mục:` dạng `Eigenvector — vector riêng; Eigenvalue — giá trị riêng`. Sau đó dùng thuật ngữ tự nhiên trong văn bản, **không gắn nghĩa tiếng Việt trong ngoặc sau từng lần nhắc**. Giữ nguyên định danh Python và đường dẫn Markdown/ảnh. Cấm tự động thay thế từ khóa bên trong `](path)`, đường dẫn ảnh hoặc code. Trắc nghiệm **20 câu song ngữ Anh–Việt**, dịch cả câu hỏi, bốn lựa chọn và giải thích đáp án.
4. Truy nguyên `GHI CHÉP GỐC`, `ĐÃ HIỆU ĐÍNH`, `AI MỞ RỘNG` **chỉ ở hồ sơ nội bộ** `sources/`/docs, KHÔNG trong bài dành cho sinh viên. Không nhắc tên repo PythoClass/PythonClass, đường dẫn ghi chép hoặc quá trình biên soạn trong `lessons/`. Không truyền lại công thức hoặc code sai; thử cú pháp, test giá trị, tránh dữ liệu rò rỉ trong ML.
5. Không sửa repository PythoClass. Không lưu secret, output chứa thông tin cá nhân hoặc nguồn bị hạn chế quyền sử dụng lên GitHub.
6. Không yêu cầu chủ dự án thủ công gửi ảnh/chép notes khi nguồn đã có thể đọc qua GitHub và công cụ được phép. Tự kiểm tra file binary bằng công cụ phù hợp, báo cáo chính xác blocker nếu không đọc được.
7. **Đã có lệnh chủ dự án 2026-10-24 triển khai toàn bộ chương trình**. Cho phép soạn các bài còn lại theo style guide. Vẫn giữ `goal_review.enabled=false` để tránh spam heartbeat; không đổi ACK/tác vụ cũ. Bài mới mang trạng thái `DRAFT` tới khi test thật.

## Tiêu chí sẵn sàng
Đã có 46 bài DRAFT trong `lessons/chapters/` và một bài PCA tham chiếu, được chủ dự án cho phép biên soạn. Chỉ nâng bài sang `CODE_VERIFIED` khi chạy code/test có bằng chứng, sang `EDITOR_REVIEWED` khi rà chuẩn mực, nguồn và trắc nghiệm. Xem `docs/CURRICULUM-QA-STATUS.md`; không đồng nhất việc có bài với đã hoàn thành mọi khái niệm nguồn.

## Hệ thống Bridge
AIBridge giữ worker identity, queue/ACK và các quyền task theo cơ chế cũ. Đổi mục tiêu tài liệu **không** là giấy phép để restart, gửi idle reminders lặp lại, replay ambiguous sends, tự tạo New Chat hay chạy lại các task Jetking. Khi cần đọc/tạo tài liệu từ PythoClass, ưu tiên GitHub; chỉ tạo các task Bridge giới hạn nhiệm vụ thật và có thể kiểm chứng.

## Kiểm tra log AIBridge theo yêu cầu

Khi owner nói `kiểm tra log`, `xem log Bridge` hoặc `chẩn đoán lỗi Bridge`,
thực hiện trực tiếp workflow trong `docs/ON_DEMAND_BRIDGE_LOG_REVIEW.md`:
fetch TaskSource chính thức → append đúng một task `runtime:read_log`
(`review_mode=on_demand`, `ack_policy=architect_review`,
`return_route=provider:OpenAI/web`) → đợi Bridge gửi log thật →
phân tích lỗi có chứng cứ → ACK chính task đó trong Git.

Không yêu cầu owner copy log VS Code nếu worker đang hoạt động.
Không tự đặt `auto_success` cho log; không biến đọc log thành
tín hiệu tiến độ bài Jetking; không đánh thức lại goal đang tạm dừng;
không đặt lịch định kỳ hoặc tạo task lặp vì chưa thấy kết quả.
Nếu chưa có `task_result`, nói rõ chưa nhận được log thực tế.

## Test script dùng chung AIBridge

Khi cần chạy unittest từ Bridge, ưu tiên route dùng chung
`verification:test_script` trong AIBridge, thay vì sao chép một
test runner riêng vào dự án. Hợp đồng tham khảo:
`nguyenletrian/AIBridge/docs/TEST_SCRIPT_CAPABILITY.md`.

- Test bộ chẩn đoán AIBridge đã đóng gói:
  `payload.suite=bridge_diagnostics`, không cần `project.workdir`.
- Test code AIClassDocuments hoặc dự án khác:
  `payload.suite=project_unittest`,
  `payload.pattern=test_<name>.py`; cần `project.workdir` cục bộ
  rõ ràng và file có sẵn trong `tests/`.
- Mọi task đều phải khai báo `permissions.run_tests=true`,
  `ack_policy=architect_review`, route trả kết quả về Architect.
  Việc chạy Python test là thực thi code đáng tin cậy, không phải sandbox.
- PASS của GitHub CI không thay thế PASS từ Windows worker.
  Sau khi nhận đúng `task_result`, Architect review và ACK.
- Route kiểm thử **không dùng thay** `runtime:read_log` để
  thu thập dữ liệu log runtime và không được tự truy cập tài khoản/nguồn học.

## Git
- Đặt bài giảng ở `lessons/chapters/PY-<nn>-<slug>.vi.md` và cập nhật `lessons/chapters/README.md` theo chuỗi tiên quyết.
- Không commit credential, session hoặc thông tin cá nhân.
- Commit nhỏ, mô tả được công việc; không overwrite công việc người dùng.
- Repo và Bridge là các thành phần riêng: cấu hình máy, endpoint và secret đặt ngoài repo.
