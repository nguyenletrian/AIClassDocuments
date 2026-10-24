# PY-27 — Eigenvalue, Eigenvector và hướng biến thiên


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Eigenvector** — vector riêng; **Eigenvalue** — giá trị riêng.

`Hệ tuyến tính → Eigenvalues/Vectors → Covariance → PCA`

Nắm liên hệ giữa cấu trúc toán học và mảng dữ liệu Python trước khi sử dụng vào học máy.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích |
|---|---|---|
| Eigenvector | vector riêng | Hướng mà phép biến đổi tuyến tính chỉ co/dãn |
| Eigenvalue | giá trị riêng | Hệ số co/dãn theo một vector riêng |
| Covariance | hiệp phương sai | Cách hai đặc trưng biến thiên cùng nhau |
| Principal direction | hướng chính | Hướng chứa nhiều phương sai nhất trong PCA |

## 3. NumPy và các hàm liên quan

**Từ vựng trong mục:** **Function** — hàm; **Shape** — kích thước mảng.

| Hàm / tham số | Dùng làm gì |
|---|---|
| `np.linalg.eigh(C)` | Trả eigenvalues/eigenvectors cho ma trận đối xứng |
| `np.linalg.eigvalsh(C)` | Chỉ trả eigenvalues của ma trận đối xứng |
| `np.cov(X,rowvar=False)` | Cột là feature, hàng là mẫu khi tính covariance |
| `np.argsort(values)[::-1]` | Sắp eigenvalue giảm dần để chọn hướng lớn |

## 4. Khái niệm liên quan

### 4.1. Eigenvector

**Từ vựng trong mục:** **Eigenvector** — vector riêng.

Hướng mà phép biến đổi tuyến tính chỉ co/dãn. Trước khi sử dụng biểu thức hãy xem phần tử, hàng/cột và đơn vị đầu vào.

```python
import numpy as np
w,v=np.linalg.eigh([[2.,0.],[0.,3.]])
print(v.shape)
```

**Kết quả khi chạy:**

```text
(2, 2)
```

**Tự kiểm tra:** Eigenvector có nghĩa gì? **Đáp án:** Hướng mà phép biến đổi tuyến tính chỉ co/dãn.

### 4.2. Eigenvalue

**Từ vựng trong mục:** **Eigenvalue** — giá trị riêng.

Hệ số co/dãn theo một vector riêng. Trước khi sử dụng biểu thức hãy xem phần tử, hàng/cột và đơn vị đầu vào.

```python
import numpy as np
print(np.linalg.eigvalsh([[2.,0.],[0.,3.]]))
```

**Kết quả khi chạy:**

```text
[2. 3.]
```

**Tự kiểm tra:** Eigenvalue có nghĩa gì? **Đáp án:** Hệ số co/dãn theo một vector riêng.

### 4.3. Covariance

**Từ vựng trong mục:** **Covariance** — hiệp phương sai.

Cách hai đặc trưng biến thiên cùng nhau. Trước khi sử dụng biểu thức hãy xem phần tử, hàng/cột và đơn vị đầu vào.

```python
import numpy as np
X=np.array([[1,2],[2,4],[3,6]])
print(np.cov(X,rowvar=False))
```

**Kết quả khi chạy:**

```text
[[1. 2.]
 [2. 4.]]
```

**Tự kiểm tra:** Covariance có nghĩa gì? **Đáp án:** Cách hai đặc trưng biến thiên cùng nhau.

### 4.4. Principal direction

**Từ vựng trong mục:** **Principal direction** — hướng chính.

Hướng chứa nhiều phương sai nhất trong PCA. Trước khi sử dụng biểu thức hãy xem phần tử, hàng/cột và đơn vị đầu vào.

```python
import numpy as np
w,v=np.linalg.eigh([[2.,0.],[0.,3.]])
print(v[:,-1])
```

**Kết quả khi chạy:**

```text
[0. 1.]
```

