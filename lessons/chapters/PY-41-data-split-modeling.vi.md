# PY-41 — Phân hoạch dữ liệu, classification và clustering


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Train set** — tập huấn luyện; **Test set** — tập kiểm tra.

`Set/NumPy → Train/Test → Preprocessing → Classification/Clustering`

Kiến thức giúp sinh viên dùng Python để hiểu dữ liệu, đánh giá độ bất định và chuẩn bị dữ liệu cho AI.

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

## 4. Khái niệm với ví dụ nhỏ

### 4.1. Train set

**Từ vựng trong mục:** **Train set** — tập huấn luyện.

Mẫu dùng để học tham số mô hình. Thử đoạn code để thấy ý nghĩa đầu ra trước khi đọc bài tập.

```python
train={1,2,3};print(train)
```

**Tự kiểm tra:** Train set là gì? **Đáp án:** Mẫu dùng để học tham số mô hình.

### 4.2. Test set

**Từ vựng trong mục:** **Test set** — tập kiểm tra.

Mẫu giữ lại chỉ để đánh giá mô hình. Thử đoạn code để thấy ý nghĩa đầu ra trước khi đọc bài tập.

```python
test={4};print(test)
```

**Tự kiểm tra:** Test set là gì? **Đáp án:** Mẫu giữ lại chỉ để đánh giá mô hình.

### 4.3. Classification

**Từ vựng trong mục:** **Classification** — phân loại.

Dự đoán nhãn rời rạc từ feature. Thử đoạn code để thấy ý nghĩa đầu ra trước khi đọc bài tập.

```python
from sklearn.datasets import load_iris
print(load_iris().target[:3])
```

**Tự kiểm tra:** Classification là gì? **Đáp án:** Dự đoán nhãn rời rạc từ feature.

### 4.4. Clustering

**Từ vựng trong mục:** **Clustering** — phân cụm.

Thử nhóm mẫu giống nhau mà không cần nhãn sẵn. Thử đoạn code để thấy ý nghĩa đầu ra trước khi đọc bài tập.

```python
from sklearn.cluster import KMeans
print(KMeans(n_clusters=2,random_state=1,n_init=10))
```

**Tự kiểm tra:** Clustering là gì? **Đáp án:** Thử nhóm mẫu giống nhau mà không cần nhãn sẵn.

## 5. Năm tình huống thực tế

### Tình huống 1 — Kiểm hai tập dữ liệu rời nhau

**Từ vựng trong mục:** **Train set** — tập huấn luyện.

**Tình huống thực tế:** Một nhóm phát triển phần mềm và AI cần kiểm hai tập dữ liệu rời nhau cho công việc của mình. Dữ liệu đầu vào: train={1,2,3}, test={4,5}. Hãy xây dựng chương trình thực hiện yêu cầu và trình bày kết quả.

**Vì sao chọn cách này?** Kiểm ID train và test không trùng; không áp dụng kết luận ngoài phạm vi giả định của dữ liệu.


**Quy trình:** làm rõ ý nghĩa đầu vào → chọn phương pháp → chạy code → kiểm tra/diễn giải kết quả.

```python
train={1,2,3};test={4,5}
print(train.isdisjoint(test))
```


### Tình huống 2 — Chia Iris có phân tầng

**Từ vựng trong mục:** **Test set** — tập kiểm tra.

**Tình huống thực tế:** Một nhóm phân tích dữ liệu cần chia iris có phân tầng cho công việc của mình. Dữ liệu đầu vào: 150 hoa, 4 cột số đo cm và 1 nhãn loài. Hãy xây dựng chương trình thực hiện yêu cầu và trình bày kết quả.

**Vì sao chọn cách này?** stratify giúp tỷ lệ các loài tương tự nhau; không áp dụng kết luận ngoài phạm vi giả định của dữ liệu.


