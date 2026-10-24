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

A. 0 — 0

B. 1 — 1

C. -2 — -2

D. The number of dimensions — Số chiều của mảng

**Q2. For a 2-D array, what does `X[1, 0]` select? — Trong mảng hai chiều, `X[1, 0]` chọn gì?**

A. All columns of the first row — Mọi cột của hàng đầu

B. Row 2, column 1 — Hàng thứ hai, cột đầu tiên

C. Row 1, column 2 — Hàng đầu, cột thứ hai

D. Every row, first column — Mọi hàng, cột đầu

**Q3. What does `a[-1]` mean for a nonempty 1-D array? — `a[-1]` nghĩa là gì với mảng một chiều không rỗng?**

A. An invalid index in all cases — Chỉ số luôn không hợp lệ

B. All negative values — Mọi giá trị âm

C. The last element — Phần tử cuối

D. The first element — Phần tử đầu

**Q4. Which endpoint does a slice `a[1:4]` exclude? — Slice `a[1:4]` không lấy vị trí nào?**

A. Index 1 — Chỉ số 1

B. Index 2 — Chỉ số 2

C. Index 3 — Chỉ số 3

D. Index 4 — Chỉ số 4

**Q5. What does `X[:, 0]` select? — `X[:, 0]` lấy gì?**

A. All rows in the first column — Mọi hàng ở cột đầu

B. All columns in the first row — Mọi cột ở hàng đầu

C. Only the top-left value always — Luôn chỉ ô góc trên trái

D. Only rows with value zero — Chỉ hàng có giá trị 0

**Q6. What does `X[0, :]` select? — `X[0, :]` lấy gì?**

A. The last row — Hàng cuối

B. All columns of the first row — Mọi cột của hàng đầu

C. All rows of the first column — Mọi hàng của cột đầu

D. The diagonal — Đường chéo

**Q7. What does a Boolean mask contain? — Mặt nạ Boolean chứa gì?**

A. Only column names — Chỉ tên cột

B. Random floating-point numbers — Số thực ngẫu nhiên

C. True/False values indicating which entries to keep — Giá trị True/False cho biết phần tử nào được giữ

D. Only positive integers — Chỉ số nguyên dương

**Q8. What is selected by `a[a >= 7]`? — `a[a >= 7]` chọn gì?**

A. Only the element at index 7 — Chỉ phần tử chỉ số 7

B. The first seven entries — Bảy phần tử đầu

C. All entries smaller than 7 — Mọi phần tử nhỏ hơn 7

D. Elements at least 7 — Các phần tử từ 7 trở lên

**Q9. What does `a[[0, 2]]` illustrate? — `a[[0, 2]]` minh họa điều gì?**

A. Fancy indexing with selected positions — Fancy indexing chọn các vị trí cụ thể

B. Slicing one continuous range — Cắt một đoạn liên tục

C. A logical AND operation — Phép AND logic

D. A matrix transpose — Chuyển vị ma trận

**Q10. What is the difference between slicing and fancy indexing? — Slicing khác fancy indexing ở điểm nào?**

A. Slicing requires Boolean values only — Slicing chỉ dùng Boolean

B. Slices describe ranges; fancy indexing specifies index arrays — Slice chỉ đoạn, fancy indexing chỉ mảng vị trí

C. Both always select entire matrices — Cả hai luôn lấy cả ma trận

D. Fancy indexing never uses integers — Fancy indexing không dùng số nguyên

**Q11. In NumPy, basic slicing generally returns what? — Basic slicing của NumPy thường trả về gì?**

A. A guaranteed independent copy — Luôn là bản sao độc lập

B. A plain Python set — Một Set Python

C. A view of the original data — View chia sẻ dữ liệu với mảng gốc

D. A new CSV file — File CSV mới

**Q12. Does advanced integer-array indexing generally return a view? — Indexing bằng mảng số nguyên nâng cao thường tạo view không?**

A. Yes, it always shares memory — Có, luôn chia sẻ bộ nhớ

B. It only returns None — Nó chỉ trả None

C. It converts the source to strings — Nó chuyển nguồn thành chuỗi

D. No, it generally returns a copy — Không, thường trả bản sao

**Q13. How do you keep source data unchanged before assignment? — Làm sao giữ mảng gốc không đổi trước khi gán?**

A. Make an explicit `copy()` — Tạo bản sao bằng `copy()`

B. Always modify a slice directly — Luôn sửa trực tiếp slice

C. Use `del X` first — Xóa X trước

D. Replace every value with zero — Thay mọi giá trị bằng 0

**Q14. For shape (3,2), what does `X[:, 1]` return? — Nếu shape là (3,2), `X[:, 1]` trả về gì?**

A. An array with five values — Mảng năm giá trị

B. Three values from the second column — Ba giá trị ở cột thứ hai

C. Two values from the first row — Hai giá trị của hàng đầu

D. One value in the center — Một giá trị giữa bảng

**Q15. What does `X[:, [0, 2]]` mean when X has three columns? — `X[:, [0, 2]]` nghĩa là gì nếu X có ba cột?**

A. First two rows, all columns — Hai hàng đầu, mọi cột

B. The sum of columns zero and two — Tổng hai cột 0 và 2

C. All rows and the first and third columns — Mọi hàng, cột thứ nhất và thứ ba

D. Only the second column — Chỉ cột thứ hai

**Q16. What is the effect of `a[:3]`? — `a[:3]` có tác dụng gì?**

