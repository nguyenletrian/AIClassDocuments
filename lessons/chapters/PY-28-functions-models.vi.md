# PY-28 — Hàm tuyến tính, bậc hai, đa thức và hàm mũ

## 1. Vị trí trong chuỗi kiến thức

`Hàm Python → Hàm toán theo dữ liệu → Loss → Gradient`

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| Linear function | hàm tuyến tính | Đường thẳng có tốc độ thay đổi hằng số |
| Quadratic | hàm bậc hai | Hàm chứa x², đồ thị là parabol khi hệ số bậc hai khác 0 |
| Polynomial | hàm đa thức | Tổng các lũy thừa nguyên không âm của x |
| Exponential | hàm mũ | Biến nằm trong số mũ, thường mô tả tăng/giảm theo tỷ lệ |

## 3. Hàm và cách gọi bằng Python

| Hàm / tham số | Giải thích |
|---|---|
| `y=m*x+b` | Quan hệ tuyến tính, m là độ dốc, b là hệ số chặn |
| `y=a*x**2+b*x+c` | Quan hệ bậc hai, dùng khi đường cong |
| `np.polyval(coefficients,x)` | Đánh giá đa thức theo hệ số cao xuống thấp |
| `np.exp(x)/base**x` | Hàm mũ; cẩn thận overflow và miền thực |

## 4. Các khái niệm liên quan

### 4.1. Linear function

Đường thẳng có tốc độ thay đổi hằng số.

```python
def f(x):return 2*x+5
print(f(3))
```

### 4.2. Quadratic

Hàm chứa x², đồ thị là parabol khi hệ số bậc hai khác 0.

```python
print(2**2-3*2+1)
```

### 4.3. Polynomial

Tổng các lũy thừa nguyên không âm của x.

```python
print(3**3-2*3**2+3)
```

### 4.4. Exponential

Biến nằm trong số mũ, thường mô tả tăng/giảm theo tỷ lệ.

```python
print(2**4)
```

## 5. Năm tình huống ứng dụng thực tế

### Tình huống 1 — Ước lượng phí giao hàng

**Vấn đề:** Ước lượng phí giao hàng.

**Vì sao chọn phương án?** Mỗi km tăng một mức phí ổn định nên chọn tuyến tính

**Dữ liệu:** 3 km, phí nền 10000 đồng, 5000 đồng/km.

```python
km=3;total=10000+5000*km
print(total)
```

### Tình huống 2 — Mô hình chi phí tăng theo tải

**Vấn đề:** Mô hình chi phí tăng theo tải.

**Vì sao chọn phương án?** Chi phí có phần tăng bậc hai với tải lớn

**Dữ liệu:** Tải x=4.

```python
load=4
cost=2*load**2+3*load+10
print(cost)
```

### Tình huống 3 — Dự báo từ đa thức mô phỏng

**Vấn đề:** Dự báo từ đa thức mô phỏng.

**Vì sao chọn phương án?** polyval giúp biểu diễn đường cong hệ số đã biết

**Dữ liệu:** Ba điểm thời gian [0,1,2], hệ số [1,0,2].

```python
import numpy as np
print(np.polyval([1,0,2],np.array([0,1,2])))
```

### Tình huống 4 — Mô phỏng tăng trưởng qua kỳ

**Vấn đề:** Mô phỏng tăng trưởng qua kỳ.

**Vì sao chọn phương án?** Lũy thừa mô tả tăng 5% mỗi kỳ, không phải dự đoán chắc chắn

**Dữ liệu:** 1000 đơn vị ban đầu, 3 kỳ.

```python
start,rate,periods=1000,0.05,3
print(round(start*(1+rate)**periods,2))
```

### Tình huống 5 — Vẽ đường tuyến tính dữ liệu

**Vấn đề:** Vẽ đường tuyến tính dữ liệu.

**Vì sao chọn phương án?** linspace tạo mẫu x đều để tính y

