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

**Q1. What is aggregation in NumPy? — Phép tổng hợp trong NumPy là gì?**

A. Replacing array values without computation — Thay giá trị mảng mà không tính toán

B. Rearranging all values in descending order — Sắp mọi giá trị giảm dần

C. Converting array dimensions into text labels — Đổi kích thước mảng thành nhãn văn bản

D. Combining multiple values into summary statistics — Kết hợp nhiều giá trị thành thống kê tổng hợp

**Q2. How does `sum()` differ from `mean()`? — `sum()` khác `mean()` ra sao?**

A. `sum` always returns the largest element — `sum` luôn trả phần tử lớn nhất

B. `mean` ignores the number of values — `mean` không dùng số lượng phần tử

C. sum totals values; mean computes their average — sum cộng tổng; mean tính trung bình

D. `sum` computes average; `mean` computes total — `sum` tính trung bình; `mean` tính tổng

**Q3. What does `max()` return? — `max()` trả về gì?**

A. The sum of all elements — Tổng mọi phần tử

B. The average of the chosen values — Trung bình các giá trị được chọn

C. The largest value along the chosen axis — Giá trị lớn nhất theo trục đã chọn

D. The first item in the array — Phần tử đầu của mảng

**Q4. In a 2-D array, what does `sum(axis=0)` return? — Trong mảng hai chiều, `sum(axis=0)` trả về gì?**

A. One scalar sum for all cells — Một tổng vô hướng cho mọi ô

B. The first column with original values — Cột đầu với giá trị gốc

C. One sum per column — Một tổng cho mỗi cột

D. One sum for each row — Một tổng theo mỗi hàng

**Q5. In a 2-D array, what does `sum(axis=1)` return? — Trong mảng hai chiều, `sum(axis=1)` trả về gì?**

A. One sum for each column — Một tổng theo mỗi cột

B. A one-dimensional array of all original values — Mảng một chiều gồm mọi giá trị ban đầu

C. The last row without adding values — Hàng cuối mà không cộng giá trị

D. One sum per row — Một tổng cho mỗi hàng

**Q6. What does broadcasting allow? — Broadcasting cho phép làm gì?**

A. Multiplying two matrices using dot products — Nhân hai ma trận bằng tích vô hướng

B. Operating on arrays with compatible shapes — Thực hiện phép toán trên các mảng có shape tương thích

C. Arbitrary operations regardless of shape compatibility — Mọi phép toán dù shape không tương thích

D. Always making a physical copy of the smaller operand — Luôn sao chép vật lý toán hạng nhỏ

**Q7. Why does `a + 1` work on a numeric ndarray? — Vì sao `a + 1` hoạt động với ndarray số?**

A. The scalar broadcasts to every array element — Số 1 được broadcast tới từng phần tử

B. A scalar is added only to the first element — Vô hướng chỉ cộng vào phần tử đầu

C. Scalar addition means matrix multiplication — Cộng vô hướng nghĩa là nhân ma trận

D. NumPy converts the array into a list first — NumPy đổi mảng thành List trước

**Q8. Which pair of trailing dimensions is broadcast-compatible? — Hai chiều cuối nào tương thích broadcasting?**

A. Equal sizes or one size equal to 1 — Bằng nhau hoặc một chiều có kích thước 1

B. Two dimensions are compatible when their sizes add to four — Hai chiều hợp lệ khi tổng kích thước bằng bốn

C. Every pair of positive dimension sizes is compatible — Mọi cặp kích thước chiều dương đều tương thích

D. Only dimensions with exactly zero size are compatible — Chỉ chiều có kích thước đúng 0 mới tương thích

**Q9. What happens for incompatible broadcast shapes? — Điều gì xảy ra khi hai shape không tương thích broadcasting?**

A. A ValueError is generally raised — Thường phát sinh ValueError

B. NumPy silently removes unmatched rows — NumPy âm thầm xóa hàng không khớp

C. NumPy guarantees a valid result by padding zeros — NumPy bảo đảm kết quả bằng cách chèn số 0

D. The result is always `None` — Kết quả luôn là `None`

**Q10. What is vectorization? — Vectorization là gì?**

A. Reducing every array into one scalar only — Chỉ gộp mọi mảng thành một vô hướng

B. Automatically turning numbers into strings — Tự chuyển số thành chuỗi

C. Requiring a Python `for` loop around each item — Bắt buộc dùng vòng `for` Python quanh từng phần tử

D. Applying numerical operations to arrays directly — Áp dụng phép toán số trực tiếp lên mảng

