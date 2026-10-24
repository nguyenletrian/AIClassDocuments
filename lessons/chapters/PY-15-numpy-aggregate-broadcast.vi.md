# PY-15 — NumPy tổng hợp, axis và broadcasting


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Aggregate** — phép tổng hợp; **Axis** — trục tính.

`Index/Slice → Aggregate/Broadcast → Vectorization → AI`

Sau NumPy indexing và slicing, ta học cách tính tổng, trung bình theo đúng trục, cộng hoặc nhân nhiều giá trị đồng loạt, thay vì xử lý từng phần tử bằng các vòng lặp riêng.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Dùng khi nào |
|---|---|---|
| Aggregate | phép tổng hợp | Gom nhiều giá trị thành chỉ số thống kê |
| Axis | trục tính | Chiều dọc theo phép gom giá trị |
| Broadcasting | quảng bá mảng | Mở rộng kích thước tương thích khi tính |
| Vectorization | vector hóa | Tính cả mảng không cần viết vòng for từng phần tử |

## 3. Thư viện, hàm và lựa chọn

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / tham số | Giải thích ngay theo hàm |
|---|---|
| `np.sum(X,axis=0)` | Tổng theo từng cột, axis=1 tổng theo hàng |
| `np.mean()/np.max()/np.min()` | Tổng hợp trung bình, cực đại và cực tiểu |
| `X + scalar / X + vector` | Broadcast nếu shape tương thích |
| `np.sqrt()/np.exp()` | Biến đổi từng phần tử, chú ý miền giá trị |


## 4. Khái niệm liên quan

Sau khi biết tạo và chọn ô trong `ndarray`, ta cần **tổng hợp và biến đổi nhiều giá trị cùng lúc**. Phần này tiếp nối bảng doanh thu và điểm số: tổng hợp để rút ra thống kê, chọn `axis` để biết tổng hợp theo hàng hay cột, rồi dùng broadcasting và vectorization để xử lý đồng loạt mà không viết từng phép tính.

### 4.1. Aggregation — Tổng hợp từ nhiều giá trị

**Từ vựng trong mục:** **Aggregation** — tổng hợp; **Sum/mean** — tổng/trung bình.

Khi quản lý doanh thu, ta thường không cần xem từng giao dịch mà muốn biết **tổng**, **trung bình** hoặc **cao nhất**. Đó là **phép tổng hợp (aggregation)**: kết hợp nhiều giá trị thành một giá trị thống kê. Với doanh thu ba ngày `[10,20,30]` triệu đồng, `sum()` cho 60 triệu đồng; `mean()` cho 20 triệu đồng/ngày; `max()` cho 30 triệu đồng. Không nhầm tổng với trung bình.

```python
import numpy as np

sales = np.array([10, 20, 30])
print(sales.sum(), sales.mean(), sales.max())
```

**Kết quả khi chạy:**

```text
60 20.0 30
```

Tổng 60 triệu đồng, trung bình 20 triệu đồng/ngày và ngày cao nhất 30 triệu đồng.

### 4.2. Axis — Tổng hợp theo hàng hoặc cột

**Từ vựng trong mục:** **Axis** — trục tính; **Row/column** — hàng/cột.

Trong bảng doanh thu có **hai hàng cửa hàng** A, B và **ba cột ngày**, `sales.sum(axis=1)` tính tổng ba ngày trên từng **hàng cửa hàng**; còn `sales.sum(axis=0)` tính tổng hai cửa hàng theo từng **cột ngày**. `axis=0` gom **qua các hàng**, `axis=1` gom **qua các cột**. Vì vậy trước khi chọn axis, phải biết mỗi chiều đang mô tả gì.

```python
import numpy as np

sales = np.array([[10, 20, 30], [8, 12, 16]])
print(sales.sum(axis=1))
```

**Kết quả khi chạy:**

```text
[60 36]
```

Kết quả có hai phần tử vì mảng có hai hàng: cửa hàng A tổng 60 và B tổng 36 triệu đồng.

### 4.3. Broadcasting — Áp dụng phép toán theo chiều tương thích

**Từ vựng trong mục:** **Broadcasting** — quảng bá mảng; **Shape** — kích thước.

