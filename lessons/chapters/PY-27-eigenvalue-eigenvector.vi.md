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

**No Note — Không chú thích**

```python
import numpy as np

A = np.diag([2.0, 3.0])
v = np.array([0.0, 1.0])
print(A @ v)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Minh họa vector riêng giữ nguyên hướng khi bị ma trận giãn theo trục.
# Dữ liệu: A=diag(2,3) giãn x gấp 2, y gấp 3; v=[0,1] trùng trục y.
# NumPy (np) cung cấp mảng số và các hàm đại số tuyến tính/covariance.
import numpy as np

# np.diag() đặt hai hệ số trên đường chéo, các ô khác bằng 0.
A = np.diag([2.0, 3.0])
# v là vector hướng y với hai thành phần x=0,y=1.
v = np.array([0.0, 1.0])
# @ nhân ma trận với vector: ra [0,3], giữ phương y và giãn gấp 3; đó là hướng riêng.
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

**No Note — Không chú thích**

```python
import numpy as np

A = np.diag([2.0, 3.0])
print(np.linalg.eigvalsh(A))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Đọc các trị riêng của ma trận đường chéo đối xứng bằng eigvalsh().
# Dữ liệu: A là ma trận 2×2 đối xứng, hệ số giãn theo hai trục bằng 2 và 3.
# NumPy (np) cung cấp mảng số và các hàm đại số tuyến tính/covariance.
import numpy as np

# diag() tạo ma trận đường chéo thực đối xứng.
A = np.diag([2.0, 3.0])
# eigvalsh() trả TRỊ RIÊNG tăng dần của ma trận đối xứng, KHÔNG trả vector riêng; phù hợp vì A đối xứng.
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

**No Note — Không chú thích**

```python
import numpy as np

X = np.array([[1, 2], [2, 4], [3, 6]])
print(np.cov(X, rowvar=False))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tính covariance của hai cột số liệu có quan hệ y=2x.
# Dữ liệu: Ba hàng quan sát, cột y gấp đôi x; covariance mô tả biến thiên cùng nhau.
# NumPy (np) cung cấp mảng số và các hàm đại số tuyến tính/covariance.
import numpy as np

# Mỗi hàng là một mẫu, mỗi cột là một biến x/y.
X = np.array([[1, 2], [2, 4], [3, 6]])
# np.cov() tính hiệp phương sai mẫu (mẫu số n−1); rowvar=False nghĩa biến theo CỘT, không theo hàng; kết quả ma trận 2×2.
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

**No Note — Không chú thích**

```python
import numpy as np

C = np.diag([2.0, 3.0])
values, vectors = np.linalg.eigh(C)
print(np.abs(vectors[:, -1]))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Chọn vector riêng ứng với trị riêng lớn nhất để hiểu hướng PCA.
# Dữ liệu: C=diag(2,3) là covariance giả định; chiều y biến thiên nhiều nhất.
# NumPy (np) cung cấp mảng số và các hàm đại số tuyến tính/covariance.
import numpy as np

