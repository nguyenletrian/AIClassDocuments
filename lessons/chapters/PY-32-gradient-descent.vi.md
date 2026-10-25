# PY-32 — Đạo hàm riêng, gradient descent và learning rate


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Partial derivative** — đạo hàm riêng; **Gradient** — vector gradient.

`Derivative → Gradient → Optimization → Training`

**Học xong dùng để làm gì?** Cập nhật tham số từng bước để giảm loss, phát hiện hiện tượng học quá nhanh gây dao động.

**Kết nối kiến thức tiếp theo:** PY-33 dùng Jacobian/Hessian để xem độ nhạy và độ cong trong bài toán nhiều biến.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| Partial derivative | đạo hàm riêng | Đạo hàm theo một biến khi các biến khác giữ cố định |
| Gradient | vector gradient | Vector gồm các đạo hàm riêng của hàm nhiều biến |
| Learning rate | tốc độ học | Bước nhân gradient khi cập nhật tham số |
| Epoch | vòng huấn luyện | Một lượt sử dụng hết dữ liệu train để cập nhật mô hình |

## 3. Hàm và cách gọi bằng Python

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm / tham số | Giải thích |
|---|---|
| `sympy.diff(f,x)` | Đạo hàm riêng của hàm f theo x |
| `grad=[df/dx,df/dy,...]` | Ghép các đạo hàm riêng thành vector |
| `w = w - lr * gradient` | Cập nhật đi ngược hướng tăng loss |
| `np.mean((pred-y)**2)` | Loss MSE mẫu cho tối ưu hồi quy |

## 4. Khái niệm chính và liên quan

**Mạch kiến thức:** Đạo hàm riêng đo độ dốc theo từng tham số; gradient gom các độ dốc; gradient descent dùng hướng ngược gradient với learning rate thích hợp; epoch nói về số lượt đi qua tập train, không mặc định bằng số bước cập nhật.

### 4.1. Partial derivative — Độ dốc theo một tham số

**Từ vựng:** **Partial derivative** — đạo hàm riêng; **Fixed variable** — biến giữ cố định.

Một mô hình có hai tham số x,y và loss `f(x,y)=x²+3xy+y²`. **Đạo hàm riêng theo x** giả sử y giữ nguyên, được `2x+3y`, còn theo y là `3x+2y`. Ở điểm `(1,2)`, hai độ dốc lần lượt 8 và 7. Đạo hàm riêng khác đạo hàm hàm một biến vì ta phải chỉ rõ **biến đang thay đổi**.

```python
# Mục đích: Độ dốc theo một tham số.
import sympy as sp

x, y = sp.symbols('x y')
f = x ** 2 + 3 * x * y + y ** 2
print(sp.diff(f, x))
```

**Kết quả khi chạy:**

```text
2*x + 3*y
```

Đạo hàm riêng theo x bằng 2x+3y, coi y là hằng số.

### 4.2. Gradient — Tập hợp độ dốc của tất cả tham số

**Từ vựng:** **Gradient** — vector gradient; **Parameter** — tham số mô hình.

Nếu loss phụ thuộc nhiều tham số, **gradient** gom các đạo hàm riêng **theo đúng thứ tự tham số**: `∇f=(∂f/∂x, ∂f/∂y)`. Với `f=x²+y²` tại `(3,4)`, gradient `[6,8]` là vector hai chiều. Gradient chỉ **hướng tăng nhanh nhất cục bộ** của f; đi theo **gradient âm** giúp thử giảm loss khi bước đủ nhỏ.

```python
# Mục đích: Tập hợp độ dốc của tất cả tham số.
import numpy as np

params = np.array([3.0, 4.0])
print((2 * params).tolist())
```

**Kết quả khi chạy:**

```text
[6.0, 8.0]
```

Gradient tại (3,4) có hai thành phần: đạo hàm theo x bằng 6, theo y bằng 8.

### 4.3. Learning rate — Độ dài bước cập nhật

**Từ vựng:** **Learning rate** — tốc độ học; **Update** — cập nhật.

