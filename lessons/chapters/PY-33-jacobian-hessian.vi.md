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

**No Note — Không chú thích**

```python
import sympy as sp

x, y = sp.symbols('x y')
F = sp.Matrix([x + y, x * y])
J = F.jacobian([x, y])
print(J.subs({x: 3, y: 2}).tolist())
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Lập Jacobian để đo mức thay đổi của hai đầu ra theo hai đầu vào x,y.
# Dữ liệu: F=(x+y, x*y), điểm kiểm x=3,y=2; Jacobian có hai hàng đầu ra × hai cột đầu vào.
# SymPy xây hàm nhiều biến và đạo hàm riêng bằng ký hiệu.
import sympy as sp

# Tạo hai biến tượng trưng x,y; chưa thế bằng dữ liệu số.
x, y = sp.symbols('x y')
# Matrix tạo vector CỘT gồm hai biểu thức đầu ra: tổng và tích của x,y.
F = sp.Matrix([x + y, x * y])
# jacobian([x,y]) tạo bảng đạo hàm riêng, mỗi HÀNG cho một đầu ra, mỗi CỘT cho một biến; shape (2,2).
J = F.jacobian([x, y])
# subs({x:3,y:2}) thế đồng thời hai tọa độ để có Jacobian số tại điểm đó.
# tolist() chuyển ma trận SymPy thành list hai hàng để hiển thị dễ đọc.
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

**No Note — Không chú thích**

```python
import sympy as sp

x, y = sp.symbols('x y')
loss = x ** 2 + 2 * y ** 2
print(sp.hessian(loss, [x, y]).tolist())
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tính Hessian của hàm loss hai biến để biết độ cong ở từng hướng.
# Dữ liệu: Loss=x²+2y², độ cong theo y lớn gấp đôi độ cong x.
# SymPy sp.hessian() tính đạo hàm riêng cấp hai.
import sympy as sp

# x,y là hai tham số cần khảo sát độ cong.
x, y = sp.symbols('x y')
# Hàm loss parabol hai chiều, hệ số y lớn hơn làm bề mặt dốc hơn theo y.
loss = x ** 2 + 2 * y ** 2
# hessian(f,[x,y]) tạo ma trận các đạo hàm riêng bậc hai, gồm ∂²f/∂x², ∂²f/∂x∂y,...; ở đây [[2,0],[0,4]].
# Chuyển SymPy Matrix thành list lồng để in hai hàng.
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

**No Note — Không chú thích**

```python
import sympy as sp

x, y = sp.symbols('x y')
loss = (x - 3) ** 2 + (y - 2) ** 2
solution = sp.solve([sp.diff(loss, x), sp.diff(loss, y)], [x, y])
print(solution[x], solution[y])
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Giải hệ gradient bằng 0 để tìm điểm dừng của hàm loss hai biến.
# Dữ liệu: Loss=(x-3)²+(y-2)², kỳ vọng điểm tối thiểu tại (3,2).
# SymPy tạo phương trình ký hiệu và giải đồng thời.
import sympy as sp

# Khai báo hai biến đầu vào x,y.
x, y = sp.symbols('x y')
# Hai bình phương không âm, bằng 0 tại x=3, y=2.
loss = (x - 3) ** 2 + (y - 2) ** 2
# diff(loss,x) lấy đạo hàm riêng theo x để xét điểm dừng.
# diff(loss,y) lấy đạo hàm riêng theo y.
# solve(danh_sách_phương_trình,[x,y]) tìm nghiệm đồng thời khi cả hai thành phần gradient bằng 0.
solution = sp.solve([sp.diff(loss, x), sp.diff(loss, y)], [x, y])
# solution là dictionary nghiệm theo ký hiệu; [x] là giá trị x, [y] là giá trị y.
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

**No Note — Không chú thích**

```python
import numpy as np

H = np.array([[2.0, 0.0], [0.0, -2.0]])
print(np.linalg.eigvalsh(H))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Quan sát dấu của trị riêng Hessian để nhận diện bề mặt có hướng lên và hướng xuống.
# Dữ liệu: Hessian H=diag(2,-2), một hướng cong lên và một hướng cong xuống: dạng yên ngựa.
# NumPy eigvalsh() lấy trị riêng của ma trận thực đối xứng.
import numpy as np

