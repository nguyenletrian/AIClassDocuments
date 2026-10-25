# PY-28 — Hàm tuyến tính, bậc hai, đa thức và hàm mũ


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Linear function** — hàm tuyến tính; **Quadratic** — hàm bậc hai.

`Hàm Python → Hàm toán theo dữ liệu → Loss → Gradient`

**Học xong dùng để làm gì?** Mô tả dự đoán bằng hàm f(x), nhận biết đầu vào, đầu ra và ảnh hưởng của tham số.

**Kết nối kiến thức tiếp theo:** PY-29 bổ sung hàm kích hoạt để biểu diễn quan hệ phi tuyến.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| Linear function | hàm tuyến tính | Đường thẳng có tốc độ thay đổi hằng số |
| Quadratic | hàm bậc hai | Hàm chứa x², đồ thị là parabol khi hệ số bậc hai khác 0 |
| Polynomial | hàm đa thức | Tổng các lũy thừa nguyên không âm của x |
| Exponential | hàm mũ | Biến nằm trong số mũ, thường mô tả tăng/giảm theo tỷ lệ |

## 3. Hàm và cách gọi bằng Python

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm / tham số | Giải thích |
|---|---|
| `y=m*x+b` | Quan hệ tuyến tính, m là độ dốc, b là hệ số chặn |
| `y=a*x**2+b*x+c` | Quan hệ bậc hai, dùng khi đường cong |
| `np.polyval(coefficients,x)` | Đánh giá đa thức theo hệ số cao xuống thấp |
| `np.exp(x)/base**x` | Hàm mũ; cẩn thận overflow và miền thực |

## 4. Khái niệm liên quan

**Nội dung chính:** đầu vào x được chuyển thành đầu ra y theo một quy tắc. Hàm bậc nhất tạo đường thẳng với độ dốc không đổi; hàm bậc hai và đa thức tạo đường cong; hàm mũ nhân theo tỷ lệ sau mỗi kỳ. Mỗi ví dụ nói rõ biến, hệ số và đơn vị.

### 4.1. Linear function — Mỗi bước tăng một mức cố định

**Từ vựng trong mục:** **Linear function** — hàm bậc nhất; **Slope/intercept** — hệ số góc/hệ số chặn.

Trong bài, **hàm tuyến tính dạng affine** `y=m*x+b` mô tả đầu ra thay đổi đều theo đầu vào. Dịch vụ thu 10 nghìn đồng ban đầu và 5 nghìn mỗi km: x là số km, m=5 nghìn/km, b=10 nghìn. Đi 3 km hết 25 nghìn đồng. Đồ thị là đường thẳng; m nói **mỗi km thêm bao nhiêu**, b nói **giá ở x=0**. Trong toán tuyến tính thuần túy, `mx+b` với b khác 0 gọi chính xác là hàm affine.

```python
# Mục đích: Mỗi bước tăng một mức cố định.
def delivery_fee(km):
    return 5 * km + 10

print(delivery_fee(3))
```

**Kết quả khi chạy:**

```text
25
```

Phí là 25 nghìn đồng, gồm phí gốc 10 và 3×5 nghìn theo khoảng cách.

### 4.2. Quadratic — Mức thay đổi không cố định

**Từ vựng trong mục:** **Quadratic** — bậc hai; **Coefficient** — hệ số.

Hàm bậc hai `y=ax²+bx+c` (a khác 0) có đồ thị **parabol**, khác đường thẳng vì tốc độ thay đổi không cố định. Ví dụ chi phí mẫu `2x² + 3x + 10` với x là mức tải (đơn vị tải đã quy định), 2 có đơn vị chi phí/tải², 3 là chi phí/tải và 10 là chi phí cố định. Khi x=4, giá trị bằng 54. Không hiểu hệ số bình phương là chi phí thực nếu mô hình mới chỉ là giả định.

