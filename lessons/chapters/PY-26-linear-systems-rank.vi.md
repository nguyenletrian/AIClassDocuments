# PY-26 — Hệ phương trình tuyến tính, rank và nghiệm


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Linear system** — hệ tuyến tính; **Rank** — hạng ma trận.

`Ma trận → Rank/Solve → Regression → AI`

**Học xong dùng để làm gì?** Kiểm tra hệ ràng buộc có đủ thông tin để giải hay có phương trình trùng, thiếu hoặc mâu thuẫn.

**Kết nối kiến thức tiếp theo:** PY-27 xác định hướng đặc biệt của phép biến đổi ma trận qua trị riêng/vector riêng.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích |
|---|---|---|
| Linear system | hệ tuyến tính | Nhiều phương trình chứa cùng các ẩn số |
| Rank | hạng ma trận | Số hàng/cột độc lập tuyến tính |
| Coefficient matrix | ma trận hệ số | Các hệ số của ẩn trong Ax=b |
| Residual | sai số dư | Độ sai khác giữa dự đoán Ax và b |

## 3. NumPy và các hàm liên quan

**Từ vựng trong mục:** **Function** — hàm; **Shape** — kích thước mảng.

| Hàm / tham số | Dùng làm gì |
|---|---|
| `np.linalg.solve(A,b)` | Giải Ax=b khi ma trận A vuông không suy biến |
| `np.linalg.matrix_rank(A)` | Kiểm tra số chiều độc lập tuyến tính |
| `np.column_stack((A,b))` | Ghép ma trận hệ số và vế phải thành augmented matrix |
| `np.linalg.lstsq(A,b,rcond=None)` | Tìm nghiệm bình phương tối thiểu khi quá nhiều phương trình |

## 4. Khái niệm liên quan

**Nội dung chính:** một hệ tuyến tính liên kết nhiều phương trình qua cùng các ẩn. Ta xác định đúng **hàng = phương trình**, **cột = ẩn**, **vế phải = giá trị đã biết**, sau đó kiểm tra tính độc lập và độ khớp của nghiệm.

### 4.1. Linear system — Một hệ phương trình chung các ẩn

**Từ vựng trong mục:** **Linear system** — hệ tuyến tính; **Equation** — phương trình.

Hệ tuyến tính là **nhiều phương trình cùng chứa các ẩn cần tìm**. Cửa hàng bán loại A giá `x` và loại B giá `y` (đơn vị nghìn đồng): mua một A và một B hết 5; mua hai A và một B hết 8. Ta có `x+y=5` và `2x+y=8`. Để viết `Ax=b`, mỗi **hàng của A là một phương trình**, mỗi **cột là hệ số của một ẩn**, `b` chứa tổng tiền từng hóa đơn. Giải hệ tìm được x=3, y=2.

**No Note — Không chú thích**

```python
import numpy as np

A = np.array([[1, 1], [2, 1]], dtype=float)
b = np.array([5, 8], dtype=float)
print(np.linalg.solve(A, b))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Giải hệ hai phương trình tuyến tính để tìm hai ẩn từ bảng hệ số và vế phải.
# Dữ liệu: A có hai hàng phương trình và hai cột ẩn; b=[5,8] là kết quả từng phương trình.
# NumPy cung cấp ndarray và np.linalg.solve() để giải hệ tuyến tính.
import numpy as np

# A là ma trận hệ số 2×2; dtype=float ép hệ số sang số thực cho phép giải có phần lẻ.
A = np.array([[1, 1], [2, 1]], dtype=float)
# b là vector vế phải dài 2, mỗi ô ứng với một hàng của A.
b = np.array([5, 8], dtype=float)
# solve(A,b) tìm vector x thỏa A@x=b bằng thuật toán giải hệ, không phải nhân nghịch đảo thủ công; yêu cầu A vuông không suy biến.
print(np.linalg.solve(A, b))
```

**Kết quả khi chạy:**

```text
[3. 2.]
```

Loại A giá 3 nghìn và loại B giá 2 nghìn đồng; nghiệm đồng thời thỏa hai hóa đơn.

### 4.2. Rank — Số thông tin độc lập

**Từ vựng trong mục:** **Rank** — hạng; **Linear dependence** — phụ thuộc tuyến tính.

**Rank** cho biết có bao nhiêu hàng/cột độc lập tuyến tính trong một ma trận. Ví dụ hai hàng `[1,2]` và `[2,4]`: hàng sau chỉ bằng hai lần hàng đầu nên không đưa thêm thông tin độc lập. Rank bằng 1 dù bảng có hai hàng và hai cột. Với một hệ 2 ẩn, nếu rank(A)=2 và A vuông thì nghiệm duy nhất khi hệ có vế phải b phù hợp (ở đây ma trận khả nghịch); nếu rank thấp cần kiểm tra cả ma trận mở rộng để biết vô nghiệm hay vô số nghiệm.

**No Note — Không chú thích**

```python
import numpy as np

A = np.array([[1, 2], [2, 4]])
print(np.linalg.matrix_rank(A))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Đo hạng ma trận để biết có bao nhiêu hàng/cột mang thông tin độc lập.
# Dữ liệu: Ma trận 2×2, hàng thứ hai gấp đôi hàng thứ nhất, nên chỉ có một hướng thông tin độc lập.
# NumPy linalg có phương thức xác định hạng ma trận.
import numpy as np

# Hai hàng [1,2] và [2,4] phụ thuộc tuyến tính vì một hàng là hai lần hàng kia.
A = np.array([[1, 2], [2, 4]])
# matrix_rank() dùng phân rã số học để đếm số hướng độc lập của ma trận; trả 1, KHÔNG phải số hàng hay số cột.
print(np.linalg.matrix_rank(A))
```

**Kết quả khi chạy:**

```text
1
```

Hai hàng phụ thuộc nhau nên số chiều thông tin độc lập chỉ là một.

### 4.3. Coefficient matrix — Bảng hệ số và vế phải

**Từ vựng trong mục:** **Coefficient matrix** — ma trận hệ số; **Augmented matrix** — ma trận mở rộng.

