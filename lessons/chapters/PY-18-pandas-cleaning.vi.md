# PY-18 — Pandas: missing values, duplicates và kiểu dữ liệu

*DRAFT · Dữ liệu minh họa để luyện tập, chưa xác nhận kiểm thử Windows*

## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Missing value** — giá trị thiếu; **Duplicate** — bản ghi trùng.

`DataFrame → Data Cleaning → EDA → ML Pipeline`

Nắm khái niệm của bài này giúp xử lý đúng dữ liệu có nhiều đối tượng và đặc trưng trước khi dùng trong AI.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Dùng khi nào |
|---|---|---|
| Missing value | giá trị thiếu | Ô không chứa số liệu hợp lệ |
| Duplicate | bản ghi trùng | Hai hàng dữ liệu giống nhau |
| Imputation | điền khuyết | Thay ô trống bằng giá trị phù hợp |
| Data validation | kiểm tra dữ liệu | Xác nhận dữ liệu đúng kiểu và giới hạn |

## 3. Thư viện, hàm và lựa chọn

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / tham số | Giải thích ngay theo hàm |
|---|---|
| `df.isna().sum()` | Đếm số ô khuyết theo cột |
| `df.fillna()/dropna()` | Điền hoặc bỏ dữ liệu thiếu; cân nhắc mất mẫu |
| `df.duplicated()/drop_duplicates()` | Phát hiện và loại bỏ hàng trùng |
| `pd.to_numeric(errors='coerce')` | Chuyển chuỗi lỗi thành NaN để xử lý có kiểm soát |

Trong code demo, chú thích dữ liệu và lý do xử lý; các flags đã được giải thích ngay tại bảng hàm này.

## 4. Khái niệm liên quan và ví dụ nhỏ

### 4.1. Missing value

**Từ vựng trong mục:** **Missing value** — giá trị thiếu.

Ô không chứa số liệu hợp lệ. Hãy xem ví dụ nhỏ trước khi đưa ý tưởng này vào một bảng dữ liệu lớn hơn.

```python
import pandas as pd
print(pd.Series([1,None]).isna())
```

**Tự kiểm tra:** Missing value có nghĩa gì? **Đáp án:** Ô không chứa số liệu hợp lệ.

### 4.2. Duplicate

**Từ vựng trong mục:** **Duplicate** — bản ghi trùng.

Hai hàng dữ liệu giống nhau. Hãy xem ví dụ nhỏ trước khi đưa ý tưởng này vào một bảng dữ liệu lớn hơn.

```python
import pandas as pd
print(pd.Series([1,1]).duplicated())
```

**Tự kiểm tra:** Duplicate có nghĩa gì? **Đáp án:** Hai hàng dữ liệu giống nhau.

### 4.3. Imputation

**Từ vựng trong mục:** **Imputation** — điền khuyết.

Thay ô trống bằng giá trị phù hợp. Hãy xem ví dụ nhỏ trước khi đưa ý tưởng này vào một bảng dữ liệu lớn hơn.

```python
import pandas as pd
print(pd.Series([1,None]).fillna(0))
```

**Tự kiểm tra:** Imputation có nghĩa gì? **Đáp án:** Thay ô trống bằng giá trị phù hợp.

### 4.4. Data validation

**Từ vựng trong mục:** **Data validation** — kiểm tra dữ liệu.

Xác nhận dữ liệu đúng kiểu và giới hạn. Hãy xem ví dụ nhỏ trước khi đưa ý tưởng này vào một bảng dữ liệu lớn hơn.

```python
import pandas as pd
print(pd.to_numeric(pd.Series(['2']),errors='coerce'))
```

**Tự kiểm tra:** Data validation có nghĩa gì? **Đáp án:** Xác nhận dữ liệu đúng kiểu và giới hạn.

## 5. Năm tình huống thực tế

### Tình huống 1 — Báo số khách thiếu tuổi

**Từ vựng trong mục:** **Missing value** — giá trị thiếu.

