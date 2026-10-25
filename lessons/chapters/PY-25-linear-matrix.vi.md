# PY-25 — Ma trận, chuyển vị, nhân ma trận và định thức


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Matrix** — ma trận; **Transpose** — chuyển vị.

`Vector → Matrix → Hệ tuyến tính → Eigenvalue/PCA`

**Học xong dùng để làm gì?** Tổ chức bảng đặc trưng thành ma trận và nhân ma trận để biến đổi dữ liệu nhiều chiều.

**Kết nối kiến thức tiếp theo:** PY-26 giải các ràng buộc dưới dạng hệ tuyến tính và kiểm tra rank.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích |
|---|---|---|
| Matrix | ma trận | Bảng hai chiều chứa giá trị theo hàng và cột |
| Transpose | chuyển vị | Đổi vai trò hàng và cột của ma trận |
| Determinant | định thức | Số của ma trận vuông dùng xét tính khả nghịch |
| Inverse | ma trận nghịch đảo | Ma trận B làm AB=BA=I khi tồn tại |

## 3. NumPy và các hàm liên quan

**Từ vựng trong mục:** **Function** — hàm; **Shape** — kích thước mảng.

| Hàm / tham số | Dùng làm gì |
|---|---|
| `np.eye(n)` | Ma trận đơn vị vuông, nhân vào không đổi vector |
| `A.T / np.transpose(A)` | Chuyển vị ma trận |
| `A @ B` | Nhân ma trận khi số cột A bằng số hàng B |
| `np.linalg.det()/inv()` | Định thức và nghịch đảo khi khả nghịch; giải hệ nên ưu tiên solve |

## 4. Khái niệm liên quan

**Ma trận (matrix)** là bảng có hàng và cột được xác định rõ theo dữ liệu. Từ bảng điểm hai học viên và ba môn, bài học giải thích chuyển vị để đổi cách xem, nhân ma trận để tổng hợp trọng số, rồi định thức và nghịch đảo khi làm việc với ma trận vuông.

### 4.1. Matrix — Bảng số có hàng và cột

Ma trận là bảng số hai chiều. Với điểm học viên An `[8,7,9]` và Bình `[6,5,8]` ở ba môn Toán, Văn, Python, bảng có **hai hàng học viên** và **ba cột môn**. Giá trị `[1,0]` nghĩa là điểm Toán của Bình bằng 6. `shape` cho kích thước, theo thứ tự (số hàng, số cột).

```python
# Mục đích: Bảng số có hàng và cột.
import numpy as np

scores = np.array([[8, 7, 9], [6, 5, 8]])
print(scores.shape)
```

**Kết quả khi chạy:**

```text
(2, 3)
```

Bảng có hai học viên và ba môn học.

### 4.2. Transpose — Hoán đổi hai trục

Chuyển vị `A.T` biến hàng thành cột và cột thành hàng. Với bảng điểm hai học viên × ba môn, ma trận sau chuyển vị có ba hàng môn và hai cột học viên. Ví dụ hàng đầu là điểm Toán của An và Bình, `[8,6]`; không có điểm nào bị thay đổi.

```python
# Mục đích: Hoán đổi hai trục.
import numpy as np

scores = np.array([[8, 7, 9], [6, 5, 8]])
print(scores.T)
```

**Kết quả khi chạy:**

```text
[[8 6]
 [7 5]
 [9 8]]
```

Kết quả gồm ba hàng môn × hai cột học viên.

### 4.3. Matrix multiplication — Nhân ma trận

Nhân `X @ W` yêu cầu số cột của X bằng số hàng của W. Bảng điểm X có shape `(2,3)`, trọng số ba môn W có shape `(3,1)`, tích có shape `(2,1)` cho điểm tổng của từng học viên. Dòng An là `8×0.2 + 7×0.3 + 9×0.5 = 8.2`. `@` khác phép nhân từng phần tử `*`.

