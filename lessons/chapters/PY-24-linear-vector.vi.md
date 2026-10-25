# PY-24 — Scalar, vector, norm, đơn vị và dot product


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Scalar** — đại lượng vô hướng; **Vector** — véc-tơ.

`NumPy → Scalar/Vector → Matrix → PCA`

**Học xong dùng để làm gì?** Biểu diễn học viên hay sản phẩm dưới dạng vector đặc trưng số và thực hiện phép cộng/trừ vector.

**Kết nối kiến thức tiếp theo:** PY-25 xếp nhiều vector thành ma trận để tính cùng lúc nhiều quan sát.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích |
|---|---|---|
| Scalar | đại lượng vô hướng | Một số đơn lẻ có thể đo độ lớn |
| Vector | véc-tơ | Dãy số mô tả nhiều thành phần của một đối tượng |
| Norm | độ lớn véc-tơ | Độ dài theo chuẩn đã chọn |
| Dot product | tích vô hướng | Nhân từng cặp tọa độ tương ứng rồi cộng |

## 3. NumPy và các hàm liên quan

**Từ vựng trong mục:** **Function** — hàm; **Shape** — kích thước mảng.

| Hàm / tham số | Dùng làm gì |
|---|---|
| `np.array([...],dtype=float)` | Tạo véc-tơ kiểu thực khi phép tính tạo phần thập phân |
| `np.linalg.norm(v)` | Độ lớn Euclidean của véc-tơ |
| `v/np.linalg.norm(v)` | Chuẩn hóa về độ dài 1, phải tránh norm bằng 0 |
| `a @ b / np.dot(a,b)` | Tích vô hướng nếu hai vector một chiều cùng độ dài |

## 4. Khái niệm liên quan

Bài học nối bốn ý: **scalar** là số đơn lẻ, **vector** chứa tọa độ, **norm** đo độ dài, **dot product** kết hợp các thành phần. Robot dịch chuyển `(3,4)` mét có vector hai chiều nhưng quãng đường thẳng chỉ là một số bằng 5 mét.

### 4.1. Scalar — Số đơn lẻ và đơn vị

Scalar là một giá trị số như vận tốc 2,5 mét/giây. Python lưu số, còn ý nghĩa và đơn vị phải do người lập trình nêu. Scalar khác vector vì không chứa nhiều thành phần tọa độ.

```python
# Mục đích: Số đơn lẻ và đơn vị.
speed = 2.5
print(speed)
```

**Kết quả khi chạy:**

```text
2.5
```

Số 2.5 đại diện vận tốc m/s, không phải tọa độ.

### 4.2. Vector — Các tọa độ có thứ tự

Vector là dãy tọa độ theo một hệ trục. Robot đi 3 m theo x và 4 m theo y nên dùng vector `[3,4]`. Phần tử đầu là x, phần tử sau là y. Đổi `[3,4]` thành `[4,3]` sẽ đổi ý nghĩa hai trục.

```python
# Mục đích: Các tọa độ có thứ tự.
import numpy as np

movement = np.array([3, 4])
print(movement)
```

**Kết quả khi chạy:**

```text
[3 4]
```

Hai phần tử lần lượt là độ dịch chuyển theo x và y (mét).

### 4.3. Norm — Độ dài vector

Chuẩn Euclid là độ dài `sqrt(x²+y²)`. Với vector `(3,4)`, độ dài bằng `sqrt(9+16)=5` m. Vector đơn vị giữ hướng và có norm bằng 1; muốn chuẩn hóa phải chia các thành phần cho norm, trừ trường hợp norm bằng 0.

```python
# Mục đích: Độ dài vector.
import numpy as np

movement = np.array([3.0, 4.0])
print(np.linalg.norm(movement))
```

**Kết quả khi chạy:**

```text
5.0
```

Robot cách gốc tọa độ 5 mét theo đường thẳng.

### 4.4. Dot product — Nhân và cộng cùng vị trí

Tích vô hướng của hai vector cùng số chiều bằng tổng các tích từng thành phần: `(1,2)·(3,4)=1×3+2×4=11`. Dùng để tính điểm có trọng số hoặc kiểm tra hai vector khác không vuông góc (khi tích vô hướng bằng 0).

