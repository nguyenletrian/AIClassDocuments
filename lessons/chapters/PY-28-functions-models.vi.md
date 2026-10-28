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

**No Note — Không chú thích**

```python
def delivery_fee(km):
    return 5 * km + 10

print(delivery_fee(3))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Dùng hàm bậc nhất để tính phí giao hàng tăng đều theo quãng đường.
# Dữ liệu: km là số kilômét, phí có đơn vị minh họa nghìn đồng, phí nền 10 và thêm 5 mỗi km.
# def định nghĩa hàm nhận quãng đường km; return trả phí để nơi gọi sử dụng.
def delivery_fee(km):
    # 5 là phí mỗi km, +10 là phần cố định; mỗi km tăng thêm đúng 5 nên đây là quan hệ tuyến tính.
    return 5 * km + 10

# Gọi hàm với quãng đường 3 km, print() hiển thị 25 nghìn đồng.
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

**No Note — Không chú thích**

```python
def cost(load):
    return 2 * load ** 2 + 3 * load + 10

print(cost(4))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Minh họa chi phí bậc hai tăng nhanh hơn khi tải ngày càng lớn.
# Dữ liệu: load là mức tải không âm theo đơn vị giả lập, cost là điểm chi phí giả lập.
# Định nghĩa hàm nhận mức tải, trả giá trị chi phí tương ứng.
def cost(load):
    # **2 bình phương mức tải tạo độ cong: tăng thêm 1 tải về sau tốn nhiều hơn lúc đầu.
    # Gồm chi phí bậc hai, thành phần tăng đều và chi phí nền 10.
    return 2 * load ** 2 + 3 * load + 10

# Gọi mức tải 4; print() cho chi phí của đúng đầu vào này.
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

**No Note — Không chú thích**

```python
import numpy as np

x = np.array([0, 1, 2])
print(np.polyval([1, 0, 2], x))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Dùng np.polyval() tính một đa thức bậc hai trên ba đầu vào cùng lúc.
# Dữ liệu: x là vector [0,1,2], hệ số [1,0,2] biểu diễn x² + 0*x +2 theo thứ tự bậc cao xuống thấp.
# NumPy hỗ trợ tính đa thức vector hóa trên nhiều x.
import numpy as np

# Mảng x chứa ba điểm cần tính chung.
x = np.array([0, 1, 2])
# polyval(hệ_số,x) tính đa thức; hệ số theo LŨY THỪA GIẢM DẦN (x², x, hằng), trả mảng kết quả cho từng x.
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

**No Note — Không chú thích**

```python
initial = 1000
rate = 0.05
periods = 3
print(round(initial * (1 + rate) ** periods, 2))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Minh họa tăng trưởng lũy kế khi mỗi kỳ cộng cùng một tỷ lệ trên tổng mới.
# Dữ liệu: Giá trị đầu 1000 đơn vị, rate=0.05 là 5%/kỳ, periods=3 kỳ.
# Số dư ban đầu trước khi nhân theo từng kỳ.
initial = 1000
# 0.05 tương ứng 5% mỗi kỳ, không phải tăng 5 đơn vị.
rate = 0.05
# Ba lần áp dụng tỷ lệ tăng trên giá trị vừa có được.
periods = 3
# 1+rate là hệ số tăng 1.05 mỗi kỳ; **3 nhân lặp hệ số ba lần (lãi kép).
# round(...,2) làm tròn kết quả HIỂN THỊ hai chữ số thập phân, không ảnh hưởng đầu vào.
print(round(initial * (1 + rate) ** periods, 2))
```

**Kết quả khi chạy:**

```text
1157.63
```

Sau ba kỳ tăng trưởng lũy kế, chỉ số khoảng 1157,63 đơn vị, không phải giá trị dự báo chắc chắn.

## 5. Năm tình huống hàm số — từ mô hình tuyến tính đến so khớp đường cong

### Tình huống 1 — Cấp 1: Tính phí giao hàng cho 10 chuyến bằng hàm bậc nhất

**Từ vựng trong mục:** **Affine function** — hàm bậc nhất có hệ số chặn; **Slope** — độ dốc.

**Tình huống thực tế:** Đơn vị giao hàng có **10 chuyến**, mỗi chuyến có quãng đường lần lượt từ **1 đến 10 km**. Theo bảng phí **giả lập**, mỗi chuyến thu **10 nghìn đồng phí khởi đầu** và **5 nghìn đồng cho mỗi km**, không có phụ phí khác. Thu ngân muốn biết phí chuyến dài 1 km và tổng tiền của cả 10 chuyến mà không phải viết riêng một phép tính cho từng chuyến.

**Vì sao chọn cách này?** **Hàm số** mô tả một quy tắc biến đầu vào thành đầu ra: `delivery_fee(km)` nhận **số km** rồi trả **số tiền nghìn đồng**. Quy tắc này **tuyến tính**, vì mỗi thêm 1 km làm phí tăng đúng 5 nghìn đồng, còn khoản 10 nghìn là phí nền ngay cả trước khi tính quãng đường. Dùng `def` viết quy tắc **một lần**, vòng `for` gọi lại cho mười quãng đường rồi cộng kết quả. Chuyến 1 km phải gồm cả phí nền và phí theo km; nếu chỉ nhân số km với 5 thì sẽ bỏ quên phí cố định.

**Quy trình:**
1. Tạo list 10 số km và hàm phí đơn giản.
2. Áp dụng hàm cho từng chuyến, giữ đúng đơn vị.
3. Báo số chuyến, phí đầu và tổng cộng.

**No Note — Không chú thích**

```python
distances_km = [1,2,3,4,5,6,7,8,9,10]
def delivery_fee(km):
    return 10 + 5 * km
