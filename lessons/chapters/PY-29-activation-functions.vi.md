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

**No Note — Không chú thích**

```python
import numpy as np

signals = np.array([-2, 0, 3])
print(np.maximum(0, signals).tolist())
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Áp dụng ReLU để giữ tín hiệu không âm và thay mọi tín hiệu âm bằng 0.
# Dữ liệu: Vector ba tín hiệu đầu vào -2, 0, 3, mỗi ô là một nơ-ron giả lập.
# NumPy giúp áp hàm kích hoạt trực tiếp trên mọi phần tử mảng.
import numpy as np

# Mảng đầu vào một chiều gồm tín hiệu âm, 0 và dương.
signals = np.array([-2, 0, 3])
# maximum(0,signals) chọn số lớn hơn giữa 0 và từng tín hiệu, tức ReLU(x)=max(0,x); đầu ra [0,0,3].
# tolist() đổi ndarray về list Python để hiển thị dễ đọc.
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

**No Note — Không chú thích**

```python
import numpy as np

x = np.array([-1.0, 0.0, 1.0])
scores = 1 / (1 + np.exp(-x))
print(np.round(scores, 3).tolist())
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Dùng Sigmoid biến ba logit âm, không, dương thành giá trị nằm giữa 0 và 1.
# Dữ liệu: Logit x=-1,0,1 là điểm thô không phải xác suất; đầu ra sigmoid có dạng xác suất.
# NumPy np.exp() tính hàm mũ tự nhiên trên mảng.
import numpy as np

# Ba điểm đầu vào thực, cả âm và dương.
x = np.array([-1.0, 0.0, 1.0])
# exp() tính e^(-x) theo từng ô; dấu âm đổi dấu đầu vào trước phép mũ.
# Sigmoid có đường cong chữ S: đầu ra gần 0 với x âm lớn, bằng 0.5 khi x=0, gần 1 với x dương lớn.
scores = 1 / (1 + np.exp(-x))
# round(...,3) làm tròn ba chữ số sau dấu thập phân để in, không thay scores gốc.
# tolist() chuyển ndarray của ba kết quả thành list Python.
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

**No Note — Không chú thích**

```python
import numpy as np

x = np.array([-1.0, 0.0, 1.0])
print(np.round(np.tanh(x), 3).tolist())
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Áp tanh để nén tín hiệu về khoảng -1 đến 1 và giữ dấu.
# Dữ liệu: Ba đầu vào -1,0,1, điểm dương/âm vẫn được phân biệt.
# NumPy có hàm tanh vector hóa.
import numpy as np

# Vector ba logit có giá trị âm, bằng 0, dương.
x = np.array([-1.0, 0.0, 1.0])
# tanh(x) có giá trị từ -1 đến 1, đi qua 0, giữ dấu đầu vào; khác sigmoid nằm 0..1.
# np.round(...,3) làm tròn kết quả hiển thị đến ba chữ số thập phân.
# tolist() đổi mảng số thành list Python để print().
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

**No Note — Không chú thích**

```python
import numpy as np

z = np.array([2.0, 1.0, 0.1])
e = np.exp(z - z.max())
p = e / e.sum()
print(np.round(p, 3).tolist())
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Dùng Softmax chuyển ba điểm lớp thô thành tỷ lệ dương tổng bằng 1.
# Dữ liệu: Ba logit của ba lớp [2,1,0.1], không phải xác suất ban đầu.
# NumPy có exp(), max(), sum() để tính softmax ổn định.
import numpy as np

# Mỗi phần tử là điểm thô của một lớp; lớp 0 đang lớn nhất.
z = np.array([2.0, 1.0, 0.1])
# z.max() lấy logit lớn nhất; trừ nó khỏi tất cả ô giúp tránh exp của số quá lớn (chống overflow), không đổi tỷ lệ softmax.
# np.exp() lấy e mũ cho từng logit đã dịch, biến điểm thành trọng số dương.
e = np.exp(z - z.max())
# e.sum() cộng trọng số ba lớp, chia từng ô để ra xác suất chuẩn hóa tổng đúng 1.
p = e / e.sum()
# round(...,3) chỉ làm tròn để in ba số thập phân, không làm lại phép chuẩn hóa.
# tolist() chuyển ndarray thành list Python.
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

**Tình huống thực tế:** Trong một mô hình mạng nơ-ron **giả lập**, tầng xử lý nhận **10 tín hiệu thô** không có đơn vị. Có tín hiệu âm, bằng 0 và dương, ví dụ -5 và 5. Bài yêu cầu dùng quy tắc **ReLU** để chặn tín hiệu âm thành 0, giữ tín hiệu dương, rồi đếm bao nhiêu đầu ra bằng 0 và bao nhiêu đầu ra còn dương. Đây là phép thử tính toán, không phải tín hiệu điện của thiết bị thật.

