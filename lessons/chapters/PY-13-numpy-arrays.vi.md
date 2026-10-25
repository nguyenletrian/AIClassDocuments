# PY-13 — NumPy ndarray, shape, dtype và axis


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **ndarray** — mảng NumPy; **Shape** — kích thước mảng.

`List → NumPy Array → Matrix → PCA`

**Học xong dùng để làm gì?** Biểu diễn dữ liệu số trong mảng có shape và dtype, tính tổng/trung bình theo chiều dữ liệu.

**Kết nối kiến thức tiếp theo:** PY-14 chọn hàng, cột hoặc phần tử thỏa ngưỡng trong mảng.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| ndarray | mảng NumPy | Một mảng đồng nhất về kiểu phần tử |
| Shape | kích thước mảng | Số phần tử trên từng chiều |
| dtype | kiểu phần tử | Kiểu dữ liệu của giá trị trong mảng |
| Axis | trục tính toán | Chiều dọc theo phép tổng hợp |

## 3. Thư viện, hàm và tham số

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm/cú pháp | Giải thích và lý do dùng |
|---|---|
| `np.array(data,dtype=float)` | Tạo mảng số thực, dtype=float cho phép lưu phần thập phân |
| `X.shape/X.ndim/X.size` | Xem hàng/cột, số chiều, số phần tử |
| `X.mean(axis=0)` | Tính trung bình của từng CỘT từ các hàng |
| `np.zeros()/np.ones()` | Tạo dữ liệu số được khởi tạo rõ hình dạng |

## 4. Khái niệm liên quan

**NumPy ndarray** là công cụ lưu số liệu có cấu trúc. Một bảng có 3 học viên × 2 môn sẽ xuyên suốt phần khái niệm: từ tạo bảng, xem kích thước, hiểu kiểu phần tử cho tới tính toán theo cột. Nhờ giữ nguyên ý nghĩa hàng và cột, kết quả thống kê sẽ không bị hiểu nhầm.

### 4.1. ndarray — Mảng số cho nhiều học viên

**Từ vựng trong mục:** **ndarray** — mảng NumPy; **Element** — phần tử.

**NumPy** là thư viện hỗ trợ tính toán trên nhiều số cùng lúc. Kiểu dữ liệu chính là `ndarray` — một **mảng nhiều chiều**. Ví dụ trung tâm có ba học viên An, Bình, Lan (theo thứ tự ba hàng) và hai môn Toán, Python (theo thứ tự hai cột). Các điểm `[8,9]`, `[6,7]`, `[9,8]` nằm cùng một bảng. **Mỗi hàng** là một người, **mỗi cột** là một môn, **mỗi ô** là điểm của người đó ở môn đó trên thang 10.

```python
# Mục đích: Mảng số cho nhiều học viên.
import numpy as np

scores = np.array([
    [8, 9],
    [6, 7],
    [9, 8],
])
print(scores)
```

**Kết quả khi chạy:**

```text
[[8 9]
 [6 7]
 [9 8]]
```

Hàng đầu là điểm của An, hàng thứ hai của Bình, hàng thứ ba của Lan; hai số trên một hàng lần lượt thuộc hai môn.

### 4.2. Shape — Kích thước của mảng

**Từ vựng trong mục:** **Shape** — kích thước; **Row/column** — hàng/cột.

Thuộc tính `shape` cho biết **số phần tử ở từng chiều** của mảng. Với bảng điểm ba học viên, hai môn, `shape == (3, 2)`: con số 3 là **số hàng/học viên**, con số 2 là **số cột/môn**. Thuộc tính `size` là số ô dữ liệu (3 × 2 = 6), còn `ndim` là số chiều (2). Không nhầm mảng `(3,2)` với ba môn của hai học viên.

```python
# Mục đích: Kích thước của mảng.
import numpy as np

scores = np.array([[8, 9], [6, 7], [9, 8]])
print(scores.shape, scores.size)
```

**Kết quả khi chạy:**

```text
(3, 2) 6
```

Bảng có 3 người × 2 môn = 6 giá trị điểm; đây là mảng hai chiều.