```python
# Mục đích: Nhân ma trận.
import numpy as np

X = np.array([[8, 7, 9], [6, 5, 8]])
W = np.array([[0.2], [0.3], [0.5]])
print(X @ W)
```

**Kết quả khi chạy:**

```text
[[8.2]
 [6.7]]
```

Hai hàng là hai học viên; một cột là điểm tổng kết của mỗi người.

### 4.4. Determinant và inverse — Khả nghịch

Định thức `det(A)` là số xác định cho **ma trận vuông**. Với A=`[[2,1],[1,2]]`, định thức bằng `2×2 - 1×1 = 3`, khác 0, nên tồn tại ma trận nghịch đảo `A⁻¹` thỏa `A @ A⁻¹ = I`. Nếu định thức bằng 0 thì không có nghịch đảo. Khi giải hệ phương trình, ưu tiên `np.linalg.solve` hơn việc tính nghịch đảo trực tiếp.

```python
# Mục đích: Khả nghịch.
import numpy as np

A = np.array([[2.0, 1.0], [1.0, 2.0]])
print(round(float(np.linalg.det(A)), 6))
```

**Kết quả khi chạy:**

```text
3.0
```

Định thức 3 khác 0, nên ma trận vuông này khả nghịch.

## 5. Năm tình huống ma trận — từ chuyển vị đến kiểm tra hệ suy biến

### Tình huống 1 — Cấp 1: Lập ma trận bán hàng từ 10 lượt ghi

**Từ vựng trong mục:** **Matrix** — ma trận; **Transpose** — chuyển vị; **Shape** — số hàng/cột.

**Tình huống thực tế:** Quầy bán ghi **10 lượt doanh thu**, gồm hai ngày liên tiếp của **5 cửa hàng** S01…S05 (đơn vị triệu đồng/ngày). Dữ liệu đang ở dạng một dãy [S01 ngày 1, S01 ngày 2, S02 ngày 1, …]. Cần chuyển thành bảng **5 hàng cửa hàng × 2 cột ngày**, tính tổng của S03, rồi chuyển vị thành bảng theo ngày.

**Vì sao chọn cách này?** Ma trận giúp mỗi hàng/cột có ý nghĩa cố định. `reshape(5,2)` sắp dữ liệu theo đúng thứ tự đã ghi, `.T` đổi góc nhìn từ cửa hàng sang ngày mà không làm mất ô.

**Quy trình:**
1. Lưu 10 số liệu theo thứ tự cửa hàng–ngày.
2. Reshape thành ma trận `(5,2)`, tổng hai ngày của S03.
3. Chuyển vị sang `(2,5)` và đối chiếu tổng số phần tử.

```python
import numpy as np
raw = np.array([10,12,9,14,11,13,15,16,12,18], dtype=float)
sales = raw.reshape(5, 2)
by_day = sales.T
if raw.size != 10 or sales.size != 10 or by_day.size != 10:
    raise ValueError("Cần giữ đủ 10 số liệu khi đổi dạng và chuyển vị.")
print("Lượt ghi:", raw.size)
print("Bảng cửa hàng:", sales.shape)
print("Bảng theo ngày:", by_day.shape)
print("S03 (triệu đồng):", int(sales[2].sum()))
```

**Kết quả khi chạy:**

```text
Lượt ghi: 10
Bảng cửa hàng: (5, 2)
Bảng theo ngày: (2, 5)
S03 (triệu đồng): 24
```

Đầu ra tổng của S03 là doanh thu **hai ngày** theo đơn vị triệu đồng, không phải trung bình ngày.

### Tình huống 2 — Cấp 2: Nhân ma trận 12 học viên × 3 tiêu chí với 2 thang đánh giá

**Từ vựng trong mục:** **Matrix multiplication** — nhân ma trận; **Weights** — trọng số; **Dimension** — kích thước.