**Vì sao chọn cách này?** **Hàm kích hoạt** biến tín hiệu của một tầng thành đầu ra theo quy tắc nhất định. **ReLU** giữ số dương như cũ, nhưng đổi mọi số âm thành **0**; nó **không xóa vị trí nơ-ron** hay rút ngắn mảng. `np.maximum(0, signals)` áp quy tắc ấy cho cả 10 tín hiệu trong một lần; sau đó so từng đầu ra với 0 để đếm. Cần phân biệt **tín hiệu đầu vào âm** và **đầu ra bằng 0**: đầu ra bằng 0 còn gồm cả tín hiệu đầu vào vốn bằng 0. Quy tắc này đơn giản và hay dùng ở các tầng giữa, không có nghĩa mọi số âm ngoài thực tế đều vô giá trị.

**Quy trình:**
1. Lưu 10 giá trị gồm âm, 0 và dương.
2. Áp ReLU cho toàn bộ mảng.
3. Đếm phần tử có đầu ra bằng 0, đối chiếu đầu ra đầu/cuối.

**No Note — Không chú thích**

```python
import numpy as np
signals = np.array([-5,-3,-1,0,1,2,4,-2,3,5], dtype=float)
activated = np.maximum(0, signals)
if activated.shape != (10,) or signals.shape != (10,):
    raise ValueError("Cần đúng 10 tín hiệu và 10 giá trị ReLU.")
print("Nơ-ron:", len(activated))
print("Đầu ra bằng 0:", int((activated == 0).sum()))
print("Đầu ra dương:", int((activated > 0).sum()))
print("Mẫu đầu/cuối:", int(activated[0]), int(activated[-1]))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Kiểm đầu ra ReLU trên 10 tín hiệu và đếm số bị chặn ở 0.
# Dữ liệu: 10 tín hiệu từ âm tới dương, dtype=float, mỗi tín hiệu ứng với một nơ-ron giả lập.
# NumPy maximum và các mask Boolean chạy trên vector.
import numpy as np
# 10 giá trị thực từ -5 đến 5 theo thứ tự, có âm/0/dương.
signals = np.array([-5,-3,-1,0,1,2,4,-2,3,5], dtype=float)
# ReLU chọn max(0,x) TỪNG Ô, thay x âm bằng 0, giữ nguyên x dương.
activated = np.maximum(0, signals)
# shape (10,) là một vector 10 đầu ra; kiểm cả tín hiệu và đầu ra đều đủ.
if activated.shape != (10,) or signals.shape != (10,):
    # ValueError dừng nếu shape, số mẫu hoặc giới hạn đầu ra không thỏa kỳ vọng.
    raise ValueError("Cần đúng 10 tín hiệu và 10 giá trị ReLU.")
# len() đếm 10 tín hiệu đã kích hoạt.
print("Nơ-ron:", len(activated))
# == 0 tạo mask Boolean ở ô bị ReLU tắt hoặc vốn 0; .sum() đếm số True.
print("Đầu ra bằng 0:", int((activated == 0).sum()))
# Mask >0 đếm số ô giữ đầu ra dương; int() in số nguyên Python.
print("Đầu ra dương:", int((activated > 0).sum()))
# [0] là mẫu đầu, [-1] mẫu cuối; int() đổi scalar số để in.
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

**Tình huống thực tế:** Mô hình phân loại **hai lựa chọn** cho **12 mẫu thử** tạo ra 12 **logit**, tức điểm thô chưa nằm trong khoảng 0 đến 1. Trong số đó có logit âm, dương và bằng 0. Người phân tích cần biến từng điểm qua **sigmoid** để có số nằm giữa 0 và 1, đếm số mẫu có điểm **ít nhất 0,5** và kiểm tra logit bằng 0 cho kết quả đúng **0,5**.

**Vì sao chọn cách này?** **Logit** là điểm mô hình tạo ra trước khi quy đổi, có thể âm hoặc dương và **chưa phải xác suất**. **Sigmoid** đưa điểm đó về khoảng **giữa 0 và 1**; logit 0 nằm đúng giữa nên thành **0,5**, logit dương lớn hơn 0,5 và logit âm nhỏ hơn 0,5. `np.exp()` được dùng trong tính toán cho cả 12 mẫu; `>= 0.5` chỉ là **ngưỡng phân lớp minh họa**. Số sau sigmoid trông giống xác suất, nhưng **chưa thể kết luận mô hình dự báo xác suất chính xác** nếu chưa được kiểm tra hiệu chuẩn trên dữ liệu thực.

**Quy trình:**
1. Tạo 12 điểm thô gồm số âm và dương.
2. Tính vector sigmoid và đối chiếu đầu ra của logit 0.
3. Đếm số điểm đạt ngưỡng 0,5, xác nhận tất cả đầu ra nằm trong (0,1).

**No Note — Không chú thích**

```python
import numpy as np
logits = np.array([-3,-2,-1.5,-1,0,0.2,0.8,1,2,3,4,-0.5], dtype=float)
probabilities = 1 / (1 + np.exp(-logits))
if logits.size != 12 or not np.all((probabilities > 0) & (probabilities < 1)):
    raise ValueError("Cần 12 mẫu Sigmoid, mỗi xác suất phải nằm giữa 0 và 1.")
