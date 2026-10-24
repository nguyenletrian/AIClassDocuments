# PY-31 — Giới hạn, tính liên tục và đạo hàm


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Limit** — giới hạn; **Continuity** — tính liên tục.

`Hàm số → Limit → Derivative → Gradient`

Kiến thức này liên quan đến việc biểu diễn, đánh giá hoặc tối ưu tính toán phục vụ AI. Đọc ví dụ trước khi liên hệ tới mô hình phức tạp.

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

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Giới hạn tại điểm khuyết của biểu thức

**Tình huống thực tế:** Một công thức chuẩn hóa cho ra `f(x)=(x²−4)/(x−2)`; tại x=2 mẫu số bằng 0. Nhóm phân tích muốn biết **giá trị mà công thức tiến gần**, không cố tính f(2).

**Vì sao chọn cách giải này?** Dùng giới hạn vì phép thay thế trực tiếp bị chia cho 0, còn xu hướng hai phía vẫn có thể tồn tại.

**Quy trình giải:**

1. Đặt x là biến ký hiệu.
2. Tạo biểu thức với tử và mẫu, chọn điểm x=2.
3. Gọi `sp.limit`, in giới hạn.

```python
import sympy as sp

x = sp.symbols('x')
f = (x ** 2 - 4) / (x - 2)
print(sp.limit(f, x, 2))
```

**Kết quả khi chạy:**

```text
4
```

Giới hạn là 4; biểu thức gốc vẫn không xác định tại x=2.

### Tình huống 2 — Tính vận tốc từ mô hình quãng đường

**Tình huống thực tế:** Một robot được mô phỏng theo `s(t)=t²` mét, t tính bằng giây. Cần tìm vận tốc tức thời tại t=3 giây, thay vì vận tốc trung bình trên cả hành trình.

**Vì sao chọn cách giải này?** Vận tốc là đạo hàm quãng đường theo thời gian, có đơn vị mét/giây.

**Quy trình giải:**

1. Khai báo t và hàm quãng đường.
2. Lấy đạo hàm s'(t)=2t.
3. Thay t=3 rồi in vận tốc.

```python
import sympy as sp

t = sp.symbols('t')
s = t ** 2
v = sp.diff(s, t)
print(v.subs(t, 3))
```

**Kết quả khi chạy:**

```text
6
```

Vận tốc tức thời theo mô hình là 6 m/s.

### Tình huống 3 — Độ dốc của hàm doanh thu

**Tình huống thực tế:** Mô hình doanh thu giả định `R(x)=2x²+3x` nghìn đồng, x là số đơn vị hàng. Đội vận hành muốn biết mức doanh thu thay đổi cục bộ quanh x=4, chưa xét việc x chỉ nhận số nguyên trong giao dịch thực tế.

**Vì sao chọn cách giải này?** Đạo hàm chỉ ra độ tăng cục bộ của mô hình liên tục, không phải tổng doanh thu tại x=4.

**Quy trình giải:**

1. Tạo biểu thức R(x)=2x²+3x.
2. Tính R'(x)=4x+3.
3. Thay x=4, in độ dốc.

```python
import sympy as sp

x = sp.symbols('x')
revenue = 2 * x ** 2 + 3 * x
print(sp.diff(revenue, x).subs(x, 4))
```

**Kết quả khi chạy:**

```text
19
```

Độ dốc là 19 nghìn đồng mỗi đơn vị hàng theo mô hình liên tục.

### Tình huống 4 — Kiểm tra tính liên tục của hàm số

**Tình huống thực tế:** Mô hình tính vị trí `f(x)=x²` tại x=2 mét đầu vào. Cần xem giới hạn của hàm tại điểm này có bằng chính giá trị f(2) hay không.

**Vì sao chọn cách giải này?** So giới hạn với giá trị hàm là kiểm tra định nghĩa liên tục tại điểm đã chọn.

**Quy trình giải:**

1. Định nghĩa hàm và điểm x=2.
2. Tính giới hạn và giá trị tại điểm.
3. In kết quả so sánh Boolean.

```python
import sympy as sp

x = sp.symbols('x')
f = x ** 2
print(sp.limit(f, x, 2) == f.subs(x, 2))
```

