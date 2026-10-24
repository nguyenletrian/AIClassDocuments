# PCA — Giảm chiều dữ liệu để nhìn rõ vấn đề trong AI

*AI / Data Science · Bài mẫu dành cho sinh viên · Phiên bản góp ý 02*

## 1. PCA nằm ở đâu trong chuỗi kiến thức?

```text
Python cơ bản
   ↓
List / Tuple / Dictionary
   ↓
NumPy Array → Vector → Matrix
                          ↓
             Feature và Dataset
                          ↓
                Mean / Variance
                          ↓
          StandardScaler / Covariance
                          ↓
                Eigenvector / Eigenvalue
                          ↓
                  PCA ← BÀI NÀY
                          ↓
     Data Visualization / Clustering / ML Pipeline
                          ↓
            Classification / Prediction
```

**Bạn đang ở đâu?** PCA thuộc giai đoạn **tiền xử lý và biểu diễn dữ liệu (feature transformation)**, sau khi biết làm việc với mảng, vector, ma trận và thống kê mô tả; trước các bài sử dụng dữ liệu để huấn luyện mô hình AI. PCA không tự dự đoán nhãn, phân cụm hay tìm câu trả lời đúng.

**Liên hệ với bài trước:** Một **vector** biểu diễn thông tin của một đối tượng; nhiều vector cùng độ dài xếp thành **matrix**, trong đó mỗi hàng là một đối tượng và mỗi cột là một **feature**. PCA nhận matrix đó và trả về matrix mới có ít cột hơn.

## 2. English vocabulary — Các từ cần nhận biết

| English | Hiểu bằng tiếng Việt | Gặp ở đâu? |
|---|---|---|
| **Sample / Observation** | Một mẫu, một đối tượng được ghi nhận | Mỗi dòng dữ liệu |
| **Feature** | Một đặc trưng mô tả đối tượng | Mỗi cột dữ liệu |
| **Dataset** | Tập dữ liệu | Bảng nhiều dòng và cột |
| **Vector** | Một dãy số biểu diễn một đối tượng | `np.array([80, 85, 90])` |
| **Matrix** | Bảng số hai chiều | `X.shape == (8, 5)` |
| **Mean** | Giá trị trung bình | `X.mean(axis=0)` |
| **Variance** | Độ phân tán của dữ liệu | `np.var(X, axis=0)` |
| **Standardization** | Chuẩn hóa thang đo | `StandardScaler()` |
| **Covariance** | Hai đặc trưng cùng biến thiên thế nào | `np.cov(X, rowvar=False)` |
| **Eigenvector / Eigenvalue** | Hướng chính / lượng biến thiên theo hướng đó | `np.linalg.eigh(...)` |
| **Principal Component (PC)** | Trục dữ liệu mới được PCA tạo ra | `PC1`, `PC2` |
| **Dimensionality Reduction** | Giảm số lượng đặc trưng | `PCA(n_components=2)` |
| **Explained Variance Ratio** | Tỷ lệ biến thiên được mỗi PC giữ lại | `pca.explained_variance_ratio_` |
| **Fit / Transform** | Học quy tắc từ dữ liệu / áp dụng quy tắc đó | `fit()`, `transform()` |
| **Data Leakage** | Dữ liệu kiểm tra bị dùng để học trước | Tránh bằng `Pipeline` |

## 3. Thư viện và hàm Python cần biết trước khi học PCA

Cài đặt một lần:

```bash
python -m pip install numpy scikit-learn matplotlib
```

### 3.1. NumPy: biểu diễn và kiểm tra dữ liệu