# Ma trận đường chéo có phương sai lớn nhất nằm ở hướng y.
C = np.diag([2.0, 3.0])
# eigh() trả tuple (values,vectors) với values tăng dần; mỗi CỘT vectors là một vector riêng tương ứng.
values, vectors = np.linalg.eigh(C)
# [:, -1] lấy cột vector riêng CUỐI ứng với trị riêng lớn nhất.
# abs() bỏ khác biệt dấu +/- vì hai vector đối hướng biểu diễn cùng trục riêng.
print(np.abs(vectors[:, -1]))
```

**Kết quả khi chạy:**

```text
[0. 1.]
```

Hướng có phương sai lớn nhất nằm trên trục y; đổi dấu vector riêng không đổi hướng trục.

## 5. Năm tình huống trị riêng — từ nhận biết trục đến tái tạo bằng PCA

### Tình huống 1 — Cấp 1: Tìm chiều biến thiên trong 10 phép đo hai trục

**Từ vựng trong mục:** **Covariance** — hiệp phương sai; **Eigenvalue** — trị riêng; **Axis** — trục.

**Tình huống thực tế:** Kỹ thuật viên nhận **10 vị trí cảm biến** trên mặt phẳng, mỗi dòng gồm tọa độ **x và y (mm)**. Trong dữ liệu thử nghiệm, **x thay đổi từ 1 đến 10 mm**, còn **y luôn là 20 mm**. Người trực muốn biết dữ liệu biến thiên theo hướng nào, không nhầm số đo y bằng 20 với việc y có biến động lớn; đây là bài quan sát độ thay đổi chứ không phải tìm vị trí xa gốc nhất.

**Vì sao chọn cách này?** **Hiệp phương sai (covariance)** mô tả hai đại lượng **thay đổi riêng và cùng nhau** ra sao quanh mức trung bình; `np.cov(X, rowvar=False)` xem **mỗi cột** x/y là một đại lượng, mỗi hàng là một lượt đo. **Trị riêng (eigenvalue)** của bảng hiệp phương sai cho biết mức biến thiên trên các **hướng đặc biệt**. Vì mọi y đều bằng 20, y có **độ thay đổi bằng 0**, dù giá trị của nó lớn hơn x; một trị riêng sẽ bằng 0. `eigvalsh` dùng cho ma trận đối xứng và trả trị riêng mà không phải tính hướng, vì câu hỏi đầu chỉ cần mức biến thiên.

**Quy trình:**
1. Tạo 10 hàng × 2 cột và tính covariance với cột là đặc trưng.
2. Dùng `eigvalsh` đọc hai trị riêng đã sắp tăng.
3. Chọn trục có phương sai lớn nhất và diễn giải.

**No Note — Không chú thích**

```python
import numpy as np
X = np.array([[1,20],[2,20],[3,20],[4,20],[5,20],[6,20],[7,20],[8,20],[9,20],[10,20]], dtype=float)
C = np.cov(X, rowvar=False)
values = np.linalg.eigvalsh(C)
if X.shape != (10, 2):
    raise ValueError("Cần 10 lượt đo với hai đại lượng.")
print("Lượt đo:", len(X))
print("Trị riêng nhỏ:", f"{values[0]:.2f}")
print("Trị riêng lớn:", f"{values[-1]:.2f}")
print("Y không thay đổi:", bool(np.all(X[:, 1] == 20)))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Kiểm một cột không đổi khiến một trị riêng bằng 0 trong 10 mẫu.
# Dữ liệu: 10 hàng, x tăng 1..10 nhưng y luôn 20; y không mang thông tin biến thiên.
# NumPy (np) cung cấp mảng số và các hàm đại số tuyến tính/covariance.
import numpy as np
# 10 điểm có y=20 ở mọi hàng nên độ biến thiên y bằng 0.
X = np.array([[1,20],[2,20],[3,20],[4,20],[5,20],[6,20],[7,20],[8,20],[9,20],[10,20]], dtype=float)
# rowvar=False dùng các cột làm biến; covariance ước lượng theo mẫu, chia cho n−1.
C = np.cov(X, rowvar=False)
# eigvalsh trả hai trị riêng xếp tăng; trị riêng gần 0 ở trục không đổi.
values = np.linalg.eigvalsh(C)
if X.shape != (10, 2):
    # ValueError dừng nếu số hàng/cột hoặc kết quả PCA không đúng yêu cầu.
    raise ValueError("Cần 10 lượt đo với hai đại lượng.")
