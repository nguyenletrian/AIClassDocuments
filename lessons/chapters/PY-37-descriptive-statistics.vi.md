# PY-37 — Thống kê mô tả: mean, median, mode, variance và std


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Mean** — trung bình; **Median** — trung vị.

`NumPy/Pandas → Thống kê mô tả → Outlier → ML`

**Học xong dùng để làm gì?** Tóm tắt bảng số bằng trung bình, trung vị, phương sai và độ lệch chuẩn để so sánh các nhóm.

**Kết nối kiến thức tiếp theo:** PY-38 dùng phân vị/IQR để tìm giá trị khác thường mà trung bình có thể che khuất.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Khái niệm |
|---|---|---|
| Mean | trung bình | Tổng giá trị chia số quan sát |
| Median | trung vị | Giá trị giữa sau khi sắp xếp |
| Variance | phương sai | Mức phân tán bình phương quanh trung bình |
| Standard deviation | độ lệch chuẩn | Căn bậc hai của phương sai, cùng đơn vị dữ liệu |

## 3. Hàm Python và tham số quan trọng

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm / cú pháp | Cách sử dụng |
|---|---|
| `np.mean()/np.median()` | Trung bình và trung vị, median bớt nhạy với giá trị cực lớn |
| `np.var(x,ddof=0/1)` | ddof=0 cho quần thể, ddof=1 cho mẫu |
| `np.std(x,ddof=0/1)` | Độ lệch chuẩn nhất quán quy ước ddof |
| `pd.Series.mode()/value_counts()` | Giá trị phổ biến và tần suất |

## 4. Khái niệm chính và liên quan

**Mạch kiến thức:** Khi có nhiều số đo, mean và median trả lời câu hỏi giá trị ở giữa; variance và std đo mức phân tán. Mode trả lời câu hỏi nhãn nào xuất hiện nhiều nhất. Cần biết đơn vị và đang tính theo quần thể hay mẫu.

### 4.1. Mean — Điểm cân bằng của các quan sát

**Từ vựng:** **Mean** — trung bình; **Observation** — quan sát.

**Mean** cộng các giá trị rồi chia cho số quan sát. Ba đơn giao trong 2, 3, 4 ngày có trung bình `(2+3+4)/3=3` ngày. Mean sử dụng **mọi giá trị**, nên có thể bị kéo lệch nếu có một đơn rất chậm. Phải đảm bảo các thời gian dùng cùng đơn vị; mean của các mã sản phẩm không có ý nghĩa.

**No Note — Không chú thích**

```python
import numpy as np

days = np.array([2, 3, 4])
print(float(np.mean(days)))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tính mean của ba số ngày để hiểu giá trị trung bình cộng.
# Dữ liệu: Ba số lượng ngày 2,3,4; mỗi phần tử là một quan sát cùng đơn vị ngày.
# NumPy tính các thống kê cơ bản trên list và mảng số.
import numpy as np

# Tạo ndarray một chiều ba lượt quan sát, không phải ma trận nhiều cột.
days = np.array([2, 3, 4])
# mean() cộng các quan sát rồi chia số lượt (3), trả 3.0 ngày; khác median hay mode.
# float() đổi scalar NumPy về số thực Python để in.
print(float(np.mean(days)))
```

**Kết quả khi chạy:**

```text
3.0
```

Thời gian trung bình ba đơn là 3 ngày, không có nghĩa đơn nào cũng giao đúng 3 ngày.

### 4.2. Median — Vị trí giữa sau khi xếp thứ tự

**Từ vựng:** **Median** — trung vị; **Outlier** — giá trị khác biệt lớn.

**Median** là số ở giữa khi dữ liệu được **sắp tăng dần**; nếu có số quan sát chẵn thì là trung bình hai số giữa. Với giá trị đơn hàng `[100,120,10000]` nghìn đồng, trung vị 120 nghìn, còn mean vượt 3.400 nghìn vì đơn 10.000 quá lớn. Median thường giúp mô tả giá trị trung tâm khi dữ liệu lệch, nhưng không thay thế việc kiểm tra liệu giá trị bất thường có hợp lệ.

**No Note — Không chú thích**

```python
import numpy as np

amounts = [100, 120, 10000]
print(float(np.median(amounts)))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tìm trung vị của ba số tiền, tránh để khoản rất lớn làm lệch điểm giữa.
# Dữ liệu: Ba hóa đơn 100,120,10000 nghìn đồng, hóa đơn cuối lớn bất thường.
# NumPy hỗ trợ trung vị qua median().
import numpy as np

# List ba số tiền; khoản 10.000 rất lớn nhưng không làm dịch vị trí phần tử giữa.
amounts = [100, 120, 10000]
# median() sắp giá trị rồi lấy điểm ở GIỮA, ở đây 120; với số lượt chẵn lấy trung bình hai ô giữa.
# float() ép kết quả về float Python cho print().
print(float(np.median(amounts)))
```

**Kết quả khi chạy:**

```text
120.0
```

Trung vị 120 nghìn đồng ít bị ảnh hưởng bởi đơn 10.000 nghìn đồng.

