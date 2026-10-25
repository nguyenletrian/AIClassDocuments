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
# Mục đích: Đọc điểm ở hàng thứ hai, cột thứ nhất của mảng hai chiều.
# Dữ liệu: 2 hàng học viên, 2 cột điểm theo hai môn; chỉ số NumPy đếm từ 0.
# NumPy dùng np.array() để tạo mảng 2 chiều.
import numpy as np

# Hai list con thành hai hàng, mỗi hàng có hai cột.
scores = np.array([[8, 9], [6, 7]])
# [1,0] chọn hàng chỉ số 1 (học viên thứ hai), cột 0 (môn thứ nhất), kết quả 6.
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
# Mục đích: Cắt lấy hai phần tử liên tiếp bằng chỉ số bắt đầu/kết thúc.
# Dữ liệu: Một vector 4 số 5,6,7,8; [1:3] lấy các chỉ số 1,2.
# import numpy as np: đặt tên ngắn np để dùng các thao tác ndarray.
import numpy as np

# Tạo vector một chiều từ bốn phần tử.
scores = np.array([5, 6, 7, 8])
# Slice [bắt đầu:kết thúc] lấy chỉ số 1 và 2, KHÔNG lấy 3; trả mảng [6,7].
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
# Mục đích: Tạo mask Boolean chọn tất cả điểm từ 7 trở lên.
# Dữ liệu: 3 điểm số 4,7,9; mask so theo từng phần tử.
# import numpy as np: đặt tên ngắn np để dùng các thao tác ndarray.
import numpy as np

# Mảng 3 điểm cho phép so sánh vector hóa.
scores = np.array([4, 7, 9])
# So từng ô với 7 tạo mask Boolean [False,True,True].
mask = scores >= 7
# Boolean indexing lấy chỉ các ô mask True, trả mảng mới [7,9].
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
# Mục đích: Chọn hai chỉ số không liền nhau bằng fancy indexing.
# Dữ liệu: 3 điểm 3,5,7; chỉ số được chọn là 0 và 2.
# import numpy as np: đặt tên ngắn np để dùng các thao tác ndarray.
import numpy as np

# Mảng đầu gồm ba phần tử ở chỉ số 0,1,2.
scores = np.array([3, 5, 7])
# Fancy indexing dùng list chỉ số rời rạc [0,2], trả [3,7] thành một mảng mới.
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

**Tình huống thực tế:** Giáo viên có bảng điểm **10 học viên H01–H10**, mỗi hàng ghi điểm **Toán trước, Python sau** trên thang **10 điểm**. Họ muốn tra riêng điểm Python của học viên **H04** để so với phiếu giấy; các hàng và cột đã có thứ tự nên không cần duyệt mọi điểm để tìm một ô.

**Vì sao chọn cách này?** NumPy lưu bảng thành mảng **hai chiều**: chỉ số đầu là **hàng học viên**, chỉ số sau là **cột môn**. Python đếm chỉ số từ **0**, nên học viên thứ tư H04 nằm ở hàng `3`, còn môn Python là cột thứ hai nên có chỉ số `1`. Lệnh `scores[3, 1]` lấy đúng **một ô điểm**, không lấy toàn bộ hàng. Nếu dùng `scores[4, 1]`, chương trình sẽ đọc nhầm H05, một lỗi hay gặp khi người mới áp dụng số thứ tự thông thường cho chỉ số Python.

**Quy trình:**
1. Tạo mảng `(10,2)` đúng thứ tự mã người và môn.
2. Dùng một cặp chỉ số hàng–cột để lấy H04/Python.
3. In hình dạng dữ liệu và giá trị đã chọn.

