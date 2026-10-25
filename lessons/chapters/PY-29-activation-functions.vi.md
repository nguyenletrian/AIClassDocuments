# PY-29 — Activation: ReLU, sigmoid, tanh, softmax


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **ReLU** — hàm chỉnh lưu; **Sigmoid** — hàm sigmoid.

`Hàm số → Activation → Neural Network → Classification`

**Học xong dùng để làm gì?** Hiểu ReLU/sigmoid biến đổi tín hiệu và giúp mô hình vượt giới hạn của lớp tuyến tính thuần túy.

**Kết nối kiến thức tiếp theo:** PY-30 dùng loss để đo dự đoán sai thực tế bao nhiêu.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| ReLU | hàm chỉnh lưu | Giữ số dương, số âm thành 0 |
| Sigmoid | hàm sigmoid | Ánh xạ số thực về khoảng (0,1) |
| Tanh | hàm tanh | Ánh xạ số thực về (-1,1) |
| Softmax | hàm softmax | Biến logits thành phân phối xác suất tổng bằng 1 |

## 3. Hàm và cách gọi bằng Python

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm / tham số | Giải thích |
|---|---|
| `np.maximum(0,x)` | ReLU, tạo phi tuyến cho mạng |
| `1/(1+np.exp(-x))` | Sigmoid, cẩn thận số quá lớn |
| `np.tanh(x)` | Kích hoạt có đầu ra âm/dương |
| `np.exp(z-max(z))/sum(... )` | Softmax ổn định hơn tính exp(z) trực tiếp |

## 4. Khái niệm liên quan

**Nội dung chính:** một mạng nơ-ron áp hàm kích hoạt lên điểm thô để tạo quan hệ phi tuyến. ReLU chặn phần âm, sigmoid nén về (0,1), tanh giữ dấu trong (−1,1), còn softmax ràng buộc nhiều lớp thành phân phối có tổng 1.

### 4.1. ReLU — Giữ phần dương, chặn phần âm

**Từ vựng trong mục:** **ReLU** — Rectified Linear Unit; **Activation** — kích hoạt.

**Activation function (hàm kích hoạt)** biến đổi đầu ra của một nơ-ron trước khi chuyển sang bước kế tiếp. **ReLU** tính `max(0,x)`: đầu vào âm được chuyển về 0, đầu vào dương được giữ. Ví dụ các tín hiệu `[-2,0,3]` thành `[0,0,3]`. Đây là hàm gấp khúc tại 0, giúp mạng có quan hệ phi tuyến; song nơ-ron có thể ngừng cập nhật nếu liên tục nhận vùng âm.

```python
# Mục đích: Giữ phần dương, chặn phần âm.
import numpy as np

signals = np.array([-2, 0, 3])
print(np.maximum(0, signals).tolist())
```

**Kết quả khi chạy:**

```text
[0, 0, 3]
```

ReLU không giữ phần âm; đầu vào dương bằng 3 đi qua không đổi.

### 4.2. Sigmoid — Ánh xạ một điểm thô sang (0,1)

**Từ vựng trong mục:** **Sigmoid** — hàm chữ S; **Logit** — điểm thô.

**Sigmoid** là `1/(1+exp(-x))`, đổi một **logit** (điểm thô có thể âm hoặc dương) thành số trong khoảng **(0,1)**. Ở x=0 đầu ra đúng 0.5; x âm dưới 0.5 và x dương trên 0.5. Trong phân loại nhị phân, thường dùng sigmoid cho lớp dương, nhưng bản thân giá trị đầu ra **không bảo đảm là xác suất đã hiệu chuẩn**. Khi x quá lớn về độ lớn, cần triển khai số học ổn định hơn công thức trực tiếp.

```python
# Mục đích: Ánh xạ một điểm thô sang (0,1).
import numpy as np

x = np.array([-1.0, 0.0, 1.0])
scores = 1 / (1 + np.exp(-x))
print(np.round(scores, 3).tolist())
```

**Kết quả khi chạy:**

```text
[0.269, 0.5, 0.731]
```

Điểm âm được ánh xạ dưới 0.5, điểm 0 thành 0.5 và điểm dương trên 0.5.

