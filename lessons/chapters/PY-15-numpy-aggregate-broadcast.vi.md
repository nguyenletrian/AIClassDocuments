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

A. Combining multiple values into summary statistics — Kết hợp nhiều giá trị thành thống kê tổng hợp

B. Creating a new class by inheritance — Tạo lớp con nhờ kế thừa

C. Reading every file in a folder — Đọc mọi file trong thư mục

D. Converting all arrays to strings — Đổi mọi mảng thành chuỗi

**Q2. How does `sum()` differ from `mean()`? — `sum()` khác `mean()` ra sao?**

A. mean returns the largest number — mean trả số lớn nhất

B. sum totals values; mean computes their average — sum cộng tổng; mean tính trung bình

C. sum sorts; mean deletes values — sum sắp xếp; mean xóa giá trị

D. Both always return the same result — Cả hai luôn bằng nhau

**Q3. What does `max()` return? — `max()` trả về gì?**

A. The number of columns only — Chỉ số cột

B. The sum of every negative value — Tổng các số âm

C. The largest value along the chosen axis — Giá trị lớn nhất theo trục đã chọn

D. The arithmetic average — Trung bình cộng

**Q4. In a 2-D array, what does `sum(axis=0)` return? — Trong mảng hai chiều, `sum(axis=0)` trả về gì?**

A. One sum per row — Một tổng cho mỗi hàng

B. Only the first row — Chỉ hàng đầu

C. A boolean mask — Mặt nạ Boolean

D. One sum per column — Một tổng cho mỗi cột

**Q5. In a 2-D array, what does `sum(axis=1)` return? — Trong mảng hai chiều, `sum(axis=1)` trả về gì?**

A. One sum per row — Một tổng cho mỗi hàng

B. One sum per column — Một tổng cho mỗi cột

C. Only a scalar index — Chỉ một chỉ số

D. The data type of values — Kiểu dữ liệu

**Q6. What does broadcasting allow? — Broadcasting cho phép làm gì?**

A. Replacing a function with a class — Thay hàm bằng lớp

B. Operating on arrays with compatible shapes — Thực hiện phép toán trên các mảng có shape tương thích

C. Using any shapes without restrictions — Dùng mọi shape không giới hạn

D. Automatically converting all arrays to CSV — Tự chuyển mọi mảng thành CSV

**Q7. Why does `a + 1` work on a numeric ndarray? — Vì sao `a + 1` hoạt động với ndarray số?**

A. Only the first element is changed — Chỉ phần tử đầu thay đổi

B. It performs matrix multiplication — Nó nhân ma trận

C. The scalar broadcasts to every array element — Số 1 được broadcast tới từng phần tử

D. The array is converted to a string — Mảng bị chuyển thành chuỗi

**Q8. Which pair of trailing dimensions is broadcast-compatible? — Hai chiều cuối nào tương thích broadcasting?**

A. Only both zero — Chỉ khi cùng bằng 0

B. Always 2 and 3 — Luôn là 2 và 3

C. Any unrelated positive sizes — Hai số dương bất kỳ

D. Equal sizes or one size equal to 1 — Bằng nhau hoặc một chiều có kích thước 1

**Q9. What happens for incompatible broadcast shapes? — Điều gì xảy ra khi hai shape không tương thích broadcasting?**

A. A ValueError is generally raised — Thường phát sinh ValueError

B. NumPy silently discards extra rows — NumPy tự bỏ hàng thừa

C. NumPy always returns None — NumPy luôn trả None

D. A CSV file is created — Một file CSV được tạo

**Q10. What is vectorization? — Vectorization là gì?**

A. Removing all calculations — Loại bỏ mọi phép tính

B. Applying numerical operations to arrays directly — Áp dụng phép toán số trực tiếp lên mảng

C. Manually printing each item — Tự in từng phần tử

D. Turning every number into a set — Biến mọi số thành Set

