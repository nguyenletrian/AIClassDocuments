# PY-38 — Quantile, IQR, outlier, skewness và kurtosis


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Quantile** — phân vị; **IQR** — khoảng tứ phân vị.

`Thống kê mô tả → Quantile/IQR → Outlier → Kiểm tra dữ liệu ML`

**Học xong dùng để làm gì?** Dùng Q1/Q3/IQR phát hiện quan sát nằm xa phân bố, phân biệt ngoại lệ thật và nhập liệu sai.

**Kết nối kiến thức tiếp theo:** PY-39 xem kết quả thống kê thay đổi như thế nào khi lấy mẫu nhiều lần.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Khái niệm |
|---|---|---|
| Quantile | phân vị | Giá trị chia phân phối theo tỷ lệ tích lũy |
| IQR | khoảng tứ phân vị | Khoảng cách Q3-Q1, mô tả 50% dữ liệu giữa |
| Skewness | độ lệch phân phối | Mức bất đối xứng của phân phối quanh tâm |
| Kurtosis | độ nhọn/đuôi phân phối | Chỉ số mô tả đặc điểm đuôi so với chuẩn theo quy ước |

## 3. Thư viện và hàm Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cách viết | Khi nào dùng, ý nghĩa tham số |
|---|---|
| `np.quantile(x,[.25,.5,.75])` | Tìm các phân vị 25%, 50%, 75% |
| `Q1 - 1.5*IQR` và `Q3 + 1.5*IQR` | Ngưỡng dưới và trên để gắn cờ giá trị cần rà soát |
| `pd.Series.skew()` | Đánh giá bất đối xứng, nhạy với cỡ mẫu |
| `pd.Series.kurt()` | Excess kurtosis theo quy ước Pandas |

## 4. Khái niệm chính và liên quan

**Mạch kiến thức:** Phân vị cho biết vị trí của một giá trị trong dãy đã sắp; IQR đo độ rộng phần giữa để sàng lọc ngoại lệ; skewness nói về bất đối xứng và kurtosis liên quan đặc điểm đuôi. Bất thường không đồng nghĩa sai dữ liệu.

### 4.1. Quantile — Mốc chia thứ tự dữ liệu

**Từ vựng:** **Quantile** — phân vị; **Q1/Q2/Q3** — tứ phân vị.

Phân vị q là mốc trên dãy số đã sắp, liên quan đến tỷ lệ giá trị ở phía dưới. **Q1** ứng với mức 25%, **Q2** là trung vị 50%, **Q3** ứng với 75%. Ví dụ năm hóa đơn 10,20,30,40,50 nghìn đồng: `np.quantile(x,0.75)` trả 40. Với bộ dữ liệu nhỏ, phương pháp **nội suy** giữa vị trí của các số làm cho kết quả phụ thuộc quy ước từng thư viện; không phải lúc nào phân vị cũng là số gốc trong dữ liệu.

**No Note — Không chú thích**

```python
import numpy as np

amounts = [10, 20, 30, 40, 50]
print(float(np.quantile(amounts, 0.75)))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Lấy phân vị 75% để biết ngưỡng mà khoảng ba phần tư số tiền nằm dưới.
# Dữ liệu: Năm khoản tiền 10,20,30,40,50 cùng đơn vị, mốc q=0.75 là phân vị thứ ba.
# NumPy hỗ trợ tính phân vị qua quantile().
import numpy as np

# List 5 khoản tiền, không phải các giá trị xác suất.
amounts = [10, 20, 30, 40, 50]
# quantile(data,q) lấy giá trị tại phân vị q=0.75 (Q3), theo phương pháp nội suy tuyến tính mặc định khi cần; 75% là vị trí dữ liệu, không phải nhân tổng với 0.75.
# float() đưa scalar NumPy về số Python để in.
print(float(np.quantile(amounts, 0.75)))
```

**Kết quả khi chạy:**

```text
40.0
```

Mốc phân vị 75% bằng 40 nghìn đồng theo phương pháp nội suy mặc định NumPy.

### 4.2. IQR — Độ rộng nửa giữa bộ dữ liệu

**Từ vựng:** **IQR** — khoảng tứ phân vị; **Q1/Q3** — phân vị 25%/75%.

**IQR = Q3−Q1** đo độ rộng của khoảng chứa phần giữa dữ liệu. Với `[1,2,3,4,5]`, Q1=2 và Q3=4, nên IQR=2 đơn vị. Một cách **gắn cờ** ngoại lệ là ngoài các ngưỡng `Q1−1.5×IQR` hoặc `Q3+1.5×IQR`. Đây chỉ là quy tắc rà soát, **không chứng minh dữ liệu sai**; chẳng hạn một hóa đơn lớn có thể hoàn toàn hợp lệ.

**No Note — Không chú thích**

```python
import numpy as np

x = [1, 2, 3, 4, 5]
q1, q3 = np.quantile(x, [0.25, 0.75])
print(float(q3 - q1))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tính IQR bằng khoảng cách giữa phân vị 25% và 75%.
# Dữ liệu: Năm giá trị đã sắp 1,2,3,4,5; IQR thể hiện độ rộng 50% số liệu ở giữa.
# NumPy quantile() cho phép lấy nhiều phân vị trong một lần gọi.
import numpy as np

# List 5 quan sát dạng số.
x = [1, 2, 3, 4, 5]
# Trả hai mốc Q1 (25%) và Q3 (75%) theo thứ tự yêu cầu; phép gán q1,q3 tách hai giá trị.
q1, q3 = np.quantile(x, [0.25, 0.75])
# IQR là khoảng rộng từ Q1 tới Q3, không phải max-min toàn bộ dữ liệu.
# float() chuyển scalar kết quả thành float Python.
print(float(q3 - q1))
```

**Kết quả khi chạy:**

