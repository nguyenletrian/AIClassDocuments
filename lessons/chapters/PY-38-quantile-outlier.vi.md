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

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Mốc 75% của giá trị đơn hàng

**Tình huống thực tế:** Năm hóa đơn có giá trị 10,20,30,40,50 nghìn đồng. Bộ phận kinh doanh muốn mốc phân vị 75% để mô tả vị trí của hóa đơn cao trong nhóm.

**Vì sao chọn cách giải này?** Phân vị xét vị trí theo thứ tự đã sắp, không dựa trên trung bình mọi hóa đơn.

**Quy trình giải:**

1. Lưu năm giá trị theo nghìn đồng.
2. Tính phân vị 0.75 bằng `np.quantile`.
3. In mốc theo nghìn đồng và nêu quy ước nội suy.

```python
# Mục đích: Mốc 75% của giá trị đơn hàng.
import numpy as np

amounts = [10, 20, 30, 40, 50]
print(float(np.quantile(amounts, 0.75)))
```

**Kết quả khi chạy:**

```text
40.0
```

Mốc 75% bằng 40 nghìn đồng theo quy ước NumPy mặc định.

### Tình huống 2 — Gắn cờ hóa đơn lớn cần kiểm tra

**Tình huống thực tế:** Tám hóa đơn có số tiền `[10,11,12,12,13,15,16,90]` nghìn đồng. Kế toán muốn tìm những hóa đơn vượt ngưỡng IQR để xem lại chứng từ, không xóa ngay.

**Vì sao chọn cách giải này?** IQR đo phần giữa và ngưỡng 1.5×IQR tạo danh sách điểm cần xác minh.

**Quy trình giải:**

1. Tính Q1, Q3 và IQR trên toàn bộ tám hóa đơn.
2. Lập ngưỡng dưới và trên bằng 1.5×IQR.
3. Lọc số tiền ngoài hai ngưỡng và in List.

```python
# Mục đích: Gắn cờ hóa đơn lớn cần kiểm tra.
import numpy as np

amounts = np.array([10, 11, 12, 12, 13, 15, 16, 90])
q1, q3 = np.quantile(amounts, [0.25, 0.75])
iqr = q3 - q1
outliers = amounts[(amounts < q1 - 1.5 * iqr) | (amounts > q3 + 1.5 * iqr)]
print(outliers.tolist())
```

**Kết quả khi chạy:**

```text
[90]
```

Hóa đơn 90 nghìn đồng bị gắn cờ để xác minh; không kết luận đây là lỗi ghi chép.

### Tình huống 3 — Kiểm tra độ lệch phải của dữ liệu

**Tình huống thực tế:** Bốn lần đo `[1,1,2,8]` cùng đơn vị có một giá trị lớn hơn nhiều. Nhóm phân tích muốn biết phân phối mẫu lệch về phía giá trị lớn hay nhỏ.

**Vì sao chọn cách giải này?** Skewness dương thể hiện đuôi phải dài hơn; `Series.skew` tính hệ số phù hợp cho dữ liệu một chiều.

**Quy trình giải:**

1. Tạo Series bốn số đo.
2. Tính hệ số skew theo quy ước Pandas.
3. Làm tròn ba chữ số rồi đánh giá dấu, không xem là bằng chứng dữ liệu sai.

```python
# Mục đích: Kiểm tra độ lệch phải của dữ liệu.
import pandas as pd

measurements = pd.Series([1, 1, 2, 8])
print(round(float(measurements.skew()), 3))
```

**Kết quả khi chạy:**

```text
1.887
```

Skew dương gợi ý đuôi phải dài; cỡ mẫu bốn quan sát còn rất nhỏ.

### Tình huống 4 — Đánh giá đặc điểm đuôi của một mẫu

**Tình huống thực tế:** Mười số đo cùng đơn vị `[2,3,3,4,4,5,5,6,7,20]` có một số lớn. Nhóm phân tích cần xem hệ số kurtosis dư có đáng chú ý không.

**Vì sao chọn cách giải này?** Kurtosis dư nhạy với chênh lệch lớn bậc bốn, giúp so đặc điểm đuôi theo quy ước Pandas.

**Quy trình giải:**

1. Tạo Series mười số đo.
2. Dùng `kurt()` tính excess kurtosis.
3. Làm tròn ba chữ số và nêu giới hạn mẫu nhỏ.

```python
# Mục đích: Đánh giá đặc điểm đuôi của một mẫu.
import pandas as pd

measurements = pd.Series([2, 3, 3, 4, 4, 5, 5, 6, 7, 20])
print(round(float(measurements.kurt()), 3))
```

**Kết quả khi chạy:**

```text
7.824
```

Mẫu có kurtosis dư dương cao, nhưng chỉ là dấu hiệu phân bố, không phải phép kết luận chất lượng dữ liệu.

### Tình huống 5 — Điền giá trị thiếu trong nhóm có số cực lớn

**Tình huống thực tế:** Ba hóa đơn là 100,120,10.000 nghìn đồng và có một ô chưa biết. Muốn điền tạm ô thiếu bằng trung vị của **các số quan sát được** trước khi dùng thử mô hình.

**Vì sao chọn cách giải này?** Median bền hơn mean khi có giá trị cực lớn; số điền chỉ là ước lượng, không phải dữ liệu thật.

**Quy trình giải:**

1. Tạo Series gồm ba giá trị và một None.
2. Tính median từ ba số không thiếu.
3. Điền None bằng median và in danh sách để kiểm tra.

```python
# Mục đích: Điền giá trị thiếu trong nhóm có số cực lớn.
import pandas as pd

amounts = pd.Series([100, 120, 10000, None])
print(amounts.fillna(amounts.median()).tolist())
```

**Kết quả khi chạy:**

```text
[100.0, 120.0, 10000.0, 120.0]
```

Ô thiếu được điền tạm 120 nghìn đồng; với ML cần tính median trên train để tránh rò rỉ.

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
