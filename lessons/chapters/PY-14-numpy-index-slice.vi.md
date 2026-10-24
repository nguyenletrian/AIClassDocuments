# PY-14 — NumPy indexing, slicing, boolean và fancy indexing


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Index** — chỉ số; **Slice** — cắt lát.

`NumPy ndarray → Chọn hàng/cột → DataFrame/PCA`

**Học xong dùng để làm gì?** Lọc quan sát, chọn cột đặc trưng, hiểu lúc nào thao tác sửa dữ liệu gốc qua view.

**Kết nối kiến thức tiếp theo:** PY-15 thực hiện phép tổng hợp và broadcasting trên dữ liệu được chọn.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Dùng khi nào |
|---|---|---|
| Index | chỉ số | Địa chỉ phần tử của mảng |
| Slice | cắt lát | Lấy một đoạn theo start:stop |
| Boolean mask | mặt nạ logic | Mảng True/False để lọc phần tử |
| Fancy indexing | chỉ số nâng cao | Chọn nhiều vị trí theo danh sách chỉ số |

## 3. Thư viện, hàm và lựa chọn

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / tham số | Giải thích ngay theo hàm |
|---|---|
| `X[row,col]` | Chọn một ô theo hàng/cột, đếm từ 0 |
| `X[:,j] / X[i,:]` | Lấy cả cột j hoặc hàng i |
| `X[condition]` | Giữ các phần tử thỏa điều kiện logic |
| `X[:,[0,2]]` | Chọn các cột không liền nhau |


## 4. Khái niệm liên quan

Trong bảng điểm NumPy, **hàng là học viên**, **cột là môn học**, **ô là điểm một học viên ở một môn**. Bài này đi từ chọn một ô bằng chỉ số đến chọn nhiều ô/hàng/cột bằng slice, mặt nạ Boolean và fancy indexing. Mỗi cách trả lời một câu hỏi khác nhau khi làm việc với dữ liệu.

### 4.1. Indexing — Đọc một vị trí

**Từ vựng trong mục:** **Index** — chỉ số; **Row/column** — hàng/cột.

Mảng hai chiều giống một bảng có hàng và cột. Giả sử `scores` có **hai hàng học viên** An, Bình và **hai cột môn** Toán, Python, lần lượt là `[[8,9],[6,7]]`. **Chỉ số bắt đầu từ 0**; `scores[1,0]` lấy hàng thứ hai (Bình), cột đầu (Toán), cho điểm 6. Dấu phẩy trong `[row, col]` phân biệt vị trí hàng và cột.

```python
# Mục đích: Đọc một vị trí.
import numpy as np

scores = np.array([[8, 9], [6, 7]])
print(scores[1, 0])
```

**Kết quả khi chạy:**

```text
6
```

Chỉ số hàng 1 và cột 0 lấy điểm Toán của học viên thứ hai, không phải điểm học viên đầu.

### 4.2. Slicing — Cắt một đoạn liên tiếp

**Từ vựng trong mục:** **Slice** — lát cắt; **Start/stop** — đầu/cuối.

**Slicing** chọn một đoạn theo chỉ số, cú pháp `[start:stop]` lấy từ start **đến trước stop**. Với điểm `[5,6,7,8]`, `scores[1:3]` lấy vị trí 1 và 2, nghĩa là hai điểm 6, 7. Trên bảng hai chiều, `scores[:,0]` lấy tất cả hàng nhưng chỉ cột đầu; dấu `:` đứng riêng nghĩa là lấy toàn bộ chiều đó. Lát cắt NumPy cơ bản có thể là **view** dùng chung bộ nhớ với mảng gốc.

```python
# Mục đích: Cắt một đoạn liên tiếp.
import numpy as np

scores = np.array([5, 6, 7, 8])
print(scores[1:3])
```

**Kết quả khi chạy:**

```text
[6 7]
```

Giá trị 8 ở vị trí 3 không được lấy vì điểm stop bị loại khỏi lát cắt.

### 4.3. Boolean mask — Lọc theo điều kiện

**Từ vựng trong mục:** **Boolean mask** — mặt nạ logic; **Condition** — điều kiện.

