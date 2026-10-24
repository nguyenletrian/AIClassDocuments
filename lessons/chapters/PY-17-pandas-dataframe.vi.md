# PY-17 — Pandas Series, DataFrame và đọc CSV


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Series** — chuỗi Pandas; **DataFrame** — bảng dữ liệu.

`NumPy ndarray → Pandas DataFrame → Làm sạch → EDA/AI`

Nắm khái niệm của bài này giúp xử lý đúng dữ liệu có nhiều đối tượng và đặc trưng trước khi dùng trong AI.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Dùng khi nào |
|---|---|---|
| Series | chuỗi Pandas | Dữ liệu một chiều có nhãn chỉ mục |
| DataFrame | bảng dữ liệu | Bảng có hàng và cột đặt tên |
| Column | cột | Một feature mang ý nghĩa xác định |
| CSV | tệp giá trị phân cách | Định dạng văn bản cho bảng có header |

## 3. Thư viện, hàm và lựa chọn

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / tham số | Giải thích ngay theo hàm |
|---|---|
| `pd.Series(values)` | Tạo dãy có chỉ mục |
| `pd.DataFrame(data)` | Tạo bảng từ dictionary/list record |
| `pd.read_csv(path)` | Đọc CSV có tiêu đề, quy định đường dẫn/encoding |
| `df.head()/df.info()/df.describe()` | Xem nhanh bản ghi, schema, thống kê |


## 4. Khái niệm liên quan

### 4.1. Series

**Từ vựng trong mục:** **Series** — chuỗi Pandas.

Series là dãy dữ liệu một chiều có chỉ số, giúp gắn giá trị với vị trí hoặc nhãn.

```python
import pandas as pd
print(pd.Series([3,4]))
```

**Kết quả khi chạy:**

```text
0    3
1    4
dtype: int64
```

### 4.2. DataFrame

**Từ vựng trong mục:** **DataFrame** — bảng dữ liệu.

DataFrame là bảng có hàng và cột; mỗi cột mang một loại thông tin rõ ràng.

```python
import pandas as pd
print(pd.DataFrame({'x':[1,2]}))
```

**Kết quả khi chạy:**

```text
   x
0  1
1  2
```

### 4.3. Column

**Từ vựng trong mục:** **Column** — cột.

Cột là một thuộc tính, chẳng hạn `Price` biểu thị giá và `Qty` biểu thị số lượng.

```python
import pandas as pd
x=pd.DataFrame({'price':[10]});print(x['price'])
```

**Kết quả khi chạy:**

```text
0    10
Name: price, dtype: int64
```

### 4.4. CSV

**Từ vựng trong mục:** **CSV** — tệp giá trị phân cách.

`read_csv` đọc bảng từ dữ liệu CSV; hàng đầu thường chứa tên cột.

```python
import pandas as pd,io
print(pd.read_csv(io.StringIO('x\n1')))
```

**Kết quả khi chạy:**

```text
   x
0  1
```

## 5. Năm tình huống thực tế

### Tình huống 1 — Tạo bảng giá sản phẩm

**Từ vựng trong mục:** **Series** — chuỗi Pandas.

**Tình huống thực tế:** Cửa hàng quản lý hai mặt hàng: Pen giá 10.000 đồng, số lượng 2; Book giá 35.000 đồng, số lượng 1. Tạo và in bảng có cột Product, Price, Qty.

**Vì sao chọn cách giải này?** DataFrame đặt tên các cột, mỗi hàng là một sản phẩm.

**Quy trình giải:** Tạo bảng theo các cột và hàng đã nêu → chọn phép Pandas phù hợp → in và đọc kết quả.

```python
import pandas as pd
df=pd.DataFrame({"Product":["Pen","Book"],"Price":[10000,35000],"Qty":[2,1]})
print(df)
```

**Kết quả khi chạy:**

```text
  Product  Price  Qty
0     Pen  10000    2
1    Book  35000    1
```

**Kết quả:** Đọc bảng hoặc giá trị in ngay bên dưới để kiểm tra những hàng và cột được giữ lại.

### Tình huống 2 — Đọc đơn từ CSV văn bản

**Từ vựng trong mục:** **DataFrame** — bảng dữ liệu.

