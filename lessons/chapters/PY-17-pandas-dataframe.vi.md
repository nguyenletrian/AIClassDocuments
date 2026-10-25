# PY-17 — Pandas Series, DataFrame và đọc CSV


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Series** — chuỗi Pandas; **DataFrame** — bảng dữ liệu.

`NumPy ndarray → Pandas DataFrame → Làm sạch → EDA/AI`

**Học xong dùng để làm gì?** Đọc CSV thành bảng, kiểm tra kiểu và tên cột, tính kết quả theo từng bản ghi.

**Kết nối kiến thức tiếp theo:** PY-18 làm sạch giá trị thiếu, trùng và sai định dạng trước khi phân tích.

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
# Mục đích: Dữ liệu một chiều có nhãn.
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
# Mục đích: Bảng hàng và cột.
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
# Mục đích: Đọc và tính trên thuộc tính.
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
# Mục đích: Đọc bảng từ văn bản CSV.
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

## 5. Năm tình huống Pandas — từ Series đến bảng có nhãn để phân tích

### Tình huống 1 — Cấp 1: Series có nhãn của 10 học viên

**Từ vựng trong mục:** **Series** — dãy có nhãn; **Index** — nhãn hàng; **loc** — tra theo nhãn.

**Tình huống thực tế:** Trung tâm có **10 học viên** H01…H10, mỗi dòng là tuổi (năm) của một học viên. Giáo vụ cần đọc tuổi H07 theo mã, không phụ thuộc thứ tự dòng hiển thị, rồi tính tuổi trung bình.

**Vì sao chọn cách này?** `pd.Series(values,index=ids)` gắn mã học viên cho từng số, `loc` tra theo nhãn thay vì vị trí list. Điều này quan trọng khi bảng được sắp lại.

**Quy trình:**
1. Tạo 10 mã đúng thứ tự tuổi đã ghi.
2. Tạo Series gắn index và đọc H07 bằng `.loc`.
3. Kiểm tra số bản ghi và in trung bình một chữ số thập phân.

```python
import pandas as pd
ages = [18,19,20,21,19,22,23,20,21,24]
ids = [f"H{i:02d}" for i in range(1, 11)]
series = pd.Series(ages, index=ids)
assert len(series) == 10
print("Học viên:", len(series))
print("Tuổi H07:", int(series.loc["H07"]))
print(f"Tuổi TB: {series.mean():.1f}")
```

**Kết quả khi chạy:**

```text
Học viên: 10
Tuổi H07: 23
Tuổi TB: 20.7
```

Nhãn H07 là mã học viên, không phải vị trí 7. Tuổi trung bình là thống kê của 10 người, không dùng để suy ra độ tuổi của một người cụ thể.

### Tình huống 2 — Cấp 2: DataFrame của 12 dòng giỏ hàng với các cột có đơn vị

**Từ vựng trong mục:** **DataFrame** — bảng dữ liệu; **Column** — cột; **Calculated field** — cột tính.

**Tình huống thực tế:** Quầy sách nhập **12 mặt hàng** P01…P12, mỗi hàng gồm giá (nghìn đồng/món) và số lượng (món). Cần tạo bảng với ba cột gốc, thêm cột thành tiền theo dòng và in tổng toàn giỏ; không nhầm tổng đơn giá với số tiền phải trả.

**Vì sao chọn cách này?** DataFrame giữ từng thuộc tính trong cột có tên rõ ràng; phép nhân `df['price'] * df['qty']` chạy đúng trên từng dòng, tạo cột thành tiền trước khi cộng.

**Quy trình:**
1. Ghép ba danh sách mã hàng, giá, số lượng đồng hàng.
2. Tạo DataFrame và thêm `amount`.
3. Đếm bản ghi, kiểm tra thành tiền mặt hàng đầu và tổng toàn giỏ.

