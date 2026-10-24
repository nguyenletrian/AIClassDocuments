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

A. A one-dimensional labeled data structure — Cấu trúc dữ liệu một chiều có nhãn

B. A two-dimensional labeled table — Bảng dữ liệu hai chiều có nhãn

C. One field across multiple records — Một thuộc tính qua nhiều bản ghi

D. Parse tabular CSV data into a DataFrame — Đọc dữ liệu CSV thành DataFrame

**Q2. What is a Pandas DataFrame? — Pandas DataFrame là gì?**

A. A one-dimensional labeled data structure — Cấu trúc dữ liệu một chiều có nhãn

B. A two-dimensional labeled table — Bảng dữ liệu hai chiều có nhãn

C. One field across multiple records — Một thuộc tính qua nhiều bản ghi

D. Parse tabular CSV data into a DataFrame — Đọc dữ liệu CSV thành DataFrame

**Q3. What does a column represent? — Một cột trong bảng thể hiện gì?**

A. A one-dimensional labeled data structure — Cấu trúc dữ liệu một chiều có nhãn

B. A two-dimensional labeled table — Bảng dữ liệu hai chiều có nhãn

C. One field across multiple records — Một thuộc tính qua nhiều bản ghi

D. Parse tabular CSV data into a DataFrame — Đọc dữ liệu CSV thành DataFrame

**Q4. What is the purpose of `pd.read_csv()`? — `pd.read_csv()` dùng để làm gì?**

A. A one-dimensional labeled data structure — Cấu trúc dữ liệu một chiều có nhãn

B. A two-dimensional labeled table — Bảng dữ liệu hai chiều có nhãn

C. One field across multiple records — Một thuộc tính qua nhiều bản ghi

D. Parse tabular CSV data into a DataFrame — Đọc dữ liệu CSV thành DataFrame

**Q5. What does `pd.Series([1,2])` return? — `pd.Series([1,2])` trả về gì?**

A. A Series with default index 0,1 — Series có index mặc định 0,1

B. A DataFrame containing one column — DataFrame có một cột

C. A Series containing column x — Series chứa cột x

D. A tuple with row and column counts — Tuple gồm số hàng và số cột

**Q6. What does `df[['x']]` return? — `df[['x']]` trả về gì?**

A. A Series with default index 0,1 — Series có index mặc định 0,1

B. A DataFrame containing one column — DataFrame có một cột

C. A Series containing column x — Series chứa cột x

D. A tuple with row and column counts — Tuple gồm số hàng và số cột

**Q7. What does `df['x']` return in a normal DataFrame? — `df['x']` thường trả về gì?**

A. A Series with default index 0,1 — Series có index mặc định 0,1

B. A DataFrame containing one column — DataFrame có một cột

C. A Series containing column x — Series chứa cột x

D. A tuple with row and column counts — Tuple gồm số hàng và số cột

**Q8. What does `df.shape` return? — `df.shape` trả về gì?**

A. A Series with default index 0,1 — Series có index mặc định 0,1

B. A DataFrame containing one column — DataFrame có một cột

C. A Series containing column x — Series chứa cột x

D. A tuple with row and column counts — Tuple gồm số hàng và số cột

**Q9. What does `df.head(3)` show? — `df.head(3)` hiển thị gì?**

A. The first three rows — Ba hàng đầu

B. Data types of columns — Kiểu dữ liệu của các cột

C. Columns, non-null counts and data types — Các cột, số ô không thiếu và kiểu dữ liệu

D. Descriptive statistics such as mean and quartiles — Thống kê mô tả như trung bình và các tứ phân vị

**Q10. What does `df.dtypes` describe? — `df.dtypes` mô tả gì?**

A. The first three rows — Ba hàng đầu

B. Data types of columns — Kiểu dữ liệu của các cột

C. Columns, non-null counts and data types — Các cột, số ô không thiếu và kiểu dữ liệu

D. Descriptive statistics such as mean and quartiles — Thống kê mô tả như trung bình và các tứ phân vị

**Q11. What does `df.info()` primarily summarize? — `df.info()` chủ yếu tóm tắt gì?**

A. The first three rows — Ba hàng đầu

B. Data types of columns — Kiểu dữ liệu của các cột

C. Columns, non-null counts and data types — Các cột, số ô không thiếu và kiểu dữ liệu

D. Descriptive statistics such as mean and quartiles — Thống kê mô tả như trung bình và các tứ phân vị

**Q12. What does `df.describe()` commonly provide for numeric columns? — `df.describe()` thường cung cấp gì cho cột số?**

A. The first three rows — Ba hàng đầu

B. Data types of columns — Kiểu dữ liệu của các cột

C. Columns, non-null counts and data types — Các cột, số ô không thiếu và kiểu dữ liệu

D. Descriptive statistics such as mean and quartiles — Thống kê mô tả như trung bình và các tứ phân vị

**Q13. What is an index in a DataFrame? — Index của DataFrame là gì?**

A. Labels identifying rows — Các nhãn xác định hàng

B. Index labels — Nhãn index

C. Column labels — Các tên cột

D. One observation or record — Một quan sát hoặc bản ghi

**Q14. How are Series values aligned during arithmetic? — Pandas căn các giá trị Series khi tính toán bằng gì?**