| Hàm / thuộc tính | Khi nào dùng | Ví dụ |
|---|---|---|
| `np.array()` | Chuyển dữ liệu thành matrix số | `X = np.array([[2, 3], [4, 5]])` |
| `X.shape` | Kiểm tra số mẫu, số feature | `(2, 2)` |
| `X.mean(axis=0)` | Tính trung bình từng feature | `[3., 4.]` |
| `np.var(X, axis=0)` | Đo mức độ phân tán từng feature | `[1., 1.]` |
| `np.cov(X, rowvar=False)` | Kiểm tra các cột cùng biến thiên | Matrix hiệp phương sai |
| `np.linalg.eigh(C)` | Đọc eigenvalue/eigenvector của matrix đối xứng `C` | Phân tích hướng biến thiên |

Ví dụ ngắn:

```python
import numpy as np

X = np.array([[2, 3], [4, 5]], dtype=float)
print("Samples x Features:", X.shape)  # (2, 2)
print("Mean per feature:", X.mean(axis=0))  # [3. 4.]
```

### 3.2. scikit-learn: những lệnh sẽ dùng liên tục

| Hàm / thuộc tính | Vai trò |
|---|---|
| `StandardScaler()` | Đưa các feature khác đơn vị về thang đo so sánh được |
| `scaler.fit_transform(X)` | Học trung bình/độ lệch chuẩn rồi chuẩn hóa `X` |
| `scaler.transform(X_new)` | Chuẩn hóa dữ liệu mới theo **quy tắc đã học**, không học lại |
| `PCA(n_components=2)` | Yêu cầu hai trục dữ liệu mới |
| `PCA(n_components=0.95, svd_solver="full")` | Chọn ít trục nhất để giữ tối thiểu 95% phương sai trong tập đang fit |
| `pca.fit_transform(X)` | Học trục PCA và chuyển dữ liệu sang hệ trục mới |
| `pca.transform(X_new)` | Chiếu dữ liệu mới lên các trục PCA đã học |
| `pca.components_` | Xem mỗi trục PC kết hợp các feature ban đầu ra sao |
| `pca.explained_variance_ratio_` | Xem mỗi trục giữ bao nhiêu phần phương sai |
| `Pipeline([...])` | Xử lý các bước theo đúng thứ tự, tránh học nhầm dữ liệu test |

**Ghi nhớ `fit` khác `transform`:** `fit` tạo ra quy tắc từ tập dữ liệu; `transform` áp dụng đúng quy tắc đó cho dữ liệu khác. Khi có train/test, chỉ gọi `fit` trên **train**.

## 4. Khái niệm PCA và những khái niệm con

### 4.1. Tại sao phải giảm chiều dữ liệu?

Một cửa hàng phân tích khách hàng bằng 5 thông tin: số lần truy cập, số đơn hàng, tổng chi tiêu, thời gian xem sản phẩm và số lần quay lại. Mỗi khách hàng có thể được biểu diễn bằng vector 5 số. Hàng nghìn khách hàng tạo thành matrix có **5 feature**.

Nếu hai hoặc nhiều feature phản ánh những xu hướng gần giống nhau, chúng có thể mang thông tin trùng lặp. PCA tạo các feature mới (`PC1`, `PC2`, ...) để tóm tắt phần lớn **mức biến thiên** của bảng gốc bằng ít cột hơn. Điều này giúp trực quan hóa và đôi khi giúp mô hình xử lý gọn hơn.

**Không nên suy luận:** Giữ 95% phương sai **không có nghĩa** mô hình AI đạt 95% accuracy. PCA cũng có thể làm mất tín hiệu dự đoán quan trọng.

### 4.2. Subconcept — Feature, Vector, Matrix

Một khách hàng: `customer = np.array([12, 4, 950, 18, 7])` là **vector** gồm 5 feature.

Nhiều khách hàng: `X = np.array([[...], [...], ...])` là **matrix**; `X.shape` cho biết số khách hàng và số đặc trưng. Nếu PCA trả về `X_new.shape == (100, 2)`, vẫn có **100 khách hàng**, nhưng mỗi khách hàng được mô tả bằng **2 tọa độ PC** thay vì 5 feature gốc.

