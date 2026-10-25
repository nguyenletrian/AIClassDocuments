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
# Mục đích: Tìm đạo hàm riêng của hàm có hai tham số, chỉ xét thay đổi theo x.
# Dữ liệu: f=x²+3xy+y²; x và y là hai biến độc lập, tính đạo hàm theo x khi y được giữ cố định.
# SymPy tính đạo hàm biểu thức có nhiều biến bằng ký hiệu.
import sympy as sp

# Tạo hai biến x, y tượng trưng; có thể đạo hàm theo một biến trong khi giữ biến kia.
x, y = sp.symbols('x y')
# Biểu thức có phần x², tương tác xy và y².
f = x ** 2 + 3 * x * y + y ** 2
# diff(f,x) tính ĐẠO HÀM RIÊNG theo x, xem y như hằng số; kết quả 2x+3y, không phải đạo hàm theo cả hai.
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
# Mục đích: Tính gradient của tổng bình phương hai tham số qua phép toán vector hóa.
# Dữ liệu: Tham số [3,4], hàm mục tiêu ngầm f=w1²+w2², gradient là hai đạo hàm riêng.
# NumPy cho tính trực tiếp theo từng phần tử của vector.
import numpy as np

# Vector hai tham số w1=3, w2=4, dtype float.
params = np.array([3.0, 4.0])
# Với loss là tổng bình phương tham số, gradient là 2*w ở từng thành phần, không phải một độ dốc scalar.
# tolist() chuyển ndarray gradient thành list Python [6,8] để hiển thị.
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
# Mục đích: Thực hiện một bước gradient descent với learning rate 0.1 trên hàm w².
# Dữ liệu: Trọng số w=3 ban đầu, độ dốc là 2w; learning_rate=0.1 là độ lớn bước đi theo hướng giảm.
# w là một tham số cần tối ưu, ban đầu bằng 3.
w = 3.0
# Tốc độ học 0.1 nhân với gradient để quyết định kích thước mỗi bước; quá lớn có thể vượt điểm tối ưu.
learning_rate = 0.1
# Đạo hàm w² là 2w; lấy w trừ learning_rate×gradient để đi NGƯỢC chiều tăng loss.
w = w - learning_rate * 2 * w
# round(...,2) làm tròn trọng số mới để in, không phải số epoch hoặc loss.
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
# Mục đích: Minh họa epoch là một vòng huấn luyện qua dữ liệu, bằng ba lần đếm.
# Dữ liệu: Ba epoch đánh số 1..3; ví dụ chỉ in thứ tự, chưa thật sự fit mô hình.
# range(start,stop) sinh 1,2,3; cận cuối 4 bị loại.
# Mỗi vòng tượng trưng một epoch, tức một lượt học trọn bộ train trong ứng dụng thật.
for epoch in range(1, 4):
    # Ở đây chỉ hiển thị số epoch, không có bước cập nhật mô hình hay dữ liệu train.
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

**Tình huống thực tế:** Một công cụ dự báo nhận **10 điểm mục tiêu từ 2 đến 11**, mỗi điểm đại diện một lượt đo giả lập. Công cụ đang quá đơn giản: nó trả **cùng một số w cho tất cả 10 lượt**, ban đầu w = 0. Người học muốn thử **một lần điều chỉnh w** để dự báo đỡ lệch hơn, rồi so **MSE trước và sau**, chứ không thay đổi từng điểm đo.

**Vì sao chọn cách này?** **Loss (mất mát)** đo mức mô hình đoán lệch so với điểm mục tiêu; **MSE** lấy trung bình những sai lệch đã bình phương nên các lần sai nhiều bị phạt nặng hơn. **Gradient** nói cho ta biết khi thay đổi w rất ít thì loss có xu hướng tăng theo phía nào. Chương trình tính gradient từ **đủ 10 mục tiêu**, sau đó bước **ngược hướng gradient** để thử giảm sai số. **Learning rate 0,1** quyết định độ lớn bước sửa, không phải 10% số điểm đo; sau đúng một bước, tính lại MSE để kiểm chứng, không mặc định hễ cập nhật là tốt hơn.

**Quy trình:**
1. Tạo 10 số mục tiêu và đặt w=0.
2. Tính MSE, gradient rồi cập nhật với lr=0,1.
3. So MSE trước/sau và in giá trị w mới.

