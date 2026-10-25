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
# Mục đích: Phân biệt đầu vào và nhãn đích qua dữ liệu Iris của scikit-learn.
# Dữ liệu: Iris có 150 hoa, 4 đặc trưng/hoa và một nhãn loài/hoa.
# sklearn.datasets cung cấp dữ liệu mẫu Iris cho ví dụ nhận dạng đầu vào/nhãn.
# load_iris() tải bộ dữ liệu mẫu Iris; không dùng dữ liệu của người học.
from sklearn.datasets import load_iris

# load_iris() tải bộ dữ liệu mẫu Iris; không dùng dữ liệu của người học.
# Đối tượng Bunch của sklearn giữ ma trận feature tại data.data và nhãn tại data.target.
data = load_iris()
# data.data.shape=(150,4): 150 hàng là hoa, bốn cột là số đo.
# data.target.shape=(150,): một mã loài cho mỗi hoa, không phải bốn nhãn.
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
# Mục đích: Điền ô dữ liệu thiếu bằng trung vị của các giá trị còn lại.
# Dữ liệu: Series gồm ba giá trị 5, None, 7; None được hiểu là ô chưa ghi, không phải 0.
# Pandas quản lý bảng, dữ liệu thiếu và thao tác làm sạch.
import pandas as pd

# Series của Pandas giữ các vị trí có giá trị thiếu (NaN).
values = pd.Series([5.0, None, 7.0])
# median() lấy trung vị chỉ từ các ô có dữ liệu, ra 6; mặc định bỏ qua NaN.
# fillna(value) thay ô thiếu bằng trung vị, trả Series mới nếu không có inplace=True.
# tolist() đổi kết quả Series thành list Python để dễ đọc.
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
# Mục đích: Tạo pipeline tiền xử lý và phân loại nhưng chưa huấn luyện mô hình.
# Dữ liệu: Ba bước imputer→scaler→LogisticRegression; chưa có X_train hoặc y_train.
# make_pipeline ghép các bước để transform Test bằng thống kê Train đã học.
from sklearn.pipeline import make_pipeline
# SimpleImputer thay dữ liệu thiếu theo thống kê chỉ học từ Train.
from sklearn.impute import SimpleImputer
# StandardScaler học mean/SD từng cột từ Train rồi chuẩn hóa.
from sklearn.preprocessing import StandardScaler
# LogisticRegression phân loại nhãn rời rạc, không dự báo giá trị liên tục.
from sklearn.linear_model import LogisticRegression

# make_pipeline() ghép các bước thành một quy trình; chỉ khi fit() mới học thống kê và tham số từ dữ liệu.
model = make_pipeline(
    # strategy='median' dùng trung vị theo TỪNG CỘT được học khi fit; không dùng mean.
    SimpleImputer(strategy='median'),
    # Scaler đưa đặc trưng về gần mean 0 và std 1 dựa trên dữ liệu train sau điền ô thiếu.
    StandardScaler(),
    # Bộ phân loại LogisticRegression tối ưu tối đa 1000 vòng lặp, không phải 1000 mẫu.
    LogisticRegression(max_iter=1000),
)
# steps là list ba cặp (tên,bước); len() đếm ba thành phần, không phải Accuracy.
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
# Mục đích: Đọc bảng nhầm lẫn để hiểu mô hình dự đoán sai lớp nào.
# Dữ liệu: 4 nhãn thật và 4 nhãn đoán, cùng thứ tự mỗi học viên; có một lớp 1 bị đoán nhầm 0.
# confusion_matrix dùng để đếm các cặp (nhãn thật,nhãn dự đoán).
from sklearn.metrics import confusion_matrix

# Nhãn thật y_true của bốn hồ sơ, không phải xác suất.
actual = [0, 1, 1, 0]
# Nhãn dự đoán y_pred theo đúng thứ tự actual.
predicted = [0, 1, 0, 0]
# Hàng là nhãn THẬT, cột là nhãn DỰ ĐOÁN; phần tử hàng 1/cột 0 là false negative lớp 1.
# Chuyển ma trận NumPy 2×2 thành list lồng để in.
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

**Tình huống thực tế:** Trung tâm đào tạo chuẩn bị **10 hồ sơ HV01–HV10** để thử làm dự án dự đoán kết quả học tập. Mỗi hàng ghi mã học viên, **số giờ tự học trong tuần (`hours`, giờ/tuần)**, **số bài luyện tập (`practice`, bài)** và kết quả `passed`: **0 là chưa đạt, 1 là đạt**. Có **6 người chưa đạt và 4 người đạt**. Trước khi đưa dữ liệu cho máy học, nhóm phải kiểm có đủ 10 người, mỗi người một mã, hai thông tin đầu vào đều có số, và **không đưa kết quả `passed` vào các cột dùng để dự đoán**. Câu hỏi ở bước này chỉ là dữ liệu đã sẵn sàng chưa, chưa phải mô hình dự đoán đúng bao nhiêu.

**Vì sao chọn cách này?** **Feature (đặc trưng)** là thông tin mô hình có thể nhìn để dự đoán; trong bài gồm **giờ học** và **số bài luyện tập**. **Label (nhãn)** là câu trả lời đúng mà sau này mô hình phải đoán, chính là `passed`. `pandas.DataFrame(records)` tạo bảng **mỗi hàng một người**; `X = df[['hours', 'practice']]` chọn đúng hai cột đầu vào, `y = df['passed']` giữ riêng câu trả lời. Sau đó kiểm số hàng, `X.shape` (hình dạng **10 hàng × 2 cột**), đếm hai nhãn, dùng `duplicated()` tìm mã trùng và `isna()` đếm ô thiếu. Mã HV01 là **định danh**, không phải một đại lượng đo mức học tập nên không đưa vào X; đưa `passed` vào X sẽ làm mô hình **nhìn thấy đáp án** và tạo kết quả đánh giá sai lệch. Bước này chỉ kiểm dữ liệu, chưa huấn luyện.