Gradient descent cập nhật tham số bằng `w_new = w − lr × gradient`. Với `L(w)=w²`, ta có đạo hàm `2w`. Bắt đầu w=3 và lr=0.1, gradient=6 nên w mới bằng `3−0.1×6=2.4`. **Learning rate** không phải một đạo hàm; nó quyết định bước đi. Quá lớn có thể dao động/phân kỳ, quá nhỏ có thể rất chậm.

```python
# Mục đích: Độ dài bước cập nhật.
w = 3.0
learning_rate = 0.1
w = w - learning_rate * 2 * w
print(round(w, 2))
```

**Kết quả khi chạy:**

```text
2.4
```

Một bước đi ngược gradient đưa tham số từ 3 xuống 2.4, gần cực tiểu w=0 hơn.

### 4.4. Epoch — Một lượt qua dữ liệu train

**Từ vựng:** **Epoch** — một vòng qua tập train; **Step** — một bước cập nhật.

**Epoch** thường là một lượt xử lý toàn bộ dữ liệu train. Nó **không bằng một bước gradient** trong mọi trường hợp: khi huấn luyện minibatch, một epoch có nhiều batch và nhiều lần cập nhật. Để minh họa vòng lặp, có thể in số thứ tự epoch 1, 2, 3. Với **gradient descent một batch toàn bộ dữ liệu**, mỗi epoch thường tương ứng một lần cập nhật; cách đếm và kiểm tra loss cần nhất quán.

```python
# Mục đích: Một lượt qua dữ liệu train.
for epoch in range(1, 4):
    print(epoch)
```

**Kết quả khi chạy:**

```text
1
2
3
```

Có ba lượt epoch được đánh số 1 đến 3; đây mới là bộ đếm, không phải bản thân việc huấn luyện.

## 5. Năm tình huống Gradient Descent — từ một bước đến hồi quy hai tham số

### Tình huống 1 — Cấp 1: Một bước gradient từ 10 điểm giá trị mục tiêu

**Từ vựng trong mục:** **Gradient** — hướng dốc; **Learning rate** — tốc độ học; **Loss** — mức sai.

**Tình huống thực tế:** Có **10 số mục tiêu** 2–11 (đơn vị điểm) từ 10 lần đo. Một mô hình đơn giản chỉ dự đoán **một hằng số w** cho mọi lượt; bắt đầu từ w=0, cần thử một bước giảm MSE với learning rate 0,1 rồi so loss trước/sau.

**Vì sao chọn cách này?** Đạo hàm MSE theo w là trung bình hai lần sai số; đi **ngược** gradient là bước thử giảm loss. Ví dụ chưa xây mô hình nhiều tham số nên người mới thấy rõ w thay đổi ra sao.

**Quy trình:**
1. Tạo 10 số mục tiêu và đặt w=0.
2. Tính MSE, gradient rồi cập nhật với lr=0,1.
3. So MSE trước/sau và in giá trị w mới.

```python
import numpy as np
targets = np.array([2,3,4,5,6,7,8,9,10,11], dtype=float)
w = 0.0
before = np.mean((w - targets)**2)
gradient = 2 * np.mean(w - targets)
w = w - 0.1 * gradient
after = np.mean((w - targets)**2)
if len(targets) != 10:
    raise ValueError("Cần đúng 10 bản ghi mục tiêu.")
print("Bản ghi:", len(targets))
print(f"Trọng số sau bước: {w:.2f}")
print("Loss giảm:", bool(after < before))
```

**Kết quả khi chạy:**

```text
Bản ghi: 10
Trọng số sau bước: 1.30
Loss giảm: True
```

Một bước chưa đưa w tới giá trị tối ưu, nhưng cho thấy hướng cập nhật làm sai số trên mười điểm giảm.

### Tình huống 2 — Cấp 2: Đạo hàm riêng hệ số từ 12 cặp x/y có chặn cố định

**Từ vựng trong mục:** **Partial derivative** — đạo hàm riêng; **Coefficient** — hệ số; **Full batch** — toàn bộ dữ liệu.