Trong `Ax=b`, **A chỉ chứa hệ số của các ẩn**, còn b chứa **giá trị đích của từng phương trình**. Ví dụ hệ `x+y=5`, `2x+y=8` có A hai hàng × hai cột, b dài hai phần tử. Ghép b thành một cột cuối bằng `np.column_stack((A,b))` cho ma trận mở rộng 2×3. Cột cuối này **không phải một ẩn mới**. Khi giải, số hàng A phải bằng số phần tử b.

**No Note — Không chú thích**

```python
import numpy as np

A = np.array([[1, 1], [2, 1]])
b = np.array([5, 8])
print(np.column_stack((A, b)))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Ghép ma trận hệ số A với cột vế phải b thành ma trận mở rộng.
# Dữ liệu: A có 2 phương trình × 2 ẩn; b=[5,8] là cột kết quả tương ứng.
# NumPy column_stack ghép các cột theo chiều ngang.
import numpy as np

# A chứa hai cột hệ số ứng với hai ẩn cho từng phương trình.
A = np.array([[1, 1], [2, 1]])
# b là vector vế phải có đúng hai giá trị theo hai hàng A.
b = np.array([5, 8])
# column_stack((A,b)) ghép b thành CỘT thứ ba, trả ma trận mở rộng 2×3; các hàng phải cùng số lượng.
print(np.column_stack((A, b)))
```

**Kết quả khi chạy:**

```text
[[1 1 5]
 [2 1 8]]
```

Hai cột đầu là hệ số của x, y; cột cuối là tổng tiền hóa đơn.

### 4.4. Residual — Sai lệch và nghiệm bình phương tối thiểu

**Từ vựng trong mục:** **Residual** — sai số dư; **Least squares** — bình phương tối thiểu.

Khi thử nghiệm x cho hệ `Ax=b`, **sai số dư** `r=Ax-b` đo mỗi phương trình lệch bao nhiêu so với vế phải. Nếu `r=0` thì nghiệm thỏa chính xác; dữ liệu đo thực tế thường có nhiễu nên không tìm được nghiệm thỏa mọi hàng. Khi số phương trình nhiều hơn số ẩn, `np.linalg.lstsq` tìm x làm **tổng bình phương các sai số dư nhỏ nhất**. Ví dụ ba số đo có x=1,2,3 và giá trị y=2,4,6.1; fit đường `y=m*x+c` không khớp hoàn toàn và cho gần `m=2.05`, `c=-0.067`.

**No Note — Không chú thích**

```python
import numpy as np

x = np.array([1, 2, 3])
y = np.array([2, 4, 6.1])
A = np.column_stack((x, np.ones_like(x)))
coeff = np.linalg.lstsq(A, y, rcond=None)[0]
print(np.round(coeff, 3))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tìm đường thẳng gần ba điểm nhất bằng nghiệm bình phương tối thiểu.
# Dữ liệu: Ba điểm (x,y) = (1,2), (2,4), (3,6.1); muốn ước lượng độ dốc và hệ số chặn.
# NumPy hỗ trợ tạo ma trận thiết kế và hồi quy bình phương tối thiểu.
import numpy as np

# x là ba giá trị đầu vào (tọa độ ngang), mỗi giá trị thuộc cùng lượt với y.
x = np.array([1, 2, 3])
# y chứa ba kết quả thực đo, có nhiễu 6.1 khiến ba phương trình không khớp tuyệt đối.
y = np.array([2, 4, 6.1])
# ones_like(x) tạo vector ba số 1 cùng shape, đại diện hệ số chặn của đường thẳng.
# Ghép cột x và cột 1 thành A shape (3,2), phù hợp mô hình y≈slope*x+intercept.
A = np.column_stack((x, np.ones_like(x)))
# lstsq giải nghiệm làm TỔNG BÌNH PHƯƠNG sai lệch nhỏ nhất khi dữ liệu nhiễu; rcond=None dùng ngưỡng mặc định NumPy để quyết định hạng.
# [0] lấy vector HỆ SỐ đầu tiên của tuple lstsq trả về, không phải điểm dữ liệu đầu tiên.
coeff = np.linalg.lstsq(A, y, rcond=None)[0]
# np.round(...,3) chỉ làm tròn hệ số khi hiển thị ba chữ số thập phân, không làm thay đổi fit ban đầu.
print(np.round(coeff, 3))
```

**Kết quả khi chạy:**

```text
[ 2.05  -0.067]
```

Hệ số góc xấp xỉ 2,05 và hệ số chặn xấp xỉ −0,067; đây là nghiệm xấp xỉ do số đo có nhiễu.

## 5. Năm tình huống hệ tuyến tính — từ giải đúng đến xấp xỉ với dữ liệu nhiễu

### Tình huống 1 — Cấp 1: Giải giá hai mặt hàng từ 10 hóa đơn

**Từ vựng trong mục:** **Linear system** — hệ tuyến tính; **solve** — giải nghiệm; **Residual** — sai lệch.

**Tình huống thực tế:** Một cửa hàng ghi **10 hóa đơn** bán hai loại hàng A và B. Trên mỗi hóa đơn có **số món A**, **số món B** và **tổng tiền**, đơn vị **nghìn đồng**; ví dụ hóa đơn đầu có mỗi loại một món, tổng 5 nghìn đồng, hóa đơn thứ hai có hai món A và một món B, tổng 8 nghìn đồng. Giá một món của mỗi loại chưa biết nhưng giữ nguyên trong cả 10 hóa đơn. Thu ngân muốn tìm giá từng loại rồi kiểm lại **tất cả hóa đơn** để bảo đảm giá ấy giải thích đúng số tiền.

**Vì sao chọn cách này?** **Hệ phương trình** ở đây là hai hóa đơn chứa hai mức giá chưa biết; với ví dụ đầu tiên, cộng giá một món A và một món B được 5 nghìn đồng, còn hóa đơn thứ hai có thêm một món A nên tổng là 8 nghìn đồng. Hai cách phối số lượng khác nhau cho đủ thông tin tìm riêng từng giá. `np.linalg.solve()` giải **hai phương trình đầu** để tìm hai giá, nhưng một nghiệm khớp hai dòng chưa chắc đúng cả sổ. Vì vậy `quantities @ prices` tính lại tiền của **cả 10 hóa đơn** rồi lấy chênh lệch với tiền thực; sai số rất nhỏ được bỏ qua bằng ngưỡng tính toán. Không nên kết luận mọi dòng đúng chỉ vì giải được hai dòng mẫu.

