# Tổng hợp kiến thức — Assignment 1 (Dictionary CRUD)

## Bài học liên quan
- [PY-08 — Dictionary](../../../lessons/chapters/PY-08-dictionary.vi.md)
- [PY-09 — Hàm và lambda](../../../lessons/chapters/PY-09-functions-lambda.vi.md)
- [PY-44 — CLI CRUD](../../../lessons/chapters/PY-44-cli-crud-validation.vi.md)

## 1. Vì sao dùng Dictionary?
Mỗi học viên có **mã duy nhất**, nên dùng một dictionary bên ngoài với mã làm key sẽ giúp tìm và cập nhật trực tiếp, thay vì phải duyệt toàn bộ danh sách. Mỗi value là dictionary chứa `name` và `score`. Ví dụ `students["S001"]["score"]` truy cập điểm của mã `S001`.

## 2. Các thao tác CRUD
- **Create:** kiểm tra mã chưa tồn tại, tên không rỗng và điểm là số từ 0 đến 10 rồi thêm.
- **Read:** duyệt `.items()`, hiển thị mã, tên, điểm rõ ràng.
- **Update:** kiểm tra mã có tồn tại trước khi thay tên hoặc điểm.
- **Delete:** yêu cầu xác nhận trước khi gọi `del`/`.pop()`, tránh xóa nhầm.

## 3. Phân loại và thống kê
- `sorted(students.items(), key=lambda item: item[1]["score"])` sắp xếp theo điểm.
- `max`, `min`, `sum / len` tính điểm cao nhất, thấp nhất và trung bình, nhưng cần xử lý danh sách rỗng.
- Thang phân loại trong `SOLUTION.py` được chọn rõ ràng: **Excellent ≥ 9**, **Good ≥ 7**, **Average ≥ 5**, còn lại **Poor**. Đây là quy ước minh họa vì đề gốc không cố định ngưỡng.

## 4. Các tình huống biên
Mã trùng, tên trống, điểm âm/lớn hơn 10, nhập chữ thay số, kho dữ liệu rỗng, nhập xác nhận khác `y` cần được xử lý có thông báo dễ hiểu.

**Thực hành:** chạy `SOLUTION.py` ở chế độ demo (`--demo`) để kiểm tra các thao tác, hoặc chạy không đối số để vào menu.
