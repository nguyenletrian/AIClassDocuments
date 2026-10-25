# PY-27 — Eigenvalue, Eigenvector và hướng biến thiên


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Eigenvector** — vector riêng; **Eigenvalue** — giá trị riêng.

`Hệ tuyến tính → Eigenvalues/Vectors → Covariance → PCA`

**Học xong dùng để làm gì?** Tìm các hướng giữ nguyên phương khi ma trận tác động, làm nền để hiểu PCA và biến đổi dữ liệu.

**Kết nối kiến thức tiếp theo:** PY-28 mô tả quan hệ giữa vector đầu vào và dự đoán bằng hàm toán học.

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

**Nội dung chính:** ma trận biến đổi có thể giữ nguyên phương của một số vector riêng. Khi ma trận là hiệp phương sai, trị riêng đo phương sai theo hướng đó, tạo cầu nối sang PCA.

### 4.1. Eigenvector — Hướng không bị xoay sau biến đổi

**Từ vựng trong mục:** **Eigenvector** — vector riêng; **Transformation** — phép biến đổi.

Một **eigenvector** là vector khác không mà khi nhân với ma trận vuông A, nó chỉ đổi **độ lớn hoặc đảo chiều**, không rời khỏi đường phương ban đầu: `A @ v = λ*v`. Ví dụ ma trận `diag(2,3)` nhân vector `[0,1]` cho `[0,3]`, vẫn nằm trên trục tung. Điều kiện là vector khác không và phù hợp số chiều của A; vector riêng không phải bất kỳ vector nào.

```python
# Mục đích: Hướng không bị xoay sau biến đổi.
import numpy as np

A = np.diag([2.0, 3.0])
v = np.array([0.0, 1.0])
print(A @ v)
```

**Kết quả khi chạy:**

```text
[0. 3.]
```

Đầu ra vẫn có hoành độ 0; phương trục tung được giữ, độ dài theo chiều đó nhân ba.

### 4.2. Eigenvalue — Hệ số biến đổi trên hướng riêng

**Từ vựng trong mục:** **Eigenvalue** — trị riêng; **Scale factor** — hệ số co giãn.

**Trị riêng** λ cho biết A phóng đại, thu nhỏ hoặc đảo chiều **vector riêng** bao nhiêu lần. Với `diag(2,3)`, hướng trục x có λ=2 và trục y có λ=3. Đó là tính chất của ma trận A; trị riêng **không** tự động mang nghĩa phương sai trừ khi A đang là **ma trận hiệp phương sai**. `np.linalg.eigvalsh` lấy các trị riêng của ma trận đối xứng theo thứ tự tăng dần.

```python
# Mục đích: Hệ số biến đổi trên hướng riêng.
import numpy as np

A = np.diag([2.0, 3.0])
print(np.linalg.eigvalsh(A))
```

**Kết quả khi chạy:**

```text
[2. 3.]
```

Hai trị riêng là 2 và 3, tương ứng mức co giãn của hai trục tọa độ.

### 4.3. Covariance — Hai đặc trưng cùng thay đổi ra sao?

**Từ vựng trong mục:** **Covariance** — hiệp phương sai; **Feature** — đặc trưng.

**Hiệp phương sai** đo xu hướng hai đặc trưng tăng/giảm cùng nhau. Dữ liệu có ba **hàng mẫu** `(1,2)`, `(2,4)`, `(3,6)` và hai **cột đặc trưng** x, y, trong đó y=2x. `np.cov(X,rowvar=False)` lấy **cột là biến**, **hàng là quan sát**, trả ma trận 2×2. Các ô đường chéo là phương sai từng biến, hai ô còn lại là hiệp phương sai. Không nhầm covariance với tương quan chuẩn hóa từ −1 đến 1.

```python
# Mục đích: Hai đặc trưng cùng thay đổi ra sao?.
import numpy as np

X = np.array([[1, 2], [2, 4], [3, 6]])
print(np.cov(X, rowvar=False))
```

**Kết quả khi chạy:**

```text
[[1. 2.]
 [2. 4.]]
```

Biến y có phương sai gấp bốn x và hiệp phương sai dương 2, vì y tăng theo x.

### 4.4. Principal direction — Hướng biến thiên chính trong PCA

**Từ vựng trong mục:** **Principal direction** — hướng chính; **PCA** — phân tích thành phần chính.