print("Mẫu:", len(logits))
print("Từ 0.5:", int((probabilities >= 0.5).sum()))
print("Logit 0:", f"{probabilities[logits == 0][0]:.3f}")
print("Logit -3:", f"{probabilities[0]:.3f}")
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Đánh giá Sigmoid trên 12 logit và dùng ngưỡng 0.5 để đếm nhãn dương.
# Dữ liệu: 12 logit điểm thô từ -3 tới 4, trước kích hoạt chưa phải xác suất.
# NumPy vector hóa phép mũ và so sánh xác suất.
import numpy as np
# 12 điểm thô số thực; giá trị âm/0/dương.
logits = np.array([-3,-2,-1.5,-1,0,0.2,0.8,1,2,3,4,-0.5], dtype=float)
# exp() tính hàm mũ e^(-logit) từng ô, thành phần của Sigmoid.
# Sigmoid chuyển từng điểm thô sang 0..1; 0 map thành 0.5.
probabilities = 1 / (1 + np.exp(-logits))
# size là số ô đầu vào, kỳ vọng 12.
# Mỗi so sánh tạo mask, & là AND theo từng ô, np.all() buộc mọi đầu ra nằm TRONG khoảng (0,1), không dùng 'and' với ndarray.
if logits.size != 12 or not np.all((probabilities > 0) & (probabilities < 1)):
    # ValueError dừng nếu shape, số mẫu hoặc giới hạn đầu ra không thỏa kỳ vọng.
    raise ValueError("Cần 12 mẫu Sigmoid, mỗi xác suất phải nằm giữa 0 và 1.")
print("Mẫu:", len(logits))
# So xác suất với ngưỡng quyết định 0.5 rồi sum() mask để đếm số thuộc lớp dương.
print("Từ 0.5:", int((probabilities >= 0.5).sum()))
# logits==0 tạo mask; probabilities[mask] lọc giá trị của logit 0, [0] lấy một phần tử trong mảng lọc.
print("Logit 0:", f"{probabilities[logits == 0][0]:.3f}")
# [0] lấy giá trị logit -3 theo vị trí nguồn; :.3f in ba chữ số lẻ.
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

**Tình huống thực tế:** Một tầng xử lý thử nghiệm nhận **15 tín hiệu từ -7 đến 7**, gồm các giá trị âm, 0 và dương. Nhóm muốn dùng **tanh** để đưa tín hiệu về khoảng gần **-1 đến 1**, rồi xem dấu của tín hiệu có được giữ không và có bao nhiêu đầu ra tiến sát hai đầu mút, cụ thể **độ lớn lớn hơn 0,99**. Các con số không có đơn vị và chỉ dùng để minh họa quy tắc kích hoạt.

**Vì sao chọn cách này?** **Tanh** cũng là một hàm kích hoạt nhưng khác sigmoid ở chỗ đầu ra có thể **âm, bằng 0 hoặc dương**. Nó giữ dấu của đầu vào và đưa các số có độ lớn rất lớn về **gần -1 hoặc gần +1**; đó gọi là **bão hòa**. `np.tanh(signals)` tính đủ 15 đầu ra; `np.abs()` lấy **độ lớn bất kể dấu** để đếm những đầu ra có độ lớn **vượt 0,99**. Khi gần bão hòa, tăng thêm đầu vào thường làm đầu ra đổi rất ít, điều cần chú ý khi huấn luyện mô hình; bài chỉ quan sát hiện tượng này, chưa huấn luyện mạng.

**Quy trình:**
1. Tạo 15 giá trị đầu vào đối xứng qua 0.
2. Dùng `np.tanh` và kiểm dấu bằng so sánh.
3. Đếm các trường hợp đầu ra có độ lớn trên 0,99.