**Kết quả khi chạy:**

```text
True
```

Mô hình liên tục tại x=2 vì giới hạn và giá trị thực của hàm đều là 4.

### Tình huống 5 — Ước lượng vận tốc từ năm lần đo

**Tình huống thực tế:** Cảm biến ghi quãng đường theo mô hình `s=t²` mét ở thời điểm 0,1,2,3,4 giây. Chỉ có năm mẫu rời rạc, nên cần **ước lượng** đạo hàm thay vì dùng biểu thức ký hiệu.

**Vì sao chọn cách giải này?** `np.gradient` dùng chênh lệch hữu hạn; biên có thể kém chính xác hơn các điểm giữa.

**Quy trình giải:**

1. Tạo trục thời gian năm giây và quãng đường tương ứng.
2. Gọi `np.gradient(distance,time)`.
3. In năm ước lượng vận tốc theo m/s.

```python
import numpy as np

time = np.arange(5, dtype=float)
distance = time ** 2
print(np.gradient(distance, time))
```

**Kết quả khi chạy:**

```text
[1. 2. 4. 6. 7.]
```

Ở các điểm giữa, ước lượng bằng đạo hàm 2t; hai đầu dùng sai phân một phía nên khác giá trị tức thời chính xác.

## 6. Sai lầm thường gặp

- Giới hạn không nhất thiết bằng giá trị hàm tại điểm nếu hàm không liên tục hoặc không xác định ở đó.
- Muốn liên tục cần giới hạn trái, phải và giá trị hàm bằng nhau.
- Đạo hàm là tốc độ thay đổi tức thời; độ dốc trung bình trên một khoảng có thể khác.
- Với quãng đường theo giây, đạo hàm có đơn vị m/s; không diễn giải thành mét.
- `np.gradient` xấp xỉ từ mẫu; ở đầu và cuối dãy thường dùng sai phân một phía.
- SymPy là thư viện ngoài cần cài khi chạy các ví dụ ký hiệu.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Q1. What does a limit describe? — Giới hạn mô tả gì?**

A. What f(x) approaches as x approaches a point — Giá trị f(x) tiến đến khi x tiến gần một điểm

B. The two-sided limit exists and equals f(a) — Giới hạn hai phía tồn tại và bằng f(a)

C. Instantaneous rate of change — Tốc độ thay đổi tức thời

D. The derivative evaluated at a — Giá trị đạo hàm tại a

**Q2. What does continuity at x=a require? — Liên tục tại x=a cần gì?**

A. What f(x) approaches as x approaches a point — Giá trị f(x) tiến đến khi x tiến gần một điểm

B. The two-sided limit exists and equals f(a) — Giới hạn hai phía tồn tại và bằng f(a)

C. Instantaneous rate of change — Tốc độ thay đổi tức thời

D. The derivative evaluated at a — Giá trị đạo hàm tại a

**Q3. What does a derivative describe? — Đạo hàm mô tả gì?**

A. What f(x) approaches as x approaches a point — Giá trị f(x) tiến đến khi x tiến gần một điểm

B. The two-sided limit exists and equals f(a) — Giới hạn hai phía tồn tại và bằng f(a)

C. Instantaneous rate of change — Tốc độ thay đổi tức thời

D. The derivative evaluated at a — Giá trị đạo hàm tại a

**Q4. What is tangent slope at x=a? — Độ dốc tiếp tuyến tại x=a là gì?**

A. What f(x) approaches as x approaches a point — Giá trị f(x) tiến đến khi x tiến gần một điểm

B. The two-sided limit exists and equals f(a) — Giới hạn hai phía tồn tại và bằng f(a)

C. Instantaneous rate of change — Tốc độ thay đổi tức thời

D. The derivative evaluated at a — Giá trị đạo hàm tại a

**Q5. What does `sp.limit(f,x,a)` calculate? — `sp.limit(f,x,a)` tính gì?**

A. The limit of f as x approaches a — Giới hạn của f khi x tiến đến a

B. The derivative of f with respect to x — Đạo hàm f theo biến x

C. Substitutes a into symbolic expression — Thay a vào biểu thức ký hiệu