**Tình huống thực tế:** Một trung tâm ghi **12 học viên**, mỗi hàng có ba điểm lý thuyết, thực hành, dự án (thang 10). Cần tạo **hai điểm đánh giá khác nhau**: chuyên môn (trọng số 50%, 20%, 30%) và hợp tác (10%, 30%, 60%). Hãy tính cho đủ 12 học viên và đếm số người có điểm hợp tác **từ 8**.

**Vì sao chọn cách này?** Ma trận điểm `(12,3)` nhân ma trận trọng số `(3,2)` cho bảng `(12,2)`; mỗi cột đầu ra là một thang đánh giá. Không được nhầm nhân từng phần tử với nhân ma trận.

**Quy trình:**
1. Ghi rõ thứ tự ba tiêu chí và hai nhóm trọng số.
2. Kiểm tra kích thước 12×3 và 3×2; dùng `@`.
3. In hai điểm của người đầu tiên và đếm ngưỡng hợp tác.

```python
import numpy as np
scores = np.array([[5,6,7],[6,8,10],[7,10,9],[8,7,8],[9,9,7],[5,6,10],[6,8,9],[7,10,8],[8,7,7],[9,9,10],[5,6,9],[6,8,8]], dtype=float)
weights = np.array([[0.5, 0.1], [0.2, 0.3], [0.3, 0.6]])
ratings = scores @ weights
if scores.shape != (12, 3) or weights.shape != (3, 2):
    raise ValueError("Bảng điểm 12x3 phải ghép đúng ma trận trọng số 3x2.")
if ratings.shape != (12, 2):
    raise ValueError("Kết quả phải có hai đánh giá cho mỗi trong 12 học viên.")
print("Học viên:", ratings.shape[0])
print("Cột đánh giá:", ratings.shape[1])
print(f"H01 chuyên môn: {ratings[0,0]:.2f}")
print(f"H01 hợp tác: {ratings[0,1]:.2f}")
print("Hợp tác >=8:", int((ratings[:,1] >= 8).sum()))
```

**Kết quả khi chạy:**

```text
Học viên: 12
Cột đánh giá: 2
H01 chuyên môn: 5.80
H01 hợp tác: 6.50
Hợp tác >=8: 6
```

Đầu ra có hai cột **với ý nghĩa khác nhau**; tỷ lệ đạt là yêu cầu giả lập, không phải thang chấm chính thức.

### Tình huống 3 — Cấp 3: Đổi hệ trục 15 tọa độ bằng ma trận quay khả nghịch

**Từ vựng trong mục:** **Transformation** — phép biến đổi; **Determinant** — định thức; **Inverse** — ma trận nghịch đảo.

**Tình huống thực tế:** Một robot ghi **15 điểm tọa độ** trong mặt phẳng (mét); mỗi hàng có tọa độ x/y. Hệ thống muốn đổi các điểm sang hệ trục quay 90° (quy ước véc-tơ hàng của bài), **không làm thay đổi khoảng cách tới gốc**. Cần xác minh ma trận quay có thể đảo ngược bằng định thức và so độ dài trước/sau cho cả 15 điểm.

**Vì sao chọn cách này?** Nhân tọa độ với ma trận quay cho vị trí ở hệ trục mới; định thức khác 0 chứng tỏ có phép biến đổi ngược. Kiểm tra norm giúp học viên hiểu đây là phép quay chứ không phải tùy ý làm co giãn.

**Quy trình:**
1. Tạo ma trận 15×2 chứa các điểm có đơn vị mét.
2. Nhân với ma trận xoay 2×2, kiểm tra định thức khác 0.
3. Dùng `np.allclose` kiểm độ dài và in điểm đầu trước/sau.

