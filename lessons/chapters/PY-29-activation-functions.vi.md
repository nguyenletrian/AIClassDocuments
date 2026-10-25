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

## 5. Năm tình huống Activation — từ ReLU đến phân loại 20 mẫu

### Tình huống 1 — Cấp 1: Chặn tín hiệu âm của 10 nơ-ron bằng ReLU

**Từ vựng trong mục:** **ReLU** — hàm giữ phần dương; **Activation** — kích hoạt.

**Tình huống thực tế:** Một tầng mạng thử nghiệm nhận **10 điểm thô** (không đơn vị) của 10 nơ-ron, mỗi phần tử là tín hiệu trước hàm kích hoạt. Điểm âm cần bị chặn về 0, còn điểm dương được giữ. Cần đếm số phần tử bị chặn và số phần tử còn dương.

**Vì sao chọn cách này?** `np.maximum(0, x)` áp dụng cùng quy tắc cho toàn bộ tín hiệu; khác cách xóa các nơ-ron có đầu vào âm, hàm vẫn giữ nguyên số phần tử đầu ra.

**Quy trình:**
1. Lưu 10 giá trị gồm âm, 0 và dương.
2. Áp ReLU cho toàn bộ mảng.
3. Đếm phần tử có đầu ra bằng 0, đối chiếu đầu ra đầu/cuối.

```python
import numpy as np
signals = np.array([-5,-3,-1,0,1,2,4,-2,3,5], dtype=float)
activated = np.maximum(0, signals)
assert activated.shape == signals.shape == (10,)
print("Nơ-ron:", len(activated))
print("Đầu ra bằng 0:", int((activated == 0).sum()))
print("Đầu ra dương:", int((activated > 0).sum()))
print("Mẫu đầu/cuối:", int(activated[0]), int(activated[-1]))
```

**Kết quả khi chạy:**

```text
Nơ-ron: 10
Đầu ra bằng 0: 5
Đầu ra dương: 5
Mẫu đầu/cuối: 0 5
```

Đầu ra ReLU bằng 0 có thể bắt nguồn từ **đầu vào âm hoặc bằng 0**, hai trường hợp cần phân biệt khi phân tích.

### Tình huống 2 — Cấp 2: Ánh xạ 12 logit sang điểm sigmoid

**Từ vựng trong mục:** **Sigmoid** — hàm chữ S; **Logit** — điểm thô; **Threshold** — ngưỡng.

**Tình huống thực tế:** Hệ phân loại nhị phân trả **12 logit** không đơn vị, mỗi hàng là điểm thô của một mẫu. Giá trị âm, 0 và dương đều có mặt. Cần biến chúng thành điểm sigmoid trong (0,1), đếm số mẫu có điểm **từ 0,5** trở lên và kiểm tra logit 0 biến thành đúng 0,5.

**Vì sao chọn cách này?** Sigmoid nén điểm thô sang (0,1) để dễ dùng ngưỡng nhị phân; bản thân điểm sigmoid không chứng minh mô hình đã được hiệu chuẩn xác suất. Ví dụ dùng logit nhỏ để người mới theo dõi công thức trực tiếp.

**Quy trình:**
1. Tạo 12 điểm thô gồm số âm và dương.
2. Tính vector sigmoid và đối chiếu đầu ra của logit 0.
3. Đếm số điểm đạt ngưỡng 0,5, xác nhận tất cả đầu ra nằm trong (0,1).

```python
import numpy as np
logits = np.array([-3,-2,-1.5,-1,0,0.2,0.8,1,2,3,4,-0.5], dtype=float)
probabilities = 1 / (1 + np.exp(-logits))
assert logits.size == 12 and np.all((probabilities > 0) & (probabilities < 1))
print("Mẫu:", len(logits))
print("Từ 0.5:", int((probabilities >= 0.5).sum()))
print("Logit 0:", f"{probabilities[logits == 0][0]:.3f}")
print("Logit -3:", f"{probabilities[0]:.3f}")
```