### 4.3. dtype — Kiểu của các phần tử

**Từ vựng trong mục:** **dtype** — kiểu dữ liệu phần tử; **Float** — số thực.

Một `ndarray` thông thường lưu các phần tử bằng một kiểu dữ liệu chung (`dtype`). Với điểm có phần thập phân như 8,5, ta dùng `dtype=float` khi tạo mảng để giữ phần lẻ và thuận tiện tính trung bình. NumPy trên môi trường thông dụng dùng `float64` cho lựa chọn `float`. Ngược lại, nếu ép điểm thập phân thành số nguyên, phần lẻ có thể mất.

```python
# Mục đích: Kiểu của các phần tử.
import numpy as np

scores = np.array([8.5, 7.0], dtype=float)
print(scores.dtype, scores.size)
```

**Kết quả khi chạy:**

```text
float64 2
```

Mảng có hai điểm dạng số thực; `8.5` được giữ chứ không bị cắt thành `8`.

### 4.4. Axis — Tính theo hàng hoặc cột

**Từ vựng trong mục:** **Axis** — trục tính toán; **Mean** — trung bình.

Khi tổng hợp dữ liệu hai chiều, **`axis=0` gom các hàng để cho ra một kết quả trên mỗi cột**; **`axis=1` gom các cột để cho ra một kết quả trên mỗi hàng**. Trong bảng ba học viên × hai môn, `scores.mean(axis=0)` tính điểm trung bình **từng môn**: môn Toán `(8+6+9)/3 ≈ 7,67`, môn Python `(9+7+8)/3 = 8`. Nếu đổi sang `axis=1`, sẽ ra ba điểm trung bình tương ứng ba học viên.

```python
# Mục đích: Tính theo hàng hoặc cột.
import numpy as np

scores = np.array([[8, 9], [6, 7], [9, 8]], dtype=float)
print(scores.mean(axis=0))
```

**Kết quả khi chạy:**

```text
[7.66666667 8.        ]
```

Mảng đầu ra có hai số vì bảng có hai **cột/môn**; kết quả lần lượt là trung bình Toán và Python.

## 5. Năm tình huống NumPy Array — tăng từ shape đến dữ liệu nhiều cột

### Tình huống 1 — Cấp 1: Tạo bảng điểm 10 học viên có hai cột

**Từ vựng trong mục:** **ndarray** — mảng NumPy; **Shape** — hình dạng; **dtype** — kiểu phần tử.

**Tình huống thực tế:** Trung tâm lưu **10 hàng** học viên H01…H10, mỗi hàng có điểm Toán và Python (thang 10). Cần biết số người, số môn và kiểu phần tử, không nhầm 20 ô với 20 học viên.

**Vì sao chọn cách này?** `np.array(..., dtype=float)` chuyển bảng số thành mảng đồng nhất; `shape` mô tả số hàng/cột, `size` đếm tổng ô và `dtype.kind` cho biết phần tử dạng số thực.

**Quy trình:**
1. Ghi 10 dòng điểm theo đúng thứ tự hai môn.
2. Tạo ndarray kiểu số thực với NumPy.
3. Đọc `shape`, `size` và kiểu phần tử.

```python
import numpy as np
rows = [[8,9],[7,8],[9,10],[6,7],[8,7],[5,8],[9,9],[7,6],[10,8],[8,9]]
scores = np.array(rows, dtype=float)
if scores.shape != (10, 2):
    raise ValueError("Bảng phải có đúng 10 học viên và 2 môn.")
print("Số học viên:", scores.shape[0])
print("Số môn:", scores.shape[1])
print("Số ô:", scores.size)
print("Kiểu số thực:", scores.dtype.kind == "f")
```

**Kết quả khi chạy:**

```text
Số học viên: 10
Số môn: 2
Số ô: 20
Kiểu số thực: True
```

Một hàng đại diện cho một học viên; `dtype=float` cho phép mở rộng với điểm có phần thập phân dù dữ liệu ban đầu chỉ ghi số nguyên.

### Tình huống 2 — Cấp 2: Trung bình doanh thu ba loại hàng trong 12 ngày