### 4.3. Variance — Sai khác bình phương quanh mean

**Từ vựng:** **Variance** — phương sai; **ddof** — số bậc tự do trừ đi.

Phương sai đo độ phân tán bằng **trung bình bình phương sai lệch so với mean**. Điểm `[6,8,10]` có mean 8, các lệch `[-2,0,2]`, bình phương `[4,0,4]`. Phương sai **quần thể** `ddof=0` bằng `8/3≈2.667` điểm². Nếu dùng để **ước lượng từ mẫu**, phương sai mẫu với `ddof=1` là `8/2=4` điểm². Cần nêu rõ đang dùng mẫu hay toàn bộ quần thể.

**No Note — Không chú thích**

```python
import numpy as np

scores = [6, 8, 10]
print(round(float(np.var(scores, ddof=0)), 3))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tính phương sai quần thể của ba điểm và giải thích tham số ddof=0.
# Dữ liệu: Ba điểm 6,8,10 trên cùng thang điểm; coi ba lượt là toàn bộ quần thể quan tâm.
# NumPy np.var() tính trung bình sai lệch bình phương với mean.
import numpy as np

# Ba quan sát cùng đơn vị điểm để tính mức phân tán.
scores = [6, 8, 10]
# var() tính phương sai; ddof=0 nghĩa chia cho N (quần thể). Nếu ước lượng từ mẫu thường dùng ddof=1 chia N−1; đơn vị là điểm².
# float() chuyển NumPy scalar sang float, round(...,3) làm tròn ba số thập phân khi in.
print(round(float(np.var(scores, ddof=0)), 3))
```

**Kết quả khi chạy:**

```text
2.667
```

Phương sai quần thể 2,667 điểm bình phương; không phải số điểm trung bình.

### 4.4. Standard deviation — Độ phân tán cùng đơn vị dữ liệu

**Từ vựng:** **Standard deviation** — độ lệch chuẩn; **Mode** — yếu vị.

**Standard deviation (std)** là căn bậc hai của phương sai, có **cùng đơn vị** với số đo. Cảm biến nhiệt độ đo `[20,21,19,20]` °C: mean=20 °C, std quần thể bằng `sqrt(0.5)≈0.707` °C. Trong khi đó **mode** là giá trị xuất hiện nhiều nhất, ở đây 20 °C hai lần; đây là câu hỏi về tần suất, không phải độ phân tán.

**No Note — Không chú thích**

```python
import numpy as np

celsius = [20, 21, 19, 20]
print(round(float(np.std(celsius, ddof=0)), 3))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tính độ lệch chuẩn quần thể để mô tả độ phân tán theo cùng đơn vị °C.
# Dữ liệu: Bốn nhiệt độ °C 20,21,19,20, coi là toàn bộ bốn quan sát cần tóm tắt.
# NumPy std() tính độ lệch chuẩn là căn bậc hai của phương sai.
import numpy as np

# Bốn lượt đo độ C, cùng đơn vị nên có thể tính độ phân tán.
celsius = [20, 21, 19, 20]
# std(ddof=0) lấy căn phương sai quần thể (chia N), kết quả cùng đơn vị °C; ddof=1 là ước lượng mẫu.
# float() đổi scalar, round(...,3) định dạng ba chữ số thập phân.
print(round(float(np.std(celsius, ddof=0)), 3))
```

**Kết quả khi chạy:**

```text
0.707
```

Độ lệch chuẩn 0,707 °C mô tả dao động nhiệt quanh mean 20 °C.

## 5. Năm tình huống thống kê mô tả — từ mean đến báo cáo dữ liệu thiếu

### Tình huống 1 — Cấp 1: Trung bình thời gian xử lý của 10 yêu cầu

**Từ vựng trong mục:** **Mean** — trung bình; **Observation** — một lượt quan sát.

**Tình huống thực tế:** Nhóm hỗ trợ có **10 phiếu yêu cầu**, mỗi phiếu ghi thời gian xử lý thực tế tính bằng **phút**. Các lượt mất từ **2 đến 5 phút** và dữ liệu gồm đủ mười phiếu trong ca thử nghiệm. Quản lý muốn biết **tổng số phút** đã dùng, **trung bình mỗi phiếu** và phiếu ngắn nhất/dài nhất để có bức tranh sơ bộ về khối lượng công việc; không được tưởng tất cả phiếu đều bằng thời gian trung bình.

**Vì sao chọn cách này?** **Thống kê mô tả** là cách tóm tắt những giá trị đã quan sát, chưa phải dự báo tương lai. `sum()` cho **tổng thời gian 10 phiếu**, đơn vị **phút**, còn `mean()` chia đều tổng ấy trên **10 phiếu** để mô tả một phiếu trung bình. `min()` và `max()` cho hai mức biên, giúp thấy có phiếu nhanh hơn hoặc chậm hơn mức trung bình. Cả mười số đo có cùng đơn vị nên có thể cộng được; đừng hiểu mean là thời gian cố định bắt buộc cho mọi yêu cầu.