```python
import pandas as pd
prices = [10,15,20,12,30,18,14,25,11,17,35,22]
quantities = [2,1,4,3,2,5,1,2,4,2,1,3]
df = pd.DataFrame({"sku": [f"P{i:02d}" for i in range(1, 13)],
                   "price_thousand": prices, "quantity": quantities})
df["amount_thousand"] = df["price_thousand"] * df["quantity"]
assert df.shape == (12, 4)
print("Mặt hàng:", len(df))
print("P01 thành tiền:", int(df.loc[0, "amount_thousand"]))
print("Tổng (nghìn đồng):", int(df["amount_thousand"].sum()))
```

**Kết quả khi chạy:**

```text
Mặt hàng: 12
P01 thành tiền: 20
Tổng (nghìn đồng): 544
```

Một hàng tương ứng một mặt hàng của giỏ; đơn giá tính theo nghìn đồng, số lượng theo món, thành tiền theo nghìn đồng.

### Tình huống 3 — Cấp 3: Đọc 15 đơn CSV và đối chiếu schema

**Từ vựng trong mục:** **read_csv** — đọc CSV; **Schema** — cấu trúc dữ liệu; **dtype** — kiểu cột.

**Tình huống thực tế:** Cửa hàng xuất **15 đơn** từ CSV giả lập; mỗi dòng gồm mã đơn, kênh bán `web/store/phone` và doanh số (đồng/đơn). Người quản lý cần kiểm tra số dòng, tên cột và tổng doanh số, tránh coi `order_id` là số khiến số 0 đầu mã bị mất.

**Vì sao chọn cách này?** `pd.read_csv(StringIO(...), dtype={'id': 'string'})` giữ mã định danh như chuỗi, còn cột doanh số được đọc thành số cho tính tổng; dùng bộ đệm văn bản để chạy ngay không cần file bên ngoài.

**Quy trình:**
1. Tạo CSV với một dòng tiêu đề và 15 đơn hàng.
2. Đọc qua pandas, chỉ định kiểu chuỗi cho mã đơn.
3. Kiểm tra schema, tổng đơn và số đơn từ kênh web.

```python
import pandas as pd
from io import StringIO
csv_text = "id,channel,amount_vnd\n" + "\n".join(
    f"{row['id']},{row['channel']},{row['amount']}" for row in [{"id":"O01","channel":"web","amount":10000},{"id":"O02","channel":"store","amount":15000},{"id":"O03","channel":"phone","amount":20000},{"id":"O04","channel":"web","amount":25000},{"id":"O05","channel":"store","amount":30000},{"id":"O06","channel":"phone","amount":10000},{"id":"O07","channel":"web","amount":15000},{"id":"O08","channel":"store","amount":20000},{"id":"O09","channel":"phone","amount":25000},{"id":"O10","channel":"web","amount":30000},{"id":"O11","channel":"store","amount":10000},{"id":"O12","channel":"phone","amount":15000},{"id":"O13","channel":"web","amount":20000},{"id":"O14","channel":"store","amount":25000},{"id":"O15","channel":"phone","amount":30000}])
df = pd.read_csv(StringIO(csv_text), dtype={"id": "string"})
assert len(df) == 15
print("Đơn:", len(df))
print("Cột:", ", ".join(df.columns))
print("Kênh web:", int((df["channel"] == "web").sum()))
print("Tổng (đồng):", int(df["amount_vnd"].sum()))
```

**Kết quả khi chạy:**

```text
Đơn: 15
Cột: id, channel, amount_vnd
Kênh web: 5
Tổng (đồng): 300000
```

Mã `O01` được giữ nguyên ký tự; phần cộng chỉ áp dụng cho doanh số (đồng), không áp dụng cho mã khách hay tên kênh.

### Tình huống 4 — Cấp 4: Kiểm tra 18 hồ sơ đầu vào bằng info và to_numeric