D. Derivatives from sampled y and x values — Đạo hàm từ các giá trị y, x lấy mẫu

**Q6. What does `sp.diff(f,x)` return? — `sp.diff(f,x)` trả gì?**

A. The limit of f as x approaches a — Giới hạn của f khi x tiến đến a

B. The derivative of f with respect to x — Đạo hàm f theo biến x

C. Substitutes a into symbolic expression — Thay a vào biểu thức ký hiệu

D. Derivatives from sampled y and x values — Đạo hàm từ các giá trị y, x lấy mẫu

**Q7. What does `expr.subs(x,a)` do? — `expr.subs(x,a)` làm gì?**

A. The limit of f as x approaches a — Giới hạn của f khi x tiến đến a

B. The derivative of f with respect to x — Đạo hàm f theo biến x

C. Substitutes a into symbolic expression — Thay a vào biểu thức ký hiệu

D. Derivatives from sampled y and x values — Đạo hàm từ các giá trị y, x lấy mẫu

**Q8. What does `np.gradient(y,x)` approximate? — `np.gradient(y,x)` xấp xỉ gì?**

A. The limit of f as x approaches a — Giới hạn của f khi x tiến đến a

B. The derivative of f with respect to x — Đạo hàm f theo biến x

C. Substitutes a into symbolic expression — Thay a vào biểu thức ký hiệu

D. Derivatives from sampled y and x values — Đạo hàm từ các giá trị y, x lấy mẫu

**Q9. What is the derivative of x²? — Đạo hàm của x² là gì?**

A. `2*x` — `2*x`

B. Zero — Bằng 0

C. 6 — 6

D. 4 — 4

**Q10. What is the derivative of a constant? — Đạo hàm của một hằng số là gì?**

A. `2*x` — `2*x`

B. Zero — Bằng 0

C. 6 — 6

D. 4 — 4

**Q11. What is the slope of x² at x=3? — Độ dốc của x² tại x=3 là gì?**

A. `2*x` — `2*x`

B. Zero — Bằng 0

C. 6 — 6

D. 4 — 4

**Q12. What is the limit of (x²−4)/(x−2) at x=2? — Giới hạn của (x²−4)/(x−2) khi x→2 là gì?**

A. `2*x` — `2*x`

B. Zero — Bằng 0

C. 6 — 6

D. 4 — 4

**Q13. What may happen if the left and right limits differ? — Nếu giới hạn trái và phải khác nhau thì sao?**

A. The two-sided limit does not exist — Giới hạn hai phía không tồn tại

B. Distance per unit time — Khoảng cách trên mỗi đơn vị thời gian

C. Sampling spacing and numerical scheme — Khoảng cách mẫu và cách lấy sai phân

D. Yes, if nearby values approach one number — Có, nếu giá trị lân cận tiến đến cùng một số

**Q14. What does a derivative unit become for distance over time? — Đạo hàm quãng đường theo thời gian có đơn vị gì?**

A. The two-sided limit does not exist — Giới hạn hai phía không tồn tại

B. Distance per unit time — Khoảng cách trên mỗi đơn vị thời gian

C. Sampling spacing and numerical scheme — Khoảng cách mẫu và cách lấy sai phân

D. Yes, if nearby values approach one number — Có, nếu giá trị lân cận tiến đến cùng một số

**Q15. What determines finite-difference accuracy? — Độ chính xác sai phân hữu hạn phụ thuộc gì?**

A. The two-sided limit does not exist — Giới hạn hai phía không tồn tại

B. Distance per unit time — Khoảng cách trên mỗi đơn vị thời gian

C. Sampling spacing and numerical scheme — Khoảng cách mẫu và cách lấy sai phân

D. Yes, if nearby values approach one number — Có, nếu giá trị lân cận tiến đến cùng một số

**Q16. Can a function have a finite limit at an undefined point? — Hàm chưa xác định tại một điểm có thể có giới hạn hữu hạn không?**

A. The two-sided limit does not exist — Giới hạn hai phía không tồn tại

B. Distance per unit time — Khoảng cách trên mỗi đơn vị thời gian

C. Sampling spacing and numerical scheme — Khoảng cách mẫu và cách lấy sai phân

