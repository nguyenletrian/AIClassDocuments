# PY-46 — Mini project: dữ liệu → làm sạch → mô hình → đánh giá


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Feature** — đặc trưng; **Label** — nhãn.

`Python → NumPy/Pandas → Train/Test → Pipeline → Report`

Bài này hệ thống hóa kiến thức đã học thành các thao tác thực hành có đầu vào và đầu ra rõ ràng.

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

## 4. Khái niệm liên quan và ví dụ nhỏ

### 4.1. Feature

**Từ vựng trong mục:** **Feature** — đặc trưng.

Cột đầu vào cho mô hình.

```python
x=[[1,2],[3,4]]
print(len(x[0]))
```

**Tự kiểm tra:** Feature nghĩa là gì? **Đáp án:** Cột đầu vào cho mô hình.

### 4.2. Label

**Từ vựng trong mục:** **Label** — nhãn.

Giá trị mục tiêu cần dự đoán.

```python
y=[0,1]
print(y)
```

**Tự kiểm tra:** Label nghĩa là gì? **Đáp án:** Giá trị mục tiêu cần dự đoán.

### 4.3. Pipeline

**Từ vựng trong mục:** **Pipeline** — chuỗi xử lý.

Gom tiền xử lý và mô hình thành các bước.

```python
from sklearn.pipeline import Pipeline
print(Pipeline)
```

**Tự kiểm tra:** Pipeline nghĩa là gì? **Đáp án:** Gom tiền xử lý và mô hình thành các bước.

### 4.4. Evaluation

**Từ vựng trong mục:** **Evaluation** — đánh giá.

Đo kết quả trên dữ liệu chưa dùng để fit.

```python
print(8/10)
```

**Tự kiểm tra:** Evaluation nghĩa là gì? **Đáp án:** Đo kết quả trên dữ liệu chưa dùng để fit.

## 5. Năm tình huống thực tế

### Tình huống 1 — Kiểm schema dữ liệu

**Từ vựng trong mục:** **Feature** — đặc trưng.

**Bài toán:** Kiểm schema dữ liệu.

**Vì sao chọn cách này?** Nêu rõ đầu vào và nhãn trước khi huấn luyện

**Dữ liệu:** Iris có 150 hoa × 4 số đo cm và một nhãn loài.

**Quy trình:** Hiểu dữ liệu → chọn lệnh/hàm → thực hiện → kiểm chứng kết quả → ghi hạn chế.

```python
from sklearn.datasets import load_iris
D=load_iris()
print(D.data.shape,D.target.shape)
```


### Tình huống 2 — Chia tập có phân tầng

**Từ vựng trong mục:** **Label** — nhãn.

**Bài toán:** Chia tập có phân tầng.

**Vì sao chọn cách này?** stratify giúp tỷ lệ nhãn ba loài ổn định

**Dữ liệu:** Iris có 3 loài.

**Quy trình:** Hiểu dữ liệu → chọn lệnh/hàm → thực hiện → kiểm chứng kết quả → ghi hạn chế.

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
D=load_iris();a,b,c,d=train_test_split(D.data,D.target,stratify=D.target,random_state=42,test_size=.25)
print(a.shape,b.shape)
```


### Tình huống 3 — Huấn luyện pipeline

**Từ vựng trong mục:** **Pipeline** — chuỗi xử lý.

**Bài toán:** Huấn luyện pipeline.

**Vì sao chọn cách này?** Gộp chuẩn hóa và phân loại để không fit toàn bộ dữ liệu test

**Dữ liệu:** Iris với 4 đặc trưng cm.

**Quy trình:** Hiểu dữ liệu → chọn lệnh/hàm → thực hiện → kiểm chứng kết quả → ghi hạn chế.

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
D=load_iris();a,b,c,d=train_test_split(D.data,D.target,stratify=D.target,random_state=42,test_size=.25)
m=make_pipeline(StandardScaler(),LogisticRegression(max_iter=1000));m.fit(a,c)
print(m.score(b,d))
```


### Tình huống 4 — Dùng confusion matrix

