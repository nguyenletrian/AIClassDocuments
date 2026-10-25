# Tổng hợp kiến thức — Lab Session 5 (Student List)

## Bài học liên quan
- [PY-05 — Vòng lặp](../../../lessons/chapters/PY-05-loops.vi.md)
- [PY-06 — List](../../../lessons/chapters/PY-06-lists.vi.md)
- [PY-09 — Hàm](../../../lessons/chapters/PY-09-functions-lambda.vi.md)

## 1. List lưu nhiều học viên
`students` là **một list**, mỗi phần tử có `id`, `name`, `score`. Có thể lưu mỗi học viên bằng dictionary để thao tác dễ đọc. Bài này khác Assignment 1: **kho dữ liệu chính phải là list**, không chuyển toàn bộ sang dictionary theo ID.

## 2. Các tác vụ
- **Add:** `.append()` sau khi xác thực mã duy nhất và điểm hợp lệ.
- **Display:** `for student in students`.
- **Search:** so sánh tên sau khi `.strip().casefold()`, có thể có nhiều kết quả.
- **Delete:** tìm học viên theo ID trước, sau đó `.remove()` hoặc `.pop(index)`.
- **Sort:** `sorted(students, key=lambda s: s["score"], reverse=...)`; không thay đổi list gốc trừ khi có chủ đích.
- **Stats:** `max`, `min`, `sum`, `len` với trường hợp list rỗng.

## 3. Lỗi thường gặp từ code thử nghiệm
`input().split(" ")` chia sai tên có nhiều từ; `"8" > "10"` không phải so sánh điểm số; xóa phần tử khi đang duyệt có thể gây bỏ sót. Giải pháp đầy đủ thực hiện kiểm tra trước khi lưu và tính toán.

**Bài gốc không quy định tối thiểu 10 dữ liệu:** lời giải chứa 12 học viên giả lập để thuận tiện luyện tập.
