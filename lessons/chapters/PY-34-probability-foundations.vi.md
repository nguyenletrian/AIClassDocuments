# PY-34 — Xác suất, không gian mẫu và biến cố


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Experiment** — phép thử; **Sample space** — không gian mẫu.

`Logic/Tập hợp → Xác suất → Bayes → Dự đoán bất định`

Bài này kết nối dữ liệu thực nghiệm với cách tính xác suất, thống kê và các bước học máy.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Khái niệm |
|---|---|---|
| Experiment | phép thử | Thao tác có kết quả quan sát được |
| Sample space | không gian mẫu | Tập mọi kết quả khả dĩ |
| Event | biến cố | Nhóm kết quả được quan tâm |
| Probability | xác suất | Mức khả năng xảy ra một biến cố, từ 0 tới 1 |

## 3. Hàm Python và tham số quan trọng

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm / cú pháp | Cách sử dụng |
|---|---|
| `len(event)/len(space)` | Xác suất cổ điển khi kết quả đồng khả năng |
| `random.choice(values)` | Rút một phần tử ngẫu nhiên từ danh sách |
| `np.random.default_rng(seed)` | Tạo bộ sinh ngẫu nhiên tái lập |
| `np.mean(condition)` | Ước lượng tỷ lệ đúng trong mô phỏng |

## 4. Khái niệm liên quan, ví dụ nhỏ

### 4.1. Experiment

**Từ vựng trong mục:** **Experiment** — phép thử.

Thao tác có kết quả quan sát được. Trước khi tính, phân biệt điều kiện áp dụng và ý nghĩa của đầu vào.

```python
import random
print(random.choice([0,1]))
```

**Tự kiểm tra:** Experiment là gì? **Đáp án:** Thao tác có kết quả quan sát được.

### 4.2. Sample space

**Từ vựng trong mục:** **Sample space** — không gian mẫu.

Tập mọi kết quả khả dĩ. Trước khi tính, phân biệt điều kiện áp dụng và ý nghĩa của đầu vào.

```python
print(set(range(1,7)))
```

**Tự kiểm tra:** Sample space là gì? **Đáp án:** Tập mọi kết quả khả dĩ.

### 4.3. Event

**Từ vựng trong mục:** **Event** — biến cố.

Nhóm kết quả được quan tâm. Trước khi tính, phân biệt điều kiện áp dụng và ý nghĩa của đầu vào.

```python
print({2,4,6})
```

**Tự kiểm tra:** Event là gì? **Đáp án:** Nhóm kết quả được quan tâm.

### 4.4. Probability

**Từ vựng trong mục:** **Probability** — xác suất.

Mức khả năng xảy ra một biến cố, từ 0 tới 1. Trước khi tính, phân biệt điều kiện áp dụng và ý nghĩa của đầu vào.

```python
print(3/6)
```

**Tự kiểm tra:** Probability là gì? **Đáp án:** Mức khả năng xảy ra một biến cố, từ 0 tới 1.

## 5. Năm tình huống thực tế

### Tình huống 1 — Xác suất xúc xắc chẵn

**Từ vựng trong mục:** **Experiment** — phép thử.

**Tình huống thực tế:** Một nhóm phát triển AI cần xác suất xúc xắc chẵn để phục vụ một công việc cụ thể. Đầu vào được cung cấp: Xúc xắc công bằng có mặt 1..6. Hãy viết chương trình xử lý thông tin trên và giải thích kết quả.

**Vì sao chọn phương pháp này?** Ba mặt chẵn trong sáu mặt đồng khả năng. Không dùng kết quả mô phỏng làm bằng chứng thống kê khi thiếu đủ mẫu và giả định.


**Quy trình:** làm rõ giả định → mô tả biến cố/đặc trưng → chọn hàm → kiểm tra kết quả, giới hạn và độ nhạy.

```python
space=set(range(1,7));even={2,4,6}
print(len(even)/len(space))
```


### Tình huống 2 — Mô phỏng tung đồng xu

**Từ vựng trong mục:** **Sample space** — không gian mẫu.

**Tình huống thực tế:** Một nhóm phân tích đang hỗ trợ quyết định vận hành cần mô phỏng tung đồng xu để phục vụ một công việc cụ thể. Đầu vào được cung cấp: 1000 lần tung giả lập. Hãy viết chương trình xử lý thông tin trên và giải thích kết quả.

