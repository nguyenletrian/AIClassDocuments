# PY-24 — Scalar, vector, norm, đơn vị và dot product

## 1. Vị trí trong chuỗi kiến thức

`NumPy → Scalar/Vector → Matrix → PCA`

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích |
|---|---|---|
| Scalar | đại lượng vô hướng | Một số đơn lẻ có thể đo độ lớn |
| Vector | véc-tơ | Dãy số mô tả nhiều thành phần của một đối tượng |
| Norm | độ lớn véc-tơ | Độ dài theo chuẩn đã chọn |
| Dot product | tích vô hướng | Nhân từng cặp tọa độ tương ứng rồi cộng |

## 3. NumPy và các hàm liên quan

| Hàm / tham số | Dùng làm gì |
|---|---|
| `np.array([...],dtype=float)` | Tạo véc-tơ kiểu thực khi phép tính tạo phần thập phân |
| `np.linalg.norm(v)` | Độ lớn Euclidean của véc-tơ |
| `v/np.linalg.norm(v)` | Chuẩn hóa về độ dài 1, phải tránh norm bằng 0 |
| `a @ b / np.dot(a,b)` | Tích vô hướng nếu hai vector một chiều cùng độ dài |

## 4. Khái niệm kèm ví dụ nhỏ

### 4.1. Scalar

Một số đơn lẻ có thể đo độ lớn.

```python
rate=2.5
print(rate)
```

### 4.2. Vector

Dãy số mô tả nhiều thành phần của một đối tượng.

```python
import numpy as np
print(np.array([3,4]))
```

### 4.3. Norm

Độ dài theo chuẩn đã chọn.

```python
import numpy as np
print(np.linalg.norm([3,4]))
```

### 4.4. Dot product

Nhân từng cặp tọa độ tương ứng rồi cộng.

```python
import numpy as np
print(np.dot([1,2],[3,4]))
```

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Tính khoảng cách 2D

**Vấn đề:** Tính khoảng cách 2D.

**Vì sao chọn phương án?** Norm từ véc-tơ độ lệch giúp tính khoảng cách đến gốc

**Dữ liệu:** Vị trí điểm [3,4] mét.

```python
import numpy as np
v=np.array([3,4],dtype=float)
print(np.linalg.norm(v))
```

### Tình huống 2 — Chuẩn hóa hướng di chuyển

**Vấn đề:** Chuẩn hóa hướng di chuyển.

**Vì sao chọn phương án?** Chia norm giúp hướng có độ dài 1 trước điều khiển tốc độ

**Dữ liệu:** Véc-tơ [3,4] mét.

```python
import numpy as np
v=np.array([3.,4.]);norm=np.linalg.norm(v)
u=v/norm if norm else v
print(u)
```

### Tình huống 3 — Điểm tổng kết có trọng số

**Vấn đề:** Điểm tổng kết có trọng số.

**Vì sao chọn phương án?** Dot product của điểm và trọng số tạo điểm tổng

**Dữ liệu:** Điểm 8 7 9; trọng số 0.2,0.3,0.5.

```python
import numpy as np
scores=np.array([8,7,9]);weights=np.array([.2,.3,.5])
print(scores@weights)
```

### Tình huống 4 — Tìm hai hướng vuông góc

**Vấn đề:** Tìm hai hướng vuông góc.

**Vì sao chọn phương án?** Dot bằng 0 cho hai vector khác 0 biểu thị trực giao

**Dữ liệu:** a=[1,0], b=[0,1].

```python
import numpy as np
a=np.array([1,0]);b=np.array([0,1])
print(a@b)
```

### Tình huống 5 — Tính sai khác cảm biến

**Vấn đề:** Tính sai khác cảm biến.

**Vì sao chọn phương án?** Norm của hiệu vector đo mức sai khác tổng hợp

**Dữ liệu:** Hai kênh cảm biến trên cùng đơn vị.

```python
import numpy as np
a=np.array([20,30]);b=np.array([23,34])
print(np.linalg.norm(a-b))
```

## 6. Sai lầm cần tránh

Phân biệt vector một chiều với ma trận hai chiều, tránh nhân ma trận sai shape; covariance và eigenvalue không phải độ chính xác mô hình. Các ví dụ số không có ý nghĩa dự đoán nếu thiếu bước đánh giá.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ


**Q1. What is Scalar? — Thuật ngữ Scalar có nghĩa gì?**

A. It instead means Dãy số mô tả nhiều thành phần của một đối tượng — Dãy số mô tả nhiều thành phần của một đối tượng

B. It means Một số đơn lẻ có thể đo độ lớn — Một số đơn lẻ có thể đo độ lớn

C. It instead means Độ dài theo chuẩn đã chọn — Độ dài theo chuẩn đã chọn

