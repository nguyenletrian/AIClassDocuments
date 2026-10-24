# PCA — Giảm chiều dữ liệu để nhìn rõ vấn đề trong AI

*AI / Data Science · Tài liệu tự học dành cho sinh viên · Phiên bản góp ý 03*

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

## 4. PCA và các khái niệm liên quan

Phần này đi theo đúng thứ tự: **giải thích bằng lời → ví dụ nhỏ → Python thực hiện phép tính → đọc kết quả**. Mỗi khái niệm là một mắt xích để hiểu PCA, không phải một chủ đề toán học tách rời.

### 4.1. Vì sao có lúc phải giảm số thông tin?

Một cửa hàng lưu rất nhiều thông tin về khách: số lần ghé xem, số đơn, số tiền đã chi, thời gian xem hàng, số lần quay lại… Khi dữ liệu có quá nhiều cột, chúng ta khó vẽ, khó nhìn sự khác nhau giữa các khách và đôi khi phải xử lý nhiều giá trị có xu hướng giống nhau.

**PCA** (Principal Component Analysis) tạo ra một bộ cột số **mới** để tóm tắt sự biến thiên trong các cột ban đầu. Thay vì cố chọn hai cột cũ, PCA có thể kết hợp thông tin từ nhiều cột để tạo hai tọa độ mới, phục vụ quan sát hoặc làm đầu vào cho các bước xử lý tiếp theo.

**Lưu ý quan trọng:** PCA không dự đoán ai sẽ mua hàng và không tự phân loại khách. Giữ 95% phương sai **không có nghĩa** mô hình AI dự đoán đúng 95%.

### 4.2. Feature (đặc trưng), Vector (dãy số), Matrix (bảng dữ liệu)

**Feature là gì?** Feature là **một thuộc tính dùng để mô tả một đối tượng**. Ví dụ, ứng dụng bán hàng muốn hiểu hành vi khách hàng. Đối với *mỗi khách*, cửa hàng ghi lại năm thông tin:

| Feature | Ý nghĩa | Giá trị của khách A |
|---|---|---:|
| Visits | Số lần vào cửa hàng | 12 |
| Orders | Số đơn đã đặt | 4 |
| Spending | Tổng chi tiêu, tính bằng nghìn đồng | 950 |
| ViewingMinutes | Số phút xem hàng | 18 |
| Returns | Số lần quay lại | 7 |

Như vậy, **một khách hàng có 5 feature**. Feature không có nghĩa là một thuật toán hay một công thức: đó chỉ là **thông tin đầu vào** mô tả điều chúng ta đang xét.

**Vector là gì?** Khi gom năm giá trị của *một khách* theo thứ tự cố định vào một dãy số, ta có một **vector**. Đây là cách Python biểu diễn hồ sơ một khách hàng:

```python
import numpy as np

# Thứ tự: Visits, Orders, Spending, ViewingMinutes, Returns.
# Ta lưu các giá trị theo cùng thứ tự để không nhầm "đơn hàng" với "chi tiêu".
customer = np.array([12, 4, 950, 18, 7])

print(customer.shape)  # (5,) -> một dãy có 5 giá trị
print(customer[2])     # 950 -> tổng chi tiêu (nghìn đồng)
```

**Matrix là gì?** Khi có **nhiều khách**, ta xếp vector của mỗi khách thành một **hàng**, còn mỗi feature thành một **cột**. Bảng số hai chiều này gọi là *matrix* (ma trận).

```python
import numpy as np

# Ba khách hàng, mỗi người được mô tả bằng đúng năm feature.
X = np.array([
    [12, 4, 950, 18, 7],
    [15, 5, 1200, 22, 9],
    [ 8, 2,  500, 10, 3],
], dtype=float)

print(X.shape)  # (3, 5) -> 3 khách, 5 feature
print(X[0])     # Vector của khách đầu tiên
print(X[:, 2])  # [950. 1200. 500.] -> chi tiêu của cả ba khách
```

**Liên hệ với PCA:** Hãy tưởng tượng cửa hàng có **100 khách** được mô tả bằng năm feature, nghĩa là dữ liệu có shape `(100, 5)`. Nếu áp dụng `PCA(n_components=2)` thành công, kết quả có shape `(100, 2)`:

