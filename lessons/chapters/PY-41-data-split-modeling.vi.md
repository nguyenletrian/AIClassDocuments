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

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Kiểm tra ID train/test · Cấp 1: Xác định X và y

**Tình huống thực tế:** Một nhóm thử mô hình với train `{1,2,3}` và test `{4,5}` (mỗi số là ID hồ sơ). Cần xác nhận không có ID nào xuất hiện trong cả hai tập.

**Vì sao chọn cách giải này?** Dùng `isdisjoint` cho đúng câu hỏi về phần tử trùng nhau; không phải đo độ chính xác.

**Quy trình giải:**

1. Tạo hai Set ID train và test.
2. Kiểm tra phần giao có rỗng.
3. In Boolean và nêu rằng đây chỉ là một bước chống rò rỉ.

```python
# Mục đích: Kiểm tra ID train/test.
train = {1, 2, 3}
test = {4, 5}
print(train.isdisjoint(test))
```

**Kết quả khi chạy:**

```text
True
```

Hai tập không trùng ID, chưa chứng minh mọi dữ liệu đều độc lập.

**Bài thực hành nâng cấp — cấp 1/5:** Trung tâm có **10 học viên**; mỗi hàng có hai đặc trưng là số giờ học và số bài thực hành, nhãn `y` là kết quả 0/1. Hãy xác định ma trận đặc trưng và nhãn cho 10 học viên. Cấp cao đưa dữ liệu thiếu vào và phải chia train/test trước khi học tham số điền thiếu; tập 10–20 mẫu chỉ dùng để minh họa, không đánh giá chất lượng mô hình thật.

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
# Mỗi hàng là một học viên, cột X1=giờ học, X2=số bài thực hành; nhãn y=đạt/chưa đạt.
X = np.array([[i+1,(i*3)%7+2] for i in range(10)],dtype=float)
y = np.array([i%2 for i in range(10)])
result = {'X':X.shape,'y':y.shape,'classes':sorted(set(y.tolist()))}
assert len(X)==10
print("Số học viên:",len(X))
print("Kết quả:",result)
```

**Đọc kết quả:** Kiểm tra số hàng 10, shape của train/test và chỉ số trên tập chưa fit; khi mẫu nhỏ, accuracy có độ bất định cao.

### Tình huống 2 — Phân chia Iris có phân tầng · Cấp 2: Chia train/test

**Tình huống thực tế:** Tập Iris có 150 hoa, bốn số đo cm/hoa và ba loài với 50 hoa mỗi loài. Cần dành 25% làm test nhưng duy trì tỷ lệ loài gần tương đương.

**Vì sao chọn cách giải này?** `stratify=y` chia theo nhãn, giúp test không tình cờ thiếu lớp trong bộ mẫu này.

**Quy trình giải:**

1. Nạp bảng 150×4 và nhãn 150 giá trị.
2. Dùng `train_test_split` với test_size=0.25, stratify và seed 42.
3. In shape train/test.

```python
# Mục đích: Phân chia Iris có phân tầng.
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.25,
    stratify=data.target, random_state=42,
)
print(X_train.shape, X_test.shape)
```

**Kết quả khi chạy:**

```text
(112, 4) (38, 4)
```

112 hoa dùng train, 38 hoa giữ test; mỗi hàng vẫn có bốn đặc trưng.

**Bài thực hành nâng cấp — cấp 2/5:** Trung tâm có **12 học viên**; mỗi hàng có hai đặc trưng là số giờ học và số bài thực hành, nhãn `y` là kết quả 0/1. Hãy chia 12 học viên theo nhãn để tập kiểm tra có cả hai lớp. Cấp cao đưa dữ liệu thiếu vào và phải chia train/test trước khi học tham số điền thiếu; tập 10–20 mẫu chỉ dùng để minh họa, không đánh giá chất lượng mô hình thật.

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
# Mỗi hàng là một học viên, cột X1=giờ học, X2=số bài thực hành; nhãn y=đạt/chưa đạt.
X = np.array([[i+1,(i*3)%7+2] for i in range(12)],dtype=float)
y = np.array([i%2 for i in range(12)])
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,stratify=y,random_state=42)
result = {'train':X_train.shape,'test':X_test.shape,'test_classes':sorted(set(y_test.tolist()))}
assert len(X)==12
print("Số học viên:",len(X))
print("Kết quả:",result)
```

