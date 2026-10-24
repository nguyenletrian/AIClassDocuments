# PY-18 — Pandas: missing values, duplicates và kiểu dữ liệu


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Missing value** — giá trị thiếu; **Duplicate** — bản ghi trùng.

`DataFrame → Data Cleaning → EDA → ML Pipeline`

**Học xong dùng để làm gì?** Phát hiện và xử lý dữ liệu thiếu, trùng; tránh dùng thông tin test khi điền khuyết.

**Kết nối kiến thức tiếp theo:** PY-19 ghép những bảng dữ liệu sạch và tổng hợp theo nhóm.

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
df = pd.DataFrame({"age":[20, None, 25]})
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
df = pd.DataFrame({"spent":[100, None, 200]})
df["spent"] = df["spent"].fillna(df["spent"].median())
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
df = pd.DataFrame({"id":["O1", "O1", "O2"], "amount":[10, 10, 20]})
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
s = pd.Series(["100", "bad", "250"])
print(pd.to_numeric(s, errors="coerce"))
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
train = pd.Series([10, None, 20])
test = pd.Series([None, 30])
median = train.median()
print(train.fillna(median), test.fillna(median))
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

A. Replacing missing entries with chosen estimates — Thay ô thiếu bằng giá trị ước lượng đã chọn

B. Checking types and rules before analysis — Kiểm tra kiểu và quy tắc trước khi phân tích

C. An absent or unknown data entry — Ô dữ liệu chưa có giá trị xác định

D. A record repeated under a defined matching rule — Bản ghi lặp theo tiêu chí đối chiếu xác định

**Đáp án: C**

**Giải thích:** Thiếu nghĩa là chưa có giá trị quan sát hợp lệ ở ô đó. Trong Pandas, `NaN` và `None` có thể biểu thị ô thiếu; giá trị thiếu khác một số 0 đã được đo thật.


**Q2. What is a duplicate record? — Bản ghi trùng là gì?**

A. A record repeated under a defined matching rule — Bản ghi lặp theo tiêu chí đối chiếu xác định

B. Checking types and rules before analysis — Kiểm tra kiểu và quy tắc trước khi phân tích

C. An absent or unknown data entry — Ô dữ liệu chưa có giá trị xác định

D. Replacing missing entries with chosen estimates — Thay ô thiếu bằng giá trị ước lượng đã chọn

**Đáp án: A**

**Giải thích:** Nhận diện trùng phụ thuộc các trường dùng làm tiêu chí. Hai hàng cùng mã khách có thể là hai đơn riêng, nên phải xác định tiêu chí trùng trước khi xóa dữ liệu.


**Q3. What is imputation? — Điền khuyết là gì?**

A. An absent or unknown data entry — Ô dữ liệu chưa có giá trị xác định

B. Checking types and rules before analysis — Kiểm tra kiểu và quy tắc trước khi phân tích

C. Replacing missing entries with chosen estimates — Thay ô thiếu bằng giá trị ước lượng đã chọn

D. A record repeated under a defined matching rule — Bản ghi lặp theo tiêu chí đối chiếu xác định

**Đáp án: C**

**Giải thích:** Điền khuyết dùng giá trị lựa chọn chứ không coi đó là dữ liệu đã đo thật. Điền tuổi thiếu bằng trung vị của tập train là phép ước lượng, không chứng minh tuổi thật bằng trung vị đó.


**Q4. What is data validation? — Kiểm tra dữ liệu hợp lệ là gì?**

A. A record repeated under a defined matching rule — Bản ghi lặp theo tiêu chí đối chiếu xác định

B. An absent or unknown data entry — Ô dữ liệu chưa có giá trị xác định

C. Checking types and rules before analysis — Kiểm tra kiểu và quy tắc trước khi phân tích

D. Replacing missing entries with chosen estimates — Thay ô thiếu bằng giá trị ước lượng đã chọn

**Đáp án: C**

**Giải thích:** Kiểm tra hợp lệ phát hiện sai kiểu và giá trị vượt phạm vi. Với trường tuổi, bước kiểm tra có thể yêu cầu giá trị số không âm và loại chuỗi không hợp lệ.