**Broadcasting** cho phép NumPy thực hiện phép toán giữa các đối tượng khác kích thước **nếu các chiều tương thích**. Ví dụ một trường cộng 1 điểm chuyên cần cho từng điểm trong bảng hai học viên × ba môn: phép `scores + 1` tự áp dụng 1 vào mọi ô, không cần vòng `for`. Khi một chiều có kích thước 1 hoặc bằng chiều tương ứng, NumPy thường mở rộng được; các chiều không tương thích sẽ báo `ValueError`.

```python
import numpy as np

scores = np.array([[7, 8, 9], [6, 7, 8]])
print(scores + 1)
```

**Kết quả khi chạy:**

```text
[[ 8  9 10]
 [ 7  8  9]]
```

Số 1 được cộng vào cả sáu ô, nhưng shape vẫn là 2 hàng × 3 cột.

### 4.4. Vectorization — Tính trực tiếp trên mảng

**Từ vựng trong mục:** **Vectorization** — vector hóa; **Element-wise** — theo từng phần tử.

**Vectorization** là viết phép tính trực tiếp trên toàn mảng thay vì tự lặp từng ô bằng Python. Khi ba kênh cảm biến có giá trị `[10,20,30]` và hệ số hiệu chỉnh `[1.0,0.5,2.0]`, phép `signals * factors` nhân các phần tử **cùng vị trí**: 10×1, 20×0,5 và 30×2. Đây là phép **nhân từng phần tử**, khác phép nhân ma trận `@`.

```python
import numpy as np

signals = np.array([10, 20, 30])
factors = np.array([1.0, 0.5, 2.0])
print(signals * factors)
```

**Kết quả khi chạy:**

```text
[10. 10. 60.]
```

Ba số là tín hiệu sau khi áp dụng hệ số riêng cho từng kênh; NumPy không cộng các kênh lại.

## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Tổng doanh thu từng cửa hàng

**Từ vựng trong mục:** **Aggregation** — tổng hợp; **Axis** — trục tính.

**Tình huống thực tế:** Hai cửa hàng A và B có doanh thu ba ngày lần lượt là `[10,20,30]` và `[8,12,16]`, đơn vị triệu đồng. Hãy tính tổng cho **mỗi cửa hàng** để so sánh.

**Vì sao chọn cách giải này?** Hai cửa hàng ở hai hàng, còn ba ngày ở các cột; `sum(axis=1)` tổng hợp ba ngày của mỗi hàng.

**Quy trình giải:**

1. Tạo mảng 2 hàng × 3 cột, hàng đầu là A, hàng sau là B.
2. Dùng `sum(axis=1)` cộng qua ba cột ngày.
3. In hai tổng theo thứ tự A rồi B.

```python
import numpy as np

sales = np.array([[10, 20, 30], [8, 12, 16]])
print(sales.sum(axis=1))
```

**Kết quả khi chạy:**

```text
[60 36]
```

Doanh thu ba ngày của A là 60 triệu, B là 36 triệu đồng.

### Tình huống 2 — Trung bình theo từng môn

**Từ vựng trong mục:** **Mean** — trung bình; **Axis** — trục.

**Tình huống thực tế:** Ba học viên An, Bình, Lan có điểm Toán/Python lần lượt (8,9), (6,7), (9,8) trên thang 10. Hãy tính trung bình **theo từng môn**, không phải từng học viên.

**Vì sao chọn cách giải này?** Môn học ở các cột nên `mean(axis=0)` tổng hợp các hàng học viên cho từng cột môn.

**Quy trình giải:**

1. Tạo mảng 3 hàng học viên × 2 cột môn Toán, Python.
2. Chọn `axis=0` để lấy trung bình từng cột.
3. In hai điểm trung bình.

```python
import numpy as np

scores = np.array([[8, 9], [6, 7], [9, 8]], dtype=float)
print(scores.mean(axis=0))
```

**Kết quả khi chạy:**

```text
[7.66666667 8.        ]
```

Điểm trung bình Toán ≈ 7,67; Python là 8,0.

### Tình huống 3 — Cộng điểm chuyên cần có giới hạn

**Từ vựng trong mục:** **Broadcasting** — quảng bá; **Clip** — giới hạn giá trị.

**Tình huống thực tế:** Trường có hai học viên, ba môn; điểm hiện tại lần lượt `[7,8,9]`, `[6,7,8]`. Mỗi điểm được cộng 1 điểm chuyên cần nhưng không được vượt 10. Hãy in bảng sau cộng.

**Vì sao chọn cách giải này?** Broadcasting cộng 1 vào mọi ô; `np.minimum(...,10)` bảo đảm mỗi ô không vượt điểm tối đa.