**Quy trình:**
1. Lưu 10 số phút xử lý theo thứ tự yêu cầu.
2. Tính tổng, trung bình bằng NumPy.
3. So khoảng giá trị ngắn nhất và dài nhất.

**No Note — Không chú thích**

```python
import numpy as np
minutes = np.array([2,3,4,3,2,5,3,4,2,4], dtype=float)
if minutes.size != 10:
    raise ValueError("Cần đúng 10 yêu cầu.")
print("Yêu cầu:", minutes.size)
print("Tổng phút:", int(minutes.sum()))
print(f"Trung bình (phút): {minutes.mean():.1f}")
print("Nhỏ nhất/lớn nhất:", int(minutes.min()), int(minutes.max()))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Thống kê 10 thời gian xử lý: tổng phút, trung bình, nhỏ nhất và lớn nhất.
# Dữ liệu: 10 yêu cầu, mỗi số là số phút xử lý một yêu cầu.
# NumPy cung cấp mảng và thống kê sum/mean/min/max.
import numpy as np
# np.array(...,dtype=float) tạo vector 10 số phút, cho phép thống kê dạng số thực.
# dtype=float ép sang số thực, không làm thay đổi đơn vị phút.
minutes = np.array([2,3,4,3,2,5,3,4,2,4], dtype=float)
# size là SỐ PHẦN TỬ trong ndarray; với vector này đúng 10 yêu cầu.
if minutes.size != 10:
    # ValueError báo đầu vào không đủ 10 yêu cầu, không tiếp tục kết luận sai.
    raise ValueError("Cần đúng 10 yêu cầu.")
# size là SỐ PHẦN TỬ trong ndarray; với vector này đúng 10 yêu cầu.
print("Yêu cầu:", minutes.size)
# sum() cộng tổng số phút của mọi yêu cầu; int() đổi scalar sang số nguyên Python.
print("Tổng phút:", int(minutes.sum()))
# mean() tính thời gian trung bình mỗi yêu cầu; :.1f chỉ hiển thị một chữ số lẻ.
print(f"Trung bình (phút): {minutes.mean():.1f}")
# min() tìm yêu cầu nhanh nhất và max() tìm yêu cầu chậm nhất, không phải tổng.
# max() là thời gian chậm nhất, int() để in số nguyên.
print("Nhỏ nhất/lớn nhất:", int(minutes.min()), int(minutes.max()))
```

**Kết quả khi chạy:**

```text
Yêu cầu: 10
Tổng phút: 32
Trung bình (phút): 3.2
Nhỏ nhất/lớn nhất: 2 5
```

Trung bình 3,2 phút là kết quả trên đúng mười yêu cầu đã ghi, không phải cam kết thời gian giải quyết từng yêu cầu.

### Tình huống 2 — Cấp 2: So mean và median khi 12 hóa đơn có đơn rất lớn

**Từ vựng trong mục:** **Median** — trung vị; **Outlier** — giá trị khác biệt.

**Tình huống thực tế:** Cửa hàng ghi **12 hóa đơn**, mỗi dòng là tổng số tiền của một khách trong lần mua đó, tính bằng **nghìn đồng**. Mười một đơn trong khoảng **100–140 nghìn đồng**, nhưng một đơn hợp lệ lên tới **1.000 nghìn đồng**. Chủ cửa hàng muốn chọn con số mô tả mức chi tiêu thường gặp và xem vì sao **trung bình cộng** có thể khác **trung vị** rất nhiều mà không được xóa đơn lớn.

**Vì sao chọn cách này?** **Mean** là giá trị cân bằng từ **toàn bộ 12 khoản tiền**, nên một đơn 1.000 nghìn đồng kéo nó lên rõ rệt. **Median (trung vị)** là mức **nằm giữa danh sách đã sắp xếp**; với 12 giá trị, lấy mức giữa hai hóa đơn ở trung tâm, nên ít bị ảnh hưởng bởi một khoản lớn. `np.mean()` và `np.median()` trả hai cách nhìn khác nhau, đều có đơn vị **nghìn đồng**. Đơn lớn chưa chắc là sai; nếu tự xóa chỉ để mean đẹp hơn thì báo cáo không còn trung thực. Dùng cả hai chỉ số và nêu mục tiêu khi chọn số đại diện.

**Quy trình:**
1. Ghi đủ 12 hóa đơn, giữ cả đơn lớn.
2. Tính mean và median, đối chiếu sự khác biệt.
3. In số lượng đơn và giá trị lớn nhất.

**No Note — Không chú thích**