# Ma trận Hessian đối xứng 2×2 với một trị riêng dương và một âm.
H = np.array([[2.0, 0.0], [0.0, -2.0]])
# eigvalsh() trả trị riêng tăng dần [-2,2]; trái dấu nghĩa Hessian bất định, chỉ dạng yên ngựa tại điểm dừng tương ứng.
print(np.linalg.eigvalsh(H))
```

**Kết quả khi chạy:**

```text
[-2.  2.]
```

Một trị riêng âm, một dương nên Hessian bất định; (0,0) là điểm yên ngựa của x²−y².

## 5. Năm tình huống Jacobian/Hessian — từ độ nhạy đến suy biến cục bộ

### Tình huống 1 — Cấp 1: Jacobian của hai đầu ra trên 10 cặp tín hiệu

**Từ vựng trong mục:** **Jacobian** — ma trận độ nhạy; **Partial derivative** — đạo hàm riêng.

**Tình huống thực tế:** Trạm đo có **10 cặp đầu vào x và y không đơn vị**; mỗi hàng đại diện một lượt đo, chẳng hạn lượt đầu x = 2, y = 3. Phần mềm tạo **hai chỉ số đầu ra**: một chỉ số cộng x với y, chỉ số kia nhân x với y. Kỹ thuật viên muốn biết khi **chỉ x hoặc chỉ y thay đổi rất ít**, hai kết quả nhạy đến đâu tại **lượt đầu**, để tránh nhầm đầu ra nào bị ảnh hưởng bởi biến nào.

**Vì sao chọn cách này?** **Jacobian** là một **bảng độ nhạy**: mỗi **hàng ứng với một chỉ số đầu ra**, mỗi **cột ứng với một biến đầu vào**. Một ô cho biết đầu ra ở hàng ấy thay đổi nhanh cỡ nào nếu tăng rất ít biến ở cột ấy, giữ biến kia cố định. `outputs.jacobian([x, y])` tạo bảng **2 × 2** từ hai quy tắc, rồi `subs` đưa x = 2 và y = 3 của lượt đầu vào để xem các độ nhạy tại đúng hoàn cảnh đó. Đây **không phải bảng 10 lượt đo**; 10 là số dữ liệu đã lấy, còn kích thước Jacobian được quyết định bởi số đầu ra và số đầu vào.

**Quy trình:**
1. Tạo 10 cặp x/y rồi định nghĩa hai đầu ra bằng SymPy.
2. Gọi `jacobian([x,y])` cho hàm vector.
3. Thay cặp đầu tiên vào Jacobian và in ma trận 2×2.

**No Note — Không chú thích**

```python
import sympy as sp
x, y = sp.symbols("x y")
inputs = [[2,3],[3,3],[4,3],[5,3],[6,3],[2,4],[3,4],[4,4],[5,4],[6,4]]
outputs = sp.Matrix([x+y, x*y])
J = outputs.jacobian([x, y])
first = J.subs({x: inputs[0][0], y: inputs[0][1]})
if len(inputs) != 10 or J.shape != (2, 2):
    raise ValueError("Cần 10 cặp đầu vào và Jacobian 2×2.")
print("Cặp đầu vào:", len(inputs))
print("Jacobian cặp đầu:", first.tolist())
print("Shape Jacobian:", J.shape)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tính Jacobian tại cặp đầu tiên trong 10 cặp (x,y) với hai đầu ra.
# Dữ liệu: 10 cặp điểm trên lưới x=2..6, y=3..4; đầu ra là x+y và x*y.
# SymPy xây biểu thức vector và Jacobian có thể thế tại nhiều điểm.
import sympy as sp
# Khai báo x,y là hai biến ký hiệu.
x, y = sp.symbols("x y")
# 10 list con, mỗi list là cặp [x,y], không phải 10 biến độc lập.
inputs = [[2,3],[3,3],[4,3],[5,3],[6,3],[2,4],[3,4],[4,4],[5,4],[6,4]]
# Matrix chứa hai hàm đầu ra theo thứ tự tổng, tích.
outputs = sp.Matrix([x+y, x*y])
# jacobian() cho ma trận 2 đầu ra × 2 đầu vào, hàng thể hiện đầu ra, cột thể hiện biến.
J = outputs.jacobian([x, y])
# [0] ngoài lấy cặp đầu tiên, [0] trong lấy x, [1] lấy y của cặp đó.
# subs() thế cả x và y của cặp đầu vào thứ nhất vào Jacobian ký hiệu.
first = J.subs({x: inputs[0][0], y: inputs[0][1]})
# shape là kích thước (2,2) của Jacobian, không phải 10 cặp điểm.
if len(inputs) != 10 or J.shape != (2, 2):
    # raise ValueError báo điều kiện số mẫu, shape hoặc phép đối chiếu thất bại.
    raise ValueError("Cần 10 cặp đầu vào và Jacobian 2×2.")
print("Cặp đầu vào:", len(inputs))
# tolist() đổi ma trận SymPy đã thế số thành list lồng hai hàng.
print("Jacobian cặp đầu:", first.tolist())
# shape là kích thước (2,2) của Jacobian, không phải 10 cặp điểm.
print("Shape Jacobian:", J.shape)
```

**Kết quả khi chạy:**

```text
Cặp đầu vào: 10
Jacobian cặp đầu: [[1, 1], [3, 2]]
Shape Jacobian: (2, 2)
```

Hàng đầu của Jacobian nói về F1, hàng thứ hai về F2; số `3` ở hàng F2/cột x có nghĩa là F2 thay đổi khoảng 3 đơn vị khi x tăng 1 đơn vị rất nhỏ tại cặp đầu.

### Tình huống 2 — Cấp 2: Hessian cho độ cong loss tại 12 cấu hình tham số

**Từ vựng trong mục:** **Hessian** — ma trận đạo hàm bậc hai; **Curvature** — độ cong.

**Tình huống thực tế:** Đội tối ưu thử **12 cặp thông số x, y không đơn vị** cho một hàm mất mát giả lập. Khi đi xa điểm tốt nhất, loss tăng theo cả hai hướng nhưng tăng **nhanh hơn theo y** so với x. Nhóm muốn xác nhận **độ cong** của bề mặt loss ở hai hướng, và xem độ cong ấy có đổi theo 12 cặp thông số hay giữ nguyên.

**Vì sao chọn cách này?** **Gradient** cho biết loss đổi nhanh theo từng thông số, còn **Hessian** cho biết chính các độ dốc ấy **thay đổi nhanh đến đâu**, tức **độ cong** của bề mặt. `sp.hessian(loss, [x, y])` tạo bảng độ cong theo cả hai hướng và sự tương tác giữa chúng. Với bề mặt bậc hai trong bài, Hessian **không phụ thuộc vị trí x, y**, nên kiểm cấu hình đầu và cuối sẽ giống nhau; thành phần theo y lớn hơn theo x, cho thấy cong mạnh hơn theo y. Đừng nhầm loss ở mỗi cấu hình khác nhau với việc **Hessian cũng phải khác**.

**Quy trình:**
1. Lưu 12 cặp thử và định nghĩa loss bằng SymPy.
2. Tính Hessian theo đúng thứ tự x, y.
3. Đánh giá Hessian tại điểm đầu/cuối và kiểm hai ma trận giống nhau.

**No Note — Không chú thích**

```python
import sympy as sp
x, y = sp.symbols("x y")
points = [[-1,-1],[0,-1],[1,-1],[2,-1],[-1,0],[0,0],[1,0],[2,0],[-1,1],[0,1],[1,1],[2,1]]
loss = x**2 + 2*y**2
H = sp.hessian(loss, [x, y])
first = H.subs({x: points[0][0], y: points[0][1]})
last = H.subs({x: points[-1][0], y: points[-1][1]})
if len(points) != 12:
    raise ValueError("Cần đủ 12 cấu hình Hessian.")