**Từ vựng trong mục:** **info** — mô tả cột; **to_numeric** — đổi sang số; **Missing value** — giá trị thiếu.

**Tình huống thực tế:** Biểu mẫu đăng ký có **18 hồ sơ**, mỗi hàng gồm tuổi (năm) và mức chi (đồng). Hai mức chi chưa được ghi đúng (`''` và `N/A`), nhưng tuổi của hai người vẫn hợp lệ. Cần kiểm tra cột, chuyển mức chi sang số có kiểm soát, báo số ô thiếu và tổng mức chi **chỉ trên 16 dòng có số**.

**Vì sao chọn cách này?** Pandas có thể lưu giá đầu vào là chuỗi; `pd.to_numeric(errors='coerce')` biến chuỗi sai thành NaN để đếm riêng, thay vì gây lỗi hoặc đưa vào tổng như 0. `dtypes` xác nhận sau chuyển đổi cột có dạng số.

**Quy trình:**
1. Tạo bảng 18 dòng từ danh sách tuổi và mức chi dạng chữ.
2. Đổi kiểu cột mức chi có kiểm soát; kiểm tra kiểu dữ liệu.
3. Đếm số thiếu và tổng hợp những số hợp lệ.

```python
import pandas as pd
ages = [21,22,20,19,25,23,24,20,21,26,22,23,24,19,20,21,25,22]
raw_spent = ["100000","110000","120000","130000","140000","","160000","170000","180000","190000","200000","210000","220000","N/A","240000","250000","260000","270000"]
df = pd.DataFrame({"age_years": ages, "spent_vnd": raw_spent})
df["spent_vnd"] = pd.to_numeric(df["spent_vnd"], errors="coerce")
assert len(df) == 18
print("Hồ sơ:", len(df))
print("Tuổi là số:", bool(pd.api.types.is_numeric_dtype(df["age_years"])))
print("Mức chi là số:", bool(pd.api.types.is_numeric_dtype(df["spent_vnd"])))
print("Mức chi thiếu:", int(df["spent_vnd"].isna().sum()))
print("Tổng hợp lệ (đồng):", int(df["spent_vnd"].sum()))
```

**Kết quả khi chạy:**

```text
Hồ sơ: 18
Tuổi là số: True
Mức chi là số: True
Mức chi thiếu: 2
Tổng hợp lệ (đồng): 2950000
```

Pandas tự bỏ NaN khi tính `sum`, nhưng báo cáo vẫn phải hiển thị rõ **hai hồ sơ chưa đủ dữ liệu**. Tổng này là tổng mức chi của mẫu, không phải số tiền có được từ một khách.

### Tình huống 5 — Cấp 5: Tạo bảng đặc trưng 20 học viên có nhãn kết quả

**Từ vựng trong mục:** **Feature** — đặc trưng; **Target** — nhãn dự đoán; **DataFrame schema** — cấu trúc bảng.

**Tình huống thực tế:** Một khóa học ghi **20 học viên** H01…H20; mỗi dòng có tuổi (năm), số giờ tự học trong tuần (giờ/tuần) và nhãn đã hoàn thành (1) / chưa hoàn thành (0). Hai học viên **chưa được chấm kết quả**, nên nhãn là `None`. Trước khi chuyển bảng cho bước xử lý dữ liệu tiếp theo, cần kiểm tra cột, kiểu số, tách danh sách **18 dòng có nhãn** và số dòng chờ nhãn; không tự đoán nhãn từ tuổi hoặc giờ học.

**Vì sao chọn cách này?** DataFrame giữ ba thuộc tính theo tên cột; `isna()` giúp nhận biết người thiếu nhãn, còn `loc` chọn bảng có nhãn mà không xóa hay điền dữ liệu nguyên bản. Đây mới là giai đoạn chuẩn bị bảng, chưa học/đánh giá mô hình AI.