A. Remove the first three entries — Xóa ba phần tử đầu

B. Take index 3 alone — Chỉ lấy phần tử số 3

C. Sort entries descending — Sắp phần tử giảm dần

D. Take up to the first three entries — Lấy tối đa ba phần tử đầu

**Q17. Which operation filters entire rows based on the first column? — Lệnh nào lọc cả hàng theo điều kiện ở cột đầu?**

A. `X[X[:, 0] >= 8]` — `X[X[:, 0] >= 8]`

B. `X[0, 0]` — `X[0, 0]`

C. `X[:, 0]` alone — Chỉ `X[:, 0]`

D. `X.shape` — `X.shape`

**Q18. What happens when a scalar index is beyond array bounds? — Khi chỉ số phần tử vượt giới hạn mảng thì sao?**

A. It converts the array to a dictionary — Nó chuyển mảng thành Dictionary

B. NumPy raises IndexError — NumPy báo IndexError

C. It always returns zero — Nó luôn trả 0

D. It silently creates a new row — Nó âm thầm tạo hàng mới

**Q19. How does `X[mask]` differ from `X[[0,2]]`? — `X[mask]` khác `X[[0,2]]` ra sao?**

A. A mask automatically sorts values — Mask tự sắp xếp giá trị

B. Indices always compare values to a threshold — Chỉ số luôn so giá trị với ngưỡng

C. A mask selects by condition; indices select by position — Mask chọn theo điều kiện; chỉ số chọn theo vị trí

D. Both necessarily select the same rows — Cả hai luôn lấy cùng hàng

**Q20. Why state what rows and columns represent? — Vì sao cần nêu rõ ý nghĩa hàng và cột?**

A. To force arrays into 1-D — Để buộc mảng thành một chiều

B. To avoid using dtype — Để tránh dtype

C. To make all arrays immutable — Để mọi mảng bất biến

D. To select the intended data without swapping dimensions — Để chọn đúng dữ liệu và không đảo chiều

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | The first array element is indexed by zero. | Phần tử đầu tiên được đánh chỉ số 0. |
| Q2 | **B** | NumPy uses zero-based row and column indices in that order. | NumPy dùng chỉ số hàng rồi cột, cả hai bắt đầu từ 0. |
| Q3 | **C** | Negative indices count from the end; -1 is last. | Chỉ số âm đếm từ cuối, -1 là phần tử cuối cùng. |
| Q4 | **D** | The stop endpoint in Python slicing is exclusive. | Giới hạn kết thúc của slice không được lấy. |
| Q5 | **A** | The colon means all entries along the row dimension. | Dấu hai chấm nghĩa là lấy toàn bộ theo chiều hàng. |
| Q6 | **B** | The first index chooses a row; the colon retains all columns. | Chỉ số đầu chọn hàng, dấu : giữ mọi cột. |
| Q7 | **C** | Conditions create a mask used to filter the array. | Điều kiện tạo mặt nạ để lọc phần tử phù hợp. |
| Q8 | **D** | The comparison is applied to values, not to their indices. | Phép so sánh áp dụng trên giá trị phần tử, không phải chỉ số. |
| Q9 | **A** | An index list selects the specified positions, even when nonadjacent. | Danh sách chỉ số chọn đúng các vị trí được nêu, dù không liền nhau. |
| Q10 | **B** | Index arrays enable arbitrary selections rather than only regular slices. | Mảng chỉ số cho phép chọn vị trí rời rạc thay vì đoạn chỉ số liên tiếp. |
| Q11 | **C** | A basic slice generally shares memory, so editing it may affect the source. | Slice cơ bản thường dùng chung bộ nhớ, sửa nó có thể ảnh hưởng mảng gốc. |
| Q12 | **D** | Advanced indexing commonly copies selected data, unlike basic slicing. | Indexing nâng cao thường sao chép phần dữ liệu được chọn, khác basic slicing. |
| Q13 | **A** | An independent copy prevents edits from changing the original array. | Bản sao độc lập giúp phép sửa không thay đổi mảng gốc. |
| Q14 | **B** | All three rows remain while column index 1 selects the second column. | Ba hàng được giữ, còn chỉ số cột 1 chọn cột thứ hai. |
| Q15 | **C** | The colon preserves rows and the index list selects nonadjacent columns. | Dấu : giữ mọi hàng, List chỉ số chọn hai cột rời nhau. |
| Q16 | **D** | Omitting start means start at zero; stop three is excluded. | Bỏ start nghĩa là bắt đầu từ 0, dừng trước chỉ số 3. |
| Q17 | **A** | The column comparison builds a row mask that selects complete rows. | So sánh cột đầu tạo mặt nạ theo hàng để lọc nguyên các hàng. |
| Q18 | **B** | A scalar index must refer to a position within the array's dimension. | Chỉ số đơn phải nằm trong giới hạn của chiều dữ liệu tương ứng. |
| Q19 | **C** | Boolean arrays encode which positions pass a condition, while index arrays name positions. | Mảng Boolean đánh dấu vị trí thỏa điều kiện, còn mảng chỉ số gọi trực tiếp vị trí. |
| Q20 | **D** | The same syntax can represent different information depending on how data is organized. | Cùng một cú pháp có thể lấy sai thông tin nếu hiểu nhầm cách tổ chức bảng. |

## 8. Nối bài tiếp theo

`NumPy ndarray → Chọn hàng/cột → DataFrame/PCA`.
