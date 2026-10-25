# PY-30 — Loss: MSE, MAE, Huber, cross-entropy và KL


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **MSE** — sai số bình phương trung bình; **MAE** — sai số tuyệt đối trung bình.

`Dự đoán → Sai số → Loss → Tối ưu hóa`

**Học xong dùng để làm gì?** Đo sai số dự đoán bằng MSE hoặc loss thích hợp và đặt mục tiêu cần tối ưu.

**Kết nối kiến thức tiếp theo:** PY-31 tính đạo hàm để biết loss thay đổi ra sao khi chỉnh tham số.

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

## 4. Khái niệm liên quan

**Nội dung chính:** loss đo mức sai giữa dự báo và mục tiêu. Bài học đi từ hai cách tính sai lệch trên số (**MSE**, **MAE**), tới cách kết hợp hai mức phạt (**Huber**), rồi sang loss trên **xác suất và phân phối** (**cross-entropy**, **KL**). Chọn loss phải dựa vào ý nghĩa dữ liệu và mức phạt cần thiết.

### 4.1. MSE — Sai số bình phương trung bình

**Từ vựng trong mục:** **MSE** — Mean Squared Error; **Residual** — sai lệch.

**Loss function** là hàm cho biết dự báo sai lệch đến mức nào so với mục tiêu, để ta đánh giá hoặc tối ưu mô hình. **MSE** lấy sai số `(dự báo−thực tế)`, bình phương từng sai số rồi **trung bình**. Với thực tế `[2,3]` và dự báo `[1,4]`, sai số là `[-1,+1]`, bình phương thành `[1,1]` và MSE bằng 1. Đơn vị MSE là **bình phương đơn vị đầu ra**, không phải cùng đơn vị như giá nhà.

```python
# Mục đích: Sai số bình phương trung bình.
import numpy as np

y_true = np.array([2, 3])
y_pred = np.array([1, 4])
print(np.mean((y_true - y_pred) ** 2))
```

**Kết quả khi chạy:**

```text
1.0
```

MSE bằng 1 đơn vị bình phương. Sai số lớn được phạt mạnh hơn vì bình phương.

### 4.2. MAE — Sai số tuyệt đối trung bình

**Từ vựng trong mục:** **MAE** — Mean Absolute Error; **Absolute error** — sai số tuyệt đối.

**MAE** lấy trị tuyệt đối của từng sai số rồi chia cho số quan sát. Ví dụ thực tế `[10,20,30]` và dự báo `[9,19,50]` có sai lệch tuyệt đối `[1,1,20]`, nên MAE bằng `22/3≈7.333`. Khác MSE, MAE có **cùng đơn vị** với đầu ra và không bình phương để khuếch đại lỗi lớn. Nó không có nghĩa là loại bỏ ảnh hưởng của ngoại lệ hoàn toàn.

```python
# Mục đích: Sai số tuyệt đối trung bình.
import numpy as np

y_true = np.array([10, 20, 30])
y_pred = np.array([9, 19, 50])
print(round(float(np.mean(np.abs(y_true - y_pred))), 3))
```

**Kết quả khi chạy:**

```text
7.333
```

Sai lệch trung bình tuyệt đối khoảng 7,333 đơn vị đo.

### 4.3. Huber — Trộn bình phương và tuyến tính theo ngưỡng

**Từ vựng trong mục:** **Huber loss** — tổn thất Huber; **Delta** — ngưỡng.

**Huber** dùng mức phạt giống **bình phương** khi `|e|≤δ` và chuyển sang **tuyến tính** khi lỗi vượt δ. Với δ=1: lỗi có độ lớn 1 mất 0.5, độ lớn 2 mất 1.5, độ lớn 5 mất 4.5. Trung bình ba lỗi `[-1,2,5]` là `6.5/3≈2.167`. Huber là cách cân bằng giữa MSE nhạy với lỗi lớn và MAE tăng tuyến tính; δ quyết định điểm chuyển và mang cùng đơn vị với sai số.

```python
# Mục đích: Trộn bình phương và tuyến tính theo ngưỡng.
import numpy as np

e = np.array([-1.0, 2.0, 5.0])
delta = 1.0
loss = np.where(
    np.abs(e) <= delta,
    0.5 * e ** 2,
    delta * (np.abs(e) - 0.5 * delta),
)
print(round(float(loss.mean()), 3))
```

