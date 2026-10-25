# PY-33 — Jacobian, Hessian và điểm cực trị


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Jacobian** — ma trận Jacobian; **Hessian** — ma trận Hessian.

`Gradient → Jacobian → Hessian → Tối ưu mô hình`

**Học xong dùng để làm gì?** Phân tích nhiều đầu ra thay đổi theo nhiều đầu vào và độ cong của hàm mục tiêu.

**Kết nối kiến thức tiếp theo:** PY-34 mô hình hóa dữ liệu và sự kiện không chắc chắn bằng xác suất.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Khái niệm |
|---|---|---|
| Jacobian | ma trận Jacobian | Bảng đạo hàm riêng bậc 1 của hàm nhiều đầu ra |
| Hessian | ma trận Hessian | Bảng đạo hàm riêng bậc hai của hàm vô hướng |
| Critical point | điểm tới hạn | Điểm có gradient bằng 0 hoặc không xác định |
| Curvature | độ cong | Cách độ dốc biến thiên quanh vị trí đang xét |

## 3. Hàm Python và tham số quan trọng

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm / cú pháp | Cách sử dụng |
|---|---|
| `sympy.Matrix([...]).jacobian(vars)` | Đạo hàm riêng hàm vector theo biến |
| `sympy.hessian(f,vars)` | Đạo hàm bậc hai của hàm vô hướng |
| `sympy.solve(equations,vars)` | Tìm điểm thỏa hệ điều kiện |
| `np.linalg.eigvalsh(H)` | Xét dấu eigenvalue Hessian đối xứng tại điểm cực trị |

## 4. Khái niệm chính và liên quan

**Mạch kiến thức:** Với hàm có nhiều đầu ra, Jacobian ghi độ nhạy từng đầu ra theo các biến đầu vào. Với hàm loss một đầu ra, Hessian ghi độ cong theo cặp tham số; kết hợp gradient bằng 0 và dấu trị riêng Hessian mới giúp phân biệt cực trị với yên ngựa.

### 4.1. Jacobian — Đầu ra thay đổi theo từng đầu vào

**Từ vựng:** **Jacobian** — ma trận Jacobian; **Partial derivative** — đạo hàm riêng.

Khi một hàm có **n đầu vào và m đầu ra**, Jacobian là bảng kích thước **m hàng đầu ra × n cột đầu vào**, tại mỗi ô là đạo hàm riêng của đầu ra hàng đó theo đầu vào cột đó. Với `F1=x+y`, `F2=xy`, các hàng lần lượt đại diện F1, F2; các cột theo x,y. Tại `(x,y)=(3,2)`, Jacobian bằng `[[1,1],[2,3]]`. Đây là độ nhạy cục bộ, không phải ma trận số liệu gốc.

```python
# Mục đích: Đầu ra thay đổi theo từng đầu vào.
import sympy as sp

x, y = sp.symbols('x y')
F = sp.Matrix([x + y, x * y])
J = F.jacobian([x, y])
print(J.subs({x: 3, y: 2}).tolist())
```

**Kết quả khi chạy:**

```text
[[1, 1], [2, 3]]
```

Hàng 1 là độ nhạy của F1 theo x,y; hàng 2 là độ nhạy của F2 theo x,y.

### 4.2. Hessian — Độ thay đổi của gradient

**Từ vựng:** **Hessian** — ma trận Hessian; **Second derivative** — đạo hàm bậc hai.

**Hessian** là ma trận các đạo hàm riêng **bậc hai** của một hàm **đầu ra vô hướng**. Hàm loss `L(x,y)=x²+2y²` có Hessian `[[2,0],[0,4]]`. Hàng/cột đều tương ứng thứ tự **tham số x, y**; số 4 theo y lớn hơn 2 theo x nghĩa là độ cong theo y lớn hơn trong mô hình này. Khác Jacobian cho hàm nhiều đầu ra, Hessian giúp xem gradient đổi nhanh thế nào.

```python
# Mục đích: Độ thay đổi của gradient.
import sympy as sp

x, y = sp.symbols('x y')
loss = x ** 2 + 2 * y ** 2
print(sp.hessian(loss, [x, y]).tolist())
```