print("Cấu hình:", len(points))
print("Hessian:", H.tolist())
print("Hessian không đổi:", first == last)
print("Cong hơn theo y:", H[1,1] > H[0,0])
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Xem Hessian không đổi theo 12 điểm vì hàm chi phí là đa thức bậc hai.
# Dữ liệu: 12 cấu hình (x,y), loss=x²+2y² nên Hessian luôn [[2,0],[0,4]].
# SymPy tính đạo hàm bậc hai chính xác trên biểu thức.
import sympy as sp
# Tạo hai biến ký hiệu.
x, y = sp.symbols("x y")
# 12 điểm là 12 cấu hình, mỗi list gồm hai tọa độ x/y.
points = [[-1,-1],[0,-1],[1,-1],[2,-1],[-1,0],[0,0],[1,0],[2,0],[-1,1],[0,1],[1,1],[2,1]]
# Bậc hai có độ cong không phụ thuộc vị trí: theo x hệ số cong 2, y hệ số cong 4.
loss = x**2 + 2*y**2
# hessian() tạo bảng các đạo hàm riêng cấp hai, theo thứ tự biến [x,y].
H = sp.hessian(loss, [x, y])
# Hai chỉ số chọn x/y của điểm ĐẦU; [-1] chọn điểm CUỐI.
# Thế tọa độ đầu vào Hessian để kiểm giá trị tại điểm đó.
first = H.subs({x: points[0][0], y: points[0][1]})
# [-1] chọn cấu hình cuối, [0]/[1] chọn x/y của cấu hình.
last = H.subs({x: points[-1][0], y: points[-1][1]})
if len(points) != 12:
    # raise ValueError báo điều kiện số mẫu, shape hoặc phép đối chiếu thất bại.
    raise ValueError("Cần đủ 12 cấu hình Hessian.")
print("Cấu hình:", len(points))
# tolist() trình bày Hessian thành list 2×2.
print("Hessian:", H.tolist())
# So hai SymPy Matrix bằng == để kiểm Hessian không đổi giữa hai cấu hình.
print("Hessian không đổi:", first == last)
# [1,1] là đạo hàm riêng bậc hai theo y, [0,0] theo x; so xem bề mặt cong hơn theo y.
print("Cong hơn theo y:", H[1,1] > H[0,0])
```

**Kết quả khi chạy:**

```text
Cấu hình: 12
Hessian: [[2, 0], [0, 4]]
Hessian không đổi: True
Cong hơn theo y: True
```

Độ cong là thông số của mô hình loss, không phải tọa độ x/y được đo từ 12 cấu hình.

### Tình huống 3 — Cấp 3: Tìm cực tiểu của loss hai tham số từ 15 ứng viên

**Từ vựng trong mục:** **Stationary point** — điểm dừng; **Minimum** — cực tiểu; **Eigenvalues** — trị riêng.

**Tình huống thực tế:** Nhóm hiệu chỉnh có **15 phương án cài đặt máy** theo lưới gồm năm giá trị x và ba giá trị y. Điểm đánh giá (loss, không đơn vị) nhỏ nhất theo thiết kế ở **x = 3, y = 2**. Kỹ thuật viên muốn dùng quy tắc toán học tìm điểm tốt nhất, kiểm chứng đây là **đáy** chứ không phải đỉnh, rồi xem trong 15 phương án có đúng cấu hình tốt nhất ấy không.

**Vì sao chọn cách này?** Để tìm **điểm dừng**, chương trình dùng `sympy.diff` tính độ dốc theo x/y và `sympy.solve` tìm nơi cả hai độ dốc **đều bằng 0**. Nhưng điểm dừng **chưa chắc là nhỏ nhất**. `sp.hessian` lấy độ cong; `np.linalg.eigvalsh` kiểm các **trị riêng** của bảng Hessian: ở ví dụ này **tất cả đều dương**, nghĩa là bề mặt cong lên theo mọi hướng, nên điểm dừng là **cực tiểu nghiêm ngặt**. Vòng lặp đánh giá cả **15 cấu hình có sẵn**, dùng `argmin` tìm vị trí có loss nhỏ nhất và đổi vị trí đó sang mã T01…; đây là bước so nghiệm toán học với phương án thực tế.

**Quy trình:**
1. Dùng SymPy giải đồng thời hai thành phần gradient bằng 0.
2. Dùng Hessian và trị riêng để phân loại điểm dừng.
3. So loss của 15 ứng viên, in mã ứng viên tốt nhất và nghiệm chính xác.

**No Note — Không chú thích**

```python
import sympy as sp
import numpy as np
x, y = sp.symbols("x y")
points = [[1,1],[2,1],[3,1],[4,1],[5,1],[1,2],[2,2],[3,2],[4,2],[5,2],[1,3],[2,3],[3,3],[4,3],[5,3]]
loss = (x-3)**2 + 2*(y-2)**2
solution = sp.solve([sp.diff(loss,x), sp.diff(loss,y)], [x,y])
H = np.array(sp.hessian(loss,[x,y])).astype(float)
eigenvalues = np.linalg.eigvalsh(H)
losses = []
for px, py in points:
    losses.append((px-3)**2 + 2*(py-2)**2)
