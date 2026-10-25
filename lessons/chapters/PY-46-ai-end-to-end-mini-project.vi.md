# PY-46 — Mini project: dữ liệu → làm sạch → mô hình → đánh giá


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Feature** — đặc trưng; **Label** — nhãn.

`Python → NumPy/Pandas → Train/Test → Pipeline → Report`

**Học xong dùng để làm gì?** Kết hợp chuẩn bị dữ liệu, đặc trưng, huấn luyện mô hình, đánh giá và báo cáo thành một quy trình AI có thể chạy lại.

**Kết nối kiến thức tiếp theo:** Sau bài cuối, áp dụng toàn bộ chuỗi vào bài toán thực tế tự chọn: xác định dữ liệu, đặt tiêu chí đánh giá và lưu kết quả có thể tái tạo.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| Feature | đặc trưng | Cột đầu vào cho mô hình |
| Label | nhãn | Giá trị mục tiêu cần dự đoán |
| Pipeline | chuỗi xử lý | Gom tiền xử lý và mô hình thành các bước |
| Evaluation | đánh giá | Đo kết quả trên dữ liệu chưa dùng để fit |

## 3. Hàm và cách sử dụng

**Từ vựng trong mục:** **Function** — hàm; **Option** — tùy chọn.

| Cú pháp | Mục đích và lựa chọn |
|---|---|
| `pd.DataFrame()/dropna()` | Tạo bảng và đánh giá xử lý giá trị thiếu |
| `train_test_split(...,stratify=y)` | Chia dữ liệu theo nhãn, tránh leakage |
| `make_pipeline(StandardScaler(),LogisticRegression())` | Fit scaler/model trên train trong một chuỗi |
| `model.score(X_test,y_test)` | Đánh giá tập test, không suy từ điểm train |

## 4. Khái niệm chính và liên quan

**Mạch kiến thức:** Một dự án AI bắt đầu từ việc hiểu mỗi hàng mẫu, cột đặc trưng và nhãn mục tiêu. Dữ liệu được làm sạch theo đúng quy tắc, chia train/test **trước khi học tham số xử lý**, huấn luyện bằng Pipeline rồi đánh giá trên nhãn test. Kết quả mô hình cần đọc cùng giới hạn, không chỉ nhìn một con số accuracy.

### 4.1. Feature và label — Đầu vào khác mục tiêu

**Từ vựng trong mục:** **Feature — đặc trưng; Label — nhãn**.

Trong mini-project phân loại hoa Iris, một **hàng** ứng với một bông hoa; bốn **cột feature** là chiều dài/rộng đài hoa và cánh hoa, đơn vị cm. **Label** (y) là mã loài 0,1,2 cần dự đoán. X có shape `(150,4)`, y có 150 nhãn. Không đưa cột chứa nhãn hoặc thông tin được biết sau kết quả vào X, vì đó là rò rỉ mục tiêu.

```python
# Mục đích: Đầu vào khác mục tiêu.
from sklearn.datasets import load_iris

data = load_iris()
print(data.data.shape, data.target.shape)
```

**Kết quả khi chạy:**

```text
(150, 4) (150,)
```

Mỗi trong 150 hoa có bốn số đo dùng dự đoán một trong ba loài.

### 4.2. Cleaning — Xử lý ô khuyết đúng thứ tự

**Từ vựng trong mục:** **Cleaning — làm sạch; Imputation — điền thiếu**.

Trước khi huấn luyện cần kiểm kiểu dữ liệu, giá trị thiếu, lỗi nhập và đơn vị. Nếu thiếu số đo, có thể điền bằng **median của tập train**, nhưng **không** tính median từ cả train và test. Ví dụ ba chiều dài (cm) `[5,None,7]`, median từ hai giá trị có thực là 6; điền None bằng 6. Đây là giá trị ước lượng, không phải số đo gốc.

```python
# Mục đích: Xử lý ô khuyết đúng thứ tự.
import pandas as pd

values = pd.Series([5.0, None, 7.0])
print(values.fillna(values.median()).tolist())
```

**Kết quả khi chạy:**

```text
[5.0, 6.0, 7.0]
```

Giá trị thiếu được thay bằng trung vị 6 cm của hai số đã quan sát.

### 4.3. Pipeline — Gắn tiền xử lý với mô hình

**Từ vựng trong mục:** **Pipeline — chuỗi xử lý; Fit — học tham số**.

**Pipeline** ghép các bước `SimpleImputer` → `StandardScaler` → `LogisticRegression`. Khi `.fit(X_train,y_train)`, bước điền thiếu và chuẩn hóa **học tham số từ train**, mô hình sau đó học nhãn. Khi `.predict(X_test)`, các phép biến đổi dùng lại tham số train. Điều này hạn chế rò rỉ test do tính mean/median hay scale trên toàn bảng trước khi chia.

```python
# Mục đích: Gắn tiền xử lý với mô hình.
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

model = make_pipeline(
    SimpleImputer(strategy='median'),
    StandardScaler(),
    LogisticRegression(max_iter=1000),
)
print(len(model.steps))
```

**Kết quả khi chạy:**

```text
3
```

Pipeline gồm ba bước nối tiếp: điền thiếu, chuẩn hóa, phân loại; chưa gọi fit nên chưa có mô hình đã học.