**Tình huống thực tế:** Một dây chuyền có **12 cặp số đo** x/y (x từ 1 đến 12 đơn vị đầu vào). Dữ liệu tạo theo y=2x+1; nhóm biết trước phần chặn 1, nhưng cần học hệ số dốc w từ 0. Để không nhầm gradient với tỷ lệ cố định, hãy tính độ dốc loss **từ cả 12 hàng**, cập nhật một lần và kiểm loss.

**Vì sao chọn cách này?** Giữ chặn bằng 1 rồi chỉ tối ưu w. Gradient MSE là trung bình đóng góp sai số từ cả 12 hàng nhân x; learning rate 0,005 được chọn nhỏ để không bước quá xa khi x lớn.

**Quy trình:**
1. Tạo 12 hàng, dự báo bằng `w*x+1`.
2. Tính đạo hàm loss theo w trên toàn bộ 12 hàng.
3. Cập nhật một bước, xác nhận MSE sau cập nhật nhỏ hơn trước.

```python
import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12], dtype=float)
y = 2*x + 1
w = 0.0
before = np.mean((w*x + 1 - y)**2)
gradient = 2*np.mean((w*x + 1 - y)*x)
w -= 0.005*gradient
after = np.mean((w*x + 1 - y)**2)
if x.shape != (12,) or y.shape != (12,):
    raise ValueError("Cần 12 cặp x và y.")
print("Mẫu:", len(x))
print(f"Gradient ban đầu: {gradient:.2f}")
print(f"Hệ số sau bước: {w:.3f}")
print("Loss giảm:", bool(after < before))
```

**Kết quả khi chạy:**

```text
Mẫu: 12
Gradient ban đầu: -216.67
Hệ số sau bước: 1.083
Loss giảm: True
```

Gradient của w không phải hệ số w: gradient phụ thuộc **tất cả x và sai số dự báo**.

### Tình huống 3 — Cấp 3: Theo dõi 6 bước tối ưu trên 15 mẫu chuẩn hóa

**Từ vựng trong mục:** **Gradient descent** — hạ dốc; **Iteration** — vòng cập nhật; **Loss history** — lịch sử sai số.

**Tình huống thực tế:** Một mô hình dự báo 15 giá trị y từ 15 đầu vào x đã chuẩn hóa vào (0,1], với quy luật minh họa y=2x. Mô hình y=wx bắt đầu w=0. Cần lưu **loss ở từng bước trong 6 bước cập nhật** để biết quá trình có thực sự cải thiện hay không.

**Vì sao chọn cách này?** Dùng MSE và gradient theo một hệ số, cập nhật có learning rate đủ nhỏ. Lưu lịch sử loss giúp không chỉ nhìn giá trị cuối mà còn kiểm tra sai số **giảm qua từng bước**.

**Quy trình:**
1. Chuẩn bị đúng 15 cặp x/y.
2. Lặp sáu lần: đo loss, tính gradient toàn batch rồi cập nhật w.
3. Kiểm lịch sử loss giảm, in bước đầu/cuối và hệ số mới.

```python
import numpy as np
x = np.array([0.06666666666666667,0.13333333333333333,0.2,0.26666666666666666,0.3333333333333333,0.4,0.4666666666666667,0.5333333333333333,0.6,0.6666666666666666,0.7333333333333333,0.8,0.8666666666666667,0.9333333333333333,1], dtype=float)
y = 2*x
w = 0.0
history = []
for step in range(6):
    error = w*x - y
    history.append(float(np.mean(error**2)))
    w -= 0.2*2*np.mean(error*x)
if len(x) != 15 or len(history) != 6:
    raise ValueError("Cần 15 mẫu và 6 bước kiểm tra Loss.")
print("Mẫu:", len(x))
print("Bước cập nhật:", len(history))
print(f"Loss đầu: {history[0]:.3f}")
print(f"Loss bước 6: {history[-1]:.3f}")
decreases = True
for before, after in zip(history, history[1:]):
    if before <= after:
        decreases = False
        break
print("Giảm từng bước:", decreases)
```

**Kết quả khi chạy:**

```text
Mẫu: 15
Bước cập nhật: 6
Loss đầu: 1.470
Loss bước 6: 0.300
Giảm từng bước: True
```

