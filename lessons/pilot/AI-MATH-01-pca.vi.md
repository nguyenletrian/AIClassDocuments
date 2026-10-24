# BÀI MẪU — PCA: Phân tích thành phần chính để giảm chiều dữ liệu trong AI

> **Mã bài:** AI-MATH-01 · **Trình độ:** Python căn bản + NumPy → Machine Learning nhập môn  
> **Trạng thái:** `PILOT_REVIEW` — chờ người học góp ý, **chưa phát hành đại trà**  
> **Nguồn học tập thực tế:** [`PythoClass/MON 2/3. Eigens_PCA.py`](https://github.com/nguyenletrian/PythoClass/blob/main/MON%202/3.%20Eigens_PCA.py), [`MON 2/LabSession3_4.py`](https://github.com/nguyenletrian/PythoClass/blob/main/MON%202/LabSession3_4.py), [`MON 2/Linear Algebra.py`](https://github.com/nguyenletrian/PythoClass/blob/main/MON%202/Linear%20Algebra.py).  
> **Phương pháp biên soạn:** Kế thừa chủ đề và dữ liệu sinh viên trong ghi chép, chỉnh lại lỗi/diễn giải, thêm phần toán học chuẩn, 5 bài tập và ví dụ AI do tác giả tài liệu xây dựng. Đây **không phải** bản chép nguyên văn ghi chép.  
> **Môi trường kiểm tra:** NumPy 2.3.5, scikit-learn 1.8.0; các đoạn tính toán trong phần bài tập đã được chạy đối chiếu trên môi trường Python. Hình vẽ tùy chọn cần Matplotlib.

## 1. Sau bài học, bạn làm được gì?

1. Giải thích PCA (*Principal Component Analysis* — Phân tích thành phần chính) bằng ngôn ngữ bình thường.
2. Biết khi nào PCA hữu ích và những trường hợp nó **không** bảo đảm cải thiện mô hình.
3. Hiểu mối liên hệ giữa trung bình, phương sai, ma trận hiệp phương sai, eigenvalue và eigenvector.
4. Dùng `numpy`, `StandardScaler` và `sklearn.decomposition.PCA`.
5. Kiểm tra tỷ lệ phương sai được giữ lại, vẽ dữ liệu trên mặt phẳng 2D và ghép PCA vào pipeline Machine Learning đúng cách.

**Kiến thức nên có:** Mảng NumPy, hàng/cột ma trận, hàm `mean()`, phép nhân ma trận `@`. Nếu chưa quen eigenvector, cứ bắt đầu từ trực giác ở mục 2.

## 2. Khái niệm: PCA là gì?

Giả sử chúng ta đo năng lực của mỗi sinh viên qua **5 đặc trưng**: Toán, Vật lý, Tiếng Anh, số giờ học và điểm chuyên cần. Mỗi sinh viên là một điểm trong không gian 5 chiều — con người không thể vẽ trực tiếp không gian này trên mặt giấy.

PCA tìm một **hệ trục mới**:
- Trục thứ nhất (**PC1**) là hướng mà dữ liệu biến thiên nhiều nhất.
- Trục thứ hai (**PC2**) vuông góc với PC1 và giữ được lượng biến thiên còn lại lớn nhất có thể.
- Các PC tiếp theo cũng trực giao và sắp xếp theo phương sai giảm dần.

Nếu giữ hai trục đầu, một dòng dữ liệu từ **5 số** có thể được mô tả bằng **2 tọa độ mới**. Đây là một phép **biến đổi tuyến tính không giám sát** (*unsupervised linear transformation*), không phải thuật toán phân loại.

### PCA dùng để làm gì?

- **Trực quan hóa:** biến dữ liệu nhiều đặc trưng thành tọa độ 2D/3D để quan sát nhóm, xu hướng và điểm bất thường.
- **Giảm chiều:** nén đặc trưng trước bước học máy, đôi khi giảm chi phí tính toán và bớt sự dư thừa tuyến tính.
- **Khử nhiễu:** có thể loại bỏ những hướng có phương sai rất nhỏ nếu chúng chủ yếu là nhiễu.
- **Khám phá dữ liệu:** xem đặc trưng nào đóng góp vào PC qua `components_`.

**Quan trọng:** PCA giữ *phương sai*, không trực tiếp giữ *thông tin dự đoán*. Một thành phần có phương sai nhỏ vẫn có thể chứa tín hiệu rất quan trọng cho nhãn cần dự đoán. Vì thế, không thể kết luận “PCA luôn làm AI tốt hơn”.

## 3. Toán học đằng sau PCA

Giả sử ma trận dữ liệu `X` có `n` dòng (mẫu) và `d` cột (đặc trưng).

### 3.1. Căn giữa hoặc chuẩn hóa đặc trưng

Trung bình của đặc trưng thứ `j`:

\[
\mu_j = \frac{1}{n}\sum_{i=1}^{n} x_{ij}
\]

Căn giữa: `X_c = X - μ`. Nếu các cột dùng thang đo rất khác nhau, thường dùng **StandardScaler**:

\[
z_{ij}=\frac{x_{ij}-\mu_j}{\sigma_j}
\]

`\sigma_j` trong `StandardScaler` là độ lệch chuẩn quần thể được tính trên tập `fit`. Việc **scale** không bắt buộc trong mọi bài toán PCA; quyết định phụ thuộc ý nghĩa đơn vị và mục tiêu phân tích.

### 3.2. Ma trận hiệp phương sai

Với dữ liệu đã căn giữa:

\[
C = \frac{1}{n-1}X_c^\mathsf{T}X_c
\]

`C` là ma trận `d×d`. Phần tử đường chéo là phương sai từng đặc trưng; phần tử ngoài đường chéo biểu diễn cách hai đặc trưng cùng thay đổi tuyến tính.

### 3.3. Eigenvalues và Eigenvectors

Chúng ta tìm vector riêng `v` và giá trị riêng `λ` của ma trận hiệp phương sai:

\[
Cv = \lambda v
\]

- `v` cho biết một **hướng thành phần chính**.
- `λ` cho biết lượng phương sai dọc theo hướng đó.
- Sắp `λ_1 ≥ λ_2 ≥ … ≥ λ_d`. Khi chọn `k` vector riêng lớn nhất thành `V_k`, tọa độ mới là:

\[
T = X_cV_k \qquad (n\times d)\,(d\times k)=(n\times k)
\]

PCA trong scikit-learn thường tính bằng SVD thay vì bắt buộc lập thủ công `C` rồi giải bài toán eigenvalue. Hai cách có mối liên hệ toán học chặt chẽ.

### 3.4. Tỷ lệ phương sai giữ lại

\[
\mathrm{explained\ variance\ ratio}_i
 = \frac{\lambda_i}{\sum_{j=1}^{d}\lambda_j}
\]

Tổng tỷ lệ của `k` PC cho biết phần trăm **phương sai của đầu vào** được giữ trong không gian mới. Nó **không** đồng nghĩa với phần trăm độ chính xác mô hình.

## 4. Thư viện và quy trình chuẩn trong Python

Cài đặt:

```bash
python -m pip install numpy scikit-learn matplotlib
```

| Thư viện / hàm | Công việc |
|---|---|
| `numpy.array`, `numpy.mean`, `numpy.cov` | Lưu dữ liệu và tính toán thống kê |
| `numpy.linalg.eigh` | Eigenvalues/eigenvectors cho ma trận **đối xứng** |
| `sklearn.preprocessing.StandardScaler` | Chuẩn hóa từng đặc trưng theo tập huấn luyện |
| `sklearn.decomposition.PCA` | Huấn luyện phép chiếu và giảm chiều |
| `matplotlib.pyplot` | Vẽ biểu đồ phân tán hai thành phần |
| `sklearn.pipeline.Pipeline` | Ghép biến đổi + mô hình, tránh rò rỉ dữ liệu |

**Workflow:** Chuẩn bị bảng đặc trưng → chia train/test nếu có tác vụ dự đoán → học scaler trên train → PCA `fit` trên train → `transform` dữ liệu → kiểm tra phương sai / điểm dự đoán → ghi nhận kết quả.

### Bộ dữ liệu chung cho bài tập 1, 3 và 4

Đây là **8 dòng dữ liệu sinh viên** đã có trong ghi chép `3. Eigens_PCA.py` (Toán, Vật lý, Anh văn, giờ học, chuyên cần):

```python
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

students = np.array([
    [80, 81, 72, 20, 90],
    [85, 88, 80, 22, 95],
    [60, 65, 72, 12, 75],
    [70, 72, 68, 15, 80],
    [90, 91, 88, 25, 98],
    [88, 87, 89, 20, 90],
    [40, 45, 50, 10, 70],
    [75, 73, 76, 15, 85],
], dtype=float)

features = ["Math", "Physics", "English", "StudyHours", "Attendance"]
print("Shape:", students.shape)  # (8, 5)
```

> Dữ liệu này chỉ dùng để **giảng giải**, quá nhỏ để rút ra kết luận thống kê về sinh viên thật.

## 5. Năm bài tập lập trình có lời giải mẫu

### Bài tập 1 — Hiểu dữ liệu trước khi giảm chiều

**Yêu cầu:** Từ `students`, tính trung bình từng cột, chuẩn hóa, tạo ma trận hiệp phương sai và kiểm tra tính đối xứng. Giải thích vì sao `StudyHours` và các môn học có thang đo khác nhau.

```python
# Chạy sau khối dữ liệu chung ở mục 4
means = students.mean(axis=0)
scaler = StandardScaler()
Z = scaler.fit_transform(students)
C = np.cov(Z, rowvar=False)

print("Means:", np.round(means, 2))
print("Covariance shape:", C.shape)
print("Symmetric:", np.allclose(C, C.T))
print("Diagonal:", np.round(np.diag(C), 3))
```

**Kiểm tra:** `C.shape == (5, 5)` và `Symmetric: True`. Trong ví dụ này, đường chéo xấp xỉ `1.143`, **không phải 1** vì `np.cov` dùng mẫu số `n−1`, còn `StandardScaler` dùng `n` khi tính phương sai để chuẩn hóa.

**Ứng dụng AI:** hiểu tương quan và dữ liệu dư thừa trước khi huấn luyện mô hình.

**Tự luyện thêm:** In tên cặp đặc trưng có hiệp phương sai chuẩn hóa lớn nhất ngoài đường chéo.

### Bài tập 2 — Tự triển khai PCA 2D → 1D bằng NumPy

**Yêu cầu:** Làm thủ công các bước: căn giữa → covariance → eigen → sắp thứ tự eigenvalue → lấy PC1 → chiếu dữ liệu. Dùng bộ `X` từ phần PCA trong ghi chép của bạn.

```python
import numpy as np

X = np.array([[2, 0], [0, 1], [3, 4]], dtype=float)
centered = X - X.mean(axis=0)
C = np.cov(centered, rowvar=False)

values, vectors = np.linalg.eigh(C)  # C đối xứng
order = np.argsort(values)[::-1]
values = values[order]
vectors = vectors[:, order]

pc1 = vectors[:, 0]
projected = centered @ pc1
ratio = values[0] / values.sum()

print("Eigenvalues:", np.round(values, 6))
print("New 1D coordinates:", np.round(projected, 3))
print("PC1 variance (%):", round(ratio * 100, 2))
```

**Kiểm tra:** Hai eigenvalue xấp xỉ `5.421661` và `1.245006`; PC1 giữ khoảng **81.32%** phương sai. Dấu `+/-` của vector riêng và tọa độ chiếu **có thể đảo ngược** mà vẫn đúng toán học.

**Ứng dụng AI:** hiểu toán học của PCA trước khi dùng một thư viện tự động.

**Tự luyện thêm:** Tạo `PCA(n_components=1)` từ scikit-learn và so sánh **giá trị tuyệt đối** của các tọa độ chiếu.

### Bài tập 3 — Giảm 5 đặc trưng sinh viên còn 2 chiều

**Yêu cầu:** Chuẩn hóa `students`, giảm từ `(8,5)` về `(8,2)`, in phương sai giữ lại; vẽ mỗi sinh viên thành một điểm.

```python
# Chạy sau khối dữ liệu chung ở mục 4
Z = StandardScaler().fit_transform(students)
pca = PCA(n_components=2)
points_2d = pca.fit_transform(Z)

print("New shape:", points_2d.shape)
print("Explained ratio:", np.round(pca.explained_variance_ratio_, 4))
print("Total retained (%):",
      round(pca.explained_variance_ratio_.sum() * 100, 2))

import matplotlib.pyplot as plt

plt.scatter(points_2d[:, 0], points_2d[:, 1])
for i, (x, y) in enumerate(points_2d, start=1):
    plt.annotate(f"SV{i}", (x, y), xytext=(4, 4),
                 textcoords="offset points")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA: student features 5D → 2D")
plt.grid(alpha=0.3)
plt.show()
```

**Kiểm tra:** `points_2d.shape == (8,2)`; PC1 ≈ **93.99%**, PC2 ≈ **4.67%**; tổng ≈ **98.65%** phương sai. Ở phần vẽ, tọa độ `y` **phải lấy từ cột 1** của `points_2d`. Trong ghi chép gốc, lời gọi `plt.text` vô tình lấy cột 0 cho cả `x` lẫn `y`; ví dụ đã sửa.

**Ứng dụng AI:** biểu diễn dữ liệu nhiều chiều trên một mặt phẳng để quan sát cấu trúc và nhóm mẫu.

**Tự luyện thêm:** Đổi điểm hiển thị thành màu theo một nhãn giả lập và giải thích vì sao PCA không sử dụng nhãn đó.

### Bài tập 4 — Chọn bao nhiêu PC là đủ?

**Yêu cầu:** So sánh giữ 1 PC, 2 PC và ngưỡng giữ ít nhất 95% phương sai. Không chọn số chiều chỉ vì “2D dễ vẽ”.

```python
# Chạy sau khối dữ liệu chung ở mục 4
Z = StandardScaler().fit_transform(students)
for target in [1, 2, 0.95]:
    model = PCA(n_components=target, svd_solver="full").fit(Z)
    kept = model.n_components_
    retained = model.explained_variance_ratio_.sum()
    print(f"target={target!s:>4} -> PCs={kept}, "
          f"retained={retained:.2%}")
```

**Kiểm tra:** với chính bộ dữ liệu này, `1 PC ≈ 93.99%`; `2 PC ≈ 98.65%`; ngưỡng `0.95` sẽ chọn **2 PC**. `n_components=0.95` là ngưỡng phương sai, không phải “0.95 chiều”.

**Ứng dụng AI:** cân bằng độ gọn của đặc trưng với mức thông tin thống kê được giữ lại.

**Tự luyện thêm:** Thử ngưỡng `0.90` và dự đoán số PC trước khi chạy.

### Bài tập 5 — Dùng PCA trong pipeline phân loại của AI

**Yêu cầu:** Huấn luyện `StandardScaler → PCA(2) → LogisticRegression` trên bộ Iris có sẵn trong scikit-learn. **Chia train/test trước**, để `Pipeline` chỉ học các tham số chuẩn hóa/PCA từ tập train.

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.25,
    stratify=iris.target, random_state=42
)