**Từ vựng trong mục:** **Evaluation** — đánh giá.

**Bài toán:** Dùng confusion matrix.

**Vì sao chọn cách này?** Một tỷ lệ accuracy không chỉ ra lớp nào bị nhầm

**Dữ liệu:** Các nhãn thật và dự đoán mô phỏng.

**Quy trình:** Hiểu dữ liệu → chọn lệnh/hàm → thực hiện → kiểm chứng kết quả → ghi hạn chế.

```python
from sklearn.metrics import confusion_matrix
print(confusion_matrix([0,1,1,0],[0,1,0,0]))
```


### Tình huống 5 — So baseline không PCA

**Từ vựng trong mục:** **Feature** — đặc trưng.

**Bài toán:** So baseline không PCA.

**Vì sao chọn cách này?** Phải so trên cùng tập train/test mới kết luận được

**Dữ liệu:** Iris 150 hoa, 4 đặc trưng số.

**Quy trình:** Hiểu dữ liệu → chọn lệnh/hàm → thực hiện → kiểm chứng kết quả → ghi hạn chế.

```python
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
D=load_iris();X=StandardScaler().fit_transform(D.data)
print(PCA(n_components=2).fit_transform(X).shape)
# Đây chỉ là biểu diễn, chưa phải kết quả đánh giá mô hình.
```


## 6. Nhầm lẫn cần tránh

Đừng sao chép lệnh khi chưa hiểu dữ liệu hoặc trạng thái môi trường; kết quả thử nghiệm không chứng minh rằng mọi máy và mọi bộ dữ liệu đều giống nhau.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer key** — bảng đáp án.


**Q1. What is Feature? — Thuật ngữ Feature là gì?**

A. Another term is Giá trị mục tiêu cần dự đoán — Giá trị mục tiêu cần dự đoán

B. It is Cột đầu vào cho mô hình — Cột đầu vào cho mô hình

C. Another term is Gom tiền xử lý và mô hình thành các bước — Gom tiền xử lý và mô hình thành các bước

D. Another term is Đo kết quả trên dữ liệu chưa dùng để fit — Đo kết quả trên dữ liệu chưa dùng để fit


**Q2. What is Label? — Thuật ngữ Label là gì?**

A. It is Giá trị mục tiêu cần dự đoán — Giá trị mục tiêu cần dự đoán

B. Another term is Gom tiền xử lý và mô hình thành các bước — Gom tiền xử lý và mô hình thành các bước

C. Another term is Đo kết quả trên dữ liệu chưa dùng để fit — Đo kết quả trên dữ liệu chưa dùng để fit

D. Another term is Cột đầu vào cho mô hình — Cột đầu vào cho mô hình


**Q3. What is Pipeline? — Thuật ngữ Pipeline là gì?**

A. Another term is Đo kết quả trên dữ liệu chưa dùng để fit — Đo kết quả trên dữ liệu chưa dùng để fit

B. Another term is Cột đầu vào cho mô hình — Cột đầu vào cho mô hình

C. Another term is Giá trị mục tiêu cần dự đoán — Giá trị mục tiêu cần dự đoán

D. It is Gom tiền xử lý và mô hình thành các bước — Gom tiền xử lý và mô hình thành các bước


**Q4. What is Evaluation? — Thuật ngữ Evaluation là gì?**

A. Another term is Cột đầu vào cho mô hình — Cột đầu vào cho mô hình

B. Another term is Giá trị mục tiêu cần dự đoán — Giá trị mục tiêu cần dự đoán

C. It is Đo kết quả trên dữ liệu chưa dùng để fit — Đo kết quả trên dữ liệu chưa dùng để fit

D. Another term is Gom tiền xử lý và mô hình thành các bước — Gom tiền xử lý và mô hình thành các bước


**Q5. What is pd.DataFrame()/dropna() used for? — Cú pháp pd.DataFrame()/dropna() dùng để làm gì?**

A. A different function is for Chia dữ liệu theo nhãn, tránh leakage — Chia dữ liệu theo nhãn, tránh leakage