if len(points) != 15:
    raise ValueError("Cần đủ 15 ứng viên cần đánh giá.")
print("Ứng viên:", len(points))
print("Điểm dừng:", solution[x], solution[y])
print("Hessian dương:", bool(np.all(eigenvalues > 0)))
print("Ứng viên tốt nhất:", f"T{int(np.argmin(losses))+1:02d}")
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tìm điểm dừng tối thiểu trong 15 ứng viên và xác nhận Hessian dương xác định.
# Dữ liệu: 15 điểm ứng viên x=1..5, y=1..3; loss=(x-3)²+2(y-2)².
# SymPy giải gradient bằng 0 và tính Hessian ký hiệu.
import sympy as sp
# NumPy kiểm trị riêng của Hessian, argmin() chọn ứng viên.
import numpy as np
# x,y là hai tham số mục tiêu.
x, y = sp.symbols("x y")
# 15 list điểm ứng viên, mỗi hàng một cặp x,y.
points = [[1,1],[2,1],[3,1],[4,1],[5,1],[1,2],[2,2],[3,2],[4,2],[5,2],[1,3],[2,3],[3,3],[4,3],[5,3]]
# Hàm không âm, bằng 0 ở (3,2); hệ số y khiến hướng y cong mạnh hơn.
loss = (x-3)**2 + 2*(y-2)**2
# Đạo hàm riêng theo x, kết hợp đạo hàm y thành hệ điều kiện điểm dừng.
# solve() giải đồng thời gradient_x=0 và gradient_y=0, cho nghiệm theo x,y.
solution = sp.solve([sp.diff(loss,x), sp.diff(loss,y)], [x,y])
# hessian() trả ma trận đạo hàm riêng bậc hai của loss theo [x,y].
# Đổi SymPy Hessian thành NumPy array để tính trị riêng bằng numpy.linalg.
# astype(float) ép giá trị ký hiệu sang float để eigvalsh() xử lý ma trận số.
H = np.array(sp.hessian(loss,[x,y])).astype(float)
# eigvalsh() trả trị riêng Hessian tăng dần; tất cả dương nghĩa cong lên ở mọi hướng.
eigenvalues = np.linalg.eigvalsh(H)
losses = []
# Duyệt từng cặp ứng viên, tách x/y.
for px, py in points:
    # append() lưu giá trị loss của mỗi ứng viên theo thứ tự points.
    losses.append((px-3)**2 + 2*(py-2)**2)
if len(points) != 15:
    # raise ValueError báo điều kiện số mẫu, shape hoặc phép đối chiếu thất bại.
    raise ValueError("Cần đủ 15 ứng viên cần đánh giá.")
print("Ứng viên:", len(points))
# Lấy tọa độ điểm dừng đã giải từ dictionary SymPy.
print("Điểm dừng:", solution[x], solution[y])
# Mask trị riêng >0; np.all() yêu cầu TẤT CẢ dương, xác nhận Hessian dương xác định.
print("Hessian dương:", bool(np.all(eigenvalues > 0)))
# argmin() trả vị trí 0-based của loss nhỏ nhất trong 15 ứng viên, không trả chính trị loss.
# int() chuyển chỉ số, +1 đổi sang số thứ tự 1-based và :02d tạo mã hai chữ số.
print("Ứng viên tốt nhất:", f"T{int(np.argmin(losses))+1:02d}")
```

**Kết quả khi chạy:**

```text
Ứng viên: 15
Điểm dừng: 3 2
Hessian dương: True
Ứng viên tốt nhất: T08
```

Tên 'tốt nhất' ở đây có nghĩa **loss nhỏ nhất trên đúng 15 phương án đã cho**; bài toán thực tế còn cần kiểm giới hạn vận hành của thiết bị.

### Tình huống 4 — Cấp 4: Phân loại 18 mô hình có điểm dừng: min/max/yên ngựa

**Từ vựng trong mục:** **Critical point** — điểm dừng; **Positive definite** — xác định dương; **Saddle** — yên ngựa.

**Tình huống thực tế:** Đội nghiên cứu thử **18 phiên bản hàm loss giả lập** M01–M18. Mỗi phiên bản thuộc một trong ba kiểu bề mặt: **chiếc bát có đáy** (cực tiểu), **chiếc vòm có đỉnh** (cực đại), hoặc **mặt yên ngựa** (đi lên theo một hướng nhưng đi xuống theo hướng kia). Cả ba kiểu đều có một điểm mà độ dốc bằng 0, nên nhóm muốn phân loại thật sự từ **độ cong**, đếm từng loại thay vì gọi mọi điểm dừng là điểm tối ưu.

**Vì sao chọn cách này?** Độ dốc bằng 0 chỉ nói rằng **ngay tại điểm đó đường không nghiêng về một hướng cụ thể**, chứ không cho biết đó là đáy, đỉnh hay yên ngựa. **Hessian** cung cấp thông tin về độ cong; `eigvalsh` trả các trị riêng của bảng độ cong đối xứng. Trong ba hàm bậc hai minh họa, **toàn dương** nghĩa là đáy, **toàn âm** là đỉnh, còn **vừa dương vừa âm** là yên ngựa. Chương trình đọc lần lượt **18 mô hình** và tự phân loại từ kết quả tính, không chỉ tin nhãn `type` ghi trong dữ liệu. Quy tắc dấu này áp dụng rõ ràng cho các hàm ở bài; tình huống Hessian có trị riêng bằng 0 cần xem xét thêm, không vội kết luận.

**Quy trình:**
1. Lưu 18 mã/công thức và định nghĩa Hessian của ba công thức bằng SymPy.
2. Lấy các trị riêng Hessian thực đối xứng cho mỗi phiên bản.
3. Đếm ba loại, xác nhận tổng 18.

**No Note — Không chú thích**

```python
import numpy as np
import sympy as sp
x,y = sp.symbols("x y")
models = [{"id":"M01","type":"minimum"},{"id":"M02","type":"maximum"},{"id":"M03","type":"saddle"},{"id":"M04","type":"minimum"},{"id":"M05","type":"maximum"},{"id":"M06","type":"saddle"},{"id":"M07","type":"minimum"},{"id":"M08","type":"maximum"},{"id":"M09","type":"saddle"},{"id":"M10","type":"minimum"},{"id":"M11","type":"maximum"},{"id":"M12","type":"saddle"},{"id":"M13","type":"minimum"},{"id":"M14","type":"maximum"},{"id":"M15","type":"saddle"},{"id":"M16","type":"minimum"},{"id":"M17","type":"maximum"},{"id":"M18","type":"saddle"}]
functions = {"minimum": x*x+2*y*y,
             "maximum": -x*x-2*y*y,
             "saddle": x*x-y*y}