**Tự kiểm tra:** Principal direction có nghĩa gì? **Đáp án:** Hướng chứa nhiều phương sai nhất trong PCA.

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Chọn hướng đo biến thiên lớn

**Từ vựng trong mục:** **Eigenvector** — vector riêng.

**Tình huống thực tế:** Một hệ thống giám sát muốn chọn hướng đo biến thiên lớn. Bộ dữ liệu đang có: Covariance minh họa chéo [2,3]. Hãy lập trình giải quyết yêu cầu này và đưa ra kết quả có thể kiểm tra.

**Vì sao chọn phương án?** Chọn eigenvector tương ứng eigenvalue lớn nhất; điều kiện tiên quyết là dữ liệu có shape và ý nghĩa từng giá trị rõ ràng.


**Quy trình:** mô tả dữ liệu → xác định phép tính/shape → tính bằng Python → kiểm tra kết quả.

```python
import numpy as np
C=np.diag([2.,3.])
w,v=np.linalg.eigh(C)
print(w[-1],v[:,-1])
```

**Kết quả khi chạy:**

```text
3.0 [0. 1.]
```


### Tình huống 2 — Xem dữ liệu có trùng tuyến tính

**Từ vựng trong mục:** **Eigenvalue** — giá trị riêng.

**Tình huống thực tế:** Một tổ chức đang triển khai hệ thống dữ liệu muốn xem dữ liệu có trùng tuyến tính. Bộ dữ liệu đang có: Ba điểm cùng tăng hai feature. Hãy lập trình giải quyết yêu cầu này và đưa ra kết quả có thể kiểm tra.

**Vì sao chọn phương án?** Eigenvalue gần 0 biểu thị hướng rất ít biến thiên; điều kiện tiên quyết là dữ liệu có shape và ý nghĩa từng giá trị rõ ràng.


**Quy trình:** mô tả dữ liệu → xác định phép tính/shape → tính bằng Python → kiểm tra kết quả.

```python
import numpy as np
X=np.array([[1,2],[2,4],[3,6]],dtype=float)
print(np.linalg.eigvalsh(np.cov(X,rowvar=False)))
```

**Kết quả khi chạy:**

```text
[0. 5.]
```


### Tình huống 3 — Kiểm công thức eigen

**Từ vựng trong mục:** **Covariance** — hiệp phương sai.

**Tình huống thực tế:** Một tổ chức đang triển khai hệ thống dữ liệu muốn kiểm công thức eigen. Bộ dữ liệu đang có: Ma trận chéo 2×2. Hãy lập trình giải quyết yêu cầu này và đưa ra kết quả có thể kiểm tra.

**Vì sao chọn phương án?** A@v gần lambda*v cho cặp riêng chính xác; điều kiện tiên quyết là dữ liệu có shape và ý nghĩa từng giá trị rõ ràng.


**Quy trình:** mô tả dữ liệu → xác định phép tính/shape → tính bằng Python → kiểm tra kết quả.

```python
import numpy as np
A=np.diag([2.,3.])
w,v=np.linalg.eigh(A)
print(np.allclose(A@v[:,-1],w[-1]*v[:,-1]))
```

**Kết quả khi chạy:**

```text
True
```


### Tình huống 4 — Sắp thứ tự mức phương sai

**Từ vựng trong mục:** **Principal direction** — hướng chính.

**Tình huống thực tế:** Một tổ chức đang triển khai hệ thống dữ liệu muốn sắp thứ tự mức phương sai. Bộ dữ liệu đang có: Giá trị riêng [4,1,3]. Hãy lập trình giải quyết yêu cầu này và đưa ra kết quả có thể kiểm tra.

**Vì sao chọn phương án?** argsort chọn eigenvalue lớn trước thay vì mặc định nhỏ; điều kiện tiên quyết là dữ liệu có shape và ý nghĩa từng giá trị rõ ràng.


**Quy trình:** mô tả dữ liệu → xác định phép tính/shape → tính bằng Python → kiểm tra kết quả.