**Kết quả khi chạy:**

```text
[[2, 0], [0, 4]]
```

Hàm cong mạnh hơn theo y; hai đạo hàm chéo bằng 0.

### 4.3. Critical point — Điểm cần kiểm tra cực trị

**Từ vựng:** **Critical point** — điểm tới hạn; **Stationary point** — điểm dừng.

**Điểm dừng** của hàm khả vi có gradient bằng vector 0, tức không còn hướng tăng tuyến tính ngay tại điểm. Với `L(x,y)=(x−3)²+(y−2)²`, các đạo hàm `2(x−3)`, `2(y−2)` đều bằng 0 khi `(3,2)`. Đây là **ứng viên cực trị**, chưa đủ để nói là cực tiểu: hàm hình yên ngựa cũng có thể có gradient 0. Khái niệm critical point rộng hơn còn có điểm không khả vi ở miền trong.

```python
# Mục đích: Điểm cần kiểm tra cực trị.
import sympy as sp

x, y = sp.symbols('x y')
loss = (x - 3) ** 2 + (y - 2) ** 2
solution = sp.solve([sp.diff(loss, x), sp.diff(loss, y)], [x, y])
print(solution[x], solution[y])
```

**Kết quả khi chạy:**

```text
3 2
```

Gradient bằng 0 tại (3,2); cần xét độ cong để phân loại điểm này.

### 4.4. Curvature — Phân biệt cực tiểu, cực đại, yên ngựa

**Từ vựng:** **Curvature** — độ cong; **Eigenvalue** — trị riêng.

Tại một **điểm dừng** của hàm đủ trơn, dấu trị riêng Hessian giúp phân loại: **tất cả dương** → cực tiểu địa phương nghiêm ngặt; **tất cả âm** → cực đại địa phương nghiêm ngặt; **vừa dương vừa âm** → điểm yên ngựa. Ví dụ `x²−y²` có Hessian `diag(2,−2)`, nên tại (0,0) đi theo x hàm tăng nhưng đi theo y hàm giảm. Nếu có trị riêng bằng 0, phép thử Hessian đơn giản **chưa kết luận**.

```python
# Mục đích: Phân biệt cực tiểu, cực đại, yên ngựa.
import numpy as np

H = np.array([[2.0, 0.0], [0.0, -2.0]])
print(np.linalg.eigvalsh(H))
```

**Kết quả khi chạy:**

```text
[-2.  2.]
```

Một trị riêng âm, một dương nên Hessian bất định; (0,0) là điểm yên ngựa của x²−y².

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Độ nhạy của hai đầu ra cảm biến · Cấp 1: Jacobian của hai đầu ra

**Tình huống thực tế:** Hai chỉ số đầu ra của mô hình cảm biến là `F1=x+y`, `F2=xy`; x và y là hai đầu vào đã được chuẩn hóa cùng thang. Tại x=3,y=2, cần biết mỗi đầu ra nhạy ra sao khi một đầu vào thay đổi nhỏ.

**Vì sao chọn cách giải này?** Jacobian đo đạo hàm riêng của từng đầu ra theo từng đầu vào ở điểm đang xét.

**Quy trình giải:**

1. Khai báo hai đầu vào và hai biểu thức đầu ra.
2. Tạo Jacobian với cột theo [x,y].
3. Thay x=3,y=2 và in các hệ số độ nhạy.

```python
# Mục đích: Độ nhạy của hai đầu ra cảm biến.
import sympy as sp

x, y = sp.symbols('x y')
F = sp.Matrix([x + y, x * y])
J = F.jacobian([x, y])
print(J.subs({x: 3, y: 2}).tolist())
```

**Kết quả khi chạy:**

```text
[[1, 1], [2, 3]]
```

Đầu ra F2 nhạy 2 theo x và 3 theo y tại điểm xét, khác F1 luôn nhạy 1 theo mỗi biến.

