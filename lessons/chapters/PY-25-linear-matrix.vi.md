# PY-25 — Ma trận, chuyển vị, nhân ma trận và định thức


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Matrix** — ma trận; **Transpose** — chuyển vị.

`Vector → Matrix → Hệ tuyến tính → Eigenvalue/PCA`

Nắm liên hệ giữa cấu trúc toán học và mảng dữ liệu Python trước khi sử dụng vào học máy.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích |
|---|---|---|
| Matrix | ma trận | Bảng hai chiều chứa giá trị theo hàng và cột |
| Transpose | chuyển vị | Đổi vai trò hàng và cột của ma trận |
| Determinant | định thức | Số của ma trận vuông dùng xét tính khả nghịch |
| Inverse | ma trận nghịch đảo | Ma trận B làm AB=BA=I khi tồn tại |

## 3. NumPy và các hàm liên quan

**Từ vựng trong mục:** **Function** — hàm; **Shape** — kích thước mảng.

| Hàm / tham số | Dùng làm gì |
|---|---|
| `np.eye(n)` | Ma trận đơn vị vuông, nhân vào không đổi vector |
| `A.T / np.transpose(A)` | Chuyển vị ma trận |
| `A @ B` | Nhân ma trận khi số cột A bằng số hàng B |
| `np.linalg.det()/inv()` | Định thức và nghịch đảo khi khả nghịch; giải hệ nên ưu tiên solve |

## 4. Khái niệm liên quan

**Ma trận (matrix)** là bảng có hàng và cột được xác định rõ theo dữ liệu. Từ bảng điểm hai học viên và ba môn, bài học giải thích chuyển vị để đổi cách xem, nhân ma trận để tổng hợp trọng số, rồi định thức và nghịch đảo khi làm việc với ma trận vuông.

### 4.1. Matrix — Bảng số có hàng và cột

Ma trận là bảng số hai chiều. Với điểm học viên An `[8,7,9]` và Bình `[6,5,8]` ở ba môn Toán, Văn, Python, bảng có **hai hàng học viên** và **ba cột môn**. Giá trị `[1,0]` nghĩa là điểm Toán của Bình bằng 6. `shape` cho kích thước, theo thứ tự (số hàng, số cột).

```python
import numpy as np

scores = np.array([[8, 7, 9], [6, 5, 8]])
print(scores.shape)
```

**Kết quả khi chạy:**

```text
(2, 3)
```

Bảng có hai học viên và ba môn học.

### 4.2. Transpose — Hoán đổi hai trục

Chuyển vị `A.T` biến hàng thành cột và cột thành hàng. Với bảng điểm hai học viên × ba môn, ma trận sau chuyển vị có ba hàng môn và hai cột học viên. Ví dụ hàng đầu là điểm Toán của An và Bình, `[8,6]`; không có điểm nào bị thay đổi.

```python
import numpy as np

scores = np.array([[8, 7, 9], [6, 5, 8]])
print(scores.T)
```

**Kết quả khi chạy:**

```text
[[8 6]
 [7 5]
 [9 8]]
```

Kết quả gồm ba hàng môn × hai cột học viên.

### 4.3. Matrix multiplication — Nhân ma trận

Nhân `X @ W` yêu cầu số cột của X bằng số hàng của W. Bảng điểm X có shape `(2,3)`, trọng số ba môn W có shape `(3,1)`, tích có shape `(2,1)` cho điểm tổng của từng học viên. Dòng An là `8×0.2 + 7×0.3 + 9×0.5 = 8.2`. `@` khác phép nhân từng phần tử `*`.

```python
import numpy as np

X = np.array([[8, 7, 9], [6, 5, 8]])
W = np.array([[0.2], [0.3], [0.5]])
print(X @ W)
```

**Kết quả khi chạy:**

```text
[[8.2]
 [6.7]]
```

Hai hàng là hai học viên; một cột là điểm tổng kết của mỗi người.

