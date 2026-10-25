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

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Từng bước giảm một loss đơn giản · Cấp 1: Tính loss ban đầu

**Tình huống thực tế:** Một tham số điều khiển mô phỏng w được tối ưu với `L(w)=w²` (loss không đơn vị). Bắt đầu `w=4`, learning rate 0.1, thực hiện 10 lần cập nhật và xem w tiến gần 0 ra sao.

**Vì sao chọn cách giải này?** Với đạo hàm 2w, bước `w←w−0.1×2w` làm giảm độ lớn w mỗi lần trong ví dụ lồi này.

**Quy trình giải:**

1. Đặt w=4 và learning rate 0.1.
2. Lặp 10 lần, mỗi lần lấy gradient=2w rồi trừ bước cập nhật.
3. In w làm tròn bốn chữ số.

```python
# Mục đích: Từng bước giảm một loss đơn giản.
w = 4.0
lr = 0.1
for _ in range(10):
    w = w - lr * 2 * w
print(round(w, 4))
```

**Kết quả khi chạy:**

```text
0.4295
```

Tham số đi từ 4 xuống khoảng 0.4295, tiến gần cực tiểu 0.

**Bài thực hành nâng cấp — cấp 1/5:** Nhóm đào tạo có **10 quan sát** giờ học (`x`, giờ) và điểm kiểm tra (`y`, điểm/100), mô phỏng quan hệ tuyến tính. Hãy tính MSE trước khi cập nhật trọng số. Các cấp sau phải chọn learning rate, so sai số và loại nhãn không đo được trước khi học tham số.

```python
import numpy as np
# Mỗi dòng: x giờ học, y điểm dự báo mục tiêu (điểm/100).
all_x = np.arange(1,11,dtype=float)
all_y = np.array([5, 7, 9, 11, 13, 15, 17, 19, 21, 23],dtype=float)
mask = np.isfinite(all_y)
x, y = all_x[mask], all_y[mask]
def train(rate, epochs):
    w = b = 0.0
    for _ in range(epochs):
        residual = w*x+b-y
        dw = 2*np.mean(x*residual)
        db = 2*np.mean(residual)
        w -= rate*dw
        b -= rate*db
    return w,b,float(np.mean((w*x+b-y)**2))
result = round(float(np.mean((0*x+0-y)**2)),3)
print("Số quan sát:",len(all_x))
print("Kết quả:",result)
```

**Đọc kết quả:** Mẫu đầu vào 10, `MSE` tính trên mẫu hợp lệ. Giá trị của w và b cần được đọc cùng loss cuối; loss giảm không có nghĩa đã dự đoán đúng tuyệt đối.

### Tình huống 2 — Tìm đạo hàm riêng tại một điểm · Cấp 2: Tính đạo hàm riêng

**Tình huống thực tế:** Loss theo hai tham số là `f=x²+3xy+y²`, tại x=1,y=2. Đội kỹ thuật muốn biết chỉ thay đổi x làm loss nhạy thế nào nếu giữ y cố định.

**Vì sao chọn cách giải này?** Lấy đạo hàm riêng theo x rồi thay giá trị hai biến mới đúng ý nghĩa thay một tham số.

**Quy trình giải:**

1. Khai báo biến x,y và biểu thức f.
2. Tính ∂f/∂x bằng `sp.diff(f,x)`.
3. Thay x=1,y=2 và in độ dốc riêng.

```python
# Mục đích: Tìm đạo hàm riêng tại một điểm.
import sympy as sp

x, y = sp.symbols('x y')
f = x ** 2 + 3 * x * y + y ** 2
print(sp.diff(f, x).subs({x: 1, y: 2}))
```

**Kết quả khi chạy:**

```text
8
```

Nếu tăng x rất nhỏ quanh (1,2), loss tăng xấp xỉ 8 lần phần thay đổi x.

**Bài thực hành nâng cấp — cấp 2/5:** Nhóm đào tạo có **12 quan sát** giờ học (`x`, giờ) và điểm kiểm tra (`y`, điểm/100), mô phỏng quan hệ tuyến tính. Hãy tính đồng thời gradient của w và b. Các cấp sau phải chọn learning rate, so sai số và loại nhãn không đo được trước khi học tham số.