```text
2.0
```

Nửa giữa của dữ liệu trải rộng 2 đơn vị theo quy tắc phân vị đã chọn.

### 4.3. Skewness — Độ bất đối xứng của phân phối

**Từ vựng:** **Skewness** — độ lệch; **Right tail** — đuôi phải.

**Skewness** đo mức bất đối xứng. Một dãy như `[1,1,2,8]` có ba số nhỏ và một số lớn, khiến **đuôi phải kéo dài** và độ lệch dương. `pd.Series.skew()` trả hệ số skew đã được hiệu chỉnh theo công thức Pandas; tính trên mẫu ít quan sát rất kém ổn định. Không suy ra mọi giá trị lớn đều là lỗi từ skew dương.

**No Note — Không chú thích**

```python
import pandas as pd

x = pd.Series([1, 1, 2, 8])
print(round(float(x.skew()), 3))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Dùng skewness đánh giá phân phối có đuôi kéo về phía giá trị lớn.
# Dữ liệu: Bốn số 1,1,2,8, giá trị 8 nằm xa về phía phải.
# Pandas Series có phương thức skew() để đo độ lệch dạng phân phối.
import pandas as pd

# Tạo Series gồm bốn giá trị, trong đó 8 là giá trị cao rõ rệt.
x = pd.Series([1, 1, 2, 8])
# skew() trả hệ số lệch đã điều chỉnh theo kích thước mẫu của pandas: dương thường nghĩa đuôi PHẢI dài hơn, âm là đuôi trái; không phải xác suất.
# float() chuẩn hóa scalar về Python, round(...,3) làm tròn để hiển thị.
print(round(float(x.skew()), 3))
```

**Kết quả khi chạy:**

```text
1.887
```

Độ lệch dương khoảng 1,887 gợi ý đuôi phải dài hơn đuôi trái.

### 4.4. Kurtosis — Đặc điểm đuôi theo quy ước

**Từ vựng:** **Kurtosis** — độ nhọn/hệ số liên quan đến đuôi; **Excess kurtosis** — kurtosis dư.

**Kurtosis** liên quan đến các moment bậc bốn và độ nặng của đuôi phân phối; không nên hiểu đơn giản chỉ là **độ cao của đỉnh**. Pandas `Series.kurt()` trả **excess kurtosis**, lấy phân phối chuẩn làm mốc 0. Với dãy `[2,3,3,4,4,5,5,6,7,20]`, số 20 rất lớn có thể làm kurtosis dư dương. Trên mẫu nhỏ, chỉ số này biến động mạnh.

**No Note — Không chú thích**

```python
import pandas as pd

x = pd.Series([2, 3, 3, 4, 4, 5, 5, 6, 7, 20])
print(round(float(x.kurt()), 3))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Dùng excess kurtosis của Pandas để mô tả độ nặng đuôi phân phối.
# Dữ liệu: Mười giá trị có đa số từ 2 đến 7 và một số 20 lớn bất thường.
# Pandas kurt() dùng quy ước excess kurtosis (phân phối chuẩn có mốc khoảng 0).
import pandas as pd

# Series lưu mười quan sát số thực/số nguyên.
x = pd.Series([2, 3, 3, 4, 4, 5, 5, 6, 7, 20])
# kurt() trả excess kurtosis hiệu chỉnh theo mẫu; giá trị cao gợi ý đuôi nặng/ngoại lệ, KHÔNG trực tiếp đếm số ngoại lệ.
# round(...,3) giới hạn số thập phân để dễ đọc, không sửa giá trị dữ liệu.
print(round(float(x.kurt()), 3))
```

**Kết quả khi chạy:**

```text
7.824
```

Excess kurtosis dương lớn cho thấy mẫu này có hành vi đuôi bất thường so với dạng chuẩn.

## 5. Năm tình huống Quantile/IQR — từ phân vị đến phát hiện ngoại lệ theo nhóm

### Tình huống 1 — Cấp 1: Tìm các tứ phân vị của 10 hóa đơn

**Từ vựng trong mục:** **Quantile** — phân vị; **Interpolation** — nội suy.

**Tình huống thực tế:** Cửa hàng lập bảng **10 hóa đơn**, mỗi đơn có giá trị tính bằng **nghìn đồng**, từ 10 đến 28 theo thứ tự tăng dần. Chủ cửa hàng muốn tìm ba **mốc chia dữ liệu** là Q1, trung vị Q2 và Q3 để hiểu nhóm hóa đơn nằm ở vùng giá thấp, giữa và cao, thay vì chỉ xem đơn rẻ nhất và đắt nhất.

**Vì sao chọn cách này?** **Phân vị** là các mốc dùng để nhìn vị trí của giá trị trong **danh sách đã sắp thứ tự**. **Q1** đại diện vùng khoảng một phần tư thấp, **median/Q2** chia dữ liệu thành nửa thấp và nửa cao, **Q3** đại diện vùng khoảng ba phần tư. `np.quantile(amounts, [0.25, 0.5, 0.75])` lấy ba mốc này từ **10 khoản tiền có cùng đơn vị**. Vì vị trí phân vị có thể nằm **giữa hai hóa đơn thật**, NumPy có thể **nội suy** ra một mức không xuất hiện nguyên vẹn trong dữ liệu; đây là mốc mô tả, không phải một hóa đơn bị bỏ sót.

**Quy trình:**
1. Ghi đúng 10 giá trị cùng đơn vị.
2. Tính đồng thời các phân vị 25%, 50%, 75% bằng NumPy.
3. In ba mốc và số đơn để đọc đúng ý nghĩa.

**No Note — Không chú thích**