**Bài thực hành nâng cấp — cấp 1/5:** Một hệ có **10 trạng thái đo** hai đầu vào a, b; mỗi hàng là một trạng thái, đầu ra là hai đại lượng tính từ chúng. Hãy tính Jacobian tại một quan sát cụ thể. Độ khó tăng từ đạo hàm riêng tại một điểm lên kiểm tra độ cong, cực trị và Jacobian hàng loạt; cấp 4–5 bỏ trạng thái có `NaN` khỏi phép tính.

```python
import numpy as np
import sympy as sp
# Mỗi hàng = 1 trạng thái hệ, a = áp suất (đơn vị mẫu), b = nhiệt (đơn vị mẫu).
xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ys = [20+(i*3)%11 for i in range(10)]
raw = np.column_stack((xs,ys)).astype(float)
clean = raw[np.isfinite(raw).all(axis=1)]
a,b = sp.symbols('a b')
outputs = sp.Matrix([a*a+b,a*b])
jac = outputs.jacobian([a,b])
loss = (a-3)**2+2*(b-5)**2
hess = sp.hessian(loss,(a,b))
result = np.asarray(jac.subs({a:clean[0,0],b:clean[0,1]}),dtype=float).round(3).tolist()
print("Số phép đo:",len(raw))
print("Kết quả:",result)
```

**Đọc kết quả:** Ma trận Jacobian của hai đầu ra/hai đầu vào có shape (2,2); khi xử lý tập dữ liệu, mỗi trạng thái hợp lệ tạo thêm một ma trận riêng.

### Tình huống 2 — Độ cong của loss hai tham số · Cấp 2: Hessian của loss

**Tình huống thực tế:** Loss mô hình là `L=x²+2y²` với x,y không đơn vị; đội phát triển muốn so độ cong hai hướng thay đổi tham số để chọn cách tối ưu.

**Vì sao chọn cách giải này?** Hessian chứa đạo hàm riêng bậc hai, so được mức cong theo hai tham số.

**Quy trình giải:**

1. Định nghĩa hàm loss hai biến.
2. Lấy Hessian theo thứ tự [x,y].
3. In ma trận 2×2, so các ô đường chéo.

```python
# Mục đích: Độ cong của loss hai tham số.
import sympy as sp

x, y = sp.symbols('x y')
loss = x ** 2 + 2 * y ** 2
print(sp.hessian(loss, [x, y]).tolist())
```

**Kết quả khi chạy:**

```text
[[2, 0], [0, 4]]
```

Mức cong theo y bằng 4, lớn hơn mức cong theo x bằng 2.

**Bài thực hành nâng cấp — cấp 2/5:** Một hệ có **12 trạng thái đo** hai đầu vào a, b; mỗi hàng là một trạng thái, đầu ra là hai đại lượng tính từ chúng. Hãy tính Hessian của hàm loss hai tham số. Độ khó tăng từ đạo hàm riêng tại một điểm lên kiểm tra độ cong, cực trị và Jacobian hàng loạt; cấp 4–5 bỏ trạng thái có `NaN` khỏi phép tính.

```python
import numpy as np
import sympy as sp
# Mỗi hàng = 1 trạng thái hệ, a = áp suất (đơn vị mẫu), b = nhiệt (đơn vị mẫu).
xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
ys = [20+(i*3)%11 for i in range(12)]
raw = np.column_stack((xs,ys)).astype(float)
clean = raw[np.isfinite(raw).all(axis=1)]
a,b = sp.symbols('a b')
outputs = sp.Matrix([a*a+b,a*b])
jac = outputs.jacobian([a,b])
loss = (a-3)**2+2*(b-5)**2
hess = sp.hessian(loss,(a,b))
result = {'hessian':np.asarray(hess,dtype=float).tolist(),'rows':len(clean)}
print("Số phép đo:",len(raw))
print("Kết quả:",result)
```

**Đọc kết quả:** Ma trận Jacobian của hai đầu ra/hai đầu vào có shape (2,2); khi xử lý tập dữ liệu, mỗi trạng thái hợp lệ tạo thêm một ma trận riêng.

### Tình huống 3 — Tìm bộ tham số làm loss nhỏ nhất · Cấp 3: Tìm điểm cực tiểu