```python
# Mục đích: Mức thay đổi không cố định.
def cost(load):
    return 2 * load ** 2 + 3 * load + 10

print(cost(4))
```

**Kết quả khi chạy:**

```text
54
```

Với tải 4, mô hình cho chi phí 54 đơn vị tiền; đây là kết quả theo hàm đã đặt.

### 4.3. Polynomial — Nhiều lũy thừa của một biến

**Từ vựng trong mục:** **Polynomial** — đa thức; **Degree** — bậc đa thức.

**Đa thức** cộng các hạng `a_n*x^n` theo lũy thừa nguyên không âm. Tuyến tính là bậc 1, bậc hai là bậc 2, và còn có đa thức bậc cao hơn. `np.polyval([1,0,2], x)` biểu diễn `x² + 0*x + 2`; **hệ số đặt từ bậc cao xuống bậc thấp**, rất dễ viết ngược. Với ba đầu vào 0,1,2, hàm cho kết quả 2,3,6.

```python
# Mục đích: Nhiều lũy thừa của một biến.
import numpy as np

x = np.array([0, 1, 2])
print(np.polyval([1, 0, 2], x))
```

**Kết quả khi chạy:**

```text
[2 3 6]
```

Hệ số `[1,0,2]` nghĩa là x²+2, không phải 1+2x².

### 4.4. Exponential — Nhân tỷ lệ lặp qua mỗi kỳ

**Từ vựng trong mục:** **Exponential** — hàm mũ; **Growth rate** — tỷ lệ tăng.

**Hàm mũ** có biến ở **số mũ**, ví dụ `y=y0*(1+r)^t`. Với một chỉ số ban đầu 1.000 đơn vị và tỷ lệ tăng 5% mỗi kỳ, sau 3 kỳ là `1000×1.05³ = 1157.625`. Làm tròn hai chữ số được 1157.63. Hàm mũ khác tuyến tính vì mỗi kỳ tăng 5% của **giá trị mới**, không phải luôn tăng 50 đơn vị. Mô hình này chỉ mô phỏng một giả định tăng trưởng đều.

```python
# Mục đích: Nhân tỷ lệ lặp qua mỗi kỳ.
initial = 1000
rate = 0.05
periods = 3
print(round(initial * (1 + rate) ** periods, 2))
```

**Kết quả khi chạy:**

```text
1157.63
```

Sau ba kỳ tăng trưởng lũy kế, chỉ số khoảng 1157,63 đơn vị, không phải giá trị dự báo chắc chắn.

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Tính phí giao hàng theo km · Cấp 1: Thử một phép biến đổi

**Tình huống thực tế:** Dịch vụ tính 10.000 đồng cố định và 5.000 đồng/km. Một khách đặt giao 3 km. Hãy tính tổng phí đồng với mô hình tăng đều theo km.

**Vì sao chọn cách giải này?** Phí tăng đúng một mức cố định theo mỗi km nên dùng hàm dạng `base+rate*km`.

**Quy trình giải:**

1. Đặt `km=3`, phí gốc 10.000 và 5.000 đồng/km.
2. Nhân số km với đơn giá rồi cộng phí gốc.
3. In tổng phí tính theo đồng.

```python
# Mục đích: Tính phí giao hàng theo km.
km = 3
fee = 10000 + 5000 * km
print(fee)
```

**Kết quả khi chạy:**

```text
25000
```

Tổng phí 25.000 đồng gồm 10.000 phí gốc và 15.000 theo km.

**Bài thực hành nâng cấp — cấp 1/5:** Đơn vị phân tích ghi **10 chuyến hàng với quãng đường đầu vào x (km)**. Hãy dùng hàm tuyến tính dự đoán chi phí 10 chuyến. Ở cấp 4–5 có số đo bị thiếu, cần xử lý riêng trước khi tính hoặc chuẩn hóa thay vì dùng nó làm giá trị thật.