```python
import numpy as np
amounts = np.array([10,12,14,16,18,20,22,24,26,28], dtype=float)
q1, median, q3 = np.quantile(amounts, [0.25, 0.5, 0.75])
if len(amounts) != 10:
    raise ValueError("Cần đủ 10 hóa đơn.")
print("Hóa đơn:", len(amounts))
print(f"Q1 (nghìn đồng): {q1:.1f}")
print(f"Median (nghìn đồng): {median:.1f}")
print(f"Q3 (nghìn đồng): {q3:.1f}")
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Báo Q1, median và Q3 của 10 hóa đơn theo cùng một lệnh quantile.
# Dữ liệu: 10 khoản từ 10 tới 28 nghìn đồng, phân vị mô tả mốc theo thứ tự tiền tăng.
# NumPy quantile() hỗ trợ nhiều mốc phân vị trong một lần.
import numpy as np
# Vector 10 số tiền, dtype=float giữ khả năng nội suy ra số lẻ.
amounts = np.array([10,12,14,16,18,20,22,24,26,28], dtype=float)
# Trả Q1, median/Q2, Q3 tương ứng tỷ lệ 25%,50%,75%; NumPy mặc định nội suy tuyến tính khi vị trí nằm giữa hai mẫu.
q1, median, q3 = np.quantile(amounts, [0.25, 0.5, 0.75])
# len() kiểm đủ 10 hóa đơn, không phải giá trị phân vị.
if len(amounts) != 10:
    # ValueError cảnh báo thiếu hồ sơ nguồn trước khi kết luận.
    raise ValueError("Cần đủ 10 hóa đơn.")
# len() kiểm đủ 10 hóa đơn, không phải giá trị phân vị.
print("Hóa đơn:", len(amounts))
# :.1f hiển thị Q1 theo nghìn đồng với một số lẻ.
print(f"Q1 (nghìn đồng): {q1:.1f}")
# Median là trung vị sau sắp xếp, không phải trung bình cộng.
print(f"Median (nghìn đồng): {median:.1f}")
# Q3 là mốc phân vị 75%, không phải giá lớn nhất.
print(f"Q3 (nghìn đồng): {q3:.1f}")
```

**Kết quả khi chạy:**

```text
Hóa đơn: 10
Q1 (nghìn đồng): 14.5
Median (nghìn đồng): 19.0
Q3 (nghìn đồng): 23.5
```

Mốc Q1=14,5 nghìn đồng không phải một đơn giá gốc; đó là kết quả nội suy theo quy tắc mặc định của NumPy.

### Tình huống 2 — Cấp 2: Dùng IQR rà soát hóa đơn 500 trong 12 đơn

**Từ vựng trong mục:** **IQR** — khoảng tứ phân vị; **Fence** — ngưỡng gắn cờ; **Outlier** — điểm bất thường.

**Tình huống thực tế:** Một quầy bán hàng có **12 hóa đơn** tính bằng **nghìn đồng**; **11 hóa đơn từ 100 đến 145**, còn một hóa đơn giá **500**. Nhân viên muốn tìm xem hóa đơn nào **nằm xa vùng mua hàng thường gặp** theo quy tắc IQR để đưa vào danh sách kiểm tra chứng từ. Họ không được xóa hóa đơn 500 vì chưa có bằng chứng đó là số tiền sai.

**Vì sao chọn cách này?** **IQR** là độ rộng của **vùng dữ liệu từ Q1 tới Q3**, tức phần nằm giữa của bảng đã sắp xếp. Chương trình lấy Q1/Q3, rồi tạo hai **hàng rào kiểm tra** ở phía thấp và cao, cách mỗi đầu thêm **1,5 lần IQR**. Số nào ngoài hàng rào được **gắn cờ ngoại lệ**; với 12 hóa đơn này, khoản 500 nghìn đồng quá cao so với nhóm còn lại nên đáng kiểm tra. `np.quantile()` và phép lọc chỉ tìm **điểm khác thường theo quy tắc thống kê**, không chứng minh khoản 500 là gian lận hay sai dữ liệu. 1,5 là ngưỡng quy ước thường dùng, không phải luật kinh doanh.

**Quy trình:**
1. Tìm Q1 và Q3 của đúng 12 đơn.
2. Tạo ngưỡng dưới/trên từ khoảng tứ phân vị.
3. Tìm số đơn ngoài khoảng và giá trị cần xem xét.

**No Note — Không chú thích**

```python
import numpy as np
amounts = np.array([100,105,110,115,120,120,125,130,135,140,145,500], dtype=float)
q1, q3 = np.quantile(amounts, [0.25, 0.75])
iqr = q3 - q1
low, high = q1 - 1.5*iqr, q3 + 1.5*iqr
flagged = amounts[(amounts < low) | (amounts > high)]
if amounts.size != 12:
    raise ValueError("Cần đủ 12 hóa đơn để tính IQR.")
print("Hóa đơn:", amounts.size)
print(f"IQR (nghìn đồng): {iqr:.2f}")
print(f"Ngưỡng trên: {high:.1f}")
print("Đơn cần xem:", flagged.astype(int).tolist())
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Phát hiện hóa đơn cao bất thường bằng hàng rào 1.5×IQR mà không xóa dữ liệu.
# Dữ liệu: 12 hóa đơn nghìn đồng, một khoản 500 rất cao so dãy 100..145.
# NumPy tính phân vị và lọc mảng theo điều kiện.
import numpy as np
# Vector 12 khoản tiền float, đơn vị nghìn đồng.
amounts = np.array([100,105,110,115,120,120,125,130,135,140,145,500], dtype=float)
# Lấy Q1/Q3 từ 12 giá trị gốc, chưa loại bất cứ hóa đơn nào.
q1, q3 = np.quantile(amounts, [0.25, 0.75])
# IQR=Q3−Q1 là độ rộng khoảng giữa, làm thang đo cho hàng rào ngoại lệ.
iqr = q3 - q1
# Hàng rào dưới Q1−1.5 IQR; ngưỡng tham khảo thống kê chứ không tự kết luận dữ liệu sai.
# Hàng rào trên Q3+1.5 IQR; 1.5 là quy tắc Tukey thường dùng, cần xem xét bối cảnh.
low, high = q1 - 1.5*iqr, q3 + 1.5*iqr
# So từng ô với hai ngưỡng, | là OR theo phần tử; mask True nếu nằm ngoài bất kỳ hàng rào nào.
# Boolean indexing tạo mảng các giá trị cần kiểm tra mà không sửa amounts gốc.
flagged = amounts[(amounts < low) | (amounts > high)]
# size đếm 12 khoản trong vector.
if amounts.size != 12:
    # Dừng nếu không đủ 12 hóa đơn để so sánh phân vị.
    raise ValueError("Cần đủ 12 hóa đơn để tính IQR.")
# size đếm 12 khoản trong vector.
print("Hóa đơn:", amounts.size)
# Định dạng IQR hai chữ số lẻ theo nghìn đồng.
print(f"IQR (nghìn đồng): {iqr:.2f}")
print(f"Ngưỡng trên: {high:.1f}")
# astype(int) chuyển số tiền sang int để dễ in, tolist() đổi ndarray thành list Python; không xóa giá trị khỏi nguồn.
print("Đơn cần xem:", flagged.astype(int).tolist())
```

