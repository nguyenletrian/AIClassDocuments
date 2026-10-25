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

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Trung bình thời gian giao ba đơn · Cấp 1: Mean cơ bản

**Tình huống thực tế:** Ba đơn hàng có thời gian giao lần lượt 2,3,4 ngày, theo cùng quy định đo. Quản lý muốn một chỉ số đại diện mức thời gian giao trung bình.

**Vì sao chọn cách giải này?** Mean phù hợp khi cần tổng thời gian trên mỗi đơn và dữ liệu không có ngoại lệ lớn.

**Quy trình giải:**

1. Đưa ba thời gian theo ngày vào một mảng.
2. Tính trung bình bằng `np.mean`.
3. In kết quả, chú ý không phải mọi đơn đều bằng mean.

```python
# Mục đích: Trung bình thời gian giao ba đơn.
import numpy as np

days = np.array([2, 3, 4])
print(float(np.mean(days)))
```

**Kết quả khi chạy:**

```text
3.0
```

Trung bình ba đơn là 3 ngày.

**Bài thực hành nâng cấp — cấp 1/5:** Ứng dụng thống kê **10 ngày sử dụng**; mỗi hàng là số phút hoạt động trong một ngày. Hãy tính mean của 10 ngày sử dụng ứng dụng. Các cấp tăng số ngày đồng thời đưa thêm số đo thiếu để thấy sự khác biệt giữa thống kê dữ liệu hợp lệ và thống kê nhầm cả giá trị thiếu.

```python
import numpy as np
import pandas as pd
# Mỗi phần tử là số phút ứng dụng được sử dụng trong một ngày.
values = np.array([35, 44, 53, 56, 65, 74, 77, 86, 95, 98],dtype=float)
valid = values[np.isfinite(values)]
result = round(float(valid.mean()),2)
print("Số ngày:",len(values))
print("Kết quả:",result)
```

**Đọc kết quả:** 10 ngày ban đầu. Sample variance sử dụng `ddof=1`; độ lệch chuẩn đo bằng phút, còn phương sai mang đơn vị phút bình phương.

### Tình huống 2 — So mean và median hóa đơn · Cấp 2: Median và mode

**Tình huống thực tế:** Cửa hàng có ba hóa đơn 100, 120 và 10.000 nghìn đồng. Cần trình bày một giá trị trung tâm ít bị hóa đơn cực lớn kéo lên.

**Vì sao chọn cách giải này?** Median bền hơn với giá trị cực đoan so với mean; in cả hai để thấy sự khác biệt.

**Quy trình giải:**

1. Lưu ba hóa đơn theo nghìn đồng.
2. Tính mean và median cùng bộ dữ liệu.
3. Làm tròn mean ba chữ số và in trung vị.

```python
# Mục đích: So mean và median hóa đơn.
import numpy as np

amounts = [100, 120, 10000]
print(round(float(np.mean(amounts)), 3), float(np.median(amounts)))
```

**Kết quả khi chạy:**

```text
3406.667 120.0
```

Mean cao bất thường nhưng trung vị 120 nghìn gần hai hóa đơn thông thường.

**Bài thực hành nâng cấp — cấp 2/5:** Ứng dụng thống kê **12 ngày sử dụng**; mỗi hàng là số phút hoạt động trong một ngày. Hãy tính median và mode của 12 ngày. Các cấp tăng số ngày đồng thời đưa thêm số đo thiếu để thấy sự khác biệt giữa thống kê dữ liệu hợp lệ và thống kê nhầm cả giá trị thiếu.

```python
import numpy as np
import pandas as pd
# Mỗi phần tử là số phút ứng dụng được sử dụng trong một ngày.
values = np.array([35, 44, 53, 56, 65, 74, 77, 86, 95, 98, 107, 116],dtype=float)
valid = values[np.isfinite(values)]
result = {'median':float(np.median(valid)),'mode':float(pd.Series(valid).mode().iloc[0])}
print("Số ngày:",len(values))
print("Kết quả:",result)
```

**Đọc kết quả:** 12 ngày ban đầu. Sample variance sử dụng `ddof=1`; độ lệch chuẩn đo bằng phút, còn phương sai mang đơn vị phút bình phương.

### Tình huống 3 — Đo độ phân tán điểm thi · Cấp 3: Độ phân tán mẫu

**Tình huống thực tế:** Ba điểm kiểm tra `[6,8,10]` (điểm trên thang 10) tạo toàn bộ nhóm cần mô tả. Cần tính phương sai **quần thể** của nhóm này.

**Vì sao chọn cách giải này?** Bình phương sai khác làm mất dấu âm, sau đó lấy trung bình trên cả ba điểm `ddof=0`.

**Quy trình giải:**

1. Tạo mảng điểm [6,8,10].
2. Tính `np.var(...,ddof=0)` vì đang mô tả toàn bộ nhóm.
3. In kết quả ba chữ số.

```python
# Mục đích: Đo độ phân tán điểm thi.
import numpy as np

scores = [6, 8, 10]
print(round(float(np.var(scores, ddof=0)), 3))
```

**Kết quả khi chạy:**

```text
2.667
```

Phương sai quần thể khoảng 2,667 điểm².

**Bài thực hành nâng cấp — cấp 3/5:** Ứng dụng thống kê **15 ngày sử dụng**; mỗi hàng là số phút hoạt động trong một ngày. Hãy tính variance và standard deviation mẫu trên 15 ngày. Các cấp tăng số ngày đồng thời đưa thêm số đo thiếu để thấy sự khác biệt giữa thống kê dữ liệu hợp lệ và thống kê nhầm cả giá trị thiếu.

