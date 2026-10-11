# Kiểm tra log Bridge theo yêu cầu

**Câu lệnh dành cho owner:** `kiểm tra log Bridge`, `xem log AIBridge`,
`kiểm tra lỗi Bridge` hoặc `đọc 50 dòng log gần nhất`.

Architect phải thao tác **ngay trong lượt được yêu cầu**, không bắt owner
mở terminal VS Code để copy/paste nếu Bridge đang chạy. Đây là tác vụ thủ
công độc lập, **không phụ thuộc** trạng thái `AWAITING_SOURCE` của Jetking.

## Luồng thực hiện

1. Fetch `bridgeTask.json` từ branch `main` trong repo AIClassDocuments.
   Chỉ sử dụng TaskSource và identity hiện tại làm nguồn chuẩn.
2. Kiểm tra đã có một task `runtime:read_log` đang pending hoặc đã gửi mà
   chờ ACK chưa. **Không tạo trùng** nếu cùng yêu cầu đã được xếp hàng.
3. Tạo một `task_id` mới, duy nhất, chẳng hạn
   `aiclassdocuments-manual-log-YYYYMMDD-HHMMSS` (giờ Việt Nam). Tạo task
   bằng bản sao các trường nhận diện `system_id`, `project_id`,
   `worker_id`, `execution_target`, `delivery_target`, `project`
   của task Bridge hiện có; tuyệt đối không tự đoán CDP port.
4. Append duy nhất task kiểm tra log vào `tasks`; giữ nguyên lịch sử task
   và `goal_review`. Commit lên `main` bằng optimistic SHA update.
5. Chờ Bridge polling TaskSource → chạy `runtime:read_log` → gửi
   `type=task_result` đến cuộc hội thoại Architect qua Edge/CDP.
   Nếu task chưa gửi, **không** nói đã đọc log. Không tạo task thứ hai
   để thúc ép task thứ nhất.
6. Đọc `data.entries`, xác định lỗi, nguyên nhân có bằng chứng,
   mức độ chắc chắn và hành động đề xuất. Chỉ đề xuất sửa code/
   restart khi kết quả thực tế đủ hỗ trợ.
7. ACK chính xác `task_id` vừa nhận: `architect_ack=true`,
   `bridge_completed=true`, `status=completed` khi đọc được log,
   `status=failed` khi đọc log thất bại; giữ nguyên các task khác.
   Không tự bật `goal_review.enabled` và không tạo `queue_exhausted`.

## Hợp đồng task

```json
{
  "task_id": "aiclassdocuments-manual-log-unique-id",
  "status": "pending",
  "bridge_completed": false,
  "architect_ack": false,
  "system_id": "aiclassdocuments",
  "project_id": "AIClassDocuments",
  "worker_id": "AIClassDocuments-architect",
  "execution_target": {
    "kind": "bridge-runtime",
    "host": "127.0.0.1",
    "port": 0,
    "instance_id": "AIClassDocuments-architect"
  },
  "delivery_target": {
    "kind": "browser-cdp",
    "host": "127.0.0.1",
    "port": 9222,
    "instance_id": "AIClassDocuments-architect"
  },
  "project": {
    "repository": "https://github.com/nguyenletrian/AIClassDocuments.git",
    "branch": "main"
  },
  "action": {"type": "runtime", "target": "read_log"},
  "permissions": {
    "read": true, "edit": false, "execute": false,
    "commit": false, "push": false
  },
  "metadata": {
    "review_mode": "on_demand",
    "ack_policy": "architect_review"
  },
  "payload": {"tail_lines": 30},
  "return_route": {"type": "provider", "target": "OpenAI", "via": "web"}
}
```

Trường identity trong ví dụ chỉ để minh họa; luôn đối chiếu TaskSource
trước khi commit. `tail_lines` mặc định 30 và giới hạn tối đa 60. Bridge
chỉ được đọc file `runtime.log` trong thư mục worker của chính nó;
không đọc shell history, các terminal không liên quan, cookie/token hoặc
file tùy ý. Log được rút gọn và che các mẫu bí mật phổ biến trước khi gửi.

**Quan trọng:** `ack_policy: auto_success` không phù hợp cho task đọc
log vì nó đánh dấu xong mà không gửi kết quả về Architect. Bridge sau
bản vá PR #15 từ chối auto-success cho toàn bộ `runtime:read_log`.

## Khi Bridge không gửi được

Nếu Edge/ChatGPT bận, draft không rỗng hoặc selector Send không khả dụng,
Bridge giữ lại kết quả và trạng thái chờ. Architect không được suy diễn đã
đọc log, không reset hàng đợi, không bơm lại task tương tự, và phải báo
rõ chưa nhận được kết quả. Khi có bằng chứng delivery, ACK mới kết thúc
chu kỳ. Giới hạn này ngăn vòng nhập/xóa và spam từng gặp trước đây.
