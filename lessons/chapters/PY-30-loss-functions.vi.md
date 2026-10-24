# PY-30 — Loss: MSE, MAE, Huber, cross-entropy và KL


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **MSE** — sai số bình phương trung bình; **MAE** — sai số tuyệt đối trung bình.

`Dự đoán → Sai số → Loss → Tối ưu hóa`

Kiến thức này liên quan đến việc biểu diễn, đánh giá hoặc tối ưu tính toán phục vụ AI. Đọc ví dụ trước khi liên hệ tới mô hình phức tạp.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| MSE | sai số bình phương trung bình | Trung bình bình phương hiệu dự đoán và giá trị thật |
| MAE | sai số tuyệt đối trung bình | Trung bình trị tuyệt đối sai số |
| Cross-entropy | entropy chéo | Phạt dự đoán xác suất sai nhãn mạnh hơn |
| KL divergence | độ lệch KL | Đo sai khác một chiều giữa hai phân phối xác suất |

## 3. Hàm và cách gọi bằng Python

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm / tham số | Giải thích |
|---|---|
| `np.mean((y-pred)**2)` | MSE nhạy với sai số lớn do bình phương |
| `np.mean(np.abs(y-pred))` | MAE ít khuếch đại outlier hơn MSE |
| `np.where(abs_err<=delta,... )` | Huber phối hợp bình phương và tuyến tính |
| `-np.sum(y*np.log(probs))` | Cross-entropy trên xác suất có clip để tránh log(0) |

## 4. Các khái niệm liên quan

### 4.1. MSE

**Từ vựng trong mục:** **MSE** — sai số bình phương trung bình.

Trung bình bình phương hiệu dự đoán và giá trị thật. Thử mã nhỏ để nhìn thấy giá trị trước khi làm bài toán phức tạp hơn.

```python
import numpy as np
print(np.mean((np.array([2,3])-np.array([1,4]))**2))
```

**Tự kiểm tra:** MSE là gì? **Đáp án:** Trung bình bình phương hiệu dự đoán và giá trị thật.

### 4.2. MAE

**Từ vựng trong mục:** **MAE** — sai số tuyệt đối trung bình.

Trung bình trị tuyệt đối sai số. Thử mã nhỏ để nhìn thấy giá trị trước khi làm bài toán phức tạp hơn.

```python
import numpy as np
print(np.mean(np.abs(np.array([2,3])-np.array([1,4]))))
```

**Tự kiểm tra:** MAE là gì? **Đáp án:** Trung bình trị tuyệt đối sai số.

### 4.3. Cross-entropy

**Từ vựng trong mục:** **Cross-entropy** — entropy chéo.

Phạt dự đoán xác suất sai nhãn mạnh hơn. Thử mã nhỏ để nhìn thấy giá trị trước khi làm bài toán phức tạp hơn.

```python
import math
print(-math.log(.8))
```

**Tự kiểm tra:** Cross-entropy là gì? **Đáp án:** Phạt dự đoán xác suất sai nhãn mạnh hơn.

### 4.4. KL divergence

**Từ vựng trong mục:** **KL divergence** — độ lệch KL.

Đo sai khác một chiều giữa hai phân phối xác suất. Thử mã nhỏ để nhìn thấy giá trị trước khi làm bài toán phức tạp hơn.

```python
import numpy as np
p=np.array([.5,.5]);q=np.array([.6,.4]);print(np.sum(p*np.log(p/q)))
```

**Tự kiểm tra:** KL divergence là gì? **Đáp án:** Đo sai khác một chiều giữa hai phân phối xác suất.

## 5. Năm tình huống ứng dụng thực tế

### Tình huống 1 — Đánh giá sai giá nhà

**Từ vựng trong mục:** **MSE** — sai số bình phương trung bình.

**Vấn đề:** Đánh giá sai giá nhà.

**Vì sao chọn phương án?** MSE phạt dự đoán sai lớn hơn nhiều; không dùng công thức hoặc mô hình phức tạp hơn khi các giả định chưa được kiểm tra.