print("Lượt đo:", len(X))
# [0] là trị nhỏ nhất, [-1] lớn nhất, :.2f định dạng hai chữ số lẻ.
print("Trị riêng nhỏ:", f"{values[0]:.2f}")
print("Trị riêng lớn:", f"{values[-1]:.2f}")
# [:,1] lấy toàn bộ cột y; ==20 tạo mask bool; np.all() yêu cầu tất cả True; bool() chuyển về Boolean Python.
print("Y không thay đổi:", bool(np.all(X[:, 1] == 20)))
```

**Kết quả khi chạy:**

```text
Lượt đo: 10
Trị riêng nhỏ: 0.00
Trị riêng lớn: 9.17
Y không thay đổi: True
```

Ở cấp này, phương sai y bằng 0 không có nghĩa tọa độ y bằng 0; cảm biến luôn ghi **20 mm**.

### Tình huống 2 — Cấp 2: Nhận biết chiều dư thừa của 12 bản ghi phụ thuộc

**Từ vựng trong mục:** **Linear dependence** — phụ thuộc tuyến tính; **Eigenvalue** — trị riêng.

**Tình huống thực tế:** Một máy ghi **12 mẫu**, mỗi mẫu gồm chỉ số **x** và chỉ số thứ hai **luôn bằng hai lần x**. Đây là hai cột số giả lập không có đơn vị; nhìn bảng thấy có hai cột, nhưng cột thứ hai có thể dự đoán hoàn toàn từ cột thứ nhất. Người phân tích muốn biết có mấy **hướng biến thiên độc lập** trước khi dùng hai cột làm đầu vào cho mô hình.

**Vì sao chọn cách này?** Khi cột thứ hai **luôn gấp đôi** cột thứ nhất, chúng không phải hai nguồn biến thiên khác nhau. Ma trận hiệp phương sai được tính sau khi xét sự thay đổi quanh trung bình của 12 mẫu; nó sẽ có **một trị riêng lớn hơn 0** và **một trị riêng gần 0**. `np.linalg.eigvalsh()` phù hợp vì hiệp phương sai là ma trận đối xứng; dùng ngưỡng `1e-9` khi đếm trị riêng dương để tránh sai số máy tính được hiểu là thông tin mới. Bớt một cột ở đây không làm mất thông tin tuyến tính, nhưng kết luận ấy phụ thuộc đúng quan hệ trong dữ liệu mẫu.

**Quy trình:**
1. Ghi 12 cặp x/2x và tính hiệp phương sai.
2. Tính các trị riêng qua `eigvalsh` để tránh số phức do sai số thuật toán.
3. Đếm số trị riêng dương theo ngưỡng nhỏ.

**No Note — Không chú thích**

```python
import numpy as np
X = np.array([[1,2],[2,4],[3,6],[4,8],[5,10],[6,12],[7,14],[8,16],[9,18],[10,20],[11,22],[12,24]], dtype=float)
C = np.cov(X, rowvar=False)
eigenvalues = np.linalg.eigvalsh(C)
if X.shape != (12, 2):
    raise ValueError("Cần đúng 12 mẫu hai chiều.")
print("Mẫu:", len(X))
labels = []
for value in eigenvalues:
    labels.append(f"{value:.2f}")
print("Trị riêng:", ", ".join(labels))
print("Chiều có biến thiên:", int((eigenvalues > 1e-9).sum()))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Đếm hướng biến thiên độc lập khi 12 điểm đều nằm trên đường thẳng.
# Dữ liệu: 12 điểm hai chiều y=2x; thực chất chỉ một hướng độc lập.
# NumPy (np) cung cấp mảng số và các hàm đại số tuyến tính/covariance.
import numpy as np
# 12 hàng (x,y) với y luôn gấp đôi x: hai cột không độc lập.
X = np.array([[1,2],[2,4],[3,6],[4,8],[5,10],[6,12],[7,14],[8,16],[9,18],[10,20],[11,22],[12,24]], dtype=float)
# rowvar=False nghĩa mỗi cột x/y là một biến, các hàng là lượt đo.
C = np.cov(X, rowvar=False)
# Trị riêng từ ma trận đối xứng C xếp tăng, một hướng gần 0 vì dữ liệu trên đường.
eigenvalues = np.linalg.eigvalsh(C)
if X.shape != (12, 2):
    # ValueError dừng nếu số hàng/cột hoặc kết quả PCA không đúng yêu cầu.
    raise ValueError("Cần đúng 12 mẫu hai chiều.")