**Dữ liệu:** 5 điểm x từ 0 đến 10.

```python
import numpy as np
x=np.linspace(0,10,5)
y=2*x+5
print(list(zip(x,y)))
```

## 6. Các lỗi dễ gặp

Hàm kích hoạt và loss không tự thay thế quy trình huấn luyện; đạo hàm theo một biến không giống gradient nhiều biến. Tránh tràn số mũ, log(0), chia cho 0; luôn để ý learning rate và đơn vị.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ


**Q1. What does Linear function mean? — Thuật ngữ Linear function có nghĩa gì?**

A. It instead means Hàm chứa x², đồ thị là parabol khi hệ số bậc hai khác 0 — Hàm chứa x², đồ thị là parabol khi hệ số bậc hai khác 0

B. It means Đường thẳng có tốc độ thay đổi hằng số — Đường thẳng có tốc độ thay đổi hằng số

C. It instead means Tổng các lũy thừa nguyên không âm của x — Tổng các lũy thừa nguyên không âm của x

D. It instead means Biến nằm trong số mũ, thường mô tả tăng/giảm theo tỷ lệ — Biến nằm trong số mũ, thường mô tả tăng/giảm theo tỷ lệ


**Q2. What does Quadratic mean? — Thuật ngữ Quadratic có nghĩa gì?**

A. It means Hàm chứa x², đồ thị là parabol khi hệ số bậc hai khác 0 — Hàm chứa x², đồ thị là parabol khi hệ số bậc hai khác 0

B. It instead means Tổng các lũy thừa nguyên không âm của x — Tổng các lũy thừa nguyên không âm của x

C. It instead means Biến nằm trong số mũ, thường mô tả tăng/giảm theo tỷ lệ — Biến nằm trong số mũ, thường mô tả tăng/giảm theo tỷ lệ

D. It instead means Đường thẳng có tốc độ thay đổi hằng số — Đường thẳng có tốc độ thay đổi hằng số


**Q3. What does Polynomial mean? — Thuật ngữ Polynomial có nghĩa gì?**

A. It instead means Biến nằm trong số mũ, thường mô tả tăng/giảm theo tỷ lệ — Biến nằm trong số mũ, thường mô tả tăng/giảm theo tỷ lệ

B. It instead means Đường thẳng có tốc độ thay đổi hằng số — Đường thẳng có tốc độ thay đổi hằng số

C. It instead means Hàm chứa x², đồ thị là parabol khi hệ số bậc hai khác 0 — Hàm chứa x², đồ thị là parabol khi hệ số bậc hai khác 0

D. It means Tổng các lũy thừa nguyên không âm của x — Tổng các lũy thừa nguyên không âm của x


**Q4. What does Exponential mean? — Thuật ngữ Exponential có nghĩa gì?**

A. It instead means Đường thẳng có tốc độ thay đổi hằng số — Đường thẳng có tốc độ thay đổi hằng số

B. It instead means Hàm chứa x², đồ thị là parabol khi hệ số bậc hai khác 0 — Hàm chứa x², đồ thị là parabol khi hệ số bậc hai khác 0

C. It means Biến nằm trong số mũ, thường mô tả tăng/giảm theo tỷ lệ — Biến nằm trong số mũ, thường mô tả tăng/giảm theo tỷ lệ

D. It instead means Tổng các lũy thừa nguyên không âm của x — Tổng các lũy thừa nguyên không âm của x


**Q5. What does y=m*x+b do? — Mục đích của y=m*x+b là gì?**

A. Another operation does Quan hệ bậc hai, dùng khi đường cong — Quan hệ bậc hai, dùng khi đường cong

B. It is used to Quan hệ tuyến tính, m là độ dốc, b là hệ số chặn — Quan hệ tuyến tính, m là độ dốc, b là hệ số chặn

C. Another operation does Đánh giá đa thức theo hệ số cao xuống thấp — Đánh giá đa thức theo hệ số cao xuống thấp