D. It instead means Nhân từng cặp tọa độ tương ứng rồi cộng — Nhân từng cặp tọa độ tương ứng rồi cộng


**Q2. What is Vector? — Thuật ngữ Vector có nghĩa gì?**

A. It means Dãy số mô tả nhiều thành phần của một đối tượng — Dãy số mô tả nhiều thành phần của một đối tượng

B. It instead means Độ dài theo chuẩn đã chọn — Độ dài theo chuẩn đã chọn

C. It instead means Nhân từng cặp tọa độ tương ứng rồi cộng — Nhân từng cặp tọa độ tương ứng rồi cộng

D. It instead means Một số đơn lẻ có thể đo độ lớn — Một số đơn lẻ có thể đo độ lớn


**Q3. What is Norm? — Thuật ngữ Norm có nghĩa gì?**

A. It instead means Nhân từng cặp tọa độ tương ứng rồi cộng — Nhân từng cặp tọa độ tương ứng rồi cộng

B. It instead means Một số đơn lẻ có thể đo độ lớn — Một số đơn lẻ có thể đo độ lớn

C. It instead means Dãy số mô tả nhiều thành phần của một đối tượng — Dãy số mô tả nhiều thành phần của một đối tượng

D. It means Độ dài theo chuẩn đã chọn — Độ dài theo chuẩn đã chọn


**Q4. What is Dot product? — Thuật ngữ Dot product có nghĩa gì?**

A. It instead means Một số đơn lẻ có thể đo độ lớn — Một số đơn lẻ có thể đo độ lớn

B. It instead means Dãy số mô tả nhiều thành phần của một đối tượng — Dãy số mô tả nhiều thành phần của một đối tượng

C. It means Nhân từng cặp tọa độ tương ứng rồi cộng — Nhân từng cặp tọa độ tương ứng rồi cộng

D. It instead means Độ dài theo chuẩn đã chọn — Độ dài theo chuẩn đã chọn


**Q5. What does np.array([...],dtype=float) help with? — Hàm np.array([...],dtype=float) giúp làm gì?**

A. Another function helps to Độ lớn Euclidean của véc-tơ — Độ lớn Euclidean của véc-tơ

B. It helps to Tạo véc-tơ kiểu thực khi phép tính tạo phần thập phân — Tạo véc-tơ kiểu thực khi phép tính tạo phần thập phân

C. Another function helps to Chuẩn hóa về độ dài 1, phải tránh norm bằng 0 — Chuẩn hóa về độ dài 1, phải tránh norm bằng 0

D. Another function helps to Tích vô hướng nếu hai vector một chiều cùng độ dài — Tích vô hướng nếu hai vector một chiều cùng độ dài


**Q6. What does np.linalg.norm(v) help with? — Hàm np.linalg.norm(v) giúp làm gì?**

A. It helps to Độ lớn Euclidean của véc-tơ — Độ lớn Euclidean của véc-tơ

B. Another function helps to Chuẩn hóa về độ dài 1, phải tránh norm bằng 0 — Chuẩn hóa về độ dài 1, phải tránh norm bằng 0

C. Another function helps to Tích vô hướng nếu hai vector một chiều cùng độ dài — Tích vô hướng nếu hai vector một chiều cùng độ dài

D. Another function helps to Tạo véc-tơ kiểu thực khi phép tính tạo phần thập phân — Tạo véc-tơ kiểu thực khi phép tính tạo phần thập phân


**Q7. What does v/np.linalg.norm(v) help with? — Hàm v/np.linalg.norm(v) giúp làm gì?**

A. Another function helps to Tích vô hướng nếu hai vector một chiều cùng độ dài — Tích vô hướng nếu hai vector một chiều cùng độ dài

B. Another function helps to Tạo véc-tơ kiểu thực khi phép tính tạo phần thập phân — Tạo véc-tơ kiểu thực khi phép tính tạo phần thập phân

C. Another function helps to Độ lớn Euclidean của véc-tơ — Độ lớn Euclidean của véc-tơ

D. It helps to Chuẩn hóa về độ dài 1, phải tránh norm bằng 0 — Chuẩn hóa về độ dài 1, phải tránh norm bằng 0


**Q8. What does a @ b / np.dot(a,b) help with? — Hàm a @ b / np.dot(a,b) giúp làm gì?**

A. Another function helps to Tạo véc-tơ kiểu thực khi phép tính tạo phần thập phân — Tạo véc-tơ kiểu thực khi phép tính tạo phần thập phân

B. Another function helps to Độ lớn Euclidean của véc-tơ — Độ lớn Euclidean của véc-tơ

C. It helps to Tích vô hướng nếu hai vector một chiều cùng độ dài — Tích vô hướng nếu hai vector một chiều cùng độ dài

