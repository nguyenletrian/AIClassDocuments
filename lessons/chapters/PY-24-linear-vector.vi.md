# PY-24 — Scalar, vector, norm, đơn vị và dot product


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Scalar** — đại lượng vô hướng; **Vector** — véc-tơ.

`NumPy → Scalar/Vector → Matrix → PCA`

**Học xong dùng để làm gì?** Biểu diễn học viên hay sản phẩm dưới dạng vector đặc trưng số và thực hiện phép cộng/trừ vector.

**Kết nối kiến thức tiếp theo:** PY-25 xếp nhiều vector thành ma trận để tính cùng lúc nhiều quan sát.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích |
|---|---|---|
| Scalar | đại lượng vô hướng | Một số đơn lẻ có thể đo độ lớn |
| Vector | véc-tơ | Dãy số mô tả nhiều thành phần của một đối tượng |
| Norm | độ lớn véc-tơ | Độ dài theo chuẩn đã chọn |
| Dot product | tích vô hướng | Nhân từng cặp tọa độ tương ứng rồi cộng |

## 3. NumPy và các hàm liên quan

**Từ vựng trong mục:** **Function** — hàm; **Shape** — kích thước mảng.

| Hàm / tham số | Dùng làm gì |
|---|---|
| `np.array([...],dtype=float)` | Tạo véc-tơ kiểu thực khi phép tính tạo phần thập phân |
| `np.linalg.norm(v)` | Độ lớn Euclidean của véc-tơ |
| `v/np.linalg.norm(v)` | Chuẩn hóa về độ dài 1, phải tránh norm bằng 0 |
| `a @ b / np.dot(a,b)` | Tích vô hướng nếu hai vector một chiều cùng độ dài |

## 4. Khái niệm liên quan

Bài học nối bốn ý: **scalar** là số đơn lẻ, **vector** chứa tọa độ, **norm** đo độ dài, **dot product** kết hợp các thành phần. Robot dịch chuyển `(3,4)` mét có vector hai chiều nhưng quãng đường thẳng chỉ là một số bằng 5 mét.

### 4.1. Scalar — Số đơn lẻ và đơn vị

Scalar là một giá trị số như vận tốc 2,5 mét/giây. Python lưu số, còn ý nghĩa và đơn vị phải do người lập trình nêu. Scalar khác vector vì không chứa nhiều thành phần tọa độ.

**No Note — Không chú thích**

```python
speed = 2.5
print(speed)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Phân biệt một giá trị vô hướng với đại lượng có nhiều thành phần.
# Dữ liệu: speed=2.5 là một giá trị tốc độ giả lập; chưa biểu diễn hướng hay các trục tọa độ.
# 2.5 là scalar (số đơn) mô tả độ lớn; chưa phải vector hướng trong không gian.
speed = 2.5
# print() hiển thị số đang lưu để phân biệt scalar với mảng tọa độ.
print(speed)
```

**Kết quả khi chạy:**

```text
2.5
```

Số 2.5 đại diện vận tốc m/s, không phải tọa độ.

### 4.2. Vector — Các tọa độ có thứ tự

Vector là dãy tọa độ theo một hệ trục. Robot đi 3 m theo x và 4 m theo y nên dùng vector `[3,4]`. Phần tử đầu là x, phần tử sau là y. Đổi `[3,4]` thành `[4,3]` sẽ đổi ý nghĩa hai trục.

**No Note — Không chú thích**

```python
import numpy as np

movement = np.array([3, 4])
print(movement)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Biểu diễn độ dịch chuyển hai chiều bằng vector các tọa độ x,y có thứ tự.
# Dữ liệu: Vector [3,4] gồm hai thành phần tọa độ x và y, không phải hai mẫu dữ liệu độc lập.
# NumPy tạo vector từ list và thực hiện các phép toán theo phần tử.
import numpy as np

# np.array() tạo ndarray một chiều shape (2,); vị trí 0 là x=3, vị trí 1 là y=4.
movement = np.array([3, 4])
# In hai tọa độ theo thứ tự, không tự tính độ dài.
print(movement)
```

**Kết quả khi chạy:**

```text
[3 4]
```

Hai phần tử lần lượt là độ dịch chuyển theo x và y (mét).

### 4.3. Norm — Độ dài vector

Chuẩn Euclid là độ dài `sqrt(x²+y²)`. Với vector `(3,4)`, độ dài bằng `sqrt(9+16)=5` m. Vector đơn vị giữ hướng và có norm bằng 1; muốn chuẩn hóa phải chia các thành phần cho norm, trừ trường hợp norm bằng 0.

**No Note — Không chú thích**

```python
import numpy as np

movement = np.array([3.0, 4.0])
print(np.linalg.norm(movement))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tính độ dài Euclid của vector chuyển động (3,4) bằng NumPy.
# Dữ liệu: Hai thành phần x=3, y=4 theo cùng đơn vị khoảng cách.
# NumPy hỗ trợ phép tính độ dài vector trong np.linalg.
import numpy as np

# dtype suy ra số thực vì tọa độ có dấu thập phân; mỗi ô là một trục.
movement = np.array([3.0, 4.0])
# linalg.norm(vector) mặc định tính độ dài Euclid: căn tổng bình phương các thành phần, ở đây 5 đơn vị.
print(np.linalg.norm(movement))
```

**Kết quả khi chạy:**

```text
5.0
```

