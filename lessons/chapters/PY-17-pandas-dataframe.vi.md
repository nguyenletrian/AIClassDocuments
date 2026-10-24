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
df = pd.DataFrame({"Product":["Pen", "Book"], "Price":[10000, 35000], "Qty":[2, 1]})
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
import pandas as pd
import io
csv_text = "id,amount\nO1,10000\nO2,30000\n"
df = pd.read_csv(io.StringIO(csv_text))
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
df = pd.DataFrame({"Price":[10, 20], "Qty":[2, 3]})
df["Revenue"] = df.Price*df.Qty
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
df = pd.DataFrame({"name":["A", "B"], "qty":[2, 3]})
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
df = pd.DataFrame({"visits":[2, 5], "spent":[100, 200], "city":["A", "B"]})
X = df[["visits", "spent"]]
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

**Q1. What is a Pandas Series? — Pandas Series là gì?**

A. Parse tabular CSV data into a DataFrame — Đọc dữ liệu CSV thành DataFrame

B. One field across multiple records — Một thuộc tính qua nhiều bản ghi

C. A two-dimensional labeled table — Bảng dữ liệu hai chiều có nhãn

D. A one-dimensional labeled data structure — Cấu trúc dữ liệu một chiều có nhãn

**Q2. What is a Pandas DataFrame? — Pandas DataFrame là gì?**

A. A one-dimensional labeled data structure — Cấu trúc dữ liệu một chiều có nhãn

B. A two-dimensional labeled table — Bảng dữ liệu hai chiều có nhãn

C. Parse tabular CSV data into a DataFrame — Đọc dữ liệu CSV thành DataFrame

D. One field across multiple records — Một thuộc tính qua nhiều bản ghi

**Q3. What does a column represent? — Một cột trong bảng thể hiện gì?**

A. A one-dimensional labeled data structure — Cấu trúc dữ liệu một chiều có nhãn

B. One field across multiple records — Một thuộc tính qua nhiều bản ghi

C. A two-dimensional labeled table — Bảng dữ liệu hai chiều có nhãn

D. Parse tabular CSV data into a DataFrame — Đọc dữ liệu CSV thành DataFrame

**Q4. What is the purpose of `pd.read_csv()`? — `pd.read_csv()` dùng để làm gì?**

A. A one-dimensional labeled data structure — Cấu trúc dữ liệu một chiều có nhãn

B. One field across multiple records — Một thuộc tính qua nhiều bản ghi

C. A two-dimensional labeled table — Bảng dữ liệu hai chiều có nhãn

D. Parse tabular CSV data into a DataFrame — Đọc dữ liệu CSV thành DataFrame

**Q5. What does `pd.Series([1,2])` return? — `pd.Series([1,2])` trả về gì?**

A. A Series containing column x — Series chứa cột x

B. A Series with default index 0,1 — Series có index mặc định 0,1

C. A DataFrame containing one column — DataFrame có một cột

D. A tuple with row and column counts — Tuple gồm số hàng và số cột

**Q6. What does `df[['x']]` return? — `df[['x']]` trả về gì?**

A. A DataFrame containing one column — DataFrame có một cột

B. A tuple with row and column counts — Tuple gồm số hàng và số cột

C. A Series containing column x — Series chứa cột x

D. A Series with default index 0,1 — Series có index mặc định 0,1

**Q7. When DataFrame column labels are unique, what does `df['x']` return? — Khi tên cột DataFrame không trùng nhau, `df['x']` trả về gì?**

A. A tuple with row and column counts — Tuple gồm số hàng và số cột

B. A Series containing column x — Series chứa cột x

C. A DataFrame containing one column — DataFrame có một cột

D. A Series with default index 0,1 — Series có index mặc định 0,1

**Q8. What does `df.shape` return? — `df.shape` trả về gì?**

A. A Series with default index 0,1 — Series có index mặc định 0,1

B. A DataFrame containing one column — DataFrame có một cột

C. A Series containing column x — Series chứa cột x

D. A tuple with row and column counts — Tuple gồm số hàng và số cột