**Quy trình:** làm rõ ý nghĩa đầu vào → chọn phương pháp → chạy code → kiểm tra/diễn giải kết quả.

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
D=load_iris();Xtr,Xte,ytr,yte=train_test_split(D.data,D.target,test_size=.25,stratify=D.target,random_state=42)
print(Xtr.shape,Xte.shape)
```


### Tình huống 3 — Phân loại trong pipeline

**Từ vựng trong mục:** **Classification** — phân loại.

**Tình huống thực tế:** Một nhóm phát triển phần mềm và AI cần phân loại trong pipeline cho công việc của mình. Dữ liệu đầu vào: Iris: số đo đài hoa/cánh hoa cm. Hãy xây dựng chương trình thực hiện yêu cầu và trình bày kết quả.

**Vì sao chọn cách này?** Scaler và mô hình chỉ fit trên train, không rò rỉ test; không áp dụng kết luận ngoài phạm vi giả định của dữ liệu.


**Quy trình:** làm rõ ý nghĩa đầu vào → chọn phương pháp → chạy code → kiểm tra/diễn giải kết quả.

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
D=load_iris();a,b,c,d=train_test_split(D.data,D.target,test_size=.25,stratify=D.target,random_state=42)
model=make_pipeline(StandardScaler(),LogisticRegression(max_iter=1000));model.fit(a,c)
print(model.score(b,d))
```


### Tình huống 4 — Gom nhóm điểm 2D

**Từ vựng trong mục:** **Clustering** — phân cụm.

**Tình huống thực tế:** Một trung tâm đào tạo cần gom nhóm điểm 2d cho công việc của mình. Dữ liệu đầu vào: 4 điểm [0,0], [0,1], [10,10], [10,11]. Hãy xây dựng chương trình thực hiện yêu cầu và trình bày kết quả.

**Vì sao chọn cách này?** KMeans chỉ thử nhóm chứ không biết nhãn thật; không áp dụng kết luận ngoài phạm vi giả định của dữ liệu.


**Quy trình:** làm rõ ý nghĩa đầu vào → chọn phương pháp → chạy code → kiểm tra/diễn giải kết quả.

```python
import numpy as np
from sklearn.cluster import KMeans
X=np.array([[0,0],[0,1],[10,10],[10,11]])
print(KMeans(n_clusters=2,random_state=42,n_init=10).fit_predict(X))
```


### Tình huống 5 — So clustering với classification

**Từ vựng trong mục:** **Train set** — tập huấn luyện.

**Tình huống thực tế:** Một nhóm phân tích dữ liệu cần so clustering với classification cho công việc của mình. Dữ liệu đầu vào: Iris data với target và đặc trưng riêng. Hãy xây dựng chương trình thực hiện yêu cầu và trình bày kết quả.

**Vì sao chọn cách này?** Không dùng accuracy của nhãn KMeans tùy ý như nhãn lớp có giám sát; không áp dụng kết luận ngoài phạm vi giả định của dữ liệu.


**Quy trình:** làm rõ ý nghĩa đầu vào → chọn phương pháp → chạy code → kiểm tra/diễn giải kết quả.

```python
from sklearn.datasets import load_iris
D=load_iris()
print(D.data.shape,D.target.shape)
print(set(D.target.tolist()))
```


## 6. Nhầm lẫn thường gặp

- Không nhầm thống kê/tỷ lệ mô phỏng với xác suất dự đoán chắc chắn.
- Kiểm tra giả định, cỡ mẫu, đơn vị, độ nhạy kết quả và data leakage trước khi ứng dụng AI thật.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.


**Q1. What is Train set? — Khái niệm Train set là gì?**

A. Another concept is Mẫu giữ lại chỉ để đánh giá mô hình — Mẫu giữ lại chỉ để đánh giá mô hình

B. It is Mẫu dùng để học tham số mô hình — Mẫu dùng để học tham số mô hình

C. Another concept is Dự đoán nhãn rời rạc từ feature — Dự đoán nhãn rời rạc từ feature

D. Another concept is Thử nhóm mẫu giống nhau mà không cần nhãn sẵn — Thử nhóm mẫu giống nhau mà không cần nhãn sẵn


**Q2. What is Test set? — Khái niệm Test set là gì?**

A. It is Mẫu giữ lại chỉ để đánh giá mô hình — Mẫu giữ lại chỉ để đánh giá mô hình

B. Another concept is Dự đoán nhãn rời rạc từ feature — Dự đoán nhãn rời rạc từ feature

C. Another concept is Thử nhóm mẫu giống nhau mà không cần nhãn sẵn — Thử nhóm mẫu giống nhau mà không cần nhãn sẵn

D. Another concept is Mẫu dùng để học tham số mô hình — Mẫu dùng để học tham số mô hình


**Q3. What is Classification? — Khái niệm Classification là gì?**

A. Another concept is Thử nhóm mẫu giống nhau mà không cần nhãn sẵn — Thử nhóm mẫu giống nhau mà không cần nhãn sẵn

B. Another concept is Mẫu dùng để học tham số mô hình — Mẫu dùng để học tham số mô hình

