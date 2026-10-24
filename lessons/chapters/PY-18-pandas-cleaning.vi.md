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

**Data cleaning (làm sạch dữ liệu)** là quá trình tìm và xử lý các giá trị thiếu, dòng lặp và giá trị sai kiểu trước khi phân tích. Với dữ liệu khách hàng và đơn hàng, ta đi từ **phát hiện** thiếu/trùng → **quyết định** xử lý → **kiểm tra** kết quả; không xóa hoặc điền giá trị chỉ vì hàm có sẵn.

### 4.1. Missing values — Phát hiện dữ liệu thiếu

**Từ vựng trong mục:** **Missing value** — giá trị thiếu; **NaN** — giá trị số thiếu.

**Giá trị thiếu** là ô chưa có dữ liệu hợp lệ, chẳng hạn ba khách hàng có tuổi `[20, None, 25]` và khách thứ hai chưa khai báo. Trong DataFrame, **mỗi hàng là một khách**, cột `age` là tuổi (năm). Pandas thường biểu diễn số thiếu là `NaN`; `isna()` tạo giá trị Boolean đánh dấu ô thiếu, rồi `sum()` đếm số trường hợp `True`. Thiếu khác với tuổi 0: không được tùy tiện coi khách chưa nhập tuổi là trẻ sơ sinh.

```python
import pandas as pd

customers = pd.DataFrame({'age': [20, None, 25]})
print(customers['age'].isna().sum())
```

**Kết quả khi chạy:**

```text
1
```

Có một khách chưa có tuổi. Kết quả là **số ô thiếu**, không phải giá trị tuổi của khách.

### 4.2. Duplicates — Nhận diện dòng trùng

**Từ vựng trong mục:** **Duplicate** — bản ghi trùng; **Row** — hàng.

Dữ liệu có thể chứa một giao dịch được ghi hai lần. Ví dụ bảng gồm các dòng `(O1, 10)`, `(O1, 10)`, `(O2, 20)`: **mỗi hàng là một giao dịch**, cột `id` là mã đơn, `amount` là tiền. `duplicated()` đánh dấu dòng lặp giống hệt **sau dòng đầu tiên**; `drop_duplicates()` giữ một bản. Tuy nhiên hai giao dịch cùng mã chưa chắc trùng hoàn toàn nếu số tiền hoặc chi tiết khác nhau — phải xác định quy tắc nhận diện trùng trước khi xóa.

```python
import pandas as pd

orders = pd.DataFrame({'id': ['O1', 'O1', 'O2'], 'amount': [10, 10, 20]})
print(orders.duplicated().tolist())
```

**Kết quả khi chạy:**

```text
[False, True, False]
```

Dòng thứ hai lặp đúng mọi cột của dòng đầu, nên chỉ dòng ấy được đánh dấu trùng.

### 4.3. Imputation — Điền dữ liệu thiếu hợp lý

**Từ vựng trong mục:** **Imputation** — điền khuyết; **Median** — trung vị.

**Điền khuyết** thay giá trị thiếu bằng một giá trị được lựa chọn theo ý nghĩa dữ liệu. Giả sử ba mức chi tiêu là `[100, None, 200]` nghìn đồng. Trung vị của hai số có thật là `(100+200)/2 = 150`; `fillna(median)` điền 150 vào ô thiếu. Không có một cách điền đúng cho mọi bài toán: với mã đơn thiếu nên xác minh nguồn, không tự thay bằng số trung vị. Nếu có tập train/test, thống kê dùng để điền phải học từ **train** để tránh rò rỉ dữ liệu.

```python
import pandas as pd

spent = pd.Series([100, None, 200], dtype=float)
median = spent.median()
print(spent.fillna(median).tolist())
```

**Kết quả khi chạy:**

```text
[100.0, 150.0, 200.0]
```

Ô thứ hai được điền 150 nghìn đồng; hai số đo hợp lệ 100 và 200 được giữ nguyên.

### 4.4. Data validation — Kiểm tra giá trị và kiểu

**Từ vựng trong mục:** **Validation** — kiểm tra tính hợp lệ; **Coerce** — chuyển giá trị sai thành thiếu.

**Kiểm tra dữ liệu** bảo đảm kiểu và phạm vi phù hợp trước khi tính. Một bảng giá nhận ba chuỗi `'100'`, `'bad'`, `'250'`. `pd.to_numeric(errors='coerce')` chuyển chuỗi số thành số thực, còn chữ `bad` không đổi được thành `NaN`. Sau đó mới quyết định bỏ hàng, điền khuyết hay yêu cầu sửa ở nguồn. Nếu dùng `errors='raise'`, trường hợp không hợp lệ sẽ phát sinh lỗi để chương trình xử lý.

