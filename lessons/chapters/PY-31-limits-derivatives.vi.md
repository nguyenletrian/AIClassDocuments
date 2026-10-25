# PY-31 — Giới hạn, tính liên tục và đạo hàm


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Limit** — giới hạn; **Continuity** — tính liên tục.

`Hàm số → Limit → Derivative → Gradient`

**Học xong dùng để làm gì?** Đo tốc độ thay đổi của hàm theo biến và suy ra chiều tăng/giảm của sai số.

**Kết nối kiến thức tiếp theo:** PY-32 dùng gradient và tốc độ học để cập nhật trọng số mô hình.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| Limit | giới hạn | Giá trị hàm tiến gần khi đầu vào tiến đến điểm |
| Continuity | tính liên tục | Giới hạn và giá trị hàm phù hợp tại điểm xét |
| Derivative | đạo hàm | Tốc độ thay đổi cục bộ của hàm theo đầu vào |
| Tangent slope | độ dốc tiếp tuyến | Giá trị đạo hàm tại một điểm |

## 3. Hàm và cách gọi bằng Python

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm / tham số | Giải thích |
|---|---|
| `sympy.symbols()/limit()` | Tạo biến ký hiệu và tính giới hạn kể cả điểm không xác định |
| `sympy.diff(f,x)` | Đạo hàm theo biến x |
| `expr.subs(x,value)` | Thay giá trị vào công thức symbolic |
| `np.gradient(y,x)` | Ước lượng đạo hàm từ dãy mẫu, phụ thuộc bước lấy mẫu |

## 4. Khái niệm chính và liên quan

**Mạch kiến thức:** Giới hạn mô tả xu hướng gần một điểm; liên tục đòi hỏi xu hướng ấy bằng giá trị tại điểm; đạo hàm dùng giới hạn để đo độ thay đổi; độ dốc tiếp tuyến là đạo hàm sau khi thay một tọa độ cụ thể.

### 4.1. Limit — Giá trị hàm tiến đến

**Từ vựng:** **Limit** — giới hạn; **Approach** — tiến gần.

Giới hạn hỏi **f(x) tiến gần giá trị nào khi x tiến gần a**, không bắt buộc f(a) phải có giá trị. Ví dụ `(x²−4)/(x−2)` không xác định tại x=2 vì mẫu số bằng 0. Với x khác 2, rút gọn thành `x+2`; khi x→2, kết quả tiến đến **4**. `sympy.limit` tính giá trị tiến đến của biểu thức thay vì thay trực tiếp x=2 gây chia 0.

```python
# Mục đích: Giá trị hàm tiến đến.
import sympy as sp

x = sp.symbols('x')
f = (x ** 2 - 4) / (x - 2)
print(sp.limit(f, x, 2))
```

**Kết quả khi chạy:**

```text
4
```

Giới hạn bằng 4 dù biểu thức gốc không xác định ngay tại x=2.

### 4.2. Continuity — Hàm liên tục tại một điểm

**Từ vựng:** **Continuity** — tính liên tục; **Function value** — giá trị hàm.

Hàm liên tục tại x=a nếu **f(a) tồn tại**, giới hạn từ hai phía tồn tại và bằng f(a). Ví dụ quãng đường mô phỏng `s(t)=t²` là hàm liên tục; tại t=2 giây, `s(2)=4` mét và khi t tiến gần 2, quãng đường cũng tiến đến 4 mét. Đây là tính chất của **mô hình hàm**, không tự suy ra cảm biến vật lý hoạt động liên tục.

```python
# Mục đích: Hàm liên tục tại một điểm.
import sympy as sp

t = sp.symbols('t')
s = t ** 2
print(sp.limit(s, t, 2) == s.subs(t, 2))
```

**Kết quả khi chạy:**

```text
True
```

Giới hạn bằng giá trị hàm ở t=2, nên mô hình liên tục tại điểm xét.

### 4.3. Derivative — Tốc độ thay đổi tức thời

**Từ vựng:** **Derivative** — đạo hàm; **Rate of change** — tốc độ thay đổi.

