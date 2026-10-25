# PY-41 — Phân hoạch dữ liệu, classification và clustering


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Train set** — tập huấn luyện; **Test set** — tập kiểm tra.

`Set/NumPy → Train/Test → Preprocessing → Classification/Clustering`

**Học xong dùng để làm gì?** Tách tập dữ liệu đúng cách, huấn luyện mô hình và đánh giá kết quả trên dữ liệu độc lập.

**Kết nối kiến thức tiếp theo:** PY-42 chuẩn bị dữ liệu chữ thành token và đặc trưng phục vụ mô hình.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Khái niệm |
|---|---|---|
| Train set | tập huấn luyện | Mẫu dùng để học tham số mô hình |
| Test set | tập kiểm tra | Mẫu giữ lại chỉ để đánh giá mô hình |
| Classification | phân loại | Dự đoán nhãn rời rạc từ feature |
| Clustering | phân cụm | Thử nhóm mẫu giống nhau mà không cần nhãn sẵn |

## 3. Thư viện và hàm Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cách viết | Khi nào dùng, ý nghĩa tham số |
|---|---|
| `train_test_split(...,test_size=.25,stratify=y)` | Chia train/test có xét tỷ lệ nhãn |
| `Pipeline([('scale',...),('model',...)])` | Fit chỉ trên train để giảm leakage |
| `LogisticRegression(max_iter=1000)` | Mô hình phân loại có giám sát |
| `KMeans(n_clusters=2,random_state=42,n_init=10)` | Phân nhóm không giám sát, số nhóm là giả định |

## 4. Khái niệm chính và liên quan

**Mạch kiến thức:** Để đánh giá mô hình đáng tin, trước hết chia dữ liệu thành train và test. Classification học cách đoán nhãn từ ví dụ đã có nhãn; clustering nhóm các điểm tương tự khi chưa có nhãn. Một test độc lập giúp tránh tự đánh giá trên dữ liệu đã học.

### 4.1. Train set — Tập để học tham số

**Từ vựng:** **Train set**.

Dữ liệu train chứa các hàng quan sát dùng để mô hình **học** tham số. Trong bảng Iris, mỗi hàng là một hoa, bốn cột là kích thước tính bằng cm và nhãn là loài. Nếu lấy 112 hoa để train thì các đặc trưng của chúng được đưa vào `fit`; không đưa test vào học scaler hoặc chỉnh siêu tham số.

```python
# Mục đích: Tập để học tham số.
from sklearn.datasets import load_iris

data = load_iris()
print(data.data.shape, data.target.shape)
```

**Kết quả khi chạy:**

```text
(150, 4) (150,)
```

150 hàng hoa, bốn cột đặc trưng và một nhãn cho mỗi hàng.

### 4.2. Test set — Tập chỉ dùng để đánh giá cuối

**Từ vựng:** **Test set**.

Test set là các mẫu giữ lại, không dùng để fit hay chọn cách xử lý. Một cách kiểm tra tối thiểu là **ID train không trùng ID test**. Điều đó chưa đủ loại rò rỉ qua các mẫu liên quan, đặc trưng sinh từ tương lai, hoặc bản ghi trùng nội dung nhưng khác ID.

```python
# Mục đích: Tập chỉ dùng để đánh giá cuối.
train_ids = {1, 2, 3}
test_ids = {4, 5}
print(train_ids.isdisjoint(test_ids))
```

**Kết quả khi chạy:**

```text
True
```

Không có ID xuất hiện ở cả train và test; vẫn cần kiểm tra rò rỉ gián tiếp.

### 4.3. Classification — Dự đoán nhãn đã biết

**Từ vựng:** **Classification**.

Classification là học có giám sát: từ **X là các đặc trưng**, mô hình dự đoán **y là nhãn**. Iris có ba nhãn loài là 0,1,2. Một classifier học từ những hàng đã có nhãn rồi dự đoán loài của hoa mới; khác regression dự đoán giá trị liên tục và không thể thay độ chính xác bằng khoảng cách giữa nhãn số.

```python
# Mục đích: Dự đoán nhãn đã biết.
from sklearn.datasets import load_iris

data = load_iris()
print(sorted(set(data.target.tolist())))
```

**Kết quả khi chạy:**

```text
[0, 1, 2]
```

Ba số là mã phân loại ba loài, không phải các đại lượng đo theo cm.

### 4.4. Clustering — Nhóm mẫu khi chưa có nhãn

**Từ vựng:** **Clustering**.

Clustering là học không giám sát: tìm các nhóm điểm gần nhau trong không gian đặc trưng, **không dùng nhãn thật để huấn luyện**. Ví dụ hai cụm điểm quanh `[0,0]` và `[10,10]`; KMeans tìm hai tâm nhóm. Mã cụm `0`/`1` chỉ là định danh tùy cách khởi tạo, không đồng nghĩa nhãn lớp 0/1 của bài phân loại.

