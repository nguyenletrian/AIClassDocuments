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


**Q1. What does Index mean? — Ý nghĩa của Index là gì?**

A. It instead describes Lấy một đoạn theo start:stop — Lấy một đoạn theo start:stop

B. The concept is Địa chỉ phần tử của mảng — Địa chỉ phần tử của mảng

C. It instead describes Mảng True/False để lọc phần tử — Mảng True/False để lọc phần tử

D. It instead describes Chọn nhiều vị trí theo danh sách chỉ số — Chọn nhiều vị trí theo danh sách chỉ số


**Q2. What does Slice mean? — Ý nghĩa của Slice là gì?**

A. The concept is Lấy một đoạn theo start:stop — Lấy một đoạn theo start:stop

B. It instead describes Mảng True/False để lọc phần tử — Mảng True/False để lọc phần tử

C. It instead describes Chọn nhiều vị trí theo danh sách chỉ số — Chọn nhiều vị trí theo danh sách chỉ số

D. It instead describes Địa chỉ phần tử của mảng — Địa chỉ phần tử của mảng


**Q3. What does Boolean mask mean? — Ý nghĩa của Boolean mask là gì?**

A. It instead describes Chọn nhiều vị trí theo danh sách chỉ số — Chọn nhiều vị trí theo danh sách chỉ số

B. It instead describes Địa chỉ phần tử của mảng — Địa chỉ phần tử của mảng

C. It instead describes Lấy một đoạn theo start:stop — Lấy một đoạn theo start:stop

D. The concept is Mảng True/False để lọc phần tử — Mảng True/False để lọc phần tử


**Q4. What does Fancy indexing mean? — Ý nghĩa của Fancy indexing là gì?**

A. It instead describes Địa chỉ phần tử của mảng — Địa chỉ phần tử của mảng

B. It instead describes Lấy một đoạn theo start:stop — Lấy một đoạn theo start:stop

C. The concept is Chọn nhiều vị trí theo danh sách chỉ số — Chọn nhiều vị trí theo danh sách chỉ số

D. It instead describes Mảng True/False để lọc phần tử — Mảng True/False để lọc phần tử


**Q5. What is the role of X[row,col]? — Vai trò của X[row,col] là gì?**

A. Another operation would Lấy cả cột j hoặc hàng i — Lấy cả cột j hoặc hàng i

B. It is used to Chọn một ô theo hàng/cột, đếm từ 0 — Chọn một ô theo hàng/cột, đếm từ 0

C. Another operation would Giữ các phần tử thỏa điều kiện logic — Giữ các phần tử thỏa điều kiện logic

D. Another operation would Chọn các cột không liền nhau — Chọn các cột không liền nhau


**Q6. What is the role of X[:,j] / X[i,:]? — Vai trò của X[:,j] / X[i,:] là gì?**

A. It is used to Lấy cả cột j hoặc hàng i — Lấy cả cột j hoặc hàng i

B. Another operation would Giữ các phần tử thỏa điều kiện logic — Giữ các phần tử thỏa điều kiện logic

C. Another operation would Chọn các cột không liền nhau — Chọn các cột không liền nhau

D. Another operation would Chọn một ô theo hàng/cột, đếm từ 0 — Chọn một ô theo hàng/cột, đếm từ 0


**Q7. What is the role of X[condition]? — Vai trò của X[condition] là gì?**

A. Another operation would Chọn các cột không liền nhau — Chọn các cột không liền nhau

B. Another operation would Chọn một ô theo hàng/cột, đếm từ 0 — Chọn một ô theo hàng/cột, đếm từ 0

C. Another operation would Lấy cả cột j hoặc hàng i — Lấy cả cột j hoặc hàng i

D. It is used to Giữ các phần tử thỏa điều kiện logic — Giữ các phần tử thỏa điều kiện logic


**Q8. What is the role of X[:,[0,2]]? — Vai trò của X[:,[0,2]] là gì?**

A. Another operation would Chọn một ô theo hàng/cột, đếm từ 0 — Chọn một ô theo hàng/cột, đếm từ 0

B. Another operation would Lấy cả cột j hoặc hàng i — Lấy cả cột j hoặc hàng i