### 4.3. Tanh — Giữ dấu âm và dương quanh zero

**Từ vựng trong mục:** **Tanh** — tang hyperbolic; **Zero-centered** — cân quanh 0.

**Tanh** cũng cong chữ S nhưng đầu ra nằm trong **(−1,1)** thay vì (0,1). Đầu vào âm cho đầu ra âm, đầu vào 0 cho 0, đầu vào dương cho dương. Vì cân quanh 0, tanh có thể thích hợp khi cần giữ dấu tín hiệu. Với x=−1,0,1 kết quả khoảng −0.762, 0, 0.762. Khi |x| rất lớn, tanh bão hòa gần ±1 nên độ dốc nhỏ.

```python
# Mục đích: Giữ dấu âm và dương quanh zero.
import numpy as np

x = np.array([-1.0, 0.0, 1.0])
print(np.round(np.tanh(x), 3).tolist())
```

**Kết quả khi chạy:**

```text
[-0.762, 0.0, 0.762]
```

Hàm giữ dấu âm/dương và bằng 0 tại đầu vào 0.

### 4.4. Softmax — So sánh nhiều lớp cùng lúc

**Từ vựng trong mục:** **Softmax** — chuẩn hóa điểm nhiều lớp; **Class logit** — điểm thô theo lớp.

Khi mô hình phân loại **một nhãn trong ba lớp loại trừ nhau**, nó có ba logit (điểm thô) `z=[2,1,0.1]`. Softmax dùng `exp(z_i)/sum(exp(z_j))` để mỗi lớp nhận giá trị trong (0,1) và **tổng các lớp bằng 1**. Trừ `max(z)` trước khi tính exp giúp giảm nguy cơ tràn số mà không đổi kết quả. Khác sigmoid áp riêng từng giá trị, softmax ràng buộc các lớp cạnh tranh nhau.

```python
# Mục đích: So sánh nhiều lớp cùng lúc.
import numpy as np

z = np.array([2.0, 1.0, 0.1])
e = np.exp(z - z.max())
p = e / e.sum()
print(np.round(p, 3).tolist())
```

**Kết quả khi chạy:**

```text
[0.659, 0.242, 0.099]
```

Lớp đầu có điểm chuẩn hóa cao nhất; tổng ba điểm trước làm tròn là 1.

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Chặn tín hiệu âm bằng ReLU · Cấp 1: Thử một phép biến đổi

**Tình huống thực tế:** Một lớp mạng nhận bốn tín hiệu đầu vào `[-2,0,3,5]`, không có đơn vị vì đây là logit nội bộ. Cần giữ giá trị dương và cho mọi giá trị âm về 0.

**Vì sao chọn cách giải này?** ReLU đúng với quy tắc xử lý `max(0,x)` mà không cần từng điều kiện `if`.

**Quy trình giải:**

1. Lưu bốn đầu vào trong ndarray.
2. Áp `np.maximum(0,x)` đồng thời lên mọi phần tử.
3. In các giá trị sau kích hoạt.

```python
# Mục đích: Chặn tín hiệu âm bằng ReLU.
import numpy as np

x = np.array([-2, 0, 3, 5])
print(np.maximum(0, x).tolist())
```

**Kết quả khi chạy:**

```text
[0, 0, 3, 5]
```

Hai giá trị âm/0 cho đầu ra 0, hai giá trị dương được giữ.

**Bài thực hành nâng cấp — cấp 1/5:** Đơn vị phân tích ghi **10 tín hiệu đầu vào x (logit, không có đơn vị)**. Hãy áp dụng ReLU để đưa 10 tín hiệu âm về 0. Ở cấp 4–5 có số đo bị thiếu, cần xử lý riêng trước khi tính hoặc chuẩn hóa thay vì dùng nó làm giá trị thật.

```python
import numpy as np
# Mỗi phần tử là một chuyến hàng / một tín hiệu, đơn vị phụ thuộc bài toán.
x = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4],dtype=float)
clean = x[np.isfinite(x)]
result = np.maximum(x,0).round(3).tolist()
print("Số quan sát:",len(x))
print("Kết quả:",result)
```

