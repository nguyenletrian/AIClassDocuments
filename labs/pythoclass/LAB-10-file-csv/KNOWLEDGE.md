# Tổng hợp kiến thức — Lab Session 10

## Bài học liên quan
- [PY-08 — Dictionary](../../../lessons/chapters/PY-08-dictionary.vi.md)
- [PY-09 — Hàm](../../../lessons/chapters/PY-09-functions-lambda.vi.md)
- [PY-12 — File, CSV và ngoại lệ](../../../lessons/chapters/PY-12-file-csv-errors.vi.md)
- [PY-44 — Ứng dụng CLI CRUD](../../../lessons/chapters/PY-44-cli-crud-validation.vi.md)

## 1. File I/O giúp lưu thông tin giữa các lần chạy
`students.csv` là bảng có cột mã, tên, lớp và 3 điểm. Mỗi hàng đại diện một học viên. Đọc bằng `csv.DictReader`, ghi bằng `csv.DictWriter` để giữ tên cột. Sử dụng `pathlib.Path(__file__).resolve().parent` để tệp dữ liệu nằm cùng thư mục chương trình.

## 2. Kiểm tra dữ liệu
- **ID duy nhất:** kiểm tra trước khi thêm.
- **Tên/lớp không trống:** `.strip()` rồi kiểm tra.
- **Điểm là số 0..100:** đổi bằng `float()` sau khi bắt `ValueError`.
- **Lỗi file:** `FileNotFoundError`, `OSError`, `csv.Error`.
- **Average:** `(Python+Math+ML)/3` đối với mỗi học viên.

## 3. Ghi file an toàn
Ghi ra một file tạm cạnh `students.csv` trước, sau đó `replace()` để tránh hỏng file chính khi ghi dang dở. Không tự lưu dữ liệu khi chưa bấm chọn **Save**. `SOLUTION.py` dùng module `csv` của thư viện chuẩn; không phụ thuộc Pandas.

## 4. Cách thực hành
`students.csv` kèm theo có 10 dòng và tên giả lập; có thể làm trên bản copy khi muốn giữ dữ liệu mẫu.