### 4.4. Evaluation — Đánh giá trên dữ liệu chưa fit

**Từ vựng trong mục:** **Evaluation — đánh giá; Confusion matrix — ma trận nhầm lẫn**.

Đánh giá phân loại phải so nhãn dự đoán với nhãn thật của **test giữ riêng**. **Accuracy** là số dự đoán đúng chia tổng số mẫu, nhưng có thể gây hiểu sai nếu một lớp rất phổ biến. **Confusion matrix** ghi số mẫu theo **hàng = nhãn thật**, **cột = nhãn dự đoán**; ô ngoài đường chéo cho biết những lỗi nhầm lớp cụ thể.

```python
# Mục đích: Đánh giá trên dữ liệu chưa fit.
from sklearn.metrics import confusion_matrix

actual = [0, 1, 1, 0]
predicted = [0, 1, 0, 0]
print(confusion_matrix(actual, predicted).tolist())
```

**Kết quả khi chạy:**

```text
[[2, 0], [1, 1]]
```

Lớp thật 0 có hai mẫu dự đoán đúng; lớp thật 1 có một mẫu nhầm sang 0 và một mẫu đúng.

## 5. Năm tình huống mini-project AI — từ kiểm 10 hồ sơ đến báo cáo 20 dòng

### Tình huống 1 — Cấp 1: Kiểm cấu trúc 10 hồ sơ trước khi làm dự án AI

**Từ vựng trong mục:** **Feature** — đặc trưng; **Label** — nhãn; **Data validation** — kiểm dữ liệu.

**Tình huống thực tế:** Trung tâm có **10 hồ sơ học viên HV01…HV10**, mỗi hàng gồm `id` (mã duy nhất), `hours` (giờ tự học/tuần), `practice` (số bài luyện tập) và nhãn `passed` (0: chưa đạt, 1: đạt). Trước khi xây mô hình, cần kiểm số hàng, cột đầu vào, số nhãn 0/1 và xem có mã trùng hay ô thiếu không. Không đưa `passed` vào X.

**Vì sao chọn cách này?** Bất kỳ mô hình nào cũng cần bảng X và nhãn y khớp **một hàng một người**. Kiểm cấu trúc từ đầu tránh gắn điểm đích vào feature gây rò rỉ, hoặc coi mã hồ sơ là biến đo lường.

**Quy trình:**
1. Tạo đủ 10 hàng với ý nghĩa/đơn vị từng cột.
2. Lấy đúng hai feature số sang X, nhãn mục tiêu sang y.
3. Xác nhận số dòng khớp, ID duy nhất, không thiếu số đo và in phân bố nhãn.

```python
import pandas as pd
records = [{"id":"HV01","hours":1,"practice":2,"passed":0},{"id":"HV02","hours":2,"practice":3,"passed":0},{"id":"HV03","hours":3,"practice":4,"passed":0},{"id":"HV04","hours":4,"practice":5,"passed":0},{"id":"HV05","hours":5,"practice":2,"passed":0},{"id":"HV06","hours":1,"practice":3,"passed":0},{"id":"HV07","hours":2,"practice":4,"passed":1},{"id":"HV08","hours":3,"practice":5,"passed":1},{"id":"HV09","hours":4,"practice":2,"passed":1},{"id":"HV10","hours":5,"practice":3,"passed":1}]
df = pd.DataFrame(records)
X = df[["hours", "practice"]]
y = df["passed"]
assert len(df) == 10 and X.shape == (10, 2) and len(y) == 10
print("Hồ sơ:", len(df))
print("Feature:", X.shape[1])
print("Nhãn 0/1:", int((y==0).sum()), int((y==1).sum()))
print("ID trùng:", int(df["id"].duplicated().sum()))
print("Ô feature thiếu:", int(X.isna().sum().sum()))
```

**Kết quả khi chạy:**

```text
Hồ sơ: 10
Feature: 2
Nhãn 0/1: 6 4
ID trùng: 0
Ô feature thiếu: 0
```

Đây là dữ liệu học tập **giả lập**, không phải hồ sơ thật. Đếm nhãn chưa cho biết mô hình dự đoán được bao nhiêu mẫu mới.

### Tình huống 2 — Cấp 2: Tách 12 học viên có phân tầng và đặt điểm baseline

**Từ vựng trong mục:** **Stratified split** — chia giữ tỷ lệ lớp; **Baseline** — mốc so sánh; **Test set** — tập đánh giá.

**Tình huống thực tế:** Trường có **12 hồ sơ HV01…HV12** với số giờ tự học (giờ/tuần), bài luyện tập (bài) và nhãn đạt/chưa đạt, **sáu người mỗi lớp**. Cần giữ riêng **bốn hồ sơ test**, train trên tám hồ sơ còn lại và thử mô hình mốc luôn đoán lớp thường gặp nhất. Kết quả baseline là điểm khởi đầu để đánh giá mô hình phức tạp ở bài sau, không dùng ID như feature.

**Vì sao chọn cách này?** `train_test_split(..., stratify=y)` giữ hai lớp trong cả train/test; `DummyClassifier(strategy='most_frequent')` cho một mốc dễ giải thích. Mô hình chỉ `.fit()` từ train, không xem nhãn test trước khi đánh giá.