**Vấn đề:** Báo số khách thiếu tuổi.

**Vì sao chọn cách giải này?** isna().sum() giúp biết cột nào cần xử lý. Đây là lựa chọn đơn giản, có thể chạy thử độc lập trước khi dùng trên dữ liệu lớn.

**Dữ liệu:** 3 khách, cột age có một None; mỗi hàng của bảng là một mẫu, mỗi cột là một thuộc tính theo đơn vị trong mô tả. Các số là dữ liệu minh họa.

**Quy trình:** hiểu hàng/cột → chọn hàm → chạy phép tính → so sánh trước/sau → kiểm tra trường hợp biên.

```python
import pandas as pd
df=pd.DataFrame({"age":[20,None,25]})
print(df.isna().sum())
```

**Đọc kết quả:** Kiểm tra shape và giá trị in ra. Không suy diễn độ chính xác một mô hình AI từ dữ liệu demo.

### Tình huống 2 — Điền giá trị trung vị

**Từ vựng trong mục:** **Duplicate** — bản ghi trùng.

**Vấn đề:** Điền giá trị trung vị.

**Vì sao chọn cách giải này?** Median đỡ bị ảnh hưởng bởi một giá trị quá lớn. Đây là lựa chọn đơn giản, có thể chạy thử độc lập trước khi dùng trên dữ liệu lớn.

**Dữ liệu:** Cột chi tiêu 3 khách có 1 None; mỗi hàng của bảng là một mẫu, mỗi cột là một thuộc tính theo đơn vị trong mô tả. Các số là dữ liệu minh họa.

**Quy trình:** hiểu hàng/cột → chọn hàm → chạy phép tính → so sánh trước/sau → kiểm tra trường hợp biên.

```python
import pandas as pd
df=pd.DataFrame({"spent":[100,None,200]})
df["spent"]=df["spent"].fillna(df["spent"].median())
print(df)
```

**Đọc kết quả:** Kiểm tra shape và giá trị in ra. Không suy diễn độ chính xác một mô hình AI từ dữ liệu demo.

### Tình huống 3 — Loại trùng mã đơn

**Từ vựng trong mục:** **Imputation** — điền khuyết.

**Vấn đề:** Loại trùng mã đơn.

**Vì sao chọn cách giải này?** Loại dòng trùng sau khi xác nhận cùng bản ghi. Đây là lựa chọn đơn giản, có thể chạy thử độc lập trước khi dùng trên dữ liệu lớn.

**Dữ liệu:** 3 dòng mã O1 O1 O2; mỗi hàng của bảng là một mẫu, mỗi cột là một thuộc tính theo đơn vị trong mô tả. Các số là dữ liệu minh họa.

**Quy trình:** hiểu hàng/cột → chọn hàm → chạy phép tính → so sánh trước/sau → kiểm tra trường hợp biên.

```python
import pandas as pd
df=pd.DataFrame({"id":["O1","O1","O2"],"amount":[10,10,20]})
print(df.drop_duplicates())
```

**Đọc kết quả:** Kiểm tra shape và giá trị in ra. Không suy diễn độ chính xác một mô hình AI từ dữ liệu demo.

### Tình huống 4 — Đổi chuỗi giá sang số

**Từ vựng trong mục:** **Data validation** — kiểm tra dữ liệu.

**Vấn đề:** Đổi chuỗi giá sang số.

**Vì sao chọn cách giải này?** coerce đánh dấu đầu vào lỗi để không tính nhầm. Đây là lựa chọn đơn giản, có thể chạy thử độc lập trước khi dùng trên dữ liệu lớn.

**Dữ liệu:** Giá ['100','bad','250'] đồng; mỗi hàng của bảng là một mẫu, mỗi cột là một thuộc tính theo đơn vị trong mô tả. Các số là dữ liệu minh họa.

**Quy trình:** hiểu hàng/cột → chọn hàm → chạy phép tính → so sánh trước/sau → kiểm tra trường hợp biên.