Với **ma trận hiệp phương sai đối xứng**, vector riêng của **trị riêng lớn nhất** biểu diễn hướng có phương sai lớn nhất. Đây là nguyên lý của PCA. Ví dụ hiệp phương sai `diag(2,3)` có phương sai theo x là 2 và theo y là 3, nên hướng chính là trục y. **Dấu của eigenvector không cố định**: `[0,1]` và `[0,-1]` đều mô tả cùng một trục. Lấy `abs` khi chỉ muốn minh họa độ lớn thành phần.

```python
# Mục đích: Hướng biến thiên chính trong PCA.
import numpy as np

C = np.diag([2.0, 3.0])
values, vectors = np.linalg.eigh(C)
print(np.abs(vectors[:, -1]))
```

**Kết quả khi chạy:**

```text
[0. 1.]
```

Hướng có phương sai lớn nhất nằm trên trục y; đổi dấu vector riêng không đổi hướng trục.

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Chọn hướng biến thiên lớn nhất · Cấp 1: Bài toán cơ bản

**Tình huống thực tế:** Một bảng thống kê hai đặc trưng đã được chuẩn hóa ý nghĩa đơn vị và có hiệp phương sai `diag(2,3)`. Cần xác định hướng mang nhiều phương sai hơn.

**Vì sao chọn cách giải này?** `eigh` dành cho ma trận đối xứng và trả trị riêng tăng dần; trị riêng cuối lớn nhất cùng vector riêng tương ứng.

**Quy trình giải:**

1. Tạo ma trận hiệp phương sai 2×2.
2. Tìm trị riêng và các vector riêng bằng `eigh`.
3. In trị riêng lớn nhất và độ lớn các thành phần vector riêng để không phụ thuộc dấu.

```python
# Mục đích: Chọn hướng biến thiên lớn nhất.
import numpy as np

C = np.diag([2.0, 3.0])
values, vectors = np.linalg.eigh(C)
print(values[-1], np.abs(vectors[:, -1]))
```

**Kết quả khi chạy:**

```text
3.0 [0. 1.]
```

Trục y là hướng chính với phương sai 3, lớn hơn trục x (2).

**Bài thực hành nâng cấp — cấp 1/5:** Nhóm phân tích có **10 phép đo**, mỗi hàng là một phương trình/quan sát, hai cột là hệ số của hai đại lượng chưa biết (hoặc hai đặc trưng đo). Hãy tìm eigenvalue lớn nhất của covariance trên 10 quan sát. Ở cấp 4–5 có quan sát không đầy đủ và các bước đánh giá để không coi phép tính số là tự động đúng.

```python
import numpy as np
# Mỗi hàng = một phép đo; hai cột = hệ số/đặc trưng x1, x2.
xs = [42, 70, 58, 91, 35, 76, 88, 64, 54, 96]
ys = [20+(k*7)%75 for k in range(1,11)]
array = np.column_stack((xs,ys)).astype(float)
clean = array[np.isfinite(array).all(axis=1)]
cov = np.cov(clean,rowvar=False)
eigvals,eigvecs = np.linalg.eigh(cov)
result = round(float(np.linalg.eigvalsh(np.cov(clean,rowvar=False))[-1]),3)
assert array.shape==(10,2)
print("Số quan sát:",len(array))
print("Kết quả:",result)
```

**Đọc kết quả:** Dữ liệu gốc có 10 hàng, ma trận dùng tính toán giữ các hàng đầy đủ; báo rõ rank, residual hoặc tỉ lệ phương sai tùy tác vụ.

### Tình huống 2 — Phát hiện dữ liệu phụ thuộc tuyến tính · Cấp 2: Phân tích cấu trúc

**Tình huống thực tế:** Ba hàng quan sát có hai đặc trưng lần lượt `(1,2)`, `(2,4)`, `(3,6)`; cột hai luôn gấp đôi cột một. Cần xem ma trận hiệp phương sai có hướng hoàn toàn không biến thiên không.

**Vì sao chọn cách giải này?** Khi hai cột phụ thuộc tuyến tính, ma trận hiệp phương sai có ít nhất một trị riêng gần 0.

**Quy trình giải:**

1. Lưu ba hàng quan sát và hai cột đặc trưng.
2. Tính hiệp phương sai theo cột bằng `rowvar=False`.
3. Dùng `eigvalsh` lấy hai trị riêng.

