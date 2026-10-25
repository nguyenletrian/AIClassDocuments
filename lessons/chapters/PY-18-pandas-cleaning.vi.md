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
# Mục đích: Phát hiện dữ liệu thiếu.
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
# Mục đích: Nhận diện dòng trùng.
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
# Mục đích: Điền dữ liệu thiếu hợp lý.
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
# Mục đích: Kiểm tra giá trị và kiểu.
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

## 5. Năm tình huống làm sạch dữ liệu — từ phát hiện đến tránh leakage

### Tình huống 1 — Cấp 1: Phát hiện tuổi thiếu trong 10 hồ sơ

**Từ vựng trong mục:** **Missing value** — giá trị thiếu; **isna** — kiểm tra ô trống.

**Tình huống thực tế:** Bộ phận tuyển sinh tiếp nhận **10 hồ sơ** H01…H10, mỗi hàng là tuổi học viên (năm). H03 và H08 chưa khai tuổi (`None`). Cần đếm số hồ sơ thiếu tuổi và giữ nguyên các tuổi đã nhập, tuyệt đối không biến thiếu thành 0 tuổi.

**Vì sao chọn cách này?** `isna()` tạo một cột đúng/sai theo vị trí, rồi `sum()` đếm các dòng thiếu. Ở bước phát hiện chưa cần xóa hay điền số để tránh thay dữ liệu gốc.

**Quy trình:**
1. Tạo DataFrame 10 mã học viên và tuổi.
2. Dùng `isna()` trên cột tuổi để xác định mã thiếu.
3. In tổng số hồ sơ, số thiếu và mã cần bổ sung.

```python
import pandas as pd
df = pd.DataFrame({"id": [f"H{i:02d}" for i in range(1, 11)],
                   "age": [25,28,None,31,22,29,35,None,26,32]})
missing = df["age"].isna()
assert len(df) == 10
print("Hồ sơ:", len(df))
print("Thiếu tuổi:", int(missing.sum()))
print("Cần bổ sung:", ", ".join(df.loc[missing, "id"]))
```

**Kết quả khi chạy:**

```text
Hồ sơ: 10
Thiếu tuổi: 2
Cần bổ sung: H03, H08
```

Hai học viên còn thiếu tuổi vẫn tồn tại trong báo cáo; số 0 không được dùng làm tuổi điền vào.

### Tình huống 2 — Cấp 2: Điền trung vị cho hai trong 12 mức chi

**Từ vựng trong mục:** **Imputation** — điền khuyết; **Median** — trung vị; **Copy** — bản sao.

**Tình huống thực tế:** Cửa hàng khảo sát **12 mức chi** (nghìn đồng/khách), trong đó khách thứ 4 và thứ 9 chưa khai. Nhóm phân tích quyết định **thử** điền trung vị của mười mức chi có thật để có bảng làm việc, nhưng phải giữ bảng thô để kiểm tra; đây không phải dữ liệu chi tiêu thực tế của hai khách.

**Vì sao chọn cách này?** `median()` trên cột có thiếu tự bỏ NaN, còn `fillna()` tạo giá trị thay thế. Việc giữ bản gốc tách bạch số đo thật với số được suy ra; không sử dụng giá trị này như giao dịch thật.

**Quy trình:**
1. Tạo 12 khoản chi và đếm số thiếu trước sửa.
2. Tính trung vị từ dữ liệu có thật; sao chép bảng rồi `fillna`.
3. So sánh số thiếu của bản gốc và bản thử, in giá trị đã điền.

```python
import pandas as pd
raw = pd.DataFrame({"spent_thousand": [100,120,140,None,160,180,200,220,None,240,260,280]})
median = raw["spent_thousand"].median()
working = raw.copy()
working["spent_thousand"] = working["spent_thousand"].fillna(median)
assert len(raw) == 12
print("Khách:", len(raw))
print("Thiếu ban đầu:", int(raw["spent_thousand"].isna().sum()))
print(f"Trung vị (nghìn đồng): {median:.1f}")
print("Thiếu sau điền:", int(working["spent_thousand"].isna().sum()))
print("Bản gốc vẫn thiếu:", int(raw["spent_thousand"].isna().sum()))
```