```python
import numpy as np
amounts = np.array([100,105,110,110,115,120,125,130,130,135,140,1000], dtype=float)
if len(amounts) != 12:
    raise ValueError("Cần đủ 12 hóa đơn.")
print("Hóa đơn:", len(amounts))
print(f"Mean (nghìn đồng): {amounts.mean():.2f}")
print(f"Median (nghìn đồng): {np.median(amounts):.2f}")
print("Đơn lớn nhất:", int(amounts.max()))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: So mean và median của 12 hóa đơn khi có một hóa đơn cực lớn.
# Dữ liệu: 12 hóa đơn nghìn đồng, trong đó 1000 là khoản lớn bất thường so 100..145.
# NumPy mean() và median() đo hai cách đại diện cho vị trí trung tâm.
import numpy as np
# Tạo vector 12 hóa đơn float, mỗi ô là một giá trị tiền nghìn đồng.
amounts = np.array([100,105,110,110,115,120,125,130,130,135,140,1000], dtype=float)
# len() đếm 12 hóa đơn, không phải tổng giá trị.
if len(amounts) != 12:
    # Dừng khi số hồ sơ không đúng kỳ vọng để tránh diễn giải sai.
    raise ValueError("Cần đủ 12 hóa đơn.")
# len() đếm 12 hóa đơn, không phải tổng giá trị.
print("Hóa đơn:", len(amounts))
# mean() cộng tiền chia 12, bị kéo lên bởi hóa đơn 1000; :.2f in hai chữ số lẻ.
print(f"Mean (nghìn đồng): {amounts.mean():.2f}")
# median() lấy điểm giữa sau sắp xếp, ít nhạy với một hóa đơn ngoại lệ.
print(f"Median (nghìn đồng): {np.median(amounts):.2f}")
# max() nhận giá trị lớn nhất của 12 hóa đơn; int() đổi sang số nguyên Python.
print("Đơn lớn nhất:", int(amounts.max()))
```

**Kết quả khi chạy:**

```text
Hóa đơn: 12
Mean (nghìn đồng): 193.33
Median (nghìn đồng): 122.50
Đơn lớn nhất: 1000
```

Median là trung bình của hai giá trị giữa vì có số hóa đơn chẵn; không phải trung bình 12 hóa đơn.

### Tình huống 3 — Cấp 3: Tìm mode của 15 lượt chọn sản phẩm

**Từ vựng trong mục:** **Mode** — giá trị phổ biến nhất; **Frequency** — số lần xuất hiện.

**Tình huống thực tế:** Quầy văn phòng phẩm ghi **15 lượt chọn nhóm hàng**, như Bút, Vở, Thước, Tẩy; mỗi lượt là **một lựa chọn** chứ không phải giá tiền. Nhân viên muốn biết nhóm nào được chọn nhiều nhất và có bao nhiêu lượt của nhóm đó, để chuẩn bị hàng lên kệ. Họ không thể cộng chữ 'Bút' với chữ 'Vở' rồi tính trung bình số học.

**Vì sao chọn cách này?** **Mode (mốt)** là **giá trị hoặc nhãn xuất hiện nhiều nhất**. Vì đây là dữ liệu **phân loại** (tên nhóm hàng), `pd.Series(...).value_counts()` đếm số lượt theo từng nhãn; dòng có số đếm cao nhất cho biết nhóm được chọn nhiều nhất. **Mean** và phương sai đòi dữ liệu số có ý nghĩa tính toán, không phù hợp với chữ 'Bút' hay 'Tẩy'. Một nhãn được chọn nhiều nhất trong đúng **15 lượt mẫu** chưa đủ chứng minh nó luôn bán chạy nhất trong mọi ca.

**Quy trình:**
1. Ghi 15 nhãn sản phẩm theo thứ tự lượt.
2. Đếm tần suất bằng Series.
3. Sắp tần suất giảm và in nhãn nhiều nhất.

**No Note — Không chú thích**

```python
import pandas as pd
categories = ["Bút","Vở","Bút","Thước","Bút","Tẩy","Vở","Bút","Thước","Vở","Bút","Vở","Tẩy","Bút","Thước"]
counts = pd.Series(categories).value_counts()
if len(categories) != 15:
    raise ValueError("Cần đủ 15 lượt chọn sản phẩm.")
print("Lượt chọn:", len(categories))
print("Nhãn khác nhau:", len(counts))
print("Mode:", counts.index[0])
print("Số lượt mode:", int(counts.iloc[0]))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Dùng mode để tìm loại mặt hàng được chọn phổ biến nhất trong 15 lượt.
# Dữ liệu: 15 lựa chọn Bút/Vở/Thước/Tẩy; mỗi lượt là một phiếu chọn, có nhãn lặp.
# Pandas Series chứa dãy nhãn và value_counts() đếm từng loại.
import pandas as pd
# List 15 tên sản phẩm, nhãn trùng có nghĩa nhiều lượt chọn.
categories = ["Bút","Vở","Bút","Thước","Bút","Tẩy","Vở","Bút","Thước","Vở","Bút","Vở","Tẩy","Bút","Thước"]
# Series() đổi list thành chuỗi Pandas; value_counts() đếm số lần mỗi nhãn, mặc định xếp theo tần suất GIẢM DẦN.
counts = pd.Series(categories).value_counts()
# len() đếm 15 phiếu chọn; khác len(counts) là số nhãn KHÁC NHAU.
if len(categories) != 15:
    # Báo lỗi khi chưa đủ 15 phiếu chọn.
    raise ValueError("Cần đủ 15 lượt chọn sản phẩm.")
# len() đếm 15 phiếu chọn; khác len(counts) là số nhãn KHÁC NHAU.
print("Lượt chọn:", len(categories))
# Đếm loại sản phẩm đã xuất hiện, không phải tổng lượt.
print("Nhãn khác nhau:", len(counts))
# index là danh sách nhãn của Series đếm, [0] lấy nhãn tần suất cao nhất (mode), không phải giá trị số.
print("Mode:", counts.index[0])
# iloc[0] lấy GIÁ TRỊ SỐ ĐẾM đầu tiên theo vị trí; int() chuyển sang số nguyên Python.
print("Số lượt mode:", int(counts.iloc[0]))
```