```python
# Mục đích: Đọc điểm Python của H04 trong bảng 10 học viên × 2 môn.
# Dữ liệu: 10 hàng học viên H01..H10, cột 0 môn A, cột 1 điểm Python (thang 10).
# import numpy as np: đặt tên ngắn np để dùng các thao tác ndarray.
import numpy as np
# Mảng 10 hàng × 2 cột, mỗi hàng là điểm của học viên tương ứng.
scores = np.array([[8,9],[7,8],[6,7],[9,9],[10,7],[7,6],[8,8],[5,7],[9,10],[8,6]])
# shape là (số hàng,số cột); shape (10,2) kiểm đầu vào.
if scores.shape != (10, 2):
    # ValueError thông báo dữ liệu hoặc phép kiểm không đạt, dừng việc tính tiếp.
    raise ValueError("Bảng cần đúng 10 học viên, 2 môn.")
# shape là (số hàng,số cột); shape (10,2) kiểm đầu vào.
# shape[0] trả 10 học viên, khác shape[1] là hai môn.
print("Học viên:", scores.shape[0])
# [3,1] đọc hàng H04 (vì index bắt đầu 0), cột thứ hai Python; int() đổi thành số nguyên Python.
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

**Tình huống thực tế:** Siêu thị lưu doanh thu trong **12 ngày**, mỗi ngày có ba cột **thực phẩm, sách, đồ dùng**, đơn vị **nghìn đồng**. Quản lý cần cộng doanh thu thực phẩm của **bốn ngày đầu** để xem kết quả đầu kỳ, đồng thời tra riêng doanh thu đồ dùng của **ngày thứ 12**. Hai yêu cầu này chỉ liên quan tới các phần nhất định của bảng.

**Vì sao chọn cách này?** **Indexing** là chọn một ô cụ thể; **slicing** là chọn một đoạn liên tiếp. `sales[:4, 0]` lấy các hàng từ đầu **đến trước hàng chỉ số 4**, tức bốn ngày đầu, và chỉ chọn cột thực phẩm có chỉ số 0. `sales[-1, 2]` đọc **hàng cuối** (ngày 12) và cột đồ dùng có chỉ số 2. Sau đó cộng các giá trị trong lát cắt thực phẩm; không cộng cả ba cột vì quản lý chỉ hỏi một nhóm. Số âm `-1` trong chỉ số nghĩa là vị trí cuối, không phải doanh thu âm.

**Quy trình:**
1. Tạo mảng `(12,3)`, mỗi hàng là một ngày.
2. Lấy cột thực phẩm của ngày 1–4 bằng `data[:4, 0]`.
3. Cộng lát cắt và lấy ô đồ dùng ngày cuối.

```python
# Mục đích: Cắt doanh thu thực phẩm bốn ngày đầu và đồ dùng ngày 12.
# Dữ liệu: 12 hàng ngày × 3 cột doanh thu thực phẩm, sách và đồ dùng (nghìn đồng).
# import numpy as np: đặt tên ngắn np để dùng các thao tác ndarray.
import numpy as np
# 12 hàng ngày và 3 cột doanh thu; dtype=int giữ số nguyên nghìn đồng.
sales = np.array([[100,50,25],[110,55,27],[120,60,29],[130,65,31],[140,70,33],[150,75,35],[160,80,37],[170,85,39],[180,90,41],[190,95,43],[200,100,45],[210,105,47]], dtype=int)
# [:4,0] lấy hàng 0..3 (bốn ngày đầu), chỉ cột 0 thực phẩm; view theo slice.
first_four_food = sales[:4, 0]
# shape (12,3); first_four_food.shape (4,) là vector bốn giá trị.
if sales.shape != (12, 3) or first_four_food.shape != (4,):
    # ValueError thông báo dữ liệu hoặc phép kiểm không đạt, dừng việc tính tiếp.
    raise ValueError("Cần đủ 12 ngày và 4 doanh thu thực phẩm đầu.")
# shape (12,3); first_four_food.shape (4,) là vector bốn giá trị.
print("Ngày:", sales.shape[0])
# sum() cộng bốn giá trị thực phẩm đầu (nghìn đồng).
print("Thực phẩm 4 ngày (nghìn đồng):", int(first_four_food.sum()))
# [-1,2] lấy hàng cuối (ngày 12), cột thứ ba đồ dùng; int() in số nguyên.
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

**Tình huống thực tế:** Khóa học có **15 học viên H01–H15** với điểm ba môn **Toán, Văn, Python**, mỗi môn thang **10 điểm**. Lớp thực hành nâng cao chỉ nhận người có **Toán từ 8 điểm** và **Python từ 8 điểm**, cả hai phải đúng. Giáo vụ cần biết có bao nhiêu học viên đủ điều kiện và mã của họ để gửi lịch học.

**Vì sao chọn cách này?** **Mặt nạ Boolean** là một dãy giá trị `True`/`False`, tương ứng từng học viên có đạt điều kiện hay không. NumPy so toàn bộ cột Toán với mốc 8, rồi so cột Python với mốc 8; dấu `&` ghép hai kết quả **theo từng hàng**, nên chỉ người vượt cả hai ngưỡng mới có `True`. Đặt ngoặc quanh mỗi phép so sánh để Python hiểu đúng thứ tự thực hiện. `np.flatnonzero(mask)` lấy vị trí các hàng được chọn; cộng 1 khi chuyển vị trí thành mã H01... vì chỉ số bắt đầu từ 0. Không dùng `and` thông thường với hai mảng nhiều phần tử vì nó không thực hiện phép kiểm tra từng hàng như mong muốn.

