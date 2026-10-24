# PY-39 — Lấy mẫu, CLT và sai số chuẩn


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Population** — tổng thể; **Sample** — mẫu.

`Thống kê → Sampling → Central Limit Theorem → Confidence Interval`

Kiến thức giúp sinh viên dùng Python để hiểu dữ liệu, đánh giá độ bất định và chuẩn bị dữ liệu cho AI.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Khái niệm |
|---|---|---|
| Population | tổng thể | Toàn bộ đối tượng cần nghiên cứu |
| Sample | mẫu | Nhóm con lấy từ tổng thể theo cách rõ ràng |
| CLT | định lý giới hạn trung tâm | Phân phối trung bình mẫu tiến gần chuẩn theo điều kiện thích hợp |
| Standard error | sai số chuẩn | Độ biến thiên của một thống kê giữa các mẫu |

## 3. Thư viện và hàm Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cách viết | Khi nào dùng, ý nghĩa tham số |
|---|---|
| `df.sample(n=,random_state=)` | Lấy mẫu có thể lặp, chú ý phương pháp lấy mẫu |
| `rng.choice(values,size=,replace=)` | Lấy mẫu thay thế hoặc không thay thế |
| `np.mean(samples,axis=1)` | Tính trung bình từng lần lấy mẫu |
| `s / np.sqrt(n)` | Ước lượng SE của mean từ std mẫu s |

## 4. Khái niệm với ví dụ nhỏ

### 4.1. Population

**Từ vựng trong mục:** **Population** — tổng thể.

Toàn bộ đối tượng cần nghiên cứu. Thử đoạn code để thấy ý nghĩa đầu ra trước khi đọc bài tập.

```python
population=list(range(100));print(len(population))
```

**Tự kiểm tra:** Population là gì? **Đáp án:** Toàn bộ đối tượng cần nghiên cứu.

### 4.2. Sample

**Từ vựng trong mục:** **Sample** — mẫu.

Nhóm con lấy từ tổng thể theo cách rõ ràng. Thử đoạn code để thấy ý nghĩa đầu ra trước khi đọc bài tập.

```python
import random
print(random.sample(range(20),5))
```

**Tự kiểm tra:** Sample là gì? **Đáp án:** Nhóm con lấy từ tổng thể theo cách rõ ràng.

### 4.3. CLT

**Từ vựng trong mục:** **CLT** — định lý giới hạn trung tâm.

Phân phối trung bình mẫu tiến gần chuẩn theo điều kiện thích hợp. Thử đoạn code để thấy ý nghĩa đầu ra trước khi đọc bài tập.

```python
import numpy as np
r=np.random.default_rng(1);print([r.normal(size=10).mean() for _ in range(3)])
```

**Tự kiểm tra:** CLT là gì? **Đáp án:** Phân phối trung bình mẫu tiến gần chuẩn theo điều kiện thích hợp.

### 4.4. Standard error

**Từ vựng trong mục:** **Standard error** — sai số chuẩn.

Độ biến thiên của một thống kê giữa các mẫu. Thử đoạn code để thấy ý nghĩa đầu ra trước khi đọc bài tập.

```python
import numpy as np
print(np.std([1,2,3],ddof=1)/np.sqrt(3))
```

**Tự kiểm tra:** Standard error là gì? **Đáp án:** Độ biến thiên của một thống kê giữa các mẫu.

## 5. Năm tình huống thực tế

### Tình huống 1 — Rút mẫu kiểm kê

**Từ vựng trong mục:** **Population** — tổng thể.

**Tình huống thực tế:** Một nhóm phân tích dữ liệu cần rút mẫu kiểm kê cho công việc của mình. Dữ liệu đầu vào: 20 đơn, lấy ngẫu nhiên 5. Hãy xây dựng chương trình thực hiện yêu cầu và trình bày kết quả.

**Vì sao chọn cách này?** Lấy ngẫu nhiên một số đơn để kiểm tra thủ công; không áp dụng kết luận ngoài phạm vi giả định của dữ liệu.


**Quy trình:** làm rõ ý nghĩa đầu vào → chọn phương pháp → chạy code → kiểm tra/diễn giải kết quả.

```python
import random
print(random.Random(42).sample(list(range(1,21)),5))
```


### Tình huống 2 — So biến thiên mean mẫu

**Từ vựng trong mục:** **Sample** — mẫu.