**Quy trình:**
1. Tạo bảng 10 hàng số lượng và 10 tổng tiền cùng thứ tự.
2. Chọn hai hàng độc lập đầu để giải hệ 2 ẩn.
3. Dự tính tổng tiền cả 10 hàng rồi đếm sai lệch lớn hơn ngưỡng nhỏ.

**No Note — Không chú thích**

```python
import numpy as np
quantities = np.array([[1,1],[2,1],[3,1],[4,1],[1,2],[2,2],[3,2],[4,2],[1,3],[2,3]], dtype=float)
totals = np.array([5,8,11,14,7,10,13,16,9,12], dtype=float)
prices = np.linalg.solve(quantities[:2], totals[:2])
residual = quantities @ prices - totals
if quantities.shape != (10, 2):
    raise ValueError("Cần đủ 10 hóa đơn và hai số lượng.")
print("Hóa đơn:", len(totals))
print("Giá A (nghìn đồng):", f"{prices[0]:.1f}")
print("Giá B (nghìn đồng):", f"{prices[1]:.1f}")
print("Hóa đơn sai:", int((np.abs(residual) > 1e-8).sum()))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Giải hai giá sản phẩm từ 10 hóa đơn và dùng phần dư kiểm toàn bộ hóa đơn.
# Dữ liệu: 10 hàng hóa đơn, hai cột số lượng món A/B; totals là tổng tiền nghìn đồng từng hóa đơn.
# NumPy giải hệ hai ẩn và tính phần dư cho nhiều hóa đơn.
import numpy as np
# Ma trận (10,2); mỗi hàng là số lượng sản phẩm A, B, dtype=float phục vụ giải.
quantities = np.array([[1,1],[2,1],[3,1],[4,1],[1,2],[2,2],[3,2],[4,2],[1,3],[2,3]], dtype=float)
# Vector 10 tổng tiền (nghìn đồng) cùng thứ tự hàng quantities.
totals = np.array([5,8,11,14,7,10,13,16,9,12], dtype=float)
# [:2] lấy HAI hóa đơn đầu (vị trí 0 và 1), làm hệ 2×2 đủ để tìm hai giá.
# [:2] lấy vế phải tương ứng với hai hóa đơn đã chọn.
# solve() tìm hai đơn giá nghìn đồng sao cho hai hóa đơn đầu khớp chính xác; cần ma trận con khả nghịch.
prices = np.linalg.solve(quantities[:2], totals[:2])
# @ nhân mỗi hàng số lượng với vector giá, trả tổng tiền dự đoán từng hóa đơn.
# Trừ totals để có phần dư dự đoán trừ thực tế từng hóa đơn (nghìn đồng).
residual = quantities @ prices - totals
# shape (10,2) bảo đảm đủ 10 hóa đơn và 2 mặt hàng.
if quantities.shape != (10, 2):
    # raise ValueError() dừng nếu không đủ hàng/cột hoặc điều kiện dữ liệu kiểm thử sai.
    raise ValueError("Cần đủ 10 hóa đơn và hai số lượng.")
print("Hóa đơn:", len(totals))
# [0] là giá A, [1] giá B; :.1f chỉ định in một chữ số thập phân.
print("Giá A (nghìn đồng):", f"{prices[0]:.1f}")
print("Giá B (nghìn đồng):", f"{prices[1]:.1f}")
# abs() lấy độ lớn phần dư; ngưỡng 1e-8 nghìn đồng loại sai số số thực cực nhỏ, .sum() đếm hóa đơn vượt ngưỡng.
print("Hóa đơn sai:", int((np.abs(residual) > 1e-8).sum()))
```

**Kết quả khi chạy:**

```text
Hóa đơn: 10
Giá A (nghìn đồng): 3.0
Giá B (nghìn đồng): 2.0
Hóa đơn sai: 0
```

Đơn giá là **nghìn đồng/món**, còn tổng tiền là nghìn đồng; nghiệm chỉ có ý nghĩa vì hai phương trình đầu độc lập.

### Tình huống 2 — Cấp 2: Nhận biết hai cột phụ thuộc trong 12 lượt vận hành

**Từ vựng trong mục:** **Rank** — hạng ma trận; **Linear dependence** — phụ thuộc tuyến tính.

**Tình huống thực tế:** Trạm máy theo dõi **12 lượt vận hành**, mỗi lượt ghi số **giờ chạy máy x** và một cột báo cáo được tạo bằng **hai lần số giờ x**. Người quản lý định dùng hai cột để dự đoán, nhưng lo rằng cột thứ hai không bổ sung thông tin mới. Họ cần biết bảng có thực sự **hai nguồn số liệu độc lập** hay chỉ một nguồn được ghi lại theo cách khác.

**Vì sao chọn cách này?** **Hạng ma trận (rank)** là số hướng thông tin **độc lập về mặt tuyến tính**. Hãy hình dung biết cột giờ chạy là 5 giờ thì cột kia chắc chắn là 10; nó không kể thêm một điều gì chưa biết. `np.column_stack()` ghép hai cột thành bảng 12 hàng; `np.linalg.matrix_rank(X)` kiểm tra số cột thực sự độc lập. Kết quả hạng **1** nghĩa là hai cột chỉ tạo **một hướng thông tin**. Đây là phụ thuộc tuyến tính giữa các cột, không có nghĩa 12 lượt vận hành chỉ còn một lượt hoặc số giờ chạy là sai.

**Quy trình:**
1. Lưu 12 cặp số giờ, cột hai bằng hai lần cột một.
2. Gọi `matrix_rank` để kiểm số chiều độc lập.
3. Kiểm tra hai cột phụ thuộc và in kích thước/hạng.

**No Note — Không chú thích**

