# PY-38 — Quantile, IQR, outlier, skewness và kurtosis

*DRAFT · Các ví dụ minh họa và giả định phải được kiểm tra trước khi ứng dụng thực*

## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Quantile** — phân vị; **IQR** — khoảng tứ phân vị.

`Thống kê mô tả → Quantile/IQR → Outlier → Kiểm tra dữ liệu ML`

Kiến thức giúp sinh viên dùng Python để hiểu dữ liệu, đánh giá độ bất định và chuẩn bị dữ liệu cho AI.

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
| `Q1 - 1.5*IQR / Q3 + 1.5*IQR` | Ngưỡng gợi ý điểm ngoại lai, không phải chắc chắn lỗi |
| `pd.Series.skew()` | Đánh giá bất đối xứng, nhạy với cỡ mẫu |
| `pd.Series.kurt()` | Excess kurtosis theo quy ước Pandas |

## 4. Khái niệm với ví dụ nhỏ

### 4.1. Quantile

**Từ vựng trong mục:** **Quantile** — phân vị.

Giá trị chia phân phối theo tỷ lệ tích lũy. Thử đoạn code để thấy ý nghĩa đầu ra trước khi đọc bài tập.

```python
import numpy as np
print(np.quantile([1,2,3,4],.25))
```

**Tự kiểm tra:** Quantile là gì? **Đáp án:** Giá trị chia phân phối theo tỷ lệ tích lũy.

### 4.2. IQR

**Từ vựng trong mục:** **IQR** — khoảng tứ phân vị.

Khoảng cách Q3-Q1, mô tả 50% dữ liệu giữa. Thử đoạn code để thấy ý nghĩa đầu ra trước khi đọc bài tập.

```python
import numpy as np
x=[1,2,3,4,5];print(np.quantile(x,.75)-np.quantile(x,.25))
```

**Tự kiểm tra:** IQR là gì? **Đáp án:** Khoảng cách Q3-Q1, mô tả 50% dữ liệu giữa.

### 4.3. Skewness

**Từ vựng trong mục:** **Skewness** — độ lệch phân phối.

Mức bất đối xứng của phân phối quanh tâm. Thử đoạn code để thấy ý nghĩa đầu ra trước khi đọc bài tập.

```python
import pandas as pd
print(pd.Series([1,1,2,8]).skew())
```

**Tự kiểm tra:** Skewness là gì? **Đáp án:** Mức bất đối xứng của phân phối quanh tâm.

### 4.4. Kurtosis

**Từ vựng trong mục:** **Kurtosis** — độ nhọn/đuôi phân phối.

Chỉ số mô tả đặc điểm đuôi so với chuẩn theo quy ước. Thử đoạn code để thấy ý nghĩa đầu ra trước khi đọc bài tập.

```python
import pandas as pd
print(pd.Series([1,2,3,4,5]).kurt())
```

**Tự kiểm tra:** Kurtosis là gì? **Đáp án:** Chỉ số mô tả đặc điểm đuôi so với chuẩn theo quy ước.

## 5. Năm tình huống thực tế

### Tình huống 1 — Mốc chi tiêu 75%

**Từ vựng trong mục:** **Quantile** — phân vị.

**Vấn đề:** Mốc chi tiêu 75%.

**Vì sao chọn cách này?** Phân vị chia nhóm khách theo vị trí chi tiêu; không áp dụng kết luận ngoài phạm vi giả định của dữ liệu.

**Dữ liệu:** 5 số chi tiêu [10,20,30,40,50], nghìn đồng. Dữ liệu ví dụ và đơn vị đo nêu rõ; không thay cho dữ liệu kiểm chứng ngoài đời.

**Quy trình:** làm rõ ý nghĩa đầu vào → chọn phương pháp → chạy code → kiểm tra/diễn giải kết quả.

```python
import numpy as np
x=[10,20,30,40,50]
print(np.quantile(x,.75))
```

