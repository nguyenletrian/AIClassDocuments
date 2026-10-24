# PY-40 — Kiểm định giả thuyết, p-value và khoảng tin cậy

*DRAFT · Các ví dụ minh họa và giả định phải được kiểm tra trước khi ứng dụng thực*

## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Null hypothesis** — giả thuyết không; **p-value** — giá trị p.

`CLT/SE → Hypothesis Testing → Confidence Interval → A/B Test`

Kiến thức giúp sinh viên dùng Python để hiểu dữ liệu, đánh giá độ bất định và chuẩn bị dữ liệu cho AI.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Khái niệm |
|---|---|---|
| Null hypothesis | giả thuyết không | Phát biểu gốc đem kiểm định, ký hiệu H0 |
| p-value | giá trị p | Độ bất thường của dữ liệu nếu giả định H0 đúng |
| T-test | kiểm định t | Kiểm định trung bình khi phương sai tổng thể chưa biết |
| Confidence interval | khoảng tin cậy | Khoảng tính theo quy trình có mức bao phủ dài hạn xác định |

## 3. Thư viện và hàm Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cách viết | Khi nào dùng, ý nghĩa tham số |
|---|---|
| `scipy.stats.ttest_1samp(values,popmean)` | Kiểm định mean so với mốc, giả định cần kiểm tra |
| `scipy.stats.t.interval(confidence,df,loc,scale)` | Khoảng tin cậy mean theo t-distribution |
| `scipy.stats.sem(values)` | Ước lượng sai số chuẩn từ mẫu |
| `pvalue < alpha` | Quy tắc bác bỏ H0, không phải P(H0 đúng) |

## 4. Khái niệm với ví dụ nhỏ

### 4.1. Null hypothesis

**Từ vựng trong mục:** **Null hypothesis** — giả thuyết không.

Phát biểu gốc đem kiểm định, ký hiệu H0. Thử đoạn code để thấy ý nghĩa đầu ra trước khi đọc bài tập.

```python
print('H0: mean = 50')
```

**Tự kiểm tra:** Null hypothesis là gì? **Đáp án:** Phát biểu gốc đem kiểm định, ký hiệu H0.

### 4.2. p-value

**Từ vựng trong mục:** **p-value** — giá trị p.

Độ bất thường của dữ liệu nếu giả định H0 đúng. Thử đoạn code để thấy ý nghĩa đầu ra trước khi đọc bài tập.

```python
from scipy.stats import ttest_1samp
print(ttest_1samp([8,9,10,11,12],10).pvalue)
```

**Tự kiểm tra:** p-value là gì? **Đáp án:** Độ bất thường của dữ liệu nếu giả định H0 đúng.

### 4.3. T-test

**Từ vựng trong mục:** **T-test** — kiểm định t.

Kiểm định trung bình khi phương sai tổng thể chưa biết. Thử đoạn code để thấy ý nghĩa đầu ra trước khi đọc bài tập.

```python
from scipy.stats import ttest_1samp
print(ttest_1samp([8,9,10,11,12],10).statistic)
```

**Tự kiểm tra:** T-test là gì? **Đáp án:** Kiểm định trung bình khi phương sai tổng thể chưa biết.

### 4.4. Confidence interval

**Từ vựng trong mục:** **Confidence interval** — khoảng tin cậy.

Khoảng tính theo quy trình có mức bao phủ dài hạn xác định. Thử đoạn code để thấy ý nghĩa đầu ra trước khi đọc bài tập.

```python
import numpy as np
print(np.mean([2,3,4]))
```

**Tự kiểm tra:** Confidence interval là gì? **Đáp án:** Khoảng tính theo quy trình có mức bao phủ dài hạn xác định.

## 5. Năm tình huống thực tế

### Tình huống 1 — Đánh giá điểm trung bình so với 50

**Từ vựng trong mục:** **Null hypothesis** — giả thuyết không.

**Vấn đề:** Đánh giá điểm trung bình so với 50.

**Vì sao chọn cách này?** T-test giúp so mean của mẫu với một chuẩn đã định; không áp dụng kết luận ngoài phạm vi giả định của dữ liệu.