**Kết quả khi chạy:**

```text
Hóa đơn: 12
IQR (nghìn đồng): 22.50
Ngưỡng trên: 170.0
Đơn cần xem: [500]
```

Một hóa đơn thật có thể vượt ngưỡng IQR hợp lệ; cần đối chiếu hóa đơn nguồn trước khi quyết định xử lý.

### Tình huống 3 — Cấp 3: So mean, median và độ lệch phải trên 15 thời gian

**Từ vựng trong mục:** **Skewness** — độ lệch bất đối xứng; **Right tail** — đuôi phải.

**Tình huống thực tế:** Trung tâm chăm sóc đo **15 lượt thời gian phục vụ**, đơn vị **phút**; 14 lượt kéo dài khoảng **10–16 phút**, có một lượt **90 phút**. Quản lý muốn xem mức thời gian thông thường, tính trung bình so với trung vị và hiểu bảng thời gian có **đuôi kéo dài về phía các lượt rất lâu** hay không. Phiếu 90 phút có thể là ca phức tạp thật, không nhất thiết lỗi nhập.

**Vì sao chọn cách này?** **Skewness (độ lệch)** mô tả hình dạng phân phối có **đuôi kéo dài về bên cao hay bên thấp**. Khi 14 lượt từ 10–16 phút nhưng một lượt 90 phút, **mean** bị kéo lên mạnh hơn **median**, và độ lệch thường **dương** do đuôi kéo về phía thời gian cao. `pd.Series.skew()` đo đặc điểm bất đối xứng từ chính **15 lượt**; kiểm `> 0` giúp giải thích hướng của đuôi. Không dùng kết quả này để tự xóa phiếu 90 phút: mẫu nhỏ và một trường hợp rất lâu có thể là sự kiện thực.

**Quy trình:**
1. Tạo 15 số phút phục vụ.
2. Tính mean, median và skewness bằng Pandas.
3. So dấu skew và hai thước đo trung tâm.

**No Note — Không chú thích**

```python
import pandas as pd
minutes = pd.Series([10,10,11,11,12,12,12,13,14,14,15,15,15,16,90], dtype=float)
if len(minutes) != 15:
    raise ValueError("Cần đủ 15 lượt đo thời gian.")
print("Lượt:", len(minutes))
print(f"Mean (phút): {minutes.mean():.2f}")
print(f"Median (phút): {minutes.median():.2f}")
print(f"Skew: {minutes.skew():.3f}")
print("Lệch phải:", bool(minutes.skew() > 0))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: So mean và median cùng hệ số lệch phải trong 15 thời gian có ngoại lệ 90 phút.
# Dữ liệu: 15 lần xử lý, đa số 10..16 phút, một lượt 90 phút kéo dài đuôi phải.
# Pandas Series tính mean, median và skew trên dãy số.
import pandas as pd
# Tạo Series 15 thời gian dtype=float, mỗi lượt tính phút.
minutes = pd.Series([10,10,11,11,12,12,12,13,14,14,15,15,15,16,90], dtype=float)
# len() bảo đảm đủ 15 thời gian trước khi đánh giá.
if len(minutes) != 15:
    # Báo lỗi số lượt không đúng thay vì so bảng thiếu.
    raise ValueError("Cần đủ 15 lượt đo thời gian.")
# len() bảo đảm đủ 15 thời gian trước khi đánh giá.
print("Lượt:", len(minutes))
# mean() là trung bình cộng, nhạy với thời gian 90 phút.
print(f"Mean (phút): {minutes.mean():.2f}")
# median() lấy điểm giữa sau sắp xếp, ít chịu tác động của lượt 90 phút.
print(f"Median (phút): {minutes.median():.2f}")
# skew() là độ lệch đã điều chỉnh trong pandas; dương cho thấy đuôi phân phối kéo sang phía giá trị lớn.
print(f"Skew: {minutes.skew():.3f}")
# skew() là độ lệch đã điều chỉnh trong pandas; dương cho thấy đuôi phân phối kéo sang phía giá trị lớn.
# bool() biểu diễn kết luận skew dương; không tự suy rằng mọi giá trị lớn đều là sai.
print("Lệch phải:", bool(minutes.skew() > 0))
```

**Kết quả khi chạy:**

```text
Lượt: 15
Mean (phút): 18.00
Median (phút): 13.00
Skew: 3.811
Lệch phải: True
```