**Đọc kết quả:** Kiểm tra đầu ra với ví dụ, thay đầu vào để thấy giới hạn và trường hợp không phù hợp.

### Tình huống 2 — Kiểm outlier hóa đơn

**Từ vựng trong mục:** **IQR** — khoảng tứ phân vị.

**Vấn đề:** Kiểm outlier hóa đơn.

**Vì sao chọn cách này?** IQR gợi ý hóa đơn bất thường để rà soát; không áp dụng kết luận ngoài phạm vi giả định của dữ liệu.

**Dữ liệu:** 8 đơn [10,11,12,12,13,15,16,90], nghìn đồng. Dữ liệu ví dụ và đơn vị đo nêu rõ; không thay cho dữ liệu kiểm chứng ngoài đời.

**Quy trình:** làm rõ ý nghĩa đầu vào → chọn phương pháp → chạy code → kiểm tra/diễn giải kết quả.

```python
import numpy as np
x=np.array([10,11,12,12,13,15,16,90])
q1,q3=np.quantile(x,[.25,.75]);iqr=q3-q1
print(x[(x<q1-1.5*iqr)|(x>q3+1.5*iqr)])
```

**Đọc kết quả:** Kiểm tra đầu ra với ví dụ, thay đầu vào để thấy giới hạn và trường hợp không phù hợp.

### Tình huống 3 — So độ lệch phân phối

**Từ vựng trong mục:** **Skewness** — độ lệch phân phối.

**Vấn đề:** So độ lệch phân phối.

**Vì sao chọn cách này?** skew dương giúp nhận ra đuôi phải dài; không áp dụng kết luận ngoài phạm vi giả định của dữ liệu.

**Dữ liệu:** Giá trị [1,1,2,8]. Dữ liệu ví dụ và đơn vị đo nêu rõ; không thay cho dữ liệu kiểm chứng ngoài đời.

**Quy trình:** làm rõ ý nghĩa đầu vào → chọn phương pháp → chạy code → kiểm tra/diễn giải kết quả.

```python
import pandas as pd
print(pd.Series([1,1,2,8]).skew())
```

**Đọc kết quả:** Kiểm tra đầu ra với ví dụ, thay đầu vào để thấy giới hạn và trường hợp không phù hợp.

### Tình huống 4 — Xem độ nhọn phân phối

**Từ vựng trong mục:** **Kurtosis** — độ nhọn/đuôi phân phối.

**Vấn đề:** Xem độ nhọn phân phối.

**Vì sao chọn cách này?** kurt có ý nghĩa khi cỡ mẫu và quy ước phù hợp; không áp dụng kết luận ngoài phạm vi giả định của dữ liệu.

**Dữ liệu:** 10 giá trị đo minh họa. Dữ liệu ví dụ và đơn vị đo nêu rõ; không thay cho dữ liệu kiểm chứng ngoài đời.

**Quy trình:** làm rõ ý nghĩa đầu vào → chọn phương pháp → chạy code → kiểm tra/diễn giải kết quả.

```python
import pandas as pd
s=pd.Series([2,3,3,4,4,5,5,6,7,20])
print(s.kurt())
```

**Đọc kết quả:** Kiểm tra đầu ra với ví dụ, thay đầu vào để thấy giới hạn và trường hợp không phù hợp.

### Tình huống 5 — Chọn cách điền dữ liệu

**Từ vựng trong mục:** **Quantile** — phân vị.

**Vấn đề:** Chọn cách điền dữ liệu.

**Vì sao chọn cách này?** Median có thể hữu ích khi có giá trị lớn bất thường; không áp dụng kết luận ngoài phạm vi giả định của dữ liệu.

**Dữ liệu:** [100,120,10000,None] nghìn đồng. Dữ liệu ví dụ và đơn vị đo nêu rõ; không thay cho dữ liệu kiểm chứng ngoài đời.

**Quy trình:** làm rõ ý nghĩa đầu vào → chọn phương pháp → chạy code → kiểm tra/diễn giải kết quả.

