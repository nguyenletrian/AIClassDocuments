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

A. Reading every file in a folder — Đọc mọi file trong thư mục

B. Converting all arrays to strings — Đổi mọi mảng thành chuỗi

C. Creating a new class by inheritance — Tạo lớp con nhờ kế thừa

D. Combining multiple values into summary statistics — Kết hợp nhiều giá trị thành thống kê tổng hợp

**Q2. How does `sum()` differ from `mean()`? — `sum()` khác `mean()` ra sao?**

A. Both always return the same result — Cả hai luôn bằng nhau

B. sum totals values; mean computes their average — sum cộng tổng; mean tính trung bình

C. sum sorts; mean deletes values — sum sắp xếp; mean xóa giá trị

D. mean returns the largest number — mean trả số lớn nhất

**Q3. What does `max()` return? — `max()` trả về gì?**

A. The arithmetic average — Trung bình cộng

B. The sum of every negative value — Tổng các số âm

C. The largest value overall or along a specified axis — Giá trị lớn nhất toàn mảng hoặc theo trục được chỉ định

D. The number of columns only — Chỉ số cột

**Q4. In a 2-D array, what does `sum(axis=0)` return? — Trong mảng hai chiều, `sum(axis=0)` trả về gì?**

A. One sum per row — Một tổng cho mỗi hàng

B. One sum per column — Một tổng cho mỗi cột

C. Only the first row — Chỉ hàng đầu

D. A boolean mask — Mặt nạ Boolean

**Q5. In a 2-D array, what does `sum(axis=1)` return? — Trong mảng hai chiều, `sum(axis=1)` trả về gì?**

A. The data type of values — Kiểu dữ liệu

B. One sum per column — Một tổng cho mỗi cột

C. Only a scalar index — Chỉ một chỉ số

D. One sum per row — Một tổng cho mỗi hàng

**Q6. What does broadcasting allow? — Broadcasting cho phép làm gì?**

A. Automatically converting all arrays to CSV — Tự chuyển mọi mảng thành CSV

B. Operating on arrays with compatible shapes — Thực hiện phép toán trên các mảng có shape tương thích

C. Replacing a function with a class — Thay hàm bằng lớp

D. Using any shapes without restrictions — Dùng mọi shape không giới hạn

**Q7. Why does `a + 1` work on a numeric ndarray? — Vì sao `a + 1` hoạt động với ndarray số?**

A. The array is converted to a string — Mảng bị chuyển thành chuỗi

B. Only the first element is changed — Chỉ phần tử đầu thay đổi

C. The scalar broadcasts to every array element — Số 1 được broadcast tới từng phần tử

D. It performs matrix multiplication — Nó nhân ma trận

**Q8. Which pair of trailing dimensions is broadcast-compatible? — Hai chiều cuối nào tương thích broadcasting?**

A. Only both zero — Chỉ khi cùng bằng 0

B. Equal sizes or one size equal to 1 — Bằng nhau hoặc một chiều có kích thước 1

C. Always 2 and 3 — Luôn là 2 và 3

D. Any unrelated positive sizes — Hai số dương bất kỳ

**Q9. What happens for incompatible broadcast shapes? — Điều gì xảy ra khi hai shape không tương thích broadcasting?**

A. A ValueError is generally raised — Thường phát sinh ValueError

B. NumPy always returns None — NumPy luôn trả None

C. NumPy silently discards extra rows — NumPy tự bỏ hàng thừa

D. A CSV file is created — Một file CSV được tạo

**Q10. What is vectorization? — Vectorization là gì?**

A. Removing all calculations — Loại bỏ mọi phép tính

B. Applying numerical operations to arrays directly — Áp dụng phép toán số trực tiếp lên mảng

C. Turning every number into a set — Biến mọi số thành Set

D. Manually printing each item — Tự in từng phần tử

**Q11. What does NumPy `a * b` do for equal-shaped numeric arrays? — NumPy `a * b` làm gì với hai mảng số cùng shape?**

A. Multiply corresponding elements — Nhân các phần tử cùng vị trí

B. Concatenate the arrays — Nối hai mảng

C. Always compute matrix multiplication — Luôn nhân ma trận

D. Compare the shapes only — Chỉ so sánh shape

**Q12. Which operator is used for matrix multiplication? — Toán tử nào dùng để nhân ma trận?**