**No Note — Không chú thích**

```python
import numpy as np
signals = np.array([-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7], dtype=float)
activated = np.tanh(signals)
if signals.size != 15:
    raise ValueError("Cần đủ 15 tín hiệu Tanh.")
print("Tín hiệu:", len(signals))
print("Tanh(0):", f"{activated[signals == 0][0]:.3f}")
print("Bão hòa |y| > 0.99:", int((np.abs(activated) > 0.99).sum()))
print("Giữ dấu:", bool(np.all(np.sign(activated) == np.sign(signals))))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Kiểm Tanh trên 15 tín hiệu, số tín hiệu bão hòa và khả năng giữ dấu.
# Dữ liệu: 15 logit -7..7, điểm không bằng 0 có dấu âm hoặc dương.
# NumPy np.tanh() kích hoạt theo từng ô, np.sign() kiểm dấu.
import numpy as np
# 15 tín hiệu, dtype=float; có giá trị đối xứng âm/dương quanh 0.
signals = np.array([-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7], dtype=float)
# tanh nén giá trị vào (-1,1), âm vẫn âm, dương vẫn dương, 0→0.
activated = np.tanh(signals)
# size đếm 15 phần tử vector.
if signals.size != 15:
    # ValueError dừng nếu shape, số mẫu hoặc giới hạn đầu ra không thỏa kỳ vọng.
    raise ValueError("Cần đủ 15 tín hiệu Tanh.")
print("Tín hiệu:", len(signals))
# signals==0 là mask tìm logit 0; [0] chọn đầu ra tương ứng, :.3f in 3 số lẻ.
print("Tanh(0):", f"{activated[signals == 0][0]:.3f}")
# abs() lấy độ lớn đầu ra, ngưỡng 0.99 đánh dấu tín hiệu gần ±1 (bão hòa); .sum() đếm.
print("Bão hòa |y| > 0.99:", int((np.abs(activated) > 0.99).sum()))
# np.sign() trả -1,0,+1 theo dấu; == so từng ô hai vector để xác minh tanh giữ dấu.
# np.all() True chỉ khi mọi vị trí đều giữ dấu; bool() đổi về bool Python.
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

**Tình huống thực tế:** Một bộ phân loại có **18 mẫu**, mỗi mẫu cần chọn một trong **ba lớp A, B hoặc C**. Mô hình xuất ba **logit** không đơn vị cho từng mẫu; một dòng có điểm thô gần **1.000** nên nếu tính hàm mũ trực tiếp có nguy cơ ra số quá lớn. Nhóm muốn biến ba điểm mỗi mẫu thành ba **điểm softmax có tổng bằng 1**, đếm số mẫu chọn từng lớp và kiểm tra dòng logit rất lớn vẫn cho kết quả hữu hạn.

**Vì sao chọn cách này?** **Softmax** chuyển ba logit của **một mẫu** thành ba điểm dương có **tổng bằng 1**, hữu ích khi chọn **một lớp trong ba lớp loại trừ nhau**. Vì một logit tới gần 1.000, tính `np.exp()` trực tiếp có thể bị **tràn số** (quá lớn để máy lưu). Chương trình trừ **logit lớn nhất của mỗi hàng** trước rồi mới tính mũ; điều này không đổi tỷ lệ so sánh giữa ba lớp trong cùng mẫu mà giúp tính ổn định. `axis=1` chỉ việc xử lý **ba lớp ngang một hàng**, không gộp 18 mẫu vào chung một phân phối. `argmax(axis=1)` chọn lớp điểm cao nhất của từng mẫu; tổng mỗi hàng gần 1 chứ tổng tất cả 18 hàng không phải 1.

**Quy trình:**
1. Tạo mảng 18×3 có một hàng logit rất lớn.
2. Trừ max theo `axis=1`, lấy mũ rồi chia tổng hàng.
3. Kiểm tra tổng xác suất từng hàng, đếm nhãn dự đoán A/B/C.

**No Note — Không chú thích**

```python
import numpy as np
logits = np.array([[3,1,0],[0,3,1],[1,0,3],[1000,999,998],[0,3,1],[1,0,3],[3,1,0],[0,3,1],[1,0,3],[3,1,0],[0,3,1],[1,0,3],[3,1,0],[0,3,1],[1,0,3],[3,1,0],[0,3,1],[1,0,3]], dtype=float)
shifted = logits - logits.max(axis=1, keepdims=True)
exp_values = np.exp(shifted)
probs = exp_values / exp_values.sum(axis=1, keepdims=True)
predictions = probs.argmax(axis=1)
if logits.shape != (18, 3) or probs.shape != (18, 3):
    raise ValueError("Cần đủ 18 mẫu, mỗi mẫu có 3 lớp.")