**Kết quả khi chạy:**

```text
2.167
```

Tổn thất trung bình xấp xỉ 2,167 theo Huber δ=1; lỗi lớn không bị bình phương mãi.

### 4.4. Cross-entropy và KL — So nhãn hoặc phân phối

**Từ vựng trong mục:** **Cross-entropy** — entropy chéo; **KL divergence** — phân kỳ KL.

**Cross-entropy** đánh giá phân phối dự báo so với phân phối nhãn/đích. Với phân loại một nhãn đúng, dự báo xác suất cho nhãn đúng là 0.8 thì loss bằng `−ln(0.8)≈0.2231`: xác suất cho nhãn đúng càng thấp, phạt càng lớn. **KL divergence** `D_KL(P||Q)=Σ P_i ln(P_i/Q_i)` so sự khác nhau giữa **hai phân phối** P và Q; với `P=[0.5,0.5]`, `Q=[0.6,0.4]`, KL≈0.0204. KL **không đối xứng** và không phải khoảng cách hình học. Các xác suất trong log cần dương; trong code thực tế có thể clip hoặc xử lý giá trị 0 đúng quy ước.

```python
# Mục đích: So nhãn hoặc phân phối.
import numpy as np

p_true = 0.8
P = np.array([0.5, 0.5])
Q = np.array([0.6, 0.4])
print(round(float(-np.log(p_true)), 4))
print(round(float(np.sum(P * np.log(P / Q))), 4))
```

**Kết quả khi chạy:**

```text
0.2231
0.0204
```

Dòng đầu là cross-entropy của nhãn đúng; dòng sau là KL từ phân phối P sang Q. Hai số mang ý nghĩa khác nhau.

## 5. Năm tình huống Loss — từ MSE đến entropy chéo và KL trên nhiều mẫu

### Tình huống 1 — Cấp 1: Đánh giá dự báo 10 chuyến giao hàng bằng MSE

**Từ vựng trong mục:** **MSE** — trung bình bình phương sai số; **Residual** — sai lệch dự báo.

**Tình huống thực tế:** Đơn vị giao hàng lưu **10 chuyến**, mỗi chuyến có một thời gian giao **thực tế** và một thời gian do hệ thống **dự đoán**, cùng đơn vị **phút/chuyến**. Ví dụ chuyến đầu thực tế 20 phút nhưng dự đoán 21 phút. Người quản lý muốn biết mô hình dự báo lệch bao nhiêu xét chung cả 10 chuyến bằng **MSE**, và chuyến nào đó có độ lệch tuyệt đối lớn nhất bao nhiêu phút; chưa cần điều chỉnh mô hình.

**Vì sao chọn cách này?** **Loss (hàm mất mát)** là cách đo mức dự đoán **khác kết quả thật** để đánh giá mô hình. Trước tiên chương trình trừ thời gian thực tế khỏi dự đoán của **từng chuyến**; chênh lệch có thể âm hoặc dương. **MSE** lấy bình phương từng chênh lệch rồi tính trung bình nên các sai lệch lớn ảnh hưởng mạnh hơn; đơn vị kết quả là **phút bình phương (phút²)**, không phải phút giao hàng. `np.abs()` bỏ dấu âm khi tìm **sai số tuyệt đối lớn nhất**, giá trị này mới có đơn vị phút. Không thể nhìn MSE rồi nói trung bình mô hình sai từng ấy phút.

**Quy trình:**
1. Tạo hai dãy 10 thời gian theo cùng thứ tự chuyến.
2. Trừ hai dãy để nhận sai số, bình phương rồi lấy trung bình.
3. In MSE và sai lệch tuyệt đối lớn nhất để đối chiếu.

```python
import numpy as np
actual_minutes = np.array([20,23,25,28,30,32,34,35,37,40], dtype=float)
predicted_minutes = np.array([21,22,24,30,31,30,36,35,39,38], dtype=float)
errors = predicted_minutes - actual_minutes
if actual_minutes.shape != (10,) or predicted_minutes.shape != (10,):
    raise ValueError("Cần đủ 10 thời gian thực tế và dự đoán.")
print("Chuyến:", len(actual_minutes))
print(f"MSE (phút²): {np.mean(errors ** 2):.2f}")
print("Sai số lớn nhất (phút):", int(np.max(np.abs(errors))))
```