fees = []
for km in distances_km:
    fees.append(delivery_fee(km))
if len(fees) != 10:
    raise ValueError("Cần tính phí đủ 10 chuyến.")
print("Chuyến:", len(fees))
print("Phí chuyến đầu (nghìn đồng):", fees[0])
print("Tổng phí (nghìn đồng):", sum(fees))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tính giá giao hàng cho 10 chuyến theo km bằng hàm phí tuyến tính.
# Dữ liệu: 10 chuyến có quãng đường 1..10 km, giá nền 10 và giá theo km 5 nghìn đồng.
# List khoảng cách 10 chuyến, mỗi số là km của một đơn.
distances_km = [1,2,3,4,5,6,7,8,9,10]
# Hàm trả phí nghìn đồng cho quãng đường km; không tự in kết quả.
def delivery_fee(km):
    # Tiền nền 10 nghìn đồng và 5 nghìn đồng cho mỗi km.
    return 10 + 5 * km
# List kết quả phí mỗi chuyến, theo cùng thứ tự nguồn.
fees = []
# Duyệt 10 khoảng cách, gọi một lần mỗi chuyến.
for km in distances_km:
    # append() nhận giá trị return của hàm và lưu vào list.
    fees.append(delivery_fee(km))
# len() kiểm đã tính đủ 10 lượt, ValueError báo thiếu chuyến.
if len(fees) != 10:
    # ValueError báo số lượng hoặc shape không đủ yêu cầu, tránh dùng kết quả chưa kiểm chứng.
    raise ValueError("Cần tính phí đủ 10 chuyến.")
print("Chuyến:", len(fees))
# [0] là tiền chuyến đầu tiên, không phải tổng mọi chuyến.
print("Phí chuyến đầu (nghìn đồng):", fees[0])
# sum() cộng phí của tất cả 10 chuyến, đơn vị nghìn đồng.
print("Tổng phí (nghìn đồng):", sum(fees))
```

**Kết quả khi chạy:**

```text
Chuyến: 10
Phí chuyến đầu (nghìn đồng): 15
Tổng phí (nghìn đồng): 375
```

Hệ số 5 có đơn vị **nghìn đồng/km**, không phải 5 km; chính sách này chỉ là dữ liệu minh họa.

### Tình huống 2 — Cấp 2: Nhận biết chi phí bậc hai từ 12 mức tải

**Từ vựng trong mục:** **Quadratic** — hàm bậc hai; **Marginal increase** — mức tăng giữa hai bước.

**Tình huống thực tế:** Xưởng thử máy có **12 mức tải** được đánh số từ 1 đến 12; mỗi mức tạo một chi phí **nghìn đồng** theo quy tắc minh họa. Khi tải tăng cao, chi phí tăng nhanh hơn chứ không tăng đều cùng một số tiền. Người vận hành muốn so phần chi phí tăng **từ tải 1 lên 2** với **từ tải 11 lên 12** để hiểu vì sao không thể dùng một mức tăng cố định cho mọi mức tải.

**Vì sao chọn cách này?** **Hàm bậc hai** có phần phụ thuộc vào **bình phương mức tải**, nên khi tải càng cao thì cùng một bước tăng tải có thể làm chi phí tăng **nhiều hơn trước**. Hàm `expense(load)` trong bài còn có phần tăng đều theo tải và phí nền; ba phần cùng tạo ra giá dự kiến. Vòng lặp tính đủ 12 mức, rồi chương trình lấy **chi phí tải 2 trừ tải 1** và **chi phí tải 12 trừ tải 11** để so hai lần tăng. Đây là mô hình giả lập để hiểu hình dạng hàm, không phải chi phí tiêu thụ của một máy thật.

**Quy trình:**
1. Tạo 12 mức tải và áp dụng hàm chi phí.
2. Lấy hiệu chi phí giữa các mức tải kề nhau.
3. In chi phí ở hai đầu và hai mức tăng để giải thích độ cong.

**No Note — Không chú thích**

```python
loads = [1,2,3,4,5,6,7,8,9,10,11,12]
def expense(load):
    return 2 * load ** 2 + 3 * load + 10