**Vì sao chọn phương pháp này?** Đếm tỷ lệ mặt sấp khi có nhiều lần thử. Không dùng kết quả mô phỏng làm bằng chứng thống kê khi thiếu đủ mẫu và giả định.


**Quy trình:** làm rõ giả định → mô tả biến cố/đặc trưng → chọn hàm → kiểm tra kết quả, giới hạn và độ nhạy.

```python
import numpy as np
rng=np.random.default_rng(42)
tosses=rng.integers(0,2,size=1000)
print(tosses.mean())
```


### Tình huống 3 — Hai xúc xắc tổng bằng 9

**Từ vựng trong mục:** **Event** — biến cố.

**Tình huống thực tế:** Một nhóm phân tích đang hỗ trợ quyết định vận hành cần hai xúc xắc tổng bằng 9 để phục vụ một công việc cụ thể. Đầu vào được cung cấp: Hai xúc xắc công bằng độc lập. Hãy viết chương trình xử lý thông tin trên và giải thích kết quả.

**Vì sao chọn phương pháp này?** Đếm cặp kết quả thỏa tổng 9 trên 36 kết quả. Không dùng kết quả mô phỏng làm bằng chứng thống kê khi thiếu đủ mẫu và giả định.


**Quy trình:** làm rõ giả định → mô tả biến cố/đặc trưng → chọn hàm → kiểm tra kết quả, giới hạn và độ nhạy.

```python
pairs=[(a,b) for a in range(1,7) for b in range(1,7)]
print(sum(a+b==9 for a,b in pairs)/len(pairs))
```


### Tình huống 4 — Ước lượng tỷ lệ sự kiện

**Từ vựng trong mục:** **Probability** — xác suất.

**Tình huống thực tế:** Một nhóm phân tích đang hỗ trợ quyết định vận hành cần ước lượng tỷ lệ sự kiện để phục vụ một công việc cụ thể. Đầu vào được cung cấp: 10000 lần với xác suất 0.2. Hãy viết chương trình xử lý thông tin trên và giải thích kết quả.

**Vì sao chọn phương pháp này?** Mô phỏng rút ngẫu nhiên với seed để lặp lại. Không dùng kết quả mô phỏng làm bằng chứng thống kê khi thiếu đủ mẫu và giả định.


**Quy trình:** làm rõ giả định → mô tả biến cố/đặc trưng → chọn hàm → kiểm tra kết quả, giới hạn và độ nhạy.

```python
import numpy as np
r=np.random.default_rng(1)
print(np.mean(r.random(10000)<.2))
```


### Tình huống 5 — So lý thuyết với thực nghiệm

**Từ vựng trong mục:** **Experiment** — phép thử.

**Tình huống thực tế:** Một nhóm phân tích đang hỗ trợ quyết định vận hành cần so lý thuyết với thực nghiệm để phục vụ một công việc cụ thể. Đầu vào được cung cấp: Đồng xu công bằng, 100 và 10000 lần. Hãy viết chương trình xử lý thông tin trên và giải thích kết quả.

**Vì sao chọn phương pháp này?** Số lượt thử tăng khiến ước lượng thường ổn định hơn. Không dùng kết quả mô phỏng làm bằng chứng thống kê khi thiếu đủ mẫu và giả định.


**Quy trình:** làm rõ giả định → mô tả biến cố/đặc trưng → chọn hàm → kiểm tra kết quả, giới hạn và độ nhạy.

```python
import numpy as np
r=np.random.default_rng(7)
for n in [100,10000]:
    print(n,(r.integers(0,2,n)==1).mean())
```


## 6. Những nhầm lẫn thường gặp

Xác suất có điều kiện cần mẫu nền; xác suất của phân phối liên tục tại một điểm không phải PDF; thống kê từ một nhóm nhỏ không tự chứng minh kết quả cho quần thể. Chú ý định nghĩa mean/std và giả định độc lập.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.


**Q1. What is Experiment? — Thuật ngữ Experiment là gì?**

A. Another concept means Tập mọi kết quả khả dĩ — Tập mọi kết quả khả dĩ

B. It means Thao tác có kết quả quan sát được — Thao tác có kết quả quan sát được

C. Another concept means Nhóm kết quả được quan tâm — Nhóm kết quả được quan tâm

D. Another concept means Mức khả năng xảy ra một biến cố, từ 0 tới 1 — Mức khả năng xảy ra một biến cố, từ 0 tới 1


**Q2. What is Sample space? — Thuật ngữ Sample space là gì?**

