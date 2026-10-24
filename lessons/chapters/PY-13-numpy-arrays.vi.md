# PY-13 — NumPy ndarray, shape, dtype và axis


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **ndarray** — mảng NumPy; **Shape** — kích thước mảng.

`List → NumPy Array → Matrix → PCA`

Sau List, ta chuyển sang NumPy để xử lý nhiều điểm hoặc số đo trong một mảng. Bài này giải thích cách đọc hàng, cột, kích thước, kiểu phần tử và trục tính toán trước khi dùng các phép xử lý dữ liệu cho AI.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| ndarray | mảng NumPy | Một mảng đồng nhất về kiểu phần tử |
| Shape | kích thước mảng | Số phần tử trên từng chiều |
| dtype | kiểu phần tử | Kiểu dữ liệu của giá trị trong mảng |
| Axis | trục tính toán | Chiều dọc theo phép tổng hợp |

## 3. Thư viện, hàm và tham số

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm/cú pháp | Giải thích và lý do dùng |
|---|---|
| `np.array(data,dtype=float)` | Tạo mảng số thực, dtype=float cho phép lưu phần thập phân |
| `X.shape/X.ndim/X.size` | Xem hàng/cột, số chiều, số phần tử |
| `X.mean(axis=0)` | Tính trung bình của từng CỘT từ các hàng |
| `np.zeros()/np.ones()` | Tạo dữ liệu số được khởi tạo rõ hình dạng |

## 4. Khái niệm liên quan

**NumPy ndarray** là công cụ lưu số liệu có cấu trúc. Một bảng có 3 học viên × 2 môn sẽ xuyên suốt phần khái niệm: từ tạo bảng, xem kích thước, hiểu kiểu phần tử cho tới tính toán theo cột. Nhờ giữ nguyên ý nghĩa hàng và cột, kết quả thống kê sẽ không bị hiểu nhầm.

### 4.1. ndarray — Mảng số cho nhiều học viên

**Từ vựng trong mục:** **ndarray** — mảng NumPy; **Element** — phần tử.

**NumPy** là thư viện hỗ trợ tính toán trên nhiều số cùng lúc. Kiểu dữ liệu chính là `ndarray` — một **mảng nhiều chiều**. Ví dụ trung tâm có ba học viên An, Bình, Lan (theo thứ tự ba hàng) và hai môn Toán, Python (theo thứ tự hai cột). Các điểm `[8,9]`, `[6,7]`, `[9,8]` nằm cùng một bảng. **Mỗi hàng** là một người, **mỗi cột** là một môn, **mỗi ô** là điểm của người đó ở môn đó trên thang 10.

```python
import numpy as np

scores = np.array([
    [8, 9],
    [6, 7],
    [9, 8],
])
print(scores)
```

**Kết quả khi chạy:**

```text
[[8 9]
 [6 7]
 [9 8]]
```

Hàng đầu là điểm của An, hàng thứ hai của Bình, hàng thứ ba của Lan; hai số trên một hàng lần lượt thuộc hai môn.

### 4.2. Shape — Kích thước của mảng

**Từ vựng trong mục:** **Shape** — kích thước; **Row/column** — hàng/cột.

Thuộc tính `shape` cho biết **số phần tử ở từng chiều** của mảng. Với bảng điểm ba học viên, hai môn, `shape == (3, 2)`: con số 3 là **số hàng/học viên**, con số 2 là **số cột/môn**. Thuộc tính `size` là số ô dữ liệu (3 × 2 = 6), còn `ndim` là số chiều (2). Không nhầm mảng `(3,2)` với ba môn của hai học viên.

```python
import numpy as np

scores = np.array([[8, 9], [6, 7], [9, 8]])
print(scores.shape, scores.size)
```

**Kết quả khi chạy:**

```text
(3, 2) 6
```

Bảng có 3 người × 2 môn = 6 giá trị điểm; đây là mảng hai chiều.

### 4.3. dtype — Kiểu của các phần tử

**Từ vựng trong mục:** **dtype** — kiểu dữ liệu phần tử; **Float** — số thực.

Một `ndarray` thông thường lưu các phần tử bằng một kiểu dữ liệu chung (`dtype`). Với điểm có phần thập phân như 8,5, ta dùng `dtype=float` khi tạo mảng để giữ phần lẻ và thuận tiện tính trung bình. NumPy trên môi trường thông dụng dùng `float64` cho lựa chọn `float`. Ngược lại, nếu ép điểm thập phân thành số nguyên, phần lẻ có thể mất.

```python
import numpy as np

scores = np.array([8.5, 7.0], dtype=float)
print(scores.dtype, scores.size)
```