D. Another function helps to Chuẩn hóa về độ dài 1, phải tránh norm bằng 0 — Chuẩn hóa về độ dài 1, phải tránh norm bằng 0


**Q9. Why choose this method for scenario 1? — Vì sao chọn cách làm tình huống 1?**

A. Chia norm giúp hướng có độ dài 1 trước điều khiển tốc độ — Chia norm giúp hướng có độ dài 1 trước điều khiển tốc độ

B. Norm từ véc-tơ độ lệch giúp tính khoảng cách đến gốc — Norm từ véc-tơ độ lệch giúp tính khoảng cách đến gốc

C. Dot product của điểm và trọng số tạo điểm tổng — Dot product của điểm và trọng số tạo điểm tổng

D. Dot bằng 0 cho hai vector khác 0 biểu thị trực giao — Dot bằng 0 cho hai vector khác 0 biểu thị trực giao


**Q10. Why choose this method for scenario 2? — Vì sao chọn cách làm tình huống 2?**

A. Chia norm giúp hướng có độ dài 1 trước điều khiển tốc độ — Chia norm giúp hướng có độ dài 1 trước điều khiển tốc độ

B. Dot product của điểm và trọng số tạo điểm tổng — Dot product của điểm và trọng số tạo điểm tổng

C. Dot bằng 0 cho hai vector khác 0 biểu thị trực giao — Dot bằng 0 cho hai vector khác 0 biểu thị trực giao

D. Norm của hiệu vector đo mức sai khác tổng hợp — Norm của hiệu vector đo mức sai khác tổng hợp


**Q11. Why choose this method for scenario 3? — Vì sao chọn cách làm tình huống 3?**

A. Dot bằng 0 cho hai vector khác 0 biểu thị trực giao — Dot bằng 0 cho hai vector khác 0 biểu thị trực giao

B. Norm của hiệu vector đo mức sai khác tổng hợp — Norm của hiệu vector đo mức sai khác tổng hợp

C. Norm từ véc-tơ độ lệch giúp tính khoảng cách đến gốc — Norm từ véc-tơ độ lệch giúp tính khoảng cách đến gốc

D. Dot product của điểm và trọng số tạo điểm tổng — Dot product của điểm và trọng số tạo điểm tổng


**Q12. Why choose this method for scenario 4? — Vì sao chọn cách làm tình huống 4?**

A. Norm của hiệu vector đo mức sai khác tổng hợp — Norm của hiệu vector đo mức sai khác tổng hợp

B. Norm từ véc-tơ độ lệch giúp tính khoảng cách đến gốc — Norm từ véc-tơ độ lệch giúp tính khoảng cách đến gốc

C. Dot bằng 0 cho hai vector khác 0 biểu thị trực giao — Dot bằng 0 cho hai vector khác 0 biểu thị trực giao

D. Chia norm giúp hướng có độ dài 1 trước điều khiển tốc độ — Chia norm giúp hướng có độ dài 1 trước điều khiển tốc độ


**Q13. Why choose this method for scenario 5? — Vì sao chọn cách làm tình huống 5?**

A. Norm từ véc-tơ độ lệch giúp tính khoảng cách đến gốc — Norm từ véc-tơ độ lệch giúp tính khoảng cách đến gốc

B. Norm của hiệu vector đo mức sai khác tổng hợp — Norm của hiệu vector đo mức sai khác tổng hợp

C. Chia norm giúp hướng có độ dài 1 trước điều khiển tốc độ — Chia norm giúp hướng có độ dài 1 trước điều khiển tốc độ

D. Dot product của điểm và trọng số tạo điểm tổng — Dot product của điểm và trọng số tạo điểm tổng


**Q14. What input is relevant to scenario 1? — Dữ liệu nào của tình huống 1?**

A. The input is Vị trí điểm [3,4] mét — Vị trí điểm [3,4] mét

B. Different data: Véc-tơ [3,4] mét — Véc-tơ [3,4] mét

C. Different data: Điểm 8 7 9; trọng số 0.2,0.3,0.5 — Điểm 8 7 9; trọng số 0.2,0.3,0.5

D. Different data: a=[1,0], b=[0,1] — a=[1,0], b=[0,1]


**Q15. What input is relevant to scenario 2? — Dữ liệu nào của tình huống 2?**

A. Different data: Điểm 8 7 9; trọng số 0.2,0.3,0.5 — Điểm 8 7 9; trọng số 0.2,0.3,0.5

B. Different data: a=[1,0], b=[0,1] — a=[1,0], b=[0,1]

C. Different data: Hai kênh cảm biến trên cùng đơn vị — Hai kênh cảm biến trên cùng đơn vị