```python
# Mục đích: Nhóm mẫu khi chưa có nhãn.
import numpy as np
from sklearn.cluster import KMeans

X = np.array([[0, 0], [0, 1], [10, 10], [10, 11]])
labels = KMeans(n_clusters=2, random_state=42, n_init=10).fit_predict(X)
print(len(set(labels.tolist())))
```

**Kết quả khi chạy:**

```text
2
```

KMeans tìm được hai cụm; mã số gắn cho từng cụm có thể đổi.

## 5. Năm tình huống chia dữ liệu, classification và clustering — từ 10 đến 20 hồ sơ

### Tình huống 1 — Cấp 1: Giữ riêng 2 trong 10 học viên để đánh giá

**Từ vựng trong mục:** **Train** — tập huấn luyện; **Test** — tập đánh giá; **Disjoint** — không trùng.

**Tình huống thực tế:** Trung tâm đào tạo có **10 hồ sơ H01–H10**. Mỗi hồ sơ ghi mã học viên, số giờ luyện tập **(giờ/tuần)** và điểm kiểm tra **(thang 10)**. Nhóm muốn dùng **8 học viên đầu** để chuẩn bị mô hình và giữ riêng **2 người cuối** để đánh giá sau này. Trước khi học, cần kiểm tra không có mã nào vừa nằm trong train vừa nằm trong test và hai nhóm vẫn bao phủ đủ 10 người.

**Vì sao chọn cách này?** **Train** là dữ liệu được dùng khi học quy tắc; **test** được giữ lại để đo khả năng áp dụng cho người **chưa gặp lúc học**. `records[:8]` lấy 8 hồ sơ đầu còn `records[8:]` lấy hai hồ sơ cuối; đây là **chia theo thứ tự mã**, không phải lấy ngẫu nhiên. `set` các mã giúp kiểm `isdisjoint()` (hai nhóm không chung mã) và phép hợp giúp xác nhận đủ 10 người. Việc hai nhóm không trùng là điều kiện cần, nhưng nếu hồ sơ được sắp theo ngày hay nhãn thì cách cắt này vẫn có thể làm hai nhóm khác nhau thiếu đại diện.

**Quy trình:**
1. Tạo 10 bộ ID–giờ–điểm, mỗi hàng là một người.
2. Chia 8 dòng đầu train, 2 dòng cuối test.
3. Kiểm tra giao ID bằng Set và số người của cả hai nhóm.

```python
records = []
for i in range(1, 11):
    records.append({"id":f"H{i:02d}", "hours":i, "score":min(10, 4+i//2)})
train = records[:8]
test = records[8:]
train_ids = set()
for row in train:
    train_ids.add(row["id"])
test_ids = set()
for row in test:
    test_ids.add(row["id"])
if len(records) != 10:
    raise ValueError("Cần đủ 10 hồ sơ để chia Train/Test.")
print("Hồ sơ:", len(records))
print("Train/test:", len(train), len(test))
print("ID không giao nhau:", train_ids.isdisjoint(test_ids))
print("Phủ toàn bộ:", len(train_ids | test_ids) == 10)
```

**Kết quả khi chạy:**

```text
Hồ sơ: 10
Train/test: 8 2
ID không giao nhau: True
Phủ toàn bộ: True
```

ID rời nhau chỉ là điều kiện cần: nếu một người có hai ID khác nhau hoặc đặc trưng chứa thông tin tương lai, vẫn có thể xảy ra rò rỉ.

### Tình huống 2 — Cấp 2: Chia phân tầng 12 hồ sơ cân bằng nhãn

**Từ vựng trong mục:** **Stratify** — giữ tỷ lệ nhãn; **Random state** — hạt giống ngẫu nhiên.

**Tình huống thực tế:** Đội tư vấn có **12 hồ sơ S01–S12**, mỗi người có điểm hoạt động và **nhãn 0** (chưa đăng ký) hoặc **1** (đã đăng ký). Có đúng **6 người ở mỗi nhãn**, nhưng nếu chia tùy tiện thì nhóm kiểm tra chỉ có một nhãn, khó đánh giá công bằng. Nhóm cần chia thành **8 hồ sơ train và 4 hồ sơ test**, giữ được cả nhãn 0 và 1 ở mỗi phần, đồng thời không dùng lại cùng khách.

**Vì sao chọn cách này?** **Phân tầng (stratify)** là chia mẫu sao cho **tỷ lệ hai nhãn** được duy trì trong những phần được tạo, khi số lượng cho phép. `train_test_split(..., test_size=4, stratify=y)` chia **12 khách** thành 8 người học và 4 người đánh giá; nhãn được dùng để **quyết định tỷ lệ chia**, không có nghĩa mô hình đã học từ nhãn test. `random_state=42` giữ kết quả chia có thể lặp lại. Chương trình đếm riêng số 0/1 của train và test và kiểm tập mã không giao nhau; mẫu 12 vẫn quá nhỏ để kết luận chắc chắn hiệu quả mô hình ngoài thực tế.