```python
import numpy as np
points = np.array([[1,2],[2,2],[3,2],[4,2],[5,2],[1,3],[2,3],[3,3],[4,3],[5,3],[1,4],[2,4],[3,4],[4,4],[5,4]], dtype=float)
rotate = np.array([[0.0, -1.0], [1.0, 0.0]])
converted = points @ rotate
if points.shape != (15, 2) or converted.shape != (15, 2):
    raise ValueError("Phải có đúng 15 điểm gốc và điểm đã đổi tọa độ.")
if not np.allclose(np.linalg.norm(points, axis=1), np.linalg.norm(converted, axis=1)):
    raise ValueError("Phép quay phải bảo toàn chiều dài của từng điểm.")
print("Điểm:", len(points))
print(f"Định thức: {np.linalg.det(rotate):.1f}")
original_labels = []
converted_labels = []
for value in points[0]:
    original_labels.append(f"{value:.1f}")
for value in converted[0]:
    converted_labels.append(f"{value:.1f}")
print("Điểm đầu (gốc):", ", ".join(original_labels))
print("Điểm đầu (mới):", ", ".join(converted_labels))
```

**Kết quả khi chạy:**

```text
Điểm: 15
Định thức: 1.0
Điểm đầu (gốc): 1.0, 2.0
Điểm đầu (mới): 2.0, -1.0
```

Độ dài giữ nguyên nhưng tọa độ trục mới khác, thể hiện tính chất của phép quay. `np.linalg.det` là **một số** dùng kiểm tra khả nghịch, không phải tọa độ.

### Tình huống 4 — Cấp 4: Giải hệ cảm biến 2 kênh cho 18 lượt đo

**Từ vựng trong mục:** **Linear system** — hệ tuyến tính; **np.linalg.solve** — giải hệ; **Residual** — sai số đối chiếu.

**Tình huống thực tế:** Máy đo có **18 lượt đo** của hai nguồn x/y (đơn vị gốc là đơn vị tín hiệu); mỗi hàng cho hai giá trị pha trộn bởi cảm biến: kênh A nhận hai phần x và một phần y, kênh B nhận một phần x và ba phần y. Cần **phục hồi hai giá trị gốc cho từng lượt** dựa trên ma trận hệ số cố định 2×2, rồi xác nhận khi ghép lại tín hiệu kênh thì trùng số đã nhận.

**Vì sao chọn cách này?** `np.linalg.solve` giải hệ trực tiếp từ ma trận hệ số và giá trị đo, thường tốt hơn tự tính nghịch đảo chỉ để tìm nghiệm. Trước khi giải, kiểm tra ma trận vuông và không suy biến; sau khi giải, đối chiếu bằng `allclose`.

**Quy trình:**
1. Lưu ma trận hệ số 2×2 và 18 cặp số đo theo kênh.
2. Dùng `solve` trên ma trận kênh đã chuyển vị để giải 18 lượt cùng lúc.
3. Ghép nghiệm trở lại số đo, xác nhận sai số số học nhỏ và in nghiệm đầu.

```python
import numpy as np
mix = np.array([[2.0, 1.0], [1.0, 3.0]])
measured = np.array([[4,7],[6,8],[8,9],[10,10],[12,11],[14,12],[5,10],[7,11],[9,12],[11,13],[13,14],[15,15],[6,13],[8,14],[10,15],[12,16],[14,17],[16,18]], dtype=float)
restored = np.linalg.solve(mix, measured.T).T
reconstructed = restored @ mix.T
if measured.shape != (18, 2) or restored.shape != (18, 2):
    raise ValueError("Cần đủ 18 lượt đo và hai thông số khôi phục.")
if not np.allclose(reconstructed, measured):
    raise ValueError("Tái tạo số đo phải khớp dữ liệu đầu vào.")
print("Lượt đo:", len(measured))
print(f"Định thức: {np.linalg.det(mix):.1f}")
first_values = []
for value in restored[0]:
    first_values.append(f"{value:.1f}")
print("Nguồn đầu:", ", ".join(first_values))
print("Khôi phục đúng:", bool(np.allclose(reconstructed, measured)))
```