**Kết quả khi chạy:**

```text
Lượt chọn: 15
Nhãn khác nhau: 4
Mode: Bút
Số lượt mode: 6
```

Mode cho biết nhãn thường thấy nhất **trong 15 lượt**, không kết luận sản phẩm ấy sẽ được chọn nhiều nhất trong mọi ca.

### Tình huống 4 — Cấp 4: Phân biệt phương sai mẫu và quần thể trên 18 nhiệt độ

**Từ vựng trong mục:** **Variance** — phương sai; **Standard deviation** — độ lệch chuẩn; **ddof** — hiệu chỉnh mẫu.

**Tình huống thực tế:** Phòng máy có **18 lượt đo nhiệt độ**, tính bằng **°C**. Kỹ thuật viên muốn biết nhiệt độ **dao động quanh trung bình** nhiều hay ít. Họ muốn so hai cách tính: nếu 18 lượt là **toàn bộ dữ liệu của ca này** và nếu chúng chỉ là **mẫu để ước lượng các ca tương tự**, đồng thời đổi kết quả dao động về đơn vị °C để dễ đọc.

**Vì sao chọn cách này?** **Phương sai** mô tả mức các số đo phân tán quanh trung bình, bằng cách dùng **độ lệch đã bình phương**; vì nhiệt độ tính bằng °C nên phương sai có đơn vị **°C²**. **Độ lệch chuẩn** là căn của phương sai để trở về **°C**, dễ so với chênh lệch nhiệt độ trong thực tế hơn. `ddof=0` dùng mẫu số theo **18 lượt như toàn bộ nhóm đang xét**; `ddof=1` dùng **hiệu chỉnh khi 18 lượt là mẫu ước lượng phương sai quần thể**, nên với cùng dữ liệu thường cho phương sai lớn hơn một chút. Chọn `ddof` theo câu hỏi thống kê, không tùy chọn chỉ để ra con số mong muốn.

**Quy trình:**
1. Lưu 18 nhiệt độ và ghi rõ đơn vị °C.
2. Tính phương sai với hai quy ước ddof=0 và ddof=1.
3. Tính std mẫu và kiểm phương sai mẫu lớn hơn phương sai quần thể.

**No Note — Không chú thích**

```python
import numpy as np
celsius = np.array([18,19,20,21,22,23,24,25,26,27,18,19,20,21,22,23,24,25], dtype=float)
pop_var = np.var(celsius, ddof=0)
sample_var = np.var(celsius, ddof=1)
if len(celsius) != 18:
    raise ValueError("Cần đủ 18 lượt đo nhiệt độ.")
print("Lượt đo:", len(celsius))
print(f"Phương sai quần thể (°C²): {pop_var:.3f}")
print(f"Phương sai mẫu (°C²): {sample_var:.3f}")
print(f"Std mẫu (°C): {np.std(celsius, ddof=1):.3f}")
print("Hiệu chỉnh làm tăng phương sai:", bool(sample_var > pop_var))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: So phương sai quần thể và phương sai mẫu của 18 nhiệt độ, giải thích ddof.
# Dữ liệu: 18 số đo °C; ddof=0 chia N, ddof=1 chia N−1 vì ước lượng từ mẫu.
# NumPy cung cấp var() và std() với tùy chọn ddof (bậc tự do trừ đi).
import numpy as np
# Tạo vector 18 nhiệt độ kiểu float, đơn vị °C.
celsius = np.array([18,19,20,21,22,23,24,25,26,27,18,19,20,21,22,23,24,25], dtype=float)
# ddof=0 chia tổng bình phương sai lệch cho N=18, phù hợp phương sai quần thể quan sát.
pop_var = np.var(celsius, ddof=0)
# ddof=1 chia N−1=17, là phương sai mẫu điều chỉnh nên thường lớn hơn khi dữ liệu biến thiên.
sample_var = np.var(celsius, ddof=1)
# len() kiểm đủ 18 lượt đo.
if len(celsius) != 18:
    # Báo dữ liệu nhiệt độ thiếu/không đúng số lượt.
    raise ValueError("Cần đủ 18 lượt đo nhiệt độ.")
# len() kiểm đủ 18 lượt đo.
print("Lượt đo:", len(celsius))
print(f"Phương sai quần thể (°C²): {pop_var:.3f}")
print(f"Phương sai mẫu (°C²): {sample_var:.3f}")
# std() lấy căn của phương sai mẫu ddof=1, trở lại đơn vị °C (khác phương sai °C²).
print(f"Std mẫu (°C): {np.std(celsius, ddof=1):.3f}")
# So hai giá trị; hiệu chỉnh ddof=1 tăng ước lượng so ddof=0 với N>1 và phương sai dương.
# bool() đổi kết quả so sánh thành True/False Python khi in.
print("Hiệu chỉnh làm tăng phương sai:", bool(sample_var > pop_var))
```

