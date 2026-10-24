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


**Q1. What is Matrix? — Thuật ngữ Matrix có nghĩa gì?**

A. It instead means Đổi vai trò hàng và cột của ma trận — Đổi vai trò hàng và cột của ma trận

B. It means Bảng hai chiều chứa giá trị theo hàng và cột — Bảng hai chiều chứa giá trị theo hàng và cột

C. It instead means Số của ma trận vuông dùng xét tính khả nghịch — Số của ma trận vuông dùng xét tính khả nghịch

D. It instead means Ma trận B làm AB=BA=I khi tồn tại — Ma trận B làm AB=BA=I khi tồn tại


**Q2. What is Transpose? — Thuật ngữ Transpose có nghĩa gì?**

A. It means Đổi vai trò hàng và cột của ma trận — Đổi vai trò hàng và cột của ma trận

B. It instead means Số của ma trận vuông dùng xét tính khả nghịch — Số của ma trận vuông dùng xét tính khả nghịch

C. It instead means Ma trận B làm AB=BA=I khi tồn tại — Ma trận B làm AB=BA=I khi tồn tại

D. It instead means Bảng hai chiều chứa giá trị theo hàng và cột — Bảng hai chiều chứa giá trị theo hàng và cột


**Q3. What is Determinant? — Thuật ngữ Determinant có nghĩa gì?**

A. It instead means Ma trận B làm AB=BA=I khi tồn tại — Ma trận B làm AB=BA=I khi tồn tại

B. It instead means Bảng hai chiều chứa giá trị theo hàng và cột — Bảng hai chiều chứa giá trị theo hàng và cột

C. It instead means Đổi vai trò hàng và cột của ma trận — Đổi vai trò hàng và cột của ma trận

D. It means Số của ma trận vuông dùng xét tính khả nghịch — Số của ma trận vuông dùng xét tính khả nghịch


**Q4. What is Inverse? — Thuật ngữ Inverse có nghĩa gì?**

A. It instead means Bảng hai chiều chứa giá trị theo hàng và cột — Bảng hai chiều chứa giá trị theo hàng và cột

B. It instead means Đổi vai trò hàng và cột của ma trận — Đổi vai trò hàng và cột của ma trận

C. It means Ma trận B làm AB=BA=I khi tồn tại — Ma trận B làm AB=BA=I khi tồn tại

D. It instead means Số của ma trận vuông dùng xét tính khả nghịch — Số của ma trận vuông dùng xét tính khả nghịch


**Q5. What does np.eye(n) help with? — Hàm np.eye(n) giúp làm gì?**

A. Another function helps to Chuyển vị ma trận — Chuyển vị ma trận

B. It helps to Ma trận đơn vị vuông, nhân vào không đổi vector — Ma trận đơn vị vuông, nhân vào không đổi vector

C. Another function helps to Nhân ma trận khi số cột A bằng số hàng B — Nhân ma trận khi số cột A bằng số hàng B

D. Another function helps to Định thức và nghịch đảo khi khả nghịch; giải hệ nên ưu tiên solve — Định thức và nghịch đảo khi khả nghịch; giải hệ nên ưu tiên solve


**Q6. What does A.T / np.transpose(A) help with? — Hàm A.T / np.transpose(A) giúp làm gì?**

A. It helps to Chuyển vị ma trận — Chuyển vị ma trận

B. Another function helps to Nhân ma trận khi số cột A bằng số hàng B — Nhân ma trận khi số cột A bằng số hàng B

C. Another function helps to Định thức và nghịch đảo khi khả nghịch; giải hệ nên ưu tiên solve — Định thức và nghịch đảo khi khả nghịch; giải hệ nên ưu tiên solve

D. Another function helps to Ma trận đơn vị vuông, nhân vào không đổi vector — Ma trận đơn vị vuông, nhân vào không đổi vector


**Q7. What does A @ B help with? — Hàm A @ B giúp làm gì?**

A. Another function helps to Định thức và nghịch đảo khi khả nghịch; giải hệ nên ưu tiên solve — Định thức và nghịch đảo khi khả nghịch; giải hệ nên ưu tiên solve

B. Another function helps to Ma trận đơn vị vuông, nhân vào không đổi vector — Ma trận đơn vị vuông, nhân vào không đổi vector

C. Another function helps to Chuyển vị ma trận — Chuyển vị ma trận

D. It helps to Nhân ma trận khi số cột A bằng số hàng B — Nhân ma trận khi số cột A bằng số hàng B


**Q8. What does np.linalg.det()/inv() help with? — Hàm np.linalg.det()/inv() giúp làm gì?**

A. Another function helps to Ma trận đơn vị vuông, nhân vào không đổi vector — Ma trận đơn vị vuông, nhân vào không đổi vector

B. Another function helps to Chuyển vị ma trận — Chuyển vị ma trận