**Từ vựng trong mục:** **Axis** — trục tổng hợp; **Mean** — trung bình.

**Tình huống thực tế:** Cửa hàng ghi doanh thu **12 ngày**, mỗi hàng tương ứng một ngày, ba cột là thực phẩm, sách, đồ dùng (nghìn đồng). Người quản lý cần doanh thu trung bình **cho từng loại hàng qua 12 ngày**, không phải trung bình của mỗi ngày.

**Vì sao chọn cách này?** Trong mảng `(12, 3)`, `mean(axis=0)` gom các hàng theo từng cột, cho ra ba số. Nếu chọn `axis=1`, kết quả có 12 số — trả lời câu hỏi khác.

**Quy trình:**
1. Tạo bảng 12 hàng × 3 cột đúng đơn vị.
2. Chọn `axis=0` để tổng hợp theo loại hàng.
3. In ba giá trị theo nhãn đã định và xác nhận shape đầu ra.

```python
import numpy as np
sales = np.array([[10,20,30],[11,21,31],[12,22,32],[13,23,33],[14,24,34],[15,25,35],[16,26,36],[17,27,37],[18,28,38],[19,29,39],[20,30,40],[21,31,41]], dtype=float)
average = sales.mean(axis=0)
if sales.shape != (12, 3) or average.shape != (3,):
    raise ValueError("Bảng bán hàng phải có 12 ngày, 3 nhóm.")
print("Ngày:", sales.shape[0])
print("Thực phẩm:", f"{average[0]:.1f}")
print("Sách:", f"{average[1]:.1f}")
print("Đồ dùng:", f"{average[2]:.1f}")
```

**Kết quả khi chạy:**

```text
Ngày: 12
Thực phẩm: 15.5
Sách: 25.5
Đồ dùng: 35.5
```

Mỗi kết quả là mức trung bình ngày của **một cột** (nghìn đồng/ngày), không phải tổng doanh thu mười hai ngày.

### Tình huống 3 — Cấp 3: Tổng doanh thu hai ca cho 15 cửa hàng

**Từ vựng trong mục:** **Axis=1** — tổng theo hàng; **argmax** — vị trí lớn nhất; **ndim** — số chiều.

**Tình huống thực tế:** Chuỗi bán lẻ có **15 cửa hàng** S01…S15. Một hàng gồm doanh thu ca sáng và ca chiều (nghìn đồng). Giám sát cần cộng hai ca **cho từng cửa hàng**, rồi tìm mã cửa hàng có tổng cao nhất.

**Vì sao chọn cách này?** `sum(axis=1)` gộp các cột ca trong từng hàng; `argmax()` cho chỉ số hàng có tổng lớn nhất. `axis=0` sẽ cộng theo ca trên toàn bộ cửa hàng, không giải quyết yêu cầu.

**Quy trình:**
1. Tạo ndarray `(15,2)`; hàng là cửa hàng, cột là ca.
2. Gọi `sum(axis=1)` để ra 15 tổng riêng.
3. Dùng `argmax()` và chuyển chỉ số bắt đầu từ 0 thành mã cửa hàng.

```python
import numpy as np
sales = np.array([[50,30],[52,31],[54,32],[56,33],[58,34],[60,35],[62,36],[64,37],[66,38],[68,39],[70,40],[72,41],[74,42],[76,43],[78,44]], dtype=int)
per_store = sales.sum(axis=1)
peak = int(per_store.argmax())
if sales.shape != (15, 2):
    raise ValueError("Bảng phải có 15 cửa hàng và 2 nhóm doanh thu.")
print("Cửa hàng:", sales.shape[0])
print("Tổng S01 (nghìn đồng):", int(per_store[0]))
print("Cửa hàng cao nhất:", f"S{peak+1:02d}")
print("Doanh thu cao nhất:", int(per_store[peak]))
```

**Kết quả khi chạy:**

```text
Cửa hàng: 15
Tổng S01 (nghìn đồng): 80
Cửa hàng cao nhất: S15
Doanh thu cao nhất: 122
```