- **100 hàng** vẫn tương ứng với đúng 100 khách ban đầu — PCA không xóa khách hàng.
- **2 cột mới** là hai tọa độ tổng hợp `PC1` và `PC2`, **không phải** hai feature ban đầu được chọn ra nguyên vẹn.
- Để đọc lại chi tiêu hay số đơn gốc, phải giữ bảng `X` ban đầu; không thể coi cột PC1 là "Spending".

**Nói ngắn gọn:** Feature là **thông tin**, vector là **một hồ sơ**, matrix là **nhiều hồ sơ**, còn PCA giúp biểu diễn mỗi hồ sơ bằng ít tọa độ tổng hợp hơn.

### 4.3. Mean (trung bình), Variance (phương sai), Standardization (chuẩn hóa)

**Mean** là trung bình của một cột, giúp biết giá trị thường gặp. **Variance** là mức độ các giá trị trong cột phân tán quanh trung bình: nếu mọi khách chi gần bằng nhau, phương sai chi tiêu sẽ nhỏ; nếu có khách chi rất ít và khách chi rất nhiều, phương sai lớn.

**Standardization** là đưa những cột dùng thang đo khác nhau về mức có thể so sánh. Ví dụ số đơn thường chỉ vài đơn, nhưng chi tiêu lại hàng trăm hoặc hàng nghìn. Nếu không xem xét đơn vị, một cột có số lớn có thể chi phối PCA chỉ do cách ghi số. `StandardScaler` tính trung bình và độ lệch chuẩn của từng cột rồi thực hiện phép tính tương đương **(giá trị − trung bình cột) / độ lệch chuẩn cột**.

**Ví dụ nhỏ — ba khách với hai thông tin:**

```python
import numpy as np
from sklearn.preprocessing import StandardScaler

# Mỗi hàng là một khách: [số đơn, chi tiêu (nghìn đồng)].
X = np.array([[1, 100], [2, 200], [3, 300]], dtype=float)

# axis=0 nghĩa là tính theo từng cột cho tất cả khách.
print("Mean:", X.mean(axis=0))  # [  2. 200.]
print("Variance:", X.var(axis=0))  # [6.666... 6666.666...]

# Hai cột có đơn vị rất khác nhau nên thử chuẩn hóa trước PCA.
scaled = StandardScaler().fit_transform(X)
print("Scaled mean:", np.round(scaled.mean(axis=0), 5))  # [0. 0.]
print("Scaled variance:", np.round(scaled.var(axis=0), 5))  # [1. 1.]
```

**Đọc kết quả:** Hai cột vẫn mô tả ba khách, nhưng giá trị đã được đổi sang thang đo chuẩn. Không phải dữ liệu nào cũng bắt buộc chuẩn hóa; hãy xét ý nghĩa đơn vị và mục tiêu phân tích.

### 4.4. Covariance (hiệp phương sai), Eigenvector (hướng riêng), Eigenvalue (giá trị riêng)

**Covariance** giúp mô tả *hai feature có xu hướng thay đổi cùng nhau hay không*. Ví dụ, nếu khách ghé cửa hàng nhiều hơn và số đơn hàng cũng thường tăng, hai cột có thể có hiệp phương sai dương. Khi một cột tăng mà cột kia thường giảm, hiệp phương sai có thể âm. Gần 0 có nghĩa ít biến thiên **tuyến tính cùng nhau**, không khẳng định các biến hoàn toàn không liên quan.

**Eigenvector** trong bối cảnh PCA có thể hình dung là một **hướng mới** mà dữ liệu trải dài theo đó. **Eigenvalue** cho biết **mức phương sai** của dữ liệu theo hướng riêng tương ứng. PCA ưu tiên hướng có eigenvalue lớn để giữ lại mức biến thiên đáng kể. Không cần tự giải phương trình ma trận trong bài này vì NumPy có hàm tính sẵn.

**Ví dụ nhỏ — lượt ghé và đơn hàng tăng cùng nhau:**

```python
import numpy as np

# Hai feature tăng gần như cùng nhau ở ba khách.
X = np.array([[1, 1], [2, 2], [3, 3]], dtype=float)

# rowvar=False: mỗi cột là một feature, mỗi hàng là một khách.
covariance = np.cov(X, rowvar=False)

# Covariance là ma trận đối xứng, vì vậy dùng eigh thay cho eig.
eigenvalues, eigenvectors = np.linalg.eigh(covariance)

print("Covariance:", covariance)
print("Eigenvalues:", np.round(eigenvalues, 2))  # [0. 2.]
print("Direction count:", eigenvectors.shape[1])  # 2
```

