# Tổng hợp kiến thức — Lab Session 5 & 6

## Bài học liên quan
- [PY-24 — Vector](../../../lessons/chapters/PY-24-linear-vector.vi.md)
- [PY-28 — Hàm số cho AI](../../../lessons/chapters/PY-28-functions-models.vi.md)
- [PY-30 — Hàm mất mát](../../../lessons/chapters/PY-30-loss-functions.vi.md)
- [PY-31 — Đạo hàm](../../../lessons/chapters/PY-31-limits-derivatives.vi.md)
- [PY-32 — Gradient Descent](../../../lessons/chapters/PY-32-gradient-descent.vi.md)
- [PY-33 — Hessian](../../../lessons/chapters/PY-33-jacobian-hessian.vi.md)

## 1. Mạch học
**Dữ liệu** (giờ học X, điểm y) → **dự đoán** `y_hat = w*X+b` → **MSE** đo độ lệch → **gradient** chỉ hướng cần giảm sai số → **gradient descent** cập nhật w và b → **Hessian** mô tả độ cong theo từng cặp tham số.

## 2. Các khái niệm
- **Weight (w):** mức điểm dự đoán thay đổi khi giờ học tăng 1 đơn vị.
- **Bias (b):** giá trị dự đoán tại X = 0; không nhất thiết có ý nghĩa ngoại suy thực tế.
- **MSE:** bình phương sai số rồi lấy trung bình; đơn vị của MSE là bình phương đơn vị điểm, không phải phần trăm.
- **Partial derivative:** mức thay đổi của loss theo **một** tham số trong lúc giữ các tham số khác cố định.
- **Gradient:** gom các đạo hàm bậc 1 thành một vector.
- **Hessian:** ma trận các đạo hàm bậc 2; eigenvalue dương biểu thị loss có độ cong hướng lên theo hướng tương ứng.

## 3. Hai mức bài toán
- **Task 3:** `(2w+b-5)**2` là một ví dụ hàm loss cực nhỏ, đủ để nhìn từng đạo hàm.
- **Task 4–5:** dùng loss trên **toàn bộ 8 quan sát**; gradient và Hessian khác ví dụ một điểm. Tránh trộn chúng.

## 4. Kiểm chứng bằng đồ thị
Vẽ scatter dữ liệu và đường hồi quy từ dự đoán; vẽ MSE theo epoch để quan sát giảm dần. `SOLUTION.py` lưu hình tại `outputs/` khi chạy (thư mục sinh ra, không cần commit). So sánh giá trị đầu/cuối, không gọi mô hình đạt 100% chính xác chỉ vì loss giảm.

Cài: `pip install numpy matplotlib sympy`.