D. Yes, if nearby values approach one number — Có, nếu giá trị lân cận tiến đến cùng một số

**Q17. How does a derivative differ from an average slope? — Đạo hàm khác độ dốc trung bình thế nào?**

A. It describes a local infinitesimal change — Nó mô tả độ thay đổi cục bộ rất nhỏ

B. 2 — 2

C. `sympy.diff` — `sympy.diff`

D. It often uses one-sided differences — Nó thường dùng sai phân một phía

**Q18. What is the derivative of 2x+3? — Đạo hàm của 2x+3 là gì?**

A. It describes a local infinitesimal change — Nó mô tả độ thay đổi cục bộ rất nhỏ

B. 2 — 2

C. `sympy.diff` — `sympy.diff`

D. It often uses one-sided differences — Nó thường dùng sai phân một phía

**Q19. Which tool calculates symbolic derivatives? — Công cụ nào tính đạo hàm ký hiệu?**

A. It describes a local infinitesimal change — Nó mô tả độ thay đổi cục bộ rất nhỏ

B. 2 — 2

C. `sympy.diff` — `sympy.diff`

D. It often uses one-sided differences — Nó thường dùng sai phân một phía

**Q20. Why is a numerical gradient at a boundary less accurate? — Vì sao gradient số ở biên có thể kém chính xác hơn?**

A. It describes a local infinitesimal change — Nó mô tả độ thay đổi cục bộ rất nhỏ

B. 2 — 2

C. `sympy.diff` — `sympy.diff`

D. It often uses one-sided differences — Nó thường dùng sai phân một phía

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | A limit concerns nearby input values. | Giới hạn xét đầu vào lân cận điểm. |
| Q2 | **B** | Continuity requires limit and function value to match. | Liên tục đòi hỏi giới hạn bằng giá trị hàm. |
| Q3 | **C** | Derivative measures change at a point. | Đạo hàm đo độ thay đổi tại điểm. |
| Q4 | **D** | The slope of the tangent is f'(a). | Độ dốc tiếp tuyến là f'(a). |
| Q5 | **A** | limit is symbolic and need not substitute at a singularity. | limit tính giới hạn mà không cần thế tại điểm kỳ dị. |
| Q6 | **B** | diff computes a symbolic derivative. | diff tính đạo hàm ký hiệu. |
| Q7 | **C** | subs evaluates a symbolic expression by substitution. | subs thay giá trị vào biểu thức ký hiệu. |
| Q8 | **D** | gradient estimates derivatives from samples. | gradient xấp xỉ đạo hàm từ mẫu. |
| Q9 | **A** | The power rule gives 2x. | Quy tắc đạo hàm lũy thừa cho 2x. |
| Q10 | **B** | A constant does not change. | Hằng số không đổi theo biến. |
| Q11 | **C** | 2×3 equals six. | 2 nhân 3 bằng sáu. |
| Q12 | **D** | The removable factor leaves x+2 nearby. | Rút gọn gần điểm còn x+2. |
| Q13 | **A** | Unequal one-sided limits prevent a two-sided limit. | Giới hạn một phía khác nhau khiến giới hạn hai phía không có. |
| Q14 | **B** | Dividing distance by time gives speed units. | Quãng đường chia thời gian cho đơn vị vận tốc. |
| Q15 | **C** | Sample spacing affects estimated slopes. | Khoảng lấy mẫu ảnh hưởng độ dốc ước lượng. |
| Q16 | **D** | The limit can exist even if the original point is undefined. | Giới hạn có thể có dù hàm không xác định ngay điểm đó. |
| Q17 | **A** | Instantaneous slope is a limiting local quantity. | Độ dốc tức thời là đại lượng giới hạn cục bộ. |
| Q18 | **B** | The slope coefficient of 2x is two. | Hệ số của x cho đạo hàm bằng 2. |
| Q19 | **C** | SymPy exposes symbolic differentiation with diff. | SymPy hỗ trợ đạo hàm ký hiệu bằng diff. |
| Q20 | **D** | Endpoint estimates frequently rely on one-sided data. | Ước lượng ở đầu dãy thường dùng dữ liệu một phía. |

## 8. Bài tiếp theo

`Hàm số → Limit → Derivative → Gradient`.