**Quy trình:**
1. Tạo đủ 10 hàng với ý nghĩa/đơn vị từng cột.
2. Lấy đúng hai feature số sang X, nhãn mục tiêu sang y.
3. Xác nhận số dòng khớp, ID duy nhất, không thiếu số đo và in phân bố nhãn.

```python
# Mục đích: Kiểm dữ liệu đầu vào của bài toán dự đoán đỗ: số hồ sơ, đặc trưng, nhãn, trùng mã và ô khuyết.
# Dữ liệu: 10 học viên HV01..HV10; hours=giờ học, practice=số lần thực hành, passed=nhãn 0/1.
# Pandas quản lý bảng, dữ liệu thiếu và thao tác làm sạch.
import pandas as pd
# List 10 dictionary, mỗi dict là một học viên; hours/practice là đầu vào, passed là kết quả cần đoán.
records = [{"id":"HV01","hours":1,"practice":2,"passed":0},{"id":"HV02","hours":2,"practice":3,"passed":0},{"id":"HV03","hours":3,"practice":4,"passed":0},{"id":"HV04","hours":4,"practice":5,"passed":0},{"id":"HV05","hours":5,"practice":2,"passed":0},{"id":"HV06","hours":1,"practice":3,"passed":0},{"id":"HV07","hours":2,"practice":4,"passed":1},{"id":"HV08","hours":3,"practice":5,"passed":1},{"id":"HV09","hours":4,"practice":2,"passed":1},{"id":"HV10","hours":5,"practice":3,"passed":1}]
# DataFrame tạo bảng một hàng trên mỗi dictionary, cột từ các key.
df = pd.DataFrame(records)
# Hai cặp ngoặc vuông chọn DANH SÁCH hai cột thành DataFrame X shape (10,2), không dùng passed làm feature.
X = df[["hours", "practice"]]
# Một cặp ngoặc chọn Series nhãn y 10 giá trị 0/1.
y = df["passed"]
# shape lưu (số hàng,số cột); kiểm đúng 10 học viên và 2 feature.
# Điều kiện bảo vệ kiểm cấu trúc số mẫu và tránh Train/Test dùng chung trước khi báo cáo.
if len(df) != 10 or X.shape != (10, 2) or len(y) != 10:
    # raise ném lỗi khi cấu trúc dữ liệu không hợp lệ; tránh in kết luận thiếu mẫu.
    # raise ValueError dừng kịch bản khi dữ liệu không đúng số mẫu hoặc điều kiện kiểm thử.
    raise ValueError("Cần 10 hồ sơ, hai đặc trưng và 10 nhãn.")
print("Hồ sơ:", len(df))
# shape[1] lấy SỐ CỘT đặc trưng, khác shape[0] là số hàng.
print("Feature:", X.shape[1])
# So từng nhãn với 0/1 tạo mask Boolean; sum() đếm lượt True trong từng lớp.
print("Nhãn 0/1:", int((y==0).sum()), int((y==1).sum()))
# duplicated() đánh dấu ID lặp từ lần xuất hiện thứ hai; sum() đếm dòng trùng nhưng không xóa.
print("ID trùng:", int(df["id"].duplicated().sum()))
# isna() đánh dấu NaN từng ô; sum() thứ nhất tổng theo cột, thứ hai tổng tất cả cột.
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

**Tình huống thực tế:** Nhóm giáo viên có **12 hồ sơ HV01–HV12** với hai đặc trưng **giờ tự học (giờ/tuần)** và **số bài luyện tập (bài)**, cùng nhãn `passed` **0/1**. Sáu người thuộc lớp 0 và sáu người thuộc lớp 1. Trước khi thử mô hình học máy thực sự, họ muốn dành **8 hồ sơ để học (train)**, **4 hồ sơ chưa dùng để đánh giá (test)**, rồi xem một cách dự đoán cực đơn giản — **luôn đoán nhãn thường gặp nhất trong train** — đạt bao nhiêu trên bốn người test. Đây là **mức chuẩn ban đầu (baseline)** để biết mô hình phức tạp có cải thiện thật hay không.

**Vì sao chọn cách này?** **Train/test split** dành một phần người học làm **dữ liệu kiểm tra chưa được dùng trong huấn luyện**. `train_test_split` giữ đủ hai nhãn bằng `stratify=y`; `random_state=42` giúp tạo lại đúng cách chia 8/4 để đối chiếu. **DummyClassifier** kiểu `most_frequent` chỉ học xem **nhãn nào xuất hiện nhiều nhất trong tám người train**, rồi dùng nhãn ấy cho mọi dự đoán, không nhìn giờ học hay số bài để tìm quy luật. `accuracy` là **tỷ lệ nhãn dự đoán đúng trong bốn người test**; dữ liệu test cân bằng hai lớp nên baseline đạt **0,50**, không phải kết quả mô hình đã hiểu việc học. Đặt baseline trước khi thử mô hình mới giúp có một mốc so sánh; mẫu bốn người quá nhỏ để khẳng định chất lượng trên toàn bộ học viên.

**Quy trình:**
1. Đọc 12 bộ X/y/ID có cùng thứ tự.
2. Chia 8 train và 4 test phân tầng, kiểm ID không giao nhau.
3. Fit baseline trên train, đánh giá accuracy trên test và in số mẫu của từng lớp test.

```python
# Mục đích: Chia Train/Test cân bằng nhãn và đo mô hình baseline luôn chọn lớp phổ biến.
# Dữ liệu: 12 học viên, hai feature hours/practice và nhãn 0/1, chọn 8 Train + 4 Test.
# NumPy hỗ trợ ndarray, NaN và chỉ số các hàng train/test.
import numpy as np
# DummyClassifier là baseline đoán lớp phổ biến, không học quan hệ feature.
from sklearn.dummy import DummyClassifier
# train_test_split chia đồng bộ hàng Train và Test trước khi fit.
from sklearn.model_selection import train_test_split
# Mỗi dictionary lưu id, giờ học, lượt luyện tập và nhãn đỗ; 12 mẫu tạo hai nhóm nhãn.
records = [{"id":"HV01","hours":1,"practice":2,"passed":0},{"id":"HV02","hours":2,"practice":3,"passed":0},{"id":"HV03","hours":3,"practice":4,"passed":0},{"id":"HV04","hours":1,"practice":2,"passed":0},{"id":"HV05","hours":2,"practice":3,"passed":0},{"id":"HV06","hours":3,"practice":4,"passed":0},{"id":"HV07","hours":6,"practice":8,"passed":1},{"id":"HV08","hours":7,"practice":9,"passed":1},{"id":"HV09","hours":8,"practice":10,"passed":1},{"id":"HV10","hours":6,"practice":8,"passed":1},{"id":"HV11","hours":7,"practice":9,"passed":1},{"id":"HV12","hours":8,"practice":10,"passed":1}]
# List sẽ chứa một cặp [hours,practice] cho mỗi học viên, theo đúng thứ tự nhãn.
features = []
# List nhãn passed cùng vị trí với features.
labels = []
for row in records:
    # append() đưa hai feature của hồ sơ hiện tại vào X.
    features.append([row["hours"], row["practice"]])
    # append() ghi nhãn tương ứng để X/y không lệch hàng.
    labels.append(row["passed"])