**Quy trình:**
1. Tạo bảng `(15,3)`, xác định cột Toán 0 và Python 2.
2. Tạo mặt nạ `(X[:,0]>=8) & (X[:,2]>=8)`.
3. Dùng `np.flatnonzero` lấy chỉ số hàng và tạo mã học viên.

```python
# Mục đích: Lọc 15 học viên đạt đồng thời ngưỡng điểm môn 1 và môn 3.
# Dữ liệu: 15 hàng học viên, cột 0/1/2 ứng với ba môn; yêu cầu môn đầu và môn thứ ba đều >=8.
# import numpy as np: đặt tên ngắn np để dùng các thao tác ndarray.
import numpy as np
# 15 hàng học viên, 3 cột điểm; dtype=int dùng số nguyên.
scores = np.array([[5,7,4],[6,9,5],[7,7,6],[8,9,7],[9,7,8],[10,9,9],[5,7,10],[6,9,4],[7,7,5],[8,9,6],[9,7,7],[10,9,8],[5,7,9],[6,9,10],[7,7,4]], dtype=int)
# [:,0] là toàn bộ 15 giá trị cột môn thứ nhất, [:,2] là cột thứ ba.
# & nối TỪNG phần tử Boolean của hai điều kiện, ngoặc bao mỗi so sánh; khác từ khóa and cho scalar.
mask = (scores[:, 0] >= 8) & (scores[:, 2] >= 8)
# flatnonzero() trả chỉ số 0-based của những vị trí mask True, không trả điểm.
selected = np.flatnonzero(mask)
ids = []
# Duyệt vị trí 0-based, cộng 1 rồi f-string :02d tạo mã H01..H15.
for i in selected:
    ids.append(f"H{i+1:02d}")
# shape (15,3) xác minh đúng số học viên/môn.
if scores.shape != (15, 3):
    # ValueError thông báo dữ liệu hoặc phép kiểm không đạt, dừng việc tính tiếp.
    raise ValueError("Bảng cần đúng 15 học viên và 3 điểm.")
# shape (15,3) xác minh đúng số học viên/môn.
print("Học viên:", scores.shape[0])
# len() đếm mã đạt cả hai điều kiện.
print("Đủ điều kiện:", len(ids))
# List rỗng có giá trị False; nếu có mã mới ghép chuỗi.
if ids:
    # join() ghép các mã bằng dấu phẩy và khoảng trắng.
    labels = ", ".join(ids)
else:
    labels = "Không có"
# int() chuyển NumPy scalar về số nguyên Python để in.
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

**Tình huống thực tế:** Đội kiểm toán nhận bảng gốc gồm **18 đơn O01–O18**. Mỗi hàng có đơn giá (**nghìn đồng/món**), số lượng (**món**) và mã kênh bán. Kiểm toán viên được yêu cầu xem bốn dòng theo **thứ tự O18, O05, O12, O05**; mã O05 xuất hiện **hai lần trong yêu cầu tra cứu** chứ không phải vì bảng gốc có hai đơn O05. Cần tính tổng tiền của đúng bốn dòng đã yêu cầu và thử sửa một ô trong bảng kết quả mà không làm đổi dữ liệu gốc.

**Vì sao chọn cách này?** **Fancy indexing** nghĩa là chọn các hàng bằng một **danh sách vị trí bất kỳ**, không nhất thiết liên tiếp hay tăng dần. `[17, 4, 11, 4]` tương ứng O18, O05, O12, O05: hàng O05 được đưa vào **hai lần trong bảng truy vấn**, vì đúng như yêu cầu kiểm toán. Tổng được tính trên bốn dòng truy vấn, nên tiền O05 cũng được tính hai lần trong **tổng truy vấn**; đây không phải doanh thu thật của 18 đơn nguồn. Với cách chọn này NumPy tạo một **mảng mới**, vì vậy đặt giá ở dòng đầu của mảng kết quả về 0 không làm mất giá O18 trong bảng gốc.

**Quy trình:**
1. Tạo mảng `(18,3)` với ba cột được ghi rõ.
2. Chọn các vị trí 17, 4, 11, 4 bằng fancy indexing.
3. Tính tổng tiền bốn dòng truy vấn, sửa một ô trong bản chọn rồi đối chiếu mảng gốc.

```python
# Mục đích: Chọn các dòng hóa đơn rời rạc, bao gồm dòng trùng, mà không sửa mảng gốc.
# Dữ liệu: 18 đơn, cột 0 giá (nghìn đồng), cột 1 số món, cột 2 mã loại; chỉ số [17,4,11,4] truy vấn O18, O05, O12, O05.
# import numpy as np: đặt tên ngắn np để dùng các thao tác ndarray.
import numpy as np
# 18 hàng đơn × 3 cột (giá, số lượng, loại); dtype=int để tính tiền.
orders = np.array([[100,1,0],[120,2,1],[140,3,2],[160,4,0],[180,5,1],[200,1,2],[220,2,0],[240,3,1],[260,4,2],[280,5,0],[300,1,1],[320,2,2],[340,3,0],[360,4,1],[380,5,2],[400,1,0],[420,2,1],[440,3,2]], dtype=int)
# Danh sách [17,4,11,4] chọn bốn hàng, trong đó O05 được chọn hai lần.
indices = [17, 4, 11, 4]
# Fancy indexing tạo BẢN SAO mảng, giữ cả hai lần chỉ số 4; không phải slice/view.
selected = orders[indices]
# [:,0] lấy giá, [:,1] số lượng của bốn dòng đã chọn; nhân từng hàng rồi sum() tiền nghìn đồng.
query_total = int((selected[:, 0] * selected[:, 1]).sum())
# Đọc giá O18 từ mảng nguồn trước khi thay đổi bản sao.
# Đối chiếu giá gốc O18 không thay đổi; int() đổi NumPy scalar về int Python.
original_price = int(orders[17, 0])
# Sửa ô đầu trong BẢN SAO selected, không sửa orders do fancy indexing.
selected[0, 0] = 0
# shape (18,3), selected.shape (4,3) kiểm đúng dữ liệu truy vấn.
if orders.shape != (18, 3) or selected.shape != (4, 3):
    # ValueError thông báo dữ liệu hoặc phép kiểm không đạt, dừng việc tính tiếp.
    raise ValueError("Bảng gốc phải có 18 đơn và truy vấn có 4 dòng.")