**Quy trình:**
1. Tạo 20 bản ghi với mã, tuổi, số giờ học và nhãn hoàn thành.
2. Kiểm tra khóa mã duy nhất, nhãn chỉ 0/1 hoặc thiếu.
3. Dùng `.loc` lấy các dòng có nhãn và in số cần bổ sung.

```python
import pandas as pd
records = pd.DataFrame({
    "student_id": [f"H{i:02d}" for i in range(1, 21)],
    "age_years": [18,19,20,21,22,23,24,25,26,18,19,20,21,22,23,24,25,26,18,19],
    "study_hours": [5,7,9,11,5,7,9,11,5,7,9,11,5,7,9,11,5,7,9,11],
    "completed": [1,1,0,0,1,1,None,0,1,1,0,0,1,1,0,0,1,1,None,0],
})
labelled = records.loc[records["completed"].notna()].copy()
assert len(records) == 20 and records["student_id"].is_unique
assert labelled["completed"].isin([0, 1]).all()
print("Học viên:", len(records))
print("Có nhãn:", len(labelled))
print("Chờ nhãn:", int(records["completed"].isna().sum()))
print("Hoàn thành:", int((labelled["completed"] == 1).sum()))
print("Cột đặc trưng:", ", ".join(["age_years", "study_hours"]))
```

**Kết quả khi chạy:**

```text
Học viên: 20
Có nhãn: 18
Chờ nhãn: 2
Hoàn thành: 10
Cột đặc trưng: age_years, study_hours
```

Không sử dụng các dòng thiếu nhãn để báo tỷ lệ hoàn thành. Bảng đặc trưng hai cột và nhãn là các khái niệm khác nhau; không suy luận kết quả học tập từ dữ liệu giả lập.

## 6. Sai lầm thường gặp

- **Series** một chiều, **DataFrame** hai chiều. `df['x']` chọn Series; `df[['x']]` giữ dạng DataFrame một cột.
- Phải hiểu **index** là nhãn hàng, không nhất thiết là cột dữ liệu. Pandas căn dữ liệu theo index khi kết hợp các Series.
- Đơn giá, số lượng và doanh thu có **đơn vị khác nhau**; nhân `price × qty` mới có ý nghĩa là thành tiền.
- CSV vốn là văn bản; cần xem lại `dtype` vì dữ liệu bẩn có thể khiến cột số bị đọc thành chuỗi.
- Không đưa mã định danh hoặc nhãn `city` vào mô hình dự đoán chỉ vì chúng có mặt trong bảng; phải chọn đặc trưng theo mục tiêu.

## 7. Trắc nghiệm

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a Pandas Series? | Pandas Series là gì?**

A. Parse tabular CSV data into a DataFrame | Đọc dữ liệu CSV thành DataFrame

B. One field across multiple records | Một thuộc tính qua nhiều bản ghi

C. A two-dimensional labeled table | Bảng dữ liệu hai chiều có nhãn

D. A one-dimensional labeled data structure | Cấu trúc dữ liệu một chiều có nhãn

**Đáp án: D**

**Giải thích:** Series liên kết từng giá trị với một nhãn index. Ví dụ `pd.Series([5,6], index=['a','b'])` gắn nhãn `'a'`, `'b'` cho các giá trị, khác với List không có hệ nhãn riêng.


**Q2. What is a Pandas DataFrame? | Pandas DataFrame là gì?**

A. A one-dimensional labeled data structure | Cấu trúc dữ liệu một chiều có nhãn

B. A two-dimensional labeled table | Bảng dữ liệu hai chiều có nhãn

C. Parse tabular CSV data into a DataFrame | Đọc dữ liệu CSV thành DataFrame

D. One field across multiple records | Một thuộc tính qua nhiều bản ghi

**Đáp án: B**

**Giải thích:** DataFrame tổ chức bản ghi thành hàng và trường thành cột. Bảng gồm ba quan sát và hai trường có shape `(3,2)`; Series lại là cấu trúc một chiều có nhãn.