**Dữ liệu:** 7 điểm [48,52,55,49,51,47,53]. Dữ liệu ví dụ và đơn vị đo nêu rõ; không thay cho dữ liệu kiểm chứng ngoài đời.

**Quy trình:** làm rõ ý nghĩa đầu vào → chọn phương pháp → chạy code → kiểm tra/diễn giải kết quả.

```python
from scipy.stats import ttest_1samp
x=[48,52,55,49,51,47,53]
print(ttest_1samp(x,popmean=50).pvalue)
```

**Đọc kết quả:** Kiểm tra đầu ra với ví dụ, thay đầu vào để thấy giới hạn và trường hợp không phù hợp.

### Tình huống 2 — Khoảng tin cậy thời gian giao hàng

**Từ vựng trong mục:** **p-value** — giá trị p.

**Vấn đề:** Khoảng tin cậy thời gian giao hàng.

**Vì sao chọn cách này?** t.interval dùng std mẫu khi n nhỏ và giả định phù hợp; không áp dụng kết luận ngoài phạm vi giả định của dữ liệu.

**Dữ liệu:** 5 số ngày [2,3,3,4,2]. Dữ liệu ví dụ và đơn vị đo nêu rõ; không thay cho dữ liệu kiểm chứng ngoài đời.

**Quy trình:** làm rõ ý nghĩa đầu vào → chọn phương pháp → chạy code → kiểm tra/diễn giải kết quả.

```python
import numpy as np
from scipy.stats import t,sem
x=np.array([2.,3.,3.,4.,2.]);mean=x.mean()
print(t.interval(.95,df=len(x)-1,loc=mean,scale=sem(x)))
```

**Đọc kết quả:** Kiểm tra đầu ra với ví dụ, thay đầu vào để thấy giới hạn và trường hợp không phù hợp.

### Tình huống 3 — Xem sai số chuẩn

**Từ vựng trong mục:** **T-test** — kiểm định t.

**Vấn đề:** Xem sai số chuẩn.

**Vì sao chọn cách này?** sem cho biết mức bất định của mean mẫu; không áp dụng kết luận ngoài phạm vi giả định của dữ liệu.

**Dữ liệu:** 5 ngày giao hàng. Dữ liệu ví dụ và đơn vị đo nêu rõ; không thay cho dữ liệu kiểm chứng ngoài đời.

**Quy trình:** làm rõ ý nghĩa đầu vào → chọn phương pháp → chạy code → kiểm tra/diễn giải kết quả.

```python
from scipy.stats import sem
print(sem([2,3,3,4,2]))
```

**Đọc kết quả:** Kiểm tra đầu ra với ví dụ, thay đầu vào để thấy giới hạn và trường hợp không phù hợp.

### Tình huống 4 — Kiểm định thang thời gian

**Từ vựng trong mục:** **Confidence interval** — khoảng tin cậy.

**Vấn đề:** Kiểm định thang thời gian.

**Vì sao chọn cách này?** So pvalue với ngưỡng alpha chứ không coi pvalue là xác suất H0 đúng; không áp dụng kết luận ngoài phạm vi giả định của dữ liệu.

**Dữ liệu:** Giả sử alpha=0.05. Dữ liệu ví dụ và đơn vị đo nêu rõ; không thay cho dữ liệu kiểm chứng ngoài đời.

**Quy trình:** làm rõ ý nghĩa đầu vào → chọn phương pháp → chạy code → kiểm tra/diễn giải kết quả.

```python
from scipy.stats import ttest_1samp
p=ttest_1samp([5,6,7,8,9],popmean=6).pvalue
print("Reject H0" if p<.05 else "Not enough evidence")
```

**Đọc kết quả:** Kiểm tra đầu ra với ví dụ, thay đầu vào để thấy giới hạn và trường hợp không phù hợp.

### Tình huống 5 — Phân biệt ý nghĩa alpha

**Từ vựng trong mục:** **Null hypothesis** — giả thuyết không.

**Vấn đề:** Phân biệt ý nghĩa alpha.

**Vì sao chọn cách này?** Thay alpha đổi quyết định chứ không đổi dữ liệu pvalue; không áp dụng kết luận ngoài phạm vi giả định của dữ liệu.

