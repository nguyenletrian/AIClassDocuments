# PY-14 — NumPy indexing, slicing, boolean và fancy indexing


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Index** — chỉ số; **Slice** — cắt lát.

`NumPy ndarray → Chọn hàng/cột → DataFrame/PCA`

Sau NumPy ndarray và shape, ta học cách lấy đúng phần tử, cột, hàng hoặc nhóm thỏa điều kiện. Chỉ số, lát cắt, mặt nạ Boolean và fancy indexing có mục đích khác nhau.

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

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. Where does Python/NumPy indexing begin? — Chỉ số Python/NumPy bắt đầu từ đâu?**

A. The array's number of dimensions — Số chiều của mảng

B. 0 — 0

C. 1 — 1

D. -1 — -1

**Q2. For a 2-D array, what does `X[1, 0]` select? — Trong mảng hai chiều, `X[1, 0]` chọn gì?**

A. All rows in the first column — Mọi hàng của cột đầu

B. Row 2, column 1 — Hàng thứ hai, cột đầu tiên

C. First row and second column — Hàng thứ nhất cột thứ hai

D. The entire second row — Toàn bộ hàng thứ hai

**Q3. What does `a[-1]` mean for a nonempty 1-D array? — `a[-1]` nghĩa là gì với mảng một chiều không rỗng?**

A. All elements with negative values — Mọi phần tử có giá trị âm

B. An invalid index for every array — Chỉ số không hợp lệ với mọi mảng

C. The last element — Phần tử cuối

D. The first element — Phần tử đầu

**Q4. Which endpoint does a slice `a[1:4]` exclude? — Slice `a[1:4]` không lấy vị trí nào?**

A. Index 1 — Chỉ số 1

B. Index 2 — Chỉ số 2

C. Index 3 — Chỉ số 3

D. Index 4 — Chỉ số 4

**Q5. For a two-dimensional NumPy array `X`, what does `X[:, 0]` select? — Với mảng NumPy hai chiều `X`, `X[:, 0]` chọn gì?**

A. Every column in the first row — Mọi cột của hàng đầu

B. Only the single top-left entry — Chỉ một ô góc trái trên

C. Rows whose entries equal zero — Các hàng có phần tử bằng 0

D. All rows in the first column — Mọi hàng ở cột đầu

**Q6. For a two-dimensional NumPy array `X`, what does `X[0, :]` select? — Với mảng NumPy hai chiều `X`, `X[0, :]` chọn gì?**

A. Every row of the first column — Mọi hàng ở cột đầu

B. Only the scalar at top left — Chỉ giá trị ở góc trái trên

C. All entries in the final row — Mọi ô ở hàng cuối

D. All columns of the first row — Mọi cột của hàng đầu

**Q7. What does a Boolean mask contain? — Mặt nạ Boolean chứa gì?**

A. A sequence of sorted integer positions — Dãy vị trí số nguyên đã sắp

B. A list of column names — List tên cột

C. True/False values indicating which entries to keep — Giá trị True/False cho biết phần tử nào được giữ

D. Only the indexes of negative numbers — Chỉ chỉ số các số âm

**Q8. What is selected by `a[a >= 7]`? — `a[a >= 7]` chọn gì?**

A. Elements strictly greater than 7 — Những phần tử lớn hơn 7 nghiêm ngặt

B. Elements at least 7 — Các phần tử từ 7 trở lên

C. Entries at indexes 0 through 6 — Các phần tử từ chỉ số 0 đến 6

D. Only the item at index 7 — Chỉ phần tử tại chỉ số 7

**Q9. What does `a[[0, 2]]` illustrate? — `a[[0, 2]]` minh họa điều gì?**

A. Fancy indexing with selected positions — Fancy indexing chọn các vị trí cụ thể

B. Basic slicing across consecutive positions — Slice cơ bản các vị trí liên tiếp

C. Boolean masking with a condition — Lọc bằng mặt nạ Boolean có điều kiện

D. Matrix transposition — Phép chuyển vị ma trận

**Q10. What is the difference between slicing and fancy indexing? — Slicing khác fancy indexing ở điểm nào?**

A. Fancy indexing only supports Boolean values — Indexing nâng cao chỉ hỗ trợ Boolean

B. Basic slices specify any arbitrary index list — Slice cơ bản chỉ định được danh sách chỉ số bất kỳ

C. Slices describe ranges; fancy indexing specifies index arrays — Slice chỉ đoạn, fancy indexing chỉ mảng vị trí

D. Both always generate shared-memory views — Cả hai luôn tạo view chia sẻ bộ nhớ