**Đọc kết quả:** Đã nhận 10 mẫu; chỉ số và đơn vị phải được hiểu trong bài toán hàm kích hoạt; cùng một dữ liệu có thể tạo ra đầu ra khác nhau theo phương pháp.

### Tình huống 2 — Chuyển ba logit bằng sigmoid · Cấp 2: Tính trên toàn bộ dữ liệu

**Tình huống thực tế:** Mô hình phân loại nhị phân có ba điểm thô `[-1,0,1]` của ba quan sát. Cần biến đổi điểm về khoảng (0,1) để so sánh.

**Vì sao chọn cách giải này?** Sigmoid tác động lên từng điểm riêng và cho 0.5 khi logit bằng 0.

**Quy trình giải:**

1. Lưu ba logit dạng float.
2. Áp công thức sigmoid lên mảng.
3. Làm tròn ba chữ số và in.

```python
# Mục đích: Chuyển ba logit bằng sigmoid.
import numpy as np

x = np.array([-1.0, 0.0, 1.0])
print(np.round(1 / (1 + np.exp(-x)), 3).tolist())
```

**Kết quả khi chạy:**

```text
[0.269, 0.5, 0.731]
```

Thứ tự ba quan sát không đổi; điểm sigmoid chưa mặc nhiên được hiệu chuẩn.

**Bài thực hành nâng cấp — cấp 2/5:** Đơn vị phân tích ghi **12 tín hiệu đầu vào x (logit, không có đơn vị)**. Hãy dùng sigmoid đưa 12 logit vào khoảng 0 đến 1. Ở cấp 4–5 có số đo bị thiếu, cần xử lý riêng trước khi tính hoặc chuẩn hóa thay vì dùng nó làm giá trị thật.

```python
import numpy as np
# Mỗi phần tử là một chuyến hàng / một tín hiệu, đơn vị phụ thuộc bài toán.
x = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, -5],dtype=float)
clean = x[np.isfinite(x)]
result = (1/(1+np.exp(-x))).round(3).tolist()
print("Số quan sát:",len(x))
print("Kết quả:",result)
```

**Đọc kết quả:** Đã nhận 12 mẫu; chỉ số và đơn vị phải được hiểu trong bài toán hàm kích hoạt; cùng một dữ liệu có thể tạo ra đầu ra khác nhau theo phương pháp.

### Tình huống 3 — Giữ tín hiệu âm dương bằng tanh · Cấp 3: Kết hợp phi tuyến

**Tình huống thực tế:** Một mạng dùng tín hiệu âm, 0, dương để biểu diễn hướng tác động; đầu vào lần lượt là −1,0,1. Cần đầu ra cân quanh 0.

**Vì sao chọn cách giải này?** Tanh giữ dấu trong khoảng (−1,1), phù hợp hơn sigmoid nếu cần tín hiệu âm.

**Quy trình giải:**

1. Tạo ba tín hiệu số thực.
2. Áp `np.tanh` và làm tròn.
3. In ba giá trị sau biến đổi.

```python
# Mục đích: Giữ tín hiệu âm dương bằng tanh.
import numpy as np

x = np.array([-1.0, 0.0, 1.0])
print(np.round(np.tanh(x), 3).tolist())
```

**Kết quả khi chạy:**

```text
[-0.762, 0.0, 0.762]
```

Tín hiệu âm vẫn âm, dương vẫn dương và giá trị 0 giữ nguyên.

**Bài thực hành nâng cấp — cấp 3/5:** Đơn vị phân tích ghi **15 tín hiệu đầu vào x (logit, không có đơn vị)**. Hãy so tanh giữ dấu trên 15 tín hiệu đầu vào. Ở cấp 4–5 có số đo bị thiếu, cần xử lý riêng trước khi tính hoặc chuẩn hóa thay vì dùng nó làm giá trị thật.

```python
import numpy as np
# Mỗi phần tử là một chuyến hàng / một tín hiệu, đơn vị phụ thuộc bài toán.
x = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, -5, -4, -3, -2],dtype=float)
clean = x[np.isfinite(x)]
result = np.tanh(x).round(3).tolist()
print("Số quan sát:",len(x))
print("Kết quả:",result)
```