**Q5. What does `isna()` identify? — `isna()` phát hiện gì?**

A. Missing entries — Các ô thiếu

B. Turns invalid numeric text into NaN — Chuyển chữ không đổi được sang số thành NaN

C. Repeated rows after the first occurrence — Các hàng lặp sau lần xuất hiện đầu

D. Replaces missing entries with a value — Thay ô thiếu bằng giá trị cho trước

**Đáp án: A**

**Giải thích:** isna trả mặt nạ Boolean đánh dấu giá trị thiếu. Với `[2, NaN]`, `isna()` đánh dấu `[False, True]`; hàm xác định chỗ thiếu mà không xóa dữ liệu.


**Q6. What does `duplicated()` mark by default? — `duplicated()` mặc định đánh dấu gì?**

A. Turns invalid numeric text into NaN — Chuyển chữ không đổi được sang số thành NaN

B. Repeated rows after the first occurrence — Các hàng lặp sau lần xuất hiện đầu

C. Replaces missing entries with a value — Thay ô thiếu bằng giá trị cho trước

D. Missing entries — Các ô thiếu

**Đáp án: B**

**Giải thích:** duplicated xét toàn hàng nếu không chỉ định subset. Với hai hàng giống nhau, hàng đầu thường nhận `False`, hàng sau nhận `True`; `subset=` thay đổi các cột dùng để xét trùng.


**Q7. What does `fillna(value)` do? — `fillna(value)` làm gì?**

A. Turns invalid numeric text into NaN — Chuyển chữ không đổi được sang số thành NaN

B. Missing entries — Các ô thiếu

C. Repeated rows after the first occurrence — Các hàng lặp sau lần xuất hiện đầu

D. Replaces missing entries with a value — Thay ô thiếu bằng giá trị cho trước

**Đáp án: D**

**Giải thích:** fillna thay ô thiếu mà giữ các giá trị hợp lệ. Với điểm thiếu, `df.fillna(0)` mặc định trả DataFrame đã điền mà không đổi `df` nếu chưa gán kết quả hoặc yêu cầu sửa tại chỗ.


**Q8. What does `pd.to_numeric(..., errors='coerce')` do with invalid text? — `to_numeric(..., errors='coerce')` xử lý chuỗi không phải số thế nào?**

A. Replaces missing entries with a value — Thay ô thiếu bằng giá trị cho trước

B. Turns invalid numeric text into NaN — Chuyển chữ không đổi được sang số thành NaN

C. Repeated rows after the first occurrence — Các hàng lặp sau lần xuất hiện đầu

D. Missing entries — Các ô thiếu

**Đáp án: B**

**Giải thích:** Cơ chế coerce đánh dấu lỗi chuyển kiểu là thiếu chứ không đoán số. Khi đổi kiểu số, chuỗi `'bad'` trở thành dấu thiếu, còn chuỗi hợp lệ như `'12'` được chuyển thành số 12.


**Q9. What does `dropna()` normally remove? — `dropna()` mặc định xóa gì?**

A. Rows containing missing data — Các hàng chứa dữ liệu thiếu

B. The middle value after sorting, or mean of the two middle values — Giá trị giữa khi sắp, hoặc trung bình hai giá trị giữa

C. Raise an exception on invalid input — Báo ngoại lệ khi đầu vào không hợp lệ

D. The first occurrence of each distinct row — Lần xuất hiện đầu của từng hàng khác nhau

**Đáp án: A**

**Giải thích:** DataFrame.dropna mặc định bỏ hàng có ít nhất một ô thiếu. Với DataFrame có ô thiếu, `dropna()` mặc định bỏ hàng chứa ít nhất một ô thiếu; nó không tự điền các ô đó.


**Q10. What does `drop_duplicates()` normally keep? — `drop_duplicates()` thường giữ gì?**

A. The middle value after sorting, or mean of the two middle values — Giá trị giữa khi sắp, hoặc trung bình hai giá trị giữa

B. The first occurrence of each distinct row — Lần xuất hiện đầu của từng hàng khác nhau

C. Rows containing missing data — Các hàng chứa dữ liệu thiếu

D. Raise an exception on invalid input — Báo ngoại lệ khi đầu vào không hợp lệ