```python
import numpy as np
hours = np.array([1,2,3,4,5,6,7,8,9,10,11,12], dtype=float)
X = np.column_stack((hours, 2 * hours))
if X.shape != (12, 2):
    raise ValueError("Cần đủ 12 lượt vận hành với hai cột.")
print("Lượt vận hành:", X.shape[0])
print("Cột:", X.shape[1])
print("Hạng:", int(np.linalg.matrix_rank(X)))
print("Cột 2 = 2 × cột 1:", bool(np.allclose(X[:, 1], 2 * X[:, 0])))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Phát hiện hai cột dữ liệu có quan hệ phụ thuộc bằng matrix_rank.
# Dữ liệu: 12 lượt vận hành theo giờ; cột thứ nhất giờ, cột thứ hai luôn đúng gấp đôi số giờ.
# NumPy tạo mảng và xác định số cột độc lập.
import numpy as np
# Vector 12 số giờ, dtype=float để dùng tính toán số học.
hours = np.array([1,2,3,4,5,6,7,8,9,10,11,12], dtype=float)
# column_stack ghép hai cột, cột thứ hai bằng 2×cột đầu nên không có thông tin độc lập bổ sung.
X = np.column_stack((hours, 2 * hours))
# shape (12,2) nghĩa 12 lượt quan sát và 2 cột dữ liệu.
if X.shape != (12, 2):
    # raise ValueError() dừng nếu không đủ hàng/cột hoặc điều kiện dữ liệu kiểm thử sai.
    raise ValueError("Cần đủ 12 lượt vận hành với hai cột.")
# shape (12,2) nghĩa 12 lượt quan sát và 2 cột dữ liệu.
# shape[0] đếm lượt/hàng, shape[1] đếm cột biến đo.
print("Lượt vận hành:", X.shape[0])
# shape (12,2) nghĩa 12 lượt quan sát và 2 cột dữ liệu.
print("Cột:", X.shape[1])
# matrix_rank() đếm số hướng độc lập, chỉ bằng 1 khi hai cột tỷ lệ cố định.
print("Hạng:", int(np.linalg.matrix_rank(X)))
# [:,1] lấy tất cả hàng của cột thứ hai, [:,0] lấy cột đầu.
# allclose() so từng giá trị với dung sai số thực, an toàn hơn == khi phép toán float.
# bool() biểu diễn kết quả kiểm NumPy dưới dạng True/False Python.
print("Cột 2 = 2 × cột 1:", bool(np.allclose(X[:, 1], 2 * X[:, 0])))
```

**Kết quả khi chạy:**

```text
Lượt vận hành: 12
Cột: 2
Hạng: 1
Cột 2 = 2 × cột 1: True
```

Hai cột không phải hai đặc trưng độc lập; rank bằng 1 dù ma trận có 12 hàng và 2 cột.

### Tình huống 3 — Cấp 3: Phục hồi 15 cặp tín hiệu từ hai kênh

**Từ vựng trong mục:** **Coefficient matrix** — ma trận hệ số; **Augmented data** — dữ liệu mở rộng; **solve** — giải hệ.

**Tình huống thực tế:** Một máy đo có **15 lượt ghi tín hiệu**; mỗi lượt cho hai số đo kênh A và B theo một quy tắc pha trộn cố định. A chứa **hai phần nguồn x và một phần nguồn y**; B chứa **một phần x và ba phần y**. Hai nguồn x, y chưa biết và có cùng đơn vị tín hiệu như số đo. Kỹ thuật viên cần khôi phục hai nguồn **cho từng lượt**, rồi thử pha lại để chắc chắn khớp cả 15 cặp số đã nhận.

**Vì sao chọn cách này?** **Ma trận hệ số** `A` ghi cách hai nguồn góp vào mỗi kênh. Ma trận này **giữ nguyên cho cả 15 lần đo** và có đủ thông tin để phân biệt nguồn x với y. `np.linalg.solve(A, measured.T)` giải nhiều cặp số đo trong **một lần gọi**; `.T` đổi từ dạng mỗi lượt một hàng sang cách hàm giải nhận các vế phải ở từng cột, rồi chuyển kết quả về mỗi lượt một hàng. Sau giải, `restored @ A.T` thử **pha ngược lại** hai nguồn vừa tìm; `np.allclose()` xác nhận số tái tạo gần bằng số đo gốc. Nếu chỉ đọc nghiệm mà không tái tạo, sai thứ tự kênh hoặc nhầm hệ số có thể không được phát hiện.

**Quy trình:**
1. Tạo ma trận hệ số và 15 cặp kênh được đo.
2. Chuyển vị số đo, đưa vào `np.linalg.solve` rồi chuyển vị kết quả.
3. Tái tạo hai kênh và kiểm tra mọi lượt.

**No Note — Không chú thích**

```python
import numpy as np
A = np.array([[2., 1.], [1., 3.]])
measured = np.array([[4,7],[6,8],[8,9],[10,10],[12,11],[5,10],[7,11],[9,12],[11,13],[13,14],[6,13],[8,14],[10,15],[12,16],[14,17]], dtype=float)
restored = np.linalg.solve(A, measured.T).T
if measured.shape != (15, 2) or restored.shape != (15, 2):
    raise ValueError("Cần đúng 15 lượt đo hai tín hiệu.")
print("Lượt đo:", len(restored))
print("Hạng hệ số:", int(np.linalg.matrix_rank(A)))
first_values = []
for value in restored[0]:
    first_values.append(f"{value:.1f}")
print("Tín hiệu gốc đầu:", ", ".join(first_values))
print("Tái tạo đúng:", bool(np.allclose(restored @ A.T, measured)))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Khôi phục 15 cặp tín hiệu gốc từ hỗn hợp đo bằng hệ tuyến tính hai chiều.
# Dữ liệu: 15 hàng số đo hỗn hợp, hai cột cảm biến, A là ma trận trộn 2×2 biết trước.
# NumPy giải hệ nhiều vế phải đồng thời bằng linalg.solve().
import numpy as np
# Ma trận hệ số trộn tín hiệu 2×2, float; hạng đủ 2 thì có nghiệm duy nhất.
A = np.array([[2., 1.], [1., 3.]])
# 15 hàng × 2 số đo thực tế, mỗi hàng là một lượt đo.
measured = np.array([[4,7],[6,8],[8,9],[10,10],[12,11],[5,10],[7,11],[9,12],[11,13],[13,14],[6,13],[8,14],[10,15],[12,16],[14,17]], dtype=float)
# Chuyển vị từ (15,2) thành (2,15) để mỗi lượt trở thành một cột vế phải.
# solve(A,B) giải 15 hệ cùng A; .T cuối đưa đáp số về 15 hàng × 2 cột gốc.
restored = np.linalg.solve(A, measured.T).T
# Đối chiếu cả nguồn và số liệu khôi phục có shape (15,2).
if measured.shape != (15, 2) or restored.shape != (15, 2):
    # raise ValueError() dừng nếu không đủ hàng/cột hoặc điều kiện dữ liệu kiểm thử sai.
    raise ValueError("Cần đúng 15 lượt đo hai tín hiệu.")
print("Lượt đo:", len(restored))
# matrix_rank(A) xác minh hệ số có 2 hướng độc lập, không phải 15 lượt đo.
print("Hạng hệ số:", int(np.linalg.matrix_rank(A)))
first_values = []
# [0] lấy hai tín hiệu khôi phục của lượt đo thứ nhất.
for value in restored[0]:
    # f-string :.1f hiển thị một chữ số thập phân cho từng tín hiệu.
    first_values.append(f"{value:.1f}")
# join() nối các giá trị đã định dạng bằng dấu phẩy và khoảng trắng.
print("Tín hiệu gốc đầu:", ", ".join(first_values))
# Vì mỗi tín hiệu khôi phục là vector HÀNG, @ A.T tái tạo đúng hỗn hợp; .T của A phù hợp quy ước solve theo cột.
# allclose() so mảng tái tạo với dữ liệu đo trong dung sai số thực; bool() để in Boolean Python.
print("Tái tạo đúng:", bool(np.allclose(restored @ A.T, measured)))
```