**Quy trình giải:**

1. Lưu điểm trong mảng 2 hàng × 3 cột.
2. Cộng 1 cho toàn bộ mảng theo broadcasting.
3. Áp dụng `np.minimum` giới hạn điểm 10 rồi in kết quả.

```python
import numpy as np

scores = np.array([[7, 8, 9], [6, 7, 8]])
print(np.minimum(scores + 1, 10))
```

**Kết quả khi chạy:**

```text
[[ 8  9 10]
 [ 7  8  9]]
```

Mỗi ô tăng một điểm; điểm 9 chỉ lên 10, không vượt giới hạn.

### Tình huống 4 — Hiệu chỉnh ba kênh cảm biến

**Từ vựng trong mục:** **Vectorization** — vector hóa; **Element-wise** — theo phần tử.

**Tình huống thực tế:** Ba kênh cảm biến có giá trị `[10,20,30]` và hệ số hiệu chỉnh tương ứng `[1.0,0.5,2.0]`. Hãy tính tín hiệu sau hiệu chỉnh của từng kênh.

**Vì sao chọn cách giải này?** Nhân hai mảng cùng shape sẽ nhân từng vị trí tương ứng, đơn giản hơn viết ba phép nhân riêng.

**Quy trình giải:**

1. Tạo mảng tín hiệu và mảng hệ số theo cùng thứ tự kênh.
2. Nhân hai mảng trực tiếp bằng `*`.
3. In ba giá trị sau hiệu chỉnh.

```python
import numpy as np

signals = np.array([10, 20, 30])
factors = np.array([1.0, 0.5, 2.0])
print(signals * factors)
```

**Kết quả khi chạy:**

```text
[10. 10. 60.]
```

Tín hiệu lần lượt là 10, 10 và 60 theo đơn vị của từng kênh.

### Tình huống 5 — Tìm giá trị cao nhất theo cột

**Từ vựng trong mục:** **Aggregation** — tổng hợp; **Max** — cực đại.

**Tình huống thực tế:** Bảng có ba ngày đo và hai kênh cảm biến: các hàng là `(2,4)`, `(5,1)`, `(3,6)` theo cùng đơn vị đo trên từng kênh. Hãy tìm mức lớn nhất của **mỗi kênh**, không phải mỗi ngày.

**Vì sao chọn cách giải này?** Kênh nằm theo cột, nên `max(axis=0)` lấy giá trị lớn nhất trong các hàng cho mỗi cột.

**Quy trình giải:**

1. Tạo bảng ba hàng ngày × hai cột kênh.
2. Dùng `max(axis=0)` lấy cực đại từng cột.
3. In hai số cực đại theo thứ tự kênh.

```python
import numpy as np

values = np.array([[2, 4], [5, 1], [3, 6]])
print(values.max(axis=0))
```

**Kết quả khi chạy:**

```text
[5 6]
```

Kênh thứ nhất có giá trị tối đa 5, kênh thứ hai tối đa 6.

## 6. Sai lầm thường gặp

- Với mảng hai chiều, `axis=0` tổng hợp **theo cột** (gom các hàng), còn `axis=1` tổng hợp **theo hàng** (gom các cột). Không đoán axis chỉ từ tên hàm.
- `sum`, `mean`, `max` có ý nghĩa khác nhau: tổng, trung bình và cực đại, không thể thay thế tùy tiện.
- Broadcasting chỉ hoạt động khi **shape tương thích**. Hai mảng có chiều không tương thích có thể phát sinh `ValueError`.
- Dấu `*` của NumPy nhân **từng phần tử**, không phải phép nhân ma trận `@`.
- Khi cộng điểm, phải áp dụng giới hạn tối đa nếu quy định yêu cầu, ví dụ `np.minimum(scores + 1, 10)`.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.


**Q1. What does Aggregate mean? — Ý nghĩa của Aggregate là gì?**

A. It instead describes Chiều dọc theo phép gom giá trị — Chiều dọc theo phép gom giá trị

B. The concept is Gom nhiều giá trị thành chỉ số thống kê — Gom nhiều giá trị thành chỉ số thống kê

C. It instead describes Mở rộng kích thước tương thích khi tính — Mở rộng kích thước tương thích khi tính

D. It instead describes Tính cả mảng không cần viết vòng for từng phần tử — Tính cả mảng không cần viết vòng for từng phần tử


**Q2. What does Axis mean? — Ý nghĩa của Axis là gì?**

