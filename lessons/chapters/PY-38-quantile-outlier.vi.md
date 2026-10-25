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

```python
# Mục đích: Mốc chia thứ tự dữ liệu.
import numpy as np

amounts = [10, 20, 30, 40, 50]
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

```python
# Mục đích: Độ rộng nửa giữa bộ dữ liệu.
import numpy as np

x = [1, 2, 3, 4, 5]
q1, q3 = np.quantile(x, [0.25, 0.75])
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

```python
# Mục đích: Độ bất đối xứng của phân phối.
import pandas as pd

x = pd.Series([1, 1, 2, 8])
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

```python
# Mục đích: Đặc điểm đuôi theo quy ước.
import pandas as pd

x = pd.Series([2, 3, 3, 4, 4, 5, 5, 6, 7, 20])
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

A. A value associated with a cumulative rank | Giá trị gắn với một mức thứ hạng tích lũy

B. The difference Q3−Q1 | Hiệu Q3−Q1

C. Distribution asymmetry | Mức bất đối xứng phân phối

D. Fourth-moment tail behavior relative to normal | Đặc trưng moment bậc bốn/đuôi so với chuẩn

**Đáp án: A**

**Giải thích:** Phân vị chia dữ liệu sắp thứ tự theo tỷ lệ.


**Q2. What is IQR? | IQR là gì?**

A. A value associated with a cumulative rank | Giá trị gắn với một mức thứ hạng tích lũy

B. The difference Q3−Q1 | Hiệu Q3−Q1

C. Distribution asymmetry | Mức bất đối xứng phân phối

D. Fourth-moment tail behavior relative to normal | Đặc trưng moment bậc bốn/đuôi so với chuẩn

**Đáp án: B**

**Giải thích:** Nó đo độ rộng nửa giữa dữ liệu.


**Q3. What does skewness measure? | Skewness đo gì?**

A. A value associated with a cumulative rank | Giá trị gắn với một mức thứ hạng tích lũy

B. The difference Q3−Q1 | Hiệu Q3−Q1

C. Distribution asymmetry | Mức bất đối xứng phân phối

D. Fourth-moment tail behavior relative to normal | Đặc trưng moment bậc bốn/đuôi so với chuẩn

**Đáp án: C**

**Giải thích:** Dấu gợi ý phía đuôi dài.


**Q4. What does excess kurtosis measure? | Excess kurtosis mô tả gì?**

A. A value associated with a cumulative rank | Giá trị gắn với một mức thứ hạng tích lũy

B. The difference Q3−Q1 | Hiệu Q3−Q1

C. Distribution asymmetry | Mức bất đối xứng phân phối

D. Fourth-moment tail behavior relative to normal | Đặc trưng moment bậc bốn/đuôi so với chuẩn

**Đáp án: D**

**Giải thích:** Pandas dùng mốc 0 cho chuẩn.


**Q5. What is the Q2 quantile? | Q2 là phân vị nào?**

A. The median | Trung vị

B. The 75th-percentile value | Giá trị phân vị 75%

C. Q3+1.5×IQR | Q3+1.5×IQR

D. Q1−1.5×IQR | Q1−1.5×IQR

**Đáp án: A**

**Giải thích:** Q2 tương ứng phân vị 50%.


**Q6. What does np.quantile(x,0.75) return? | np.quantile(x,0.75) trả gì?**

A. The median | Trung vị

B. The 75th-percentile value | Giá trị phân vị 75%

C. Q3+1.5×IQR | Q3+1.5×IQR

D. Q1−1.5×IQR | Q1−1.5×IQR

**Đáp án: B**

**Giải thích:** Đây là Q3 theo quy ước nội suy đã chọn.


**Q7. How is an upper IQR fence computed? | Ngưỡng trên IQR được tính sao?**

A. The median | Trung vị

B. The 75th-percentile value | Giá trị phân vị 75%

C. Q3+1.5×IQR | Q3+1.5×IQR

D. Q1−1.5×IQR | Q1−1.5×IQR

**Đáp án: C**

**Giải thích:** Giá trị vượt được gắn cờ rà soát.


**Q8. How is a lower IQR fence computed? | Ngưỡng dưới IQR được tính sao?**

A. The median | Trung vị

B. The 75th-percentile value | Giá trị phân vị 75%

C. Q3+1.5×IQR | Q3+1.5×IQR

D. Q1−1.5×IQR | Q1−1.5×IQR

**Đáp án: D**

**Giải thích:** Giá trị dưới là ứng viên ngoại lệ.


**Q9. What does positive skew suggest? | Skew dương gợi ý gì?**

A. A longer right tail | Đuôi phải dài hơn

B. A longer left tail | Đuôi trái dài hơn

C. Excess kurtosis | Kurtosis dư

D. A skewness statistic | Hệ số độ lệch phân phối

**Đáp án: A**

**Giải thích:** Giá trị lớn kéo đuôi sang phải.


**Q10. What does negative skew suggest? | Skew âm gợi ý gì?**

A. A longer right tail | Đuôi phải dài hơn