**Kết quả khi chạy:**

```text
Lượt đo: 15
Hạng hệ số: 2
Tín hiệu gốc đầu: 1.0, 2.0
Tái tạo đúng: True
```

Một cặp giá trị quan sát phải ứng với **cùng lượt**; không ghép kênh A của lượt này với B của lượt khác.

### Tình huống 4 — Cấp 4: Phát hiện 18 phương trình không nhất quán bằng hạng mở rộng

**Từ vựng trong mục:** **Augmented matrix** — ma trận mở rộng; **Inconsistent system** — hệ vô nghiệm; **Residual** — sai số dư.

**Tình huống thực tế:** Phòng hiệu chuẩn ghi **18 lượt dữ liệu**, mỗi lượt có thời gian máy hoạt động **x (giờ)** và mức tiêu thụ **y (đơn vị mô phỏng)**. Nhóm giả định tất cả số đo tuân theo **một đường thẳng chung**, tức tăng thêm một lượng cố định theo giờ. Tuy nhiên, ở lượt thứ 10, mức tiêu thụ bị ghi cao hơn dự kiến **7 đơn vị**. Kỹ thuật viên muốn biết liệu có thể tìm **một đường thẳng đi qua chính xác cả 18 điểm** không, trước khi chuyển sang cách tìm đường gần đúng.

**Vì sao chọn cách này?** **Hạng của hệ số** cho biết hai thành phần đường thẳng (mức tăng và mức nền) có độc lập không; **hạng ma trận mở rộng** còn tính cả cột số đo thực tế `y`. Nếu thêm cột `y` làm hạng tăng, nghĩa là các số đo **không thể đồng thời khớp hoàn toàn** cùng một quy tắc tuyến tính. Trong ví dụ, lượt 10 bị lệch 7 đơn vị nên hệ 18 dòng bị mâu thuẫn. `np.linalg.matrix_rank()` kiểm tra hai hạng trước khi tìm nghiệm. `np.linalg.solve()` không phù hợp cho bảng **18 hàng × 2 cột** vì đó không phải ma trận vuông 2×2; bài này chỉ kiểm tra **có thể khớp chính xác hay không**, chưa tìm đường gần đúng.

**Quy trình:**
1. Tạo bảng hệ số 18 hàng, hai cột x và cột 1; y là vế phải.
2. Ghép ma trận mở rộng bằng `column_stack`, tính hai hạng.
3. Báo kết luận có hay không nghiệm khớp mọi lượt.

**No Note — Không chú thích**

```python
import numpy as np
hours = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], dtype=float)
y = np.array([7,9,11,13,15,17,19,21,23,32,27,29,31,33,35,37,39,41], dtype=float)
A = np.column_stack((hours, np.ones_like(hours)))
augmented = np.column_stack((A, y))
rank_a = int(np.linalg.matrix_rank(A))
rank_aug = int(np.linalg.matrix_rank(augmented))
if A.shape != (18, 2) or augmented.shape != (18, 3):
    raise ValueError("Hệ có 18 phương trình, hai hệ số và một vế phải.")
print("Số phương trình:", len(y))
print("Hạng hệ số:", rank_a)
print("Hạng mở rộng:", rank_aug)
print("Khớp tất cả:", rank_a == rank_aug)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: So hạng hệ số và ma trận mở rộng để phát hiện 18 phương trình không khớp một đường thẳng duy nhất.
# Dữ liệu: 18 cặp (giờ,giá trị đo), đầu ra tại giờ 10 lệch khỏi xu thế chung.
# NumPy cho phép dựng ma trận mở rộng và so hạng tuyến tính.
import numpy as np
# 18 giá trị giờ làm biến đầu vào, dtype=float.
hours = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], dtype=float)
# 18 số đo cùng vị trí với giờ, có một điểm lệch khiến hệ thiếu nghiệm chính xác.
y = np.array([7,9,11,13,15,17,19,21,23,32,27,29,31,33,35,37,39,41], dtype=float)
# Tạo 18 số 1 cho hệ số chặn (intercept) trong mô hình y=slope*hours+intercept.
# A=(giờ,cột1) có shape (18,2), hai cột tương ứng hai hệ số chưa biết.
A = np.column_stack((hours, np.ones_like(hours)))
# Thêm y thành cột thứ ba cho ma trận mở rộng shape (18,3).
augmented = np.column_stack((A, y))
# Hạng A đếm số cột phương trình độc lập.
rank_a = int(np.linalg.matrix_rank(A))
# Hạng mở rộng đếm thêm ràng buộc của vế phải; lớn hơn hạng A nghĩa không có nghiệm khớp TẤT CẢ phương trình.
rank_aug = int(np.linalg.matrix_rank(augmented))
# Đối chiếu shape 18×2 và 18×3 trước báo cáo.
if A.shape != (18, 2) or augmented.shape != (18, 3):
    # raise ValueError() dừng nếu không đủ hàng/cột hoặc điều kiện dữ liệu kiểm thử sai.
    raise ValueError("Hệ có 18 phương trình, hai hệ số và một vế phải.")
print("Số phương trình:", len(y))
print("Hạng hệ số:", rank_a)
print("Hạng mở rộng:", rank_aug)
# So hạng là điều kiện tồn tại nghiệm chính xác; False ở dữ liệu có sai lệch.
print("Khớp tất cả:", rank_a == rank_aug)
```