Sáu **bước full-batch** ở đây cũng tương ứng sáu lượt xem toàn bộ 15 mẫu; nếu dùng minibatch, số bước và số epoch có thể khác.

### Tình huống 4 — Cấp 4: So learning rate ổn định và quá lớn trên 18 mục tiêu

**Từ vựng trong mục:** **Learning rate** — độ dài bước; **Overshoot** — bước vượt quá; **Divergence** — phân kỳ.

**Tình huống thực tế:** Máy phân loại giả lập thu **18 điểm mục tiêu** trong khoảng 10–15, mỗi hàng là một lượt. Một mô hình chỉ dự báo hằng w từ 0 được chạy **5 bước** với hai learning rate 0,1 và 1,1 trên cùng dữ liệu. Cần so loss cuối để chứng minh learning rate quá cao có thể **vượt qua điểm tối ưu liên tục** và làm loss tăng.

**Vì sao chọn cách này?** Trên bài toán loss hình bát úp ngược (hình bát úp lên, có cực tiểu), learning rate 0,1 cập nhật tiến về trung bình; 1,1 khiến mỗi bước nhảy qua phía đối diện và biên độ lớn dần. So cùng dữ liệu giúp tách ảnh hưởng của learning rate.

**Quy trình:**
1. Tạo 18 giá trị mục tiêu và MSE cho dự báo hằng w.
2. Chạy hai bản sao 5 bước, chỉ khác learning rate.
3. Báo loss ban đầu, hai loss cuối và kiểm bản tốc độ học lớn bị tăng loss.

```python
import numpy as np
targets = np.array([10,11,12,13,14,15,10,11,12,13,14,15,10,11,12,13,14,15], dtype=float)
def train(lr):
    w = 0.0
    for step in range(5):
        gradient = 2*np.mean(w - targets)
        w -= lr*gradient
    return float(np.mean((w - targets)**2))
initial = float(np.mean(targets**2))
small = train(0.1)
large = train(1.1)
if len(targets) != 18:
    raise ValueError("Cần 18 giá trị mục tiêu khi so learning rate.")
print("Mẫu:", len(targets))
print(f"Loss đầu: {initial:.2f}")
print(f"Loss sau lr=0.1: {small:.2f}")
print(f"Loss sau lr=1.1: {large:.2f}")
print("lr lớn làm loss tăng:", bool(large > initial))
```

**Kết quả khi chạy:**

```text
Mẫu: 18
Loss đầu: 159.17
Loss sau lr=0.1: 19.69
Loss sau lr=1.1: 970.38
lr lớn làm loss tăng: True
```

Learning rate lớn không **luôn** gây phân kỳ, nhưng ở hàm và bước cập nhật cụ thể này, nó khiến quá trình không hội tụ.

### Tình huống 5 — Cấp 5: Huấn luyện hai tham số hồi quy với 20 cặp đo qua 300 epoch

**Từ vựng trong mục:** **Batch gradient** — gradient toàn bộ; **Epoch** — lượt học; **MSE** — sai số bình phương.

**Tình huống thực tế:** Phòng nghiên cứu có **20 cặp đo** x/y: đầu vào từ 0 đến 1,9 (đơn vị đo chuẩn hóa), đầu ra giả lập y=2x+1. Cần học **cả độ dốc w và hệ số chặn b**, ban đầu bằng 0, bằng 300 epoch full-batch; sau đó kiểm tra mô hình gần hai tham số đúng và MSE giảm.

**Vì sao chọn cách này?** Khi tối ưu đồng thời w/b, gradient có hai thành phần theo đúng thứ tự tham số. Bước full-batch dùng toàn bộ 20 mẫu; 300 epoch chỉ là số lượt thử trong ví dụ, không khẳng định mọi mô hình đều cần số epoch này.

**Quy trình:**
1. Tạo 20 mẫu (x,y) và đặt w=b=0.
2. Trong mỗi epoch, tính lỗi 20 hàng, gradient cho w và b, cập nhật cùng learning rate 0,1.
3. So loss đầu/cuối, in hai tham số cuối và xác nhận MSE giảm.