```python
import numpy as np
values=np.array([4,1,3])
print(np.argsort(values)[::-1])
```

**Kết quả khi chạy:**

```text
[0 2 1]
```


### Tình huống 5 — So với PCA của sklearn

**Từ vựng trong mục:** **Eigenvector** — vector riêng.

**Tình huống thực tế:** Một tổ chức đang triển khai hệ thống dữ liệu muốn so với PCA của sklearn. Bộ dữ liệu đang có: 3 khách × 2 feature. Hãy lập trình giải quyết yêu cầu này và đưa ra kết quả có thể kiểm tra.

**Vì sao chọn phương án?** Hai PC giảm dữ liệu ba hàng và hai cột thành một chiều; điều kiện tiên quyết là dữ liệu có shape và ý nghĩa từng giá trị rõ ràng.


**Quy trình:** mô tả dữ liệu → xác định phép tính/shape → tính bằng Python → kiểm tra kết quả.

```python
import numpy as np
from sklearn.decomposition import PCA
X=np.array([[1,2],[2,3],[3,4]],dtype=float)
print(PCA(n_components=1).fit_transform(X).shape)
```

**Kết quả khi chạy:**

```text
(3, 1)
```


## 6. Sai lầm cần tránh

Phân biệt vector một chiều với ma trận hai chiều, tránh nhân ma trận sai shape; covariance và eigenvalue không phải độ chính xác mô hình. Các ví dụ số không có ý nghĩa dự đoán nếu thiếu bước đánh giá.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.


**Q1. What is Eigenvector? — Thuật ngữ Eigenvector có nghĩa gì?**

A. It instead means Hệ số co/dãn theo một vector riêng — Hệ số co/dãn theo một vector riêng

B. It means Hướng mà phép biến đổi tuyến tính chỉ co/dãn — Hướng mà phép biến đổi tuyến tính chỉ co/dãn

C. It instead means Cách hai đặc trưng biến thiên cùng nhau — Cách hai đặc trưng biến thiên cùng nhau

D. It instead means Hướng chứa nhiều phương sai nhất trong PCA — Hướng chứa nhiều phương sai nhất trong PCA


**Q2. What is Eigenvalue? — Thuật ngữ Eigenvalue có nghĩa gì?**

A. It means Hệ số co/dãn theo một vector riêng — Hệ số co/dãn theo một vector riêng

B. It instead means Cách hai đặc trưng biến thiên cùng nhau — Cách hai đặc trưng biến thiên cùng nhau

C. It instead means Hướng chứa nhiều phương sai nhất trong PCA — Hướng chứa nhiều phương sai nhất trong PCA

D. It instead means Hướng mà phép biến đổi tuyến tính chỉ co/dãn — Hướng mà phép biến đổi tuyến tính chỉ co/dãn


**Q3. What is Covariance? — Thuật ngữ Covariance có nghĩa gì?**

A. It instead means Hướng chứa nhiều phương sai nhất trong PCA — Hướng chứa nhiều phương sai nhất trong PCA

B. It instead means Hướng mà phép biến đổi tuyến tính chỉ co/dãn — Hướng mà phép biến đổi tuyến tính chỉ co/dãn

C. It instead means Hệ số co/dãn theo một vector riêng — Hệ số co/dãn theo một vector riêng

D. It means Cách hai đặc trưng biến thiên cùng nhau — Cách hai đặc trưng biến thiên cùng nhau


**Q4. What is Principal direction? — Thuật ngữ Principal direction có nghĩa gì?**

A. It instead means Hướng mà phép biến đổi tuyến tính chỉ co/dãn — Hướng mà phép biến đổi tuyến tính chỉ co/dãn

B. It instead means Hệ số co/dãn theo một vector riêng — Hệ số co/dãn theo một vector riêng

C. It means Hướng chứa nhiều phương sai nhất trong PCA — Hướng chứa nhiều phương sai nhất trong PCA