**Tình huống thực tế:** Một mô hình có hàm loss `L=(x−3)²+(y−2)²`. Cần tìm hai tham số tại đó loss không còn giảm theo đạo hàm riêng bậc nhất.

**Vì sao chọn cách giải này?** Giải hệ gradient bằng 0 cho ứng viên tối ưu, rồi dùng dạng tổng bình phương để xác nhận cực tiểu.

**Quy trình giải:**

1. Lấy đạo hàm L theo x và y.
2. Giải đồng thời hai phương trình bằng 0.
3. In tọa độ bộ tham số nghiệm.

```python
# Mục đích: Tìm bộ tham số làm loss nhỏ nhất.
import sympy as sp

x, y = sp.symbols('x y')
loss = (x - 3) ** 2 + (y - 2) ** 2
solution = sp.solve([sp.diff(loss, x), sp.diff(loss, y)], [x, y])
print(solution[x], solution[y])
```

**Kết quả khi chạy:**

```text
3 2
```

Điểm (3,2) là cực tiểu toàn cục của tổng hai bình phương không âm.

**Bài thực hành nâng cấp — cấp 3/5:** Một hệ có **15 trạng thái đo** hai đầu vào a, b; mỗi hàng là một trạng thái, đầu ra là hai đại lượng tính từ chúng. Hãy tìm điểm gradient bằng 0 và xác nhận Hessian dương. Độ khó tăng từ đạo hàm riêng tại một điểm lên kiểm tra độ cong, cực trị và Jacobian hàng loạt; cấp 4–5 bỏ trạng thái có `NaN` khỏi phép tính.

```python
import numpy as np
import sympy as sp
# Mỗi hàng = 1 trạng thái hệ, a = áp suất (đơn vị mẫu), b = nhiệt (đơn vị mẫu).
xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
ys = [20+(i*3)%11 for i in range(15)]
raw = np.column_stack((xs,ys)).astype(float)
clean = raw[np.isfinite(raw).all(axis=1)]
a,b = sp.symbols('a b')
outputs = sp.Matrix([a*a+b,a*b])
jac = outputs.jacobian([a,b])
loss = (a-3)**2+2*(b-5)**2
hess = sp.hessian(loss,(a,b))
result = {'critical':sp.solve([sp.diff(loss,a),sp.diff(loss,b)],[a,b]),'hessian_eig':np.linalg.eigvalsh(np.asarray(hess,dtype=float)).tolist()}
print("Số phép đo:",len(raw))
print("Kết quả:",result)
```

**Đọc kết quả:** Ma trận Jacobian của hai đầu ra/hai đầu vào có shape (2,2); khi xử lý tập dữ liệu, mỗi trạng thái hợp lệ tạo thêm một ma trận riêng.

### Tình huống 4 — Phân biệt điểm yên ngựa với cực tiểu · Cấp 4: Phát hiện điểm yên ngựa

**Tình huống thực tế:** Loss thử nghiệm `L=x²−y²` có điểm dừng tại (0,0). Tuy nhiên theo trục x hàm tăng, theo trục y hàm giảm; nhóm kỹ thuật cần biết có phải cực tiểu không.

**Vì sao chọn cách giải này?** Trị riêng Hessian trái dấu là bằng chứng điểm dừng dạng yên ngựa.

**Quy trình giải:**

1. Tạo Hessian `[[2,0],[0,-2]]` tại điểm (0,0).
2. Tính trị riêng đối xứng bằng `eigvalsh`.
3. Kiểm tra có cả trị riêng âm và dương, in kết luận.

```python
# Mục đích: Phân biệt điểm yên ngựa với cực tiểu.
import numpy as np

H = np.array([[2.0, 0.0], [0.0, -2.0]])
values = np.linalg.eigvalsh(H)
print(bool((values < 0).any() and (values > 0).any()))
```

**Kết quả khi chạy:**

```text
True
```

Hessian bất định; điểm dừng này là yên ngựa, không phải cực tiểu.