```python
# Mục đích: Phát hiện dữ liệu phụ thuộc tuyến tính.
import numpy as np

X = np.array([[1, 2], [2, 4], [3, 6]], dtype=float)
print(np.linalg.eigvalsh(np.cov(X, rowvar=False)))
```

**Kết quả khi chạy:**

```text
[0. 5.]
```

Một hướng có phương sai 0 do cột hai phụ thuộc cột đầu; hướng còn lại có phương sai 5.

**Bài thực hành nâng cấp — cấp 2/5:** Nhóm phân tích có **12 phép đo**, mỗi hàng là một phương trình/quan sát, hai cột là hệ số của hai đại lượng chưa biết (hoặc hai đặc trưng đo). Hãy kiểm tra rank của ma trận dữ liệu trước khi phân tích. Ở cấp 4–5 có quan sát không đầy đủ và các bước đánh giá để không coi phép tính số là tự động đúng.

```python
import numpy as np
# Mỗi hàng = một phép đo; hai cột = hệ số/đặc trưng x1, x2.
xs = [42, 70, 58, 91, 35, 76, 88, 64, 54, 96, 47, 82]
ys = [20+(k*7)%75 for k in range(1,13)]
array = np.column_stack((xs,ys)).astype(float)
clean = array[np.isfinite(array).all(axis=1)]
cov = np.cov(clean,rowvar=False)
eigvals,eigvecs = np.linalg.eigh(cov)
result = int(np.linalg.matrix_rank(clean))
assert array.shape==(12,2)
print("Số quan sát:",len(array))
print("Kết quả:",result)
```

**Đọc kết quả:** Dữ liệu gốc có 12 hàng, ma trận dùng tính toán giữ các hàng đầy đủ; báo rõ rank, residual hoặc tỉ lệ phương sai tùy tác vụ.

### Tình huống 3 — Kiểm nghiệm phương trình vector riêng · Cấp 3: Kiểm chứng đại số

**Tình huống thực tế:** Cho ma trận A=`diag(2,3)`. Chọn vector riêng ứng với trị riêng lớn nhất và kiểm tra quan hệ `A@v = λ*v`.

**Vì sao chọn cách giải này?** `np.allclose` đối chiếu hai vế trong sai số số thực, tránh so bằng tuyệt đối.

**Quy trình giải:**

1. Tìm cặp trị riêng/vector riêng từ A đối xứng.
2. Lấy trị riêng lớn nhất và cột vector tương ứng.
3. So hai vế `A@v` và `λ*v`.

```python
# Mục đích: Kiểm nghiệm phương trình vector riêng.
import numpy as np

A = np.diag([2.0, 3.0])
values, vectors = np.linalg.eigh(A)
print(np.allclose(A @ vectors[:, -1], values[-1] * vectors[:, -1]))
```

**Kết quả khi chạy:**

```text
True
```

Cặp trị riêng và vector riêng đáp ứng định nghĩa của eigenvector.

**Bài thực hành nâng cấp — cấp 3/5:** Nhóm phân tích có **15 phép đo**, mỗi hàng là một phương trình/quan sát, hai cột là hệ số của hai đại lượng chưa biết (hoặc hai đặc trưng đo). Hãy xác minh Av gần bằng lambda*v với vector riêng. Ở cấp 4–5 có quan sát không đầy đủ và các bước đánh giá để không coi phép tính số là tự động đúng.

```python
import numpy as np
# Mỗi hàng = một phép đo; hai cột = hệ số/đặc trưng x1, x2.
xs = [42, 70, 58, 91, 35, 76, 88, 64, 54, 96, 47, 82, 69, 73, 61]
ys = [20+(k*7)%75 for k in range(1,16)]
array = np.column_stack((xs,ys)).astype(float)
clean = array[np.isfinite(array).all(axis=1)]
cov = np.cov(clean,rowvar=False)
eigvals,eigvecs = np.linalg.eigh(cov)
result = bool(np.allclose(cov@eigvecs[:,1],eigvals[1]*eigvecs[:,1]))
assert array.shape==(15,2)
print("Số quan sát:",len(array))
print("Kết quả:",result)
```

**Đọc kết quả:** Dữ liệu gốc có 15 hàng, ma trận dùng tính toán giữ các hàng đầy đủ; báo rõ rank, residual hoặc tỉ lệ phương sai tùy tác vụ.