**Q11. What does NumPy `a * b` do for equal-shaped numeric arrays? — NumPy `a * b` làm gì với hai mảng số cùng shape?**

A. Concatenate the arrays — Nối hai mảng

B. Compare the shapes only — Chỉ so sánh shape

C. Multiply corresponding elements — Nhân các phần tử cùng vị trí

D. Always compute matrix multiplication — Luôn nhân ma trận

**Q12. Which operator is used for matrix multiplication? — Toán tử nào dùng để nhân ma trận?**

A. `*` alone — Chỉ `*`

B. `and` — `and`

C. `%` — `%`

D. `@` — `@`

**Q13. What does `np.minimum(a, 10)` do? — `np.minimum(a, 10)` có tác dụng gì?**

A. Cap each value at 10 — Giới hạn mỗi giá trị tối đa 10

B. Select the largest value only — Chỉ chọn số lớn nhất

C. Sum all values and multiply by 10 — Cộng tổng rồi nhân 10

D. Remove every element below 10 — Xóa mọi phần tử dưới 10

**Q14. How does `np.min()` differ from `np.minimum()`? — `np.min()` khác `np.minimum()` thế nào?**

A. min performs sorting descending — min sắp xếp giảm dần

B. min reduces values; minimum compares values element-wise — min tổng hợp lấy cực tiểu; minimum so từng phần tử

C. Both always return the same shape — Cả hai luôn trả cùng shape

D. minimum reads files; min writes files — minimum đọc file, min ghi file

**Q15. For shape `(2,3)`, what is the shape of `sum(axis=1)`? — Với shape `(2,3)`, `sum(axis=1)` có shape nào?**

A. `(2,3)` — `(2,3)`

B. `(1,3)` — `(1,3)`

C. `(2,)` — `(2,)`

D. `(3,)` — `(3,)`

**Q16. For shape `(2,3)`, what is the shape of `mean(axis=0)`? — Với shape `(2,3)`, `mean(axis=0)` có shape nào?**

A. `(2,)` — `(2,)`

B. `(2,3)` — `(2,3)`

C. `(3,2)` — `(3,2)`

D. `(3,)` — `(3,)`

**Q17. Which expression adds a distinct offset to each column of a `(2,3)` matrix? — Biểu thức nào cộng một giá trị riêng cho mỗi cột của ma trận (2,3)?**

A. `X + np.array([1,2,3])` — `X + np.array([1,2,3])`

B. `X + np.array([1,2])` — `X + np.array([1,2])`

C. `X @ np.array([1,2,3])` — `X @ np.array([1,2,3])`

D. `X.shape + 1` — `X.shape + 1`

**Q18. Which statement about broadcasting is correct? — Phát biểu nào đúng về broadcasting?**

A. It requires writing explicit for loops — Nó bắt buộc viết vòng for

B. It may apply a smaller operand without physically copying it — Nó có thể áp toán hạng nhỏ mà không cần sao chép vật lý

C. It always duplicates the entire array in memory first — Nó luôn sao chép toàn mảng trước

D. It permanently changes the array shape in every case — Nó luôn thay shape vĩnh viễn

**Q19. How do aggregation and vectorization differ? — Aggregation khác vectorization thế nào?**

A. Vectorization must reduce to one number — Vectorization luôn phải trả một số

B. Aggregation never uses NumPy — Aggregation không bao giờ dùng NumPy

C. Aggregation summarizes values; vectorization operates over arrays — Aggregation tổng hợp giá trị; vectorization tính trực tiếp trên mảng

D. Both mean sorting only — Cả hai chỉ là sắp xếp

**Q20. Why should data meaning be known before choosing `axis`? — Vì sao phải hiểu ý nghĩa dữ liệu trước khi chọn `axis`?**

A. It changes Python syntax rules — Nó đổi quy tắc cú pháp Python

B. It ensures every value is positive — Nó bảo đảm mọi giá trị dương