C. Another concept is Mẫu giữ lại chỉ để đánh giá mô hình — Mẫu giữ lại chỉ để đánh giá mô hình

D. It is Dự đoán nhãn rời rạc từ feature — Dự đoán nhãn rời rạc từ feature


**Q4. What is Clustering? — Khái niệm Clustering là gì?**

A. Another concept is Mẫu dùng để học tham số mô hình — Mẫu dùng để học tham số mô hình

B. Another concept is Mẫu giữ lại chỉ để đánh giá mô hình — Mẫu giữ lại chỉ để đánh giá mô hình

C. It is Thử nhóm mẫu giống nhau mà không cần nhãn sẵn — Thử nhóm mẫu giống nhau mà không cần nhãn sẵn

D. Another concept is Dự đoán nhãn rời rạc từ feature — Dự đoán nhãn rời rạc từ feature


**Q5. When should train_test_split(...,test_size=.25,stratify=y) be used? — Khi nào nên dùng train_test_split(...,test_size=.25,stratify=y)?**

A. Another operation is for Fit chỉ trên train để giảm leakage — Fit chỉ trên train để giảm leakage

B. When you need to Chia train/test có xét tỷ lệ nhãn — Chia train/test có xét tỷ lệ nhãn

C. Another operation is for Mô hình phân loại có giám sát — Mô hình phân loại có giám sát

D. Another operation is for Phân nhóm không giám sát, số nhóm là giả định — Phân nhóm không giám sát, số nhóm là giả định


**Q6. When should Pipeline([('scale',...),('model',...)]) be used? — Khi nào nên dùng Pipeline([('scale',...),('model',...)])?**

A. When you need to Fit chỉ trên train để giảm leakage — Fit chỉ trên train để giảm leakage

B. Another operation is for Mô hình phân loại có giám sát — Mô hình phân loại có giám sát

C. Another operation is for Phân nhóm không giám sát, số nhóm là giả định — Phân nhóm không giám sát, số nhóm là giả định

D. Another operation is for Chia train/test có xét tỷ lệ nhãn — Chia train/test có xét tỷ lệ nhãn


**Q7. When should LogisticRegression(max_iter=1000) be used? — Khi nào nên dùng LogisticRegression(max_iter=1000)?**

A. Another operation is for Phân nhóm không giám sát, số nhóm là giả định — Phân nhóm không giám sát, số nhóm là giả định

B. Another operation is for Chia train/test có xét tỷ lệ nhãn — Chia train/test có xét tỷ lệ nhãn

C. Another operation is for Fit chỉ trên train để giảm leakage — Fit chỉ trên train để giảm leakage

D. When you need to Mô hình phân loại có giám sát — Mô hình phân loại có giám sát


**Q8. When should KMeans(n_clusters=2,random_state=42,n_init=10) be used? — Khi nào nên dùng KMeans(n_clusters=2,random_state=42,n_init=10)?**

A. Another operation is for Chia train/test có xét tỷ lệ nhãn — Chia train/test có xét tỷ lệ nhãn

B. Another operation is for Fit chỉ trên train để giảm leakage — Fit chỉ trên train để giảm leakage

C. When you need to Phân nhóm không giám sát, số nhóm là giả định — Phân nhóm không giám sát, số nhóm là giả định

D. Another operation is for Mô hình phân loại có giám sát — Mô hình phân loại có giám sát


**Q9. Why is this method used in scenario 1? — Vì sao dùng phương pháp ở tình huống 1?**

A. stratify giúp tỷ lệ các loài tương tự nhau — stratify giúp tỷ lệ các loài tương tự nhau

B. Kiểm ID train và test không trùng — Kiểm ID train và test không trùng

C. Scaler và mô hình chỉ fit trên train, không rò rỉ test — Scaler và mô hình chỉ fit trên train, không rò rỉ test

D. KMeans chỉ thử nhóm chứ không biết nhãn thật — KMeans chỉ thử nhóm chứ không biết nhãn thật


**Q10. Why is this method used in scenario 2? — Vì sao dùng phương pháp ở tình huống 2?**

A. stratify giúp tỷ lệ các loài tương tự nhau — stratify giúp tỷ lệ các loài tương tự nhau

B. Scaler và mô hình chỉ fit trên train, không rò rỉ test — Scaler và mô hình chỉ fit trên train, không rò rỉ test

C. KMeans chỉ thử nhóm chứ không biết nhãn thật — KMeans chỉ thử nhóm chứ không biết nhãn thật