results = []
for row in models:
    H = np.array(sp.hessian(functions[row["type"]],[x,y]), dtype=float)
    eig = np.linalg.eigvalsh(H)
    if np.all(eig > 0):
        kind = "minimum"
    elif np.all(eig < 0):
        kind = "maximum"
    else:
        kind = "saddle"
    results.append(kind)
if len(models) != 18:
    raise ValueError("Cần đủ 18 mô hình cực trị.")
print("Mô hình:", len(models))
print("Cực tiểu:", results.count("minimum"))
print("Cực đại:", results.count("maximum"))
print("Yên ngựa:", results.count("saddle"))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Phân nhóm 18 hàm bậc hai theo trị riêng Hessian: cực tiểu, cực đại, yên ngựa.
# Dữ liệu: 18 mô hình lặp ba dạng loss: x²+2y², -x²-2y², x²-y², mỗi dạng sáu lượt.
# NumPy chuyển Hessian SymPy thành số và kiểm trị riêng.
import numpy as np
# SymPy tạo ba hàm bậc hai và tính Hessian.
import sympy as sp
# Hai biến x,y cho mỗi bề mặt.
x,y = sp.symbols("x y")
# 18 dictionary với id và type mô hình; type chỉ tên kiểm thử, phân loại vẫn dựa Hessian.
models = [{"id":"M01","type":"minimum"},{"id":"M02","type":"maximum"},{"id":"M03","type":"saddle"},{"id":"M04","type":"minimum"},{"id":"M05","type":"maximum"},{"id":"M06","type":"saddle"},{"id":"M07","type":"minimum"},{"id":"M08","type":"maximum"},{"id":"M09","type":"saddle"},{"id":"M10","type":"minimum"},{"id":"M11","type":"maximum"},{"id":"M12","type":"saddle"},{"id":"M13","type":"minimum"},{"id":"M14","type":"maximum"},{"id":"M15","type":"saddle"},{"id":"M16","type":"minimum"},{"id":"M17","type":"maximum"},{"id":"M18","type":"saddle"}]
# Dictionary gắn type với ba công thức bậc hai tương ứng.
functions = {"minimum": x*x+2*y*y,
             "maximum": -x*x-2*y*y,
             "saddle": x*x-y*y}
results = []
# Duyệt từng mô hình và lấy đúng công thức qua khóa type.
for row in models:
    # sp.hessian() tính ma trận độ cong bậc hai của công thức đang xét.
    # Chuyển Hessian sang ndarray float cho eigvalsh.
    H = np.array(sp.hessian(functions[row["type"]],[x,y]), dtype=float)
    # eigvalsh() trả trị riêng của Hessian đối xứng; dấu trị riêng phân biệt các dạng cong.
    eig = np.linalg.eigvalsh(H)
    # Tất cả trị riêng dương nghĩa cực tiểu tại điểm dừng (Hessian dương xác định).
    if np.all(eig > 0):
        kind = "minimum"
    # Tất cả trị riêng âm nghĩa cực đại tại điểm dừng.
    elif np.all(eig < 0):
        kind = "maximum"
    else:
        # Với ba loại mô hình đã dựng, trường hợp còn lại có trị riêng trái dấu nên là yên ngựa; quy tắc else này không đủ phân loại Hessian có trị riêng bằng 0 nói chung.
        kind = "saddle"
    # append() lưu nhãn kết quả để đếm thống kê.
    results.append(kind)
# Kiểm đủ 18 mô hình trước khi báo cáo.
if len(models) != 18:
    # raise ValueError báo điều kiện số mẫu, shape hoặc phép đối chiếu thất bại.
    raise ValueError("Cần đủ 18 mô hình cực trị.")