costs = []
for load in loads:
    costs.append(expense(load))
if len(costs) != 12:
    raise ValueError("Cần tính chi phí đủ 12 mức tải.")
print("Mức tải:", len(loads))
print("Tải 1:", costs[0])
print("Tải 12:", costs[-1])
print("Tăng 1→2:", costs[1] - costs[0])
print("Tăng 11→12:", costs[-1] - costs[-2])
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Cho thấy hàm bậc hai làm chi phí tăng theo mức tải nhanh dần trên 12 mức.
# Dữ liệu: 12 mức tải nguyên 1..12; output là chi phí số giả lập, không phải hóa đơn thực tế.
# List 12 mức tải ngày càng tăng để so mức tăng chi phí.
loads = [1,2,3,4,5,6,7,8,9,10,11,12]
# Hàm tự định nghĩa nhận một mức tải và trả chi phí tại mức đó.
def expense(load):
    # Bình phương load làm phần chi phí tăng theo độ lớn của tải, khác hàm bậc nhất tăng cố định.
    # Gồm phần bậc hai, phần tuyến tính và mức nền 10.
    return 2 * load ** 2 + 3 * load + 10
costs = []
for load in loads:
    # append() giữ chi phí từng tải theo thứ tự loads.
    costs.append(expense(load))
if len(costs) != 12:
    # ValueError báo số lượng hoặc shape không đủ yêu cầu, tránh dùng kết quả chưa kiểm chứng.
    raise ValueError("Cần tính chi phí đủ 12 mức tải.")
print("Mức tải:", len(loads))
# [0] phí mức tải 1; [-1] phí tải 12 (chỉ số âm lấy phần tử cuối).
print("Tải 1:", costs[0])
# [-1] là phí cuối, [-2] phí áp chót; hiệu hai ô cho mức tăng tải 11→12.
print("Tải 12:", costs[-1])
# [0] phí mức tải 1; [-1] phí tải 12 (chỉ số âm lấy phần tử cuối).
# Chênh lệch tải 1→2 để đối chiếu với mức 11→12: không cố định vì hàm bậc hai.
print("Tăng 1→2:", costs[1] - costs[0])
# [-1] là phí cuối, [-2] phí áp chót; hiệu hai ô cho mức tăng tải 11→12.
print("Tăng 11→12:", costs[-1] - costs[-2])
```

**Kết quả khi chạy:**

```text
Mức tải: 12
Tải 1: 15
Tải 12: 334
Tăng 1→2: 9
Tăng 11→12: 49
```

Chi phí trong bài là số **giả lập**, không phải quy luật tiêu hao được đo của một máy thực tế.

### Tình huống 3 — Cấp 3: Đánh giá đa thức trên 15 vị trí cảm biến

**Từ vựng trong mục:** **Polynomial** — đa thức; **polyval** — đánh giá đa thức; **Coefficient order** — thứ tự hệ số.

**Tình huống thực tế:** Thiết bị hiệu chỉnh thử **15 vị trí từ -7 đến 7**, mỗi vị trí được gán chỉ số đầu ra **không đơn vị** theo một quy tắc **đa thức bậc hai** đã cho. Kỹ thuật viên cần tạo bảng kết quả của đủ 15 vị trí, tra giá trị tại **x = 0** và tìm **vị trí có đầu ra nhỏ nhất** để đối chiếu với đường cong dự kiến. Các vị trí âm chỉ biểu thị phía bên kia gốc, không phải dữ liệu lỗi.

**Vì sao chọn cách này?** **Đa thức** là cách ghép các thành phần như một số cố định, phần tăng theo x và phần tăng theo bình phương x. `np.polyval([1, 2, 3], positions)` dùng **hệ số theo thứ tự từ bậc cao xuống thấp**, tính cùng quy tắc cho cả 15 vị trí; nếu đảo thứ tự hệ số thì sẽ thành đường cong khác. `np.argmin(output)` tìm **vị trí trong mảng** có đầu ra nhỏ nhất, không trả luôn giá trị x; chương trình dùng vị trí ấy để lấy cả **giá trị nhỏ nhất** và **tọa độ của nó**. Cần phân biệt vị trí thứ mấy trong danh sách với tọa độ x có thể âm.

**Quy trình:**
1. Tạo 15 giá trị x và ma trận hệ số `[1,2,3]`.
2. Áp `np.polyval` lên cả vector vị trí.
3. Tra đầu ra tại x=0, xác định vị trí cho giá trị nhỏ nhất.

**No Note — Không chú thích**

```python
import numpy as np
positions = np.array([-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7], dtype=float)
output = np.polyval([1, 2, 3], positions)
minimum = int(np.argmin(output))
if len(output) != 15:
    raise ValueError("Cần đúng 15 vị trí tính hàm.")