**Tình huống thực tế:** Một nhóm phân tích dữ liệu cần so biến thiên mean mẫu cho công việc của mình. Dữ liệu đầu vào: Tổng thể 10000 giá trị lệch, mỗi mẫu n=40. Hãy xây dựng chương trình thực hiện yêu cầu và trình bày kết quả.

**Vì sao chọn cách này?** Rút mẫu nhiều lần để quan sát trung bình mẫu; không áp dụng kết luận ngoài phạm vi giả định của dữ liệu.


**Quy trình:** làm rõ ý nghĩa đầu vào → chọn phương pháp → chạy code → kiểm tra/diễn giải kết quả.

```python
import numpy as np
r=np.random.default_rng(1)
pop=r.exponential(scale=2,size=10000)
means=[r.choice(pop,size=40,replace=True).mean() for _ in range(200)]
print(np.mean(means),np.std(means))
```


### Tình huống 3 — Tính sai số chuẩn điểm

**Từ vựng trong mục:** **CLT** — định lý giới hạn trung tâm.

**Tình huống thực tế:** Một trung tâm đào tạo cần tính sai số chuẩn điểm cho công việc của mình. Dữ liệu đầu vào: 5 điểm [6,7,8,9,10]. Hãy xây dựng chương trình thực hiện yêu cầu và trình bày kết quả.

**Vì sao chọn cách này?** SE khác độ lệch chuẩn của điểm riêng lẻ; không áp dụng kết luận ngoài phạm vi giả định của dữ liệu.


**Quy trình:** làm rõ ý nghĩa đầu vào → chọn phương pháp → chạy code → kiểm tra/diễn giải kết quả.

```python
import numpy as np
x=np.array([6,7,8,9,10],dtype=float)
print(x.std(ddof=1)/np.sqrt(len(x)))
```


### Tình huống 4 — Cỡ mẫu tăng tác động SE

**Từ vựng trong mục:** **Standard error** — sai số chuẩn.

**Tình huống thực tế:** Một nhóm phân tích dữ liệu cần cỡ mẫu tăng tác động se cho công việc của mình. Dữ liệu đầu vào: sigma=10, n=25 và 100. Hãy xây dựng chương trình thực hiện yêu cầu và trình bày kết quả.

**Vì sao chọn cách này?** Với sigma giữ nguyên, SE giảm theo căn n; không áp dụng kết luận ngoài phạm vi giả định của dữ liệu.


**Quy trình:** làm rõ ý nghĩa đầu vào → chọn phương pháp → chạy code → kiểm tra/diễn giải kết quả.

```python
import numpy as np
sigma=10
for n in [25,100]:print(n,sigma/np.sqrt(n))
```


### Tình huống 5 — Lấy mẫu bảng khách hàng

**Từ vựng trong mục:** **Population** — tổng thể.

**Tình huống thực tế:** Một doanh nghiệp cần lấy mẫu bảng khách hàng cho công việc của mình. Dữ liệu đầu vào: 10 khách, lấy 3. Hãy xây dựng chương trình thực hiện yêu cầu và trình bày kết quả.

**Vì sao chọn cách này?** random_state giữ kết quả thử lặp lại; không áp dụng kết luận ngoài phạm vi giả định của dữ liệu.


**Quy trình:** làm rõ ý nghĩa đầu vào → chọn phương pháp → chạy code → kiểm tra/diễn giải kết quả.

```python
import pandas as pd
df=pd.DataFrame({"id":list(range(10))})
print(df.sample(n=3,random_state=42))
```


## 6. Nhầm lẫn thường gặp

- Không nhầm thống kê/tỷ lệ mô phỏng với xác suất dự đoán chắc chắn.
- Kiểm tra giả định, cỡ mẫu, đơn vị, độ nhạy kết quả và data leakage trước khi ứng dụng AI thật.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.


**Q1. What is Population? — Khái niệm Population là gì?**

A. Another concept is Nhóm con lấy từ tổng thể theo cách rõ ràng — Nhóm con lấy từ tổng thể theo cách rõ ràng

B. It is Toàn bộ đối tượng cần nghiên cứu — Toàn bộ đối tượng cần nghiên cứu

C. Another concept is Phân phối trung bình mẫu tiến gần chuẩn theo điều kiện thích hợp — Phân phối trung bình mẫu tiến gần chuẩn theo điều kiện thích hợp

D. Another concept is Độ biến thiên của một thống kê giữa các mẫu — Độ biến thiên của một thống kê giữa các mẫu


**Q2. What is Sample? — Khái niệm Sample là gì?**

A. It is Nhóm con lấy từ tổng thể theo cách rõ ràng — Nhóm con lấy từ tổng thể theo cách rõ ràng