A. The concept is Chiều dọc theo phép gom giá trị — Chiều dọc theo phép gom giá trị

B. It instead describes Mở rộng kích thước tương thích khi tính — Mở rộng kích thước tương thích khi tính

C. It instead describes Tính cả mảng không cần viết vòng for từng phần tử — Tính cả mảng không cần viết vòng for từng phần tử

D. It instead describes Gom nhiều giá trị thành chỉ số thống kê — Gom nhiều giá trị thành chỉ số thống kê


**Q3. What does Broadcasting mean? — Ý nghĩa của Broadcasting là gì?**

A. It instead describes Tính cả mảng không cần viết vòng for từng phần tử — Tính cả mảng không cần viết vòng for từng phần tử

B. It instead describes Gom nhiều giá trị thành chỉ số thống kê — Gom nhiều giá trị thành chỉ số thống kê

C. It instead describes Chiều dọc theo phép gom giá trị — Chiều dọc theo phép gom giá trị

D. The concept is Mở rộng kích thước tương thích khi tính — Mở rộng kích thước tương thích khi tính


**Q4. What does Vectorization mean? — Ý nghĩa của Vectorization là gì?**

A. It instead describes Gom nhiều giá trị thành chỉ số thống kê — Gom nhiều giá trị thành chỉ số thống kê

B. It instead describes Chiều dọc theo phép gom giá trị — Chiều dọc theo phép gom giá trị

C. The concept is Tính cả mảng không cần viết vòng for từng phần tử — Tính cả mảng không cần viết vòng for từng phần tử

D. It instead describes Mở rộng kích thước tương thích khi tính — Mở rộng kích thước tương thích khi tính


**Q5. What is the role of np.sum(X,axis=0)? — Vai trò của np.sum(X,axis=0) là gì?**

A. Another operation would Tổng hợp trung bình, cực đại và cực tiểu — Tổng hợp trung bình, cực đại và cực tiểu

B. It is used to Tổng theo từng cột, axis=1 tổng theo hàng — Tổng theo từng cột, axis=1 tổng theo hàng

C. Another operation would Broadcast nếu shape tương thích — Broadcast nếu shape tương thích

D. Another operation would Biến đổi từng phần tử, chú ý miền giá trị — Biến đổi từng phần tử, chú ý miền giá trị


**Q6. What is the role of np.mean()/np.max()/np.min()? — Vai trò của np.mean()/np.max()/np.min() là gì?**

A. It is used to Tổng hợp trung bình, cực đại và cực tiểu — Tổng hợp trung bình, cực đại và cực tiểu

B. Another operation would Broadcast nếu shape tương thích — Broadcast nếu shape tương thích

C. Another operation would Biến đổi từng phần tử, chú ý miền giá trị — Biến đổi từng phần tử, chú ý miền giá trị

D. Another operation would Tổng theo từng cột, axis=1 tổng theo hàng — Tổng theo từng cột, axis=1 tổng theo hàng


**Q7. What is the role of X + scalar / X + vector? — Vai trò của X + scalar / X + vector là gì?**

A. Another operation would Biến đổi từng phần tử, chú ý miền giá trị — Biến đổi từng phần tử, chú ý miền giá trị

B. Another operation would Tổng theo từng cột, axis=1 tổng theo hàng — Tổng theo từng cột, axis=1 tổng theo hàng

C. Another operation would Tổng hợp trung bình, cực đại và cực tiểu — Tổng hợp trung bình, cực đại và cực tiểu

D. It is used to Broadcast nếu shape tương thích — Broadcast nếu shape tương thích


**Q8. What is the role of np.sqrt()/np.exp()? — Vai trò của np.sqrt()/np.exp() là gì?**

A. Another operation would Tổng theo từng cột, axis=1 tổng theo hàng — Tổng theo từng cột, axis=1 tổng theo hàng

B. Another operation would Tổng hợp trung bình, cực đại và cực tiểu — Tổng hợp trung bình, cực đại và cực tiểu

C. It is used to Biến đổi từng phần tử, chú ý miền giá trị — Biến đổi từng phần tử, chú ý miền giá trị

D. Another operation would Broadcast nếu shape tương thích — Broadcast nếu shape tương thích


**Q9. Which reason fits example 1? — Lý do nào phù hợp ví dụ 1?**

A. axis=0 gom toàn bộ học sinh theo một cột môn — axis=0 gom toàn bộ học sinh theo một cột môn