**Quy trình:**
1. Tạo 12 mã, đặc trưng điểm và nhãn nhị phân.
2. Chia bằng stratify với test_size=4, giữ ID tương ứng.
3. Đếm nhãn train/test, xác nhận ID không trùng và mỗi nhóm có hai nhãn.

```python
from sklearn.model_selection import train_test_split
records = [{"id":"S01","score":5,"label":0},{"id":"S02","score":6,"label":1},{"id":"S03","score":7,"label":0},{"id":"S04","score":8,"label":1},{"id":"S05","score":9,"label":0},{"id":"S06","score":10,"label":1},{"id":"S07","score":11,"label":0},{"id":"S08","score":12,"label":1},{"id":"S09","score":13,"label":0},{"id":"S10","score":14,"label":1},{"id":"S11","score":15,"label":0},{"id":"S12","score":16,"label":1}]
ids = []
y = []
for row in records:
    ids.append(row["id"])
    y.append(row["label"])
train_ids, test_ids, y_train, y_test = train_test_split(
    ids, y, test_size=4, random_state=42, stratify=y)
if len(records) != 12:
    raise ValueError("Cần đủ 12 hồ sơ và nhãn.")
print("Hồ sơ:", len(records))
print("Train/test:", len(train_ids), len(test_ids))
print("Nhãn train 0/1:", y_train.count(0), y_train.count(1))
print("Nhãn test 0/1:", y_test.count(0), y_test.count(1))
print("ID không giao nhau:", set(train_ids).isdisjoint(test_ids))
```

**Kết quả khi chạy:**

```text
Hồ sơ: 12
Train/test: 8 4
Nhãn train 0/1: 4 4
Nhãn test 0/1: 2 2
ID không giao nhau: True
```

Phân tầng dùng nhãn **chỉ để quyết định cách chia**, không có nghĩa mô hình được nhìn nhãn test khi fit.

### Tình huống 3 — Cấp 3: Huấn luyện classifier trong Pipeline với 15 bông hoa

**Từ vựng trong mục:** **Classification** — phân loại có nhãn; **Pipeline** — chuỗi xử lý; **Leakage** — rò rỉ thông tin.

**Tình huống thực tế:** Nhóm học máy chuẩn bị **15 hồ sơ hoa F01–F15**, mỗi bông được ghi **chiều dài, chiều rộng cánh hoa (cm)** và nhãn thuộc **một trong ba loài 0, 1, 2**. Mỗi loài có 5 bông. Họ muốn học cách phân loại từ **9 mẫu train**, giữ **6 mẫu test** để thử dự đoán, và đặc biệt tránh dùng số đo của hoa test khi tính mức trung bình/độ phân tán cho bước chuẩn hóa.

**Vì sao chọn cách này?** **StandardScaler** chuẩn hóa số đo bằng các thông số như **trung bình** và **độ lệch chuẩn** học từ dữ liệu. Nếu tính các thông số ấy trên **cả 15 bông** trước khi chia, thông tin từ 6 hoa test đã đi vào quá trình chuẩn bị mô hình: đó là **rò rỉ dữ liệu (data leakage)**. `Pipeline` gói scaler và `LogisticRegression`: lệnh `fit` chỉ chạy trên 9 hoa train rồi áp **cùng phép chuẩn hóa đã học** lên 6 hoa test khi dự đoán. `stratify=y` giữ các loài có đại diện khi chia; `random_state=42` giúp chạy lại cùng một cách chọn. Điểm accuracy đo trên test là số dự đoán đúng trong **6 mẫu**, không đảm bảo tỷ lệ đúng của thế giới thật.

**Quy trình:**
1. Tạo 15 dòng có đủ ID, hai số đo cm, ba nhãn.
2. Tách train/test phân tầng 9/6 và ghép `StandardScaler` + `LogisticRegression`.
3. Fit chỉ trên train, kiểm scaler mean bằng train mean và in số dự đoán/độ chính xác test.

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
records = [{"id":"F01","length_cm":1.5,"width_cm":0.5,"species":0},{"id":"F02","length_cm":1.6,"width_cm":0.53,"species":0},{"id":"F03","length_cm":1.7,"width_cm":0.56,"species":0},{"id":"F04","length_cm":1.8,"width_cm":0.59,"species":0},{"id":"F05","length_cm":1.9,"width_cm":0.62,"species":0},{"id":"F06","length_cm":4.5,"width_cm":1.5,"species":1},{"id":"F07","length_cm":4.6,"width_cm":1.53,"species":1},{"id":"F08","length_cm":4.7,"width_cm":1.56,"species":1},{"id":"F09","length_cm":4.8,"width_cm":1.59,"species":1},{"id":"F10","length_cm":4.9,"width_cm":1.62,"species":1},{"id":"F11","length_cm":7.5,"width_cm":2.5,"species":2},{"id":"F12","length_cm":7.6,"width_cm":2.53,"species":2},{"id":"F13","length_cm":7.7,"width_cm":2.56,"species":2},{"id":"F14","length_cm":7.8,"width_cm":2.59,"species":2},{"id":"F15","length_cm":7.9,"width_cm":2.62,"species":2}]
features = []
labels = []
for row in records:
    features.append([row["length_cm"], row["width_cm"]])
    labels.append(row["species"])