B. Another concept is Phân phối trung bình mẫu tiến gần chuẩn theo điều kiện thích hợp — Phân phối trung bình mẫu tiến gần chuẩn theo điều kiện thích hợp

C. Another concept is Độ biến thiên của một thống kê giữa các mẫu — Độ biến thiên của một thống kê giữa các mẫu

D. Another concept is Toàn bộ đối tượng cần nghiên cứu — Toàn bộ đối tượng cần nghiên cứu


**Q3. What is CLT? — Khái niệm CLT là gì?**

A. Another concept is Độ biến thiên của một thống kê giữa các mẫu — Độ biến thiên của một thống kê giữa các mẫu

B. Another concept is Toàn bộ đối tượng cần nghiên cứu — Toàn bộ đối tượng cần nghiên cứu

C. Another concept is Nhóm con lấy từ tổng thể theo cách rõ ràng — Nhóm con lấy từ tổng thể theo cách rõ ràng

D. It is Phân phối trung bình mẫu tiến gần chuẩn theo điều kiện thích hợp — Phân phối trung bình mẫu tiến gần chuẩn theo điều kiện thích hợp


**Q4. What is Standard error? — Khái niệm Standard error là gì?**

A. Another concept is Toàn bộ đối tượng cần nghiên cứu — Toàn bộ đối tượng cần nghiên cứu

B. Another concept is Nhóm con lấy từ tổng thể theo cách rõ ràng — Nhóm con lấy từ tổng thể theo cách rõ ràng

C. It is Độ biến thiên của một thống kê giữa các mẫu — Độ biến thiên của một thống kê giữa các mẫu

D. Another concept is Phân phối trung bình mẫu tiến gần chuẩn theo điều kiện thích hợp — Phân phối trung bình mẫu tiến gần chuẩn theo điều kiện thích hợp


**Q5. When should df.sample(n=,random_state=) be used? — Khi nào nên dùng df.sample(n=,random_state=)?**

A. Another operation is for Lấy mẫu thay thế hoặc không thay thế — Lấy mẫu thay thế hoặc không thay thế

B. When you need to Lấy mẫu có thể lặp, chú ý phương pháp lấy mẫu — Lấy mẫu có thể lặp, chú ý phương pháp lấy mẫu

C. Another operation is for Tính trung bình từng lần lấy mẫu — Tính trung bình từng lần lấy mẫu

D. Another operation is for Ước lượng SE của mean từ std mẫu s — Ước lượng SE của mean từ std mẫu s


**Q6. When should rng.choice(values,size=,replace=) be used? — Khi nào nên dùng rng.choice(values,size=,replace=)?**

A. When you need to Lấy mẫu thay thế hoặc không thay thế — Lấy mẫu thay thế hoặc không thay thế

B. Another operation is for Tính trung bình từng lần lấy mẫu — Tính trung bình từng lần lấy mẫu

C. Another operation is for Ước lượng SE của mean từ std mẫu s — Ước lượng SE của mean từ std mẫu s

D. Another operation is for Lấy mẫu có thể lặp, chú ý phương pháp lấy mẫu — Lấy mẫu có thể lặp, chú ý phương pháp lấy mẫu


**Q7. When should np.mean(samples,axis=1) be used? — Khi nào nên dùng np.mean(samples,axis=1)?**

A. Another operation is for Ước lượng SE của mean từ std mẫu s — Ước lượng SE của mean từ std mẫu s

B. Another operation is for Lấy mẫu có thể lặp, chú ý phương pháp lấy mẫu — Lấy mẫu có thể lặp, chú ý phương pháp lấy mẫu

C. Another operation is for Lấy mẫu thay thế hoặc không thay thế — Lấy mẫu thay thế hoặc không thay thế

D. When you need to Tính trung bình từng lần lấy mẫu — Tính trung bình từng lần lấy mẫu


**Q8. When should s / np.sqrt(n) be used? — Khi nào nên dùng s / np.sqrt(n)?**

A. Another operation is for Lấy mẫu có thể lặp, chú ý phương pháp lấy mẫu — Lấy mẫu có thể lặp, chú ý phương pháp lấy mẫu

B. Another operation is for Lấy mẫu thay thế hoặc không thay thế — Lấy mẫu thay thế hoặc không thay thế

C. When you need to Ước lượng SE của mean từ std mẫu s — Ước lượng SE của mean từ std mẫu s

D. Another operation is for Tính trung bình từng lần lấy mẫu — Tính trung bình từng lần lấy mẫu