**Q11. What does NumPy `a * b` do for equal-shaped numeric arrays? — NumPy `a * b` làm gì với hai mảng số cùng shape?**

A. Concatenation of array elements — Nối phần tử của các mảng

B. Only checking if the arrays have equal shape — Chỉ kiểm tra shape có bằng nhau

C. Multiply corresponding elements — Nhân các phần tử cùng vị trí

D. Matrix multiplication regardless of array dimensions — Nhân ma trận bất kể các chiều

**Q12. Which operator is used for matrix multiplication? — Toán tử nào dùng để nhân ma trận?**

A. `*` — `*`

B. `and` — `and`

C. `%` — `%`

D. `@` — `@`

**Q13. What does `np.minimum(a, 10)` do? — `np.minimum(a, 10)` có tác dụng gì?**

A. Making every array element equal to 10 — Đặt mọi phần tử bằng 10

B. Cap each value at 10 — Giới hạn mỗi giá trị tối đa 10

C. Discarding every value below 10 — Loại mọi giá trị nhỏ hơn 10

D. Returning only the smallest element of the full array — Chỉ trả cực tiểu toàn mảng

**Q14. How does `np.min()` differ from `np.minimum()`? — `np.min()` khác `np.minimum()` thế nào?**

A. `np.minimum` sorts values before selecting one element — `np.minimum` sắp xếp rồi chọn một phần tử

B. min reduces values; minimum compares values element-wise — min tổng hợp lấy cực tiểu; minimum so từng phần tử

C. `np.min` compares each pair elementwise — `np.min` so sánh từng cặp phần tử

D. Both functions always return scalar values — Cả hai hàm luôn trả vô hướng

**Q15. For shape `(2,3)`, what is the shape of `sum(axis=1)`? — Với shape `(2,3)`, `sum(axis=1)` có shape nào?**

A. `(1,3)` — `(1,3)`

B. `(2,)` — `(2,)`

C. `(3,)` — `(3,)`

D. `(2,3)` — `(2,3)`

**Q16. For shape `(2,3)`, what is the shape of `mean(axis=0)`? — Với shape `(2,3)`, `mean(axis=0)` có shape nào?**

A. `(2,3)` — `(2,3)`

B. `(3,2)` — `(3,2)`

C. `(3,)` — `(3,)`

D. `(2,)` — `(2,)`

**Q17. Which expression adds a distinct offset to each column of a `(2,3)` matrix? — Biểu thức nào cộng một giá trị riêng cho mỗi cột của ma trận (2,3)?**

A. `X + np.array([1, 2])` — `X + np.array([1, 2])`

B. `X @ np.array([1, 2, 3])` — `X @ np.array([1, 2, 3])`

C. `X.shape + 1` — `X.shape + 1`

D. `X + np.array([1,2,3])` — `X + np.array([1,2,3])`

**Q18. Which statement about broadcasting is correct? — Phát biểu nào đúng về broadcasting?**

A. It may apply a smaller operand without physically copying it — Nó có thể áp toán hạng nhỏ mà không cần sao chép vật lý

B. It always duplicates the smaller operand before calculation — Nó luôn sao chép toán hạng nhỏ trước khi tính

C. It only works after manually expanding shapes with loops — Nó chỉ chạy sau khi mở shape thủ công bằng vòng lặp

D. It guarantees no output array will be allocated — Nó bảo đảm không cấp phát mảng kết quả

**Q19. How do aggregation and vectorization differ? — Aggregation khác vectorization thế nào?**

A. Aggregation summarizes values; vectorization operates over arrays — Aggregation tổng hợp giá trị; vectorization tính trực tiếp trên mảng

B. Aggregation always returns a sorted list — Tổng hợp luôn trả List đã sắp

C. Vectorization always reduces to one scalar — Vector hóa luôn gộp thành một vô hướng

D. Aggregation and vectorization are identical terms — Tổng hợp và vector hóa là hai thuật ngữ giống hệt

**Q20. Why should data meaning be known before choosing `axis`? — Vì sao phải hiểu ý nghĩa dữ liệu trước khi chọn `axis`?**

A. Naming rows and columns changes the numerical dtype — Đặt tên hàng và cột làm đổi dtype số

B. It determines whether rows or columns answer the question — Nó quyết định cần tổng hợp theo hàng hay cột

C. `axis` always refers to subjects regardless of layout — `axis` luôn chỉ môn học bất kể cách xếp dữ liệu