### 4.4. Determinant và inverse — Khả nghịch

Định thức `det(A)` là số xác định cho **ma trận vuông**. Với A=`[[2,1],[1,2]]`, định thức bằng `2×2 - 1×1 = 3`, khác 0, nên tồn tại ma trận nghịch đảo `A⁻¹` thỏa `A @ A⁻¹ = I`. Nếu định thức bằng 0 thì không có nghịch đảo. Khi giải hệ phương trình, ưu tiên `np.linalg.solve` hơn việc tính nghịch đảo trực tiếp.

```python
import numpy as np

A = np.array([[2.0, 1.0], [1.0, 2.0]])
print(round(float(np.linalg.det(A)), 6))
```

**Kết quả khi chạy:**

```text
3.0
```

Định thức 3 khác 0, nên ma trận vuông này khả nghịch.

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Đổi bố cục dữ liệu báo cáo

**Từ vựng trong mục:** **Matrix** — ma trận.

**Tình huống thực tế:** Báo cáo bán hàng có 2 cửa hàng và 3 ngày, mỗi hàng là một cửa hàng. Đổi thành 3 hàng ngày và 2 cột cửa hàng.

**Vì sao chọn cách giải này?** Chuyển vị đổi bảng hai hàng cửa hàng × ba cột ngày thành ba hàng ngày × hai cột cửa hàng.


**Quy trình giải:**

1. Lưu bảng hai cửa hàng × ba ngày.
2. Chuyển vị bằng `.T`.
3. In shape `(3,2)` tương ứng ngày × cửa hàng.

```python
import numpy as np
X=np.array([[10,20,30],[12,8,5]])
print(X.T.shape)
```

**Kết quả khi chạy:**

```text
(3, 2)
```


### Tình huống 2 — Nhân bảng điểm và trọng số

**Từ vựng trong mục:** **Matrix multiplication** — nhân ma trận.

**Tình huống thực tế:** Hai học viên có điểm theo ba môn lần lượt (8,7,9) và (6,5,8); hệ số là (0.2,0.3,0.5). Tính điểm có trọng số.

**Vì sao chọn cách giải này?** Nhân bảng điểm 2×3 với trọng số 3×1 tạo mỗi học viên một điểm tổng.


**Quy trình giải:**

1. Tạo bảng hai học viên × ba môn.
2. Đặt trọng số ba môn theo một cột (3×1).
3. Nhân `X @ W` và in hai điểm tổng.

```python
import numpy as np
X=np.array([[8,7,9],[6,5,8]])
W=np.array([[.2],[.3],[.5]])
print(X@W)
```

**Kết quả khi chạy:**

```text
[[8.2]
 [6.7]]
```


### Tình huống 3 — Kiểm tra ma trận khả nghịch

**Từ vựng trong mục:** **Determinant** — định thức.

**Tình huống thực tế:** Ma trận hệ số [[2,1],[1,2]] có thể khả nghịch nếu định thức khác 0. Tính định thức để kiểm tra.

**Vì sao chọn cách giải này?** Định thức khác 0 xác định ma trận vuông khả nghịch; làm tròn hạn chế nhiễu số cuối.


**Quy trình giải:**

1. Tạo ma trận vuông hệ số `[[2,1],[1,2]]`.
2. Tính định thức và làm tròn sáu chữ số.
3. Kiểm tra giá trị 3 khác 0 để kết luận khả nghịch.

```python
import numpy as np
A=np.array([[2,1],[1,2]],dtype=float)
print(round(np.linalg.det(A),6))
```

**Kết quả khi chạy:**

```text
3.0
```


### Tình huống 4 — Kiểm tra nghịch đảo

**Từ vựng trong mục:** **Inverse** — ma trận nghịch đảo.

**Tình huống thực tế:** Với ma trận đường chéo diag(2,4), kiểm tra tích ma trận và nghịch đảo có gần ma trận đơn vị không.