```python
# Mục đích: Nhân và cộng cùng vị trí.
import numpy as np

a = np.array([1, 2])
b = np.array([3, 4])
print(a @ b)
```

**Kết quả khi chạy:**

```text
11
```

Tích vô hướng trả một scalar bằng 11.

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Tính khoảng cách 2D · Cấp 1: Một phép cơ bản

**Từ vựng trong mục:** **Scalar** — đại lượng vô hướng.

**Tình huống thực tế:** Robot di chuyển từ (0,0) tới (3,4) mét. Tính khoảng cách theo đường thẳng.

**Vì sao chọn cách giải này?** Norm của vector dịch chuyển là khoảng cách tới gốc.


**Quy trình giải:**

1. Tạo vector từ (0,0) đến (3,4) mét.
2. Tính norm Euclid.
3. In khoảng cách 5 mét.

```python
# Mục đích: Tính khoảng cách 2D.
import numpy as np
v = np.array([3, 4], dtype=float)
print(np.linalg.norm(v))
```

**Kết quả khi chạy:**

```text
5.0
```

**Bài thực hành nâng cấp — cấp 1/5:** Robot ghi **10 điểm đo tọa độ 2D**, mỗi hàng là một vị trí và hai cột là tọa độ x/y, đơn vị mét. Hãy tính chuẩn của vector 2D đầu tiên. Dữ liệu thiếu ở mức 4–5 được loại khi tính ma trận cần đầy đủ hai tọa độ; đồng thời giữ số hàng gốc để kiểm tra.

```python
import numpy as np
# Mỗi hàng là một điểm đo robot: cột 0=x (m), cột 1=y (m).
xs = [42, 70, 58, 91, 35, 76, 88, 64, 54, 96]
ys = [20+(k*7)%75 for k in range(1,11)]
array = np.column_stack((xs,ys)).astype(float)
clean = array[np.isfinite(array).all(axis=1)]
result = round(float(np.linalg.norm(clean[0])),3)
assert array.shape==(10,2)
print("Số điểm đo:",len(array))
print("Kết quả:",result)
```

**Đọc kết quả:** Số quan sát 10; đọc shape, số hàng hợp lệ và đơn vị từ phép xử lý. Không đánh đồng norm, dot product hoặc định thức với một đại lượng vô đơn vị.

### Tình huống 2 — Chuẩn hóa hướng di chuyển · Cấp 2: Xử lý hàng loạt

**Từ vựng trong mục:** **Vector** — véc-tơ.

**Tình huống thực tế:** Robot nhận vector hướng (3,4). Chuẩn hóa thành vector đơn vị để chỉ biểu thị hướng.

**Vì sao chọn cách giải này?** Chia vector cho norm tạo hướng có độ dài bằng 1.


**Quy trình giải:**

1. Tạo vector hướng (3,4) dạng float.
2. Tính norm và chia nếu norm khác 0.
3. In vector đơn vị [0.6,0.8].

```python
# Mục đích: Chuẩn hóa hướng di chuyển.
import numpy as np
v = np.array([3., 4.])
norm = np.linalg.norm(v)
u = v/norm if norm else v
print(u)
```

**Kết quả khi chạy:**

```text
[0.6 0.8]
```

**Bài thực hành nâng cấp — cấp 2/5:** Robot ghi **12 điểm đo tọa độ 2D**, mỗi hàng là một vị trí và hai cột là tọa độ x/y, đơn vị mét. Hãy chuẩn hóa 12 vector, tránh chia cho vector 0. Dữ liệu thiếu ở mức 4–5 được loại khi tính ma trận cần đầy đủ hai tọa độ; đồng thời giữ số hàng gốc để kiểm tra.

```python
import numpy as np
# Mỗi hàng là một điểm đo robot: cột 0=x (m), cột 1=y (m).
xs = [42, 70, 58, 91, 35, 76, 88, 64, 54, 96, 47, 82]
ys = [20+(k*7)%75 for k in range(1,13)]
array = np.column_stack((xs,ys)).astype(float)
clean = array[np.isfinite(array).all(axis=1)]
result = np.linalg.norm(clean,axis=1)[:5].round(3).tolist()
assert array.shape==(12,2)
print("Số điểm đo:",len(array))
print("Kết quả:",result)
```