**Kết quả khi chạy:**

```text
Khách: 12
Thiếu ban đầu: 2
Trung vị (nghìn đồng): 190.0
Thiếu sau điền: 0
Bản gốc vẫn thiếu: 2
```

Trung vị là một lựa chọn minh họa; quyết định điền hay bỏ dữ liệu phải xét mục đích phân tích và ý nghĩa giá trị thiếu.

### Tình huống 3 — Cấp 3: Loại đúng hàng trùng hoàn toàn trong 15 giao dịch

**Từ vựng trong mục:** **Duplicate** — bản ghi trùng; **drop_duplicates** — bỏ hàng trùng.

**Tình huống thực tế:** Một nhân viên nhập **15 dòng** đơn hàng gồm mã đơn và số tiền (nghìn đồng). Có ba dòng nhập lặp nguyên vẹn (cùng mã và số tiền). Cần biết số dòng trùng và số giao dịch sau bỏ trùng; đồng thời giải thích rằng chỉ được khử trùng khi đây thực sự là bản nhập lặp, không phải hai lần mua hợp lệ có cùng số tiền.

**Vì sao chọn cách này?** `duplicated()` so **tất cả cột** phát hiện hàng y hệt nhau; `drop_duplicates()` giữ bản đầu, không loại hai mã khác nhau chỉ vì số tiền bằng nhau.

**Quy trình:**
1. Tạo bảng với 15 cặp mã–tiền.
2. Đếm hàng trùng hoàn toàn bằng `duplicated()`.
3. Khử trùng trên bản làm việc, đối chiếu số dòng còn lại và tổng tiền.

```python
import pandas as pd
rows = [("O01",100),("O02",150),("O03",100),("O01",100),("O04",200),("O05",180),("O02",150),("O06",130),("O07",220),("O08",170),("O09",160),("O09",160),("O10",190),("O11",110),("O12",250)]
df = pd.DataFrame(rows, columns=["order_id", "amount_thousand"])
repeat_count = int(df.duplicated().sum())
cleaned = df.drop_duplicates().copy()
assert len(df) == 15 and len(cleaned) + repeat_count == 15
print("Dòng gốc:", len(df))
print("Dòng trùng:", repeat_count)
print("Dòng duy nhất:", len(cleaned))
print("Mã O01 còn:", int((cleaned["order_id"] == "O01").sum()))
```

**Kết quả khi chạy:**

```text
Dòng gốc: 15
Dòng trùng: 3
Dòng duy nhất: 12
Mã O01 còn: 1
```

Chỉ khử ba hàng xác định là bị nhập lặp; nếu có số hóa đơn hợp lệ khác, không được xóa chỉ vì giá trị thanh toán trùng nhau.

### Tình huống 4 — Cấp 4: Chuyển 18 giá tiền dạng chữ và rà soát giá sai

**Từ vựng trong mục:** **to_numeric** — chuyển sang số; **errors=coerce** — biến lỗi thành NaN; **Validation** — kiểm dữ liệu.

**Tình huống thực tế:** Nhà bán hàng nhập **18 đơn giá** (đồng/món), một hàng cho một SKU. Ba giá trị nhập sai ở dòng 4 (`bad`), 11 (rỗng), 17 (`N/A`). Cần chuyển kiểu để tính tổng **15 đơn giá có số**, giữ danh sách SKU chưa có giá và không dùng 0 đồng làm giá giả định.

**Vì sao chọn cách này?** `pd.to_numeric(errors='coerce')` xử lý chuỗi lỗi bằng NaN để có thể kiểm tra, không làm chương trình dừng; sau đó `notna()` xác định giá thật và `isna()` chỉ ra mã cần sửa.

**Quy trình:**
1. Tạo 18 chuỗi giá có mã P01…P18.
2. Chuyển kiểu theo cột bằng `to_numeric(errors='coerce')`.
3. Đếm dòng hợp lệ/lỗi, in mã lỗi và tổng giá các dòng có số.