A. It means Tập mọi kết quả khả dĩ — Tập mọi kết quả khả dĩ

B. Another concept means Nhóm kết quả được quan tâm — Nhóm kết quả được quan tâm

C. Another concept means Mức khả năng xảy ra một biến cố, từ 0 tới 1 — Mức khả năng xảy ra một biến cố, từ 0 tới 1

D. Another concept means Thao tác có kết quả quan sát được — Thao tác có kết quả quan sát được


**Q3. What is Event? — Thuật ngữ Event là gì?**

A. Another concept means Mức khả năng xảy ra một biến cố, từ 0 tới 1 — Mức khả năng xảy ra một biến cố, từ 0 tới 1

B. Another concept means Thao tác có kết quả quan sát được — Thao tác có kết quả quan sát được

C. Another concept means Tập mọi kết quả khả dĩ — Tập mọi kết quả khả dĩ

D. It means Nhóm kết quả được quan tâm — Nhóm kết quả được quan tâm


**Q4. What is Probability? — Thuật ngữ Probability là gì?**

A. Another concept means Thao tác có kết quả quan sát được — Thao tác có kết quả quan sát được

B. Another concept means Tập mọi kết quả khả dĩ — Tập mọi kết quả khả dĩ

C. It means Mức khả năng xảy ra một biến cố, từ 0 tới 1 — Mức khả năng xảy ra một biến cố, từ 0 tới 1

D. Another concept means Nhóm kết quả được quan tâm — Nhóm kết quả được quan tâm


**Q5. What does len(event)/len(space) calculate? — Hàm len(event)/len(space) tính gì?**

A. Another calculation is Rút một phần tử ngẫu nhiên từ danh sách — Rút một phần tử ngẫu nhiên từ danh sách

B. It calculates Xác suất cổ điển khi kết quả đồng khả năng — Xác suất cổ điển khi kết quả đồng khả năng

C. Another calculation is Tạo bộ sinh ngẫu nhiên tái lập — Tạo bộ sinh ngẫu nhiên tái lập

D. Another calculation is Ước lượng tỷ lệ đúng trong mô phỏng — Ước lượng tỷ lệ đúng trong mô phỏng


**Q6. What does random.choice(values) calculate? — Hàm random.choice(values) tính gì?**

A. It calculates Rút một phần tử ngẫu nhiên từ danh sách — Rút một phần tử ngẫu nhiên từ danh sách

B. Another calculation is Tạo bộ sinh ngẫu nhiên tái lập — Tạo bộ sinh ngẫu nhiên tái lập

C. Another calculation is Ước lượng tỷ lệ đúng trong mô phỏng — Ước lượng tỷ lệ đúng trong mô phỏng

D. Another calculation is Xác suất cổ điển khi kết quả đồng khả năng — Xác suất cổ điển khi kết quả đồng khả năng


**Q7. What does np.random.default_rng(seed) calculate? — Hàm np.random.default_rng(seed) tính gì?**

A. Another calculation is Ước lượng tỷ lệ đúng trong mô phỏng — Ước lượng tỷ lệ đúng trong mô phỏng

B. Another calculation is Xác suất cổ điển khi kết quả đồng khả năng — Xác suất cổ điển khi kết quả đồng khả năng

C. Another calculation is Rút một phần tử ngẫu nhiên từ danh sách — Rút một phần tử ngẫu nhiên từ danh sách

D. It calculates Tạo bộ sinh ngẫu nhiên tái lập — Tạo bộ sinh ngẫu nhiên tái lập


**Q8. What does np.mean(condition) calculate? — Hàm np.mean(condition) tính gì?**

A. Another calculation is Xác suất cổ điển khi kết quả đồng khả năng — Xác suất cổ điển khi kết quả đồng khả năng

B. Another calculation is Rút một phần tử ngẫu nhiên từ danh sách — Rút một phần tử ngẫu nhiên từ danh sách

C. It calculates Ước lượng tỷ lệ đúng trong mô phỏng — Ước lượng tỷ lệ đúng trong mô phỏng

D. Another calculation is Tạo bộ sinh ngẫu nhiên tái lập — Tạo bộ sinh ngẫu nhiên tái lập


**Q9. Why use this method in scenario 1? — Vì sao chọn phương pháp trong tình huống 1?**

A. Đếm tỷ lệ mặt sấp khi có nhiều lần thử — Đếm tỷ lệ mặt sấp khi có nhiều lần thử