print("Mẫu:", len(X))
labels = []
for value in eigenvalues:
    # f-string :.2f hiển thị từng trị riêng với hai chữ số sau dấu thập phân.
    labels.append(f"{value:.2f}")
print("Trị riêng:", ", ".join(labels))
# Ngưỡng 1e-9 bỏ sai số float gần 0; > tạo mask, sum() đếm chiều biến thiên đáng kể.
print("Chiều có biến thiên:", int((eigenvalues > 1e-9).sum()))
```

**Kết quả khi chạy:**

```text
Mẫu: 12
Trị riêng: 0.00, 65.00
Chiều có biến thiên: 1
```

Trị riêng 0 không nói rằng một cột toàn số 0, mà nói hai cột không độc lập với nhau.

### Tình huống 3 — Cấp 3: Đối chiếu vector riêng trên 15 tọa độ dạng lưới

**Từ vựng trong mục:** **Eigenvector** — véc-tơ riêng; **Eigen-equation** — quan hệ riêng; **eigh** — tìm trị và véc-tơ riêng.

**Tình huống thực tế:** Robot khảo sát **15 vị trí trên sàn** theo hình lưới **5 cột × 3 hàng**, mỗi vị trí có tọa độ **(x, y) tính bằng mét**. Nhóm kỹ thuật muốn biết hai **hướng biến thiên chính** của các điểm và kiểm tra bằng phép tính rằng mỗi hướng được thuật toán xác định đúng, thay vì chỉ ước lượng bằng mắt trên hình vẽ.

**Vì sao chọn cách này?** **Véc-tơ riêng (eigenvector)** là một **hướng** mà khi nhân với ma trận, hướng ấy **không bị xoay sang hướng khác**, chỉ thay đổi độ lớn theo **trị riêng** tương ứng. `np.linalg.eigh(C)` cho cả các mức biến thiên và hai hướng riêng của ma trận hiệp phương sai **đối xứng**. Chương trình dùng `C @ vectors` so với `vectors * values`, rồi `np.allclose()` để kiểm sai khác số thực nhỏ do máy tính. Dấu của véc-tơ riêng có thể đảo (+ thành -) nhưng vẫn chỉ cùng một trục, nên không ép dấu theo hình vẽ. Đây là phép **kiểm chứng kết quả**, không phải robot phải di chuyển theo hướng ấy.

**Quy trình:**
1. Tạo 15 mẫu lưới và tính covariance 2×2.
2. Nhận trị riêng và cột véc-tơ riêng bằng `eigh`.
3. Kiểm chứng từng cột véc-tơ qua quan hệ riêng.

**No Note — Không chú thích**

```python
import numpy as np
X = np.array([[0,0],[1,0],[2,0],[3,0],[4,0],[0,1],[1,1],[2,1],[3,1],[4,1],[0,2],[1,2],[2,2],[3,2],[4,2]], dtype=float)
C = np.cov(X, rowvar=False)
values, vectors = np.linalg.eigh(C)
verified = np.allclose(C @ vectors, vectors * values)
if X.shape != (15, 2):
    raise ValueError("Cần đúng 15 điểm hai chiều.")
print("Điểm:", len(X))
labels = []
for value in values:
    labels.append(f"{value:.3f}")