**Kết quả khi chạy:**

```text
Chuyến: 10
MSE (phút²): 2.40
Sai số lớn nhất (phút): 2
```

MSE tính trên **cùng 10 chuyến**; không được trộn sai thứ tự thực tế và dự báo khi đánh giá.

### Tình huống 2 — Cấp 2: So MAE và MSE khi 12 số đo có một ngoại lệ lớn

**Từ vựng trong mục:** **MAE** — sai số tuyệt đối trung bình; **Outlier** — ngoại lệ; **Comparison** — so sánh.

**Tình huống thực tế:** Phòng kiểm định có **12 lần cân**, mỗi lần gồm khối lượng thực tế và dự đoán, tính bằng **gam (g)**. Mười một lần dự đoán lệch khoảng **2 g**, nhưng ở lần thứ chín hệ thống dự đoán 230 g thay vì 180 g, lệch **50 g**. Người kiểm định muốn so mức sai lệch khi tính bằng **MAE** với **MSE** để hiểu vì sao một lần đo bị lỗi lớn có thể ảnh hưởng mạnh tới đánh giá chung.

**Vì sao chọn cách này?** **MAE** là trung bình **độ lớn sai lệch**, không quan tâm dự báo cao hay thấp hơn thực tế; kết quả vẫn tính bằng **gam**. **MSE** bình phương sai lệch trước khi lấy trung bình nên trường hợp **50 g** đóng góp mạnh hơn nhiều so với mỗi lượt lệch 2 g; kết quả có đơn vị **g²**. Chương trình tính cả hai trên **cùng 12 lượt**, đồng thời đếm lượt sai hơn 10 g. Hai con số MAE và MSE **khác đơn vị**, nên không so số lớn nhỏ của chúng để chọn mô hình tốt hơn; phải hiểu mục đích phạt lỗi và dùng cùng thước đo khi so các mô hình.

**Quy trình:**
1. Tạo 12 cặp số đo–dự báo, có đúng một ngoại lệ 50 g.
2. Tính sai số tuyệt đối và bình phương trên từng hàng.
3. Báo MAE, MSE và số điểm có lỗi lớn hơn 10 g.

```python
import numpy as np
actual_g = np.array([100,110,120,130,140,150,160,170,180,190,200,210], dtype=float)
predicted_g = np.array([102,108,122,128,142,148,162,168,230,188,202,208], dtype=float)
e = predicted_g - actual_g
if len(e) != 12:
    raise ValueError("Cần đúng 12 lỗi cân đo.")
print("Lượt đo:", len(e))
print(f"MAE (g): {np.mean(np.abs(e)):.2f}")
print(f"MSE (g²): {np.mean(e ** 2):.2f}")
print("Lỗi > 10 g:", int((np.abs(e) > 10).sum()))
```

**Kết quả khi chạy:**

```text
Lượt đo: 12
MAE (g): 6.00
MSE (g²): 212.00
Lỗi > 10 g: 1
```

MAE không loại bỏ sự cố ngoại lệ; nó chỉ **không bình phương** sự cố ấy như MSE.

### Tình huống 3 — Cấp 3: Dùng Huber cho 15 sai lệch cảm biến có hai lỗi bất thường

**Từ vựng trong mục:** **Huber** — hàm mất mát lai; **Delta** — ngưỡng; **Robustness** — giảm độ nhạy với ngoại lệ.

**Tình huống thực tế:** Một trạm dự báo nhiệt độ ghi **15 sai lệch**, mỗi số là nhiệt độ dự đoán trừ giá trị chuẩn, đơn vị **°C**. Hầu hết sai số nhỏ nhưng có hai lượt lệch **+8 °C** và **-7 °C**. Đội kỹ thuật chọn **mức chuyển δ = 1 °C** trong phép đo Huber minh họa, muốn đếm số lần sai lệch vượt ngưỡng này và xem Huber trung bình khác MAE ra sao trên đúng 15 lượt.