### Tình huống 4 — Sắp hướng theo độ biến thiên · Cấp 4: Có nhiễu hoặc số đo thiếu

**Tình huống thực tế:** Hệ thống thống kê có ba phương sai trên các hướng độc lập lần lượt là `[4,1,3]`. Cần ưu tiên hướng có phương sai cao nhất.

**Vì sao chọn cách giải này?** `argsort` trả chỉ số theo giá trị, rồi `[::-1]` đảo sang thứ tự giảm dần.

**Quy trình giải:**

1. Tạo mảng trị riêng `[4,1,3]`.
2. Tính chỉ số sắp tăng, rồi đảo thứ tự.
3. In chỉ số của các hướng từ lớn tới nhỏ.

```python
# Mục đích: Sắp hướng theo độ biến thiên.
import numpy as np

values = np.array([4, 1, 3])
print(np.argsort(values)[::-1])
```

**Kết quả khi chạy:**

```text
[0 2 1]
```

Ưu tiên hướng ở vị trí 0 (phương sai 4), tiếp đến vị trí 2 (3), cuối vị trí 1 (1).

**Bài thực hành nâng cấp — cấp 4/5:** Nhóm phân tích có **18 phép đo**, mỗi hàng là một phương trình/quan sát, hai cột là hệ số của hai đại lượng chưa biết (hoặc hai đặc trưng đo). Hãy sắp các eigenvalue và xử lý hàng đo bị thiếu. Ở cấp 4–5 có quan sát không đầy đủ và các bước đánh giá để không coi phép tính số là tự động đúng.

```python
import numpy as np
# Mỗi hàng = một phép đo; hai cột = hệ số/đặc trưng x1, x2.
xs = [42, 70, 58, 91, 35, 76, 88, 64, 54, 96, 47, 82, 69, 73, 61, np.nan, 90, 39]
ys = [20+(k*7)%75 for k in range(1,19)]
array = np.column_stack((xs,ys)).astype(float)
clean = array[np.isfinite(array).all(axis=1)]
cov = np.cov(clean,rowvar=False)
eigvals,eigvecs = np.linalg.eigh(cov)
result = {'eigenvalues':eigvals[::-1].round(4).tolist(),'missing':len(array)-len(clean)}
assert array.shape==(18,2)
print("Số quan sát:",len(array))
print("Kết quả:",result)
```

**Đọc kết quả:** Dữ liệu gốc có 18 hàng, ma trận dùng tính toán giữ các hàng đầy đủ; báo rõ rank, residual hoặc tỉ lệ phương sai tùy tác vụ.

### Tình huống 5 — Giảm số cột đặc trưng bằng PCA · Cấp 5: Tổng hợp và đánh giá

**Tình huống thực tế:** Ba quan sát hai chiều `(1,2)`, `(2,3)`, `(3,4)` được lưu thành bảng 3 hàng × 2 cột. Cần chiếu dữ liệu xuống một trục biến thiên chính để minh họa giảm chiều.

**Vì sao chọn cách giải này?** PCA tìm hướng có phương sai lớn; `n_components=1` giữ một trục, không giảm số hàng quan sát.

**Quy trình giải:**

1. Tạo bảng 3×2, hàng là quan sát và cột là đặc trưng.
2. Khởi tạo `PCA(n_components=1)` từ scikit-learn (thư viện cần cài).
3. Fit/transform và in shape dữ liệu sau chiếu.

```python
# Mục đích: Giảm số cột đặc trưng bằng PCA.
import numpy as np
from sklearn.decomposition import PCA

X = np.array([[1, 2], [2, 3], [3, 4]], dtype=float)
projected = PCA(n_components=1).fit_transform(X)
print(projected.shape)
```

**Kết quả khi chạy:**

```text
(3, 1)
```

Ba mẫu vẫn giữ nguyên; mỗi mẫu còn một giá trị tọa độ trên trục chính.

**Bài thực hành nâng cấp — cấp 5/5:** Nhóm phân tích có **20 phép đo**, mỗi hàng là một phương trình/quan sát, hai cột là hệ số của hai đại lượng chưa biết (hoặc hai đặc trưng đo). Hãy chiếu 20 quan sát xuống 1 chiều PCA và nêu số mẫu được giữ lại. Ở cấp 4–5 có quan sát không đầy đủ và các bước đánh giá để không coi phép tính số là tự động đúng.

