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

## 5. Năm tình huống véc-tơ — từ khoảng cách đến kiểm tra sai số đa trục

### Tình huống 1 — Cấp 1: Cộng 10 bước di chuyển và đo độ lệch cuối

**Từ vựng trong mục:** **Vector** — véc-tơ có thứ tự; **Scalar** — số đơn lẻ; **Norm** — độ dài.

**Tình huống thực tế:** Robot ghi **10 bước dịch chuyển**, mỗi bản ghi là cặp `(đi theo trục x, đi theo trục y)` tính bằng mét. Có bước đi âm vì robot có thể đi ngược chiều trục. Cần biết vị trí lệch so với điểm xuất phát và khoảng cách **đường thẳng từ điểm xuất phát**, không nhầm với tổng quãng đường đã đi.

**Vì sao chọn cách này?** Véc-tơ lưu hướng và độ dịch chuyển theo hai trục, còn `np.linalg.norm` biến véc-tơ tổng thành **một số** khoảng cách đường thẳng. Nếu chỉ cộng độ dài mỗi bước sẽ tính tổng quãng đường, là một yêu cầu khác.

**Quy trình:**
1. Tạo 10 véc-tơ 2 chiều với đơn vị mét.
2. Cộng theo trục x/y bằng `sum(axis=0)`.
3. Tính norm của véc-tơ tổng và in đơn vị.

```python
import numpy as np
steps = np.array([[3,4],[0,2],[-2,0],[1,-1],[2,2],[-3,1],[0,-4],[4,0],[-1,3],[2,-2]], dtype=float)
ending = steps.sum(axis=0)
assert steps.shape == (10, 2)
print("Bước:", len(steps))
print("Lệch x (m):", int(ending[0]))
print("Lệch y (m):", int(ending[1]))
print(f"Cách gốc (m): {np.linalg.norm(ending):.2f}")
```

**Kết quả khi chạy:**

```text
Bước: 10
Lệch x (m): 6
Lệch y (m): 5
Cách gốc (m): 7.81
```

Véc-tơ tổng có thể nhỏ hơn tổng quãng đường đi, vì các bước di chuyển ngược chiều triệt tiêu nhau.

### Tình huống 2 — Cấp 2: Chuẩn hóa 12 hướng robot nhưng không chia cho 0

**Từ vựng trong mục:** **Unit vector** — véc-tơ đơn vị; **Zero vector** — véc-tơ không; **Normalization** — chuẩn hóa.

**Tình huống thực tế:** Bộ điều hướng nhận **12 véc-tơ hướng** `(x,y)` không đơn vị, mỗi hàng là một yêu cầu hướng đi. Hai hàng có `(0,0)` nghĩa là **chưa có hướng hợp lệ**. Cần chuẩn hóa mười hướng khác không về độ dài 1, đồng thời báo đúng hai hàng không thể chuẩn hóa, thay vì thực hiện phép chia cho 0.

**Vì sao chọn cách này?** Chia véc-tơ cho norm chỉ thực hiện được khi độ dài lớn hơn 0. Dùng mặt nạ chọn những véc-tơ khác 0, không đoán một hướng mặc định khi dữ liệu chưa xác định.

**Quy trình:**
1. Tạo mảng `(12,2)` và tính norm riêng từng hàng.
2. Chỉ chia các hàng có norm dương; giữ véc-tơ không cho kiểm tra.
3. Đếm số hướng hợp lệ, in véc-tơ đầu sau chuẩn hóa.

```python
import numpy as np
vectors = np.array([[3,4],[0,0],[5,0],[-3,4],[0,5],[6,8],[1,1],[-4,0],[2,-2],[0,-2],[4,3],[0,0]], dtype=float)
lengths = np.linalg.norm(vectors, axis=1)
valid = lengths > 0
normalized = np.zeros_like(vectors)
normalized[valid] = vectors[valid] / lengths[valid, None]
assert len(vectors) == 12
print("Yêu cầu:", len(vectors))
print("Hướng hợp lệ:", int(valid.sum()))
print("Hướng chưa xác định:", int((~valid).sum()))
print("Véc-tơ đầu:", ", ".join(f"{x:.2f}" for x in normalized[0]))
```