**Quy trình:**
1. Đọc 12 bộ X/y/ID có cùng thứ tự.
2. Chia 8 train và 4 test phân tầng, kiểm ID không giao nhau.
3. Fit baseline trên train, đánh giá accuracy trên test và in số mẫu của từng lớp test.

```python
import numpy as np
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import train_test_split
records = [{"id":"HV01","hours":1,"practice":2,"passed":0},{"id":"HV02","hours":2,"practice":3,"passed":0},{"id":"HV03","hours":3,"practice":4,"passed":0},{"id":"HV04","hours":1,"practice":2,"passed":0},{"id":"HV05","hours":2,"practice":3,"passed":0},{"id":"HV06","hours":3,"practice":4,"passed":0},{"id":"HV07","hours":6,"practice":8,"passed":1},{"id":"HV08","hours":7,"practice":9,"passed":1},{"id":"HV09","hours":8,"practice":10,"passed":1},{"id":"HV10","hours":6,"practice":8,"passed":1},{"id":"HV11","hours":7,"practice":9,"passed":1},{"id":"HV12","hours":8,"practice":10,"passed":1}]
X = np.array([[r["hours"],r["practice"]] for r in records],dtype=float)
y = np.array([r["passed"] for r in records])
train,test = train_test_split(np.arange(12),test_size=4,random_state=42,stratify=y)
model = DummyClassifier(strategy="most_frequent")
model.fit(X[train],y[train])
accuracy = model.score(X[test],y[test])
assert len(records) == 12 and set(train).isdisjoint(test)
print("Hồ sơ:", len(records))
print("Train/test:", len(train), len(test))
print("Nhãn test 0/1:", int((y[test]==0).sum()), int((y[test]==1).sum()))
print(f"Accuracy baseline: {accuracy:.2f}")
```

**Kết quả khi chạy:**

```text
Hồ sơ: 12
Train/test: 8 4
Nhãn test 0/1: 2 2
Accuracy baseline: 0.50
```

Baseline cố ý đơn giản; accuracy 0,50 ở đây là **hai trong bốn hồ sơ test**, không đủ để khẳng định hiệu quả trên người học mới.

### Tình huống 3 — Cấp 3: Huấn luyện Pipeline trên 15 hoa có số đo bị khuyết

**Từ vựng trong mục:** **Imputation** — điền thiếu; **Pipeline** — chuỗi xử lý; **Leakage** — rò rỉ dữ liệu.

**Tình huống thực tế:** Nhóm nghiên cứu có **15 hoa F01…F15**, mỗi hàng chứa chiều dài cánh (cm), chiều dài đài (cm), nhãn ba loài 0/1/2, đúng năm hoa mỗi loài. Hai ô đo bị thiếu: một chiều dài cánh và một chiều dài đài. Cần chia 9 train/6 test có phân tầng, **chỉ học median điền thiếu từ train**, chuẩn hóa và Logistic Regression rồi dự đoán sáu hoa giữ riêng.

**Vì sao chọn cách này?** Điền giá trị thiếu từ **toàn bộ 15 hoa trước khi chia** sẽ cho test tham gia tính median gây leakage. Pipeline kết hợp `SimpleImputer` → `StandardScaler` → classifier, mỗi bước học thông số chỉ từ train.

**Quy trình:**
1. Lưu 15 hoa và chuyển None trong cột số thành NaN; kiểm đúng hai ô thiếu.
2. Tách train/test phân tầng 9/6 trước khi `.fit()` tiền xử lý.
3. Huấn luyện Pipeline, so median đã học với `nanmedian(X_train)`, đo accuracy test và kiểm số dự đoán.

```python
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
records = [{"id":"F01","petal_cm":1.1,"sepal_cm":3,"species":0},{"id":"F02","petal_cm":1.2000000000000002,"sepal_cm":3.03,"species":0},{"id":"F03","petal_cm":1.3,"sepal_cm":3.06,"species":0},{"id":"F04","petal_cm":None,"sepal_cm":3.09,"species":0},{"id":"F05","petal_cm":1.5,"sepal_cm":3.12,"species":0},{"id":"F06","petal_cm":4.1,"sepal_cm":4,"species":1},{"id":"F07","petal_cm":4.199999999999999,"sepal_cm":4.03,"species":1},{"id":"F08","petal_cm":4.3,"sepal_cm":4.06,"species":1},{"id":"F09","petal_cm":4.3999999999999995,"sepal_cm":4.09,"species":1},{"id":"F10","petal_cm":4.5,"sepal_cm":4.12,"species":1},{"id":"F11","petal_cm":7.1,"sepal_cm":5,"species":2},{"id":"F12","petal_cm":7.199999999999999,"sepal_cm":None,"species":2},{"id":"F13","petal_cm":7.3,"sepal_cm":5.06,"species":2},{"id":"F14","petal_cm":7.3999999999999995,"sepal_cm":5.09,"species":2},{"id":"F15","petal_cm":7.5,"sepal_cm":5.12,"species":2}]
X = np.array([[r["petal_cm"],r["sepal_cm"]] for r in records],dtype=float)
y = np.array([r["species"] for r in records])
train,test = train_test_split(np.arange(len(records)),test_size=6,
                              random_state=42,stratify=y)
pipeline = make_pipeline(SimpleImputer(strategy="median"),
                         StandardScaler(),LogisticRegression(max_iter=1000))
pipeline.fit(X[train],y[train])
predicted = pipeline.predict(X[test])
imputer = pipeline.named_steps["simpleimputer"]
assert X.shape == (15,2) and len(predicted) == 6
print("Hoa:", len(records))
print("Ô thiếu ban đầu:", int(np.isnan(X).sum()))
print("Train/test:", len(train),len(test))
print("Median chỉ từ train:", bool(np.allclose(imputer.statistics_,np.nanmedian(X[train],axis=0))))
print(f"Accuracy test: {(predicted==y[test]).mean():.2f}")
```