```python
import numpy as np
# Mỗi phần tử là một chuyến hàng / một tín hiệu, đơn vị phụ thuộc bài toán.
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],dtype=float)
clean = x[np.isfinite(x)]
result = (3*x+5).tolist()
print("Số quan sát:",len(x))
print("Kết quả:",result)
```

**Đọc kết quả:** Đã nhận 10 mẫu; chỉ số và đơn vị phải được hiểu trong bài toán dự báo; cùng một dữ liệu có thể tạo ra đầu ra khác nhau theo phương pháp.

### Tình huống 2 — Tính chi phí theo tải có thành phần bậc hai · Cấp 2: Tính trên toàn bộ dữ liệu

**Tình huống thực tế:** Mô hình giả định chi phí là `2x²+3x+10`, đơn vị tiền đã chọn. Thiết bị đang có tải x=4. Tính chi phí theo công thức.

**Vì sao chọn cách giải này?** Hàm bậc hai mô tả phần chi phí có độ tăng lớn dần khi mức tải tăng.

**Quy trình giải:**

1. Nhận mức tải 4.
2. Thay x=4 vào biểu thức gồm hạng bậc hai, tuyến tính và chi phí cố định.
3. In giá trị 54 đơn vị tiền.

```python
# Mục đích: Tính chi phí theo tải có thành phần bậc hai.
load = 4
cost = 2 * load ** 2 + 3 * load + 10
print(cost)
```

**Kết quả khi chạy:**

```text
54
```

Chi phí theo mô hình đã cho bằng 54 đơn vị tiền.

**Bài thực hành nâng cấp — cấp 2/5:** Đơn vị phân tích ghi **12 chuyến hàng với quãng đường đầu vào x (km)**. Hãy dùng hàm bậc hai phản ánh hao phí theo 12 mức tải. Ở cấp 4–5 có số đo bị thiếu, cần xử lý riêng trước khi tính hoặc chuẩn hóa thay vì dùng nó làm giá trị thật.

```python
import numpy as np
# Mỗi phần tử là một chuyến hàng / một tín hiệu, đơn vị phụ thuộc bài toán.
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],dtype=float)
clean = x[np.isfinite(x)]
result = (2*x*x+3*x+5).tolist()
print("Số quan sát:",len(x))
print("Kết quả:",result)
```

**Đọc kết quả:** Đã nhận 12 mẫu; chỉ số và đơn vị phải được hiểu trong bài toán dự báo; cùng một dữ liệu có thể tạo ra đầu ra khác nhau theo phương pháp.

### Tình huống 3 — Tính đầu ra đa thức trên nhiều điểm · Cấp 3: Kết hợp phi tuyến

**Tình huống thực tế:** Mô hình minh họa `y=x²+2` cần đánh giá ở đầu vào x=0,1,2. In các kết quả theo thứ tự đầu vào.

**Vì sao chọn cách giải này?** `np.polyval` áp hệ số một lần cho toàn mảng và không cần tự viết vòng lặp tính x²+2.

**Quy trình giải:**

1. Tạo mảng `[0,1,2]`.
2. Truyền hệ số đa thức từ bậc cao tới thấp `[1,0,2]`.
3. In ba kết quả cùng thứ tự.

```python
# Mục đích: Tính đầu ra đa thức trên nhiều điểm.
import numpy as np

x = np.array([0, 1, 2])
print(np.polyval([1, 0, 2], x))
```

**Kết quả khi chạy:**

```text
[2 3 6]
```

Đầu ra ở x=0,1,2 lần lượt là 2, 3, 6.

**Bài thực hành nâng cấp — cấp 3/5:** Đơn vị phân tích ghi **15 chuyến hàng với quãng đường đầu vào x (km)**. Hãy đưa 15 điểm đầu vào qua một đa thức bậc ba. Ở cấp 4–5 có số đo bị thiếu, cần xử lý riêng trước khi tính hoặc chuẩn hóa thay vì dùng nó làm giá trị thật.