**Dữ liệu:** pvalue=0.04, alpha 0.01 và 0.05. Dữ liệu ví dụ và đơn vị đo nêu rõ; không thay cho dữ liệu kiểm chứng ngoài đời.

**Quy trình:** làm rõ ý nghĩa đầu vào → chọn phương pháp → chạy code → kiểm tra/diễn giải kết quả.

```python
p=.04
for alpha in [.01,.05]:print(alpha,p<alpha)
```

**Đọc kết quả:** Kiểm tra đầu ra với ví dụ, thay đầu vào để thấy giới hạn và trường hợp không phù hợp.

## 6. Nhầm lẫn thường gặp

- Không nhầm thống kê/tỷ lệ mô phỏng với xác suất dự đoán chắc chắn.
- Kiểm tra giả định, cỡ mẫu, đơn vị, độ nhạy kết quả và data leakage trước khi ứng dụng AI thật.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.


**Q1. What is Null hypothesis? — Khái niệm Null hypothesis là gì?**

A. Another concept is Độ bất thường của dữ liệu nếu giả định H0 đúng — Độ bất thường của dữ liệu nếu giả định H0 đúng

B. It is Phát biểu gốc đem kiểm định, ký hiệu H0 — Phát biểu gốc đem kiểm định, ký hiệu H0

C. Another concept is Kiểm định trung bình khi phương sai tổng thể chưa biết — Kiểm định trung bình khi phương sai tổng thể chưa biết

D. Another concept is Khoảng tính theo quy trình có mức bao phủ dài hạn xác định — Khoảng tính theo quy trình có mức bao phủ dài hạn xác định


**Q2. What is p-value? — Khái niệm p-value là gì?**

A. It is Độ bất thường của dữ liệu nếu giả định H0 đúng — Độ bất thường của dữ liệu nếu giả định H0 đúng

B. Another concept is Kiểm định trung bình khi phương sai tổng thể chưa biết — Kiểm định trung bình khi phương sai tổng thể chưa biết

C. Another concept is Khoảng tính theo quy trình có mức bao phủ dài hạn xác định — Khoảng tính theo quy trình có mức bao phủ dài hạn xác định

D. Another concept is Phát biểu gốc đem kiểm định, ký hiệu H0 — Phát biểu gốc đem kiểm định, ký hiệu H0


**Q3. What is T-test? — Khái niệm T-test là gì?**

A. Another concept is Khoảng tính theo quy trình có mức bao phủ dài hạn xác định — Khoảng tính theo quy trình có mức bao phủ dài hạn xác định

B. Another concept is Phát biểu gốc đem kiểm định, ký hiệu H0 — Phát biểu gốc đem kiểm định, ký hiệu H0

C. Another concept is Độ bất thường của dữ liệu nếu giả định H0 đúng — Độ bất thường của dữ liệu nếu giả định H0 đúng

D. It is Kiểm định trung bình khi phương sai tổng thể chưa biết — Kiểm định trung bình khi phương sai tổng thể chưa biết


**Q4. What is Confidence interval? — Khái niệm Confidence interval là gì?**

A. Another concept is Phát biểu gốc đem kiểm định, ký hiệu H0 — Phát biểu gốc đem kiểm định, ký hiệu H0

B. Another concept is Độ bất thường của dữ liệu nếu giả định H0 đúng — Độ bất thường của dữ liệu nếu giả định H0 đúng

C. It is Khoảng tính theo quy trình có mức bao phủ dài hạn xác định — Khoảng tính theo quy trình có mức bao phủ dài hạn xác định

D. Another concept is Kiểm định trung bình khi phương sai tổng thể chưa biết — Kiểm định trung bình khi phương sai tổng thể chưa biết


**Q5. When should scipy.stats.ttest_1samp(values,popmean) be used? — Khi nào nên dùng scipy.stats.ttest_1samp(values,popmean)?**

A. Another operation is for Khoảng tin cậy mean theo t-distribution — Khoảng tin cậy mean theo t-distribution