# Ép đặc trưng thành ma trận số thực shape (12,2), phù hợp sklearn.
X = np.array(features, dtype=float)
# Nhãn y thành vector 12 phần tử, một lớp cho mỗi người.
y = np.array(labels)
# Chia các chỉ số hàng thay vì chia X và y độc lập, giúp trích dữ liệu đồng bộ.
# arange(12) tạo các chỉ số 0..11, cận 12 không bao gồm.
# test_size=4 giữ đúng bốn mẫu CHƯA fit để kiểm tra, không có nghĩa 4%.
# Cố định trạng thái ngẫu nhiên để phép chia có thể lặp lại.
# Giữ tỷ lệ nhãn 0/1 gần giống nhau trên Train/Test.
train,test = train_test_split(np.arange(12),test_size=4,random_state=42,stratify=y)
# Baseline không học quy luật feature: luôn dự đoán nhãn đông nhất trong TRAIN.
model = DummyClassifier(strategy="most_frequent")
# fit() học baseline CHỈ từ các hàng Train; X[train] và y[train] dùng cùng index.
model.fit(X[train],y[train])
# score() trả Accuracy trên Test: tỷ lệ dự đoán đúng từ 4 hồ sơ chưa fit.
accuracy = model.score(X[test],y[test])
# Chuyển Train sang set rồi kiểm không có index trùng với Test, tránh rò rỉ mẫu.
# Điều kiện bảo vệ kiểm cấu trúc số mẫu và tránh Train/Test dùng chung trước khi báo cáo.
if len(records) != 12 or not set(train).isdisjoint(test):
    # raise ValueError dừng kịch bản khi dữ liệu không đúng số mẫu hoặc điều kiện kiểm thử.
    raise ValueError("Cần 12 hồ sơ và Train/Test không trùng mẫu.")
print("Hồ sơ:", len(records))
# len() đếm tám mẫu train (len(test) đếm bốn mẫu test).
print("Train/test:", len(train), len(test))
# Boolean mask chỉ đếm nhãn lớp 0/1 trong Test, không phải toàn bộ 12 mẫu.
print("Nhãn test 0/1:", int((y[test]==0).sum()), int((y[test]==1).sum()))
# f-string :.2f chỉ làm tròn Accuracy khi IN, giá trị lưu vẫn là số thực gốc.
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

**Tình huống thực tế:** Nhóm nghiên cứu cây trồng có **15 bông hoa F01–F15**, mỗi bông ghi hai phép đo **chiều dài cánh hoa và chiều dài đài hoa (cm)**, cùng mã loài **0, 1 hoặc 2**; mỗi loài có năm bông. **F04 thiếu chiều dài cánh**, còn **F12 thiếu chiều dài đài** nên không thể đưa thẳng mọi ô vào mô hình. Nhóm cần giữ **6 bông test**, học từ **9 bông train**, dùng thông tin của train để điền số đo còn thiếu, rồi thử phân loại loài của sáu bông được giữ riêng. Mục tiêu còn là kiểm chắc chắn **sáu bông test không bị dùng khi tính cách điền thiếu**.