C. It helps to Định thức và nghịch đảo khi khả nghịch; giải hệ nên ưu tiên solve — Định thức và nghịch đảo khi khả nghịch; giải hệ nên ưu tiên solve

D. Another function helps to Nhân ma trận khi số cột A bằng số hàng B — Nhân ma trận khi số cột A bằng số hàng B


**Q9. Why choose this method for scenario 1? — Vì sao chọn cách làm tình huống 1?**

A. Matrix product kết hợp các đặc trưng theo trọng số — Matrix product kết hợp các đặc trưng theo trọng số

B. Chuyển vị giúp đổi hàng cửa hàng thành cột cửa hàng — Chuyển vị giúp đổi hàng cửa hàng thành cột cửa hàng

C. Det khác 0 chỉ đối với ma trận vuông mới có nghịch đảo — Det khác 0 chỉ đối với ma trận vuông mới có nghịch đảo

D. Tích A@inv(A) phải gần đơn vị — Tích A@inv(A) phải gần đơn vị


**Q10. Why choose this method for scenario 2? — Vì sao chọn cách làm tình huống 2?**

A. Matrix product kết hợp các đặc trưng theo trọng số — Matrix product kết hợp các đặc trưng theo trọng số

B. Det khác 0 chỉ đối với ma trận vuông mới có nghịch đảo — Det khác 0 chỉ đối với ma trận vuông mới có nghịch đảo

C. Tích A@inv(A) phải gần đơn vị — Tích A@inv(A) phải gần đơn vị

D. Shape không phù hợp sẽ báo lỗi nên kiểm trước — Shape không phù hợp sẽ báo lỗi nên kiểm trước


**Q11. Why choose this method for scenario 3? — Vì sao chọn cách làm tình huống 3?**

A. Tích A@inv(A) phải gần đơn vị — Tích A@inv(A) phải gần đơn vị

B. Shape không phù hợp sẽ báo lỗi nên kiểm trước — Shape không phù hợp sẽ báo lỗi nên kiểm trước

C. Chuyển vị giúp đổi hàng cửa hàng thành cột cửa hàng — Chuyển vị giúp đổi hàng cửa hàng thành cột cửa hàng

D. Det khác 0 chỉ đối với ma trận vuông mới có nghịch đảo — Det khác 0 chỉ đối với ma trận vuông mới có nghịch đảo


**Q12. Why choose this method for scenario 4? — Vì sao chọn cách làm tình huống 4?**

A. Shape không phù hợp sẽ báo lỗi nên kiểm trước — Shape không phù hợp sẽ báo lỗi nên kiểm trước

B. Chuyển vị giúp đổi hàng cửa hàng thành cột cửa hàng — Chuyển vị giúp đổi hàng cửa hàng thành cột cửa hàng

C. Tích A@inv(A) phải gần đơn vị — Tích A@inv(A) phải gần đơn vị

D. Matrix product kết hợp các đặc trưng theo trọng số — Matrix product kết hợp các đặc trưng theo trọng số


**Q13. Why choose this method for scenario 5? — Vì sao chọn cách làm tình huống 5?**

A. Chuyển vị giúp đổi hàng cửa hàng thành cột cửa hàng — Chuyển vị giúp đổi hàng cửa hàng thành cột cửa hàng

B. Shape không phù hợp sẽ báo lỗi nên kiểm trước — Shape không phù hợp sẽ báo lỗi nên kiểm trước

C. Matrix product kết hợp các đặc trưng theo trọng số — Matrix product kết hợp các đặc trưng theo trọng số

D. Det khác 0 chỉ đối với ma trận vuông mới có nghịch đảo — Det khác 0 chỉ đối với ma trận vuông mới có nghịch đảo


**Q14. What input is relevant to scenario 1? — Dữ liệu nào của tình huống 1?**

A. The input is 2 cửa hàng × 3 ngày — 2 cửa hàng × 3 ngày

B. Different data: 2 SV × 3 môn → 2 kết quả — 2 SV × 3 môn → 2 kết quả

C. Different data: Ma trận vuông 2×2 — Ma trận vuông 2×2

D. Different data: Ma trận chéo 2×2 — Ma trận chéo 2×2


**Q15. What input is relevant to scenario 2? — Dữ liệu nào của tình huống 2?**

A. Different data: Ma trận vuông 2×2 — Ma trận vuông 2×2

B. Different data: Ma trận chéo 2×2 — Ma trận chéo 2×2

C. Different data: A (2×3), B (3×2) — A (2×3), B (3×2)

D. The input is 2 SV × 3 môn → 2 kết quả — 2 SV × 3 môn → 2 kết quả


**Q16. What input is relevant to scenario 3? — Dữ liệu nào của tình huống 3?**

A. Different data: Ma trận chéo 2×2 — Ma trận chéo 2×2

B. Different data: A (2×3), B (3×2) — A (2×3), B (3×2)