```python
import numpy as np
import pandas as pd
# Mỗi phần tử là số phút ứng dụng được sử dụng trong một ngày.
values = np.array([35, 44, 53, 56, 65, 74, 77, 86, 95, 98, 107, 116, 119, 128, 137],dtype=float)
valid = values[np.isfinite(values)]
result = {'sample_variance':round(float(np.var(valid,ddof=1)),2),'sample_std_minutes':round(float(np.std(valid,ddof=1)),2)}
print("Số ngày:",len(values))
print("Kết quả:",result)
```

**Đọc kết quả:** 15 ngày ban đầu. Sample variance sử dụng `ddof=1`; độ lệch chuẩn đo bằng phút, còn phương sai mang đơn vị phút bình phương.

### Tình huống 4 — Kiểm tra độ dao động nhiệt độ · Cấp 4: Xử lý giá trị khuyết

**Tình huống thực tế:** Cảm biến ghi 20,21,19,20 °C tại bốn thời điểm. Nhóm kiểm soát muốn đo mức dao động, giữ đơn vị °C để dễ so ngưỡng vận hành.

**Vì sao chọn cách giải này?** Std là căn phương sai, giữ cùng đơn vị nhiệt độ để có thể đọc trực tiếp.

**Quy trình giải:**

1. Lưu bốn nhiệt độ theo °C.
2. Dùng std quần thể `ddof=0`.
3. Làm tròn ba chữ số và in.

```python
# Mục đích: Kiểm tra độ dao động nhiệt độ.
import numpy as np

celsius = [20, 21, 19, 20]
print(round(float(np.std(celsius, ddof=0)), 3))
```

**Kết quả khi chạy:**

```text
0.707
```

Std khoảng 0,707 °C quanh mức trung bình 20 °C.

**Bài thực hành nâng cấp — cấp 4/5:** Ứng dụng thống kê **18 ngày sử dụng**; mỗi hàng là số phút hoạt động trong một ngày. Hãy không thay NaN bằng 0 khi tính trung bình và thống kê. Các cấp tăng số ngày đồng thời đưa thêm số đo thiếu để thấy sự khác biệt giữa thống kê dữ liệu hợp lệ và thống kê nhầm cả giá trị thiếu.

```python
import numpy as np
import pandas as pd
# Mỗi phần tử là số phút ứng dụng được sử dụng trong một ngày.
values = np.array([35, 44, 53, 56, 65, 74, 77, 86, 95, 98, 107, 116, 119, 128, 137, np.nan, 149, 158],dtype=float)
valid = values[np.isfinite(values)]
result = {'valid':len(valid),'missing':len(values)-len(valid),'mean':round(float(valid.mean()),2)}
print("Số ngày:",len(values))
print("Kết quả:",result)
```

**Đọc kết quả:** 18 ngày ban đầu. Sample variance sử dụng `ddof=1`; độ lệch chuẩn đo bằng phút, còn phương sai mang đơn vị phút bình phương.

### Tình huống 5 — Tìm nhãn sản phẩm xuất hiện nhiều nhất · Cấp 5: Thống kê đầy đủ

**Tình huống thực tế:** Danh sách năm lượt mua mang mã `A,A,B,C,A`. Mỗi phần tử là một lượt, không phải số lượng tồn kho. Cần tìm mã được mua nhiều lượt nhất.

**Vì sao chọn cách giải này?** Mode hoặc `value_counts` phù hợp với nhãn phân loại; không lấy mean của chữ.

**Quy trình giải:**

1. Tạo Series nhãn từng lượt mua.
2. Dùng `value_counts` đếm tần suất.
3. Lấy nhãn đầu và số lượt mua.

```python
# Mục đích: Tìm nhãn sản phẩm xuất hiện nhiều nhất.
import pandas as pd

products = pd.Series(['A', 'A', 'B', 'C', 'A'])
counts = products.value_counts()
print(counts.index[0], int(counts.iloc[0]))
```

**Kết quả khi chạy:**

```text
A 3
```

Mã A xuất hiện ba lượt, nhiều nhất trong danh sách.

**Bài thực hành nâng cấp — cấp 5/5:** Ứng dụng thống kê **20 ngày sử dụng**; mỗi hàng là số phút hoạt động trong một ngày. Hãy báo mean, median, mode, range, sample std và ngày thiếu. Các cấp tăng số ngày đồng thời đưa thêm số đo thiếu để thấy sự khác biệt giữa thống kê dữ liệu hợp lệ và thống kê nhầm cả giá trị thiếu.

```python
import numpy as np
import pandas as pd
# Mỗi phần tử là số phút ứng dụng được sử dụng trong một ngày.
values = np.array([35, 44, 53, 56, 65, 74, 77, 86, 95, 98, 107, 116, 119, 128, 137, np.nan, 149, 158, 161, np.nan],dtype=float)
valid = values[np.isfinite(values)]
result = {'mean':round(float(valid.mean()),2),'median':float(np.median(valid)),'mode':float(pd.Series(valid).mode().iloc[0]),'range':float(np.ptp(valid)),'sample_std':round(float(np.std(valid,ddof=1)),2),'missing':len(values)-len(valid)}
print("Số ngày:",len(values))
print("Kết quả:",result)
```

**Đọc kết quả:** 20 ngày ban đầu. Sample variance sử dụng `ddof=1`; độ lệch chuẩn đo bằng phút, còn phương sai mang đơn vị phút bình phương.

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