**Kết quả khi chạy:**

```text
Lượt đo: 18
Định thức: 5.0
Nguồn đầu: 1.0, 2.0
Khôi phục đúng: True
```

Mỗi hàng là một bài toán hai ẩn, cùng chung ma trận hệ số. Ví dụ đo lý tưởng không có nhiễu; đo thật còn cần đánh giá sai số và độ nhạy.

### Tình huống 5 — Cấp 5: Kiểm tra 20 ma trận hiệu chuẩn và không giải hệ suy biến

**Từ vựng trong mục:** **Singular matrix** — ma trận suy biến; **Determinant** — định thức; **Numerical stability** — ổn định số.

**Tình huống thực tế:** Nhà máy ghi **20 lượt hiệu chuẩn**, mỗi bản ghi có mã M01…M20, một ma trận hệ số 2×2 và hai số đo. Ba lượt M06, M12, M18 có hai hàng hệ số tỷ lệ nhau nên **không thể phục hồi duy nhất hai nguồn tín hiệu**. Cần tự động xác định lượt không thể giải, chỉ giải các hệ khả nghịch, kiểm tra bằng ghép lại phép nhân và báo số lượt thành công. Không thay kết quả thất bại bằng số 0.

**Vì sao chọn cách này?** Định thức gần 0 cho thấy ma trận không có nghịch đảo duy nhất; cố `solve()` vô điều kiện sẽ gặp lỗi. Đối với hệ đủ điều kiện, giải và kiểm tra lại số đo bằng `allclose` trước khi nhận kết quả.

**Quy trình:**
1. Tạo 20 bản ghi với ID, ma trận 2×2 và vector quan sát.
2. Kiểm tra định thức theo ngưỡng nhỏ đã nêu, đưa trường hợp suy biến vào nhóm cần xem.
3. Chỉ gọi `np.linalg.solve()` trên trường hợp đạt, ghép kết quả lại để xác nhận và đối chiếu số lượt.

```python
import numpy as np
records = [{"id":"M01","coeff":[[2,1],[1,2]],"measurement":[4,5],"original":[1,2]},{"id":"M02","coeff":[[3,1],[1,3]],"measurement":[9,11],"original":[2,3]},{"id":"M03","coeff":[[4,1],[1,4]],"measurement":[16,19],"original":[3,4]},{"id":"M04","coeff":[[2,1],[1,5]],"measurement":[13,29],"original":[4,5]},{"id":"M05","coeff":[[3,1],[1,2]],"measurement":[17,9],"original":[5,2]},{"id":"M06","coeff":[[2,1],[4,2]],"measurement":[5,10],"original":[1,3]},{"id":"M07","coeff":[[2,1],[1,4]],"measurement":[8,18],"original":[2,4]},{"id":"M08","coeff":[[3,1],[1,5]],"measurement":[14,28],"original":[3,5]},{"id":"M09","coeff":[[4,1],[1,2]],"measurement":[18,8],"original":[4,2]},{"id":"M10","coeff":[[2,1],[1,3]],"measurement":[13,14],"original":[5,3]},{"id":"M11","coeff":[[3,1],[1,4]],"measurement":[7,17],"original":[1,4]},{"id":"M12","coeff":[[2,1],[4,2]],"measurement":[9,18],"original":[2,5]},{"id":"M13","coeff":[[2,1],[1,2]],"measurement":[8,7],"original":[3,2]},{"id":"M14","coeff":[[3,1],[1,3]],"measurement":[15,13],"original":[4,3]},{"id":"M15","coeff":[[4,1],[1,4]],"measurement":[24,21],"original":[5,4]},{"id":"M16","coeff":[[2,1],[1,5]],"measurement":[7,26],"original":[1,5]},{"id":"M17","coeff":[[3,1],[1,2]],"measurement":[8,6],"original":[2,2]},{"id":"M18","coeff":[[2,1],[4,2]],"measurement":[9,18],"original":[3,3]},{"id":"M19","coeff":[[2,1],[1,4]],"measurement":[12,20],"original":[4,4]},{"id":"M20","coeff":[[3,1],[1,5]],"measurement":[20,30],"original":[5,5]}]
solved, singular = [], []
for record in records:
    matrix = np.array(record["coeff"], dtype=float)
    measured = np.array(record["measurement"], dtype=float)
    if abs(np.linalg.det(matrix)) < 1e-9:
        singular.append(record["id"])
        continue
    values = np.linalg.solve(matrix, measured)
    if not np.allclose(matrix @ values, measured):
        raise ValueError("Giải hệ phải tái tạo đúng số đo hiệu chuẩn.")
    solved.append(record["id"])
if len(records) != 20 or len(solved) + len(singular) != 20:
    raise ValueError("Phải kiểm tra đủ 20 lượt hiệu chuẩn, kể cả ma trận suy biến.")
print("Lượt hiệu chuẩn:", len(records))
print("Giải được:", len(solved))
print("Không thể giải:", ", ".join(singular))
print("Đối chiếu đủ:", len(solved) + len(singular) == len(records))
```