**Đọc kết quả:** Một hướng có phương sai lớn hơn, hướng kia gần như không có phương sai vì hai feature giống nhau trong ví dụ. PCA có thể tận dụng sự trùng lặp tuyến tính này để giảm chiều. Không dùng kết luận này để xóa dữ liệu đo lường quan trọng trong hệ thống thực.

### 4.5. Principal Component (PC1, PC2) và tỷ lệ phương sai giữ lại

**Principal Component (PC)** là **đặc trưng mới** do PCA tạo từ các đặc trưng cũ. **PC1** giữ lượng phương sai lớn nhất, **PC2** giữ lượng phương sai lớn nhất còn lại theo hướng vuông góc với PC1. Hai cột `PC1`, `PC2` không trùng với hai cột gốc.

**Explained variance ratio** là tỷ lệ phương sai được một PC giữ lại. Nếu hai PC cộng lại được 98%, điều đó chỉ nói rằng hai hướng mới giữ khoảng 98% **mức biến thiên** trên dữ liệu dùng để học PCA, không phải mô hình đúng 98%.

**Ví dụ nhỏ — rút năm thông tin sinh viên còn hai tọa độ:**

```python
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Các cột: Toán, Vật lý, Tiếng Anh, giờ học, chuyên cần.
X = np.array([
    [80, 81, 72, 20, 90], [85, 88, 80, 22, 95],
    [60, 65, 72, 12, 75], [70, 72, 68, 15, 80],
    [90, 91, 88, 25, 98], [88, 87, 89, 20, 90],
    [40, 45, 50, 10, 70], [75, 73, 76, 15, 85],
], dtype=float)

# Chuẩn hóa để điểm (0–100) và giờ học không bị lệch do thang đo.
scaled = StandardScaler().fit_transform(X)

# Cần xem dữ liệu trên đồ thị phẳng, vì vậy giữ hai tọa độ PC.
pca = PCA(n_components=2)
X_new = pca.fit_transform(scaled)

print("Before:", X.shape)  # (8, 5)
print("After:", X_new.shape)  # (8, 2)
print("Retained (%):", round(pca.explained_variance_ratio_.sum() * 100, 2))
```

**Đọc kết quả:** Vẫn có **8 sinh viên** nhưng mỗi người có **2 tọa độ PC**, thay cho năm thông tin ban đầu trong bảng biểu diễn mới. Trên dữ liệu minh họa, tỷ lệ phương sai giữ lại khoảng **98,65%**. Đây không phải thước đo chất lượng học tập của sinh viên.

### 4.6. Fit (học từ dữ liệu), Transform (áp dụng) và Data Leakage (rò rỉ dữ liệu)

**Fit** là bước để một bộ xử lý học các thông số từ dữ liệu đầu vào. Với `StandardScaler`, đó là trung bình và độ lệch chuẩn; với `PCA`, đó là các hướng PC. **Transform** là bước áp dụng những thông số đã học lên dữ liệu cần xử lý.

Khi xây dựng AI, dữ liệu **train** dùng để học, còn dữ liệu **test** để kiểm tra mô hình trên mẫu chưa thấy. Nếu để scaler hoặc PCA học cả dữ liệu test trước khi đánh giá, ta tạo **data leakage**: thông tin đáng ra phải giữ lại cho lúc kiểm tra đã lọt vào quá trình học.

**Ví dụ nhỏ — áp dụng cùng quy tắc cho khách mới:**

```python
import numpy as np
from sklearn.preprocessing import StandardScaler

# Ba khách cũ dùng để học cách chuẩn hóa.
train = np.array([[1, 100], [2, 200], [3, 300]], dtype=float)

# Một khách mới để thử; không fit lại theo dữ liệu của riêng khách này.
new_customer = np.array([[4, 350]], dtype=float)

scaler = StandardScaler()
scaler.fit(train)                     # Học chỉ từ khách đã dùng huấn luyện
new_scaled = scaler.transform(new_customer)  # Áp dụng quy tắc đã học

print("New shape:", new_scaled.shape)  # (1, 2)
```

**Khi sử dụng PCA để đánh giá mô hình dự đoán**, hãy đặt `StandardScaler` và `PCA` trong `Pipeline` rồi gọi `fit` trên tập train. Trình tự đầy đủ được minh họa ở tình huống 5.

## 5. Năm tình huống lập trình trong thực tế

