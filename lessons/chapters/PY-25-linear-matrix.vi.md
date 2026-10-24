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

### 4.1. Matrix

**Từ vựng trong mục:** **Matrix** — ma trận.

Bảng hai chiều chứa giá trị theo hàng và cột. Trước khi sử dụng biểu thức hãy xem phần tử, hàng/cột và đơn vị đầu vào.

```python
import numpy as np
print(np.array([[1,2],[3,4]]).shape)
```

**Kết quả khi chạy:**

```text
(2, 2)
```

**Tự kiểm tra:** Matrix có nghĩa gì? **Đáp án:** Bảng hai chiều chứa giá trị theo hàng và cột.

### 4.2. Transpose

**Từ vựng trong mục:** **Transpose** — chuyển vị.

Đổi vai trò hàng và cột của ma trận. Trước khi sử dụng biểu thức hãy xem phần tử, hàng/cột và đơn vị đầu vào.

```python
import numpy as np
print(np.array([[1,2],[3,4]]).T)
```

**Kết quả khi chạy:**

```text
[[1 3]
 [2 4]]
```

**Tự kiểm tra:** Transpose có nghĩa gì? **Đáp án:** Đổi vai trò hàng và cột của ma trận.

### 4.3. Determinant

**Từ vựng trong mục:** **Determinant** — định thức.

Số của ma trận vuông dùng xét tính khả nghịch. Trước khi sử dụng biểu thức hãy xem phần tử, hàng/cột và đơn vị đầu vào.

```python
import numpy as np
print(np.linalg.det([[1,2],[3,4]]))
```

**Kết quả khi chạy:**

```text
-2.0000000000000004
```

**Tự kiểm tra:** Determinant có nghĩa gì? **Đáp án:** Số của ma trận vuông dùng xét tính khả nghịch.

### 4.4. Inverse

**Từ vựng trong mục:** **Inverse** — ma trận nghịch đảo.

Ma trận B làm AB=BA=I khi tồn tại. Trước khi sử dụng biểu thức hãy xem phần tử, hàng/cột và đơn vị đầu vào.

```python
import numpy as np
print(np.linalg.inv([[2.,0.],[0.,3.]]))
```

**Kết quả khi chạy:**

```text
[[0.5        0.        ]
 [0.         0.33333333]]
```

**Tự kiểm tra:** Inverse có nghĩa gì? **Đáp án:** Ma trận B làm AB=BA=I khi tồn tại.

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Đổi bố cục dữ liệu báo cáo

**Từ vựng trong mục:** **Matrix** — ma trận.

**Tình huống thực tế:** Một tổ chức đang triển khai hệ thống dữ liệu muốn đổi bố cục dữ liệu báo cáo. Bộ dữ liệu đang có: 2 cửa hàng × 3 ngày. Hãy lập trình giải quyết yêu cầu này và đưa ra kết quả có thể kiểm tra.

**Vì sao chọn phương án?** Chuyển vị giúp đổi hàng cửa hàng thành cột cửa hàng; điều kiện tiên quyết là dữ liệu có shape và ý nghĩa từng giá trị rõ ràng.


**Quy trình:** mô tả dữ liệu → xác định phép tính/shape → tính bằng Python → kiểm tra kết quả.

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

**Từ vựng trong mục:** **Transpose** — chuyển vị.

**Tình huống thực tế:** Một trường học muốn nhân bảng điểm và trọng số. Bộ dữ liệu đang có: 2 SV × 3 môn → 2 kết quả. Hãy lập trình giải quyết yêu cầu này và đưa ra kết quả có thể kiểm tra.

**Vì sao chọn phương án?** Matrix product kết hợp các đặc trưng theo trọng số; điều kiện tiên quyết là dữ liệu có shape và ý nghĩa từng giá trị rõ ràng.


**Quy trình:** mô tả dữ liệu → xác định phép tính/shape → tính bằng Python → kiểm tra kết quả.

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

**Tình huống thực tế:** Một nhóm phân tích dữ liệu muốn kiểm tra ma trận khả nghịch. Bộ dữ liệu đang có: Ma trận vuông 2×2. Hãy lập trình giải quyết yêu cầu này và đưa ra kết quả có thể kiểm tra.

**Vì sao chọn phương án?** Det khác 0 chỉ đối với ma trận vuông mới có nghịch đảo; điều kiện tiên quyết là dữ liệu có shape và ý nghĩa từng giá trị rõ ràng.


**Quy trình:** mô tả dữ liệu → xác định phép tính/shape → tính bằng Python → kiểm tra kết quả.

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

**Tình huống thực tế:** Một tổ chức đang triển khai hệ thống dữ liệu muốn kiểm tra nghịch đảo. Bộ dữ liệu đang có: Ma trận chéo 2×2. Hãy lập trình giải quyết yêu cầu này và đưa ra kết quả có thể kiểm tra.

**Vì sao chọn phương án?** Tích A@inv(A) phải gần đơn vị; điều kiện tiên quyết là dữ liệu có shape và ý nghĩa từng giá trị rõ ràng.


**Quy trình:** mô tả dữ liệu → xác định phép tính/shape → tính bằng Python → kiểm tra kết quả.

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

**Tình huống thực tế:** Một tổ chức đang triển khai hệ thống dữ liệu muốn kiểm tra shape trước nhân. Bộ dữ liệu đang có: A (2×3), B (3×2). Hãy lập trình giải quyết yêu cầu này và đưa ra kết quả có thể kiểm tra.

**Vì sao chọn phương án?** Shape không phù hợp sẽ báo lỗi nên kiểm trước; điều kiện tiên quyết là dữ liệu có shape và ý nghĩa từng giá trị rõ ràng.


**Quy trình:** mô tả dữ liệu → xác định phép tính/shape → tính bằng Python → kiểm tra kết quả.

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


## 6. Sai lầm cần tránh

Phân biệt vector một chiều với ma trận hai chiều, tránh nhân ma trận sai shape; covariance và eigenvalue không phải độ chính xác mô hình. Các ví dụ số không có ý nghĩa dự đoán nếu thiếu bước đánh giá.

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