**Kết quả khi chạy:**

```text
Lượt hiệu chuẩn: 20
Giải được: 17
Không thể giải: M06, M12, M18
Đối chiếu đủ: True
```

Ngưỡng định thức trong ví dụ dùng để phát hiện ma trận suy biến rõ ràng, chưa phải quy tắc số học tổng quát cho mọi ma trận rất lớn hoặc có thang đo chênh lệch; những hệ gần suy biến cần kiểm tra điều kiện số kỹ hơn.

## 6. Sai lầm thường gặp

- `shape=(2,3)` nghĩa là hai hàng và ba cột, không phải ba hàng hai cột.
- `.T` hoán đổi trục; phép nhân `@` yêu cầu số cột bên trái bằng số hàng bên phải.
- Định thức chỉ tính trên ma trận vuông; ma trận có định thức 0 không có nghịch đảo.
- Dữ liệu số thực có sai số làm tròn; dùng `np.allclose` khi kiểm tra gần đúng với ma trận đơn vị.
- Khi giải hệ tuyến tính, thường ưu tiên `np.linalg.solve` thay vì tính nghịch đảo trực tiếp.

## 7. Trắc nghiệm

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a matrix? | Ma trận là gì?**

A. A two-dimensional array of values | Bảng dữ liệu hai chiều

B. A matrix with rows and columns exchanged | Ma trận đổi vai trò hàng và cột

C. Rows of the left matrix with columns of the right | Hàng ma trận trái với cột ma trận phải

D. A scalar associated with a square matrix | Một số gắn với ma trận vuông

**Đáp án: A**

**Giải thích:** Ma trận sắp phần tử theo hàng và cột.


**Q2. What is the transpose of a matrix? | Chuyển vị của ma trận là gì?**

A. A two-dimensional array of values | Bảng dữ liệu hai chiều

B. A matrix with rows and columns exchanged | Ma trận đổi vai trò hàng và cột

C. Rows of the left matrix with columns of the right | Hàng ma trận trái với cột ma trận phải

D. A scalar associated with a square matrix | Một số gắn với ma trận vuông

**Đáp án: B**

**Giải thích:** Chuyển vị hoán đổi các trục ma trận.


**Q3. What does matrix multiplication combine? | Phép nhân ma trận kết hợp gì?**

A. A two-dimensional array of values | Bảng dữ liệu hai chiều

B. A matrix with rows and columns exchanged | Ma trận đổi vai trò hàng và cột

C. Rows of the left matrix with columns of the right | Hàng ma trận trái với cột ma trận phải

D. A scalar associated with a square matrix | Một số gắn với ma trận vuông

**Đáp án: C**

**Giải thích:** Mỗi ô kết quả là tích vô hướng một hàng với một cột.