**Q9. What does `df.head(3)` show? — `df.head(3)` hiển thị gì?**

A. Columns, non-null counts and data types — Các cột, số ô không thiếu và kiểu dữ liệu

B. Data types of columns — Kiểu dữ liệu của các cột

C. The first three rows — Ba hàng đầu

D. Descriptive statistics such as mean and quartiles — Thống kê mô tả như trung bình và các tứ phân vị

**Q10. What does `df.dtypes` describe? — `df.dtypes` mô tả gì?**

A. Descriptive statistics such as mean and quartiles — Thống kê mô tả như trung bình và các tứ phân vị

B. The first three rows — Ba hàng đầu

C. Data types of columns — Kiểu dữ liệu của các cột

D. Columns, non-null counts and data types — Các cột, số ô không thiếu và kiểu dữ liệu

**Q11. What does `df.info()` primarily summarize? — `df.info()` chủ yếu tóm tắt gì?**

A. The first three rows — Ba hàng đầu

B. Data types of columns — Kiểu dữ liệu của các cột

C. Descriptive statistics such as mean and quartiles — Thống kê mô tả như trung bình và các tứ phân vị

D. Columns, non-null counts and data types — Các cột, số ô không thiếu và kiểu dữ liệu

**Q12. What does `df.describe()` commonly provide for numeric columns? — `df.describe()` thường cung cấp gì cho cột số?**

A. Descriptive statistics such as mean and quartiles — Thống kê mô tả như trung bình và các tứ phân vị

B. The first three rows — Ba hàng đầu

C. Columns, non-null counts and data types — Các cột, số ô không thiếu và kiểu dữ liệu

D. Data types of columns — Kiểu dữ liệu của các cột

**Q13. What is an index in a DataFrame? — Index của DataFrame là gì?**

A. Column labels — Các tên cột

B. One observation or record — Một quan sát hoặc bản ghi

C. Labels identifying rows — Các nhãn xác định hàng

D. Index labels — Nhãn index

**Q14. How are Series values aligned during arithmetic? — Pandas căn các giá trị Series khi tính toán bằng gì?**

A. Labels identifying rows — Các nhãn xác định hàng

B. One observation or record — Một quan sát hoặc bản ghi

C. Index labels — Nhãn index

D. Column labels — Các tên cột

**Q15. What does `df.columns` contain? — `df.columns` chứa gì?**

A. One observation or record — Một quan sát hoặc bản ghi

B. Index labels — Nhãn index

C. Column labels — Các tên cột

D. Labels identifying rows — Các nhãn xác định hàng

**Q16. What is a DataFrame row usually intended to represent? — Mỗi hàng DataFrame thường nên biểu diễn gì?**

A. One observation or record — Một quan sát hoặc bản ghi

B. Column labels — Các tên cột

C. Index labels — Nhãn index

D. Labels identifying rows — Các nhãn xác định hàng

**Q17. What does `df['price'] * df['qty']` calculate? — `df['price'] * df['qty']` tính gì?**

A. An element-wise product aligned by index — Tích từng phần tử được căn theo index

B. To interpret the data and calculations correctly — Để hiểu đúng dữ liệu và phép tính

C. A numeric column may be parsed as text — Cột số có thể bị đọc thành chữ

D. Two named columns — Hai cột được nêu tên

**Q18. What does `df[['a','b']]` select? — `df[['a','b']]` chọn gì?**

A. A numeric column may be parsed as text — Cột số có thể bị đọc thành chữ

B. An element-wise product aligned by index — Tích từng phần tử được căn theo index

C. To interpret the data and calculations correctly — Để hiểu đúng dữ liệu và phép tính

D. Two named columns — Hai cột được nêu tên

**Q19. What is a frequent risk when loading CSV numeric data? — Nguy cơ thường gặp khi đọc số từ CSV là gì?**

A. A numeric column may be parsed as text — Cột số có thể bị đọc thành chữ

B. Two named columns — Hai cột được nêu tên

C. An element-wise product aligned by index — Tích từng phần tử được căn theo index

D. To interpret the data and calculations correctly — Để hiểu đúng dữ liệu và phép tính