**Kết quả khi chạy:**

```text
Hoa: 15
Ô thiếu ban đầu: 2
Train/test: 9 6
Median chỉ từ train: True
Accuracy test: 1.00
```

Accuracy phụ thuộc đúng **sáu hoa test giả lập**; cần dữ liệu ngoài bài để đánh giá thực tế. Mỗi số đo bị thiếu vẫn có đơn vị cm, không được tự đổi thiếu thành 0 cm.

### Tình huống 4 — Cấp 4: Đánh giá 18 hồ sơ mất ô và lệch lớp bằng confusion matrix

**Từ vựng trong mục:** **Class imbalance** — lệch tỷ lệ lớp; **Confusion matrix** — ma trận nhầm lẫn; **Recall** — độ thu hồi.

**Tình huống thực tế:** Đơn vị đào tạo có **18 hồ sơ C01…C18**, mỗi hàng gồm giờ tự học/tuần (`hours`), số hoạt động đã hoàn thành (`activities`) và nhãn hoàn thành khóa (`completed`). Có **12 nhãn 0 và 6 nhãn 1**, ba ô feature thiếu; cần tách 12 train/6 test, dùng Pipeline điền thiếu, so Logistic Regression với baseline luôn chọn lớp nhiều nhất, rồi đọc **nhầm lẫn của lớp 1** thay vì chỉ accuracy.

**Vì sao chọn cách này?** Khi lớp 0 đông hơn, baseline có thể đạt nhiều lượt đúng mà **không phát hiện người hoàn thành nào**. Ma trận nhầm lẫn ghi **hàng nhãn thật, cột dự đoán** và recall lớp 1 cho biết phát hiện được bao nhiêu người hoàn thành trong hai người lớp 1 ở test.

**Quy trình:**
1. Tạo 18 dòng với nhãn lệch và ba ô thiếu hợp lệ.
2. Chia test 6 theo nhãn; fit imputer/scaler/classifier chỉ trên 12 train, cùng tập test cho baseline.
3. Báo baseline accuracy, accuracy model, recall lớp 1 và ma trận nhầm lẫn test.

```python
import numpy as np
from sklearn.dummy import DummyClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,recall_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
records = [{"id":"C01","hours":1,"activities":2,"completed":0},{"id":"C02","hours":2,"activities":3,"completed":0},{"id":"C03","hours":None,"activities":4,"completed":0},{"id":"C04","hours":4,"activities":2,"completed":0},{"id":"C05","hours":1,"activities":3,"completed":0},{"id":"C06","hours":2,"activities":4,"completed":0},{"id":"C07","hours":3,"activities":2,"completed":0},{"id":"C08","hours":4,"activities":3,"completed":0},{"id":"C09","hours":1,"activities":4,"completed":0},{"id":"C10","hours":2,"activities":2,"completed":0},{"id":"C11","hours":3,"activities":3,"completed":0},{"id":"C12","hours":4,"activities":4,"completed":0},{"id":"C13","hours":7,"activities":9,"completed":1},{"id":"C14","hours":8,"activities":10,"completed":1},{"id":"C15","hours":9,"activities":11,"completed":1},{"id":"C16","hours":7,"activities":None,"completed":1},{"id":"C17","hours":8,"activities":10,"completed":1},{"id":"C18","hours":None,"activities":11,"completed":1}]
X = np.array([[r["hours"],r["activities"]] for r in records],dtype=float)
y = np.array([r["completed"] for r in records])
train,test = train_test_split(np.arange(len(records)),test_size=6,
                              random_state=42,stratify=y)
baseline = DummyClassifier(strategy="most_frequent").fit(X[train],y[train])
model = make_pipeline(SimpleImputer(strategy="median"),
                      StandardScaler(),LogisticRegression(max_iter=1000))
model.fit(X[train],y[train])
pred = model.predict(X[test])
cm = confusion_matrix(y[test],pred,labels=[0,1])
assert len(records)==18 and len(train)==12 and len(test)==6
print("Hồ sơ:", len(records))
print("Ô thiếu:", int(np.isnan(X).sum()))
print("Nhãn test 0/1:", int((y[test]==0).sum()),int((y[test]==1).sum()))
print(f"Accuracy baseline: {baseline.score(X[test],y[test]):.2f}")
print(f"Accuracy model: {(pred==y[test]).mean():.2f}")
print(f"Recall lớp 1: {recall_score(y[test],pred):.2f}")
print("Confusion (thật theo hàng):",cm.tolist())
```

**Kết quả khi chạy:**