**Vì sao chọn cách này?** **Dữ liệu thiếu** có nghĩa là **chưa có phép đo**, không phải chiều dài 0 cm. **Median (trung vị)** là số nằm giữa những giá trị có số sau khi sắp thứ tự; `SimpleImputer(strategy='median')` dùng trung vị **tính riêng từng cột từ chín bông train** để điền ô thiếu khi cần. **StandardScaler** tiếp tục đưa các cột số đo về cách biểu diễn phù hợp cho mô hình, rồi **Logistic Regression** học cách phân biệt ba loài. `make_pipeline` xếp các bước theo đúng thứ tự **điền thiếu → chuẩn hóa → phân loại**: gọi `fit` chỉ với train khiến thông số của cả ba bước được học **không có hoa test**. Nếu tính trung vị hoặc trung bình từ cả 15 bông trước khi chia sẽ có **rò rỉ dữ liệu (data leakage)**. Chương trình so trung vị bên trong pipeline với trung vị train, dự đoán sáu hoa test và tính accuracy; kết quả 1,00 trên mẫu nhỏ giả lập **không chứng minh mô hình luôn đúng**.

**Quy trình:**
1. Lưu 15 hoa và chuyển None trong cột số thành NaN; kiểm đúng hai ô thiếu.
2. Tách train/test phân tầng 9/6 trước khi `.fit()` tiền xử lý.
3. Huấn luyện Pipeline, so median đã học với `nanmedian(X_train)`, đo accuracy test và kiểm số dự đoán.