Mảng tổng có 15 phần tử, bằng số cửa hàng; giá trị trong mỗi phần tử là tổng **hai ca cùng một cửa hàng**.

### Tình huống 4 — Cấp 4: Kiểm tra shape/dtype của 18 số đo có dữ liệu thiếu

**Từ vựng trong mục:** **NaN** — giá trị số thiếu; **np.isnan** — kiểm tra NaN; **np.nanmean** — trung bình bỏ qua NaN.

**Tình huống thực tế:** Trạm đo ghi **18 lượt**, mỗi hàng gồm nhiệt độ °C và độ ẩm % trong hai cột. Độ ẩm của lượt thứ 6 và 15 bị thiếu (`None`), nhưng nhiệt độ ở hai lượt đó vẫn được ghi. Cần đếm đúng giá trị thiếu ở cột độ ẩm và lấy trung bình độ ẩm từ các lượt có số, không đưa giá trị thiếu vào như 0%.

**Vì sao chọn cách này?** NumPy mảng số thực không lưu `None` như số đo; minh họa chuyển `None` thành `np.nan` rồi dùng `np.isnan` và `np.nanmean`. Tách từng cột giúp không bỏ nhiệt độ tốt chỉ vì độ ẩm thiếu.

**Quy trình:**
1. Tạo 18 cặp đo với `np.nan` ở đúng ô độ ẩm thiếu.
2. Kiểm tra shape `(18,2)` và mặt nạ NaN trên cột thứ hai.
3. Tính trung bình chỉ các giá trị độ ẩm không phải NaN.

```python
import numpy as np
raw = [[24,50],[24.25,51],[24.5,52],[24.75,53],[25,54],[25.25,None],[25.5,56],[25.75,57],[26,58],[26.25,59],[26.5,60],[26.75,61],[27,62],[27.25,63],[27.5,None],[27.75,65],[28,66],[28.25,67]]
rows = []
for temperature, humidity in raw:
    if humidity is None:
        cleaned_humidity = np.nan
    else:
        cleaned_humidity = humidity
    rows.append((temperature, cleaned_humidity))
measurements = np.array(rows, dtype=float)
missing = np.isnan(measurements[:, 1])
if measurements.shape != (18, 2):
    raise ValueError("Cần đủ 18 lượt đo, mỗi lượt hai giá trị.")
print("Lượt đo:", measurements.shape[0])
print("Thiếu độ ẩm:", int(missing.sum()))
print("Nhiệt độ vẫn đủ:", int(np.isfinite(measurements[:, 0]).sum()))
print(f"Độ ẩm trung bình: {np.nanmean(measurements[:, 1]):.2f} %")
```

**Kết quả khi chạy:**

```text
Lượt đo: 18
Thiếu độ ẩm: 2
Nhiệt độ vẫn đủ: 18
Độ ẩm trung bình: 58.38 %
```

Ở đây `np.nan` được dùng để **biểu diễn số đo thiếu**, không phải độ ẩm bằng 0. Trường hợp cột toàn NaN cần quy tắc riêng trước khi tính trung bình.

### Tình huống 5 — Cấp 5: Chuẩn hóa báo cáo 20 ngày: số đo, trục và thiếu dữ liệu

**Từ vựng trong mục:** **Shape validation** — kiểm hình dạng; **dtype** — kiểu mảng; **Axis=0** — tổng hợp từng cột.

**Tình huống thực tế:** Nhóm nghiên cứu có **20 ngày quan sát giả lập**; mỗi ngày là một hàng gồm giờ ngủ (giờ), thời gian vận động (phút) và nhịp tim nghỉ (nhịp/phút). Có **hai ngày** không đo nhịp tim, nhưng giờ ngủ và vận động vẫn có. Cần kiểm tra 20 hàng × 3 cột, tính trung bình từng chỉ số trên dữ liệu hợp lệ và báo số đo tim thiếu trước khi đưa số liệu sang bài chọn hàng/cột.