**Kết quả khi chạy:**

```text
Số phương trình: 18
Hạng hệ số: 2
Hạng mở rộng: 3
Khớp tất cả: False
```

Điều này không chứng minh toàn bộ dữ liệu vô dụng; nó chỉ chứng minh không thể có **nghiệm chính xác chung** cho tất cả phương trình.

### Tình huống 5 — Cấp 5: Ước lượng tuyến tính từ 20 số đo nhiễu và kiểm tra sai số dư

**Từ vựng trong mục:** **Least squares** — bình phương tối thiểu; **Residual** — sai số dư; **Rank** — hạng.

**Tình huống thực tế:** Nhà máy đo **20 cặp số liệu** giờ chạy máy (**giờ**) và năng lượng dùng (**kWh**). Phần lớn dữ liệu tăng gần **4 kWh cho mỗi giờ thêm**, từ mức nền khoảng **10 kWh**, nhưng lượt 5 và 17 có sai lệch giả lập. Người phân tích cần tìm một đường thẳng **gần phù hợp nhất** với toàn bộ 20 lượt, báo mức tăng theo giờ, mức nền, sai số trung bình bình phương **MSE** và số lượt dự báo sai quá **5 kWh**.

**Vì sao chọn cách này?** **Bình phương tối thiểu** được dùng khi có nhiều số đo hơn số thông số cần tìm và các điểm **không nằm chính xác trên cùng một đường**. `np.linalg.lstsq()` chọn mức tăng theo giờ (**kWh/giờ**) và mức nền (**kWh**) sao cho tổng các **sai lệch đã bình phương** là nhỏ nhất; các sai lệch lớn bị phạt mạnh hơn. Sau đó chương trình dự đoán lại 20 lượt, tính **MSE** bằng trung bình bình phương sai lệch (đơn vị **kWh²**) và đếm lượt lệch quá 5 kWh. Đây là đường khớp **gần đúng**, không phải cách sửa số đo nhiễu thành sự thật; nếu cần giải thích sự cố ở lượt 5, 17 phải kiểm tra dữ liệu nguồn.

**Quy trình:**
1. Tạo A từ 20 cặp x/y với một cột x và một cột 1.
2. Fit bằng `lstsq` khi A có hạng 2.
3. Tính phần dư, MSE và số lượt có sai lệch lớn.

**No Note — Không chú thích**

```python
import numpy as np
hours = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], dtype=float)
energy = np.array([14,18,22,26,42,34,38,42,46,50,54,58,62,66,70,74,70,82,86,90], dtype=float)
A = np.column_stack((hours, np.ones_like(hours)))
slope, intercept = np.linalg.lstsq(A, energy, rcond=None)[0]
residual = A @ np.array([slope, intercept]) - energy
if A.shape != (20, 2) or np.linalg.matrix_rank(A) != 2:
    raise ValueError("Cần đủ 20 lượt đo và hai cột độc lập.")
print("Lượt đo:", len(energy))
print(f"Độ dốc (kWh/giờ): {slope:.2f}")
print(f"Nền (kWh): {intercept:.2f}")
print(f"MSE (kWh²): {np.mean(residual ** 2):.2f}")
print("Lệch > 5 kWh:", int((np.abs(residual) > 5).sum()))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Fit đường tuyến tính cho 20 lượt năng lượng bằng least squares và đếm số đo lệch quá 5 kWh.
# Dữ liệu: 20 cặp (giờ hoạt động,điện tiêu thụ kWh); một số lượt có nhiễu, ước lượng độ dốc kWh/giờ và nền kWh.
# NumPy cung cấp matrix_rank(), lstsq() và thống kê phần dư.
import numpy as np
# 20 giờ vận hành, dtype=float làm cột đặc trưng.
hours = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], dtype=float)
# 20 số điện kWh theo thứ tự giờ, có vài giá trị nhiễu so đường thẳng.
energy = np.array([14,18,22,26,42,34,38,42,46,50,54,58,62,66,70,74,70,82,86,90], dtype=float)
# Vector 20 số 1 tạo cột hệ số chặn (điện nền).
# Ghép giờ và hằng số 1 thành A shape (20,2) cho y≈slope*hours+intercept.
A = np.column_stack((hours, np.ones_like(hours)))
# lstsq tìm độ dốc và hệ số nền giảm tổng bình phương sai lệch; rcond=None dùng ngưỡng hạng mặc định; [0] lấy vector nghiệm.
# Giải cấu trúc hai giá trị: slope kWh mỗi giờ, intercept kWh nền khi giờ bằng 0.
slope, intercept = np.linalg.lstsq(A, energy, rcond=None)[0]
# @ tính lượng điện dự đoán từ hệ số fit cho từng giờ, một giá trị mỗi hàng.
# Trừ số thực đo để ra residual (kWh) theo từng lượt.
residual = A @ np.array([slope, intercept]) - energy
# shape (20,2) kiểm đúng số mẫu và hai hệ số.
# Đòi hai cột độc lập để xác định slope/intercept, tránh fit không xác định.
if A.shape != (20, 2) or np.linalg.matrix_rank(A) != 2:
    # raise ValueError() dừng nếu không đủ hàng/cột hoặc điều kiện dữ liệu kiểm thử sai.
    raise ValueError("Cần đủ 20 lượt đo và hai cột độc lập.")
print("Lượt đo:", len(energy))
print(f"Độ dốc (kWh/giờ): {slope:.2f}")
print(f"Nền (kWh): {intercept:.2f}")
# **2 bình phương mỗi phần dư kWh; np.mean() tính MSE có đơn vị kWh², nhấn mạnh phạt sai số lớn.
print(f"MSE (kWh²): {np.mean(residual ** 2):.2f}")
# abs() lấy độ lệch không dấu, >5 tạo mask, sum() đếm lượt lệch hơn 5 kWh.
print("Lệch > 5 kWh:", int((np.abs(residual) > 5).sum()))
```