**Vì sao chọn cách giải này?** Nhân ma trận với nghịch đảo gần ma trận đơn vị; `allclose` chấp nhận sai số dấu phẩy động.


**Quy trình giải:**

1. Tạo ma trận đường chéo `diag(2,4)`.
2. Tính nghịch đảo rồi nhân `A @ inv(A)`.
3. So với ma trận đơn vị bằng `np.allclose`.

```python
import numpy as np
A=np.diag([2.,4.])
print(np.allclose(A@np.linalg.inv(A),np.eye(2)))
```

**Kết quả khi chạy:**

```text
True
```


### Tình huống 5 — Kiểm tra shape trước nhân

**Từ vựng trong mục:** **Matrix** — ma trận.

**Tình huống thực tế:** Một ma trận 2×3 nhân một ma trận 3×2. Kiểm tra kích thước tích kết quả.

**Vì sao chọn cách giải này?** Kiểm tra chiều trong bằng nhau để xác định phép nhân hợp lệ và shape kết quả.


**Quy trình giải:**

1. Tạo A shape 2×3 và B shape 3×2.
2. So số cột A với số hàng B.
3. Nhân A@B và in shape `(2,2)`.

```python
import numpy as np
A=np.ones((2,3))
B=np.ones((3,2))
assert A.shape[1]==B.shape[0]
print((A@B).shape)
```

**Kết quả khi chạy:**

```text
(2, 2)
```


## 6. Sai lầm thường gặp

- `shape=(2,3)` nghĩa là hai hàng và ba cột, không phải ba hàng hai cột.
- `.T` hoán đổi trục; phép nhân `@` yêu cầu số cột bên trái bằng số hàng bên phải.
- Định thức chỉ tính trên ma trận vuông; ma trận có định thức 0 không có nghịch đảo.
- Dữ liệu số thực có sai số làm tròn; dùng `np.allclose` khi kiểm tra gần đúng với ma trận đơn vị.
- Khi giải hệ tuyến tính, thường ưu tiên `np.linalg.solve` thay vì tính nghịch đảo trực tiếp.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a matrix? — Ma trận là gì?**

A. A two-dimensional array of values — Bảng dữ liệu hai chiều

B. A matrix with rows and columns exchanged — Ma trận đổi vai trò hàng và cột

C. Rows of the left matrix with columns of the right — Hàng ma trận trái với cột ma trận phải

D. A scalar associated with a square matrix — Một số gắn với ma trận vuông

**Q2. What is the transpose of a matrix? — Chuyển vị của ma trận là gì?**

A. A two-dimensional array of values — Bảng dữ liệu hai chiều

B. A matrix with rows and columns exchanged — Ma trận đổi vai trò hàng và cột

C. Rows of the left matrix with columns of the right — Hàng ma trận trái với cột ma trận phải

D. A scalar associated with a square matrix — Một số gắn với ma trận vuông

**Q3. What does matrix multiplication combine? — Phép nhân ma trận kết hợp gì?**

A. A two-dimensional array of values — Bảng dữ liệu hai chiều

B. A matrix with rows and columns exchanged — Ma trận đổi vai trò hàng và cột

C. Rows of the left matrix with columns of the right — Hàng ma trận trái với cột ma trận phải

D. A scalar associated with a square matrix — Một số gắn với ma trận vuông

**Q4. What is a determinant? — Định thức là gì?**

A. A two-dimensional array of values — Bảng dữ liệu hai chiều

B. A matrix with rows and columns exchanged — Ma trận đổi vai trò hàng và cột

C. Rows of the left matrix with columns of the right — Hàng ma trận trái với cột ma trận phải

D. A scalar associated with a square matrix — Một số gắn với ma trận vuông

**Q5. What is the shape of a matrix with two rows and three columns? — Ma trận hai hàng ba cột có shape gì?**

A. `(2, 3)` — `(2, 3)`

B. `(3, 2)` — `(3, 2)`

C. `(2, 1)` — `(2, 1)`