**Đáp án: B**

**Giải thích:** Mặc định các lần lặp sau của cùng hàng sẽ bị bỏ. Với các hàng A, A, B, mặc định giữ A đầu và B, không giữ A cuối trừ khi đặt `keep='last'`.


**Q11. What is the median? — Trung vị là gì?**

A. Raise an exception on invalid input — Báo ngoại lệ khi đầu vào không hợp lệ

B. The first occurrence of each distinct row — Lần xuất hiện đầu của từng hàng khác nhau

C. Rows containing missing data — Các hàng chứa dữ liệu thiếu

D. The middle value after sorting, or mean of the two middle values — Giá trị giữa khi sắp, hoặc trung bình hai giá trị giữa

**Đáp án: D**

**Giải thích:** Trung vị ít nhạy với giá trị cực đoan hơn trung bình cộng. Với dãy đã sắp `[1,2,100]`, trung vị là 2 còn trung bình lớn hơn 34; nếu số phần tử chẵn thì lấy trung bình hai số ở giữa.


**Q12. What is the meaning of `errors='raise'` in numeric conversion? — `errors='raise'` khi đổi sang số có nghĩa gì?**

A. Rows containing missing data — Các hàng chứa dữ liệu thiếu

B. The middle value after sorting, or mean of the two middle values — Giá trị giữa khi sắp, hoặc trung bình hai giá trị giữa

C. The first occurrence of each distinct row — Lần xuất hiện đầu của từng hàng khác nhau

D. Raise an exception on invalid input — Báo ngoại lệ khi đầu vào không hợp lệ

**Đáp án: D**

**Giải thích:** Raise làm lỗi lộ rõ thay vì chuyển âm thầm thành thiếu. Dùng `pd.to_numeric(['bad'], errors='raise')` báo lỗi, còn `errors='coerce'` trả dấu giá trị số bị thiếu.


**Q13. What is data leakage in train/test preprocessing? — Data leakage khi chuẩn bị train/test là gì?**

A. Zero may have a different real-world meaning — Số 0 có thể mang ý nghĩa thực tế khác

B. To audit and reverse cleaning decisions — Để đối chiếu và phục hồi quyết định xử lý

C. Records with shared IDs may still represent distinct events — Hai dòng cùng ID vẫn có thể là sự kiện khác nhau

D. Using information from test data while fitting preprocessing — Dùng thông tin của test khi học tham số tiền xử lý

**Đáp án: D**

**Giải thích:** Thống kê tiền xử lý phải học chỉ từ tập train. Tính trung vị điền khuyết trên cả train và test làm thông tin của tập đánh giá lọt vào giai đoạn chuẩn bị mô hình.


**Q14. Why is replacing every missing value with zero risky? — Vì sao thay mọi ô thiếu bằng 0 là rủi ro?**

A. To audit and reverse cleaning decisions — Để đối chiếu và phục hồi quyết định xử lý

B. Using information from test data while fitting preprocessing — Dùng thông tin của test khi học tham số tiền xử lý

C. Zero may have a different real-world meaning — Số 0 có thể mang ý nghĩa thực tế khác

D. Records with shared IDs may still represent distinct events — Hai dòng cùng ID vẫn có thể là sự kiện khác nhau

**Đáp án: C**

**Giải thích:** Tuổi chưa nhập không tự đồng nghĩa tuổi bằng 0. Số lượng hàng thiếu nghĩa là chưa biết, còn số lượng 0 nói rõ không có món nào; thay hai trường hợp cho nhau sẽ đổi ý nghĩa.


**Q15. Why check key columns before removing duplicates? — Vì sao phải xem cột khóa trước khi xóa trùng?**

A. Records with shared IDs may still represent distinct events — Hai dòng cùng ID vẫn có thể là sự kiện khác nhau

B. Using information from test data while fitting preprocessing — Dùng thông tin của test khi học tham số tiền xử lý

C. Zero may have a different real-world meaning — Số 0 có thể mang ý nghĩa thực tế khác

D. To audit and reverse cleaning decisions — Để đối chiếu và phục hồi quyết định xử lý

**Đáp án: A**