```python
import numpy as np
# Mỗi hàng = một phép đo; hai cột = hệ số/đặc trưng x1, x2.
xs = [42, 70, 58, 91, 35, 76, 88, 64, 54, 96, 47, 82, 69, 73, 61, np.nan, 90, 39, 85, np.nan]
ys = [20+(k*7)%75 for k in range(1,21)]
array = np.column_stack((xs,ys)).astype(float)
clean = array[np.isfinite(array).all(axis=1)]
cov = np.cov(clean,rowvar=False)
eigvals,eigvecs = np.linalg.eigh(cov)
result = {'before':clean.shape,'after':((clean-clean.mean(axis=0))@eigvecs[:,-1:]).shape,'variance_ratio':round(float(eigvals[-1]/eigvals.sum()),4)}
assert array.shape==(20,2)
print("Số quan sát:",len(array))
print("Kết quả:",result)
```

**Đọc kết quả:** Dữ liệu gốc có 20 hàng, ma trận dùng tính toán giữ các hàng đầy đủ; báo rõ rank, residual hoặc tỉ lệ phương sai tùy tác vụ.

## 6. Sai lầm thường gặp

- Eigenvector là **hướng**, eigenvalue là **hệ số** nhân theo hướng ấy; không hoán đổi hai khái niệm.
- Chỉ diễn giải eigenvalue như phương sai khi A là ma trận hiệp phương sai.
- Với covariance, các hàng là mẫu và cột là đặc trưng khi `rowvar=False`; đảo trục làm thay đổi kết quả.
- Eigenvector và vector đối dấu biểu diễn cùng trục; không kiểm tra dấu từng phần tử cứng nhắc.
- `np.linalg.eigh` thích hợp cho ma trận đối xứng. PCA cần xem thang đo và đơn vị từng đặc trưng.
- scikit-learn là thư viện ngoài; cần cài trước khi chạy ví dụ PCA.

## 7. Trắc nghiệm

**Chỉ kiểm tra kiến thức bài học; không kiểm tra ghi nhớ tình huống đánh số.**

**Q1. What defines an eigenvector v of A? | Điều kiện định nghĩa vector riêng v của A là gì?**

A. `A @ v = λ*v` with v nonzero | `A @ v = λ*v` với v khác không

B. Scaling along a corresponding eigenvector | Hệ số co giãn theo vector riêng tương ứng

C. How two variables vary together | Hai biến cùng biến thiên ra sao

D. A covariance eigenvector with high eigenvalue | Vector riêng hiệp phương sai có trị riêng lớn

**Đáp án: A**

**Giải thích:** Vector khác không giữ phương đến hệ số nhân.


**Q2. What does an eigenvalue represent? | Trị riêng biểu thị gì?**

A. `A @ v = λ*v` with v nonzero | `A @ v = λ*v` với v khác không

B. Scaling along a corresponding eigenvector | Hệ số co giãn theo vector riêng tương ứng

C. How two variables vary together | Hai biến cùng biến thiên ra sao

D. A covariance eigenvector with high eigenvalue | Vector riêng hiệp phương sai có trị riêng lớn

**Đáp án: B**

**Giải thích:** Trị riêng là hệ số λ nhân vector riêng.


**Q3. What does covariance describe? | Hiệp phương sai mô tả gì?**

A. `A @ v = λ*v` with v nonzero | `A @ v = λ*v` với v khác không

B. Scaling along a corresponding eigenvector | Hệ số co giãn theo vector riêng tương ứng

C. How two variables vary together | Hai biến cùng biến thiên ra sao

D. A covariance eigenvector with high eigenvalue | Vector riêng hiệp phương sai có trị riêng lớn

**Đáp án: C**

**Giải thích:** Hiệp phương sai đo sự biến thiên cùng nhau.


**Q4. What is a principal direction in PCA? | Hướng chính trong PCA là gì?**

A. `A @ v = λ*v` with v nonzero | `A @ v = λ*v` với v khác không

B. Scaling along a corresponding eigenvector | Hệ số co giãn theo vector riêng tương ứng

C. How two variables vary together | Hai biến cùng biến thiên ra sao

D. A covariance eigenvector with high eigenvalue | Vector riêng hiệp phương sai có trị riêng lớn

**Đáp án: D**

**Giải thích:** Vector riêng hiệp phương sai nổi bật mang phương sai lớn nhất.


**Q5. Which function suits a symmetric matrix eigendecomposition? | Hàm nào phù hợp phân rã trị riêng ma trận đối xứng?**