D. Another operation does Hàm mũ; cẩn thận overflow và miền thực — Hàm mũ; cẩn thận overflow và miền thực


**Q6. What does y=a*x**2+b*x+c do? — Mục đích của y=a*x**2+b*x+c là gì?**

A. It is used to Quan hệ bậc hai, dùng khi đường cong — Quan hệ bậc hai, dùng khi đường cong

B. Another operation does Đánh giá đa thức theo hệ số cao xuống thấp — Đánh giá đa thức theo hệ số cao xuống thấp

C. Another operation does Hàm mũ; cẩn thận overflow và miền thực — Hàm mũ; cẩn thận overflow và miền thực

D. Another operation does Quan hệ tuyến tính, m là độ dốc, b là hệ số chặn — Quan hệ tuyến tính, m là độ dốc, b là hệ số chặn


**Q7. What does np.polyval(coefficients,x) do? — Mục đích của np.polyval(coefficients,x) là gì?**

A. Another operation does Hàm mũ; cẩn thận overflow và miền thực — Hàm mũ; cẩn thận overflow và miền thực

B. Another operation does Quan hệ tuyến tính, m là độ dốc, b là hệ số chặn — Quan hệ tuyến tính, m là độ dốc, b là hệ số chặn

C. Another operation does Quan hệ bậc hai, dùng khi đường cong — Quan hệ bậc hai, dùng khi đường cong

D. It is used to Đánh giá đa thức theo hệ số cao xuống thấp — Đánh giá đa thức theo hệ số cao xuống thấp


**Q8. What does np.exp(x)/base**x do? — Mục đích của np.exp(x)/base**x là gì?**

A. Another operation does Quan hệ tuyến tính, m là độ dốc, b là hệ số chặn — Quan hệ tuyến tính, m là độ dốc, b là hệ số chặn

B. Another operation does Quan hệ bậc hai, dùng khi đường cong — Quan hệ bậc hai, dùng khi đường cong

C. It is used to Hàm mũ; cẩn thận overflow và miền thực — Hàm mũ; cẩn thận overflow và miền thực

D. Another operation does Đánh giá đa thức theo hệ số cao xuống thấp — Đánh giá đa thức theo hệ số cao xuống thấp


**Q9. Why use this method in scenario 1? — Vì sao chọn cách giải ở tình huống 1?**

A. Chi phí có phần tăng bậc hai với tải lớn — Chi phí có phần tăng bậc hai với tải lớn

B. Mỗi km tăng một mức phí ổn định nên chọn tuyến tính — Mỗi km tăng một mức phí ổn định nên chọn tuyến tính

C. polyval giúp biểu diễn đường cong hệ số đã biết — polyval giúp biểu diễn đường cong hệ số đã biết

D. Lũy thừa mô tả tăng 5% mỗi kỳ, không phải dự đoán chắc chắn — Lũy thừa mô tả tăng 5% mỗi kỳ, không phải dự đoán chắc chắn


**Q10. Why use this method in scenario 2? — Vì sao chọn cách giải ở tình huống 2?**

A. Chi phí có phần tăng bậc hai với tải lớn — Chi phí có phần tăng bậc hai với tải lớn

B. polyval giúp biểu diễn đường cong hệ số đã biết — polyval giúp biểu diễn đường cong hệ số đã biết

C. Lũy thừa mô tả tăng 5% mỗi kỳ, không phải dự đoán chắc chắn — Lũy thừa mô tả tăng 5% mỗi kỳ, không phải dự đoán chắc chắn

D. linspace tạo mẫu x đều để tính y — linspace tạo mẫu x đều để tính y


**Q11. Why use this method in scenario 3? — Vì sao chọn cách giải ở tình huống 3?**

A. Lũy thừa mô tả tăng 5% mỗi kỳ, không phải dự đoán chắc chắn — Lũy thừa mô tả tăng 5% mỗi kỳ, không phải dự đoán chắc chắn