C. The input is Ma trận vuông 2×2 — Ma trận vuông 2×2

D. Different data: 2 cửa hàng × 3 ngày — 2 cửa hàng × 3 ngày


**Q17. What input is relevant to scenario 4? — Dữ liệu nào của tình huống 4?**

A. Different data: A (2×3), B (3×2) — A (2×3), B (3×2)

B. The input is Ma trận chéo 2×2 — Ma trận chéo 2×2

C. Different data: 2 cửa hàng × 3 ngày — 2 cửa hàng × 3 ngày

D. Different data: 2 SV × 3 môn → 2 kết quả — 2 SV × 3 môn → 2 kết quả


**Q18. What input is relevant to scenario 5? — Dữ liệu nào của tình huống 5?**

A. The input is A (2×3), B (3×2) — A (2×3), B (3×2)

B. Different data: 2 cửa hàng × 3 ngày — 2 cửa hàng × 3 ngày

C. Different data: 2 SV × 3 môn → 2 kết quả — 2 SV × 3 môn → 2 kết quả

D. Different data: Ma trận vuông 2×2 — Ma trận vuông 2×2


**Q19. What should be checked for matrix operations? — Phép toán ma trận phải kiểm tra gì?**

A. Only line spacing — Chỉ khoảng cách dòng

B. Only file suffix — Chỉ phần mở rộng file

C. Only terminal width — Chỉ độ rộng terminal

D. Shapes and data units — Shape và đơn vị dữ liệu


**Q20. Why is one numeric example not enough for AI? — Vì sao một ví dụ số chưa đủ đánh giá AI?**

A. It always proves generalization — Nó luôn chứng minh khả năng tổng quát

B. It removes the need for test data — Nó bỏ được tập kiểm tra

C. It does not establish predictive performance — Nó không đo chất lượng dự đoán

D. It guarantees no leakage — Nó bảo đảm không rò rỉ dữ liệu

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | It means Bảng hai chiều chứa giá trị theo hàng và cột | Bảng hai chiều chứa giá trị theo hàng và cột |
| Q2 | **A** | It means Đổi vai trò hàng và cột của ma trận | Đổi vai trò hàng và cột của ma trận |
| Q3 | **D** | It means Số của ma trận vuông dùng xét tính khả nghịch | Số của ma trận vuông dùng xét tính khả nghịch |
| Q4 | **C** | It means Ma trận B làm AB=BA=I khi tồn tại | Ma trận B làm AB=BA=I khi tồn tại |
| Q5 | **B** | It helps to Ma trận đơn vị vuông, nhân vào không đổi vector | Ma trận đơn vị vuông, nhân vào không đổi vector |
| Q6 | **A** | It helps to Chuyển vị ma trận | Chuyển vị ma trận |
| Q7 | **D** | It helps to Nhân ma trận khi số cột A bằng số hàng B | Nhân ma trận khi số cột A bằng số hàng B |
| Q8 | **C** | It helps to Định thức và nghịch đảo khi khả nghịch; giải hệ nên ưu tiên solve | Định thức và nghịch đảo khi khả nghịch; giải hệ nên ưu tiên solve |
| Q9 | **B** | Chuyển vị giúp đổi hàng cửa hàng thành cột cửa hàng | Chuyển vị giúp đổi hàng cửa hàng thành cột cửa hàng |
| Q10 | **A** | Matrix product kết hợp các đặc trưng theo trọng số | Matrix product kết hợp các đặc trưng theo trọng số |
| Q11 | **D** | Det khác 0 chỉ đối với ma trận vuông mới có nghịch đảo | Det khác 0 chỉ đối với ma trận vuông mới có nghịch đảo |
| Q12 | **C** | Tích A@inv(A) phải gần đơn vị | Tích A@inv(A) phải gần đơn vị |
| Q13 | **B** | Shape không phù hợp sẽ báo lỗi nên kiểm trước | Shape không phù hợp sẽ báo lỗi nên kiểm trước |
| Q14 | **A** | The input is 2 cửa hàng × 3 ngày | 2 cửa hàng × 3 ngày |
| Q15 | **D** | The input is 2 SV × 3 môn → 2 kết quả | 2 SV × 3 môn → 2 kết quả |
| Q16 | **C** | The input is Ma trận vuông 2×2 | Ma trận vuông 2×2 |
| Q17 | **B** | The input is Ma trận chéo 2×2 | Ma trận chéo 2×2 |
| Q18 | **A** | The input is A (2×3), B (3×2) | A (2×3), B (3×2) |
| Q19 | **D** | Shapes and data units | Shape và đơn vị dữ liệu |
| Q20 | **C** | It does not establish predictive performance | Nó không đo chất lượng dự đoán |

## 8. Nối sang bài kế tiếp

`Vector → Matrix → Hệ tuyến tính → Eigenvalue/PCA`.