**Kết quả khi chạy:**

```text
Lượt đo: 18
Phương sai quần thể (°C²): 7.164
Phương sai mẫu (°C²): 7.585
Std mẫu (°C): 2.754
Hiệu chỉnh làm tăng phương sai: True
```

Khác biệt do **quy ước đang thống kê toàn bộ hay ước lượng từ mẫu**; bản thân 18 số đo không đổi.

### Tình huống 5 — Cấp 5: Báo cáo mô tả 20 thời gian giao có một bản ghi thiếu

**Từ vựng trong mục:** **Missingness** — dữ liệu thiếu; **Describe** — bảng mô tả; **Median** — trung vị.

**Tình huống thực tế:** Đơn vị vận chuyển thu **20 phiếu thời gian giao**, đơn vị **phút**, nhưng **phiếu thứ 20** chưa được điền nên lưu `None`. Người quản lý cần giữ đủ **20 phiếu gốc**, đếm được **19 phiếu có thời gian** và **1 phiếu thiếu**, rồi tính trung bình, trung vị và độ lệch chuẩn từ đúng 19 phiếu có số. Phiếu thiếu không có nghĩa người giao mất 0 phút.

**Vì sao chọn cách này?** `None` hoặc **NaN** nghĩa là **chưa biết thời gian**, khác 0 phút là một số đo cụ thể. `pd.Series(raw, dtype='float64')` giữ được cả những giá trị có số và ô thiếu; `dropna()` tạo danh sách **19 giá trị hợp lệ** để tính, còn `isna()` đếm **một phiếu chưa ghi**. `mean()` tính thời gian bình quân, `median()` là mức giữa và `std(ddof=1)` cho độ lệch chuẩn mẫu, tất cả đều dựa trên dữ liệu có số. Không xóa phiếu thiếu khỏi báo cáo gốc hoặc thay bằng 0, vì như vậy có thể làm thời gian trung bình thấp đi và giấu mất việc cần bổ sung dữ liệu.

**Quy trình:**
1. Tạo 20 dòng và đổi giá trị thiếu thành NaN.
2. Đếm missing trước khi tính và lấy danh sách có số.
3. Tính mean, median, sample std có đơn vị.

**No Note — Không chú thích**

```python
import pandas as pd
raw = [20,21,22,22,23,24,24,25,26,27,21,22,23,24,25,26,27,28,29,None]
data = pd.Series(raw, dtype="float64")
valid = data.dropna()
if len(data) != 20:
    raise ValueError("Cần đủ 20 phiếu ghi thời gian, kể cả lượt thiếu.")
print("Phiếu:", len(data))
print("Đủ thời gian:", len(valid))
print("Thiếu:", int(data.isna().sum()))
print(f"Mean (phút): {valid.mean():.2f}")
print(f"Median (phút): {valid.median():.2f}")
print(f"Std mẫu (phút): {valid.std(ddof=1):.2f}")
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Làm sạch một thời gian thiếu rồi tính mean, median và độ lệch chuẩn mẫu của 19 lượt hợp lệ.
# Dữ liệu: 20 phiếu thời gian tính phút; một None là lượt thiếu, không phải thời gian 0.
# Pandas Series hỗ trợ missing values, dropna và thống kê có ddof.
import pandas as pd
# 20 lượt, có một None đại diện chưa ghi thời gian.
raw = [20,21,22,22,23,24,24,25,26,27,21,22,23,24,25,26,27,28,29,None]
# Series() tạo dãy số, dtype='float64' cho phép lưu NaN bên cạnh số thực.
data = pd.Series(raw, dtype="float64")
# dropna() trả Series chỉ gồm 19 lượt có số, mặc định KHÔNG sửa data gốc và không đổi None thành 0.
valid = data.dropna()
# len() vẫn bằng 20 phiếu gồm cả lượt thiếu, khác len(valid)=19.
if len(data) != 20:
    # Dừng nếu số phiếu gốc khác 20, không nhầm số phiếu với số hợp lệ.
    raise ValueError("Cần đủ 20 phiếu ghi thời gian, kể cả lượt thiếu.")
# len() vẫn bằng 20 phiếu gồm cả lượt thiếu, khác len(valid)=19.
print("Phiếu:", len(data))
print("Đủ thời gian:", len(valid))
# isna() đánh dấu ô thiếu True, sum() đếm số phiếu thiếu; int() chuyển số về Python.
print("Thiếu:", int(data.isna().sum()))
# mean() lấy thời gian trung bình trong 19 lượt hợp lệ, đơn vị phút.
print(f"Mean (phút): {valid.mean():.2f}")
# median() tìm thời gian ở giữa dãy hợp lệ đã xếp.
print(f"Median (phút): {valid.median():.2f}")
# std(ddof=1) tính độ lệch chuẩn MẪU, chia N−1 trong phương sai, đơn vị phút; :.2f chỉ định dạng khi in.
print(f"Std mẫu (phút): {valid.std(ddof=1):.2f}")
```