```python
# Mục đích: Giảm MSE dự đoán một hằng w trên 10 mục tiêu bằng một bước gradient.
# Dữ liệu: 10 số mục tiêu 2..11, w khởi tạo 0; hàm loss là trung bình bình phương (w-target).
# NumPy vector hóa hiệu dự đoán và mục tiêu cho toàn bộ train.
import numpy as np
# Mảng 10 mục tiêu số thực, một giá trị trên mỗi bản ghi.
targets = np.array([2,3,4,5,6,7,8,9,10,11], dtype=float)
# Khởi tạo dự đoán hằng cho mọi mẫu bằng 0 trước học.
w = 0.0
# Trừ w cho từng target, **2 bình phương và mean() lấy MSE ban đầu.
before = np.mean((w - targets)**2)
# Gradient theo tham số hằng w của MSE bằng hai lần trung bình sai lệch; không dùng độ lệch tuyệt đối.
gradient = 2 * np.mean(w - targets)
# Cập nhật w ngược chiều gradient với learning rate=0.1, chỉ MỘT bước.
w = w - 0.1 * gradient
# Trừ w cho từng target, **2 bình phương và mean() lấy MSE ban đầu.
# Tính lại MSE với w mới để so sau bước cập nhật.
after = np.mean((w - targets)**2)
# len() xác minh đủ 10 mẫu huấn luyện.
if len(targets) != 10:
    # raise ValueError dừng khi số mẫu hoặc số lần cập nhật không đúng điều kiện kiểm tra.
    raise ValueError("Cần đúng 10 bản ghi mục tiêu.")
print("Bản ghi:", len(targets))
print(f"Trọng số sau bước: {w:.2f}")
# So loss sau với trước; bool() đưa kết quả NumPy thành Boolean Python.
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

**Tình huống thực tế:** Trạm thử nghiệm có **12 cặp x và y**, x là mức đầu vào từ **1 đến 12**, y là chỉ số kết quả được tạo theo đường thẳng có **mức nền 1** và phần tăng phụ thuộc x. Mô hình đã biết mức nền nhưng chưa biết **mức tăng cho một đơn vị x**, gọi là w, nên bắt đầu thử w = 0. Nhóm muốn dùng **cả 12 cặp** để điều chỉnh w một lần và kiểm tra xem mức sai lệch trung bình có giảm không.

**Vì sao chọn cách này?** Với mô hình đường thẳng này, mức nền **1 đã cố định**, chỉ còn phải học **độ dốc w**. Khi dự báo của mẫu x còn thấp hơn y, mẫu có x lớn cũng ảnh hưởng mạnh hơn tới việc phải chỉnh w; vì vậy gradient tính từ **sai lệch của từng hàng nhân với x**, rồi lấy trung bình 12 mẫu. `w -= 0.005 * gradient` nghĩa là chỉnh w **ngược hướng loss tăng**, với bước khá nhỏ vì x lên tới 12. Cập nhật bằng cách chỉ lấy sai số của một mẫu sẽ không đại diện cho đủ dữ liệu; ngược lại bước quá lớn có thể vượt qua mức phù hợp.

**Quy trình:**
1. Tạo 12 hàng, dự báo bằng `w*x+1`.
2. Tính đạo hàm loss theo w trên toàn bộ 12 hàng.
3. Cập nhật một bước, xác nhận MSE sau cập nhật nhỏ hơn trước.

```python
# Mục đích: Điều chỉnh hệ số dốc w của mô hình y≈w*x+1 bằng một bước gradient trên 12 mẫu.
# Dữ liệu: 12 đầu vào x=1..12, nhãn y=2x+1; chặn b=1 đã cố định, chỉ cần học w.
# NumPy hỗ trợ lấy mean của lỗi theo 12 mẫu.
import numpy as np
# 12 đặc trưng x số thực tương ứng với từng nhãn y.
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12], dtype=float)
# Tạo nhãn giả lập đúng từ đường thẳng độ dốc 2, chặn 1.
y = 2*x + 1
# w khởi tạo 0, trong khi hệ số thực là 2.
w = 0.0
# MSE của dự đoán w*x+1 so với y, dùng lỗi theo từng hàng.
before = np.mean((w*x + 1 - y)**2)
# Gradient MSE theo w: sai lệch nhân thêm x (vì dự đoán phụ thuộc w qua w*x), rồi mean×2.
gradient = 2*np.mean((w*x + 1 - y)*x)
# -= là gán w mới bằng w cũ trừ learning rate 0.005 nhân gradient; tốc độ nhỏ vì x có thể lớn.
w -= 0.005*gradient
# MSE của dự đoán w*x+1 so với y, dùng lỗi theo từng hàng.
# Tính lại MSE sau cập nhật để xem một bước có giảm lỗi không.
after = np.mean((w*x + 1 - y)**2)
# shape (12,) bảo đảm cả x và y có 12 mẫu khớp vị trí.
if x.shape != (12,) or y.shape != (12,):
    # raise ValueError dừng khi số mẫu hoặc số lần cập nhật không đúng điều kiện kiểm tra.
    raise ValueError("Cần 12 cặp x và y.")