```python
import numpy as np
x = np.array([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9], dtype=float)
y = 2*x + 1
w, b = 0.0, 0.0
initial = float(np.mean((w*x+b-y)**2))
for epoch in range(300):
    error = w*x+b-y
    dw = 2*np.mean(error*x)
    db = 2*np.mean(error)
    w -= 0.1*dw
    b -= 0.1*db
mse = float(np.mean((w*x+b-y)**2))
if x.size != 20:
    raise ValueError("Cần đủ 20 điểm train.")
print("Mẫu:", len(x))
print("Epoch:", 300)
print(f"Trọng số w: {w:.2f}")
print(f"Chặn b: {b:.2f}")
print(f"MSE cuối: {mse:.6f}")
print("MSE giảm:", mse < initial)
```

**Kết quả khi chạy:**

```text
Mẫu: 20
Epoch: 300
Trọng số w: 2.00
Chặn b: 1.00
MSE cuối: 0.000000
MSE giảm: True
```

Vì dữ liệu được tạo đúng theo đường thẳng, hồi quy có thể đạt MSE rất nhỏ. Với dữ liệu thực có nhiễu phải đánh giá trên tập chưa dùng để học.

## 6. Sai lầm thường gặp

- Đạo hàm riêng chỉ thay một tham số; gradient chứa nhiều đạo hàm riêng theo đúng thứ tự tham số.
- Gradient chỉ hướng **tăng nhanh nhất**, nên gradient descent thường trừ gradient.
- Learning rate quá lớn có thể phân kỳ; quá nhỏ khiến học chậm.
- Một epoch không luôn tương ứng một lần cập nhật vì minibatch có nhiều bước.
- Ghi loss giúp theo dõi tiến triển nhưng loss train giảm chưa bảo đảm kết quả validation tốt.
- Khi tính MSE theo dữ liệu, phải ghép đúng từng mẫu x với nhãn y.

## 7. Trắc nghiệm

**Q1. What is a partial derivative? | Đạo hàm riêng là gì?**

A. Change rate in one variable while others are held fixed | Tốc độ thay đổi theo một biến khi giữ các biến khác cố định

B. A vector of partial derivatives | Vector gồm các đạo hàm riêng

C. A factor controlling an optimization update step | Hệ số điều khiển độ lớn bước cập nhật tối ưu

D. One pass through the training dataset | Một lượt đi qua tập dữ liệu train

**Đáp án: A**

**Giải thích:** Chỉ thay một biến và giữ biến khác cố định.


**Q2. What is a gradient? | Gradient là gì?**

A. Change rate in one variable while others are held fixed | Tốc độ thay đổi theo một biến khi giữ các biến khác cố định

B. A vector of partial derivatives | Vector gồm các đạo hàm riêng

C. A factor controlling an optimization update step | Hệ số điều khiển độ lớn bước cập nhật tối ưu

D. One pass through the training dataset | Một lượt đi qua tập dữ liệu train

**Đáp án: B**

**Giải thích:** Các đạo hàm riêng hợp thành một vector.


**Q3. What is a learning rate? | Learning rate là gì?**

A. Change rate in one variable while others are held fixed | Tốc độ thay đổi theo một biến khi giữ các biến khác cố định

B. A vector of partial derivatives | Vector gồm các đạo hàm riêng

C. A factor controlling an optimization update step | Hệ số điều khiển độ lớn bước cập nhật tối ưu

D. One pass through the training dataset | Một lượt đi qua tập dữ liệu train

**Đáp án: C**

**Giải thích:** Nó nhân mức độ cập nhật.


**Q4. What is an epoch in training? | Epoch trong huấn luyện là gì?**

A. Change rate in one variable while others are held fixed | Tốc độ thay đổi theo một biến khi giữ các biến khác cố định

B. A vector of partial derivatives | Vector gồm các đạo hàm riêng

C. A factor controlling an optimization update step | Hệ số điều khiển độ lớn bước cập nhật tối ưu

D. One pass through the training dataset | Một lượt đi qua tập dữ liệu train