Nếu các điểm là `[4,7,9]` và yêu cầu giữ điểm từ 7 trở lên, phép `scores >= 7` tạo mặt nạ `[False, True, True]`. Dùng `scores[mask]` chỉ lấy phần tử ứng với `True`. Với bảng hai chiều, `X[X[:,0] >= 8]` giữ **các hàng có điểm ở cột đầu đạt 8**, chứ không chỉ lấy các ô điểm cao.

```python
# Mục đích: Lọc theo điều kiện.
import numpy as np

scores = np.array([4, 7, 9])
mask = scores >= 7
print(scores[mask])
```

**Kết quả khi chạy:**

```text
[7 9]
```

Hai giá trị 7 và 9 vượt hoặc bằng ngưỡng, còn 4 bị loại.

### 4.4. Fancy indexing — Chọn vị trí rời rạc

**Từ vựng trong mục:** **Fancy indexing** — chỉ số nâng cao; **Index array** — mảng chỉ số.

Khác với **Slice** lấy đoạn liên tiếp, **Fancy indexing** cho phép chỉ định nhiều vị trí không liền nhau. Với `[3,5,7]`, `scores[[0,2]]` lấy phần tử đầu và cuối, bỏ phần tử giữa. Trên bảng hai chiều, `X[:, [0,2]]` lấy cột thứ nhất và thứ ba. Fancy indexing bằng mảng chỉ số thường tạo **bản sao** thay vì view của dữ liệu gốc.

```python
# Mục đích: Chọn vị trí rời rạc.
import numpy as np

scores = np.array([3, 5, 7])
print(scores[[0, 2]])
```

**Kết quả khi chạy:**

```text
[3 7]
```

Chương trình lấy vị trí 0 và 2 mà không phải lấy cả đoạn 0–2.

## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Tra điểm một học viên

**Từ vựng trong mục:** **Index** — chỉ số; **Shape** — kích thước.

**Tình huống thực tế:** Trung tâm có điểm Toán và Python của ba học viên An (8,9), Bình (6,7), Lan (9,8), thang 10. Hãy in **điểm Toán của Bình** bằng chỉ số hàng và cột.

**Vì sao chọn cách giải này?** `scores[1,0]` định vị chính xác hàng Bình và cột Toán, vì Python đếm từ 0.

**Quy trình giải:**

1. Lưu ba học viên theo hàng An, Bình, Lan.
2. Lưu môn Toán ở cột 0, Python ở cột 1.
3. Lấy ô `[1,0]` và in giá trị.

```python
# Mục đích: Tra điểm một học viên.
import numpy as np

scores = np.array([[8, 9], [6, 7], [9, 8]])
print(scores[1, 0])
```

**Kết quả khi chạy:**

```text
6
```

Học viên Bình có điểm Toán 6 trên thang 10.

### Tình huống 2 — Lọc học viên có điểm cao

**Từ vựng trong mục:** **Boolean mask** — mặt nạ Boolean; **Threshold** — ngưỡng.

**Tình huống thực tế:** Vẫn bảng ba học viên, hai môn Toán và Python như trên. Trung tâm chỉ muốn giữ những học viên có **điểm Toán từ 8 trở lên**. Hãy in nguyên hàng điểm của những học viên đạt ngưỡng.

**Vì sao chọn cách giải này?** Mặt nạ `scores[:,0] >= 8` được tạo từ cột Toán, sau đó áp vào toàn bộ hàng.

**Quy trình giải:**

1. Lấy cột Toán của cả ba học viên bằng `scores[:, 0]`.
2. So sánh với 8 để tạo mặt nạ Boolean.
3. Lấy các hàng thỏa ngưỡng và in bảng.

```python
# Mục đích: Lọc học viên có điểm cao.
import numpy as np

scores = np.array([[8, 9], [6, 7], [9, 8]])
print(scores[scores[:, 0] >= 8])
```

**Kết quả khi chạy:**

```text
[[8 9]
 [9 8]]
```

An và Lan có điểm Toán từ 8 trở lên; Bình không đạt.

### Tình huống 3 — Chọn hai môn không liền nhau

**Từ vựng trong mục:** **Fancy indexing** — chỉ số nâng cao; **Column** — cột.

**Tình huống thực tế:** Hai học viên có điểm của ba môn Toán, Văn, Python lần lượt là `[8,7,9]` và `[6,5,8]`. Giáo viên chỉ muốn xem **Toán và Python**, bỏ cột Văn ở giữa.