B. linspace tạo mẫu x đều để tính y — linspace tạo mẫu x đều để tính y

C. Mỗi km tăng một mức phí ổn định nên chọn tuyến tính — Mỗi km tăng một mức phí ổn định nên chọn tuyến tính

D. polyval giúp biểu diễn đường cong hệ số đã biết — polyval giúp biểu diễn đường cong hệ số đã biết


**Q12. Why use this method in scenario 4? — Vì sao chọn cách giải ở tình huống 4?**

A. linspace tạo mẫu x đều để tính y — linspace tạo mẫu x đều để tính y

B. Mỗi km tăng một mức phí ổn định nên chọn tuyến tính — Mỗi km tăng một mức phí ổn định nên chọn tuyến tính

C. Lũy thừa mô tả tăng 5% mỗi kỳ, không phải dự đoán chắc chắn — Lũy thừa mô tả tăng 5% mỗi kỳ, không phải dự đoán chắc chắn

D. Chi phí có phần tăng bậc hai với tải lớn — Chi phí có phần tăng bậc hai với tải lớn


**Q13. Why use this method in scenario 5? — Vì sao chọn cách giải ở tình huống 5?**

A. Mỗi km tăng một mức phí ổn định nên chọn tuyến tính — Mỗi km tăng một mức phí ổn định nên chọn tuyến tính

B. linspace tạo mẫu x đều để tính y — linspace tạo mẫu x đều để tính y

C. Chi phí có phần tăng bậc hai với tải lớn — Chi phí có phần tăng bậc hai với tải lớn

D. polyval giúp biểu diễn đường cong hệ số đã biết — polyval giúp biểu diễn đường cong hệ số đã biết


**Q14. Which input belongs to scenario 1? — Tình huống 1 sử dụng dữ liệu gì?**

A. The input is 3 km, phí nền 10000 đồng, 5000 đồng/km — 3 km, phí nền 10000 đồng, 5000 đồng/km

B. Another input is Tải x=4 — Tải x=4

C. Another input is Ba điểm thời gian [0,1,2], hệ số [1,0,2] — Ba điểm thời gian [0,1,2], hệ số [1,0,2]

D. Another input is 1000 đơn vị ban đầu, 3 kỳ — 1000 đơn vị ban đầu, 3 kỳ


**Q15. Which input belongs to scenario 2? — Tình huống 2 sử dụng dữ liệu gì?**

A. Another input is Ba điểm thời gian [0,1,2], hệ số [1,0,2] — Ba điểm thời gian [0,1,2], hệ số [1,0,2]

B. Another input is 1000 đơn vị ban đầu, 3 kỳ — 1000 đơn vị ban đầu, 3 kỳ

C. Another input is 5 điểm x từ 0 đến 10 — 5 điểm x từ 0 đến 10

D. The input is Tải x=4 — Tải x=4


**Q16. Which input belongs to scenario 3? — Tình huống 3 sử dụng dữ liệu gì?**

A. Another input is 1000 đơn vị ban đầu, 3 kỳ — 1000 đơn vị ban đầu, 3 kỳ

B. Another input is 5 điểm x từ 0 đến 10 — 5 điểm x từ 0 đến 10

C. The input is Ba điểm thời gian [0,1,2], hệ số [1,0,2] — Ba điểm thời gian [0,1,2], hệ số [1,0,2]

D. Another input is 3 km, phí nền 10000 đồng, 5000 đồng/km — 3 km, phí nền 10000 đồng, 5000 đồng/km


**Q17. Which input belongs to scenario 4? — Tình huống 4 sử dụng dữ liệu gì?**

A. Another input is 5 điểm x từ 0 đến 10 — 5 điểm x từ 0 đến 10

B. The input is 1000 đơn vị ban đầu, 3 kỳ — 1000 đơn vị ban đầu, 3 kỳ

