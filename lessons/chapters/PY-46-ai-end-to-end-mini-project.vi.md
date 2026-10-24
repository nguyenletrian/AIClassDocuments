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

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Kiểm cấu trúc dữ liệu trước khi mô hình hóa

**Từ vựng trong mục:** **Feature** — đặc trưng; **Label** — nhãn; **Test set** — tập đánh giá.

**Tình huống thực tế:** Nhóm đào tạo dùng dữ liệu Iris công khai có 150 hoa, bốn số đo cm mỗi hoa và nhãn thuộc ba loài. Trước khi viết mô hình, cần xác nhận mỗi hoa có đủ cột đặc trưng và một nhãn.

**Vì sao chọn cách giải này?** Kiểm `shape` ngay từ đầu để tránh ghép sai chiều dữ liệu với vector nhãn.

**Quy trình giải:**

1. Nạp Iris và lấy X, y.
2. In shape của X và y.
3. Xác nhận 150 hàng X khớp 150 phần tử y.

```python
# Mục đích: Kiểm cấu trúc dữ liệu trước khi mô hình hóa.
from sklearn.datasets import load_iris

data = load_iris()
print(data.data.shape, data.target.shape)
```

**Kết quả khi chạy:**

```text
(150, 4) (150,)
```

Có 150 mẫu và bốn cột đặc trưng mỗi mẫu, tương ứng 150 nhãn.

### Tình huống 2 — Giữ tỷ lệ lớp khi chia train/test

**Từ vựng trong mục:** **Feature** — đặc trưng; **Label** — nhãn; **Test set** — tập đánh giá.

**Tình huống thực tế:** Iris có ba loài, mỗi loài 50 hoa. Cần chia 25% test, đảm bảo mô hình không thấy dữ liệu test trong lúc fit và tỷ lệ nhãn gần được giữ.

**Vì sao chọn cách giải này?** `train_test_split` với `stratify` giảm nguy cơ tỷ lệ lớp thay đổi ngẫu nhiên ở tập test.

**Quy trình giải:**

1. Nạp Iris và chia theo y với test_size=0.25, seed 42.
2. Giữ riêng X_train, X_test, y_train, y_test.
3. In shape hai ma trận đặc trưng.

```python
# Mục đích: Giữ tỷ lệ lớp khi chia train/test.
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

112 hoa train và 38 hoa test, vẫn giữ bốn cột cm.

### Tình huống 3 — Huấn luyện pipeline chống rò rỉ

**Từ vựng trong mục:** **Feature** — đặc trưng; **Label** — nhãn; **Test set** — tập đánh giá.

**Tình huống thực tế:** Nhóm kỹ thuật muốn học phân loại loài Iris từ bốn số đo cm, có quy tắc điền giá trị thiếu, chuẩn hóa và Logistic Regression. Tập test 25% không được dùng để fit bước tiền xử lý.

**Vì sao chọn cách giải này?** Pipeline áp cùng các biến đổi đã học từ train cho test, không chuẩn hóa cả 150 mẫu trước khi chia.

**Quy trình giải:**

1. Chia Iris thành train/test theo nhãn.
2. Tạo pipeline imputer → scaler → classifier và fit trên train.
3. Dự đoán X_test và in số nhãn được trả về.

```python
# Mục đích: Huấn luyện pipeline chống rò rỉ.
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.25,
    stratify=data.target, random_state=42,
)
model = make_pipeline(
    SimpleImputer(strategy='median'), StandardScaler(),
    LogisticRegression(max_iter=1000),
)
model.fit(X_train, y_train)
print(len(model.predict(X_test)))
```

**Kết quả khi chạy:**

```text
38
```

Pipeline đưa ra một dự đoán lớp cho mỗi mẫu test, nhưng chưa đủ để nói độ chính xác.

### Tình huống 4 — Đọc nhầm lẫn giữa các lớp

**Từ vựng trong mục:** **Feature** — đặc trưng; **Label** — nhãn; **Test set** — tập đánh giá.

**Tình huống thực tế:** Một mô hình dự đoán bốn trường hợp có nhãn thật `[0,1,1,0]` và dự đoán `[0,1,0,0]`. Cần biết lớp nào bị nhầm chứ không chỉ accuracy 3/4.

**Vì sao chọn cách giải này?** Ma trận nhầm lẫn đặt nhãn thật theo hàng, dự đoán theo cột; ô ngoài đường chéo biểu thị lỗi.

**Quy trình giải:**

1. Lưu hai danh sách nhãn cùng thứ tự quan sát.
2. Tạo `confusion_matrix` rồi đổi sang List.
3. In bảng 2×2, đọc từng ô theo hàng thật–cột dự đoán.

```python
# Mục đích: Đọc nhầm lẫn giữa các lớp.
from sklearn.metrics import confusion_matrix

actual = [0, 1, 1, 0]
predicted = [0, 1, 0, 0]
print(confusion_matrix(actual, predicted).tolist())
```

**Kết quả khi chạy:**

```text
[[2, 0], [1, 1]]
```

Một mẫu lớp 1 bị đoán nhầm thành 0; ba trong bốn mẫu dự đoán đúng.

### Tình huống 5 — So baseline và PCA đúng nguyên tắc

**Từ vựng trong mục:** **Feature** — đặc trưng; **Label** — nhãn; **Test set** — tập đánh giá.

**Tình huống thực tế:** Trên Iris, nhóm thực hành muốn so một baseline dùng bốn đặc trưng với mô hình PCA giảm còn hai thành phần. Cần xác định shape trước/sau trên **train**, tránh fit PCA lên toàn dữ liệu test.

**Vì sao chọn cách giải này?** PCA phải fit trên train trong pipeline; hai thành phần là đặc trưng được rút ra, không phải nhãn loài.

**Quy trình giải:**

1. Chia Iris trước, rồi fit scaler và PCA trên X_train.
2. Biến đổi X_test bằng đúng hai bộ biến đổi đã fit.
3. In shape của train/test sau PCA để thấy số cột giảm còn 2.

```python
# Mục đích: So baseline và PCA đúng nguyên tắc.
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.25,
    stratify=data.target, random_state=42,
)
features = make_pipeline(StandardScaler(), PCA(n_components=2))
train_2d = features.fit_transform(X_train)
test_2d = features.transform(X_test)
print(train_2d.shape, test_2d.shape)
```

**Kết quả khi chạy:**

```text
(112, 2) (38, 2)
```

PCA giảm bốn cột cm thành hai thành phần tổng hợp, giữ số hoa. Muốn so hiệu quả phải huấn luyện và đánh giá trên cùng split.

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