Robot cách gốc tọa độ 5 mét theo đường thẳng.

### 4.4. Dot product — Nhân và cộng cùng vị trí

Tích vô hướng của hai vector cùng số chiều bằng tổng các tích từng thành phần: `(1,2)·(3,4)=1×3+2×4=11`. Dùng để tính điểm có trọng số hoặc kiểm tra hai vector khác không vuông góc (khi tích vô hướng bằng 0).

**No Note — Không chú thích**

```python
import numpy as np

a = np.array([1, 2])
b = np.array([3, 4])
print(a @ b)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tính tích vô hướng của hai vector hai chiều bằng toán tử @.
# Dữ liệu: a=[1,2], b=[3,4]; các thành phần cùng trục được nhân rồi cộng.
# NumPy định nghĩa @ cho nhân ma trận/tích vô hướng tùy kích thước.
import numpy as np

# Vector a có hai tọa độ theo thứ tự x,y.
a = np.array([1, 2])
# Vector b phải có cùng số thành phần với a để tính tích vô hướng.
b = np.array([3, 4])
# Với hai vector 1 chiều, @ trả scalar 1×3 + 2×4 = 11; khác * tạo vector nhân từng vị trí.
print(a @ b)
```

**Kết quả khi chạy:**

```text
11
```

Tích vô hướng trả một scalar bằng 11.

## 5. Năm tình huống véc-tơ — từ khoảng cách đến kiểm tra sai số đa trục

### Tình huống 1 — Cấp 1: Cộng 10 bước di chuyển và đo độ lệch cuối

**Từ vựng trong mục:** **Vector** — véc-tơ có thứ tự; **Scalar** — số đơn lẻ; **Norm** — độ dài.

**Tình huống thực tế:** Một robot di chuyển trên sàn theo **10 lệnh**; mỗi lệnh chứa hai số: đi theo chiều ngang **x** và chiều dọc **y**, đều tính bằng **mét**. Số âm nghĩa là đi ngược hướng dương của trục, ví dụ `(-2, 0)` là lùi 2 m trên trục x. Sau cả 10 lệnh, người điều khiển muốn biết robot đang lệch điểm xuất phát bao nhiêu mét theo từng trục và **khoảng cách đường thẳng từ điểm xuất phát**, không phải tổng quãng đường đã di chuyển.

**Vì sao chọn cách này?** **Véc-tơ** là cặp số ghi **mức dịch chuyển và hướng** theo từng trục, nên số âm là hợp lệ. `steps.sum(axis=0)` cộng **riêng các bước x** và **riêng các bước y** để ra véc-tơ vị trí cuối so với gốc: những bước đi ngược nhau có thể triệt tiêu. `np.linalg.norm(ending)` tính độ dài **đường thẳng từ gốc đến vị trí cuối** dựa trên cả hai thành phần; nó khác việc cộng độ dài từng bước. Robot có thể đi một vòng rồi về gần gốc: đường đã đi dài nhưng khoảng cách cuối tới gốc nhỏ.

**Quy trình:**
1. Tạo 10 véc-tơ 2 chiều với đơn vị mét.
2. Cộng theo trục x/y bằng `sum(axis=0)`.
3. Tính norm của véc-tơ tổng và in đơn vị.

**No Note — Không chú thích**

```python
import numpy as np
steps = np.array([[3,4],[0,2],[-2,0],[1,-1],[2,2],[-3,1],[0,-4],[4,0],[-1,3],[2,-2]], dtype=float)
ending = steps.sum(axis=0)
if steps.shape != (10, 2):
    raise ValueError("Cần đủ 10 bước chuyển động hai chiều.")
print("Bước:", len(steps))
print("Lệch x (m):", int(ending[0]))
print("Lệch y (m):", int(ending[1]))
print(f"Cách gốc (m): {np.linalg.norm(ending):.2f}")
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Cộng 10 bước chuyển động hai chiều thành độ lệch x/y và khoảng cách tới gốc.
# Dữ liệu: 10 hàng bước [dx,dy], đơn vị mét; bước âm là đi ngược chiều trục.
# NumPy cho phép cộng vector từng cột theo nhiều hàng.
import numpy as np
# 10 cặp dx/dy, dtype=float tạo bảng hai cột số thực.
steps = np.array([[3,4],[0,2],[-2,0],[1,-1],[2,2],[-3,1],[0,-4],[4,0],[-1,3],[2,-2]], dtype=float)
# sum(axis=0) cộng THEO HÀNG, trả hai tổng cột dx/dy, là vị trí cuối so với gốc.
ending = steps.sum(axis=0)
# shape (10,2) kiểm 10 bước và 2 tọa độ mỗi bước.
if steps.shape != (10, 2):
    # raise ValueError() chặn kết luận nếu số bản ghi hoặc shape không đạt yêu cầu.
    raise ValueError("Cần đủ 10 bước chuyển động hai chiều.")
# len() đếm số hàng bước, ở đây 10, không phải tổng ô.
print("Bước:", len(steps))
# [0] là độ lệch x, [1] độ lệch y; int() đưa giá trị NumPy về int để in.
print("Lệch x (m):", int(ending[0]))
print("Lệch y (m):", int(ending[1]))
# norm() lấy khoảng cách thẳng từ gốc đến tọa độ cuối; :.2f chỉ định in hai chữ số sau dấu thập phân, đơn vị mét.
print(f"Cách gốc (m): {np.linalg.norm(ending):.2f}")
```