Đạo hàm `f'(x)` cho biết đầu ra thay đổi bao nhiêu **khi đầu vào thay đổi rất nhỏ**. Về công thức, đó là giới hạn `(f(x+h)−f(x))/h` khi h→0 nếu giới hạn tồn tại. Với `f(x)=x²`, ta có `f'(x)=2x`; độ dốc không cố định: tại x=1 là 2, tại x=3 là 6. Nếu f là quãng đường (mét) theo thời gian (giây), đơn vị đạo hàm là mét/giây.

```python
# Mục đích: Tốc độ thay đổi tức thời.
import sympy as sp

x = sp.symbols('x')
print(sp.diff(x ** 2, x))
```

**Kết quả khi chạy:**

```text
2*x
```

Đạo hàm là biểu thức 2x; tăng x thì độ dốc cục bộ tăng.

### 4.4. Tangent slope — Độ dốc tại một giá trị cụ thể

**Từ vựng:** **Tangent** — tiếp tuyến; **Slope** — độ dốc.

Nếu đạo hàm là **hàm mô tả độ dốc**, thì độ dốc tiếp tuyến tại x=a là **một số**, chính là `f'(a)`. Với đường `f(x)=x²`, đạo hàm `2x`, nên tại x=3 độ dốc bằng 6. Phân biệt `sp.diff` tạo biểu thức đạo hàm và `.subs(x,3)` thay tọa độ để lấy độ dốc tại đúng điểm đó.

```python
# Mục đích: Độ dốc tại một giá trị cụ thể.
import sympy as sp

x = sp.symbols('x')
slope = sp.diff(x ** 2, x)
print(slope.subs(x, 3))
```

**Kết quả khi chạy:**

```text
6
```

Đường cong có độ dốc tiếp tuyến bằng 6 tại x=3.

## 5. Năm tình huống Giới hạn/Đạo hàm — từ điểm khuyết đến sai phân không đều

### Tình huống 1 — Cấp 1: Quan sát 10 giá trị tiến gần một điểm biểu thức không xác định

**Từ vựng trong mục:** **Limit** — giới hạn; **Removable discontinuity** — điểm khuyết có thể bổ sung.

**Tình huống thực tế:** Chương trình hiệu chuẩn dùng biểu thức `(x²−4)/(x−2)` để đổi tín hiệu x sang chỉ số đầu ra (không đơn vị). Có **10 lượt đầu vào** nằm gần mức x=2: năm lượt nhỏ hơn 2 và năm lượt lớn hơn 2. Công thức gốc không tính được **ngay tại x=2**, nhưng cần tìm chỉ số nó tiến đến từ hai phía để quyết định giá trị dùng khi xử lý điểm khuyết.

**Vì sao chọn cách này?** Giới hạn mô tả xu hướng **gần** điểm cần xét; nó không đòi phép chia có nghĩa ngay ở điểm đó. Mẫu hai phía minh họa xu hướng, còn `sympy.limit` cho kết quả chính xác.

**Quy trình:**
1. Tạo 10 số đầu vào, không có số nào bằng 2.
2. Tính đầu ra ở hai giá trị gần nhất, quan sát chúng xấp xỉ nhau.
3. Dùng SymPy xác định giới hạn tại 2 và đối chiếu.

```python
import sympy as sp
x = sp.symbols("x")
f = (x**2 - 4) / (x - 2)
inputs = [1.9,1.95,1.99,1.995,1.999,2.1,2.05,2.01,2.005,2.001]
results = []
for value in inputs:
    results.append(float(f.subs(x, value)))
limit_at_two = sp.limit(f, x, 2)
if len(inputs) != 10 or 2 in inputs:
    raise ValueError("Cần đúng 10 điểm tiến gần 2, không lấy đúng x=2.")
print("Lượt đo:", len(inputs))
print(f"Gần từ trái: {results[4]:.3f}")
print(f"Gần từ phải: {results[-1]:.3f}")
print("Giới hạn:", limit_at_two)
```

**Kết quả khi chạy:**