```python
import pandas as pd
df = pd.DataFrame({"sku": [f"P{i:02d}" for i in range(1, 19)],
                   "raw_price_vnd": ["50000","55000","60000","bad","70000","75000","80000","85000","90000","95000","","105000","110000","115000","120000","125000","N/A","135000"]})
df["price_vnd"] = pd.to_numeric(df["raw_price_vnd"], errors="coerce")
bad = df["price_vnd"].isna()
assert len(df) == 18
print("SKU:", len(df))
print("Giá hợp lệ:", int((~bad).sum()))
print("Cần sửa:", ", ".join(df.loc[bad, "sku"]))
print("Tổng đơn giá (đồng):", int(df["price_vnd"].sum()))
```

**Kết quả khi chạy:**

```text
SKU: 18
Giá hợp lệ: 15
Cần sửa: P04, P11, P17
Tổng đơn giá (đồng): 1370000
```

Tổng đơn giá không phải doanh thu. Nếu cần doanh thu phải ghép thêm số lượng bán cho từng SKU.

### Tình huống 5 — Cấp 5: Tách 20 hồ sơ train/test trước khi tính trung vị điền khuyết

**Từ vựng trong mục:** **Data leakage** — rò rỉ dữ liệu; **Train/test split** — chia tập; **Imputation** — điền khuyết.

**Tình huống thực tế:** Một đội học máy có **20 hồ sơ giả lập** H01…H20; mỗi người có tuổi (năm), mức chi (nghìn đồng) và nhãn nhóm quan sát. Theo phân chia định trước, **15 hồ sơ đầu dùng tập train**, 5 hồ sơ cuối dùng test. Có hai giá trị thiếu ở train và **một giá trị test đặc biệt lớn**. Cần tính trung vị **chỉ từ train** để điền, áp cùng trung vị đó cho test nếu test thiếu, giữ bản gốc và tuyệt đối không dùng thống kê test để chọn giá trị train.

**Vì sao chọn cách này?** Nếu tính trung vị từ cả 20 người trước khi tách, dữ liệu test đã góp phần quyết định cách xử lý train, gây **data leakage**. Cách đúng là tách trước rồi học thống kê từ train; trong ví dụ này test có giá trị bất thường để nhấn mạnh nguyên tắc.

**Quy trình:**
1. Tạo DataFrame 20 người; tách 15 dòng đầu/5 dòng cuối.
2. Tính median từ `train` trên số hợp lệ, không dùng `test`.
3. Dùng một median cố định điền vào bản train/test, đối chiếu số dòng và giá trị của train.

```python
import pandas as pd
raw = pd.DataFrame({"id": [f"H{i:02d}" for i in range(1, 21)],
                    "age_years": [20,21,22,23,24,25,26,27,20,21,22,23,24,25,26,27,20,21,22,23],
                    "spent_thousand": [100,113,None,139,152,165,178,191,204,None,110,123,136,149,162,175,999,201,214,107]})
train = raw.iloc[:15].copy()
test = raw.iloc[15:].copy()
train_median = train["spent_thousand"].median()
train["spent_thousand"] = train["spent_thousand"].fillna(train_median)
test["spent_thousand"] = test["spent_thousand"].fillna(train_median)
assert len(raw) == len(train) + len(test) == 20
assert raw["spent_thousand"].isna().sum() == 2
print("Hồ sơ:", len(raw))
print("Train:", len(train))
print("Test:", len(test))
print("Thiếu train trước:", 2)
print(f"Trung vị học từ train: {train_median:.1f}")
print("Thiếu sau điền:", int(train["spent_thousand"].isna().sum() + test["spent_thousand"].isna().sum()))
```

**Kết quả khi chạy:**

```text
Hồ sơ: 20
Train: 15
Test: 5
Thiếu train trước: 2
Trung vị học từ train: 149.0
Thiếu sau điền: 0
```

Trung vị của train được tái sử dụng khi xử lý test; bản dữ liệu thô vẫn giữ dấu vết dữ liệu thiếu. Không biến chỉ số từ test thành tham số chọn trong lúc chuẩn bị train.