**Đọc kết quả:** Đã nhận 15 mẫu; chỉ số và đơn vị phải được hiểu trong bài toán hàm kích hoạt; cùng một dữ liệu có thể tạo ra đầu ra khác nhau theo phương pháp.

### Tình huống 4 — Chuẩn hóa ba điểm phân loại · Cấp 4: Ổn định và dữ liệu thiếu

**Tình huống thực tế:** Một mô hình dự đoán một trong ba loại sản phẩm với logit `[2,1,0.1]`; cần tỷ trọng cho từng lớp sao cho tổng bằng 1.

**Vì sao chọn cách giải này?** Softmax biến toàn bộ bộ logit thành một phân phối, có bước trừ cực đại để tính ổn định.

**Quy trình giải:**

1. Lưu ba logit cho ba lớp loại trừ nhau.
2. Trừ logit lớn nhất rồi tính exp.
3. Chia cho tổng exp, in giá trị đã làm tròn.

```python
# Mục đích: Chuẩn hóa ba điểm phân loại.
import numpy as np

z = np.array([2.0, 1.0, 0.1])
e = np.exp(z - z.max())
prob = e / e.sum()
print(np.round(prob, 3).tolist())
```

**Kết quả khi chạy:**

```text
[0.659, 0.242, 0.099]
```

Lớp đầu nhận điểm lớn nhất. Giá trị làm tròn không được dùng để kiểm tra tổng chính xác tuyệt đối.

**Bài thực hành nâng cấp — cấp 4/5:** Đơn vị phân tích ghi **18 tín hiệu đầu vào x (logit, không có đơn vị)**. Hãy chuẩn hóa 18 logit bằng softmax ổn định số học. Ở cấp 4–5 có số đo bị thiếu, cần xử lý riêng trước khi tính hoặc chuẩn hóa thay vì dùng nó làm giá trị thật.

```python
import numpy as np
# Mỗi phần tử là một chuyến hàng / một tín hiệu, đơn vị phụ thuộc bài toán.
x = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, -5, -4, -3, -2, np.nan, 0, 1],dtype=float)
clean = x[np.isfinite(x)]
result = (np.exp(clean-clean.max())/np.exp(clean-clean.max()).sum()).round(4).tolist()
print("Số quan sát:",len(x))
print("Kết quả:",result)
```

**Đọc kết quả:** Đã nhận 18 mẫu; chỉ số và đơn vị phải được hiểu trong bài toán hàm kích hoạt; cùng một dữ liệu có thể tạo ra đầu ra khác nhau theo phương pháp.

### Tình huống 5 — Ghép hai ReLU thành hàm có khoảng chết · Cấp 5: So sánh nhiều mô hình

**Tình huống thực tế:** Đầu vào x chạy qua −2, −1, 0, 1, 2. Đội nghiên cứu muốn hàm bằng 0 trong đoạn [−1,1] nhưng tăng bên ngoài hai mép.

**Vì sao chọn cách giải này?** Tổng `ReLU(x−1)+ReLU(−x−1)` tạo hàm gấp khúc đối xứng quanh 0.

**Quy trình giải:**

1. Tạo năm điểm x cách đều từ −2 tới 2.
2. Áp hai ReLU lên x−1 và −x−1.
3. Cộng hai kết quả và in dãy.

```python
# Mục đích: Ghép hai ReLU thành hàm có khoảng chết.
import numpy as np

x = np.arange(-2, 3)
y = np.maximum(0, x - 1) + np.maximum(0, -x - 1)
print(y.tolist())
```

**Kết quả khi chạy:**

```text
[1, 0, 0, 0, 1]
```

Hàm có giá trị 0 ở ba điểm giữa và tăng đối xứng ở ngoài khoảng.

**Bài thực hành nâng cấp — cấp 5/5:** Đơn vị phân tích ghi **20 tín hiệu đầu vào x (logit, không có đơn vị)**. Hãy so sánh ReLU, sigmoid, tanh và softmax trên 20 tín hiệu có số đo thiếu. Ở cấp 4–5 có số đo bị thiếu, cần xử lý riêng trước khi tính hoặc chuẩn hóa thay vì dùng nó làm giá trị thật.