**Kết quả khi chạy:**

```text
Bước: 10
Lệch x (m): 6
Lệch y (m): 5
Cách gốc (m): 7.81
```

Véc-tơ tổng có thể nhỏ hơn tổng quãng đường đi, vì các bước di chuyển ngược chiều triệt tiêu nhau.

### Tình huống 2 — Cấp 2: Chuẩn hóa 12 hướng robot nhưng không chia cho 0

**Từ vựng trong mục:** **Unit vector** — véc-tơ đơn vị; **Zero vector** — véc-tơ không; **Normalization** — chuẩn hóa.

**Tình huống thực tế:** Bộ điều khiển nhận **12 véc-tơ chỉ hướng**, mỗi véc-tơ là hai số `(x, y)` chưa cần gắn đơn vị. Mười véc-tơ có ít nhất một thành phần khác 0, nhưng có hai cặp `(0, 0)` không chỉ ra được hướng nào. Nhóm kỹ thuật muốn đổi **mười hướng hợp lệ** thành véc-tơ dài 1 để dễ so sánh và ghi riêng hai yêu cầu chưa xác định, không tự bịa một hướng cho chúng.

**Vì sao chọn cách này?** **Chuẩn hóa véc-tơ** ở đây nghĩa là giữ nguyên **hướng chỉ**, nhưng đưa độ dài mỗi véc-tơ hợp lệ về **1**; nhờ vậy hai lệnh cùng hướng có thể được so mà không bị ảnh hưởng bởi số lớn nhỏ ban đầu. `np.linalg.norm(..., axis=1)` đo độ dài từng hàng; điều kiện `lengths > 0` chỉ chọn các hàng có hướng xác định. NumPy chỉ chia các hàng ấy cho độ dài tương ứng; các hàng `(0,0)` không được chia vì sẽ chia cho 0. Chương trình đếm riêng hai hàng này và để chúng ở dạng 0 trong mảng kết quả, nhưng **không coi đó là hướng chuẩn hợp lệ**.

**Quy trình:**
1. Tạo mảng `(12,2)` và tính norm riêng từng hàng.
2. Chỉ chia các hàng có norm dương; giữ véc-tơ không cho kiểm tra.
3. Đếm số hướng hợp lệ, in véc-tơ đầu sau chuẩn hóa.

**No Note — Không chú thích**

```python
import numpy as np
vectors = np.array([[3,4],[0,0],[5,0],[-3,4],[0,5],[6,8],[1,1],[-4,0],[2,-2],[0,-2],[4,3],[0,0]], dtype=float)
lengths = np.linalg.norm(vectors, axis=1)
valid = lengths > 0
normalized = np.zeros_like(vectors)
normalized[valid] = vectors[valid] / lengths[valid, None]
if len(vectors) != 12:
    raise ValueError("Cần đủ 12 véc-tơ cần chuẩn hóa.")
print("Yêu cầu:", len(vectors))
print("Hướng hợp lệ:", int(valid.sum()))
print("Hướng chưa xác định:", int((~valid).sum()))
values = []
for x in normalized[0]:
    values.append(f"{x:.2f}")
print("Véc-tơ đầu:", ", ".join(values))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Chuẩn hóa 12 vector về hướng dài một đơn vị, tránh chia cho 0 ở vector rỗng.
# Dữ liệu: 12 hàng vector hai trục, gồm hai vector [0,0] không có hướng xác định.
# NumPy áp dụng phép toán vector hóa trên toàn bộ mảng 12×2.
import numpy as np
# dtype=float để phép chia ra thành phần hướng thực; hai cột x/y.
vectors = np.array([[3,4],[0,0],[5,0],[-3,4],[0,5],[6,8],[1,1],[-4,0],[2,-2],[0,-2],[4,3],[0,0]], dtype=float)
# norm(...,axis=1) tính độ dài riêng cho TỪNG HÀNG vector, trả 12 độ dài; axis=0 sẽ gom theo cột.
lengths = np.linalg.norm(vectors, axis=1)
# Tạo mặt nạ True tại những vector có độ dài khác 0; vector [0,0] không chia được.
valid = lengths > 0
# zeros_like() tạo mảng 12×2 toàn 0 cùng shape/dtype làm vùng chứa kết quả.
normalized = np.zeros_like(vectors)
# vectors[valid] chọn những hàng có hướng; lengths[valid,None] đổi vector độ dài thành cột (n,1) để broadcast chia cả x,y theo độ dài từng hàng.
# Chỉ cập nhật hàng hợp lệ; hàng vector 0 vẫn giữ [0,0] làm giá trị thay thế không có hướng.
normalized[valid] = vectors[valid] / lengths[valid, None]
if len(vectors) != 12:
    # raise ValueError() chặn kết luận nếu số bản ghi hoặc shape không đạt yêu cầu.
    raise ValueError("Cần đủ 12 véc-tơ cần chuẩn hóa.")
print("Yêu cầu:", len(vectors))
print("Hướng hợp lệ:", int(valid.sum()))
# ~ đảo mặt nạ Boolean, .sum() đếm hàng có độ dài 0; valid.sum() đếm hàng có hướng.
print("Hướng chưa xác định:", int((~valid).sum()))
values = []
# [0] lấy hai thành phần hướng đã chuẩn hóa của vector đầu tiên.
for x in normalized[0]:
    # f-string :.2f hiển thị mỗi thành phần với hai chữ số thập phân.
    values.append(f"{x:.2f}")
# join() nối hai tọa độ dạng chuỗi bằng ', ' thành một dòng báo cáo.
print("Véc-tơ đầu:", ", ".join(values))
```

