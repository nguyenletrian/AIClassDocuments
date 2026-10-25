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

**No Note — Không chú thích**

```python
import sympy as sp

x = sp.symbols('x')
f = (x ** 2 - 4) / (x - 2)
print(sp.limit(f, x, 2))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tìm giới hạn ở x=2 của biểu thức không xác định trực tiếp tại x=2.
# Dữ liệu: Hàm (x²-4)/(x-2); điểm x=2 làm mẫu số bằng 0 nhưng có giới hạn hữu hạn.
# SymPy tính toán biểu thức toán học bằng ký hiệu, sp là tên ngắn của thư viện.
import sympy as sp

# symbols('x') tạo biến KÝ HIỆU, khác một số x đã gán giá trị.
x = sp.symbols('x')
# Tại x=2 biểu thức 0/0 chưa xác định; với x khác 2 biểu thức rút gọn được thành x+2.
f = (x ** 2 - 4) / (x - 2)
# limit(biểu_thức, biến, điểm) xét giá trị tiến GẦN 2, không thay x=2 trực tiếp; kết quả 4.
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

**No Note — Không chú thích**

```python
import sympy as sp

t = sp.symbols('t')
s = t ** 2
print(sp.limit(s, t, 2) == s.subs(t, 2))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Kiểm tính liên tục bằng so giới hạn với giá trị hàm tại t=2.
# Dữ liệu: Hàm vị trí s=t² không đứt đoạn tại t=2.
# SymPy biểu diễn ký hiệu và tính giới hạn.
import sympy as sp

# Tạo biến ký hiệu t dùng cho hàm s.
t = sp.symbols('t')
# **2 nâng t lên bình phương, đây là hàm vị trí giả lập.
s = t ** 2
# Lấy giá trị hàm TIẾN ĐẾN khi t gần 2.
# subs(t,2) THẾ t=2 vào biểu thức để lấy đúng giá trị tại điểm; hai giá trị bằng nhau nghĩa liên tục ở đây.
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

**No Note — Không chú thích**

```python
import sympy as sp

x = sp.symbols('x')
print(sp.diff(x ** 2, x))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Dùng đạo hàm ký hiệu tìm tốc độ thay đổi của x² theo x.
# Dữ liệu: Hàm f=x², cần biểu thức độ dốc thay đổi theo từng x.
# SymPy sp.diff() lấy đạo hàm của biểu thức theo biến ký hiệu.
import sympy as sp

# Khai báo x là biến tượng trưng thay vì một số cụ thể.
x = sp.symbols('x')
# diff(f,x) đạo hàm theo x; độ dốc của x² là 2x tại từng vị trí, print() hiển thị biểu thức.
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

**No Note — Không chú thích**

```python
import sympy as sp

x = sp.symbols('x')
slope = sp.diff(x ** 2, x)
print(slope.subs(x, 3))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tính độ dốc tức thời tại x=3 bằng đạo hàm rồi thế biến.
# Dữ liệu: Hàm f=x², hỏi độ dốc tại x=3 (đơn vị đầu ra trên một đơn vị đầu vào).
# SymPy tách bước tính đạo hàm và bước thế giá trị.
import sympy as sp

# Biến x ký hiệu giữ công thức còn phụ thuộc x.
x = sp.symbols('x')
# diff() tạo biểu thức đạo hàm 2x, chưa phải độ dốc tại một điểm.
slope = sp.diff(x ** 2, x)
# subs(x,3) thay x=3 trong ĐẠO HÀM, kết quả độ dốc 6, không phải f(3)=9.
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

**Tình huống thực tế:** Một phần mềm hiệu chuẩn nhận **10 giá trị tín hiệu x không có đơn vị**, gồm năm giá trị ngay dưới 2 và năm giá trị ngay trên 2. Công thức đổi tín hiệu thành chỉ số có phép chia cho phần chênh lệch giữa x và 2, nên nếu nhập đúng **x = 2** chương trình không chia được. Kỹ thuật viên muốn xem kết quả **tiến gần giá trị nào từ cả hai phía**, để hiểu điểm bị khuyết chứ không tự coi phép chia tại 2 là hợp lệ.