**Tình huống thực tế:** Ứng dụng nhận CSV có hai đơn O1 trị giá 10.000 và O2 trị giá 30.000 đồng. Đọc và in bảng hai đơn hàng.

**Vì sao chọn cách giải này?** `read_csv` chuyển CSV thành DataFrame; `head()` xem những hàng đầu.

**Quy trình giải:** Tạo bảng theo các cột và hàng đã nêu → chọn phép Pandas phù hợp → in và đọc kết quả.

```python
import pandas as pd,io
csv_text="id,amount\nO1,10000\nO2,30000\n"
df=pd.read_csv(io.StringIO(csv_text))
print(df.head())
```

**Kết quả khi chạy:**

```text
   id  amount
0  O1   10000
1  O2   30000
```

**Kết quả:** Đọc bảng hoặc giá trị in ngay bên dưới để kiểm tra những hàng và cột được giữ lại.

### Tình huống 3 — Tạo doanh thu mỗi dòng

**Từ vựng trong mục:** **Column** — cột.

**Tình huống thực tế:** Hai sản phẩm có đơn giá `[10,20]` và số lượng `[2,3]` theo cùng đơn vị tiền. Thêm cột doanh thu mỗi dòng bằng giá nhân số lượng.

**Vì sao chọn cách giải này?** Pandas nhân từng hàng của hai cột Price và Qty.

**Quy trình giải:** Tạo bảng theo các cột và hàng đã nêu → chọn phép Pandas phù hợp → in và đọc kết quả.

```python
import pandas as pd
df=pd.DataFrame({"Price":[10,20],"Qty":[2,3]})
df["Revenue"]=df.Price*df.Qty
print(df)
```

**Kết quả khi chạy:**

```text
   Price  Qty  Revenue
0     10    2       20
1     20    3       60
```

**Kết quả:** Đọc bảng hoặc giá trị in ngay bên dưới để kiểm tra những hàng và cột được giữ lại.

### Tình huống 4 — Xem kiểu dữ liệu đầu vào

**Từ vựng trong mục:** **CSV** — tệp giá trị phân cách.

**Tình huống thực tế:** Bảng có tên A, B và số lượng 2, 3 sản phẩm. In kiểu dữ liệu của hai cột để kiểm tra.

**Vì sao chọn cách giải này?** `dtypes` cho biết cột chữ và cột số đang được lưu dưới kiểu nào.

**Quy trình giải:** Tạo bảng theo các cột và hàng đã nêu → chọn phép Pandas phù hợp → in và đọc kết quả.

```python
import pandas as pd
df=pd.DataFrame({"name":["A","B"],"qty":[2,3]})
print(df.dtypes)
```

**Kết quả khi chạy:**

```text
name    object
qty      int64
dtype: object
```

**Kết quả:** Đọc bảng hoặc giá trị in ngay bên dưới để kiểm tra những hàng và cột được giữ lại.

### Tình huống 5 — Chọn dữ liệu tập huấn luyện

**Từ vựng trong mục:** **Series** — chuỗi Pandas.

**Tình huống thực tế:** Bảng hai khách có `visits` là 2, 5; `spent` là 100, 200; `city` là A, B. Chọn hai cột visits và spent làm dữ liệu mô hình rồi in kích thước.

**Vì sao chọn cách giải này?** `df[[...]]` chọn hai cột, bỏ city khỏi đầu vào mẫu.

**Quy trình giải:** Tạo bảng theo các cột và hàng đã nêu → chọn phép Pandas phù hợp → in và đọc kết quả.

```python
import pandas as pd
df=pd.DataFrame({"visits":[2,5],"spent":[100,200],"city":["A","B"]})
X=df[["visits","spent"]]
print(X.shape)
```

**Kết quả khi chạy:**

```text
(2, 2)
```

**Kết quả:** Đọc bảng hoặc giá trị in ngay bên dưới để kiểm tra những hàng và cột được giữ lại.

## 6. Sai lầm thường gặp

Các tham số như axis, shape, dtype hoặc cách xử lý giá trị thiếu có thể thay đổi kết quả. Trước khi xử lý phải biết số hàng, số cột, đơn vị và mục đích của từng phép biến đổi.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.


**Q1. What does Series mean? — Ý nghĩa của Series là gì?**

