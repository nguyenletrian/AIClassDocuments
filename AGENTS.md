# AIClassDocuments — Hướng dẫn agent (PythoClass-first)

## Mục đích được chủ dự án đổi ngày 2026-10-24
Tài liệu tham chiếu **chính** là repository [nguyenletrian/PythoClass](https://github.com/nguyenletrian/PythoClass), chứa bài ghi chép, lab, scripts và notebooks của chủ dự án. Nhiệm vụ mới là **biên soạn lại thành giáo trình Python ứng dụng AI chuẩn xác và có thể thực hành**, không phải chép lại nguyên văn hay dịch khóa Jetking. Các ghi nhận Jetking cũ chỉ còn là hồ sơ lịch sử, không được tự ý tái kích hoạt.

Mọi công việc biên soạn tuân thủ [docs/PYTHOCLASS-CURRICULUM.md](docs/PYTHOCLASS-CURRICULUM.md).

## Nguyên tắc biên soạn
1. Quét đủ file trong `sources/pythoclass-file-inventory.csv`; bóc tách mọi khái niệm **dù chỉ xuất hiện ngắn** và lưu trong bản đồ chủ đề. Không công bố "đã xử lý toàn bộ" khi chưa duyệt 65/65 file.
2. Mỗi bài bao gồm: **khái niệm**, **mục đích**, **công thức nếu có**, **thư viện Python**, **cách sử dụng Python**, **ứng dụng thực tế trong lập trình AI**, **khoảng năm bài tập** kèm code và kiểm chứng.
3. Dùng tiếng Việt rõ ràng; thuật ngữ tiếng Anh giữ tại lần đầu. Xây dựng đường học từ căn bản lên nâng cao, ưu tiên kiến thức trước–sau.
4. Phân biệt: `GHI CHÉP GỐC`, `ĐÃ HIỆU ĐÍNH`, `AI MỞ RỘNG`. Không truyền lại công thức hoặc code sai; thử cú pháp, test giá trị, tránh dữ liệu rò rỉ trong ML.
5. Không sửa repository PythoClass. Không lưu secret, output chứa thông tin cá nhân hoặc nguồn bị hạn chế quyền sử dụng lên GitHub.
6. Không yêu cầu chủ dự án thủ công gửi ảnh/chép notes khi nguồn đã có thể đọc qua GitHub và công cụ được phép. Tự kiểm tra file binary bằng công cụ phù hợp, báo cáo chính xác blocker nếu không đọc được.
7. **Chỉ triển khai một bài mẫu PCA** dưới `lessons/pilot/`. Giữ `goal_review.enabled=false` và không tạo task viết hàng loạt cho đến khi chủ dự án xem và góp ý mẫu.

## Tiêu chí sẵn sàng
Bài mẫu chỉ ở `PILOT_REVIEW` khi đã có nguồn cụ thể, đủ cấu trúc yêu cầu, kết quả bài tập đã đối chiếu và các giới hạn được ghi rõ. Chuyển sang `OWNER_APPROVED` khi chủ dự án đánh giá bố cục và nội dung. Các lô bài tiếp theo chỉ mở sau đó.

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
- Đặt mỗi bài ở `lessons/<lessonId>-<slug>.md`.
- Không commit credential, session hoặc thông tin cá nhân.
- Commit nhỏ, mô tả được công việc; không overwrite công việc người dùng.
- Repo và Bridge là các thành phần riêng: cấu hình máy, endpoint và secret đặt ngoài repo.