## 6. Sai lầm thường gặp

- **Thiếu dữ liệu** không đồng nghĩa với 0; điền 0 vào tuổi, giá hay lượng hàng thiếu có thể làm sai thống kê.
- `duplicated()` mặc định xét toàn bộ các cột; xóa trùng phải hiểu **khóa định danh** và ý nghĩa từng bản ghi.
- `drop_duplicates()` thường giữ **index cũ**; cần `reset_index(drop=True)` nếu muốn đánh lại nhãn hàng.
- `to_numeric(errors='coerce')` đổi dữ liệu sai thành NaN, **không tự đoán** giá trị thật.
- Với Machine Learning, chỉ tính trung vị/trung bình để điền từ **tập train**, sau đó áp dụng cho test để tránh data leakage.

## 7. Trắc nghiệm

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a missing value? | Giá trị thiếu là gì?**

A. Replacing missing entries with chosen estimates | Thay ô thiếu bằng giá trị ước lượng đã chọn

B. Checking types and rules before analysis | Kiểm tra kiểu và quy tắc trước khi phân tích

C. An absent or unknown data entry | Ô dữ liệu chưa có giá trị xác định

D. A record repeated under a defined matching rule | Bản ghi lặp theo tiêu chí đối chiếu xác định

**Đáp án: C**

**Giải thích:** Thiếu nghĩa là chưa có giá trị quan sát hợp lệ ở ô đó. Trong Pandas, `NaN` và `None` có thể biểu thị ô thiếu; giá trị thiếu khác một số 0 đã được đo thật.


**Q2. What is a duplicate record? | Bản ghi trùng là gì?**

A. A record repeated under a defined matching rule | Bản ghi lặp theo tiêu chí đối chiếu xác định

B. Checking types and rules before analysis | Kiểm tra kiểu và quy tắc trước khi phân tích

C. An absent or unknown data entry | Ô dữ liệu chưa có giá trị xác định

D. Replacing missing entries with chosen estimates | Thay ô thiếu bằng giá trị ước lượng đã chọn

**Đáp án: A**

**Giải thích:** Nhận diện trùng phụ thuộc các trường dùng làm tiêu chí. Hai hàng cùng mã khách có thể là hai đơn riêng, nên phải xác định tiêu chí trùng trước khi xóa dữ liệu.


**Q3. What is imputation? | Điền khuyết là gì?**

A. An absent or unknown data entry | Ô dữ liệu chưa có giá trị xác định

B. Checking types and rules before analysis | Kiểm tra kiểu và quy tắc trước khi phân tích

C. Replacing missing entries with chosen estimates | Thay ô thiếu bằng giá trị ước lượng đã chọn

D. A record repeated under a defined matching rule | Bản ghi lặp theo tiêu chí đối chiếu xác định

**Đáp án: C**

**Giải thích:** Điền khuyết dùng giá trị lựa chọn chứ không coi đó là dữ liệu đã đo thật. Điền tuổi thiếu bằng trung vị của tập train là phép ước lượng, không chứng minh tuổi thật bằng trung vị đó.


**Q4. What is data validation? | Kiểm tra dữ liệu hợp lệ là gì?**

A. A record repeated under a defined matching rule | Bản ghi lặp theo tiêu chí đối chiếu xác định

B. An absent or unknown data entry | Ô dữ liệu chưa có giá trị xác định

C. Checking types and rules before analysis | Kiểm tra kiểu và quy tắc trước khi phân tích

D. Replacing missing entries with chosen estimates | Thay ô thiếu bằng giá trị ước lượng đã chọn

**Đáp án: C**

**Giải thích:** Kiểm tra hợp lệ phát hiện sai kiểu và giá trị vượt phạm vi. Với trường tuổi, bước kiểm tra có thể yêu cầu giá trị số không âm và loại chuỗi không hợp lệ.


**Q5. What does `isna()` identify? | `isna()` phát hiện gì?**

A. Missing entries | Các ô thiếu

B. Turns invalid numeric text into NaN | Chuyển chữ không đổi được sang số thành NaN

C. Repeated rows after the first occurrence | Các hàng lặp sau lần xuất hiện đầu