D. `axis` must be 0 for every aggregation — `axis` phải bằng 0 cho mọi phép tổng hợp

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **D** | Aggregation combines multiple array values into summaries, such as a sum, mean or maximum. For `[2,4,6]`, `mean` is 4, whereas a vectorized elementwise operation may retain three values. | Aggregation tổng hợp nhiều giá trị mảng thành kết quả tóm tắt như tổng, trung bình hoặc cực đại. Với `[2,4,6]`, trung bình bằng 4; phép toán theo từng phần tử có thể vẫn giữ ba giá trị. |
| Q2 | **C** | `sum()` adds all included values, whereas `mean()` divides that total by the number of included entries. For `[2,4,6]`, sum is 12 and mean is `12/3=4`; they answer different questions. | `sum()` cộng các giá trị được xét, còn `mean()` chia tổng cho số phần tử được xét. Với `[2,4,6]`, tổng là 12 và trung bình bằng `12/3=4`; hai phép trả lời mục đích khác nhau. |
| Q3 | **C** | `max()` finds the greatest value in the selected group or along an axis. For `[3,9,5]`, it returns 9, not the sum 17 or arithmetic average. | `max()` lấy giá trị lớn nhất trong nhóm được chọn hoặc theo một trục. Với `[3,9,5]`, nó cho 9, không phải tổng 17 hay trung bình cộng. |
| Q4 | **C** | On a 2-D array, `sum(axis=0)` reduces rows and returns one sum per column. For `[[1,2],[3,4]]`, the output is `[4,6]`, not the row sums `[3,7]`. | Với mảng hai chiều, `sum(axis=0)` gộp các hàng và trả một tổng theo từng cột. Với `[[1,2],[3,4]]`, đầu ra `[4,6]`, không phải tổng từng hàng `[3,7]`. |
| Q5 | **D** | On a 2-D array, `sum(axis=1)` adds across columns within each row. For `[[1,2],[3,4]]`, it returns `[3,7]`; `axis=0` would instead return `[4,6]`. | Với mảng hai chiều, `sum(axis=1)` cộng qua các cột trên từng hàng. Với `[[1,2],[3,4]]`, kết quả `[3,7]`; còn `axis=0` sẽ cho `[4,6]`. |
| Q6 | **B** | Broadcasting allows elementwise operations on arrays whose shapes align by NumPy's compatibility rules. Dimensions are compared from the right; two are compatible if equal or either equals one. | Broadcasting cho phép phép toán theo phần tử trên các mảng có shape phù hợp quy tắc NumPy. Các chiều được đối chiếu từ phải sang trái; hai chiều tương thích khi bằng nhau hoặc một bên bằng một. |
| Q7 | **A** | A scalar has no array axes and can broadcast against a numeric array. Thus `np.array([1,2]) + 1` produces `[2,3]` by adding one to each element, without a Python `for` loop. | Vô hướng không có trục mảng và có thể broadcast với mảng số. Vì vậy `np.array([1,2]) + 1` tạo `[2,3]` bằng cách cộng một cho từng phần tử mà không cần vòng `for` Python. |
| Q8 | **A** | Broadcasting checks dimensions from the right: sizes match when equal or one is one. For example trailing sizes 3 and 1 work, whereas 2 and 3 cannot match without another compatible dimension. | Broadcasting xét các chiều từ bên phải: kích thước hợp lệ nếu bằng nhau hoặc có một bên bằng 1. Ví dụ kích thước cuối 3 và 1 dùng được, còn 2 và 3 không ghép trực tiếp được. |
| Q9 | **A** | Incompatible shapes cannot align for ordinary elementwise operations, and NumPy typically raises `ValueError`. For example shapes `(2,3)` and `(2,)` conflict at their trailing dimensions 3 and 2. | Các shape không tương thích không thể ghép cho phép toán theo phần tử thông thường, và NumPy thường gây `ValueError`. Ví dụ `(2,3)` và `(2,)` xung đột ở chiều cuối 3 so với 2. |
| Q10 | **D** | Vectorization expresses numerical calculations directly over arrays, often avoiding explicit loops in user Python code. For example `a*2` scales every element of an ndarray, whereas a `for` loop could calculate the same results item by item. | Vectorization diễn đạt phép tính trực tiếp trên mảng, thường không cần tự viết vòng lặp Python. Ví dụ `a*2` nhân đôi từng phần tử ndarray, còn vòng `for` có thể tính tương tự từng phần tử. |
| Q11 | **C** | For equal-shaped numerical ndarrays, `a*b` multiplies corresponding elements, not matrices. If `a=[1,2]` and `b=[3,4]`, the result is `[3,8]`; matrix multiplication uses `@` when dimensions allow. | Với hai ndarray số cùng shape, `a*b` nhân từng cặp phần tử, không phải nhân ma trận. Nếu `a=[1,2]` và `b=[3,4]`, kết quả `[3,8]`; nhân ma trận dùng `@` khi các chiều phù hợp. |
| Q12 | **D** | The `@` operator performs matrix multiplication according to linear-algebra dimension rules. Unlike `*`, it combines rows and columns; a `(2,3)` matrix multiplied by a `(3,4)` matrix produces shape `(2,4)`. | Toán tử `@` thực hiện nhân ma trận theo quy tắc chiều của đại số tuyến tính. Khác `*`, phép này kết hợp hàng và cột; ma trận `(2,3)` nhân `(3,4)` cho shape `(2,4)`. |
| Q13 | **B** | `np.minimum(a,10)` takes the smaller value at each element, effectively capping numbers above 10. For `a=[7,12]`, it returns `[7,10]`, which is not the single minimum of the whole array. | `np.minimum(a,10)` lấy giá trị nhỏ hơn theo từng phần tử, tức chặn các số lớn hơn 10. Với `a=[7,12]`, kết quả `[7,10]`, không phải một cực tiểu chung của toàn mảng. |
| Q14 | **B** | `np.min(a)` aggregates values by finding a minimum, often returning a scalar when no axis is given. `np.minimum(a,b)` compares matching or broadcastable elements and returns elementwise results. | `np.min(a)` tổng hợp bằng cách lấy cực tiểu, thường trả một số nếu không nêu axis. `np.minimum(a,b)` so sánh từng cặp phần tử tương ứng hoặc broadcast được và trả kết quả theo phần tử. |
| Q15 | **B** | With input shape `(2,3)`, `sum(axis=1)` reduces the three columns within each of the two rows. One sum per row remains, giving a one-dimensional output shape `(2,)`, unless `keepdims=True` is requested. | Với đầu vào shape `(2,3)`, `sum(axis=1)` gộp ba cột ở mỗi một trong hai hàng. Mỗi hàng còn một tổng nên shape đầu ra là `(2,)`, trừ khi yêu cầu `keepdims=True`. |
| Q16 | **C** | For `(2,3)`, `mean(axis=0)` reduces the two rows for each of three columns. Three means remain, so the result shape is `(3,)`; `axis=1` would instead leave two means. | Với `(2,3)`, `mean(axis=0)` gộp hai hàng ở mỗi một trong ba cột. Còn ba trung bình nên shape kết quả `(3,)`; nếu dùng `axis=1` sẽ còn hai trung bình. |
| Q17 | **D** | `X+np.array([1,2,3])` broadcasts a length-three vector across both rows of a `(2,3)` array. Each column receives its own offset, unlike a length-two vector whose trailing dimension does not match three columns. | `X+np.array([1,2,3])` broadcast vector ba phần tử qua cả hai hàng của mảng `(2,3)`. Mỗi cột nhận độ lệch riêng, khác vector dài hai không khớp chiều cuối gồm ba cột. |
| Q18 | **A** | Broadcasting often acts as a virtual expansion instead of physically copying a smaller operand into a large array first. It may still allocate a result array; virtual broadcasting does not guarantee the whole operation uses no extra memory. | Broadcasting thường hoạt động như mở rộng ảo thay vì sao chép sẵn toán hạng nhỏ thành mảng lớn. Phép toán vẫn có thể cấp phát mảng kết quả; mở rộng ảo không bảo đảm không tốn thêm bộ nhớ. |
| Q19 | **A** | Aggregation reduces groups into summaries, often removing an axis, while vectorization applies operations across arrays without writing per-item Python loops. A vectorized sum can perform aggregation, so these ideas are related but not identical. | Aggregation gom nhóm thành kết quả tóm tắt, thường giảm số chiều, còn vectorization thực hiện phép toán trên mảng mà không tự viết vòng Python cho mỗi phần tử. Phép sum vector hóa có thể là tổng hợp nên hai khái niệm liên hệ nhưng không đồng nghĩa. |
| Q20 | **B** | The meaning of `axis` depends on what rows and columns represent. If rows are learners and columns subjects, `mean(axis=0)` averages each subject across learners; confusing the axes would answer a different question. | Ý nghĩa `axis` phụ thuộc hàng và cột biểu diễn gì. Nếu hàng là học viên và cột là môn, `mean(axis=0)` tính điểm trung bình từng môn qua học viên; nhầm trục sẽ trả lời một câu hỏi khác. |

## 8. Nối bài tiếp theo

`Index/Slice → Aggregate/Broadcast → Vectorization → AI`.