A. It instead describes Bảng có hàng và cột đặt tên — Bảng có hàng và cột đặt tên

B. The concept is Dữ liệu một chiều có nhãn chỉ mục — Dữ liệu một chiều có nhãn chỉ mục

C. It instead describes Một feature mang ý nghĩa xác định — Một feature mang ý nghĩa xác định

D. It instead describes Định dạng văn bản cho bảng có header — Định dạng văn bản cho bảng có header


**Q2. What does DataFrame mean? — Ý nghĩa của DataFrame là gì?**

A. The concept is Bảng có hàng và cột đặt tên — Bảng có hàng và cột đặt tên

B. It instead describes Một feature mang ý nghĩa xác định — Một feature mang ý nghĩa xác định

C. It instead describes Định dạng văn bản cho bảng có header — Định dạng văn bản cho bảng có header

D. It instead describes Dữ liệu một chiều có nhãn chỉ mục — Dữ liệu một chiều có nhãn chỉ mục


**Q3. What does Column mean? — Ý nghĩa của Column là gì?**

A. It instead describes Định dạng văn bản cho bảng có header — Định dạng văn bản cho bảng có header

B. It instead describes Dữ liệu một chiều có nhãn chỉ mục — Dữ liệu một chiều có nhãn chỉ mục

C. It instead describes Bảng có hàng và cột đặt tên — Bảng có hàng và cột đặt tên

D. The concept is Một feature mang ý nghĩa xác định — Một feature mang ý nghĩa xác định


**Q4. What does CSV mean? — Ý nghĩa của CSV là gì?**

A. It instead describes Dữ liệu một chiều có nhãn chỉ mục — Dữ liệu một chiều có nhãn chỉ mục

B. It instead describes Bảng có hàng và cột đặt tên — Bảng có hàng và cột đặt tên

C. The concept is Định dạng văn bản cho bảng có header — Định dạng văn bản cho bảng có header

D. It instead describes Một feature mang ý nghĩa xác định — Một feature mang ý nghĩa xác định


**Q5. What is the role of pd.Series(values)? — Vai trò của pd.Series(values) là gì?**

A. Another operation would Tạo bảng từ dictionary/list record — Tạo bảng từ dictionary/list record

B. It is used to Tạo dãy có chỉ mục — Tạo dãy có chỉ mục

C. Another operation would Đọc CSV có tiêu đề, quy định đường dẫn/encoding — Đọc CSV có tiêu đề, quy định đường dẫn/encoding

D. Another operation would Xem nhanh bản ghi, schema, thống kê — Xem nhanh bản ghi, schema, thống kê


**Q6. What is the role of pd.DataFrame(data)? — Vai trò của pd.DataFrame(data) là gì?**

A. It is used to Tạo bảng từ dictionary/list record — Tạo bảng từ dictionary/list record

B. Another operation would Đọc CSV có tiêu đề, quy định đường dẫn/encoding — Đọc CSV có tiêu đề, quy định đường dẫn/encoding

C. Another operation would Xem nhanh bản ghi, schema, thống kê — Xem nhanh bản ghi, schema, thống kê

D. Another operation would Tạo dãy có chỉ mục — Tạo dãy có chỉ mục


**Q7. What is the role of pd.read_csv(path)? — Vai trò của pd.read_csv(path) là gì?**

A. Another operation would Xem nhanh bản ghi, schema, thống kê — Xem nhanh bản ghi, schema, thống kê

B. Another operation would Tạo dãy có chỉ mục — Tạo dãy có chỉ mục

C. Another operation would Tạo bảng từ dictionary/list record — Tạo bảng từ dictionary/list record

D. It is used to Đọc CSV có tiêu đề, quy định đường dẫn/encoding — Đọc CSV có tiêu đề, quy định đường dẫn/encoding


**Q8. What is the role of df.head()/df.info()/df.describe()? — Vai trò của df.head()/df.info()/df.describe() là gì?**

A. Another operation would Tạo dãy có chỉ mục — Tạo dãy có chỉ mục

B. Another operation would Tạo bảng từ dictionary/list record — Tạo bảng từ dictionary/list record

C. It is used to Xem nhanh bản ghi, schema, thống kê — Xem nhanh bản ghi, schema, thống kê