D. Replaces missing entries with a value | Thay ô thiếu bằng giá trị cho trước

**Đáp án: A**

**Giải thích:** isna trả mặt nạ Boolean đánh dấu giá trị thiếu. Với `[2, NaN]`, `isna()` đánh dấu `[False, True]`; hàm xác định chỗ thiếu mà không xóa dữ liệu.


**Q6. What does `duplicated()` mark by default? | `duplicated()` mặc định đánh dấu gì?**

A. Turns invalid numeric text into NaN | Chuyển chữ không đổi được sang số thành NaN

B. Repeated rows after the first occurrence | Các hàng lặp sau lần xuất hiện đầu

C. Replaces missing entries with a value | Thay ô thiếu bằng giá trị cho trước

D. Missing entries | Các ô thiếu

**Đáp án: B**

**Giải thích:** duplicated xét toàn hàng nếu không chỉ định subset. Với hai hàng giống nhau, hàng đầu thường nhận `False`, hàng sau nhận `True`; `subset=` thay đổi các cột dùng để xét trùng.


**Q7. What does `fillna(value)` do? | `fillna(value)` làm gì?**

A. Turns invalid numeric text into NaN | Chuyển chữ không đổi được sang số thành NaN

B. Missing entries | Các ô thiếu

C. Repeated rows after the first occurrence | Các hàng lặp sau lần xuất hiện đầu

D. Replaces missing entries with a value | Thay ô thiếu bằng giá trị cho trước

**Đáp án: D**

**Giải thích:** fillna thay ô thiếu mà giữ các giá trị hợp lệ. Với điểm thiếu, `df.fillna(0)` mặc định trả DataFrame đã điền mà không đổi `df` nếu chưa gán kết quả hoặc yêu cầu sửa tại chỗ.


**Q8. What does `pd.to_numeric(..., errors='coerce')` do with invalid text? | `to_numeric(..., errors='coerce')` xử lý chuỗi không phải số thế nào?**

A. Replaces missing entries with a value | Thay ô thiếu bằng giá trị cho trước

B. Turns invalid numeric text into NaN | Chuyển chữ không đổi được sang số thành NaN

C. Repeated rows after the first occurrence | Các hàng lặp sau lần xuất hiện đầu

D. Missing entries | Các ô thiếu

**Đáp án: B**

**Giải thích:** Cơ chế coerce đánh dấu lỗi chuyển kiểu là thiếu chứ không đoán số. Khi đổi kiểu số, chuỗi `'bad'` trở thành dấu thiếu, còn chuỗi hợp lệ như `'12'` được chuyển thành số 12.


**Q9. What does `dropna()` normally remove? | `dropna()` mặc định xóa gì?**

A. Rows containing missing data | Các hàng chứa dữ liệu thiếu

B. The middle value after sorting, or mean of the two middle values | Giá trị giữa khi sắp, hoặc trung bình hai giá trị giữa

C. Raise an exception on invalid input | Báo ngoại lệ khi đầu vào không hợp lệ

D. The first occurrence of each distinct row | Lần xuất hiện đầu của từng hàng khác nhau

**Đáp án: A**

**Giải thích:** DataFrame.dropna mặc định bỏ hàng có ít nhất một ô thiếu. Với DataFrame có ô thiếu, `dropna()` mặc định bỏ hàng chứa ít nhất một ô thiếu; nó không tự điền các ô đó.


**Q10. What does `drop_duplicates()` normally keep? | `drop_duplicates()` thường giữ gì?**

A. The middle value after sorting, or mean of the two middle values | Giá trị giữa khi sắp, hoặc trung bình hai giá trị giữa

B. The first occurrence of each distinct row | Lần xuất hiện đầu của từng hàng khác nhau

C. Rows containing missing data | Các hàng chứa dữ liệu thiếu

D. Raise an exception on invalid input | Báo ngoại lệ khi đầu vào không hợp lệ

**Đáp án: B**

**Giải thích:** Mặc định các lần lặp sau của cùng hàng sẽ bị bỏ. Với các hàng A, A, B, mặc định giữ A đầu và B, không giữ A cuối trừ khi đặt `keep='last'`.