```python
import pandas as pd
s=pd.Series(["100","bad","250"])
print(pd.to_numeric(s,errors="coerce"))
```

**Đọc kết quả:** Kiểm tra shape và giá trị in ra. Không suy diễn độ chính xác một mô hình AI từ dữ liệu demo.

### Tình huống 5 — Chuẩn bị train/test tránh leakage

**Từ vựng trong mục:** **Missing value** — giá trị thiếu.

**Vấn đề:** Chuẩn bị train/test tránh leakage.

**Vì sao chọn cách giải này?** Median phải học từ train và dùng lại cho test. Đây là lựa chọn đơn giản, có thể chạy thử độc lập trước khi dùng trên dữ liệu lớn.

**Dữ liệu:** Train [10,None,20], test [None,30]; mỗi hàng của bảng là một mẫu, mỗi cột là một thuộc tính theo đơn vị trong mô tả. Các số là dữ liệu minh họa.

**Quy trình:** hiểu hàng/cột → chọn hàm → chạy phép tính → so sánh trước/sau → kiểm tra trường hợp biên.

```python
import pandas as pd
train=pd.Series([10,None,20]);test=pd.Series([None,30])
median=train.median()
print(train.fillna(median),test.fillna(median))
```

**Đọc kết quả:** Kiểm tra shape và giá trị in ra. Không suy diễn độ chính xác một mô hình AI từ dữ liệu demo.

## 6. Sai lầm thường gặp

Các tham số như axis, shape, dtype hoặc cách xử lý giá trị thiếu có thể thay đổi kết quả. Trước khi xử lý phải biết số hàng, số cột, đơn vị và mục đích của từng phép biến đổi.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.


**Q1. What does Missing value mean? — Ý nghĩa của Missing value là gì?**

A. It instead describes Hai hàng dữ liệu giống nhau — Hai hàng dữ liệu giống nhau

B. The concept is Ô không chứa số liệu hợp lệ — Ô không chứa số liệu hợp lệ

C. It instead describes Thay ô trống bằng giá trị phù hợp — Thay ô trống bằng giá trị phù hợp

D. It instead describes Xác nhận dữ liệu đúng kiểu và giới hạn — Xác nhận dữ liệu đúng kiểu và giới hạn


**Q2. What does Duplicate mean? — Ý nghĩa của Duplicate là gì?**

A. The concept is Hai hàng dữ liệu giống nhau — Hai hàng dữ liệu giống nhau

B. It instead describes Thay ô trống bằng giá trị phù hợp — Thay ô trống bằng giá trị phù hợp

C. It instead describes Xác nhận dữ liệu đúng kiểu và giới hạn — Xác nhận dữ liệu đúng kiểu và giới hạn

D. It instead describes Ô không chứa số liệu hợp lệ — Ô không chứa số liệu hợp lệ


**Q3. What does Imputation mean? — Ý nghĩa của Imputation là gì?**

A. It instead describes Xác nhận dữ liệu đúng kiểu và giới hạn — Xác nhận dữ liệu đúng kiểu và giới hạn

B. It instead describes Ô không chứa số liệu hợp lệ — Ô không chứa số liệu hợp lệ

C. It instead describes Hai hàng dữ liệu giống nhau — Hai hàng dữ liệu giống nhau

D. The concept is Thay ô trống bằng giá trị phù hợp — Thay ô trống bằng giá trị phù hợp


**Q4. What does Data validation mean? — Ý nghĩa của Data validation là gì?**

A. It instead describes Ô không chứa số liệu hợp lệ — Ô không chứa số liệu hợp lệ

B. It instead describes Hai hàng dữ liệu giống nhau — Hai hàng dữ liệu giống nhau

C. The concept is Xác nhận dữ liệu đúng kiểu và giới hạn — Xác nhận dữ liệu đúng kiểu và giới hạn

D. It instead describes Thay ô trống bằng giá trị phù hợp — Thay ô trống bằng giá trị phù hợp


**Q5. What is the role of df.isna().sum()? — Vai trò của df.isna().sum() là gì?**