**Q3. What does a column represent? | Một cột trong bảng thể hiện gì?**

A. A one-dimensional labeled data structure | Cấu trúc dữ liệu một chiều có nhãn

B. One field across multiple records | Một thuộc tính qua nhiều bản ghi

C. A two-dimensional labeled table | Bảng dữ liệu hai chiều có nhãn

D. Parse tabular CSV data into a DataFrame | Đọc dữ liệu CSV thành DataFrame

**Đáp án: B**

**Giải thích:** Cột lưu cùng một thuộc tính ở các hàng. Nếu các hàng là đơn hàng, cột `price` ghi giá của từng đơn và cần xác định rõ đơn vị tiền tệ.


**Q4. What is the purpose of `pd.read_csv()`? | `pd.read_csv()` dùng để làm gì?**

A. A one-dimensional labeled data structure | Cấu trúc dữ liệu một chiều có nhãn

B. One field across multiple records | Một thuộc tính qua nhiều bản ghi

C. A two-dimensional labeled table | Bảng dữ liệu hai chiều có nhãn

D. Parse tabular CSV data into a DataFrame | Đọc dữ liệu CSV thành DataFrame

**Đáp án: D**

**Giải thích:** read_csv đọc các trường được phân cách cùng hàng tên cột. Ví dụ hàng tiêu đề CSV `name,score` tạo tên cột tương ứng, nhưng các ô số sai định dạng vẫn có thể cần làm sạch sau khi đọc.


**Q5. What does `pd.Series([1,2])` return? | `pd.Series([1,2])` trả về gì?**

A. A Series containing column x | Series chứa cột x

B. A Series with default index 0,1 | Series có index mặc định 0,1

C. A DataFrame containing one column | DataFrame có một cột

D. A tuple with row and column counts | Tuple gồm số hàng và số cột

**Đáp án: B**

**Giải thích:** Không chỉ định nhãn thì Pandas tự gán chỉ số nguyên. Không truyền index, hai giá trị nhận nhãn `0` và `1`; kết quả là Series chứ không phải DataFrame một cột.


**Q6. What does `df[['x']]` return? | `df[['x']]` trả về gì?**

A. A DataFrame containing one column | DataFrame có một cột

B. A tuple with row and column counts | Tuple gồm số hàng và số cột

C. A Series containing column x | Series chứa cột x

D. A Series with default index 0,1 | Series có index mặc định 0,1

**Đáp án: A**

**Giải thích:** Hai lớp ngoặc vuông chọn danh sách cột và giữ dạng bảng. Nếu `df` có năm hàng, `df[['x']]` giữ kết quả hai chiều với shape `(5,1)`, khác `df['x']`.


**Q7. When DataFrame column labels are unique, what does `df['x']` return? | Khi tên cột DataFrame không trùng nhau, `df['x']` trả về gì?**

A. A tuple with row and column counts | Tuple gồm số hàng và số cột

B. A Series containing column x | Series chứa cột x

C. A DataFrame containing one column | DataFrame có một cột

D. A Series with default index 0,1 | Series có index mặc định 0,1

**Đáp án: B**

**Giải thích:** Tra cứu một cột bằng ngoặc đơn trả Series. Với tên cột không trùng, `df['x']` là Series một chiều; hai lớp ngoặc vuông thì trả DataFrame.


**Q8. What does `df.shape` return? | `df.shape` trả về gì?**

A. A Series with default index 0,1 | Series có index mặc định 0,1

B. A DataFrame containing one column | DataFrame có một cột

C. A Series containing column x | Series chứa cột x

D. A tuple with row and column counts | Tuple gồm số hàng và số cột

**Đáp án: D**

**Giải thích:** Shape cho biết hai kích thước của DataFrame. Với DataFrame bốn bản ghi và ba trường, `df.shape` là `(4,3)`, không phải số ô không thiếu.