```python
import numpy as np
# Mỗi phần tử là một chuyến hàng / một tín hiệu, đơn vị phụ thuộc bài toán.
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],dtype=float)
clean = x[np.isfinite(x)]
result = (0.1*x**3-x*x+5*x+20).round(2).tolist()
print("Số quan sát:",len(x))
print("Kết quả:",result)
```

**Đọc kết quả:** Đã nhận 15 mẫu; chỉ số và đơn vị phải được hiểu trong bài toán dự báo; cùng một dữ liệu có thể tạo ra đầu ra khác nhau theo phương pháp.

### Tình huống 4 — Mô phỏng tăng trưởng theo kỳ · Cấp 4: Ổn định và dữ liệu thiếu

**Tình huống thực tế:** Một chỉ số có giá trị ban đầu 1.000 đơn vị, được giả định tăng 5% mỗi kỳ, kéo dài ba kỳ liên tiếp. Hãy tính kết quả cuối.

**Vì sao chọn cách giải này?** Lũy thừa mô tả tăng dựa trên giá trị của kỳ trước, khác cộng một lượng cố định.

**Quy trình giải:**

1. Gán chỉ số ban đầu 1000, tỷ lệ 0.05 và số kỳ 3.
2. Tính `initial*(1+rate)**periods`.
3. Làm tròn hai chữ số và in kết quả.

```python
# Mục đích: Mô phỏng tăng trưởng theo kỳ.
initial = 1000
rate = 0.05
periods = 3
print(round(initial * (1 + rate) ** periods, 2))
```

**Kết quả khi chạy:**

```text
1157.63
```

Giá trị sau ba kỳ là khoảng 1157.63 đơn vị theo giả định tăng trưởng.

**Bài thực hành nâng cấp — cấp 4/5:** Đơn vị phân tích ghi **18 chuyến hàng với quãng đường đầu vào x (km)**. Hãy mô tả tăng trưởng bằng hàm mũ, kiểm tra giá trị thiếu. Ở cấp 4–5 có số đo bị thiếu, cần xử lý riêng trước khi tính hoặc chuẩn hóa thay vì dùng nó làm giá trị thật.

```python
import numpy as np
# Mỗi phần tử là một chuyến hàng / một tín hiệu, đơn vị phụ thuộc bài toán.
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, np.nan, 17, 18],dtype=float)
clean = x[np.isfinite(x)]
result = {'valid':int(np.isfinite(x).sum()),'growth':np.exp(0.05*x[np.isfinite(x)]).round(3).tolist()}
print("Số quan sát:",len(x))
print("Kết quả:",result)
```

**Đọc kết quả:** Đã nhận 18 mẫu; chỉ số và đơn vị phải được hiểu trong bài toán dự báo; cùng một dữ liệu có thể tạo ra đầu ra khác nhau theo phương pháp.

### Tình huống 5 — Tạo các điểm của đường dự đoán · Cấp 5: So sánh nhiều mô hình

**Tình huống thực tế:** Đội phân tích muốn kiểm tra đường y=2x+5 tại sáu giá trị x cách đều từ 0 đến 10. Cần liệt kê từng cặp (x,y) để dễ vẽ sau này.

**Vì sao chọn cách giải này?** `np.linspace` tạo mốc cách đều; NumPy tính y cho toàn bộ mốc và `zip` ghép đúng từng cặp.

**Quy trình giải:**

1. Tạo sáu mốc x từ 0 đến 10 bằng `linspace`.
2. Tính y=2x+5 cho từng mốc.
3. Ghép các cặp và in dạng số nguyên (ở đây mọi giá trị đều nguyên).

```python
# Mục đích: Tạo các điểm của đường dự đoán.
import numpy as np

x = np.linspace(0, 10, 6)
y = 2 * x + 5
print([(int(a), int(b)) for a, b in zip(x, y)])
```

**Kết quả khi chạy:**