**Vì sao chọn cách giải này?** Fancy indexing `[:, [0, 2]]` chọn hai cột rời nhau mà vẫn giữ mọi hàng học viên.

**Quy trình giải:**

1. Lưu hai hàng học viên và ba cột theo thứ tự Toán, Văn, Python.
2. Chọn tất cả hàng với `:` và cột 0, 2 bằng danh sách chỉ số.
3. In bảng hai cột kết quả.

```python
# Mục đích: Chọn hai môn không liền nhau.
import numpy as np

scores = np.array([[8, 7, 9], [6, 5, 8]])
print(scores[:, [0, 2]])
```

**Kết quả khi chạy:**

```text
[[8 9]
 [6 8]]
```

Bảng còn lại hai môn Toán và Python, giữ nguyên hai hàng học viên.

### Tình huống 4 — Lấy ba khách hàng đầu

**Từ vựng trong mục:** **Slice** — lát cắt; **Array** — mảng.

**Tình huống thực tế:** Cửa hàng có năm khoản chi tiêu khách hàng là `[100,200,50,300,120]` nghìn đồng, lưu theo thứ tự thời gian. Hãy lấy **ba khoản đầu tiên** để kiểm tra nhanh.

**Vì sao chọn cách giải này?** `[:3]` lấy các chỉ số 0, 1, 2 mà không lấy chỉ số 3.

**Quy trình giải:**

1. Tạo mảng gồm năm khoản chi tiêu theo thứ tự.
2. Dùng lát cắt `[:3]` lấy ba vị trí đầu.
3. In ba số tiền (nghìn đồng).

```python
# Mục đích: Lấy ba khách hàng đầu.
import numpy as np

spending = np.array([100, 200, 50, 300, 120])
print(spending[:3])
```

**Kết quả khi chạy:**

```text
[100 200  50]
```

Ba khoản đầu là 100, 200 và 50 nghìn đồng.

### Tình huống 5 — Thay mã số đo lỗi trên bản sao

**Từ vựng trong mục:** **Boolean mask** — mặt nạ Boolean; **Copy** — bản sao.

**Tình huống thực tế:** Cảm biến lưu nhiệt độ `[20,-1,23,24]` °C; `-1` là mã lỗi, **không phải nhiệt độ thật**. Hãy tạo bản sao, thay mã lỗi bằng 0 để minh họa phép gán có điều kiện, đồng thời giữ nguyên mảng gốc.

**Vì sao chọn cách giải này?** `copy()` tránh sửa đầu vào; mặt nạ `<0` chọn mã âm cần thay. Giá trị 0 ở bản xử lý chỉ là **giá trị tạm**, không được suy diễn là số đo thật.

**Quy trình giải:**

1. Lưu mảng gốc và tạo `clean = values.copy()`.
2. Chọn phần tử âm bằng `clean < 0`.
3. Gán 0 ở vị trí đó, in cả hai mảng để so sánh.

```python
# Mục đích: Thay mã số đo lỗi trên bản sao.
import numpy as np

values = np.array([20, -1, 23, 24])
clean = values.copy()
clean[clean < 0] = 0
print(values, clean)
```

**Kết quả khi chạy:**

```text
[20 -1 23 24] [20  0 23 24]
```

Bản gốc giữ `-1`; bản sao đổi mã lỗi thành 0. Trong dữ liệu thực tế cần đánh dấu thiếu thay vì coi 0 °C là số đo hợp lệ.

## 6. Sai lầm thường gặp

- Chỉ số bắt đầu từ **0**. Mảng có ba hàng thì hàng thứ ba là chỉ số 2, không phải 3.
- `a[1:3]` lấy phần tử 1, 2 và **không** lấy 3. Lát cắt NumPy cơ bản thường là view: sửa view có thể sửa mảng gốc.
- Mặt nạ Boolean chọn phần tử/hàng thỏa điều kiện, còn Fancy indexing chọn vị trí theo danh sách chỉ số và thường tạo bản sao.
- Trong mảng 2-D, `X[:, 0]` là cột đầu, `X[0, :]` là hàng đầu: không đảo ý nghĩa hàng/cột.
- Không coi mã lỗi cảm biến `-1` hay giá trị tạm `0` là số đo hợp lệ khi phân tích dữ liệu thật.

