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

## 5. Năm tình huống chỉ số NumPy — từ ô đơn đến lọc nhiều điều kiện

### Tình huống 1 — Cấp 1: Lấy đúng một ô điểm từ bảng 10 học viên

**Từ vựng trong mục:** **Index** — chỉ số; **Row** — hàng; **Column** — cột.

**Tình huống thực tế:** Giáo viên nhập **10 học viên** H01…H10; mỗi hàng gồm điểm Toán và Python theo thứ tự cột, thang điểm 10. Cần đọc **điểm Python của H04** để đối chiếu phiếu, không đọc nhầm hàng thứ 4 thành chỉ số 4.

**Vì sao chọn cách này?** NumPy đếm chỉ số từ 0, nên H04 ở hàng 3 và môn Python ở cột 1. Truy cập `scores[3,1]` cho một giá trị cụ thể.

**Quy trình:**
1. Tạo mảng `(10,2)` đúng thứ tự mã người và môn.
2. Dùng một cặp chỉ số hàng–cột để lấy H04/Python.
3. In hình dạng dữ liệu và giá trị đã chọn.

```python
import numpy as np
scores = np.array([[8,9],[7,8],[6,7],[9,9],[10,7],[7,6],[8,8],[5,7],[9,10],[8,6]])
if scores.shape != (10, 2):
    raise ValueError("Bảng cần đúng 10 học viên, 2 môn.")
print("Học viên:", scores.shape[0])
print("Python của H04:", int(scores[3, 1]))
```

**Kết quả khi chạy:**

```text
Học viên: 10
Python của H04: 9
```

Giá trị `scores[3,1]` là 9 điểm trên thang 10; đây là một ô, không phải nguyên hàng học viên.

### Tình huống 2 — Cấp 2: Cắt bốn ngày đầu và một cột trong 12 ngày

**Từ vựng trong mục:** **Slice** — lát cắt; **Step** — bước nhảy; **Array view** — vùng nhìn mảng.

**Tình huống thực tế:** Siêu thị ghi doanh số **12 ngày** theo ba nhóm thực phẩm, sách và đồ dùng (nghìn đồng/ngày). Quản lý muốn tổng doanh thu **cột thực phẩm của bốn ngày đầu**, đồng thời đối chiếu doanh thu đồ dùng ngày 12.

**Vì sao chọn cách này?** Lát cắt `[:4, 0]` chọn đúng bốn hàng đầu và một cột; `[-1, 2]` lấy hàng cuối, cột đồ dùng. Kết hợp slicing với indexing trả kết quả rõ đơn vị.

**Quy trình:**
1. Tạo mảng `(12,3)`, mỗi hàng là một ngày.
2. Lấy cột thực phẩm của ngày 1–4 bằng `data[:4, 0]`.
3. Cộng lát cắt và lấy ô đồ dùng ngày cuối.

```python
import numpy as np
sales = np.array([[100,50,25],[110,55,27],[120,60,29],[130,65,31],[140,70,33],[150,75,35],[160,80,37],[170,85,39],[180,90,41],[190,95,43],[200,100,45],[210,105,47]], dtype=int)
first_four_food = sales[:4, 0]
if sales.shape != (12, 3) or first_four_food.shape != (4,):
    raise ValueError("Cần đủ 12 ngày và 4 doanh thu thực phẩm đầu.")
print("Ngày:", sales.shape[0])
print("Thực phẩm 4 ngày (nghìn đồng):", int(first_four_food.sum()))
print("Đồ dùng ngày 12:", int(sales[-1, 2]))
```

**Kết quả khi chạy:**

```text
Ngày: 12
Thực phẩm 4 ngày (nghìn đồng): 460
Đồ dùng ngày 12: 47
```

Vị trí cuối của lát cắt là **giới hạn không bao gồm**, nên `[:4]` gồm bốn ngày đầu chứ không phải năm ngày.

### Tình huống 3 — Cấp 3: Lọc 15 học viên thỏa hai ngưỡng bằng mặt nạ

**Từ vựng trong mục:** **Boolean mask** — mặt nạ đúng/sai; **AND** — kết hợp điều kiện; **Filtering** — lọc.