```python
# Mục đích: Huấn luyện phân loại 3 loài hoa với imputer→scaler→logistic chỉ fit trên Train.
# Dữ liệu: 15 hoa F01..F15, hai feature petal_cm/sepal_cm đo cm, vài None, ba loài 0/1/2; Test 6 hoa.
# NumPy hỗ trợ ndarray, NaN và chỉ số các hàng train/test.
import numpy as np
# SimpleImputer thay dữ liệu thiếu theo thống kê chỉ học từ Train.
from sklearn.impute import SimpleImputer
# LogisticRegression phân loại nhãn rời rạc, không dự báo giá trị liên tục.
from sklearn.linear_model import LogisticRegression
# train_test_split chia đồng bộ hàng Train và Test trước khi fit.
from sklearn.model_selection import train_test_split
# make_pipeline ghép các bước để transform Test bằng thống kê Train đã học.
from sklearn.pipeline import make_pipeline
# StandardScaler học mean/SD từng cột từ Train rồi chuẩn hóa.
from sklearn.preprocessing import StandardScaler
# List 15 hoa có None nghĩa số đo thiếu, không phải 0 cm; nhãn species là mục tiêu dự đoán.
records = [{"id":"F01","petal_cm":1.1,"sepal_cm":3,"species":0},{"id":"F02","petal_cm":1.2000000000000002,"sepal_cm":3.03,"species":0},{"id":"F03","petal_cm":1.3,"sepal_cm":3.06,"species":0},{"id":"F04","petal_cm":None,"sepal_cm":3.09,"species":0},{"id":"F05","petal_cm":1.5,"sepal_cm":3.12,"species":0},{"id":"F06","petal_cm":4.1,"sepal_cm":4,"species":1},{"id":"F07","petal_cm":4.199999999999999,"sepal_cm":4.03,"species":1},{"id":"F08","petal_cm":4.3,"sepal_cm":4.06,"species":1},{"id":"F09","petal_cm":4.3999999999999995,"sepal_cm":4.09,"species":1},{"id":"F10","petal_cm":4.5,"sepal_cm":4.12,"species":1},{"id":"F11","petal_cm":7.1,"sepal_cm":5,"species":2},{"id":"F12","petal_cm":7.199999999999999,"sepal_cm":None,"species":2},{"id":"F13","petal_cm":7.3,"sepal_cm":5.06,"species":2},{"id":"F14","petal_cm":7.3999999999999995,"sepal_cm":5.09,"species":2},{"id":"F15","petal_cm":7.5,"sepal_cm":5.12,"species":2}]
# Tạo list hai đặc trưng (cánh hoa, đài hoa) theo đúng thứ tự mỗi hàng.
features = []
# Tạo list nhãn loài của cùng hàng feature.
labels = []
for row in records:
    # append() giữ cặp feature có thể có None, imputer xử lý sau.
    features.append([row["petal_cm"], row["sepal_cm"]])
    # append() giữ nhãn species của hoa đang xét.
    labels.append(row["species"])
# Chuyển None thành NaN trong ndarray số thực shape (15,2).
X = np.array(features, dtype=float)
# Mảng nhãn 15 giá trị nguyên (mỗi hoa một nhãn).
y = np.array(labels)
# Chia INDEX Train/Test trước khi fit để tránh rò rỉ thống kê tiền xử lý.
# Sáu hoa dùng làm Test, chín hoa Train.
train,test = train_test_split(np.arange(len(records)),test_size=6,
                              # Seed cố định phép chia; stratify=y giúp phân bố cả ba loài vào hai tập.
                              random_state=42,stratify=y)
# Imputer dùng trung vị mỗi cột được học CHỈ ở Train để điền NaN.
pipeline = make_pipeline(SimpleImputer(strategy="median"),
                         # Sau impute, chuẩn hóa theo Train rồi phân loại; max_iter=1000 giới hạn bước tối ưu.
                         StandardScaler(),LogisticRegression(max_iter=1000))
# fit() học ba bước của pipeline CHỈ từ Train, không nhìn trước Test.
pipeline.fit(X[train],y[train])
# predict() biến đổi Test bằng imputer/scaler đã fit và đoán nhãn.
predicted = pipeline.predict(X[test])
# named_steps chọn bước SimpleImputer theo tên tự sinh, đọc thống kê đã học.
imputer = pipeline.named_steps["simpleimputer"]
# Điều kiện bảo vệ kiểm cấu trúc số mẫu và tránh Train/Test dùng chung trước khi báo cáo.
if X.shape != (15, 2) or len(predicted) != 6:
    # raise ValueError dừng kịch bản khi dữ liệu không đúng số mẫu hoặc điều kiện kiểm thử.
    raise ValueError("Cần đủ 15 mẫu hoa và 6 dự đoán test.")
print("Hoa:", len(records))
# np.isnan(X) đánh dấu ô NaN trong dữ liệu gốc; sum() đếm số ô bị thiếu.
print("Ô thiếu ban đầu:", int(np.isnan(X).sum()))
print("Train/test:", len(train),len(test))
# statistics_ là vector trung vị TỪ TRAIN cho từng cột feature sau fit.
# nanmedian bỏ qua NaN và tính trung vị TỪNG CỘT (axis=0) của TRAIN, không lấy từ toàn bộ X.
# allclose() đối chiếu hai mảng số với dung sai floating-point, không dùng == tuyệt đối.
print("Median chỉ từ train:", bool(np.allclose(imputer.statistics_,np.nanmedian(X[train],axis=0))))
# Mask True khi dự đoán đúng từng mẫu Test, mean() là Accuracy 0..1.
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

**Tình huống thực tế:** Trung tâm đào tạo có **18 học viên C01–C18**. Mỗi dòng gồm **giờ tự học mỗi tuần**, **số hoạt động đã hoàn thành** và nhãn `completed`: **0 chưa hoàn thành**, **1 đã hoàn thành**. Có **12 người nhãn 0**, **6 người nhãn 1** và **ba ô dữ liệu đầu vào chưa có số**. Trung tâm giữ **12 hồ sơ train, 6 hồ sơ test**, rồi so mô hình Logistic Regression đã điền thiếu/chuẩn hóa với cách đoán lớp đông nhất. Điều quan trọng không chỉ là dự đoán đúng bao nhiêu người, mà còn là **trong hai người đã hoàn thành ở test, mô hình tìm được mấy người**.

**Vì sao chọn cách này?** Khi **lớp 0 nhiều gấp đôi lớp 1**, cách luôn đoán 'chưa hoàn thành' có thể đạt accuracy khoảng **hai phần ba** nhưng vẫn **bỏ sót mọi người thực sự hoàn thành**. Vì thế bài giữ riêng **6 người test** với **4 nhãn 0 và 2 nhãn 1**, kiểm cả **accuracy** (tỷ lệ dự đoán đúng) lẫn **recall lớp 1** (trong hai người thật sự hoàn thành, mô hình nhận ra bao nhiêu). `DummyClassifier` cung cấp baseline; pipeline `SimpleImputer → StandardScaler → LogisticRegression` học từ **12 người train** và xử lý **ba ô thiếu** mà không học thông số từ test. **Confusion matrix (ma trận nhầm lẫn)** đặt **nhãn thật theo hàng, dự đoán theo cột**, để đọc được số người đúng/sai của từng lớp, không chỉ một số accuracy tổng. Việc kết quả mẫu này tốt chưa nói lên mô hình có hiệu quả với học viên ngoài dữ liệu giả lập.

**Quy trình:**
1. Tạo 18 dòng với nhãn lệch và ba ô thiếu hợp lệ.
2. Chia test 6 theo nhãn; fit imputer/scaler/classifier chỉ trên 12 train, cùng tập test cho baseline.
3. Báo baseline accuracy, accuracy model, recall lớp 1 và ma trận nhầm lẫn test.

```python
# Mục đích: So baseline với mô hình thực tế bằng Accuracy, Recall lớp 1 và bảng nhầm lẫn.
# Dữ liệu: 18 học viên completed 0/1, 2 feature hours/activities có ô thiếu, Train=12/Test=6.
# NumPy hỗ trợ ndarray, NaN và chỉ số các hàng train/test.
import numpy as np
# DummyClassifier là baseline đoán lớp phổ biến, không học quan hệ feature.
from sklearn.dummy import DummyClassifier
# SimpleImputer thay dữ liệu thiếu theo thống kê chỉ học từ Train.
from sklearn.impute import SimpleImputer
# LogisticRegression phân loại nhãn rời rạc, không dự báo giá trị liên tục.
from sklearn.linear_model import LogisticRegression
# confusion_matrix tạo bảng nhầm lẫn; recall_score đánh giá khả năng nhận lớp 1.
from sklearn.metrics import confusion_matrix,recall_score
# train_test_split chia đồng bộ hàng Train và Test trước khi fit.
from sklearn.model_selection import train_test_split
# make_pipeline ghép các bước để transform Test bằng thống kê Train đã học.
from sklearn.pipeline import make_pipeline
# StandardScaler học mean/SD từng cột từ Train rồi chuẩn hóa.
from sklearn.preprocessing import StandardScaler
# 18 dict, mỗi dict có giờ/hoạt động và nhãn completed; None nghĩa chưa ghi feature.
records = [{"id":"C01","hours":1,"activities":2,"completed":0},{"id":"C02","hours":2,"activities":3,"completed":0},{"id":"C03","hours":None,"activities":4,"completed":0},{"id":"C04","hours":4,"activities":2,"completed":0},{"id":"C05","hours":1,"activities":3,"completed":0},{"id":"C06","hours":2,"activities":4,"completed":0},{"id":"C07","hours":3,"activities":2,"completed":0},{"id":"C08","hours":4,"activities":3,"completed":0},{"id":"C09","hours":1,"activities":4,"completed":0},{"id":"C10","hours":2,"activities":2,"completed":0},{"id":"C11","hours":3,"activities":3,"completed":0},{"id":"C12","hours":4,"activities":4,"completed":0},{"id":"C13","hours":7,"activities":9,"completed":1},{"id":"C14","hours":8,"activities":10,"completed":1},{"id":"C15","hours":9,"activities":11,"completed":1},{"id":"C16","hours":7,"activities":None,"completed":1},{"id":"C17","hours":8,"activities":10,"completed":1},{"id":"C18","hours":None,"activities":11,"completed":1}]
# Danh sách hai feature cho từng học viên.
features = []
# Danh sách nhãn 0/1 theo đúng thứ tự người.
labels = []
for row in records:
    # append() thêm cặp [hours,activities], có thể có None.
    features.append([row["hours"], row["activities"]])
    # append() thêm completed của cùng bản ghi.
    labels.append(row["completed"])