## 7. Trắc nghiệm

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. Where does Python/NumPy indexing begin? | Chỉ số Python/NumPy bắt đầu từ đâu?**

A. -2 | -2

B. 0 | 0

C. The number of dimensions | Số chiều của mảng

D. 1 | 1

**Đáp án: B**

**Giải thích:** Chỉ số bắt đầu từ không: `a[0]` là phần tử đầu, còn `a[1]` là phần tử thứ hai. Chỉ số âm đếm ngược từ cuối.


**Q2. For a 2-D array, what does `X[1, 0]` select? | Trong mảng hai chiều, `X[1, 0]` chọn gì?**

A. Every row, first column | Mọi hàng, cột đầu

B. Row 2, column 1 | Hàng thứ hai, cột đầu tiên

C. All columns of the first row | Mọi cột của hàng đầu

D. Row 1, column 2 | Hàng đầu, cột thứ hai

**Đáp án: B**

**Giải thích:** Mảng 2D được truy cập theo `X[hàng, cột]`, với chỉ số bắt đầu từ không. Vì thế `X[1, 0]` là hàng hai, cột một.


**Q3. What does `a[-1]` mean for a nonempty 1-D array? | `a[-1]` nghĩa là gì với mảng một chiều không rỗng?**

A. An invalid index in all cases | Chỉ số luôn không hợp lệ

B. The last element | Phần tử cuối

C. All negative values | Mọi giá trị âm

D. The first element | Phần tử đầu

**Đáp án: B**

**Giải thích:** Với mảng không rỗng, chỉ số `-1` lấy phần tử cuối; ở `[4, 6, 8]` đó là `8`. Ngược lại, chỉ số `0` lấy phần tử đầu.


**Q4. Which endpoint does a slice `a[1:4]` exclude? | Slice `a[1:4]` không lấy vị trí nào?**

A. Index 3 | Chỉ số 3

B. Index 1 | Chỉ số 1

C. Index 4 | Chỉ số 4

D. Index 2 | Chỉ số 2

**Đáp án: C**

**Giải thích:** Chỉ số dừng của slice không được lấy: `a[1:4]` chọn vị trí 1, 2, 3 nếu có. Vị trí 4 không thuộc lát cắt.


**Q5. What does `X[:, 0]` select? | `X[:, 0]` lấy gì?**

A. Only the top-left value always | Luôn chỉ ô góc trên trái

B. All columns in the first row | Mọi cột ở hàng đầu

C. Only rows with value zero | Chỉ hàng có giá trị 0

D. All rows in the first column | Mọi hàng ở cột đầu

**Đáp án: D**

**Giải thích:** Trong `X[:, 0]`, dấu `:` chọn mọi hàng và `0` chọn cột đầu. Kết quả là dữ liệu theo cột, khác `X[0, :]` lấy một hàng.


**Q6. What does `X[0, :]` select? | `X[0, :]` lấy gì?**

A. All columns of the first row | Mọi cột của hàng đầu

B. The last row | Hàng cuối

C. All rows of the first column | Mọi hàng của cột đầu

D. The diagonal | Đường chéo

**Đáp án: A**

**Giải thích:** `X[0, :]` cố định hàng số không và giữ mọi cột. Với `[[1,2],[3,4]]`, kết quả là hàng đầu `[1,2]`, không phải cột đầu.


**Q7. What does a Boolean mask contain? | Mặt nạ Boolean chứa gì?**

A. Only positive integers | Chỉ số nguyên dương

B. Random floating-point numbers | Số thực ngẫu nhiên

C. Only column names | Chỉ tên cột

D. True/False values indicating which entries to keep | Giá trị True/False cho biết phần tử nào được giữ

**Đáp án: D**

**Giải thích:** Mặt nạ Boolean chứa các vị trí `True` và `False`, thường sinh từ phép so sánh. Với `[4, 8]`, điều kiện `a >= 7` chỉ chọn phần tử thứ hai.


**Q8. What is selected by `a[a >= 7]`? | `a[a >= 7]` chọn gì?**

A. All entries smaller than 7 | Mọi phần tử nhỏ hơn 7

B. Only the element at index 7 | Chỉ phần tử chỉ số 7

C. Elements at least 7 | Các phần tử từ 7 trở lên

D. The first seven entries | Bảy phần tử đầu