Skew dương chỉ mô tả phân bố dữ liệu đang có; không kết luận lượt 90 phút là sai số đo.

### Tình huống 4 — Cấp 4: Phân biệt độ lệch phải và kurtosis của 18 mẫu

**Từ vựng trong mục:** **Kurtosis** — mô tả đuôi; **Excess kurtosis** — kurtosis dư; **Skewness** — bất đối xứng.

**Tình huống thực tế:** Phòng thí nghiệm ghi **18 lần đo mức tín hiệu**, cùng một đơn vị chỉ số; 17 lần nằm khoảng **20–36**, một lần lên tới **120**. Kỹ thuật viên muốn biết dữ liệu có **bất đối xứng về phía giá trị cao** không, số đo cực lớn làm hình dạng phân phối thay đổi ra sao và cờ cảnh báo IQR có chỉ ra 120 để kiểm tra lại thiết bị hay không.

**Vì sao chọn cách này?** **Skew** cho biết phân phối lệch trái/phải, còn **excess kurtosis** đo đặc điểm liên quan đến **mức nhạy với các độ lệch lớn/đuôi cực trị** so với chuẩn tham chiếu; đây không đơn thuần là độ nhọn ở đỉnh biểu đồ. `pd.Series.kurt()` trả excess kurtosis, với mốc tham chiếu của phân phối chuẩn là **0**. Một giá trị 120 so với 17 giá trị quanh 20–36 ảnh hưởng mạnh đến cả hai thống kê. Chương trình đồng thời dùng **hàng rào IQR phía trên** để liệt kê số đo cần xem; phát hiện điểm lạ là **đầu mối kiểm tra**, không phải bằng chứng cảm biến đã hỏng.

**Quy trình:**
1. Tạo 18 mức tín hiệu, giữ lại số đo 120 để rà soát.
2. Tính skew và kurt của Pandas theo quy ước thư viện.
3. Gắn cờ bằng IQR để nhận biết điểm cần xác minh.

**No Note — Không chú thích**

```python
import numpy as np
import pandas as pd
signal = pd.Series([20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,120], dtype=float)
q1, q3 = np.quantile(signal, [0.25, 0.75])
outliers = signal[signal > q3 + 1.5*(q3-q1)]
if len(signal) != 18:
    raise ValueError("Cần đủ 18 số đo tín hiệu.")
print("Mẫu:", len(signal))
print(f"Skew: {signal.skew():.3f}")
print(f"Excess kurtosis: {signal.kurt():.3f}")
print("Giá trị cần xem:", outliers.astype(int).tolist())
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Dùng IQR đánh dấu tín hiệu lớn và xem skew cùng excess kurtosis của 18 mẫu.
# Dữ liệu: 18 tín hiệu, phần lớn 20..36 nhưng có một giá trị 120 cao vượt cụm.
# NumPy quantile() lấy Q1, Q3 và tạo ngưỡng theo IQR.
import numpy as np
# Pandas Series skew()/kurt() mô tả độ lệch và đuôi.
import pandas as pd
# 18 số đo kiểu float, không xóa điểm 120 khỏi nguồn.
signal = pd.Series([20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,120], dtype=float)
# Tính Q1/Q3 từ Series như vector số và dùng nội suy phân vị mặc định.
q1, q3 = np.quantile(signal, [0.25, 0.75])
# So từng giá trị với hàng rào TRÊN bằng Q3+1.5 IQR; chỉ lọc ngoại lệ cao, chưa kiểm hàng rào dưới.
# Lập chỉ mục bằng mask Boolean tạo Series con các điểm cần xem, nguồn signal vẫn giữ nguyên.
outliers = signal[signal > q3 + 1.5*(q3-q1)]
# len() xác nhận đủ 18 phép đo.
if len(signal) != 18:
    # Ngừng khi không đủ dữ liệu để diễn giải.
    raise ValueError("Cần đủ 18 số đo tín hiệu.")
# len() xác nhận đủ 18 phép đo.
print("Mẫu:", len(signal))
# skew() >0 thường mô tả đuôi phải dài, giá trị 120 có thể làm tăng hệ số.
print(f"Skew: {signal.skew():.3f}")
# kurt() theo Pandas là excess kurtosis; điểm 120 làm đuôi có thể nặng, không phải tỷ lệ ngoại lệ.
print(f"Excess kurtosis: {signal.kurt():.3f}")
# astype(int) đổi định dạng giá trị khi in, tolist() chuyển Series thành list Python; không xóa khỏi dữ liệu gốc.
print("Giá trị cần xem:", outliers.astype(int).tolist())
```

**Kết quả khi chạy:**

```text
Mẫu: 18
Skew: 3.900
Excess kurtosis: 15.980
Giá trị cần xem: [120]
```

Chỉ số độ lệch và kurtosis nhạy với giá trị rất lớn, vì vậy cần kết hợp hiểu nguồn số đo chứ không chỉ gắn nhãn bằng một con số.

### Tình huống 5 — Cấp 5: Phát hiện ngoại lệ riêng hai nhóm trên 20 sản phẩm có ô thiếu

**Từ vựng trong mục:** **Group-wise IQR** — IQR theo nhóm; **Missing data** — dữ liệu thiếu; **Data integrity** — tính toàn vẹn.

**Tình huống thực tế:** Kho chứa **20 sản phẩm P01–P20** thuộc hai loại A và B, mỗi loại 10 sản phẩm. **Khối lượng** đo bằng **gam**: nhóm A chủ yếu **50–57 g**, nhóm B chủ yếu **150–158 g**. P09 của nhóm A chưa cân, P10 nặng **110 g** và P20 nặng **220 g**. Nhân viên muốn biết số mẫu thiếu và **mã khối lượng bất thường so với chính nhóm của nó**, không so sản phẩm A với giá trị bình thường của nhóm B.