**Kết quả khi chạy:**

```text
Yêu cầu: 12
Hướng hợp lệ: 10
Hướng chưa xác định: 2
Véc-tơ đầu: 0.60, 0.80
```

Véc-tơ không vẫn được bảo toàn trên bản dữ liệu xử lý nhưng **không** được coi là hướng di chuyển có độ dài 1.

### Tình huống 3 — Cấp 3: Dot product cho 15 điểm tổng kết theo ba tiêu chí

**Từ vựng trong mục:** **Dot product** — tích vô hướng; **Weight** — trọng số; **Threshold** — ngưỡng.

**Tình huống thực tế:** Giáo viên ghi **15 học viên** H01…H15; mỗi hàng có ba điểm lý thuyết, thực hành, dự án (thang 10). Quy tắc nội bộ cho ba trọng số tương ứng 20%, 30%, 50%, học viên đạt từ **7,5 điểm tổng kết**. Hãy tính một điểm cho mỗi người và đếm số người đạt, giữ đúng thứ tự trọng số so với cột.

**Vì sao chọn cách này?** Tích vô hướng nhân mỗi điểm của **cùng học viên** với trọng số cột tương ứng rồi cộng lại. Thay trọng số sai cột sẽ cho kết quả khác dù dữ liệu không đổi.

**Quy trình:**
1. Tạo ma trận 15 × 3 và véc-tơ ba trọng số.
2. Nhân `scores @ weights` để có 15 kết quả.
3. Đếm người đạt ngưỡng 7,5; in điểm đầu và cuối để đối chiếu.

```python
import numpy as np
scores = np.array([[5,6,7],[6,8,10],[7,10,9],[8,7,8],[9,9,7],[5,6,10],[6,8,9],[7,10,8],[8,7,7],[9,9,10],[5,6,9],[6,8,8],[7,10,7],[8,7,10],[9,9,9]], dtype=float)
weights = np.array([0.2, 0.3, 0.5])
final_scores = scores @ weights
assert scores.shape == (15, 3) and final_scores.shape == (15,)
print("Học viên:", len(final_scores))
print(f"H01: {final_scores[0]:.2f}")
print(f"H15: {final_scores[-1]:.2f}")
print("Đạt 7.5:", int((final_scores >= 7.5).sum()))
```

**Kết quả khi chạy:**

```text
Học viên: 15
H01: 6.30
H15: 9.00
Đạt 7.5: 12
```

Trọng số phản ánh quy định giả lập của lớp; dot product tạo một số theo mỗi học viên, không phải một bảng 15 × 3 sau khi tính.

### Tình huống 4 — Cấp 4: Phân 18 hướng vuông góc và ngược chiều với hướng chuẩn

**Từ vựng trong mục:** **Orthogonality** — vuông góc; **Dot product** — tích vô hướng; **Projection** — chiếu theo trục.

**Tình huống thực tế:** Robot cần so **18 véc-tơ hướng điều khiển** `(x,y)` với hướng chuẩn đi sang phải `(1,0)`, mỗi dòng là một lệnh. Nếu tích vô hướng bằng 0, lệnh vuông góc; nếu âm, lệnh có thành phần ngược chiều; nếu dương, có thành phần cùng chiều. Cần đếm ba nhóm mà không chỉ nhìn dấu một tọa độ trên hình.

**Vì sao chọn cách này?** Tích vô hướng so hướng của véc-tơ với hướng chuẩn. Trong dữ liệu ví dụ mọi véc-tơ đều khác không; phép so bằng 0 được áp trên các số nguyên nên không có nhiễu dấu phẩy động.

**Quy trình:**
1. Tạo mảng 18 hàng × 2 cột và véc-tơ chuẩn.
2. Tính 18 tích vô hướng `directions @ reference`.
3. Đếm trường hợp âm, 0 và dương; xác minh tổng bằng 18.