**Kết quả khi chạy:**

```text
Mẫu: 12
Từ 0.5: 7
Logit 0: 0.500
Logit -3: 0.047
```

Ngưỡng 0,5 là lựa chọn minh họa; dùng ngưỡng thật cần xét chi phí sai lệch và dữ liệu kiểm chứng.

### Tình huống 3 — Cấp 3: So dấu và hiện tượng bão hòa của tanh trên 15 tín hiệu

**Từ vựng trong mục:** **Tanh** — hàm hyperbolic; **Saturation** — bão hòa; **Zero-centered** — đối xứng qua 0.

**Tình huống thực tế:** Cảm biến giả lập đưa ra **15 tín hiệu** từ -7 đến 7 theo thứ tự. Người học cần áp tanh, kiểm tra đầu ra có giữ đúng dấu và đếm số tín hiệu bị bão hòa khi trị tuyệt đối đầu ra **lớn hơn 0,99**.

**Vì sao chọn cách này?** Tanh giữ đầu ra âm/dương quanh 0, khác sigmoid luôn dương. Khi đầu vào lớn về độ lớn, kết quả sát -1/+1, nên mức thay đổi nhỏ và được gọi là bão hòa.

**Quy trình:**
1. Tạo 15 giá trị đầu vào đối xứng qua 0.
2. Dùng `np.tanh` và kiểm dấu bằng so sánh.
3. Đếm các trường hợp đầu ra có độ lớn trên 0,99.

```python
import numpy as np
signals = np.array([-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7], dtype=float)
activated = np.tanh(signals)
assert signals.size == 15
print("Tín hiệu:", len(signals))
print("Tanh(0):", f"{activated[signals == 0][0]:.3f}")
print("Bão hòa |y| > 0.99:", int((np.abs(activated) > 0.99).sum()))
print("Giữ dấu:", bool(np.all(np.sign(activated) == np.sign(signals))))
```

**Kết quả khi chạy:**

```text
Tín hiệu: 15
Tanh(0): 0.000
Bão hòa |y| > 0.99: 10
Giữ dấu: True
```

Không được coi đầu ra gần ±1 là tín hiệu ban đầu cũng chỉ có độ lớn 1; hàm đã nén đầu vào.

### Tình huống 4 — Cấp 4: Softmax ổn định cho 18 mẫu phân loại ba lớp

**Từ vựng trong mục:** **Softmax** — chuẩn hóa theo hàng; **Numerical stability** — ổn định số; **Argmax** — lớp lớn nhất.

**Tình huống thực tế:** Một mô hình trả **18 bản ghi** với ba logit đại diện cho lớp A/B/C loại trừ nhau; mỗi hàng là một mẫu, ba cột là điểm thô của các lớp. Một mẫu có logit gần 1.000, nên tính mũ trực tiếp có nguy cơ tràn số. Cần chuẩn hóa theo **từng hàng** và đếm lớp có điểm cao nhất.

**Vì sao chọn cách này?** Trừ logit lớn nhất **của từng hàng** trước khi `np.exp` giúp softmax ổn định, không thay đổi tỷ lệ trong hàng; tổng mỗi hàng bằng 1 nhưng tổng cả 18 hàng sẽ bằng 18.

**Quy trình:**
1. Tạo mảng 18×3 có một hàng logit rất lớn.
2. Trừ max theo `axis=1`, lấy mũ rồi chia tổng hàng.
3. Kiểm tra tổng xác suất từng hàng, đếm nhãn dự đoán A/B/C.