**Kết quả khi chạy:**

```text
Yêu cầu: 12
Hướng hợp lệ: 10
Hướng chưa xác định: 2
Véc-tơ đầu: 0.60, 0.80
```

Véc-tơ không vẫn được bảo toàn trên bản dữ liệu xử lý nhưng **không** được coi là hướng di chuyển có độ dài 1.

### Tình huống 3 — Cấp 3: Dot product cho 15 điểm tổng kết theo ba tiêu chí

**Từ vựng trong mục:** **Dot product** — tích vô hướng; **Weight** — trọng số; **Threshold** — ngưỡng.

**Tình huống thực tế:** Giáo viên lưu bảng **15 học viên H01–H15**, mỗi học viên có ba điểm **lý thuyết, thực hành, dự án** trên thang 10. Quy tắc chấm minh họa cho các phần này lần lượt **20%, 30%, 50%** và yêu cầu điểm cuối đạt **ít nhất 7,5**. Giáo vụ cần tính một điểm tổng kết cho mỗi người, xem điểm của H01 và H15, rồi đếm bao nhiêu người đạt, không ghép điểm giữa các học viên.

**Vì sao chọn cách này?** **Tích vô hướng** là cách kết hợp hai dãy số cùng thứ tự bằng việc nhân các phần tương ứng rồi cộng. Mỗi hàng là ba điểm **của đúng một học viên**, còn dãy trọng số có thứ tự **lý thuyết, thực hành, dự án**. `scores @ weights` áp một quy tắc tính điểm như nhau cho cả 15 hàng, tạo **15 điểm cuối**; dự án góp 50% nên có ảnh hưởng lớn nhất. Nếu đổi thứ tự các trọng số mà không đổi thứ tự cột điểm, kết quả sẽ sai. Điều kiện `>= 7.5` tính cả học viên đạt **đúng 7,5**, không chỉ người cao hơn ngưỡng.

**Quy trình:**
1. Tạo ma trận 15 × 3 và véc-tơ ba trọng số.
2. Nhân `scores @ weights` để có 15 kết quả.
3. Đếm người đạt ngưỡng 7,5; in điểm đầu và cuối để đối chiếu.

**No Note — Không chú thích**

```python
import numpy as np
scores = np.array([[5,6,7],[6,8,10],[7,10,9],[8,7,8],[9,9,7],[5,6,10],[6,8,9],[7,10,8],[8,7,7],[9,9,10],[5,6,9],[6,8,8],[7,10,7],[8,7,10],[9,9,9]], dtype=float)
weights = np.array([0.2, 0.3, 0.5])
final_scores = scores @ weights
if scores.shape != (15, 3) or final_scores.shape != (15,):
    raise ValueError("Cần đủ 15 học viên với 3 môn và 15 điểm cuối.")
print("Học viên:", len(final_scores))
print(f"H01: {final_scores[0]:.2f}")
print(f"H15: {final_scores[-1]:.2f}")
print("Đạt 7.5:", int((final_scores >= 7.5).sum()))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tính điểm tổng hợp có trọng số cho 15 học viên bằng tích vector theo mỗi hàng.
# Dữ liệu: 15 hàng học viên × 3 môn; trọng số giả định 20%, 30%, 50% tương ứng theo ba cột, tổng 100%.
# NumPy thực hiện phép nhân bảng điểm với vector trọng số qua @.
import numpy as np
# dtype=float lưu bảng 15×3, một người mỗi hàng, một môn mỗi cột.
scores = np.array([[5,6,7],[6,8,10],[7,10,9],[8,7,8],[9,9,7],[5,6,10],[6,8,9],[7,10,8],[8,7,7],[9,9,10],[5,6,9],[6,8,8],[7,10,7],[8,7,10],[9,9,9]], dtype=float)
# Vector [0.2,0.3,0.5] là mức đóng góp TỪNG MÔN; không phải tần suất học viên.
weights = np.array([0.2, 0.3, 0.5])
# @ nhân từng hàng ba điểm với ba trọng số rồi cộng, trả 15 điểm tổng hợp một chiều.
final_scores = scores @ weights
# shape (15,3) và final_scores (15,) xác nhận một kết quả cho mỗi học viên.
if scores.shape != (15, 3) or final_scores.shape != (15,):
    # raise ValueError() chặn kết luận nếu số bản ghi hoặc shape không đạt yêu cầu.
    raise ValueError("Cần đủ 15 học viên với 3 môn và 15 điểm cuối.")
print("Học viên:", len(final_scores))
# [0] là H01, [-1] H15; :.2f hiển thị điểm hai chữ số lẻ.
print(f"H01: {final_scores[0]:.2f}")
# [-1] lấy điểm học viên cuối mà không phải ghi chỉ số 14.
print(f"H15: {final_scores[-1]:.2f}")
# >= 7.5 tạo mask Boolean theo từng người; sum() đếm số True đạt ngưỡng.
print("Đạt 7.5:", int((final_scores >= 7.5).sum()))
```

**Kết quả khi chạy:**

```text
Học viên: 15
H01: 6.30
H15: 9.00
Đạt 7.5: 12
```