**Vì sao chọn cách này?** **Huber loss** là một cách phạt sai lệch có hai vùng: khi sai lệch nhỏ thì phạt theo kiểu **bình phương** để nhạy với việc cải thiện gần đúng, còn khi sai lệch lớn thì chuyển sang tăng **gần tuyến tính** để ngoại lệ không chi phối mạnh như MSE. **δ = 1 °C** là ngưỡng chuyển giữa hai cách phạt do bài tập chọn, không phải ngưỡng an toàn của trạm đo. `np.abs(errors_c)` lấy độ lớn 15 sai số; `np.where(...)` chọn mức phạt tương ứng **cho từng lượt**, kể cả hai lượt +8 °C và -7 °C. Huber trung bình và MAE dùng cách phạt khác nhau, nên cần ghi tên phương pháp khi báo kết quả; không coi số Huber là nhiệt độ trung bình của cảm biến.

**Quy trình:**
1. Lưu 15 sai số có dấu và đặt ngưỡng Huber δ=1.
2. Áp từng nhánh theo trị tuyệt đối của sai số bằng `np.where`.
3. In Huber, MAE và số lượt có trị lỗi vượt δ.

```python
import numpy as np
errors_c = np.array([-1,1,-2,0,0.5,-0.5,1.5,-1.5,2,0,0.2,-0.2,8,-7,1], dtype=float)
delta = 1.0
abserr = np.abs(errors_c)
huber = np.where(abserr <= delta,
                 0.5 * errors_c**2,
                 delta * (abserr - 0.5 * delta))
if errors_c.size != 15:
    raise ValueError("Cần đúng 15 sai số nhiệt độ.")
print("Số đo:", len(errors_c))
print("Lỗi > δ:", int((abserr > delta).sum()))
print(f"Huber trung bình: {huber.mean():.3f}")
print(f"MAE (°C): {abserr.mean():.3f}")
```

**Kết quả khi chạy:**

```text
Số đo: 15
Lỗi > δ: 6
Huber trung bình: 1.386
MAE (°C): 1.760
```

Ví dụ chỉ minh họa lựa chọn loss; dữ liệu thực cần điều chỉnh δ dựa trên thang đo và mục tiêu học máy.

### Tình huống 4 — Cấp 4: Cross-entropy của 18 nhãn trong bài toán ba lớp

**Từ vựng trong mục:** **Cross-entropy** — entropy chéo; **True-class probability** — xác suất lớp đúng; **Clipping** — chặn biên số.

**Tình huống thực tế:** Nhóm phân loại ảnh có **18 ảnh thử**, mỗi ảnh được gắn một **nhãn đúng** thuộc A, B hoặc C và một **điểm mô hình gán cho chính lớp đúng**, nằm trong khoảng 0 đến 1. Ở ảnh thứ sáu và mười lăm, điểm dành cho lớp đúng rất nhỏ (**0,05** và **0,01**). Người phân tích muốn tính **cross-entropy trung bình**, tìm ảnh bị phạt nặng nhất và tránh lỗi máy tính nếu một mô hình khác gán điểm bằng 0.

**Vì sao chọn cách này?** **Cross-entropy** trong bài đo mức mô hình **không tin vào lớp thật** đến đâu: điểm của lớp đúng càng nhỏ thì **mức phạt càng lớn**. Ví dụ ảnh có lớp thật là B mà mô hình chỉ gán điểm 0,01 cho B sẽ bị phạt nặng hơn ảnh có điểm 0,75 cho lớp đúng. Chương trình dùng `-np.log(...)` để đổi điểm của lớp đúng thành loss, rồi lấy trung bình **18 ảnh**; `argmax()` tìm **vị trí ảnh bị phạt lớn nhất**. `np.clip(..., 1e-12, 1)` giới hạn giá trị trước khi lấy log vì `log(0)` không xác định; đây là **bảo vệ tính toán**, không phải cách sửa một dự báo kém thành dự báo đúng. Nhãn 0/1/2 dùng để nhận diện lớp, không phải số tiền hay điểm số.