### 4.3. Subconcept — Mean, Variance và Standardization

Ví dụ: cột `TotalSpending` có giá trị hàng nghìn, còn `Orders` chỉ vài đơn. Nếu dùng trực tiếp, đặc trưng có đơn vị lớn có thể chi phối PCA. Chuẩn hóa thường giúp so sánh các đặc trưng có đơn vị khác nhau.

**Công thức thể hiện ngay trong Python:**

```python
import numpy as np
from sklearn.preprocessing import StandardScaler

X = np.array([[10, 1000], [20, 2000], [30, 3000]], dtype=float)

# Vì hai cột có thang đo khác nhau, nên chuẩn hóa theo từng cột.
Z = StandardScaler().fit_transform(X)
print(np.round(Z.mean(axis=0), 5))  # [0. 0.]
print(np.round(Z.var(axis=0), 5))   # [1. 1.]
```

`StandardScaler` thực hiện phép tính tương đương `(giá_trị - trung_bình_cột) / độ_lệch_chuẩn_cột`. Không phải bài toán nào cũng bắt buộc chuẩn hóa: cần xét ý nghĩa của từng đơn vị dữ liệu.

### 4.4. Subconcept — Covariance, Eigenvalue và Eigenvector

- **Covariance** cho biết hai cột có xu hướng tăng/giảm cùng nhau hay không. Trong Python: `np.cov(Z, rowvar=False)`. Giá trị gần 0 chỉ gợi ý ít quan hệ **tuyến tính**, không chứng minh hai cột độc lập.
- **Eigenvector** có thể hiểu là một **hướng biến thiên** trong dữ liệu. Với matrix covariance đối xứng, Python đọc các hướng bằng `np.linalg.eigh(C)`.
- **Eigenvalue** cho biết phương sai ứng với hướng đó. PCA ưu tiên các hướng có eigenvalue lớn hơn.

Không cần tự giải đa thức hay tính định thức để sử dụng PCA trong bài này. Ví dụ nhận diện bằng Python:

```python
import numpy as np

Z = np.array([[-1., -1.], [0., 0.], [1., 1.]])
C = np.cov(Z, rowvar=False)  # Hai cột thay đổi cùng nhau.
values, vectors = np.linalg.eigh(C)
print("Eigenvalues:", np.round(values, 2))  # [0. 2.]
print("Number of eigenvectors:", vectors.shape[1])  # 2
```

### 4.5. Subconcept — PC1, PC2 và explained variance ratio

`PC1` là trục giữ nhiều phương sai nhất; `PC2` là trục mới vuông góc với PC1 giữ phần phương sai tiếp theo. Khi chuyển từ 5 feature xuống 2 PC, **PC1 không đồng nghĩa với “feature số 1”** và PC2 cũng không phải feature số 2.

Đọc tỷ lệ giữ lại bằng Python:

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([
    [80, 81, 72, 20, 90], [85, 88, 80, 22, 95],
    [60, 65, 72, 12, 75], [70, 72, 68, 15, 80],
    [90, 91, 88, 25, 98], [88, 87, 89, 20, 90],
    [40, 45, 50, 10, 70], [75, 73, 76, 15, 85],
], dtype=float)