```python
import pandas as pd
s=pd.Series([100,120,10000,None])
print(s.fillna(s.median()))
```

**Đọc kết quả:** Kiểm tra đầu ra với ví dụ, thay đầu vào để thấy giới hạn và trường hợp không phù hợp.

## 6. Nhầm lẫn thường gặp

- Không nhầm thống kê/tỷ lệ mô phỏng với xác suất dự đoán chắc chắn.
- Kiểm tra giả định, cỡ mẫu, đơn vị, độ nhạy kết quả và data leakage trước khi ứng dụng AI thật.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.


**Q1. What is Quantile? — Khái niệm Quantile là gì?**

A. Another concept is Khoảng cách Q3-Q1, mô tả 50% dữ liệu giữa — Khoảng cách Q3-Q1, mô tả 50% dữ liệu giữa

B. It is Giá trị chia phân phối theo tỷ lệ tích lũy — Giá trị chia phân phối theo tỷ lệ tích lũy

C. Another concept is Mức bất đối xứng của phân phối quanh tâm — Mức bất đối xứng của phân phối quanh tâm

D. Another concept is Chỉ số mô tả đặc điểm đuôi so với chuẩn theo quy ước — Chỉ số mô tả đặc điểm đuôi so với chuẩn theo quy ước


**Q2. What is IQR? — Khái niệm IQR là gì?**

A. It is Khoảng cách Q3-Q1, mô tả 50% dữ liệu giữa — Khoảng cách Q3-Q1, mô tả 50% dữ liệu giữa

B. Another concept is Mức bất đối xứng của phân phối quanh tâm — Mức bất đối xứng của phân phối quanh tâm

C. Another concept is Chỉ số mô tả đặc điểm đuôi so với chuẩn theo quy ước — Chỉ số mô tả đặc điểm đuôi so với chuẩn theo quy ước

D. Another concept is Giá trị chia phân phối theo tỷ lệ tích lũy — Giá trị chia phân phối theo tỷ lệ tích lũy


**Q3. What is Skewness? — Khái niệm Skewness là gì?**

A. Another concept is Chỉ số mô tả đặc điểm đuôi so với chuẩn theo quy ước — Chỉ số mô tả đặc điểm đuôi so với chuẩn theo quy ước

B. Another concept is Giá trị chia phân phối theo tỷ lệ tích lũy — Giá trị chia phân phối theo tỷ lệ tích lũy

C. Another concept is Khoảng cách Q3-Q1, mô tả 50% dữ liệu giữa — Khoảng cách Q3-Q1, mô tả 50% dữ liệu giữa

D. It is Mức bất đối xứng của phân phối quanh tâm — Mức bất đối xứng của phân phối quanh tâm


**Q4. What is Kurtosis? — Khái niệm Kurtosis là gì?**

A. Another concept is Giá trị chia phân phối theo tỷ lệ tích lũy — Giá trị chia phân phối theo tỷ lệ tích lũy

B. Another concept is Khoảng cách Q3-Q1, mô tả 50% dữ liệu giữa — Khoảng cách Q3-Q1, mô tả 50% dữ liệu giữa

C. It is Chỉ số mô tả đặc điểm đuôi so với chuẩn theo quy ước — Chỉ số mô tả đặc điểm đuôi so với chuẩn theo quy ước

D. Another concept is Mức bất đối xứng của phân phối quanh tâm — Mức bất đối xứng của phân phối quanh tâm


**Q5. When should np.quantile(x,[.25,.5,.75]) be used? — Khi nào nên dùng np.quantile(x,[.25,.5,.75])?**

A. Another operation is for Ngưỡng gợi ý điểm ngoại lai, không phải chắc chắn lỗi — Ngưỡng gợi ý điểm ngoại lai, không phải chắc chắn lỗi

B. When you need to Tìm các phân vị 25%, 50%, 75% — Tìm các phân vị 25%, 50%, 75%