B. It is for Tạo bảng và đánh giá xử lý giá trị thiếu — Tạo bảng và đánh giá xử lý giá trị thiếu

C. A different function is for Fit scaler/model trên train trong một chuỗi — Fit scaler/model trên train trong một chuỗi

D. A different function is for Đánh giá tập test, không suy từ điểm train — Đánh giá tập test, không suy từ điểm train


**Q6. What is train_test_split(...,stratify=y) used for? — Cú pháp train_test_split(...,stratify=y) dùng để làm gì?**

A. It is for Chia dữ liệu theo nhãn, tránh leakage — Chia dữ liệu theo nhãn, tránh leakage

B. A different function is for Fit scaler/model trên train trong một chuỗi — Fit scaler/model trên train trong một chuỗi

C. A different function is for Đánh giá tập test, không suy từ điểm train — Đánh giá tập test, không suy từ điểm train

D. A different function is for Tạo bảng và đánh giá xử lý giá trị thiếu — Tạo bảng và đánh giá xử lý giá trị thiếu


**Q7. What is make_pipeline(StandardScaler(),LogisticRegression()) used for? — Cú pháp make_pipeline(StandardScaler(),LogisticRegression()) dùng để làm gì?**

A. A different function is for Đánh giá tập test, không suy từ điểm train — Đánh giá tập test, không suy từ điểm train

B. A different function is for Tạo bảng và đánh giá xử lý giá trị thiếu — Tạo bảng và đánh giá xử lý giá trị thiếu

C. A different function is for Chia dữ liệu theo nhãn, tránh leakage — Chia dữ liệu theo nhãn, tránh leakage

D. It is for Fit scaler/model trên train trong một chuỗi — Fit scaler/model trên train trong một chuỗi


**Q8. What is model.score(X_test,y_test) used for? — Cú pháp model.score(X_test,y_test) dùng để làm gì?**

A. A different function is for Tạo bảng và đánh giá xử lý giá trị thiếu — Tạo bảng và đánh giá xử lý giá trị thiếu

B. A different function is for Chia dữ liệu theo nhãn, tránh leakage — Chia dữ liệu theo nhãn, tránh leakage

C. It is for Đánh giá tập test, không suy từ điểm train — Đánh giá tập test, không suy từ điểm train

D. A different function is for Fit scaler/model trên train trong một chuỗi — Fit scaler/model trên train trong một chuỗi


**Q9. Why choose this approach in scenario 1? — Vì sao chọn cách làm trong tình huống 1?**

A. stratify giúp tỷ lệ nhãn ba loài ổn định — stratify giúp tỷ lệ nhãn ba loài ổn định

B. Nêu rõ đầu vào và nhãn trước khi huấn luyện — Nêu rõ đầu vào và nhãn trước khi huấn luyện

C. Gộp chuẩn hóa và phân loại để không fit toàn bộ dữ liệu test — Gộp chuẩn hóa và phân loại để không fit toàn bộ dữ liệu test

D. Một tỷ lệ accuracy không chỉ ra lớp nào bị nhầm — Một tỷ lệ accuracy không chỉ ra lớp nào bị nhầm


**Q10. Why choose this approach in scenario 2? — Vì sao chọn cách làm trong tình huống 2?**

A. stratify giúp tỷ lệ nhãn ba loài ổn định — stratify giúp tỷ lệ nhãn ba loài ổn định

B. Gộp chuẩn hóa và phân loại để không fit toàn bộ dữ liệu test — Gộp chuẩn hóa và phân loại để không fit toàn bộ dữ liệu test

C. Một tỷ lệ accuracy không chỉ ra lớp nào bị nhầm — Một tỷ lệ accuracy không chỉ ra lớp nào bị nhầm

D. Phải so trên cùng tập train/test mới kết luận được — Phải so trên cùng tập train/test mới kết luận được


**Q11. Why choose this approach in scenario 3? — Vì sao chọn cách làm trong tình huống 3?**