```text
Hồ sơ: 18
Ô thiếu: 3
Nhãn test 0/1: 4 2
Accuracy baseline: 0.67
Accuracy model: 1.00
Recall lớp 1: 1.00
Confusion (thật theo hàng): [[4, 0], [0, 2]]
```

Những chỉ số này mô tả **sáu hồ sơ test** của bài. Không tự chọn mô hình theo test để rồi tuyên bố test vẫn là đánh giá cuối độc lập.

### Tình huống 5 — Cấp 5: Mini-project 20 hồ sơ: kiểm trùng, điền thiếu, so ba mô hình và xuất báo cáo

**Từ vựng trong mục:** **End-to-end pipeline** — quy trình xuyên suốt; **PCA** — giảm chiều; **Model report** — báo cáo mô hình.

**Tình huống thực tế:** Trung tâm có **20 dòng hồ sơ H01…H19** (vì dòng cuối trùng mã H15), mỗi dòng gồm `hours` (giờ học/tuần), `visits` (lượt truy cập), `projects` (số dự án hoàn thành) và nhãn `passed` 0/1. Có **một ID trùng, một ô dấu hỏi, một ô trống và một ô 'N/A'**. Cần kiểm và loại ID trùng, giữ 19 hồ sơ độc lập, chuyển ô số nhập sai thành thiếu, chia train/test phân tầng **14/5**, rồi so baseline, Logistic Regression đầy đủ ba đặc trưng và Logistic Regression sau PCA hai thành phần **trên đúng cùng split**. Xuất báo cáo JSON với accuracy và confusion matrix; không dùng test để chọn siêu tham số.

**Vì sao chọn cách này?** Đây là quy trình kết hợp những bài trước: kiểm lỗi đầu vào **trước khi chia**, sau đó mọi bước có tham số (`SimpleImputer`, `StandardScaler`, `PCA`, classifier) phải `.fit()` chỉ trên train. Ba mô hình chạy trên **cùng năm hồ sơ test** để so công bằng. Accuracy cao trên năm mẫu giả lập chưa có ý nghĩa đảm bảo thực tế.

**Quy trình:**
1. Tạo 20 bản ghi, báo một ID lặp; giữ bản ghi xuất hiện đầu tiên của mỗi ID.
2. Chuyển ba cột đo sang số, coi dữ liệu không đọc được là NaN; chia 19 hồ sơ còn lại thành train 14/test 5 có phân tầng.
3. Fit baseline, pipeline đầy đủ và pipeline PCA hai thành phần trên cùng train; dự đoán cùng test, xuất `model_report_20.json` chứa số dòng, missing, accuracy và confusion matrix.

```python
import json
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.dummy import DummyClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
raw = [{"id":"H01","hours":1,"visits":1,"projects":0,"passed":0},{"id":"H02","hours":2,"visits":2,"projects":1,"passed":0},{"id":"H03","hours":3,"visits":3,"projects":0,"passed":0},{"id":"H04","hours":1,"visits":1,"projects":1,"passed":0},{"id":"H05","hours":2,"visits":"?","projects":0,"passed":0},{"id":"H06","hours":3,"visits":3,"projects":1,"passed":0},{"id":"H07","hours":1,"visits":1,"projects":0,"passed":0},{"id":"H08","hours":2,"visits":2,"projects":1,"passed":0},{"id":"H09","hours":3,"visits":3,"projects":0,"passed":0},{"id":"H10","hours":1,"visits":1,"projects":1,"passed":0},{"id":"H11","hours":7,"visits":8,"projects":5,"passed":1},{"id":"H12","hours":8,"visits":9,"projects":6,"passed":1},{"id":"H13","hours":9,"visits":10,"projects":5,"passed":1},{"id":"H14","hours":7,"visits":8,"projects":6,"passed":1},{"id":"H15","hours":None,"visits":9,"projects":5,"passed":1},{"id":"H16","hours":9,"visits":10,"projects":6,"passed":1},{"id":"H17","hours":7,"visits":8,"projects":5,"passed":1},{"id":"H18","hours":8,"visits":9,"projects":"N/A","passed":1},{"id":"H19","hours":9,"visits":10,"projects":5,"passed":1},{"id":"H15","hours":7,"visits":8,"projects":6,"passed":1}]
df = pd.DataFrame(raw)
duplicate_count = int(df["id"].duplicated().sum())
df = df.drop_duplicates(subset="id",keep="first").reset_index(drop=True)
feature_columns = ["hours","visits","projects"]
X = df[feature_columns].apply(pd.to_numeric,errors="coerce").to_numpy(dtype=float)
y = df["passed"].to_numpy(dtype=int)
missing_count = int(np.isnan(X).sum())
train,test = train_test_split(np.arange(len(df)),test_size=5,
                              random_state=42,stratify=y)
baseline = DummyClassifier(strategy="most_frequent").fit(X[train],y[train])
full = make_pipeline(SimpleImputer(strategy="median"),StandardScaler(),
                     LogisticRegression(max_iter=1000))
pca = make_pipeline(SimpleImputer(strategy="median"),StandardScaler(),
                    PCA(n_components=2),LogisticRegression(max_iter=1000))
full.fit(X[train],y[train])
pca.fit(X[train],y[train])
pred = full.predict(X[test])
report = {"raw_rows":len(raw),"unique_rows":len(df),"duplicates":duplicate_count,
          "missing_cells":missing_count,"train_rows":len(train),"test_rows":len(test),
          "accuracy_baseline":round(accuracy_score(y[test],baseline.predict(X[test])),2),
          "accuracy_full":round(accuracy_score(y[test],pred),2),
          "accuracy_pca":round(accuracy_score(y[test],pca.predict(X[test])),2),
          "confusion":confusion_matrix(y[test],pred,labels=[0,1]).tolist()}
path = Path("model_report_20.json")
path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
assert len(raw)==20 and len(df)==19 and set(train).isdisjoint(test)
print("Dòng gốc/trùng/còn:",report["raw_rows"],report["duplicates"],report["unique_rows"])
print("Ô thiếu sau chuyển kiểu:",report["missing_cells"])
print("Train/test:",report["train_rows"],report["test_rows"])
print("Accuracy baseline/full/PCA:",report["accuracy_baseline"],report["accuracy_full"],report["accuracy_pca"])
print("Confusion (thật theo hàng):",report["confusion"])
print("Đã lưu JSON:",path.is_file() and json.loads(path.read_text(encoding="utf-8"))==report)
```

