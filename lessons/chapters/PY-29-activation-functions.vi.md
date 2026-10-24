# PY-29 — Activation: ReLU, sigmoid, tanh, softmax

## 1. Vị trí trong chuỗi kiến thức

`Hàm số → Activation → Neural Network → Classification`

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| ReLU | hàm chỉnh lưu | Giữ số dương, số âm thành 0 |
| Sigmoid | hàm sigmoid | Ánh xạ số thực về khoảng (0,1) |
| Tanh | hàm tanh | Ánh xạ số thực về (-1,1) |
| Softmax | hàm softmax | Biến logits thành phân phối xác suất tổng bằng 1 |

## 3. Hàm và cách gọi bằng Python

| Hàm / tham số | Giải thích |
|---|---|
| `np.maximum(0,x)` | ReLU, tạo phi tuyến cho mạng |
| `1/(1+np.exp(-x))` | Sigmoid, cẩn thận số quá lớn |
| `np.tanh(x)` | Kích hoạt có đầu ra âm/dương |
| `np.exp(z-max(z))/sum(... )` | Softmax ổn định hơn tính exp(z) trực tiếp |

## 4. Các khái niệm liên quan

### 4.1. ReLU

Giữ số dương, số âm thành 0.

```python
import numpy as np
print(np.maximum(0,[-2,3]))
```

### 4.2. Sigmoid

Ánh xạ số thực về khoảng (0,1).

```python
import numpy as np
x=np.array([0.]);print(1/(1+np.exp(-x)))
```

### 4.3. Tanh

Ánh xạ số thực về (-1,1).

```python
import numpy as np
print(np.tanh([0.,1.]))
```

### 4.4. Softmax

Biến logits thành phân phối xác suất tổng bằng 1.

```python
import numpy as np
z=np.array([1.,2.]);e=np.exp(z-z.max());print(e/e.sum())
```

## 5. Năm tình huống ứng dụng thực tế

### Tình huống 1 — Kích hoạt tín hiệu nhiễu âm

**Vấn đề:** Kích hoạt tín hiệu nhiễu âm.

**Vì sao chọn phương án?** ReLU chặn giá trị âm khi đó là chính sách kích hoạt

**Dữ liệu:** 4 tín hiệu giả lập [-2,0,3,5].

```python
import numpy as np
x=np.array([-2.,0.,3.,5.])
print(np.maximum(0,x))
```

### Tình huống 2 — Đổi điểm thô sang tỷ lệ

**Vấn đề:** Đổi điểm thô sang tỷ lệ.

**Vì sao chọn phương án?** Sigmoid cho giá trị nằm giữa 0 và 1, không tự hiệu chuẩn xác suất

**Dữ liệu:** Điểm số [-1,0,1].

```python
import numpy as np
x=np.array([-1.,0.,1.])
print(1/(1+np.exp(-x)))
```

### Tình huống 3 — Kích hoạt đối xứng

**Vấn đề:** Kích hoạt đối xứng.

**Vì sao chọn phương án?** tanh cho dấu âm/dương quanh 0

**Dữ liệu:** Tín hiệu [-1,0,1].

```python
import numpy as np
print(np.tanh([-1,0,1]))
```

### Tình huống 4 — Chuẩn hóa điểm phân loại

**Vấn đề:** Chuẩn hóa điểm phân loại.

**Vì sao chọn phương án?** Softmax tạo tổng xác suất bằng 1 từ logits

**Dữ liệu:** Ba logit [2,1,0.1].

```python
import numpy as np
z=np.array([2.,1.,.1]);e=np.exp(z-z.max())
p=e/e.sum();print(p,p.sum())
```

### Tình huống 5 — So mô hình tuyến tính và ReLU

**Vấn đề:** So mô hình tuyến tính và ReLU.

**Vì sao chọn phương án?** Một hoặc nhiều lớp ReLU cho phép dạng hàm gấp khúc

**Dữ liệu:** Dữ liệu x từ -2 tới 2.

```python
import numpy as np
x=np.linspace(-2,2,5)
y=np.maximum(0,x-1)+np.maximum(0,-x-1)
print(y)
```

## 6. Các lỗi dễ gặp

Hàm kích hoạt và loss không tự thay thế quy trình huấn luyện; đạo hàm theo một biến không giống gradient nhiều biến. Tránh tràn số mũ, log(0), chia cho 0; luôn để ý learning rate và đơn vị.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ


**Q1. What does ReLU mean? — Thuật ngữ ReLU có nghĩa gì?**