B. Ba mặt chẵn trong sáu mặt đồng khả năng — Ba mặt chẵn trong sáu mặt đồng khả năng

C. Đếm cặp kết quả thỏa tổng 9 trên 36 kết quả — Đếm cặp kết quả thỏa tổng 9 trên 36 kết quả

D. Mô phỏng rút ngẫu nhiên với seed để lặp lại — Mô phỏng rút ngẫu nhiên với seed để lặp lại


**Q10. Why use this method in scenario 2? — Vì sao chọn phương pháp trong tình huống 2?**

A. Đếm tỷ lệ mặt sấp khi có nhiều lần thử — Đếm tỷ lệ mặt sấp khi có nhiều lần thử

B. Đếm cặp kết quả thỏa tổng 9 trên 36 kết quả — Đếm cặp kết quả thỏa tổng 9 trên 36 kết quả

C. Mô phỏng rút ngẫu nhiên với seed để lặp lại — Mô phỏng rút ngẫu nhiên với seed để lặp lại

D. Số lượt thử tăng khiến ước lượng thường ổn định hơn — Số lượt thử tăng khiến ước lượng thường ổn định hơn


**Q11. Why use this method in scenario 3? — Vì sao chọn phương pháp trong tình huống 3?**

A. Mô phỏng rút ngẫu nhiên với seed để lặp lại — Mô phỏng rút ngẫu nhiên với seed để lặp lại

B. Số lượt thử tăng khiến ước lượng thường ổn định hơn — Số lượt thử tăng khiến ước lượng thường ổn định hơn

C. Ba mặt chẵn trong sáu mặt đồng khả năng — Ba mặt chẵn trong sáu mặt đồng khả năng

D. Đếm cặp kết quả thỏa tổng 9 trên 36 kết quả — Đếm cặp kết quả thỏa tổng 9 trên 36 kết quả


**Q12. Why use this method in scenario 4? — Vì sao chọn phương pháp trong tình huống 4?**

A. Số lượt thử tăng khiến ước lượng thường ổn định hơn — Số lượt thử tăng khiến ước lượng thường ổn định hơn

B. Ba mặt chẵn trong sáu mặt đồng khả năng — Ba mặt chẵn trong sáu mặt đồng khả năng

C. Mô phỏng rút ngẫu nhiên với seed để lặp lại — Mô phỏng rút ngẫu nhiên với seed để lặp lại

D. Đếm tỷ lệ mặt sấp khi có nhiều lần thử — Đếm tỷ lệ mặt sấp khi có nhiều lần thử


**Q13. Why use this method in scenario 5? — Vì sao chọn phương pháp trong tình huống 5?**

A. Ba mặt chẵn trong sáu mặt đồng khả năng — Ba mặt chẵn trong sáu mặt đồng khả năng

B. Số lượt thử tăng khiến ước lượng thường ổn định hơn — Số lượt thử tăng khiến ước lượng thường ổn định hơn

C. Đếm tỷ lệ mặt sấp khi có nhiều lần thử — Đếm tỷ lệ mặt sấp khi có nhiều lần thử

D. Đếm cặp kết quả thỏa tổng 9 trên 36 kết quả — Đếm cặp kết quả thỏa tổng 9 trên 36 kết quả


**Q14. Which input is from scenario 1? — Dữ liệu nào thuộc tình huống 1?**

A. The input is Xúc xắc công bằng có mặt 1..6 — Xúc xắc công bằng có mặt 1..6

B. Another input is 1000 lần tung giả lập — 1000 lần tung giả lập

C. Another input is Hai xúc xắc công bằng độc lập — Hai xúc xắc công bằng độc lập

D. Another input is 10000 lần với xác suất 0.2 — 10000 lần với xác suất 0.2


**Q15. Which input is from scenario 2? — Dữ liệu nào thuộc tình huống 2?**

A. Another input is Hai xúc xắc công bằng độc lập — Hai xúc xắc công bằng độc lập

B. Another input is 10000 lần với xác suất 0.2 — 10000 lần với xác suất 0.2

C. Another input is Đồng xu công bằng, 100 và 10000 lần — Đồng xu công bằng, 100 và 10000 lần

D. The input is 1000 lần tung giả lập — 1000 lần tung giả lập


**Q16. Which input is from scenario 3? — Dữ liệu nào thuộc tình huống 3?**

A. Another input is 10000 lần với xác suất 0.2 — 10000 lần với xác suất 0.2

