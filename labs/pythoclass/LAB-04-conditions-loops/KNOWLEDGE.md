# Tổng hợp kiến thức — Lab Session 4

## Bài học liên quan
- [PY-03 — Toán tử](../../../lessons/chapters/PY-03-operators-logic.vi.md)
- [PY-04 — if/elif/else](../../../lessons/chapters/PY-04-if-elif-else.vi.md)
- [PY-05 — Vòng lặp](../../../lessons/chapters/PY-05-loops.vi.md)

## 1. Cấu trúc điều kiện
`if` thực hiện nhánh khi điều kiện đúng; `elif` kiểm tra trường hợp tiếp theo; `else` xử lý phần còn lại. Kiểm tra **miền dữ liệu trước**: tháng phải thuộc 1..12; năm có thể kiểm tra là số nguyên dương.

### Sắp ba số
Đề yêu cầu chỉ dùng `if/else`: so sánh rồi hoán đổi từng cặp, không dùng `sort` làm câu trả lời chính.

### Tháng, quý, năm nhuận
Một năm chia 4 quý, mỗi quý 3 tháng. Số ngày trong tháng phụ thuộc tháng và riêng tháng 2 phụ thuộc năm nhuận: chia hết cho 400 **hoặc** chia hết cho 4 và không chia hết cho 100.

### Đọc số bằng chữ
Tách trăm/chục/đơn vị bằng `//` và `%`, sau đó áp quy tắc tiếng Việt. Các trường hợp 0, 10, 15, 20, 21, 25, 101, 105 cần xử lý riêng theo cách đọc.

### Tiền điện lũy tiến
Tính tiền từng **bậc sử dụng**, không lấy toàn bộ số kWh nhân một mức giá duy nhất. Với giá trong Word: 120 kWh → 50×1800 + 50×2000 + 20×2500 = **240000 VND**. Ví dụ **282000 VND trong Word không khớp** bảng giá.

## 2. Vòng lặp
- `for`: dùng khi biết số lần lặp hoặc cần duyệt tập hợp xác định.
- `while`: dùng khi phải lặp đến khi điều kiện thay đổi; ví dụ đếm chữ số bằng cách chia lấy nguyên cho 10.
- **Số nguyên tố:** số lớn hơn 1, không có ước khác 1 và chính nó; có thể kiểm tra đến căn bậc hai.
- **GCD:** thuật toán Euclid lặp lấy phần dư đến khi phần dư bằng 0.
- **Nested loops:** vòng ngoài chọn dòng, vòng trong in từng ký tự/phần tử của dòng.

**Kiểm tra đầu ra:** xem đủ 14 bài trong `SOLUTION.py`, mỗi bài có ví dụ minh họa và assertion.