```text
Lượt đo: 10
Gần từ trái: 3.999
Gần từ phải: 4.001
Giới hạn: 4
```

Biểu thức gốc có điểm khuyết tại x=2. **Giới hạn bằng 4** không đồng nghĩa biểu thức gốc đã có giá trị tại điểm ấy.

### Tình huống 2 — Cấp 2: Tính vận tốc tức thời ở 12 mốc thời gian

**Từ vựng trong mục:** **Derivative** — đạo hàm; **Rate of change** — tốc độ thay đổi.

**Tình huống thực tế:** Robot đi theo quãng đường mô phỏng `s(t)=t²` (mét), t tính bằng giây. Người vận hành ghi **12 mốc thời gian** 0–11 giây, mỗi hàng là một mốc. Cần tính vận tốc tức thời tại từng mốc và so lúc 3 giây với lúc 11 giây; không lấy quãng đường làm vận tốc.

**Vì sao chọn cách này?** Đạo hàm của quãng đường theo thời gian là vận tốc (m/giây). `sympy.diff` tìm hàm vận tốc một lần rồi `subs` tính nó trên 12 mốc khác nhau.

**Quy trình:**
1. Định nghĩa quãng đường bằng SymPy và lấy đạo hàm theo t.
2. Thay 12 mốc thời gian vào biểu thức vận tốc.
3. In vận tốc ở hai mốc và kiểm số lượng đầu ra.

```python
import sympy as sp
t = sp.symbols("t")
position = t**2
velocity = sp.diff(position, t)
times = [0,1,2,3,4,5,6,7,8,9,10,11]
values = []
for second in times:
    values.append(velocity.subs(t, second))
if len(times) != 12 or len(values) != 12:
    raise ValueError("Cần đủ 12 mốc thời gian và 12 vận tốc.")
print("Mốc thời gian:", len(times))
print("Vận tốc ở 3 giây (m/giây):", values[3])
print("Vận tốc ở 11 giây (m/giây):", values[-1])
```

**Kết quả khi chạy:**

```text
Mốc thời gian: 12
Vận tốc ở 3 giây (m/giây): 6
Vận tốc ở 11 giây (m/giây): 22
```

Tại t=3, **quãng đường là 9 m nhưng vận tốc là 6 m/giây**; hai đại lượng này có đơn vị khác nhau.

### Tình huống 3 — Cấp 3: Đo mức tăng chi phí tại 15 mức tải bằng tiếp tuyến

**Từ vựng trong mục:** **Tangent slope** — độ dốc tiếp tuyến; **Marginal cost** — chi phí cận biên.

**Tình huống thực tế:** Xưởng có **15 mức tải** từ 1 đến 15 đơn vị, mỗi hàng là một mức. Quy tắc chi phí giả lập `2q²+3q+10` (nghìn đồng). Quản đốc cần biết mỗi khi tải tăng một chút thì chi phí thay đổi nhanh đến đâu ở mức tải thấp nhất và cao nhất.

**Vì sao chọn cách này?** Đạo hàm `4q+3` cho **độ dốc tại một mức tải cụ thể**, khác tổng chi phí. Khi q tăng, độ dốc tăng, cho thấy tải lớn làm chi phí cận biên theo mô hình cao hơn.

**Quy trình:**
1. Lưu 15 mức tải và hàm chi phí tương ứng.
2. Lấy đạo hàm theo q, thay từng mức tải vào.
3. Báo độ dốc đầu và cuối, xác nhận dãy độ dốc tăng.

```python
import sympy as sp
q = sp.symbols("q")
cost = 2*q**2 + 3*q + 10
marginal = sp.diff(cost, q)
loads = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
slopes = []
for load in loads:
    slopes.append(int(marginal.subs(q, load)))
if len(slopes) != 15:
    raise ValueError("Cần tính đủ 15 mức tải.")
print("Mức tải:", len(slopes))
print("Mức tăng ở tải 1:", slopes[0])
print("Mức tăng ở tải 15:", slopes[-1])
slopes_increase = True
for a, b in zip(slopes, slopes[1:]):
    if a >= b:
        slopes_increase = False
        break
print("Độ dốc tăng:", slopes_increase)
```