**Đọc kết quả:** Kiểm tra số hàng 12, shape của train/test và chỉ số trên tập chưa fit; khi mẫu nhỏ, accuracy có độ bất định cao.

### Tình huống 3 — Fit scaler và mô hình trên train · Cấp 3: Fit và đánh giá

**Tình huống thực tế:** Nhóm học máy dùng bốn kích thước của Iris để đoán một trong ba loài. Cần chuẩn hóa số đo mà không dùng trung bình/độ lệch chuẩn của test trong lúc fit.

**Vì sao chọn cách giải này?** Pipeline tự fit scaler và Logistic Regression trên train, rồi áp cùng biến đổi lên test.

**Quy trình giải:**

1. Chia Iris trước khi fit bất kỳ phép chuẩn hóa nào.
2. Tạo pipeline StandardScaler → LogisticRegression và fit train.
3. In số mẫu dự đoán trên test.

```python
# Mục đích: Fit scaler và mô hình trên train.
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.25,
    stratify=data.target, random_state=42,
)
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)
print(len(model.predict(X_test)))
```

**Kết quả khi chạy:**

```text
38
```

Model trả một dự đoán nhãn cho mỗi hoa trong 38 hoa test.

**Bài thực hành nâng cấp — cấp 3/5:** Trung tâm có **15 học viên**; mỗi hàng có hai đặc trưng là số giờ học và số bài thực hành, nhãn `y` là kết quả 0/1. Hãy fit logistic regression trên train và đánh giá ở tập chưa thấy. Cấp cao đưa dữ liệu thiếu vào và phải chia train/test trước khi học tham số điền thiếu; tập 10–20 mẫu chỉ dùng để minh họa, không đánh giá chất lượng mô hình thật.

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
# Mỗi hàng là một học viên, cột X1=giờ học, X2=số bài thực hành; nhãn y=đạt/chưa đạt.
X = np.array([[i+1,(i*3)%7+2] for i in range(15)],dtype=float)
y = np.array([i%2 for i in range(15)])
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,stratify=y,random_state=42)
model = LogisticRegression(max_iter=1000).fit(X_train,y_train)
result = {'accuracy':round(float(model.score(X_test,y_test)),3),'test_size':len(y_test)}
assert len(X)==15
print("Số học viên:",len(X))
print("Kết quả:",result)
```

**Đọc kết quả:** Kiểm tra số hàng 15, shape của train/test và chỉ số trên tập chưa fit; khi mẫu nhỏ, accuracy có độ bất định cao.

### Tình huống 4 — Nhóm bốn tọa độ 2D · Cấp 4: Xử lý dữ liệu thiếu không leakage

**Tình huống thực tế:** Bốn điểm trong mặt phẳng, hai điểm quanh `[0,0]`, hai điểm quanh `[10,10]`, chưa có nhãn. Cần phát hiện số cụm khi yêu cầu trước `k=2`.

**Vì sao chọn cách giải này?** KMeans phân nhóm từ khoảng cách giữa các đặc trưng, không dùng y thật.

**Quy trình giải:**

1. Tạo ma trận X shape (4,2), mỗi hàng là một điểm (x,y) cùng đơn vị.
2. Fit KMeans với k=2, seed cố định.
3. Đếm số mã cụm khác nhau, tránh phụ thuộc hoán đổi mã cụm.

```python
# Mục đích: Nhóm bốn tọa độ 2D.
import numpy as np
from sklearn.cluster import KMeans