A. `and` — `and`

B. `%` — `%`

C. `@` — `@`

D. `*` alone — Chỉ `*`

**Q13. For finite numeric array values, what does `np.minimum(a, 10)` do? — Với mảng chứa các giá trị số hữu hạn, `np.minimum(a, 10)` làm gì?**

A. Sum all values and multiply by 10 — Cộng tổng rồi nhân 10

B. Select the largest value only — Chỉ chọn số lớn nhất

C. Remove every element below 10 — Xóa mọi phần tử dưới 10

D. Cap each value at 10 — Giới hạn mỗi giá trị tối đa 10

**Q14. How does `np.min()` differ from `np.minimum()`? — `np.min()` khác `np.minimum()` thế nào?**

A. min performs sorting descending — min sắp xếp giảm dần

B. Both always return the same shape — Cả hai luôn trả cùng shape

C. min reduces values; minimum compares values element-wise — min tổng hợp lấy cực tiểu; minimum so từng phần tử

D. minimum reads files; min writes files — minimum đọc file, min ghi file

**Q15. For shape `(2,3)`, what is the shape of `sum(axis=1)`? — Với shape `(2,3)`, `sum(axis=1)` có shape nào?**

A. `(2,3)` — `(2,3)`

B. `(1,3)` — `(1,3)`

C. `(3,)` — `(3,)`

D. `(2,)` — `(2,)`

**Q16. For shape `(2,3)`, what is the shape of `mean(axis=0)`? — Với shape `(2,3)`, `mean(axis=0)` có shape nào?**

A. `(3,2)` — `(3,2)`

B. `(2,3)` — `(2,3)`

C. `(2,)` — `(2,)`

D. `(3,)` — `(3,)`

**Q17. Which expression adds a distinct offset to each column of a `(2,3)` matrix? — Biểu thức nào cộng một giá trị riêng cho mỗi cột của ma trận (2,3)?**

A. `X + np.array([1,2,3])` — `X + np.array([1,2,3])`

B. `X.shape + 1` — `X.shape + 1`

C. `X @ np.array([1,2,3])` — `X @ np.array([1,2,3])`

D. `X + np.array([1,2])` — `X + np.array([1,2])`

**Q18. Which statement about broadcasting is correct? — Phát biểu nào đúng về broadcasting?**

A. It may apply a smaller operand without physically copying it — Nó có thể áp toán hạng nhỏ mà không cần sao chép vật lý

B. It permanently changes the array shape in every case — Nó luôn thay shape vĩnh viễn

C. It always duplicates the entire array in memory first — Nó luôn sao chép toàn mảng trước

D. It requires writing explicit for loops — Nó bắt buộc viết vòng for

**Q19. How do aggregation and vectorization differ? — Aggregation khác vectorization thế nào?**

A. Aggregation summarizes values; vectorization operates over arrays — Aggregation tổng hợp giá trị; vectorization tính trực tiếp trên mảng

B. Both mean sorting only — Cả hai chỉ là sắp xếp

C. Aggregation never uses NumPy — Aggregation không bao giờ dùng NumPy

D. Vectorization must reduce to one number — Vectorization luôn phải trả một số

**Q20. Why should data meaning be known before choosing `axis`? — Vì sao phải hiểu ý nghĩa dữ liệu trước khi chọn `axis`?**

A. It avoids specifying array shape — Nó giúp khỏi nêu shape

B. It ensures every value is positive — Nó bảo đảm mọi giá trị dương

C. It determines whether rows or columns answer the question — Nó quyết định cần tổng hợp theo hàng hay cột