**Vì sao chọn cách này?** Mỗi loại sản phẩm có **mức khối lượng thông thường khác nhau**, nên phải tính **Q1, Q3 và IQR riêng cho nhóm A và B** bằng `groupby('group')`. `dropna()` bỏ riêng ô khối lượng **chưa cân** khi tính mốc, còn `isna()` vẫn giúp báo rõ số mẫu thiếu. Trong mỗi nhóm, quy tắc **1,5 lần IQR** gắn cờ những mã ở quá xa vùng giữa, như P10 hoặc P20; **mã sản phẩm** được giữ để kiểm lại hàng thật. Nếu gộp A và B thành một bảng trước khi tính ngưỡng, hai cụm khối lượng 50 g và 150 g có thể làm ngưỡng chung trở nên vô ích, che các trường hợp bất thường trong từng loại.

**Quy trình:**
1. Tạo 20 hàng, ghi đơn vị g và tên nhóm.
2. Với từng nhóm, loại NaN chỉ khi tính Q1/Q3 và IQR.
3. Lưu ID ngoài ngưỡng của từng nhóm, báo tổng hàng, thiếu và danh sách cần xem.

**No Note — Không chú thích**

```python
import numpy as np
import pandas as pd
mass = [50,51,52,53,54,55,56,57,None,110,150,151,152,153,154,155,156,157,158,220]
ids = []
for i in range(1, 21):
    ids.append(f"P{i:02d}")
df = pd.DataFrame({"id": ids,
                   "group": ["A"]*10 + ["B"]*10, "mass_g": mass})
flagged = []
for group, subset in df.groupby("group"):
    valid = subset["mass_g"].dropna()
    q1, q3 = np.quantile(valid, [0.25, 0.75])
    low, high = q1-1.5*(q3-q1), q3+1.5*(q3-q1)
    flagged.extend(subset.loc[(subset["mass_g"] < low) | (subset["mass_g"] > high), "id"])
if len(df) != 20:
    raise ValueError("Cần đủ 20 mẫu khối lượng, kể cả lượt thiếu.")
print("Sản phẩm:", len(df))
print("Thiếu khối lượng:", int(df["mass_g"].isna().sum()))
print("Ngoại lệ theo nhóm:", ", ".join(sorted(flagged)))
print("Hàng còn có khối lượng:", int(df["mass_g"].notna().sum()))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Phát hiện ngoại lệ riêng từng nhóm A/B trong 20 sản phẩm, không nhầm quy mô hai nhóm.
# Dữ liệu: 20 sản phẩm P01..P20; khối lượng gram, một None là thiếu; A/B mỗi nhóm 10 sản phẩm với phân phối khác nhau.
# NumPy lấy phân vị cho dữ liệu số còn hợp lệ của từng nhóm.
import numpy as np
# Pandas DataFrame hỗ trợ phân nhóm, dropna, loc và cột thiếu.
import pandas as pd
# 20 khối lượng gram, None biểu thị chưa đo, không được thay bằng 0 trước tính phân vị.
mass = [50,51,52,53,54,55,56,57,None,110,150,151,152,153,154,155,156,157,158,220]
ids = []
# range(1,21) sinh thứ tự 1..20, không lấy 21.
for i in range(1, 21):
    # f-string :02d thêm số 0 đầu mã P01..P20.
    # append() giữ mã theo cùng vị trí mỗi khối lượng.
    ids.append(f"P{i:02d}")
# Tạo 20 hàng id/group/mass_g; list nhóm A 10 lần rồi B 10 lần, mỗi hàng một sản phẩm.
df = pd.DataFrame({"id": ids,
                   # List multiplication tạo 10 nhãn A rồi 10 B, không phải phép nhân xác suất.
                   "group": ["A"]*10 + ["B"]*10, "mass_g": mass})
flagged = []
# groupby('group') tách bảng thành hai nhóm độc lập A/B trước khi tìm hàng rào, tránh áp một ngưỡng chung sai bối cảnh.
for group, subset in df.groupby("group"):
    # dropna() loại tạm ô None/NaN CHỈ khi tính phân vị của nhóm, không xóa hàng gốc khỏi df.
    valid = subset["mass_g"].dropna()
    # Tính Q1/Q3 trên số đo hợp lệ riêng từng nhóm; mốc có thể khác nhau giữa A và B.
    q1, q3 = np.quantile(valid, [0.25, 0.75])
    # Hàng rào dưới Q1−1.5 IQR, trên Q3+1.5 IQR của nhóm hiện tại.
    low, high = q1-1.5*(q3-q1), q3+1.5*(q3-q1)
    # Hai điều kiện nối bằng | Boolean từng ô; NaN không so đạt ngưỡng nên không bị gắn nhãn ngoại lệ theo phép này.
    # loc[mask,'id'] trả các mã ngoại lệ trong nhóm hiện tại, không dùng chỉ số hàng làm mã.
    # extend() thêm từng mã ngoại lệ vào list chung, không lồng cả Series thành một phần tử.
    flagged.extend(subset.loc[(subset["mass_g"] < low) | (subset["mass_g"] > high), "id"])
# len() kiểm đủ 20 sản phẩm, gồm cả mẫu thiếu.
if len(df) != 20:
    # Dừng nếu số lượng hồ sơ nguồn không bằng 20.
    raise ValueError("Cần đủ 20 mẫu khối lượng, kể cả lượt thiếu.")
# len() kiểm đủ 20 sản phẩm, gồm cả mẫu thiếu.
print("Sản phẩm:", len(df))
# isna() nhận các khối lượng thiếu, sum() đếm True; không đồng nghĩa ngoại lệ.
print("Thiếu khối lượng:", int(df["mass_g"].isna().sum()))
# sorted() sắp mã được cảnh báo, join() ghép chuỗi để in ổn định.
print("Ngoại lệ theo nhóm:", ", ".join(sorted(flagged)))
# notna() đánh dấu mẫu có khối lượng, sum() đếm còn bao nhiêu mẫu đo được.
print("Hàng còn có khối lượng:", int(df["mass_g"].notna().sum()))
```