**Q11. What is the median? | Trung vị là gì?**

A. Raise an exception on invalid input | Báo ngoại lệ khi đầu vào không hợp lệ

B. The first occurrence of each distinct row | Lần xuất hiện đầu của từng hàng khác nhau

C. Rows containing missing data | Các hàng chứa dữ liệu thiếu

D. The middle value after sorting, or mean of the two middle values | Giá trị giữa khi sắp, hoặc trung bình hai giá trị giữa

**Đáp án: D**

**Giải thích:** Trung vị ít nhạy với giá trị cực đoan hơn trung bình cộng. Với dãy đã sắp `[1,2,100]`, trung vị là 2 còn trung bình lớn hơn 34; nếu số phần tử chẵn thì lấy trung bình hai số ở giữa.


**Q12. What is the meaning of `errors='raise'` in numeric conversion? | `errors='raise'` khi đổi sang số có nghĩa gì?**

A. Rows containing missing data | Các hàng chứa dữ liệu thiếu

B. The middle value after sorting, or mean of the two middle values | Giá trị giữa khi sắp, hoặc trung bình hai giá trị giữa

C. The first occurrence of each distinct row | Lần xuất hiện đầu của từng hàng khác nhau

D. Raise an exception on invalid input | Báo ngoại lệ khi đầu vào không hợp lệ

**Đáp án: D**

**Giải thích:** Raise làm lỗi lộ rõ thay vì chuyển âm thầm thành thiếu. Dùng `pd.to_numeric(['bad'], errors='raise')` báo lỗi, còn `errors='coerce'` trả dấu giá trị số bị thiếu.


**Q13. What is data leakage in train/test preprocessing? | Data leakage khi chuẩn bị train/test là gì?**

A. Zero may have a different real-world meaning | Số 0 có thể mang ý nghĩa thực tế khác

B. To audit and reverse cleaning decisions | Để đối chiếu và phục hồi quyết định xử lý

C. Records with shared IDs may still represent distinct events | Hai dòng cùng ID vẫn có thể là sự kiện khác nhau

D. Using information from test data while fitting preprocessing | Dùng thông tin của test khi học tham số tiền xử lý

**Đáp án: D**

**Giải thích:** Thống kê tiền xử lý phải học chỉ từ tập train. Tính trung vị điền khuyết trên cả train và test làm thông tin của tập đánh giá lọt vào giai đoạn chuẩn bị mô hình.


**Q14. Why is replacing every missing value with zero risky? | Vì sao thay mọi ô thiếu bằng 0 là rủi ro?**

A. To audit and reverse cleaning decisions | Để đối chiếu và phục hồi quyết định xử lý

B. Using information from test data while fitting preprocessing | Dùng thông tin của test khi học tham số tiền xử lý

C. Zero may have a different real-world meaning | Số 0 có thể mang ý nghĩa thực tế khác

D. Records with shared IDs may still represent distinct events | Hai dòng cùng ID vẫn có thể là sự kiện khác nhau

**Đáp án: C**

**Giải thích:** Tuổi chưa nhập không tự đồng nghĩa tuổi bằng 0. Số lượng hàng thiếu nghĩa là chưa biết, còn số lượng 0 nói rõ không có món nào; thay hai trường hợp cho nhau sẽ đổi ý nghĩa.


**Q15. Why check key columns before removing duplicates? | Vì sao phải xem cột khóa trước khi xóa trùng?**

A. Records with shared IDs may still represent distinct events | Hai dòng cùng ID vẫn có thể là sự kiện khác nhau

B. Using information from test data while fitting preprocessing | Dùng thông tin của test khi học tham số tiền xử lý

C. Zero may have a different real-world meaning | Số 0 có thể mang ý nghĩa thực tế khác

D. To audit and reverse cleaning decisions | Để đối chiếu và phục hồi quyết định xử lý

**Đáp án: A**

**Giải thích:** Quy tắc nghiệp vụ xác định hai dòng có thực sự trùng không. Hai giao dịch của cùng khách hàng có thể là hai sự kiện hợp lệ khác nhau dù trùng một mã định danh.