**Dữ liệu:** Giá thật [100,200], dự đoán [110,170], triệu đồng. Các đơn vị và phép tính đã ghi trong đoạn mô tả; dữ liệu minh họa không dùng làm kết luận thực.

**Quy trình:** xác định giá trị/hàm → chọn phương pháp → lập trình → quan sát giá trị/shape → thử thêm đầu vào.

```python
import numpy as np
y=np.array([100,200]);pred=np.array([110,170])
print(np.mean((y-pred)**2))
```

**Đọc kết quả:** So sánh số in ra với công thức trong bài. Nếu dữ liệu thực có nhiễu, phải kiểm tra điều kiện và giới hạn trước khi ứng dụng vào AI.

### Tình huống 2 — Đánh giá dự báo có outlier

**Từ vựng trong mục:** **MAE** — sai số tuyệt đối trung bình.

**Vấn đề:** Đánh giá dự báo có outlier.

**Vì sao chọn phương án?** MAE giúp so mức sai số tuyệt đối dễ hiểu; không dùng công thức hoặc mô hình phức tạp hơn khi các giả định chưa được kiểm tra.

**Dữ liệu:** Doanh thu [10,20,30], dự đoán [9,19,50]. Các đơn vị và phép tính đã ghi trong đoạn mô tả; dữ liệu minh họa không dùng làm kết luận thực.

**Quy trình:** xác định giá trị/hàm → chọn phương pháp → lập trình → quan sát giá trị/shape → thử thêm đầu vào.

```python
import numpy as np
print(np.mean(np.abs(np.array([10,20,30])-np.array([9,19,50]))))
```

**Đọc kết quả:** So sánh số in ra với công thức trong bài. Nếu dữ liệu thực có nhiễu, phải kiểm tra điều kiện và giới hạn trước khi ứng dụng vào AI.

### Tình huống 3 — Tính Huber cho lỗi đo

**Từ vựng trong mục:** **Cross-entropy** — entropy chéo.

**Vấn đề:** Tính Huber cho lỗi đo.

**Vì sao chọn phương án?** Huber xử lý sai số nhỏ bằng bình phương, lớn bằng tuyến tính; không dùng công thức hoặc mô hình phức tạp hơn khi các giả định chưa được kiểm tra.

**Dữ liệu:** Sai số [-1,2,5], delta=1. Các đơn vị và phép tính đã ghi trong đoạn mô tả; dữ liệu minh họa không dùng làm kết luận thực.

**Quy trình:** xác định giá trị/hàm → chọn phương pháp → lập trình → quan sát giá trị/shape → thử thêm đầu vào.

```python
import numpy as np
e=np.array([-1.,2.,5.]);delta=1.
loss=np.where(np.abs(e)<=delta,.5*e**2,delta*(np.abs(e)-.5*delta))
print(loss.mean())
```

**Đọc kết quả:** So sánh số in ra với công thức trong bài. Nếu dữ liệu thực có nhiễu, phải kiểm tra điều kiện và giới hạn trước khi ứng dụng vào AI.

### Tình huống 4 — Phạt nhãn dự đoán sai

**Từ vựng trong mục:** **KL divergence** — độ lệch KL.

**Vấn đề:** Phạt nhãn dự đoán sai.

**Vì sao chọn phương án?** Cross-entropy dùng xác suất của đúng nhãn; không dùng công thức hoặc mô hình phức tạp hơn khi các giả định chưa được kiểm tra.

**Dữ liệu:** Xác suất đúng nhãn 0.8. Các đơn vị và phép tính đã ghi trong đoạn mô tả; dữ liệu minh họa không dùng làm kết luận thực.

**Quy trình:** xác định giá trị/hàm → chọn phương pháp → lập trình → quan sát giá trị/shape → thử thêm đầu vào.

```python
import math
prob_true=.8
print(-math.log(prob_true))
```

**Đọc kết quả:** So sánh số in ra với công thức trong bài. Nếu dữ liệu thực có nhiễu, phải kiểm tra điều kiện và giới hạn trước khi ứng dụng vào AI.

### Tình huống 5 — So phân phối dự báo

**Từ vựng trong mục:** **MSE** — sai số bình phương trung bình.

**Vấn đề:** So phân phối dự báo.