**Q11. In NumPy, basic slicing generally returns what? — Basic slicing của NumPy thường trả về gì?**

A. A view of the original data — View chia sẻ dữ liệu với mảng gốc

B. An independent deep copy guaranteed by all slices — Bản sao độc lập được bảo đảm cho mọi slice

C. A new CSV file containing selected cells — Tệp CSV mới chứa ô đã chọn

D. A Python set of selected values — Set Python của các giá trị đã chọn

**Q12. Does advanced integer-array indexing generally return a view? — Indexing bằng mảng số nguyên nâng cao thường tạo view không?**

A. No, it generally returns a copy — Không, thường trả bản sao

B. Yes, all advanced indexing reads share original memory — Có, mọi kết quả đọc indexing nâng cao đều chia sẻ bộ nhớ gốc

C. It always returns `None` — Nó luôn trả `None`

D. It changes all original array elements to zero — Nó đổi mọi phần tử mảng gốc thành 0

**Q13. How do you keep source data unchanged before assignment? — Làm sao giữ mảng gốc không đổi trước khi gán?**

A. Delete the source array before copying — Xóa mảng nguồn trước khi sao chép

B. Make an explicit `copy()` — Tạo bản sao bằng `copy()`

C. Use a regular slice, which always copies — Dùng slice thông thường vốn luôn sao chép

D. Assign directly to the original `X` — Gán trực tiếp lên `X` gốc

**Q14. For shape (3,2), what does `X[:, 1]` return? — Nếu shape là (3,2), `X[:, 1]` trả về gì?**

A. A single scalar from row 1 column 1 — Một vô hướng tại hàng 1 cột 1

B. Three values from the second column — Ba giá trị ở cột thứ hai

C. Two elements from the second row — Hai phần tử của hàng thứ hai

D. Three values from the first column — Ba giá trị của cột đầu

**Q15. What does `X[:, [0, 2]]` mean when X has three columns? — `X[:, [0, 2]]` nghĩa là gì nếu X có ba cột?**

A. All rows with columns 0 and 1 — Mọi hàng với cột 0 và 1

B. Only the first and third rows — Chỉ hàng thứ nhất và thứ ba

C. The sum of columns 0 and 2 — Tổng cột 0 và 2

D. All rows and the first and third columns — Mọi hàng, cột thứ nhất và thứ ba

**Q16. What is the effect of `a[:3]`? — `a[:3]` có tác dụng gì?**

A. Selects only the element at index 3 — Chỉ lấy phần tử có chỉ số 3

B. Sorts the first three elements descending — Sắp ba phần tử đầu theo thứ tự giảm

C. Take up to the first three entries — Lấy tối đa ba phần tử đầu

D. Removes the first three elements from the source — Xóa ba phần tử đầu khỏi nguồn

**Q17. Which operation filters entire rows based on the first column? — Lệnh nào lọc cả hàng theo điều kiện ở cột đầu?**

A. `X[X[:, 0] >= 8]` — `X[X[:, 0] >= 8]`

B. `X[:, 0]` without a Boolean condition — `X[:, 0]` không có điều kiện Boolean

C. `X[0, 0]` — `X[0, 0]`

D. `X.shape` — `X.shape`

**Q18. What happens when a scalar index is beyond array bounds? — Khi chỉ số phần tử vượt giới hạn mảng thì sao?**

A. NumPy raises IndexError — NumPy báo IndexError

B. It returns `None` for the missing element — Nó trả `None` với phần tử thiếu

C. It silently adds a new row or column — Nó tự thêm hàng hoặc cột

D. It returns the array's last value — Nó trả giá trị cuối mảng

**Q19. For a 2-D array `X` and a one-dimensional Boolean mask marking its rows, how does `X[mask]` differ from `X[[0, 2]]`? — Với `X` hai chiều và mặt nạ Boolean một chiều đánh dấu các hàng, `X[mask]` khác `X[[0, 2]]` thế nào?**

A. `X[[0,2]]` compares values against threshold 2 — `X[[0,2]]` so sánh giá trị với ngưỡng 2

B. The mask always selects exactly rows 0 and 2 — Mặt nạ luôn chỉ chọn hàng 0 và 2

C. A mask selects by condition; indices select by position — Mask chọn theo điều kiện; chỉ số chọn theo vị trí

D. The mask always sorts selected rows — Mặt nạ luôn sắp lại hàng đã chọn

**Q20. Why state what rows and columns represent? — Vì sao cần nêu rõ ý nghĩa hàng và cột?**