**Quy trình:**
1. Tạo 18 nhãn đúng và điểm của lớp đúng tương ứng.
2. Clip điểm trong khoảng an toàn rồi lấy `-log`.
3. Tìm mất mát trung bình và mã mẫu có loss lớn nhất.

```python
import numpy as np
labels = np.array([0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2], dtype=int)
true_class_scores = np.array([0.55,0.6000000000000001,0.65,0.7000000000000001,0.75,0.05,0.6000000000000001,0.65,0.7000000000000001,0.75,0.55,0.6000000000000001,0.65,0.7000000000000001,0.01,0.55,0.6000000000000001,0.65], dtype=float)
losses = -np.log(np.clip(true_class_scores, 1e-12, 1.0))
worst = int(losses.argmax())
if labels.shape != (18,) or true_class_scores.shape != (18,):
    raise ValueError("Cần 18 nhãn và 18 xác suất của nhãn đúng.")
if not np.all((labels >= 0) & (labels < 3)):
    raise ValueError("Nhãn chỉ được là 0, 1 hoặc 2.")
print("Mẫu:", len(labels))
print(f"Cross-entropy TB: {losses.mean():.3f}")
print("Loss lớn nhất:", f"M{worst+1:02d}")
print(f"Loss mẫu lớn nhất: {losses[worst]:.3f}")
```

**Kết quả khi chạy:**

```text
Mẫu: 18
Cross-entropy TB: 0.823
Loss lớn nhất: M15
Loss mẫu lớn nhất: 4.605
```

Điểm softmax chưa chắc là xác suất đã hiệu chuẩn. Vì thế đây là đánh giá loss trên dữ liệu minh họa, không phải chứng minh chất lượng mô hình.

### Tình huống 5 — Cấp 5: Kiểm KL divergence của 20 phân phối dự báo và phân biệt chiều so sánh

**Từ vựng trong mục:** **KL divergence** — phân kỳ KL; **Probability distribution** — phân phối; **Asymmetry** — không đối xứng.

**Tình huống thực tế:** Đội kiểm thử có **20 bộ dự báo ba lớp A/B/C**. Mỗi bộ gồm ba số dương có tổng bằng 1, gọi là phân phối **Q**; nhóm lấy một phân phối chuẩn **P = [0,5; 0,3; 0,2]** để đối chiếu. Trong 20 bộ có các dòng Q trùng P và các dòng lệch dần. Họ muốn tính độ khác nhau theo **KL(P‖Q)**, xem khi hai phân phối giống nhau thì kết quả ra sao, và kiểm tra vì sao đổi thứ tự thành **KL(Q‖P)** có thể cho kết quả khác.

**Vì sao chọn cách này?** **Phân phối xác suất** ở đây là ba mức tỷ lệ cho ba nhóm, mỗi số dương và **cả ba cộng lại bằng 1**. **KL divergence** đo mức khác nhau của Q **khi dùng P làm phân phối tham chiếu**, nhưng cách đo này **có hướng**: so P với Q không nhất thiết bằng so Q với P. Chương trình kiểm tra mọi Q có đủ ba giá trị dương, tổng từng hàng gần bằng 1, rồi tính KL cho **20 hàng độc lập**, không gộp 20 hàng thành một phân phối. Khi Q đúng bằng P, KL bằng **0**; kết quả lý thuyết không âm, sai số âm cực nhỏ có thể do máy tính. Không gọi KL là **khoảng cách hình học đối xứng** hay tự hiểu KL là tỷ lệ dự báo chính xác.

**Quy trình:**
1. Tạo P một hàng chuẩn và 20 phân phối Q đều hợp lệ.
2. Tính log theo từng cột, cộng theo hàng để có 20 giá trị `KL(P||Q)`.
3. Đối chiếu dòng Q=P, trung bình và hai chiều trên dòng khác P.