**Vì sao chọn phương án?** KL khác 0 khi phân phối thay đổi, lưu ý bất đối xứng; không dùng công thức hoặc mô hình phức tạp hơn khi các giả định chưa được kiểm tra.

**Dữ liệu:** p=[.5,.5], q=[.6,.4]. Các đơn vị và phép tính đã ghi trong đoạn mô tả; dữ liệu minh họa không dùng làm kết luận thực.

**Quy trình:** xác định giá trị/hàm → chọn phương pháp → lập trình → quan sát giá trị/shape → thử thêm đầu vào.

```python
import numpy as np
p=np.array([.5,.5]);q=np.array([.6,.4])
print(np.sum(p*np.log(p/q)))
```

**Đọc kết quả:** So sánh số in ra với công thức trong bài. Nếu dữ liệu thực có nhiễu, phải kiểm tra điều kiện và giới hạn trước khi ứng dụng vào AI.

## 6. Các lỗi dễ gặp

Hàm kích hoạt và loss không tự thay thế quy trình huấn luyện; đạo hàm theo một biến không giống gradient nhiều biến. Tránh tràn số mũ, log(0), chia cho 0; luôn để ý learning rate và đơn vị.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.


**Q1. What does MSE mean? — Thuật ngữ MSE có nghĩa gì?**

A. It instead means Trung bình trị tuyệt đối sai số — Trung bình trị tuyệt đối sai số

B. It means Trung bình bình phương hiệu dự đoán và giá trị thật — Trung bình bình phương hiệu dự đoán và giá trị thật

C. It instead means Phạt dự đoán xác suất sai nhãn mạnh hơn — Phạt dự đoán xác suất sai nhãn mạnh hơn

D. It instead means Đo sai khác một chiều giữa hai phân phối xác suất — Đo sai khác một chiều giữa hai phân phối xác suất


**Q2. What does MAE mean? — Thuật ngữ MAE có nghĩa gì?**

A. It means Trung bình trị tuyệt đối sai số — Trung bình trị tuyệt đối sai số

B. It instead means Phạt dự đoán xác suất sai nhãn mạnh hơn — Phạt dự đoán xác suất sai nhãn mạnh hơn

C. It instead means Đo sai khác một chiều giữa hai phân phối xác suất — Đo sai khác một chiều giữa hai phân phối xác suất

D. It instead means Trung bình bình phương hiệu dự đoán và giá trị thật — Trung bình bình phương hiệu dự đoán và giá trị thật


**Q3. What does Cross-entropy mean? — Thuật ngữ Cross-entropy có nghĩa gì?**

A. It instead means Đo sai khác một chiều giữa hai phân phối xác suất — Đo sai khác một chiều giữa hai phân phối xác suất

B. It instead means Trung bình bình phương hiệu dự đoán và giá trị thật — Trung bình bình phương hiệu dự đoán và giá trị thật

C. It instead means Trung bình trị tuyệt đối sai số — Trung bình trị tuyệt đối sai số

D. It means Phạt dự đoán xác suất sai nhãn mạnh hơn — Phạt dự đoán xác suất sai nhãn mạnh hơn


**Q4. What does KL divergence mean? — Thuật ngữ KL divergence có nghĩa gì?**

A. It instead means Trung bình bình phương hiệu dự đoán và giá trị thật — Trung bình bình phương hiệu dự đoán và giá trị thật

B. It instead means Trung bình trị tuyệt đối sai số — Trung bình trị tuyệt đối sai số

C. It means Đo sai khác một chiều giữa hai phân phối xác suất — Đo sai khác một chiều giữa hai phân phối xác suất

D. It instead means Phạt dự đoán xác suất sai nhãn mạnh hơn — Phạt dự đoán xác suất sai nhãn mạnh hơn


**Q5. What does np.mean((y-pred)**2) do? — Mục đích của np.mean((y-pred)**2) là gì?**

A. Another operation does MAE ít khuếch đại outlier hơn MSE — MAE ít khuếch đại outlier hơn MSE

B. It is used to MSE nhạy với sai số lớn do bình phương — MSE nhạy với sai số lớn do bình phương

