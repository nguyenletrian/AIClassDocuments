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

```python
# Mục đích: Điểm cân bằng của các quan sát.
import numpy as np

days = np.array([2, 3, 4])
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

```python
# Mục đích: Vị trí giữa sau khi xếp thứ tự.
import numpy as np

amounts = [100, 120, 10000]
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

```python
# Mục đích: Sai khác bình phương quanh mean.
import numpy as np

scores = [6, 8, 10]
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

```python
# Mục đích: Độ phân tán cùng đơn vị dữ liệu.
import numpy as np

celsius = [20, 21, 19, 20]
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

**Tình huống thực tế:** Nhân viên đo thời gian xử lý **10 yêu cầu hỗ trợ**, mỗi hàng một yêu cầu và thời gian tính bằng phút. Cần tổng số phút, trung bình mỗi yêu cầu và thời gian ngắn nhất/dài nhất để ước lượng công việc trong ca.

**Vì sao chọn cách này?** Mean gộp **toàn bộ 10 thời gian có cùng đơn vị**; thống kê min/max giúp không lầm rằng mọi yêu cầu đều mất thời gian bằng mean.

**Quy trình:**
1. Lưu 10 số phút xử lý theo thứ tự yêu cầu.
2. Tính tổng, trung bình bằng NumPy.
3. So khoảng giá trị ngắn nhất và dài nhất.

```python
import numpy as np
minutes = np.array([2,3,4,3,2,5,3,4,2,4], dtype=float)
assert minutes.size == 10
print("Yêu cầu:", minutes.size)
print("Tổng phút:", int(minutes.sum()))
print(f"Trung bình (phút): {minutes.mean():.1f}")
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

**Tình huống thực tế:** Một cửa hàng có **12 hóa đơn**, mỗi dòng là thành tiền của một đơn, đơn vị nghìn đồng. Có một hóa đơn 1.000 nghìn đồng hợp lệ, cao hơn hẳn 11 đơn còn lại. Muốn có chỉ số đại diện cho mức chi phổ biến, quản lý cần xem **cả mean lẫn median**, không tự xóa đơn lớn.

**Vì sao chọn cách này?** Mean sử dụng mọi số và bị kéo về phía hóa đơn lớn; median chọn vị trí giữa đã sắp nên ít biến động khi có một giá trị cực cao. Hai chỉ số phản ánh **hai cách mô tả khác nhau**, không có cái nào luôn đúng hơn.

**Quy trình:**
1. Ghi đủ 12 hóa đơn, giữ cả đơn lớn.
2. Tính mean và median, đối chiếu sự khác biệt.
3. In số lượng đơn và giá trị lớn nhất.

```python
import numpy as np
amounts = np.array([100,105,110,110,115,120,125,130,130,135,140,1000], dtype=float)
assert len(amounts) == 12
print("Hóa đơn:", len(amounts))
print(f"Mean (nghìn đồng): {amounts.mean():.2f}")
print(f"Median (nghìn đồng): {np.median(amounts):.2f}")
print("Đơn lớn nhất:", int(amounts.max()))
```

**Kết quả khi chạy:**

```text
Hóa đơn: 12
Mean (nghìn đồng): 201.67
Median (nghìn đồng): 122.50
Đơn lớn nhất: 1000
```

Median là trung bình của hai giá trị giữa vì có số hóa đơn chẵn; không phải trung bình 12 hóa đơn.

### Tình huống 3 — Cấp 3: Tìm mode của 15 lượt chọn sản phẩm

**Từ vựng trong mục:** **Mode** — giá trị phổ biến nhất; **Frequency** — số lần xuất hiện.

**Tình huống thực tế:** Quầy văn phòng phẩm ghi **15 lượt chọn sản phẩm**, mỗi hàng là nhãn nhóm sản phẩm như Bút, Vở, Thước hoặc Tẩy. Nhân viên cần biết loại nào được chọn nhiều nhất, đồng thời báo lượt chọn của từng loại. Không tính mean của nhãn vì nhãn không phải đại lượng số.

**Vì sao chọn cách này?** `value_counts()` đếm số lượt mỗi nhãn, `mode()` hoặc dòng đầu của bảng tần suất cho nhãn nhiều nhất. Đây là bài toán nhãn phân loại, không dùng phương sai hay trung bình.

**Quy trình:**
1. Ghi 15 nhãn sản phẩm theo thứ tự lượt.
2. Đếm tần suất bằng Series.
3. Sắp tần suất giảm và in nhãn nhiều nhất.

```python
import pandas as pd
categories = ["Bút","Vở","Bút","Thước","Bút","Tẩy","Vở","Bút","Thước","Vở","Bút","Vở","Tẩy","Bút","Thước"]
counts = pd.Series(categories).value_counts()
assert len(categories) == 15
print("Lượt chọn:", len(categories))
print("Nhãn khác nhau:", len(counts))
print("Mode:", counts.index[0])
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

**Tình huống thực tế:** Phòng máy đo **18 lần nhiệt độ** (°C), mỗi hàng một lượt. Nếu xem đây là **toàn bộ ca** thì dùng phương sai quần thể `ddof=0`; nếu xem đây là mẫu để ước lượng ca tương tự thì dùng `ddof=1`. Hãy tính cả hai và độ lệch chuẩn của mẫu để thấy mẫu số khác nhau.