B. When you need to Kiểm định mean so với mốc, giả định cần kiểm tra — Kiểm định mean so với mốc, giả định cần kiểm tra

C. Another operation is for Ước lượng sai số chuẩn từ mẫu — Ước lượng sai số chuẩn từ mẫu

D. Another operation is for Quy tắc bác bỏ H0, không phải P(H0 đúng) — Quy tắc bác bỏ H0, không phải P(H0 đúng)


**Q6. When should scipy.stats.t.interval(confidence,df,loc,scale) be used? — Khi nào nên dùng scipy.stats.t.interval(confidence,df,loc,scale)?**

A. When you need to Khoảng tin cậy mean theo t-distribution — Khoảng tin cậy mean theo t-distribution

B. Another operation is for Ước lượng sai số chuẩn từ mẫu — Ước lượng sai số chuẩn từ mẫu

C. Another operation is for Quy tắc bác bỏ H0, không phải P(H0 đúng) — Quy tắc bác bỏ H0, không phải P(H0 đúng)

D. Another operation is for Kiểm định mean so với mốc, giả định cần kiểm tra — Kiểm định mean so với mốc, giả định cần kiểm tra


**Q7. When should scipy.stats.sem(values) be used? — Khi nào nên dùng scipy.stats.sem(values)?**

A. Another operation is for Quy tắc bác bỏ H0, không phải P(H0 đúng) — Quy tắc bác bỏ H0, không phải P(H0 đúng)

B. Another operation is for Kiểm định mean so với mốc, giả định cần kiểm tra — Kiểm định mean so với mốc, giả định cần kiểm tra

C. Another operation is for Khoảng tin cậy mean theo t-distribution — Khoảng tin cậy mean theo t-distribution

D. When you need to Ước lượng sai số chuẩn từ mẫu — Ước lượng sai số chuẩn từ mẫu


**Q8. When should pvalue < alpha be used? — Khi nào nên dùng pvalue < alpha?**

A. Another operation is for Kiểm định mean so với mốc, giả định cần kiểm tra — Kiểm định mean so với mốc, giả định cần kiểm tra

B. Another operation is for Khoảng tin cậy mean theo t-distribution — Khoảng tin cậy mean theo t-distribution

C. When you need to Quy tắc bác bỏ H0, không phải P(H0 đúng) — Quy tắc bác bỏ H0, không phải P(H0 đúng)

D. Another operation is for Ước lượng sai số chuẩn từ mẫu — Ước lượng sai số chuẩn từ mẫu


**Q9. Why is this method used in scenario 1? — Vì sao dùng phương pháp ở tình huống 1?**

A. t.interval dùng std mẫu khi n nhỏ và giả định phù hợp — t.interval dùng std mẫu khi n nhỏ và giả định phù hợp

B. T-test giúp so mean của mẫu với một chuẩn đã định — T-test giúp so mean của mẫu với một chuẩn đã định

C. sem cho biết mức bất định của mean mẫu — sem cho biết mức bất định của mean mẫu

D. So pvalue với ngưỡng alpha chứ không coi pvalue là xác suất H0 đúng — So pvalue với ngưỡng alpha chứ không coi pvalue là xác suất H0 đúng


**Q10. Why is this method used in scenario 2? — Vì sao dùng phương pháp ở tình huống 2?**

A. t.interval dùng std mẫu khi n nhỏ và giả định phù hợp — t.interval dùng std mẫu khi n nhỏ và giả định phù hợp

B. sem cho biết mức bất định của mean mẫu — sem cho biết mức bất định của mean mẫu

C. So pvalue với ngưỡng alpha chứ không coi pvalue là xác suất H0 đúng — So pvalue với ngưỡng alpha chứ không coi pvalue là xác suất H0 đúng

D. Thay alpha đổi quyết định chứ không đổi dữ liệu pvalue — Thay alpha đổi quyết định chứ không đổi dữ liệu pvalue


**Q11. Why is this method used in scenario 3? — Vì sao dùng phương pháp ở tình huống 3?**

A. So pvalue với ngưỡng alpha chứ không coi pvalue là xác suất H0 đúng — So pvalue với ngưỡng alpha chứ không coi pvalue là xác suất H0 đúng