# X float shape (18,2), None trở thành NaN cho imputer.
X = np.array(features, dtype=float)
# y có 18 nhãn lớp.
y = np.array(labels)
# Chia bằng index chung cho X/y, không fit trên Test.
# Test có sáu học viên, Train có 12.
train,test = train_test_split(np.arange(len(records)),test_size=6,
                              # Cố định cách chia và giữ tỷ lệ nhãn trong hai tập.
                              random_state=42,stratify=y)
# Baseline chỉ đoán lớp phổ biến từ Train, bỏ qua feature.
baseline = DummyClassifier(strategy="most_frequent").fit(X[train],y[train])
# Imputer học median ở Train để điền thiếu trước khi scaler.
model = make_pipeline(SimpleImputer(strategy="median"),
                      # Scaler chuẩn hóa rồi logistic phân loại, max_iter giới hạn vòng tối ưu.
                      StandardScaler(),LogisticRegression(max_iter=1000))
# fit mô hình từ 12 hàng Train, không sử dụng nhãn Test.
model.fit(X[train],y[train])
# predict() trả sáu dự đoán Test.
pred = model.predict(X[test])
# labels=[0,1] đặt thứ tự lớp cố định; HÀNG là thật, CỘT là đoán, có cả TP/FP/FN/TN.
cm = confusion_matrix(y[test],pred,labels=[0,1])
# Điều kiện bảo vệ kiểm cấu trúc số mẫu và tránh Train/Test dùng chung trước khi báo cáo.
if len(records) != 18 or len(train) != 12 or len(test) != 6:
    # raise ValueError dừng kịch bản khi dữ liệu không đúng số mẫu hoặc điều kiện kiểm thử.
    raise ValueError("Cần đủ 18 hồ sơ chia 12 train và 6 test.")
print("Hồ sơ:", len(records))
# Mask NaN đếm số ô feature thiếu trên ma trận gốc.
print("Ô thiếu:", int(np.isnan(X).sum()))
# Dùng chỉ số Test và mask Boolean để đếm nhãn thật hai lớp.
print("Nhãn test 0/1:", int((y[test]==0).sum()),int((y[test]==1).sum()))
# Baseline Accuracy trên tập Test để có mốc so sánh.
print(f"Accuracy baseline: {baseline.score(X[test],y[test]):.2f}")
# Mask so từng nhãn đoán/thật, mean() cho Accuracy của mô hình.
print(f"Accuracy model: {(pred==y[test]).mean():.2f}")
# Recall mặc định lớp dương 1 = TP/(TP+FN), đo tỷ lệ người thật hoàn thành được phát hiện.
print(f"Recall lớp 1: {recall_score(y[test],pred):.2f}")
# tolist() đổi confusion matrix ndarray sang list hai hàng để in.
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

**Tình huống thực tế:** Trung tâm muốn hoàn thiện một báo cáo AI từ **20 dòng hồ sơ**, mỗi dòng có mã học viên, **giờ học (`hours`, giờ/tuần)**, **lượt truy cập (`visits`, lượt)**, **dự án hoàn thành (`projects`, dự án)** và nhãn `passed` **0/1**. Dòng cuối dùng lại **mã H15**, nên thực tế chỉ có **19 học viên duy nhất**; các ô `?`, trống và `N/A` làm **ba ô đầu vào không hợp lệ hoặc chưa có dữ liệu**. Nhóm cần phát hiện mã trùng, chuyển đầu vào về số, giữ **14 học viên train và 5 test**, rồi so **mức baseline**, **Logistic Regression dùng cả ba đặc trưng**, và **Logistic Regression sau khi giảm còn hai thành phần PCA** trên **cùng năm học viên test**. Cuối cùng cần xuất báo cáo **JSON** có số hồ sơ, độ đúng và ma trận nhầm lẫn, mà không dùng test để học cách xử lý dữ liệu.