**Vì sao chọn cách này?** **Giới hạn** giúp trả lời giá trị của biểu thức đang **tiến tới đâu khi đầu vào tới gần một điểm**, kể cả khi không thể tính biểu thức đúng tại điểm đó. Chương trình thử năm số **nhỏ hơn 2** và năm số **lớn hơn 2**, nhưng cố ý **không có đúng 2** để tránh chia cho 0. Hai phía cùng tiến gần một chỉ số; `sympy.limit` dùng tính toán ký hiệu để xác định giá trị tiến tới một cách chính xác hơn việc đoán bằng vài số thập phân. Giá trị giới hạn **không tự làm công thức gốc tại x=2 có nghĩa**; nếu muốn dùng ở điểm khuyết, phải định nghĩa rõ quy tắc bổ sung.

**Quy trình:**
1. Tạo 10 số đầu vào, không có số nào bằng 2.
2. Tính đầu ra ở hai giá trị gần nhất, quan sát chúng xấp xỉ nhau.
3. Dùng SymPy xác định giới hạn tại 2 và đối chiếu.

**No Note — Không chú thích**

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

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Dò 10 giá trị hàm từ hai phía gần x=2 và so với giới hạn chính xác.
# Dữ liệu: 10 giá trị x từ 1.9 đến 2.001, không có x=2 vì mẫu số bằng 0; kết quả tiến gần 4.
# SymPy giúp tính công thức ở các điểm và lấy giới hạn chính xác.
import sympy as sp
# Tạo ký hiệu x cho biểu thức hữu tỉ.
x = sp.symbols("x")
# Ở đúng x=2 phép chia không xác định; ở gần 2 hàm tiến tới 4.
f = (x**2 - 4) / (x - 2)
# 10 điểm khảo sát từ trái (<2) và phải (>2), không phải 10 mẫu ngẫu nhiên.
inputs = [1.9,1.95,1.99,1.995,1.999,2.1,2.05,2.01,2.005,2.001]
# List rỗng để lưu giá trị f tại từng điểm theo thứ tự.
results = []
# Lặp qua từng giá trị x trong list.
for value in inputs:
    # subs() thế từng x vào biểu thức; float() đổi kết quả SymPy sang số thực Python để in.
    # append() giữ một đầu ra cho mỗi x.
    results.append(float(f.subs(x, value)))
# limit() lấy giới hạn ký hiệu tại 2, không đánh giá f(2).
limit_at_two = sp.limit(f, x, 2)
# in kiểm có vô tình đưa giá trị bị chia 0 vào list hay không.
if len(inputs) != 10 or 2 in inputs:
    # ValueError báo lỗi cấu trúc dữ liệu và ngừng xử lý, tránh kết quả thiếu/không phù hợp.
    raise ValueError("Cần đúng 10 điểm tiến gần 2, không lấy đúng x=2.")
print("Lượt đo:", len(inputs))
# [4] là điểm cuối nhóm bên trái x=1.999; [-1] là điểm cuối nhóm bên phải x=2.001, :.3f in ba số lẻ.
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

**Tình huống thực tế:** Robot chạy theo quy tắc quãng đường **tăng theo bình phương thời gian**, với thời gian tính bằng **giây** và quãng đường tính bằng **mét**. Người vận hành có **12 mốc từ 0 đến 11 giây** và muốn biết **vận tốc tức thời** ở mỗi mốc, đặc biệt so mốc **3 giây và 11 giây**. Vận tốc là mức quãng đường đang tăng trong một giây tại thời điểm ấy, không phải tổng số mét robot đã đi.

**Vì sao chọn cách này?** **Đạo hàm theo thời gian** cho biết quãng đường **đang thay đổi nhanh đến mức nào** tại một thời điểm, vì vậy dùng để tìm **vận tốc tức thời**, có đơn vị **mét/giây**. `sympy.diff(position, t)` tìm quy tắc tính vận tốc một lần từ quy tắc quãng đường; `subs(t, second)` thế lần lượt **12 mốc thời gian** để lấy kết quả cụ thể. Ở mốc sau, quãng đường tăng nhanh hơn nên vận tốc lớn hơn. Nếu lấy quãng đường tại 11 giây rồi gọi là vận tốc 11 m/giây thì đã **nhầm tổng quãng đường với tốc độ thay đổi**.

**Quy trình:**
1. Định nghĩa quãng đường bằng SymPy và lấy đạo hàm theo t.
2. Thay 12 mốc thời gian vào biểu thức vận tốc.
3. In vận tốc ở hai mốc và kiểm số lượng đầu ra.