D. Không dùng accuracy của nhãn KMeans tùy ý như nhãn lớp có giám sát — Không dùng accuracy của nhãn KMeans tùy ý như nhãn lớp có giám sát


**Q11. Why is this method used in scenario 3? — Vì sao dùng phương pháp ở tình huống 3?**

A. KMeans chỉ thử nhóm chứ không biết nhãn thật — KMeans chỉ thử nhóm chứ không biết nhãn thật

B. Không dùng accuracy của nhãn KMeans tùy ý như nhãn lớp có giám sát — Không dùng accuracy của nhãn KMeans tùy ý như nhãn lớp có giám sát

C. Kiểm ID train và test không trùng — Kiểm ID train và test không trùng

D. Scaler và mô hình chỉ fit trên train, không rò rỉ test — Scaler và mô hình chỉ fit trên train, không rò rỉ test


**Q12. Why is this method used in scenario 4? — Vì sao dùng phương pháp ở tình huống 4?**

A. Không dùng accuracy của nhãn KMeans tùy ý như nhãn lớp có giám sát — Không dùng accuracy của nhãn KMeans tùy ý như nhãn lớp có giám sát

B. Kiểm ID train và test không trùng — Kiểm ID train và test không trùng

C. KMeans chỉ thử nhóm chứ không biết nhãn thật — KMeans chỉ thử nhóm chứ không biết nhãn thật

D. stratify giúp tỷ lệ các loài tương tự nhau — stratify giúp tỷ lệ các loài tương tự nhau


**Q13. Why is this method used in scenario 5? — Vì sao dùng phương pháp ở tình huống 5?**

A. Kiểm ID train và test không trùng — Kiểm ID train và test không trùng

B. Không dùng accuracy của nhãn KMeans tùy ý như nhãn lớp có giám sát — Không dùng accuracy của nhãn KMeans tùy ý như nhãn lớp có giám sát

C. stratify giúp tỷ lệ các loài tương tự nhau — stratify giúp tỷ lệ các loài tương tự nhau

D. Scaler và mô hình chỉ fit trên train, không rò rỉ test — Scaler và mô hình chỉ fit trên train, không rò rỉ test


**Q14. Which input describes scenario 1? — Dữ liệu nào thuộc tình huống 1?**

A. The input is train={1,2,3}, test={4,5} — train={1,2,3}, test={4,5}

B. Another input is 150 hoa, 4 cột số đo cm và 1 nhãn loài — 150 hoa, 4 cột số đo cm và 1 nhãn loài

C. Another input is Iris: số đo đài hoa/cánh hoa cm — Iris: số đo đài hoa/cánh hoa cm

D. Another input is 4 điểm [0,0], [0,1], [10,10], [10,11] — 4 điểm [0,0], [0,1], [10,10], [10,11]


**Q15. Which input describes scenario 2? — Dữ liệu nào thuộc tình huống 2?**

A. Another input is Iris: số đo đài hoa/cánh hoa cm — Iris: số đo đài hoa/cánh hoa cm

B. Another input is 4 điểm [0,0], [0,1], [10,10], [10,11] — 4 điểm [0,0], [0,1], [10,10], [10,11]

C. Another input is Iris data với target và đặc trưng riêng — Iris data với target và đặc trưng riêng

D. The input is 150 hoa, 4 cột số đo cm và 1 nhãn loài — 150 hoa, 4 cột số đo cm và 1 nhãn loài


**Q16. Which input describes scenario 3? — Dữ liệu nào thuộc tình huống 3?**

A. Another input is 4 điểm [0,0], [0,1], [10,10], [10,11] — 4 điểm [0,0], [0,1], [10,10], [10,11]

B. Another input is Iris data với target và đặc trưng riêng — Iris data với target và đặc trưng riêng

C. The input is Iris: số đo đài hoa/cánh hoa cm — Iris: số đo đài hoa/cánh hoa cm

D. Another input is train={1,2,3}, test={4,5} — train={1,2,3}, test={4,5}


**Q17. Which input describes scenario 4? — Dữ liệu nào thuộc tình huống 4?**

A. Another input is Iris data với target và đặc trưng riêng — Iris data với target và đặc trưng riêng

B. The input is 4 điểm [0,0], [0,1], [10,10], [10,11] — 4 điểm [0,0], [0,1], [10,10], [10,11]

C. Another input is train={1,2,3}, test={4,5} — train={1,2,3}, test={4,5}