**Kết quả khi chạy:**

```text
float64 2
```

Mảng có hai điểm dạng số thực; `8.5` được giữ chứ không bị cắt thành `8`.

### 4.4. Axis — Tính theo hàng hoặc cột

**Từ vựng trong mục:** **Axis** — trục tính toán; **Mean** — trung bình.

Khi tổng hợp dữ liệu hai chiều, **`axis=0` gom các hàng để cho ra một kết quả trên mỗi cột**; **`axis=1` gom các cột để cho ra một kết quả trên mỗi hàng**. Trong bảng ba học viên × hai môn, `scores.mean(axis=0)` tính điểm trung bình **từng môn**: môn Toán `(8+6+9)/3 ≈ 7,67`, môn Python `(9+7+8)/3 = 8`. Nếu đổi sang `axis=1`, sẽ ra ba điểm trung bình tương ứng ba học viên.

```python
import numpy as np

scores = np.array([[8, 9], [6, 7], [9, 8]], dtype=float)
print(scores.mean(axis=0))
```

**Kết quả khi chạy:**

```text
[7.66666667 8.        ]
```

Mảng đầu ra có hai số vì bảng có hai **cột/môn**; kết quả lần lượt là trung bình Toán và Python.

## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Gom bảng điểm học viên

**Từ vựng trong mục:** **ndarray** — mảng NumPy; **Shape** — kích thước.

**Tình huống thực tế:** Trung tâm ghi điểm hai môn Toán và Python của ba học viên theo thứ tự An (8,9), Bình (6,7), Lan (9,8), thang điểm 10. Hãy tạo mảng và in số hàng, số cột.

**Vì sao chọn cách giải này?** `np.array` gom điểm thành bảng, `shape` cho biết đúng 3 học viên và 2 môn.

**Quy trình giải:**

1. Tạo mảng hai chiều, mỗi hàng ứng với một học viên.
2. Giữ thứ tự cột Toán rồi Python.
3. In `scores.shape` để xác minh số người và môn.

```python
import numpy as np

scores = np.array([[8, 9], [6, 7], [9, 8]], dtype=float)
print(scores.shape)
```

**Kết quả khi chạy:**

```text
(3, 2)
```

Kết quả cho biết 3 hàng học viên và 2 cột môn học.

### Tình huống 2 — Trung bình theo từng môn

**Từ vựng trong mục:** **Axis** — trục tính toán; **Mean** — trung bình.

**Tình huống thực tế:** Với cùng bảng ba học viên, hai môn Toán và Python, trung tâm cần điểm trung bình của **mỗi môn** trên thang 10. Hãy in hai số trung bình theo thứ tự cột.

**Vì sao chọn cách giải này?** `mean(axis=0)` gom các học viên cùng cột môn và tính trung bình.

**Quy trình giải:**

1. Tạo mảng 3 hàng × 2 cột theo thứ tự Toán, Python.
2. Tính `scores.mean(axis=0)`.
3. Đối chiếu hai số với phép tính trung bình ở từng cột.

```python
import numpy as np

scores = np.array([[8, 9], [6, 7], [9, 8]], dtype=float)
print(scores.mean(axis=0))
```

**Kết quả khi chạy:**

```text
[7.66666667 8.        ]
```

Toán trung bình khoảng 7,67; Python trung bình 8,00 điểm.

### Tình huống 3 — Tính tổng doanh thu mỗi cửa hàng

**Từ vựng trong mục:** **Axis** — trục tính toán; **Sum** — phép cộng tổng.

**Tình huống thực tế:** Cửa hàng A có doanh thu ba ngày `[10,20,30]`, cửa hàng B có `[8,12,16]`, đơn vị triệu đồng. Bảng có **hai hàng cửa hàng** và **ba cột ngày**. Hãy tính tổng doanh thu riêng của từng cửa hàng.

**Vì sao chọn cách giải này?** Vì cửa hàng nằm trên hàng, `sum(axis=1)` cộng ba cột ngày cho mỗi hàng.

**Quy trình giải:**

1. Tạo `sales` với hàng đầu là cửa hàng A và hàng sau là B.
2. Cộng theo `axis=1`, tức theo từng hàng.
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

Cửa hàng A thu 60 triệu đồng; cửa hàng B thu 36 triệu đồng.

### Tình huống 4 — Tạo bảng dự báo khởi tạo

**Từ vựng trong mục:** **Shape** — kích thước; **Zero array** — mảng số 0.

**Tình huống thực tế:** Đội phân tích chuẩn bị một bảng dự báo cho 2 cửa hàng và 3 ngày, chưa tính giá trị. Hãy tạo mảng toàn số 0 và in hình dạng bảng.