A. `np.linalg.eigh(C)` | `np.linalg.eigh(C)`

B. `np.linalg.eigvalsh(C)` | `np.linalg.eigvalsh(C)`

C. `np.cov(X,rowvar=False)` | `np.cov(X,rowvar=False)`

D. `np.argsort(values)[::-1]` | `np.argsort(values)[::-1]`

**Đáp án: A**

**Giải thích:** eigh được thiết kế cho ma trận đối xứng/Hermitian.


**Q6. Which function returns only symmetric eigenvalues? | Hàm nào chỉ trả trị riêng ma trận đối xứng?**

A. `np.linalg.eigh(C)` | `np.linalg.eigh(C)`

B. `np.linalg.eigvalsh(C)` | `np.linalg.eigvalsh(C)`

C. `np.cov(X,rowvar=False)` | `np.cov(X,rowvar=False)`

D. `np.argsort(values)[::-1]` | `np.argsort(values)[::-1]`

**Đáp án: B**

**Giải thích:** eigvalsh không trả vector riêng.


**Q7. Which call treats DataFrame-like columns as variables? | Lệnh nào coi cột là biến khi tính covariance?**

A. `np.linalg.eigh(C)` | `np.linalg.eigh(C)`

B. `np.linalg.eigvalsh(C)` | `np.linalg.eigvalsh(C)`

C. `np.cov(X,rowvar=False)` | `np.cov(X,rowvar=False)`

D. `np.argsort(values)[::-1]` | `np.argsort(values)[::-1]`

**Đáp án: C**

**Giải thích:** rowvar=False coi cột là biến.


**Q8. Which expression sorts eigenvalue indices descending? | Biểu thức nào sắp chỉ số trị riêng giảm dần?**

A. `np.linalg.eigh(C)` | `np.linalg.eigh(C)`

B. `np.linalg.eigvalsh(C)` | `np.linalg.eigvalsh(C)`

C. `np.cov(X,rowvar=False)` | `np.cov(X,rowvar=False)`

D. `np.argsort(values)[::-1]` | `np.argsort(values)[::-1]`

**Đáp án: D**

**Giải thích:** argsort cho chỉ số tăng; đảo để được giảm.


**Q9. What is the shape of a covariance matrix for three features? | Ma trận covariance cho ba đặc trưng có shape gì?**

A. `(3,3)` | `(3,3)`

B. Columns of the second returned array | Các cột của mảng trả về thứ hai

C. v and −v describe the same eigendirection | v và −v biểu diễn cùng trục riêng

D. No variance along that direction | Không biến thiên theo hướng đó

**Đáp án: A**

**Giải thích:** Mỗi đặc trưng ghép với từng đặc trưng.


**Q10. Which object contains eigenvectors returned by `eigh`? | Trong kết quả của `eigh`, vector riêng nằm đâu?**

A. `(3,3)` | `(3,3)`

B. Columns of the second returned array | Các cột của mảng trả về thứ hai

C. v and −v describe the same eigendirection | v và −v biểu diễn cùng trục riêng

D. No variance along that direction | Không biến thiên theo hướng đó

**Đáp án: B**

**Giải thích:** eigh lưu mỗi vector riêng ở một cột.


**Q11. Why can an eigenvector's sign change? | Vì sao dấu vector riêng có thể đảo?**

A. `(3,3)` | `(3,3)`

B. Columns of the second returned array | Các cột của mảng trả về thứ hai

C. v and −v describe the same eigendirection | v và −v biểu diễn cùng trục riêng

D. No variance along that direction | Không biến thiên theo hướng đó

**Đáp án: C**

**Giải thích:** Đảo dấu vector riêng vẫn thỏa phương trình.


**Q12. What does a zero covariance eigenvalue suggest? | Trị riêng covariance bằng 0 gợi ý gì?**

A. `(3,3)` | `(3,3)`

B. Columns of the second returned array | Các cột của mảng trả về thứ hai

C. v and −v describe the same eigendirection | v và −v biểu diễn cùng trục riêng

D. No variance along that direction | Không biến thiên theo hướng đó

**Đáp án: D**

**Giải thích:** Trị riêng 0 nghĩa là không có phương sai theo trục đó.


**Q13. How does PCA choose its first component? | PCA chọn thành phần đầu ra sao?**