**Q4. What is a determinant? | Định thức là gì?**

A. A two-dimensional array of values | Bảng dữ liệu hai chiều

B. A matrix with rows and columns exchanged | Ma trận đổi vai trò hàng và cột

C. Rows of the left matrix with columns of the right | Hàng ma trận trái với cột ma trận phải

D. A scalar associated with a square matrix | Một số gắn với ma trận vuông

**Đáp án: D**

**Giải thích:** Định thức hỗ trợ kiểm tra tính khả nghịch.


**Q5. What is the shape of a matrix with two rows and three columns? | Ma trận hai hàng ba cột có shape gì?**

A. `(2, 3)` | `(2, 3)`

B. `(3, 2)` | `(3, 2)`

C. `(2, 1)` | `(2, 1)`

D. `(3, 3)` | `(3, 3)`

**Đáp án: A**

**Giải thích:** Shape ghi số hàng trước số cột.


**Q6. What is the transpose shape of a (2,3) matrix? | Chuyển vị ma trận (2,3) có shape gì?**

A. `(2, 3)` | `(2, 3)`

B. `(3, 2)` | `(3, 2)`

C. `(2, 1)` | `(2, 1)`

D. `(3, 3)` | `(3, 3)`

**Đáp án: B**

**Giải thích:** Hàng và cột đổi vai trò.


**Q7. What shape results from (2,3) @ (3,1)? | Phép (2,3) @ (3,1) cho shape gì?**

A. `(2, 3)` | `(2, 3)`

B. `(3, 2)` | `(3, 2)`

C. `(2, 1)` | `(2, 1)`

D. `(3, 3)` | `(3, 3)`

**Đáp án: C**

**Giải thích:** Hai chiều trong bằng 3; giữ hai chiều ngoài.


**Q8. What is the shape of `np.eye(3)`? | `np.eye(3)` tạo ma trận shape nào?**

A. `(2, 3)` | `(2, 3)`

B. `(3, 2)` | `(3, 2)`

C. `(2, 1)` | `(2, 1)`

D. `(3, 3)` | `(3, 3)`

**Đáp án: D**

**Giải thích:** Ma trận đơn vị bậc 3 là ma trận vuông.


**Q9. Which operator performs matrix multiplication? | Toán tử nào thực hiện nhân ma trận?**

A. `@` | `@`

B. `.T` | `.T`

C. `np.linalg.det(A)` | `np.linalg.det(A)`

D. `np.linalg.inv(A)` | `np.linalg.inv(A)`

**Đáp án: A**

**Giải thích:** @ thực hiện đúng quy tắc nhân ma trận.


**Q10. Which attribute returns the transpose of a 2-D ndarray? | Thuộc tính nào cho chuyển vị mảng 2-D?**

A. `@` | `@`

B. `.T` | `.T`

C. `np.linalg.det(A)` | `np.linalg.det(A)`

D. `np.linalg.inv(A)` | `np.linalg.inv(A)`

**Đáp án: B**

**Giải thích:** T là thuộc tính chuyển vị tiện dụng.


**Q11. Which function computes a square matrix determinant? | Hàm nào tính định thức ma trận vuông?**

A. `@` | `@`

B. `.T` | `.T`

C. `np.linalg.det(A)` | `np.linalg.det(A)`

D. `np.linalg.inv(A)` | `np.linalg.inv(A)`

**Đáp án: C**

**Giải thích:** det trả định thức dạng số.


**Q12. Which function computes a nonsingular matrix inverse? | Hàm nào tính nghịch đảo ma trận khả nghịch?**

A. `@` | `@`

B. `.T` | `.T`

C. `np.linalg.det(A)` | `np.linalg.det(A)`

D. `np.linalg.inv(A)` | `np.linalg.inv(A)`

**Đáp án: D**

**Giải thích:** inv tính nghịch đảo khi ma trận khả nghịch.