```python
import pandas as pd

raw = pd.Series(['100', 'bad', '250'])
prices = pd.to_numeric(raw, errors='coerce')
print(prices.isna().sum())
```

**Kết quả khi chạy:**

```text
1
```

Có đúng một giá trị giá không hợp lệ. Chuyển thành NaN giúp phát hiện, không có nghĩa đã sửa được giá trị thật.

## 5. Năm tình huống thực tế

### Tình huống 1 — Báo số khách thiếu tuổi

**Từ vựng trong mục:** **Missing value** — giá trị thiếu.

**Tình huống thực tế:** Một bảng tuổi khách có ba hàng `[20, None, 25]`, trong đó khách thứ hai chưa nhập tuổi. Đếm số tuổi bị thiếu.

**Vì sao chọn cách giải này?** `isna()` đánh dấu các ô thiếu; `sum()` đếm các ô đó theo cột.

**Quy trình giải:**

1. Tạo bảng `age` gồm ba khách, người thứ hai có giá trị thiếu.
2. Dùng `isna()` đánh dấu từng ô thiếu.
3. Dùng `sum()` đếm và in số trường hợp cần rà soát.

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

### Tình huống 2 — Điền giá trị trung vị

**Từ vựng trong mục:** **Imputation** — điền khuyết; **Median** — trung vị.

**Tình huống thực tế:** Cửa hàng có mức chi tiêu `[100, None, 200]` đơn vị tiền; một dòng chưa có số liệu. Điền chỗ thiếu bằng trung vị của số liệu hiện có.

**Vì sao chọn cách giải này?** Trung vị của 100 và 200 là 150; `fillna` chỉ thay giá trị thiếu.

**Quy trình giải:**

1. Tạo cột `spent` có hai số 100, 200 và một ô thiếu.
2. Tính trung vị từ các số có thật, được 150.
3. Gọi `fillna` trên cột chi tiêu và in bảng đã điền.

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

### Tình huống 3 — Loại dòng trùng hoàn toàn

**Từ vựng trong mục:** **Duplicate** — bản ghi trùng.

**Tình huống thực tế:** Đơn hàng có ba dòng O1:10, O1:10 và O2:20, trong đó hai dòng O1 giống hệt nhau. Loại dòng trùng hoàn toàn và in bảng còn lại.

**Vì sao chọn cách giải này?** `drop_duplicates()` giữ một bản của những dòng giống nhau.

**Quy trình giải:**

1. Tạo bảng ba dòng với hai bản ghi O1 giống hệt và một O2.
2. Gọi `drop_duplicates()` để loại dòng trùng hoàn toàn.
3. In bảng còn hai bản ghi; giữ nguyên index cũ nếu không reset.

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

### Tình huống 4 — Đổi chuỗi giá sang số

**Từ vựng trong mục:** **Data validation** — kiểm tra dữ liệu.

**Tình huống thực tế:** Dữ liệu giá nhận ba chuỗi `100`, `bad`, `250`. Giá trị `bad` không thể đổi thành số. Đổi các chuỗi số thành số, còn giá trị không hợp lệ thành NaN.

**Vì sao chọn cách giải này?** `to_numeric(errors='coerce')` cho phép xử lý giá trị sai kiểu mà không dừng chương trình.

**Quy trình giải:**

1. Đọc ba chuỗi giá, trong đó `'bad'` không phải số.
2. Dùng `pd.to_numeric(..., errors='coerce')` chuyển lỗi thành NaN.
3. In Series và xác định vị trí giá chưa hợp lệ.

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

### Tình huống 5 — Chuẩn bị train/test tránh leakage

**Từ vựng trong mục:** **Missing value** — giá trị thiếu.

**Tình huống thực tế:** Dữ liệu train là `[10, None, 20]` và test là `[None,30]`. Lấy trung vị từ train rồi điền số thiếu của cả train và test.

**Vì sao chọn cách giải này?** Tính thống kê chỉ từ tập train giúp tránh rò rỉ thông tin từ test.

**Quy trình giải:**

1. Tạo riêng Series train `[10, None, 20]` và test `[None, 30]`.
2. Tính trung vị **chỉ trên train**, thu được 15.
3. Dùng 15 điền vào ô thiếu của cả train và test, không học từ test.