A. By largest explained variance | Theo phương sai giải thích lớn nhất

B. Variance of one feature | Phương sai của một đặc trưng

C. Two | Hai

D. `A @ v` approximately equals `λ*v` | `A @ v` xấp xỉ `λ*v`

**Đáp án: A**

**Giải thích:** Thành phần đầu tương ứng phương sai cao nhất.


**Q14. What does a covariance diagonal entry represent? | Ô đường chéo covariance biểu thị gì?**

A. By largest explained variance | Theo phương sai giải thích lớn nhất

B. Variance of one feature | Phương sai của một đặc trưng

C. Two | Hai

D. `A @ v` approximately equals `λ*v` | `A @ v` xấp xỉ `λ*v`

**Đáp án: B**

**Giải thích:** Hiệp phương sai của biến với chính nó là phương sai.


**Q15. How many eigenvalues does a 2×2 symmetric matrix have counting multiplicity? | Ma trận đối xứng 2×2 có bao nhiêu trị riêng tính cả bội?**

A. By largest explained variance | Theo phương sai giải thích lớn nhất

B. Variance of one feature | Phương sai của một đặc trưng

C. Two | Hai

D. `A @ v` approximately equals `λ*v` | `A @ v` xấp xỉ `λ*v`

**Đáp án: C**

**Giải thích:** Ma trận 2×2 có hai trị riêng tính bội.


**Q16. Which relation validates an eigenpair? | Quan hệ nào dùng kiểm tra cặp riêng?**

A. By largest explained variance | Theo phương sai giải thích lớn nhất

B. Variance of one feature | Phương sai của một đặc trưng

C. Two | Hai

D. `A @ v` approximately equals `λ*v` | `A @ v` xấp xỉ `λ*v`

**Đáp án: D**

**Giải thích:** Cặp riêng thỏa Av=λv theo sai số số học.


**Q17. Which data layout corresponds to `rowvar=False`? | `rowvar=False` tương ứng bố trí nào?**

A. Rows are samples and columns are features | Hàng là mẫu và cột là đặc trưng

B. Only when the matrix is an appropriate covariance matrix | Chỉ khi ma trận là covariance phù hợp

C. One principal-component feature per sample | Một đặc trưng thành phần chính cho mỗi mẫu

D. Feature scales and units | Thang đo và đơn vị các đặc trưng

**Đáp án: A**

**Giải thích:** Quan sát nằm theo hàng khi rowvar=False.


**Q18. Does an eigenvalue always mean variance? | Trị riêng có luôn mang nghĩa phương sai không?**

A. Rows are samples and columns are features | Hàng là mẫu và cột là đặc trưng

B. Only when the matrix is an appropriate covariance matrix | Chỉ khi ma trận là covariance phù hợp

C. One principal-component feature per sample | Một đặc trưng thành phần chính cho mỗi mẫu

D. Feature scales and units | Thang đo và đơn vị các đặc trưng

**Đáp án: B**

**Giải thích:** Diễn giải phương sai cần ma trận hiệp phương sai.


**Q19. What does `PCA(n_components=1)` preserve? | `PCA(n_components=1)` giữ lại gì?**

A. Rows are samples and columns are features | Hàng là mẫu và cột là đặc trưng

B. Only when the matrix is an appropriate covariance matrix | Chỉ khi ma trận là covariance phù hợp

C. One principal-component feature per sample | Một đặc trưng thành phần chính cho mỗi mẫu

D. Feature scales and units | Thang đo và đơn vị các đặc trưng

**Đáp án: C**

**Giải thích:** Dữ liệu sau chiếu còn một cột, vẫn giữ số hàng.


**Q20. What should be considered before comparing PCA variances across features? | Cần lưu ý gì trước khi so phương sai PCA giữa đặc trưng?**

A. Rows are samples and columns are features | Hàng là mẫu và cột là đặc trưng

B. Only when the matrix is an appropriate covariance matrix | Chỉ khi ma trận là covariance phù hợp

C. One principal-component feature per sample | Một đặc trưng thành phần chính cho mỗi mẫu

D. Feature scales and units | Thang đo và đơn vị các đặc trưng

**Đáp án: D**

**Giải thích:** Đặc trưng có thang lớn có thể lấn át PCA nếu chưa chuẩn hóa.

## 8. Nối sang bài kế tiếp

`Hệ tuyến tính → Eigenvalues/Vectors → Covariance → PCA`.