X = np.array(features)
y = np.array(labels)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=6,
                                                  stratify=y,random_state=42)
model = Pipeline([("scale", StandardScaler()),
                  ("classifier", LogisticRegression(max_iter=1000))])
model.fit(X_train,y_train)
predicted = model.predict(X_test)
if len(records) != 15:
    raise ValueError("Cần đủ 15 mẫu hoa có nhãn.")
print("Hoa:", len(records))
print("Train/test:", len(X_train), len(X_test))
print("Scaler chỉ fit train:", bool(np.allclose(model.named_steps["scale"].mean_, X_train.mean(axis=0))))
print("Đã dự đoán:", len(predicted))
print("Accuracy hợp lệ:", bool(0 <= np.mean(predicted==y_test) <= 1))
```

**Kết quả khi chạy:**

```text
Hoa: 15
Train/test: 9 6
Scaler chỉ fit train: True
Đã dự đoán: 6
Accuracy hợp lệ: True
```

Accuracy chỉ được tính từ **sáu hoa test**, không phải bằng chứng kết quả sẽ giữ nguyên ngoài dữ liệu mô phỏng.

### Tình huống 4 — Cấp 4: KMeans tìm hai cụm trong 18 tọa độ không có nhãn

**Từ vựng trong mục:** **Clustering** — gom cụm không giám sát; **Centroid** — tâm cụm.

**Tình huống thực tế:** Kho robot ghi **18 vị trí vật thể trên sàn**, mỗi vị trí là hai tọa độ **x, y (mét)**. Có **9 vật thể gần (1,1)** và **9 vật thể gần (11,11)**, nhưng bảng không có nhãn 'vùng gần' hay 'vùng xa'. Người vận hành muốn chương trình tự tìm **hai cụm vị trí**, báo số vật thể từng cụm và vị trí tâm theo trục x, không tự gọi mã cụm 0 là bên trái.

**Vì sao chọn cách này?** **KMeans** là thuật toán **phân cụm không giám sát**: nó nhận tọa độ, tìm hai tâm và đưa mỗi điểm vào cụm gần tâm thích hợp, **không cần nhãn đúng**. Ở đây hai vùng trên sàn cách nhau khá xa nên yêu cầu **hai cụm** là giả định dễ quan sát; `n_clusters=2` không phải số cụm mà thuật toán tự xác nhận cho mọi dữ liệu. `random_state=42` và `n_init=10` giúp việc khởi tạo và lặp thử có thể tái lập tốt hơn. Số nhãn cụm `0` và `1` chỉ là **tên do thuật toán gán**, có thể đổi chỗ; vì vậy dùng `sorted` để so kích thước và sắp **tâm theo tọa độ x** thay vì gán cố định 0 là vùng trái.

**Quy trình:**
1. Tạo 18 điểm có đơn vị m, không tạo nhãn để fit.
2. Dùng KMeans với 2 nhóm và random_state cố định.
3. Sắp kích thước hai nhóm, sắp tâm theo tọa độ x để báo cáo ổn định.

```python
import numpy as np
from sklearn.cluster import KMeans
points = np.array([[0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2],[10,10],[11,10],[12,10],[10,11],[11,11],[12,11],[10,12],[11,12],[12,12]],dtype=float)
model = KMeans(n_clusters=2, random_state=42, n_init=10).fit(points)
counts = sorted(np.bincount(model.labels_).tolist())
centers = model.cluster_centers_[np.argsort(model.cluster_centers_[:,0])]
if points.shape != (18,2):
    raise ValueError("Cần đúng 18 điểm để phân cụm.")
print("Vật thể:", len(points))
print("Số cụm:", len(counts))
print("Vật thể mỗi cụm:", counts)
center_positions = []
for value in centers[:, 0]:
    center_positions.append(round(float(value), 1))