**Vì sao chọn cách này?** Đây là một **quy trình AI đầu-cuối thu nhỏ** gồm **kiểm dữ liệu → chia train/test → xử lý thiếu → học mô hình → đánh giá → lưu báo cáo**. `drop_duplicates(subset='id', keep='first')` chỉ giữ **lần xuất hiện đầu của H15**, nên từ 20 dòng còn 19 mã duy nhất; cần đối chiếu hồ sơ thật trước khi tự quyết định xóa bản ghi nào trong dự án thực tế. `pd.to_numeric(errors='coerce')` đổi `?`, ô trống và `N/A` thành giá trị thiếu **NaN**, báo **ba ô** cần xử lý thay vì giả làm 0. Sau `train_test_split(..., stratify=y, random_state=42)`, cả baseline, mô hình dùng ba feature và mô hình PCA đều được huấn luyện trên **cùng 14 người train** và đánh giá trên **cùng 5 người test** để so công bằng. `SimpleImputer` và `StandardScaler` chỉ học từ train; **PCA** là cách chuyển ba đặc trưng thành **hai hướng biến thiên mới**, cũng phải fit trên train. **Accuracy** cho tỷ lệ đúng, **confusion matrix** cho biết từng lớp bị nhầm ra sao; `json.dumps` lưu các con số vào `model_report_20.json` để kiểm lại. Đây là thử nghiệm trên ít dữ liệu giả lập; không dùng kết quả test để điều chỉnh siêu tham số rồi vẫn gọi năm hồ sơ ấy là đánh giá độc lập.

**Quy trình:**
1. Tạo 20 bản ghi, báo một ID lặp; giữ bản ghi xuất hiện đầu tiên của mỗi ID.
2. Chuyển ba cột đo sang số, coi dữ liệu không đọc được là NaN; chia 19 hồ sơ còn lại thành train 14/test 5 có phân tầng.
3. Fit baseline, pipeline đầy đủ và pipeline PCA hai thành phần trên cùng train; dự đoán cùng test, xuất `model_report_20.json` chứa số dòng, missing, accuracy và confusion matrix.