**Giải thích:** Quy tắc nghiệp vụ xác định hai dòng có thực sự trùng không. Hai giao dịch của cùng khách hàng có thể là hai sự kiện hợp lệ khác nhau dù trùng một mã định danh.


**Q16. Why preserve the original raw data while cleaning? — Vì sao nên giữ dữ liệu gốc khi làm sạch?**

A. Zero may have a different real-world meaning — Số 0 có thể mang ý nghĩa thực tế khác

B. To audit and reverse cleaning decisions — Để đối chiếu và phục hồi quyết định xử lý

C. Records with shared IDs may still represent distinct events — Hai dòng cùng ID vẫn có thể là sự kiện khác nhau

D. Using information from test data while fitting preprocessing — Dùng thông tin của test khi học tham số tiền xử lý

**Đáp án: B**

**Giải thích:** Bản gốc giúp kiểm tra từng phép biến đổi. Giữ bản nguồn không đổi giúp so sánh trước/sau và xem xét lại các quyết định làm sạch chưa đúng.


**Q17. What does a Boolean missing-value mask contain? — Mặt nạ dữ liệu thiếu chứa gì?**

A. True and False values — Các giá trị True và False

B. Original retained-row labels remain — Nhãn index của hàng được giữ vẫn còn

C. Choose a justified missing-data treatment — Chọn cách xử lý dữ liệu thiếu có cơ sở

D. Rebuilds sequential indices without retaining old index as a column — Đánh lại index tuần tự, không giữ index cũ thành cột

**Đáp án: A**

**Giải thích:** Mỗi vị trí cho biết ô dữ liệu có thiếu hay không. Một ô mask là `True` nếu đầu vào tương ứng bị thiếu và `False` nếu không; mask không phải danh sách giá trị thay thế.


**Q18. What happens to index labels after `drop_duplicates()` by default? — Sau `drop_duplicates()`, index mặc định thay đổi thế nào?**

A. True and False values — Các giá trị True và False

B. Choose a justified missing-data treatment — Chọn cách xử lý dữ liệu thiếu có cơ sở

C. Rebuilds sequential indices without retaining old index as a column — Đánh lại index tuần tự, không giữ index cũ thành cột

D. Original retained-row labels remain — Nhãn index của hàng được giữ vẫn còn

**Đáp án: D**

**Giải thích:** Xóa hàng trùng không tự đánh lại index cho hàng còn lại. Xóa các hàng mang nhãn 1 và 3 không tự đánh lại nhãn còn lại; phải reset index riêng nếu muốn nhãn liên tiếp.


**Q19. What does `reset_index(drop=True)` do? — `reset_index(drop=True)` làm gì?**

A. Original retained-row labels remain — Nhãn index của hàng được giữ vẫn còn

B. Choose a justified missing-data treatment — Chọn cách xử lý dữ liệu thiếu có cơ sở

C. Rebuilds sequential indices without retaining old index as a column — Đánh lại index tuần tự, không giữ index cũ thành cột

D. True and False values — Các giá trị True và False

**Đáp án: C**

**Giải thích:** Đánh lại nhãn hàng giúp bảng đã xử lý dễ đọc hơn. Sau khi bỏ hàng, `reset_index(drop=True)` tạo nhãn `0,1,2,...` mà không đưa index cũ thành cột mới.


**Q20. What should happen after coercing invalid numeric text to NaN? — Sau khi chuyển chuỗi số sai thành NaN cần làm gì?**

A. Rebuilds sequential indices without retaining old index as a column — Đánh lại index tuần tự, không giữ index cũ thành cột

B. Choose a justified missing-data treatment — Chọn cách xử lý dữ liệu thiếu có cơ sở

C. Original retained-row labels remain — Nhãn index của hàng được giữ vẫn còn

D. True and False values — Các giá trị True và False

**Đáp án: B**

**Giải thích:** Coerce phát hiện lỗi, không khôi phục được giá trị thực chưa biết. Sau khi coerce, hãy đếm số ô bị thiếu rồi quyết định loại bỏ, từ chối hay điền khuyết theo yêu cầu bài toán.

## 8. Nối bài tiếp theo

`DataFrame → Data Cleaning → EDA → ML Pipeline`.