X = np.array([[0, 0], [0, 1], [10, 10], [10, 11]])
cluster_ids = KMeans(n_clusters=2, n_init=10, random_state=42).fit_predict(X)
print(len(set(cluster_ids.tolist())))
```

**Kết quả khi chạy:**

```text
2
```

Bốn điểm được chia thành hai nhóm, không tự biết nhóm nào là nhãn thật.

**Bài thực hành nâng cấp — cấp 4/5:** Trung tâm có **18 học viên**; mỗi hàng có hai đặc trưng là số giờ học và số bài thực hành, nhãn `y` là kết quả 0/1. Hãy đưa bước điền thiếu và chuẩn hóa vào pipeline khi có 18 hồ sơ. Cấp cao đưa dữ liệu thiếu vào và phải chia train/test trước khi học tham số điền thiếu; tập 10–20 mẫu chỉ dùng để minh họa, không đánh giá chất lượng mô hình thật.

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
# Mỗi hàng là một học viên, cột X1=giờ học, X2=số bài thực hành; nhãn y=đạt/chưa đạt.
X = np.array([[i+1,(i*3)%7+2] for i in range(18)],dtype=float)
y = np.array([i%2 for i in range(18)])
X[15,0] = np.nan
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,stratify=y,random_state=42)
pipe = make_pipeline(SimpleImputer(strategy='median'),StandardScaler(),LogisticRegression(max_iter=1000))
pipe.fit(X_train,y_train)
result = {'test_accuracy':round(float(pipe.score(X_test,y_test)),3),'missing':int(np.isnan(X).sum())}
assert len(X)==18
print("Số học viên:",len(X))
print("Kết quả:",result)
```

**Đọc kết quả:** Kiểm tra số hàng 18, shape của train/test và chỉ số trên tập chưa fit; khi mẫu nhỏ, accuracy có độ bất định cao.

### Tình huống 5 — So classification và clustering · Cấp 5: So pipeline với baseline

**Tình huống thực tế:** Dữ liệu Iris có bốn đặc trưng số (cm) và nhãn loài. Nhóm thực hành cần xác định thông tin đầu vào nào được phép dùng ở mô hình có giám sát và không giám sát.

**Vì sao chọn cách giải này?** Kiểm tra shape của X và y làm rõ classifier dùng cả nhãn lúc fit, trong khi clustering fit từ X.

**Quy trình giải:**

1. Nạp Iris, lấy X chứa kích thước hoa và y chứa nhãn.
2. In shape X và y.
3. Phân biệt dùng `(X,y)` để train classification với dùng `X` cho clustering.

```python
# Mục đích: So classification và clustering.
from sklearn.datasets import load_iris

data = load_iris()
print(data.data.shape, data.target.shape)
```

**Kết quả khi chạy:**

```text
(150, 4) (150,)
```

Mỗi hoa có bốn đặc trưng và một nhãn; KMeans không sử dụng nhãn để fit.

**Bài thực hành nâng cấp — cấp 5/5:** Trung tâm có **20 học viên**; mỗi hàng có hai đặc trưng là số giờ học và số bài thực hành, nhãn `y` là kết quả 0/1. Hãy so baseline với pipeline trên cùng một phép chia 20 hồ sơ. Cấp cao đưa dữ liệu thiếu vào và phải chia train/test trước khi học tham số điền thiếu; tập 10–20 mẫu chỉ dùng để minh họa, không đánh giá chất lượng mô hình thật.

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
# Mỗi hàng là một học viên, cột X1=giờ học, X2=số bài thực hành; nhãn y=đạt/chưa đạt.
X = np.array([[i+1,(i*3)%7+2] for i in range(20)],dtype=float)
y = np.array([i%2 for i in range(20)])
X[15,0] = np.nan
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,stratify=y,random_state=42)
pipe = make_pipeline(SimpleImputer(strategy='median'),StandardScaler(),LogisticRegression(max_iter=1000)).fit(X_train,y_train)
base = make_pipeline(SimpleImputer(strategy='median'),LogisticRegression(max_iter=1000)).fit(X_train,y_train)
result = {'pipeline_accuracy':round(float(pipe.score(X_test,y_test)),3),'baseline_accuracy':round(float(base.score(X_test,y_test)),3),'test_size':len(y_test)}
assert len(X)==20
print("Số học viên:",len(X))
print("Kết quả:",result)
```

**Đọc kết quả:** Kiểm tra số hàng 20, shape của train/test và chỉ số trên tập chưa fit; khi mẫu nhỏ, accuracy có độ bất định cao.

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