**Đáp án: C**

**Giải thích:** Biểu thức so giá trị với ngưỡng 7 rồi giữ phần tử thỏa điều kiện. Với `[4, 7, 9]`, kết quả là `[7, 9]`, không phải phần tử có chỉ số 7.


**Q9. What does `a[[0, 2]]` illustrate? | `a[[0, 2]]` minh họa điều gì?**

A. A logical AND operation | Phép AND logic

B. Slicing one continuous range | Cắt một đoạn liên tục

C. Fancy indexing with selected positions | Fancy indexing chọn các vị trí cụ thể

D. A matrix transpose | Chuyển vị ma trận

**Đáp án: C**

**Giải thích:** `a[[0, 2]]` dùng mảng chỉ số nguyên để chọn các vị trí cụ thể. Nó có thể lấy phần tử đầu và thứ ba không liền nhau, khác với lát cắt liên tục.


**Q10. What is the difference between slicing and fancy indexing? | Slicing khác fancy indexing ở điểm nào?**

A. Both always select entire matrices | Cả hai luôn lấy cả ma trận

B. Slicing requires Boolean values only | Slicing chỉ dùng Boolean

C. Slices describe ranges; fancy indexing specifies index arrays | Slice chỉ đoạn, fancy indexing chỉ mảng vị trí

D. Fancy indexing never uses integers | Fancy indexing không dùng số nguyên

**Đáp án: C**

**Giải thích:** Slice xác định dãy chỉ số có quy luật như `a[1:6:2]`; fancy indexing nguyên chỉ vị trí tùy ý như `a[[5, 1, 5]]`. Fancy indexing có thể lặp hoặc đổi thứ tự vị trí.


**Q11. In NumPy, basic slicing generally returns what? | Basic slicing của NumPy thường trả về gì?**

A. A view of the original data | View chia sẻ dữ liệu với mảng gốc

B. A guaranteed independent copy | Luôn là bản sao độc lập

C. A plain Python set | Một Set Python

D. A new CSV file | File CSV mới

**Đáp án: A**

**Giải thích:** Basic slicing thường trả view chia sẻ bộ nhớ nền. Sửa `part = a[1:3]` có thể ảnh hưởng giá trị gốc tương ứng; hãy dùng `.copy()` khi cần dữ liệu độc lập.


**Q12. Does advanced integer-array indexing generally return a view? | Indexing bằng mảng số nguyên nâng cao thường tạo view không?**

A. Yes, it always shares memory | Có, luôn chia sẻ bộ nhớ

B. No, it generally returns a copy | Không, thường trả bản sao

C. It converts the source to strings | Nó chuyển nguồn thành chuỗi

D. It only returns None | Nó chỉ trả None

**Đáp án: B**

**Giải thích:** Indexing nâng cao bằng số nguyên thường sao chép dữ liệu được chọn thay vì tạo view. Sửa `b = a[[0,2]]` thường không đổi `a`; gán trực tiếp `a[[0,2]] = ...` là thao tác khác.


**Q13. How do you keep source data unchanged before assignment? | Làm sao giữ mảng gốc không đổi trước khi gán?**

A. Make an explicit `copy()` | Tạo bản sao bằng `copy()`

B. Use `del X` first | Xóa X trước

C. Always modify a slice directly | Luôn sửa trực tiếp slice

D. Replace every value with zero | Thay mọi giá trị bằng 0

**Đáp án: A**

**Giải thích:** Lệnh `b = a.copy()` tạo bộ nhớ riêng trước khi sửa. Sau đó gán `b[0] = 9` không đổi `a[0]`, khác với sửa view dùng chung dữ liệu.


**Q14. For shape (3,2), what does `X[:, 1]` return? | Nếu shape là (3,2), `X[:, 1]` trả về gì?**

A. Three values from the second column | Ba giá trị ở cột thứ hai

B. Two values from the first row | Hai giá trị của hàng đầu

C. An array with five values | Mảng năm giá trị

D. One value in the center | Một giá trị giữa bảng

**Đáp án: A**

**Giải thích:** Mảng `(3,2)` có ba hàng hai cột. `X[:, 1]` lấy cột thứ hai qua cả ba hàng, cho kết quả có shape `(3,)`.