print("Trị riêng:", ", ".join(labels))
print("Kiểm chứng:", bool(verified))
print("Số hướng:", vectors.shape[1])
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Kiểm phương trình C@v=λv cho các vector riêng của 15 điểm hai chiều.
# Dữ liệu: 15 điểm tạo lưới 5×3, mỗi hàng một điểm x,y.
# NumPy (np) cung cấp mảng số và các hàm đại số tuyến tính/covariance.
import numpy as np
# 15 hàng điểm trên lưới hai chiều, dtype=float phục vụ tính covariance.
X = np.array([[0,0],[1,0],[2,0],[3,0],[4,0],[0,1],[1,1],[2,1],[3,1],[4,1],[0,2],[1,2],[2,2],[3,2],[4,2]], dtype=float)
# cov 2×2 dùng hai cột làm hai biến, chia n−1 theo mặc định.
C = np.cov(X, rowvar=False)
# eigh() trả trị riêng và vector riêng (vector được xếp theo CỘT).
values, vectors = np.linalg.eigh(C)
# @ nhân C đồng thời với mỗi cột vector riêng.
# Broadcast trị riêng tương ứng theo cột, tạo λv cho mỗi vector.
# allclose() kiểm C@v ≈ λv trong dung sai floating-point, không dùng == tuyệt đối.
verified = np.allclose(C @ vectors, vectors * values)
if X.shape != (15, 2):
    # ValueError dừng nếu số hàng/cột hoặc kết quả PCA không đúng yêu cầu.
    raise ValueError("Cần đúng 15 điểm hai chiều.")
print("Điểm:", len(X))
labels = []
for value in values:
    # Định dạng :.3f in ba số thập phân.
    labels.append(f"{value:.3f}")
