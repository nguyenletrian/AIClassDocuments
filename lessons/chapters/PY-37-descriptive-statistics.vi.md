# PY-37 — Thống kê mô tả: mean, median, mode, variance và std


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Mean** — trung bình; **Median** — trung vị.

`NumPy/Pandas → Thống kê mô tả → Outlier → ML`

Bài này kết nối dữ liệu thực nghiệm với cách tính xác suất, thống kê và các bước học máy.

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

## 4. Khái niệm liên quan, ví dụ nhỏ

### 4.1. Mean

**Từ vựng trong mục:** **Mean** — trung bình.

Tổng giá trị chia số quan sát. Trước khi tính, phân biệt điều kiện áp dụng và ý nghĩa của đầu vào.

```python
import numpy as np
print(np.mean([2,4,6]))
```

**Tự kiểm tra:** Mean là gì? **Đáp án:** Tổng giá trị chia số quan sát.

### 4.2. Median

**Từ vựng trong mục:** **Median** — trung vị.

Giá trị giữa sau khi sắp xếp. Trước khi tính, phân biệt điều kiện áp dụng và ý nghĩa của đầu vào.

```python
import numpy as np
print(np.median([2,4,100]))
```

**Tự kiểm tra:** Median là gì? **Đáp án:** Giá trị giữa sau khi sắp xếp.

### 4.3. Variance

**Từ vựng trong mục:** **Variance** — phương sai.

Mức phân tán bình phương quanh trung bình. Trước khi tính, phân biệt điều kiện áp dụng và ý nghĩa của đầu vào.

```python
import numpy as np
print(np.var([1,2,3]))
```

**Tự kiểm tra:** Variance là gì? **Đáp án:** Mức phân tán bình phương quanh trung bình.

### 4.4. Standard deviation

**Từ vựng trong mục:** **Standard deviation** — độ lệch chuẩn.

Căn bậc hai của phương sai, cùng đơn vị dữ liệu. Trước khi tính, phân biệt điều kiện áp dụng và ý nghĩa của đầu vào.

```python
import numpy as np
print(np.std([1,2,3]))
```

**Tự kiểm tra:** Standard deviation là gì? **Đáp án:** Căn bậc hai của phương sai, cùng đơn vị dữ liệu.

## 5. Năm tình huống thực tế

### Tình huống 1 — Trung bình thời gian giao hàng

**Từ vựng trong mục:** **Mean** — trung bình.

**Vấn đề:** Trung bình thời gian giao hàng.

**Vì sao chọn phương pháp này?** Mean tóm tắt thời gian thường gặp khi dữ liệu tương đối đều. Không dùng kết quả mô phỏng làm bằng chứng thống kê khi thiếu đủ mẫu và giả định.

**Dữ liệu:** [2,3,4] ngày.

**Quy trình:** làm rõ giả định → mô tả biến cố/đặc trưng → chọn hàm → kiểm tra kết quả, giới hạn và độ nhạy.

```python
import numpy as np
print(np.mean([2,3,4]))
```


### Tình huống 2 — So trung vị tiền hàng

**Từ vựng trong mục:** **Median** — trung vị.

**Vấn đề:** So trung vị tiền hàng.

**Vì sao chọn phương pháp này?** Có đơn cực lớn nên median dễ đại diện cho giá phổ biến hơn. Không dùng kết quả mô phỏng làm bằng chứng thống kê khi thiếu đủ mẫu và giả định.

**Dữ liệu:** [100,120,10000] nghìn đồng.

**Quy trình:** làm rõ giả định → mô tả biến cố/đặc trưng → chọn hàm → kiểm tra kết quả, giới hạn và độ nhạy.

```python
import numpy as np
x=[100,120,10000]
print(np.mean(x),np.median(x))
```


### Tình huống 3 — Tính phương sai điểm

**Từ vựng trong mục:** **Variance** — phương sai.

**Vấn đề:** Tính phương sai điểm.

**Vì sao chọn phương pháp này?** Variance đo sự phân tán theo đơn vị bình phương. Không dùng kết quả mô phỏng làm bằng chứng thống kê khi thiếu đủ mẫu và giả định.