**Kết quả khi chạy:**

```text
Dòng gốc/trùng/còn: 20 1 19
Ô thiếu sau chuyển kiểu: 3
Train/test: 14 5
Accuracy baseline/full/PCA: 0.6 1.0 1.0
Confusion (thật theo hàng): [[3, 0], [0, 2]]
Đã lưu JSON: True
```

Bản báo cáo chứa đúng dữ liệu **mô phỏng** và chỉ số từ năm test; không được coi kết quả này là chứng nhận độ tin cậy ngoài đời. Không thử nhiều phương án rồi chọn dựa trên chính năm test nếu vẫn muốn gọi đó là đánh giá cuối độc lập.

## 6. Sai lầm thường gặp

- X là cột đặc trưng, y là nhãn; không đưa nhãn hoặc kết quả biết sau sự kiện vào feature.
- Phải chia train/test trước khi học median, mean/std hoặc PCA để tránh rò rỉ.
- Không `fit_transform` PCA trên X_test; chỉ `transform` bằng PCA đã fit từ train.
- Accuracy cao vẫn có thể che lỗi lớp hiếm; đọc thêm confusion matrix theo hàng thật–cột dự đoán.
- Thay đổi split hoặc metric khi so hai phương pháp sẽ gây so sánh thiếu công bằng.
- Đánh giá trên test không phải huấn luyện; chỉnh siêu tham số dựa mãi vào test làm rò rỉ đánh giá.

## 7. Trắc nghiệm

**Q1. What is a feature in supervised learning? | Feature trong học có giám sát là gì?**

A. An input measurement used by the predictor | Đại lượng đo đầu vào mô hình sử dụng

B. A target value the model should predict | Giá trị đích mô hình cần dự đoán

C. An ordered chain of preprocessing and model steps | Chuỗi tiền xử lý và mô hình có thứ tự

D. Checking predictions against held-out targets | So dự đoán với nhãn thật giữ riêng

**Đáp án: A**

**Giải thích:** Trong Iris, bốn số đo cm nằm ở X, không phải nhãn y. Nếu đưa kết quả tương lai hoặc mã lớp vào X, đánh giá sẽ dễ giả tạo do rò rỉ.


**Q2. What is a label? | Label là gì?**

A. An input measurement used by the predictor | Đại lượng đo đầu vào mô hình sử dụng

B. A target value the model should predict | Giá trị đích mô hình cần dự đoán

C. An ordered chain of preprocessing and model steps | Chuỗi tiền xử lý và mô hình có thứ tự

D. Checking predictions against held-out targets | So dự đoán với nhãn thật giữ riêng

**Đáp án: B**

**Giải thích:** Classifier có giám sát học từ nhãn thật ghép với từng hàng train. Mỗi trong 150 hàng đặc trưng cần có nhãn tương ứng khi train.


**Q3. What is a pipeline? | Pipeline là gì?**

A. An input measurement used by the predictor | Đại lượng đo đầu vào mô hình sử dụng

B. A target value the model should predict | Giá trị đích mô hình cần dự đoán

C. An ordered chain of preprocessing and model steps | Chuỗi tiền xử lý và mô hình có thứ tự

D. Checking predictions against held-out targets | So dự đoán với nhãn thật giữ riêng

**Đáp án: C**

**Giải thích:** Nó fit bộ biến đổi trên train rồi tái sử dụng cho dữ liệu sau. Thứ tự rất quan trọng: điền thiếu và chuẩn hóa trước dự đoán, nhưng tham số chỉ học từ train.


**Q4. What is evaluation? | Evaluation là gì?**

A. An input measurement used by the predictor | Đại lượng đo đầu vào mô hình sử dụng

B. A target value the model should predict | Giá trị đích mô hình cần dự đoán

C. An ordered chain of preprocessing and model steps | Chuỗi tiền xử lý và mô hình có thứ tự

D. Checking predictions against held-out targets | So dự đoán với nhãn thật giữ riêng

**Đáp án: D**

**Giải thích:** Test cuối đánh giá dữ liệu chưa fit, không dùng lại mẫu học. Hãy dùng test giữ riêng không thay đổi; điểm train cao có thể chỉ là ghi nhớ dữ liệu.