**Kết quả khi chạy:**

```text
Mức tải: 15
Mức tăng ở tải 1: 7
Mức tăng ở tải 15: 63
Độ dốc tăng: True
```

Đơn vị độ dốc là **nghìn đồng trên một đơn vị tải**; không coi nó là tổng tiền của chuyến sản xuất.

### Tình huống 4 — Cấp 4: Phát hiện điểm nhảy dù đã ghi 18 mốc số đo

**Từ vựng trong mục:** **Continuity** — tính liên tục; **One-sided limit** — giới hạn một phía.

**Tình huống thực tế:** Ứng dụng tính chỉ số phụ phí theo thời gian t (giờ): **trước t=8** sử dụng `t+5`, từ **t=8 trở đi** sử dụng `t+7`. Bảng có **18 mốc giờ** 0–17 (mỗi hàng một thời điểm). Người vận hành muốn biết khi thời gian vừa chạm 8 giờ, mức phụ phí có nhảy đột ngột hay không; dữ liệu rời rạc chỉ gợi ý, phải kiểm công thức hai phía.

**Vì sao chọn cách này?** Để liên tục tại 8, giới hạn trái, giới hạn phải và giá trị tại 8 phải bằng nhau. Hai biểu thức nhánh khác nhau cho hai mức 13 và 15, nên dù có 18 quan sát, hệ số phụ phí vẫn có **điểm không liên tục**.

**Quy trình:**
1. Tạo 18 thời điểm và tính đầu ra theo đúng hai nhánh.
2. Dùng `sympy.limit` cho biểu thức nhánh trái/phải khi t tới 8.
3. So hai giới hạn với giá trị hàm tại 8 rồi báo kết luận.

```python
import sympy as sp
t = sp.symbols("t")
times = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
values = []
for hour in times:
    if hour < 8:
        value = hour + 5
    else:
        value = hour + 7
    values.append(value)
left = sp.limit(t + 5, t, 8)
right = sp.limit(t + 7, t, 8)
continuous = left == right == values[8]
if len(times) != 18:
    raise ValueError("Cần đủ 18 mốc giờ.")
print("Mốc giờ:", len(times))
print("Giới hạn trái:", left)
print("Giới hạn phải:", right)
print("Giá trị ở 8:", values[8])
print("Liên tục ở 8:", continuous)
```

**Kết quả khi chạy:**

```text
Mốc giờ: 18
Giới hạn trái: 13
Giới hạn phải: 15
Giá trị ở 8: 15
Liên tục ở 8: False
```

Điểm t=8 có giá trị thật theo **nhánh phải**; vẫn không liên tục vì khi đến từ bên trái, hàm tiến đến giá trị khác.

### Tình huống 5 — Cấp 5: Đối chiếu đạo hàm giải tích với 20 điểm đo không đều

**Từ vựng trong mục:** **Numerical gradient** — đạo hàm số; **Sampling interval** — khoảng lấy mẫu; **Boundary effect** — sai số ở mép.

**Tình huống thực tế:** Robot cung cấp **20 bản ghi** thời gian–quãng đường: thời điểm lấy mẫu **không cách đều**, từ 0 đến 28 giây, quãng đường giả lập theo `s(t)=t²+2t` (m). Cần ước lượng vận tốc từ bảng bằng `np.gradient(s, t)`, so với đạo hàm chính xác và tìm hiểu tại sao **các điểm ở hai mép** có thể khác các điểm giữa.

**Vì sao chọn cách này?** Đưa **tọa độ thời gian thật** vào `np.gradient` là thiết yếu khi khoảng lấy mẫu không đều. Đối với hàm bậc hai, sai phân trung tâm tại các điểm giữa tái tạo đúng đạo hàm; biên dùng sai phân một phía mặc định nên có sai số.

**Quy trình:**
1. Tạo 20 thời điểm và quãng đường theo cùng thứ tự.
2. Tính vận tốc số bằng `np.gradient` có truyền thời gian, so với `2*t+2`.
3. Kiểm 18 điểm trong khớp và in sai số mép đầu/cuối.