Z = StandardScaler().fit_transform(X)
pca = PCA(n_components=2)
new_features = pca.fit_transform(Z)
retained = pca.explained_variance_ratio_.sum() * 100
print(new_features.shape)  # (8, 2)
print(f"Retained variance: {retained:.2f}%")  # xấp xỉ 98.65%
```

Mục đích `explained_variance_ratio_` là **đánh giá thông tin biến thiên còn lại**, không đo độ chính xác của mô hình phân loại.

### 4.6. Subconcept — Fit, Transform và Data Leakage

Nếu dùng PCA trước bước phân loại/dự đoán, dữ liệu **test** phải được giữ lại để đánh giá khách quan. Học cả thông số chuẩn hóa lẫn trục PCA trên **train** rồi mới áp dụng cho test.

```python
# Trình tự đúng khi có bài toán dự đoán:
# train_test_split(...) → model.fit(X_train, y_train)
# → model.predict(X_test)
# Pipeline sẽ giúp scaler và PCA chỉ fit trên phần train.
```

## 5. Năm tình huống lập trình trong thực tế

Mỗi tình huống đều gồm: **vấn đề → chọn khái niệm → quy trình → code có chú thích tại sao → kiểm tra kết quả**. Dữ liệu nhỏ là dữ liệu minh họa, không phải kết luận về người hay doanh nghiệp thật.

### Tình huống 1 — Phòng đào tạo muốn nhìn tổng quan hồ sơ học tập

**Vấn đề:** Bộ phận hỗ trợ sinh viên lưu 5 thông tin cho mỗi người: điểm Toán, Vật lý, tiếng Anh, giờ tự học, chuyên cần. Năm cột làm biểu đồ khó nhìn. Cần một sơ đồ 2D để khám phá các nhóm hồ sơ tương tự, **không tự động chấm điểm hay quyết định ai học yếu**.

**Chọn khái niệm:** Matrix, StandardScaler, PCA, explained variance, scatter plot.

**Quy trình:** Chuẩn bị bảng 8 × 5 → chuẩn hóa các thang đo → PCA giữ hai trục → kiểm tra phương sai → vẽ từng hồ sơ sinh viên lên 2D.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

profiles = np.array([
    [80, 81, 72, 20, 90], [85, 88, 80, 22, 95],
    [60, 65, 72, 12, 75], [70, 72, 68, 15, 80],
    [90, 91, 88, 25, 98], [88, 87, 89, 20, 90],
    [40, 45, 50, 10, 70], [75, 73, 76, 15, 85],
], dtype=float)

# Vì điểm số, giờ học và chuyên cần dùng thang khác nhau,
# cần đưa các cột về thang đo so sánh được trước PCA.
scaled = StandardScaler().fit_transform(profiles)

# Muốn vẽ trên mặt phẳng nên chọn hai trục, không phải hai cột gốc.
pca = PCA(n_components=2)
map_2d = pca.fit_transform(scaled)

# Kiểm tra xem khi chuyển từ 5 cột sang 2 cột ta giữ bao nhiêu phương sai.
print("New shape:", map_2d.shape)
print("Retained (%):", round(100 * pca.explained_variance_ratio_.sum(), 2))

plt.scatter(map_2d[:, 0], map_2d[:, 1])
for index, (x, y) in enumerate(map_2d, start=1):
    # Chú thích bằng nhãn ẩn danh; không sử dụng dữ liệu cá nhân thật.
    plt.annotate(f"SV{index}", (x, y), xytext=(4, 4), textcoords="offset points")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Student profiles after PCA")
plt.grid(alpha=0.3)
plt.show()
```

**Kiểm tra:** shape `(8, 2)`, tổng phương sai giữ lại khoảng **98.65%**. Các điểm gần nhau *trong mặt phẳng PCA* có hồ sơ tương tự theo phép biến đổi đang dùng; điều này không tự động chứng minh họ giống nhau về năng lực thực tế.

### Tình huống 2 — Nhà máy có cảm biến đo thông tin gần như trùng lặp

**Vấn đề:** Máy móc có 3 kênh cảm biến cùng đo tải hệ thống theo cách khác nhau. Kỹ sư muốn khám phá liệu tín hiệu có thể biểu diễn gọn hơn trước khi vẽ dashboard hay không.

**Chọn khái niệm:** Feature, correlation, covariance, PCA và PC1.

**Quy trình:** Gom các phép đo thành matrix → kiểm tra mức tương quan → chuẩn hóa → thử giữ một PC → xem tỷ lệ phương sai còn lại. Nếu PC1 thấp, giữ nhiều PC hơn.