print("Vị trí:", len(positions))
print("Tại x=0:", int(output[positions == 0][0]))
print("Đầu ra nhỏ nhất:", int(output[minimum]))
print("Vị trí nhỏ nhất:", int(positions[minimum]))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Khảo sát 15 vị trí x từ -7 đến 7 để tìm giá trị nhỏ nhất của đa thức.
# Dữ liệu: x có đơn vị vị trí giả lập, output của đa thức x²+2x+3 là thang điểm chi phí giả lập.
# NumPy polyVal và argmin cho phép xử lý một vector vị trí.
import numpy as np
# 15 x từ -7..7, dtype=float tạo mảng số thực.
positions = np.array([-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7], dtype=float)
# polyval() tính x²+2x+3 theo hệ số bậc cao→thấp tại từng phần tử positions.
output = np.polyval([1, 2, 3], positions)
# argmin() trả CHỈ SỐ 0-based của giá trị nhỏ nhất, không trả chính giá trị; int() đổi scalar sang số nguyên.
minimum = int(np.argmin(output))
if len(output) != 15:
    # ValueError báo số lượng hoặc shape không đủ yêu cầu, tránh dùng kết quả chưa kiểm chứng.
    raise ValueError("Cần đúng 15 vị trí tính hàm.")
print("Vị trí:", len(positions))
# positions==0 tạo mask; output[mask] lọc giá trị tại x=0; [0] chọn phần tử đầu trong kết quả lọc.
print("Tại x=0:", int(output[positions == 0][0]))
# Trả giá trị đầu ra ở chỉ số minimum tìm thấy.
print("Đầu ra nhỏ nhất:", int(output[minimum]))
# Dùng cùng chỉ số minimum truy ngược vị trí x ứng với giá trị nhỏ nhất.
print("Vị trí nhỏ nhất:", int(positions[minimum]))
```

**Kết quả khi chạy:**

```text
Vị trí: 15
Tại x=0: 3
Đầu ra nhỏ nhất: 2
Vị trí nhỏ nhất: -1
```

Giá trị nhỏ nhất xảy ra tại x=-1, không phải nhất thiết tại x=0; thứ tự hệ số ảnh hưởng trực tiếp hình dạng đường cong.

### Tình huống 4 — Cấp 4: Mô phỏng 18 kỳ tăng trưởng lũy kế bằng hàm mũ

**Từ vựng trong mục:** **Exponential** — hàm mũ; **Compounding** — tăng lũy kế; **Growth rate** — tỷ lệ tăng.

**Tình huống thực tế:** Bộ phận kinh doanh so **hai giả định tăng trưởng** của một chỉ số bắt đầu ở **1.000 điểm** vào kỳ 0. Với giả định A, chỉ số tăng **3% trên giá trị đang có sau mỗi kỳ**; với B, mỗi kỳ chỉ cộng **30 điểm cố định**. Báo cáo gồm **18 kỳ, từ 0 đến 17**. Quản lý muốn xem hai chỉ số ở kỳ cuối và khoản chênh lệch, vì dù kỳ đầu tăng như nhau, về sau hai quy tắc có thể cho kết quả khác.

**Vì sao chọn cách này?** **Tăng trưởng lũy kế** có nghĩa mức tăng kỳ sau được tính từ **giá trị đã tăng của kỳ trước**; ví dụ 3% trên 1.030 điểm sẽ lớn hơn 3% trên 1.000 điểm. Đó là cách hoạt động của **hàm mũ** trong `compound`. Còn `linear` chỉ cộng 30 điểm mỗi kỳ, nên có **mức tăng tuyệt đối không đổi**. `np.arange(18)` tạo đúng các kỳ **0–17**, rồi cả hai quy tắc dùng cùng danh sách mốc để so công bằng. Nếu tưởng tăng 3% là cộng thêm 30 điểm trong **mọi kỳ**, người học sẽ nhầm tăng theo tỷ lệ với tăng cố định.

**Quy trình:**
1. Tạo vector 18 kỳ từ 0 tới 17.
2. Tính chuỗi tăng lũy kế bằng phép lũy thừa và chuỗi tuyến tính tăng 30 điểm/kỳ.
3. In kỳ cuối của hai mô hình và chênh lệch.

**No Note — Không chú thích**

```python
import numpy as np
periods = np.arange(18)
compound = 1000 * (1.03 ** periods)
linear = 1000 + 30 * periods
if compound.size != 18 or linear.size != 18:
    raise ValueError("Cần đủ 18 kỳ của cả hai cách tính.")
