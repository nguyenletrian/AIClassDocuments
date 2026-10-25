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

```python
# Mục đích: Một hệ phương trình chung các ẩn.
import numpy as np

A = np.array([[1, 1], [2, 1]], dtype=float)
b = np.array([5, 8], dtype=float)
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

```python
# Mục đích: Số thông tin độc lập.
import numpy as np

A = np.array([[1, 2], [2, 4]])
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

```python
# Mục đích: Bảng hệ số và vế phải.
import numpy as np

A = np.array([[1, 1], [2, 1]])
b = np.array([5, 8])
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

```python
# Mục đích: Sai lệch và nghiệm bình phương tối thiểu.
import numpy as np

x = np.array([1, 2, 3])
y = np.array([2, 4, 6.1])
A = np.column_stack((x, np.ones_like(x)))
coeff = np.linalg.lstsq(A, y, rcond=None)[0]
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

**Tình huống thực tế:** Cửa hàng có **10 hóa đơn**, mỗi hàng là số lượng sản phẩm A, số lượng B (món) và tổng tiền (nghìn đồng). Giá mỗi món cố định nhưng chưa biết. Hai hóa đơn đầu có tổ hợp số lượng khác nhau nên đủ thông tin tìm giá; cần tìm giá A/B và kiểm tra **cả 10 hóa đơn**, không chỉ hai dòng được chọn để giải.

**Vì sao chọn cách này?** Mỗi hóa đơn là một phương trình với hai ẩn giá. `np.linalg.solve` giải hệ 2×2 đầu; phép nhân `A @ prices` sau đó kiểm tra toàn bộ 10 hóa đơn có khớp tiền thực tế hay không.

**Quy trình:**
1. Tạo bảng 10 hàng số lượng và 10 tổng tiền cùng thứ tự.
2. Chọn hai hàng độc lập đầu để giải hệ 2 ẩn.
3. Dự tính tổng tiền cả 10 hàng rồi đếm sai lệch lớn hơn ngưỡng nhỏ.

```python
import numpy as np
quantities = np.array([[1,1],[2,1],[3,1],[4,1],[1,2],[2,2],[3,2],[4,2],[1,3],[2,3]], dtype=float)
totals = np.array([5,8,11,14,7,10,13,16,9,12], dtype=float)
prices = np.linalg.solve(quantities[:2], totals[:2])
residual = quantities @ prices - totals
assert quantities.shape == (10, 2)
print("Hóa đơn:", len(totals))
print("Giá A (nghìn đồng):", f"{prices[0]:.1f}")
print("Giá B (nghìn đồng):", f"{prices[1]:.1f}")
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

**Tình huống thực tế:** Một trạm ghi **12 lần vận hành**, mỗi hàng gồm số giờ chạy máy x (giờ) và một cột được tính đúng bằng hai lần x. Kỹ thuật viên muốn biết bảng 12×2 chứa hai nguồn thông tin độc lập hay chỉ một, trước khi dùng dữ liệu để giải hệ.

**Vì sao chọn cách này?** Cột thứ hai chỉ là bản phóng đại cột đầu, không mang thêm một chiều thông tin tuyến tính. `matrix_rank()` cho biết số chiều độc lập, nhỏ hơn số cột khi phụ thuộc.

**Quy trình:**
1. Lưu 12 cặp số giờ, cột hai bằng hai lần cột một.
2. Gọi `matrix_rank` để kiểm số chiều độc lập.
3. Kiểm tra hai cột phụ thuộc và in kích thước/hạng.

```python
import numpy as np
hours = np.array([1,2,3,4,5,6,7,8,9,10,11,12], dtype=float)
X = np.column_stack((hours, 2 * hours))
assert X.shape == (12, 2)
print("Lượt vận hành:", X.shape[0])
print("Cột:", X.shape[1])
print("Hạng:", int(np.linalg.matrix_rank(X)))
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

**Tình huống thực tế:** Thiết bị có **15 lượt đo**, mỗi lượt trộn hai tín hiệu gốc x/y theo cùng quy tắc: kênh A nhận `2x+y`, kênh B nhận `x+3y` (đơn vị tín hiệu). Hai số đo của một lượt tạo một vector vế phải. Cần giải từng lượt và kiểm tra dữ liệu khôi phục tái tạo chính xác các kênh.

**Vì sao chọn cách này?** Ma trận hệ số 2×2 không đổi và có định thức khác 0. NumPy có thể giải **15 vế phải cùng lúc** khi cột của bảng số đo là một lượt, tránh viết 15 lời gọi giải riêng.

**Quy trình:**
1. Tạo ma trận hệ số và 15 cặp kênh được đo.
2. Chuyển vị số đo, đưa vào `np.linalg.solve` rồi chuyển vị kết quả.
3. Tái tạo hai kênh và kiểm tra mọi lượt.