**Đọc kết quả:** Số quan sát 12; đọc shape, số hàng hợp lệ và đơn vị từ phép xử lý. Không đánh đồng norm, dot product hoặc định thức với một đại lượng vô đơn vị.

### Tình huống 3 — Điểm tổng kết có trọng số · Cấp 3: Kết hợp vector/ma trận

**Từ vựng trong mục:** **Dot product** — tích vô hướng.

**Tình huống thực tế:** Điểm ba môn của học viên là [8,7,9] theo trọng số [20%,30%,50%]. Tính điểm tổng kết.

**Vì sao chọn cách giải này?** Tích vô hướng kết hợp điểm số và trọng số từng môn.


**Quy trình giải:**

1. Lưu ba điểm và ba trọng số theo cùng thứ tự môn.
2. Nhân bằng `@` để tính tổng có trọng số.
3. In 8.2 điểm trên thang 10.

```python
# Mục đích: Điểm tổng kết có trọng số.
import numpy as np
scores = np.array([8, 7, 9])
weights = np.array([.2, .3, .5])
print(scores@weights)
```

**Kết quả khi chạy:**

```text
8.2
```

**Bài thực hành nâng cấp — cấp 3/5:** Robot ghi **15 điểm đo tọa độ 2D**, mỗi hàng là một vị trí và hai cột là tọa độ x/y, đơn vị mét. Hãy tính điểm theo dot product cho 15 vector đặc trưng. Dữ liệu thiếu ở mức 4–5 được loại khi tính ma trận cần đầy đủ hai tọa độ; đồng thời giữ số hàng gốc để kiểm tra.

```python
import numpy as np
# Mỗi hàng là một điểm đo robot: cột 0=x (m), cột 1=y (m).
xs = [42, 70, 58, 91, 35, 76, 88, 64, 54, 96, 47, 82, 69, 73, 61]
ys = [20+(k*7)%75 for k in range(1,16)]
array = np.column_stack((xs,ys)).astype(float)
clean = array[np.isfinite(array).all(axis=1)]
result = (clean@np.array([0.4,0.6])).round(2).tolist()
assert array.shape==(15,2)
print("Số điểm đo:",len(array))
print("Kết quả:",result)
```

**Đọc kết quả:** Số quan sát 15; đọc shape, số hàng hợp lệ và đơn vị từ phép xử lý. Không đánh đồng norm, dot product hoặc định thức với một đại lượng vô đơn vị.

### Tình huống 4 — Tìm hai hướng vuông góc · Cấp 4: Giá trị thiếu và ràng buộc

**Từ vựng trong mục:** **Dot product** — tích vô hướng.

**Tình huống thực tế:** Hai hướng [1,0] và [0,1] cần kiểm tra vuông góc bằng tích vô hướng.

**Vì sao chọn cách giải này?** Tích vô hướng bằng 0 với hai vector khác không chứng tỏ vuông góc.


**Quy trình giải:**

1. Tạo hai vector khác không [1,0] và [0,1].
2. Tính tích vô hướng.
3. In 0 và xác định hai vector vuông góc.

```python
# Mục đích: Tìm hai hướng vuông góc.
import numpy as np
a = np.array([1, 0])
b = np.array([0, 1])
print(a@b)
```

**Kết quả khi chạy:**

```text
0
```

**Bài thực hành nâng cấp — cấp 4/5:** Robot ghi **18 điểm đo tọa độ 2D**, mỗi hàng là một vị trí và hai cột là tọa độ x/y, đơn vị mét. Hãy đếm và loại vector có số đo thiếu trước khi tính norm. Dữ liệu thiếu ở mức 4–5 được loại khi tính ma trận cần đầy đủ hai tọa độ; đồng thời giữ số hàng gốc để kiểm tra.

```python
import numpy as np
# Mỗi hàng là một điểm đo robot: cột 0=x (m), cột 1=y (m).
xs = [42, 70, 58, 91, 35, 76, 88, 64, 54, 96, 47, 82, 69, 73, 61, np.nan, 90, 39]
ys = [20+(k*7)%75 for k in range(1,19)]
array = np.column_stack((xs,ys)).astype(float)
clean = array[np.isfinite(array).all(axis=1)]
result = {'valid':len(clean),'missing':int(len(array)-len(clean)),'mean_norm':round(float(np.linalg.norm(clean,axis=1).mean()),2)}
assert array.shape==(18,2)
print("Số điểm đo:",len(array))
print("Kết quả:",result)
```