Trọng số phản ánh quy định giả lập của lớp; dot product tạo một số theo mỗi học viên, không phải một bảng 15 × 3 sau khi tính.

### Tình huống 4 — Cấp 4: Phân 18 hướng vuông góc và ngược chiều với hướng chuẩn

**Từ vựng trong mục:** **Orthogonality** — vuông góc; **Dot product** — tích vô hướng; **Projection** — chiếu theo trục.

**Tình huống thực tế:** Robot nhận **18 lệnh di chuyển hai chiều** `(x, y)`; mỗi số cho biết mức điều khiển dọc một trục. Kỹ thuật viên lấy hướng chuẩn **sang phải** là véc-tơ `(1, 0)` và muốn chia các lệnh thành ba nhóm: có thành phần **cùng chiều** với hướng chuẩn, **ngược chiều**, hoặc **vuông góc**. Một lệnh vừa đi sang phải vừa đi lên vẫn có phần cùng chiều; không nên chỉ nhìn toàn bộ mũi tên mà kết luận theo cảm giác.

**Vì sao chọn cách này?** **Tích vô hướng** còn cho biết một hướng điều khiển có phần **cùng hay ngược** với hướng chuẩn. Với hướng chuẩn `(1,0)`, kết quả dương khi lệnh có phần đi sang phải; âm khi có phần đi sang trái; bằng 0 khi lệnh **vuông góc** với hướng sang phải, ví dụ chỉ đi lên hoặc xuống. `directions @ reference` tính cùng cách cho đủ 18 lệnh, sau đó chương trình đếm ba nhóm theo dấu kết quả. Vì dữ liệu mẫu là các số nguyên nhỏ và hướng chuẩn đơn giản, so đúng bằng 0 phù hợp ở đây; với dữ liệu đo số thực có sai số, có thể cần ngưỡng gần 0.

**Quy trình:**
1. Tạo mảng 18 hàng × 2 cột và véc-tơ chuẩn.
2. Tính 18 tích vô hướng `directions @ reference`.
3. Đếm trường hợp âm, 0 và dương; xác minh tổng bằng 18.

**No Note — Không chú thích**

```python
import numpy as np
directions = np.array([[-1,0],[0,1],[1,0],[0,-1],[1,1],[-1,1],[-1,0],[0,1],[1,0],[0,-1],[1,1],[-1,1],[-1,0],[0,1],[1,0],[0,-1],[1,1],[-1,1]], dtype=float)
reference = np.array([1.0, 0.0])
projections = directions @ reference
if directions.shape != (18, 2):
    raise ValueError("Cần đủ 18 lệnh chuyển động hai chiều.")
print("Lệnh:", len(directions))
print("Ngược chiều:", int((projections < 0).sum()))
print("Vuông góc:", int((projections == 0).sum()))
print("Cùng chiều:", int((projections > 0).sum()))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Dùng tích vô hướng để phân loại 18 hướng so với trục +x: ngược, vuông góc, cùng hướng.
# Dữ liệu: 18 lệnh (dx,dy), trục tham chiếu [1,0] hướng +x; các giá trị chưa nhất thiết là vector đơn vị.
# NumPy hỗ trợ tích vô hướng theo từng hàng của ma trận hướng.
import numpy as np
# 18 hàng là các hướng di chuyển 2 chiều x,y, dtype=float.
directions = np.array([[-1,0],[0,1],[1,0],[0,-1],[1,1],[-1,1],[-1,0],[0,1],[1,0],[0,-1],[1,1],[-1,1],[-1,0],[0,1],[1,0],[0,-1],[1,1],[-1,1]], dtype=float)
# Vector tham chiếu nằm trên trục x dương, chiều dài 1; cùng thứ tự thành phần x,y.
reference = np.array([1.0, 0.0])
# @ lấy tích vô hướng với tham chiếu cho từng hàng, trả 18 scalar; vì reference=[1,0], chính là thành phần x của hướng.
projections = directions @ reference
# shape (18,2) kiểm đủ lệnh và hai tọa độ.
if directions.shape != (18, 2):
    # raise ValueError() chặn kết luận nếu số bản ghi hoặc shape không đạt yêu cầu.
    raise ValueError("Cần đủ 18 lệnh chuyển động hai chiều.")
print("Lệnh:", len(directions))
# Tích âm nghĩa ngược chiều x dương; sum() đếm số mask True.
print("Ngược chiều:", int((projections < 0).sum()))
# Tích bằng 0 nghĩa vuông góc với trục x (đối với vector khác 0), đếm lượt bằng 0.
print("Vuông góc:", int((projections == 0).sum()))
# Tích dương nghĩa có thành phần cùng chiều x dương, không nhất thiết vector song song trục.
print("Cùng chiều:", int((projections > 0).sum()))
```

**Kết quả khi chạy:**

```text
Lệnh: 18
Ngược chiều: 6
Vuông góc: 6
Cùng chiều: 6
```

Phân loại bằng tích vô hướng là về **thành phần hướng so với véc-tơ chuẩn**, không suy ra robot đã thực sự di chuyển bao xa.

### Tình huống 5 — Cấp 5: Xếp hạng sai số 20 cảm biến ba trục bằng độ dài véc-tơ

**Từ vựng trong mục:** **Residual vector** — véc-tơ sai lệch; **Norm** — độ lớn sai số; **Ranking** — xếp hạng.