A. Một tỷ lệ accuracy không chỉ ra lớp nào bị nhầm — Một tỷ lệ accuracy không chỉ ra lớp nào bị nhầm

B. Phải so trên cùng tập train/test mới kết luận được — Phải so trên cùng tập train/test mới kết luận được

C. Nêu rõ đầu vào và nhãn trước khi huấn luyện — Nêu rõ đầu vào và nhãn trước khi huấn luyện

D. Gộp chuẩn hóa và phân loại để không fit toàn bộ dữ liệu test — Gộp chuẩn hóa và phân loại để không fit toàn bộ dữ liệu test


**Q12. Why choose this approach in scenario 4? — Vì sao chọn cách làm trong tình huống 4?**

A. Phải so trên cùng tập train/test mới kết luận được — Phải so trên cùng tập train/test mới kết luận được

B. Nêu rõ đầu vào và nhãn trước khi huấn luyện — Nêu rõ đầu vào và nhãn trước khi huấn luyện

C. Một tỷ lệ accuracy không chỉ ra lớp nào bị nhầm — Một tỷ lệ accuracy không chỉ ra lớp nào bị nhầm

D. stratify giúp tỷ lệ nhãn ba loài ổn định — stratify giúp tỷ lệ nhãn ba loài ổn định


**Q13. Why choose this approach in scenario 5? — Vì sao chọn cách làm trong tình huống 5?**

A. Nêu rõ đầu vào và nhãn trước khi huấn luyện — Nêu rõ đầu vào và nhãn trước khi huấn luyện

B. Phải so trên cùng tập train/test mới kết luận được — Phải so trên cùng tập train/test mới kết luận được

C. stratify giúp tỷ lệ nhãn ba loài ổn định — stratify giúp tỷ lệ nhãn ba loài ổn định

D. Gộp chuẩn hóa và phân loại để không fit toàn bộ dữ liệu test — Gộp chuẩn hóa và phân loại để không fit toàn bộ dữ liệu test


**Q14. What input is used in scenario 1? — Tình huống 1 sử dụng đầu vào nào?**

A. Iris có 150 hoa × 4 số đo cm và một nhãn loài — Iris có 150 hoa × 4 số đo cm và một nhãn loài

B. Iris có 3 loài — Iris có 3 loài

C. Iris với 4 đặc trưng cm — Iris với 4 đặc trưng cm

D. Các nhãn thật và dự đoán mô phỏng — Các nhãn thật và dự đoán mô phỏng


**Q15. What input is used in scenario 2? — Tình huống 2 sử dụng đầu vào nào?**

A. Iris với 4 đặc trưng cm — Iris với 4 đặc trưng cm

B. Các nhãn thật và dự đoán mô phỏng — Các nhãn thật và dự đoán mô phỏng

C. Iris 150 hoa, 4 đặc trưng số — Iris 150 hoa, 4 đặc trưng số

D. Iris có 3 loài — Iris có 3 loài


**Q16. What input is used in scenario 3? — Tình huống 3 sử dụng đầu vào nào?**

A. Các nhãn thật và dự đoán mô phỏng — Các nhãn thật và dự đoán mô phỏng

B. Iris 150 hoa, 4 đặc trưng số — Iris 150 hoa, 4 đặc trưng số

C. Iris với 4 đặc trưng cm — Iris với 4 đặc trưng cm

D. Iris có 150 hoa × 4 số đo cm và một nhãn loài — Iris có 150 hoa × 4 số đo cm và một nhãn loài


**Q17. What input is used in scenario 4? — Tình huống 4 sử dụng đầu vào nào?**

A. Iris 150 hoa, 4 đặc trưng số — Iris 150 hoa, 4 đặc trưng số

B. Các nhãn thật và dự đoán mô phỏng — Các nhãn thật và dự đoán mô phỏng

C. Iris có 150 hoa × 4 số đo cm và một nhãn loài — Iris có 150 hoa × 4 số đo cm và một nhãn loài

D. Iris có 3 loài — Iris có 3 loài


**Q18. What input is used in scenario 5? — Tình huống 5 sử dụng đầu vào nào?**

