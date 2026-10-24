# PY-24 — Scalar, vector, norm, đơn vị và dot product


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Scalar** — đại lượng vô hướng; **Vector** — véc-tơ.

`NumPy → Scalar/Vector → Matrix → PCA`

Nắm liên hệ giữa cấu trúc toán học và mảng dữ liệu Python trước khi sử dụng vào học máy.

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

### Tình huống 1 — Tính khoảng cách 2D

**Từ vựng trong mục:** **Scalar** — đại lượng vô hướng.

**Tình huống thực tế:** Robot di chuyển từ (0,0) tới (3,4) mét. Tính khoảng cách theo đường thẳng.

**Vì sao chọn cách giải này?** Norm của vector dịch chuyển là khoảng cách tới gốc.


**Quy trình giải:**

1. Tạo vector từ (0,0) đến (3,4) mét.
2. Tính norm Euclid.
3. In khoảng cách 5 mét.

```python
import numpy as np
v = np.array([3, 4], dtype=float)
print(np.linalg.norm(v))
```

**Kết quả khi chạy:**

```text
5.0
```


### Tình huống 2 — Chuẩn hóa hướng di chuyển

**Từ vựng trong mục:** **Vector** — véc-tơ.

**Tình huống thực tế:** Robot nhận vector hướng (3,4). Chuẩn hóa thành vector đơn vị để chỉ biểu thị hướng.

**Vì sao chọn cách giải này?** Chia vector cho norm tạo hướng có độ dài bằng 1.


**Quy trình giải:**

1. Tạo vector hướng (3,4) dạng float.
2. Tính norm và chia nếu norm khác 0.
3. In vector đơn vị [0.6,0.8].

