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

**Pandas** giúp quản lý dữ liệu dạng bảng trước khi phân tích và huấn luyện AI. Ta bắt đầu từ một dãy có nhãn (**Series**), mở rộng thành bảng nhiều thuộc tính (**DataFrame**), chọn và tính trên từng cột, rồi đọc dữ liệu thật từ **CSV**. Trong mọi ví dụ, phải nêu rõ một hàng đại diện cho ai/cái gì và một cột là thuộc tính nào.

### 4.1. Series — Dữ liệu một chiều có nhãn

**Từ vựng trong mục:** **Series** — dãy có nhãn; **Index** — nhãn hàng.

**Series** là dãy một chiều của Pandas, trong đó mỗi giá trị gắn với một **index** (nhãn). Ví dụ theo dõi điểm hai học viên An, Bình: nhãn `An`, `Binh` xác định ai sở hữu giá trị 8 hay 6. Khác List thuần túy thường truy cập bằng vị trí, Series còn truy cập theo **nhãn** bằng `.loc`. Khi không tự đặt nhãn, Pandas thường tạo chỉ số 0, 1, 2...

```python
import pandas as pd

scores = pd.Series([8, 6], index=['An', 'Binh'])
print(scores.loc['Binh'])
```

**Kết quả khi chạy:**

```text
6
```

Nhãn `Binh` trỏ tới giá trị điểm 6; nhãn là chỉ số hàng, không phải nội dung một cột riêng.

### 4.2. DataFrame — Bảng hàng và cột

**Từ vựng trong mục:** **DataFrame** — bảng dữ liệu; **Row/column** — hàng/cột.

**DataFrame** là bảng hai chiều. Cửa hàng có hai sản phẩm: Pen giá 10.000 đồng và Book giá 35.000 đồng. **Mỗi hàng** là một sản phẩm, **mỗi cột** là một thuộc tính (`Product` tên hàng; `Price` giá đơn vị đồng). Chỉ số 0, 1 bên trái là **index**, không phải một cột dữ liệu mặc định. Mỗi cột tương tự một Series có chung nhãn hàng.

```python
import pandas as pd

products = pd.DataFrame({
    'Product': ['Pen', 'Book'],
    'Price': [10000, 35000],
})
print(products)
```

**Kết quả khi chạy:**

```text
  Product  Price
0     Pen  10000
1    Book  35000
```

Bảng có 2 hàng sản phẩm × 2 cột thuộc tính; số 0 và 1 là nhãn index mặc định.

### 4.3. Column và dtype — Đọc và tính trên thuộc tính

**Từ vựng trong mục:** **Column** — cột; **dtype** — kiểu dữ liệu cột.

Cột là tập các giá trị của **một thuộc tính** trên nhiều hàng. Với đơn giá `[10,20]` nghìn đồng và số lượng `[2,3]` cái, ta tạo hai cột `price` và `qty` rồi thêm `revenue = price * qty`. Pandas thực hiện phép nhân **theo hàng có cùng index**. Đơn giá nhân số lượng tạo doanh thu 20 và 60 nghìn đồng. `df['price']` chọn một cột, còn `df[['price','qty']]` chọn bảng hai cột.

```python
import pandas as pd

sales = pd.DataFrame({'price': [10, 20], 'qty': [2, 3]})
sales['revenue'] = sales['price'] * sales['qty']
print(sales['revenue'].tolist())
```

**Kết quả khi chạy:**

```text
[20, 60]
```

Hai số là doanh thu của hàng thứ nhất và thứ hai. Nhân cột có ý nghĩa khi các giá trị đã căn đúng theo cùng hàng.

### 4.4. read_csv — Đọc bảng từ văn bản CSV

**Từ vựng trong mục:** **CSV** — bảng văn bản phân cách; **read_csv** — đọc CSV.

**CSV** lưu dữ liệu theo các dòng văn bản, thường dòng đầu chứa tên cột. `pd.read_csv()` chuyển nội dung thành DataFrame, có thể từ đường dẫn file hoặc bộ đệm `StringIO`. Ví dụ hai đơn hàng O1, O2 với `amount` 100 và 200 đồng; **mỗi hàng là một đơn**, cột `id` là mã đơn, cột `amount` là số tiền. Pandas thường tự nhận dạng cột số, nhưng dữ liệu phức tạp có thể cần chỉ định kiểu hoặc làm sạch trước khi tính.

```python
import pandas as pd
from io import StringIO

csv_text = 'id,amount\nO1,100\nO2,200\n'
orders = pd.read_csv(StringIO(csv_text))
print(orders['amount'].sum())
```

**Kết quả khi chạy:**

```text
300
```

Tổng số tiền hai đơn là 300 đồng. `read_csv` đọc bảng từ văn bản chứ không cần nhập lại thủ công từng dòng.