D. The input is Véc-tơ [3,4] mét — Véc-tơ [3,4] mét


**Q16. What input is relevant to scenario 3? — Dữ liệu nào của tình huống 3?**

A. Different data: a=[1,0], b=[0,1] — a=[1,0], b=[0,1]

B. Different data: Hai kênh cảm biến trên cùng đơn vị — Hai kênh cảm biến trên cùng đơn vị

C. The input is Điểm 8 7 9; trọng số 0.2,0.3,0.5 — Điểm 8 7 9; trọng số 0.2,0.3,0.5

D. Different data: Vị trí điểm [3,4] mét — Vị trí điểm [3,4] mét


**Q17. What input is relevant to scenario 4? — Dữ liệu nào của tình huống 4?**

A. Different data: Hai kênh cảm biến trên cùng đơn vị — Hai kênh cảm biến trên cùng đơn vị

B. The input is a=[1,0], b=[0,1] — a=[1,0], b=[0,1]

C. Different data: Vị trí điểm [3,4] mét — Vị trí điểm [3,4] mét

D. Different data: Véc-tơ [3,4] mét — Véc-tơ [3,4] mét


**Q18. What input is relevant to scenario 5? — Dữ liệu nào của tình huống 5?**

A. The input is Hai kênh cảm biến trên cùng đơn vị — Hai kênh cảm biến trên cùng đơn vị

B. Different data: Vị trí điểm [3,4] mét — Vị trí điểm [3,4] mét

C. Different data: Véc-tơ [3,4] mét — Véc-tơ [3,4] mét

D. Different data: Điểm 8 7 9; trọng số 0.2,0.3,0.5 — Điểm 8 7 9; trọng số 0.2,0.3,0.5


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
| Q1 | **B** | It means Một số đơn lẻ có thể đo độ lớn | Một số đơn lẻ có thể đo độ lớn |
| Q2 | **A** | It means Dãy số mô tả nhiều thành phần của một đối tượng | Dãy số mô tả nhiều thành phần của một đối tượng |
| Q3 | **D** | It means Độ dài theo chuẩn đã chọn | Độ dài theo chuẩn đã chọn |
| Q4 | **C** | It means Nhân từng cặp tọa độ tương ứng rồi cộng | Nhân từng cặp tọa độ tương ứng rồi cộng |
| Q5 | **B** | It helps to Tạo véc-tơ kiểu thực khi phép tính tạo phần thập phân | Tạo véc-tơ kiểu thực khi phép tính tạo phần thập phân |
| Q6 | **A** | It helps to Độ lớn Euclidean của véc-tơ | Độ lớn Euclidean của véc-tơ |
| Q7 | **D** | It helps to Chuẩn hóa về độ dài 1, phải tránh norm bằng 0 | Chuẩn hóa về độ dài 1, phải tránh norm bằng 0 |
| Q8 | **C** | It helps to Tích vô hướng nếu hai vector một chiều cùng độ dài | Tích vô hướng nếu hai vector một chiều cùng độ dài |
| Q9 | **B** | Norm từ véc-tơ độ lệch giúp tính khoảng cách đến gốc | Norm từ véc-tơ độ lệch giúp tính khoảng cách đến gốc |
| Q10 | **A** | Chia norm giúp hướng có độ dài 1 trước điều khiển tốc độ | Chia norm giúp hướng có độ dài 1 trước điều khiển tốc độ |
| Q11 | **D** | Dot product của điểm và trọng số tạo điểm tổng | Dot product của điểm và trọng số tạo điểm tổng |
| Q12 | **C** | Dot bằng 0 cho hai vector khác 0 biểu thị trực giao | Dot bằng 0 cho hai vector khác 0 biểu thị trực giao |
| Q13 | **B** | Norm của hiệu vector đo mức sai khác tổng hợp | Norm của hiệu vector đo mức sai khác tổng hợp |
| Q14 | **A** | The input is Vị trí điểm [3,4] mét | Vị trí điểm [3,4] mét |
| Q15 | **D** | The input is Véc-tơ [3,4] mét | Véc-tơ [3,4] mét |
| Q16 | **C** | The input is Điểm 8 7 9; trọng số 0.2,0.3,0.5 | Điểm 8 7 9; trọng số 0.2,0.3,0.5 |
| Q17 | **B** | The input is a=[1,0], b=[0,1] | a=[1,0], b=[0,1] |
| Q18 | **A** | The input is Hai kênh cảm biến trên cùng đơn vị | Hai kênh cảm biến trên cùng đơn vị |
| Q19 | **D** | Shapes and data units | Shape và đơn vị dữ liệu |
| Q20 | **C** | It does not establish predictive performance | Nó không đo chất lượng dự đoán |