```python
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


### Tình huống 3 — Điểm tổng kết có trọng số

**Từ vựng trong mục:** **Dot product** — tích vô hướng.

**Tình huống thực tế:** Điểm ba môn của học viên là [8,7,9] theo trọng số [20%,30%,50%]. Tính điểm tổng kết.

**Vì sao chọn cách giải này?** Tích vô hướng kết hợp điểm số và trọng số từng môn.


**Quy trình giải:**

1. Lưu ba điểm và ba trọng số theo cùng thứ tự môn.
2. Nhân bằng `@` để tính tổng có trọng số.
3. In 8.2 điểm trên thang 10.

```python
import numpy as np
scores = np.array([8, 7, 9])
weights = np.array([.2, .3, .5])
print(scores@weights)
```

**Kết quả khi chạy:**

```text
8.2
```


### Tình huống 4 — Tìm hai hướng vuông góc

**Từ vựng trong mục:** **Dot product** — tích vô hướng.

**Tình huống thực tế:** Hai hướng [1,0] và [0,1] cần kiểm tra vuông góc bằng tích vô hướng.

**Vì sao chọn cách giải này?** Tích vô hướng bằng 0 với hai vector khác không chứng tỏ vuông góc.


**Quy trình giải:**

1. Tạo hai vector khác không [1,0] và [0,1].
2. Tính tích vô hướng.
3. In 0 và xác định hai vector vuông góc.

```python
import numpy as np
a = np.array([1, 0])
b = np.array([0, 1])
print(a@b)
```

**Kết quả khi chạy:**

```text
0
```


### Tình huống 5 — Tính sai khác cảm biến

**Từ vựng trong mục:** **Scalar** — đại lượng vô hướng.

**Tình huống thực tế:** Hai lần đo cảm biến theo cặp cùng đơn vị là (20,30) và (23,34). Tính độ lệch Euclid.

**Vì sao chọn cách giải này?** Norm của hiệu vector đo khoảng cách giữa hai lần đo.


**Quy trình giải:**

1. Lưu hai cặp đo cùng đơn vị.
2. Tính hiệu vector và norm của hiệu.
3. In chênh lệch Euclid là 5.

```python
import numpy as np
a = np.array([20, 30])
b = np.array([23, 34])
print(np.linalg.norm(a-b))
```

**Kết quả khi chạy:**

```text
5.0
```


## 6. Sai lầm thường gặp

- Scalar là số đơn; vector là dãy các thành phần có thứ tự.
- Khi tính khoảng cách, các thành phần phải cùng hệ trục và đơn vị phù hợp.
- Không chuẩn hóa vector không vì norm bằng 0.
- Dấu `*` NumPy nhân từng phần tử; `@` với hai vector 1-D tính tích vô hướng.
- Khi kiểm tra vuông góc với dữ liệu float, nên so với một ngưỡng sai số nhỏ.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a scalar? — Scalar là gì?**

A. One numeric value — Một giá trị số

B. An ordered list of components — Dãy thành phần có thứ tự

C. Square root of the sum of squared components — Căn của tổng bình phương các thành phần

D. Sum of pairwise component products — Tổng tích các cặp thành phần tương ứng

**Q2. What is a vector? — Vector là gì?**

A. One numeric value — Một giá trị số

B. An ordered list of components — Dãy thành phần có thứ tự

C. Square root of the sum of squared components — Căn của tổng bình phương các thành phần

D. Sum of pairwise component products — Tổng tích các cặp thành phần tương ứng

**Q3. What is Euclidean norm? — Norm Euclid là gì?**

A. One numeric value — Một giá trị số

B. An ordered list of components — Dãy thành phần có thứ tự

C. Square root of the sum of squared components — Căn của tổng bình phương các thành phần

D. Sum of pairwise component products — Tổng tích các cặp thành phần tương ứng

**Q4. What is the dot product? — Tích vô hướng là gì?**

A. One numeric value — Một giá trị số

B. An ordered list of components — Dãy thành phần có thứ tự

C. Square root of the sum of squared components — Căn của tổng bình phương các thành phần

D. Sum of pairwise component products — Tổng tích các cặp thành phần tương ứng

**Q5. Which function creates a NumPy vector? — Hàm nào tạo vector NumPy?**

A. `np.array([1, 2])` — `np.array([1, 2])`

B. `np.linalg.norm(v)` — `np.linalg.norm(v)`

C. `v / np.linalg.norm(v)` — `v / np.linalg.norm(v)`

D. `a @ b` — `a @ b`

**Q6. Which function computes a vector's L2 length? — Hàm nào tính độ dài L2 của vector?**

A. `np.array([1, 2])` — `np.array([1, 2])`

B. `np.linalg.norm(v)` — `np.linalg.norm(v)`

C. `v / np.linalg.norm(v)` — `v / np.linalg.norm(v)`

D. `a @ b` — `a @ b`

**Q7. Which expression normalizes a nonzero vector? — Biểu thức nào chuẩn hóa vector khác không?**

A. `np.array([1, 2])` — `np.array([1, 2])`

B. `np.linalg.norm(v)` — `np.linalg.norm(v)`

C. `v / np.linalg.norm(v)` — `v / np.linalg.norm(v)`

D. `a @ b` — `a @ b`

**Q8. Which expression computes the dot product of two 1-D vectors? — Biểu thức nào tính tích vô hướng hai vector 1-D?**

A. `np.array([1, 2])` — `np.array([1, 2])`

B. `np.linalg.norm(v)` — `np.linalg.norm(v)`

C. `v / np.linalg.norm(v)` — `v / np.linalg.norm(v)`

D. `a @ b` — `a @ b`

**Q9. What is the norm of vector (3,4)? — Norm của vector (3,4) bằng bao nhiêu?**

A. 5 — 5

B. (0.6,0.8) — (0.6,0.8)

C. 11 — 11

D. 0 — 0

**Q10. What is the unit vector in the direction (3,4)? — Vector đơn vị theo hướng (3,4) là gì?**

A. 5 — 5

B. (0.6,0.8) — (0.6,0.8)

C. 11 — 11

D. 0 — 0

**Q11. What is the dot product (1,2)·(3,4)? — Tích vô hướng (1,2)·(3,4) bằng bao nhiêu?**

A. 5 — 5

B. (0.6,0.8) — (0.6,0.8)

C. 11 — 11

D. 0 — 0

**Q12. What is the dot product of (1,0) and (0,1)? — Tích vô hướng của (1,0) và (0,1) là bao nhiêu?**

A. 5 — 5

B. (0.6,0.8) — (0.6,0.8)

C. 11 — 11

D. 0 — 0

**Q13. What is the dot product of two nonzero perpendicular vectors? — Tích vô hướng của hai vector khác không vuông góc là gì?**

A. Zero — Bằng không

B. That its norm is nonzero — Norm khác không

C. The result can be physically misleading — Kết quả có thể sai ý nghĩa vật lý

D. They must have equal lengths — Chúng phải có cùng số phần tử

**Q14. What must be checked before normalizing a vector? — Cần kiểm tra gì trước khi chuẩn hóa vector?**

A. Zero — Bằng không

B. That its norm is nonzero — Norm khác không

C. The result can be physically misleading — Kết quả có thể sai ý nghĩa vật lý

D. They must have equal lengths — Chúng phải có cùng số phần tử

**Q15. What happens if coordinate units are mixed in a distance calculation? — Nếu đơn vị tọa độ không thống nhất khi tính khoảng cách thì sao?**

A. Zero — Bằng không

B. That its norm is nonzero — Norm khác không

C. The result can be physically misleading — Kết quả có thể sai ý nghĩa vật lý

D. They must have equal lengths — Chúng phải có cùng số phần tử

**Q16. What must be true to compute a 1-D dot product? — Muốn tính tích vô hướng của hai vector 1-D cần điều kiện gì?**

A. Zero — Bằng không

B. That its norm is nonzero — Norm khác không

C. The result can be physically misleading — Kết quả có thể sai ý nghĩa vật lý

D. They must have equal lengths — Chúng phải có cùng số phần tử

**Q17. What does multiplying a vector by a scalar do? — Nhân vector với scalar làm gì?**

A. Scales every component — Nhân từng thành phần với scalar

B. Subtract corresponding components — Trừ các thành phần cùng vị trí

C. Euclidean distance between a and b — Khoảng cách Euclid giữa a và b

D. To multiply each weight by its intended feature — Để trọng số nhân đúng đặc trưng tương ứng

**Q18. How is vector subtraction performed? — Phép trừ vector được thực hiện thế nào?**

A. Scales every component — Nhân từng thành phần với scalar

B. Subtract corresponding components — Trừ các thành phần cùng vị trí

C. Euclidean distance between a and b — Khoảng cách Euclid giữa a và b

D. To multiply each weight by its intended feature — Để trọng số nhân đúng đặc trưng tương ứng

**Q19. What does `np.linalg.norm(a-b)` measure? — `np.linalg.norm(a-b)` đo điều gì?**

A. Scales every component — Nhân từng thành phần với scalar

B. Subtract corresponding components — Trừ các thành phần cùng vị trí

C. Euclidean distance between a and b — Khoảng cách Euclid giữa a và b

D. To multiply each weight by its intended feature — Để trọng số nhân đúng đặc trưng tương ứng

**Q20. Why are feature weights paired with values in the same order? — Vì sao trọng số cần cùng thứ tự với các giá trị?**

A. Scales every component — Nhân từng thành phần với scalar

B. Subtract corresponding components — Trừ các thành phần cùng vị trí

C. Euclidean distance between a and b — Khoảng cách Euclid giữa a và b

D. To multiply each weight by its intended feature — Để trọng số nhân đúng đặc trưng tương ứng

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | A scalar has magnitude without vector components. | Scalar không gồm nhiều thành phần tọa độ. |
| Q2 | **B** | Vector positions identify coordinates or features. | Vị trí từng thành phần biểu thị tọa độ hoặc đặc trưng. |
| Q3 | **C** | L2 norm measures Euclidean length. | Norm L2 đo độ dài theo Euclid. |
| Q4 | **D** | A dot product yields a scalar for equally sized 1-D vectors. | Tích vô hướng cho một số từ hai vector cùng số thành phần. |
| Q5 | **A** | The array constructor stores ordered numeric components. | np.array lưu các thành phần số theo thứ tự. |
| Q6 | **B** | The default norm on a 1-D numeric vector is Euclidean. | Norm mặc định trên vector số một chiều là Euclid. |
| Q7 | **C** | Dividing by its norm creates length one. | Chia cho norm đưa độ dài vector về một. |
| Q8 | **D** | The @ operator computes their inner product. | Toán tử @ tính tích vô hướng của hai vector. |
| Q9 | **A** | The Pythagorean length is sqrt(9+16). | Độ dài Pythagoras là căn của 9+16. |
| Q10 | **B** | Divide each component by length five. | Chia mỗi thành phần cho độ dài năm. |
| Q11 | **C** | Compute 1×3 + 2×4. | Tính 1×3 + 2×4. |
| Q12 | **D** | Both pairwise products vanish. | Cả hai tích thành phần đều bằng không. |
| Q13 | **A** | Orthogonality corresponds to a zero inner product. | Hai hướng trực giao có tích vô hướng bằng không. |
| Q14 | **B** | Dividing by a zero norm is undefined. | Chia cho norm bằng không không xác định. |
| Q15 | **C** | Consistent units are needed for meaningful norms. | Tính norm có ý nghĩa khi đơn vị phù hợp. |
| Q16 | **D** | Components are paired position by position. | Từng thành phần được ghép theo vị trí tương ứng. |
| Q17 | **A** | Scalar multiplication changes component magnitudes. | Nhân scalar làm đổi độ lớn từng thành phần. |
| Q18 | **B** | Subtraction is component-wise. | Phép trừ vector diễn ra theo từng thành phần. |
| Q19 | **C** | The norm of displacement gives distance. | Norm của độ dịch chuyển cho khoảng cách. |
| Q20 | **D** | A misordered vector produces a different dot product. | Sai thứ tự tạo ra tích vô hướng khác. |

## 8. Nối sang bài kế tiếp

`NumPy → Scalar/Vector → Matrix → PCA`.