```python
# Mục đích: Chạy quy trình ML toàn diện: làm sạch 20 dòng, bỏ trùng, Train/Test, baseline, full, PCA và lưu JSON.
# Dữ liệu: 20 hàng raw có ID H15 trùng thành 19 học viên; ba feature hours/visits/projects có '?', 'N/A', None; nhãn passed 0/1; Test=5.
# json xử lý chuyển đổi dictionary ↔ JSON văn bản (dumps/loads).
import json
# Path thao tác file báo cáo và đường dẫn tương đối theo hệ điều hành.
from pathlib import Path
# NumPy hỗ trợ ndarray, NaN và chỉ số các hàng train/test.
import numpy as np
# Pandas quản lý bảng, dữ liệu thiếu và thao tác làm sạch.
import pandas as pd
# PCA giảm chiều dữ liệu theo hướng có phương sai lớn, chỉ fit từ Train.
from sklearn.decomposition import PCA
# DummyClassifier là baseline đoán lớp phổ biến, không học quan hệ feature.
from sklearn.dummy import DummyClassifier
# SimpleImputer thay dữ liệu thiếu theo thống kê chỉ học từ Train.
from sklearn.impute import SimpleImputer
# LogisticRegression phân loại nhãn rời rạc, không dự báo giá trị liên tục.
from sklearn.linear_model import LogisticRegression
# accuracy_score đo tỷ lệ đúng, confusion_matrix đếm đúng/sai từng lớp.
from sklearn.metrics import accuracy_score,confusion_matrix
# train_test_split chia đồng bộ hàng Train và Test trước khi fit.
from sklearn.model_selection import train_test_split
# make_pipeline ghép các bước để transform Test bằng thống kê Train đã học.
from sklearn.pipeline import make_pipeline
# StandardScaler học mean/SD từng cột từ Train rồi chuẩn hóa.
from sklearn.preprocessing import StandardScaler
# 20 dictionary có id, giờ học, lượt truy cập, dự án và nhãn; ID H15 trùng, một số chuỗi không phải số gây thiếu.
raw = [{"id":"H01","hours":1,"visits":1,"projects":0,"passed":0},{"id":"H02","hours":2,"visits":2,"projects":1,"passed":0},{"id":"H03","hours":3,"visits":3,"projects":0,"passed":0},{"id":"H04","hours":1,"visits":1,"projects":1,"passed":0},{"id":"H05","hours":2,"visits":"?","projects":0,"passed":0},{"id":"H06","hours":3,"visits":3,"projects":1,"passed":0},{"id":"H07","hours":1,"visits":1,"projects":0,"passed":0},{"id":"H08","hours":2,"visits":2,"projects":1,"passed":0},{"id":"H09","hours":3,"visits":3,"projects":0,"passed":0},{"id":"H10","hours":1,"visits":1,"projects":1,"passed":0},{"id":"H11","hours":7,"visits":8,"projects":5,"passed":1},{"id":"H12","hours":8,"visits":9,"projects":6,"passed":1},{"id":"H13","hours":9,"visits":10,"projects":5,"passed":1},{"id":"H14","hours":7,"visits":8,"projects":6,"passed":1},{"id":"H15","hours":None,"visits":9,"projects":5,"passed":1},{"id":"H16","hours":9,"visits":10,"projects":6,"passed":1},{"id":"H17","hours":7,"visits":8,"projects":5,"passed":1},{"id":"H18","hours":8,"visits":9,"projects":"N/A","passed":1},{"id":"H19","hours":9,"visits":10,"projects":5,"passed":1},{"id":"H15","hours":7,"visits":8,"projects":6,"passed":1}]
# DataFrame tạo 20 hàng bảng thô, chưa làm sạch.
df = pd.DataFrame(raw)
# duplicated() True với lần xuất hiện ID lặp sau lần đầu; sum() đếm hàng trùng.
duplicate_count = int(df["id"].duplicated().sum())
# Bỏ ID lặp chỉ dựa cột id, giữ BẢN ĐẦU; không tự gộp số liệu bản sau.
# Đánh lại index bảng từ 0, drop=True không giữ index cũ thành cột.
df = df.drop_duplicates(subset="id",keep="first").reset_index(drop=True)
# Ba tên cột giờ, truy cập, dự án; không lấy ID hoặc passed làm feature.
feature_columns = ["hours","visits","projects"]
# to_numeric chuyển các cột sang số; errors='coerce' biến '?'/'N/A' thành NaN thay vì dừng lỗi.
# Chuyển bảng ba feature sang ndarray float shape (19,3) với NaN cho dữ liệu thiếu.
X = df[feature_columns].apply(pd.to_numeric,errors="coerce").to_numpy(dtype=float)
# Chuyển nhãn passed sang vector int 19 phần tử.
y = df["passed"].to_numpy(dtype=int)
# isnan đánh ô NaN, sum() đếm ô feature thiếu SAU đổi kiểu.
missing_count = int(np.isnan(X).sum())
# Chia các index học viên duy nhất thành Train/Test trước khi mọi phép fit.
# arange(n) sinh chỉ số 0..n−1 để dùng chung cho X/y.
# Dành 5 học viên duy nhất cho Test và 14 cho Train.
train,test = train_test_split(np.arange(len(df)),test_size=5,
                              # Cố định phép chia và giữ tỷ lệ nhãn 0/1 gần tương đương.
                              random_state=42,stratify=y)
# Baseline dự đoán nhãn lớp đông nhất Train, không học feature.
baseline = DummyClassifier(strategy="most_frequent").fit(X[train],y[train])
# Full pipeline: impute median trên Train → scale trên Train → classifier.
full = make_pipeline(SimpleImputer(strategy="median"),StandardScaler(),
                     # Bộ phân loại logistic, max_iter giới hạn số vòng tối ưu.
                     LogisticRegression(max_iter=1000))
# Full pipeline: impute median trên Train → scale trên Train → classifier.
pca = make_pipeline(SimpleImputer(strategy="median"),StandardScaler(),
                    # PCA giữ hai thành phần chính từ ba feature sau impute/scale; phải fit chỉ trên TRAIN để tránh rò rỉ.
                    # Bộ phân loại logistic, max_iter giới hạn số vòng tối ưu.
                    PCA(n_components=2),LogisticRegression(max_iter=1000))
# Fit full pipeline từ 14 hàng Train, không dùng Test.
full.fit(X[train],y[train])
# Fit cả PCA và bộ phân loại từ Train; tên biến pca ở đây là TOÀN PIPELINE.
pca.fit(X[train],y[train])
# Dự đoán nhãn của 5 mẫu Test với pipeline full.
pred = full.predict(X[test])
# Dictionary tổng hợp kích thước, chất lượng mô hình và confusion để lưu/so sánh.
report = {"raw_rows":len(raw),"unique_rows":len(df),"duplicates":duplicate_count,
          "missing_cells":missing_count,"train_rows":len(train),"test_rows":len(test),
          # Accuracy baseline: lấy nhãn thật Test so với nhãn baseline đoán, là tỷ lệ đúng.
          "accuracy_baseline":round(accuracy_score(y[test],baseline.predict(X[test])),2),
          # Accuracy full so nhãn y_test với nhãn pred của full pipeline.
          "accuracy_full":round(accuracy_score(y[test],pred),2),
          # Accuracy của pipeline PCA; không đánh giá PCA riêng lẻ mà classifier sau PCA.
          "accuracy_pca":round(accuracy_score(y[test],pca.predict(X[test])),2),
          # labels cố định thứ tự lớp, hàng thật/cột dự đoán; tolist() đổi ndarray sang JSON-compatible list.
          "confusion":confusion_matrix(y[test],pred,labels=[0,1]).tolist()}
# Tên báo cáo JSON tương đối với current working directory; file sẽ được ghi ra ổ đĩa.
path = Path("model_report_20.json")
# dumps() chuyển dict thành chuỗi JSON; ensure_ascii=False giữ dấu tiếng Việt, indent=2 thụt dòng đẹp, không ảnh hưởng giá trị.
# write_text(...,encoding='utf-8') ghi chuỗi JSON tới file, có thể ghi đè file cùng tên trong cwd.
path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
# Kiểm hai tập chỉ số không có học viên trùng nhau, tránh leakage.
# Chỉ 19 ID duy nhất sau khi bỏ một hàng H15 trùng; 20 raw là dữ liệu nguồn.
# Điều kiện bảo vệ kiểm cấu trúc số mẫu và tránh Train/Test dùng chung trước khi báo cáo.
if len(raw) != 20 or len(df) != 19 or not set(train).isdisjoint(test):
    # raise ValueError dừng kịch bản khi dữ liệu không đúng số mẫu hoặc điều kiện kiểm thử.
    raise ValueError("Cần 20 dòng đầu vào, 19 hồ sơ duy nhất và Train/Test không trùng.")
print("Dòng gốc/trùng/còn:",report["raw_rows"],report["duplicates"],report["unique_rows"])
print("Ô thiếu sau chuyển kiểu:",report["missing_cells"])
print("Train/test:",report["train_rows"],report["test_rows"])
print("Accuracy baseline/full/PCA:",report["accuracy_baseline"],report["accuracy_full"],report["accuracy_pca"])
print("Confusion (thật theo hàng):",report["confusion"])
# read_text UTF-8 mở file vừa lưu; json.loads() parse về dictionary để đối chiếu với report trong RAM.
# Kiểm tồn tại file thật, không chỉ có tên path.
# So dict JSON đọc lại với dict đã tạo để kiểm file lưu/đọc chính xác.
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