**Q13. When is a square matrix invertible? | Khi nào ma trận vuông khả nghịch?**

A. Its determinant is nonzero | Định thức khác không

B. 3 | 3

C. Identity matrix | Ma trận đơn vị

D. `np.allclose(A, B)` | `np.allclose(A, B)`

**Đáp án: A**

**Giải thích:** Định thức khác 0 tương đương khả nghịch.


**Q14. What is determinant of [[2,1],[1,2]]? | Định thức [[2,1],[1,2]] bằng gì?**

A. Its determinant is nonzero | Định thức khác không

B. 3 | 3

C. Identity matrix | Ma trận đơn vị

D. `np.allclose(A, B)` | `np.allclose(A, B)`

**Đáp án: B**

**Giải thích:** Định thức 2×2 bằng 2×2−1×1.


**Q15. What does `A @ inv(A)` approximate? | `A @ inv(A)` gần bằng gì?**

A. Its determinant is nonzero | Định thức khác không

B. 3 | 3

C. Identity matrix | Ma trận đơn vị

D. `np.allclose(A, B)` | `np.allclose(A, B)`

**Đáp án: C**

**Giải thích:** Nhân ma trận với nghịch đảo bằng I trong tính toán chính xác.


**Q16. How do you test approximate equality of float arrays? | Kiểm tra hai mảng float gần bằng nhau bằng gì?**

A. Its determinant is nonzero | Định thức khác không

B. 3 | 3

C. Identity matrix | Ma trận đơn vị

D. `np.allclose(A, B)` | `np.allclose(A, B)`

**Đáp án: D**

**Giải thích:** allclose chấp nhận sai số dấu phẩy động nhỏ.


**Q17. Which dimensions must match for A @ B? | Nhân A @ B cần các chiều nào bằng nhau?**

A. Columns of A and rows of B | Số cột A và số hàng B

B. Element-wise multiplication | Nhân theo từng phần tử

C. `np.linalg.solve(A, b)` | `np.linalg.solve(A, b)`

D. A linear algebra error | Lỗi đại số tuyến tính

**Đáp án: A**

**Giải thích:** Nhân ma trận yêu cầu hai chiều trong trùng.


**Q18. What does `A * B` do for compatible NumPy arrays? | `A * B` trên mảng NumPy tương thích làm gì?**

A. Columns of A and rows of B | Số cột A và số hàng B

B. Element-wise multiplication | Nhân theo từng phần tử

C. `np.linalg.solve(A, b)` | `np.linalg.solve(A, b)`

D. A linear algebra error | Lỗi đại số tuyến tính

**Đáp án: B**

**Giải thích:** Dấu sao nhân phần tử tương ứng có broadcasting.


**Q19. What is preferred to solve Ax=b numerically? | Để giải hệ Ax=b bằng NumPy nên ưu tiên gì?**

A. Columns of A and rows of B | Số cột A và số hàng B

B. Element-wise multiplication | Nhân theo từng phần tử

C. `np.linalg.solve(A, b)` | `np.linalg.solve(A, b)`

D. A linear algebra error | Lỗi đại số tuyến tính

**Đáp án: C**

**Giải thích:** Giải trực tiếp thường tốt hơn tính nghịch đảo rồi nhân.


**Q20. What happens to a singular matrix when using `np.linalg.inv`? | Dùng `np.linalg.inv` với ma trận suy biến thường gây gì?**

A. Columns of A and rows of B | Số cột A và số hàng B

B. Element-wise multiplication | Nhân theo từng phần tử

C. `np.linalg.solve(A, b)` | `np.linalg.solve(A, b)`

D. A linear algebra error | Lỗi đại số tuyến tính

**Đáp án: D**

**Giải thích:** Ma trận suy biến không có nghịch đảo.

## 8. Nối sang bài kế tiếp

`Vector → Matrix → Hệ tuyến tính → Eigenvalue/PCA`.