```python
import numpy as np
# Mỗi dòng: x giờ học, y điểm dự báo mục tiêu (điểm/100).
all_x = np.arange(1,13,dtype=float)
all_y = np.array([5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27],dtype=float)
mask = np.isfinite(all_y)
x, y = all_x[mask], all_y[mask]
def train(rate, epochs):
    w = b = 0.0
    for _ in range(epochs):
        residual = w*x+b-y
        dw = 2*np.mean(x*residual)
        db = 2*np.mean(residual)
        w -= rate*dw
        b -= rate*db
    return w,b,float(np.mean((w*x+b-y)**2))
result = {'dw':round(float(np.mean(2*x*(0*x-y))),3),'db':round(float(np.mean(2*(0*x-y))),3)}
print("Số quan sát:",len(all_x))
print("Kết quả:",result)
```

**Đọc kết quả:** Mẫu đầu vào 12, `MSE` tính trên mẫu hợp lệ. Giá trị của w và b cần được đọc cùng loss cuối; loss giảm không có nghĩa đã dự đoán đúng tuyệt đối.

### Tình huống 3 — Theo dõi lịch sử loss khi tối ưu · Cấp 3: Thực hiện nhiều epoch

**Tình huống thực tế:** Một tham số mô phỏng khởi đầu w=3 với `L(w)=w²`. Nhóm phát triển muốn ghi loss trước năm lần cập nhật để xem loss có giảm theo từng bước không.

**Vì sao chọn cách giải này?** Ghi loss trong List cho thấy xu hướng hội tụ thay vì chỉ biết giá trị cuối.

**Quy trình giải:**

1. Tạo List `history`, đặt w=3 và lr=0.1.
2. Mỗi vòng thêm `round(w*w,3)` vào lịch sử rồi cập nhật w.
3. In năm số loss theo thứ tự.

```python
# Mục đích: Theo dõi lịch sử loss khi tối ưu.
w = 3.0
history = []
for _ in range(5):
    history.append(round(w ** 2, 3))
    w = w - 0.1 * 2 * w
print(history)
```

**Kết quả khi chạy:**

```text
[9.0, 5.76, 3.686, 2.359, 1.51]
```

Loss giảm dần qua năm giá trị, nhưng kết quả này chỉ phản ánh hàm lồi một biến đang mô phỏng.

**Bài thực hành nâng cấp — cấp 3/5:** Nhóm đào tạo có **15 quan sát** giờ học (`x`, giờ) và điểm kiểm tra (`y`, điểm/100), mô phỏng quan hệ tuyến tính. Hãy chạy 500 epoch và kiểm tra loss giảm. Các cấp sau phải chọn learning rate, so sai số và loại nhãn không đo được trước khi học tham số.

```python
import numpy as np
# Mỗi dòng: x giờ học, y điểm dự báo mục tiêu (điểm/100).
all_x = np.arange(1,16,dtype=float)
all_y = np.array([5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33],dtype=float)
mask = np.isfinite(all_y)
x, y = all_x[mask], all_y[mask]
def train(rate, epochs):
    w = b = 0.0
    for _ in range(epochs):
        residual = w*x+b-y
        dw = 2*np.mean(x*residual)
        db = 2*np.mean(residual)
        w -= rate*dw
        b -= rate*db
    return w,b,float(np.mean((w*x+b-y)**2))
result = {'initial':round(float(np.mean(y**2)),2),'after':round(train(0.003,500)[2],4)}
print("Số quan sát:",len(all_x))
print("Kết quả:",result)
```

**Đọc kết quả:** Mẫu đầu vào 15, `MSE` tính trên mẫu hợp lệ. Giá trị của w và b cần được đọc cùng loss cuối; loss giảm không có nghĩa đã dự đoán đúng tuyệt đối.

### Tình huống 4 — So bước học nhỏ và quá lớn · Cấp 4: So hai learning rate

**Tình huống thực tế:** Một mô hình thử tối ưu `L(w)=w²` từ w=4, chạy 5 bước với hai learning rate 0.1 và 1.1. Cần kiểm tra cả hai có làm loss giảm như nhau không.

**Vì sao chọn cách giải này?** Learning rate 1.1 vượt khoảng ổn định của hàm này, làm tham số đổi dấu và độ lớn tăng.

**Quy trình giải:**

1. Với từng learning rate, đặt lại w=4 để so công bằng.
2. Cập nhật 5 bước bằng gradient 2w.
3. In loss cuối sau làm tròn ba chữ số.

```python
# Mục đích: So bước học nhỏ và quá lớn.
for lr in [0.1, 1.1]:
    w = 4.0
    for _ in range(5):
        w = w - lr * 2 * w
    print(lr, round(w ** 2, 3))
```

**Kết quả khi chạy:**

```text
0.1 1.718
1.1 99.068
```

Với lr 0.1, loss còn 1.718; với lr 1.1 loss tăng lên 99.068 dù cùng điểm khởi đầu.