```python
import numpy as np
t = np.array([0,1,3,4,6,7,9,10,12,13,15,16,18,19,21,22,24,25,27,28], dtype=float)
s = t**2 + 2*t
numerical = np.gradient(s, t)
analytical = 2*t + 2
if len(t) != 20 or not np.all(np.diff(t) > 0):
    raise ValueError("Cần 20 mốc thời gian tăng dần.")
print("Số lần đo:", len(t))
print("Giữa khớp:", bool(np.allclose(numerical[1:-1], analytical[1:-1])))
print(f"Sai số mép đầu (m/giây): {abs(numerical[0]-analytical[0]):.1f}")
print(f"Sai số mép cuối (m/giây): {abs(numerical[-1]-analytical[-1]):.1f}")
```

**Kết quả khi chạy:**

```text
Số lần đo: 20
Giữa khớp: True
Sai số mép đầu (m/giây): 1.0
Sai số mép cuối (m/giây): 1.0
```

Trong dữ liệu thực có nhiễu đo, điểm giữa cũng có thể lệch; ở đây khớp vì **hàm được tạo đúng theo quy luật bậc hai**.

## 6. Sai lầm thường gặp

- Giới hạn không nhất thiết bằng giá trị hàm tại điểm nếu hàm không liên tục hoặc không xác định ở đó.
- Muốn liên tục cần giới hạn trái, phải và giá trị hàm bằng nhau.
- Đạo hàm là tốc độ thay đổi tức thời; độ dốc trung bình trên một khoảng có thể khác.
- Với quãng đường theo giây, đạo hàm có đơn vị m/s; không diễn giải thành mét.
- `np.gradient` xấp xỉ từ mẫu; ở đầu và cuối dãy thường dùng sai phân một phía.
- SymPy là thư viện ngoài cần cài khi chạy các ví dụ ký hiệu.

## 7. Trắc nghiệm

**Q1. What does a limit describe? | Giới hạn mô tả gì?**

A. What f(x) approaches as x approaches a point | Giá trị f(x) tiến đến khi x tiến gần một điểm

B. The two-sided limit exists and equals f(a) | Giới hạn hai phía tồn tại và bằng f(a)

C. Instantaneous rate of change | Tốc độ thay đổi tức thời

D. The derivative evaluated at a | Giá trị đạo hàm tại a

**Đáp án: A**

**Giải thích:** Giới hạn xét đầu vào lân cận điểm.


**Q2. What does continuity at x=a require? | Liên tục tại x=a cần gì?**

A. What f(x) approaches as x approaches a point | Giá trị f(x) tiến đến khi x tiến gần một điểm

B. The two-sided limit exists and equals f(a) | Giới hạn hai phía tồn tại và bằng f(a)

C. Instantaneous rate of change | Tốc độ thay đổi tức thời

D. The derivative evaluated at a | Giá trị đạo hàm tại a

**Đáp án: B**

**Giải thích:** Liên tục đòi hỏi giới hạn bằng giá trị hàm.


**Q3. What does a derivative describe? | Đạo hàm mô tả gì?**

A. What f(x) approaches as x approaches a point | Giá trị f(x) tiến đến khi x tiến gần một điểm

B. The two-sided limit exists and equals f(a) | Giới hạn hai phía tồn tại và bằng f(a)

C. Instantaneous rate of change | Tốc độ thay đổi tức thời

D. The derivative evaluated at a | Giá trị đạo hàm tại a

**Đáp án: C**

**Giải thích:** Đạo hàm đo độ thay đổi tại điểm.


**Q4. What is tangent slope at x=a? | Độ dốc tiếp tuyến tại x=a là gì?**

A. What f(x) approaches as x approaches a point | Giá trị f(x) tiến đến khi x tiến gần một điểm

B. The two-sided limit exists and equals f(a) | Giới hạn hai phía tồn tại và bằng f(a)

C. Instantaneous rate of change | Tốc độ thay đổi tức thời