**Q15. What does `X[:, [0, 2]]` mean when X has three columns? | `X[:, [0, 2]]` nghĩa là gì nếu X có ba cột?**

A. First two rows, all columns | Hai hàng đầu, mọi cột

B. The sum of columns zero and two | Tổng hai cột 0 và 2

C. All rows and the first and third columns | Mọi hàng, cột thứ nhất và thứ ba

D. Only the second column | Chỉ cột thứ hai

**Đáp án: C**

**Giải thích:** Với ba cột, chỉ số `[0,2]` xác định cột thứ nhất và thứ ba. Dấu hai chấm giữ mọi hàng; biểu thức chọn hai cột chứ không cộng giá trị của chúng.


**Q16. What is the effect of `a[:3]`? | `a[:3]` có tác dụng gì?**

A. Take up to the first three entries | Lấy tối đa ba phần tử đầu

B. Take index 3 alone | Chỉ lấy phần tử số 3

C. Sort entries descending | Sắp phần tử giảm dần

D. Remove the first three entries | Xóa ba phần tử đầu

**Đáp án: A**

**Giải thích:** Bỏ start nghĩa là mặc định từ không, còn chỉ số dừng 3 không được lấy. Vì vậy `a[:3]` lấy tối đa ba phần tử đầu ngay cả khi mảng ngắn hơn; nó không xóa chúng.


**Q17. Which operation filters entire rows based on the first column? | Lệnh nào lọc cả hàng theo điều kiện ở cột đầu?**

A. `X.shape` | `X.shape`

B. `X[:, 0]` alone | Chỉ `X[:, 0]`

C. `X[0, 0]` | `X[0, 0]`

D. `X[X[:, 0] >= 8]` | `X[X[:, 0] >= 8]`

**Đáp án: D**

**Giải thích:** `X[:,0] >= 8` tạo một Boolean cho mỗi hàng bằng cách xét giá trị cột đầu. Dùng mask này để lấy từ `X` sẽ giữ nguyên các hàng thỏa điều kiện, không chỉ phần tử cột đầu.


**Q18. What happens when a scalar index is beyond array bounds? | Khi chỉ số phần tử vượt giới hạn mảng thì sao?**

A. It silently creates a new row | Nó âm thầm tạo hàng mới

B. NumPy raises IndexError | NumPy báo IndexError

C. It converts the array to a dictionary | Nó chuyển mảng thành Dictionary

D. It always returns zero | Nó luôn trả 0

**Đáp án: B**

**Giải thích:** Chỉ số đơn vượt phạm vi một trục mảng gây `IndexError`. Với mảng dài ba phần tử, chỉ số 3 không hợp lệ vì vị trí dương cuối là 2; truy cập không tự mở rộng mảng.


**Q19. How does `X[mask]` differ from `X[[0,2]]`? | `X[mask]` khác `X[[0,2]]` ra sao?**

A. Both necessarily select the same rows | Cả hai luôn lấy cùng hàng

B. A mask automatically sorts values | Mask tự sắp xếp giá trị

C. Indices always compare values to a threshold | Chỉ số luôn so giá trị với ngưỡng

D. A mask selects by condition; indices select by position | Mask chọn theo điều kiện; chỉ số chọn theo vị trí

**Đáp án: D**

**Giải thích:** Mask Boolean đánh dấu vị trí vượt qua phép kiểm tra, còn mảng chỉ số nguyên nêu thẳng các vị trí. Mask dựa trên điều kiện và `X[[0,2]]` không nhất thiết chọn cùng hàng.


**Q20. Why state what rows and columns represent? | Vì sao cần nêu rõ ý nghĩa hàng và cột?**

A. To make all arrays immutable | Để mọi mảng bất biến

B. To force arrays into 1-D | Để buộc mảng thành một chiều

C. To avoid using dtype | Để tránh dtype

D. To select the intended data without swapping dimensions | Để chọn đúng dữ liệu và không đảo chiều

**Đáp án: D**

**Giải thích:** Ý nghĩa từng trục quyết định lát cắt nào trả lời đúng vấn đề. Nếu hàng là học viên và cột là môn, `X[:,0]` lấy điểm môn đầu của mọi học viên, còn `X[0,:]` lấy điểm các môn của học viên đầu.

## 8. Nối bài tiếp theo

`NumPy ndarray → Chọn hàng/cột → DataFrame/PCA`.