## 5. Năm tình huống thực tế

### Tình huống 1 — Tạo bảng giá sản phẩm

**Từ vựng trong mục:** **Series** — chuỗi Pandas.

**Tình huống thực tế:** Cửa hàng quản lý hai mặt hàng: Pen giá 10.000 đồng, số lượng 2; Book giá 35.000 đồng, số lượng 1. Tạo và in bảng có cột Product, Price, Qty.

**Vì sao chọn cách giải này?** DataFrame đặt tên các cột, mỗi hàng là một sản phẩm.

**Quy trình giải:**

1. Tạo mỗi hàng là một sản phẩm với cột `Product`, `Price`, `Qty`.
2. Giữ đơn giá theo đồng và số lượng theo cái.
3. In DataFrame, kiểm tra Pen và Book nằm ở hai hàng.

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

### Tình huống 2 — Đọc đơn từ CSV văn bản

**Từ vựng trong mục:** **DataFrame** — bảng dữ liệu.

**Tình huống thực tế:** Ứng dụng nhận CSV có hai đơn O1 trị giá 10.000 và O2 trị giá 30.000 đồng. Đọc và in bảng hai đơn hàng.

**Vì sao chọn cách giải này?** `read_csv` chuyển CSV thành DataFrame; `head()` xem những hàng đầu.

**Quy trình giải:**

1. Lưu CSV có tiêu đề `id,amount` và hai đơn O1, O2.
2. Đưa văn bản vào `StringIO`, đọc bằng `pd.read_csv`.
3. In `head()` để kiểm tra cột mã đơn và số tiền.

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

### Tình huống 3 — Tạo doanh thu mỗi dòng

**Từ vựng trong mục:** **Column** — cột.

**Tình huống thực tế:** Hai sản phẩm có đơn giá `[10,20]` và số lượng `[2,3]` theo cùng đơn vị tiền. Thêm cột doanh thu mỗi dòng bằng giá nhân số lượng.

**Vì sao chọn cách giải này?** Pandas nhân từng hàng của hai cột Price và Qty.

**Quy trình giải:**

1. Tạo bảng hai hàng với cột `Price` và `Qty` cùng thứ tự sản phẩm.
2. Nhân hai cột để thêm `Revenue` theo từng hàng.
3. In bảng, kiểm tra doanh thu 20 và 60 theo đơn vị tiền đã chọn.

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

### Tình huống 4 — Xem kiểu dữ liệu đầu vào

**Từ vựng trong mục:** **CSV** — tệp giá trị phân cách.

**Tình huống thực tế:** Bảng có tên A, B và số lượng 2, 3 sản phẩm. In kiểu dữ liệu của hai cột để kiểm tra.

**Vì sao chọn cách giải này?** `dtypes` cho biết cột chữ và cột số đang được lưu dưới kiểu nào.

**Quy trình giải:**

1. Tạo cột `name` gồm chữ và `qty` gồm số nguyên.
2. Truy cập `df.dtypes` để kiểm tra kiểu của từng cột.
3. Đối chiếu `name` dạng chuỗi và `qty` dạng số nguyên.

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

### Tình huống 5 — Chọn dữ liệu tập huấn luyện

**Từ vựng trong mục:** **Series** — chuỗi Pandas.

**Tình huống thực tế:** Bảng hai khách có `visits` là 2, 5; `spent` là 100, 200; `city` là A, B. Chọn hai cột visits và spent làm dữ liệu mô hình rồi in kích thước.

**Vì sao chọn cách giải này?** `df[[...]]` chọn hai cột, bỏ city khỏi đầu vào mẫu.

**Quy trình giải:**

1. Tạo bảng hai khách gồm `visits`, `spent`, `city`.
2. Chọn đúng hai cột số `visits`, `spent` làm đầu vào.
3. In `shape` của bảng chọn để thấy hai hàng × hai đặc trưng.

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

## 6. Sai lầm thường gặp

- **Series** một chiều, **DataFrame** hai chiều. `df['x']` chọn Series; `df[['x']]` giữ dạng DataFrame một cột.
- Phải hiểu **index** là nhãn hàng, không nhất thiết là cột dữ liệu. Pandas căn dữ liệu theo index khi kết hợp các Series.
- Đơn giá, số lượng và doanh thu có **đơn vị khác nhau**; nhân `price × qty` mới có ý nghĩa là thành tiền.
- CSV vốn là văn bản; cần xem lại `dtype` vì dữ liệu bẩn có thể khiến cột số bị đọc thành chuỗi.
- Không đưa mã định danh hoặc nhãn `city` vào mô hình dự đoán chỉ vì chúng có mặt trong bảng; phải chọn đặc trưng theo mục tiêu.

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