**Tình huống thực tế:** Khóa học có **15 học viên** H01…H15 với ba cột điểm Toán, Văn, Python (thang 10). Để tham gia lớp thực hành nâng cao, học viên phải đạt **Toán từ 8** và **Python từ 8** cùng lúc. Cần liệt kê chính xác mã đủ điều kiện và số người tương ứng.

**Vì sao chọn cách này?** Đặt ngoặc cho từng điều kiện so sánh và dùng toán tử phần tử `&` để nối hai mặt nạ NumPy; `and` của Python không áp trực tiếp cho hai mảng Boolean nhiều phần tử.

**Quy trình:**
1. Tạo bảng `(15,3)`, xác định cột Toán 0 và Python 2.
2. Tạo mặt nạ `(X[:,0]>=8) & (X[:,2]>=8)`.
3. Dùng `np.flatnonzero` lấy chỉ số hàng và tạo mã học viên.

```python
import numpy as np
scores = np.array([[5,7,4],[6,9,5],[7,7,6],[8,9,7],[9,7,8],[10,9,9],[5,7,10],[6,9,4],[7,7,5],[8,9,6],[9,7,7],[10,9,8],[5,7,9],[6,9,10],[7,7,4]], dtype=int)
mask = (scores[:, 0] >= 8) & (scores[:, 2] >= 8)
selected = np.flatnonzero(mask)
ids = []
for i in selected:
    ids.append(f"H{i+1:02d}")
if scores.shape != (15, 3):
    raise ValueError("Bảng cần đúng 15 học viên và 3 điểm.")
print("Học viên:", scores.shape[0])
print("Đủ điều kiện:", len(ids))
if ids:
    labels = ", ".join(ids)
else:
    labels = "Không có"
print("Mã:", labels)
```

**Kết quả khi chạy:**

```text
Học viên: 15
Đủ điều kiện: 3
Mã: H05, H06, H12
```

Mặt nạ đánh dấu từng **hàng học viên**, không xóa cột khác và không bỏ qua điều kiện nào.

### Tình huống 4 — Cấp 4: Chọn bốn dòng theo mã từ 18 đơn và giữ bản gốc

**Từ vựng trong mục:** **Fancy indexing** — chọn nhiều vị trí; **Copy** — bản sao; **Repeated index** — chỉ số lặp.

**Tình huống thực tế:** Đội kiểm toán có **18 đơn hàng** O01…O18, mỗi hàng gồm đơn giá (nghìn đồng/món), số lượng (món) và mã kênh (0–2). Kiểm toán cần xem các đơn **O18, O05, O12, O05 theo đúng thứ tự yêu cầu** — mã O05 xuất hiện hai lần trong **danh sách truy vấn**, không phải hai đơn thực tế. Hãy tính tổng tiền của bốn dòng được chọn, và chứng minh khi sửa bảng kết quả thì bảng gốc không đổi.

**Vì sao chọn cách này?** Fancy indexing nhận danh sách chỉ số không liên tiếp, có thể lặp và trả một mảng mới độc lập; vì O05 được chọn hai lần, tổng của **các dòng được chọn** sẽ cộng hai lần nhưng không phải doanh thu thật của 18 đơn.

**Quy trình:**
1. Tạo mảng `(18,3)` với ba cột được ghi rõ.
2. Chọn các vị trí 17, 4, 11, 4 bằng fancy indexing.
3. Tính tổng tiền bốn dòng truy vấn, sửa một ô trong bản chọn rồi đối chiếu mảng gốc.

```python
import numpy as np
orders = np.array([[100,1,0],[120,2,1],[140,3,2],[160,4,0],[180,5,1],[200,1,2],[220,2,0],[240,3,1],[260,4,2],[280,5,0],[300,1,1],[320,2,2],[340,3,0],[360,4,1],[380,5,2],[400,1,0],[420,2,1],[440,3,2]], dtype=int)
indices = [17, 4, 11, 4]
selected = orders[indices]
query_total = int((selected[:, 0] * selected[:, 1]).sum())
original_price = int(orders[17, 0])
selected[0, 0] = 0
if orders.shape != (18, 3) or selected.shape != (4, 3):
    raise ValueError("Bảng gốc phải có 18 đơn và truy vấn có 4 dòng.")
print("Đơn nguồn:", orders.shape[0])
print("Dòng truy vấn:", selected.shape[0])
print("Tổng dòng truy vấn (nghìn đồng):", query_total)
print("Giá O18 trong nguồn:", int(orders[17, 0]))
```