print("Tâm theo trục x:", center_positions)
```

**Kết quả khi chạy:**

```text
Vật thể: 18
Số cụm: 2
Vật thể mỗi cụm: [9, 9]
Tâm theo trục x: [1.0, 11.0]
```

Người học không được gọi cụm số 0 là loài số 0 chỉ vì hai hệ thống cùng dùng số; nhãn cụm chỉ là định danh.

### Tình huống 5 — Cấp 5: So dự đoán có giám sát và gom cụm trên 20 khách hàng

**Từ vựng trong mục:** **Classification vs. clustering** — phân loại so với gom cụm; **Adjusted Rand Index** — độ phù hợp cụm không lệ thuộc mã.

**Tình huống thực tế:** Đội phân tích có **20 hồ sơ khách H01–H20**, mỗi hồ sơ gồm hai chỉ số hành vi x/y **không đơn vị** và nhãn tham chiếu **0 hoặc 1** (mỗi nhãn 10 khách). Họ muốn so hai công việc: **phân loại** học nhãn từ **16 hồ sơ train** rồi kiểm trên **4 test**, còn **phân cụm** tìm hai nhóm chỉ từ các chỉ số x/y. Cần báo kết quả của mỗi cách đúng ý nghĩa, không nhầm tên cụm do máy tự đặt với nhãn tham chiếu.

**Vì sao chọn cách này?** **Classification** giải bài toán có **nhãn đúng đã biết**; mô hình `StandardScaler` + `LogisticRegression` học từ **16 hồ sơ** rồi tính **accuracy trên 4 hồ sơ test** chưa dùng học. **Clustering** dùng `KMeans` chỉ trên đặc trưng x/y của **20 hồ sơ**, không đưa nhãn tham chiếu vào `fit_predict`. Chỉ **sau khi tìm cụm**, `adjusted_rand_score` (ARI) dùng nhãn thật để **đối chiếu độ tương hợp hai cách chia**, đồng thời không bị ảnh hưởng bởi việc gọi cụm là 0 hay 1. Đây là hai nhiệm vụ và hai cách đánh giá khác nhau: accuracy không thay thế ARI, còn ARI cao không có nghĩa KMeans đã được dạy nhãn.

**Quy trình:**
1. Tạo 20 hàng có ID, x/y, nhãn; tách train/test phân tầng.
2. Fit Pipeline classifier trên 16 train và đánh giá 4 test.
3. Fit KMeans trên toàn bộ 20 đặc trưng **không có nhãn**, tính ARI chỉ để đối chiếu kết quả.

```python
import numpy as np
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import adjusted_rand_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
records = [{"id":"H01","x":0,"y":1,"label":0},{"id":"H02","x":0.2,"y":1,"label":0},{"id":"H03","x":0.4,"y":1,"label":0},{"id":"H04","x":0.6000000000000001,"y":1,"label":0},{"id":"H05","x":0.8,"y":1,"label":0},{"id":"H06","x":0,"y":1.2,"label":0},{"id":"H07","x":0.2,"y":1.2,"label":0},{"id":"H08","x":0.4,"y":1.2,"label":0},{"id":"H09","x":0.6000000000000001,"y":1.2,"label":0},{"id":"H10","x":0.8,"y":1.2,"label":0},{"id":"H11","x":8,"y":9,"label":1},{"id":"H12","x":8.2,"y":9,"label":1},{"id":"H13","x":8.4,"y":9,"label":1},{"id":"H14","x":8.6,"y":9,"label":1},{"id":"H15","x":8.8,"y":9,"label":1},{"id":"H16","x":8,"y":9.2,"label":1},{"id":"H17","x":8.2,"y":9.2,"label":1},{"id":"H18","x":8.4,"y":9.2,"label":1},{"id":"H19","x":8.6,"y":9.2,"label":1},{"id":"H20","x":8.8,"y":9.2,"label":1}]
features = []
labels = []
for row in records:
    features.append([row["x"], row["y"]])
    labels.append(row["label"])
X = np.array(features, dtype=float)
y = np.array(labels)
ids = np.arange(len(records))
train, test = train_test_split(ids, test_size=4, stratify=y, random_state=42)
clf = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
clf.fit(X[train], y[train])
accuracy = float(clf.score(X[test], y[test]))
clusters = KMeans(n_clusters=2,random_state=42,n_init=10).fit_predict(X)
ari = adjusted_rand_score(y,clusters)
if len(records) != 20 or not set(train).isdisjoint(test):
    raise ValueError("Cần 20 hồ sơ và Train/Test không được trùng mẫu.")