```python
import numpy as np
directions = np.array([[-1,0],[0,1],[1,0],[0,-1],[1,1],[-1,1],[-1,0],[0,1],[1,0],[0,-1],[1,1],[-1,1],[-1,0],[0,1],[1,0],[0,-1],[1,1],[-1,1]], dtype=float)
reference = np.array([1.0, 0.0])
projections = directions @ reference
assert directions.shape == (18, 2)
print("Lệnh:", len(directions))
print("Ngược chiều:", int((projections < 0).sum()))
print("Vuông góc:", int((projections == 0).sum()))
print("Cùng chiều:", int((projections > 0).sum()))
```

**Kết quả khi chạy:**

```text
Lệnh: 18
Ngược chiều: 6
Vuông góc: 6
Cùng chiều: 6
```

Phân loại bằng tích vô hướng là về **thành phần hướng so với véc-tơ chuẩn**, không suy ra robot đã thực sự di chuyển bao xa.

### Tình huống 5 — Cấp 5: Xếp hạng sai số 20 cảm biến ba trục bằng độ dài véc-tơ

**Từ vựng trong mục:** **Residual vector** — véc-tơ sai lệch; **Norm** — độ lớn sai số; **Ranking** — xếp hạng.

**Tình huống thực tế:** Nhà máy có **20 lượt đo 3 trục** X/Y/Z, mỗi hàng gồm véc-tơ dự kiến và véc-tơ cảm biến (đơn vị mm trên mỗi trục). Một số lượt lệch nhiều hơn ở Z. Kỹ thuật viên cần tính độ lớn sai lệch của từng lượt, đánh dấu khi độ lớn **lớn hơn 2 mm**, tìm lượt sai nhất và trung bình độ lớn sai lệch. Đây là phép đối chiếu hình học, không phải chẩn đoán hỏng thiết bị.

**Vì sao chọn cách này?** Trừ từng véc-tơ quan sát với chuẩn tạo véc-tơ sai lệch ba chiều; `norm(axis=1)` trả một số mm cho từng lượt. Tính tổng sai số từng trục có dấu có thể triệt tiêu nhau, nên dùng norm khi hỏi độ lệch tổng thể.

**Quy trình:**
1. Lưu 20 cặp véc-tơ 3D theo đúng thứ tự trục.
2. Tính sai lệch từng hàng, sau đó norm của 20 véc-tơ.
3. Đếm vượt ngưỡng 2 mm, tìm mã lượt lớn nhất và báo trung bình.

```python
import numpy as np
observed = np.array([[10,20,30],[11,21,31],[12,22,32],[13,23,30],[14,20,31],[10,21,32],[11,22,30],[12,23,31],[13,20,32],[14,21,30],[10,22,31],[11,23,32],[12,20,30],[13,21,31],[14,22,32],[10,23,30],[11,20,31],[12,21,32],[13,22,30],[14,23,31]], dtype=float)
expected = np.array([[11,19,33],[12,20,31],[13,21,32],[14,22,30],[15,19,31],[11,20,32],[12,21,30],[13,22,34],[14,19,32],[15,20,30],[11,21,31],[12,22,32],[13,19,30],[14,20,31],[15,21,35],[11,22,30],[12,19,31],[13,20,32],[14,21,30],[15,22,31]], dtype=float)
residual = observed - expected
errors = np.linalg.norm(residual, axis=1)
worst = int(errors.argmax())
assert observed.shape == expected.shape == (20, 3)
print("Lượt đo:", len(errors))
print("Vượt 2 mm:", int((errors > 2).sum()))
print("Lượt sai nhất:", f"M{worst+1:02d}")
print(f"Sai số lớn nhất (mm): {errors[worst]:.2f}")
print(f"Sai số TB (mm): {errors.mean():.2f}")
```

**Kết quả khi chạy:**

```text
Lượt đo: 20
Vượt 2 mm: 3
Lượt sai nhất: M01
Sai số lớn nhất (mm): 3.32
Sai số TB (mm): 1.70
```

Mỗi hàng là một lượt đo 3 trục có cùng đơn vị mm. Mức 2 mm là **ngưỡng ví dụ**, phải do chuyên gia thiết bị quyết định khi ứng dụng thật.

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