print("Kỳ:", len(periods))
print(f"Lũy kế cuối: {compound[-1]:.2f}")
print(f"Tuyến tính cuối: {linear[-1]:.2f}")
print(f"Chênh lệch: {compound[-1]-linear[-1]:.2f}")
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: So giá trị tích lũy tuyến tính và tăng lũy kế 3% qua 18 kỳ.
# Dữ liệu: 18 kỳ được đánh số từ 0 đến 17, ban đầu 1000 đơn vị, lũy kế tăng 3%/kỳ.
# NumPy arange tạo chuỗi kỳ và lũy thừa theo từng phần tử.
import numpy as np
# arange(18) sinh vector 18 số 0..17, không chứa 18; kỳ 0 là thời điểm ban đầu.
periods = np.arange(18)
# Broadcast phép lũy thừa: mỗi kỳ t dùng hệ số 1.03^t, lãi kép trên số dư mới.
# Nhân giá trị gốc 1000 để có lũy kế từng kỳ.
compound = 1000 * (1.03 ** periods)
# Tăng tuyến tính đúng 30 đơn vị mỗi kỳ, KHÔNG tái đầu tư lãi tăng.
linear = 1000 + 30 * periods
# size đếm đủ 18 phần tử của mỗi vector, không phải giá trị cuối.
if compound.size != 18 or linear.size != 18:
    # ValueError báo số lượng hoặc shape không đủ yêu cầu, tránh dùng kết quả chưa kiểm chứng.
    raise ValueError("Cần đủ 18 kỳ của cả hai cách tính.")
print("Kỳ:", len(periods))
# [-1] là kỳ cuối số 17; :.2f làm tròn hiển thị hai chữ số thập phân.
print(f"Lũy kế cuối: {compound[-1]:.2f}")
# Đọc mức tuyến tính tại cùng kỳ cuối để so công bằng.
print(f"Tuyến tính cuối: {linear[-1]:.2f}")
# [-1] là kỳ cuối số 17; :.2f làm tròn hiển thị hai chữ số thập phân.
# Đọc mức tuyến tính tại cùng kỳ cuối để so công bằng.
# Chênh lệch ở kỳ cuối biểu thị ảnh hưởng của cộng dồn tỷ lệ so với tăng cố định.
print(f"Chênh lệch: {compound[-1]-linear[-1]:.2f}")
```

**Kết quả khi chạy:**

```text
Kỳ: 18
Lũy kế cuối: 1652.85
Tuyến tính cuối: 1510.00
Chênh lệch: 142.85
```

Không suy ra giá trị tăng trưởng chắc chắn từ mô hình giả lập; nếu giả định 3% mỗi kỳ sai thì đường cong không còn phù hợp.

### Tình huống 5 — Cấp 5: Đánh giá hai mô hình trên 20 quan sát cong

**Từ vựng trong mục:** **Model fit** — độ khớp mô hình; **MSE** — sai số bình phương; **Extrapolation** — ngoại suy.

**Tình huống thực tế:** Nhóm phân tích dựng **20 mức tải từ 0 đến 19**, mỗi mức có một chi phí mô phỏng **nghìn đồng** được tạo theo đường cong bậc hai. Họ thử hai cách dự báo trên **chính 20 điểm này**: mô hình **tuyến tính** chỉ tăng theo một mức cố định và mô hình **bậc hai** có thể uốn cong theo tải. Nhóm muốn tính mức sai lệch bình phương trung bình của từng mô hình và xem mô hình nào khớp **bộ dữ liệu minh họa** hơn, chưa khẳng định dự báo dữ liệu mới sẽ tốt hơn.

**Vì sao chọn cách này?** **Mô hình** là một quy tắc tạo giá trị dự báo từ mức tải. **MSE** (sai số bình phương trung bình) đo trung bình các sai lệch đã bình phương giữa **giá trị quan sát và dự báo**; sai lệch lớn bị tính nặng hơn. Với bộ dữ liệu này, chi phí được tạo **đúng từ một quy tắc bậc hai**, nên mô hình bậc hai khớp gần như hoàn toàn, trong khi đường thẳng bỏ sót phần cong. `np.polyval()` dùng các hệ số bậc hai, còn `np.mean()` tổng hợp các sai lệch bình phương trên đủ 20 dòng. Kết quả chỉ chứng minh độ khớp **trên dữ liệu đã dựng**, chưa cho biết mô hình có khái quát tốt trên dữ liệu mới hay không.

**Quy trình:**
1. Tạo 20 đầu vào và 20 chi phí quan sát có đơn vị.
2. Tính dự báo bằng hai hàm khác nhau.
3. Đối chiếu MSE, chọn mô hình có sai số nhỏ nhất và báo quy mô dữ liệu.

**No Note — Không chú thích**

```python
import numpy as np
loads = np.arange(20, dtype=float)
observed = 2 * loads**2 + 3 * loads + 10
linear = 3 * loads + 10
quadratic = np.polyval([2, 3, 10], loads)
mse_linear = np.mean((observed - linear) ** 2)
mse_quadratic = np.mean((observed - quadratic) ** 2)
if observed.shape != (20,) or linear.shape != (20,) or quadratic.shape != (20,):
    raise ValueError("Cần 20 quan sát để đối chiếu hai mô hình.")