**Q5. What does an Iris feature row represent? | Một hàng feature Iris biểu diễn gì?**

A. Four measurements for one flower | Bốn số đo của một bông hoa

B. The target class per sample | Lớp mục tiêu cho từng mẫu

C. Unavailable evaluation information entering fitting | Thông tin đánh giá đáng lẽ chưa biết lọt vào fit

D. To check sample/feature dimensions and alignment | Để kiểm chiều mẫu/đặc trưng và sự khớp nhãn

**Đáp án: A**

**Giải thích:** Hàng là một mẫu hoa, cột là số đo như chiều dài cánh. Với shape (150,4), 150 là mẫu, bốn là biến đo theo cm.


**Q6. What does y represent in classification? | y biểu diễn gì khi phân loại?**

A. Four measurements for one flower | Bốn số đo của một bông hoa

B. The target class per sample | Lớp mục tiêu cho từng mẫu

C. Unavailable evaluation information entering fitting | Thông tin đánh giá đáng lẽ chưa biết lọt vào fit

D. To check sample/feature dimensions and alignment | Để kiểm chiều mẫu/đặc trưng và sự khớp nhãn

**Đáp án: B**

**Giải thích:** Nhãn y phải ghép một-một với các hàng X. Nếu X và y sai thứ tự, thuật toán đúng vẫn học sai mối quan hệ dữ liệu–nhãn.


**Q7. What is data leakage? | Rò rỉ dữ liệu là gì?**

A. Four measurements for one flower | Bốn số đo của một bông hoa

B. The target class per sample | Lớp mục tiêu cho từng mẫu

C. Unavailable evaluation information entering fitting | Thông tin đánh giá đáng lẽ chưa biết lọt vào fit

D. To check sample/feature dimensions and alignment | Để kiểm chiều mẫu/đặc trưng và sự khớp nhãn

**Đáp án: C**

**Giải thích:** Fit tiền xử lý trên test hoặc dùng kết quả tương lai có thể làm chỉ số ảo. Rò rỉ còn xảy ra nếu chọn đặc trưng từ toàn bộ dữ liệu trước khi chia.


**Q8. Why inspect X.shape and y.shape first? | Vì sao kiểm X.shape và y.shape đầu tiên?**

A. Four measurements for one flower | Bốn số đo của một bông hoa

B. The target class per sample | Lớp mục tiêu cho từng mẫu

C. Unavailable evaluation information entering fitting | Thông tin đánh giá đáng lẽ chưa biết lọt vào fit

D. To check sample/feature dimensions and alignment | Để kiểm chiều mẫu/đặc trưng và sự khớp nhãn

**Đáp án: D**

**Giải thích:** Số hàng X lệch số nhãn y khiến việc fit sai. Hàng và nhãn lệch nhau phải được sửa trước khi fit hoặc tính điểm.


**Q9. What does train_test_split do? | train_test_split làm gì?**

A. Separates data into fitting and held-out portions | Chia dữ liệu thành phần học và phần giữ riêng

B. To preserve approximate class ratios in split parts | Để giữ tương đối tỷ lệ lớp trong các tập

C. Training features | Các đặc trưng train

D. Training features only | Chỉ đặc trưng train

**Đáp án: A**

**Giải thích:** Hàm chia dữ liệu, không tự học mô hình hay đo accuracy. Phải giữ cả X và y train/test; chia dữ liệu không tự tương đương huấn luyện.


**Q10. Why use stratify=y? | Vì sao dùng stratify=y?**

A. Separates data into fitting and held-out portions | Chia dữ liệu thành phần học và phần giữ riêng

B. To preserve approximate class ratios in split parts | Để giữ tương đối tỷ lệ lớp trong các tập

C. Training features | Các đặc trưng train

D. Training features only | Chỉ đặc trưng train

**Đáp án: B**

**Giải thích:** Giúp giảm lệch lớp khi mỗi lớp có đủ mẫu. Phân tầng hữu ích khi lớp ít mẫu có nguy cơ vắng khỏi tập test.


**Q11. What should SimpleImputer learn from? | SimpleImputer nên học từ đâu?**

A. Separates data into fitting and held-out portions | Chia dữ liệu thành phần học và phần giữ riêng

B. To preserve approximate class ratios in split parts | Để giữ tương đối tỷ lệ lớp trong các tập

C. Training features | Các đặc trưng train

D. Training features only | Chỉ đặc trưng train

**Đáp án: C**

**Giải thích:** Median tính từ toàn bộ dữ liệu làm lộ thống kê test. Hàng test không được tác động đến giá trị điền học được, kể cả khi hàng ấy thiếu dữ liệu.


**Q12. What should StandardScaler learn from? | StandardScaler nên fit từ đâu?**

A. Separates data into fitting and held-out portions | Chia dữ liệu thành phần học và phần giữ riêng

B. To preserve approximate class ratios in split parts | Để giữ tương đối tỷ lệ lớp trong các tập

C. Training features | Các đặc trưng train

D. Training features only | Chỉ đặc trưng train

**Đáp án: D**

**Giải thích:** Biến đổi test bằng mean/std train, không fit từ test. Mean và variance từ train phải được áp nhất quán lên mọi mẫu mới.