print("Mẫu:", len(x))
# f-string :.2f định dạng gradient hai số thập phân.
print(f"Gradient ban đầu: {gradient:.2f}")
# f-string :.3f định dạng trọng số mới ba số thập phân.
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

**Tình huống thực tế:** Mô hình được giao **15 mẫu đầu vào x đã đưa về khoảng 0 đến 1**, mỗi mẫu có mục tiêu y đúng bằng hai lần x. Ban đầu mô hình dự báo theo quy tắc nhân x với hệ số **w = 0**, nên kết quả thấp hơn mục tiêu. Người học sẽ điều chỉnh w theo **6 bước học**, ghi lại mức mất mát tại mỗi bước và kiểm tra các mức ghi được có giảm dần hay không, thay vì chỉ nhìn hệ số cuối.

**Vì sao chọn cách này?** **Gradient descent (giảm dần theo gradient)** là quá trình thử sửa tham số theo hướng làm sai số nhỏ đi, rồi đo lại nhiều lần. Chương trình tính sai lệch của **15 mẫu**, ghi MSE vào `history`, tính gradient và mới chỉnh w cho lượt kế. Như vậy `history` chứa **6 lần đo loss trước mỗi lần cập nhật**, không phải sáu giá trị đều đo sau bước chỉnh tương ứng. Dùng vòng `for` giúp lặp cùng quy trình; so các số trong `history` theo thứ tự để phát hiện loss không giảm. Việc chọn learning rate **0,2** chỉ phù hợp với ví dụ đầu vào đã chuẩn hóa này, không phải mức tốt cho mọi bài toán.

**Quy trình:**
1. Chuẩn bị đúng 15 cặp x/y.
2. Lặp sáu lần: đo loss, tính gradient toàn batch rồi cập nhật w.
3. Kiểm lịch sử loss giảm, in bước đầu/cuối và hệ số mới.