**Đáp án: D**

**Giải thích:** Một epoch xử lý hết dữ liệu train một lượt.


**Q5. Which tool differentiates f with respect to x symbolically? | Hàm nào đạo hàm ký hiệu f theo x?**

A. `sp.diff(f,x)` | `sp.diff(f,x)`

B. `w = w - lr*gradient` | `w = w - lr*gradient`

C. `np.mean((pred-y)**2)` | `np.mean((pred-y)**2)`

D. A `for` loop | Vòng lặp `for`

**Đáp án: A**

**Giải thích:** diff tính đạo hàm ký hiệu.


**Q6. Which expression is a gradient-descent update? | Biểu thức nào cập nhật theo gradient descent?**

A. `sp.diff(f,x)` | `sp.diff(f,x)`

B. `w = w - lr*gradient` | `w = w - lr*gradient`

C. `np.mean((pred-y)**2)` | `np.mean((pred-y)**2)`

D. A `for` loop | Vòng lặp `for`

**Đáp án: B**

**Giải thích:** Trừ gradient nhằm giảm loss cục bộ.


**Q7. Which formula is MSE? | Công thức nào là MSE?**

A. `sp.diff(f,x)` | `sp.diff(f,x)`

B. `w = w - lr*gradient` | `w = w - lr*gradient`

C. `np.mean((pred-y)**2)` | `np.mean((pred-y)**2)`

D. A `for` loop | Vòng lặp `for`

**Đáp án: C**

**Giải thích:** MSE trung bình bình phương sai số.


**Q8. Which Python construct repeats optimization steps? | Cấu trúc Python nào lặp các bước tối ưu?**

A. `sp.diff(f,x)` | `sp.diff(f,x)`

B. `w = w - lr*gradient` | `w = w - lr*gradient`

C. `np.mean((pred-y)**2)` | `np.mean((pred-y)**2)`

D. A `for` loop | Vòng lặp `for`

**Đáp án: D**

**Giải thích:** for lặp các bước cập nhật.


**Q9. What is ∂(x²+3xy)/∂x? | Đạo hàm riêng theo x của x²+3xy là gì?**

A. `2*x+3*y` | `2*x+3*y`

B. `[2*x,2*y]` | `[2*x,2*y]`

C. `2*w` | `2*w`

D. 2.4 | 2.4

**Đáp án: A**

**Giải thích:** Lấy đạo hàm x² và xy theo x.


**Q10. What is the gradient of x²+y²? | Gradient của x²+y² là gì?**

A. `2*x+3*y` | `2*x+3*y`

B. `[2*x,2*y]` | `[2*x,2*y]`

C. `2*w` | `2*w`

D. 2.4 | 2.4

**Đáp án: B**

**Giải thích:** Mỗi đạo hàm bằng hai lần tọa độ.


**Q11. For loss w², what is its derivative? | Đạo hàm loss w² là gì?**

A. `2*x+3*y` | `2*x+3*y`

B. `[2*x,2*y]` | `[2*x,2*y]`

C. `2*w` | `2*w`

D. 2.4 | 2.4

**Đáp án: C**

**Giải thích:** Dùng quy tắc lũy thừa cho w².


**Q12. If w=3, lr=0.1 and grad=6, what is next w? | Nếu w=3, lr=0.1 và gradient=6, w mới là gì?**

A. `2*x+3*y` | `2*x+3*y`

B. `[2*x,2*y]` | `[2*x,2*y]`

C. `2*w` | `2*w`

D. 2.4 | 2.4

**Đáp án: D**

**Giải thích:** 3−0.1×6=2.4.


**Q13. Why might a large learning rate fail? | Vì sao learning rate lớn dễ thất bại?**

A. Updates can overshoot or diverge | Bước cập nhật có thể vượt cực tiểu hoặc phân kỳ

B. It can make convergence slow | Nó có thể làm hội tụ chậm

C. Locally reduce the objective | Giảm hàm mục tiêu về mặt cục bộ

D. No, minibatches can cause multiple updates | Không, nhiều minibatch có thể tạo nhiều lần cập nhật

