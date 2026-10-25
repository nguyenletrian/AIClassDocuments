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

## 5. Năm tình huống Jacobian/Hessian — từ độ nhạy đến suy biến cục bộ

### Tình huống 1 — Cấp 1: Jacobian của hai đầu ra trên 10 cặp tín hiệu

**Từ vựng trong mục:** **Jacobian** — ma trận độ nhạy; **Partial derivative** — đạo hàm riêng.

**Tình huống thực tế:** Trạm đo có **10 cặp đầu vào x và y không đơn vị**; mỗi hàng đại diện một lượt đo, chẳng hạn lượt đầu x = 2, y = 3. Phần mềm tạo **hai chỉ số đầu ra**: một chỉ số cộng x với y, chỉ số kia nhân x với y. Kỹ thuật viên muốn biết khi **chỉ x hoặc chỉ y thay đổi rất ít**, hai kết quả nhạy đến đâu tại **lượt đầu**, để tránh nhầm đầu ra nào bị ảnh hưởng bởi biến nào.

**Vì sao chọn cách này?** **Jacobian** là một **bảng độ nhạy**: mỗi **hàng ứng với một chỉ số đầu ra**, mỗi **cột ứng với một biến đầu vào**. Một ô cho biết đầu ra ở hàng ấy thay đổi nhanh cỡ nào nếu tăng rất ít biến ở cột ấy, giữ biến kia cố định. `outputs.jacobian([x, y])` tạo bảng **2 × 2** từ hai quy tắc, rồi `subs` đưa x = 2 và y = 3 của lượt đầu vào để xem các độ nhạy tại đúng hoàn cảnh đó. Đây **không phải bảng 10 lượt đo**; 10 là số dữ liệu đã lấy, còn kích thước Jacobian được quyết định bởi số đầu ra và số đầu vào.

**Quy trình:**
1. Tạo 10 cặp x/y rồi định nghĩa hai đầu ra bằng SymPy.
2. Gọi `jacobian([x,y])` cho hàm vector.
3. Thay cặp đầu tiên vào Jacobian và in ma trận 2×2.

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