D. The derivative evaluated at a | Giá trị đạo hàm tại a

**Đáp án: D**

**Giải thích:** Độ dốc tiếp tuyến là f'(a).


**Q5. What does `sp.limit(f,x,a)` calculate? | `sp.limit(f,x,a)` tính gì?**

A. The limit of f as x approaches a | Giới hạn của f khi x tiến đến a

B. The derivative of f with respect to x | Đạo hàm f theo biến x

C. Substitutes a into symbolic expression | Thay a vào biểu thức ký hiệu

D. Derivatives from sampled y and x values | Đạo hàm từ các giá trị y, x lấy mẫu

**Đáp án: A**

**Giải thích:** limit tính giới hạn mà không cần thế tại điểm kỳ dị.


**Q6. What does `sp.diff(f,x)` return? | `sp.diff(f,x)` trả gì?**

A. The limit of f as x approaches a | Giới hạn của f khi x tiến đến a

B. The derivative of f with respect to x | Đạo hàm f theo biến x

C. Substitutes a into symbolic expression | Thay a vào biểu thức ký hiệu

D. Derivatives from sampled y and x values | Đạo hàm từ các giá trị y, x lấy mẫu

**Đáp án: B**

**Giải thích:** diff tính đạo hàm ký hiệu.


**Q7. What does `expr.subs(x,a)` do? | `expr.subs(x,a)` làm gì?**

A. The limit of f as x approaches a | Giới hạn của f khi x tiến đến a

B. The derivative of f with respect to x | Đạo hàm f theo biến x

C. Substitutes a into symbolic expression | Thay a vào biểu thức ký hiệu

D. Derivatives from sampled y and x values | Đạo hàm từ các giá trị y, x lấy mẫu

**Đáp án: C**

**Giải thích:** subs thay giá trị vào biểu thức ký hiệu.


**Q8. What does `np.gradient(y,x)` approximate? | `np.gradient(y,x)` xấp xỉ gì?**

A. The limit of f as x approaches a | Giới hạn của f khi x tiến đến a

B. The derivative of f with respect to x | Đạo hàm f theo biến x

C. Substitutes a into symbolic expression | Thay a vào biểu thức ký hiệu

D. Derivatives from sampled y and x values | Đạo hàm từ các giá trị y, x lấy mẫu

**Đáp án: D**

**Giải thích:** gradient xấp xỉ đạo hàm từ mẫu.


**Q9. What is the derivative of x²? | Đạo hàm của x² là gì?**

A. `2*x` | `2*x`

B. Zero | Bằng 0

C. 6 | 6

D. 4 | 4

**Đáp án: A**

**Giải thích:** Quy tắc đạo hàm lũy thừa cho 2x.


**Q10. What is the derivative of a constant? | Đạo hàm của một hằng số là gì?**

A. `2*x` | `2*x`

B. Zero | Bằng 0

C. 6 | 6

D. 4 | 4

**Đáp án: B**

**Giải thích:** Hằng số không đổi theo biến.


**Q11. What is the slope of x² at x=3? | Độ dốc của x² tại x=3 là gì?**

A. `2*x` | `2*x`

B. Zero | Bằng 0

C. 6 | 6

D. 4 | 4

**Đáp án: C**

**Giải thích:** 2 nhân 3 bằng sáu.


**Q12. What is the limit of (x²−4)/(x−2) at x=2? | Giới hạn của (x²−4)/(x−2) khi x→2 là gì?**

A. `2*x` | `2*x`

B. Zero | Bằng 0

C. 6 | 6

D. 4 | 4

**Đáp án: D**

**Giải thích:** Rút gọn gần điểm còn x+2.


**Q13. What may happen if the left and right limits differ? | Nếu giới hạn trái và phải khác nhau thì sao?**

A. The two-sided limit does not exist | Giới hạn hai phía không tồn tại

B. Distance per unit time | Khoảng cách trên mỗi đơn vị thời gian

C. Sampling spacing and numerical scheme | Khoảng cách mẫu và cách lấy sai phân