C. Another operation is for Đánh giá bất đối xứng, nhạy với cỡ mẫu — Đánh giá bất đối xứng, nhạy với cỡ mẫu

D. Another operation is for Excess kurtosis theo quy ước Pandas — Excess kurtosis theo quy ước Pandas


**Q6. When should Q1 - 1.5*IQR / Q3 + 1.5*IQR be used? — Khi nào nên dùng Q1 - 1.5*IQR / Q3 + 1.5*IQR?**

A. When you need to Ngưỡng gợi ý điểm ngoại lai, không phải chắc chắn lỗi — Ngưỡng gợi ý điểm ngoại lai, không phải chắc chắn lỗi

B. Another operation is for Đánh giá bất đối xứng, nhạy với cỡ mẫu — Đánh giá bất đối xứng, nhạy với cỡ mẫu

C. Another operation is for Excess kurtosis theo quy ước Pandas — Excess kurtosis theo quy ước Pandas

D. Another operation is for Tìm các phân vị 25%, 50%, 75% — Tìm các phân vị 25%, 50%, 75%


**Q7. When should pd.Series.skew() be used? — Khi nào nên dùng pd.Series.skew()?**

A. Another operation is for Excess kurtosis theo quy ước Pandas — Excess kurtosis theo quy ước Pandas

B. Another operation is for Tìm các phân vị 25%, 50%, 75% — Tìm các phân vị 25%, 50%, 75%

C. Another operation is for Ngưỡng gợi ý điểm ngoại lai, không phải chắc chắn lỗi — Ngưỡng gợi ý điểm ngoại lai, không phải chắc chắn lỗi

D. When you need to Đánh giá bất đối xứng, nhạy với cỡ mẫu — Đánh giá bất đối xứng, nhạy với cỡ mẫu


**Q8. When should pd.Series.kurt() be used? — Khi nào nên dùng pd.Series.kurt()?**

A. Another operation is for Tìm các phân vị 25%, 50%, 75% — Tìm các phân vị 25%, 50%, 75%

B. Another operation is for Ngưỡng gợi ý điểm ngoại lai, không phải chắc chắn lỗi — Ngưỡng gợi ý điểm ngoại lai, không phải chắc chắn lỗi

C. When you need to Excess kurtosis theo quy ước Pandas — Excess kurtosis theo quy ước Pandas

D. Another operation is for Đánh giá bất đối xứng, nhạy với cỡ mẫu — Đánh giá bất đối xứng, nhạy với cỡ mẫu


**Q9. Why is this method used in scenario 1? — Vì sao dùng phương pháp ở tình huống 1?**

A. IQR gợi ý hóa đơn bất thường để rà soát — IQR gợi ý hóa đơn bất thường để rà soát

B. Phân vị chia nhóm khách theo vị trí chi tiêu — Phân vị chia nhóm khách theo vị trí chi tiêu

C. skew dương giúp nhận ra đuôi phải dài — skew dương giúp nhận ra đuôi phải dài

D. kurt có ý nghĩa khi cỡ mẫu và quy ước phù hợp — kurt có ý nghĩa khi cỡ mẫu và quy ước phù hợp


**Q10. Why is this method used in scenario 2? — Vì sao dùng phương pháp ở tình huống 2?**

A. IQR gợi ý hóa đơn bất thường để rà soát — IQR gợi ý hóa đơn bất thường để rà soát

B. skew dương giúp nhận ra đuôi phải dài — skew dương giúp nhận ra đuôi phải dài

C. kurt có ý nghĩa khi cỡ mẫu và quy ước phù hợp — kurt có ý nghĩa khi cỡ mẫu và quy ước phù hợp

D. Median có thể hữu ích khi có giá trị lớn bất thường — Median có thể hữu ích khi có giá trị lớn bất thường


**Q11. Why is this method used in scenario 3? — Vì sao dùng phương pháp ở tình huống 3?**

A. kurt có ý nghĩa khi cỡ mẫu và quy ước phù hợp — kurt có ý nghĩa khi cỡ mẫu và quy ước phù hợp