print("Mẫu:", len(logits))
print("Tổng hàng đều là 1:", bool(np.allclose(probs.sum(axis=1), 1)))
counts = []
for k in range(3):
    counts.append(int((predictions == k).sum()))
print("Nhãn A/B/C:", *counts)
print("Mẫu logit lớn hữu hạn:", bool(np.isfinite(probs[3]).all()))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tính Softmax ổn định cho 18 dòng ba lớp và thống kê lớp dự đoán.
# Dữ liệu: 18 hàng mẫu, 3 cột điểm logit lớp A/B/C, gồm một hàng logit [1000,999,998] rất lớn.
# NumPy tính exp, max, sum, argmax và kiểm tính hữu hạn.
import numpy as np
# Bảng shape (18,3): một hàng ứng với một mẫu, ba cột A/B/C là điểm thô.
logits = np.array([[3,1,0],[0,3,1],[1,0,3],[1000,999,998],[0,3,1],[1,0,3],[3,1,0],[0,3,1],[1,0,3],[3,1,0],[0,3,1],[1,0,3],[3,1,0],[0,3,1],[1,0,3],[3,1,0],[0,3,1],[1,0,3]], dtype=float)
# axis=1 lấy điểm cao nhất CỦA TỪNG HÀNG, keepdims=True giữ shape (18,1) để broadcast an toàn về 18×3.
# Trừ max từng hàng trước khi exp để tránh overflow với logit 1000; Softmax không đổi khi mọi điểm một hàng cùng trừ hằng số.
shifted = logits - logits.max(axis=1, keepdims=True)
# e^x cho từng logit đã dịch, ra trọng số dương hữu hạn.
exp_values = np.exp(shifted)
# sum(axis=1) cộng ba trọng số mỗi hàng, keepdims=True giữ cột (18,1) để chia từng ô đúng hàng.
# Broadcast chia mỗi hàng cho tổng của chính hàng để xác suất mỗi hàng cộng bằng 1.
probs = exp_values / exp_values.sum(axis=1, keepdims=True)
# argmax(axis=1) trả chỉ số cột lớp lớn nhất trên TỪNG HÀNG, mã 0/1/2; không trả xác suất.
predictions = probs.argmax(axis=1)
# Kiểm đúng 18 mẫu và ba lớp, cả logits/probs đều shape (18,3).
if logits.shape != (18, 3) or probs.shape != (18, 3):
    # ValueError dừng nếu shape, số mẫu hoặc giới hạn đầu ra không thỏa kỳ vọng.
    raise ValueError("Cần đủ 18 mẫu, mỗi mẫu có 3 lớp.")
print("Mẫu:", len(logits))
# sum(axis=1) lấy tổng ba lớp mỗi hàng, allclose() so gần 1 có dung sai số thực.
print("Tổng hàng đều là 1:", bool(np.allclose(probs.sum(axis=1), 1)))
counts = []
# range(3) tạo các mã lớp 0,1,2; không có 3.
for k in range(3):
    # Mask xác định hàng dự đoán là lớp k, sum() đếm số mẫu của lớp đó.
    counts.append(int((predictions == k).sum()))
# *counts giải nén ba phần tử list thành ba đối số print riêng, ứng với A/B/C.
print("Nhãn A/B/C:", *counts)
# [3] là hàng logit 1000 (index từ 0); isfinite() kiểm không NaN/inf, .all() đòi cả ba ô hợp lệ.
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

**Tình huống thực tế:** Một mô hình thử có **20 mẫu**, mỗi mẫu gồm hai tín hiệu đầu vào **x và y** cùng nhãn đúng **0 hoặc 1**. Dữ liệu được tạo theo quy tắc nhãn là 1 khi **tổng x và y lớn hơn 0**. Mô hình lại dùng ReLU chặn riêng từng tín hiệu âm, cộng các tín hiệu đã chặn, bớt 1 rồi dùng sigmoid quyết định theo ngưỡng **0,5**. Nhóm muốn biết dự đoán đúng và sai bao nhiêu lần để thấy biến đổi đầu vào có thể làm mất thông tin cần phân lớp.