```python
import numpy as np
# Mỗi phần tử là một chuyến hàng / một tín hiệu, đơn vị phụ thuộc bài toán.
x = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, -5, -4, -3, -2, np.nan, 0, 1, 2, np.nan],dtype=float)
clean = x[np.isfinite(x)]
result = {'valid':int(np.isfinite(x).sum()),'relu_mean':round(float(np.maximum(clean,0).mean()),3),'sigmoid_mean':round(float((1/(1+np.exp(-clean))).mean()),3),'softmax_sum':round(float((np.exp(clean-clean.max())/np.exp(clean-clean.max()).sum()).sum()),3)}
print("Số quan sát:",len(x))
print("Kết quả:",result)
```

**Đọc kết quả:** Đã nhận 20 mẫu; chỉ số và đơn vị phải được hiểu trong bài toán hàm kích hoạt; cùng một dữ liệu có thể tạo ra đầu ra khác nhau theo phương pháp.

## 6. Sai lầm thường gặp

- ReLU không chặn **giá trị dương lớn**; nó chỉ chặn phần âm.
- Sigmoid nén mỗi giá trị về (0,1), nhưng các giá trị này không tự trở thành xác suất đã hiệu chuẩn.
- Tanh nằm trong (−1,1), còn sigmoid trong (0,1); không thay thế khi cần giữ tín hiệu âm.
- Softmax áp **cùng lúc** lên các logit của nhiều lớp; không áp độc lập từng logit.
- Khi tính softmax nên trừ logit lớn nhất trước `exp` để giảm tràn số.
- Softmax phù hợp các lớp loại trừ nhau; nhiều nhãn có thể đồng thời đúng thường dùng nhiều đầu ra sigmoid thay vì ép tổng một.

## 7. Trắc nghiệm

**Chỉ hỏi kiến thức, phân biệt hàm và cách đọc đầu ra; không hỏi tình huống đánh số.**

**Q1. What is a ReLU activation? | Hàm kích hoạt ReLU là gì?**

A. `max(0,x)` | `max(0,x)`

B. `1/(1+exp(-x))` | `1/(1+exp(-x))`

C. A smooth activation mapping into (−1,1) | Hàm trơn đưa giá trị vào (−1,1)

D. Normalization of several class logits to sum one | Chuẩn hóa nhiều logit lớp có tổng bằng một

**Đáp án: A**

**Giải thích:** ReLU chặn giá trị âm về không.


**Q2. What is sigmoid? | Sigmoid là gì?**

A. `max(0,x)` | `max(0,x)`

B. `1/(1+exp(-x))` | `1/(1+exp(-x))`

C. A smooth activation mapping into (−1,1) | Hàm trơn đưa giá trị vào (−1,1)

D. Normalization of several class logits to sum one | Chuẩn hóa nhiều logit lớp có tổng bằng một

**Đáp án: B**

**Giải thích:** Sigmoid là phép biến đổi logistic hình chữ S.


**Q3. What is tanh? | Tanh là gì?**

A. `max(0,x)` | `max(0,x)`

B. `1/(1+exp(-x))` | `1/(1+exp(-x))`

C. A smooth activation mapping into (−1,1) | Hàm trơn đưa giá trị vào (−1,1)

D. Normalization of several class logits to sum one | Chuẩn hóa nhiều logit lớp có tổng bằng một

**Đáp án: C**

**Giải thích:** Tanh cân quanh 0 và giới hạn giữa −1 và 1.


**Q4. What is softmax? | Softmax là gì?**

A. `max(0,x)` | `max(0,x)`

B. `1/(1+exp(-x))` | `1/(1+exp(-x))`

C. A smooth activation mapping into (−1,1) | Hàm trơn đưa giá trị vào (−1,1)

D. Normalization of several class logits to sum one | Chuẩn hóa nhiều logit lớp có tổng bằng một

**Đáp án: D**

**Giải thích:** Softmax ràng buộc điểm lớp thành một phân phối chuẩn hóa.