D. It instead means Cách hai đặc trưng biến thiên cùng nhau — Cách hai đặc trưng biến thiên cùng nhau


**Q5. What does np.linalg.eigh(C) help with? — Hàm np.linalg.eigh(C) giúp làm gì?**

A. Another function helps to Chỉ trả eigenvalues của ma trận đối xứng — Chỉ trả eigenvalues của ma trận đối xứng

B. It helps to Trả eigenvalues/eigenvectors cho ma trận đối xứng — Trả eigenvalues/eigenvectors cho ma trận đối xứng

C. Another function helps to Cột là feature, hàng là mẫu khi tính covariance — Cột là feature, hàng là mẫu khi tính covariance

D. Another function helps to Sắp eigenvalue giảm dần để chọn hướng lớn — Sắp eigenvalue giảm dần để chọn hướng lớn


**Q6. What does np.linalg.eigvalsh(C) help with? — Hàm np.linalg.eigvalsh(C) giúp làm gì?**

A. It helps to Chỉ trả eigenvalues của ma trận đối xứng — Chỉ trả eigenvalues của ma trận đối xứng

B. Another function helps to Cột là feature, hàng là mẫu khi tính covariance — Cột là feature, hàng là mẫu khi tính covariance

C. Another function helps to Sắp eigenvalue giảm dần để chọn hướng lớn — Sắp eigenvalue giảm dần để chọn hướng lớn

D. Another function helps to Trả eigenvalues/eigenvectors cho ma trận đối xứng — Trả eigenvalues/eigenvectors cho ma trận đối xứng


**Q7. What does np.cov(X,rowvar=False) help with? — Hàm np.cov(X,rowvar=False) giúp làm gì?**

A. Another function helps to Sắp eigenvalue giảm dần để chọn hướng lớn — Sắp eigenvalue giảm dần để chọn hướng lớn

B. Another function helps to Trả eigenvalues/eigenvectors cho ma trận đối xứng — Trả eigenvalues/eigenvectors cho ma trận đối xứng

C. Another function helps to Chỉ trả eigenvalues của ma trận đối xứng — Chỉ trả eigenvalues của ma trận đối xứng

D. It helps to Cột là feature, hàng là mẫu khi tính covariance — Cột là feature, hàng là mẫu khi tính covariance


**Q8. What does np.argsort(values)[::-1] help with? — Hàm np.argsort(values)[::-1] giúp làm gì?**

A. Another function helps to Trả eigenvalues/eigenvectors cho ma trận đối xứng — Trả eigenvalues/eigenvectors cho ma trận đối xứng

B. Another function helps to Chỉ trả eigenvalues của ma trận đối xứng — Chỉ trả eigenvalues của ma trận đối xứng

C. It helps to Sắp eigenvalue giảm dần để chọn hướng lớn — Sắp eigenvalue giảm dần để chọn hướng lớn

D. Another function helps to Cột là feature, hàng là mẫu khi tính covariance — Cột là feature, hàng là mẫu khi tính covariance


**Q9. Why choose this method for scenario 1? — Vì sao chọn cách làm tình huống 1?**

A. Eigenvalue gần 0 biểu thị hướng rất ít biến thiên — Eigenvalue gần 0 biểu thị hướng rất ít biến thiên

B. Chọn eigenvector tương ứng eigenvalue lớn nhất — Chọn eigenvector tương ứng eigenvalue lớn nhất

C. A@v gần lambda*v cho cặp riêng chính xác — A@v gần lambda*v cho cặp riêng chính xác

D. argsort chọn eigenvalue lớn trước thay vì mặc định nhỏ — argsort chọn eigenvalue lớn trước thay vì mặc định nhỏ


**Q10. Why choose this method for scenario 2? — Vì sao chọn cách làm tình huống 2?**

A. Eigenvalue gần 0 biểu thị hướng rất ít biến thiên — Eigenvalue gần 0 biểu thị hướng rất ít biến thiên