C. It is used to Chọn các cột không liền nhau — Chọn các cột không liền nhau

D. Another operation would Giữ các phần tử thỏa điều kiện logic — Giữ các phần tử thỏa điều kiện logic


**Q9. Which reason fits example 1? — Lý do nào phù hợp ví dụ 1?**

A. Mask lọc hàng điểm Python>=8 — Mask lọc hàng điểm Python>=8

B. Lấy đúng hàng sinh viên và cột môn học — Lấy đúng hàng sinh viên và cột môn học

C. Fancy indexing chọn cột không cần liền nhau — Fancy indexing chọn cột không cần liền nhau

D. Slice theo chiều hàng để xem mẫu báo cáo — Slice theo chiều hàng để xem mẫu báo cáo


**Q10. Which reason fits example 2? — Lý do nào phù hợp ví dụ 2?**

A. Mask lọc hàng điểm Python>=8 — Mask lọc hàng điểm Python>=8

B. Fancy indexing chọn cột không cần liền nhau — Fancy indexing chọn cột không cần liền nhau

C. Slice theo chiều hàng để xem mẫu báo cáo — Slice theo chiều hàng để xem mẫu báo cáo

D. Thao tác mask trên bản sao để không đổi mảng gốc — Thao tác mask trên bản sao để không đổi mảng gốc


**Q11. Which reason fits example 3? — Lý do nào phù hợp ví dụ 3?**

A. Slice theo chiều hàng để xem mẫu báo cáo — Slice theo chiều hàng để xem mẫu báo cáo

B. Thao tác mask trên bản sao để không đổi mảng gốc — Thao tác mask trên bản sao để không đổi mảng gốc

C. Lấy đúng hàng sinh viên và cột môn học — Lấy đúng hàng sinh viên và cột môn học

D. Fancy indexing chọn cột không cần liền nhau — Fancy indexing chọn cột không cần liền nhau


**Q12. Which reason fits example 4? — Lý do nào phù hợp ví dụ 4?**

A. Thao tác mask trên bản sao để không đổi mảng gốc — Thao tác mask trên bản sao để không đổi mảng gốc

B. Lấy đúng hàng sinh viên và cột môn học — Lấy đúng hàng sinh viên và cột môn học

C. Slice theo chiều hàng để xem mẫu báo cáo — Slice theo chiều hàng để xem mẫu báo cáo

D. Mask lọc hàng điểm Python>=8 — Mask lọc hàng điểm Python>=8


**Q13. Which reason fits example 5? — Lý do nào phù hợp ví dụ 5?**

A. Lấy đúng hàng sinh viên và cột môn học — Lấy đúng hàng sinh viên và cột môn học

B. Thao tác mask trên bản sao để không đổi mảng gốc — Thao tác mask trên bản sao để không đổi mảng gốc

C. Mask lọc hàng điểm Python>=8 — Mask lọc hàng điểm Python>=8

D. Fancy indexing chọn cột không cần liền nhau — Fancy indexing chọn cột không cần liền nhau


**Q14. Which input matches example 1? — Dữ liệu nào phù hợp ví dụ 1?**

A. The stated data are 3 học sinh × 2 môn, điểm thang 10 — 3 học sinh × 2 môn, điểm thang 10

B. Other data: 3 học sinh × 2 môn — 3 học sinh × 2 môn

C. Other data: 2 sinh viên × 3 môn — 2 sinh viên × 3 môn

D. Other data: 5 khách với điểm chi tiêu — 5 khách với điểm chi tiêu


**Q15. Which input matches example 2? — Dữ liệu nào phù hợp ví dụ 2?**

A. Other data: 2 sinh viên × 3 môn — 2 sinh viên × 3 môn

B. Other data: 5 khách với điểm chi tiêu — 5 khách với điểm chi tiêu

C. Other data: 4 nhiệt độ có một giá trị âm lỗi — 4 nhiệt độ có một giá trị âm lỗi

D. The stated data are 3 học sinh × 2 môn — 3 học sinh × 2 môn


**Q16. Which input matches example 3? — Dữ liệu nào phù hợp ví dụ 3?**

A. Other data: 5 khách với điểm chi tiêu — 5 khách với điểm chi tiêu