**Đọc kết quả:** Số quan sát 18; đọc shape, số hàng hợp lệ và đơn vị từ phép xử lý. Không đánh đồng norm, dot product hoặc định thức với một đại lượng vô đơn vị.

### Tình huống 5 — Tính sai khác cảm biến · Cấp 5: Bài toán tổng hợp

**Từ vựng trong mục:** **Scalar** — đại lượng vô hướng.

**Tình huống thực tế:** Hai lần đo cảm biến theo cặp cùng đơn vị là (20,30) và (23,34). Tính độ lệch Euclid.

**Vì sao chọn cách giải này?** Norm của hiệu vector đo khoảng cách giữa hai lần đo.


**Quy trình giải:**

1. Lưu hai cặp đo cùng đơn vị.
2. Tính hiệu vector và norm của hiệu.
3. In chênh lệch Euclid là 5.

```python
# Mục đích: Tính sai khác cảm biến.
import numpy as np
a = np.array([20, 30])
b = np.array([23, 34])
print(np.linalg.norm(a-b))
```

**Kết quả khi chạy:**

```text
5.0
```

**Bài thực hành nâng cấp — cấp 5/5:** Robot ghi **20 điểm đo tọa độ 2D**, mỗi hàng là một vị trí và hai cột là tọa độ x/y, đơn vị mét. Hãy tổng hợp norm, dot product và số vector hợp lệ trên 20 đối tượng. Dữ liệu thiếu ở mức 4–5 được loại khi tính ma trận cần đầy đủ hai tọa độ; đồng thời giữ số hàng gốc để kiểm tra.

```python
import numpy as np
# Mỗi hàng là một điểm đo robot: cột 0=x (m), cột 1=y (m).
xs = [42, 70, 58, 91, 35, 76, 88, 64, 54, 96, 47, 82, 69, 73, 61, np.nan, 90, 39, 85, np.nan]
ys = [20+(k*7)%75 for k in range(1,21)]
array = np.column_stack((xs,ys)).astype(float)
clean = array[np.isfinite(array).all(axis=1)]
result = {'shape':array.shape,'valid':len(clean),'score_mean':round(float((clean@np.array([0.4,0.6])).mean()),2),'max_norm':round(float(np.linalg.norm(clean,axis=1).max()),2)}
assert array.shape==(20,2)
print("Số điểm đo:",len(array))
print("Kết quả:",result)
```

**Đọc kết quả:** Số quan sát 20; đọc shape, số hàng hợp lệ và đơn vị từ phép xử lý. Không đánh đồng norm, dot product hoặc định thức với một đại lượng vô đơn vị.

## 6. Sai lầm thường gặp

- Scalar là số đơn; vector là dãy các thành phần có thứ tự.
- Khi tính khoảng cách, các thành phần phải cùng hệ trục và đơn vị phù hợp.
- Không chuẩn hóa vector không vì norm bằng 0.
- Dấu `*` NumPy nhân từng phần tử; `@` với hai vector 1-D tính tích vô hướng.
- Khi kiểm tra vuông góc với dữ liệu float, nên so với một ngưỡng sai số nhỏ.

## 7. Trắc nghiệm

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a scalar? | Scalar là gì?**

A. One numeric value | Một giá trị số

B. An ordered list of components | Dãy thành phần có thứ tự

C. Square root of the sum of squared components | Căn của tổng bình phương các thành phần

D. Sum of pairwise component products | Tổng tích các cặp thành phần tương ứng

**Đáp án: A**

**Giải thích:** Scalar không gồm nhiều thành phần tọa độ.


**Q2. What is a vector? | Vector là gì?**

A. One numeric value | Một giá trị số

B. An ordered list of components | Dãy thành phần có thứ tự

C. Square root of the sum of squared components | Căn của tổng bình phương các thành phần

D. Sum of pairwise component products | Tổng tích các cặp thành phần tương ứng