C. Another input is 3 km, phí nền 10000 đồng, 5000 đồng/km — 3 km, phí nền 10000 đồng, 5000 đồng/km

D. Another input is Tải x=4 — Tải x=4


**Q18. Which input belongs to scenario 5? — Tình huống 5 sử dụng dữ liệu gì?**

A. The input is 5 điểm x từ 0 đến 10 — 5 điểm x từ 0 đến 10

B. Another input is 3 km, phí nền 10000 đồng, 5000 đồng/km — 3 km, phí nền 10000 đồng, 5000 đồng/km

C. Another input is Tải x=4 — Tải x=4

D. Another input is Ba điểm thời gian [0,1,2], hệ số [1,0,2] — Ba điểm thời gian [0,1,2], hệ số [1,0,2]


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
| Q1 | **B** | It means Đường thẳng có tốc độ thay đổi hằng số | Đường thẳng có tốc độ thay đổi hằng số |
| Q2 | **A** | It means Hàm chứa x², đồ thị là parabol khi hệ số bậc hai khác 0 | Hàm chứa x², đồ thị là parabol khi hệ số bậc hai khác 0 |
| Q3 | **D** | It means Tổng các lũy thừa nguyên không âm của x | Tổng các lũy thừa nguyên không âm của x |
| Q4 | **C** | It means Biến nằm trong số mũ, thường mô tả tăng/giảm theo tỷ lệ | Biến nằm trong số mũ, thường mô tả tăng/giảm theo tỷ lệ |
| Q5 | **B** | It is used to Quan hệ tuyến tính, m là độ dốc, b là hệ số chặn | Quan hệ tuyến tính, m là độ dốc, b là hệ số chặn |
| Q6 | **A** | It is used to Quan hệ bậc hai, dùng khi đường cong | Quan hệ bậc hai, dùng khi đường cong |
| Q7 | **D** | It is used to Đánh giá đa thức theo hệ số cao xuống thấp | Đánh giá đa thức theo hệ số cao xuống thấp |
| Q8 | **C** | It is used to Hàm mũ; cẩn thận overflow và miền thực | Hàm mũ; cẩn thận overflow và miền thực |
| Q9 | **B** | Mỗi km tăng một mức phí ổn định nên chọn tuyến tính | Mỗi km tăng một mức phí ổn định nên chọn tuyến tính |
| Q10 | **A** | Chi phí có phần tăng bậc hai với tải lớn | Chi phí có phần tăng bậc hai với tải lớn |
| Q11 | **D** | polyval giúp biểu diễn đường cong hệ số đã biết | polyval giúp biểu diễn đường cong hệ số đã biết |
| Q12 | **C** | Lũy thừa mô tả tăng 5% mỗi kỳ, không phải dự đoán chắc chắn | Lũy thừa mô tả tăng 5% mỗi kỳ, không phải dự đoán chắc chắn |
| Q13 | **B** | linspace tạo mẫu x đều để tính y | linspace tạo mẫu x đều để tính y |
| Q14 | **A** | The input is 3 km, phí nền 10000 đồng, 5000 đồng/km | 3 km, phí nền 10000 đồng, 5000 đồng/km |
| Q15 | **D** | The input is Tải x=4 | Tải x=4 |
| Q16 | **C** | The input is Ba điểm thời gian [0,1,2], hệ số [1,0,2] | Ba điểm thời gian [0,1,2], hệ số [1,0,2] |
| Q17 | **B** | The input is 1000 đơn vị ban đầu, 3 kỳ | 1000 đơn vị ban đầu, 3 kỳ |
| Q18 | **A** | The input is 5 điểm x từ 0 đến 10 | 5 điểm x từ 0 đến 10 |
| Q19 | **D** | Input meaning and units | Ý nghĩa và đơn vị đầu vào |
| Q20 | **C** | Verify results and edge cases | Kiểm tra kết quả và trường hợp biên |