**Dữ liệu:** [6,8,10] điểm.

**Quy trình:** làm rõ giả định → mô tả biến cố/đặc trưng → chọn hàm → kiểm tra kết quả, giới hạn và độ nhạy.

```python
import numpy as np
print(np.var([6,8,10],ddof=0))
```


### Tình huống 4 — Xem độ ổn định cảm biến

**Từ vựng trong mục:** **Standard deviation** — độ lệch chuẩn.

**Vấn đề:** Xem độ ổn định cảm biến.

**Vì sao chọn phương pháp này?** Std biểu diễn độ phân tán cùng đơn vị với giá trị gốc. Không dùng kết quả mô phỏng làm bằng chứng thống kê khi thiếu đủ mẫu và giả định.

**Dữ liệu:** [20,21,19,20] độ C.

**Quy trình:** làm rõ giả định → mô tả biến cố/đặc trưng → chọn hàm → kiểm tra kết quả, giới hạn và độ nhạy.

```python
import numpy as np
print(np.std([20,21,19,20],ddof=0))
```


### Tình huống 5 — Tìm loại sản phẩm phổ biến

**Từ vựng trong mục:** **Mean** — trung bình.

**Vấn đề:** Tìm loại sản phẩm phổ biến.

**Vì sao chọn phương pháp này?** value_counts cho số lần mỗi nhãn xuất hiện. Không dùng kết quả mô phỏng làm bằng chứng thống kê khi thiếu đủ mẫu và giả định.

**Dữ liệu:** Nhãn A,A,B,C,A.

**Quy trình:** làm rõ giả định → mô tả biến cố/đặc trưng → chọn hàm → kiểm tra kết quả, giới hạn và độ nhạy.

```python
import pandas as pd
s=pd.Series(["A","A","B","C","A"])
print(s.value_counts())
```


## 6. Những nhầm lẫn thường gặp

Xác suất có điều kiện cần mẫu nền; xác suất của phân phối liên tục tại một điểm không phải PDF; thống kê từ một nhóm nhỏ không tự chứng minh kết quả cho quần thể. Chú ý định nghĩa mean/std và giả định độc lập.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.


**Q1. What is Mean? — Thuật ngữ Mean là gì?**

A. Another concept means Giá trị giữa sau khi sắp xếp — Giá trị giữa sau khi sắp xếp

B. It means Tổng giá trị chia số quan sát — Tổng giá trị chia số quan sát

C. Another concept means Mức phân tán bình phương quanh trung bình — Mức phân tán bình phương quanh trung bình

D. Another concept means Căn bậc hai của phương sai, cùng đơn vị dữ liệu — Căn bậc hai của phương sai, cùng đơn vị dữ liệu


**Q2. What is Median? — Thuật ngữ Median là gì?**

A. It means Giá trị giữa sau khi sắp xếp — Giá trị giữa sau khi sắp xếp

B. Another concept means Mức phân tán bình phương quanh trung bình — Mức phân tán bình phương quanh trung bình

C. Another concept means Căn bậc hai của phương sai, cùng đơn vị dữ liệu — Căn bậc hai của phương sai, cùng đơn vị dữ liệu

D. Another concept means Tổng giá trị chia số quan sát — Tổng giá trị chia số quan sát


**Q3. What is Variance? — Thuật ngữ Variance là gì?**

A. Another concept means Căn bậc hai của phương sai, cùng đơn vị dữ liệu — Căn bậc hai của phương sai, cùng đơn vị dữ liệu

B. Another concept means Tổng giá trị chia số quan sát — Tổng giá trị chia số quan sát

C. Another concept means Giá trị giữa sau khi sắp xếp — Giá trị giữa sau khi sắp xếp

D. It means Mức phân tán bình phương quanh trung bình — Mức phân tán bình phương quanh trung bình


**Q4. What is Standard deviation? — Thuật ngữ Standard deviation là gì?**

A. Another concept means Tổng giá trị chia số quan sát — Tổng giá trị chia số quan sát

B. Another concept means Giá trị giữa sau khi sắp xếp — Giá trị giữa sau khi sắp xếp