**Vì sao chọn cách này?** Kết hợp mảng `float`, `np.nan`, kiểm tra shape và `np.nanmean(axis=0)` đảm bảo thống kê chạy theo ba cột có đơn vị khác nhau mà không nhầm cột hoặc coi dòng thiếu là 0. Đây là kiểm định bảng đầu vào, chưa kết luận sức khỏe.

**Quy trình:**
1. Lưu 20 bộ ba giá trị, chuyển ô nhịp tim thiếu thành NaN.
2. Kiểm tra shape, các đơn vị/kiểu số và số ô NaN ở cột tim.
3. Tổng hợp theo `axis=0` và in ba trung bình có nhãn/đơn vị.

```python
import numpy as np
raw = [[6,40,60],[7,43,62],[8,46,64],[9,49,None],[10,52,68],[6,55,70],[7,58,72],[8,41,74],[9,44,76],[10,47,78],[6,50,80],[7,53,82],[8,56,84],[9,59,61],[10,42,63],[6,45,65],[7,48,67],[8,51,None],[9,54,71],[10,57,73]]
records = []
for sleep, movement, heart in raw:
    if heart is None:
        cleaned_heart = np.nan
    else:
        cleaned_heart = heart
    records.append([sleep, movement, cleaned_heart])
data = np.array(records, dtype=float)
if data.shape != (20, 3) or data.dtype.kind != "f":
    raise ValueError("Cần đủ 20 ngày, ba cột dữ liệu dạng số thực.")
means = np.nanmean(data, axis=0)
print("Số ngày:", data.shape[0])
print("Số cột:", data.shape[1])
print("Thiếu nhịp tim:", int(np.isnan(data[:, 2]).sum()))
print(f"Ngủ (giờ): {means[0]:.2f}")
print(f"Vận động (phút): {means[1]:.2f}")
print(f"Nhịp tim (nhịp/phút): {means[2]:.2f}")
```

**Kết quả khi chạy:**

```text
Số ngày: 20
Số cột: 3
Thiếu nhịp tim: 2
Ngủ (giờ): 8.00
Vận động (phút): 49.50
Nhịp tim (nhịp/phút): 70.56
```

Mỗi cột có **đơn vị và ý nghĩa riêng**; không cộng ba cột để thành một chỉ số duy nhất. Đây là dữ liệu minh họa, không dùng để chẩn đoán.

## 6. Sai lầm thường gặp

- `shape=(3,2)` là **3 hàng và 2 cột**, không phải ngược lại; phải ghi rõ mỗi hàng/cột đại diện điều gì.
- `axis=0` tổng hợp theo từng cột trong mảng hai chiều; `axis=1` tổng hợp theo từng hàng. Chọn nhầm trục khiến ý nghĩa kết quả khác đi.
- `dtype=float` giữ phần thập phân, còn kiểu số nguyên có thể cắt phần lẻ nếu ép dữ liệu không phù hợp.
- Kết quả trung bình là số thực; các chữ số cuối có thể phụ thuộc biểu diễn dấu phẩy động, nên giải thích bằng giá trị gần đúng khi cần.
- `np.zeros()` chỉ tạo giá trị khởi tạo 0; không được diễn giải là dự báo thực tế đã được mô hình tính.

## 7. Trắc nghiệm

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a NumPy `ndarray`? | `ndarray` của NumPy là gì?**

A. A class inheritance rule | Quy tắc kế thừa lớp

B. A Python exception | Một ngoại lệ Python

C. A single text file | Một tệp văn bản đơn

D. An array for data with a common dtype | Mảng dữ liệu có kiểu phần tử chung

**Đáp án: D**

**Giải thích:** `ndarray` lưu phần tử theo một hay nhiều chiều có chỉ số và một `dtype` chung. Ví dụ `np.array([1, 2, 3])` là mảng số một chiều, không phải tệp hay ngoại lệ Python.


**Q2. What does `shape=(3, 2)` mean for a 2-D array? | `shape=(3, 2)` nghĩa là gì với mảng hai chiều?**

A. Only three total elements | Chỉ có ba phần tử

B. Three rows and two columns | Ba hàng và hai cột

C. Two rows and three columns | Hai hàng và ba cột