**Kết quả khi chạy:**

```text
Phiếu: 20
Đủ thời gian: 19
Thiếu: 1
Mean (phút): 24.16
Median (phút): 24.00
Std mẫu (phút): 2.54
```

Trung bình mô tả 19 phiếu có số, **không đại diện** cho phiếu thiếu nếu lý do thiếu liên quan đến thời gian giao.

## 6. Sai lầm thường gặp

- Mean bị ảnh hưởng bởi ngoại lệ cực lớn; median thường bền hơn nhưng không phát hiện lỗi thay cho việc kiểm tra dữ liệu.
- `ddof=0` chia cho n; `ddof=1` chia cho n−1 và cần ít nhất hai quan sát để có ước lượng mẫu.
- Variance mang đơn vị bình phương; std mang đơn vị gốc.
- Mode/value_counts dành cho nhãn phân loại; không lấy trung bình của mã chữ.
- Đừng diễn giải std của quan sát thành sai số chuẩn của trung bình mẫu.
- Đổi dữ liệu về cùng đơn vị trước khi tính thống kê.

## 7. Trắc nghiệm

**Q1. What does mean calculate? | Mean tính gì?**

A. Sum divided by observation count | Tổng chia số quan sát

B. Middle ranked value after sorting | Giá trị ở giữa sau khi sắp

C. Squared dispersion around the mean | Độ phân tán bình phương quanh mean

D. Spread in original measurement units | Độ phân tán cùng đơn vị gốc

**Đáp án: A**

**Giải thích:** Mọi quan sát góp vào trung bình.


**Q2. What is median? | Median là gì?**

A. Sum divided by observation count | Tổng chia số quan sát

B. Middle ranked value after sorting | Giá trị ở giữa sau khi sắp

C. Squared dispersion around the mean | Độ phân tán bình phương quanh mean

D. Spread in original measurement units | Độ phân tán cùng đơn vị gốc

**Đáp án: B**

**Giải thích:** Trung vị dựa trên thứ tự, không dựa trên tổng độ lớn.


**Q3. What does variance measure? | Variance đo gì?**

A. Sum divided by observation count | Tổng chia số quan sát

B. Middle ranked value after sorting | Giá trị ở giữa sau khi sắp

C. Squared dispersion around the mean | Độ phân tán bình phương quanh mean

D. Spread in original measurement units | Độ phân tán cùng đơn vị gốc

**Đáp án: C**

**Giải thích:** Nó lấy trung bình bình phương độ lệch.


**Q4. What does standard deviation measure? | Std đo gì?**

A. Sum divided by observation count | Tổng chia số quan sát

B. Middle ranked value after sorting | Giá trị ở giữa sau khi sắp

C. Squared dispersion around the mean | Độ phân tán bình phương quanh mean

D. Spread in original measurement units | Độ phân tán cùng đơn vị gốc

**Đáp án: D**

**Giải thích:** Std là căn bậc hai phương sai.


**Q5. What is the median of [1, 2, 3, 10, 10]? | Trung vị của [1, 2, 3, 10, 10] bằng bao nhiêu?**

A. 2 | 2

B. 5 | 5

C. 3 | 3

D. 10 | 10

**Đáp án: C**

**Giải thích:** Dữ liệu đã tăng dần, có 5 số nên trung vị là số thứ ba: 3.


**Q6. A score is 80, the mean is 60, and standard deviation is 10. What is the z-score? | Điểm số là 80, trung bình 60, độ lệch chuẩn 10. Điểm z là bao nhiêu?**

A. 1 | 1

B. 2 | 2

C. 4 | 4

D. 20 | 20

**Đáp án: B**

**Giải thích:** z = (80 − 60)/10 = 2, nghĩa là cao hơn trung bình hai độ lệch chuẩn.


**Q7. What is the mean of [2, 4, 9]? | Giá trị trung bình của [2, 4, 9] là bao nhiêu?**

A. 5 | 5

B. 4 | 4

C. 6 | 6

D. 15 | 15

**Đáp án: A**

**Giải thích:** Cộng các giá trị 2 + 4 + 9 = 15 rồi chia cho 3 quan sát: mean = 5.


**Q8. When is the population standard deviation equal to zero? | Khi nào độ lệch chuẩn của tổng thể bằng 0?**

A. When the mean is zero | Khi trung bình bằng 0

B. When all values are positive | Khi tất cả số đều dương

C. When the sample is large | Khi mẫu lớn

D. When all observations are equal | Khi tất cả quan sát bằng nhau

**Đáp án: D**

**Giải thích:** Nếu tất cả giá trị giống nhau, không có độ lệch khỏi trung bình, nên phương sai và độ lệch chuẩn đều bằng 0.