```python
import numpy as np
logits = np.array([[3,1,0],[0,3,1],[1,0,3],[1000,999,998],[0,3,1],[1,0,3],[3,1,0],[0,3,1],[1,0,3],[3,1,0],[0,3,1],[1,0,3],[3,1,0],[0,3,1],[1,0,3],[3,1,0],[0,3,1],[1,0,3]], dtype=float)
shifted = logits - logits.max(axis=1, keepdims=True)
exp_values = np.exp(shifted)
probs = exp_values / exp_values.sum(axis=1, keepdims=True)
predictions = probs.argmax(axis=1)
assert logits.shape == probs.shape == (18, 3)
print("Mẫu:", len(logits))
print("Tổng hàng đều là 1:", bool(np.allclose(probs.sum(axis=1), 1)))
print("Nhãn A/B/C:", *(int((predictions == k).sum()) for k in range(3)))
print("Mẫu logit lớn hữu hạn:", bool(np.isfinite(probs[3]).all()))
```

**Kết quả khi chạy:**

```text
Mẫu: 18
Tổng hàng đều là 1: True
Nhãn A/B/C: 6 6 6
Mẫu logit lớn hữu hạn: True
```

Softmax xử lý **ba lớp cạnh tranh trong mỗi mẫu**, không dùng một sigmoid riêng rẽ rồi giả định tổng bằng 1.

### Tình huống 5 — Cấp 5: Ghép ReLU và sigmoid để phân loại 20 mẫu, kiểm cả nhãn thật

**Từ vựng trong mục:** **Activation pipeline** — chuỗi kích hoạt; **ReLU** — chặn âm; **Sigmoid** — điểm nhị phân.

**Tình huống thực tế:** Một hệ thống thử nghiệm có **20 mẫu**, mỗi hàng gồm hai tín hiệu x/y không đơn vị và nhãn tham chiếu 0/1. Theo quy tắc dữ liệu minh họa, nhãn thật là 1 khi **x+y lớn hơn 0**. Mô hình đơn giản lại chặn từng tín hiệu âm bằng ReLU, cộng chúng, trừ 1 rồi sigmoid. Cần tính dự đoán ngưỡng 0,5, số mẫu đúng/sai và so với nhãn thật để thấy biến đổi phi tuyến **có thể làm mất thông tin dấu**.

**Vì sao chọn cách này?** ReLU và sigmoid có vai trò khác nhau: ReLU làm phi tuyến ở tầng giữa, sigmoid nén logit đầu ra. Không được đánh giá mô hình chỉ bằng số đầu ra lớn hơn 0,5; cần **nhãn thật** để kiểm đúng/sai.

**Quy trình:**
1. Tạo 20 hàng hai tín hiệu cùng 20 nhãn được định nghĩa rõ.
2. Áp ReLU, tính logit tổng và sigmoid, chuyển điểm thành nhãn theo ngưỡng 0,5.
3. Đếm số dự đoán đúng/sai và kiểm tổng bằng 20.

```python
import numpy as np
X = np.array([[-2,-1],[-1,-1],[0,-1],[1,-1],[2,-1],[-2,0],[-1,0],[0,0],[1,0],[2,0],[-2,1],[-1,1],[0,1],[1,1],[2,1],[-2,2],[-1,2],[0,2],[1,2],[2,2]], dtype=float)
labels = np.array([0,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0,1,1,1,1], dtype=int)
hidden = np.maximum(0, X)
logits = hidden.sum(axis=1) - 1
scores = 1 / (1 + np.exp(-logits))
predicted = (scores >= 0.5).astype(int)
correct = int((predicted == labels).sum())
assert X.shape == (20, 2) and labels.shape == predicted.shape == (20,)
print("Mẫu:", len(labels))
print("Dự đoán đúng:", correct)
print("Dự đoán sai:", len(labels) - correct)
print("Có nhãn dương:", int(labels.sum()))
```

**Kết quả khi chạy:**

```text
Mẫu: 20
Dự đoán đúng: 16
Dự đoán sai: 4
Có nhãn dương: 10
```

Đây là pipeline với trọng số cố định **không được huấn luyện**; số mẫu đúng chỉ kiểm tra hành vi trên dữ liệu giả lập.

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