C. It means Căn bậc hai của phương sai, cùng đơn vị dữ liệu — Căn bậc hai của phương sai, cùng đơn vị dữ liệu

D. Another concept means Mức phân tán bình phương quanh trung bình — Mức phân tán bình phương quanh trung bình


**Q5. What does np.mean()/np.median() calculate? — Hàm np.mean()/np.median() tính gì?**

A. Another calculation is ddof=0 cho quần thể, ddof=1 cho mẫu — ddof=0 cho quần thể, ddof=1 cho mẫu

B. It calculates Trung bình và trung vị, median bớt nhạy với giá trị cực lớn — Trung bình và trung vị, median bớt nhạy với giá trị cực lớn

C. Another calculation is Độ lệch chuẩn nhất quán quy ước ddof — Độ lệch chuẩn nhất quán quy ước ddof

D. Another calculation is Giá trị phổ biến và tần suất — Giá trị phổ biến và tần suất


**Q6. What does np.var(x,ddof=0/1) calculate? — Hàm np.var(x,ddof=0/1) tính gì?**

A. It calculates ddof=0 cho quần thể, ddof=1 cho mẫu — ddof=0 cho quần thể, ddof=1 cho mẫu

B. Another calculation is Độ lệch chuẩn nhất quán quy ước ddof — Độ lệch chuẩn nhất quán quy ước ddof

C. Another calculation is Giá trị phổ biến và tần suất — Giá trị phổ biến và tần suất

D. Another calculation is Trung bình và trung vị, median bớt nhạy với giá trị cực lớn — Trung bình và trung vị, median bớt nhạy với giá trị cực lớn


**Q7. What does np.std(x,ddof=0/1) calculate? — Hàm np.std(x,ddof=0/1) tính gì?**

A. Another calculation is Giá trị phổ biến và tần suất — Giá trị phổ biến và tần suất

B. Another calculation is Trung bình và trung vị, median bớt nhạy với giá trị cực lớn — Trung bình và trung vị, median bớt nhạy với giá trị cực lớn

C. Another calculation is ddof=0 cho quần thể, ddof=1 cho mẫu — ddof=0 cho quần thể, ddof=1 cho mẫu

D. It calculates Độ lệch chuẩn nhất quán quy ước ddof — Độ lệch chuẩn nhất quán quy ước ddof


**Q8. What does pd.Series.mode()/value_counts() calculate? — Hàm pd.Series.mode()/value_counts() tính gì?**

A. Another calculation is Trung bình và trung vị, median bớt nhạy với giá trị cực lớn — Trung bình và trung vị, median bớt nhạy với giá trị cực lớn

B. Another calculation is ddof=0 cho quần thể, ddof=1 cho mẫu — ddof=0 cho quần thể, ddof=1 cho mẫu

C. It calculates Giá trị phổ biến và tần suất — Giá trị phổ biến và tần suất

D. Another calculation is Độ lệch chuẩn nhất quán quy ước ddof — Độ lệch chuẩn nhất quán quy ước ddof


**Q9. Why use this method in scenario 1? — Vì sao chọn phương pháp trong tình huống 1?**

A. Có đơn cực lớn nên median dễ đại diện cho giá phổ biến hơn — Có đơn cực lớn nên median dễ đại diện cho giá phổ biến hơn

B. Mean tóm tắt thời gian thường gặp khi dữ liệu tương đối đều — Mean tóm tắt thời gian thường gặp khi dữ liệu tương đối đều

C. Variance đo sự phân tán theo đơn vị bình phương — Variance đo sự phân tán theo đơn vị bình phương

D. Std biểu diễn độ phân tán cùng đơn vị với giá trị gốc — Std biểu diễn độ phân tán cùng đơn vị với giá trị gốc


**Q10. Why use this method in scenario 2? — Vì sao chọn phương pháp trong tình huống 2?**

A. Có đơn cực lớn nên median dễ đại diện cho giá phổ biến hơn — Có đơn cực lớn nên median dễ đại diện cho giá phổ biến hơn