A. It instead means Ánh xạ số thực về khoảng (0,1) — Ánh xạ số thực về khoảng (0,1)

B. It means Giữ số dương, số âm thành 0 — Giữ số dương, số âm thành 0

C. It instead means Ánh xạ số thực về (-1,1) — Ánh xạ số thực về (-1,1)

D. It instead means Biến logits thành phân phối xác suất tổng bằng 1 — Biến logits thành phân phối xác suất tổng bằng 1


**Q2. What does Sigmoid mean? — Thuật ngữ Sigmoid có nghĩa gì?**

A. It means Ánh xạ số thực về khoảng (0,1) — Ánh xạ số thực về khoảng (0,1)

B. It instead means Ánh xạ số thực về (-1,1) — Ánh xạ số thực về (-1,1)

C. It instead means Biến logits thành phân phối xác suất tổng bằng 1 — Biến logits thành phân phối xác suất tổng bằng 1

D. It instead means Giữ số dương, số âm thành 0 — Giữ số dương, số âm thành 0


**Q3. What does Tanh mean? — Thuật ngữ Tanh có nghĩa gì?**

A. It instead means Biến logits thành phân phối xác suất tổng bằng 1 — Biến logits thành phân phối xác suất tổng bằng 1

B. It instead means Giữ số dương, số âm thành 0 — Giữ số dương, số âm thành 0

C. It instead means Ánh xạ số thực về khoảng (0,1) — Ánh xạ số thực về khoảng (0,1)

D. It means Ánh xạ số thực về (-1,1) — Ánh xạ số thực về (-1,1)


**Q4. What does Softmax mean? — Thuật ngữ Softmax có nghĩa gì?**

A. It instead means Giữ số dương, số âm thành 0 — Giữ số dương, số âm thành 0

B. It instead means Ánh xạ số thực về khoảng (0,1) — Ánh xạ số thực về khoảng (0,1)

C. It means Biến logits thành phân phối xác suất tổng bằng 1 — Biến logits thành phân phối xác suất tổng bằng 1

D. It instead means Ánh xạ số thực về (-1,1) — Ánh xạ số thực về (-1,1)


**Q5. What does np.maximum(0,x) do? — Mục đích của np.maximum(0,x) là gì?**

A. Another operation does Sigmoid, cẩn thận số quá lớn — Sigmoid, cẩn thận số quá lớn

B. It is used to ReLU, tạo phi tuyến cho mạng — ReLU, tạo phi tuyến cho mạng

C. Another operation does Kích hoạt có đầu ra âm/dương — Kích hoạt có đầu ra âm/dương

D. Another operation does Softmax ổn định hơn tính exp(z) trực tiếp — Softmax ổn định hơn tính exp(z) trực tiếp


**Q6. What does 1/(1+np.exp(-x)) do? — Mục đích của 1/(1+np.exp(-x)) là gì?**

A. It is used to Sigmoid, cẩn thận số quá lớn — Sigmoid, cẩn thận số quá lớn

B. Another operation does Kích hoạt có đầu ra âm/dương — Kích hoạt có đầu ra âm/dương

C. Another operation does Softmax ổn định hơn tính exp(z) trực tiếp — Softmax ổn định hơn tính exp(z) trực tiếp

D. Another operation does ReLU, tạo phi tuyến cho mạng — ReLU, tạo phi tuyến cho mạng


**Q7. What does np.tanh(x) do? — Mục đích của np.tanh(x) là gì?**

A. Another operation does Softmax ổn định hơn tính exp(z) trực tiếp — Softmax ổn định hơn tính exp(z) trực tiếp

B. Another operation does ReLU, tạo phi tuyến cho mạng — ReLU, tạo phi tuyến cho mạng

C. Another operation does Sigmoid, cẩn thận số quá lớn — Sigmoid, cẩn thận số quá lớn

D. It is used to Kích hoạt có đầu ra âm/dương — Kích hoạt có đầu ra âm/dương


**Q8. What does np.exp(z-max(z))/sum(... ) do? — Mục đích của np.exp(z-max(z))/sum(... ) là gì?**

A. Another operation does ReLU, tạo phi tuyến cho mạng — ReLU, tạo phi tuyến cho mạng

B. Another operation does Sigmoid, cẩn thận số quá lớn — Sigmoid, cẩn thận số quá lớn

C. It is used to Softmax ổn định hơn tính exp(z) trực tiếp — Softmax ổn định hơn tính exp(z) trực tiếp

D. Another operation does Kích hoạt có đầu ra âm/dương — Kích hoạt có đầu ra âm/dương