**Vì sao chọn cách giải này?** `np.zeros((2, 3))` khởi tạo đúng số hàng cửa hàng và số cột ngày; số 0 mới là giá trị ban đầu, không phải doanh thu dự báo đã xác minh.

**Quy trình giải:**

1. Gọi `np.zeros` với hình dạng `(2, 3)`.
2. Mỗi hàng dành cho một cửa hàng, mỗi cột dành cho một ngày.
3. In `forecast.shape` để kiểm tra cấu trúc.

```python
import numpy as np

forecast = np.zeros((2, 3))
print(forecast.shape)
```

**Kết quả khi chạy:**

```text
(2, 3)
```

Bảng dành cho hai cửa hàng, ba ngày, tổng cộng sáu vị trí chưa có dự báo thực.

### Tình huống 5 — Kiểm tra kiểu và số lượng điểm

**Từ vựng trong mục:** **dtype** — kiểu phần tử; **size** — số phần tử.

**Tình huống thực tế:** Trung tâm nhập hai điểm kiểm tra 7,5 và 8,0 của một học viên. Hãy dùng mảng số thực để giữ phần thập phân rồi in kiểu và số lượng điểm.

**Vì sao chọn cách giải này?** `dtype=float` tránh mất phần thập phân; `size` đếm đúng hai số được lưu.

**Quy trình giải:**

1. Tạo mảng chứa `7.5` và `8.0` với `dtype=float`.
2. Truy cập thuộc tính `dtype` và `size`.
3. In tên kiểu và số phần tử.

```python
import numpy as np

scores = np.array([7.5, 8.0], dtype=float)
print(scores.dtype, scores.size)
```

**Kết quả khi chạy:**

```text
float64 2
```

Dữ liệu gồm hai điểm kiểu `float64`, không phải chuỗi.

## 6. Sai lầm thường gặp

- `shape=(3,2)` là **3 hàng và 2 cột**, không phải ngược lại; phải ghi rõ mỗi hàng/cột đại diện điều gì.
- `axis=0` tổng hợp theo từng cột trong mảng hai chiều; `axis=1` tổng hợp theo từng hàng. Chọn nhầm trục khiến ý nghĩa kết quả khác đi.
- `dtype=float` giữ phần thập phân, còn kiểu số nguyên có thể cắt phần lẻ nếu ép dữ liệu không phù hợp.
- Kết quả trung bình là số thực; các chữ số cuối có thể phụ thuộc biểu diễn dấu phẩy động, nên giải thích bằng giá trị gần đúng khi cần.
- `np.zeros()` chỉ tạo giá trị khởi tạo 0; không được diễn giải là dự báo thực tế đã được mô hình tính.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a NumPy `ndarray`? — `ndarray` của NumPy là gì?**

A. An array for data with a common dtype — Mảng dữ liệu có kiểu phần tử chung

B. A single text file — Một tệp văn bản đơn

C. A Python exception — Một ngoại lệ Python

D. A class inheritance rule — Quy tắc kế thừa lớp

**Q2. What does `shape=(3, 2)` mean for a 2-D array? — `shape=(3, 2)` nghĩa là gì với mảng hai chiều?**

A. Only three total elements — Chỉ có ba phần tử

B. Three rows and two columns — Ba hàng và hai cột

C. Two rows and three columns — Hai hàng và ba cột

D. Three dimensions and two values — Ba chiều và hai giá trị

**Q3. What is the size of an array with shape `(3, 2)`? — Mảng có shape `(3, 2)` chứa bao nhiêu phần tử?**

A. 2 — 2

B. 5 — 5

C. 6 — 6

D. 3 — 3

**Q4. What does `ndim` report? — Thuộc tính `ndim` cho biết gì?**

A. The number of rows only — Chỉ số hàng

B. The data type of an element — Kiểu phần tử

C. The maximum array value — Giá trị lớn nhất

D. The number of array dimensions — Số chiều của mảng

**Q5. What does `dtype` describe? — `dtype` mô tả gì?**

A. The data type of array elements — Kiểu dữ liệu của các phần tử

B. The array's row count — Số hàng

C. The file's extension — Phần mở rộng của file

D. The mean of all entries — Trung bình các phần tử

**Q6. Why specify `dtype=float` when storing decimal scores? — Vì sao dùng `dtype=float` khi lưu điểm có phần lẻ?**

A. To delete missing records — Để xóa bản ghi thiếu

B. To preserve fractional values — Để giữ giá trị có phần thập phân

C. To force integer truncation — Để ép cắt về số nguyên

D. To change rows into columns — Để đổi hàng thành cột