```python
import numpy as np
A = np.array([[2., 1.], [1., 3.]])
measured = np.array([[4,7],[6,8],[8,9],[10,10],[12,11],[5,10],[7,11],[9,12],[11,13],[13,14],[6,13],[8,14],[10,15],[12,16],[14,17]], dtype=float)
restored = np.linalg.solve(A, measured.T).T
assert measured.shape == restored.shape == (15, 2)
print("Lượt đo:", len(restored))
print("Hạng hệ số:", int(np.linalg.matrix_rank(A)))
print("Tín hiệu gốc đầu:", ", ".join(f"{v:.1f}" for v in restored[0]))
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

**Tình huống thực tế:** Bộ phận hiệu chuẩn ghi **18 cặp** số giờ vận hành x (giờ) và mức tiêu thụ y (đơn vị giả lập). Quy tắc kỹ thuật dự kiến là đường thẳng `y = m*x + c` với một cặp m/c áp dụng chung. Lượt 10 bị nhập cao hơn 7 đơn vị, nên **không có một cặp m/c khớp chính xác cả 18 lượt**. Cần phát hiện vấn đề bằng so hạng hệ số và hạng ma trận mở rộng.

**Vì sao chọn cách này?** Nếu `rank([A|b])` lớn hơn `rank(A)`, các phương trình không thể đồng thời đúng. Không được dùng `solve` cho ma trận 18×2 không vuông; so hạng chỉ ra hệ không nhất quán trước khi thử xấp xỉ.

**Quy trình:**
1. Tạo bảng hệ số 18 hàng, hai cột x và cột 1; y là vế phải.
2. Ghép ma trận mở rộng bằng `column_stack`, tính hai hạng.
3. Báo kết luận có hay không nghiệm khớp mọi lượt.

```python
import numpy as np
hours = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], dtype=float)
y = np.array([7,9,11,13,15,17,19,21,23,32,27,29,31,33,35,37,39,41], dtype=float)
A = np.column_stack((hours, np.ones_like(hours)))
augmented = np.column_stack((A, y))
rank_a = int(np.linalg.matrix_rank(A))
rank_aug = int(np.linalg.matrix_rank(augmented))
assert A.shape == (18, 2) and augmented.shape == (18, 3)
print("Số phương trình:", len(y))
print("Hạng hệ số:", rank_a)
print("Hạng mở rộng:", rank_aug)
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

**Tình huống thực tế:** Nhà máy có **20 lần đo**: mỗi hàng gồm số giờ chạy x (giờ) và năng lượng y (kWh) trong cùng khoảng quan sát. Mẫu giả lập gần đường thẳng tăng 4 kWh/giờ, có mức nền 10 kWh; lượt thứ 5 và 17 bị nhiễu. Cần tìm hệ số góc và chặn xấp xỉ bằng bình phương tối thiểu, sau đó báo MSE và số lần dự báo lệch quá 5 kWh.

**Vì sao chọn cách này?** Khác hệ có nghiệm chính xác, `lstsq` chọn đường thẳng làm tổng sai số bình phương thấp nhất khi 20 phương trình không khớp hoàn toàn. Phải giữ đơn vị: độ dốc kWh/giờ, hệ số chặn kWh, MSE kWh².

**Quy trình:**
1. Tạo A từ 20 cặp x/y với một cột x và một cột 1.
2. Fit bằng `lstsq` khi A có hạng 2.
3. Tính phần dư, MSE và số lượt có sai lệch lớn.

```python
import numpy as np
hours = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], dtype=float)
energy = np.array([14,18,22,26,42,34,38,42,46,50,54,58,62,66,70,74,70,82,86,90], dtype=float)
A = np.column_stack((hours, np.ones_like(hours)))
slope, intercept = np.linalg.lstsq(A, energy, rcond=None)[0]
residual = A @ np.array([slope, intercept]) - energy
assert A.shape == (20, 2) and np.linalg.matrix_rank(A) == 2
print("Lượt đo:", len(energy))
print(f"Độ dốc (kWh/giờ): {slope:.2f}")
print(f"Nền (kWh): {intercept:.2f}")
print(f"MSE (kWh²): {np.mean(residual ** 2):.2f}")
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


**Q5. Which tool solves a nonsingular square system? | Hàm nào giải hệ vuông không suy biến?**

A. `np.linalg.solve(A,b)` | `np.linalg.solve(A,b)`

B. `np.linalg.matrix_rank(A)` | `np.linalg.matrix_rank(A)`

C. `np.column_stack((A,b))` | `np.column_stack((A,b))`

D. `np.linalg.lstsq(A,b,rcond=None)` | `np.linalg.lstsq(A,b,rcond=None)`

**Đáp án: A**

**Giải thích:** solve dùng cho ma trận hệ số vuông, không suy biến.


**Q6. Which tool determines matrix rank? | Hàm nào tính hạng ma trận?**

A. `np.linalg.solve(A,b)` | `np.linalg.solve(A,b)`

B. `np.linalg.matrix_rank(A)` | `np.linalg.matrix_rank(A)`

C. `np.column_stack((A,b))` | `np.column_stack((A,b))`

D. `np.linalg.lstsq(A,b,rcond=None)` | `np.linalg.lstsq(A,b,rcond=None)`

**Đáp án: B**

**Giải thích:** matrix_rank đo số chiều độc lập.


**Q7. Which tool builds an augmented matrix? | Hàm nào ghép ma trận mở rộng?**

A. `np.linalg.solve(A,b)` | `np.linalg.solve(A,b)`

B. `np.linalg.matrix_rank(A)` | `np.linalg.matrix_rank(A)`

C. `np.column_stack((A,b))` | `np.column_stack((A,b))`

D. `np.linalg.lstsq(A,b,rcond=None)` | `np.linalg.lstsq(A,b,rcond=None)`

**Đáp án: C**

**Giải thích:** column_stack ghép b thành cột bên cạnh A.


**Q8. Which tool computes a least-squares solution? | Hàm nào tìm nghiệm bình phương tối thiểu?**

A. `np.linalg.solve(A,b)` | `np.linalg.solve(A,b)`

B. `np.linalg.matrix_rank(A)` | `np.linalg.matrix_rank(A)`

C. `np.column_stack((A,b))` | `np.column_stack((A,b))`

D. `np.linalg.lstsq(A,b,rcond=None)` | `np.linalg.lstsq(A,b,rcond=None)`

**Đáp án: D**

**Giải thích:** lstsq tối thiểu hóa bình phương độ dài Ax−b.


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