```python
# Mục đích: Theo dõi 6 giá trị MSE trong quá trình học trọng số trên 15 điểm của y=2x.
# Dữ liệu: 15 x trong (0,1], nhãn y=2x; w từ 0, learning rate 0.2 và 6 lần cập nhật.
# NumPy thực hiện vector hóa tính dự đoán/lỗi cho cả 15 mẫu.
import numpy as np
# 15 đầu vào x từ 1/15 đến 1 (số thực), giúp mức gradient vừa phải.
x = np.array([0.06666666666666667,0.13333333333333333,0.2,0.26666666666666666,0.3333333333333333,0.4,0.4666666666666667,0.5333333333333333,0.6,0.6666666666666666,0.7333333333333333,0.8,0.8666666666666667,0.9333333333333333,1], dtype=float)
# Nhãn đích là đường thẳng hệ số thực 2, không có chặn.
y = 2*x
# Trọng số dự đoán ban đầu bằng 0.
w = 0.0
# List lưu loss TRƯỚC mỗi bước cập nhật, tương ứng 6 lần kiểm.
history = []
# range(6) có 6 lượt step=0..5, không lấy 6.
for step in range(6):
    # Dự đoán vector w*x trừ nhãn y để được sai số từng mẫu.
    error = w*x - y
    # **2 bình phương lỗi rồi mean() tính MSE tại w hiện tại.
    # float() đổi NumPy scalar loss thành số Python; append() lưu trước khi đổi w.
    history.append(float(np.mean(error**2)))
    # Gradient theo w là 2×mean(error*x); -= cập nhật ngược chiều với learning rate=0.2.
    w -= 0.2*2*np.mean(error*x)
# Kiểm đúng 15 mẫu và 6 bản ghi loss.
if len(x) != 15 or len(history) != 6:
    # raise ValueError dừng khi số mẫu hoặc số lần cập nhật không đúng điều kiện kiểm tra.
    raise ValueError("Cần 15 mẫu và 6 bước kiểm tra Loss.")
print("Mẫu:", len(x))
print("Bước cập nhật:", len(history))
# [0] là loss trước bước 1, [-1] loss ngay TRƯỚC bước 6 (không phải loss sau bước 6).
print(f"Loss đầu: {history[0]:.3f}")
print(f"Loss bước 6: {history[-1]:.3f}")
decreases = True
# Ghép từng loss với loss tiếp theo nhờ [1:] bỏ mục đầu để so mức giảm.
for before, after in zip(history, history[1:]):
    # Nếu loss mới không nhỏ hơn loss trước, đặt cờ False và break sớm.
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

**Tình huống thực tế:** Một hệ thống dự đoán **một số chung w** cho **18 điểm mục tiêu từ 10 đến 15** (mỗi giá trị xuất hiện ba lần). Nhóm muốn xem vì sao chọn mức học **0,1** có thể cải thiện sau **5 lần cập nhật**, còn mức học quá lớn **1,1** có thể khiến dự đoán liên tục nhảy qua mức phù hợp và càng sai. Cả hai phép thử phải bắt đầu cùng w = 0 và dùng đúng 18 điểm để so sánh công bằng.

**Vì sao chọn cách này?** **Learning rate** là độ lớn mỗi lần chỉnh tham số. Với loss dạng **chiếc bát hướng lên**, đáy bát là vị trí dự báo chung w khiến sai số nhỏ nhất. Learning rate **0,1** đưa w tiến dần về vùng đáy, còn **1,1** lớn quá làm nó nhảy từ phía này qua phía kia của đáy với biên độ tăng; sau 5 bước MSE có thể **cao hơn cả ban đầu**. Hàm `train(lr)` cho hai lần chạy cùng **18 mục tiêu** và cùng xuất phát w = 0, chỉ đổi learning rate để thấy rõ nguyên nhân. Không phải mọi learning rate lớn đều sai; vấn đề là **lớn so với độ cong của loss**.

**Quy trình:**
1. Tạo 18 giá trị mục tiêu và MSE cho dự báo hằng w.
2. Chạy hai bản sao 5 bước, chỉ khác learning rate.
3. Báo loss ban đầu, hai loss cuối và kiểm bản tốc độ học lớn bị tăng loss.

```python
# Mục đích: So learning rate nhỏ 0.1 với quá lớn 1.1 khi fit 18 mục tiêu bằng một tham số hằng.
# Dữ liệu: 18 mục tiêu số thực 10..15 lặp ba lần, mỗi thử nghiệm học 5 bước từ w=0.
# NumPy hỗ trợ MSE và gradient trung bình.
import numpy as np
# 18 mục tiêu cùng đơn vị giả lập, dùng chung cho hai tốc độ học.
targets = np.array([10,11,12,13,14,15,10,11,12,13,14,15,10,11,12,13,14,15], dtype=float)
# Định nghĩa hàm thử nghiệm nhận learning rate lr, trả loss sau 5 bước, mỗi lần khởi động w=0.
def train(lr):
    # Khởi tạo w lại trong hàm để so hai lr công bằng.
    w = 0.0
    # Năm lượt cập nhật liên tục, không tạo dữ liệu mới.
    for step in range(5):
        # Gradient của trung bình bình phương sai lệch theo hằng w; còn dấu cho biết chiều giảm.
        gradient = 2*np.mean(w - targets)
        # Learning rate nhân độ dốc rồi trừ; với lr=1.1, bước có thể vượt qua điểm tối ưu và dao động tăng.
        w -= lr*gradient
    # Hàm train trả MSE cuối dưới dạng float Python.
    return float(np.mean((w - targets)**2))
# Vì w=0, MSE trước học bằng mean(target²); dùng làm mốc ban đầu.
initial = float(np.mean(targets**2))
# Chạy năm bước với lr nhỏ, thường giảm dần loss.
small = train(0.1)
# Chạy từ đầu với lr=1.1; lớn hơn ngưỡng ổn định cho bài toán hằng w, có thể làm loss tăng.
large = train(1.1)
if len(targets) != 18:
    # raise ValueError dừng khi số mẫu hoặc số lần cập nhật không đúng điều kiện kiểm tra.
    raise ValueError("Cần 18 giá trị mục tiêu khi so learning rate.")
print("Mẫu:", len(targets))
print(f"Loss đầu: {initial:.2f}")
print(f"Loss sau lr=0.1: {small:.2f}")
print(f"Loss sau lr=1.1: {large:.2f}")
# Cờ True báo loss lr lớn vượt loss trước học, không phải cứ lr lớn luôn xấu với mọi bài toán.
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