```python
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Mỗi dòng là một thời điểm; ba cột là các phép đo có xu hướng giống nhau.
sensors = np.array([
    [20, 40, 200], [22, 43, 218], [25, 49, 249],
    [27, 54, 269], [30, 61, 302], [33, 67, 331],
    [35, 71, 352], [38, 76, 379],
], dtype=float)

# Xem các cột có tương quan không trước khi thử nén chúng.
correlation = np.corrcoef(sensors, rowvar=False)
print("Correlation (rounded):\n", np.round(correlation, 2))

# Đơn vị/độ lớn khác nhau nên chuẩn hóa trước khi giảm chiều.
scaled = StandardScaler().fit_transform(sensors)
pca = PCA(n_components=1)
compressed = pca.fit_transform(scaled)

print("Before / after:", sensors.shape, "→", compressed.shape)
print("Variance retained (%):", round(100 * pca.explained_variance_ratio_.sum(), 2))
```

**Kiểm tra:** shape thay từ `(8, 3)` thành `(8, 1)` và tỷ lệ giữ lại gần 100% trên bộ dữ liệu mẫu. **Không** nên vì tỷ lệ cao mà xóa cảm biến thật: những sai số hiếm hoặc điều kiện bất thường có thể bị mất.

### Tình huống 3 — Bộ phận marketing muốn khám phá nhóm khách hàng

**Vấn đề:** Mỗi khách có số lượt xem hàng, đơn hàng, chi tiêu và thời gian tương tác. Cần xem nhóm khách nào có hành vi tương tự trước khi thiết kế chiến dịch. Không thể trực quan hóa cả bốn feature trên một đồ thị 2D.

**Chọn khái niệm:** StandardScaler + PCA để tạo 2 tọa độ, sau đó **KMeans** để thử nhóm khách hàng. PCA **không tự phân cụm**.

**Quy trình:** Dữ liệu khách hàng → scale → PCA 2D → KMeans 2 nhóm trên hai tọa độ mới → xem số khách từng nhóm. Việc chọn KMeans trên PC hay toàn bộ feature cần được đánh giá riêng khi áp dụng thật.

```python
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# [số lượt xem, số đơn, chi tiêu, số phút tương tác]
customers = np.array([
    [12, 1, 120, 8], [14, 1, 150, 9], [18, 2, 230, 11],
    [20, 2, 250, 12], [16, 1, 140, 10],
    [80, 11, 1600, 60], [90, 12, 1750, 70], [76, 10, 1550, 55],
    [88, 14, 1900, 68], [95, 13, 1850, 72],
], dtype=float)

# Các cột chi tiêu và lượt xem lớn hơn số đơn, cần cùng thang đo.
scaled = StandardScaler().fit_transform(customers)

# Chọn hai PC để dễ vẽ và dễ quan sát nhóm.
locations = PCA(n_components=2).fit_transform(scaled)

# KMeans mới là bước quyết định nhãn nhóm; PCA chỉ biến đổi tọa độ.
labels = KMeans(n_clusters=2, random_state=42, n_init=10).fit_predict(locations)

print("PCA shape:", locations.shape)
print("Customers per group:", np.bincount(labels))
print("Labels:", labels)
```

**Kiểm tra:** shape `(10, 2)` và có 2 nhóm theo cấu hình `n_clusters=2`. **Nhãn `0`/`1` là tên nhóm tùy ý**, không có nghĩa khách tốt/xấu hoặc phân khúc đã được xác nhận.

### Tình huống 4 — Đội vận hành muốn giảm số cột nhưng không mất quá nhiều biến thiên

**Vấn đề:** Một dashboard bán hàng chứa 5 feature cho các cửa hàng: số khách, số đơn, doanh thu, số lượt quảng cáo được nhấp và số sản phẩm bán ra. Cần hệ thống tự chọn số PC thay vì luôn cố định hai chiều.