B. Variance đo sự phân tán theo đơn vị bình phương — Variance đo sự phân tán theo đơn vị bình phương

C. Std biểu diễn độ phân tán cùng đơn vị với giá trị gốc — Std biểu diễn độ phân tán cùng đơn vị với giá trị gốc

D. value_counts cho số lần mỗi nhãn xuất hiện — value_counts cho số lần mỗi nhãn xuất hiện


**Q11. Why use this method in scenario 3? — Vì sao chọn phương pháp trong tình huống 3?**

A. Std biểu diễn độ phân tán cùng đơn vị với giá trị gốc — Std biểu diễn độ phân tán cùng đơn vị với giá trị gốc

B. value_counts cho số lần mỗi nhãn xuất hiện — value_counts cho số lần mỗi nhãn xuất hiện

C. Mean tóm tắt thời gian thường gặp khi dữ liệu tương đối đều — Mean tóm tắt thời gian thường gặp khi dữ liệu tương đối đều

D. Variance đo sự phân tán theo đơn vị bình phương — Variance đo sự phân tán theo đơn vị bình phương


**Q12. Why use this method in scenario 4? — Vì sao chọn phương pháp trong tình huống 4?**

A. value_counts cho số lần mỗi nhãn xuất hiện — value_counts cho số lần mỗi nhãn xuất hiện

B. Mean tóm tắt thời gian thường gặp khi dữ liệu tương đối đều — Mean tóm tắt thời gian thường gặp khi dữ liệu tương đối đều

C. Std biểu diễn độ phân tán cùng đơn vị với giá trị gốc — Std biểu diễn độ phân tán cùng đơn vị với giá trị gốc

D. Có đơn cực lớn nên median dễ đại diện cho giá phổ biến hơn — Có đơn cực lớn nên median dễ đại diện cho giá phổ biến hơn


**Q13. Why use this method in scenario 5? — Vì sao chọn phương pháp trong tình huống 5?**

A. Mean tóm tắt thời gian thường gặp khi dữ liệu tương đối đều — Mean tóm tắt thời gian thường gặp khi dữ liệu tương đối đều

B. value_counts cho số lần mỗi nhãn xuất hiện — value_counts cho số lần mỗi nhãn xuất hiện

C. Có đơn cực lớn nên median dễ đại diện cho giá phổ biến hơn — Có đơn cực lớn nên median dễ đại diện cho giá phổ biến hơn

D. Variance đo sự phân tán theo đơn vị bình phương — Variance đo sự phân tán theo đơn vị bình phương


**Q14. Which input is from scenario 1? — Dữ liệu nào thuộc tình huống 1?**

A. The input is [2,3,4] ngày — [2,3,4] ngày

B. Another input is [100,120,10000] nghìn đồng — [100,120,10000] nghìn đồng

C. Another input is [6,8,10] điểm — [6,8,10] điểm

D. Another input is [20,21,19,20] độ C — [20,21,19,20] độ C


**Q15. Which input is from scenario 2? — Dữ liệu nào thuộc tình huống 2?**

A. Another input is [6,8,10] điểm — [6,8,10] điểm

B. Another input is [20,21,19,20] độ C — [20,21,19,20] độ C

C. Another input is Nhãn A,A,B,C,A — Nhãn A,A,B,C,A

D. The input is [100,120,10000] nghìn đồng — [100,120,10000] nghìn đồng


**Q16. Which input is from scenario 3? — Dữ liệu nào thuộc tình huống 3?**

A. Another input is [20,21,19,20] độ C — [20,21,19,20] độ C

B. Another input is Nhãn A,A,B,C,A — Nhãn A,A,B,C,A

C. The input is [6,8,10] điểm — [6,8,10] điểm

D. Another input is [2,3,4] ngày — [2,3,4] ngày


**Q17. Which input is from scenario 4? — Dữ liệu nào thuộc tình huống 4?**

A. Another input is Nhãn A,A,B,C,A — Nhãn A,A,B,C,A

B. The input is [20,21,19,20] độ C — [20,21,19,20] độ C

C. Another input is [2,3,4] ngày — [2,3,4] ngày