**Vì sao chọn cách này?** Phương sai bình phương các sai lệch nên có đơn vị °C²; độ lệch chuẩn lấy căn để trở về °C. Nêu rõ ddof giúp người đọc không lấy hai kết quả khác nhau làm lỗi code.

**Quy trình:**
1. Lưu 18 nhiệt độ và ghi rõ đơn vị °C.
2. Tính phương sai với hai quy ước ddof=0 và ddof=1.
3. Tính std mẫu và kiểm phương sai mẫu lớn hơn phương sai quần thể.

```python
import numpy as np
celsius = np.array([18,19,20,21,22,23,24,25,26,27,18,19,20,21,22,23,24,25], dtype=float)
pop_var = np.var(celsius, ddof=0)
sample_var = np.var(celsius, ddof=1)
assert len(celsius) == 18
print("Lượt đo:", len(celsius))
print(f"Phương sai quần thể (°C²): {pop_var:.3f}")
print(f"Phương sai mẫu (°C²): {sample_var:.3f}")
print(f"Std mẫu (°C): {np.std(celsius, ddof=1):.3f}")
print("Hiệu chỉnh làm tăng phương sai:", bool(sample_var > pop_var))
```

**Kết quả khi chạy:**

```text
Lượt đo: 18
Phương sai quần thể (°C²): 6.917
Phương sai mẫu (°C²): 7.324
Std mẫu (°C): 2.706
Hiệu chỉnh làm tăng phương sai: True
```

Khác biệt do **quy ước đang thống kê toàn bộ hay ước lượng từ mẫu**; bản thân 18 số đo không đổi.

### Tình huống 5 — Cấp 5: Báo cáo mô tả 20 thời gian giao có một bản ghi thiếu

**Từ vựng trong mục:** **Missingness** — dữ liệu thiếu; **Describe** — bảng mô tả; **Median** — trung vị.

**Tình huống thực tế:** Nhà vận chuyển có **20 phiếu giao**, mỗi phiếu một thời gian xử lý (phút); phiếu cuối chưa ghi nên là `None`, **không phải 0 phút**. Cần lập thống kê cho 19 phiếu có số, đếm riêng một phiếu thiếu, so mean/median và phương sai mẫu. Không bỏ cả phiếu khỏi tổng số bản ghi.

**Vì sao chọn cách này?** Chuyển thiếu sang NaN rồi dùng `dropna()` hoặc `describe()` giữ số phiếu nguồn và số có dữ liệu tách biệt. Phương sai mẫu chỉ tính trên 19 giá trị, tránh kéo mean xuống do điền 0 sai.

**Quy trình:**
1. Tạo 20 dòng và đổi giá trị thiếu thành NaN.
2. Đếm missing trước khi tính và lấy danh sách có số.
3. Tính mean, median, sample std có đơn vị.

```python
import pandas as pd
raw = [20,21,22,22,23,24,24,25,26,27,21,22,23,24,25,26,27,28,29,None]
data = pd.Series(raw, dtype="float64")
valid = data.dropna()
assert len(data) == 20
print("Phiếu:", len(data))
print("Đủ thời gian:", len(valid))
print("Thiếu:", int(data.isna().sum()))
print(f"Mean (phút): {valid.mean():.2f}")
print(f"Median (phút): {valid.median():.2f}")
print(f"Std mẫu (phút): {valid.std(ddof=1):.2f}")
```

**Kết quả khi chạy:**

```text
Phiếu: 20
Đủ thời gian: 19
Thiếu: 1
Mean (phút): 24.16
Median (phút): 24.00
Std mẫu (phút): 2.58
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


**Q5. What is mode? | Mode là gì?**

A. Most frequent observed value | Giá trị xuất hiện nhiều nhất

B. Divide sum of squares by n | Chia tổng bình phương cho n

C. Divide by n−1 | Chia cho n−1

D. Frequency per distinct label | Tần suất từng nhãn khác nhau

**Đáp án: A**

**Giải thích:** Yếu vị dùng được cho nhãn lẫn số.


**Q6. What is ddof=0 in np.var? | ddof=0 trong np.var là gì?**

A. Most frequent observed value | Giá trị xuất hiện nhiều nhất

B. Divide sum of squares by n | Chia tổng bình phương cho n

C. Divide by n−1 | Chia cho n−1

D. Frequency per distinct label | Tần suất từng nhãn khác nhau

**Đáp án: B**

**Giải thích:** Nó tính phương sai theo quy ước quần thể.


**Q7. What is ddof=1 for sample variance? | ddof=1 dùng cho gì?**

A. Most frequent observed value | Giá trị xuất hiện nhiều nhất

B. Divide sum of squares by n | Chia tổng bình phương cho n

C. Divide by n−1 | Chia cho n−1

D. Frequency per distinct label | Tần suất từng nhãn khác nhau

**Đáp án: C**

**Giải thích:** Đó là ước lượng phương sai mẫu thông dụng.


**Q8. What does value_counts() produce? | value_counts() tạo gì?**

A. Most frequent observed value | Giá trị xuất hiện nhiều nhất

B. Divide sum of squares by n | Chia tổng bình phương cho n

C. Divide by n−1 | Chia cho n−1

D. Frequency per distinct label | Tần suất từng nhãn khác nhau

**Đáp án: D**

**Giải thích:** Nó đếm lượt xuất hiện của từng nhãn.


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
