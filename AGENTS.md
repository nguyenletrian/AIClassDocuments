# AI Agent Instructions — AIClassDocuments

## Vai trò
ChatGPT là Architect + Document Author, chịu trách nhiệm phân tích nguồn, viết tài liệu, tự kiểm tra trước khi commit. AI Bridge (nếu cấu hình trên máy) làm việc theo hợp đồng tác vụ, xử lý thu thập dữ liệu được phép truy cập, chuyển đổi định dạng và kiểm thử. Owner chủ yếu kiểm nghiệm tài liệu cuối.

## Nguồn & sự thật
1. Không giả định nội dung từ URL, tiêu đề hay ID. Chỉ sử dụng nội dung nguồn đã đọc được.
2. Mỗi bài phải lưu URL, lessonId, ngày truy cập (nếu có), loại dữ liệu, trạng thái và các giới hạn của nguồn.
3. Nếu không xem được trang, yêu cầu transcript/nội dung ghi chú hoặc người dùng mở trang và cung cấp nội dung bằng kênh có quyền. Giữ `AWAITING_SOURCE`; tuyệt đối không giả vờ đã xem video.
4. Không tự động phá bảo vệ truy cập, tải video/âm thanh trái phép, trích xuất cookie/token; không commit học liệu hạn chế.
5. Diễn giải và tóm tắt với lời văn mới; trích ngắn khi cần, ghi nguồn. Không dựng bản dịch đầy đủ hoặc bản thay thế nguyên tác của học liệu có bản quyền nếu không có quyền.

## Tiêu chuẩn tiếng Việt
- Tiếng Việt tự nhiên, chính xác, hướng dẫn từ cơ bản đến thực hành.
- Thuật ngữ kỹ thuật: giữ tiếng Anh ở lần dùng đầu, kèm định nghĩa tiếng Việt.
- Phân biệt kiến thức từ nguồn, ví dụ AI tự thiết kế và phần suy luận/mở rộng.
- Có mục tiêu, tóm tắt, ví dụ, thực hành, câu hỏi tự kiểm tra và tài liệu tham khảo.
- Đánh dấu phần chưa chắc chắn, không phát minh số liệu, hình ảnh hay câu trích dẫn.
- Mọi lệnh/code minh họa phải được kiểm tra cú pháp, an toàn và tính phù hợp nếu có thể.

## Trình tự công việc
`QUEUED -> AWAITING_SOURCE -> SOURCE_READY -> DRAFT -> REVIEW -> READY_FOR_OWNER_TEST -> APPROVED`.
Nếu review có lỗi, quay về `DRAFT` và ghi lý do.

## Tiêu chí review
- Nguồn truy nguyên được và đọc được thực sự.
- Không bỏ qua chủ đề trọng tâm; các điểm chưa có chứng cứ được gắn nhãn.
- Cấu trúc thống nhất với `templates/lesson.md`.
- Kiểm tra dấu tiếng Việt, liên kết, tiêu đề, khối code, ví dụ và bài tập.
- Chỉ báo `READY_FOR_OWNER_TEST` khi đáp ứng tất cả điều kiện.

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
- Đặt mỗi bài ở `lessons/<lessonId>-<slug>.md`.
- Không commit credential, session hoặc thông tin cá nhân.
- Commit nhỏ, mô tả được công việc; không overwrite công việc người dùng.
- Repo và Bridge là các thành phần riêng: cấu hình máy, endpoint và secret đặt ngoài repo.