C. Another operation does Huber phối hợp bình phương và tuyến tính — Huber phối hợp bình phương và tuyến tính

D. Another operation does Cross-entropy trên xác suất có clip để tránh log(0) — Cross-entropy trên xác suất có clip để tránh log(0)


**Q6. What does np.mean(np.abs(y-pred)) do? — Mục đích của np.mean(np.abs(y-pred)) là gì?**

A. It is used to MAE ít khuếch đại outlier hơn MSE — MAE ít khuếch đại outlier hơn MSE

B. Another operation does Huber phối hợp bình phương và tuyến tính — Huber phối hợp bình phương và tuyến tính

C. Another operation does Cross-entropy trên xác suất có clip để tránh log(0) — Cross-entropy trên xác suất có clip để tránh log(0)

D. Another operation does MSE nhạy với sai số lớn do bình phương — MSE nhạy với sai số lớn do bình phương


**Q7. What does np.where(abs_err<=delta,... ) do? — Mục đích của np.where(abs_err<=delta,... ) là gì?**

A. Another operation does Cross-entropy trên xác suất có clip để tránh log(0) — Cross-entropy trên xác suất có clip để tránh log(0)

B. Another operation does MSE nhạy với sai số lớn do bình phương — MSE nhạy với sai số lớn do bình phương

C. Another operation does MAE ít khuếch đại outlier hơn MSE — MAE ít khuếch đại outlier hơn MSE

D. It is used to Huber phối hợp bình phương và tuyến tính — Huber phối hợp bình phương và tuyến tính


**Q8. What does -np.sum(y*np.log(probs)) do? — Mục đích của -np.sum(y*np.log(probs)) là gì?**

A. Another operation does MSE nhạy với sai số lớn do bình phương — MSE nhạy với sai số lớn do bình phương

B. Another operation does MAE ít khuếch đại outlier hơn MSE — MAE ít khuếch đại outlier hơn MSE

C. It is used to Cross-entropy trên xác suất có clip để tránh log(0) — Cross-entropy trên xác suất có clip để tránh log(0)

D. Another operation does Huber phối hợp bình phương và tuyến tính — Huber phối hợp bình phương và tuyến tính


**Q9. Why use this method in scenario 1? — Vì sao chọn cách giải ở tình huống 1?**

A. MAE giúp so mức sai số tuyệt đối dễ hiểu — MAE giúp so mức sai số tuyệt đối dễ hiểu

B. MSE phạt dự đoán sai lớn hơn nhiều — MSE phạt dự đoán sai lớn hơn nhiều

C. Huber xử lý sai số nhỏ bằng bình phương, lớn bằng tuyến tính — Huber xử lý sai số nhỏ bằng bình phương, lớn bằng tuyến tính

D. Cross-entropy dùng xác suất của đúng nhãn — Cross-entropy dùng xác suất của đúng nhãn


**Q10. Why use this method in scenario 2? — Vì sao chọn cách giải ở tình huống 2?**

A. MAE giúp so mức sai số tuyệt đối dễ hiểu — MAE giúp so mức sai số tuyệt đối dễ hiểu

B. Huber xử lý sai số nhỏ bằng bình phương, lớn bằng tuyến tính — Huber xử lý sai số nhỏ bằng bình phương, lớn bằng tuyến tính

C. Cross-entropy dùng xác suất của đúng nhãn — Cross-entropy dùng xác suất của đúng nhãn

D. KL khác 0 khi phân phối thay đổi, lưu ý bất đối xứng — KL khác 0 khi phân phối thay đổi, lưu ý bất đối xứng


**Q11. Why use this method in scenario 3? — Vì sao chọn cách giải ở tình huống 3?**

A. Cross-entropy dùng xác suất của đúng nhãn — Cross-entropy dùng xác suất của đúng nhãn

B. KL khác 0 khi phân phối thay đổi, lưu ý bất đối xứng — KL khác 0 khi phân phối thay đổi, lưu ý bất đối xứng

C. MSE phạt dự đoán sai lớn hơn nhiều — MSE phạt dự đoán sai lớn hơn nhiều