**Kết quả khi chạy:**

```text
Sản phẩm: 20
Thiếu khối lượng: 1
Ngoại lệ theo nhóm: P10, P20
Hàng còn có khối lượng: 19
```

Đây là **hai điểm cần xem lại theo nhóm**, chưa phải hai sản phẩm bị hỏng. Mẫu P09 thiếu khối lượng cần xử lý riêng trước khi ra quyết định.

## 6. Sai lầm thường gặp

- Q1 và Q3 phụ thuộc phương pháp nội suy, nhất là với mẫu nhỏ; cần giữ nhất quán giữa các thư viện.
- IQR dùng ngưỡng **gợi ý** ngoại lệ, không chứng minh giá trị là lỗi hay phải xóa.
- Skew dương nói về đuôi phải; skew âm nói về đuôi trái, không đồng nghĩa mean luôn lớn/nhỏ trong mọi dữ liệu.
- Kurtosis liên quan moment bậc bốn/đuôi, không chỉ độ cao đỉnh; Pandas trả **excess kurtosis**.
- Skew và kurt mẫu nhỏ không ổn định; cần xem đồ thị và nguồn dữ liệu.
- Khi điền khuyết cho ML, tính median trên train, không lấy thông tin test.

## 7. Trắc nghiệm

**Q1. What is a quantile? | Phân vị là gì?**

A. Fourth-moment tail behavior relative to normal | Đặc trưng moment bậc bốn/đuôi so với chuẩn

B. The difference Q3−Q1 | Hiệu Q3−Q1

C. A value associated with a cumulative rank | Giá trị gắn với một mức thứ hạng tích lũy

D. Distribution asymmetry | Mức bất đối xứng phân phối

**Đáp án: C**

**Giải thích:** Phân vị chia dữ liệu sắp thứ tự theo tỷ lệ.


**Q2. What is IQR? | IQR là gì?**

A. The difference Q3−Q1 | Hiệu Q3−Q1

B. A value associated with a cumulative rank | Giá trị gắn với một mức thứ hạng tích lũy

C. Fourth-moment tail behavior relative to normal | Đặc trưng moment bậc bốn/đuôi so với chuẩn

D. Distribution asymmetry | Mức bất đối xứng phân phối

**Đáp án: A**

**Giải thích:** Nó đo độ rộng nửa giữa dữ liệu.


**Q3. What does skewness measure? | Skewness đo gì?**

A. Fourth-moment tail behavior relative to normal | Đặc trưng moment bậc bốn/đuôi so với chuẩn

B. Distribution asymmetry | Mức bất đối xứng phân phối

C. A value associated with a cumulative rank | Giá trị gắn với một mức thứ hạng tích lũy

D. The difference Q3−Q1 | Hiệu Q3−Q1

**Đáp án: B**

**Giải thích:** Dấu gợi ý phía đuôi dài.


**Q4. What does excess kurtosis measure? | Excess kurtosis mô tả gì?**

A. A value associated with a cumulative rank | Giá trị gắn với một mức thứ hạng tích lũy

B. Distribution asymmetry | Mức bất đối xứng phân phối

C. The difference Q3−Q1 | Hiệu Q3−Q1

D. Fourth-moment tail behavior relative to normal | Đặc trưng moment bậc bốn/đuôi so với chuẩn

**Đáp án: D**

**Giải thích:** Pandas dùng mốc 0 cho chuẩn.


**Q5. If Q1 = 4 and Q3 = 10, what is the interquartile range (IQR)? | Nếu Q1 = 4, Q3 = 10, khoảng tứ phân vị IQR là bao nhiêu?**

A. 6 | 6

B. 4 | 4

C. 2.5 | 2.5

D. 14 | 14

**Đáp án: A**

**Giải thích:** IQR = Q3 − Q1 = 10 − 4 = 6.


**Q6. If Q1 = 4 and Q3 = 10, what is the upper outlier fence using 1.5 × IQR? | Nếu Q1 = 4 và Q3 = 10, ngưỡng ngoại lệ trên theo quy tắc 1.5 × IQR bằng bao nhiêu?**

A. 19 | 19

B. 15 | 15

C. 21 | 21

D. 16 | 16

**Đáp án: A**

**Giải thích:** IQR = 6, nên ngưỡng trên = Q3 + 1.5 × IQR = 10 + 9 = 19.


**Q7. A value is flagged as an outlier by the IQR rule. What can we conclude? | Một giá trị bị đánh dấu ngoại lệ theo quy tắc IQR. Kết luận nào hợp lý?**

A. It must equal the median | Nó bằng trung vị

B. It must be deleted | Bắt buộc phải xóa

C. It needs checking, but is not necessarily wrong | Nên kiểm tra, nhưng chưa chắc là dữ liệu sai

D. It proves a sensor failed | Chứng minh cảm biến bị lỗi

**Đáp án: C**

**Giải thích:** Quy tắc IQR chỉ đánh dấu giá trị nằm xa vùng giữa dữ liệu. Ngoại lệ có thể là giá trị thật.


**Q8. In a typically right-skewed distribution, which comparison is often observed? | Trong phân phối lệch phải điển hình, mối quan hệ nào thường gặp?**

A. Mean = median always | Trung bình luôn bằng trung vị

B. Mean < median always | Trung bình luôn nhỏ hơn trung vị

C. Mean > median often | Trung bình thường lớn hơn trung vị

D. Standard deviation is zero | Độ lệch chuẩn bằng 0