**Đáp án: A**

**Giải thích:** Bước lớn có thể vượt qua cực tiểu liên tục.


**Q14. Why might a very small learning rate be inefficient? | Vì sao learning rate quá nhỏ kém hiệu quả?**

A. Updates can overshoot or diverge | Bước cập nhật có thể vượt cực tiểu hoặc phân kỳ

B. It can make convergence slow | Nó có thể làm hội tụ chậm

C. Locally reduce the objective | Giảm hàm mục tiêu về mặt cục bộ

D. No, minibatches can cause multiple updates | Không, nhiều minibatch có thể tạo nhiều lần cập nhật

**Đáp án: B**

**Giải thích:** Bước quá nhỏ khiến tối ưu chậm.


**Q15. What does moving opposite the gradient aim to do? | Đi ngược gradient nhằm làm gì?**

A. Updates can overshoot or diverge | Bước cập nhật có thể vượt cực tiểu hoặc phân kỳ

B. It can make convergence slow | Nó có thể làm hội tụ chậm

C. Locally reduce the objective | Giảm hàm mục tiêu về mặt cục bộ

D. No, minibatches can cause multiple updates | Không, nhiều minibatch có thể tạo nhiều lần cập nhật

**Đáp án: C**

**Giải thích:** Gradient âm là hướng giảm với bước đủ nhỏ.


**Q16. Does one epoch always equal one update? | Một epoch luôn bằng một lần cập nhật không?**

A. Updates can overshoot or diverge | Bước cập nhật có thể vượt cực tiểu hoặc phân kỳ

B. It can make convergence slow | Nó có thể làm hội tụ chậm

C. Locally reduce the objective | Giảm hàm mục tiêu về mặt cục bộ

D. No, minibatches can cause multiple updates | Không, nhiều minibatch có thể tạo nhiều lần cập nhật

**Đáp án: D**

**Giải thích:** Một epoch có thể gồm nhiều batch.


**Q17. Why record loss history? | Vì sao lưu lịch sử loss?**

A. To inspect optimization progress | Để xem tiến trình tối ưu

B. Each error must use its correct sample | Mỗi sai số cần đúng cặp quan sát

C. No, generalization needs validation | Không, cần kiểm chứng trên dữ liệu mới

D. Steepest increase | Hướng tăng nhanh nhất

**Đáp án: A**

**Giải thích:** Lịch sử cho thấy xu hướng giảm hoặc bất ổn.


**Q18. Why pair features and targets in the same order? | Vì sao cần ghép x và y cùng thứ tự?**

A. To inspect optimization progress | Để xem tiến trình tối ưu

B. Each error must use its correct sample | Mỗi sai số cần đúng cặp quan sát

C. No, generalization needs validation | Không, cần kiểm chứng trên dữ liệu mới

D. Steepest increase | Hướng tăng nhanh nhất

**Đáp án: B**

**Giải thích:** Hàng ghép sai làm sai số vô nghĩa.


**Q19. Does falling training loss guarantee test accuracy? | Loss train giảm có đảm bảo độ chính xác test?**

A. To inspect optimization progress | Để xem tiến trình tối ưu

B. Each error must use its correct sample | Mỗi sai số cần đúng cặp quan sát

C. No, generalization needs validation | Không, cần kiểm chứng trên dữ liệu mới

D. Steepest increase | Hướng tăng nhanh nhất

**Đáp án: C**

**Giải thích:** Cần dữ liệu độc lập để đo tổng quát hóa.


**Q20. Which direction does a gradient point locally? | Gradient hướng theo phía nào về mặt cục bộ?**

A. To inspect optimization progress | Để xem tiến trình tối ưu

B. Each error must use its correct sample | Mỗi sai số cần đúng cặp quan sát

C. No, generalization needs validation | Không, cần kiểm chứng trên dữ liệu mới

D. Steepest increase | Hướng tăng nhanh nhất

**Đáp án: D**

**Giải thích:** Gradient hướng tăng cục bộ nhanh nhất.

## 8. Bài tiếp theo

`Derivative → Gradient → Optimization → Training`.