D. Huber xử lý sai số nhỏ bằng bình phương, lớn bằng tuyến tính — Huber xử lý sai số nhỏ bằng bình phương, lớn bằng tuyến tính


**Q12. Why use this method in scenario 4? — Vì sao chọn cách giải ở tình huống 4?**

A. KL khác 0 khi phân phối thay đổi, lưu ý bất đối xứng — KL khác 0 khi phân phối thay đổi, lưu ý bất đối xứng

B. MSE phạt dự đoán sai lớn hơn nhiều — MSE phạt dự đoán sai lớn hơn nhiều

C. Cross-entropy dùng xác suất của đúng nhãn — Cross-entropy dùng xác suất của đúng nhãn

D. MAE giúp so mức sai số tuyệt đối dễ hiểu — MAE giúp so mức sai số tuyệt đối dễ hiểu


**Q13. Why use this method in scenario 5? — Vì sao chọn cách giải ở tình huống 5?**

A. MSE phạt dự đoán sai lớn hơn nhiều — MSE phạt dự đoán sai lớn hơn nhiều

B. KL khác 0 khi phân phối thay đổi, lưu ý bất đối xứng — KL khác 0 khi phân phối thay đổi, lưu ý bất đối xứng

C. MAE giúp so mức sai số tuyệt đối dễ hiểu — MAE giúp so mức sai số tuyệt đối dễ hiểu

D. Huber xử lý sai số nhỏ bằng bình phương, lớn bằng tuyến tính — Huber xử lý sai số nhỏ bằng bình phương, lớn bằng tuyến tính


**Q14. Which input belongs to scenario 1? — Tình huống 1 sử dụng dữ liệu gì?**

A. The input is Giá thật [100,200], dự đoán [110,170], triệu đồng — Giá thật [100,200], dự đoán [110,170], triệu đồng

B. Another input is Doanh thu [10,20,30], dự đoán [9,19,50] — Doanh thu [10,20,30], dự đoán [9,19,50]

C. Another input is Sai số [-1,2,5], delta=1 — Sai số [-1,2,5], delta=1

D. Another input is Xác suất đúng nhãn 0.8 — Xác suất đúng nhãn 0.8


**Q15. Which input belongs to scenario 2? — Tình huống 2 sử dụng dữ liệu gì?**

A. Another input is Sai số [-1,2,5], delta=1 — Sai số [-1,2,5], delta=1

B. Another input is Xác suất đúng nhãn 0.8 — Xác suất đúng nhãn 0.8

C. Another input is p=[.5,.5], q=[.6,.4] — p=[.5,.5], q=[.6,.4]

D. The input is Doanh thu [10,20,30], dự đoán [9,19,50] — Doanh thu [10,20,30], dự đoán [9,19,50]


**Q16. Which input belongs to scenario 3? — Tình huống 3 sử dụng dữ liệu gì?**

A. Another input is Xác suất đúng nhãn 0.8 — Xác suất đúng nhãn 0.8

B. Another input is p=[.5,.5], q=[.6,.4] — p=[.5,.5], q=[.6,.4]

C. The input is Sai số [-1,2,5], delta=1 — Sai số [-1,2,5], delta=1

D. Another input is Giá thật [100,200], dự đoán [110,170], triệu đồng — Giá thật [100,200], dự đoán [110,170], triệu đồng


**Q17. Which input belongs to scenario 4? — Tình huống 4 sử dụng dữ liệu gì?**

A. Another input is p=[.5,.5], q=[.6,.4] — p=[.5,.5], q=[.6,.4]

B. The input is Xác suất đúng nhãn 0.8 — Xác suất đúng nhãn 0.8

C. Another input is Giá thật [100,200], dự đoán [110,170], triệu đồng — Giá thật [100,200], dự đoán [110,170], triệu đồng

D. Another input is Doanh thu [10,20,30], dự đoán [9,19,50] — Doanh thu [10,20,30], dự đoán [9,19,50]


**Q18. Which input belongs to scenario 5? — Tình huống 5 sử dụng dữ liệu gì?**

A. The input is p=[.5,.5], q=[.6,.4] — p=[.5,.5], q=[.6,.4]