D. `(3, 3)` — `(3, 3)`

**Q6. What is the transpose shape of a (2,3) matrix? — Chuyển vị ma trận (2,3) có shape gì?**

A. `(2, 3)` — `(2, 3)`

B. `(3, 2)` — `(3, 2)`

C. `(2, 1)` — `(2, 1)`

D. `(3, 3)` — `(3, 3)`

**Q7. What shape results from (2,3) @ (3,1)? — Phép (2,3) @ (3,1) cho shape gì?**

A. `(2, 3)` — `(2, 3)`

B. `(3, 2)` — `(3, 2)`

C. `(2, 1)` — `(2, 1)`

D. `(3, 3)` — `(3, 3)`

**Q8. What is the shape of `np.eye(3)`? — `np.eye(3)` tạo ma trận shape nào?**

A. `(2, 3)` — `(2, 3)`

B. `(3, 2)` — `(3, 2)`

C. `(2, 1)` — `(2, 1)`

D. `(3, 3)` — `(3, 3)`

**Q9. Which operator performs matrix multiplication? — Toán tử nào thực hiện nhân ma trận?**

A. `@` — `@`

B. `.T` — `.T`

C. `np.linalg.det(A)` — `np.linalg.det(A)`

D. `np.linalg.inv(A)` — `np.linalg.inv(A)`

**Q10. Which attribute returns the transpose of a 2-D ndarray? — Thuộc tính nào cho chuyển vị mảng 2-D?**

A. `@` — `@`

B. `.T` — `.T`

C. `np.linalg.det(A)` — `np.linalg.det(A)`

D. `np.linalg.inv(A)` — `np.linalg.inv(A)`

**Q11. Which function computes a square matrix determinant? — Hàm nào tính định thức ma trận vuông?**

A. `@` — `@`

B. `.T` — `.T`

C. `np.linalg.det(A)` — `np.linalg.det(A)`

D. `np.linalg.inv(A)` — `np.linalg.inv(A)`

**Q12. Which function computes a nonsingular matrix inverse? — Hàm nào tính nghịch đảo ma trận khả nghịch?**

A. `@` — `@`

B. `.T` — `.T`

C. `np.linalg.det(A)` — `np.linalg.det(A)`

D. `np.linalg.inv(A)` — `np.linalg.inv(A)`

**Q13. When is a square matrix invertible? — Khi nào ma trận vuông khả nghịch?**

A. Its determinant is nonzero — Định thức khác không

B. 3 — 3

C. Identity matrix — Ma trận đơn vị

D. `np.allclose(A, B)` — `np.allclose(A, B)`

**Q14. What is determinant of [[2,1],[1,2]]? — Định thức [[2,1],[1,2]] bằng gì?**

A. Its determinant is nonzero — Định thức khác không

B. 3 — 3

C. Identity matrix — Ma trận đơn vị

D. `np.allclose(A, B)` — `np.allclose(A, B)`

**Q15. What does `A @ inv(A)` approximate? — `A @ inv(A)` gần bằng gì?**

A. Its determinant is nonzero — Định thức khác không

B. 3 — 3

C. Identity matrix — Ma trận đơn vị

D. `np.allclose(A, B)` — `np.allclose(A, B)`

**Q16. How do you test approximate equality of float arrays? — Kiểm tra hai mảng float gần bằng nhau bằng gì?**

A. Its determinant is nonzero — Định thức khác không

B. 3 — 3

C. Identity matrix — Ma trận đơn vị

D. `np.allclose(A, B)` — `np.allclose(A, B)`

**Q17. Which dimensions must match for A @ B? — Nhân A @ B cần các chiều nào bằng nhau?**

A. Columns of A and rows of B — Số cột A và số hàng B

B. Element-wise multiplication — Nhân theo từng phần tử

C. `np.linalg.solve(A, b)` — `np.linalg.solve(A, b)`

D. A linear algebra error — Lỗi đại số tuyến tính