**Q20. Why define what each row and column means? — Vì sao cần nêu ý nghĩa từng hàng và cột?**

A. A numeric column may be parsed as text — Cột số có thể bị đọc thành chữ

B. To interpret the data and calculations correctly — Để hiểu đúng dữ liệu và phép tính

C. An element-wise product aligned by index — Tích từng phần tử được căn theo index

D. Two named columns — Hai cột được nêu tên

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **D** | Series associates values with an index. For instance, `pd.Series([5,6], index=['a','b'])` labels the values with `'a'` and `'b'`, unlike a plain unlabeled list. | Series liên kết từng giá trị với một nhãn index. Ví dụ `pd.Series([5,6], index=['a','b'])` gắn nhãn `'a'`, `'b'` cho các giá trị, khác với List không có hệ nhãn riêng. |
| Q2 | **B** | A DataFrame organizes records in rows and fields in columns. A table with three observations and two fields has shape `(3,2)`; a Series instead has one labeled axis. | DataFrame tổ chức bản ghi thành hàng và trường thành cột. Bảng gồm ba quan sát và hai trường có shape `(3,2)`; Series lại là cấu trúc một chiều có nhãn. |
| Q3 | **B** | A column holds the same kind of attribute for each row. If rows are orders, a `price` column records the price for each order and should carry an explicit currency unit. | Cột lưu cùng một thuộc tính ở các hàng. Nếu các hàng là đơn hàng, cột `price` ghi giá của từng đơn và cần xác định rõ đơn vị tiền tệ. |
| Q4 | **D** | read_csv interprets separated fields and header names. For example, a CSV header `name,score` becomes column labels, although malformed numeric cells may need later cleaning. | read_csv đọc các trường được phân cách cùng hàng tên cột. Ví dụ hàng tiêu đề CSV `name,score` tạo tên cột tương ứng, nhưng các ô số sai định dạng vẫn có thể cần làm sạch sau khi đọc. |
| Q5 | **B** | Default integer labels are assigned when none are given. Without an explicit index, the two values receive labels `0` and `1`; this is a Series, not a one-column DataFrame. | Không chỉ định nhãn thì Pandas tự gán chỉ số nguyên. Không truyền index, hai giá trị nhận nhãn `0` và `1`; kết quả là Series chứ không phải DataFrame một cột. |
| Q6 | **A** | Double brackets select a list of columns and preserve tabular form. If `df` has five rows, `df[['x']]` preserves a two-dimensional result with shape `(5,1)`, unlike `df['x']`. | Hai lớp ngoặc vuông chọn danh sách cột và giữ dạng bảng. Nếu `df` có năm hàng, `df[['x']]` giữ kết quả hai chiều với shape `(5,1)`, khác `df['x']`. |
| Q7 | **B** | Single-bracket column lookup returns a Series. With unique column names, `df['x']` is a one-dimensional Series; double brackets instead return a DataFrame. | Tra cứu một cột bằng ngoặc đơn trả Series. Với tên cột không trùng, `df['x']` là Series một chiều; hai lớp ngoặc vuông thì trả DataFrame. |
| Q8 | **D** | Shape gives the two dimensions of a DataFrame. For a DataFrame with four records and three fields, `df.shape` is `(4,3)`, not the count of nonmissing cells. | Shape cho biết hai kích thước của DataFrame. Với DataFrame bốn bản ghi và ba trường, `df.shape` là `(4,3)`, không phải số ô không thiếu. |
| Q9 | **C** | head returns the requested number of top rows. If the DataFrame has only two rows, `head(3)` returns those two rather than inventing another row. | head lấy số hàng đầu theo đối số. Nếu DataFrame chỉ có hai hàng, `head(3)` trả hai hàng đó chứ không tạo thêm hàng giả. |
| Q10 | **C** | Each column can have its own dtype. A `price` column can have float dtype while `name` has text dtype; `dtypes` does not calculate descriptive statistics. | Mỗi cột có thể mang dtype riêng. Cột `price` có thể có dtype thực, còn `name` mang kiểu văn bản; `dtypes` không tính thống kê mô tả. |
| Q11 | **D** | info reports the table structure and completeness. It displays column names, non-null counts, dtypes and memory usage; it is not the same as previewing records with `head()`. | info cho biết cấu trúc và mức độ đầy đủ của bảng. Nó hiển thị tên cột, số giá trị không thiếu, dtype và bộ nhớ; khác thao tác xem trước hàng dữ liệu bằng `head()`. |
| Q12 | **A** | describe computes basic summaries for numeric fields. For numeric values `[2,4,6]`, the mean is 4 and quartiles describe their spread; `head()` only displays original rows. | describe tính những thống kê cơ bản cho cột số. Với số `[2,4,6]`, trung bình bằng 4 và các tứ phân vị cho biết mức phân tán; `head()` chỉ hiển thị hàng dữ liệu gốc. |
| Q13 | **C** | The index is separate from ordinary columns unless explicitly converted. Indexes can be labels such as student IDs and are separate from normal data columns unless reset or converted. | Index tách với các cột thông thường trừ khi được chuyển đổi. Index có thể là nhãn như mã học viên và tách khỏi các cột dữ liệu thường, trừ khi được đưa trở lại thành cột. |
| Q14 | **C** | Pandas aligns data by matching index labels. If two Series list labels in different orders, Pandas matches the same labels before adding values instead of blindly pairing positions. | Pandas ghép giá trị theo các nhãn index tương ứng. Nếu hai Series sắp nhãn theo thứ tự khác nhau, Pandas ghép giá trị cùng nhãn trước khi cộng chứ không cộng máy móc theo vị trí. |
| Q15 | **C** | The columns index lists field names. For columns `name` and `age`, `list(df.columns)` gives their names; it does not list the row indices. | Thuộc tính columns liệt kê tên trường. Với các cột `name` và `age`, `list(df.columns)` trả danh sách tên cột, không phải nhãn hàng. |
| Q16 | **A** | A consistent row meaning makes aggregations interpretable. A row may be one learner, one purchase or one measurement, but it must be described consistently to interpret statistics. | Ý nghĩa hàng nhất quán giúp hiểu đúng các phép tổng hợp. Một hàng có thể là một học viên, giao dịch hoặc lần đo, nhưng cần định nghĩa nhất quán để hiểu đúng thống kê. |
| Q17 | **A** | Aligned price and quantity values are multiplied for each record. If an aligned row has price 10 dollars and quantity 3 items, its product is 30 dollars, not a cross-row total. | Giá và lượng tương ứng được nhân ở từng bản ghi. Nếu cùng một hàng có giá 10 đô la và số lượng 3 món, tích là 30 đô la, không phải tổng của nhiều hàng. |
| Q18 | **D** | A list of names selects multiple columns. The result remains a DataFrame with both `a` and `b` in the given order, whereas `df['a']` normally returns a Series. | Danh sách tên cho phép lấy nhiều cột. Kết quả vẫn là DataFrame chứa `a` và `b` theo thứ tự đã nêu, còn `df['a']` thường trả Series. |
| Q19 | **A** | Malformed values can prevent numeric type inference. A cell such as `'unknown'` inside a numeric column may force a text/object dtype, so verify and convert before arithmetic. | Giá trị không hợp lệ có thể khiến Pandas không nhận kiểu số. Ô như `'unknown'` nằm trong cột số có thể khiến kiểu bị suy ra thành văn bản/object, nên phải kiểm tra và đổi kiểu trước khi tính. |
| Q20 | **B** | Row and column semantics determine what a result means. If rows are sales and columns include price and quantity, documenting units prevents multiplying unrelated fields or misreading revenue. | Ý nghĩa hàng và cột quyết định cách diễn giải kết quả. Nếu hàng là giao dịch và cột gồm giá cùng số lượng, nêu rõ đơn vị giúp tránh nhân nhầm trường và hiểu sai doanh thu. |

## 8. Nối bài tiếp theo

`NumPy ndarray → Pandas DataFrame → Làm sạch → EDA/AI`.