**Kết quả khi chạy:**

```text
Lượt đo: 20
Độ dốc (kWh/giờ): 3.82
Nền (kWh): 12.06
MSE (kWh²): 9.31
Lệch > 5 kWh: 2
```

MSE bị ảnh hưởng bởi hai điểm nhiễu; không nên lấy đường fit này làm quy luật tiêu thụ chắc chắn của một thiết bị thật.

## 6. Sai lầm thường gặp

- Một hàng của A là một phương trình; một cột là hệ số của một ẩn. Không được đảo hai chiều khi đọc dữ liệu.
- b là giá trị đã biết ở vế phải, không phải cột hệ số của một ẩn mới.
- Hệ phụ thuộc hàng có thể vô nghiệm hoặc vô số nghiệm; xét cả rank(A) và rank([A, b]), không kết luận chỉ từ rank(A).
- `solve` dành cho ma trận vuông khả nghịch; `lstsq` giải gần đúng được cả hệ có nhiều số đo.
- Residual có dấu; bình phương tối thiểu tối ưu tổng **bình phương** dư chứ không tối ưu tổng dư có dấu.
- Chỉ dùng `np.allclose` để kiểm nghiệm trong sai số số học, không coi đó là bằng nhau tuyệt đối.

## 7. Trắc nghiệm

**Các câu hỏi chỉ kiểm tra khái niệm và cách áp dụng kiến thức, không yêu cầu nhớ tình huống thực hành.**

**Q1. What is a linear system? | Hệ tuyến tính là gì?**

A. Several linear equations sharing unknowns | Nhiều phương trình tuyến tính chung các ẩn

B. The number of linearly independent rows or columns | Số hàng hoặc cột độc lập tuyến tính

C. The coefficients multiplying the unknowns | Các hệ số nhân với từng ẩn

D. `A @ x - b` | `A @ x - b`

**Đáp án: A**

**Giải thích:** Các phương trình cùng chứa các ẩn cần giải.


**Q2. What does the rank of a matrix measure? | Rank của ma trận đo gì?**

A. Several linear equations sharing unknowns | Nhiều phương trình tuyến tính chung các ẩn

B. The number of linearly independent rows or columns | Số hàng hoặc cột độc lập tuyến tính

C. The coefficients multiplying the unknowns | Các hệ số nhân với từng ẩn

D. `A @ x - b` | `A @ x - b`

**Đáp án: B**

**Giải thích:** Rank đếm hướng độc lập, không chỉ số hàng.


**Q3. What does a coefficient matrix contain? | Ma trận hệ số chứa gì?**

A. Several linear equations sharing unknowns | Nhiều phương trình tuyến tính chung các ẩn

B. The number of linearly independent rows or columns | Số hàng hoặc cột độc lập tuyến tính

C. The coefficients multiplying the unknowns | Các hệ số nhân với từng ẩn

D. `A @ x - b` | `A @ x - b`

**Đáp án: C**

**Giải thích:** Ma trận chứa hệ số số học của từng ẩn.


**Q4. What is the residual vector for Ax=b? | Vector sai số dư của Ax=b là gì?**

A. Several linear equations sharing unknowns | Nhiều phương trình tuyến tính chung các ẩn

B. The number of linearly independent rows or columns | Số hàng hoặc cột độc lập tuyến tính

C. The coefficients multiplying the unknowns | Các hệ số nhân với từng ẩn

D. `A @ x - b` | `A @ x - b`

**Đáp án: D**

**Giải thích:** Lấy Ax trừ b cho độ lệch từng phương trình.


**Q5. Solve x + y = 7 and x − y = 3. What are x and y? | Giải hệ x + y = 7 và x − y = 3. Tìm x và y.**

A. x = 4, y = 3 | x = 4, y = 3

B. x = 2, y = 5 | x = 2, y = 5

C. x = 5, y = 2 | x = 5, y = 2

D. x = 7, y = 0 | x = 7, y = 0

**Đáp án: C**

**Giải thích:** Cộng hai phương trình: 2x = 10 nên x = 5; thay vào x + y = 7 được y = 2.


**Q6. What can be concluded about x + y = 3 and x + y = 5? | Hệ x + y = 3 và x + y = 5 có kết luận gì?**

A. A unique solution | Có nghiệm duy nhất

B. No solution | Vô nghiệm

C. Exactly two solutions | Có đúng hai nghiệm

D. The solution is (3, 5) | Nghiệm là (3, 5)

**Đáp án: B**

**Giải thích:** Cùng một tổng x + y không thể đồng thời bằng 3 và 5, nên hai phương trình mâu thuẫn.


**Q7. What is the determinant of [[1, 2], [2, 4]]? | Định thức của [[1, 2], [2, 4]] là bao nhiêu?**

A. 0 | 0

B. 2 | 2

C. 4 | 4

D. 8 | 8

**Đáp án: A**

**Giải thích:** 1 × 4 − 2 × 2 = 0; hàng thứ hai gấp đôi hàng thứ nhất, nên ma trận thiếu hạng.


**Q8. Does (x, y) = (2, 1) solve x + 2y = 4 and 3x + y = 7? | Cặp (x, y) = (2, 1) có giải đúng hệ x + 2y = 4 và 3x + y = 7 không?**

A. No, the first equation fails | Không, phương trình đầu sai

B. No, the second equation fails | Không, phương trình sau sai

C. No, both equations fail | Không, cả hai đều sai

D. Yes, both equations hold | Có, cả hai đều đúng

**Đáp án: D**

**Giải thích:** Thế x = 2, y = 1: 2 + 2 × 1 = 4 và 3 × 2 + 1 = 7, nên đây là một nghiệm.


**Q9. For Ax=b with A shape (3,2), what do the rows represent? | Với A shape (3,2), các hàng biểu diễn gì?**

A. Three equations or observations | Ba phương trình hoặc quan sát

B. Coefficients of two unknowns | Hệ số của hai ẩn

C. The right-hand-side values | Các giá trị vế phải

D. It cannot have a unique solution for every b | Không thể có nghiệm duy nhất với mọi b

**Đáp án: A**

**Giải thích:** Ba hàng tương ứng ba quan sát hoặc phương trình.