C. It avoids specifying array shape — Nó giúp khỏi nêu shape

D. It determines whether rows or columns answer the question — Nó quyết định cần tổng hợp theo hàng hay cột

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | Functions such as sum and mean summarize a group of numbers.~Hàm như sum và mean tóm tắt một nhóm giá trị số. | undefined |
| Q2 | **B** | A mean divides the sum by the number of included values.~Trung bình được tính bằng tổng chia số giá trị được tính. | undefined |
| Q3 | **C** | Maximum selects an extreme value, not a sum or mean.~Phép cực đại chọn giá trị lớn nhất, không phải tổng hay trung bình. | undefined |
| Q4 | **D** | Axis 0 reduces over rows, preserving the column dimension.~Axis 0 tổng hợp qua các hàng và giữ kết quả theo cột. | undefined |
| Q5 | **A** | Axis 1 reduces across columns of each row.~Axis 1 cộng các cột trên từng hàng. | undefined |
| Q6 | **B** | NumPy can virtually expand compatible dimensions during element-wise operations.~NumPy có thể mở rộng chiều tương thích khi tính theo phần tử. | undefined |
| Q7 | **C** | A scalar can be applied element-wise without a Python loop.~Số đơn được áp vào từng phần tử mà không cần vòng for Python. | undefined |
| Q8 | **D** | Broadcasting compares shapes from the right; dimensions are compatible if equal or one is 1.~Broadcasting xét các chiều từ phải sang trái; chiều tương thích khi bằng nhau hoặc một bên là 1. | undefined |
| Q9 | **A** | Element-wise operations need compatible dimensions to align values.~Tính theo phần tử cần các chiều có thể ghép tương thích. | undefined |
| Q10 | **B** | Array operations replace explicit per-element loops in user code.~Phép toán mảng thay cho vòng lặp Python phải viết cho từng phần tử. | undefined |
| Q11 | **C** | The star operator is element-wise multiplication for ndarrays.~Toán tử sao `*` nhân theo từng phần tử của ndarray. | undefined |
| Q12 | **D** | The @ operator follows matrix multiplication rules rather than element-wise multiplication.~Toán tử @ tuân theo quy tắc nhân ma trận, không phải nhân theo từng phần tử. | undefined |
| Q13 | **A** | It returns the smaller of each array value and the given scalar.~Hàm chọn số nhỏ hơn giữa từng phần tử và ngưỡng 10. | undefined |
| Q14 | **B** | np.min reduces along an axis; np.minimum performs element-wise comparisons.~np.min lấy giá trị nhỏ nhất qua một trục; np.minimum so sánh từng ô. | undefined |
| Q15 | **C** | Summing across three columns leaves one total per row, two totals overall.~Cộng qua ba cột còn một tổng mỗi hàng, tức hai tổng. | undefined |
| Q16 | **D** | Reducing the two rows leaves one mean for each of three columns.~Gộp hai hàng còn một trung bình cho mỗi ba cột. | undefined |
| Q17 | **A** | A length-three vector matches the three columns and broadcasts across both rows.~Vector dài 3 khớp ba cột và được áp lên cả hai hàng. | undefined |
| Q18 | **B** | Broadcasting describes compatible virtual expansion for operations.~Broadcasting mô tả việc mở rộng logic các chiều tương thích khi tính toán. | undefined |
| Q19 | **C** | Vectorized operations often preserve shapes, whereas aggregates may reduce dimensions.~Tính vector hóa thường giữ kích thước, còn tổng hợp có thể giảm số chiều. | undefined |
| Q20 | **D** | The same array operation has a different interpretation for different row/column meanings.~Cùng phép tính mảng có thể mang ý nghĩa khác nhau tùy nội dung hàng/cột. | undefined |

## 8. Nối bài tiếp theo

`Index/Slice → Aggregate/Broadcast → Vectorization → AI`.