**Bài thực hành nâng cấp — cấp 4/5:** Một hệ có **18 trạng thái đo** hai đầu vào a, b; mỗi hàng là một trạng thái, đầu ra là hai đại lượng tính từ chúng. Hãy so eigenvalue Hessian của điểm yên ngựa. Độ khó tăng từ đạo hàm riêng tại một điểm lên kiểm tra độ cong, cực trị và Jacobian hàng loạt; cấp 4–5 bỏ trạng thái có `NaN` khỏi phép tính.

```python
import numpy as np
import sympy as sp
# Mỗi hàng = 1 trạng thái hệ, a = áp suất (đơn vị mẫu), b = nhiệt (đơn vị mẫu).
xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, np.nan, 17, 18]
ys = [20+(i*3)%11 for i in range(18)]
raw = np.column_stack((xs,ys)).astype(float)
clean = raw[np.isfinite(raw).all(axis=1)]
a,b = sp.symbols('a b')
outputs = sp.Matrix([a*a+b,a*b])
jac = outputs.jacobian([a,b])
loss = (a-3)**2+2*(b-5)**2
hess = sp.hessian(loss,(a,b))
result = {'saddle_eig':np.linalg.eigvalsh(np.asarray(sp.hessian(a*a-b*b,(a,b)),dtype=float)).tolist(),'missing':len(raw)-len(clean)}
print("Số phép đo:",len(raw))
print("Kết quả:",result)
```

**Đọc kết quả:** Ma trận Jacobian của hai đầu ra/hai đầu vào có shape (2,2); khi xử lý tập dữ liệu, mỗi trạng thái hợp lệ tạo thêm một ma trận riêng.

### Tình huống 5 — Kiểm tra kích thước Jacobian · Cấp 5: Đánh giá 20 Jacobian và dữ liệu khuyết

**Tình huống thực tế:** Mô hình có ba đầu vào x,y,z và hai đầu ra `F1=x+y+z`, `F2=x*y`. Cần biết ma trận độ nhạy của mô hình có bao nhiêu hàng và cột.

**Vì sao chọn cách giải này?** Jacobian có một hàng cho mỗi đầu ra và một cột cho mỗi đầu vào; với 2 đầu ra, 3 đầu vào có shape (2,3).

**Quy trình giải:**

1. Khai báo ba đầu vào x,y,z.
2. Tạo hai đầu ra thành SymPy Matrix.
3. Tính Jacobian theo [x,y,z], in shape.

```python
# Mục đích: Kiểm tra kích thước Jacobian.
import sympy as sp

x, y, z = sp.symbols('x y z')
F = sp.Matrix([x + y + z, x * y])
print(F.jacobian([x, y, z]).shape)
```

**Kết quả khi chạy:**

```text
(2, 3)
```

Jacobian có hai hàng đầu ra và ba cột đầu vào, không nhất thiết là ma trận vuông.

**Bài thực hành nâng cấp — cấp 5/5:** Một hệ có **20 trạng thái đo** hai đầu vào a, b; mỗi hàng là một trạng thái, đầu ra là hai đại lượng tính từ chúng. Hãy tạo ma trận Jacobian cho mọi phép đo hợp lệ, đọc shape. Độ khó tăng từ đạo hàm riêng tại một điểm lên kiểm tra độ cong, cực trị và Jacobian hàng loạt; cấp 4–5 bỏ trạng thái có `NaN` khỏi phép tính.

```python
import numpy as np
import sympy as sp
# Mỗi hàng = 1 trạng thái hệ, a = áp suất (đơn vị mẫu), b = nhiệt (đơn vị mẫu).
xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, np.nan, 17, 18, 19, np.nan]
ys = [20+(i*3)%11 for i in range(20)]
raw = np.column_stack((xs,ys)).astype(float)
clean = raw[np.isfinite(raw).all(axis=1)]
a,b = sp.symbols('a b')
outputs = sp.Matrix([a*a+b,a*b])
jac = outputs.jacobian([a,b])
loss = (a-3)**2+2*(b-5)**2
hess = sp.hessian(loss,(a,b))
result = {'jacobian_shape':np.array([np.asarray(jac.subs({a:x,b:y}),dtype=float) for x,y in clean]).shape,'missing':len(raw)-len(clean),'hessian_eig':np.linalg.eigvalsh(np.asarray(hess,dtype=float)).tolist()}
print("Số phép đo:",len(raw))
print("Kết quả:",result)
```