**Tình huống thực tế:** Nhà máy có **20 lượt đo vị trí cảm biến ba chiều**, mỗi lượt ghi vị trí quan sát và vị trí kỳ vọng theo ba trục **X, Y, Z**, tất cả tính bằng **mm**. Có lượt lệch nhiều trên một trục, có lượt lệch nhỏ theo cả ba trục. Nhân viên muốn biết **độ lớn sai lệch** của mỗi lượt, đếm những lượt lệch **lớn hơn 2 mm**, xác định lượt sai nhất và mức lệch trung bình; đây chỉ là kiểm tra số liệu hình học, chưa kết luận thiết bị bị hỏng.

**Vì sao chọn cách này?** **Sai lệch véc-tơ** là chênh lệch giữa vị trí cảm biến quan sát và vị trí dự kiến theo cả ba trục. `observed - expected` cho một bộ ba sai lệch của từng lượt; `np.linalg.norm(..., axis=1)` chuyển mỗi bộ ba thành **một độ lớn luôn không âm**, đơn vị vẫn là mm. Điều này tránh việc lệch +2 mm trên trục X và -2 mm trên trục Y cộng lại thành 0 rồi bị hiểu nhầm là đo đúng. Sau đó so độ lớn với **ngưỡng 2 mm**, dùng `argmax()` tìm **vị trí lượt có sai số lớn nhất**, và `mean()` tính mức sai lệch trung bình. Ngưỡng 2 mm là quy tắc bài tập, chưa phải chuẩn chất lượng công nghiệp.

**Quy trình:**
1. Lưu 20 cặp véc-tơ 3D theo đúng thứ tự trục.
2. Tính sai lệch từng hàng, sau đó norm của 20 véc-tơ.
3. Đếm vượt ngưỡng 2 mm, tìm mã lượt lớn nhất và báo trung bình.

**No Note — Không chú thích**

```python
import numpy as np
observed = np.array([[10,20,30],[11,21,31],[12,22,32],[13,23,30],[14,20,31],[10,21,32],[11,22,30],[12,23,31],[13,20,32],[14,21,30],[10,22,31],[11,23,32],[12,20,30],[13,21,31],[14,22,32],[10,23,30],[11,20,31],[12,21,32],[13,22,30],[14,23,31]], dtype=float)
expected = np.array([[11,19,33],[12,20,31],[13,21,32],[14,22,30],[15,19,31],[11,20,32],[12,21,30],[13,22,34],[14,19,32],[15,20,30],[11,21,31],[12,22,32],[13,19,30],[14,20,31],[15,21,35],[11,22,30],[12,19,31],[13,20,32],[14,21,30],[15,22,31]], dtype=float)
residual = observed - expected
errors = np.linalg.norm(residual, axis=1)
worst = int(errors.argmax())
if observed.shape != (20, 3) or expected.shape != (20, 3):
    raise ValueError("Cần 20 lượt đo, mỗi lượt có ba tọa độ nguồn và kỳ vọng.")
print("Lượt đo:", len(errors))
print("Vượt 2 mm:", int((errors > 2).sum()))
print("Lượt sai nhất:", f"M{worst+1:02d}")
print(f"Sai số lớn nhất (mm): {errors[worst]:.2f}")
print(f"Sai số TB (mm): {errors.mean():.2f}")
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tính vector sai lệch 3D và độ dài sai số của 20 lượt đo, tìm lượt sai nhất.
# Dữ liệu: 20 hàng quan sát và 20 hàng kỳ vọng theo 3 trục tọa độ cùng thứ tự, đơn vị mm.
# NumPy cho phép trừ bảng theo từng ô và tính độ dài sai lệch vector.
import numpy as np
# 20 hàng đo thực tế, mỗi hàng [x,y,z] mm, dtype=float.
observed = np.array([[10,20,30],[11,21,31],[12,22,32],[13,23,30],[14,20,31],[10,21,32],[11,22,30],[12,23,31],[13,20,32],[14,21,30],[10,22,31],[11,23,32],[12,20,30],[13,21,31],[14,22,32],[10,23,30],[11,20,31],[12,21,32],[13,22,30],[14,23,31]], dtype=float)
# 20 hàng tọa độ kỳ vọng cùng thứ tự với observed, cũng đơn vị mm.
expected = np.array([[11,19,33],[12,20,31],[13,21,32],[14,22,30],[15,19,31],[11,20,32],[12,21,30],[13,22,34],[14,19,32],[15,20,30],[11,21,31],[12,22,32],[13,19,30],[14,20,31],[15,21,35],[11,22,30],[12,19,31],[13,20,32],[14,21,30],[15,22,31]], dtype=float)
# Trừ THEO TỪNG Ô cùng hàng/cột để lấy vector sai số tọa độ của mỗi lượt.
residual = observed - expected
# norm(...,axis=1) tính độ dài Euclid vector sai số ba trục cho từng hàng, trả 20 khoảng cách mm.
errors = np.linalg.norm(residual, axis=1)
# argmax() trả CHỈ SỐ 0-based có sai số lớn nhất, không trả trị số sai số; int() chuyển thành int Python.
worst = int(errors.argmax())
# shape (20,3) của cả hai bảng bảo đảm so đúng số lượt và số trục.
if observed.shape != (20, 3) or expected.shape != (20, 3):
    # raise ValueError() chặn kết luận nếu số bản ghi hoặc shape không đạt yêu cầu.
    raise ValueError("Cần 20 lượt đo, mỗi lượt có ba tọa độ nguồn và kỳ vọng.")
print("Lượt đo:", len(errors))
# So từng sai số với ngưỡng 2 mm, sum() trên Boolean đếm lượt vượt ngưỡng.
print("Vượt 2 mm:", int((errors > 2).sum()))
# Chỉ số argmax bắt đầu 0 nên +1 lấy số lượt, :02d tạo mã M01..M20.
print("Lượt sai nhất:", f"M{worst+1:02d}")
# Lấy sai số đúng lượt lớn nhất, :.2f hiển thị mm hai chữ số lẻ.
print(f"Sai số lớn nhất (mm): {errors[worst]:.2f}")
# mean() lấy độ dài sai số trung bình của 20 lượt, không phải trung bình từng tọa độ.
print(f"Sai số TB (mm): {errors.mean():.2f}")
```