B. A longer left tail | Đuôi trái dài hơn

C. Excess kurtosis | Kurtosis dư

D. A skewness statistic | Hệ số độ lệch phân phối

**Đáp án: B**

**Giải thích:** Giá trị nhỏ kéo đuôi về trái.


**Q11. What does Series.kurt() return? | Series.kurt() trả gì?**

A. A longer right tail | Đuôi phải dài hơn

B. A longer left tail | Đuôi trái dài hơn

C. Excess kurtosis | Kurtosis dư

D. A skewness statistic | Hệ số độ lệch phân phối

**Đáp án: C**

**Giải thích:** Pandas dùng quy ước kurtosis dư.


**Q12. What does Series.skew() return? | Series.skew() trả gì?**

A. A longer right tail | Đuôi phải dài hơn

B. A longer left tail | Đuôi trái dài hơn

C. Excess kurtosis | Kurtosis dư

D. A skewness statistic | Hệ số độ lệch phân phối

**Đáp án: D**

**Giải thích:** Nó ước lượng bất đối xứng từ mẫu.


**Q13. What is Q3−Q1 called? | Q3−Q1 gọi là gì?**

A. Interquartile range | Khoảng tứ phân vị

B. 3 | 3

C. 5 | 5

D. No; legitimate extremes may be flagged | Không; giá trị cực lớn hợp lệ vẫn có thể bị gắn cờ

**Đáp án: A**

**Giải thích:** Hiệu này chính là IQR.


**Q14. What is median of 1,3,5? | Median của 1,3,5 bằng gì?**

A. Interquartile range | Khoảng tứ phân vị

B. 3 | 3

C. 5 | 5

D. No; legitimate extremes may be flagged | Không; giá trị cực lớn hợp lệ vẫn có thể bị gắn cờ

**Đáp án: B**

**Giải thích:** Giá trị đứng giữa là ba.


**Q15. What is IQR if Q1=2 and Q3=7? | IQR nếu Q1=2, Q3=7 bằng bao nhiêu?**

A. Interquartile range | Khoảng tứ phân vị

B. 3 | 3

C. 5 | 5

D. No; legitimate extremes may be flagged | Không; giá trị cực lớn hợp lệ vẫn có thể bị gắn cờ

**Đáp án: C**

**Giải thích:** Bảy trừ hai bằng năm.


**Q16. Does an IQR outlier flag prove a measurement error? | Gắn cờ outlier theo IQR có chứng minh số đo sai không?**

A. Interquartile range | Khoảng tứ phân vị

B. 3 | 3

C. 5 | 5

D. No; legitimate extremes may be flagged | Không; giá trị cực lớn hợp lệ vẫn có thể bị gắn cờ

**Đáp án: D**

**Giải thích:** Ngưỡng chỉ là quy tắc sàng lọc.


**Q17. Why can quantile values differ between software packages? | Vì sao phân vị có thể khác giữa các phần mềm?**

A. Different interpolation conventions | Quy ước nội suy khác nhau

B. It concerns fourth moments and tails | Nó liên quan moment bậc bốn và đuôi

C. Median | Trung vị

D. Fit the imputation value on train only | Tính giá trị điền chỉ từ train

**Đáp án: A**

**Giải thích:** Mẫu nhỏ dễ cho thấy sự khác biệt quy ước.


**Q18. Why should you avoid interpreting high kurtosis only as a tall peak? | Vì sao không nên hiểu kurtosis cao chỉ là đỉnh cao?**

A. Different interpolation conventions | Quy ước nội suy khác nhau

B. It concerns fourth moments and tails | Nó liên quan moment bậc bốn và đuôi

C. Median | Trung vị

D. Fit the imputation value on train only | Tính giá trị điền chỉ từ train

**Đáp án: B**

**Giải thích:** Chỉ độ cao đỉnh không đủ diễn giải.


**Q19. What statistic is often robust for imputation with extreme values? | Thống kê nào thường phù hợp điền thiếu khi có ngoại lệ lớn?**

A. Different interpolation conventions | Quy ước nội suy khác nhau

B. It concerns fourth moments and tails | Nó liên quan moment bậc bốn và đuôi

C. Median | Trung vị

D. Fit the imputation value on train only | Tính giá trị điền chỉ từ train

**Đáp án: C**

**Giải thích:** Thứ tự khiến trung vị ít nhạy với cực trị.


**Q20. What is a crucial train/test rule when imputing missing values? | Quy tắc train/test quan trọng khi điền khuyết là gì?**

A. Different interpolation conventions | Quy ước nội suy khác nhau

B. It concerns fourth moments and tails | Nó liên quan moment bậc bốn và đuôi

C. Median | Trung vị

D. Fit the imputation value on train only | Tính giá trị điền chỉ từ train

**Đáp án: D**

**Giải thích:** Dữ liệu test không tham gia học tham số tiền xử lý.

## 8. Liên hệ bài kế tiếp

`Thống kê mô tả → Quantile/IQR → Outlier → Kiểm tra dữ liệu ML`.