**No Note — Không chú thích**

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

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tính vận tốc từ hàm vị trí s=t² tại 12 mốc thời gian.
# Dữ liệu: Thời gian t=0..11 giây, vị trí s=t² tính mét, vận tốc đạo hàm có đơn vị m/giây.
# SymPy đạo hàm công thức vị trí để suy ra vận tốc tức thời.
import sympy as sp
# t là ký hiệu thời gian có thể thay các mốc sau.
t = sp.symbols("t")
# Mô hình vị trí theo thời gian, đơn vị mét giả định.
position = t**2
# diff(s,t) cho vận tốc tức thời 2t (m/s); chưa gán mốc thời gian.
velocity = sp.diff(position, t)
# 12 giây từ 0 đến 11, mỗi mốc một số đo tính toán.
times = [0,1,2,3,4,5,6,7,8,9,10,11]
# Danh sách vận tốc sẽ được lưu cùng thứ tự với times.
values = []
for second in times:
    # subs() thế giây hiện tại vào biểu thức vận tốc, trả giá trị SymPy.
    # append() giữ kết quả một lần cho mỗi mốc.
    values.append(velocity.subs(t, second))
# Kiểm đủ cả 12 thời điểm và 12 kết quả để tránh thiếu mẫu.
if len(times) != 12 or len(values) != 12:
    # ValueError báo lỗi cấu trúc dữ liệu và ngừng xử lý, tránh kết quả thiếu/không phù hợp.
    raise ValueError("Cần đủ 12 mốc thời gian và 12 vận tốc.")
print("Mốc thời gian:", len(times))
# [3] ứng với giây thứ 3 (t=3); [-1] là mốc cuối t=11.
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

**Tình huống thực tế:** Một xưởng thử máy ở **15 mức tải từ 1 đến 15**, mỗi mức cách mức sau một đơn vị tải. Chi phí theo quy tắc mô phỏng **tăng nhanh hơn khi tải lớn**, tính bằng **nghìn đồng**. Quản đốc không chỉ hỏi tổng chi phí mà muốn biết **nếu tăng tải thêm một chút**, chi phí đang tăng nhanh cỡ nào tại tải **1** và tải **15**, để thấy vì sao phần tải cao tốn kém hơn.

**Vì sao chọn cách này?** **Chi phí cận biên** trong ví dụ là mức thay đổi của chi phí khi **tải tăng một lượng rất nhỏ** quanh một mức đang xét; đây là **độ dốc**, không phải tổng tiền hóa đơn. `sympy.diff(cost, q)` tìm quy tắc độ dốc của đường chi phí, sau đó chương trình thế vào **15 mức tải** để so mức đầu và cuối. Với đường cong bậc hai đang dùng, độ dốc lớn dần khi tải tăng. Cần phân biệt **đạo hàm tại một điểm** với phần chênh lệch tổng chi phí giữa hai mức tải cách xa nhau; chúng không phải cùng một câu hỏi.

**Quy trình:**
1. Lưu 15 mức tải và hàm chi phí tương ứng.
2. Lấy đạo hàm theo q, thay từng mức tải vào.
3. Báo độ dốc đầu và cuối, xác nhận dãy độ dốc tăng.

**No Note — Không chú thích**

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

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tìm chi phí biên tại 15 mức tải bằng đạo hàm và kiểm độ dốc có tăng.
# Dữ liệu: Mô hình cost=2q²+3q+10, q là mức tải 1..15; đơn vị chi phí giả lập.
# SymPy đạo hàm hàm chi phí theo ký hiệu q.
import sympy as sp
# q là biến tải tượng trưng để tạo đạo hàm tổng quát.
q = sp.symbols("q")
# Mô hình phi tuyến: bình phương tải khiến chi phí biên tăng khi q lớn.
cost = 2*q**2 + 3*q + 10
# Đạo hàm theo q trả tốc độ tăng chi phí tại từng tải, gọi là marginal cost.
marginal = sp.diff(cost, q)
# 15 mức tải liên tục từ 1 đến 15.
loads = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
slopes = []
for load in loads:
    # Thế từng tải vào đạo hàm; int() đổi SymPy Integer về int Python.
    # append() lưu 15 chi phí biên theo thứ tự tải.
    slopes.append(int(marginal.subs(q, load)))
if len(slopes) != 15:
    # ValueError báo lỗi cấu trúc dữ liệu và ngừng xử lý, tránh kết quả thiếu/không phù hợp.
    raise ValueError("Cần tính đủ 15 mức tải.")