**Đọc kết quả:** Ma trận Jacobian của hai đầu ra/hai đầu vào có shape (2,2); khi xử lý tập dữ liệu, mỗi trạng thái hợp lệ tạo thêm một ma trận riêng.

## 6. Sai lầm thường gặp

- Jacobian có số hàng bằng số đầu ra và số cột bằng số đầu vào; không luôn là ma trận vuông.
- Hessian dùng cho hàm vô hướng đủ khả vi hai lần; hàng/cột là các tham số, không phải hai đầu ra.
- Gradient bằng 0 mới chỉ chỉ ra điểm dừng, chưa đủ nói là cực tiểu.
- Hessian có trị riêng vừa âm vừa dương ở điểm dừng chỉ ra yên ngựa; nếu có trị riêng 0, bài kiểm bậc hai đơn giản chưa đủ.
- Khi dùng `eigvalsh`, ma trận đầu vào phải đối xứng theo phép toán đang xét.
- SymPy là thư viện ngoài; các ví dụ ký hiệu cần cài đặt.

## 7. Trắc nghiệm

**Q1. What does a Jacobian contain? | Jacobian chứa gì?**

A. First partial derivatives of vector outputs | Các đạo hàm riêng bậc một của đầu ra vector

B. Second partial derivatives of a scalar output | Các đạo hàm riêng bậc hai của đầu ra vô hướng

C. A differentiable point where the gradient is zero | Điểm khả vi có gradient bằng 0

D. Classifying local behavior near stationary points | Phân loại hành vi cục bộ gần điểm dừng

**Đáp án: A**

**Giải thích:** Mỗi hàng chứa đạo hàm bậc một của một đầu ra.


**Q2. What does a Hessian contain? | Hessian chứa gì?**

A. First partial derivatives of vector outputs | Các đạo hàm riêng bậc một của đầu ra vector

B. Second partial derivatives of a scalar output | Các đạo hàm riêng bậc hai của đầu ra vô hướng

C. A differentiable point where the gradient is zero | Điểm khả vi có gradient bằng 0

D. Classifying local behavior near stationary points | Phân loại hành vi cục bộ gần điểm dừng

**Đáp án: B**

**Giải thích:** Hessian lấy đạo hàm tiếp của gradient.


**Q3. What is a stationary point? | Điểm dừng là gì?**

A. First partial derivatives of vector outputs | Các đạo hàm riêng bậc một của đầu ra vector

B. Second partial derivatives of a scalar output | Các đạo hàm riêng bậc hai của đầu ra vô hướng

C. A differentiable point where the gradient is zero | Điểm khả vi có gradient bằng 0

D. Classifying local behavior near stationary points | Phân loại hành vi cục bộ gần điểm dừng

**Đáp án: C**

**Giải thích:** Điểm dừng có các đạo hàm riêng bậc một bằng 0.


**Q4. What is curvature information used for? | Thông tin độ cong dùng để làm gì?**

A. First partial derivatives of vector outputs | Các đạo hàm riêng bậc một của đầu ra vector

B. Second partial derivatives of a scalar output | Các đạo hàm riêng bậc hai của đầu ra vô hướng

C. A differentiable point where the gradient is zero | Điểm khả vi có gradient bằng 0

D. Classifying local behavior near stationary points | Phân loại hành vi cục bộ gần điểm dừng

**Đáp án: D**

**Giải thích:** Độ cong giúp phân loại điểm dừng.


**Q5. What is Jacobian shape for m outputs and n inputs? | Jacobian m đầu ra và n đầu vào có shape nào?**

A. `(m,n)` | `(m,n)`

B. `.jacobian(variables)` | `.jacobian(variables)`

C. `sp.hessian(f, variables)` | `sp.hessian(f, variables)`

D. `np.linalg.eigvalsh(H)` | `np.linalg.eigvalsh(H)`

**Đáp án: A**

**Giải thích:** Mỗi đầu ra là một hàng, mỗi đầu vào là một cột.


**Q6. Which SymPy method builds a Jacobian? | Hàm SymPy nào tạo Jacobian?**