**Q13. What does LogisticRegression produce in Iris? | LogisticRegression trên Iris dự đoán gì?**

A. One of three discrete flower classes | Một trong ba loài hoa rời rạc

B. Correct predictions divided by total predictions | Số dự đoán đúng chia tổng số dự đoán

C. Actual labels | Các nhãn thật

D. Predicted labels | Các nhãn dự đoán

**Đáp án: A**

**Giải thích:** Dù có chữ Regression, LogisticRegression dùng để phân loại. Mô hình có thể xuất xác suất lớp, nhưng nhiệm vụ đang xét chọn một nhãn rời rạc.


**Q14. What does accuracy count? | Accuracy đếm gì?**

A. One of three discrete flower classes | Một trong ba loài hoa rời rạc

B. Correct predictions divided by total predictions | Số dự đoán đúng chia tổng số dự đoán

C. Actual labels | Các nhãn thật

D. Predicted labels | Các nhãn dự đoán

**Đáp án: B**

**Giải thích:** Accuracy hữu ích nhưng có thể che lỗi lớp hiếm. Với tập lệch lớp, accuracy cao có thể đến từ việc chỉ đoán lớp đông nhất.


**Q15. What do confusion matrix rows mean? | Hàng của confusion matrix nghĩa là gì?**

A. One of three discrete flower classes | Một trong ba loài hoa rời rạc

B. Correct predictions divided by total predictions | Số dự đoán đúng chia tổng số dự đoán

C. Actual labels | Các nhãn thật

D. Predicted labels | Các nhãn dự đoán

**Đáp án: C**

**Giải thích:** Mỗi hàng đếm mẫu thuộc lớp thật tương ứng. Hàng đại diện nhãn thật; ô ngoài đường chéo là lỗi xuất phát từ lớp thật ở hàng đó.


**Q16. What do confusion matrix columns mean? | Cột của confusion matrix nghĩa là gì?**

A. One of three discrete flower classes | Một trong ba loài hoa rời rạc

B. Correct predictions divided by total predictions | Số dự đoán đúng chia tổng số dự đoán

C. Actual labels | Các nhãn thật

D. Predicted labels | Các nhãn dự đoán

**Đáp án: D**

**Giải thích:** Ô ngoài đường chéo là trường hợp dự đoán sang lớp khác. Cột cho biết lớp dự đoán nào nhận các mẫu bị gán nhầm.


**Q17. What does PCA reduce? | PCA giảm gì?**

A. Feature dimensionality while retaining sample rows | Số chiều đặc trưng nhưng giữ số hàng mẫu

B. To avoid using test distribution to learn axes | Tránh lấy phân phối test để học các trục

C. On the same held-out split and metric | Trên cùng tập test và chỉ số đánh giá

D. No, held-out evaluation is needed | Không, phải đánh giá dữ liệu giữ riêng

**Đáp án: A**

**Giải thích:** Thành phần PCA là trục đặc trưng mới, không phải nhãn. Trục PCA là tổ hợp đặc trưng ban đầu được học, không làm đổi số mẫu.


**Q18. Why fit PCA on train only? | Vì sao chỉ fit PCA trên train?**

A. Feature dimensionality while retaining sample rows | Số chiều đặc trưng nhưng giữ số hàng mẫu

B. To avoid using test distribution to learn axes | Tránh lấy phân phối test để học các trục

C. On the same held-out split and metric | Trên cùng tập test và chỉ số đánh giá

D. No, held-out evaluation is needed | Không, phải đánh giá dữ liệu giữ riêng

**Đáp án: B**

**Giải thích:** Test chỉ được transform bằng PCA đã fit từ train. Nếu không, thông tin phân phối test đã lọt vào biểu diễn đặc trưng.


**Q19. How should baseline and PCA models be compared? | So baseline và mô hình PCA thế nào?**

A. Feature dimensionality while retaining sample rows | Số chiều đặc trưng nhưng giữ số hàng mẫu

B. To avoid using test distribution to learn axes | Tránh lấy phân phối test để học các trục

C. On the same held-out split and metric | Trên cùng tập test và chỉ số đánh giá

D. No, held-out evaluation is needed | Không, phải đánh giá dữ liệu giữ riêng

**Đáp án: C**

**Giải thích:** Khác split hoặc metric không tách được ảnh hưởng của PCA. Train/test phải giống nhau giữa hai cách để chênh lệch metric phản ánh thay đổi mô hình.


**Q20. Does a high train score prove model generalization? | Train score cao có chứng minh tổng quát hóa?**

A. Feature dimensionality while retaining sample rows | Số chiều đặc trưng nhưng giữ số hàng mẫu

B. To avoid using test distribution to learn axes | Tránh lấy phân phối test để học các trục

C. On the same held-out split and metric | Trên cùng tập test và chỉ số đánh giá

D. No, held-out evaluation is needed | Không, phải đánh giá dữ liệu giữ riêng

**Đáp án: D**

**Giải thích:** Mô hình có thể nhớ train nhưng dự đoán kém trên mẫu mới. Cần báo metric test và lỗi theo lớp trước khi đánh giá khả năng ứng dụng thực tế.

## 8. Nối sang bài tiếp

`Python → NumPy/Pandas → Train/Test → Pipeline → Report`.