print("Mức tải:", len(slopes))
# [0] chi phí biên tại q=1, [-1] tại q=15.
print("Mức tăng ở tải 1:", slopes[0])
print("Mức tăng ở tải 15:", slopes[-1])
slopes_increase = True
# zip() ghép mỗi độ dốc với độ dốc KẾ TIẾP; slopes[1:] bỏ mục đầu, giúp kiểm tính tăng.
for a, b in zip(slopes, slopes[1:]):
    # Nếu một độ dốc không nhỏ hơn độ dốc sau thì không còn tăng nghiêm ngặt.
    if a >= b:
        slopes_increase = False
        # break thoát sớm khi tìm được trường hợp không tăng.
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

**Tình huống thực tế:** Một ứng dụng tính **chỉ số phụ phí giả lập** theo số giờ t: trước **8 giờ** dùng một quy định, từ **8 giờ trở đi** đổi sang quy định khác. Hệ thống ghi **18 mốc 0–17 giờ**; ngay trước mốc 8, chỉ số tiến gần **13**, còn bắt đầu từ 8 nó bằng **15**. Người quản lý muốn biết có một **bước nhảy đột ngột** tại thời điểm đổi quy định hay không, chứ không chỉ nhìn bảng giờ nguyên.

**Vì sao chọn cách này?** **Liên tục** tại một thời điểm nghĩa là khi tiến tới điểm đó từ **bên trái và bên phải**, kết quả đều tiến về **chính giá trị tại điểm ấy**. `sp.limit` kiểm hai biểu thức riêng ở mốc **8 giờ**, còn `values[8]` cho giá trị chương trình thật sự áp dụng tại mốc đó. Bên trái tiến tới 13 nhưng bên phải và tại 8 là 15, nên **không liên tục**: có bước nhảy 2 đơn vị chỉ số phụ phí. Một bảng chỉ có các mốc giờ nguyên không thể thay thế việc kiểm tra sát hai phía, vì có thể bỏ qua hành vi ngay nơi đổi chính sách.

**Quy trình:**
1. Tạo 18 thời điểm và tính đầu ra theo đúng hai nhánh.
2. Dùng `sympy.limit` cho biểu thức nhánh trái/phải khi t tới 8.
3. So hai giới hạn với giá trị hàm tại 8 rồi báo kết luận.

**No Note — Không chú thích**

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

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Xét tính liên tục tại giờ 8 của hàm được định nghĩa theo hai nhánh.
# Dữ liệu: 18 mốc giờ 0..17; trước giờ 8 là t+5, từ giờ 8 là t+7, nên có bước nhảy tại 8.
# SymPy tính giới hạn biểu thức của từng nhánh tại ranh giới.
import sympy as sp
# t là biến thời gian ký hiệu.
t = sp.symbols("t")
# 18 mốc giờ, giờ 8 là điểm chuyển từ nhánh trái sang phải.
times = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
values = []
for hour in times:
    # Nhánh áp dụng trước giờ 8: output=hour+5.
    if hour < 8:
        # Giá trị của nhánh trái, ứng với giờ nhỏ hơn 8.
        value = hour + 5
    else:
        # Giá trị tại và sau giờ 8, nhánh phải.
        value = hour + 7
    # Ghi đầu ra của từng giờ, [8] là giá trị thực tế tại điểm chuyển.
    values.append(value)
# Tính giới hạn công thức NHÁNH TRÁI t+5 tại mốc 8; không ghép hai nhánh.
left = sp.limit(t + 5, t, 8)
# Tính giới hạn công thức NHÁNH PHẢI t+7 tại 8; hai nhánh cho giới hạn khác nhau.
right = sp.limit(t + 7, t, 8)
# Chuỗi == yêu cầu giới hạn trái, phải và giá trị tại điểm đều bằng nhau; False nghĩa gián đoạn.
# [8] lấy giá trị của mốc 8 vì list bắt đầu từ 0.
continuous = left == right == values[8]
if len(times) != 18:
    # ValueError báo lỗi cấu trúc dữ liệu và ngừng xử lý, tránh kết quả thiếu/không phù hợp.
    raise ValueError("Cần đủ 18 mốc giờ.")
print("Mốc giờ:", len(times))
print("Giới hạn trái:", left)
print("Giới hạn phải:", right)
# [8] lấy giá trị của mốc 8 vì list bắt đầu từ 0.
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