Mỗi tình huống đều gồm: **vấn đề → chọn khái niệm → quy trình → code có chú thích tại sao → kiểm tra kết quả**. Dữ liệu nhỏ là dữ liệu minh họa, không phải kết luận về người hay doanh nghiệp thật.

### Tình huống 1 — Phòng đào tạo muốn nhìn tổng quan hồ sơ học tập

**Vấn đề:** Bộ phận hỗ trợ sinh viên lưu 5 thông tin cho mỗi người: điểm Toán, Vật lý, tiếng Anh, giờ tự học, chuyên cần. Năm cột làm biểu đồ khó nhìn. Cần một sơ đồ 2D để khám phá các nhóm hồ sơ tương tự, **không tự động chấm điểm hay quyết định ai học yếu**.

**Chọn khái niệm:** Matrix, StandardScaler, PCA, explained variance, scatter plot.

**Vì sao chọn cách này?** Mục tiêu của phòng đào tạo là **nhìn** sự phân bố hồ sơ trên một biểu đồ, chưa phải dự đoán kết quả học tập. Vì có 5 thông tin nên không thể đặt trực tiếp tất cả trên hai trục; PCA phù hợp để tạo hai tọa độ tổng hợp. Chọn `StandardScaler` vì giờ học và điểm số có đơn vị khác nhau. Ta **kiểm tra phương sai giữ lại trước khi diễn giải hình vẽ**, bởi bản đồ 2D có thể bỏ mất khác biệt quan trọng. Nếu cần đánh giá kết quả học tập thật, phải xây dựng và kiểm định một mô hình khác, không dựa riêng vào PCA.

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

**Vì sao chọn cách này?** Ba cảm biến cùng phản ánh tải máy nên chúng ta **nghi ngờ có thông tin trùng lặp**, không mặc định là trùng. Vì vậy phải xem `correlation` trước. Nếu nhiều cột đi cùng xu hướng, PCA thử biến ba kênh thành một tín hiệu tổng hợp để **vẽ dashboard gọn hơn**; `StandardScaler` tránh kênh có đơn vị lớn tự động chi phối kết quả. Chỉ giữ 1 PC nếu tỷ lệ phương sai hợp lý; không chọn PCA thay cho hệ thống cảnh báo, vì dao động bất thường hiếm có thể bị che khuất.

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

**Vì sao chọn cách này?** Marketing muốn **khám phá các nhóm hành vi**, nhưng bảng có bốn thuộc tính và chưa có nhãn nhóm đúng/sai. PCA chỉ giúp rút các đặc trưng thành **hai tọa độ có thể vẽ**, còn `KMeans` mới thử gom những điểm gần nhau thành nhóm. Chuẩn hóa được chọn để tổng chi tiêu không áp đảo số đơn chỉ do độ lớn của đơn vị. Chọn hai nhóm là một **giả thuyết thử nghiệm**, không phải sự thật về khách hàng; nên so sánh kết quả với phân nhóm từ dữ liệu gốc hoặc số nhóm khác trước khi dùng vào chiến dịch.

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

**Vì sao chọn cách này?** Hệ thống báo cáo cần **ít cột hơn nhưng không được giảm chiều quá mạnh**. Chọn cứng hai PC có thể hợp với đồ thị, nhưng không bảo đảm đủ mức biến thiên cho mọi bộ dữ liệu. Vì thế `n_components=0.95` phù hợp hơn: Python chọn **số PC ít nhất** để đạt ngưỡng phương sai mong muốn trên dữ liệu được `fit`. Chuẩn hóa trước để doanh thu không thắng các feature khác chỉ do đơn vị. Sau khi nén vẫn cần kiểm tra dữ liệu và hiệu quả báo cáo thật; 95% phương sai không bảo đảm mọi chỉ số kinh doanh được giữ nguyên.

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

**Vì sao chọn cách này?** Bài toán nông nghiệp đã có **nhãn loài hoa cần dự đoán**, nên chỉ PCA là chưa đủ: ta cần mô hình phân loại (`LogisticRegression`). PCA là một **phương án tiền xử lý cần kiểm chứng**, không được mặc định sẽ nâng accuracy. Ta tạo hai pipeline dùng cùng phép chia train/test: một có PCA, một giữ nguyên feature, rồi so sánh để quyết định có đáng giảm chiều không. `Pipeline` quan trọng vì bảo đảm scaler và PCA chỉ học từ **train**; nếu làm trên toàn bộ dữ liệu trước khi chia, kết quả kiểm tra sẽ không khách quan.

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