print("Mô hình:", len(models))
# count() đếm số chuỗi 'minimum'; tương tự 'maximum','saddle' trong list nhãn.
print("Cực tiểu:", results.count("minimum"))
print("Cực đại:", results.count("maximum"))
print("Yên ngựa:", results.count("saddle"))
```

**Kết quả khi chạy:**

```text
Mô hình: 18
Cực tiểu: 6
Cực đại: 6
Yên ngựa: 6
```

Trị riêng bằng 0 sẽ khiến **phép thử Hessian cơ bản không đủ kết luận**; ba dạng hàm minh họa ở đây không có trị riêng bằng 0.

### Tình huống 5 — Cấp 5: Kiểm tra Jacobian suy biến qua 20 trạng thái của hệ hai đầu ra

**Từ vựng trong mục:** **Jacobian determinant** — định thức Jacobian; **Sensitivity** — độ nhạy; **Singular** — suy biến.

**Tình huống thực tế:** Một hệ thống điều khiển có **20 cấu hình C01–C20**, mỗi cấu hình ghi hai tín hiệu đầu vào x, y và cho ra **hai chỉ số** theo các quy tắc phi tuyến. Kỹ thuật viên muốn biết tại cấu hình nào các đầu ra **không đủ nhạy theo hai hướng độc lập**, khiến cách suy ngược những thay đổi nhỏ của đầu vào từ đầu ra không còn được bảo đảm. Cần liệt kê mã các cấu hình ấy và đếm số cấu hình còn kiểm tra được tính khả nghịch cục bộ.

**Vì sao chọn cách này?** **Jacobian** đo mối quan hệ giữa **thay đổi nhỏ ở hai đầu vào** và **thay đổi ở hai đầu ra** tại một cấu hình. Nếu hai hàng hoặc cột của Jacobian không độc lập, một số thay đổi đầu vào không thể phân biệt chỉ từ cách các đầu ra thay đổi rất nhỏ ở điểm ấy. Với bảng **2 × 2**, **định thức gần 0** báo Jacobian suy biến, nên điều kiện đủ quen thuộc để **bảo đảm có hàm ngược cục bộ** không còn thỏa. Chương trình thế từng cặp x, y vào Jacobian, tính `np.linalg.det`, dùng ngưỡng `1e-9` để xử lý sai số rồi ghi đúng mã C01… bị suy biến. Điều đó **không tự chứng minh** mọi cách khôi phục đầu vào đều bất khả thi ở mọi vùng lân cận; chỉ không được áp dụng bảo đảm thông thường tại các điểm ấy.

**Quy trình:**
1. Dùng SymPy tính Jacobian của hai hàm đầu ra.
2. Thay từng cặp trong 20 hàng, tính định thức bằng số.
3. In mã suy biến, số cấu hình còn khả nghịch cục bộ và Jacobian mẫu.

**No Note — Không chú thích**

```python
import numpy as np
import sympy as sp
x,y = sp.symbols("x y")
points = [[1,8],[2,2],[3,2],[4,2],[5,2],[1,3],[2,3],[3,36],[4,3],[5,3],[1,4],[2,4],[3,4],[4,4],[5,80],[1,5],[2,5],[3,5],[4,5],[5,5]]
F = sp.Matrix([x*x+y, x*y+3*y])
J = F.jacobian([x,y])
singular = []
for i,(px,py) in enumerate(points,1):
    matrix = np.array(J.subs({x:px,y:py}),dtype=float)
    if abs(np.linalg.det(matrix)) < 1e-9:
        singular.append(f"C{i:02d}")
if len(points) != 20:
    raise ValueError("Cần đủ 20 cấu hình Jacobian.")
print("Cấu hình:", len(points))
print("Suy biến:", ", ".join(singular))
print("Còn định thức khác 0:", len(points)-len(singular))
print("Kích thước Jacobian:", J.shape)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Kiểm 20 Jacobian hai biến để tìm cấu hình gần suy biến theo định thức.
# Dữ liệu: 20 điểm (x,y), F=(x²+y,xy+3y); ngưỡng |det(J)|<1e-9 là tiêu chí gần suy biến.
# NumPy linalg.det() tính định thức của Jacobian số tại từng cấu hình.
import numpy as np
# SymPy lập ma trận Jacobian ký hiệu từ hàm vector F.
import sympy as sp
# Hai đầu vào ký hiệu cho hàm F.
x,y = sp.symbols("x y")
# 20 cấu hình [x,y], mỗi cặp một trường hợp kiểm đạo hàm.
points = [[1,8],[2,2],[3,2],[4,2],[5,2],[1,3],[2,3],[3,36],[4,3],[5,3],[1,4],[2,4],[3,4],[4,4],[5,80],[1,5],[2,5],[3,5],[4,5],[5,5]]
# Hai đầu ra phi tuyến làm mỗi hàng Jacobian tương ứng một hàm.
F = sp.Matrix([x*x+y, x*y+3*y])
# jacobian() tạo ma trận đạo hàm riêng 2×2 theo thứ tự biến [x,y].
J = F.jacobian([x,y])
# List lưu mã cấu hình có định thức gần 0.
singular = []
# enumerate(...,1) cung cấp số thứ tự 1..20 cho mã C01..C20; cặp (px,py) là tọa độ.
for i,(px,py) in enumerate(points,1):
    # subs() thế tọa độ cụ thể vào các đạo hàm ký hiệu.
    # Đổi Jacobian tại điểm thành ndarray số thực float trước khi lấy det().
    matrix = np.array(J.subs({x:px,y:py}),dtype=float)
    # det() lấy định thức Jacobian 2×2; bằng 0 là suy biến, không có nghịch đảo cục bộ.
    # abs() bỏ dấu định thức, so ngưỡng gần 0 để tránh sai số floating-point; ngưỡng này tùy thang dữ liệu.
    if abs(np.linalg.det(matrix)) < 1e-9:
        # f-string :02d tạo mã cấu hình hai chữ số.
        # append() lưu mã của cấu hình gần suy biến.
        singular.append(f"C{i:02d}")
# Kiểm đủ 20 cấu hình đầu vào.
if len(points) != 20:
    # raise ValueError báo điều kiện số mẫu, shape hoặc phép đối chiếu thất bại.
    raise ValueError("Cần đủ 20 cấu hình Jacobian.")