# shape (18,3), selected.shape (4,3) kiểm đúng dữ liệu truy vấn.
print("Đơn nguồn:", orders.shape[0])
# int() chuyển NumPy scalar về số nguyên Python để in.
print("Dòng truy vấn:", selected.shape[0])
# int() chuyển NumPy scalar về số nguyên Python để in.
print("Tổng dòng truy vấn (nghìn đồng):", query_total)
# Đọc giá O18 từ mảng nguồn trước khi thay đổi bản sao.
# Đối chiếu giá gốc O18 không thay đổi; int() đổi NumPy scalar về int Python.
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

**Tình huống thực tế:** Trạm theo dõi **20 cảm biến S01–S20**, mỗi cảm biến có nhiệt độ **°C** và độ ẩm **%**. Hai cảm biến chưa gửi được nhiệt độ nên được đánh dấu là thiếu dữ liệu. Kỹ thuật viên cần chọn những thiết bị có nhiệt độ **hợp lệ từ 28 °C trở lên** và độ ẩm **từ 55% trở lên**, in số lượng và mã của chúng. Sau đó họ muốn đánh dấu một giá trị trong bảng đã lọc để kiểm tra rằng bảng số đo gốc không bị sửa.

**Vì sao chọn cách này?** `np.isfinite()` giúp phát hiện nhiệt độ có phải **một số hữu hạn hợp lệ** không; chỗ thiếu được chuyển thành `np.nan` và bị loại trước khi xét ngưỡng. Chương trình tạo ba mặt nạ: nhiệt độ hợp lệ, nhiệt độ ít nhất 28 °C, độ ẩm ít nhất 55%; dùng `&` để chỉ chọn cảm biến thỏa **cả ba**. `np.flatnonzero()` trả vị trí thiết bị được chọn, từ đó tạo mã S01... Boolean indexing tạo **mảng kết quả độc lập** trong trường hợp này, nên thay giá ở mảng đã lọc không sửa bảng nguồn. Không được coi NaN là 0 °C vì sẽ che mất hai thiết bị chưa gửi số đo.

**Quy trình:**
1. Tạo mảng `(20,2)` kiểu float, chuyển nhiệt độ thiếu sang NaN.
2. Lọc theo ba điều kiện hợp lệ, nhiệt độ và độ ẩm.
3. Lấy mã từ chỉ số hàng, thay thử một giá trị trên mảng được chọn và xác nhận nguồn không đổi.