**Q9. Why is this method used in scenario 1? — Vì sao dùng phương pháp ở tình huống 1?**

A. Rút mẫu nhiều lần để quan sát trung bình mẫu — Rút mẫu nhiều lần để quan sát trung bình mẫu

B. Lấy ngẫu nhiên một số đơn để kiểm tra thủ công — Lấy ngẫu nhiên một số đơn để kiểm tra thủ công

C. SE khác độ lệch chuẩn của điểm riêng lẻ — SE khác độ lệch chuẩn của điểm riêng lẻ

D. Với sigma giữ nguyên, SE giảm theo căn n — Với sigma giữ nguyên, SE giảm theo căn n


**Q10. Why is this method used in scenario 2? — Vì sao dùng phương pháp ở tình huống 2?**

A. Rút mẫu nhiều lần để quan sát trung bình mẫu — Rút mẫu nhiều lần để quan sát trung bình mẫu

B. SE khác độ lệch chuẩn của điểm riêng lẻ — SE khác độ lệch chuẩn của điểm riêng lẻ

C. Với sigma giữ nguyên, SE giảm theo căn n — Với sigma giữ nguyên, SE giảm theo căn n

D. random_state giữ kết quả thử lặp lại — random_state giữ kết quả thử lặp lại


**Q11. Why is this method used in scenario 3? — Vì sao dùng phương pháp ở tình huống 3?**

A. Với sigma giữ nguyên, SE giảm theo căn n — Với sigma giữ nguyên, SE giảm theo căn n

B. random_state giữ kết quả thử lặp lại — random_state giữ kết quả thử lặp lại

C. Lấy ngẫu nhiên một số đơn để kiểm tra thủ công — Lấy ngẫu nhiên một số đơn để kiểm tra thủ công

D. SE khác độ lệch chuẩn của điểm riêng lẻ — SE khác độ lệch chuẩn của điểm riêng lẻ


**Q12. Why is this method used in scenario 4? — Vì sao dùng phương pháp ở tình huống 4?**

A. random_state giữ kết quả thử lặp lại — random_state giữ kết quả thử lặp lại

B. Lấy ngẫu nhiên một số đơn để kiểm tra thủ công — Lấy ngẫu nhiên một số đơn để kiểm tra thủ công

C. Với sigma giữ nguyên, SE giảm theo căn n — Với sigma giữ nguyên, SE giảm theo căn n

D. Rút mẫu nhiều lần để quan sát trung bình mẫu — Rút mẫu nhiều lần để quan sát trung bình mẫu


**Q13. Why is this method used in scenario 5? — Vì sao dùng phương pháp ở tình huống 5?**

A. Lấy ngẫu nhiên một số đơn để kiểm tra thủ công — Lấy ngẫu nhiên một số đơn để kiểm tra thủ công

B. random_state giữ kết quả thử lặp lại — random_state giữ kết quả thử lặp lại

C. Rút mẫu nhiều lần để quan sát trung bình mẫu — Rút mẫu nhiều lần để quan sát trung bình mẫu

D. SE khác độ lệch chuẩn của điểm riêng lẻ — SE khác độ lệch chuẩn của điểm riêng lẻ


**Q14. Which input describes scenario 1? — Dữ liệu nào thuộc tình huống 1?**

A. The input is 20 đơn, lấy ngẫu nhiên 5 — 20 đơn, lấy ngẫu nhiên 5

B. Another input is Tổng thể 10000 giá trị lệch, mỗi mẫu n=40 — Tổng thể 10000 giá trị lệch, mỗi mẫu n=40

C. Another input is 5 điểm [6,7,8,9,10] — 5 điểm [6,7,8,9,10]

D. Another input is sigma=10, n=25 và 100 — sigma=10, n=25 và 100


**Q15. Which input describes scenario 2? — Dữ liệu nào thuộc tình huống 2?**

A. Another input is 5 điểm [6,7,8,9,10] — 5 điểm [6,7,8,9,10]

B. Another input is sigma=10, n=25 và 100 — sigma=10, n=25 và 100

C. Another input is 10 khách, lấy 3 — 10 khách, lấy 3

D. The input is Tổng thể 10000 giá trị lệch, mỗi mẫu n=40 — Tổng thể 10000 giá trị lệch, mỗi mẫu n=40


**Q16. Which input describes scenario 3? — Dữ liệu nào thuộc tình huống 3?**

A. Another input is sigma=10, n=25 và 100 — sigma=10, n=25 và 100