D. Three dimensions and two values | Ba chiều và hai giá trị

**Đáp án: B**

**Giải thích:** Với mảng hai chiều, `shape` ghi `(số_hàng, số_cột)`. Vì vậy `(3, 2)` là ba quan sát ở các hàng và hai đặc trưng ở các cột, tổng cộng sáu ô dữ liệu.


**Q3. What is the size of an array with shape `(3, 2)`? | Mảng có shape `(3, 2)` chứa bao nhiêu phần tử?**

A. 5 | 5

B. 6 | 6

C. 3 | 3

D. 2 | 2

**Đáp án: B**

**Giải thích:** `size` của ndarray đếm toàn bộ phần tử và bằng tích các kích thước trong `shape`. Với `(3, 2)`, tính `3 × 2 = 6`; cộng hai kích thước lại sẽ cho số phần tử sai.


**Q4. What does `ndim` report? | Thuộc tính `ndim` cho biết gì?**

A. The data type of an element | Kiểu phần tử

B. The number of rows only | Chỉ số hàng

C. The number of array dimensions | Số chiều của mảng

D. The maximum array value | Giá trị lớn nhất

**Đáp án: C**

**Giải thích:** `ndim` cho số trục/chiều, không phải số giá trị được lưu. Ma trận có shape `(3, 2)` có `ndim == 2` dù `size == 6`.


**Q5. What does `dtype` describe? | `dtype` mô tả gì?**

A. The file's extension | Phần mở rộng của file

B. The data type of array elements | Kiểu dữ liệu của các phần tử

C. The mean of all entries | Trung bình các phần tử

D. The array's row count | Số hàng

**Đáp án: B**

**Giải thích:** `dtype` mô tả kiểu và cách biểu diễn chung của các phần tử mảng, như `int64` hoặc `float64`. Nó khác `shape`, vốn cho biết số phần tử trên từng trục.


**Q6. Why specify `dtype=float` when storing decimal scores? | Vì sao dùng `dtype=float` khi lưu điểm có phần lẻ?**

A. To preserve fractional values | Để giữ giá trị có phần thập phân

B. To force integer truncation | Để ép cắt về số nguyên

C. To delete missing records | Để xóa bản ghi thiếu

D. To change rows into columns | Để đổi hàng thành cột

**Đáp án: A**

**Giải thích:** `dtype=float` yêu cầu NumPy lưu giá trị dưới dạng dấu phẩy động để điểm như `8.5` giữ được phần lẻ. Nếu đổi sang kiểu nguyên, phần lẻ có thể bị bỏ trong quá trình chuyển kiểu.


**Q7. For a 2-D array, what does `mean(axis=0)` return? | Với mảng hai chiều, `mean(axis=0)` trả về gì?**

A. Only the first cell | Chỉ ô đầu tiên

B. One mean per column | Một giá trị trung bình cho mỗi cột

C. The original array unchanged | Mảng gốc không đổi

D. One mean per row | Một giá trị trung bình cho mỗi hàng

**Đáp án: B**

**Giải thích:** Với mảng 2D, `axis=0` gộp theo chiều hàng và để lại một kết quả cho từng cột. Với `[[1, 3], [5, 7]]`, `mean(axis=0)` được `[3., 5.]`, không phải các trung bình theo hàng.


**Q8. For a 2-D array, what does `sum(axis=1)` produce? | Với mảng hai chiều, `sum(axis=1)` tạo gì?**

A. A list of column names | List tên cột

B. The shape tuple only | Chỉ tuple shape

C. One sum per column | Một tổng cho mỗi cột

D. One sum per row | Một tổng cho mỗi hàng

**Đáp án: D**

**Giải thích:** `sum(axis=1)` cộng các cột trong từng hàng. Với `[[1, 3], [5, 7]]`, tổng theo hàng là `4` và `12`, tạo kết quả một chiều gồm hai giá trị.


**Q9. Which statement correctly distinguishes `shape` and `size`? | Đâu là điểm khác nhau giữa `shape` và `size`?**

A. shape lists dimensions; size counts elements | shape ghi kích thước từng chiều; size đếm phần tử