D. Another operation would Đọc CSV có tiêu đề, quy định đường dẫn/encoding — Đọc CSV có tiêu đề, quy định đường dẫn/encoding


**Q9. Which reason fits example 1? — Lý do nào phù hợp ví dụ 1?**

A. Dùng StringIO tạo CSV không phụ thuộc file máy — Dùng StringIO tạo CSV không phụ thuộc file máy

B. DataFrame tên cột giúp tránh nhầm giá với số lượng — DataFrame tên cột giúp tránh nhầm giá với số lượng

C. Một cột mới tính Price × Quantity — Một cột mới tính Price × Quantity

D. dtypes giúp phát hiện cột số bị lưu nhầm thành chuỗi — dtypes giúp phát hiện cột số bị lưu nhầm thành chuỗi


**Q10. Which reason fits example 2? — Lý do nào phù hợp ví dụ 2?**

A. Dùng StringIO tạo CSV không phụ thuộc file máy — Dùng StringIO tạo CSV không phụ thuộc file máy

B. Một cột mới tính Price × Quantity — Một cột mới tính Price × Quantity

C. dtypes giúp phát hiện cột số bị lưu nhầm thành chuỗi — dtypes giúp phát hiện cột số bị lưu nhầm thành chuỗi

D. Chỉ giữ các cột feature phù hợp để tạo X — Chỉ giữ các cột feature phù hợp để tạo X


**Q11. Which reason fits example 3? — Lý do nào phù hợp ví dụ 3?**

A. dtypes giúp phát hiện cột số bị lưu nhầm thành chuỗi — dtypes giúp phát hiện cột số bị lưu nhầm thành chuỗi

B. Chỉ giữ các cột feature phù hợp để tạo X — Chỉ giữ các cột feature phù hợp để tạo X

C. DataFrame tên cột giúp tránh nhầm giá với số lượng — DataFrame tên cột giúp tránh nhầm giá với số lượng

D. Một cột mới tính Price × Quantity — Một cột mới tính Price × Quantity


**Q12. Which reason fits example 4? — Lý do nào phù hợp ví dụ 4?**

A. Chỉ giữ các cột feature phù hợp để tạo X — Chỉ giữ các cột feature phù hợp để tạo X

B. DataFrame tên cột giúp tránh nhầm giá với số lượng — DataFrame tên cột giúp tránh nhầm giá với số lượng

C. dtypes giúp phát hiện cột số bị lưu nhầm thành chuỗi — dtypes giúp phát hiện cột số bị lưu nhầm thành chuỗi

D. Dùng StringIO tạo CSV không phụ thuộc file máy — Dùng StringIO tạo CSV không phụ thuộc file máy


**Q13. Which reason fits example 5? — Lý do nào phù hợp ví dụ 5?**

A. DataFrame tên cột giúp tránh nhầm giá với số lượng — DataFrame tên cột giúp tránh nhầm giá với số lượng

B. Chỉ giữ các cột feature phù hợp để tạo X — Chỉ giữ các cột feature phù hợp để tạo X

C. Dùng StringIO tạo CSV không phụ thuộc file máy — Dùng StringIO tạo CSV không phụ thuộc file máy

D. Một cột mới tính Price × Quantity — Một cột mới tính Price × Quantity


**Q14. Which input matches example 1? — Dữ liệu nào phù hợp ví dụ 1?**

A. The stated data are 2 sản phẩm với Price đồng, Qty cái — 2 sản phẩm với Price đồng, Qty cái

B. Other data: 2 dòng đơn, cột id,amount (đồng) — 2 dòng đơn, cột id,amount (đồng)

C. Other data: 2 sản phẩm — 2 sản phẩm

D. Other data: Một cột số lượng, một cột tên — Một cột số lượng, một cột tên


**Q15. Which input matches example 2? — Dữ liệu nào phù hợp ví dụ 2?**

A. Other data: 2 sản phẩm — 2 sản phẩm

B. Other data: Một cột số lượng, một cột tên — Một cột số lượng, một cột tên

C. Other data: 2 khách, 3 thuộc tính — 2 khách, 3 thuộc tính

D. The stated data are 2 dòng đơn, cột id,amount (đồng) — 2 dòng đơn, cột id,amount (đồng)


**Q16. Which input matches example 3? — Dữ liệu nào phù hợp ví dụ 3?**