```text
[(0, 5), (2, 9), (4, 13), (6, 17), (8, 21), (10, 25)]
```

Mỗi cặp gồm đầu vào x và đầu ra y tương ứng; đường tăng đều theo x.

**Bài thực hành nâng cấp — cấp 5/5:** Đơn vị phân tích ghi **20 chuyến hàng với quãng đường đầu vào x (km)**. Hãy so sánh dự đoán hàm tuyến tính và phi tuyến với 20 quan sát. Ở cấp 4–5 có số đo bị thiếu, cần xử lý riêng trước khi tính hoặc chuẩn hóa thay vì dùng nó làm giá trị thật.

```python
import numpy as np
# Mỗi phần tử là một chuyến hàng / một tín hiệu, đơn vị phụ thuộc bài toán.
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, np.nan, 17, 18, 19, np.nan],dtype=float)
clean = x[np.isfinite(x)]
result = {'linear_mean':round(float(np.nanmean(3*x+5)),2),'quadratic_mean':round(float(np.nanmean(2*x*x+3*x+5)),2),'missing':int(np.isnan(x).sum())}
print("Số quan sát:",len(x))
print("Kết quả:",result)
```

**Đọc kết quả:** Đã nhận 20 mẫu; chỉ số và đơn vị phải được hiểu trong bài toán dự báo; cùng một dữ liệu có thể tạo ra đầu ra khác nhau theo phương pháp.

## 6. Sai lầm thường gặp

- Hàm affine `mx+b` có hệ số chặn; không phải mọi biểu thức có chữ x đều là hàm tuyến tính theo nghĩa toán học chặt chẽ.
- Không nhầm bậc hai với hàm mũ: bậc hai có x ở cơ số rồi bình phương, hàm mũ có x ở số mũ.
- `np.polyval` đọc hệ số từ **bậc cao xuống thấp**.
- Độ dốc và hệ số chặn cần đơn vị tương thích với x và y.
- Tăng trưởng mũ giả định tỷ lệ ổn định, không bảo đảm dự báo đúng trong thực tế.
- Đồ thị đẹp hoặc khớp vài điểm chưa chứng minh mô hình dự báo tốt trên dữ liệu mới.

## 7. Trắc nghiệm

**Câu hỏi chỉ về nội dung lý thuyết, cú pháp và cách phân biệt hàm.**

**Q1. Which form is a first-degree affine function? | Dạng nào là hàm affine bậc nhất?**

A. `y=m*x+b` | `y=m*x+b`

B. `y=a*x**2+b*x+c` with a≠0 | `y=a*x**2+b*x+c` với a≠0

C. Highest nonzero power of x | Lũy thừa cao nhất có hệ số khác 0

D. A variable appears in the exponent | Biến xuất hiện ở số mũ

**Đáp án: A**

**Giải thích:** Dạng affine gồm hệ số góc và hệ số chặn.


**Q2. Which form contains a nonzero quadratic term? | Dạng nào có hạng bậc hai khác 0?**

A. `y=m*x+b` | `y=m*x+b`

B. `y=a*x**2+b*x+c` with a≠0 | `y=a*x**2+b*x+c` với a≠0

C. Highest nonzero power of x | Lũy thừa cao nhất có hệ số khác 0

D. A variable appears in the exponent | Biến xuất hiện ở số mũ

**Đáp án: B**

**Giải thích:** Hàm bậc hai có hạng x bình phương.


**Q3. What does polynomial degree measure? | Bậc đa thức cho biết gì?**

A. `y=m*x+b` | `y=m*x+b`

B. `y=a*x**2+b*x+c` with a≠0 | `y=a*x**2+b*x+c` với a≠0

C. Highest nonzero power of x | Lũy thừa cao nhất có hệ số khác 0

D. A variable appears in the exponent | Biến xuất hiện ở số mũ

**Đáp án: C**

**Giải thích:** Bậc là số mũ cao nhất có hệ số khác 0.