**Q9. In a customer dataset, what does the word "feature" mean?**

A. An attribute describing a customer  
B. An automatically predicted customer label  
C. A random row number  
D. The name of the PCA algorithm

**Q10. In an array with shape `(100, 5)`, what does 100 represent?**

A. Five hundred total features  
B. The number of PC axes  
C. The number of customers (samples)  
D. The number of target classes

**Q11. Which array represents ONE customer with five numeric features?**

A. `np.array([[1, 2], [3, 4]])`  
B. `np.array([12, 4, 950, 18, 7])`  
C. `np.array([["A", "B"]])`  
D. `np.array([])`

**Q12. What does `X.mean(axis=0)` calculate for a 2D dataset?**

A. One average across the entire dataset  
B. A mean for each sample (row)  
C. The number of samples  
D. The mean of each feature (column)

**Q13. What does a high variance of customer spending suggest?**

A. Every customer spends exactly the same amount  
B. The spending values differ substantially  
C. The model has high classification accuracy  
D. Customers have no recorded spending

**Q14. Why do we often set `rowvar=False` in `np.cov(X, rowvar=False)`?**

A. It treats columns as the variables/features  
B. It removes all rows with zeros  
C. It forces covariance to equal one  
D. It sorts customers by spending

**Q15. In the context of PCA, what does an eigenvector of the covariance matrix describe?**

A. A customer identifier  
B. A final prediction label  
C. A direction in feature space  
D. A Python library dependency

**Q16. A larger eigenvalue associated with a PCA direction generally means ...**

A. The direction holds more variance  
B. The direction is the final class prediction  
C. There are more customers in the dataset  
D. The accuracy is guaranteed to be higher

**Q17. A fitted PCA model receives a new customer record. What should you call to apply its existing axes?**

A. `fit_transform(new_customer)` to learn new axes  
B. `transform(new_customer_scaled)` using the same fitted preprocessing workflow  
C. `predict(new_customer)` on PCA alone  
D. `fit(new_customer)` before every prediction

**Q18. Three factory sensors are strongly correlated. What is a sensible first action?**

A. Delete two physical sensors immediately  
B. Declare all anomalies impossible  
C. Try PCA for dashboard compression, then check variance and safety requirements  
D. Replace all sensor readings with zeros

**Q19. What does `PCA(n_components=0.95, svd_solver="full")` request?**

A. Exactly 95 components  
B. A guaranteed 95% classification accuracy  
C. Two components for every dataset  
D. Enough components to retain at least 95% of fitted data variance

**Q20. What is the fairest simple way to test whether PCA helps a classifier?**

A. Use one train/test split and compare matched pipelines with and without PCA  
B. Test PCA on training data and the other model on different test data  
C. Keep PCA only when it produces a prettier scatter plot  
D. Fit preprocessing on the full dataset before creating a test set

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
| Q9 | **A** | A feature is an attribute such as visits or spending. |
| Q10 | **C** | Each row represents one customer (sample). |
| Q11 | **B** | A one-dimensional array can store five numeric features for one customer. |
| Q12 | **D** | With axis=0, NumPy calculates one mean per feature column. |
| Q13 | **B** | Large variance means spending values are more spread out. |
| Q14 | **A** | rowvar=False interprets columns as variables and rows as observations. |
| Q15 | **C** | Eigenvectors give directions of variation for the covariance matrix. |
| Q16 | **A** | A larger eigenvalue corresponds to more variance along that direction. |
| Q17 | **B** | New data must use the scaler and PCA already fitted on training data. |
| Q18 | **C** | PCA may compress correlated signals, but safety-critical details still matter. |
| Q19 | **D** | The solver selects enough PCs to reach the variance threshold. |
| Q20 | **A** | Compare both choices under the same data split and evaluation method. |

## 8. Nối sang bài tiếp theo

```text
Vector / Matrix → Mean / Variance → Covariance → PCA
                                         ↓
                       Visualization / KMeans / Classification
```

Bạn không cần thuộc cách chứng minh PCA để dùng nó đúng. Điều quan trọng là **nhận biết dữ liệu đang ở dạng nào, vì sao cần giảm chiều, lựa chọn hàm Python nào, kết quả phải kiểm tra điều gì và dữ liệu mới được đưa vào pipeline ra sao**.