**Tình huống thực tế:** Robot ghi **20 cặp thời gian và quãng đường**, tính bằng **giây** và **mét**, nhưng khoảng cách giữa các lần lấy mẫu **không đều**: có lần sau 1 giây, lần sau 2 giây. Quãng đường được tạo theo một quy tắc cong tăng dần. Kỹ thuật viên muốn ước lượng **vận tốc** từ chính các số đo, so với vận tốc chính xác của quy tắc mô phỏng và xem vì sao lượt đầu/lượt cuối dễ sai khác hơn những lượt ở giữa.

**Vì sao chọn cách này?** **Đạo hàm số** là ước lượng tốc độ thay đổi bằng các **giá trị đo gần nhau**, hữu ích khi có bảng số thay vì chỉ một biểu thức dễ lấy đạo hàm. `np.gradient(s, t)` nhận **cả quãng đường và các thời điểm thực tế**, vì các lần đo không cách đều; bỏ mảng thời gian sẽ ngầm giả định khoảng cách giữa lượt đo giống nhau. Ở các điểm **giữa**, NumPy có số đo ở **cả phía trước và phía sau** để ước lượng, trong khi ở hai **mép** mặc định chỉ dùng chênh lệch một phía. Với đường cong bậc hai trong bài, các điểm giữa khớp đạo hàm chính xác nhưng hai mép có sai số: đó là giới hạn của cách ước lượng, không có nghĩa cảm biến biên bị hỏng.

**Quy trình:**
1. Tạo 20 thời điểm và quãng đường theo cùng thứ tự.
2. Tính vận tốc số bằng `np.gradient` có truyền thời gian, so với `2*t+2`.
3. Kiểm 18 điểm trong khớp và in sai số mép đầu/cuối.

**No Note — Không chú thích**

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

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: So đạo hàm số np.gradient với đạo hàm giải tích tại 20 thời điểm không cách đều.
# Dữ liệu: 20 thời điểm t tăng dần, vị trí s=t²+2t tính mét, vận tốc chuẩn 2t+2 m/giây.
# NumPy np.gradient() ước lượng đạo hàm khi chỉ có giá trị đo rời rạc.
import numpy as np
# 20 thời điểm tăng dần KHÔNG đều, dtype=float để tính khoảng cách chính xác.
t = np.array([0,1,3,4,6,7,9,10,12,13,15,16,18,19,21,22,24,25,27,28], dtype=float)
# Mảng s chứa vị trí tại mỗi thời điểm, với **2 bình phương từng phần tử.
s = t**2 + 2*t
# gradient(y,x) xấp xỉ ds/dt từ dữ liệu, dùng chính vector thời gian t để xử lý bước lấy mẫu không đều; mép dùng sai phân một phía mặc định.
numerical = np.gradient(s, t)
# Đạo hàm giải tích thật của t²+2t tại từng t, làm mốc đối chiếu.
analytical = 2*t + 2
# diff(t) lấy độ chênh mốc liên tiếp; >0 kiểm mọi thời điểm đi lên để không có bước âm/trùng.
# np.all() yêu cầu tất cả khoảng cách dương, không chỉ một khoảng.
if len(t) != 20 or not np.all(np.diff(t) > 0):
    # ValueError báo lỗi cấu trúc dữ liệu và ngừng xử lý, tránh kết quả thiếu/không phù hợp.
    raise ValueError("Cần 20 mốc thời gian tăng dần.")
print("Số lần đo:", len(t))
# Slice [1:-1] lấy toàn bộ các điểm GIỮA, bỏ hai điểm biên; so với analytical bằng allclose() có dung sai float.
# Dùng cùng slice bỏ hai biên ở giá trị chuẩn để so từng mốc.
# allclose() so hai vector gần nhau trong dung sai số thực, không dùng == tuyệt đối.
print("Giữa khớp:", bool(np.allclose(numerical[1:-1], analytical[1:-1])))
# [0] là đạo hàm ước lượng mép đầu; [-1] mép cuối, độ lệch được lấy abs() để không âm.
# So ước lượng tại đúng mép đầu với giá trị giải tích tương ứng.
print(f"Sai số mép đầu (m/giây): {abs(numerical[0]-analytical[0]):.1f}")
# [-1] lấy ước lượng đạo hàm mép cuối, có thể sai do chỉ dùng điểm một phía.
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