**Q9. What is mean of 2,3,4? | Mean của 2,3,4 là bao nhiêu?**

A. 3 | 3

B. 4 | 4

C. 2/3 | 2/3

D. 1 | 1

**Đáp án: A**

**Giải thích:** Tổng 9 chia 3 bằng 3.


**Q10. What is median of 2,4,100? | Median của 2,4,100 là bao nhiêu?**

A. 3 | 3

B. 4 | 4

C. 2/3 | 2/3

D. 1 | 1

**Đáp án: B**

**Giải thích:** Bốn nằm giữa dãy đã sắp.


**Q11. What is population variance of 1,2,3? | Phương sai quần thể của 1,2,3 là gì?**

A. 3 | 3

B. 4 | 4

C. 2/3 | 2/3

D. 1 | 1

**Đáp án: C**

**Giải thích:** Bình phương lệch là 1,0,1 rồi chia ba.


**Q12. What is sample variance of 1,2,3? | Phương sai mẫu của 1,2,3 là gì?**

A. 3 | 3

B. 4 | 4

C. 2/3 | 2/3

D. 1 | 1

**Đáp án: D**

**Giải thích:** Tổng bình phương 2 chia n−1=2.


**Q13. What unit does variance have? | Variance có đơn vị gì?**

A. Squared input units | Bình phương đơn vị dữ liệu

B. Original input units | Đơn vị gốc của dữ liệu

C. Median | Trung vị

D. Mode | Yếu vị

**Đáp án: A**

**Giải thích:** Bình phương lệch làm bình phương đơn vị.


**Q14. What unit does std have? | Std có đơn vị gì?**

A. Squared input units | Bình phương đơn vị dữ liệu

B. Original input units | Đơn vị gốc của dữ liệu

C. Median | Trung vị

D. Mode | Yếu vị

**Đáp án: B**

**Giải thích:** Lấy căn đưa về đơn vị ban đầu.


**Q15. Which statistic resists large outliers better? | Thống kê nào ít nhạy với ngoại lệ cực lớn hơn?**

A. Squared input units | Bình phương đơn vị dữ liệu

B. Original input units | Đơn vị gốc của dữ liệu

C. Median | Trung vị

D. Mode | Yếu vị

**Đáp án: C**

**Giải thích:** Giá trị cực lớn ít tác động vị trí giữa.


**Q16. Which statistic is useful for categorical labels? | Thống kê nào phù hợp nhãn phân loại?**

A. Squared input units | Bình phương đơn vị dữ liệu

B. Original input units | Đơn vị gốc của dữ liệu

C. Median | Trung vị

D. Mode | Yếu vị

**Đáp án: D**

**Giải thích:** Lấy trung bình mã chữ không có ý nghĩa số học.


**Q17. Does std equal standard error? | Std có giống sai số chuẩn không?**

A. No, std measures spread of individual values | Không, std đo độ phân tán quan sát

B. Yes, large outliers can pull it up | Có, ngoại lệ lớn kéo mean lên

C. Different denominators give different results | Mẫu số khác nhau cho kết quả khác

D. Summary statistics can lose meaning | Thống kê tổng hợp có thể mất ý nghĩa

**Đáp án: A**

**Giải thích:** SE đo độ biến thiên của thống kê ước lượng.


**Q18. Can mean lie above most observations? | Mean có thể lớn hơn phần lớn quan sát không?**

A. No, std measures spread of individual values | Không, std đo độ phân tán quan sát

B. Yes, large outliers can pull it up | Có, ngoại lệ lớn kéo mean lên

C. Different denominators give different results | Mẫu số khác nhau cho kết quả khác

D. Summary statistics can lose meaning | Thống kê tổng hợp có thể mất ý nghĩa

**Đáp án: B**

**Giải thích:** Mean phụ thuộc tổng các giá trị.


**Q19. Why state ddof when reporting variance? | Vì sao báo ddof khi trình bày phương sai?**

A. No, std measures spread of individual values | Không, std đo độ phân tán quan sát

B. Yes, large outliers can pull it up | Có, ngoại lệ lớn kéo mean lên

C. Different denominators give different results | Mẫu số khác nhau cho kết quả khác

D. Summary statistics can lose meaning | Thống kê tổng hợp có thể mất ý nghĩa

**Đáp án: C**

**Giải thích:** Quy ước mẫu và quần thể khác nhau.


**Q20. What happens if values use mismatched units? | Nếu số liệu dùng đơn vị không thống nhất thì sao?**

A. No, std measures spread of individual values | Không, std đo độ phân tán quan sát

B. Yes, large outliers can pull it up | Có, ngoại lệ lớn kéo mean lên

C. Different denominators give different results | Mẫu số khác nhau cho kết quả khác

D. Summary statistics can lose meaning | Thống kê tổng hợp có thể mất ý nghĩa

**Đáp án: D**

**Giải thích:** Cần thống nhất đơn vị trước khi tính.

## 8. Liên hệ bài tiếp theo

`NumPy/Pandas → Thống kê mô tả → Outlier → ML`.