**Đáp án: B**

**Giải thích:** Vị trí từng thành phần biểu thị tọa độ hoặc đặc trưng.


**Q3. What is Euclidean norm? | Norm Euclid là gì?**

A. One numeric value | Một giá trị số

B. An ordered list of components | Dãy thành phần có thứ tự

C. Square root of the sum of squared components | Căn của tổng bình phương các thành phần

D. Sum of pairwise component products | Tổng tích các cặp thành phần tương ứng

**Đáp án: C**

**Giải thích:** Norm L2 đo độ dài theo Euclid.


**Q4. What is the dot product? | Tích vô hướng là gì?**

A. One numeric value | Một giá trị số

B. An ordered list of components | Dãy thành phần có thứ tự

C. Square root of the sum of squared components | Căn của tổng bình phương các thành phần

D. Sum of pairwise component products | Tổng tích các cặp thành phần tương ứng

**Đáp án: D**

**Giải thích:** Tích vô hướng cho một số từ hai vector cùng số thành phần.


**Q5. Which function creates a NumPy vector? | Hàm nào tạo vector NumPy?**

A. `np.array([1, 2])` | `np.array([1, 2])`

B. `np.linalg.norm(v)` | `np.linalg.norm(v)`

C. `v / np.linalg.norm(v)` | `v / np.linalg.norm(v)`

D. `a @ b` | `a @ b`

**Đáp án: A**

**Giải thích:** np.array lưu các thành phần số theo thứ tự.


**Q6. Which function computes a vector's L2 length? | Hàm nào tính độ dài L2 của vector?**

A. `np.array([1, 2])` | `np.array([1, 2])`

B. `np.linalg.norm(v)` | `np.linalg.norm(v)`

C. `v / np.linalg.norm(v)` | `v / np.linalg.norm(v)`

D. `a @ b` | `a @ b`

**Đáp án: B**

**Giải thích:** Norm mặc định trên vector số một chiều là Euclid.


**Q7. Which expression normalizes a nonzero vector? | Biểu thức nào chuẩn hóa vector khác không?**

A. `np.array([1, 2])` | `np.array([1, 2])`

B. `np.linalg.norm(v)` | `np.linalg.norm(v)`

C. `v / np.linalg.norm(v)` | `v / np.linalg.norm(v)`

D. `a @ b` | `a @ b`

**Đáp án: C**

**Giải thích:** Chia cho norm đưa độ dài vector về một.


**Q8. Which expression computes the dot product of two 1-D vectors? | Biểu thức nào tính tích vô hướng hai vector 1-D?**

A. `np.array([1, 2])` | `np.array([1, 2])`

B. `np.linalg.norm(v)` | `np.linalg.norm(v)`

C. `v / np.linalg.norm(v)` | `v / np.linalg.norm(v)`

D. `a @ b` | `a @ b`

**Đáp án: D**

**Giải thích:** Toán tử @ tính tích vô hướng của hai vector.


**Q9. What is the norm of vector (3,4)? | Norm của vector (3,4) bằng bao nhiêu?**

A. 5 | 5

B. (0.6,0.8) | (0.6,0.8)

C. 11 | 11

D. 0 | 0

**Đáp án: A**

**Giải thích:** Độ dài Pythagoras là căn của 9+16.


**Q10. What is the unit vector in the direction (3,4)? | Vector đơn vị theo hướng (3,4) là gì?**

A. 5 | 5

B. (0.6,0.8) | (0.6,0.8)

C. 11 | 11

D. 0 | 0

**Đáp án: B**

**Giải thích:** Chia mỗi thành phần cho độ dài năm.


**Q11. What is the dot product (1,2)·(3,4)? | Tích vô hướng (1,2)·(3,4) bằng bao nhiêu?**

A. 5 | 5

B. (0.6,0.8) | (0.6,0.8)

C. 11 | 11

D. 0 | 0

**Đáp án: C**

**Giải thích:** Tính 1×3 + 2×4.


**Q12. What is the dot product of (1,0) and (0,1)? | Tích vô hướng của (1,0) và (0,1) là bao nhiêu?**

A. 5 | 5

B. (0.6,0.8) | (0.6,0.8)

C. 11 | 11

D. 0 | 0