D. It changes Python syntax rules — Nó đổi quy tắc cú pháp Python

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **D** | Aggregation summarizes several numeric values into a statistic, such as `sum`, `mean`, or `max`. For `[2, 4, 6]`, a mean of `4` summarizes three values rather than preserving every entry. | Tổng hợp gộp nhiều giá trị số thành thống kê như `sum`, `mean` hoặc `max`. Với `[2, 4, 6]`, trung bình `4` tóm tắt ba giá trị thay vì giữ từng ô. |
| Q2 | **B** | `sum` adds all selected values, whereas `mean` divides that sum by the number of values. For `[2, 4, 6]`, the sum is `12` but the mean is `4`; they are not generally equal. | `sum` cộng tất cả giá trị được chọn, còn `mean` lấy tổng chia cho số giá trị. Với `[2, 4, 6]`, tổng bằng `12` nhưng trung bình bằng `4`; hai phép không thường bằng nhau. |
| Q3 | **C** | `max` selects the greatest value from an array, or separately along an axis if one is provided. For `[[1, 7], [5, 3]]`, the overall maximum is `7`, unlike `mean`, which computes an average. | `max` chọn giá trị lớn nhất của mảng hoặc riêng theo trục được chỉ định. Với `[[1, 7], [5, 3]]`, cực đại toàn mảng là `7`, khác `mean` dùng để tính trung bình. |
| Q4 | **B** | For a 2-D array, `axis=0` collapses rows while retaining one result per column. With `[[1, 2], [3, 4]]`, the column sums are `[4, 6]`, not row sums `[3, 7]`. | Với mảng 2D, `axis=0` gộp theo chiều hàng và để lại mỗi cột một kết quả. Với `[[1, 2], [3, 4]]`, tổng cột là `[4, 6]`, không phải tổng hàng `[3, 7]`. |
| Q5 | **D** | `axis=1` combines columns within each row. For `[[1, 2], [3, 4]]`, `sum(axis=1)` gives row totals `[3, 7]`; `axis=0` instead produces one total per column. | `axis=1` gộp các cột trong từng hàng. Với `[[1, 2], [3, 4]]`, `sum(axis=1)` cho tổng hàng `[3, 7]`; `axis=0` lại cho tổng theo cột. |
| Q6 | **B** | Broadcasting aligns dimensions of compatible shapes for element-wise operations without requiring explicit Python loops. For instance, a `(2,3)` matrix can add a `(3,)` vector across its rows, but a `(2,)` vector is incompatible with its trailing dimension 3. | Broadcasting ghép các chiều có kích thước tương thích để tính theo phần tử mà không phải viết vòng lặp Python. Ví dụ ma trận `(2,3)` cộng được vector `(3,)` trên các hàng, nhưng vector `(2,)` không khớp chiều cuối bằng 3. |
| Q7 | **C** | A scalar has no array axes to conflict with the numeric array, so NumPy broadcasts its value across all elements. For `a=[2,4]`, `a + 1` produces `[3,5]`, not matrix multiplication or a change to only the first item. | Số đơn không có trục mảng gây xung đột nên NumPy broadcast nó tới mọi phần tử. Với `a=[2,4]`, `a + 1` cho `[3,5]`, không phải nhân ma trận hay chỉ sửa phần tử đầu. |
| Q8 | **B** | NumPy compares aligned dimensions from right to left: each pair must match or one size must be `1`. Thus sizes `3` and `1` can broadcast, while `3` and `2` on the same axis generally cannot. | NumPy đối chiếu các chiều từ phải sang trái: mỗi cặp phải bằng nhau hoặc một bên có kích thước `1`. Vì vậy chiều `3` và `1` tương thích, còn `3` và `2` trên cùng trục thường không tương thích. |
| Q9 | **A** | Incompatible shapes cannot be aligned for an element-wise operation, so NumPy normally raises `ValueError`. For example, adding shape `(2,3)` to `(2,)` fails because the trailing dimensions 3 and 2 differ. | Shape không tương thích không thể ghép cho phép toán theo phần tử, nên NumPy thường gây `ValueError`. Ví dụ cộng `(2,3)` với `(2,)` lỗi vì hai chiều cuối 3 và 2 không khớp. |
| Q10 | **B** | Vectorization applies operations directly to NumPy arrays rather than writing a Python loop over every element. For instance, `a * 2` multiplies all numeric elements, while aggregation such as `a.sum()` reduces them to a summary. | Vector hóa áp dụng phép toán trực tiếp trên mảng NumPy thay vì viết vòng lặp Python qua từng phần tử. Ví dụ `a * 2` nhân mọi ô số, còn tổng hợp như `a.sum()` gộp chúng thành một thống kê. |
| Q11 | **A** | For NumPy numeric arrays, `*` multiplies corresponding entries with broadcasting when needed. Thus `[2,3] * [4,5]` element-wise gives `[8,15]`; matrix multiplication uses `@` instead. | Với mảng số NumPy, `*` nhân các ô tương ứng và có thể dùng broadcasting. Vì vậy hai mảng `[2,3]` và `[4,5]` nhân theo phần tử cho `[8,15]`; phép nhân ma trận dùng `@`. |
| Q12 | **C** | The `@` operator performs matrix multiplication, combining rows and columns according to linear-algebra rules. Unlike `*`, it does not simply multiply each pair of same-position entries. | Toán tử `@` thực hiện nhân ma trận theo quy tắc đại số tuyến tính, kết hợp hàng với cột. Khác `*`, nó không chỉ nhân các phần tử ở cùng vị trí. |
| Q13 | **D** | For finite numeric values, `np.minimum(a, 10)` compares each entry with 10 and keeps the smaller one. Thus `[8,12]` becomes `[8,10]`; it does not discard the entry below 10. | Với giá trị số hữu hạn, `np.minimum(a, 10)` so từng ô với 10 rồi lấy số nhỏ hơn. Vì vậy `[8,12]` thành `[8,10]`; nó không xóa phần tử nhỏ hơn 10. |
| Q14 | **C** | `np.min(a)` reduces many values to one minimum by default, or to minima along a chosen axis. `np.minimum(a,b)` compares corresponding entries element-wise using broadcasting, usually preserving an array-shaped result. | `np.min(a)` mặc định gộp nhiều giá trị thành một cực tiểu, hoặc lấy cực tiểu theo trục được chọn. `np.minimum(a,b)` so từng ô tương ứng có thể dùng broadcasting và thường trả mảng kết quả. |
| Q15 | **D** | A matrix with shape `(2,3)` has two rows, each containing three values. `sum(axis=1)` collapses those three columns within each row, leaving two totals and shape `(2,)`. | Ma trận shape `(2,3)` có hai hàng, mỗi hàng gồm ba số. `sum(axis=1)` cộng ba cột trong từng hàng, để lại hai tổng với shape `(2,)`. |
| Q16 | **D** | For a `(2,3)` array, `mean(axis=0)` averages across the two rows independently for each column. Three column means remain, so its default result shape is `(3,)`, not `(2,)`. | Với mảng `(2,3)`, `mean(axis=0)` lấy trung bình qua hai hàng cho từng cột. Còn lại ba trung bình cột, nên shape kết quả mặc định là `(3,)`, không phải `(2,)`. |
| Q17 | **A** | A length-three offset vector matches the trailing column dimension of a `(2,3)` matrix. Broadcasting adds `[1,2,3]` to both rows, assigning a distinct offset to each column; length two does not align with dimension three. | Vector bù dài ba khớp chiều cuối gồm ba cột của ma trận `(2,3)`. Broadcasting cộng `[1,2,3]` vào cả hai hàng, mỗi cột một mức riêng; vector dài hai không khớp chiều ba. |
| Q18 | **A** | Broadcasting can logically reuse a smaller operand across compatible dimensions without physically duplicating all its data first. This differs from requiring a manual loop or permanently changing the input's shape. | Broadcasting có thể tái sử dụng toán hạng nhỏ trên các chiều tương thích mà không cần nhân bản vật lý toàn bộ dữ liệu trước. Nó khác việc phải viết vòng lặp hoặc đổi shape của đầu vào vĩnh viễn. |
| Q19 | **A** | Aggregation combines values into summaries, often reducing an axis, while vectorized operations apply computations over many entries directly. For example, `a.mean()` summarizes values whereas `a * 2` transforms each entry. | Tổng hợp gộp các giá trị thành thống kê, thường giảm một trục, còn phép toán vector hóa tính trực tiếp trên nhiều ô. Ví dụ `a.mean()` tóm tắt dữ liệu, còn `a * 2` biến đổi từng phần tử. |
| Q20 | **C** | The correct axis depends on what each row and column represents. If rows denote learners and columns subjects, `mean(axis=0)` averages each subject across learners, while `mean(axis=1)` averages each learner across subjects. | Chọn trục đúng phụ thuộc ý nghĩa hàng và cột. Nếu hàng là học viên, cột là môn, `mean(axis=0)` tính trung bình từng môn qua học viên, còn `mean(axis=1)` tính trung bình các môn của mỗi học viên. |

## 8. Nối bài tiếp theo

`Index/Slice → Aggregate/Broadcast → Vectorization → AI`.