B. Another input is Đồng xu công bằng, 100 và 10000 lần — Đồng xu công bằng, 100 và 10000 lần

C. The input is Hai xúc xắc công bằng độc lập — Hai xúc xắc công bằng độc lập

D. Another input is Xúc xắc công bằng có mặt 1..6 — Xúc xắc công bằng có mặt 1..6


**Q17. Which input is from scenario 4? — Dữ liệu nào thuộc tình huống 4?**

A. Another input is Đồng xu công bằng, 100 và 10000 lần — Đồng xu công bằng, 100 và 10000 lần

B. The input is 10000 lần với xác suất 0.2 — 10000 lần với xác suất 0.2

C. Another input is Xúc xắc công bằng có mặt 1..6 — Xúc xắc công bằng có mặt 1..6

D. Another input is 1000 lần tung giả lập — 1000 lần tung giả lập


**Q18. Which input is from scenario 5? — Dữ liệu nào thuộc tình huống 5?**

A. The input is Đồng xu công bằng, 100 và 10000 lần — Đồng xu công bằng, 100 và 10000 lần

B. Another input is Xúc xắc công bằng có mặt 1..6 — Xúc xắc công bằng có mặt 1..6

C. Another input is 1000 lần tung giả lập — 1000 lần tung giả lập

D. Another input is Hai xúc xắc công bằng độc lập — Hai xúc xắc công bằng độc lập


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
| Q1 | **B** | It means Thao tác có kết quả quan sát được | Thao tác có kết quả quan sát được |
| Q2 | **A** | It means Tập mọi kết quả khả dĩ | Tập mọi kết quả khả dĩ |
| Q3 | **D** | It means Nhóm kết quả được quan tâm | Nhóm kết quả được quan tâm |
| Q4 | **C** | It means Mức khả năng xảy ra một biến cố, từ 0 tới 1 | Mức khả năng xảy ra một biến cố, từ 0 tới 1 |
| Q5 | **B** | It calculates Xác suất cổ điển khi kết quả đồng khả năng | Xác suất cổ điển khi kết quả đồng khả năng |
| Q6 | **A** | It calculates Rút một phần tử ngẫu nhiên từ danh sách | Rút một phần tử ngẫu nhiên từ danh sách |
| Q7 | **D** | It calculates Tạo bộ sinh ngẫu nhiên tái lập | Tạo bộ sinh ngẫu nhiên tái lập |
| Q8 | **C** | It calculates Ước lượng tỷ lệ đúng trong mô phỏng | Ước lượng tỷ lệ đúng trong mô phỏng |
| Q9 | **B** | Ba mặt chẵn trong sáu mặt đồng khả năng | Ba mặt chẵn trong sáu mặt đồng khả năng |
| Q10 | **A** | Đếm tỷ lệ mặt sấp khi có nhiều lần thử | Đếm tỷ lệ mặt sấp khi có nhiều lần thử |
| Q11 | **D** | Đếm cặp kết quả thỏa tổng 9 trên 36 kết quả | Đếm cặp kết quả thỏa tổng 9 trên 36 kết quả |
| Q12 | **C** | Mô phỏng rút ngẫu nhiên với seed để lặp lại | Mô phỏng rút ngẫu nhiên với seed để lặp lại |
| Q13 | **B** | Số lượt thử tăng khiến ước lượng thường ổn định hơn | Số lượt thử tăng khiến ước lượng thường ổn định hơn |
| Q14 | **A** | The input is Xúc xắc công bằng có mặt 1..6 | Xúc xắc công bằng có mặt 1..6 |
| Q15 | **D** | The input is 1000 lần tung giả lập | 1000 lần tung giả lập |
| Q16 | **C** | The input is Hai xúc xắc công bằng độc lập | Hai xúc xắc công bằng độc lập |
| Q17 | **B** | The input is 10000 lần với xác suất 0.2 | 10000 lần với xác suất 0.2 |
| Q18 | **A** | The input is Đồng xu công bằng, 100 và 10000 lần | Đồng xu công bằng, 100 và 10000 lần |
| Q19 | **D** | Assumptions, units and sample size | Giả định, đơn vị và kích thước mẫu |
| Q20 | **C** | Checking assumptions and edge cases | Kiểm tra giả định và trường hợp biên |

## 8. Liên hệ bài tiếp theo

`Logic/Tập hợp → Xác suất → Bayes → Dự đoán bất định`.