**Đáp án: C**

**Giải thích:** Đuôi kéo dài về bên phải thường làm trung bình bị kéo lên mạnh hơn trung vị; đây không phải quy tắc bắt buộc cho mọi bộ dữ liệu.


**Q9. What does positive skew suggest? | Skew dương gợi ý gì?**

A. A longer left tail | Đuôi trái dài hơn

B. Excess kurtosis | Kurtosis dư

C. A skewness statistic | Hệ số độ lệch phân phối

D. A longer right tail | Đuôi phải dài hơn

**Đáp án: D**

**Giải thích:** Giá trị lớn kéo đuôi sang phải.


**Q10. What does negative skew suggest? | Skew âm gợi ý gì?**

A. Excess kurtosis | Kurtosis dư

B. A longer right tail | Đuôi phải dài hơn

C. A skewness statistic | Hệ số độ lệch phân phối

D. A longer left tail | Đuôi trái dài hơn

**Đáp án: D**

**Giải thích:** Giá trị nhỏ kéo đuôi về trái.


**Q11. What does Series.kurt() return? | Series.kurt() trả gì?**

A. A longer right tail | Đuôi phải dài hơn

B. A longer left tail | Đuôi trái dài hơn

C. A skewness statistic | Hệ số độ lệch phân phối

D. Excess kurtosis | Kurtosis dư

**Đáp án: D**

**Giải thích:** Pandas dùng quy ước kurtosis dư.


**Q12. What does Series.skew() return? | Series.skew() trả gì?**

A. A skewness statistic | Hệ số độ lệch phân phối

B. Excess kurtosis | Kurtosis dư

C. A longer left tail | Đuôi trái dài hơn

D. A longer right tail | Đuôi phải dài hơn

**Đáp án: A**

**Giải thích:** Nó ước lượng bất đối xứng từ mẫu.


**Q13. What is Q3−Q1 called? | Q3−Q1 gọi là gì?**

A. 5 | 5

B. No; legitimate extremes may be flagged | Không; giá trị cực lớn hợp lệ vẫn có thể bị gắn cờ

C. Interquartile range | Khoảng tứ phân vị

D. 3 | 3

**Đáp án: C**

**Giải thích:** Hiệu này chính là IQR.


**Q14. What is median of 1,3,5? | Median của 1,3,5 bằng gì?**

A. 3 | 3

B. No; legitimate extremes may be flagged | Không; giá trị cực lớn hợp lệ vẫn có thể bị gắn cờ

C. Interquartile range | Khoảng tứ phân vị

D. 5 | 5

**Đáp án: A**

**Giải thích:** Giá trị đứng giữa là ba.


**Q15. What is IQR if Q1=2 and Q3=7? | IQR nếu Q1=2, Q3=7 bằng bao nhiêu?**

A. No; legitimate extremes may be flagged | Không; giá trị cực lớn hợp lệ vẫn có thể bị gắn cờ

B. 5 | 5

C. Interquartile range | Khoảng tứ phân vị

D. 3 | 3

**Đáp án: B**

**Giải thích:** Bảy trừ hai bằng năm.


**Q16. Does an IQR outlier flag prove a measurement error? | Gắn cờ outlier theo IQR có chứng minh số đo sai không?**

A. Interquartile range | Khoảng tứ phân vị

B. 5 | 5

C. No; legitimate extremes may be flagged | Không; giá trị cực lớn hợp lệ vẫn có thể bị gắn cờ

D. 3 | 3

**Đáp án: C**

**Giải thích:** Ngưỡng chỉ là quy tắc sàng lọc.


**Q17. Why can quantile values differ between software packages? | Vì sao phân vị có thể khác giữa các phần mềm?**

A. Fit the imputation value on train only | Tính giá trị điền chỉ từ train

B. Median | Trung vị

C. Different interpolation conventions | Quy ước nội suy khác nhau

D. It concerns fourth moments and tails | Nó liên quan moment bậc bốn và đuôi

**Đáp án: C**

**Giải thích:** Mẫu nhỏ dễ cho thấy sự khác biệt quy ước.


**Q18. Why should you avoid interpreting high kurtosis only as a tall peak? | Vì sao không nên hiểu kurtosis cao chỉ là đỉnh cao?**

A. Fit the imputation value on train only | Tính giá trị điền chỉ từ train

B. Different interpolation conventions | Quy ước nội suy khác nhau

C. It concerns fourth moments and tails | Nó liên quan moment bậc bốn và đuôi

D. Median | Trung vị

**Đáp án: C**

**Giải thích:** Chỉ độ cao đỉnh không đủ diễn giải.


**Q19. What statistic is often robust for imputation with extreme values? | Thống kê nào thường phù hợp điền thiếu khi có ngoại lệ lớn?**

A. Different interpolation conventions | Quy ước nội suy khác nhau

B. It concerns fourth moments and tails | Nó liên quan moment bậc bốn và đuôi

C. Fit the imputation value on train only | Tính giá trị điền chỉ từ train

D. Median | Trung vị

**Đáp án: D**

**Giải thích:** Thứ tự khiến trung vị ít nhạy với cực trị.


**Q20. What is a crucial train/test rule when imputing missing values? | Quy tắc train/test quan trọng khi điền khuyết là gì?**

A. It concerns fourth moments and tails | Nó liên quan moment bậc bốn và đuôi

B. Different interpolation conventions | Quy ước nội suy khác nhau

C. Median | Trung vị

D. Fit the imputation value on train only | Tính giá trị điền chỉ từ train

**Đáp án: D**

**Giải thích:** Dữ liệu test không tham gia học tham số tiền xử lý.

## 8. Liên hệ bài kế tiếp

`Thống kê mô tả → Quantile/IQR → Outlier → Kiểm tra dữ liệu ML`.