```python
# Mục đích: Lọc 20 cảm biến theo nhiệt độ và độ ẩm, kiểm bản sao không sửa nguồn.
# Dữ liệu: 20 cảm biến, cột 0 nhiệt độ °C với 2 None, cột 1 độ ẩm %; cần nhiệt độ >=28, độ ẩm >=55.
# import numpy as np: đặt tên ngắn np để dùng các thao tác ndarray.
import numpy as np
# 20 nhiệt độ °C, None biểu thị hai giá trị thiếu, không phải 0 độ.
raw_temp = [24,25,26,27,28,None,30,31,24,25,26,27,28,29,None,31,24,25,26,27]
# 20 độ ẩm % cùng vị trí với raw_temp.
humidity = [50,51,52,53,54,55,56,57,58,59,50,51,52,53,54,55,56,57,58,59]
rows = []
# zip() ghép nhiệt độ và độ ẩm theo chỉ số để mỗi hàng là một cảm biến.
for temp, h in zip(raw_temp, humidity):
    # is None bắt nhiệt độ chưa đo và gắn marker NaN.
    if temp is None:
        # np.nan là giá trị thiếu kiểu số thực, giữ được trong NumPy dtype=float.
        clean_temp = np.nan
    else:
        clean_temp = temp
    # append() ghi hàng (nhiệt độ đã xử lý, độ ẩm).
    rows.append([clean_temp, h])
# dtype=float cho phép lưu cả số và np.nan trong mảng 20×2.
data = np.array(rows, dtype=float)
# [:,0] lấy cột nhiệt độ mọi hàng; isfinite() trả True với số hữu hạn, False với NaN/inf.
# & nối Boolean từng hàng, ngoặc đảm bảo so sánh được tính riêng; nhiệt độ từ 28 °C.
# Cột 1 là độ ẩm, lấy từ 55% trở lên; cả ba mask phải True.
mask = np.isfinite(data[:, 0]) & (data[:, 0] >= 28) & (data[:, 1] >= 55)
# Boolean indexing trả BẢN SAO các hàng đạt điều kiện, không phải view.
selected = data[mask]
selected_ids = []
# flatnonzero() cho các vị trí 0-based của hàng được chọn.
for i in np.flatnonzero(mask):
    # f-string :02d tạo mã S01..S20 từ i+1, append() lưu mã.
    selected_ids.append(f"S{i+1:02d}")
# len() là số hàng được chọn; chỉ sửa selected khi có ít nhất một hàng.
if len(selected):
    # Thử thay dữ liệu trong mảng lọc; vì boolean indexing là copy, dữ liệu gốc data vẫn giữ nguyên.
    selected[0, 0] = 0
# shape (20,2) đối chiếu số cảm biến và số trường đo.
if data.shape != (20, 2):
    # ValueError thông báo dữ liệu hoặc phép kiểm không đạt, dừng việc tính tiếp.
    raise ValueError("Cần 20 cảm biến với hai trường đo.")
# isnan() đánh dấu đúng hai NaN nhiệt độ, sum() trên mask đếm chúng.
if int(np.isnan(data[:, 0]).sum()) != 2:
    # ValueError thông báo dữ liệu hoặc phép kiểm không đạt, dừng việc tính tiếp.
    raise ValueError("Phải ghi nhận đúng hai nhiệt độ bị thiếu.")
# any() kiểm có bất kỳ nhiệt độ nguồn của các hàng đã chọn bị đổi thành 0 hay không.
if np.any(data[mask, 0] == 0):
    # ValueError thông báo dữ liệu hoặc phép kiểm không đạt, dừng việc tính tiếp.
    raise ValueError("Truy vấn không được thay đổi dữ liệu cảm biến gốc.")
# shape (20,2) đối chiếu số cảm biến và số trường đo.
print("Cảm biến:", data.shape[0])
# isnan() đánh dấu đúng hai NaN nhiệt độ, sum() trên mask đếm chúng.
print("Thiếu nhiệt độ:", int(np.isnan(data[:, 0]).sum()))
# int() chuyển NumPy scalar về số nguyên Python để in.
print("Cần kiểm tra:", len(selected_ids))
if selected_ids:
    labels = ", ".join(selected_ids)
else:
    labels = "Không có"
# int() chuyển NumPy scalar về số nguyên Python để in.
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