**Q5. What is the output range of ReLU? | Đầu ra ReLU thuộc khoảng nào?**

A. From zero upward without a fixed upper bound | Từ không trở lên, không có cận trên cố định

B. Strictly between 0 and 1 | Nằm giữa 0 và 1, không gồm hai đầu

C. Strictly between −1 and 1 | Nằm giữa −1 và 1, không gồm hai đầu

D. They are nonnegative and sum to one | Không âm và có tổng bằng một

**Đáp án: A**

**Giải thích:** Đầu vào dương được ReLU giữ nguyên.


**Q6. What is the output range of sigmoid? | Đầu ra sigmoid thuộc khoảng nào?**

A. From zero upward without a fixed upper bound | Từ không trở lên, không có cận trên cố định

B. Strictly between 0 and 1 | Nằm giữa 0 và 1, không gồm hai đầu

C. Strictly between −1 and 1 | Nằm giữa −1 và 1, không gồm hai đầu

D. They are nonnegative and sum to one | Không âm và có tổng bằng một

**Đáp án: B**

**Giải thích:** Sigmoid với đầu vào hữu hạn nằm trong (0,1).


**Q7. What is the output range of tanh? | Đầu ra tanh thuộc khoảng nào?**

A. From zero upward without a fixed upper bound | Từ không trở lên, không có cận trên cố định

B. Strictly between 0 and 1 | Nằm giữa 0 và 1, không gồm hai đầu

C. Strictly between −1 and 1 | Nằm giữa −1 và 1, không gồm hai đầu

D. They are nonnegative and sum to one | Không âm và có tổng bằng một

**Đáp án: C**

**Giải thích:** Tanh với đầu vào hữu hạn thuộc (−1,1).


**Q8. What is true of softmax class scores? | Điều nào đúng về các điểm softmax?**

A. From zero upward without a fixed upper bound | Từ không trở lên, không có cận trên cố định

B. Strictly between 0 and 1 | Nằm giữa 0 và 1, không gồm hai đầu

C. Strictly between −1 and 1 | Nằm giữa −1 và 1, không gồm hai đầu

D. They are nonnegative and sum to one | Không âm và có tổng bằng một

**Đáp án: D**

**Giải thích:** Softmax chia từng exp cho tổng các exp.


**Q9. Which NumPy function applies ReLU? | Hàm NumPy nào thực hiện ReLU?**

A. `np.maximum(0,x)` | `np.maximum(0,x)`

B. `np.tanh(x)` | `np.tanh(x)`

C. The largest logit | Logit lớn nhất

D. Tanh | Tanh

**Đáp án: A**

**Giải thích:** maximum chặn từng phần tử.


**Q10. Which NumPy function directly computes tanh? | Hàm NumPy nào tính tanh trực tiếp?**

A. `np.maximum(0,x)` | `np.maximum(0,x)`

B. `np.tanh(x)` | `np.tanh(x)`

C. The largest logit | Logit lớn nhất

D. Tanh | Tanh

**Đáp án: B**

**Giải thích:** NumPy có hàm tanh trực tiếp.


**Q11. Which quantity should be subtracted from logits before stable softmax exponentiation? | Nên trừ gì khỏi logit trước khi tính exp softmax ổn định?**

A. `np.maximum(0,x)` | `np.maximum(0,x)`

B. `np.tanh(x)` | `np.tanh(x)`

C. The largest logit | Logit lớn nhất

D. Tanh | Tanh

**Đáp án: C**

**Giải thích:** Trừ cực đại giữ các số exp không vượt một.


**Q12. Which activation outputs exactly 0 at input 0? | Hàm nào trả đúng 0 với đầu vào 0?**

A. `np.maximum(0,x)` | `np.maximum(0,x)`

B. `np.tanh(x)` | `np.tanh(x)`

C. The largest logit | Logit lớn nhất

D. Tanh | Tanh

**Đáp án: D**

**Giải thích:** Tanh(0)=0, còn sigmoid(0)=0.5.


**Q13. What is sigmoid(0)? | sigmoid(0) bằng gì?**

A. 0.5 | 0.5

B. 0 | 0