B. Another input is Giá thật [100,200], dự đoán [110,170], triệu đồng — Giá thật [100,200], dự đoán [110,170], triệu đồng

C. Another input is Doanh thu [10,20,30], dự đoán [9,19,50] — Doanh thu [10,20,30], dự đoán [9,19,50]

D. Another input is Sai số [-1,2,5], delta=1 — Sai số [-1,2,5], delta=1


**Q19. What must be known before computing? — Trước khi tính phải biết gì?**

A. Only editor color — Chỉ màu giao diện

B. Only filename — Chỉ tên file

C. Only number of comments — Chỉ số lượng comment

D. Input meaning and units — Ý nghĩa và đơn vị đầu vào


**Q20. What makes a calculation trustworthy? — Điều gì giúp phép tính đáng tin?**

A. Assume models never fail — Cho rằng mô hình không bao giờ sai

B. Delete validation — Xóa bước xác minh

C. Verify results and edge cases — Kiểm tra kết quả và trường hợp biên

D. Guess data units — Đoán đơn vị dữ liệu

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | It means Trung bình bình phương hiệu dự đoán và giá trị thật | Trung bình bình phương hiệu dự đoán và giá trị thật |
| Q2 | **A** | It means Trung bình trị tuyệt đối sai số | Trung bình trị tuyệt đối sai số |
| Q3 | **D** | It means Phạt dự đoán xác suất sai nhãn mạnh hơn | Phạt dự đoán xác suất sai nhãn mạnh hơn |
| Q4 | **C** | It means Đo sai khác một chiều giữa hai phân phối xác suất | Đo sai khác một chiều giữa hai phân phối xác suất |
| Q5 | **B** | It is used to MSE nhạy với sai số lớn do bình phương | MSE nhạy với sai số lớn do bình phương |
| Q6 | **A** | It is used to MAE ít khuếch đại outlier hơn MSE | MAE ít khuếch đại outlier hơn MSE |
| Q7 | **D** | It is used to Huber phối hợp bình phương và tuyến tính | Huber phối hợp bình phương và tuyến tính |
| Q8 | **C** | It is used to Cross-entropy trên xác suất có clip để tránh log(0) | Cross-entropy trên xác suất có clip để tránh log(0) |
| Q9 | **B** | MSE phạt dự đoán sai lớn hơn nhiều | MSE phạt dự đoán sai lớn hơn nhiều |
| Q10 | **A** | MAE giúp so mức sai số tuyệt đối dễ hiểu | MAE giúp so mức sai số tuyệt đối dễ hiểu |
| Q11 | **D** | Huber xử lý sai số nhỏ bằng bình phương, lớn bằng tuyến tính | Huber xử lý sai số nhỏ bằng bình phương, lớn bằng tuyến tính |
| Q12 | **C** | Cross-entropy dùng xác suất của đúng nhãn | Cross-entropy dùng xác suất của đúng nhãn |
| Q13 | **B** | KL khác 0 khi phân phối thay đổi, lưu ý bất đối xứng | KL khác 0 khi phân phối thay đổi, lưu ý bất đối xứng |
| Q14 | **A** | The input is Giá thật [100,200], dự đoán [110,170], triệu đồng | Giá thật [100,200], dự đoán [110,170], triệu đồng |
| Q15 | **D** | The input is Doanh thu [10,20,30], dự đoán [9,19,50] | Doanh thu [10,20,30], dự đoán [9,19,50] |
| Q16 | **C** | The input is Sai số [-1,2,5], delta=1 | Sai số [-1,2,5], delta=1 |
| Q17 | **B** | The input is Xác suất đúng nhãn 0.8 | Xác suất đúng nhãn 0.8 |
| Q18 | **A** | The input is p=[.5,.5], q=[.6,.4] | p=[.5,.5], q=[.6,.4] |
| Q19 | **D** | Input meaning and units | Ý nghĩa và đơn vị đầu vào |
| Q20 | **C** | Verify results and edge cases | Kiểm tra kết quả và trường hợp biên |

## 8. Bài tiếp theo

`Dự đoán → Sai số → Loss → Tối ưu hóa`.