B. Thay alpha đổi quyết định chứ không đổi dữ liệu pvalue — Thay alpha đổi quyết định chứ không đổi dữ liệu pvalue

C. T-test giúp so mean của mẫu với một chuẩn đã định — T-test giúp so mean của mẫu với một chuẩn đã định

D. sem cho biết mức bất định của mean mẫu — sem cho biết mức bất định của mean mẫu


**Q12. Why is this method used in scenario 4? — Vì sao dùng phương pháp ở tình huống 4?**

A. Thay alpha đổi quyết định chứ không đổi dữ liệu pvalue — Thay alpha đổi quyết định chứ không đổi dữ liệu pvalue

B. T-test giúp so mean của mẫu với một chuẩn đã định — T-test giúp so mean của mẫu với một chuẩn đã định

C. So pvalue với ngưỡng alpha chứ không coi pvalue là xác suất H0 đúng — So pvalue với ngưỡng alpha chứ không coi pvalue là xác suất H0 đúng

D. t.interval dùng std mẫu khi n nhỏ và giả định phù hợp — t.interval dùng std mẫu khi n nhỏ và giả định phù hợp


**Q13. Why is this method used in scenario 5? — Vì sao dùng phương pháp ở tình huống 5?**

A. T-test giúp so mean của mẫu với một chuẩn đã định — T-test giúp so mean của mẫu với một chuẩn đã định

B. Thay alpha đổi quyết định chứ không đổi dữ liệu pvalue — Thay alpha đổi quyết định chứ không đổi dữ liệu pvalue

C. t.interval dùng std mẫu khi n nhỏ và giả định phù hợp — t.interval dùng std mẫu khi n nhỏ và giả định phù hợp

D. sem cho biết mức bất định của mean mẫu — sem cho biết mức bất định của mean mẫu


**Q14. Which input describes scenario 1? — Dữ liệu nào thuộc tình huống 1?**

A. The input is 7 điểm [48,52,55,49,51,47,53] — 7 điểm [48,52,55,49,51,47,53]

B. Another input is 5 số ngày [2,3,3,4,2] — 5 số ngày [2,3,3,4,2]

C. Another input is 5 ngày giao hàng — 5 ngày giao hàng

D. Another input is Giả sử alpha=0.05 — Giả sử alpha=0.05


**Q15. Which input describes scenario 2? — Dữ liệu nào thuộc tình huống 2?**

A. Another input is 5 ngày giao hàng — 5 ngày giao hàng

B. Another input is Giả sử alpha=0.05 — Giả sử alpha=0.05

C. Another input is pvalue=0.04, alpha 0.01 và 0.05 — pvalue=0.04, alpha 0.01 và 0.05

D. The input is 5 số ngày [2,3,3,4,2] — 5 số ngày [2,3,3,4,2]


**Q16. Which input describes scenario 3? — Dữ liệu nào thuộc tình huống 3?**

A. Another input is Giả sử alpha=0.05 — Giả sử alpha=0.05

B. Another input is pvalue=0.04, alpha 0.01 và 0.05 — pvalue=0.04, alpha 0.01 và 0.05

C. The input is 5 ngày giao hàng — 5 ngày giao hàng

D. Another input is 7 điểm [48,52,55,49,51,47,53] — 7 điểm [48,52,55,49,51,47,53]


**Q17. Which input describes scenario 4? — Dữ liệu nào thuộc tình huống 4?**

A. Another input is pvalue=0.04, alpha 0.01 và 0.05 — pvalue=0.04, alpha 0.01 và 0.05

B. The input is Giả sử alpha=0.05 — Giả sử alpha=0.05

C. Another input is 7 điểm [48,52,55,49,51,47,53] — 7 điểm [48,52,55,49,51,47,53]

D. Another input is 5 số ngày [2,3,3,4,2] — 5 số ngày [2,3,3,4,2]


**Q18. Which input describes scenario 5? — Dữ liệu nào thuộc tình huống 5?**

A. The input is pvalue=0.04, alpha 0.01 và 0.05 — pvalue=0.04, alpha 0.01 và 0.05