A. Another operation would Điền hoặc bỏ dữ liệu thiếu; cân nhắc mất mẫu — Điền hoặc bỏ dữ liệu thiếu; cân nhắc mất mẫu

B. It is used to Đếm số ô khuyết theo cột — Đếm số ô khuyết theo cột

C. Another operation would Phát hiện và loại bỏ hàng trùng — Phát hiện và loại bỏ hàng trùng

D. Another operation would Chuyển chuỗi lỗi thành NaN để xử lý có kiểm soát — Chuyển chuỗi lỗi thành NaN để xử lý có kiểm soát


**Q6. What is the role of df.fillna()/dropna()? — Vai trò của df.fillna()/dropna() là gì?**

A. It is used to Điền hoặc bỏ dữ liệu thiếu; cân nhắc mất mẫu — Điền hoặc bỏ dữ liệu thiếu; cân nhắc mất mẫu

B. Another operation would Phát hiện và loại bỏ hàng trùng — Phát hiện và loại bỏ hàng trùng

C. Another operation would Chuyển chuỗi lỗi thành NaN để xử lý có kiểm soát — Chuyển chuỗi lỗi thành NaN để xử lý có kiểm soát

D. Another operation would Đếm số ô khuyết theo cột — Đếm số ô khuyết theo cột


**Q7. What is the role of df.duplicated()/drop_duplicates()? — Vai trò của df.duplicated()/drop_duplicates() là gì?**

A. Another operation would Chuyển chuỗi lỗi thành NaN để xử lý có kiểm soát — Chuyển chuỗi lỗi thành NaN để xử lý có kiểm soát

B. Another operation would Đếm số ô khuyết theo cột — Đếm số ô khuyết theo cột

C. Another operation would Điền hoặc bỏ dữ liệu thiếu; cân nhắc mất mẫu — Điền hoặc bỏ dữ liệu thiếu; cân nhắc mất mẫu

D. It is used to Phát hiện và loại bỏ hàng trùng — Phát hiện và loại bỏ hàng trùng


**Q8. What is the role of pd.to_numeric(errors='coerce')? — Vai trò của pd.to_numeric(errors='coerce') là gì?**

A. Another operation would Đếm số ô khuyết theo cột — Đếm số ô khuyết theo cột

B. Another operation would Điền hoặc bỏ dữ liệu thiếu; cân nhắc mất mẫu — Điền hoặc bỏ dữ liệu thiếu; cân nhắc mất mẫu

C. It is used to Chuyển chuỗi lỗi thành NaN để xử lý có kiểm soát — Chuyển chuỗi lỗi thành NaN để xử lý có kiểm soát

D. Another operation would Phát hiện và loại bỏ hàng trùng — Phát hiện và loại bỏ hàng trùng


**Q9. Which reason fits example 1? — Lý do nào phù hợp ví dụ 1?**

A. Median đỡ bị ảnh hưởng bởi một giá trị quá lớn — Median đỡ bị ảnh hưởng bởi một giá trị quá lớn

B. isna().sum() giúp biết cột nào cần xử lý — isna().sum() giúp biết cột nào cần xử lý

C. Loại dòng trùng sau khi xác nhận cùng bản ghi — Loại dòng trùng sau khi xác nhận cùng bản ghi

D. coerce đánh dấu đầu vào lỗi để không tính nhầm — coerce đánh dấu đầu vào lỗi để không tính nhầm


**Q10. Which reason fits example 2? — Lý do nào phù hợp ví dụ 2?**

A. Median đỡ bị ảnh hưởng bởi một giá trị quá lớn — Median đỡ bị ảnh hưởng bởi một giá trị quá lớn

B. Loại dòng trùng sau khi xác nhận cùng bản ghi — Loại dòng trùng sau khi xác nhận cùng bản ghi

C. coerce đánh dấu đầu vào lỗi để không tính nhầm — coerce đánh dấu đầu vào lỗi để không tính nhầm