**Bài thực hành nâng cấp — cấp 4/5:** Nhóm đào tạo có **18 quan sát** giờ học (`x`, giờ) và điểm kiểm tra (`y`, điểm/100), mô phỏng quan hệ tuyến tính. Hãy so loss cuối của hai learning rate trên dữ liệu có số đo thiếu. Các cấp sau phải chọn learning rate, so sai số và loại nhãn không đo được trước khi học tham số.

```python
import numpy as np
# Mỗi dòng: x giờ học, y điểm dự báo mục tiêu (điểm/100).
all_x = np.arange(1,19,dtype=float)
all_y = np.array([5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, np.nan, 37, 39],dtype=float)
mask = np.isfinite(all_y)
x, y = all_x[mask], all_y[mask]
def train(rate, epochs):
    w = b = 0.0
    for _ in range(epochs):
        residual = w*x+b-y
        dw = 2*np.mean(x*residual)
        db = 2*np.mean(residual)
        w -= rate*dw
        b -= rate*db
    return w,b,float(np.mean((w*x+b-y)**2))
result = {'slow':round(train(0.001,120)[2],4),'fast':round(train(0.003,120)[2],4),'missing':int(len(all_y)-len(y))}
print("Số quan sát:",len(all_x))
print("Kết quả:",result)
```

**Đọc kết quả:** Mẫu đầu vào 18, `MSE` tính trên mẫu hợp lệ. Giá trị của w và b cần được đọc cùng loss cuối; loss giảm không có nghĩa đã dự đoán đúng tuyệt đối.

### Tình huống 5 — Fit một hệ số tuyến tính bằng gradient · Cấp 5: Fit và kiểm chứng dự báo

**Tình huống thực tế:** Dữ liệu ba điểm gồm x=`[1,2,3]` và y=`[2,4,6]`. Mô hình không có hệ số chặn, dự báo `ŷ=w*x`. Bắt đầu w=0 và dùng 100 bước cập nhật để khớp hệ số w.

**Vì sao chọn cách giải này?** Đạo hàm MSE theo w là `2×mean(x*(wx−y))`; cập nhật lặp cho hệ số gần 2.

**Quy trình giải:**

1. Tạo mảng x,y theo đúng cặp quan sát.
2. Đặt w=0, lr=0.1, lặp 100 lần để tính gradient MSE và cập nhật.
3. In w làm tròn ba chữ số.

```python
# Mục đích: Fit một hệ số tuyến tính bằng gradient.
import numpy as np

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
w = 0.0
for _ in range(100):
    gradient = 2 * np.mean(x * (w * x - y))
    w = w - 0.1 * gradient
print(round(w, 3))
```

**Kết quả khi chạy:**

```text
2.0
```

Mô hình tìm được hệ số gần 2 cho quan hệ y=2x; chưa có bước đánh giá trên dữ liệu mới.

**Bài thực hành nâng cấp — cấp 5/5:** Nhóm đào tạo có **20 quan sát** giờ học (`x`, giờ) và điểm kiểm tra (`y`, điểm/100), mô phỏng quan hệ tuyến tính. Hãy fit w,b trên 20 dòng, so với nghiệm least squares và lỗi dự đoán. Các cấp sau phải chọn learning rate, so sai số và loại nhãn không đo được trước khi học tham số.

```python
import numpy as np
# Mỗi dòng: x giờ học, y điểm dự báo mục tiêu (điểm/100).
all_x = np.arange(1,21,dtype=float)
all_y = np.array([5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, np.nan, 37, 39, 41, np.nan],dtype=float)
mask = np.isfinite(all_y)
x, y = all_x[mask], all_y[mask]
def train(rate, epochs):
    w = b = 0.0
    for _ in range(epochs):
        residual = w*x+b-y
        dw = 2*np.mean(x*residual)
        db = 2*np.mean(residual)
        w -= rate*dw
        b -= rate*db
    return w,b,float(np.mean((w*x+b-y)**2))
result = {'GD':tuple(round(t,3) for t in train(0.003,1000)[:2]),'LS':np.linalg.lstsq(np.column_stack((x,np.ones_like(x))),y,rcond=None)[0].round(3).tolist(),'loss':round(train(0.003,1000)[2],5)}
print("Số quan sát:",len(all_x))
print("Kết quả:",result)
```

**Đọc kết quả:** Mẫu đầu vào 20, `MSE` tính trên mẫu hợp lệ. Giá trị của w và b cần được đọc cùng loss cuối; loss giảm không có nghĩa đã dự đoán đúng tuyệt đối.

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