**Q9. Why use this method in scenario 1? — Vì sao chọn cách giải ở tình huống 1?**

A. Sigmoid cho giá trị nằm giữa 0 và 1, không tự hiệu chuẩn xác suất — Sigmoid cho giá trị nằm giữa 0 và 1, không tự hiệu chuẩn xác suất

B. ReLU chặn giá trị âm khi đó là chính sách kích hoạt — ReLU chặn giá trị âm khi đó là chính sách kích hoạt

C. tanh cho dấu âm/dương quanh 0 — tanh cho dấu âm/dương quanh 0

D. Softmax tạo tổng xác suất bằng 1 từ logits — Softmax tạo tổng xác suất bằng 1 từ logits


**Q10. Why use this method in scenario 2? — Vì sao chọn cách giải ở tình huống 2?**

A. Sigmoid cho giá trị nằm giữa 0 và 1, không tự hiệu chuẩn xác suất — Sigmoid cho giá trị nằm giữa 0 và 1, không tự hiệu chuẩn xác suất

B. tanh cho dấu âm/dương quanh 0 — tanh cho dấu âm/dương quanh 0

C. Softmax tạo tổng xác suất bằng 1 từ logits — Softmax tạo tổng xác suất bằng 1 từ logits

D. Một hoặc nhiều lớp ReLU cho phép dạng hàm gấp khúc — Một hoặc nhiều lớp ReLU cho phép dạng hàm gấp khúc


**Q11. Why use this method in scenario 3? — Vì sao chọn cách giải ở tình huống 3?**

A. Softmax tạo tổng xác suất bằng 1 từ logits — Softmax tạo tổng xác suất bằng 1 từ logits

B. Một hoặc nhiều lớp ReLU cho phép dạng hàm gấp khúc — Một hoặc nhiều lớp ReLU cho phép dạng hàm gấp khúc

C. ReLU chặn giá trị âm khi đó là chính sách kích hoạt — ReLU chặn giá trị âm khi đó là chính sách kích hoạt

D. tanh cho dấu âm/dương quanh 0 — tanh cho dấu âm/dương quanh 0


**Q12. Why use this method in scenario 4? — Vì sao chọn cách giải ở tình huống 4?**

A. Một hoặc nhiều lớp ReLU cho phép dạng hàm gấp khúc — Một hoặc nhiều lớp ReLU cho phép dạng hàm gấp khúc

B. ReLU chặn giá trị âm khi đó là chính sách kích hoạt — ReLU chặn giá trị âm khi đó là chính sách kích hoạt

C. Softmax tạo tổng xác suất bằng 1 từ logits — Softmax tạo tổng xác suất bằng 1 từ logits

D. Sigmoid cho giá trị nằm giữa 0 và 1, không tự hiệu chuẩn xác suất — Sigmoid cho giá trị nằm giữa 0 và 1, không tự hiệu chuẩn xác suất


**Q13. Why use this method in scenario 5? — Vì sao chọn cách giải ở tình huống 5?**

A. ReLU chặn giá trị âm khi đó là chính sách kích hoạt — ReLU chặn giá trị âm khi đó là chính sách kích hoạt

B. Một hoặc nhiều lớp ReLU cho phép dạng hàm gấp khúc — Một hoặc nhiều lớp ReLU cho phép dạng hàm gấp khúc

C. Sigmoid cho giá trị nằm giữa 0 và 1, không tự hiệu chuẩn xác suất — Sigmoid cho giá trị nằm giữa 0 và 1, không tự hiệu chuẩn xác suất

D. tanh cho dấu âm/dương quanh 0 — tanh cho dấu âm/dương quanh 0


**Q14. Which input belongs to scenario 1? — Tình huống 1 sử dụng dữ liệu gì?**

A. The input is 4 tín hiệu giả lập [-2,0,3,5] — 4 tín hiệu giả lập [-2,0,3,5]

B. Another input is Điểm số [-1,0,1] — Điểm số [-1,0,1]

C. Another input is Tín hiệu [-1,0,1] — Tín hiệu [-1,0,1]

D. Another input is Ba logit [2,1,0.1] — Ba logit [2,1,0.1]


**Q15. Which input belongs to scenario 2? — Tình huống 2 sử dụng dữ liệu gì?**

A. Another input is Tín hiệu [-1,0,1] — Tín hiệu [-1,0,1]

B. Another input is Ba logit [2,1,0.1] — Ba logit [2,1,0.1]

C. Another input is Dữ liệu x từ -2 tới 2 — Dữ liệu x từ -2 tới 2