**Q10. For Ax=b with A shape (3,2), what do the columns represent? | Với A shape (3,2), các cột biểu diễn gì?**

A. Three equations or observations | Ba phương trình hoặc quan sát

B. Coefficients of two unknowns | Hệ số của hai ẩn

C. The right-hand-side values | Các giá trị vế phải

D. It cannot have a unique solution for every b | Không thể có nghiệm duy nhất với mọi b

**Đáp án: B**

**Giải thích:** Hai cột là hệ số của hai ẩn ở từng phương trình.


**Q11. What does the final column of an augmented matrix represent? | Cột cuối của ma trận mở rộng biểu diễn gì?**

A. Three equations or observations | Ba phương trình hoặc quan sát

B. Coefficients of two unknowns | Hệ số của hai ẩn

C. The right-hand-side values | Các giá trị vế phải

D. It cannot have a unique solution for every b | Không thể có nghiệm duy nhất với mọi b

**Đáp án: C**

**Giải thích:** Ma trận mở rộng ghi các vế phải ở cột cuối.


**Q12. What does a rank-deficient square matrix imply? | Ma trận vuông thiếu hạng gợi ý điều gì?**

A. Three equations or observations | Ba phương trình hoặc quan sát

B. Coefficients of two unknowns | Hệ số của hai ẩn

C. The right-hand-side values | Các giá trị vế phải

D. It cannot have a unique solution for every b | Không thể có nghiệm duy nhất với mọi b

**Đáp án: D**

**Giải thích:** Thiếu hạng đầy đủ khiến không bảo đảm nghiệm duy nhất.


**Q13. If the residual is exactly zero, what is true? | Nếu sai số dư bằng 0 thì điều gì đúng?**

A. Every equation is satisfied | Mọi phương trình đều được thỏa

B. The sum of squared residuals | Tổng bình phương sai số dư

C. Whether a candidate solution approximately satisfies the system | Nghiệm thử có thỏa hệ gần đúng hay không

D. Ranks of A and its augmented matrix | Hạng của A và ma trận mở rộng

**Đáp án: A**

**Giải thích:** Sai số dư bằng 0 nghĩa là Ax=b.


**Q14. What does least squares minimize? | Bình phương tối thiểu làm nhỏ nhất gì?**

A. Every equation is satisfied | Mọi phương trình đều được thỏa

B. The sum of squared residuals | Tổng bình phương sai số dư

C. Whether a candidate solution approximately satisfies the system | Nghiệm thử có thỏa hệ gần đúng hay không

D. Ranks of A and its augmented matrix | Hạng của A và ma trận mở rộng

**Đáp án: B**

**Giải thích:** Bình phương sai lệch làm lỗi lớn bị phạt mạnh.


**Q15. What does `np.allclose(A@x,b)` check? | `np.allclose(A@x,b)` kiểm tra gì?**

A. Every equation is satisfied | Mọi phương trình đều được thỏa

B. The sum of squared residuals | Tổng bình phương sai số dư

C. Whether a candidate solution approximately satisfies the system | Nghiệm thử có thỏa hệ gần đúng hay không

D. Ranks of A and its augmented matrix | Hạng của A và ma trận mở rộng

**Đáp án: C**

**Giải thích:** allclose so kết quả trong ngưỡng sai số số học.


**Q16. What should be compared to diagnose inconsistency of a system? | Để xét hệ vô nghiệm cần so sánh gì?**

A. Every equation is satisfied | Mọi phương trình đều được thỏa

B. The sum of squared residuals | Tổng bình phương sai số dư

C. Whether a candidate solution approximately satisfies the system | Nghiệm thử có thỏa hệ gần đúng hay không

D. Ranks of A and its augmented matrix | Hạng của A và ma trận mở rộng

**Đáp án: D**

**Giải thích:** Hạng A khác hạng [A, b] cho biết hệ vô nghiệm.


**Q17. Why isn't the right-hand side b another unknown? | Vì sao b không phải một ẩn mới?**

A. It contains known target values | Nó chứa giá trị mục tiêu đã biết

B. They add no new independent direction | Chúng không bổ sung hướng độc lập mới

C. When observations outnumber unknowns or do not fit exactly | Khi nhiều quan sát hơn ẩn hoặc không khớp chính xác

D. Prediction is lower than actual | Dự báo thấp hơn thực tế

**Đáp án: A**

**Giải thích:** b là dữ liệu đã biết, x mới là biến chưa biết.


**Q18. What happens when rows of A are multiples of each other? | Nếu các hàng A là bội nhau thì sao?**

A. It contains known target values | Nó chứa giá trị mục tiêu đã biết

B. They add no new independent direction | Chúng không bổ sung hướng độc lập mới

C. When observations outnumber unknowns or do not fit exactly | Khi nhiều quan sát hơn ẩn hoặc không khớp chính xác

D. Prediction is lower than actual | Dự báo thấp hơn thực tế

**Đáp án: B**

**Giải thích:** Hàng tỷ lệ chỉ lặp thông tin tuyến tính.


**Q19. When is `lstsq` useful? | Khi nào `lstsq` hữu ích?**

A. It contains known target values | Nó chứa giá trị mục tiêu đã biết

B. They add no new independent direction | Chúng không bổ sung hướng độc lập mới

C. When observations outnumber unknowns or do not fit exactly | Khi nhiều quan sát hơn ẩn hoặc không khớp chính xác

D. Prediction is lower than actual | Dự báo thấp hơn thực tế

**Đáp án: C**

**Giải thích:** Bình phương tối thiểu tìm cách khớp tốt nhất khi hệ không thỏa hết.


**Q20. What does a negative residual mean under r=prediction−actual? | Sai số dư âm theo r=dự báo−thực tế nghĩa là gì?**

A. It contains known target values | Nó chứa giá trị mục tiêu đã biết

B. They add no new independent direction | Chúng không bổ sung hướng độc lập mới

C. When observations outnumber unknowns or do not fit exactly | Khi nhiều quan sát hơn ẩn hoặc không khớp chính xác

D. Prediction is lower than actual | Dự báo thấp hơn thực tế

**Đáp án: D**

**Giải thích:** Dự báo trừ thực tế là số âm khi dự báo thiếu.

## 8. Nối sang bài kế tiếp

`Ma trận → Rank/Solve → Regression → AI`.