A. Labels identifying rows — Các nhãn xác định hàng

B. Index labels — Nhãn index

C. Column labels — Các tên cột

D. One observation or record — Một quan sát hoặc bản ghi

**Q15. What does `df.columns` contain? — `df.columns` chứa gì?**

A. Labels identifying rows — Các nhãn xác định hàng

B. Index labels — Nhãn index

C. Column labels — Các tên cột

D. One observation or record — Một quan sát hoặc bản ghi

**Q16. What is a DataFrame row usually intended to represent? — Mỗi hàng DataFrame thường nên biểu diễn gì?**

A. Labels identifying rows — Các nhãn xác định hàng

B. Index labels — Nhãn index

C. Column labels — Các tên cột

D. One observation or record — Một quan sát hoặc bản ghi

**Q17. What does `df['price'] * df['qty']` calculate? — `df['price'] * df['qty']` tính gì?**

A. An element-wise product aligned by index — Tích từng phần tử được căn theo index

B. Two named columns — Hai cột được nêu tên

C. A numeric column may be parsed as text — Cột số có thể bị đọc thành chữ

D. To interpret the data and calculations correctly — Để hiểu đúng dữ liệu và phép tính

**Q18. What does `df[['a','b']]` select? — `df[['a','b']]` chọn gì?**

A. An element-wise product aligned by index — Tích từng phần tử được căn theo index

B. Two named columns — Hai cột được nêu tên

C. A numeric column may be parsed as text — Cột số có thể bị đọc thành chữ

D. To interpret the data and calculations correctly — Để hiểu đúng dữ liệu và phép tính

**Q19. What is a frequent risk when loading CSV numeric data? — Nguy cơ thường gặp khi đọc số từ CSV là gì?**

A. An element-wise product aligned by index — Tích từng phần tử được căn theo index

B. Two named columns — Hai cột được nêu tên

C. A numeric column may be parsed as text — Cột số có thể bị đọc thành chữ

D. To interpret the data and calculations correctly — Để hiểu đúng dữ liệu và phép tính

**Q20. Why define what each row and column means? — Vì sao cần nêu ý nghĩa từng hàng và cột?**

A. An element-wise product aligned by index — Tích từng phần tử được căn theo index

B. Two named columns — Hai cột được nêu tên

C. A numeric column may be parsed as text — Cột số có thể bị đọc thành chữ

D. To interpret the data and calculations correctly — Để hiểu đúng dữ liệu và phép tính

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | Series associates values with an index. | Series liên kết từng giá trị với một nhãn index. |
| Q2 | **B** | A DataFrame organizes records in rows and fields in columns. | DataFrame tổ chức bản ghi thành hàng và trường thành cột. |
| Q3 | **C** | A column holds the same kind of attribute for each row. | Cột lưu cùng một thuộc tính ở các hàng. |
| Q4 | **D** | read_csv interprets separated fields and header names. | read_csv đọc các trường được phân cách cùng hàng tên cột. |
| Q5 | **A** | Default integer labels are assigned when none are given. | Không chỉ định nhãn thì Pandas tự gán chỉ số nguyên. |
| Q6 | **B** | Double brackets select a list of columns and preserve tabular form. | Hai lớp ngoặc vuông chọn danh sách cột và giữ dạng bảng. |
| Q7 | **C** | Single-bracket column lookup returns a Series. | Tra cứu một cột bằng ngoặc đơn trả Series. |
| Q8 | **D** | Shape gives the two dimensions of a DataFrame. | Shape cho biết hai kích thước của DataFrame. |
| Q9 | **A** | head returns the requested number of top rows. | head lấy số hàng đầu theo đối số. |
| Q10 | **B** | Each column can have its own dtype. | Mỗi cột có thể mang dtype riêng. |
| Q11 | **C** | info reports the table structure and completeness. | info cho biết cấu trúc và mức độ đầy đủ của bảng. |
| Q12 | **D** | describe computes basic summaries for numeric fields. | describe tính những thống kê cơ bản cho cột số. |
| Q13 | **A** | The index is separate from ordinary columns unless explicitly converted. | Index tách với các cột thông thường trừ khi được chuyển đổi. |
| Q14 | **B** | Pandas aligns data by matching index labels. | Pandas ghép giá trị theo các nhãn index tương ứng. |
| Q15 | **C** | The columns index lists field names. | Thuộc tính columns liệt kê tên trường. |
| Q16 | **D** | A consistent row meaning makes aggregations interpretable. | Ý nghĩa hàng nhất quán giúp hiểu đúng các phép tổng hợp. |
| Q17 | **A** | Aligned price and quantity values are multiplied for each record. | Giá và lượng tương ứng được nhân ở từng bản ghi. |
| Q18 | **B** | A list of names selects multiple columns. | Danh sách tên cho phép lấy nhiều cột. |
| Q19 | **C** | Malformed values can prevent numeric type inference. | Giá trị không hợp lệ có thể khiến Pandas không nhận kiểu số. |
| Q20 | **D** | Row and column semantics determine what a result means. | Ý nghĩa hàng và cột quyết định cách diễn giải kết quả. |

## 8. Nối bài tiếp theo

`NumPy ndarray → Pandas DataFrame → Làm sạch → EDA/AI`.