D. The input is Điểm số [-1,0,1] — Điểm số [-1,0,1]


**Q16. Which input belongs to scenario 3? — Tình huống 3 sử dụng dữ liệu gì?**

A. Another input is Ba logit [2,1,0.1] — Ba logit [2,1,0.1]

B. Another input is Dữ liệu x từ -2 tới 2 — Dữ liệu x từ -2 tới 2

C. The input is Tín hiệu [-1,0,1] — Tín hiệu [-1,0,1]

D. Another input is 4 tín hiệu giả lập [-2,0,3,5] — 4 tín hiệu giả lập [-2,0,3,5]


**Q17. Which input belongs to scenario 4? — Tình huống 4 sử dụng dữ liệu gì?**

A. Another input is Dữ liệu x từ -2 tới 2 — Dữ liệu x từ -2 tới 2

B. The input is Ba logit [2,1,0.1] — Ba logit [2,1,0.1]

C. Another input is 4 tín hiệu giả lập [-2,0,3,5] — 4 tín hiệu giả lập [-2,0,3,5]

D. Another input is Điểm số [-1,0,1] — Điểm số [-1,0,1]


**Q18. Which input belongs to scenario 5? — Tình huống 5 sử dụng dữ liệu gì?**

A. The input is Dữ liệu x từ -2 tới 2 — Dữ liệu x từ -2 tới 2

B. Another input is 4 tín hiệu giả lập [-2,0,3,5] — 4 tín hiệu giả lập [-2,0,3,5]

C. Another input is Điểm số [-1,0,1] — Điểm số [-1,0,1]

D. Another input is Tín hiệu [-1,0,1] — Tín hiệu [-1,0,1]


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
| Q1 | **B** | It means Giữ số dương, số âm thành 0 | Giữ số dương, số âm thành 0 |
| Q2 | **A** | It means Ánh xạ số thực về khoảng (0,1) | Ánh xạ số thực về khoảng (0,1) |
| Q3 | **D** | It means Ánh xạ số thực về (-1,1) | Ánh xạ số thực về (-1,1) |
| Q4 | **C** | It means Biến logits thành phân phối xác suất tổng bằng 1 | Biến logits thành phân phối xác suất tổng bằng 1 |
| Q5 | **B** | It is used to ReLU, tạo phi tuyến cho mạng | ReLU, tạo phi tuyến cho mạng |
| Q6 | **A** | It is used to Sigmoid, cẩn thận số quá lớn | Sigmoid, cẩn thận số quá lớn |
| Q7 | **D** | It is used to Kích hoạt có đầu ra âm/dương | Kích hoạt có đầu ra âm/dương |
| Q8 | **C** | It is used to Softmax ổn định hơn tính exp(z) trực tiếp | Softmax ổn định hơn tính exp(z) trực tiếp |
| Q9 | **B** | ReLU chặn giá trị âm khi đó là chính sách kích hoạt | ReLU chặn giá trị âm khi đó là chính sách kích hoạt |
| Q10 | **A** | Sigmoid cho giá trị nằm giữa 0 và 1, không tự hiệu chuẩn xác suất | Sigmoid cho giá trị nằm giữa 0 và 1, không tự hiệu chuẩn xác suất |
| Q11 | **D** | tanh cho dấu âm/dương quanh 0 | tanh cho dấu âm/dương quanh 0 |
| Q12 | **C** | Softmax tạo tổng xác suất bằng 1 từ logits | Softmax tạo tổng xác suất bằng 1 từ logits |
| Q13 | **B** | Một hoặc nhiều lớp ReLU cho phép dạng hàm gấp khúc | Một hoặc nhiều lớp ReLU cho phép dạng hàm gấp khúc |
| Q14 | **A** | The input is 4 tín hiệu giả lập [-2,0,3,5] | 4 tín hiệu giả lập [-2,0,3,5] |
| Q15 | **D** | The input is Điểm số [-1,0,1] | Điểm số [-1,0,1] |
| Q16 | **C** | The input is Tín hiệu [-1,0,1] | Tín hiệu [-1,0,1] |
| Q17 | **B** | The input is Ba logit [2,1,0.1] | Ba logit [2,1,0.1] |
| Q18 | **A** | The input is Dữ liệu x từ -2 tới 2 | Dữ liệu x từ -2 tới 2 |
| Q19 | **D** | Input meaning and units | Ý nghĩa và đơn vị đầu vào |
| Q20 | **C** | Verify results and edge cases | Kiểm tra kết quả và trường hợp biên |