**Q4. What characterizes an exponential function? | Đặc điểm của hàm mũ là gì?**

A. `y=m*x+b` | `y=m*x+b`

B. `y=a*x**2+b*x+c` with a≠0 | `y=a*x**2+b*x+c` với a≠0

C. Highest nonzero power of x | Lũy thừa cao nhất có hệ số khác 0

D. A variable appears in the exponent | Biến xuất hiện ở số mũ

**Đáp án: D**

**Giải thích:** Hàm mũ có số mũ thay đổi.


**Q5. What does slope m represent in y=mx+b? | Hệ số góc m trong y=mx+b biểu thị gì?**

A. Output change per one input unit | Mức thay đổi đầu ra mỗi đơn vị đầu vào

B. Predicted output at x=0 | Đầu ra dự tính khi x=0

C. Parabola | Parabol

D. It compounds relative changes | Nó cộng dồn mức tăng theo tỷ lệ

**Đáp án: A**

**Giải thích:** Hệ số góc là mức đổi y mỗi đơn vị x.


**Q6. What does intercept b represent? | Hệ số chặn b biểu thị gì?**

A. Output change per one input unit | Mức thay đổi đầu ra mỗi đơn vị đầu vào

B. Predicted output at x=0 | Đầu ra dự tính khi x=0

C. Parabola | Parabol

D. It compounds relative changes | Nó cộng dồn mức tăng theo tỷ lệ

**Đáp án: B**

**Giải thích:** Đặt x=0 còn hệ số chặn.


**Q7. What shape does a quadratic graph typically have? | Đồ thị hàm bậc hai thường có dạng gì?**

A. Output change per one input unit | Mức thay đổi đầu ra mỗi đơn vị đầu vào

B. Predicted output at x=0 | Đầu ra dự tính khi x=0

C. Parabola | Parabol

D. It compounds relative changes | Nó cộng dồn mức tăng theo tỷ lệ

**Đáp án: C**

**Giải thích:** Hạng bậc hai khác 0 tạo đồ thị parabol.


**Q8. How does exponential growth differ from linear growth? | Tăng trưởng mũ khác tăng tuyến tính ở đâu?**

A. Output change per one input unit | Mức thay đổi đầu ra mỗi đơn vị đầu vào

B. Predicted output at x=0 | Đầu ra dự tính khi x=0

C. Parabola | Parabol

D. It compounds relative changes | Nó cộng dồn mức tăng theo tỷ lệ

**Đáp án: D**

**Giải thích:** Lãi kép nhân theo tỷ lệ mỗi kỳ.


**Q9. Which NumPy function evaluates a polynomial? | Hàm NumPy nào tính đa thức?**

A. `np.polyval(coefficients,x)` | `np.polyval(coefficients,x)`

B. Highest degree first | Bậc cao nhất trước

C. `np.exp(x)` | `np.exp(x)`

D. `np.linspace(start,stop,num)` | `np.linspace(start,stop,num)`

**Đáp án: A**

**Giải thích:** polyval tính đa thức theo các hệ số có thứ tự.


**Q10. In what order does `np.polyval` take coefficients? | `np.polyval` nhận hệ số theo thứ tự gì?**

A. `np.polyval(coefficients,x)` | `np.polyval(coefficients,x)`

B. Highest degree first | Bậc cao nhất trước

C. `np.exp(x)` | `np.exp(x)`

D. `np.linspace(start,stop,num)` | `np.linspace(start,stop,num)`

**Đáp án: B**

**Giải thích:** Hệ số bậc cao nhất đứng đầu.


**Q11. Which function computes e raised to x? | Hàm nào tính e mũ x?**

A. `np.polyval(coefficients,x)` | `np.polyval(coefficients,x)`

B. Highest degree first | Bậc cao nhất trước

C. `np.exp(x)` | `np.exp(x)`