```python
import pandas as pd
train=pd.Series([10,None,20])
test=pd.Series([None,30])
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

## 6. Sai lầm thường gặp

- **Thiếu dữ liệu** không đồng nghĩa với 0; điền 0 vào tuổi, giá hay lượng hàng thiếu có thể làm sai thống kê.
- `duplicated()` mặc định xét toàn bộ các cột; xóa trùng phải hiểu **khóa định danh** và ý nghĩa từng bản ghi.
- `drop_duplicates()` thường giữ **index cũ**; cần `reset_index(drop=True)` nếu muốn đánh lại nhãn hàng.
- `to_numeric(errors='coerce')` đổi dữ liệu sai thành NaN, **không tự đoán** giá trị thật.
- Với Machine Learning, chỉ tính trung vị/trung bình để điền từ **tập train**, sau đó áp dụng cho test để tránh data leakage.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a missing value? — Giá trị thiếu là gì?**

A. An absent or unknown data entry — Ô dữ liệu chưa có giá trị xác định

B. A record repeated under a defined matching rule — Bản ghi lặp theo tiêu chí đối chiếu xác định

C. Replacing missing entries with chosen estimates — Thay ô thiếu bằng giá trị ước lượng đã chọn

D. Checking types and rules before analysis — Kiểm tra kiểu và quy tắc trước khi phân tích

**Q2. What is a duplicate record? — Bản ghi trùng là gì?**

A. An absent or unknown data entry — Ô dữ liệu chưa có giá trị xác định

B. A record repeated under a defined matching rule — Bản ghi lặp theo tiêu chí đối chiếu xác định

C. Replacing missing entries with chosen estimates — Thay ô thiếu bằng giá trị ước lượng đã chọn

D. Checking types and rules before analysis — Kiểm tra kiểu và quy tắc trước khi phân tích

**Q3. What is imputation? — Điền khuyết là gì?**

A. An absent or unknown data entry — Ô dữ liệu chưa có giá trị xác định

B. A record repeated under a defined matching rule — Bản ghi lặp theo tiêu chí đối chiếu xác định

C. Replacing missing entries with chosen estimates — Thay ô thiếu bằng giá trị ước lượng đã chọn

D. Checking types and rules before analysis — Kiểm tra kiểu và quy tắc trước khi phân tích

**Q4. What is data validation? — Kiểm tra dữ liệu hợp lệ là gì?**

A. An absent or unknown data entry — Ô dữ liệu chưa có giá trị xác định

B. A record repeated under a defined matching rule — Bản ghi lặp theo tiêu chí đối chiếu xác định

C. Replacing missing entries with chosen estimates — Thay ô thiếu bằng giá trị ước lượng đã chọn

D. Checking types and rules before analysis — Kiểm tra kiểu và quy tắc trước khi phân tích

**Q5. What does `isna()` identify? — `isna()` phát hiện gì?**

A. Missing entries — Các ô thiếu

B. Repeated rows after the first occurrence — Các hàng lặp sau lần xuất hiện đầu

C. Replaces missing entries with a value — Thay ô thiếu bằng giá trị cho trước

D. Turns invalid numeric text into NaN — Chuyển chữ không đổi được sang số thành NaN

**Q6. What does `duplicated()` mark by default? — `duplicated()` mặc định đánh dấu gì?**

A. Missing entries — Các ô thiếu

B. Repeated rows after the first occurrence — Các hàng lặp sau lần xuất hiện đầu

C. Replaces missing entries with a value — Thay ô thiếu bằng giá trị cho trước

D. Turns invalid numeric text into NaN — Chuyển chữ không đổi được sang số thành NaN

**Q7. What does `fillna(value)` do? — `fillna(value)` làm gì?**

A. Missing entries — Các ô thiếu

B. Repeated rows after the first occurrence — Các hàng lặp sau lần xuất hiện đầu

C. Replaces missing entries with a value — Thay ô thiếu bằng giá trị cho trước

D. Turns invalid numeric text into NaN — Chuyển chữ không đổi được sang số thành NaN

**Q8. What does `pd.to_numeric(..., errors='coerce')` do with invalid text? — `to_numeric(..., errors='coerce')` xử lý chuỗi không phải số thế nào?**

A. Missing entries — Các ô thiếu

B. Repeated rows after the first occurrence — Các hàng lặp sau lần xuất hiện đầu

C. Replaces missing entries with a value — Thay ô thiếu bằng giá trị cho trước

D. Turns invalid numeric text into NaN — Chuyển chữ không đổi được sang số thành NaN

**Q9. What does `dropna()` normally remove? — `dropna()` mặc định xóa gì?**

A. Rows containing missing data — Các hàng chứa dữ liệu thiếu

B. The first occurrence of each distinct row — Lần xuất hiện đầu của từng hàng khác nhau

C. The middle value after sorting, or mean of the two middle values — Giá trị giữa khi sắp, hoặc trung bình hai giá trị giữa

D. Raise an exception on invalid input — Báo ngoại lệ khi đầu vào không hợp lệ

**Q10. What does `drop_duplicates()` normally keep? — `drop_duplicates()` thường giữ gì?**

A. Rows containing missing data — Các hàng chứa dữ liệu thiếu

B. The first occurrence of each distinct row — Lần xuất hiện đầu của từng hàng khác nhau

C. The middle value after sorting, or mean of the two middle values — Giá trị giữa khi sắp, hoặc trung bình hai giá trị giữa

D. Raise an exception on invalid input — Báo ngoại lệ khi đầu vào không hợp lệ

**Q11. What is the median? — Trung vị là gì?**

A. Rows containing missing data — Các hàng chứa dữ liệu thiếu

B. The first occurrence of each distinct row — Lần xuất hiện đầu của từng hàng khác nhau

C. The middle value after sorting, or mean of the two middle values — Giá trị giữa khi sắp, hoặc trung bình hai giá trị giữa

D. Raise an exception on invalid input — Báo ngoại lệ khi đầu vào không hợp lệ

**Q12. What is the meaning of `errors='raise'` in numeric conversion? — `errors='raise'` khi đổi sang số có nghĩa gì?**

A. Rows containing missing data — Các hàng chứa dữ liệu thiếu

B. The first occurrence of each distinct row — Lần xuất hiện đầu của từng hàng khác nhau

C. The middle value after sorting, or mean of the two middle values — Giá trị giữa khi sắp, hoặc trung bình hai giá trị giữa

D. Raise an exception on invalid input — Báo ngoại lệ khi đầu vào không hợp lệ

**Q13. What is data leakage in train/test preprocessing? — Data leakage khi chuẩn bị train/test là gì?**

A. Using information from test data while fitting preprocessing — Dùng thông tin của test khi học tham số tiền xử lý

B. Zero may have a different real-world meaning — Số 0 có thể mang ý nghĩa thực tế khác

C. Records with shared IDs may still represent distinct events — Hai dòng cùng ID vẫn có thể là sự kiện khác nhau

D. To audit and reverse cleaning decisions — Để đối chiếu và phục hồi quyết định xử lý

**Q14. Why is replacing every missing value with zero risky? — Vì sao thay mọi ô thiếu bằng 0 là rủi ro?**

A. Using information from test data while fitting preprocessing — Dùng thông tin của test khi học tham số tiền xử lý

B. Zero may have a different real-world meaning — Số 0 có thể mang ý nghĩa thực tế khác

C. Records with shared IDs may still represent distinct events — Hai dòng cùng ID vẫn có thể là sự kiện khác nhau

D. To audit and reverse cleaning decisions — Để đối chiếu và phục hồi quyết định xử lý

**Q15. Why check key columns before removing duplicates? — Vì sao phải xem cột khóa trước khi xóa trùng?**

A. Using information from test data while fitting preprocessing — Dùng thông tin của test khi học tham số tiền xử lý

B. Zero may have a different real-world meaning — Số 0 có thể mang ý nghĩa thực tế khác

C. Records with shared IDs may still represent distinct events — Hai dòng cùng ID vẫn có thể là sự kiện khác nhau

D. To audit and reverse cleaning decisions — Để đối chiếu và phục hồi quyết định xử lý

**Q16. Why preserve the original raw data while cleaning? — Vì sao nên giữ dữ liệu gốc khi làm sạch?**

A. Using information from test data while fitting preprocessing — Dùng thông tin của test khi học tham số tiền xử lý

B. Zero may have a different real-world meaning — Số 0 có thể mang ý nghĩa thực tế khác

C. Records with shared IDs may still represent distinct events — Hai dòng cùng ID vẫn có thể là sự kiện khác nhau

D. To audit and reverse cleaning decisions — Để đối chiếu và phục hồi quyết định xử lý

**Q17. What does a Boolean missing-value mask contain? — Mặt nạ dữ liệu thiếu chứa gì?**

A. True and False values — Các giá trị True và False

B. Original retained-row labels remain — Nhãn index của hàng được giữ vẫn còn

C. Rebuilds sequential indices without retaining old index as a column — Đánh lại index tuần tự, không giữ index cũ thành cột

D. Choose a justified missing-data treatment — Chọn cách xử lý dữ liệu thiếu có cơ sở

**Q18. What happens to index labels after `drop_duplicates()` by default? — Sau `drop_duplicates()`, index mặc định thay đổi thế nào?**

A. True and False values — Các giá trị True và False

B. Original retained-row labels remain — Nhãn index của hàng được giữ vẫn còn

C. Rebuilds sequential indices without retaining old index as a column — Đánh lại index tuần tự, không giữ index cũ thành cột

D. Choose a justified missing-data treatment — Chọn cách xử lý dữ liệu thiếu có cơ sở

**Q19. What does `reset_index(drop=True)` do? — `reset_index(drop=True)` làm gì?**

A. True and False values — Các giá trị True và False

B. Original retained-row labels remain — Nhãn index của hàng được giữ vẫn còn

C. Rebuilds sequential indices without retaining old index as a column — Đánh lại index tuần tự, không giữ index cũ thành cột

D. Choose a justified missing-data treatment — Chọn cách xử lý dữ liệu thiếu có cơ sở

**Q20. What should happen after coercing invalid numeric text to NaN? — Sau khi chuyển chuỗi số sai thành NaN cần làm gì?**

A. True and False values — Các giá trị True và False

B. Original retained-row labels remain — Nhãn index của hàng được giữ vẫn còn

C. Rebuilds sequential indices without retaining old index as a column — Đánh lại index tuần tự, không giữ index cũ thành cột

D. Choose a justified missing-data treatment — Chọn cách xử lý dữ liệu thiếu có cơ sở

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | Missing means there is no valid observed value at that position. | Thiếu nghĩa là chưa có giá trị quan sát hợp lệ ở ô đó. |
| Q2 | **B** | Duplicate detection depends on which fields define identity. | Nhận diện trùng phụ thuộc các trường dùng làm tiêu chí. |
| Q3 | **C** | Imputation uses a justified value rather than claiming the original was observed. | Điền khuyết dùng giá trị lựa chọn chứ không coi đó là dữ liệu đã đo thật. |
| Q4 | **D** | Validation catches invalid types and out-of-range values. | Kiểm tra hợp lệ phát hiện sai kiểu và giá trị vượt phạm vi. |
| Q5 | **A** | isna returns a Boolean mask marking absent values. | isna trả mặt nạ Boolean đánh dấu giá trị thiếu. |
| Q6 | **B** | duplicated considers whole rows unless a subset is chosen. | duplicated xét toàn hàng nếu không chỉ định subset. |
| Q7 | **C** | fillna changes missing cells without replacing valid ones. | fillna thay ô thiếu mà giữ các giá trị hợp lệ. |
| Q8 | **D** | Coercion marks conversion failures as missing rather than guessing a number. | Cơ chế coerce đánh dấu lỗi chuyển kiểu là thiếu chứ không đoán số. |
| Q9 | **A** | By default DataFrame.dropna drops rows with at least one missing entry. | DataFrame.dropna mặc định bỏ hàng có ít nhất một ô thiếu. |
| Q10 | **B** | By default duplicate later rows are removed. | Mặc định các lần lặp sau của cùng hàng sẽ bị bỏ. |
| Q11 | **C** | Median is less affected by extremes than the arithmetic mean. | Trung vị ít nhạy với giá trị cực đoan hơn trung bình cộng. |
| Q12 | **D** | Raise surfaces invalid input instead of silently coercing it. | Raise làm lỗi lộ rõ thay vì chuyển âm thầm thành thiếu. |
| Q13 | **A** | Preprocessing statistics must be learned on training data only. | Thống kê tiền xử lý phải học chỉ từ tập train. |
| Q14 | **B** | An unobserved age is not automatically an age of zero. | Tuổi chưa nhập không tự đồng nghĩa tuổi bằng 0. |
| Q15 | **C** | Business rules determine whether two rows are truly duplicates. | Quy tắc nghiệp vụ xác định hai dòng có thực sự trùng không. |
| Q16 | **D** | A raw copy allows validation of each transformation. | Bản gốc giúp kiểm tra từng phép biến đổi. |
| Q17 | **A** | Each position indicates whether its input is missing. | Mỗi vị trí cho biết ô dữ liệu có thiếu hay không. |
| Q18 | **B** | Dropped rows do not automatically renumber retained indices. | Xóa hàng trùng không tự đánh lại index cho hàng còn lại. |
| Q19 | **C** | Resetting index can make a cleaned table easier to read. | Đánh lại nhãn hàng giúp bảng đã xử lý dễ đọc hơn. |
| Q20 | **D** | Coercion detects an issue but does not recover the unknown real value. | Coerce phát hiện lỗi, không khôi phục được giá trị thực chưa biết. |

## 8. Nối bài tiếp theo

`DataFrame → Data Cleaning → EDA → ML Pipeline`.