print("Cấu hình:", len(points))
print("Suy biến:", ", ".join(singular))
# Số cấu hình không bị đánh dấu = tổng 20 trừ số gần suy biến.
print("Còn định thức khác 0:", len(points)-len(singular))
# shape (2,2) là số đầu ra × số đầu vào, không phải 20 điểm.
print("Kích thước Jacobian:", J.shape)
```

**Kết quả khi chạy:**

```text
Cấu hình: 20
Suy biến: C01, C08, C15
Còn định thức khác 0: 17
Kích thước Jacobian: (2, 2)
```

Tập mã suy biến được suy từ **Jacobian tại từng điểm**, không phải từ việc x/y có giá trị lớn hay nhỏ.

## 6. Sai lầm thường gặp

- Jacobian có số hàng bằng số đầu ra và số cột bằng số đầu vào; không luôn là ma trận vuông.
- Hessian dùng cho hàm vô hướng đủ khả vi hai lần; hàng/cột là các tham số, không phải hai đầu ra.
- Gradient bằng 0 mới chỉ chỉ ra điểm dừng, chưa đủ nói là cực tiểu.
- Hessian có trị riêng vừa âm vừa dương ở điểm dừng chỉ ra yên ngựa; nếu có trị riêng 0, bài kiểm bậc hai đơn giản chưa đủ.
- Khi dùng `eigvalsh`, ma trận đầu vào phải đối xứng theo phép toán đang xét.
- SymPy là thư viện ngoài; các ví dụ ký hiệu cần cài đặt.

## 7. Trắc nghiệm

**Q1. What does a Jacobian contain? | Jacobian chứa gì?**

A. A differentiable point where the gradient is zero | Điểm khả vi có gradient bằng 0

B. Classifying local behavior near stationary points | Phân loại hành vi cục bộ gần điểm dừng

C. First partial derivatives of vector outputs | Các đạo hàm riêng bậc một của đầu ra vector

D. Second partial derivatives of a scalar output | Các đạo hàm riêng bậc hai của đầu ra vô hướng

**Đáp án: C**

**Giải thích:** Mỗi hàng chứa đạo hàm bậc một của một đầu ra.


**Q2. What does a Hessian contain? | Hessian chứa gì?**

A. Classifying local behavior near stationary points | Phân loại hành vi cục bộ gần điểm dừng

B. First partial derivatives of vector outputs | Các đạo hàm riêng bậc một của đầu ra vector

C. Second partial derivatives of a scalar output | Các đạo hàm riêng bậc hai của đầu ra vô hướng

D. A differentiable point where the gradient is zero | Điểm khả vi có gradient bằng 0

**Đáp án: C**

**Giải thích:** Hessian lấy đạo hàm tiếp của gradient.


**Q3. What is a stationary point? | Điểm dừng là gì?**

A. Classifying local behavior near stationary points | Phân loại hành vi cục bộ gần điểm dừng

B. First partial derivatives of vector outputs | Các đạo hàm riêng bậc một của đầu ra vector

C. Second partial derivatives of a scalar output | Các đạo hàm riêng bậc hai của đầu ra vô hướng

D. A differentiable point where the gradient is zero | Điểm khả vi có gradient bằng 0

**Đáp án: D**

**Giải thích:** Điểm dừng có các đạo hàm riêng bậc một bằng 0.


**Q4. What is curvature information used for? | Thông tin độ cong dùng để làm gì?**

A. Second partial derivatives of a scalar output | Các đạo hàm riêng bậc hai của đầu ra vô hướng

B. A differentiable point where the gradient is zero | Điểm khả vi có gradient bằng 0

C. Classifying local behavior near stationary points | Phân loại hành vi cục bộ gần điểm dừng

D. First partial derivatives of vector outputs | Các đạo hàm riêng bậc một của đầu ra vector

**Đáp án: C**

**Giải thích:** Độ cong giúp phân loại điểm dừng.


**Q5. For f(x, y) = x² + y², what is its Hessian matrix? | Với f(x, y) = x² + y², ma trận Hessian bằng bao nhiêu?**

A. [[1, 0], [0, 1]] | [[1, 0], [0, 1]]

B. [[0, 0], [0, 0]] | [[0, 0], [0, 0]]

C. [[2, 0], [0, 2]] | [[2, 0], [0, 2]]

D. [[0, 2], [2, 0]] | [[0, 2], [2, 0]]

**Đáp án: C**

**Giải thích:** Đạo hàm bậc hai theo x và y đều bằng 2, hai đạo hàm chéo bằng 0.


**Q6. At which x is the derivative of f(x) = (x − 3)² zero? | Đạo hàm của f(x) = (x − 3)² bằng 0 tại x nào?**

A. x = 2 | x = 2

B. x = −3 | x = −3

C. x = 3 | x = 3

D. x = 0 | x = 0

**Đáp án: C**

**Giải thích:** f'(x) = 2(x − 3); đặt bằng 0 được x = 3.


**Q7. At a stationary point, a positive-definite Hessian indicates what? | Tại một điểm dừng, Hessian xác định dương cho biết điều gì?**

A. Always a global maximum | Luôn là cực đại toàn cục

B. A strict local minimum | Một cực tiểu địa phương nghiêm ngặt

C. A strict local maximum | Một cực đại địa phương nghiêm ngặt

D. A saddle point | Một điểm yên ngựa

**Đáp án: B**

**Giải thích:** Hessian xác định dương nghĩa là hàm cong lên theo mọi hướng ở điểm dừng; trong điều kiện trơn phù hợp, đó là cực tiểu địa phương nghiêm ngặt.


**Q8. For f(x, y) = x² − y², how is the stationary point (0, 0) classified? | Với f(x, y) = x² − y², điểm dừng (0, 0) thuộc loại nào?**

A. Neither stationary nor extremum | Không phải điểm dừng hay cực trị

B. Strict local minimum | Cực tiểu địa phương nghiêm ngặt

C. Saddle point | Điểm yên ngựa

D. Strict local maximum | Cực đại địa phương nghiêm ngặt

**Đáp án: C**

**Giải thích:** Theo trục x, f tăng khỏi 0; theo trục y, f giảm khỏi 0. Vì vậy (0, 0) là điểm yên ngựa.


**Q9. What is Hessian of x²+y²? | Hessian của x²+y² là gì?**

A. `[[2,0],[0,-2]]` | `[[2,0],[0,-2]]`

B. `[[1,1],[y,x]]` | `[[1,1],[y,x]]`

C. `[[2,0],[0,2]]` | `[[2,0],[0,2]]`

D. `(3,2)` | `(3,2)`

**Đáp án: C**

**Giải thích:** Đạo hàm bậc hai của mỗi hạng bình phương bằng 2.


**Q10. What is Hessian of x²−y²? | Hessian của x²−y² là gì?**

A. `[[2,0],[0,-2]]` | `[[2,0],[0,-2]]`

B. `(3,2)` | `(3,2)`

C. `[[1,1],[y,x]]` | `[[1,1],[y,x]]`

D. `[[2,0],[0,2]]` | `[[2,0],[0,2]]`

**Đáp án: A**

**Giải thích:** Độ cong theo y bằng âm 2.


**Q11. What are stationary coordinates for (x−3)²+(y−2)²? | Tọa độ dừng của (x−3)²+(y−2)² là gì?**

A. `(3,2)` | `(3,2)`

B. `[[2,0],[0,2]]` | `[[2,0],[0,2]]`

C. `[[2,0],[0,-2]]` | `[[2,0],[0,-2]]`

D. `[[1,1],[y,x]]` | `[[1,1],[y,x]]`

**Đáp án: A**

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

B. A saddle point | Điểm yên ngựa

C. The simple second-derivative test is inconclusive | Phép kiểm đạo hàm bậc hai đơn giản chưa kết luận

D. A strict local maximum | Cực đại địa phương nghiêm ngặt

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

A. A saddle point | Điểm yên ngựa

B. A strict local maximum | Cực đại địa phương nghiêm ngặt

C. A strict local minimum | Cực tiểu địa phương nghiêm ngặt

D. The simple second-derivative test is inconclusive | Phép kiểm đạo hàm bậc hai đơn giản chưa kết luận

**Đáp án: A**

**Giải thích:** Một số hướng tăng và hướng khác giảm.


**Q16. What if a Hessian has a zero eigenvalue at a stationary point? | Nếu Hessian có trị riêng 0 tại điểm dừng thì sao?**

A. A saddle point | Điểm yên ngựa

B. The simple second-derivative test is inconclusive | Phép kiểm đạo hàm bậc hai đơn giản chưa kết luận

C. A strict local maximum | Cực đại địa phương nghiêm ngặt

D. A strict local minimum | Cực tiểu địa phương nghiêm ngặt

**Đáp án: B**

**Giải thích:** Trị riêng 0 cần kiểm tra sâu hơn.


**Q17. What is Hessian shape for a scalar function of three inputs? | Hessian hàm vô hướng ba biến có shape nào?**

A. Sensitivities of one output to each input | Độ nhạy của một đầu ra theo từng đầu vào

B. How each output responds to one input | Các đầu ra đáp ứng với một đầu vào

C. `(3,3)` | `(3,3)`

D. It can also occur at a maximum or saddle | Nó còn xuất hiện ở cực đại hoặc yên ngựa

**Đáp án: C**

**Giải thích:** Các đạo hàm riêng bậc hai ghép từng biến với biến khác.


**Q18. What does one Jacobian row represent? | Một hàng Jacobian biểu thị gì?**

A. How each output responds to one input | Các đầu ra đáp ứng với một đầu vào

B. It can also occur at a maximum or saddle | Nó còn xuất hiện ở cực đại hoặc yên ngựa

C. `(3,3)` | `(3,3)`

D. Sensitivities of one output to each input | Độ nhạy của một đầu ra theo từng đầu vào

**Đáp án: D**

**Giải thích:** Hàng cố định đầu ra, cột đổi đầu vào.


**Q19. What does one Jacobian column represent? | Một cột Jacobian biểu thị gì?**

A. Sensitivities of one output to each input | Độ nhạy của một đầu ra theo từng đầu vào

B. It can also occur at a maximum or saddle | Nó còn xuất hiện ở cực đại hoặc yên ngựa

C. `(3,3)` | `(3,3)`

D. How each output responds to one input | Các đầu ra đáp ứng với một đầu vào

**Đáp án: D**

**Giải thích:** Cột cố định một đầu vào qua mọi đầu ra.


**Q20. Why isn't zero gradient alone sufficient to prove a minimum? | Vì sao gradient 0 chưa đủ chứng minh cực tiểu?**

A. Sensitivities of one output to each input | Độ nhạy của một đầu ra theo từng đầu vào

B. `(3,3)` | `(3,3)`

C. It can also occur at a maximum or saddle | Nó còn xuất hiện ở cực đại hoặc yên ngựa

D. How each output responds to one input | Các đầu ra đáp ứng với một đầu vào

**Đáp án: C**

**Giải thích:** Cực đại và yên ngựa cũng có thể có gradient 0.

## 8. Liên hệ bài tiếp theo

`Gradient → Jacobian → Hessian → Tối ưu mô hình`.