```python
import numpy as np
P = np.array([0.5,0.3,0.2], dtype=float)
Q = np.array([[0.5,0.3,0.2],[0.525,0.2875,0.1875],[0.55,0.27499999999999997,0.17500000000000002],[0.575,0.26249999999999996,0.1625],[0.6,0.25,0.15000000000000002],[0.5,0.3,0.2],[0.525,0.2875,0.1875],[0.55,0.27499999999999997,0.17500000000000002],[0.575,0.26249999999999996,0.1625],[0.6,0.25,0.15000000000000002],[0.5,0.3,0.2],[0.525,0.2875,0.1875],[0.55,0.27499999999999997,0.17500000000000002],[0.575,0.26249999999999996,0.1625],[0.6,0.25,0.15000000000000002],[0.5,0.3,0.2],[0.525,0.2875,0.1875],[0.55,0.27499999999999997,0.17500000000000002],[0.575,0.26249999999999996,0.1625],[0.6,0.25,0.15000000000000002]], dtype=float)
if Q.shape != (20, 3) or not np.all(Q > 0):
    raise ValueError("Cần 20 phân phối ba nhãn có xác suất dương.")
if not np.allclose(Q.sum(axis=1), 1.0):
    raise ValueError("Tổng xác suất của mỗi phân phối phải gần bằng 1.")
kl_pq = np.sum(P * np.log(P / Q), axis=1)
kl_qp = np.sum(Q * np.log(Q / P), axis=1)
print("Bộ phân phối:", len(Q))
print(f"KL đầu (P||Q): {kl_pq[0]:.4f}")
print(f"KL TB (P||Q): {kl_pq.mean():.4f}")
print("Hai chiều có thể khác:", bool(abs(kl_pq[1] - kl_qp[1]) > 1e-9))
print("Không âm:", bool(np.all(kl_pq >= -1e-12)))
```

**Kết quả khi chạy:**

```text
Bộ phân phối: 20
KL đầu (P||Q): 0.0000
KL TB (P||Q): 0.0078
Hai chiều có thể khác: True
Không âm: True
```

KL không đối xứng, và một giá trị nhỏ không tự nói hai phân phối phù hợp mục tiêu vận hành thật. Khi Q có xác suất 0, cần một quy ước xử lý riêng để tránh log không xác định.

## 6. Sai lầm thường gặp

- **MSE** có đơn vị đầu ra bình phương, **MAE** có đơn vị gốc; không đọc MSE như mức lệch tiền trung bình.
- Huber cần ngưỡng δ phù hợp đơn vị sai số; ngưỡng này quyết định khi nào chuyển từ phạt bình phương sang tuyến tính.
- Cross-entropy với nhãn đúng cần xác suất **của lớp đúng**, không phải điểm lớn nhất bất kỳ.
- `log(0)` không xác định; phải xử lý xác suất bằng công thức ổn định hoặc clip phù hợp khi dùng NumPy đơn giản.
- KL **bất đối xứng**, không phải khoảng cách Euclid và chỉ có nghĩa với các phân phối hợp lệ.
- Loss huấn luyện thấp không thay thế việc đánh giá trên tập validation/test độc lập.

## 7. Trắc nghiệm

**Chỉ hỏi kiến thức lý thuyết, so sánh loss và đọc công thức, không hỏi dữ liệu tình huống.**

**Q1. What is MSE? | MSE là gì?**

A. Mean squared prediction error | Trung bình sai số dự báo bình phương

B. Mean absolute prediction error | Trung bình trị tuyệt đối sai số

C. Quadratic for small errors and linear for large | Bình phương lỗi nhỏ, tuyến tính lỗi lớn

D. Compare two probability distributions in a directed way | So hai phân phối xác suất có phân biệt chiều

**Đáp án: A**

**Giải thích:** MSE lấy trung bình bình phương sai lệch.


**Q2. What is MAE? | MAE là gì?**

A. Mean squared prediction error | Trung bình sai số dự báo bình phương

B. Mean absolute prediction error | Trung bình trị tuyệt đối sai số

C. Quadratic for small errors and linear for large | Bình phương lỗi nhỏ, tuyến tính lỗi lớn

D. Compare two probability distributions in a directed way | So hai phân phối xác suất có phân biệt chiều

**Đáp án: B**

**Giải thích:** MAE lấy trung bình độ lệch tuyệt đối.


**Q3. What characterizes Huber loss? | Đặc trưng của Huber loss là gì?**

A. Mean squared prediction error | Trung bình sai số dự báo bình phương

B. Mean absolute prediction error | Trung bình trị tuyệt đối sai số

C. Quadratic for small errors and linear for large | Bình phương lỗi nhỏ, tuyến tính lỗi lớn