**Q18. What does `A * B` do for compatible NumPy arrays? — `A * B` trên mảng NumPy tương thích làm gì?**

A. Columns of A and rows of B — Số cột A và số hàng B

B. Element-wise multiplication — Nhân theo từng phần tử

C. `np.linalg.solve(A, b)` — `np.linalg.solve(A, b)`

D. A linear algebra error — Lỗi đại số tuyến tính

**Q19. What is preferred to solve Ax=b numerically? — Để giải hệ Ax=b bằng NumPy nên ưu tiên gì?**

A. Columns of A and rows of B — Số cột A và số hàng B

B. Element-wise multiplication — Nhân theo từng phần tử

C. `np.linalg.solve(A, b)` — `np.linalg.solve(A, b)`

D. A linear algebra error — Lỗi đại số tuyến tính

**Q20. What happens to a singular matrix when using `np.linalg.inv`? — Dùng `np.linalg.inv` với ma trận suy biến thường gây gì?**

A. Columns of A and rows of B — Số cột A và số hàng B

B. Element-wise multiplication — Nhân theo từng phần tử

C. `np.linalg.solve(A, b)` — `np.linalg.solve(A, b)`

D. A linear algebra error — Lỗi đại số tuyến tính

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | A matrix arranges entries by row and column. | Ma trận sắp phần tử theo hàng và cột. |
| Q2 | **B** | Transposition exchanges the matrix axes. | Chuyển vị hoán đổi các trục ma trận. |
| Q3 | **C** | Each output is an inner product of a row and a column. | Mỗi ô kết quả là tích vô hướng một hàng với một cột. |
| Q4 | **D** | The determinant helps determine invertibility. | Định thức hỗ trợ kiểm tra tính khả nghịch. |
| Q5 | **A** | Shape lists rows before columns. | Shape ghi số hàng trước số cột. |
| Q6 | **B** | Rows and columns exchange places. | Hàng và cột đổi vai trò. |
| Q7 | **C** | The inner 3 dimensions match; outer dimensions remain. | Hai chiều trong bằng 3; giữ hai chiều ngoài. |
| Q8 | **D** | The identity matrix of size 3 is square. | Ma trận đơn vị bậc 3 là ma trận vuông. |
| Q9 | **A** | @ follows matrix multiplication rules. | @ thực hiện đúng quy tắc nhân ma trận. |
| Q10 | **B** | T is a convenient transpose attribute. | T là thuộc tính chuyển vị tiện dụng. |
| Q11 | **C** | det returns a scalar determinant. | det trả định thức dạng số. |
| Q12 | **D** | inv computes A inverse for invertible matrices. | inv tính nghịch đảo khi ma trận khả nghịch. |
| Q13 | **A** | Nonzero determinant is equivalent to nonsingularity. | Định thức khác 0 tương đương khả nghịch. |
| Q14 | **B** | The 2×2 determinant is 2×2−1×1. | Định thức 2×2 bằng 2×2−1×1. |
| Q15 | **C** | A times its inverse equals I in exact arithmetic. | Nhân ma trận với nghịch đảo bằng I trong tính toán chính xác. |
| Q16 | **D** | allclose tolerates small floating-point errors. | allclose chấp nhận sai số dấu phẩy động nhỏ. |
| Q17 | **A** | Matrix multiplication contracts the shared inner dimension. | Nhân ma trận yêu cầu hai chiều trong trùng. |
| Q18 | **B** | Star multiplies corresponding entries with broadcasting. | Dấu sao nhân phần tử tương ứng có broadcasting. |
| Q19 | **C** | Solving directly is generally preferable to forming an explicit inverse. | Giải trực tiếp thường tốt hơn tính nghịch đảo rồi nhân. |
| Q20 | **D** | A singular matrix lacks an inverse. | Ma trận suy biến không có nghịch đảo. |

## 8. Nối sang bài kế tiếp

`Vector → Matrix → Hệ tuyến tính → Eigenvalue/PCA`.