B. Median có thể hữu ích khi có giá trị lớn bất thường — Median có thể hữu ích khi có giá trị lớn bất thường

C. Phân vị chia nhóm khách theo vị trí chi tiêu — Phân vị chia nhóm khách theo vị trí chi tiêu

D. skew dương giúp nhận ra đuôi phải dài — skew dương giúp nhận ra đuôi phải dài


**Q12. Why is this method used in scenario 4? — Vì sao dùng phương pháp ở tình huống 4?**

A. Median có thể hữu ích khi có giá trị lớn bất thường — Median có thể hữu ích khi có giá trị lớn bất thường

B. Phân vị chia nhóm khách theo vị trí chi tiêu — Phân vị chia nhóm khách theo vị trí chi tiêu

C. kurt có ý nghĩa khi cỡ mẫu và quy ước phù hợp — kurt có ý nghĩa khi cỡ mẫu và quy ước phù hợp

D. IQR gợi ý hóa đơn bất thường để rà soát — IQR gợi ý hóa đơn bất thường để rà soát


**Q13. Why is this method used in scenario 5? — Vì sao dùng phương pháp ở tình huống 5?**

A. Phân vị chia nhóm khách theo vị trí chi tiêu — Phân vị chia nhóm khách theo vị trí chi tiêu

B. Median có thể hữu ích khi có giá trị lớn bất thường — Median có thể hữu ích khi có giá trị lớn bất thường

C. IQR gợi ý hóa đơn bất thường để rà soát — IQR gợi ý hóa đơn bất thường để rà soát

D. skew dương giúp nhận ra đuôi phải dài — skew dương giúp nhận ra đuôi phải dài


**Q14. Which input describes scenario 1? — Dữ liệu nào thuộc tình huống 1?**

A. The input is 5 số chi tiêu [10,20,30,40,50], nghìn đồng — 5 số chi tiêu [10,20,30,40,50], nghìn đồng

B. Another input is 8 đơn [10,11,12,12,13,15,16,90], nghìn đồng — 8 đơn [10,11,12,12,13,15,16,90], nghìn đồng

C. Another input is Giá trị [1,1,2,8] — Giá trị [1,1,2,8]

D. Another input is 10 giá trị đo minh họa — 10 giá trị đo minh họa


**Q15. Which input describes scenario 2? — Dữ liệu nào thuộc tình huống 2?**

A. Another input is Giá trị [1,1,2,8] — Giá trị [1,1,2,8]

B. Another input is 10 giá trị đo minh họa — 10 giá trị đo minh họa

C. Another input is [100,120,10000,None] nghìn đồng — [100,120,10000,None] nghìn đồng

D. The input is 8 đơn [10,11,12,12,13,15,16,90], nghìn đồng — 8 đơn [10,11,12,12,13,15,16,90], nghìn đồng


**Q16. Which input describes scenario 3? — Dữ liệu nào thuộc tình huống 3?**

A. Another input is 10 giá trị đo minh họa — 10 giá trị đo minh họa

B. Another input is [100,120,10000,None] nghìn đồng — [100,120,10000,None] nghìn đồng

C. The input is Giá trị [1,1,2,8] — Giá trị [1,1,2,8]

D. Another input is 5 số chi tiêu [10,20,30,40,50], nghìn đồng — 5 số chi tiêu [10,20,30,40,50], nghìn đồng


**Q17. Which input describes scenario 4? — Dữ liệu nào thuộc tình huống 4?**

A. Another input is [100,120,10000,None] nghìn đồng — [100,120,10000,None] nghìn đồng

B. The input is 10 giá trị đo minh họa — 10 giá trị đo minh họa

C. Another input is 5 số chi tiêu [10,20,30,40,50], nghìn đồng — 5 số chi tiêu [10,20,30,40,50], nghìn đồng

D. Another input is 8 đơn [10,11,12,12,13,15,16,90], nghìn đồng — 8 đơn [10,11,12,12,13,15,16,90], nghìn đồng