B. Another input is 7 điểm [48,52,55,49,51,47,53] — 7 điểm [48,52,55,49,51,47,53]

C. Another input is 5 số ngày [2,3,3,4,2] — 5 số ngày [2,3,3,4,2]

D. Another input is 5 ngày giao hàng — 5 ngày giao hàng


**Q19. What should be stated before analyzing data? — Cần nêu gì trước khi phân tích dữ liệu?**

A. Only file extensions — Chỉ đuôi file

B. Only terminal colors — Chỉ màu terminal

C. Only number of lines — Chỉ số dòng code

D. Units, sample meaning and assumptions — Đơn vị, ý nghĩa mẫu và giả định


**Q20. Why is validating results important? — Vì sao cần kiểm tra kết quả?**

A. One example guarantees AI accuracy — Một ví dụ bảo đảm AI đúng

B. It replaces data collection — Nó thay việc thu thập dữ liệu

C. An example may not generalize — Ví dụ có thể không tổng quát

D. It removes test sets — Nó không cần tập kiểm tra

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | It is Phát biểu gốc đem kiểm định, ký hiệu H0 | Phát biểu gốc đem kiểm định, ký hiệu H0 |
| Q2 | **A** | It is Độ bất thường của dữ liệu nếu giả định H0 đúng | Độ bất thường của dữ liệu nếu giả định H0 đúng |
| Q3 | **D** | It is Kiểm định trung bình khi phương sai tổng thể chưa biết | Kiểm định trung bình khi phương sai tổng thể chưa biết |
| Q4 | **C** | It is Khoảng tính theo quy trình có mức bao phủ dài hạn xác định | Khoảng tính theo quy trình có mức bao phủ dài hạn xác định |
| Q5 | **B** | When you need to Kiểm định mean so với mốc, giả định cần kiểm tra | Kiểm định mean so với mốc, giả định cần kiểm tra |
| Q6 | **A** | When you need to Khoảng tin cậy mean theo t-distribution | Khoảng tin cậy mean theo t-distribution |
| Q7 | **D** | When you need to Ước lượng sai số chuẩn từ mẫu | Ước lượng sai số chuẩn từ mẫu |
| Q8 | **C** | When you need to Quy tắc bác bỏ H0, không phải P(H0 đúng) | Quy tắc bác bỏ H0, không phải P(H0 đúng) |
| Q9 | **B** | T-test giúp so mean của mẫu với một chuẩn đã định | T-test giúp so mean của mẫu với một chuẩn đã định |
| Q10 | **A** | t.interval dùng std mẫu khi n nhỏ và giả định phù hợp | t.interval dùng std mẫu khi n nhỏ và giả định phù hợp |
| Q11 | **D** | sem cho biết mức bất định của mean mẫu | sem cho biết mức bất định của mean mẫu |
| Q12 | **C** | So pvalue với ngưỡng alpha chứ không coi pvalue là xác suất H0 đúng | So pvalue với ngưỡng alpha chứ không coi pvalue là xác suất H0 đúng |
| Q13 | **B** | Thay alpha đổi quyết định chứ không đổi dữ liệu pvalue | Thay alpha đổi quyết định chứ không đổi dữ liệu pvalue |
| Q14 | **A** | The input is 7 điểm [48,52,55,49,51,47,53] | 7 điểm [48,52,55,49,51,47,53] |
| Q15 | **D** | The input is 5 số ngày [2,3,3,4,2] | 5 số ngày [2,3,3,4,2] |
| Q16 | **C** | The input is 5 ngày giao hàng | 5 ngày giao hàng |
| Q17 | **B** | The input is Giả sử alpha=0.05 | Giả sử alpha=0.05 |
| Q18 | **A** | The input is pvalue=0.04, alpha 0.01 và 0.05 | pvalue=0.04, alpha 0.01 và 0.05 |
| Q19 | **D** | Units, sample meaning and assumptions | Đơn vị, ý nghĩa mẫu và giả định |
| Q20 | **C** | An example may not generalize | Ví dụ có thể không tổng quát |

## 8. Liên hệ bài kế tiếp

`CLT/SE → Hypothesis Testing → Confidence Interval → A/B Test`.