A. To force every 2-D array to become 1-D — Buộc mọi mảng hai chiều thành một chiều

B. To change each element's dtype automatically — Tự thay dtype của từng phần tử

C. To guarantee that all columns have equal values — Bảo đảm mọi cột có giá trị bằng nhau

D. To select the intended data without swapping dimensions — Để chọn đúng dữ liệu và không đảo chiều

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | NumPy uses zero-based indexing, so the first element is at index 0. Index 1 means the second element, while index -1 counts from the end of a nonempty axis. | NumPy đánh chỉ số từ 0, nên phần tử đầu có chỉ số 0. Chỉ số 1 là phần tử thứ hai, còn -1 đếm từ cuối một chiều không rỗng. |
| Q2 | **B** | For 2-D arrays the index order is row first, column second, both starting at zero. Thus `X[1,0]` selects the second row's first column, not the first row's second column. | Với mảng hai chiều, chỉ số hàng đứng trước cột, cả hai bắt đầu từ 0. Vì vậy `X[1,0]` lấy ô hàng thứ hai cột thứ nhất, không phải hàng đầu cột thứ hai. |
| Q3 | **C** | Negative index -1 selects the last element along a nonempty one-dimensional array. For `[3,5,7]`, `a[-1]` is 7; a negative index is not a test for negative values. | Chỉ số âm -1 chọn phần tử cuối của mảng một chiều không rỗng. Với `[3,5,7]`, `a[-1]` bằng 7; chỉ số âm không phải thao tác lọc giá trị âm. |
| Q4 | **D** | Python slicing uses a half-open interval: `[1:4]` includes index 1, 2 and 3 but excludes stop index 4. This rule helps compute slice length without an extra element. | Slice Python dùng khoảng nửa mở: `[1:4]` lấy vị trí 1, 2, 3 nhưng không lấy mốc dừng 4. Quy tắc này giúp xác định đúng độ dài lát cắt. |
| Q5 | **D** | For a 2-D array, `X[:,0]` selects every row at column index zero, the first column. The colon spans row positions; it does not select only rows whose values happen to be zero. | Với mảng hai chiều, `X[:,0]` chọn mọi hàng tại cột chỉ số 0, tức cột đầu. Dấu hai chấm duyệt vị trí hàng, không lọc riêng các hàng có giá trị bằng 0. |
| Q6 | **D** | For a 2-D array, `X[0,:]` fixes row index zero and includes every column. With shape `(3,2)`, the result contains the two values of the first row, not an entire column. | Với mảng hai chiều, `X[0,:]` cố định hàng chỉ số 0 và lấy tất cả các cột. Với shape `(3,2)`, kết quả chứa hai giá trị của hàng đầu, không phải nguyên một cột. |
| Q7 | **C** | A Boolean mask marks positions as `True` or `False` so values can be selected according to a condition. For `a=np.array([2,8])`, the mask `a>=7` is `[False, True]`. | Mặt nạ Boolean đánh dấu vị trí bằng `True` hoặc `False` để chọn theo điều kiện. Với `a=np.array([2,8])`, mặt nạ `a>=7` là `[False, True]`. |
| Q8 | **B** | `a[a >= 7]` uses a Boolean condition on values and keeps those at least 7. With `a=[3,7,9]`, the result is `[7,9]`; it does not select the element at index 7. | `a[a >= 7]` dùng điều kiện Boolean trên giá trị để giữ phần tử từ 7 trở lên. Với `a=[3,7,9]`, kết quả `[7,9]`; không phải lấy phần tử ở chỉ số 7. |
| Q9 | **A** | `a[[0,2]]` uses advanced integer-array indexing to select exactly the positions 0 and 2. Unlike a slice `[0:2]`, those indexes can be nonadjacent, and advanced-indexing reads return copies. | `a[[0,2]]` dùng chỉ số mảng số nguyên nâng cao để lấy đúng vị trí 0 và 2. Khác lát cắt `[0:2]`, các vị trí có thể không liền nhau và kết quả đọc theo kiểu này là bản sao. |
| Q10 | **C** | Basic slicing specifies a regular range through start, stop and step, such as `a[1:5:2]`. Advanced integer indexing supplies explicit positions such as `a[[1,4]]`; their view/copy behavior also differs. | Slice cơ bản chỉ khoảng vị trí đều qua start, stop, step, như `a[1:5:2]`. Indexing nâng cao bằng số nguyên chỉ định vị trí riêng như `a[[1,4]]`; chúng còn khác nhau về view/copy. |
| Q11 | **A** | Basic NumPy slicing usually gives a view sharing the original data buffer. Modifying `view[0]` can therefore change the source; call `.copy()` when an independent editable array is required. | Slice NumPy cơ bản thường tạo view dùng chung vùng dữ liệu gốc. Vì vậy sửa `view[0]` có thể đổi mảng nguồn; dùng `.copy()` nếu cần mảng độc lập để sửa. |
| Q12 | **A** | Advanced integer-array indexing produces a copy when reading selected values, not a simple view. This differs from basic slices; assigning through an advanced-indexing expression on the left still updates the indexed source positions. | Đọc bằng indexing nâng cao với mảng số nguyên tạo bản sao, không phải view cơ bản. Khác slice thông thường; tuy nhiên đặt biểu thức indexing nâng cao ở vế trái phép gán vẫn cập nhật các vị trí được chọn trong nguồn. |
| Q13 | **B** | `X.copy()` creates an independent array before destructive edits, avoiding the shared-data effect of slicing views. For example `Y=X.copy(); Y[0]=0` does not change `X` just because of that assignment. | `X.copy()` tạo mảng độc lập trước khi sửa, tránh hiệu ứng chia sẻ dữ liệu của view từ slice. Ví dụ `Y=X.copy(); Y[0]=0` không làm đổi `X` chỉ vì phép gán đó. |
| Q14 | **B** | With shape `(3,2)`, `X[:,1]` keeps all three rows and selects column index one. The result is a one-dimensional array of three values, not two values from a row. | Với shape `(3,2)`, `X[:,1]` giữ cả ba hàng và lấy cột chỉ số một. Kết quả là mảng một chiều ba phần tử, không phải hai giá trị thuộc một hàng. |
| Q15 | **D** | For a 2-D array with three columns, `X[:,[0,2]]` selects all rows and only columns zero and two. The result has two selected columns and uses advanced indexing, unlike the continuous slice `X[:,0:2]`. | Với mảng hai chiều có ba cột, `X[:,[0,2]]` chọn mọi hàng và chỉ hai cột 0, 2. Kết quả có hai cột được chọn và là indexing nâng cao, khác slice liên tục `X[:,0:2]`. |
| Q16 | **C** | The slice `a[:3]` begins at index zero by default and stops before index three. It selects at most the first three elements; on a shorter array, slicing does not raise a scalar-index out-of-bounds error. | Slice `a[:3]` mặc định bắt đầu tại chỉ số 0 và dừng trước chỉ số 3. Nó lấy tối đa ba phần tử đầu; với mảng ngắn hơn, slice không gây lỗi vượt giới hạn như truy cập chỉ số đơn. |
| Q17 | **A** | For 2-D `X`, the expression `X[:,0]>=8` forms one Boolean value for each row. Indexing `X` with that row mask returns complete rows meeting the first-column condition. | Với `X` hai chiều, `X[:,0]>=8` tạo một Boolean tương ứng mỗi hàng. Dùng mặt nạ hàng này để lấy `X` sẽ trả những hàng nguyên vẹn có giá trị cột đầu từ 8 trở lên. |
| Q18 | **A** | Scalar indexing must point inside the array dimension; an out-of-range index causes `IndexError`. Slicing beyond the last position is different: a slice can simply stop at the available end. | Chỉ số đơn phải nằm trong giới hạn chiều mảng; vượt phạm vi sẽ gây `IndexError`. Slice vượt vị trí cuối khác ở chỗ nó có thể dừng tại ranh giới có sẵn. |
| Q19 | **C** | A Boolean row mask selects positions based on per-row conditions, while `X[[0,2]]` selects rows at explicitly named indexes 0 and 2. A mask needs a suitable Boolean shape and does not automatically mean the same two rows. | Mặt nạ Boolean theo hàng chọn vị trí thỏa điều kiện cho từng hàng, còn `X[[0,2]]` chọn hai hàng tại chỉ số 0 và 2. Mặt nạ cần shape Boolean phù hợp và không tự đồng nghĩa chọn đúng hai hàng này. |
| Q20 | **D** | Rows and columns must have stated meanings so an index selects the intended information. If rows represent learners and columns represent subjects, `X[:,0]` means first-subject scores across learners, not one learner's scores. | Cần nêu ý nghĩa hàng và cột để chỉ số chọn đúng thông tin. Nếu hàng là học viên và cột là môn, `X[:,0]` lấy điểm môn đầu của mọi học viên, không phải điểm mọi môn của một học viên. |

## 8. Nối bài tiếp theo

`NumPy ndarray → Chọn hàng/cột → DataFrame/PCA`.