**Đáp án: D**

**Giải thích:** Cả hai tích thành phần đều bằng không.


**Q13. What is the dot product of two nonzero perpendicular vectors? | Tích vô hướng của hai vector khác không vuông góc là gì?**

A. Zero | Bằng không

B. That its norm is nonzero | Norm khác không

C. The result can be physically misleading | Kết quả có thể sai ý nghĩa vật lý

D. They must have equal lengths | Chúng phải có cùng số phần tử

**Đáp án: A**

**Giải thích:** Hai hướng trực giao có tích vô hướng bằng không.


**Q14. What must be checked before normalizing a vector? | Cần kiểm tra gì trước khi chuẩn hóa vector?**

A. Zero | Bằng không

B. That its norm is nonzero | Norm khác không

C. The result can be physically misleading | Kết quả có thể sai ý nghĩa vật lý

D. They must have equal lengths | Chúng phải có cùng số phần tử

**Đáp án: B**

**Giải thích:** Chia cho norm bằng không không xác định.


**Q15. What happens if coordinate units are mixed in a distance calculation? | Nếu đơn vị tọa độ không thống nhất khi tính khoảng cách thì sao?**

A. Zero | Bằng không

B. That its norm is nonzero | Norm khác không

C. The result can be physically misleading | Kết quả có thể sai ý nghĩa vật lý

D. They must have equal lengths | Chúng phải có cùng số phần tử

**Đáp án: C**

**Giải thích:** Tính norm có ý nghĩa khi đơn vị phù hợp.


**Q16. What must be true to compute a 1-D dot product? | Muốn tính tích vô hướng của hai vector 1-D cần điều kiện gì?**

A. Zero | Bằng không

B. That its norm is nonzero | Norm khác không

C. The result can be physically misleading | Kết quả có thể sai ý nghĩa vật lý

D. They must have equal lengths | Chúng phải có cùng số phần tử

**Đáp án: D**

**Giải thích:** Từng thành phần được ghép theo vị trí tương ứng.


**Q17. What does multiplying a vector by a scalar do? | Nhân vector với scalar làm gì?**

A. Scales every component | Nhân từng thành phần với scalar

B. Subtract corresponding components | Trừ các thành phần cùng vị trí

C. Euclidean distance between a and b | Khoảng cách Euclid giữa a và b

D. To multiply each weight by its intended feature | Để trọng số nhân đúng đặc trưng tương ứng

**Đáp án: A**

**Giải thích:** Nhân scalar làm đổi độ lớn từng thành phần.


**Q18. How is vector subtraction performed? | Phép trừ vector được thực hiện thế nào?**

A. Scales every component | Nhân từng thành phần với scalar

B. Subtract corresponding components | Trừ các thành phần cùng vị trí

C. Euclidean distance between a and b | Khoảng cách Euclid giữa a và b

D. To multiply each weight by its intended feature | Để trọng số nhân đúng đặc trưng tương ứng

**Đáp án: B**

**Giải thích:** Phép trừ vector diễn ra theo từng thành phần.


**Q19. What does `np.linalg.norm(a-b)` measure? | `np.linalg.norm(a-b)` đo điều gì?**

A. Scales every component | Nhân từng thành phần với scalar

B. Subtract corresponding components | Trừ các thành phần cùng vị trí

C. Euclidean distance between a and b | Khoảng cách Euclid giữa a và b

D. To multiply each weight by its intended feature | Để trọng số nhân đúng đặc trưng tương ứng

**Đáp án: C**

**Giải thích:** Norm của độ dịch chuyển cho khoảng cách.


**Q20. Why are feature weights paired with values in the same order? | Vì sao trọng số cần cùng thứ tự với các giá trị?**

A. Scales every component | Nhân từng thành phần với scalar

B. Subtract corresponding components | Trừ các thành phần cùng vị trí

C. Euclidean distance between a and b | Khoảng cách Euclid giữa a và b

D. To multiply each weight by its intended feature | Để trọng số nhân đúng đặc trưng tương ứng

**Đáp án: D**

**Giải thích:** Sai thứ tự tạo ra tích vô hướng khác.

## 8. Nối sang bài kế tiếp

`NumPy → Scalar/Vector → Matrix → PCA`.