**Q16. Why preserve the original raw data while cleaning? | Vì sao nên giữ dữ liệu gốc khi làm sạch?**

A. Zero may have a different real-world meaning | Số 0 có thể mang ý nghĩa thực tế khác

B. To audit and reverse cleaning decisions | Để đối chiếu và phục hồi quyết định xử lý

C. Records with shared IDs may still represent distinct events | Hai dòng cùng ID vẫn có thể là sự kiện khác nhau

D. Using information from test data while fitting preprocessing | Dùng thông tin của test khi học tham số tiền xử lý

**Đáp án: B**

**Giải thích:** Bản gốc giúp kiểm tra từng phép biến đổi. Giữ bản nguồn không đổi giúp so sánh trước/sau và xem xét lại các quyết định làm sạch chưa đúng.


**Q17. What does a Boolean missing-value mask contain? | Mặt nạ dữ liệu thiếu chứa gì?**

A. True and False values | Các giá trị True và False

B. Original retained-row labels remain | Nhãn index của hàng được giữ vẫn còn

C. Choose a justified missing-data treatment | Chọn cách xử lý dữ liệu thiếu có cơ sở

D. Rebuilds sequential indices without retaining old index as a column | Đánh lại index tuần tự, không giữ index cũ thành cột

**Đáp án: A**

**Giải thích:** Mỗi vị trí cho biết ô dữ liệu có thiếu hay không. Một ô mask là `True` nếu đầu vào tương ứng bị thiếu và `False` nếu không; mask không phải danh sách giá trị thay thế.


**Q18. What happens to index labels after `drop_duplicates()` by default? | Sau `drop_duplicates()`, index mặc định thay đổi thế nào?**

A. True and False values | Các giá trị True và False

B. Choose a justified missing-data treatment | Chọn cách xử lý dữ liệu thiếu có cơ sở

C. Rebuilds sequential indices without retaining old index as a column | Đánh lại index tuần tự, không giữ index cũ thành cột

D. Original retained-row labels remain | Nhãn index của hàng được giữ vẫn còn

**Đáp án: D**

**Giải thích:** Xóa hàng trùng không tự đánh lại index cho hàng còn lại. Xóa các hàng mang nhãn 1 và 3 không tự đánh lại nhãn còn lại; phải reset index riêng nếu muốn nhãn liên tiếp.


**Q19. What does `reset_index(drop=True)` do? | `reset_index(drop=True)` làm gì?**

A. Original retained-row labels remain | Nhãn index của hàng được giữ vẫn còn

B. Choose a justified missing-data treatment | Chọn cách xử lý dữ liệu thiếu có cơ sở

C. Rebuilds sequential indices without retaining old index as a column | Đánh lại index tuần tự, không giữ index cũ thành cột

D. True and False values | Các giá trị True và False

**Đáp án: C**

**Giải thích:** Đánh lại nhãn hàng giúp bảng đã xử lý dễ đọc hơn. Sau khi bỏ hàng, `reset_index(drop=True)` tạo nhãn `0,1,2,...` mà không đưa index cũ thành cột mới.


**Q20. What should happen after coercing invalid numeric text to NaN? | Sau khi chuyển chuỗi số sai thành NaN cần làm gì?**

A. Rebuilds sequential indices without retaining old index as a column | Đánh lại index tuần tự, không giữ index cũ thành cột

B. Choose a justified missing-data treatment | Chọn cách xử lý dữ liệu thiếu có cơ sở

C. Original retained-row labels remain | Nhãn index của hàng được giữ vẫn còn

D. True and False values | Các giá trị True và False

**Đáp án: B**

**Giải thích:** Coerce phát hiện lỗi, không khôi phục được giá trị thực chưa biết. Sau khi coerce, hãy đếm số ô bị thiếu rồi quyết định loại bỏ, từ chối hay điền khuyết theo yêu cầu bài toán.

## 8. Nối bài tiếp theo

`DataFrame → Data Cleaning → EDA → ML Pipeline`.