A. `(m,n)` | `(m,n)`

B. `.jacobian(variables)` | `.jacobian(variables)`

C. `sp.hessian(f, variables)` | `sp.hessian(f, variables)`

D. `np.linalg.eigvalsh(H)` | `np.linalg.eigvalsh(H)`

**Đáp án: B**

**Giải thích:** Phương thức lấy mọi đạo hàm riêng bậc một.


**Q7. Which SymPy function builds a Hessian? | Hàm SymPy nào tạo Hessian?**

A. `(m,n)` | `(m,n)`

B. `.jacobian(variables)` | `.jacobian(variables)`

C. `sp.hessian(f, variables)` | `sp.hessian(f, variables)`

D. `np.linalg.eigvalsh(H)` | `np.linalg.eigvalsh(H)`

**Đáp án: C**

**Giải thích:** hessian tính các đạo hàm riêng bậc hai.


**Q8. Which tool computes symmetric Hessian eigenvalues? | Hàm nào tính trị riêng Hessian đối xứng?**

A. `(m,n)` | `(m,n)`

B. `.jacobian(variables)` | `.jacobian(variables)`

C. `sp.hessian(f, variables)` | `sp.hessian(f, variables)`

D. `np.linalg.eigvalsh(H)` | `np.linalg.eigvalsh(H)`

**Đáp án: D**

**Giải thích:** eigvalsh tính trị riêng ma trận đối xứng.


**Q9. What is Hessian of x²+y²? | Hessian của x²+y² là gì?**

A. `[[2,0],[0,2]]` | `[[2,0],[0,2]]`

B. `[[2,0],[0,-2]]` | `[[2,0],[0,-2]]`

C. `(3,2)` | `(3,2)`

D. `[[1,1],[y,x]]` | `[[1,1],[y,x]]`

**Đáp án: A**

**Giải thích:** Đạo hàm bậc hai của mỗi hạng bình phương bằng 2.


**Q10. What is Hessian of x²−y²? | Hessian của x²−y² là gì?**

A. `[[2,0],[0,2]]` | `[[2,0],[0,2]]`

B. `[[2,0],[0,-2]]` | `[[2,0],[0,-2]]`

C. `(3,2)` | `(3,2)`

D. `[[1,1],[y,x]]` | `[[1,1],[y,x]]`

**Đáp án: B**

**Giải thích:** Độ cong theo y bằng âm 2.


**Q11. What are stationary coordinates for (x−3)²+(y−2)²? | Tọa độ dừng của (x−3)²+(y−2)² là gì?**

A. `[[2,0],[0,2]]` | `[[2,0],[0,2]]`

B. `[[2,0],[0,-2]]` | `[[2,0],[0,-2]]`

C. `(3,2)` | `(3,2)`

D. `[[1,1],[y,x]]` | `[[1,1],[y,x]]`

**Đáp án: C**

**Giải thích:** Cả hai bình phương nhỏ nhất khi sai khác bằng 0.


**Q12. What is Jacobian of outputs x+y and xy? | Jacobian của đầu ra x+y và xy là gì?**

A. `[[2,0],[0,2]]` | `[[2,0],[0,2]]`

B. `[[2,0],[0,-2]]` | `[[2,0],[0,-2]]`

C. `(3,2)` | `(3,2)`

D. `[[1,1],[y,x]]` | `[[1,1],[y,x]]`

**Đáp án: D**

**Giải thích:** Lấy đạo hàm mỗi đầu ra theo x và y.


**Q13. What does a positive-definite Hessian at a stationary point indicate? | Hessian xác định dương tại điểm dừng biểu thị gì?**

A. A strict local minimum | Cực tiểu địa phương nghiêm ngặt

B. A strict local maximum | Cực đại địa phương nghiêm ngặt

C. A saddle point | Điểm yên ngựa

D. The simple second-derivative test is inconclusive | Phép kiểm đạo hàm bậc hai đơn giản chưa kết luận

**Đáp án: A**

**Giải thích:** Độ cong dương mọi hướng cho cực tiểu địa phương nghiêm ngặt.