print("Quan sát:", len(loads))
print(f"MSE tuyến tính: {mse_linear:.2f}")
print(f"MSE bậc hai: {mse_quadratic:.2f}")
if mse_quadratic < mse_linear:
    best_model = "bậc hai"
else:
    best_model = "tuyến tính"
print("Khớp hơn:", best_model)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: So mô hình tuyến tính và bậc hai khi dữ liệu thật được sinh theo quan hệ bậc hai.
# Dữ liệu: 20 mức tải từ 0..19; observed có bậc hai, linear chỉ có thành phần bậc nhất, quadratic mô phỏng đúng.
# NumPy hỗ trợ arange(), polyval(), mean() để so mô hình.
import numpy as np
# Tạo 20 đầu vào 0..19 ở dạng float, mỗi giá trị một lượt tải.
loads = np.arange(20, dtype=float)
# Giá trị observed tuân đa thức bậc hai; **2 lấy bình phương từng phần tử.
# Mô hình linear bỏ qua ảnh hưởng bình phương nên sai nhiều ở tải lớn.
observed = 2 * loads**2 + 3 * loads + 10
# Mô hình linear bỏ qua ảnh hưởng bình phương nên sai nhiều ở tải lớn.
linear = 3 * loads + 10
# polyval áp bộ hệ số 2*x²+3*x+10 đúng thứ tự bậc cao→thấp.
quadratic = np.polyval([2, 3, 10], loads)
# Trừ từng dự đoán khỏi quan sát, bình phương để phạt lệch lớn, giữ đơn vị đầu ra bình phương.
# np.mean() lấy trung bình sai số bình phương của 20 lượt, chính là MSE.
mse_linear = np.mean((observed - linear) ** 2)
# MSE của mô hình đa thức so với observed, gần 0 vì công thức trùng nhau.
mse_quadratic = np.mean((observed - quadratic) ** 2)
# shape (20,) kiểm mỗi vector đầu ra có đúng 20 giá trị, không mất lượt.
if observed.shape != (20,) or linear.shape != (20,) or quadratic.shape != (20,):
    # ValueError báo số lượng hoặc shape không đủ yêu cầu, tránh dùng kết quả chưa kiểm chứng.
    raise ValueError("Cần 20 quan sát để đối chiếu hai mô hình.")
print("Quan sát:", len(loads))
print(f"MSE tuyến tính: {mse_linear:.2f}")
print(f"MSE bậc hai: {mse_quadratic:.2f}")
# So MSE nhỏ hơn để chọn mô hình khớp dữ liệu đã giả lập tốt hơn; không có nghĩa luôn tốt nhất khi gặp dữ liệu mới.
if mse_quadratic < mse_linear:
    best_model = "bậc hai"
else:
    best_model = "tuyến tính"