B. Other data: 4 nhiệt độ có một giá trị âm lỗi — 4 nhiệt độ có một giá trị âm lỗi

C. The stated data are 2 sinh viên × 3 môn — 2 sinh viên × 3 môn

D. Other data: 3 học sinh × 2 môn, điểm thang 10 — 3 học sinh × 2 môn, điểm thang 10


**Q17. Which input matches example 4? — Dữ liệu nào phù hợp ví dụ 4?**

A. Other data: 4 nhiệt độ có một giá trị âm lỗi — 4 nhiệt độ có một giá trị âm lỗi

B. The stated data are 5 khách với điểm chi tiêu — 5 khách với điểm chi tiêu

C. Other data: 3 học sinh × 2 môn, điểm thang 10 — 3 học sinh × 2 môn, điểm thang 10

D. Other data: 3 học sinh × 2 môn — 3 học sinh × 2 môn


**Q18. Which input matches example 5? — Dữ liệu nào phù hợp ví dụ 5?**

A. The stated data are 4 nhiệt độ có một giá trị âm lỗi — 4 nhiệt độ có một giá trị âm lỗi

B. Other data: 3 học sinh × 2 môn, điểm thang 10 — 3 học sinh × 2 môn, điểm thang 10

C. Other data: 3 học sinh × 2 môn — 3 học sinh × 2 môn

D. Other data: 2 sinh viên × 3 môn — 2 sinh viên × 3 môn


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
| Q1 | **B** | The concept is Địa chỉ phần tử của mảng | Địa chỉ phần tử của mảng |
| Q2 | **A** | The concept is Lấy một đoạn theo start:stop | Lấy một đoạn theo start:stop |
| Q3 | **D** | The concept is Mảng True/False để lọc phần tử | Mảng True/False để lọc phần tử |
| Q4 | **C** | The concept is Chọn nhiều vị trí theo danh sách chỉ số | Chọn nhiều vị trí theo danh sách chỉ số |
| Q5 | **B** | It is used to Chọn một ô theo hàng/cột, đếm từ 0 | Chọn một ô theo hàng/cột, đếm từ 0 |
| Q6 | **A** | It is used to Lấy cả cột j hoặc hàng i | Lấy cả cột j hoặc hàng i |
| Q7 | **D** | It is used to Giữ các phần tử thỏa điều kiện logic | Giữ các phần tử thỏa điều kiện logic |
| Q8 | **C** | It is used to Chọn các cột không liền nhau | Chọn các cột không liền nhau |
| Q9 | **B** | Lấy đúng hàng sinh viên và cột môn học | Lấy đúng hàng sinh viên và cột môn học |
| Q10 | **A** | Mask lọc hàng điểm Python>=8 | Mask lọc hàng điểm Python>=8 |
| Q11 | **D** | Fancy indexing chọn cột không cần liền nhau | Fancy indexing chọn cột không cần liền nhau |
| Q12 | **C** | Slice theo chiều hàng để xem mẫu báo cáo | Slice theo chiều hàng để xem mẫu báo cáo |
| Q13 | **B** | Thao tác mask trên bản sao để không đổi mảng gốc | Thao tác mask trên bản sao để không đổi mảng gốc |
| Q14 | **A** | The stated data are 3 học sinh × 2 môn, điểm thang 10 | 3 học sinh × 2 môn, điểm thang 10 |
| Q15 | **D** | The stated data are 3 học sinh × 2 môn | 3 học sinh × 2 môn |
| Q16 | **C** | The stated data are 2 sinh viên × 3 môn | 2 sinh viên × 3 môn |
| Q17 | **B** | The stated data are 5 khách với điểm chi tiêu | 5 khách với điểm chi tiêu |
| Q18 | **A** | The stated data are 4 nhiệt độ có một giá trị âm lỗi | 4 nhiệt độ có một giá trị âm lỗi |
| Q19 | **D** | Rows, columns and units | Hàng, cột và đơn vị |
| Q20 | **C** | To check limitations and edge cases | Để thấy giới hạn và trường hợp biên |

## 8. Nối bài tiếp theo

`NumPy ndarray → Chọn hàng/cột → DataFrame/PCA`.