**Chọn khái niệm:** `PCA(n_components=0.95, svd_solver="full")` và `explained_variance_ratio_`.

**Quy trình:** Tạo matrix cửa hàng → chuẩn hóa → cho PCA chọn số PC giữ tối thiểu 95% phương sai → so sánh số cột và tổng phần trăm giữ lại.

```python
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Mỗi dòng mô phỏng một cửa hàng trong cùng kỳ báo cáo.
shops = np.array([
    [300, 45, 100000, 80, 70], [400, 62, 140000, 100, 92],
    [200, 30, 70000, 45, 51], [500, 75, 180000, 120, 110],
    [350, 52, 115000, 89, 79], [450, 68, 160000, 109, 98],
    [250, 36, 85000, 64, 60], [600, 90, 210000, 150, 125],
], dtype=float)

# Không để cột doanh thu lớn chi phối chỉ vì cách ghi đơn vị.
scaled = StandardScaler().fit_transform(shops)

# 0.95 yêu cầu giữ ít nhất 95% phương sai, KHÔNG phải 0.95 chiều.
pca = PCA(n_components=0.95, svd_solver="full")
compressed = pca.fit_transform(scaled)

print("Old / new shapes:", shops.shape, compressed.shape)
print("PC count:", pca.n_components_)
print("Variance retained (%):", round(100 * pca.explained_variance_ratio_.sum(), 2))
```

**Kiểm tra:** số cột mới không quá 5, tỷ lệ phương sai được giữ lại **tối thiểu 95%** với bộ dữ liệu minh họa này. Trong dự án thật, hãy so sánh hiệu quả dashboard hoặc mô hình trước/sau giảm chiều, không chỉ nhìn con số 95%.

### Tình huống 5 — Ứng dụng nông nghiệp nhận diện loài hoa từ số đo

**Vấn đề:** Một hệ thống phân loại hoa nhận 4 số đo trên mỗi mẫu hoa. Chúng ta muốn thử giảm còn 2 feature trước khi huấn luyện mô hình phân loại, nhưng vẫn cần đánh giá với dữ liệu chưa dùng để học.

**Chọn khái niệm:** Train/test split, `StandardScaler`, `PCA`, `Pipeline`, `LogisticRegression`.

**Quy trình:** Nạp bộ Iris → chia train/test → tạo pipeline scaler → PCA → classifier → chỉ `fit` trên train → đánh giá trên test → so sánh thử với pipeline không PCA.

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target,
    test_size=0.25, stratify=iris.target, random_state=42
)

# Pipeline bảo đảm scaler và PCA học từ train, không được nhìn test trước.
with_pca = Pipeline([
    ("scale", StandardScaler()),
    ("reduce", PCA(n_components=2)),
    ("predict", LogisticRegression(max_iter=1000)),
])

# Cùng loại classifier, nhưng giữ nguyên 4 feature để so sánh công bằng.
without_pca = Pipeline([
    ("scale", StandardScaler()),
    ("predict", LogisticRegression(max_iter=1000)),
])

with_pca.fit(X_train, y_train)
without_pca.fit(X_train, y_train)