**Q9. What does `df.head(3)` show? | `df.head(3)` hiển thị gì?**

A. Columns, non-null counts and data types | Các cột, số ô không thiếu và kiểu dữ liệu

B. Data types of columns | Kiểu dữ liệu của các cột

C. The first three rows | Ba hàng đầu

D. Descriptive statistics such as mean and quartiles | Thống kê mô tả như trung bình và các tứ phân vị

**Đáp án: C**

**Giải thích:** head lấy số hàng đầu theo đối số. Nếu DataFrame chỉ có hai hàng, `head(3)` trả hai hàng đó chứ không tạo thêm hàng giả.


**Q10. What does `df.dtypes` describe? | `df.dtypes` mô tả gì?**

A. Descriptive statistics such as mean and quartiles | Thống kê mô tả như trung bình và các tứ phân vị

B. The first three rows | Ba hàng đầu

C. Data types of columns | Kiểu dữ liệu của các cột

D. Columns, non-null counts and data types | Các cột, số ô không thiếu và kiểu dữ liệu

**Đáp án: C**

**Giải thích:** Mỗi cột có thể mang dtype riêng. Cột `price` có thể có dtype thực, còn `name` mang kiểu văn bản; `dtypes` không tính thống kê mô tả.


**Q11. What does `df.info()` primarily summarize? | `df.info()` chủ yếu tóm tắt gì?**

A. The first three rows | Ba hàng đầu

B. Data types of columns | Kiểu dữ liệu của các cột

C. Descriptive statistics such as mean and quartiles | Thống kê mô tả như trung bình và các tứ phân vị

D. Columns, non-null counts and data types | Các cột, số ô không thiếu và kiểu dữ liệu

**Đáp án: D**

**Giải thích:** info cho biết cấu trúc và mức độ đầy đủ của bảng. Nó hiển thị tên cột, số giá trị không thiếu, dtype và bộ nhớ; khác thao tác xem trước hàng dữ liệu bằng `head()`.


**Q12. What does `df.describe()` commonly provide for numeric columns? | `df.describe()` thường cung cấp gì cho cột số?**

A. Descriptive statistics such as mean and quartiles | Thống kê mô tả như trung bình và các tứ phân vị

B. The first three rows | Ba hàng đầu

C. Columns, non-null counts and data types | Các cột, số ô không thiếu và kiểu dữ liệu

D. Data types of columns | Kiểu dữ liệu của các cột

**Đáp án: A**

**Giải thích:** describe tính những thống kê cơ bản cho cột số. Với số `[2,4,6]`, trung bình bằng 4 và các tứ phân vị cho biết mức phân tán; `head()` chỉ hiển thị hàng dữ liệu gốc.


**Q13. What is an index in a DataFrame? | Index của DataFrame là gì?**

A. Column labels | Các tên cột

B. One observation or record | Một quan sát hoặc bản ghi

C. Labels identifying rows | Các nhãn xác định hàng

D. Index labels | Nhãn index

**Đáp án: C**

**Giải thích:** Index tách với các cột thông thường trừ khi được chuyển đổi. Index có thể là nhãn như mã học viên và tách khỏi các cột dữ liệu thường, trừ khi được đưa trở lại thành cột.


**Q14. How are Series values aligned during arithmetic? | Pandas căn các giá trị Series khi tính toán bằng gì?**

A. Labels identifying rows | Các nhãn xác định hàng

B. One observation or record | Một quan sát hoặc bản ghi

C. Index labels | Nhãn index

D. Column labels | Các tên cột

**Đáp án: C**

**Giải thích:** Pandas ghép giá trị theo các nhãn index tương ứng. Nếu hai Series sắp nhãn theo thứ tự khác nhau, Pandas ghép giá trị cùng nhãn trước khi cộng chứ không cộng máy móc theo vị trí.


**Q15. What does `df.columns` contain? | `df.columns` chứa gì?**