D. `np.linspace(start,stop,num)` | `np.linspace(start,stop,num)`

**Đáp án: C**

**Giải thích:** exp tính hàm mũ cơ số e.


**Q12. Which function makes evenly spaced samples? | Hàm nào tạo các điểm cách đều?**

A. `np.polyval(coefficients,x)` | `np.polyval(coefficients,x)`

B. Highest degree first | Bậc cao nhất trước

C. `np.exp(x)` | `np.exp(x)`

D. `np.linspace(start,stop,num)` | `np.linspace(start,stop,num)`

**Đáp án: D**

**Giải thích:** linspace tạo số lượng điểm cách đều yêu cầu.


**Q13. What is the value of y=2x+5 at x=0? | Giá trị y=2x+5 khi x=0 là gì?**

A. 5 | 5

B. 6 | 6

C. 16 | 16

D. 4 | 4

**Đáp án: A**

**Giải thích:** Khi x=0, ta có 2×0+5=5.


**Q14. What is the value of x²+2 at x=2? | Giá trị x²+2 khi x=2 là gì?**

A. 5 | 5

B. 6 | 6

C. 16 | 16

D. 4 | 4

**Đáp án: B**

**Giải thích:** Bình phương 2 rồi cộng 2 bằng 6.


**Q15. What is 2 raised to the fourth power? | 2 mũ 4 bằng gì?**

A. 5 | 5

B. 6 | 6

C. 16 | 16

D. 4 | 4

**Đáp án: C**

**Giải thích:** 2 nhân bốn lần bằng 16.


**Q16. How many intervals are between five evenly spaced points? | Năm điểm cách đều tạo bao nhiêu khoảng?**

A. 5 | 5

B. 6 | 6

C. 16 | 16

D. 4 | 4

**Đáp án: D**

**Giải thích:** n điểm tạo n−1 khoảng.


**Q17. What does `np.exp(0)` equal? | `np.exp(0)` bằng bao nhiêu?**

A. 1 | 1

B. Its slope changes with x | Độ dốc thay đổi theo x

C. A constant additive increment | Mỗi bước cộng cùng một mức

D. Accuracy on unseen real-world data | Độ chính xác trên dữ liệu thực chưa gặp

**Đáp án: A**

**Giải thích:** Cơ số khác 0 mũ 0 bằng 1.


**Q18. How does a quadratic differ from a first-degree affine function? | Hàm bậc hai khác hàm affine bậc nhất ở đâu?**

A. 1 | 1

B. Its slope changes with x | Độ dốc thay đổi theo x

C. A constant additive increment | Mỗi bước cộng cùng một mức

D. Accuracy on unseen real-world data | Độ chính xác trên dữ liệu thực chưa gặp

**Đáp án: B**

**Giải thích:** Mức tăng của hàm bậc hai thay đổi theo x.


**Q19. Which constraint gives a constant-per-step growth model? | Mô hình tăng đều mỗi bước cần điều kiện gì?**

A. 1 | 1

B. Its slope changes with x | Độ dốc thay đổi theo x

C. A constant additive increment | Mỗi bước cộng cùng một mức

D. Accuracy on unseen real-world data | Độ chính xác trên dữ liệu thực chưa gặp

**Đáp án: C**

**Giải thích:** Cộng hằng số tạo mức tăng cố định.


**Q20. What does a fitted function alone not prove? | Một hàm được khớp dữ liệu chưa chứng minh được gì?**

A. 1 | 1

B. Its slope changes with x | Độ dốc thay đổi theo x

C. A constant additive increment | Mỗi bước cộng cùng một mức

D. Accuracy on unseen real-world data | Độ chính xác trên dữ liệu thực chưa gặp

**Đáp án: D**

**Giải thích:** Khả năng dự đoán cần được kiểm chứng ngoài các ví dụ khớp.

## 8. Bài tiếp theo

`Hàm Python → Hàm toán theo dữ liệu → Loss → Gradient`.