**Kết quả khi chạy:**

```text
Lượt đo: 20
Vượt 2 mm: 3
Lượt sai nhất: M01
Sai số lớn nhất (mm): 3.32
Sai số TB (mm): 1.70
```

Mỗi hàng là một lượt đo 3 trục có cùng đơn vị mm. Mức 2 mm là **ngưỡng ví dụ**, phải do chuyên gia thiết bị quyết định khi ứng dụng thật.

## 6. Sai lầm thường gặp

- Scalar là số đơn; vector là dãy các thành phần có thứ tự.
- Khi tính khoảng cách, các thành phần phải cùng hệ trục và đơn vị phù hợp.
- Không chuẩn hóa vector không vì norm bằng 0.
- Dấu `*` NumPy nhân từng phần tử; `@` với hai vector 1-D tính tích vô hướng.
- Khi kiểm tra vuông góc với dữ liệu float, nên so với một ngưỡng sai số nhỏ.

## 7. Trắc nghiệm

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a scalar? | Scalar là gì?**

A. One numeric value | Một giá trị số

B. Sum of pairwise component products | Tổng tích các cặp thành phần tương ứng

C. An ordered list of components | Dãy thành phần có thứ tự

D. Square root of the sum of squared components | Căn của tổng bình phương các thành phần

**Đáp án: A**

**Giải thích:** Scalar không gồm nhiều thành phần tọa độ.


**Q2. What is a vector? | Vector là gì?**

A. Square root of the sum of squared components | Căn của tổng bình phương các thành phần

B. One numeric value | Một giá trị số

C. Sum of pairwise component products | Tổng tích các cặp thành phần tương ứng

D. An ordered list of components | Dãy thành phần có thứ tự

**Đáp án: D**

**Giải thích:** Vị trí từng thành phần biểu thị tọa độ hoặc đặc trưng.


**Q3. What is Euclidean norm? | Norm Euclid là gì?**

A. An ordered list of components | Dãy thành phần có thứ tự

B. Sum of pairwise component products | Tổng tích các cặp thành phần tương ứng

C. Square root of the sum of squared components | Căn của tổng bình phương các thành phần

D. One numeric value | Một giá trị số

**Đáp án: C**

**Giải thích:** Norm L2 đo độ dài theo Euclid.


**Q4. What is the dot product? | Tích vô hướng là gì?**

A. Sum of pairwise component products | Tổng tích các cặp thành phần tương ứng

B. An ordered list of components | Dãy thành phần có thứ tự

C. One numeric value | Một giá trị số

D. Square root of the sum of squared components | Căn của tổng bình phương các thành phần

**Đáp án: A**

**Giải thích:** Tích vô hướng cho một số từ hai vector cùng số thành phần.


**Q5. Given u = [1, 4] and v = [3, 2], what is u · v? | Cho u = [1, 4] và v = [3, 2], tích vô hướng u · v bằng bao nhiêu?**

A. 9 | 9

B. 11 | 11

C. 14 | 14

D. 8 | 8

**Đáp án: B**

**Giải thích:** Tính các tích cùng vị trí rồi cộng: 1 × 3 + 4 × 2 = 11. Không cộng riêng từng vector trước khi nhân.


**Q6. What is the length of vector (6, 8)? | Độ dài vector (6, 8) là bao nhiêu?**

A. 10 | 10

B. 8 | 8

C. 14 | 14

D. 100 | 100

**Đáp án: A**

**Giải thích:** Độ dài Euclid là căn bậc hai của 6² + 8² = 100, nên bằng 10.


**Q7. If u = (2, −1), what is −2u? | Nếu u = (2, −1), vector −2u bằng bao nhiêu?**

A. (−4, 2) | (−4, 2)

B. (−2, 1) | (−2, 1)

C. (4, −2) | (4, −2)

D. (−4, −2) | (−4, −2)

**Đáp án: A**

**Giải thích:** Nhân từng tọa độ của u với −2: −2 × 2 = −4 và −2 × (−1) = 2.


**Q8. Given a = (2, 1) and b = (−1, 2), what is their dot product? | Cho a = (2, 1) và b = (−1, 2), tích vô hướng bằng bao nhiêu?**

A. 1 | 1

B. 0 | 0

C. 4 | 4

D. 3 | 3

**Đáp án: B**

**Giải thích:** 2 × (−1) + 1 × 2 = 0. Hai vector khác không có tích vô hướng bằng 0 thì vuông góc.


**Q9. What is the norm of vector (3,4)? | Norm của vector (3,4) bằng bao nhiêu?**