B. size gives dtype; shape gives values | size cho kiểu dữ liệu; shape cho giá trị

C. They are always identical numbers | Chúng luôn là cùng một số

D. Both change elements automatically | Cả hai tự đổi phần tử

**Đáp án: A**

**Giải thích:** `shape` là tuple chỉ độ dài từng chiều, còn `size` là một số đếm toàn bộ phần tử. Mảng có shape `(3, 2)` gồm hai chiều và `size == 6`; hai thuộc tính này không tự sắp xếp lại dữ liệu.


**Q10. What does `np.array([1, 2, 3])` create? | `np.array([1, 2, 3])` tạo ra gì?**

A. A one-dimensional NumPy array | Một mảng NumPy một chiều

B. A class named Array | Lớp tên Array

C. A CSV file on disk | File CSV trên đĩa

D. A two-column table | Bảng hai cột

**Đáp án: A**

**Giải thích:** `np.array([1, 2, 3])` tạo ndarray có shape `(3,)`, nghĩa là một chiều chứa ba phần tử. Đây không phải bảng hai cột, vì bảng đó cần cấu trúc hai chiều.


**Q11. What does `np.zeros((2, 3))` create? | `np.zeros((2, 3))` tạo gì?**

A. A 2×3 table of missing strings | Bảng 2×3 gồm chuỗi thiếu

B. A 3×2 array of ones | Mảng 3×2 toàn số 1

C. A 2×3 array initialized to zeros | Mảng 2×3 được khởi tạo toàn số 0

D. An empty array with no elements | Mảng rỗng không có phần tử

**Đáp án: C**

**Giải thích:** `np.zeros((2, 3))` tạo hai hàng và ba cột, mọi ô khởi tạo bằng không. Mặc định các ô thuộc kiểu số thực, không phải chuỗi thiếu dữ liệu hay mảng không có phần tử.


**Q12. How is `np.ones((2, 2))` different from `np.zeros((2, 2))`? | `np.ones((2, 2))` khác `np.zeros((2, 2))` thế nào?**

A. It has four dimensions | Nó có bốn chiều

B. It cannot be used in arithmetic | Nó không thể tính toán

C. It always creates a CSV file | Nó luôn tạo file CSV

D. It initializes entries to one instead of zero | Nó khởi tạo giá trị 1 thay cho 0

**Đáp án: D**

**Giải thích:** `np.ones((2, 2))` và `np.zeros((2, 2))` cùng shape và có bốn ô số. Hàm thứ nhất điền `1`, hàm thứ hai điền `0`; không hàm nào tạo bốn chiều.


**Q13. How do NumPy array and Python List differ in numeric operations? | Mảng NumPy khác List Python về phép toán số như thế nào?**

A. A NumPy array stores only strings | Mảng NumPy chỉ lưu chuỗi

B. A List always multiplies elements element-wise | List luôn nhân từng phần tử

C. A List cannot hold numbers | List không chứa được số

D. NumPy enables element-wise numerical operations | NumPy hỗ trợ phép toán số theo từng phần tử

**Đáp án: D**

**Giải thích:** Với ndarray số, `a * 2` nhân từng phần tử lên hai: `[1, 2]` thành `[2, 4]`. Ngược lại, `[1, 2] * 2` của List Python lặp dãy thành `[1, 2, 1, 2]`.


**Q14. For an array with rows as learners and columns as subjects, what does axis=0 average? | Nếu hàng là học viên và cột là môn, `axis=0` tính trung bình theo gì?**

A. Only the last subject | Chỉ môn cuối

B. Each learner across subjects | Từng học viên qua các môn

C. Each subject across learners | Từng môn qua các học viên

D. Only the first learner | Chỉ học viên đầu

**Đáp án: C**

**Giải thích:** Nếu mỗi hàng là một học viên và mỗi cột là một môn, `mean(axis=0)` tính trung bình qua các học viên cho từng môn riêng. Có hai môn thì được hai trung bình; `axis=1` lại tính trung bình các môn của từng học viên.


**Q15. How many dimensions does a two-dimensional score table have? | Bảng điểm hai chiều có `ndim` bằng bao nhiêu?**