**Q14. What does a negative-definite Hessian at a stationary point indicate? | Hessian xác định âm tại điểm dừng biểu thị gì?**

A. A strict local minimum | Cực tiểu địa phương nghiêm ngặt

B. A strict local maximum | Cực đại địa phương nghiêm ngặt

C. A saddle point | Điểm yên ngựa

D. The simple second-derivative test is inconclusive | Phép kiểm đạo hàm bậc hai đơn giản chưa kết luận

**Đáp án: B**

**Giải thích:** Độ cong âm mọi hướng cho cực đại địa phương nghiêm ngặt.


**Q15. What do mixed-sign Hessian eigenvalues indicate at a stationary point? | Trị riêng Hessian trái dấu ở điểm dừng biểu thị gì?**

A. A strict local minimum | Cực tiểu địa phương nghiêm ngặt

B. A strict local maximum | Cực đại địa phương nghiêm ngặt

C. A saddle point | Điểm yên ngựa

D. The simple second-derivative test is inconclusive | Phép kiểm đạo hàm bậc hai đơn giản chưa kết luận

**Đáp án: C**

**Giải thích:** Một số hướng tăng và hướng khác giảm.


**Q16. What if a Hessian has a zero eigenvalue at a stationary point? | Nếu Hessian có trị riêng 0 tại điểm dừng thì sao?**

A. A strict local minimum | Cực tiểu địa phương nghiêm ngặt

B. A strict local maximum | Cực đại địa phương nghiêm ngặt

C. A saddle point | Điểm yên ngựa

D. The simple second-derivative test is inconclusive | Phép kiểm đạo hàm bậc hai đơn giản chưa kết luận

**Đáp án: D**

**Giải thích:** Trị riêng 0 cần kiểm tra sâu hơn.


**Q17. What is Hessian shape for a scalar function of three inputs? | Hessian hàm vô hướng ba biến có shape nào?**

A. `(3,3)` | `(3,3)`

B. Sensitivities of one output to each input | Độ nhạy của một đầu ra theo từng đầu vào

C. How each output responds to one input | Các đầu ra đáp ứng với một đầu vào

D. It can also occur at a maximum or saddle | Nó còn xuất hiện ở cực đại hoặc yên ngựa

**Đáp án: A**

**Giải thích:** Các đạo hàm riêng bậc hai ghép từng biến với biến khác.


**Q18. What does one Jacobian row represent? | Một hàng Jacobian biểu thị gì?**

A. `(3,3)` | `(3,3)`

B. Sensitivities of one output to each input | Độ nhạy của một đầu ra theo từng đầu vào

C. How each output responds to one input | Các đầu ra đáp ứng với một đầu vào

D. It can also occur at a maximum or saddle | Nó còn xuất hiện ở cực đại hoặc yên ngựa

**Đáp án: B**

**Giải thích:** Hàng cố định đầu ra, cột đổi đầu vào.


**Q19. What does one Jacobian column represent? | Một cột Jacobian biểu thị gì?**

A. `(3,3)` | `(3,3)`

B. Sensitivities of one output to each input | Độ nhạy của một đầu ra theo từng đầu vào

C. How each output responds to one input | Các đầu ra đáp ứng với một đầu vào

D. It can also occur at a maximum or saddle | Nó còn xuất hiện ở cực đại hoặc yên ngựa

**Đáp án: C**

**Giải thích:** Cột cố định một đầu vào qua mọi đầu ra.


**Q20. Why isn't zero gradient alone sufficient to prove a minimum? | Vì sao gradient 0 chưa đủ chứng minh cực tiểu?**

A. `(3,3)` | `(3,3)`

B. Sensitivities of one output to each input | Độ nhạy của một đầu ra theo từng đầu vào

C. How each output responds to one input | Các đầu ra đáp ứng với một đầu vào

D. It can also occur at a maximum or saddle | Nó còn xuất hiện ở cực đại hoặc yên ngựa

**Đáp án: D**

**Giải thích:** Cực đại và yên ngựa cũng có thể có gradient 0.

## 8. Liên hệ bài tiếp theo

`Gradient → Jacobian → Hessian → Tối ưu mô hình`.