print("Train / test:", len(X_train), len(X_test))
print("Accuracy with PCA:", round(with_pca.score(X_test, y_test), 4))
print("Accuracy without PCA:", round(without_pca.score(X_test, y_test), 4))
```

**Kiểm tra:** có `112` mẫu train và `38` mẫu test. Trong ví dụ cụ thể, điểm số hai pipeline có thể khác nhau: **PCA không bảo đảm cải thiện accuracy**. Đây là mô phỏng phân loại theo số đo, không phải AI nhận diện hoa bằng ảnh.

## 6. Những lỗi dễ gặp khi sử dụng PCA

| Tình huống | Điều cần nhớ |
|---|---|
| Số cột mới ít hơn số cột cũ | PCA tạo **feature mới**, không đơn giản xóa cột cũ |
| `explained_variance_ratio_ = 0.95` | Giữ 95% **phương sai**, không phải accuracy 95% |
| Các feature khác đơn vị | Cân nhắc `StandardScaler`; không áp dụng máy móc trong mọi ngữ cảnh |
| PCA trước bước phân loại | Chỉ `fit` trên tập train; dùng `Pipeline` để tránh leakage |
| Dữ liệu đã PCA rồi vẽ | PC1/PC2 là trục mới; không ghi nhãn chúng thành hai feature gốc |
| Các cụm xuất hiện gần nhau trên hình | Chưa đủ chứng minh các nhóm có ý nghĩa nghiệp vụ |
| PCA giữ nhiều phương sai | Không đảm bảo giữ mọi thông tin quan trọng cho nhãn dự đoán |

## 7. English multiple-choice questions — Kiểm tra kiến thức

**Q1. What is the primary purpose of PCA?**

A. To label samples automatically  
B. To reduce dimensionality by creating new components  
C. To remove every correlated sample  
D. To guarantee higher accuracy

**Q2. Which object stores the fraction of variance explained by each component?**

A. `pca.components_`  
B. `pca.classes_`  
C. `pca.explained_variance_ratio_`  
D. `pca.predict()`

**Q3. Why is `StandardScaler` often used before PCA?**

A. To make every feature an integer  
B. To ensure different feature scales do not dominate solely because of units  
C. To guarantee that no data is lost  
D. To convert all data into labels

**Q4. A dataset has shape `(100, 5)`. After `PCA(n_components=2)`, what is the transformed shape?**

A. `(5, 2)`  
B. `(2, 100)`  
C. `(100, 2)`  
D. `(100, 5)`

**Q5. What does `model.fit(X_train, y_train)` do in a scikit-learn `Pipeline`?**

A. Fits transformations and the estimator using the training set  
B. Fits the model on the entire dataset including the test set  
C. Only prints the model parameters  
D. Automatically creates the labels

**Q6. Does retaining 95% of PCA variance guarantee 95% classification accuracy?**

A. Yes, always  
B. Yes, if two components are used  
C. Only with KMeans  
D. No, variance retention and classification accuracy measure different things

**Q7. Which statement about PCA and KMeans is correct?**

A. PCA automatically assigns cluster labels  
B. PCA transforms features; KMeans can cluster the transformed features  
C. KMeans is required to compute eigenvectors  
D. Both always return the same labels

**Q8. What is data leakage in the PCA workflow?**

A. Drawing a scatter plot from training data  
B. Selecting two principal components  
C. Fitting preprocessing steps on test data before evaluating the model  
D. Calling `transform()` on new data

### Answer key & short explanations

| Question | Answer | Explanation |
|---|---|---|
| Q1 | **B** | PCA creates new lower-dimensional features. |
| Q2 | **C** | It stores explained variance ratios of the retained components. |
| Q3 | **B** | Feature scales can otherwise dominate PCA. |
| Q4 | **C** | The number of rows stays 100; columns become 2. |
| Q5 | **A** | The pipeline fits on training data. |
| Q6 | **D** | Variance and predictive accuracy are different measurements. |
| Q7 | **B** | PCA transforms; KMeans clusters. |
| Q8 | **C** | Test data must remain unseen during fitting. |

## 8. Nối sang bài tiếp theo

```text
Vector / Matrix → Mean / Variance → Covariance → PCA
                                         ↓
                       Visualization / KMeans / Classification
```

Bạn không cần thuộc cách chứng minh PCA để dùng nó đúng. Điều quan trọng là **nhận biết dữ liệu đang ở dạng nào, vì sao cần giảm chiều, lựa chọn hàm Python nào, kết quả phải kiểm tra điều gì và dữ liệu mới được đưa vào pipeline ra sao**.