A. One observation or record | Một quan sát hoặc bản ghi

B. Index labels | Nhãn index

C. Column labels | Các tên cột

D. Labels identifying rows | Các nhãn xác định hàng

**Đáp án: C**

**Giải thích:** Thuộc tính columns liệt kê tên trường. Với các cột `name` và `age`, `list(df.columns)` trả danh sách tên cột, không phải nhãn hàng.


**Q16. What is a DataFrame row usually intended to represent? | Mỗi hàng DataFrame thường nên biểu diễn gì?**

A. One observation or record | Một quan sát hoặc bản ghi

B. Column labels | Các tên cột

C. Index labels | Nhãn index

D. Labels identifying rows | Các nhãn xác định hàng

**Đáp án: A**

**Giải thích:** Ý nghĩa hàng nhất quán giúp hiểu đúng các phép tổng hợp. Một hàng có thể là một học viên, giao dịch hoặc lần đo, nhưng cần định nghĩa nhất quán để hiểu đúng thống kê.


**Q17. What does `df['price'] * df['qty']` calculate? | `df['price'] * df['qty']` tính gì?**

A. An element-wise product aligned by index | Tích từng phần tử được căn theo index

B. To interpret the data and calculations correctly | Để hiểu đúng dữ liệu và phép tính

C. A numeric column may be parsed as text | Cột số có thể bị đọc thành chữ

D. Two named columns | Hai cột được nêu tên

**Đáp án: A**

**Giải thích:** Giá và lượng tương ứng được nhân ở từng bản ghi. Nếu cùng một hàng có giá 10 đô la và số lượng 3 món, tích là 30 đô la, không phải tổng của nhiều hàng.


**Q18. What does `df[['a','b']]` select? | `df[['a','b']]` chọn gì?**

A. A numeric column may be parsed as text | Cột số có thể bị đọc thành chữ

B. An element-wise product aligned by index | Tích từng phần tử được căn theo index

C. To interpret the data and calculations correctly | Để hiểu đúng dữ liệu và phép tính

D. Two named columns | Hai cột được nêu tên

**Đáp án: D**

**Giải thích:** Danh sách tên cho phép lấy nhiều cột. Kết quả vẫn là DataFrame chứa `a` và `b` theo thứ tự đã nêu, còn `df['a']` thường trả Series.


**Q19. What is a frequent risk when loading CSV numeric data? | Nguy cơ thường gặp khi đọc số từ CSV là gì?**

A. A numeric column may be parsed as text | Cột số có thể bị đọc thành chữ

B. Two named columns | Hai cột được nêu tên

C. An element-wise product aligned by index | Tích từng phần tử được căn theo index

D. To interpret the data and calculations correctly | Để hiểu đúng dữ liệu và phép tính

**Đáp án: A**

**Giải thích:** Giá trị không hợp lệ có thể khiến Pandas không nhận kiểu số. Ô như `'unknown'` nằm trong cột số có thể khiến kiểu bị suy ra thành văn bản/object, nên phải kiểm tra và đổi kiểu trước khi tính.


**Q20. Why define what each row and column means? | Vì sao cần nêu ý nghĩa từng hàng và cột?**

A. A numeric column may be parsed as text | Cột số có thể bị đọc thành chữ

B. To interpret the data and calculations correctly | Để hiểu đúng dữ liệu và phép tính

C. An element-wise product aligned by index | Tích từng phần tử được căn theo index

D. Two named columns | Hai cột được nêu tên

**Đáp án: B**

**Giải thích:** Ý nghĩa hàng và cột quyết định cách diễn giải kết quả. Nếu hàng là giao dịch và cột gồm giá cùng số lượng, nêu rõ đơn vị giúp tránh nhân nhầm trường và hiểu sai doanh thu.

## 8. Nối bài tiếp theo

`NumPy ndarray → Pandas DataFrame → Làm sạch → EDA/AI`.