D. Yes, if nearby values approach one number | Có, nếu giá trị lân cận tiến đến cùng một số

**Đáp án: A**

**Giải thích:** Giới hạn một phía khác nhau khiến giới hạn hai phía không có.


**Q14. What does a derivative unit become for distance over time? | Đạo hàm quãng đường theo thời gian có đơn vị gì?**

A. The two-sided limit does not exist | Giới hạn hai phía không tồn tại

B. Distance per unit time | Khoảng cách trên mỗi đơn vị thời gian

C. Sampling spacing and numerical scheme | Khoảng cách mẫu và cách lấy sai phân

D. Yes, if nearby values approach one number | Có, nếu giá trị lân cận tiến đến cùng một số

**Đáp án: B**

**Giải thích:** Quãng đường chia thời gian cho đơn vị vận tốc.


**Q15. What determines finite-difference accuracy? | Độ chính xác sai phân hữu hạn phụ thuộc gì?**

A. The two-sided limit does not exist | Giới hạn hai phía không tồn tại

B. Distance per unit time | Khoảng cách trên mỗi đơn vị thời gian

C. Sampling spacing and numerical scheme | Khoảng cách mẫu và cách lấy sai phân

D. Yes, if nearby values approach one number | Có, nếu giá trị lân cận tiến đến cùng một số

**Đáp án: C**

**Giải thích:** Khoảng lấy mẫu ảnh hưởng độ dốc ước lượng.


**Q16. Can a function have a finite limit at an undefined point? | Hàm chưa xác định tại một điểm có thể có giới hạn hữu hạn không?**

A. The two-sided limit does not exist | Giới hạn hai phía không tồn tại

B. Distance per unit time | Khoảng cách trên mỗi đơn vị thời gian

C. Sampling spacing and numerical scheme | Khoảng cách mẫu và cách lấy sai phân

D. Yes, if nearby values approach one number | Có, nếu giá trị lân cận tiến đến cùng một số

**Đáp án: D**

**Giải thích:** Giới hạn có thể có dù hàm không xác định ngay điểm đó.


**Q17. How does a derivative differ from an average slope? | Đạo hàm khác độ dốc trung bình thế nào?**

A. It describes a local infinitesimal change | Nó mô tả độ thay đổi cục bộ rất nhỏ

B. 2 | 2

C. `sympy.diff` | `sympy.diff`

D. It often uses one-sided differences | Nó thường dùng sai phân một phía

**Đáp án: A**

**Giải thích:** Độ dốc tức thời là đại lượng giới hạn cục bộ.


**Q18. What is the derivative of 2x+3? | Đạo hàm của 2x+3 là gì?**

A. It describes a local infinitesimal change | Nó mô tả độ thay đổi cục bộ rất nhỏ

B. 2 | 2

C. `sympy.diff` | `sympy.diff`

D. It often uses one-sided differences | Nó thường dùng sai phân một phía

**Đáp án: B**

**Giải thích:** Hệ số của x cho đạo hàm bằng 2.


**Q19. Which tool calculates symbolic derivatives? | Công cụ nào tính đạo hàm ký hiệu?**

A. It describes a local infinitesimal change | Nó mô tả độ thay đổi cục bộ rất nhỏ

B. 2 | 2

C. `sympy.diff` | `sympy.diff`

D. It often uses one-sided differences | Nó thường dùng sai phân một phía

**Đáp án: C**

**Giải thích:** SymPy hỗ trợ đạo hàm ký hiệu bằng diff.


**Q20. Why is a numerical gradient at a boundary less accurate? | Vì sao gradient số ở biên có thể kém chính xác hơn?**

A. It describes a local infinitesimal change | Nó mô tả độ thay đổi cục bộ rất nhỏ

B. 2 | 2

C. `sympy.diff` | `sympy.diff`

D. It often uses one-sided differences | Nó thường dùng sai phân một phía

**Đáp án: D**

**Giải thích:** Ước lượng ở đầu dãy thường dùng dữ liệu một phía.

## 8. Bài tiếp theo

`Hàm số → Limit → Derivative → Gradient`.