D. Median phải học từ train và dùng lại cho test — Median phải học từ train và dùng lại cho test


**Q11. Which reason fits example 3? — Lý do nào phù hợp ví dụ 3?**

A. coerce đánh dấu đầu vào lỗi để không tính nhầm — coerce đánh dấu đầu vào lỗi để không tính nhầm

B. Median phải học từ train và dùng lại cho test — Median phải học từ train và dùng lại cho test

C. isna().sum() giúp biết cột nào cần xử lý — isna().sum() giúp biết cột nào cần xử lý

D. Loại dòng trùng sau khi xác nhận cùng bản ghi — Loại dòng trùng sau khi xác nhận cùng bản ghi


**Q12. Which reason fits example 4? — Lý do nào phù hợp ví dụ 4?**

A. Median phải học từ train và dùng lại cho test — Median phải học từ train và dùng lại cho test

B. isna().sum() giúp biết cột nào cần xử lý — isna().sum() giúp biết cột nào cần xử lý

C. coerce đánh dấu đầu vào lỗi để không tính nhầm — coerce đánh dấu đầu vào lỗi để không tính nhầm

D. Median đỡ bị ảnh hưởng bởi một giá trị quá lớn — Median đỡ bị ảnh hưởng bởi một giá trị quá lớn


**Q13. Which reason fits example 5? — Lý do nào phù hợp ví dụ 5?**

A. isna().sum() giúp biết cột nào cần xử lý — isna().sum() giúp biết cột nào cần xử lý

B. Median phải học từ train và dùng lại cho test — Median phải học từ train và dùng lại cho test

C. Median đỡ bị ảnh hưởng bởi một giá trị quá lớn — Median đỡ bị ảnh hưởng bởi một giá trị quá lớn

D. Loại dòng trùng sau khi xác nhận cùng bản ghi — Loại dòng trùng sau khi xác nhận cùng bản ghi


**Q14. Which input matches example 1? — Dữ liệu nào phù hợp ví dụ 1?**

A. The stated data are 3 khách, cột age có một None — 3 khách, cột age có một None

B. Other data: Cột chi tiêu 3 khách có 1 None — Cột chi tiêu 3 khách có 1 None

C. Other data: 3 dòng mã O1 O1 O2 — 3 dòng mã O1 O1 O2

D. Other data: Giá ['100','bad','250'] đồng — Giá ['100','bad','250'] đồng


**Q15. Which input matches example 2? — Dữ liệu nào phù hợp ví dụ 2?**

A. Other data: 3 dòng mã O1 O1 O2 — 3 dòng mã O1 O1 O2

B. Other data: Giá ['100','bad','250'] đồng — Giá ['100','bad','250'] đồng

C. Other data: Train [10,None,20], test [None,30] — Train [10,None,20], test [None,30]

D. The stated data are Cột chi tiêu 3 khách có 1 None — Cột chi tiêu 3 khách có 1 None


**Q16. Which input matches example 3? — Dữ liệu nào phù hợp ví dụ 3?**

A. Other data: Giá ['100','bad','250'] đồng — Giá ['100','bad','250'] đồng

B. Other data: Train [10,None,20], test [None,30] — Train [10,None,20], test [None,30]

C. The stated data are 3 dòng mã O1 O1 O2 — 3 dòng mã O1 O1 O2

D. Other data: 3 khách, cột age có một None — 3 khách, cột age có một None


**Q17. Which input matches example 4? — Dữ liệu nào phù hợp ví dụ 4?**

A. Other data: Train [10,None,20], test [None,30] — Train [10,None,20], test [None,30]

B. The stated data are Giá ['100','bad','250'] đồng — Giá ['100','bad','250'] đồng

C. Other data: 3 khách, cột age có một None — 3 khách, cột age có một None

D. Other data: Cột chi tiêu 3 khách có 1 None — Cột chi tiêu 3 khách có 1 None


**Q18. Which input matches example 5? — Dữ liệu nào phù hợp ví dụ 5?**