D. Compare two probability distributions in a directed way | So hai phân phối xác suất có phân biệt chiều

**Đáp án: C**

**Giải thích:** Huber đổi tốc độ tăng mức phạt sau một ngưỡng.


**Q4. What is KL divergence used for? | KL divergence dùng để làm gì?**

A. Mean squared prediction error | Trung bình sai số dự báo bình phương

B. Mean absolute prediction error | Trung bình trị tuyệt đối sai số

C. Quadratic for small errors and linear for large | Bình phương lỗi nhỏ, tuyến tính lỗi lớn

D. Compare two probability distributions in a directed way | So hai phân phối xác suất có phân biệt chiều

**Đáp án: D**

**Giải thích:** KL dùng tỷ số logarit theo một chiều giữa các phân phối.


**Q5. What does categorical cross-entropy penalize? | Categorical cross-entropy phạt điều gì?**

A. Low predicted probability for the correct label | Xác suất dự đoán thấp cho nhãn đúng

B. `mean((y-pred)**2)` | `mean((y-pred)**2)`

C. `mean(abs(y-pred))` | `mean(abs(y-pred))`

D. `delta` | `delta`

**Đáp án: A**

**Giải thích:** Lớp đúng cần được gán xác suất cao.


**Q6. Which formula computes MSE? | Công thức nào tính MSE?**

A. Low predicted probability for the correct label | Xác suất dự đoán thấp cho nhãn đúng

B. `mean((y-pred)**2)` | `mean((y-pred)**2)`

C. `mean(abs(y-pred))` | `mean(abs(y-pred))`

D. `delta` | `delta`

**Đáp án: B**

**Giải thích:** Bình phương từng sai lệch trước khi trung bình.


**Q7. Which formula computes MAE? | Công thức nào tính MAE?**

A. Low predicted probability for the correct label | Xác suất dự đoán thấp cho nhãn đúng

B. `mean((y-pred)**2)` | `mean((y-pred)**2)`

C. `mean(abs(y-pred))` | `mean(abs(y-pred))`

D. `delta` | `delta`

**Đáp án: C**

**Giải thích:** Lấy trị tuyệt đối từng sai lệch rồi trung bình.


**Q8. Which parameter sets Huber's transition point? | Tham số nào đặt điểm chuyển Huber?**

A. Low predicted probability for the correct label | Xác suất dự đoán thấp cho nhãn đúng

B. `mean((y-pred)**2)` | `mean((y-pred)**2)`

C. `mean(abs(y-pred))` | `mean(abs(y-pred))`

D. `delta` | `delta`

**Đáp án: D**

**Giải thích:** Delta phân chia hai miền của Huber.


**Q9. What does `−log(p_true)` represent for one correct class? | `−log(p_true)` biểu thị gì cho một nhãn đúng?**

A. Cross-entropy loss for that sample | Cross-entropy của mẫu đó

B. Nonnegative | Không âm

C. No, KL is asymmetric | Không, KL bất đối xứng

D. The distributions are identical | Hai phân phối giống nhau

**Đáp án: A**

**Giải thích:** Với one-hot, chỉ còn hạng log của lớp đúng.


**Q10. What is the sign of KL divergence for valid distributions? | KL divergence có dấu gì với phân phối hợp lệ?**

A. Cross-entropy loss for that sample | Cross-entropy của mẫu đó

B. Nonnegative | Không âm

C. No, KL is asymmetric | Không, KL bất đối xứng

D. The distributions are identical | Hai phân phối giống nhau

**Đáp án: B**

**Giải thích:** KL không âm theo bất đẳng thức Gibbs.


**Q11. Does swapping P and Q generally preserve KL? | Đổi chỗ P và Q có giữ nguyên KL không?**

A. Cross-entropy loss for that sample | Cross-entropy của mẫu đó

B. Nonnegative | Không âm

C. No, KL is asymmetric | Không, KL bất đối xứng

D. The distributions are identical | Hai phân phối giống nhau

**Đáp án: C**

**Giải thích:** D(P‖Q) và D(Q‖P) có thể khác.


**Q12. What does a zero KL divergence mean for valid finite distributions? | KL bằng 0 nghĩa là gì với các phân phối hữu hạn hợp lệ?**