D. Another input is 150 hoa, 4 cột số đo cm và 1 nhãn loài — 150 hoa, 4 cột số đo cm và 1 nhãn loài


**Q18. Which input describes scenario 5? — Dữ liệu nào thuộc tình huống 5?**

A. The input is Iris data với target và đặc trưng riêng — Iris data với target và đặc trưng riêng

B. Another input is train={1,2,3}, test={4,5} — train={1,2,3}, test={4,5}

C. Another input is 150 hoa, 4 cột số đo cm và 1 nhãn loài — 150 hoa, 4 cột số đo cm và 1 nhãn loài

D. Another input is Iris: số đo đài hoa/cánh hoa cm — Iris: số đo đài hoa/cánh hoa cm


**Q19. What should be stated before analyzing data? — Cần nêu gì trước khi phân tích dữ liệu?**

A. Only file extensions — Chỉ đuôi file

B. Only terminal colors — Chỉ màu terminal

C. Only number of lines — Chỉ số dòng code

D. Units, sample meaning and assumptions — Đơn vị, ý nghĩa mẫu và giả định


**Q20. Why is validating results important? — Vì sao cần kiểm tra kết quả?**

A. One example guarantees AI accuracy — Một ví dụ bảo đảm AI đúng

B. It replaces data collection — Nó thay việc thu thập dữ liệu

C. An example may not generalize — Ví dụ có thể không tổng quát

D. It removes test sets — Nó không cần tập kiểm tra

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | It is Mẫu dùng để học tham số mô hình | Mẫu dùng để học tham số mô hình |
| Q2 | **A** | It is Mẫu giữ lại chỉ để đánh giá mô hình | Mẫu giữ lại chỉ để đánh giá mô hình |
| Q3 | **D** | It is Dự đoán nhãn rời rạc từ feature | Dự đoán nhãn rời rạc từ feature |
| Q4 | **C** | It is Thử nhóm mẫu giống nhau mà không cần nhãn sẵn | Thử nhóm mẫu giống nhau mà không cần nhãn sẵn |
| Q5 | **B** | When you need to Chia train/test có xét tỷ lệ nhãn | Chia train/test có xét tỷ lệ nhãn |
| Q6 | **A** | When you need to Fit chỉ trên train để giảm leakage | Fit chỉ trên train để giảm leakage |
| Q7 | **D** | When you need to Mô hình phân loại có giám sát | Mô hình phân loại có giám sát |
| Q8 | **C** | When you need to Phân nhóm không giám sát, số nhóm là giả định | Phân nhóm không giám sát, số nhóm là giả định |
| Q9 | **B** | Kiểm ID train và test không trùng | Kiểm ID train và test không trùng |
| Q10 | **A** | stratify giúp tỷ lệ các loài tương tự nhau | stratify giúp tỷ lệ các loài tương tự nhau |
| Q11 | **D** | Scaler và mô hình chỉ fit trên train, không rò rỉ test | Scaler và mô hình chỉ fit trên train, không rò rỉ test |
| Q12 | **C** | KMeans chỉ thử nhóm chứ không biết nhãn thật | KMeans chỉ thử nhóm chứ không biết nhãn thật |
| Q13 | **B** | Không dùng accuracy của nhãn KMeans tùy ý như nhãn lớp có giám sát | Không dùng accuracy của nhãn KMeans tùy ý như nhãn lớp có giám sát |
| Q14 | **A** | The input is train={1,2,3}, test={4,5} | train={1,2,3}, test={4,5} |
| Q15 | **D** | The input is 150 hoa, 4 cột số đo cm và 1 nhãn loài | 150 hoa, 4 cột số đo cm và 1 nhãn loài |
| Q16 | **C** | The input is Iris: số đo đài hoa/cánh hoa cm | Iris: số đo đài hoa/cánh hoa cm |
| Q17 | **B** | The input is 4 điểm [0,0], [0,1], [10,10], [10,11] | 4 điểm [0,0], [0,1], [10,10], [10,11] |
| Q18 | **A** | The input is Iris data với target và đặc trưng riêng | Iris data với target và đặc trưng riêng |
| Q19 | **D** | Units, sample meaning and assumptions | Đơn vị, ý nghĩa mẫu và giả định |
| Q20 | **C** | An example may not generalize | Ví dụ có thể không tổng quát |

## 8. Liên hệ bài kế tiếp

`Set/NumPy → Train/Test → Preprocessing → Classification/Clustering`.