B. A@v gần lambda*v cho cặp riêng chính xác — A@v gần lambda*v cho cặp riêng chính xác

C. argsort chọn eigenvalue lớn trước thay vì mặc định nhỏ — argsort chọn eigenvalue lớn trước thay vì mặc định nhỏ

D. Hai PC giảm dữ liệu ba hàng và hai cột thành một chiều — Hai PC giảm dữ liệu ba hàng và hai cột thành một chiều


**Q11. Why choose this method for scenario 3? — Vì sao chọn cách làm tình huống 3?**

A. argsort chọn eigenvalue lớn trước thay vì mặc định nhỏ — argsort chọn eigenvalue lớn trước thay vì mặc định nhỏ

B. Hai PC giảm dữ liệu ba hàng và hai cột thành một chiều — Hai PC giảm dữ liệu ba hàng và hai cột thành một chiều

C. Chọn eigenvector tương ứng eigenvalue lớn nhất — Chọn eigenvector tương ứng eigenvalue lớn nhất

D. A@v gần lambda*v cho cặp riêng chính xác — A@v gần lambda*v cho cặp riêng chính xác


**Q12. Why choose this method for scenario 4? — Vì sao chọn cách làm tình huống 4?**

A. Hai PC giảm dữ liệu ba hàng và hai cột thành một chiều — Hai PC giảm dữ liệu ba hàng và hai cột thành một chiều

B. Chọn eigenvector tương ứng eigenvalue lớn nhất — Chọn eigenvector tương ứng eigenvalue lớn nhất

C. argsort chọn eigenvalue lớn trước thay vì mặc định nhỏ — argsort chọn eigenvalue lớn trước thay vì mặc định nhỏ

D. Eigenvalue gần 0 biểu thị hướng rất ít biến thiên — Eigenvalue gần 0 biểu thị hướng rất ít biến thiên


**Q13. Why choose this method for scenario 5? — Vì sao chọn cách làm tình huống 5?**

A. Chọn eigenvector tương ứng eigenvalue lớn nhất — Chọn eigenvector tương ứng eigenvalue lớn nhất

B. Hai PC giảm dữ liệu ba hàng và hai cột thành một chiều — Hai PC giảm dữ liệu ba hàng và hai cột thành một chiều

C. Eigenvalue gần 0 biểu thị hướng rất ít biến thiên — Eigenvalue gần 0 biểu thị hướng rất ít biến thiên

D. A@v gần lambda*v cho cặp riêng chính xác — A@v gần lambda*v cho cặp riêng chính xác


**Q14. What input is relevant to scenario 1? — Dữ liệu nào của tình huống 1?**

A. The input is Covariance minh họa chéo [2,3] — Covariance minh họa chéo [2,3]

B. Different data: Ba điểm cùng tăng hai feature — Ba điểm cùng tăng hai feature

C. Different data: Ma trận chéo 2×2 — Ma trận chéo 2×2

D. Different data: Giá trị riêng [4,1,3] — Giá trị riêng [4,1,3]


**Q15. What input is relevant to scenario 2? — Dữ liệu nào của tình huống 2?**

A. Different data: Ma trận chéo 2×2 — Ma trận chéo 2×2

B. Different data: Giá trị riêng [4,1,3] — Giá trị riêng [4,1,3]

C. Different data: 3 khách × 2 feature — 3 khách × 2 feature

D. The input is Ba điểm cùng tăng hai feature — Ba điểm cùng tăng hai feature


**Q16. What input is relevant to scenario 3? — Dữ liệu nào của tình huống 3?**

A. Different data: Giá trị riêng [4,1,3] — Giá trị riêng [4,1,3]

B. Different data: 3 khách × 2 feature — 3 khách × 2 feature

C. The input is Ma trận chéo 2×2 — Ma trận chéo 2×2

D. Different data: Covariance minh họa chéo [2,3] — Covariance minh họa chéo [2,3]