**Q18. Which input describes scenario 5? — Dữ liệu nào thuộc tình huống 5?**

A. The input is [100,120,10000,None] nghìn đồng — [100,120,10000,None] nghìn đồng

B. Another input is 5 số chi tiêu [10,20,30,40,50], nghìn đồng — 5 số chi tiêu [10,20,30,40,50], nghìn đồng

C. Another input is 8 đơn [10,11,12,12,13,15,16,90], nghìn đồng — 8 đơn [10,11,12,12,13,15,16,90], nghìn đồng

D. Another input is Giá trị [1,1,2,8] — Giá trị [1,1,2,8]


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
| Q1 | **B** | It is Giá trị chia phân phối theo tỷ lệ tích lũy | Giá trị chia phân phối theo tỷ lệ tích lũy |
| Q2 | **A** | It is Khoảng cách Q3-Q1, mô tả 50% dữ liệu giữa | Khoảng cách Q3-Q1, mô tả 50% dữ liệu giữa |
| Q3 | **D** | It is Mức bất đối xứng của phân phối quanh tâm | Mức bất đối xứng của phân phối quanh tâm |
| Q4 | **C** | It is Chỉ số mô tả đặc điểm đuôi so với chuẩn theo quy ước | Chỉ số mô tả đặc điểm đuôi so với chuẩn theo quy ước |
| Q5 | **B** | When you need to Tìm các phân vị 25%, 50%, 75% | Tìm các phân vị 25%, 50%, 75% |
| Q6 | **A** | When you need to Ngưỡng gợi ý điểm ngoại lai, không phải chắc chắn lỗi | Ngưỡng gợi ý điểm ngoại lai, không phải chắc chắn lỗi |
| Q7 | **D** | When you need to Đánh giá bất đối xứng, nhạy với cỡ mẫu | Đánh giá bất đối xứng, nhạy với cỡ mẫu |
| Q8 | **C** | When you need to Excess kurtosis theo quy ước Pandas | Excess kurtosis theo quy ước Pandas |
| Q9 | **B** | Phân vị chia nhóm khách theo vị trí chi tiêu | Phân vị chia nhóm khách theo vị trí chi tiêu |
| Q10 | **A** | IQR gợi ý hóa đơn bất thường để rà soát | IQR gợi ý hóa đơn bất thường để rà soát |
| Q11 | **D** | skew dương giúp nhận ra đuôi phải dài | skew dương giúp nhận ra đuôi phải dài |
| Q12 | **C** | kurt có ý nghĩa khi cỡ mẫu và quy ước phù hợp | kurt có ý nghĩa khi cỡ mẫu và quy ước phù hợp |
| Q13 | **B** | Median có thể hữu ích khi có giá trị lớn bất thường | Median có thể hữu ích khi có giá trị lớn bất thường |
| Q14 | **A** | The input is 5 số chi tiêu [10,20,30,40,50], nghìn đồng | 5 số chi tiêu [10,20,30,40,50], nghìn đồng |
| Q15 | **D** | The input is 8 đơn [10,11,12,12,13,15,16,90], nghìn đồng | 8 đơn [10,11,12,12,13,15,16,90], nghìn đồng |
| Q16 | **C** | The input is Giá trị [1,1,2,8] | Giá trị [1,1,2,8] |
| Q17 | **B** | The input is 10 giá trị đo minh họa | 10 giá trị đo minh họa |
| Q18 | **A** | The input is [100,120,10000,None] nghìn đồng | [100,120,10000,None] nghìn đồng |
| Q19 | **D** | Units, sample meaning and assumptions | Đơn vị, ý nghĩa mẫu và giả định |
| Q20 | **C** | An example may not generalize | Ví dụ có thể không tổng quát |

## 8. Liên hệ bài kế tiếp

`Thống kê mô tả → Quantile/IQR → Outlier → Kiểm tra dữ liệu ML`.