B. Another input is 10 khách, lấy 3 — 10 khách, lấy 3

C. The input is 5 điểm [6,7,8,9,10] — 5 điểm [6,7,8,9,10]

D. Another input is 20 đơn, lấy ngẫu nhiên 5 — 20 đơn, lấy ngẫu nhiên 5


**Q17. Which input describes scenario 4? — Dữ liệu nào thuộc tình huống 4?**

A. Another input is 10 khách, lấy 3 — 10 khách, lấy 3

B. The input is sigma=10, n=25 và 100 — sigma=10, n=25 và 100

C. Another input is 20 đơn, lấy ngẫu nhiên 5 — 20 đơn, lấy ngẫu nhiên 5

D. Another input is Tổng thể 10000 giá trị lệch, mỗi mẫu n=40 — Tổng thể 10000 giá trị lệch, mỗi mẫu n=40


**Q18. Which input describes scenario 5? — Dữ liệu nào thuộc tình huống 5?**

A. The input is 10 khách, lấy 3 — 10 khách, lấy 3

B. Another input is 20 đơn, lấy ngẫu nhiên 5 — 20 đơn, lấy ngẫu nhiên 5

C. Another input is Tổng thể 10000 giá trị lệch, mỗi mẫu n=40 — Tổng thể 10000 giá trị lệch, mỗi mẫu n=40

D. Another input is 5 điểm [6,7,8,9,10] — 5 điểm [6,7,8,9,10]


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
| Q1 | **B** | It is Toàn bộ đối tượng cần nghiên cứu | Toàn bộ đối tượng cần nghiên cứu |
| Q2 | **A** | It is Nhóm con lấy từ tổng thể theo cách rõ ràng | Nhóm con lấy từ tổng thể theo cách rõ ràng |
| Q3 | **D** | It is Phân phối trung bình mẫu tiến gần chuẩn theo điều kiện thích hợp | Phân phối trung bình mẫu tiến gần chuẩn theo điều kiện thích hợp |
| Q4 | **C** | It is Độ biến thiên của một thống kê giữa các mẫu | Độ biến thiên của một thống kê giữa các mẫu |
| Q5 | **B** | When you need to Lấy mẫu có thể lặp, chú ý phương pháp lấy mẫu | Lấy mẫu có thể lặp, chú ý phương pháp lấy mẫu |
| Q6 | **A** | When you need to Lấy mẫu thay thế hoặc không thay thế | Lấy mẫu thay thế hoặc không thay thế |
| Q7 | **D** | When you need to Tính trung bình từng lần lấy mẫu | Tính trung bình từng lần lấy mẫu |
| Q8 | **C** | When you need to Ước lượng SE của mean từ std mẫu s | Ước lượng SE của mean từ std mẫu s |
| Q9 | **B** | Lấy ngẫu nhiên một số đơn để kiểm tra thủ công | Lấy ngẫu nhiên một số đơn để kiểm tra thủ công |
| Q10 | **A** | Rút mẫu nhiều lần để quan sát trung bình mẫu | Rút mẫu nhiều lần để quan sát trung bình mẫu |
| Q11 | **D** | SE khác độ lệch chuẩn của điểm riêng lẻ | SE khác độ lệch chuẩn của điểm riêng lẻ |
| Q12 | **C** | Với sigma giữ nguyên, SE giảm theo căn n | Với sigma giữ nguyên, SE giảm theo căn n |
| Q13 | **B** | random_state giữ kết quả thử lặp lại | random_state giữ kết quả thử lặp lại |
| Q14 | **A** | The input is 20 đơn, lấy ngẫu nhiên 5 | 20 đơn, lấy ngẫu nhiên 5 |
| Q15 | **D** | The input is Tổng thể 10000 giá trị lệch, mỗi mẫu n=40 | Tổng thể 10000 giá trị lệch, mỗi mẫu n=40 |
| Q16 | **C** | The input is 5 điểm [6,7,8,9,10] | 5 điểm [6,7,8,9,10] |
| Q17 | **B** | The input is sigma=10, n=25 và 100 | sigma=10, n=25 và 100 |
| Q18 | **A** | The input is 10 khách, lấy 3 | 10 khách, lấy 3 |
| Q19 | **D** | Units, sample meaning and assumptions | Đơn vị, ý nghĩa mẫu và giả định |
| Q20 | **C** | An example may not generalize | Ví dụ có thể không tổng quát |

## 8. Liên hệ bài kế tiếp

`Thống kê → Sampling → Central Limit Theorem → Confidence Interval`.