A. 0 | 0

B. 11 | 11

C. 5 | 5

D. (0.6,0.8) | (0.6,0.8)

**Đáp án: C**

**Giải thích:** Độ dài Pythagoras là căn của 9+16.


**Q10. What is the unit vector in the direction (3,4)? | Vector đơn vị theo hướng (3,4) là gì?**

A. 5 | 5

B. (0.6,0.8) | (0.6,0.8)

C. 11 | 11

D. 0 | 0

**Đáp án: B**

**Giải thích:** Chia mỗi thành phần cho độ dài năm.


**Q11. What is the dot product (1,2)·(3,4)? | Tích vô hướng (1,2)·(3,4) bằng bao nhiêu?**

A. 5 | 5

B. 11 | 11

C. (0.6,0.8) | (0.6,0.8)

D. 0 | 0

**Đáp án: B**

**Giải thích:** Tính 1×3 + 2×4.


**Q12. What is the dot product of (1,0) and (0,1)? | Tích vô hướng của (1,0) và (0,1) là bao nhiêu?**

A. (0.6,0.8) | (0.6,0.8)

B. 0 | 0

C. 5 | 5

D. 11 | 11

**Đáp án: B**

**Giải thích:** Cả hai tích thành phần đều bằng không.


**Q13. What is the dot product of two nonzero perpendicular vectors? | Tích vô hướng của hai vector khác không vuông góc là gì?**

A. That its norm is nonzero | Norm khác không

B. Zero | Bằng không

C. They must have equal lengths | Chúng phải có cùng số phần tử

D. The result can be physically misleading | Kết quả có thể sai ý nghĩa vật lý

**Đáp án: B**

**Giải thích:** Hai hướng trực giao có tích vô hướng bằng không.


**Q14. What must be checked before normalizing a vector? | Cần kiểm tra gì trước khi chuẩn hóa vector?**

A. They must have equal lengths | Chúng phải có cùng số phần tử

B. Zero | Bằng không

C. The result can be physically misleading | Kết quả có thể sai ý nghĩa vật lý

D. That its norm is nonzero | Norm khác không

**Đáp án: D**

**Giải thích:** Chia cho norm bằng không không xác định.


**Q15. What happens if coordinate units are mixed in a distance calculation? | Nếu đơn vị tọa độ không thống nhất khi tính khoảng cách thì sao?**

A. They must have equal lengths | Chúng phải có cùng số phần tử

B. That its norm is nonzero | Norm khác không

C. The result can be physically misleading | Kết quả có thể sai ý nghĩa vật lý

D. Zero | Bằng không

**Đáp án: C**

**Giải thích:** Tính norm có ý nghĩa khi đơn vị phù hợp.


**Q16. What must be true to compute a 1-D dot product? | Muốn tính tích vô hướng của hai vector 1-D cần điều kiện gì?**

A. That its norm is nonzero | Norm khác không

B. They must have equal lengths | Chúng phải có cùng số phần tử

C. Zero | Bằng không

D. The result can be physically misleading | Kết quả có thể sai ý nghĩa vật lý

**Đáp án: B**

**Giải thích:** Từng thành phần được ghép theo vị trí tương ứng.


**Q17. What does multiplying a vector by a scalar do? | Nhân vector với scalar làm gì?**

A. To multiply each weight by its intended feature | Để trọng số nhân đúng đặc trưng tương ứng

B. Subtract corresponding components | Trừ các thành phần cùng vị trí

C. Scales every component | Nhân từng thành phần với scalar

D. Euclidean distance between a and b | Khoảng cách Euclid giữa a và b

**Đáp án: C**

**Giải thích:** Nhân scalar làm đổi độ lớn từng thành phần.


**Q18. How is vector subtraction performed? | Phép trừ vector được thực hiện thế nào?**

A. Scales every component | Nhân từng thành phần với scalar

B. Euclidean distance between a and b | Khoảng cách Euclid giữa a và b

C. To multiply each weight by its intended feature | Để trọng số nhân đúng đặc trưng tương ứng

D. Subtract corresponding components | Trừ các thành phần cùng vị trí

**Đáp án: D**

**Giải thích:** Phép trừ vector diễn ra theo từng thành phần.


**Q19. What does `np.linalg.norm(a-b)` measure? | `np.linalg.norm(a-b)` đo điều gì?**

A. To multiply each weight by its intended feature | Để trọng số nhân đúng đặc trưng tương ứng

B. Subtract corresponding components | Trừ các thành phần cùng vị trí

C. Scales every component | Nhân từng thành phần với scalar

D. Euclidean distance between a and b | Khoảng cách Euclid giữa a và b

**Đáp án: D**

**Giải thích:** Norm của độ dịch chuyển cho khoảng cách.


**Q20. Why are feature weights paired with values in the same order? | Vì sao trọng số cần cùng thứ tự với các giá trị?**

A. Euclidean distance between a and b | Khoảng cách Euclid giữa a và b

B. To multiply each weight by its intended feature | Để trọng số nhân đúng đặc trưng tương ứng

C. Scales every component | Nhân từng thành phần với scalar

D. Subtract corresponding components | Trừ các thành phần cùng vị trí

**Đáp án: B**

**Giải thích:** Sai thứ tự tạo ra tích vô hướng khác.

## 8. Nối sang bài kế tiếp

`NumPy → Scalar/Vector → Matrix → PCA`.