A. Other data: Một cột số lượng, một cột tên — Một cột số lượng, một cột tên

B. Other data: 2 khách, 3 thuộc tính — 2 khách, 3 thuộc tính

C. The stated data are 2 sản phẩm — 2 sản phẩm

D. Other data: 2 sản phẩm với Price đồng, Qty cái — 2 sản phẩm với Price đồng, Qty cái


**Q17. Which input matches example 4? — Dữ liệu nào phù hợp ví dụ 4?**

A. Other data: 2 khách, 3 thuộc tính — 2 khách, 3 thuộc tính

B. The stated data are Một cột số lượng, một cột tên — Một cột số lượng, một cột tên

C. Other data: 2 sản phẩm với Price đồng, Qty cái — 2 sản phẩm với Price đồng, Qty cái

D. Other data: 2 dòng đơn, cột id,amount (đồng) — 2 dòng đơn, cột id,amount (đồng)


**Q18. Which input matches example 5? — Dữ liệu nào phù hợp ví dụ 5?**

A. The stated data are 2 khách, 3 thuộc tính — 2 khách, 3 thuộc tính

B. Other data: 2 sản phẩm với Price đồng, Qty cái — 2 sản phẩm với Price đồng, Qty cái

C. Other data: 2 dòng đơn, cột id,amount (đồng) — 2 dòng đơn, cột id,amount (đồng)

D. Other data: 2 sản phẩm — 2 sản phẩm


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
| Q1 | **B** | The concept is Dữ liệu một chiều có nhãn chỉ mục | Dữ liệu một chiều có nhãn chỉ mục |
| Q2 | **A** | The concept is Bảng có hàng và cột đặt tên | Bảng có hàng và cột đặt tên |
| Q3 | **D** | The concept is Một feature mang ý nghĩa xác định | Một feature mang ý nghĩa xác định |
| Q4 | **C** | The concept is Định dạng văn bản cho bảng có header | Định dạng văn bản cho bảng có header |
| Q5 | **B** | It is used to Tạo dãy có chỉ mục | Tạo dãy có chỉ mục |
| Q6 | **A** | It is used to Tạo bảng từ dictionary/list record | Tạo bảng từ dictionary/list record |
| Q7 | **D** | It is used to Đọc CSV có tiêu đề, quy định đường dẫn/encoding | Đọc CSV có tiêu đề, quy định đường dẫn/encoding |
| Q8 | **C** | It is used to Xem nhanh bản ghi, schema, thống kê | Xem nhanh bản ghi, schema, thống kê |
| Q9 | **B** | DataFrame tên cột giúp tránh nhầm giá với số lượng | DataFrame tên cột giúp tránh nhầm giá với số lượng |
| Q10 | **A** | Dùng StringIO tạo CSV không phụ thuộc file máy | Dùng StringIO tạo CSV không phụ thuộc file máy |
| Q11 | **D** | Một cột mới tính Price × Quantity | Một cột mới tính Price × Quantity |
| Q12 | **C** | dtypes giúp phát hiện cột số bị lưu nhầm thành chuỗi | dtypes giúp phát hiện cột số bị lưu nhầm thành chuỗi |
| Q13 | **B** | Chỉ giữ các cột feature phù hợp để tạo X | Chỉ giữ các cột feature phù hợp để tạo X |
| Q14 | **A** | The stated data are 2 sản phẩm với Price đồng, Qty cái | 2 sản phẩm với Price đồng, Qty cái |
| Q15 | **D** | The stated data are 2 dòng đơn, cột id,amount (đồng) | 2 dòng đơn, cột id,amount (đồng) |
| Q16 | **C** | The stated data are 2 sản phẩm | 2 sản phẩm |
| Q17 | **B** | The stated data are Một cột số lượng, một cột tên | Một cột số lượng, một cột tên |
| Q18 | **A** | The stated data are 2 khách, 3 thuộc tính | 2 khách, 3 thuộc tính |
| Q19 | **D** | Rows, columns and units | Hàng, cột và đơn vị |
| Q20 | **C** | To check limitations and edge cases | Để thấy giới hạn và trường hợp biên |

## 8. Nối bài tiếp theo

`NumPy ndarray → Pandas DataFrame → Làm sạch → EDA/AI`.