**Q7. For a 2-D array, what does `mean(axis=0)` return? — Với mảng hai chiều, `mean(axis=0)` trả về gì?**

A. Only the first cell — Chỉ ô đầu tiên

B. The original array unchanged — Mảng gốc không đổi

C. One mean per column — Một giá trị trung bình cho mỗi cột

D. One mean per row — Một giá trị trung bình cho mỗi hàng

**Q8. For a 2-D array, what does `sum(axis=1)` produce? — Với mảng hai chiều, `sum(axis=1)` tạo gì?**

A. One sum per column — Một tổng cho mỗi cột

B. A list of column names — List tên cột

C. The shape tuple only — Chỉ tuple shape

D. One sum per row — Một tổng cho mỗi hàng

**Q9. Which statement correctly distinguishes `shape` and `size`? — Đâu là điểm khác nhau giữa `shape` và `size`?**

A. shape lists dimensions; size counts elements — shape ghi kích thước từng chiều; size đếm phần tử

B. They are always identical numbers — Chúng luôn là cùng một số

C. size gives dtype; shape gives values — size cho kiểu dữ liệu; shape cho giá trị

D. Both change elements automatically — Cả hai tự đổi phần tử

**Q10. What does `np.array([1, 2, 3])` create? — `np.array([1, 2, 3])` tạo ra gì?**

A. A class named Array — Lớp tên Array

B. A one-dimensional NumPy array — Một mảng NumPy một chiều

C. A two-column table — Bảng hai cột

D. A CSV file on disk — File CSV trên đĩa

**Q11. What does `np.zeros((2, 3))` create? — `np.zeros((2, 3))` tạo gì?**

A. A 3×2 array of ones — Mảng 3×2 toàn số 1

B. An empty array with no elements — Mảng rỗng không có phần tử

C. A 2×3 array initialized to zeros — Mảng 2×3 được khởi tạo toàn số 0

D. A 2×3 table of missing strings — Bảng 2×3 gồm chuỗi thiếu

**Q12. How is `np.ones((2, 2))` different from `np.zeros((2, 2))`? — `np.ones((2, 2))` khác `np.zeros((2, 2))` thế nào?**

A. It always creates a CSV file — Nó luôn tạo file CSV

B. It has four dimensions — Nó có bốn chiều

C. It cannot be used in arithmetic — Nó không thể tính toán

D. It initializes entries to one instead of zero — Nó khởi tạo giá trị 1 thay cho 0

**Q13. How do NumPy array and Python List differ in numeric operations? — Mảng NumPy khác List Python về phép toán số như thế nào?**

A. NumPy enables element-wise numerical operations — NumPy hỗ trợ phép toán số theo từng phần tử

B. A List always multiplies elements element-wise — List luôn nhân từng phần tử

C. A NumPy array stores only strings — Mảng NumPy chỉ lưu chuỗi

D. A List cannot hold numbers — List không chứa được số

**Q14. For an array with rows as learners and columns as subjects, what does axis=0 average? — Nếu hàng là học viên và cột là môn, `axis=0` tính trung bình theo gì?**

A. Only the last subject — Chỉ môn cuối

B. Each subject across learners — Từng môn qua các học viên

C. Each learner across subjects — Từng học viên qua các môn

D. Only the first learner — Chỉ học viên đầu

**Q15. How many dimensions does a two-dimensional score table have? — Bảng điểm hai chiều có `ndim` bằng bao nhiêu?**

A. 3 — 3

B. The total number of scores — Tổng số điểm

C. 2 — 2

D. 1 — 1

**Q16. Which code accesses array shape without computing new values? — Cú pháp nào lấy shape mà không tính thêm dữ liệu?**

A. `X.sort()` — `X.sort()`

B. `X.delete()` — `X.delete()`

C. `X.write()` — `X.write()`

D. `X.shape` — `X.shape`

**Q17. Which code counts all array entries? — Cú pháp nào đếm tổng số phần tử mảng?**

A. `X.size` — `X.size`

B. `X.mean()` — `X.mean()`

C. `X.dtype` — `X.dtype`

D. `X.shape[0]` in every case — Luôn `X.shape[0]`

**Q18. For finite floating-point values within the target integer range, what does NumPy `.astype(int)` do to their fractional parts? — Với giá trị dấu phẩy động hữu hạn nằm trong phạm vi kiểu số nguyên đích, NumPy `.astype(int)` xử lý phần lẻ thế nào?**

A. It rounds every value to the nearest integer — Làm tròn mọi giá trị về số nguyên gần nhất

B. It discards fractional parts toward zero — Bỏ phần lẻ theo hướng về số 0