B. axis=1 cộng các ngày trên một hàng/cửa hàng — axis=1 cộng các ngày trên một hàng/cửa hàng

C. Broadcast cộng thưởng 1 điểm cho từng môn — Broadcast cộng thưởng 1 điểm cho từng môn

D. Vector hóa nhân hệ số cho toàn bộ kênh — Vector hóa nhân hệ số cho toàn bộ kênh


**Q10. Which reason fits example 2? — Lý do nào phù hợp ví dụ 2?**

A. axis=0 gom toàn bộ học sinh theo một cột môn — axis=0 gom toàn bộ học sinh theo một cột môn

B. Broadcast cộng thưởng 1 điểm cho từng môn — Broadcast cộng thưởng 1 điểm cho từng môn

C. Vector hóa nhân hệ số cho toàn bộ kênh — Vector hóa nhân hệ số cho toàn bộ kênh

D. max(axis=0) chọn đỉnh từng feature — max(axis=0) chọn đỉnh từng feature


**Q11. Which reason fits example 3? — Lý do nào phù hợp ví dụ 3?**

A. Vector hóa nhân hệ số cho toàn bộ kênh — Vector hóa nhân hệ số cho toàn bộ kênh

B. max(axis=0) chọn đỉnh từng feature — max(axis=0) chọn đỉnh từng feature

C. axis=1 cộng các ngày trên một hàng/cửa hàng — axis=1 cộng các ngày trên một hàng/cửa hàng

D. Broadcast cộng thưởng 1 điểm cho từng môn — Broadcast cộng thưởng 1 điểm cho từng môn


**Q12. Which reason fits example 4? — Lý do nào phù hợp ví dụ 4?**

A. max(axis=0) chọn đỉnh từng feature — max(axis=0) chọn đỉnh từng feature

B. axis=1 cộng các ngày trên một hàng/cửa hàng — axis=1 cộng các ngày trên một hàng/cửa hàng

C. Vector hóa nhân hệ số cho toàn bộ kênh — Vector hóa nhân hệ số cho toàn bộ kênh

D. axis=0 gom toàn bộ học sinh theo một cột môn — axis=0 gom toàn bộ học sinh theo một cột môn


**Q13. Which reason fits example 5? — Lý do nào phù hợp ví dụ 5?**

A. axis=1 cộng các ngày trên một hàng/cửa hàng — axis=1 cộng các ngày trên một hàng/cửa hàng

B. max(axis=0) chọn đỉnh từng feature — max(axis=0) chọn đỉnh từng feature

C. axis=0 gom toàn bộ học sinh theo một cột môn — axis=0 gom toàn bộ học sinh theo một cột môn

D. Broadcast cộng thưởng 1 điểm cho từng môn — Broadcast cộng thưởng 1 điểm cho từng môn


**Q14. Which input matches example 1? — Dữ liệu nào phù hợp ví dụ 1?**

A. The stated data are 2 cửa hàng × 3 ngày, nghìn đồng — 2 cửa hàng × 3 ngày, nghìn đồng

B. Other data: 3 học sinh × 2 môn — 3 học sinh × 2 môn

C. Other data: 2 học sinh × 3 môn — 2 học sinh × 3 môn

D. Other data: 3 giá trị đo và hệ số quy đổi — 3 giá trị đo và hệ số quy đổi


**Q15. Which input matches example 2? — Dữ liệu nào phù hợp ví dụ 2?**

A. Other data: 2 học sinh × 3 môn — 2 học sinh × 3 môn

B. Other data: 3 giá trị đo và hệ số quy đổi — 3 giá trị đo và hệ số quy đổi

C. Other data: 3 mẫu × 2 kênh — 3 mẫu × 2 kênh

D. The stated data are 3 học sinh × 2 môn — 3 học sinh × 2 môn


**Q16. Which input matches example 3? — Dữ liệu nào phù hợp ví dụ 3?**

A. Other data: 3 giá trị đo và hệ số quy đổi — 3 giá trị đo và hệ số quy đổi

B. Other data: 3 mẫu × 2 kênh — 3 mẫu × 2 kênh

C. The stated data are 2 học sinh × 3 môn — 2 học sinh × 3 môn

D. Other data: 2 cửa hàng × 3 ngày, nghìn đồng — 2 cửa hàng × 3 ngày, nghìn đồng


**Q17. Which input matches example 4? — Dữ liệu nào phù hợp ví dụ 4?**

A. Other data: 3 mẫu × 2 kênh — 3 mẫu × 2 kênh