A. Cross-entropy loss for that sample | Cross-entropy của mẫu đó

B. Nonnegative | Không âm

C. No, KL is asymmetric | Không, KL bất đối xứng

D. The distributions are identical | Hai phân phối giống nhau

**Đáp án: D**

**Giải thích:** KL bằng 0 khi các phân phối trùng nhau trong điều kiện phù hợp.


**Q13. What is the unit of MSE when predictions are in meters? | Dự báo theo mét thì MSE có đơn vị gì?**

A. Square meters | Mét bình phương

B. Meters | Mét

C. MSE | MSE

D. Huber loss | Huber loss

**Đáp án: A**

**Giải thích:** Bình phương sai lệch mét cho đơn vị m².


**Q14. What is the unit of MAE when predictions are in meters? | Dự báo theo mét thì MAE có đơn vị gì?**

A. Square meters | Mét bình phương

B. Meters | Mét

C. MSE | MSE

D. Huber loss | Huber loss

**Đáp án: B**

**Giải thích:** Sai lệch tuyệt đối giữ đơn vị gốc.


**Q15. Which loss increases quadratically with error magnitude? | Loss nào tăng theo bình phương độ lớn lỗi?**

A. Square meters | Mét bình phương

B. Meters | Mét

C. MSE | MSE

D. Huber loss | Huber loss

**Đáp án: C**

**Giải thích:** MSE bình phương độ lớn lỗi.


**Q16. Which regression loss has a threshold between quadratic and linear penalties? | Loss hồi quy nào có ngưỡng chuyển bình phương sang tuyến tính?**

A. Square meters | Mét bình phương

B. Meters | Mét

C. MSE | MSE

D. Huber loss | Huber loss

**Đáp án: D**

**Giải thích:** Huber chuyển miền tại delta.


**Q17. Why clip predicted probabilities before a naive log implementation? | Vì sao clip xác suất trước khi lấy log bằng công thức đơn giản?**

A. To avoid log(0) and numerical infinities | Để tránh log(0) và vô cực số học

B. MAE | MAE

C. No, evaluate on held-out data | Không, cần đánh giá trên dữ liệu độc lập

D. Predicted probability assigned to the true class | Xác suất dự báo dành cho lớp đúng

**Đáp án: A**

**Giải thích:** Xác suất 0 gây kỳ dị log trong công thức số học đơn giản.


**Q18. Which loss is easier to interpret in the original output units? | Loss nào dễ đọc theo đơn vị đầu ra ban đầu?**

A. To avoid log(0) and numerical infinities | Để tránh log(0) và vô cực số học

B. MAE | MAE

C. No, evaluate on held-out data | Không, cần đánh giá trên dữ liệu độc lập

D. Predicted probability assigned to the true class | Xác suất dự báo dành cho lớp đúng

**Đáp án: B**

**Giải thích:** MAE báo sai số trung bình cùng đơn vị đo.


**Q19. Does a lower training loss guarantee better unseen-data performance? | Training loss thấp có bảo đảm dự đoán tốt trên dữ liệu mới?**

A. To avoid log(0) and numerical infinities | Để tránh log(0) và vô cực số học

B. MAE | MAE

C. No, evaluate on held-out data | Không, cần đánh giá trên dữ liệu độc lập

D. Predicted probability assigned to the true class | Xác suất dự báo dành cho lớp đúng

**Đáp án: C**

**Giải thích:** Khả năng tổng quát cần kiểm chứng bằng dữ liệu độc lập.


**Q20. For one-hot labels, what information matters in cross-entropy? | Với nhãn one-hot, điều gì quyết định cross-entropy?**

A. To avoid log(0) and numerical infinities | Để tránh log(0) và vô cực số học

B. MAE | MAE

C. No, evaluate on held-out data | Không, cần đánh giá trên dữ liệu độc lập

D. Predicted probability assigned to the true class | Xác suất dự báo dành cho lớp đúng

**Đáp án: D**

**Giải thích:** Âm log-likelihood dùng xác suất lớp đúng.

## 8. Bài tiếp theo

`Dự đoán → Sai số → Loss → Tối ưu hóa`.