**Vì sao chọn cách này?** ReLU và sigmoid làm **hai việc khác nhau** trong mô hình. ReLU chặn phần âm của từng tín hiệu đầu vào, khiến một số thông tin về **độ lớn âm** biến mất; sigmoid chỉ đổi điểm cuối thành số từ 0 đến 1 để áp ngưỡng dự đoán. Nhãn đúng trong bài dựa trên **tổng x và y gốc**, vì vậy các mẫu có số âm mạnh có thể bị mô hình ReLU hiểu khác: không thể lấy điểm sigmoid lớn rồi cho rằng dự đoán đúng. Chương trình phải so `predicted` với **20 nhãn tham chiếu** để đếm đúng/sai. Đây là ví dụ cho thấy chọn phép biến đổi đầu vào ảnh hưởng thông tin mô hình giữ lại, không khẳng định ReLU nói chung là không tốt.

**Quy trình:**
1. Tạo 20 hàng hai tín hiệu cùng 20 nhãn được định nghĩa rõ.
2. Áp ReLU, tính logit tổng và sigmoid, chuyển điểm thành nhãn theo ngưỡng 0,5.
3. Đếm số dự đoán đúng/sai và kiểm tổng bằng 20.

**No Note — Không chú thích**

```python
import numpy as np
X = np.array([[-2,-1],[-1,-1],[0,-1],[1,-1],[2,-1],[-2,0],[-1,0],[0,0],[1,0],[2,0],[-2,1],[-1,1],[0,1],[1,1],[2,1],[-2,2],[-1,2],[0,2],[1,2],[2,2]], dtype=float)
labels = np.array([0,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0,1,1,1,1], dtype=int)
hidden = np.maximum(0, X)
logits = hidden.sum(axis=1) - 1
scores = 1 / (1 + np.exp(-logits))
predicted = (scores >= 0.5).astype(int)
correct = int((predicted == labels).sum())
if X.shape != (20, 2) or labels.shape != (20,) or predicted.shape != (20,):
    raise ValueError("Cần đủ 20 mẫu, hai đặc trưng và 20 nhãn đối chiếu.")
print("Mẫu:", len(labels))
print("Dự đoán đúng:", correct)
print("Dự đoán sai:", len(labels) - correct)
print("Có nhãn dương:", int(labels.sum()))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Dùng ReLU hai đặc trưng, tổng tín hiệu và Sigmoid để dự đoán 20 nhãn 0/1.
# Dữ liệu: 20 hàng X có 2 đặc trưng số, labels là 20 nhãn thật 0/1 cùng thứ tự hàng.
# NumPy hỗ trợ mạng kích hoạt đơn giản hoàn toàn bằng phép toán mảng.
import numpy as np
# X shape (20,2), mỗi hàng là một mẫu, mỗi cột là một đặc trưng có thể âm hoặc dương.
X = np.array([[-2,-1],[-1,-1],[0,-1],[1,-1],[2,-1],[-2,0],[-1,0],[0,0],[1,0],[2,0],[-2,1],[-1,1],[0,1],[1,1],[2,1],[-2,2],[-1,2],[0,2],[1,2],[2,2]], dtype=float)
# 20 nhãn thật 0/1, dtype=int dùng làm đáp án đối chiếu.
labels = np.array([0,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0,1,1,1,1], dtype=int)
# ReLU TỪNG Ô: âm thành 0, dương giữ nguyên; hidden vẫn shape (20,2).
hidden = np.maximum(0, X)
# axis=1 cộng hai đặc trưng của TỪNG MẪU thành một số; trừ 1 là bias/ngưỡng giả lập trước sigmoid.
logits = hidden.sum(axis=1) - 1
# exp() tính e mũ âm logit để Sigmoid hoạt động từng mẫu.
# Sigmoid biến 20 logit thành 20 xác suất lớp dương từ 0 đến 1.
scores = 1 / (1 + np.exp(-logits))
# Ngưỡng 0.5 tạo mask Boolean: True dự đoán 1, False dự đoán 0.
# astype(int) đổi mask True/False sang mảng nhãn 1/0 để so với labels.
predicted = (scores >= 0.5).astype(int)
# So sánh từng vị trí nhãn dự đoán và nhãn thật (không tự căn lại thứ tự hàng).
# sum() mask đếm số nhãn đúng; int() chuyển sang số nguyên Python.
correct = int((predicted == labels).sum())
# shape (20,2) của X và (20,) của labels/predicted kiểm đủ mẫu.
if X.shape != (20, 2) or labels.shape != (20,) or predicted.shape != (20,):
    # ValueError dừng nếu shape, số mẫu hoặc giới hạn đầu ra không thỏa kỳ vọng.
    raise ValueError("Cần đủ 20 mẫu, hai đặc trưng và 20 nhãn đối chiếu.")
print("Mẫu:", len(labels))
print("Dự đoán đúng:", correct)
print("Dự đoán sai:", len(labels) - correct)
# Nhãn chỉ 0/1 nên sum() đếm số nhãn dương thật; không phải số dự đoán dương.
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

A. `1/(1+exp(-x))` | `1/(1+exp(-x))`

B. A smooth activation mapping into (−1,1) | Hàm trơn đưa giá trị vào (−1,1)

C. Normalization of several class logits to sum one | Chuẩn hóa nhiều logit lớp có tổng bằng một

D. `max(0,x)` | `max(0,x)`

**Đáp án: D**

**Giải thích:** ReLU chặn giá trị âm về không.


**Q2. What is sigmoid? | Sigmoid là gì?**

A. `max(0,x)` | `max(0,x)`

B. Normalization of several class logits to sum one | Chuẩn hóa nhiều logit lớp có tổng bằng một

C. A smooth activation mapping into (−1,1) | Hàm trơn đưa giá trị vào (−1,1)

D. `1/(1+exp(-x))` | `1/(1+exp(-x))`

**Đáp án: D**

**Giải thích:** Sigmoid là phép biến đổi logistic hình chữ S.


**Q3. What is tanh? | Tanh là gì?**

A. `max(0,x)` | `max(0,x)`

B. `1/(1+exp(-x))` | `1/(1+exp(-x))`

C. Normalization of several class logits to sum one | Chuẩn hóa nhiều logit lớp có tổng bằng một

D. A smooth activation mapping into (−1,1) | Hàm trơn đưa giá trị vào (−1,1)

**Đáp án: D**

**Giải thích:** Tanh cân quanh 0 và giới hạn giữa −1 và 1.


**Q4. What is softmax? | Softmax là gì?**

A. `1/(1+exp(-x))` | `1/(1+exp(-x))`

B. `max(0,x)` | `max(0,x)`

C. A smooth activation mapping into (−1,1) | Hàm trơn đưa giá trị vào (−1,1)

D. Normalization of several class logits to sum one | Chuẩn hóa nhiều logit lớp có tổng bằng một

**Đáp án: D**

**Giải thích:** Softmax ràng buộc điểm lớp thành một phân phối chuẩn hóa.


**Q5. What is ReLU(−3) if ReLU(x) = max(0, x)? | ReLU(−3) bằng bao nhiêu nếu ReLU(x) = max(0, x)?**

A. 3 | 3

B. −3 | −3

C. 0 | 0

D. 1 | 1

**Đáp án: C**

**Giải thích:** ReLU chọn giá trị lớn hơn giữa 0 và x. Với −3, giá trị lớn hơn là 0.


**Q6. What is the sigmoid output at input x = 0? | Hàm sigmoid nhận x = 0 thì kết quả là bao nhiêu?**

A. 0 | 0

B. 1 | 1

C. −1 | −1

D. 0.5 | 0.5

**Đáp án: D**

**Giải thích:** Sigmoid(0) = 1/(1 + e⁰) = 1/(1 + 1) = 0.5.


**Q7. A softmax layer outputs probabilities for three classes. What must their sum be (up to rounding)? | Softmax trả về xác suất cho ba lớp. Tổng các xác suất phải gần bằng bao nhiêu?**

A. 0.5 | 0.5

B. 3 | 3

C. 1 | 1

D. 0 | 0

**Đáp án: C**

**Giải thích:** Softmax chuẩn hóa điểm số của tất cả các lớp để các xác suất không âm và cộng lại bằng 1.


**Q8. Which statement about sigmoid is correct for any finite input? | Phát biểu nào đúng về đầu ra sigmoid với mọi đầu vào hữu hạn?**

A. The output always exceeds 1 | Kết quả luôn lớn hơn 1

B. The output lies strictly between 0 and 1 | Kết quả nằm giữa 0 và 1, không chạm hai đầu

C. The output can be negative | Kết quả có thể âm

D. The output is always exactly 0 or 1 | Kết quả luôn chính xác 0 hoặc 1

**Đáp án: B**

**Giải thích:** Với đầu vào hữu hạn, mẫu số 1 + e^(−x) lớn hơn 1, nên đầu ra dương nhưng nhỏ hơn 1.


**Q9. Which NumPy function applies ReLU? | Hàm NumPy nào thực hiện ReLU?**

A. `np.maximum(0,x)` | `np.maximum(0,x)`

B. The largest logit | Logit lớn nhất

C. Tanh | Tanh

D. `np.tanh(x)` | `np.tanh(x)`

**Đáp án: A**

**Giải thích:** maximum chặn từng phần tử.


**Q10. Which NumPy function directly computes tanh? | Hàm NumPy nào tính tanh trực tiếp?**

A. `np.tanh(x)` | `np.tanh(x)`

B. Tanh | Tanh

C. The largest logit | Logit lớn nhất

D. `np.maximum(0,x)` | `np.maximum(0,x)`

**Đáp án: A**

**Giải thích:** NumPy có hàm tanh trực tiếp.


**Q11. Which quantity should be subtracted from logits before stable softmax exponentiation? | Nên trừ gì khỏi logit trước khi tính exp softmax ổn định?**

A. `np.tanh(x)` | `np.tanh(x)`

B. `np.maximum(0,x)` | `np.maximum(0,x)`

C. The largest logit | Logit lớn nhất

D. Tanh | Tanh

**Đáp án: C**

**Giải thích:** Trừ cực đại giữ các số exp không vượt một.


**Q12. Which activation outputs exactly 0 at input 0? | Hàm nào trả đúng 0 với đầu vào 0?**

A. The largest logit | Logit lớn nhất

B. `np.tanh(x)` | `np.tanh(x)`

C. `np.maximum(0,x)` | `np.maximum(0,x)`

D. Tanh | Tanh

**Đáp án: D**

**Giải thích:** Tanh(0)=0, còn sigmoid(0)=0.5.


**Q13. What is sigmoid(0)? | sigmoid(0) bằng gì?**

A. A negative output | Giá trị đầu ra âm

B. It reduces overflow risk without changing the result | Giảm nguy cơ tràn số mà không đổi kết quả

C. 0.5 | 0.5

D. 0 | 0

**Đáp án: C**

**Giải thích:** Sigmoid tại zero bằng một nửa.


**Q14. What is ReLU(−2)? | ReLU(−2) bằng gì?**

A. A negative output | Giá trị đầu ra âm

B. It reduces overflow risk without changing the result | Giảm nguy cơ tràn số mà không đổi kết quả

C. 0.5 | 0.5

D. 0 | 0

**Đáp án: D**

**Giải thích:** ReLU chặn đầu vào âm.


**Q15. What does tanh produce for negative input? | Tanh tạo đầu ra thế nào khi đầu vào âm?**

A. A negative output | Giá trị đầu ra âm

B. 0.5 | 0.5

C. 0 | 0

D. It reduces overflow risk without changing the result | Giảm nguy cơ tràn số mà không đổi kết quả

**Đáp án: A**

**Giải thích:** Tanh giữ dấu của đầu vào hữu hạn khác 0.


**Q16. Why does subtracting max(logits) help softmax? | Vì sao trừ cực đại logit giúp softmax?**

A. 0.5 | 0.5

B. It reduces overflow risk without changing the result | Giảm nguy cơ tràn số mà không đổi kết quả

C. 0 | 0

D. A negative output | Giá trị đầu ra âm

**Đáp án: B**

**Giải thích:** Dịch đều các logit không đổi softmax nhưng giảm tràn số.


**Q17. Which output structure suits mutually exclusive multi-class prediction? | Dạng đầu ra nào phù hợp phân loại nhiều lớp loại trừ nhau?**

A. Their inputs remain in the nonpositive flat region | Đầu vào luôn ở vùng phẳng không dương

B. No, calibration needs checking | Không, cần đánh giá độ hiệu chuẩn

C. Softmax couples scores so they sum to one | Softmax ràng buộc điểm các lớp có tổng một

D. A softmax distribution over classes | Phân phối softmax trên các lớp

**Đáp án: D**

**Giải thích:** Softmax thường dùng cho đầu ra các lớp loại trừ nhau.


**Q18. Why might ReLU neurons stop updating? | Vì sao một số nơ-ron ReLU có thể ngừng cập nhật?**

A. A softmax distribution over classes | Phân phối softmax trên các lớp

B. No, calibration needs checking | Không, cần đánh giá độ hiệu chuẩn

C. Softmax couples scores so they sum to one | Softmax ràng buộc điểm các lớp có tổng một

D. Their inputs remain in the nonpositive flat region | Đầu vào luôn ở vùng phẳng không dương

**Đáp án: D**

**Giải thích:** Độ dốc ReLU bằng không ở đầu vào âm.


**Q19. Do sigmoid outputs automatically prove calibrated probabilities? | Đầu ra sigmoid có mặc nhiên là xác suất đã hiệu chuẩn không?**

A. Softmax couples scores so they sum to one | Softmax ràng buộc điểm các lớp có tổng một

B. No, calibration needs checking | Không, cần đánh giá độ hiệu chuẩn

C. Their inputs remain in the nonpositive flat region | Đầu vào luôn ở vùng phẳng không dương

D. A softmax distribution over classes | Phân phối softmax trên các lớp

**Đáp án: B**

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