print("Khớp hơn:", best_model)
```

**Kết quả khi chạy:**

```text
Quan sát: 20
MSE tuyến tính: 112533.20
MSE bậc hai: 0.00
Khớp hơn: bậc hai
```

MSE ở đây có đơn vị **(nghìn đồng)²**, khác đơn vị chi phí. Mô hình B khớp tuyệt đối vì dữ liệu được **tạo ra bằng chính dạng bậc hai**.

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

A. `y=a*x**2+b*x+c` with a≠0 | `y=a*x**2+b*x+c` với a≠0

B. A variable appears in the exponent | Biến xuất hiện ở số mũ

C. `y=m*x+b` | `y=m*x+b`

D. Highest nonzero power of x | Lũy thừa cao nhất có hệ số khác 0

**Đáp án: C**

**Giải thích:** Dạng affine gồm hệ số góc và hệ số chặn.


**Q2. Which form contains a nonzero quadratic term? | Dạng nào có hạng bậc hai khác 0?**

A. `y=m*x+b` | `y=m*x+b`

B. A variable appears in the exponent | Biến xuất hiện ở số mũ

C. Highest nonzero power of x | Lũy thừa cao nhất có hệ số khác 0

D. `y=a*x**2+b*x+c` with a≠0 | `y=a*x**2+b*x+c` với a≠0

**Đáp án: D**

**Giải thích:** Hàm bậc hai có hạng x bình phương.


**Q3. What does polynomial degree measure? | Bậc đa thức cho biết gì?**

A. A variable appears in the exponent | Biến xuất hiện ở số mũ

B. `y=m*x+b` | `y=m*x+b`

C. `y=a*x**2+b*x+c` with a≠0 | `y=a*x**2+b*x+c` với a≠0

D. Highest nonzero power of x | Lũy thừa cao nhất có hệ số khác 0

**Đáp án: D**

**Giải thích:** Bậc là số mũ cao nhất có hệ số khác 0.


**Q4. What characterizes an exponential function? | Đặc điểm của hàm mũ là gì?**

A. `y=a*x**2+b*x+c` with a≠0 | `y=a*x**2+b*x+c` với a≠0

B. Highest nonzero power of x | Lũy thừa cao nhất có hệ số khác 0

C. `y=m*x+b` | `y=m*x+b`

D. A variable appears in the exponent | Biến xuất hiện ở số mũ

**Đáp án: D**

**Giải thích:** Hàm mũ có số mũ thay đổi.


**Q5. Given f(x) = 2x + 3, what is f(4)? | Cho f(x) = 2x + 3, f(4) bằng bao nhiêu?**

A. 14 | 14

B. 8 | 8

C. 7 | 7

D. 11 | 11

**Đáp án: D**

**Giải thích:** Thay x = 4: f(4) = 2 × 4 + 3 = 11.


**Q6. At which x is f(x) = (x − 3)² equal to zero? | Hàm f(x) = (x − 3)² bằng 0 tại giá trị x nào?**

A. 6 | 6

B. 3 | 3

C. −3 | −3

D. 0 | 0

**Đáp án: B**

**Giải thích:** Bình phương bằng 0 khi biểu thức bên trong bằng 0: x − 3 = 0, nên x = 3.


**Q7. Which best describes exponential growth compared with linear growth? | Đâu là điểm khác nhau điển hình giữa tăng trưởng hàm mũ và tuyến tính?**

A. Exponential growth always stops | Tăng trưởng mũ luôn dừng

B. Both add the same amount at each step | Cả hai cùng cộng số lượng cố định mỗi bước

C. Linear growth always decreases | Tuyến tính luôn giảm

D. Exponential growth multiplies by a fixed factor in equal steps | Tăng trưởng mũ nhân theo một tỷ lệ cố định qua các bước đều

**Đáp án: D**

**Giải thích:** Hàm tuyến tính có mức tăng tuyệt đối cố định; hàm mũ tăng theo tỷ lệ nhân cố định khi đầu vào tăng đều.


**Q8. What is f(2) if f(x) = (x − 2)²? | Nếu f(x) = (x − 2)², f(2) bằng bao nhiêu?**

A. 2 | 2

B. 0 | 0

C. 8 | 8

D. 4 | 4

**Đáp án: B**

**Giải thích:** Thay x = 2: (2 − 2)² = 0.


**Q9. Which NumPy function evaluates a polynomial? | Hàm NumPy nào tính đa thức?**

A. Highest degree first | Bậc cao nhất trước

B. `np.linspace(start,stop,num)` | `np.linspace(start,stop,num)`

C. `np.exp(x)` | `np.exp(x)`

D. `np.polyval(coefficients,x)` | `np.polyval(coefficients,x)`

**Đáp án: D**

**Giải thích:** polyval tính đa thức theo các hệ số có thứ tự.


**Q10. In what order does `np.polyval` take coefficients? | `np.polyval` nhận hệ số theo thứ tự gì?**

A. `np.linspace(start,stop,num)` | `np.linspace(start,stop,num)`

B. `np.polyval(coefficients,x)` | `np.polyval(coefficients,x)`

C. `np.exp(x)` | `np.exp(x)`

D. Highest degree first | Bậc cao nhất trước

**Đáp án: D**

**Giải thích:** Hệ số bậc cao nhất đứng đầu.


**Q11. Which function computes e raised to x? | Hàm nào tính e mũ x?**

A. Highest degree first | Bậc cao nhất trước

B. `np.linspace(start,stop,num)` | `np.linspace(start,stop,num)`

C. `np.polyval(coefficients,x)` | `np.polyval(coefficients,x)`

D. `np.exp(x)` | `np.exp(x)`

**Đáp án: D**

**Giải thích:** exp tính hàm mũ cơ số e.


**Q12. Which function makes evenly spaced samples? | Hàm nào tạo các điểm cách đều?**

A. Highest degree first | Bậc cao nhất trước

B. `np.polyval(coefficients,x)` | `np.polyval(coefficients,x)`

C. `np.exp(x)` | `np.exp(x)`

D. `np.linspace(start,stop,num)` | `np.linspace(start,stop,num)`

**Đáp án: D**

**Giải thích:** linspace tạo số lượng điểm cách đều yêu cầu.


**Q13. What is the value of y=2x+5 at x=0? | Giá trị y=2x+5 khi x=0 là gì?**

A. 16 | 16

B. 4 | 4

C. 6 | 6

D. 5 | 5

**Đáp án: D**

**Giải thích:** Khi x=0, ta có 2×0+5=5.


**Q14. What is the value of x²+2 at x=2? | Giá trị x²+2 khi x=2 là gì?**

A. 6 | 6

B. 4 | 4

C. 16 | 16

D. 5 | 5

**Đáp án: A**

**Giải thích:** Bình phương 2 rồi cộng 2 bằng 6.


**Q15. What is 2 raised to the fourth power? | 2 mũ 4 bằng gì?**

A. 6 | 6

B. 5 | 5

C. 4 | 4

D. 16 | 16

**Đáp án: D**

**Giải thích:** 2 nhân bốn lần bằng 16.


**Q16. How many intervals are between five evenly spaced points? | Năm điểm cách đều tạo bao nhiêu khoảng?**

A. 5 | 5

B. 16 | 16

C. 6 | 6

D. 4 | 4

**Đáp án: D**

**Giải thích:** n điểm tạo n−1 khoảng.


**Q17. What does `np.exp(0)` equal? | `np.exp(0)` bằng bao nhiêu?**

A. A constant additive increment | Mỗi bước cộng cùng một mức

B. Accuracy on unseen real-world data | Độ chính xác trên dữ liệu thực chưa gặp

C. 1 | 1

D. Its slope changes with x | Độ dốc thay đổi theo x

**Đáp án: C**

**Giải thích:** Cơ số khác 0 mũ 0 bằng 1.


**Q18. How does a quadratic differ from a first-degree affine function? | Hàm bậc hai khác hàm affine bậc nhất ở đâu?**

A. A constant additive increment | Mỗi bước cộng cùng một mức

B. 1 | 1

C. Accuracy on unseen real-world data | Độ chính xác trên dữ liệu thực chưa gặp

D. Its slope changes with x | Độ dốc thay đổi theo x

**Đáp án: D**

**Giải thích:** Mức tăng của hàm bậc hai thay đổi theo x.


**Q19. Which constraint gives a constant-per-step growth model? | Mô hình tăng đều mỗi bước cần điều kiện gì?**

A. A constant additive increment | Mỗi bước cộng cùng một mức

B. 1 | 1

C. Accuracy on unseen real-world data | Độ chính xác trên dữ liệu thực chưa gặp

D. Its slope changes with x | Độ dốc thay đổi theo x

**Đáp án: A**

**Giải thích:** Cộng hằng số tạo mức tăng cố định.


**Q20. What does a fitted function alone not prove? | Một hàm được khớp dữ liệu chưa chứng minh được gì?**

A. A constant additive increment | Mỗi bước cộng cùng một mức

B. 1 | 1

C. Its slope changes with x | Độ dốc thay đổi theo x

D. Accuracy on unseen real-world data | Độ chính xác trên dữ liệu thực chưa gặp

**Đáp án: D**

**Giải thích:** Khả năng dự đoán cần được kiểm chứng ngoài các ví dụ khớp.

## 8. Bài tiếp theo

`Hàm Python → Hàm toán theo dữ liệu → Loss → Gradient`.