A. The stated data are Train [10,None,20], test [None,30] — Train [10,None,20], test [None,30]

B. Other data: 3 khách, cột age có một None — 3 khách, cột age có một None

C. Other data: Cột chi tiêu 3 khách có 1 None — Cột chi tiêu 3 khách có 1 None

D. Other data: 3 dòng mã O1 O1 O2 — 3 dòng mã O1 O1 O2


**Q19. What must every table clarify? — Bảng dữ liệu cần nêu rõ gì?**

A. Only editor color — Chỉ màu trình soạn

B. Only variable length — Chỉ độ dài tên biến

C. Only number of blank lines — Chỉ số dòng trống

D. Rows, columns and units — Hàng, cột và đơn vị


**Q20. Why test with different inputs? — Tại sao cần thử đầu vào khác?**

A. To guarantee machine learning accuracy — Để bảo đảm AI luôn đúng

B. To remove input validation — Để bỏ kiểm tra dữ liệu

C. To check limitations and edge cases — Để thấy giới hạn và trường hợp biên

D. To change column meanings — Để thay đổi nghĩa các cột

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | The concept is Ô không chứa số liệu hợp lệ | Ô không chứa số liệu hợp lệ |
| Q2 | **A** | The concept is Hai hàng dữ liệu giống nhau | Hai hàng dữ liệu giống nhau |
| Q3 | **D** | The concept is Thay ô trống bằng giá trị phù hợp | Thay ô trống bằng giá trị phù hợp |
| Q4 | **C** | The concept is Xác nhận dữ liệu đúng kiểu và giới hạn | Xác nhận dữ liệu đúng kiểu và giới hạn |
| Q5 | **B** | It is used to Đếm số ô khuyết theo cột | Đếm số ô khuyết theo cột |
| Q6 | **A** | It is used to Điền hoặc bỏ dữ liệu thiếu; cân nhắc mất mẫu | Điền hoặc bỏ dữ liệu thiếu; cân nhắc mất mẫu |
| Q7 | **D** | It is used to Phát hiện và loại bỏ hàng trùng | Phát hiện và loại bỏ hàng trùng |
| Q8 | **C** | It is used to Chuyển chuỗi lỗi thành NaN để xử lý có kiểm soát | Chuyển chuỗi lỗi thành NaN để xử lý có kiểm soát |
| Q9 | **B** | isna().sum() giúp biết cột nào cần xử lý | isna().sum() giúp biết cột nào cần xử lý |
| Q10 | **A** | Median đỡ bị ảnh hưởng bởi một giá trị quá lớn | Median đỡ bị ảnh hưởng bởi một giá trị quá lớn |
| Q11 | **D** | Loại dòng trùng sau khi xác nhận cùng bản ghi | Loại dòng trùng sau khi xác nhận cùng bản ghi |
| Q12 | **C** | coerce đánh dấu đầu vào lỗi để không tính nhầm | coerce đánh dấu đầu vào lỗi để không tính nhầm |
| Q13 | **B** | Median phải học từ train và dùng lại cho test | Median phải học từ train và dùng lại cho test |
| Q14 | **A** | The stated data are 3 khách, cột age có một None | 3 khách, cột age có một None |
| Q15 | **D** | The stated data are Cột chi tiêu 3 khách có 1 None | Cột chi tiêu 3 khách có 1 None |
| Q16 | **C** | The stated data are 3 dòng mã O1 O1 O2 | 3 dòng mã O1 O1 O2 |
| Q17 | **B** | The stated data are Giá ['100','bad','250'] đồng | Giá ['100','bad','250'] đồng |
| Q18 | **A** | The stated data are Train [10,None,20], test [None,30] | Train [10,None,20], test [None,30] |
| Q19 | **D** | Rows, columns and units | Hàng, cột và đơn vị |
| Q20 | **C** | To check limitations and edge cases | Để thấy giới hạn và trường hợp biên |

## 8. Nối bài tiếp theo

`DataFrame → Data Cleaning → EDA → ML Pipeline`.