D. Another input is [100,120,10000] nghìn đồng — [100,120,10000] nghìn đồng


**Q18. Which input is from scenario 5? — Dữ liệu nào thuộc tình huống 5?**

A. The input is Nhãn A,A,B,C,A — Nhãn A,A,B,C,A

B. Another input is [2,3,4] ngày — [2,3,4] ngày

C. Another input is [100,120,10000] nghìn đồng — [100,120,10000] nghìn đồng

D. Another input is [6,8,10] điểm — [6,8,10] điểm


**Q19. What must a statistical report mention? — Báo cáo thống kê cần nêu gì?**

A. Only plot colors — Chỉ màu biểu đồ

B. Only a filename — Chỉ tên tệp

C. Only code line count — Chỉ số dòng code

D. Assumptions, units and sample size — Giả định, đơn vị và kích thước mẫu


**Q20. What makes a numerical result reliable? — Điều gì làm kết quả số đáng tin?**

A. Assuming all data independent — Cho rằng mọi dữ liệu độc lập

B. Deleting verification — Xóa bước xác minh

C. Checking assumptions and edge cases — Kiểm tra giả định và trường hợp biên

D. Ignoring missing inputs — Bỏ dữ liệu thiếu mà không đánh giá

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | It means Tổng giá trị chia số quan sát | Tổng giá trị chia số quan sát |
| Q2 | **A** | It means Giá trị giữa sau khi sắp xếp | Giá trị giữa sau khi sắp xếp |
| Q3 | **D** | It means Mức phân tán bình phương quanh trung bình | Mức phân tán bình phương quanh trung bình |
| Q4 | **C** | It means Căn bậc hai của phương sai, cùng đơn vị dữ liệu | Căn bậc hai của phương sai, cùng đơn vị dữ liệu |
| Q5 | **B** | It calculates Trung bình và trung vị, median bớt nhạy với giá trị cực lớn | Trung bình và trung vị, median bớt nhạy với giá trị cực lớn |
| Q6 | **A** | It calculates ddof=0 cho quần thể, ddof=1 cho mẫu | ddof=0 cho quần thể, ddof=1 cho mẫu |
| Q7 | **D** | It calculates Độ lệch chuẩn nhất quán quy ước ddof | Độ lệch chuẩn nhất quán quy ước ddof |
| Q8 | **C** | It calculates Giá trị phổ biến và tần suất | Giá trị phổ biến và tần suất |
| Q9 | **B** | Mean tóm tắt thời gian thường gặp khi dữ liệu tương đối đều | Mean tóm tắt thời gian thường gặp khi dữ liệu tương đối đều |
| Q10 | **A** | Có đơn cực lớn nên median dễ đại diện cho giá phổ biến hơn | Có đơn cực lớn nên median dễ đại diện cho giá phổ biến hơn |
| Q11 | **D** | Variance đo sự phân tán theo đơn vị bình phương | Variance đo sự phân tán theo đơn vị bình phương |
| Q12 | **C** | Std biểu diễn độ phân tán cùng đơn vị với giá trị gốc | Std biểu diễn độ phân tán cùng đơn vị với giá trị gốc |
| Q13 | **B** | value_counts cho số lần mỗi nhãn xuất hiện | value_counts cho số lần mỗi nhãn xuất hiện |
| Q14 | **A** | The input is [2,3,4] ngày | [2,3,4] ngày |
| Q15 | **D** | The input is [100,120,10000] nghìn đồng | [100,120,10000] nghìn đồng |
| Q16 | **C** | The input is [6,8,10] điểm | [6,8,10] điểm |
| Q17 | **B** | The input is [20,21,19,20] độ C | [20,21,19,20] độ C |
| Q18 | **A** | The input is Nhãn A,A,B,C,A | Nhãn A,A,B,C,A |
| Q19 | **D** | Assumptions, units and sample size | Giả định, đơn vị và kích thước mẫu |
| Q20 | **C** | Checking assumptions and edge cases | Kiểm tra giả định và trường hợp biên |

## 8. Liên hệ bài tiếp theo

`NumPy/Pandas → Thống kê mô tả → Outlier → ML`.