A. Iris 150 hoa, 4 đặc trưng số — Iris 150 hoa, 4 đặc trưng số

B. Iris có 150 hoa × 4 số đo cm và một nhãn loài — Iris có 150 hoa × 4 số đo cm và một nhãn loài

C. Iris có 3 loài — Iris có 3 loài

D. Iris với 4 đặc trưng cm — Iris với 4 đặc trưng cm


**Q19. What is important before executing a workflow? — Trước khi chạy workflow cần điều gì?**

A. Only count blank lines — Chỉ đếm dòng trắng

B. Only change editor theme — Chỉ đổi giao diện

C. Ignore credentials — Bỏ qua quản lý tài khoản

D. Understand source, parameters and permissions — Hiểu nguồn, tham số và quyền hạn


**Q20. What should be reported after a test? — Sau khi test cần báo cáo gì?**

A. Only a success claim — Chỉ nói thành công

B. A guess of future results — Đoán kết quả tương lai

C. Observed output, failures and limits — Đầu ra thật, lỗi và giới hạn

D. No evidence — Không cần bằng chứng

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | It is Cột đầu vào cho mô hình | Cột đầu vào cho mô hình |
| Q2 | **A** | It is Giá trị mục tiêu cần dự đoán | Giá trị mục tiêu cần dự đoán |
| Q3 | **D** | It is Gom tiền xử lý và mô hình thành các bước | Gom tiền xử lý và mô hình thành các bước |
| Q4 | **C** | It is Đo kết quả trên dữ liệu chưa dùng để fit | Đo kết quả trên dữ liệu chưa dùng để fit |
| Q5 | **B** | It is for Tạo bảng và đánh giá xử lý giá trị thiếu | Tạo bảng và đánh giá xử lý giá trị thiếu |
| Q6 | **A** | It is for Chia dữ liệu theo nhãn, tránh leakage | Chia dữ liệu theo nhãn, tránh leakage |
| Q7 | **D** | It is for Fit scaler/model trên train trong một chuỗi | Fit scaler/model trên train trong một chuỗi |
| Q8 | **C** | It is for Đánh giá tập test, không suy từ điểm train | Đánh giá tập test, không suy từ điểm train |
| Q9 | **B** | Nêu rõ đầu vào và nhãn trước khi huấn luyện | Nêu rõ đầu vào và nhãn trước khi huấn luyện |
| Q10 | **A** | stratify giúp tỷ lệ nhãn ba loài ổn định | stratify giúp tỷ lệ nhãn ba loài ổn định |
| Q11 | **D** | Gộp chuẩn hóa và phân loại để không fit toàn bộ dữ liệu test | Gộp chuẩn hóa và phân loại để không fit toàn bộ dữ liệu test |
| Q12 | **C** | Một tỷ lệ accuracy không chỉ ra lớp nào bị nhầm | Một tỷ lệ accuracy không chỉ ra lớp nào bị nhầm |
| Q13 | **B** | Phải so trên cùng tập train/test mới kết luận được | Phải so trên cùng tập train/test mới kết luận được |
| Q14 | **A** | Iris có 150 hoa × 4 số đo cm và một nhãn loài | Iris có 150 hoa × 4 số đo cm và một nhãn loài |
| Q15 | **D** | Iris có 3 loài | Iris có 3 loài |
| Q16 | **C** | Iris với 4 đặc trưng cm | Iris với 4 đặc trưng cm |
| Q17 | **B** | Các nhãn thật và dự đoán mô phỏng | Các nhãn thật và dự đoán mô phỏng |
| Q18 | **A** | Iris 150 hoa, 4 đặc trưng số | Iris 150 hoa, 4 đặc trưng số |
| Q19 | **D** | Understand source, parameters and permissions | Hiểu nguồn, tham số và quyền hạn |
| Q20 | **C** | Observed output, failures and limits | Đầu ra thật, lỗi và giới hạn |

## 8. Nối sang bài tiếp

`Python → NumPy/Pandas → Train/Test → Pipeline → Report`.