**Q17. What input is relevant to scenario 4? — Dữ liệu nào của tình huống 4?**

A. Different data: 3 khách × 2 feature — 3 khách × 2 feature

B. The input is Giá trị riêng [4,1,3] — Giá trị riêng [4,1,3]

C. Different data: Covariance minh họa chéo [2,3] — Covariance minh họa chéo [2,3]

D. Different data: Ba điểm cùng tăng hai feature — Ba điểm cùng tăng hai feature


**Q18. What input is relevant to scenario 5? — Dữ liệu nào của tình huống 5?**

A. The input is 3 khách × 2 feature — 3 khách × 2 feature

B. Different data: Covariance minh họa chéo [2,3] — Covariance minh họa chéo [2,3]

C. Different data: Ba điểm cùng tăng hai feature — Ba điểm cùng tăng hai feature

D. Different data: Ma trận chéo 2×2 — Ma trận chéo 2×2


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
| Q1 | **B** | It means Hướng mà phép biến đổi tuyến tính chỉ co/dãn | Hướng mà phép biến đổi tuyến tính chỉ co/dãn |
| Q2 | **A** | It means Hệ số co/dãn theo một vector riêng | Hệ số co/dãn theo một vector riêng |
| Q3 | **D** | It means Cách hai đặc trưng biến thiên cùng nhau | Cách hai đặc trưng biến thiên cùng nhau |
| Q4 | **C** | It means Hướng chứa nhiều phương sai nhất trong PCA | Hướng chứa nhiều phương sai nhất trong PCA |
| Q5 | **B** | It helps to Trả eigenvalues/eigenvectors cho ma trận đối xứng | Trả eigenvalues/eigenvectors cho ma trận đối xứng |
| Q6 | **A** | It helps to Chỉ trả eigenvalues của ma trận đối xứng | Chỉ trả eigenvalues của ma trận đối xứng |
| Q7 | **D** | It helps to Cột là feature, hàng là mẫu khi tính covariance | Cột là feature, hàng là mẫu khi tính covariance |
| Q8 | **C** | It helps to Sắp eigenvalue giảm dần để chọn hướng lớn | Sắp eigenvalue giảm dần để chọn hướng lớn |
| Q9 | **B** | Chọn eigenvector tương ứng eigenvalue lớn nhất | Chọn eigenvector tương ứng eigenvalue lớn nhất |
| Q10 | **A** | Eigenvalue gần 0 biểu thị hướng rất ít biến thiên | Eigenvalue gần 0 biểu thị hướng rất ít biến thiên |
| Q11 | **D** | A@v gần lambda*v cho cặp riêng chính xác | A@v gần lambda*v cho cặp riêng chính xác |
| Q12 | **C** | argsort chọn eigenvalue lớn trước thay vì mặc định nhỏ | argsort chọn eigenvalue lớn trước thay vì mặc định nhỏ |
| Q13 | **B** | Hai PC giảm dữ liệu ba hàng và hai cột thành một chiều | Hai PC giảm dữ liệu ba hàng và hai cột thành một chiều |
| Q14 | **A** | The input is Covariance minh họa chéo [2,3] | Covariance minh họa chéo [2,3] |
| Q15 | **D** | The input is Ba điểm cùng tăng hai feature | Ba điểm cùng tăng hai feature |
| Q16 | **C** | The input is Ma trận chéo 2×2 | Ma trận chéo 2×2 |
| Q17 | **B** | The input is Giá trị riêng [4,1,3] | Giá trị riêng [4,1,3] |
| Q18 | **A** | The input is 3 khách × 2 feature | 3 khách × 2 feature |
| Q19 | **D** | Shapes and data units | Shape và đơn vị dữ liệu |
| Q20 | **C** | It does not establish predictive performance | Nó không đo chất lượng dự đoán |

## 8. Nối sang bài kế tiếp

`Hệ tuyến tính → Eigenvalues/Vectors → Covariance → PCA`.