print("Trị riêng:", ", ".join(labels))
print("Kiểm chứng:", bool(verified))
# shape[1] đếm số hướng/ số cột vector riêng.
print("Số hướng:", vectors.shape[1])
```

**Kết quả khi chạy:**

```text
Điểm: 15
Trị riêng: 0.714, 2.143
Kiểm chứng: True
Số hướng: 2
```

Chỉ khi nhân ma trận hiệp phương sai với **đúng véc-tơ riêng** mới thu được cùng phương đã nhân hệ số.

### Tình huống 4 — Cấp 4: Xếp hai hướng biến thiên từ 18 điểm và tỷ lệ thông tin

**Từ vựng trong mục:** **Variance ratio** — tỷ lệ phương sai; **Principal direction** — hướng chính.

**Tình huống thực tế:** Đội khảo sát thu **18 vị trí** trên lưới **6 cột × 3 hàng**, mỗi vị trí có hai tọa độ x và y cùng đơn vị. Quan sát sơ bộ cho thấy các điểm trải dài theo chiều ngang nhiều hơn chiều dọc. Nhóm muốn xác nhận **hướng có biến thiên lớn hơn** và nó chiếm **bao nhiêu phần trăm tổng biến thiên** của cả hai hướng để chọn cách biểu diễn dữ liệu.

**Vì sao chọn cách này?** Để biết dữ liệu trải dài theo **hướng nào**, chương trình tính hiệp phương sai của 18 điểm rồi lấy **trị riêng lớn nhất**: hướng tương ứng có phương sai lớn nhất. `argsort(...)[::-1]` đưa trị riêng lớn nhất lên trước và dùng véc-tơ riêng của nó; so độ lớn hai thành phần để nhận biết hướng gần trục x hay y. **Tỷ lệ phương sai giải thích** cho biết phần biến thiên trên hướng chính so với **tổng biến thiên của hai hướng**, không phải phần trăm điểm đo đúng hay độ chính xác dự báo. Vì lưới rộng theo x, kết quả ưu tiên x là phù hợp với dữ liệu mô phỏng.

**Quy trình:**
1. Tính covariance của 18 điểm quan sát.
2. Sắp hai trị riêng giảm dần và lấy tỷ trọng trị lớn trong tổng.
3. Kiểm tra hướng chính bằng giá trị tuyệt đối của véc-tơ riêng, tránh phụ thuộc dấu.

**No Note — Không chú thích**

```python
import numpy as np
points = np.array([[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[0,1],[1,1],[2,1],[3,1],[4,1],[5,1],[0,2],[1,2],[2,2],[3,2],[4,2],[5,2]], dtype=float)
C = np.cov(points, rowvar=False)
values, vectors = np.linalg.eigh(C)
order = np.argsort(values)[::-1]
principal = np.abs(vectors[:, order[0]])
if points.shape != (18, 2):
    raise ValueError("Cần đúng 18 điểm hai chiều.")
print("Điểm:", len(points))
if principal[0] > principal[1]:
    principal_axis = "x"
else:
    principal_axis = "y"
print("Hướng chính:", principal_axis)
print(f"Tỷ lệ phương sai lớn nhất: {100*values[order[0]]/values.sum():.2f}%")
print("Số chiều:", len(values))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Chọn hướng phương sai chính trên lưới 18 điểm và tính tỷ lệ giữ được.
# Dữ liệu: 18 hàng điểm tạo lưới 6×3; phương sai x lớn hơn y.
# NumPy (np) cung cấp mảng số và các hàm đại số tuyến tính/covariance.
import numpy as np
# 18 mẫu điểm x/y, dtype=float.
points = np.array([[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[0,1],[1,1],[2,1],[3,1],[4,1],[5,1],[0,2],[1,2],[2,2],[3,2],[4,2],[5,2]], dtype=float)
# rowvar=False tính covariance giữa CỘT x,y của các hàng quan sát.
C = np.cov(points, rowvar=False)
# eigh trả trị riêng tăng dần và vector riêng ở các cột.
values, vectors = np.linalg.eigh(C)
# argsort trả CHỈ SỐ tăng dần theo trị riêng; [::-1] đảo thứ tự thành giảm dần.
order = np.argsort(values)[::-1]
# [:,order[0]] chọn cột vector riêng cho trị lớn nhất.
# abs() bỏ dấu vector riêng vốn có thể đảo chiều ±.
principal = np.abs(vectors[:, order[0]])
if points.shape != (18, 2):
    # ValueError dừng nếu số hàng/cột hoặc kết quả PCA không đúng yêu cầu.
    raise ValueError("Cần đúng 18 điểm hai chiều.")
print("Điểm:", len(points))
# So độ lớn x với y để chọn tên trục gần vector chính nhất.
if principal[0] > principal[1]:
    principal_axis = "x"
else:
    principal_axis = "y"
print("Hướng chính:", principal_axis)
# Chia trị riêng lớn nhất cho tổng trị riêng, nhân 100 để ra % phương sai giữ bởi một hướng.
print(f"Tỷ lệ phương sai lớn nhất: {100*values[order[0]]/values.sum():.2f}%")
# len() đếm hai chiều/trị riêng ban đầu.
print("Số chiều:", len(values))
```

**Kết quả khi chạy:**

```text
Điểm: 18
Hướng chính: x
Tỷ lệ phương sai lớn nhất: 81.40%
Số chiều: 2
```

Trị riêng chỉ có ý nghĩa **phương sai** vì ma trận ở đây là covariance; với ma trận biến đổi khác cần giải thích theo ngữ cảnh khác.

### Tình huống 5 — Cấp 5: PCA từ 20 hồ sơ có bốn đặc trưng nhưng chỉ hai chiều độc lập

**Từ vựng trong mục:** **PCA** — thành phần chính; **Rank** — hạng; **Reconstruction** — tái tạo.

**Tình huống thực tế:** Một bài thực hành AI tạo **20 hồ sơ mô phỏng**, mỗi hồ sơ ghi **4 chỉ số không đơn vị**: `x`, `2x`, `y`, `3y`. Hai chỉ số là bản phóng to của chỉ số khác, nên thực chất chỉ có **hai hướng thông tin độc lập**. Học viên muốn nén bảng 20 hàng × 4 cột thành **20 hàng × 2 tọa độ mới**, rồi thử dựng lại bốn cột để xem có làm mất thông tin tuyến tính đáng kể không.

**Vì sao chọn cách này?** **PCA (phân tích thành phần chính)** tìm những hướng mà dữ liệu thay đổi nhiều nhất, để mô tả bảng bằng **ít tọa độ hơn**. Trước tiên `centered` trừ **trung bình từng cột** để chuyển về biến thiên quanh tâm; sau đó lấy trị riêng/véc-tơ riêng của hiệp phương sai, sắp theo mức biến thiên giảm dần và giữ **hai hướng lớn nhất**. Phép `projected = centered @ basis` chuyển 20 hồ sơ thành hai tọa độ mới; nhân ngược và cộng lại trung bình để `recreated` thử dựng lại bốn cột. Vì `2x` và `3y` không đưa thông tin độc lập mới, hai hướng đủ để dựng lại gần chính xác trong bài này. Với dữ liệu thật có nhiễu và nhiều hướng, giảm còn hai chiều **có thể mất thông tin**; không tự kết luận PCA luôn giữ trọn dữ liệu.

**Quy trình:**
1. Căn giữa bảng 20×4, tính covariance và `eigh`.
2. Chọn hai eigenvector ứng với hai trị riêng lớn nhất rồi chiếu.
3. Tái tạo bảng, kiểm tra sai số và báo tỷ lệ phương sai của hướng đầu.

**No Note — Không chú thích**

```python
import numpy as np
X = np.array([[0,0,0,0],[1,2,0,0],[2,4,0,0],[3,6,0,0],[4,8,0,0],[0,0,1,3],[1,2,1,3],[2,4,1,3],[3,6,1,3],[4,8,1,3],[0,0,2,6],[1,2,2,6],[2,4,2,6],[3,6,2,6],[4,8,2,6],[0,0,3,9],[1,2,3,9],[2,4,3,9],[3,6,3,9],[4,8,3,9]], dtype=float)
centered = X - X.mean(axis=0)
C = np.cov(X, rowvar=False)
values, vectors = np.linalg.eigh(C)
order = np.argsort(values)[::-1]
basis = vectors[:, order[:2]]
projected = centered @ basis
recreated = projected @ basis.T + X.mean(axis=0)
if X.shape != (20, 4) or projected.shape != (20, 2):
    raise ValueError("Cần 20 mẫu bốn đặc trưng và hai chiều sau PCA.")
print("Hồ sơ:", len(X))
print("Cột gốc:", X.shape[1])
print("Cột sau PCA:", projected.shape[1])
print("Trị riêng dương:", int((values > 1e-9).sum()))
print(f"Hướng đầu giữ: {100*values[order[0]]/values.sum():.2f}%")
print("Tái tạo đúng:", bool(np.allclose(recreated, X)))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Chiếu 20 hồ sơ bốn đặc trưng phụ thuộc tuyến tính xuống hai chiều rồi tái tạo.
# Dữ liệu: 20 hàng × 4 cột, cột 1=2×cột 0 và cột 3=3×cột 2; chỉ có hai hướng độc lập.
# NumPy (np) cung cấp mảng số và các hàm đại số tuyến tính/covariance.
import numpy as np
# 20 hồ sơ có 4 cột nhưng chỉ 2 cột mang biến thiên độc lập; dtype=float.
X = np.array([[0,0,0,0],[1,2,0,0],[2,4,0,0],[3,6,0,0],[4,8,0,0],[0,0,1,3],[1,2,1,3],[2,4,1,3],[3,6,1,3],[4,8,1,3],[0,0,2,6],[1,2,2,6],[2,4,2,6],[3,6,2,6],[4,8,2,6],[0,0,3,9],[1,2,3,9],[2,4,3,9],[3,6,3,9],[4,8,3,9]], dtype=float)
# mean(axis=0) tính trung bình TỪNG CỘT trên mọi hàng.
# Broadcast trừ vector bốn trung bình cho mỗi hàng, đưa từng biến về trung bình 0.
centered = X - X.mean(axis=0)
# rowvar=False tính ma trận covariance 4×4 theo CỘT (np.cov tự trừ trung bình và chia n−1).
C = np.cov(X, rowvar=False)
# eigh trả 4 trị riêng tăng dần và vector riêng ở các cột.
values, vectors = np.linalg.eigh(C)
# argsort trả chỉ số sắp tăng, [::-1] đảo để hướng phương sai lớn lên trước.
order = np.argsort(values)[::-1]
# order[:2] chọn hai trị lớn nhất; vectors[:,...] lấy hai vector riêng làm basis 4×2.
basis = vectors[:, order[:2]]
# @ chiếu từng hàng bốn chiều lên hai hướng mới, trả bảng 20×2.
projected = centered @ basis
# mean(axis=0) tính trung bình TỪNG CỘT trên mọi hàng.
# @ với basis.T (2×4) khôi phục bốn tọa độ đã căn giữa.
# Cộng lại bốn trung bình từng cột để quay về thang dữ liệu ban đầu.
recreated = projected @ basis.T + X.mean(axis=0)
if X.shape != (20, 4) or projected.shape != (20, 2):
    # ValueError dừng nếu số hàng/cột hoặc kết quả PCA không đúng yêu cầu.
    raise ValueError("Cần 20 mẫu bốn đặc trưng và hai chiều sau PCA.")
print("Hồ sơ:", len(X))
print("Cột gốc:", X.shape[1])
print("Cột sau PCA:", projected.shape[1])
# Mask trị riêng dương đáng kể, dùng đếm số hướng biến thiên.
print("Trị riêng dương:", int((values > 1e-9).sum()))
# Tỷ lệ phương sai hướng đầu = trị riêng lớn nhất / tổng trị riêng ×100 (%).
print(f"Hướng đầu giữ: {100*values[order[0]]/values.sum():.2f}%")
# allclose đối chiếu tái tạo với dữ liệu gốc có dung sai; giữ hai hướng đủ vì dữ liệu chỉ có hai hướng độc lập.
print("Tái tạo đúng:", bool(np.allclose(recreated, X)))
```

**Kết quả khi chạy:**

```text
Hồ sơ: 20
Cột gốc: 4
Cột sau PCA: 2
Trị riêng dương: 2
Hướng đầu giữ: 55.56%
Tái tạo đúng: True
```

Véc-tơ riêng đổi dấu vẫn cho không gian PCA như nhau. Không nên so chính xác từng hệ số véc-tơ theo dấu nếu mục tiêu chỉ là **hướng**.

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


**Q5. For A = [[3, 0], [0, 1]], what eigenvalue belongs to v = [1, 0]? | Với A = [[3, 0], [0, 1]], vector riêng v = [1, 0] ứng với trị riêng nào?**

A. 1 | 1

B. 3 | 3

C. 0 | 0

D. 4 | 4

**Đáp án: B**

**Giải thích:** Nhân A với v được [3, 0] = 3v; do đó trị riêng tương ứng bằng 3.


**Q6. A PCA model explains 70% variance with PC1 and 20% with PC2. How much is retained by both? | PCA giữ 70% phương sai ở PC1 và 20% ở PC2. Giữ cả hai thì được bao nhiêu?**

A. 50% | 50%

B. 70% | 70%

C. 90% | 90%

D. 100% | 100%

**Đáp án: C**

**Giải thích:** Tỷ lệ phương sai giải thích được cộng khi chọn các thành phần chính: 70% + 20% = 90%.


**Q7. In a 2-feature dataset, variance along x is 9 and along y is 1, with zero covariance. Which PCA direction comes first? | Dữ liệu hai đặc trưng có phương sai theo x là 9, theo y là 1, hiệp phương sai bằng 0. PCA chọn hướng đầu tiên nào?**

A. The x-axis | Trục x

B. The y-axis | Trục y

C. An equal mix of x and y | Pha đều x và y

D. No direction exists | Không có hướng nào

**Đáp án: A**

**Giải thích:** Khi hiệp phương sai bằng 0, trục có phương sai lớn nhất (trục x, bằng 9) là hướng thành phần chính đầu tiên.


**Q8. If the first principal component retains 80% of total variance, what percentage is not retained by that component? | Nếu thành phần chính đầu tiên giữ 80% tổng phương sai, bao nhiêu phần trăm không được giữ bởi riêng thành phần đó?**

A. 0% | 0%

B. 10% | 10%

C. 80% | 80%

D. 20% | 20%

**Đáp án: D**

**Giải thích:** Phần còn lại là 100% − 80% = 20%, nằm ở các hướng trực giao khác.


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