A. The total number of scores | Tổng số điểm

B. 3 | 3

C. 2 | 2

D. 1 | 1

**Đáp án: C**

**Giải thích:** Bảng điểm sắp theo hàng và cột có hai trục, dù có bao nhiêu hàng. Vì vậy `ndim` bằng `2`; tổng số ô điểm cần đọc từ `size`.


**Q16. Which code accesses array shape without computing new values? | Cú pháp nào lấy shape mà không tính thêm dữ liệu?**

A. `X.sort()` | `X.sort()`

B. `X.shape` | `X.shape`

C. `X.delete()` | `X.delete()`

D. `X.write()` | `X.write()`

**Đáp án: B**

**Giải thích:** `X.shape` đọc thuộc tính ndarray, trả tuple kích thước các chiều mà không sửa giá trị. Với bảng ba hàng hai cột, kết quả là `(3, 2)`; `X.sort()` thì thay đổi thứ tự phần tử.


**Q17. Which code counts all array entries? | Cú pháp nào đếm tổng số phần tử mảng?**

A. `X.shape[0]` in every case | Luôn `X.shape[0]`

B. `X.dtype` | `X.dtype`

C. `X.size` | `X.size`

D. `X.mean()` | `X.mean()`

**Đáp án: C**

**Giải thích:** `X.size` đếm phần tử qua toàn bộ các chiều. Với mảng `(3, 2)`, kết quả là `6`, còn `X.shape[0]` chỉ trả số hàng là `3`.


**Q18. For finite floating-point values within the target integer range, what does NumPy `.astype(int)` do to their fractional parts? | Với giá trị dấu phẩy động hữu hạn nằm trong phạm vi kiểu số nguyên đích, NumPy `.astype(int)` xử lý phần lẻ thế nào?**

A. It discards fractional parts toward zero | Bỏ phần lẻ theo hướng về số 0

B. It rounds every value to the nearest integer | Làm tròn mọi giá trị về số nguyên gần nhất

C. It preserves fractional parts unchanged | Giữ nguyên toàn bộ phần lẻ

D. It forces the shape to become `(1, 1)` | Buộc shape chuyển thành `(1, 1)`

**Đáp án: A**

**Giải thích:** Với số thực hữu hạn thuộc phạm vi kiểu nguyên đích, `.astype(int)` bỏ phần lẻ theo hướng về không chứ không làm tròn gần nhất. Vì vậy `[2.9, -2.9]` đổi thành số nguyên `[2, -2]` và vẫn giữ shape một chiều ban đầu.


**Q19. What is the output shape of `X.mean(axis=0)` for `X.shape == (3,2)`? | Nếu `X.shape == (3,2)`, `X.mean(axis=0)` có shape nào?**

A. `(2,)` | `(2,)`

B. `(3,)` | `(3,)`

C. `(3,2)` | `(3,2)`

D. `(1,3)` | `(1,3)`

**Đáp án: A**

**Giải thích:** Ma trận `(3, 2)` gồm ba hàng và hai cột. `mean(axis=0)` gộp ba hàng, để lại một trung bình cho mỗi cột nên shape mặc định là `(2,)`, không phải `(3,)`.


**Q20. Why label the meaning of each row and column? | Vì sao phải nêu rõ ý nghĩa từng hàng, cột?**

A. To convert a matrix into text | Để chuyển ma trận thành chữ

B. To change dtype automatically | Để tự đổi dtype

C. To avoid all numeric calculations | Để tránh mọi phép tính

D. To interpret aggregated results correctly | Để hiểu đúng kết quả tổng hợp

**Đáp án: D**

**Giải thích:** Nhãn hàng và cột cho biết giá trị tổng hợp đang đo cái gì chứ không chỉ cách tính. Nếu hàng là học viên và cột là môn, `mean(axis=0)` trả điểm trung bình từng môn; hiểu ngược cấu trúc sẽ trả lời câu hỏi khác.

## 8. Nối sang bài tiếp theo

`List → NumPy Array → Matrix → PCA`.