B. The stated data are 3 giá trị đo và hệ số quy đổi — 3 giá trị đo và hệ số quy đổi

C. Other data: 2 cửa hàng × 3 ngày, nghìn đồng — 2 cửa hàng × 3 ngày, nghìn đồng

D. Other data: 3 học sinh × 2 môn — 3 học sinh × 2 môn


**Q18. Which input matches example 5? — Dữ liệu nào phù hợp ví dụ 5?**

A. The stated data are 3 mẫu × 2 kênh — 3 mẫu × 2 kênh

B. Other data: 2 cửa hàng × 3 ngày, nghìn đồng — 2 cửa hàng × 3 ngày, nghìn đồng

C. Other data: 3 học sinh × 2 môn — 3 học sinh × 2 môn

D. Other data: 2 học sinh × 3 môn — 2 học sinh × 3 môn


**Q19. What must every table clarify? — Bảng dữ liệu cần nêu rõ gì?**

A. Only editor color — Chỉ màu trình soạn

B. Only variable length — Chỉ độ dài tên biến

C. Only number of blank lines — Chỉ số dòng trống

D. Rows, columns and units — Hàng, cột và đơn vị


**Q20. Why test with different inputs? — Tại sao cần thử đầu vào khác?**

A. To guarantee machine learning accuracy — Để bảo đảm AI luôn đúng

B. To remove input validation — Để bỏ kiểm tra dữ liệu

C. To check limitations and edge cases — Để thấy giới hạn và trường hợp biên

D. To change column meanings — Để thay đổi nghĩa các cột

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | The concept is Gom nhiều giá trị thành chỉ số thống kê | Gom nhiều giá trị thành chỉ số thống kê |
| Q2 | **A** | The concept is Chiều dọc theo phép gom giá trị | Chiều dọc theo phép gom giá trị |
| Q3 | **D** | The concept is Mở rộng kích thước tương thích khi tính | Mở rộng kích thước tương thích khi tính |
| Q4 | **C** | The concept is Tính cả mảng không cần viết vòng for từng phần tử | Tính cả mảng không cần viết vòng for từng phần tử |
| Q5 | **B** | It is used to Tổng theo từng cột, axis=1 tổng theo hàng | Tổng theo từng cột, axis=1 tổng theo hàng |
| Q6 | **A** | It is used to Tổng hợp trung bình, cực đại và cực tiểu | Tổng hợp trung bình, cực đại và cực tiểu |
| Q7 | **D** | It is used to Broadcast nếu shape tương thích | Broadcast nếu shape tương thích |
| Q8 | **C** | It is used to Biến đổi từng phần tử, chú ý miền giá trị | Biến đổi từng phần tử, chú ý miền giá trị |
| Q9 | **B** | axis=1 cộng các ngày trên một hàng/cửa hàng | axis=1 cộng các ngày trên một hàng/cửa hàng |
| Q10 | **A** | axis=0 gom toàn bộ học sinh theo một cột môn | axis=0 gom toàn bộ học sinh theo một cột môn |
| Q11 | **D** | Broadcast cộng thưởng 1 điểm cho từng môn | Broadcast cộng thưởng 1 điểm cho từng môn |
| Q12 | **C** | Vector hóa nhân hệ số cho toàn bộ kênh | Vector hóa nhân hệ số cho toàn bộ kênh |
| Q13 | **B** | max(axis=0) chọn đỉnh từng feature | max(axis=0) chọn đỉnh từng feature |
| Q14 | **A** | The stated data are 2 cửa hàng × 3 ngày, nghìn đồng | 2 cửa hàng × 3 ngày, nghìn đồng |
| Q15 | **D** | The stated data are 3 học sinh × 2 môn | 3 học sinh × 2 môn |
| Q16 | **C** | The stated data are 2 học sinh × 3 môn | 2 học sinh × 3 môn |
| Q17 | **B** | The stated data are 3 giá trị đo và hệ số quy đổi | 3 giá trị đo và hệ số quy đổi |
| Q18 | **A** | The stated data are 3 mẫu × 2 kênh | 3 mẫu × 2 kênh |
| Q19 | **D** | Rows, columns and units | Hàng, cột và đơn vị |
| Q20 | **C** | To check limitations and edge cases | Để thấy giới hạn và trường hợp biên |

## 8. Nối bài tiếp theo

`Index/Slice → Aggregate/Broadcast → Vectorization → AI`.