**Tình huống thực tế:** Nhóm nghiên cứu có **20 cặp đầu vào–đầu ra**, x từ **0 đến 1,9** và y được tạo theo quy tắc đường thẳng có **độ dốc 2, mức nền 1**. Mô hình ban đầu không biết cả hai thông số **w** (độ dốc) và **b** (mức nền), đều khởi đầu 0. Nhóm muốn cập nhật hai thông số bằng **300 epoch**, mỗi epoch sử dụng cả **20 mẫu**, rồi xem w, b có gần giá trị tạo dữ liệu và MSE có thấp hơn ban đầu không.

**Vì sao chọn cách này?** Ở đây **w** quy định mức y tăng khi x tăng, còn **b** là y dự báo khi x = 0. Nếu chỉ học w mà cố định b = 0, mô hình sẽ không diễn tả đúng dữ liệu có mức nền 1. Trong mỗi **epoch**, chương trình dùng cả **20 dòng** để tính hai gradient riêng `dw`, `db`, sau đó sửa **cả hai tham số** bằng learning rate 0,1. **Full-batch** nghĩa là mỗi epoch xét toàn bộ mẫu, không phải lấy một mẫu bất kỳ. Chạy **300 epoch** chỉ là thiết lập cho bài minh họa đã biết dữ liệu; phải xem **w, b cuối và MSE** mới kết luận mô hình đã học gần quy tắc tạo dữ liệu, không lấy số epoch làm bằng chứng tự thân.

**Quy trình:**
1. Tạo 20 mẫu (x,y) và đặt w=b=0.
2. Trong mỗi epoch, tính lỗi 20 hàng, gradient cho w và b, cập nhật cùng learning rate 0,1.
3. So loss đầu/cuối, in hai tham số cuối và xác nhận MSE giảm.

```python
# Mục đích: Huấn luyện hai tham số w,b qua 300 epoch để khớp đường y=2x+1 trên 20 mẫu.
# Dữ liệu: 20 đầu vào x=0..1.9, y=2x+1; tham số w,b đều khởi tạo 0 và learning rate 0.1.
# NumPy cho phép tính gradient trên toàn bộ 20 mẫu mỗi epoch (batch gradient descent).
import numpy as np
# 20 x thực từ 0 đến 1.9, mỗi giá trị gắn một y tương ứng.
x = np.array([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9], dtype=float)
# Sinh nhãn mục tiêu từ độ dốc 2 và chặn 1.
y = 2*x + 1
# Hai tham số ban đầu: w là độ dốc, b là hệ số chặn.
w, b = 0.0, 0.0
# Tính MSE đầu với w=b=0 trước khi học.
# Tính MSE cuối sau 300 cập nhật và đổi thành float Python.
initial = float(np.mean((w*x+b-y)**2))
# 300 epoch; mỗi vòng cập nhật dùng tất cả mẫu, không phải 300 bản ghi khác nhau.
for epoch in range(300):
    # Dự đoán hiện tại trừ nhãn thật tại từng điểm; error là vector 20 phần tử.
    error = w*x+b-y
    # dw là đạo hàm MSE theo w: nhân mỗi sai số với x, lấy trung bình rồi ×2.
    dw = 2*np.mean(error*x)
    # db là đạo hàm MSE theo b vì dự đoán phụ thuộc b với hệ số 1.
    db = 2*np.mean(error)
    # Trừ 0.1×gradient để đi theo hướng giảm loss, cập nhật độ dốc.
    w -= 0.1*dw
    # Cập nhật chặn b bằng learning rate 0.1 và gradient riêng db.
    b -= 0.1*db
# Tính MSE đầu với w=b=0 trước khi học.
# Tính MSE cuối sau 300 cập nhật và đổi thành float Python.
mse = float(np.mean((w*x+b-y)**2))
# size đếm đúng 20 mẫu train.
if x.size != 20:
    # raise ValueError dừng khi số mẫu hoặc số lần cập nhật không đúng điều kiện kiểm tra.
    raise ValueError("Cần đủ 20 điểm train.")
print("Mẫu:", len(x))
print("Epoch:", 300)
# f-string :.2f in độ dốc gần 2, có làm tròn hiển thị.
print(f"Trọng số w: {w:.2f}")
# In hệ số chặn gần 1 với hai chữ số thập phân.
print(f"Chặn b: {b:.2f}")
# In MSE cuối với sáu chữ số thập phân để thấy độ lỗi nhỏ.
print(f"MSE cuối: {mse:.6f}")
# So loss cuối với trước học, không đồng nghĩa đã kiểm mô hình trên tập test độc lập.
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