C. A negative output | Giá trị đầu ra âm

D. It reduces overflow risk without changing the result | Giảm nguy cơ tràn số mà không đổi kết quả

**Đáp án: A**

**Giải thích:** Sigmoid tại zero bằng một nửa.


**Q14. What is ReLU(−2)? | ReLU(−2) bằng gì?**

A. 0.5 | 0.5

B. 0 | 0

C. A negative output | Giá trị đầu ra âm

D. It reduces overflow risk without changing the result | Giảm nguy cơ tràn số mà không đổi kết quả

**Đáp án: B**

**Giải thích:** ReLU chặn đầu vào âm.


**Q15. What does tanh produce for negative input? | Tanh tạo đầu ra thế nào khi đầu vào âm?**

A. 0.5 | 0.5

B. 0 | 0

C. A negative output | Giá trị đầu ra âm

D. It reduces overflow risk without changing the result | Giảm nguy cơ tràn số mà không đổi kết quả

**Đáp án: C**

**Giải thích:** Tanh giữ dấu của đầu vào hữu hạn khác 0.


**Q16. Why does subtracting max(logits) help softmax? | Vì sao trừ cực đại logit giúp softmax?**

A. 0.5 | 0.5

B. 0 | 0

C. A negative output | Giá trị đầu ra âm

D. It reduces overflow risk without changing the result | Giảm nguy cơ tràn số mà không đổi kết quả

**Đáp án: D**

**Giải thích:** Dịch đều các logit không đổi softmax nhưng giảm tràn số.


**Q17. Which output structure suits mutually exclusive multi-class prediction? | Dạng đầu ra nào phù hợp phân loại nhiều lớp loại trừ nhau?**

A. A softmax distribution over classes | Phân phối softmax trên các lớp

B. Their inputs remain in the nonpositive flat region | Đầu vào luôn ở vùng phẳng không dương

C. No, calibration needs checking | Không, cần đánh giá độ hiệu chuẩn

D. Softmax couples scores so they sum to one | Softmax ràng buộc điểm các lớp có tổng một

**Đáp án: A**

**Giải thích:** Softmax thường dùng cho đầu ra các lớp loại trừ nhau.


**Q18. Why might ReLU neurons stop updating? | Vì sao một số nơ-ron ReLU có thể ngừng cập nhật?**

A. A softmax distribution over classes | Phân phối softmax trên các lớp

B. Their inputs remain in the nonpositive flat region | Đầu vào luôn ở vùng phẳng không dương

C. No, calibration needs checking | Không, cần đánh giá độ hiệu chuẩn

D. Softmax couples scores so they sum to one | Softmax ràng buộc điểm các lớp có tổng một

**Đáp án: B**

**Giải thích:** Độ dốc ReLU bằng không ở đầu vào âm.


**Q19. Do sigmoid outputs automatically prove calibrated probabilities? | Đầu ra sigmoid có mặc nhiên là xác suất đã hiệu chuẩn không?**

A. A softmax distribution over classes | Phân phối softmax trên các lớp

B. Their inputs remain in the nonpositive flat region | Đầu vào luôn ở vùng phẳng không dương

C. No, calibration needs checking | Không, cần đánh giá độ hiệu chuẩn

D. Softmax couples scores so they sum to one | Softmax ràng buộc điểm các lớp có tổng một

**Đáp án: C**

**Giải thích:** Điểm số cần kiểm tra với kết quả thực tế.


**Q20. Which difference distinguishes softmax from independent sigmoid outputs? | Điểm nào phân biệt softmax với sigmoid độc lập?**

A. A softmax distribution over classes | Phân phối softmax trên các lớp

B. Their inputs remain in the nonpositive flat region | Đầu vào luôn ở vùng phẳng không dương

C. No, calibration needs checking | Không, cần đánh giá độ hiệu chuẩn

D. Softmax couples scores so they sum to one | Softmax ràng buộc điểm các lớp có tổng một

**Đáp án: D**

**Giải thích:** Các sigmoid độc lập không bắt buộc có tổng bằng một.

## 8. Bài tiếp theo

`Hàm số → Activation → Neural Network → Classification`.