**Kết quả khi chạy:**

```text
Đơn nguồn: 18
Dòng truy vấn: 4
Tổng dòng truy vấn (nghìn đồng): 3760
Giá O18 trong nguồn: 440
```

Sửa bản chọn không đổi mảng gốc, vì fancy indexing tạo copy. Hai dòng truy vấn O05 là cố tình lặp để giải thích hành vi chọn mảng; **không** dùng tổng đó làm báo cáo doanh thu.

### Tình huống 5 — Cấp 5: Kết hợp Boolean mask, NaN và copy cho 20 cảm biến

**Từ vựng trong mục:** **View** — vùng nhìn; **Boolean indexing** — chọn theo điều kiện; **NaN** — giá trị thiếu.

**Tình huống thực tế:** Hệ thống có **20 cảm biến** S01…S20, mỗi hàng gồm nhiệt độ °C và độ ẩm %. Hai cảm biến thiếu nhiệt độ. Để chọn thiết bị cần kiểm tra, chỉ giữ số đo **hợp lệ**, nhiệt độ **từ 28 °C** và độ ẩm **từ 55%**. Hãy in số thiết bị và mã được chọn; khi đánh dấu mẫu đã lọc, dữ liệu nguồn phải nguyên vẹn.

**Vì sao chọn cách này?** NumPy dùng `np.isfinite()` kiểm tra nhiệt độ không thiếu trước khi so ngưỡng, nối điều kiện bằng `&`. Boolean indexing tạo mảng chọn độc lập, phù hợp kiểm tra/sửa mẫu mà không thay đổi bảng ghi gốc.

**Quy trình:**
1. Tạo mảng `(20,2)` kiểu float, chuyển nhiệt độ thiếu sang NaN.
2. Lọc theo ba điều kiện hợp lệ, nhiệt độ và độ ẩm.
3. Lấy mã từ chỉ số hàng, thay thử một giá trị trên mảng được chọn và xác nhận nguồn không đổi.

```python
import numpy as np
raw_temp = [24,25,26,27,28,None,30,31,24,25,26,27,28,29,None,31,24,25,26,27]
humidity = [50,51,52,53,54,55,56,57,58,59,50,51,52,53,54,55,56,57,58,59]
rows = []
for temp, h in zip(raw_temp, humidity):
    if temp is None:
        clean_temp = np.nan
    else:
        clean_temp = temp
    rows.append([clean_temp, h])
data = np.array(rows, dtype=float)
mask = np.isfinite(data[:, 0]) & (data[:, 0] >= 28) & (data[:, 1] >= 55)
selected = data[mask]
selected_ids = []
for i in np.flatnonzero(mask):
    selected_ids.append(f"S{i+1:02d}")
if len(selected):
    selected[0, 0] = 0
if data.shape != (20, 2):
    raise ValueError("Cần 20 cảm biến với hai trường đo.")
if int(np.isnan(data[:, 0]).sum()) != 2:
    raise ValueError("Phải ghi nhận đúng hai nhiệt độ bị thiếu.")
if np.any(data[mask, 0] == 0):
    raise ValueError("Truy vấn không được thay đổi dữ liệu cảm biến gốc.")
print("Cảm biến:", data.shape[0])
print("Thiếu nhiệt độ:", int(np.isnan(data[:, 0]).sum()))
print("Cần kiểm tra:", len(selected_ids))
if selected_ids:
    labels = ", ".join(selected_ids)
else:
    labels = "Không có"
print("Mã:", labels)
```

**Kết quả khi chạy:**

```text
Cảm biến: 20
Thiếu nhiệt độ: 2
Cần kiểm tra: 3
Mã: S07, S08, S16
```

Điều kiện chọn được áp theo **từng hàng có cả hai cột**. Đối với dữ liệu thiếu, chương trình không suy đoán 0 °C và không tự sửa mảng gốc.

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
