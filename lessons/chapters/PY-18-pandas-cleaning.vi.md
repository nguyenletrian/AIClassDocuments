# PY-18 — Pandas: missing values, duplicates và kiểu dữ liệu


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


## 4. Khái niệm liên quan

### 4.1. Missing value

**Từ vựng trong mục:** **Missing value** — giá trị thiếu.

Dữ liệu thiếu là ô không có giá trị, thường hiển thị thành `NaN` hoặc `None` và có thể kiểm tra bằng `isna()`.

```python
import pandas as pd
print(pd.Series([1,None]).isna())
```

**Kết quả khi chạy:**

```text
0    False
1     True
dtype: bool
```

### 4.2. Duplicate

**Từ vựng trong mục:** **Duplicate** — bản ghi trùng.

Dữ liệu trùng là những dòng lặp lại; `duplicated()` đánh dấu bản ghi trùng sau bản đầu.

```python
import pandas as pd
print(pd.Series([1,1]).duplicated())
```

**Kết quả khi chạy:**

```text
0    False
1     True
dtype: bool
```

### 4.3. Imputation

**Từ vựng trong mục:** **Imputation** — điền khuyết.

Điền khuyết thay số liệu thiếu bằng giá trị được chọn như trung vị; cần giải thích vì sao chọn giá trị đó.

```python
import pandas as pd
print(pd.Series([1,None]).fillna(0))
```

**Kết quả khi chạy:**

```text
0    1.0
1    0.0
dtype: float64
```

### 4.4. Data validation

**Từ vựng trong mục:** **Data validation** — kiểm tra dữ liệu.

Kiểm tra dữ liệu giúp phát hiện kiểu sai, giá trị ngoài khoảng hoặc chuỗi không đổi được thành số.

```python
import pandas as pd
print(pd.to_numeric(pd.Series(['2']),errors='coerce'))
```

**Kết quả khi chạy:**

```text
0    2
dtype: int64
```

## 5. Năm tình huống thực tế

### Tình huống 1 — Báo số khách thiếu tuổi

**Từ vựng trong mục:** **Missing value** — giá trị thiếu.

**Tình huống thực tế:** Một bảng tuổi khách có ba hàng `[20, None, 25]`, trong đó khách thứ hai chưa nhập tuổi. Đếm số tuổi bị thiếu.

**Vì sao chọn cách giải này?** `isna()` đánh dấu các ô thiếu; `sum()` đếm các ô đó theo cột.

**Quy trình giải:** Tạo bảng theo các cột và hàng đã nêu → chọn phép Pandas phù hợp → in và đọc kết quả.

```python
import pandas as pd
df=pd.DataFrame({"age":[20,None,25]})
print(df.isna().sum())
```

**Kết quả khi chạy:**

```text
age    1
dtype: int64
```

**Kết quả:** Đọc bảng hoặc giá trị in ngay bên dưới để kiểm tra những hàng và cột được giữ lại.

### Tình huống 2 — Điền giá trị trung vị

**Từ vựng trong mục:** **Duplicate** — bản ghi trùng.

**Tình huống thực tế:** Cửa hàng có mức chi tiêu `[100, None, 200]` đơn vị tiền; một dòng chưa có số liệu. Điền chỗ thiếu bằng trung vị của số liệu hiện có.

**Vì sao chọn cách giải này?** Trung vị của 100 và 200 là 150; `fillna` chỉ thay giá trị thiếu.

**Quy trình giải:** Tạo bảng theo các cột và hàng đã nêu → chọn phép Pandas phù hợp → in và đọc kết quả.

```python
import pandas as pd
df=pd.DataFrame({"spent":[100,None,200]})
df["spent"]=df["spent"].fillna(df["spent"].median())
print(df)
```

**Kết quả khi chạy:**

```text
   spent
0  100.0
1  150.0
2  200.0
```

**Kết quả:** Đọc bảng hoặc giá trị in ngay bên dưới để kiểm tra những hàng và cột được giữ lại.

### Tình huống 3 — Loại trùng mã đơn

**Từ vựng trong mục:** **Imputation** — điền khuyết.

**Tình huống thực tế:** Đơn hàng có ba dòng O1:10, O1:10 và O2:20, trong đó hai dòng O1 giống hệt nhau. Loại dòng trùng hoàn toàn và in bảng còn lại.

**Vì sao chọn cách giải này?** `drop_duplicates()` giữ một bản của những dòng giống nhau.

**Quy trình giải:** Tạo bảng theo các cột và hàng đã nêu → chọn phép Pandas phù hợp → in và đọc kết quả.

```python
import pandas as pd
df=pd.DataFrame({"id":["O1","O1","O2"],"amount":[10,10,20]})
print(df.drop_duplicates())
```

**Kết quả khi chạy:**

```text
   id  amount
0  O1      10
2  O2      20
```

**Kết quả:** Đọc bảng hoặc giá trị in ngay bên dưới để kiểm tra những hàng và cột được giữ lại.

### Tình huống 4 — Đổi chuỗi giá sang số

**Từ vựng trong mục:** **Data validation** — kiểm tra dữ liệu.

**Tình huống thực tế:** Dữ liệu giá nhận ba chuỗi `100`, `bad`, `250`. Giá trị `bad` không thể đổi thành số. Đổi các chuỗi số thành số, còn giá trị không hợp lệ thành NaN.

**Vì sao chọn cách giải này?** `to_numeric(errors='coerce')` cho phép xử lý giá trị sai kiểu mà không dừng chương trình.

**Quy trình giải:** Tạo bảng theo các cột và hàng đã nêu → chọn phép Pandas phù hợp → in và đọc kết quả.

```python
import pandas as pd
s=pd.Series(["100","bad","250"])
print(pd.to_numeric(s,errors="coerce"))
```

**Kết quả khi chạy:**

```text
0    100.0
1      NaN
2    250.0
dtype: float64
```

**Kết quả:** Đọc bảng hoặc giá trị in ngay bên dưới để kiểm tra những hàng và cột được giữ lại.

### Tình huống 5 — Chuẩn bị train/test tránh leakage

**Từ vựng trong mục:** **Missing value** — giá trị thiếu.

**Tình huống thực tế:** Dữ liệu train là `[10, None, 20]` và test là `[None,30]`. Lấy trung vị từ train rồi điền số thiếu của cả train và test.

**Vì sao chọn cách giải này?** Tính thống kê chỉ từ tập train giúp tránh rò rỉ thông tin từ test.

**Quy trình giải:** Tạo bảng theo các cột và hàng đã nêu → chọn phép Pandas phù hợp → in và đọc kết quả.

```python
import pandas as pd
train=pd.Series([10,None,20]);test=pd.Series([None,30])
median=train.median()
print(train.fillna(median),test.fillna(median))
```

**Kết quả khi chạy:**

```text
0    10.0
1    15.0
2    20.0
dtype: float64 0    15.0
1    30.0
dtype: float64
```

**Kết quả:** Đọc bảng hoặc giá trị in ngay bên dưới để kiểm tra những hàng và cột được giữ lại.

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