model = Pipeline([
    ("scale", StandardScaler()),
    ("pca", PCA(n_components=2)),
    ("classifier", LogisticRegression(max_iter=1000)),
])

model.fit(X_train, y_train)
print("Train size:", len(X_train))
print("Test size:", len(X_test))
print("Test accuracy:", round(model.score(X_test, y_test), 4))
```

**Kiểm tra:** `112` mẫu train, `38` mẫu test; trong môi trường kiểm tra của bản mẫu, độ chính xác test ≈ **0.8947**. Điểm số có thể thay đổi theo phiên bản thư viện hoặc thay đổi dữ liệu/chia tập.

**Ứng dụng AI:** PCA như một bước tiền xử lý bên trong pipeline phân loại. **Không `fit_transform` trên toàn bộ dữ liệu rồi mới chia train/test**, vì đó là *data leakage*.

**Tự luyện thêm:** So sánh pipeline **có** PCA và **không** PCA trên cùng tập chia; mô tả cả điểm accuracy lẫn số đặc trưng đầu vào của bộ phân loại.

## 6. Những nhầm lẫn thường gặp

| Nhầm lẫn | Cách hiểu đúng |
|---|---|
| PCA là thuật toán phân loại | PCA là biến đổi đặc trưng không giám sát |
| PC1 và PC2 tương ứng hai đặc trưng cũ | Mỗi PC thường là **tổ hợp tuyến tính** của nhiều đặc trưng |
| Hai PC giữ 98.65% nghĩa là AI đúng 98.65% | Đó chỉ là tỷ lệ **phương sai**, không phải accuracy |
| Bắt buộc StandardScaler mọi lúc | Quyết định scale tùy thang đo và mục tiêu |
| Vector riêng đổi dấu là lỗi | `v` và `-v` biểu diễn cùng trục PCA |
| `fit` PCA trên tất cả dữ liệu rồi chia train/test | Khi đánh giá mô hình dự đoán, hãy `fit` trong pipeline trên train để tránh leakage |
| Phương sai ít nghĩa là nhiễu | Chưa chắc: tín hiệu nhãn có thể nằm ở PC phương sai thấp |

## 7. Kiến thức AI liên quan

- **Computer Vision:** PCA có thể biểu diễn vector ảnh nhiều chiều bằng ít chiều hơn (ví dụ mô hình *eigenfaces* cổ điển), nhưng không thay thế biểu diễn sâu hiện đại.
- **Phát hiện bất thường:** nếu dùng PCA để tái tạo dữ liệu, mẫu có sai số tái tạo lớn *có thể* là điểm bất thường — cần kiểm định theo bài toán.
- **Clustering:** có thể dùng PCA để trực quan hóa cluster hoặc tiền xử lý, nhưng PCA không tự tạo cluster.
- **Mô hình dự đoán:** thử kết hợp PCA với hồi quy/phân loại; chọn số PC bằng đánh giá trên train/validation.

### Thuật ngữ cần nhớ

| English | Tiếng Việt |
|---|---|
| Feature | Đặc trưng |
| Dimensionality reduction | Giảm chiều dữ liệu |
| Centering | Căn giữa dữ liệu |
| Scaling / Standardization | Đưa đặc trưng về thang đo chuẩn |
| Covariance | Hiệp phương sai |
| Eigenvalue / Eigenvector | Giá trị riêng / Vector riêng |
| Principal component | Thành phần chính |
| Explained variance ratio | Tỷ lệ phương sai giải thích được |
| Data leakage | Rò rỉ thông tin từ dữ liệu đánh giá |

## 8. Tự đánh giá và hướng phát triển

1. Vì sao trước PCA ta thường phải cân nhắc `StandardScaler`?  
2. Tại sao hai giá trị eigenvector đối dấu vẫn có thể đúng?  
3. `components_` khác `explained_variance_ratio_` thế nào?  
4. Nếu PCA giữ 99% phương sai, có chắc mô hình classification sẽ đạt 99% accuracy không?  
5. Trong `Pipeline`, bước nào được `fit` trên tập test?

**Đáp án ngắn:** (1) các feature khác thang đo có thể chi phối phương sai; (2) hướng trục không phụ thuộc chọn dấu; (3) hướng thành phần so với tỷ trọng phương sai; (4) không; (5) **không có bước nào** được fit trên test.

## 9. Nguồn, hiệu đính và giới hạn

**Có trong PythoClass:** định nghĩa PCA, Eigenvalue/Eigenvector, thao tác NumPy; mẫu PCA `X=[[2,0],[0,1],[3,4]]`; `PCA(n_components=2)`; `StandardScaler`; bảng 8 sinh viên × 5 đặc trưng; cách đọc `components_` và `explained_variance_ratio_`; ví dụ vẽ biểu đồ.

**Biên soạn / mở rộng có chủ đích:** diễn giải công thức thống kê chuẩn, cảnh báo leakage, bài tập so sánh `n_components`, pipeline phân loại Iris, phân biệt phương sai và accuracy, gợi ý ứng dụng AI.

**Điểm đã hiệu đính từ ghi chép:** ví dụ vẽ vị trí nhãn sinh viên; giải thích StandardScaler và covariance; cách chọn các PC và mục đích giảm chiều. Những phần trong ghi chép chỉ là phác thảo được bổ sung định nghĩa, không coi là trích dẫn chính xác một lời giảng bên ngoài.

**Giới hạn:** Đây là bài mẫu theo **ba file nguồn được đọc đầy đủ**, chưa phải kết quả rà soát hết mọi file `.ipynb`, `.py`, `.docx`, `.pptx`, `.xlsx` của repo. Việc lập bản đồ toàn bộ chủ đề sẽ được thực hiện riêng sau khi bố cục mẫu được duyệt.

---

**Trạng thái nghiệm thu:** `PILOT_REVIEW`. Người học có thể góp ý về độ dài, mức độ toán học, ngôn ngữ, cách đặt bài tập và mức chi tiết của lời giải trước khi nhân rộng ra toàn bộ PythoClass.