print("Khách:", len(records))
print("Train/test:", len(train), len(test))
print("Accuracy test hợp lệ:", 0 <= accuracy <= 1)
print("Cụm:", len(set(clusters.tolist())))
print("ARI khi đối chiếu:", f"{ari:.2f}")
```

**Kết quả khi chạy:**

```text
Khách: 20
Train/test: 16 4
Accuracy test hợp lệ: True
Cụm: 2
ARI khi đối chiếu: 1.00
```

Độ phù hợp cao ở ví dụ vì **hai cụm giả lập được tách xa nhau**. Kết quả gom cụm không tự chứng minh nhãn tham chiếu là bản chất của khách hàng.

## 6. Sai lầm thường gặp

- Dữ liệu test không được dùng để fit scaler hoặc chọn siêu tham số; cần tách trước khi tiền xử lý học tham số.
- ID không trùng vẫn có thể rò rỉ qua bản ghi liên quan hoặc giá trị tương lai.
- Classification học từ nhãn y; clustering nhóm X không có nhãn. Không gọi mã cụm là nhãn lớp thật.
- `stratify=y` giúp giữ tỷ lệ lớp nhưng không chứng minh tập test đại diện toàn bộ dân số.
- Accuracy test khác loss train và không phản ánh đầy đủ hiệu quả trên dữ liệu mất cân bằng.
- `scikit-learn` là thư viện ngoài; phiên bản khác nhau có thể thay đổi kết quả học tối ưu.

## 7. Trắc nghiệm

**Q1. What is a train set? | Train set là gì?**

A. Data used for fitting model parameters | Dữ liệu để fit tham số mô hình

B. Held-out data for final evaluation | Dữ liệu giữ lại để đánh giá cuối

C. Supervised prediction of discrete labels | Dự đoán nhãn rời rạc có giám sát

D. Grouping unlabeled observations by similarity | Nhóm quan sát chưa có nhãn theo độ tương đồng

**Đáp án: A**

**Giải thích:** Mô hình học tham số từ mẫu train, không cập nhật bằng bản ghi test. Đơn vị học là hàng train với đặc trưng và nhãn, không phải hàng test để chấm điểm.


**Q2. What is a test set? | Test set là gì?**

A. Data used for fitting model parameters | Dữ liệu để fit tham số mô hình

B. Held-out data for final evaluation | Dữ liệu giữ lại để đánh giá cuối

C. Supervised prediction of discrete labels | Dự đoán nhãn rời rạc có giám sát

D. Grouping unlabeled observations by similarity | Nhóm quan sát chưa có nhãn theo độ tương đồng

**Đáp án: B**

**Giải thích:** Test đo hiệu quả trên dữ liệu chưa học; chỉnh đi chỉnh lại theo test làm đánh giá thiên lệch. Điểm cốt lõi là test độc lập với quá trình học; điều chỉnh lặp dựa trên test sẽ làm mất tính độc lập ấy.


**Q3. What is classification? | Classification là gì?**

A. Data used for fitting model parameters | Dữ liệu để fit tham số mô hình

B. Held-out data for final evaluation | Dữ liệu giữ lại để đánh giá cuối

C. Supervised prediction of discrete labels | Dự đoán nhãn rời rạc có giám sát

D. Grouping unlabeled observations by similarity | Nhóm quan sát chưa có nhãn theo độ tương đồng

**Đáp án: C**

**Giải thích:** Lúc train phải có nhãn; đầu ra dự đoán là loại/phân lớp. Khác phân cụm, bài phân loại có nhãn mục tiêu rõ ràng khi học.


**Q4. What is clustering? | Clustering là gì?**

A. Data used for fitting model parameters | Dữ liệu để fit tham số mô hình

B. Held-out data for final evaluation | Dữ liệu giữ lại để đánh giá cuối

C. Supervised prediction of discrete labels | Dự đoán nhãn rời rạc có giám sát

D. Grouping unlabeled observations by similarity | Nhóm quan sát chưa có nhãn theo độ tương đồng

**Đáp án: D**

**Giải thích:** Phân cụm dựa vào X mà không fit nhãn lớp có sẵn. Khác classifier, KMeans không tự hiểu ý nghĩa đời thực của số hiệu cụm.


**Q5. What does stratify=y help preserve? | stratify=y giúp giữ gì?**

A. Approximate label proportions in train and test | Tỷ lệ nhãn xấp xỉ giữa train và test

B. Training features only | Chỉ các đặc trưng train

C. Preprocessing and estimator fitting/prediction | Tiền xử lý và các bước fit/dự đoán

D. Arbitrary cluster identifiers | Định danh cụm tùy ý

**Đáp án: A**

**Giải thích:** Nó chia các lớp theo tỷ lệ gần tương ứng khi số mẫu cho phép. Nó chỉ giữ tỷ lệ lớp xấp xỉ, không bảo đảm mọi nhóm nhỏ đều đại diện.


**Q6. What does StandardScaler fit on? | StandardScaler phải fit trên dữ liệu nào?**

A. Approximate label proportions in train and test | Tỷ lệ nhãn xấp xỉ giữa train và test

B. Training features only | Chỉ các đặc trưng train

C. Preprocessing and estimator fitting/prediction | Tiền xử lý và các bước fit/dự đoán

D. Arbitrary cluster identifiers | Định danh cụm tùy ý

**Đáp án: B**

**Giải thích:** Fit từ test làm rò rỉ phân phối đánh giá vào tiền xử lý. Được áp thống kê đã học từ train lên test, nhưng không được học lại thống kê từ test.


**Q7. What does Pipeline combine? | Pipeline gộp gì?**

A. Approximate label proportions in train and test | Tỷ lệ nhãn xấp xỉ giữa train và test

B. Training features only | Chỉ các đặc trưng train

C. Preprocessing and estimator fitting/prediction | Tiền xử lý và các bước fit/dự đoán

D. Arbitrary cluster identifiers | Định danh cụm tùy ý

**Đáp án: C**

**Giải thích:** Các phép đổi đã học được áp nhất quán khi dự đoán. Vì thế tiền xử lý phải nằm trong quy trình train, không fit trước trên toàn bộ dữ liệu.


**Q8. What do KMeans cluster IDs mean? | Mã cụm KMeans có nghĩa gì?**

A. Approximate label proportions in train and test | Tỷ lệ nhãn xấp xỉ giữa train và test

B. Training features only | Chỉ các đặc trưng train

C. Preprocessing and estimator fitting/prediction | Tiền xử lý và các bước fit/dự đoán

D. Arbitrary cluster identifiers | Định danh cụm tùy ý

**Đáp án: D**

**Giải thích:** Mã có thể đổi 0↔1 dù cách chia hình học không đổi. Hãy đánh giá theo thành viên nhóm hoặc ánh xạ có căn cứ, không mặc định mã 0 là một loài cụ thể.


**Q9. What is a feature? | Feature là gì?**

A. Input measurement used to predict | Số đo đầu vào dùng để dự đoán

B. The desired discrete output class | Lớp đầu ra muốn dự đoán

C. One predicted label per input row | Một nhãn dự đoán cho mỗi hàng đầu vào

D. Prediction accuracy on test labels | Tỷ lệ dự đoán đúng trên nhãn test

**Đáp án: A**

**Giải thích:** Đặc trưng nằm ở cột X, không phải nhãn đích. Mỗi cột cần có ý nghĩa và đơn vị đo rõ ràng trước khi đưa vào classifier.


**Q10. What is a target label? | Target label là gì?**

A. Input measurement used to predict | Số đo đầu vào dùng để dự đoán

B. The desired discrete output class | Lớp đầu ra muốn dự đoán

C. One predicted label per input row | Một nhãn dự đoán cho mỗi hàng đầu vào

D. Prediction accuracy on test labels | Tỷ lệ dự đoán đúng trên nhãn test

**Đáp án: B**

**Giải thích:** Classifier học ánh xạ từ X sang y. Nhãn là mục tiêu dự đoán, không phải đặc trưng được đưa sẵn khi dự đoán.


**Q11. What does `model.predict(X_test)` return? | `model.predict(X_test)` trả gì?**

A. Input measurement used to predict | Số đo đầu vào dùng để dự đoán

B. The desired discrete output class | Lớp đầu ra muốn dự đoán

C. One predicted label per input row | Một nhãn dự đoán cho mỗi hàng đầu vào

D. Prediction accuracy on test labels | Tỷ lệ dự đoán đúng trên nhãn test

**Đáp án: C**

**Giải thích:** Mỗi hàng test có một dự đoán lớp. Số nhãn dự đoán phải bằng số hàng đầu vào, nếu không sẽ thiếu kết quả cho một số mẫu.


**Q12. What does `model.score(X_test,y_test)` mean for a standard classifier? | `model.score` cho classifier thông dụng đo gì?**

A. Input measurement used to predict | Số đo đầu vào dùng để dự đoán

B. The desired discrete output class | Lớp đầu ra muốn dự đoán

C. One predicted label per input row | Một nhãn dự đoán cho mỗi hàng đầu vào

D. Prediction accuracy on test labels | Tỷ lệ dự đoán đúng trên nhãn test

**Đáp án: D**

**Giải thích:** Score so dự đoán với nhãn thật; không phải loss train. Nếu nhãn mất cân bằng, cần đọc thêm precision/recall theo lớp hoặc confusion matrix.


**Q13. Which check detects overlapping IDs across train and test? | Phép kiểm tra nào phát hiện ID xuất hiện ở cả train và test?**

A. `train_ids.isdisjoint(test_ids)` | `train_ids.isdisjoint(test_ids)`

B. No, correlated records or future information may leak | Không, bản ghi liên quan hoặc thông tin tương lai vẫn rò rỉ

C. No, it fits features X | Không, nó fit đặc trưng X

D. Cluster numbers have arbitrary permutations | Số hiệu cụm có thể hoán đổi tùy ý

**Đáp án: A**

**Giải thích:** isdisjoint xác nhận không có cùng mã ở cả hai tập. Kiểm tra này bắt trùng mã đơn giản, không phát hiện phép đo liên quan mang mã khác nhau.


**Q14. Does disjoint ID imply zero leakage? | Không trùng ID có chắc không rò rỉ?**

A. `train_ids.isdisjoint(test_ids)` | `train_ids.isdisjoint(test_ids)`

B. No, correlated records or future information may leak | Không, bản ghi liên quan hoặc thông tin tương lai vẫn rò rỉ

C. No, it fits features X | Không, nó fit đặc trưng X

D. Cluster numbers have arbitrary permutations | Số hiệu cụm có thể hoán đổi tùy ý

**Đáp án: B**

**Giải thích:** Rò rỉ có thể qua dữ liệu liên quan, phép đổi hoặc thông tin thời gian. Rò rỉ là thông tin đáng lẽ chưa biết lọt vào train, không chỉ là vấn đề trùng mã.


**Q15. Does KMeans need y labels to fit? | KMeans cần nhãn y khi fit không?**

A. `train_ids.isdisjoint(test_ids)` | `train_ids.isdisjoint(test_ids)`

B. No, correlated records or future information may leak | Không, bản ghi liên quan hoặc thông tin tương lai vẫn rò rỉ

C. No, it fits features X | Không, nó fit đặc trưng X

D. Cluster numbers have arbitrary permutations | Số hiệu cụm có thể hoán đổi tùy ý

**Đáp án: C**

**Giải thích:** Phân cụm không giám sát và không tối ưu accuracy theo nhãn thật. KMeans chỉ cần tọa độ đặc trưng và số cụm muốn tìm.


**Q16. Why not directly compare KMeans IDs to true classes for accuracy? | Vì sao không so trực tiếp mã KMeans với lớp thật để tính accuracy?**

A. `train_ids.isdisjoint(test_ids)` | `train_ids.isdisjoint(test_ids)`

B. No, correlated records or future information may leak | Không, bản ghi liên quan hoặc thông tin tương lai vẫn rò rỉ

C. No, it fits features X | Không, nó fit đặc trưng X

D. Cluster numbers have arbitrary permutations | Số hiệu cụm có thể hoán đổi tùy ý

**Đáp án: D**

**Giải thích:** Cùng nhóm có thể gắn mã đảo ngược mà chất lượng không đổi. Nếu đổi nhãn số của hai cụm, accuracy kiểu phân loại có thể đổi dù cách chia nhóm vẫn y hệt.


**Q17. What shape does a 150-row four-feature table have? | Bảng 150 hàng, bốn đặc trưng có shape nào?**

A. (150,4) | (150,4)

B. Allocate about a quarter to test | Dành khoảng một phần tư cho test

C. Held-out final test set | Tập test cuối cùng đã giữ lại

D. Predicted known class names | Tên lớp đã biết từ dữ liệu nhãn

**Đáp án: A**

**Giải thích:** Hàng là hoa, cột là bốn đặc trưng. Chiều thứ nhất đếm số hoa, chiều thứ hai đếm số đo trên mỗi hoa.


**Q18. What does test_size=0.25 mean? | test_size=0.25 nghĩa là gì?**

A. (150,4) | (150,4)

B. Allocate about a quarter to test | Dành khoảng một phần tư cho test

C. Held-out final test set | Tập test cuối cùng đã giữ lại

D. Predicted known class names | Tên lớp đã biết từ dữ liệu nhãn

**Đáp án: B**

**Giải thích:** Làm tròn quyết định số nguyên mẫu chính xác. Với số mẫu hữu hạn, thư viện phải làm tròn tỷ lệ yêu cầu thành số lượng nguyên.


**Q19. Which dataset must be excluded from hyperparameter tuning? | Không được dùng tập nào để điều chỉnh siêu tham số?**

A. (150,4) | (150,4)

B. Allocate about a quarter to test | Dành khoảng một phần tư cho test

C. Held-out final test set | Tập test cuối cùng đã giữ lại

D. Predicted known class names | Tên lớp đã biết từ dữ liệu nhãn

**Đáp án: C**

**Giải thích:** Chọn siêu tham số bằng validation/CV thuộc phần train. Hãy chọn siêu tham số bằng validation hoặc cross-validation trên phần train, sau đó đánh giá test cuối.


**Q20. What can a classification model output that KMeans does not inherently provide? | Classifier có đầu ra gì mà KMeans không tự bảo đảm?**

A. (150,4) | (150,4)

B. Allocate about a quarter to test | Dành khoảng một phần tư cho test

C. Held-out final test set | Tập test cuối cùng đã giữ lại

D. Predicted known class names | Tên lớp đã biết từ dữ liệu nhãn

**Đáp án: D**

**Giải thích:** KMeans tạo cụm chứ không tự gán ý nghĩa lớp thật. Mã lớp là nhãn đã xác định; mã cụm chỉ đánh dấu một nhóm vừa phát hiện.

## 8. Liên hệ bài kế tiếp

`Set/NumPy → Train/Test → Preprocessing → Classification/Clustering`.