C. It preserves fractional parts unchanged — Giữ nguyên toàn bộ phần lẻ

D. It forces the shape to become `(1, 1)` — Buộc shape chuyển thành `(1, 1)`

**Q19. What is the output shape of `X.mean(axis=0)` for `X.shape == (3,2)`? — Nếu `X.shape == (3,2)`, `X.mean(axis=0)` có shape nào?**

A. `(3,2)` — `(3,2)`

B. `(1,3)` — `(1,3)`

C. `(2,)` — `(2,)`

D. `(3,)` — `(3,)`

**Q20. Why label the meaning of each row and column? — Vì sao phải nêu rõ ý nghĩa từng hàng, cột?**

A. To change dtype automatically — Để tự đổi dtype

B. To avoid all numeric calculations — Để tránh mọi phép tính

C. To convert a matrix into text — Để chuyển ma trận thành chữ

D. To interpret aggregated results correctly — Để hiểu đúng kết quả tổng hợp

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | ndarray organizes elements into one or more dimensions for numerical operations. | ndarray tổ chức phần tử theo một hay nhiều chiều để tính toán. |
| Q2 | **B** | For a 2-D array, shape lists the row count first and the column count second. | Với mảng hai chiều, shape ghi số hàng trước và số cột sau. |
| Q3 | **C** | The total element count is the product of the dimensions: 3×2. | Tổng số phần tử bằng tích kích thước hai chiều: 3×2. |
| Q4 | **D** | ndim describes dimensionality rather than the number of elements. | ndim cho biết số chiều, không phải tổng số phần tử. |
| Q5 | **A** | A common dtype governs how values in a NumPy array are represented. | dtype chung quyết định cách biểu diễn các giá trị của mảng NumPy. |
| Q6 | **B** | A floating dtype retains fractional parts such as 8.5. | Kiểu số thực giữ phần lẻ của các điểm như 8.5. |
| Q7 | **C** | Axis 0 aggregates across rows while preserving columns. | Axis 0 tổng hợp qua các hàng và giữ chiều cột. |
| Q8 | **D** | Axis 1 aggregates across columns of each row. | Axis 1 tính tổng qua các cột trong từng hàng. |
| Q9 | **A** | An array may have shape (3, 2) but size 6. | Mảng có thể có shape (3, 2) nhưng size bằng 6. |
| Q10 | **B** | A flat sequence creates a one-dimensional ndarray. | Dãy phẳng tạo ndarray một chiều. |
| Q11 | **C** | zeros creates the requested shape and fills every position with zero. | zeros tạo mảng đúng kích thước và điền 0 vào mỗi ô. |
| Q12 | **D** | Both share the same requested shape; only their initialized values differ. | Cả hai có shape như yêu cầu; chỉ khác giá trị khởi tạo. |
| Q13 | **A** | For example, ndarray times 2 multiplies values, while list times 2 repeats the list. | Ví dụ ndarray nhân 2 sẽ nhân giá trị, còn List nhân 2 lặp lại List. |
| Q14 | **B** | Each column represents a subject, and axis 0 combines rows. | Mỗi cột là một môn; axis 0 gộp các hàng học viên. |
| Q15 | **C** | A matrix-like table is two-dimensional even when it has many rows. | Bảng dạng ma trận có hai chiều dù có nhiều hàng. |
| Q16 | **D** | shape is an array attribute that reports dimensions. | shape là thuộc tính báo kích thước các chiều. |
| Q17 | **A** | size counts elements across every dimension, not just rows. | size đếm phần tử trên mọi chiều, không chỉ đếm hàng. |
| Q18 | **B** | Converting finite in-range floats to an integer dtype truncates toward zero, not to the nearest integer. For example, `np.array([2.9, -2.9]).astype(int)` contains integers `2` and `-2`; the array keeps its shape. | Khi đổi số thực hữu hạn trong phạm vi hợp lệ sang dtype nguyên, NumPy cắt phần lẻ về phía 0 chứ không làm tròn tới số gần nhất. Ví dụ `np.array([2.9, -2.9]).astype(int)` chứa số nguyên `2` và `-2`; shape của mảng giữ nguyên. |
| Q19 | **C** | Three rows are reduced, leaving two column results. | Ba hàng được tổng hợp, còn hai giá trị ứng với hai cột. |
| Q20 | **D** | Without labels, axis choices may compute the right numbers for the wrong question. | Thiếu ý nghĩa hàng/cột dễ dẫn đến tính ra số đúng phép nhưng trả lời sai câu hỏi. |

## 8. Nối sang bài tiếp theo

`List → NumPy Array → Matrix → PCA`.
