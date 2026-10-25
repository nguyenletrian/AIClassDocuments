# PY-16 — NumPy reshape, transpose, ma trận và lưu file


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Reshape** — đổi hình dạng; **Transpose** — chuyển vị.

`ndarray → Reshape/Transpose → Matrix → Model Input`

**Học xong dùng để làm gì?** Chuyển mảng thành ma trận, nhân ma trận và lưu dữ liệu NPY để dùng lại mà không mất shape/dtype.

**Kết nối kiến thức tiếp theo:** PY-17 đưa dữ liệu vào DataFrame có nhãn hàng và tên cột.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Dùng khi nào |
|---|---|---|
| Reshape | đổi hình dạng | Đổi shape nhưng giữ số phần tử |
| Transpose | chuyển vị | Đổi trục hàng và cột |
| Matrix multiply | nhân ma trận | Tạo kết quả bằng phép nhân tuyến tính |
| Serialization | lưu dữ liệu | Ghi mảng vào tệp để đọc lại |

## 3. Thư viện, hàm và lựa chọn

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / tham số | Giải thích ngay theo hàm |
|---|---|
| `reshape(rows,cols)` | Số phần tử trước/sau phải bằng nhau |
| `X.T / np.transpose(X)` | Đổi trục từ hàng thành cột |
| `A @ B / np.dot(A,B)` | Nhân tuyến tính yêu cầu kích thước tương thích |
| `np.save()/np.load()` | Lưu và đọc định dạng NPY, chỉ tải từ nguồn tin cậy |


## 4. Khái niệm liên quan

Từ một dãy nhiệt độ hoặc bảng điểm, ta cần biết **bố trí lại dữ liệu**, **đổi chiều quan sát**, **tính điểm tổng hợp** và **lưu để sử dụng lại**. Bốn khái niệm này nối nhau: `reshape` bố trí hàng/cột, `.T` chuyển vị, `@` kết hợp các chiều đúng quy tắc, còn `np.save`/`np.load` lưu và phục hồi mảng.

### 4.1. Reshape — Đổi hình dạng mảng

**Từ vựng trong mục:** **Reshape** — đổi hình dạng; **Shape** — kích thước.

**Reshape** đổi cách sắp xếp một dãy phần tử thành các hàng/cột mới **mà không đổi số phần tử**. Ví dụ máy đo có 6 nhiệt độ theo thứ tự thời gian `[20,21,22,23,24,25]` °C. Nếu mỗi hàng đại diện một ngày và mỗi cột là một giờ đo, `reshape(2,3)` tạo bảng **2 ngày × 3 giờ**. Ngày đầu chứa ba số đầu, ngày hai chứa ba số sau. Không thể reshape 6 số thành `(4,2)` vì cần 8 số.

**No Note — Không chú thích**

```python
import numpy as np

temperatures = np.array([20, 21, 22, 23, 24, 25])
print(temperatures.reshape(2, 3))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Đổi 6 lượt đo liên tiếp thành bảng 2 hàng và 3 cột mà không mất dữ liệu.
# Dữ liệu: 6 nhiệt độ °C, sau reshape mỗi hàng có ba lượt liên tiếp.
# NumPy xử lý mảng số nhiều chiều; np là tên viết tắt của thư viện.
import numpy as np

# np.array() tạo ndarray một chiều từ 6 số đo.
temperatures = np.array([20, 21, 22, 23, 24, 25])
# reshape(2,3) đổi cách tổ chức thành 2 hàng × 3 cột, giữ nguyên giá trị và thứ tự đọc; không tự tính thêm dữ liệu.
print(temperatures.reshape(2, 3))
```

**Kết quả khi chạy:**

```text
[[20 21 22]
 [23 24 25]]
```

Mỗi hàng là một ngày, mỗi cột là một giờ đo theo thứ tự. Shape đổi từ `(6,)` thành `(2,3)`, còn thứ tự giá trị không đổi.

### 4.2. Transpose — Hoán đổi ý nghĩa hàng và cột

**Từ vựng trong mục:** **Transpose** — chuyển vị; **Row/column** — hàng/cột.

**Transpose** (`.T`) tráo hai trục của bảng hai chiều. Ví dụ bảng `scores` có **2 hàng học viên** An, Bình và **3 cột môn** Toán, Văn, Python: `[8,7,9]` và `[6,5,8]`. Sau `.T`, bảng thành **3 hàng môn** và **2 cột học viên**. Các điểm giữ nguyên nhưng cách trình bày đổi, giúp thống kê theo môn dễ nhìn hơn. Khác `reshape`, chuyển vị đổi vị trí của các ô theo trục.

**No Note — Không chú thích**

```python
import numpy as np

scores = np.array([[8, 7, 9], [6, 5, 8]])
print(scores.T)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Chuyển vị ma trận để biến các cột môn thành các hàng.
# Dữ liệu: 2 học viên (hàng), 3 môn (cột), điểm theo thang 10.
# NumPy hỗ trợ mảng hai chiều và chuyển vị ma trận.
import numpy as np

# Tạo bảng điểm 2 hàng × 3 cột, mỗi hàng là một học viên.
scores = np.array([[8, 7, 9], [6, 5, 8]])
# .T là thuộc tính chuyển vị, hoán đổi trục hàng/cột thành 3 hàng môn × 2 cột học viên; thường là view nên không mặc định sao chép.
print(scores.T)
```

**Kết quả khi chạy:**

```text
[[8 6]
 [7 5]
 [9 8]]
```

Hàng đầu chứa điểm Toán của An và Bình, hàng hai là Văn, hàng ba là Python. Shape chuyển từ `(2,3)` thành `(3,2)`.

### 4.3. Matrix multiplication — Nhân ma trận

**Từ vựng trong mục:** **Matrix multiplication** — nhân ma trận; **Dot product** — tích vô hướng.

Toán tử `@` thực hiện **phép nhân ma trận**, không phải nhân từng ô như `*`. Với một học viên có điểm `[8,7,9]` cho ba môn và trọng số `[0.2,0.3,0.5]`, `scores @ weights` tính `8×0.2 + 7×0.3 + 9×0.5 = 8.2`. Với bảng nhiều học viên, các hàng là người và các cột là môn; ma trận trọng số phải có số hàng bằng số cột của bảng điểm, ví dụ `(2,3) @ (3,1) → (2,1)`.

**No Note — Không chú thích**

```python
import numpy as np

scores = np.array([8, 7, 9])
weights = np.array([0.2, 0.3, 0.5])
print(scores @ weights)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tính điểm tổng hợp theo trọng số bằng phép nhân ma trận @.
# Dữ liệu: Ba điểm [8,7,9] nhân ba tỷ trọng [20%,30%,50%], tổng trọng số là 100%.
# NumPy cung cấp phép nhân ma trận cho ndarray.
import numpy as np

# Vector 3 điểm có cùng thứ tự môn với weights.
scores = np.array([8, 7, 9])
# Vector trọng số 0.2/0.3/0.5 biểu thị mức đóng góp từng môn, không phải số học viên.
weights = np.array([0.2, 0.3, 0.5])
# @ nhân từng điểm với trọng số tương ứng rồi cộng thành một điểm tổng; khác * nhân từng ô và trả vector.
print(scores @ weights)
```

**Kết quả khi chạy:**

```text
8.2
```

Điểm có trọng số là 8,2 trên thang 10. `@` nhân các thành phần tương ứng rồi cộng thành một điểm tổng kết.

### 4.4. Serialization — Lưu và đọc lại mảng

**Từ vựng trong mục:** **Serialization** — tuần tự hóa; **NPY** — định dạng lưu mảng NumPy.

**Tuần tự hóa (serialization)** là lưu dữ liệu trong bộ nhớ thành định dạng có thể đọc lại. NumPy dùng `np.save` ghi mảng thành tệp `.npy`, chứa cả **giá trị, shape và dtype**; `np.load` phục hồi dữ liệu. Ví dụ lưu ba điểm `[3,5,7]` vào thư mục tạm rồi đọc lại để kiểm tra. `allow_pickle=False` phù hợp khi chỉ cần dữ liệu số, tránh đọc đối tượng Python được pickle hóa từ nguồn không tin cậy. `tolist()` chỉ đổi mảng thành List, **không lưu file**.

**No Note — Không chú thích**

```python
import numpy as np
from pathlib import Path
from tempfile import TemporaryDirectory

scores = np.array([3, 5, 7])
with TemporaryDirectory() as folder:
    file_path = Path(folder) / 'scores.npy'
    np.save(file_path, scores)
    restored = np.load(file_path, allow_pickle=False)
    print(restored)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Ghi mảng NumPy ra tệp .npy trong thư mục tạm và đọc lại an toàn.
# Dữ liệu: Ba điểm số [3,5,7], tệp .npy bảo toàn dữ liệu và kiểu NumPy.
# NumPy hỗ trợ định dạng lưu mảng nhị phân .npy bằng save/load.
import numpy as np
# Path biểu diễn đường dẫn để ghép file bằng toán tử /.
from pathlib import Path
# TemporaryDirectory tạo thư mục tạm và tự dọn file khi khối with kết thúc.
from tempfile import TemporaryDirectory

# Mảng gốc ba số dùng làm dữ liệu thử lưu/đọc.
scores = np.array([3, 5, 7])
# with quản lý vòng đời thư mục, dọn sạch dù không cần lệnh xóa thủ công.
with TemporaryDirectory() as folder:
    # Path(folder) / 'scores.npy' ghép tên file vào thư mục tạm.
    file_path = Path(folder) / 'scores.npy'
    # np.save() lưu mảng trong định dạng .npy, giữ thông tin shape/dtype.
    np.save(file_path, scores)
    # np.load() đọc .npy thành ndarray; allow_pickle=False chặn dữ liệu pickle khi không cần object Python, an toàn hơn với tệp không tin cậy.
    restored = np.load(file_path, allow_pickle=False)
    # In mảng tải lại để đối chiếu trực quan với [3,5,7].
    print(restored)
```

**Kết quả khi chạy:**

```text
[3 5 7]
```

Mảng được ghi ra tệp `.npy` rồi đọc lại đủ ba phần tử. Thư mục tạm tự được dọn sau khi thoát khỏi `with`.

## 5. Năm tình huống NumPy — từ reshape đến lưu ma trận kiểm kê

### Tình huống 1 — Cấp 1: Đổi 10 số đo thành bảng 5 ngày × 2 ca

**Từ vựng trong mục:** **Reshape** — đổi hình dạng; **Shape** — kích thước.

**Tình huống thực tế:** Trạm quan trắc có **10 lần đo nhiệt độ**, tính bằng **°C**, theo đúng thứ tự: ca sáng rồi ca chiều của ngày 1, tiếp đến ca sáng rồi ca chiều của ngày 2, cho tới hết **5 ngày**. Người trực nhận được một dãy 10 số, chưa có hàng hoặc cột. Họ muốn đổi thành bảng **5 hàng ngày × 2 cột ca** để xem ngay hai kết quả của ngày thứ ba, mà không làm thay đổi hay mất một số đo nào.

**Vì sao chọn cách này?** `reshape(5, 2)` chỉ **đổi cách nhìn** dãy 10 số thành 5 hàng và 2 cột; nó không đo lại, tính thêm hoặc tự sắp xếp ngày. Số 2 là hai ca của một ngày, số 5 là số ngày: mỗi hai giá trị liên tiếp được ghép vào cùng hàng vì **dữ liệu ban đầu đã được ghi theo thứ tự sáng–chiều**. Khi đọc ngày thứ ba, phải chọn hàng có chỉ số `2` vì Python bắt đầu đếm từ 0. Nếu dãy đầu vào bị đảo thứ tự ca thì `reshape` không tự phát hiện; cần xác nhận thứ tự trước khi đổi hình dạng.

**Quy trình:**
1. Lưu 10 nhiệt độ theo trình tự ngày–ca.
2. Kiểm tra số phần tử đúng bằng 5 × 2.
3. Reshape và tra hàng ngày thứ ba bằng chỉ số 2.

**No Note — Không chú thích**

```python
import numpy as np
readings = np.array([26,27,25,28,29,24,26,30,27,25])
daily = readings.reshape(5, 2)
if readings.size != 10 or daily.size != 10:
    raise ValueError("Phải giữ đủ 10 lượt đo sau khi đổi dạng.")
print("Lượt đo:", readings.size)
print("Shape:", daily.shape)
print("Ngày 3 (sáng, chiều):", daily[2].tolist())
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Sắp 10 lượt đo thành 5 ngày, mỗi ngày hai lần sáng/chiều.
# Dữ liệu: 10 nhiệt độ °C, cứ hai giá trị liên tiếp tương ứng một ngày.
# NumPy tạo mảng và đổi shape của số đo.
import numpy as np
# 10 giá trị là 10 lượt liên tục theo thứ tự ngày.
readings = np.array([26,27,25,28,29,24,26,30,27,25])
# reshape(5,2) tạo 5 hàng ngày × 2 cột sáng/chiều, không đổi thứ tự hoặc tổng số ô.
daily = readings.reshape(5, 2)
# size là tổng 10 phần tử; daily.size vẫn 10 sau đổi dạng.
if readings.size != 10 or daily.size != 10:
    # ValueError báo dữ liệu hoặc kích thước sai và dừng thay vì cho kết luận sai.
    raise ValueError("Phải giữ đủ 10 lượt đo sau khi đổi dạng.")
# size là tổng 10 phần tử; daily.size vẫn 10 sau đổi dạng.
print("Lượt đo:", readings.size)
# shape trả tuple (5,2) chỉ rõ số ngày và số lần mỗi ngày.
print("Shape:", daily.shape)
# [2] lấy hàng ngày thứ ba (vì bắt đầu 0); tolist() đổi ndarray của hai lượt về list Python dễ đọc.
print("Ngày 3 (sáng, chiều):", daily[2].tolist())
```

**Kết quả khi chạy:**

```text
Lượt đo: 10
Shape: (5, 2)
Ngày 3 (sáng, chiều): [29, 24]
```

Ngày thứ ba lấy đúng lượt 5–6 trong dãy ban đầu; `reshape` không làm thay đổi giá trị nhiệt độ.

### Tình huống 2 — Cấp 2: Chuyển bảng 12 học viên × 3 môn sang bảng theo môn

**Từ vựng trong mục:** **Transpose** — chuyển vị; **Axis** — trục; **Column** — cột.

**Tình huống thực tế:** Phòng đào tạo nhận bảng điểm của **12 học viên H01–H12**. Mỗi hàng là một người, ba cột lần lượt là **Toán, Văn, Python**, đều theo thang **10 điểm**. Giáo viên muốn trình bày lại theo từng môn: mỗi hàng là một môn, 12 cột là 12 học viên; từ đó tính tổng điểm của từng môn trên cả lớp. Bảng mới vẫn phải chứa đủ **36 ô điểm** của bảng ban đầu.

**Vì sao chọn cách này?** **Chuyển vị** (`.T`) nghĩa là đổi **hàng thành cột và cột thành hàng**: bảng 12 học viên × 3 môn trở thành bảng 3 môn × 12 học viên, nhưng từng điểm vẫn ứng với đúng người và môn. Trên bảng mới, `sum(axis=1)` cộng **theo chiều ngang từng hàng**, tức cộng đủ 12 điểm của một môn. Nếu tiếp tục dùng `axis=0` như bảng ban đầu, kết quả trả theo học viên chứ không phải môn. Đây là cách thay góc nhìn để giải một câu hỏi khác, không phải cộng các môn vào làm một điểm.

**Quy trình:**
1. Tạo bảng điểm 12 × 3 và kiểm tra thứ tự cột.
2. Chuyển vị bằng `.T` và xác nhận shape 3 × 12.
3. Cộng từng hàng đã chuyển vị để lấy tổng mỗi môn.

**No Note — Không chú thích**

```python
import numpy as np
scores = np.array([[6,7,5],[7,9,8],[8,7,5],[9,9,8],[10,7,5],[6,9,8],[7,7,5],[8,9,8],[9,7,5],[10,9,8],[6,7,5],[7,9,8]], dtype=int)
by_subject = scores.T
if scores.shape != (12, 3) or by_subject.shape != (3, 12):
    raise ValueError("Chuyển vị phải đổi bảng 12 học viên, 3 môn thành 3 hàng, 12 cột.")
print("Học viên:", scores.shape[0])
print("Sau chuyển vị:", by_subject.shape)
print("Tổng ba môn:", by_subject.sum(axis=1).tolist())
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Chuyển bảng điểm 12 học viên × 3 môn thành bảng mỗi môn một hàng và tính tổng môn.
# Dữ liệu: 12 hàng học viên, 3 cột môn, điểm trên thang 10.
# NumPy hỗ trợ chuyển vị và cộng theo trục.
import numpy as np
# dtype=int giữ điểm nguyên; bảng gốc shape (12,3).
scores = np.array([[6,7,5],[7,9,8],[8,7,5],[9,9,8],[10,7,5],[6,9,8],[7,7,5],[8,9,8],[9,7,5],[10,9,8],[6,7,5],[7,9,8]], dtype=int)
# Thuộc tính .T chuyển bảng thành (3,12): ba hàng môn, mỗi hàng 12 điểm.
by_subject = scores.T
# shape trả kích thước (12,3); sau chuyển vị là (3,12).
if scores.shape != (12, 3) or by_subject.shape != (3, 12):
    # ValueError báo dữ liệu hoặc kích thước sai và dừng thay vì cho kết luận sai.
    raise ValueError("Chuyển vị phải đổi bảng 12 học viên, 3 môn thành 3 hàng, 12 cột.")
# shape trả kích thước (12,3); sau chuyển vị là (3,12).
print("Học viên:", scores.shape[0])
print("Sau chuyển vị:", by_subject.shape)
# axis=1 cộng toàn bộ 12 cột học viên trong TỪNG hàng môn; tolist() đổi ba tổng sang list Python để in.
print("Tổng ba môn:", by_subject.sum(axis=1).tolist())
```

**Kết quả khi chạy:**

```text
Học viên: 12
Sau chuyển vị: (3, 12)
Tổng ba môn: [93, 96, 78]
```

Tổng trả theo thứ tự Toán, Văn, Python; thay trục mà không thay dữ liệu là mục đích chính của `transpose`.

### Tình huống 3 — Cấp 3: Nhân ma trận điểm 15 học viên với vector trọng số

**Từ vựng trong mục:** **Matrix multiplication** — nhân ma trận; **Vector** — vector; **Weights** — trọng số.

**Tình huống thực tế:** Một khóa học có **15 học viên**, mỗi người có ba điểm đánh giá: **lý thuyết, thực hành, dự án**, đều theo thang 10. Quy định minh họa tính điểm cuối với mức đóng góp tương ứng **20%, 30%, 50%**; dự án chiếm nhiều nhất. Giáo vụ cần tính đúng **một điểm tổng kết cho mỗi học viên** và đếm bao nhiêu người đạt **từ 8 điểm**, không lấy điểm của người này ghép với người khác.

**Vì sao chọn cách này?** **Trọng số** là phần đóng góp của từng loại điểm vào điểm cuối; ở đây lý thuyết góp 20%, thực hành 30% và dự án 50%, cộng lại thành 100%. Mỗi hàng của mảng là ba điểm của **cùng một học viên**. Phép nhân ma trận `@` áp cùng ba mức đóng góp lên từng hàng và trả về **15 điểm cuối**, mỗi người một điểm. Chẳng hạn người có điểm cao ở dự án sẽ được phần đóng góp lớn hơn tương ứng chính sách. Nếu gộp theo cột thay vì theo hàng, kết quả sẽ là điểm chung từng môn cho cả lớp chứ không phải điểm tổng kết từng người.

**Quy trình:**
1. Tạo ma trận có đúng 15 hàng và ba cột đánh giá.
2. Lưu vector trọng số theo cùng thứ tự, kiểm tra tổng trọng số bằng 1.
3. Nhân `@`, đếm số điểm tổng kết đạt 8 và in kết quả đầu.

**No Note — Không chú thích**

```python
import numpy as np
scores = np.array([[6,5,7],[7,7,8],[8,9,9],[9,6,10],[10,8,7],[6,5,8],[7,7,9],[8,9,10],[9,6,7],[10,8,8],[6,5,9],[7,7,10],[8,9,7],[9,6,8],[10,8,9]], dtype=float)
weights = np.array([0.2, 0.3, 0.5])
final = scores @ weights
if scores.shape != (15, 3) or final.shape != (15,):
    raise ValueError("Cần đủ 15 bộ điểm ba môn và 15 điểm tổng hợp.")
if not np.isclose(weights.sum(), 1.0):
    raise ValueError("Tổng trọng số ba môn phải bằng 1.")
print("Học viên:", len(final))
print(f"Điểm H01: {final[0]:.2f}")
print("Đạt từ 8:", int((final >= 8).sum()))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Dùng phép @ tính điểm trung bình có trọng số cho 15 học viên và kiểm tra tổng trọng số.
# Dữ liệu: 15 hàng học viên × 3 môn; trọng số giả định 0.2,0.3,0.5 cho ba môn tương ứng.
# NumPy thực hiện phép nhân ma trận nhanh trên toàn bộ bảng điểm.
import numpy as np
# dtype=float lưu bảng điểm dưới dạng số thực 15×3.
scores = np.array([[6,5,7],[7,7,8],[8,9,9],[9,6,10],[10,8,7],[6,5,8],[7,7,9],[8,9,10],[9,6,7],[10,8,8],[6,5,9],[7,7,10],[8,9,7],[9,6,8],[10,8,9]], dtype=float)
# Ba tỷ lệ là 20%,30%,50%; tổng bằng 1 tức 100% sức ảnh hưởng.
weights = np.array([0.2, 0.3, 0.5])
# @ nhân mỗi hàng 3 điểm với 3 trọng số và cộng; trả vector 15 điểm tổng hợp.
final = scores @ weights
# shape (15,) nghĩa 15 kết quả một chiều, một điểm cho một học viên.
if scores.shape != (15, 3) or final.shape != (15,):
    # ValueError báo dữ liệu hoặc kích thước sai và dừng thay vì cho kết luận sai.
    raise ValueError("Cần đủ 15 bộ điểm ba môn và 15 điểm tổng hợp.")
# weights.sum() cộng 3 trọng số; isclose() so với 1.0 có dung sai số thực, đáng tin hơn == tuyệt đối.
if not np.isclose(weights.sum(), 1.0):
    # ValueError báo dữ liệu hoặc kích thước sai và dừng thay vì cho kết luận sai.
    raise ValueError("Tổng trọng số ba môn phải bằng 1.")
print("Học viên:", len(final))
# [0] lấy kết quả H01; :.2f in hai chữ số thập phân.
print(f"Điểm H01: {final[0]:.2f}")
# So từng điểm với ngưỡng 8 tạo mask Boolean; sum() đếm số học viên đạt (True được tính là 1).
print("Đạt từ 8:", int((final >= 8).sum()))
```

**Kết quả khi chạy:**

```text
Học viên: 15
Điểm H01: 6.20
Đạt từ 8: 7
```

Đây là nhân ma trận thực sự: mười lăm điểm đầu ra tương ứng mười lăm học viên, không phải phép nhân 15 × 3 tạo ra 45 kết quả.

### Tình huống 4 — Cấp 4: Tái cấu trúc 18 số đo và lưu bản snapshot độc lập

**Từ vựng trong mục:** **Reshape** — đổi hình dạng; **Copy** — bản sao; **Transpose** — chuyển vị.

**Tình huống thực tế:** Nhà máy lưu **18 lượt ghi điện năng tiêu thụ**, mỗi lượt tính bằng **kWh**. Máy ghi lần lượt ba ca của ngày 1, ba ca của ngày 2… cho đến đủ **6 ngày**. Bộ phận vận hành cần xem mức cao nhất mỗi ngày, còn kiểm toán muốn một bảng khác xếp **ca thành hàng, ngày thành cột** để tiện đối chiếu. Họ sẽ thử sửa một ô trên bảng kiểm toán, nhưng bản dữ liệu ban đầu phải được giữ nguyên.

**Vì sao chọn cách này?** `reshape(6, 3)` nhóm cứ ba lượt đo liên tiếp thành **một ngày**, rồi có thể tìm mức cao nhất trong ba ca của từng ngày. **Chuyển vị** `.T` đổi góc nhìn thành **3 hàng ca × 6 cột ngày**. Tuy nhiên mảng chuyển vị có thể chỉ là một **view**, tức cách nhìn khác của cùng vùng dữ liệu, nên sửa nó có thể làm dữ liệu gốc đổi theo. `.copy()` tạo **bản độc lập** để kiểm toán thử hiệu chỉnh mà không ghi đè sổ đo ban đầu. Đây là lý do chương trình dùng `.T.copy()` thay vì chỉ `.T`.

**Quy trình:**
1. Tổ chức 18 số thành 6 ngày × 3 ca.
2. Tính giá trị lớn nhất theo hàng và chuyển vị để xem theo ca.
3. Sao chép bản chuyển vị, sửa thử một ô và kiểm chứng dữ liệu nguồn không thay đổi.

**No Note — Không chú thích**

```python
import numpy as np
values = np.array([16,19,22,25,28,18,21,24,27,17,20,23,26,16,19,22,25,28], dtype=int)
by_day = values.reshape(6, 3)
for_audit = by_day.T.copy()
original = int(by_day[0, 0])
for_audit[0, 0] = -1
if by_day.shape != (6, 3) or for_audit.shape != (3, 6):
    raise ValueError("Bảng dữ liệu phải có 6 ngày, 3 lượt và bản đối soát đã chuyển vị.")
if int(by_day[0, 0]) != original:
    raise ValueError("Chỉnh sửa bản đối soát không được thay đổi bản dữ liệu gốc.")
print("Lượt đo:", values.size)
print("Đối soát:", for_audit.shape)
print("Đỉnh 6 ngày:", by_day.max(axis=1).tolist())
print("Nguồn đầu:", int(by_day[0, 0]))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tạo bản đối soát chuyển vị độc lập từ 18 lượt đo để sửa bản đối soát không làm đổi nguồn.
# Dữ liệu: 18 giá trị được chia thành 6 ngày × 3 lượt; bản đối soát có 3 hàng lượt × 6 ngày.
# NumPy cho reshape(), chuyển vị .T và copy().
import numpy as np
# dtype=int lưu các số đo nguyên ban đầu.
values = np.array([16,19,22,25,28,18,21,24,27,17,20,23,26,16,19,22,25,28], dtype=int)
# reshape(6,3) nhóm 18 giá trị thành sáu hàng ngày, mỗi hàng ba lượt.
by_day = values.reshape(6, 3)
# .T đổi thành 3 hàng lượt × 6 cột ngày; .copy() tạo bộ nhớ độc lập, tránh thay đổi bản gốc qua view chuyển vị.
for_audit = by_day.T.copy()
# [0,0] lấy lượt thứ nhất ngày đầu; int() đổi scalar NumPy thành int Python để lưu kiểm chứng.
# Đối chiếu nguồn vẫn bằng giá trị original trước khi sửa bản copy.
original = int(by_day[0, 0])
# Thay số trong bản đối soát COPY để thử tính độc lập, không thay giá trị nguồn.
for_audit[0, 0] = -1
# shape (6,3) và (3,6) xác minh cấu trúc đã chuyển vị.
if by_day.shape != (6, 3) or for_audit.shape != (3, 6):
    # ValueError báo dữ liệu hoặc kích thước sai và dừng thay vì cho kết luận sai.
    raise ValueError("Bảng dữ liệu phải có 6 ngày, 3 lượt và bản đối soát đã chuyển vị.")
# [0,0] lấy lượt thứ nhất ngày đầu; int() đổi scalar NumPy thành int Python để lưu kiểm chứng.
# Đối chiếu nguồn vẫn bằng giá trị original trước khi sửa bản copy.
if int(by_day[0, 0]) != original:
    # ValueError báo dữ liệu hoặc kích thước sai và dừng thay vì cho kết luận sai.
    raise ValueError("Chỉnh sửa bản đối soát không được thay đổi bản dữ liệu gốc.")
print("Lượt đo:", values.size)
print("Đối soát:", for_audit.shape)
# max(axis=1) tìm đỉnh qua ba lượt CỦA MỖI NGÀY; tolist() chuyển sáu giá trị thành list Python.
print("Đỉnh 6 ngày:", by_day.max(axis=1).tolist())
# [0,0] lấy lượt thứ nhất ngày đầu; int() đổi scalar NumPy thành int Python để lưu kiểm chứng.
# Đối chiếu nguồn vẫn bằng giá trị original trước khi sửa bản copy.
print("Nguồn đầu:", int(by_day[0, 0]))
```

**Kết quả khi chạy:**

```text
Lượt đo: 18
Đối soát: (3, 6)
Đỉnh 6 ngày: [22, 28, 27, 23, 26, 28]
Nguồn đầu: 16
```

Dữ liệu theo ca là kWh mỗi lượt, không phải công suất tức thời. Bản chỉnh sửa `for_audit` độc lập với bảng gốc vì đã copy.

### Tình huống 5 — Cấp 5: Lưu và phục hồi mảng 20 kiểm kê theo hình dạng 5 × 4

**Từ vựng trong mục:** **np.save** — lưu mảng NPY; **np.load** — đọc mảng NPY; **Validation** — kiểm dữ liệu.

**Tình huống thực tế:** Kho kiểm kê **20 ngăn hàng**, sắp theo **5 kệ**, mỗi kệ **4 ngăn**. Mỗi số trong danh sách là lượng sản phẩm ở một ngăn; riêng ngăn thứ 14 ghi **-1** để báo rằng nhân viên kiểm kê nhập lỗi, **không phải tồn kho âm**. Người quản lý cần sắp 20 số vào bảng 5 × 4, đếm số ngăn có lượng hợp lệ, lưu bảng vào một tệp **NPY** tạm rồi đọc lại để kiểm tra tất cả số vẫn đúng và bảng không bị mất dạng.

**Vì sao chọn cách này?** **NPY** là định dạng lưu mảng riêng của NumPy; khác văn bản thông thường ở chỗ nó giữ cả **các giá trị, kiểu dữ liệu và hình dạng** bảng. `reshape(5, 4)` ghép đúng 20 ngăn thành năm hàng kệ và bốn cột ngăn, nhưng không tự nhận ra `-1` là số lượng sai: chương trình cần kiểm tra riêng và chỉ đếm ngăn hợp lệ. `np.save()` ghi bảng vào tệp; `np.load(..., allow_pickle=False)` đọc lại mà không bật chức năng đọc đối tượng Python không cần thiết. Dùng thư mục tạm để học viên có thể thử lưu và đọc mà không để tệp mẫu tồn tại lâu; sau khi đọc, so bảng với bản gốc để xác nhận không sai số.

**Quy trình:**
1. Tạo mảng 20 số theo vị trí, reshape thành 5 × 4.
2. Lưu `.npy` trong thư mục tạm, đọc lại với `allow_pickle=False`.
3. Xác nhận shape/kiểu và từng phần tử trùng bản gốc; chỉ tổng hợp 19 ô không âm.

**No Note — Không chú thích**

```python
from pathlib import Path
from tempfile import TemporaryDirectory
import numpy as np
values = np.array([10,17,24,11,18,25,12,19,26,13,20,27,14,-1,28,15,22,29,16,23], dtype=int)
stocks = values.reshape(5, 4)
with TemporaryDirectory() as folder:
    path = Path(folder) / "stock.npy"
    np.save(path, stocks)
    loaded = np.load(path, allow_pickle=False)
    if loaded.shape != (5, 4):
        raise ValueError("Tệp đã lưu phải chứa 5 hàng và 4 cột.")
    if not np.array_equal(loaded, stocks):
        raise ValueError("Dữ liệu đọc lại phải khớp dữ liệu đã lưu.")
    valid = loaded[loaded >= 0]
    print("Vị trí:", loaded.size)
    print("Shape:", loaded.shape)
    print("Ô hợp lệ:", valid.size)
    print("Tổng món hợp lệ:", int(valid.sum()))
    print("Giữ nguyên dữ liệu:", bool(np.array_equal(loaded, stocks)))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Lưu bảng kho 5×4 ra .npy và kiểm dữ liệu tải lại, chỉ tổng hợp ô tồn không âm.
# Dữ liệu: 20 ô tồn kho (5 hàng × 4 cột), -1 là ô dữ liệu sai cần loại khỏi tổng món.
# Path cho phép ghép vị trí lưu file bằng toán tử /.
from pathlib import Path
# TemporaryDirectory() tự tạo và dọn thư mục thử nghiệm.
from tempfile import TemporaryDirectory
# NumPy tạo, lưu, đọc và so sánh mảng số.
import numpy as np
# 20 giá trị, dtype=int lưu tồn kho dạng số nguyên, -1 là giá trị lỗi.
values = np.array([10,17,24,11,18,25,12,19,26,13,20,27,14,-1,28,15,22,29,16,23], dtype=int)
# reshape(5,4) sắp 20 ô thành 5 hàng và 4 cột, không đổi giá trị.
stocks = values.reshape(5, 4)
# with đảm bảo stock.npy không còn sau khi kết thúc thử nghiệm.
with TemporaryDirectory() as folder:
    # Ghép thư mục tạm với tên file stock.npy.
    path = Path(folder) / "stock.npy"
    # np.save() ghi mảng với shape và dtype vào file nhị phân .npy.
    np.save(path, stocks)
    # np.load() đọc mảng lại; allow_pickle=False tránh giải mã Python pickle không cần thiết.
    loaded = np.load(path, allow_pickle=False)
    if loaded.shape != (5, 4):
        # ValueError báo dữ liệu hoặc kích thước sai và dừng thay vì cho kết luận sai.
        raise ValueError("Tệp đã lưu phải chứa 5 hàng và 4 cột.")
    # array_equal() so shape và từng giá trị hai mảng sau ghi/đọc; khác so sánh == từng ô.
    if not np.array_equal(loaded, stocks):
        # ValueError báo dữ liệu hoặc kích thước sai và dừng thay vì cho kết luận sai.
        raise ValueError("Dữ liệu đọc lại phải khớp dữ liệu đã lưu.")
    # loaded >= 0 tạo mặt nạ True cho ô không âm; lập chỉ mục Boolean giữ giá trị hợp lệ, loại -1.
    valid = loaded[loaded >= 0]
    print("Vị trí:", loaded.size)
    print("Shape:", loaded.shape)
    # size trả số ô được giữ; valid.sum() cộng số món hợp lệ.
    print("Ô hợp lệ:", valid.size)
    print("Tổng món hợp lệ:", int(valid.sum()))
    # array_equal() so shape và từng giá trị hai mảng sau ghi/đọc; khác so sánh == từng ô.
    # bool() chuyển kết quả kiểm toàn mảng sang bool Python để hiển thị rõ True/False.
    print("Giữ nguyên dữ liệu:", bool(np.array_equal(loaded, stocks)))
```

**Kết quả khi chạy:**

```text
Vị trí: 20
Shape: (5, 4)
Ô hợp lệ: 19
Tổng món hợp lệ: 369
Giữ nguyên dữ liệu: True
```

Ngăn -1 được giữ lại trong file để kiểm toán, nhưng không đưa vào số lượng món hợp lệ. Chỉ đọc file NPY đáng tin cậy, không tải file không rõ nguồn.

## 6. Sai lầm thường gặp

- `reshape` chỉ thành công khi **tích các kích thước mới bằng số phần tử ban đầu**. Sáu giá trị tạo được bảng 2×3, không phải 4×2.
- `reshape` và `.T` không tương đương: reshape nhóm lại các phần tử theo thứ tự, transpose tráo vị trí theo trục.
- `A * B` nhân từng ô khi broadcast được; `A @ B` nhân ma trận theo chiều tương thích. Với ma trận 2×3, bên phải cần có 3 hàng.
- Phải xác định rõ hàng là học viên/ngày, cột là môn/giờ đo trước khi đọc kết quả.
- `np.save` tạo file thực; `array.tolist()` chỉ chuyển sang List, không ghi file. Không bật `allow_pickle=True` với dữ liệu không đáng tin.

## 7. Trắc nghiệm

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What does `reshape()` change? | `reshape()` thay đổi điều gì?**

A. The array's shape without changing its total element count | Hình dạng mảng mà không đổi số phần tử

B. Writes an array to an NPY file | Ghi mảng vào tệp NPY

C. Swaps rows and columns | Hoán đổi hàng và cột

D. Matrix multiplication | Phép nhân ma trận

**Đáp án: A**

**Giải thích:** reshape bố trí lại cùng các phần tử theo kích thước mới. Với sáu phần tử, đổi `(2,3)` thành `(3,2)` hợp lệ, nhưng đổi thành `(4,2)` thì không.


**Q2. What does `.T` do to a 2-D array? | `.T` làm gì với mảng 2-D?**

A. The array's shape without changing its total element count | Hình dạng mảng mà không đổi số phần tử

B. Writes an array to an NPY file | Ghi mảng vào tệp NPY

C. Matrix multiplication | Phép nhân ma trận

D. Swaps rows and columns | Hoán đổi hàng và cột

**Đáp án: D**

**Giải thích:** Chuyển vị tráo hai trục của ma trận. Với `[[1,2,3],[4,5,6]]`, chuyển vị tạo ba hàng lần lượt là `[1,4]`, `[2,5]`, `[3,6]`.


**Q3. What does `A @ B` mean for compatible matrices? | `A @ B` nghĩa là gì với các ma trận tương thích?**

A. Swaps rows and columns | Hoán đổi hàng và cột

B. Matrix multiplication | Phép nhân ma trận

C. The array's shape without changing its total element count | Hình dạng mảng mà không đổi số phần tử

D. Writes an array to an NPY file | Ghi mảng vào tệp NPY

**Đáp án: B**

**Giải thích:** Toán tử @ tuân theo quy tắc nhân ma trận chứ không nhân riêng từng ô. Nếu `A` có shape `(2,3)` và `B` là `(3,4)`, thì `A @ B` có shape `(2,4)`; dấu `*` lại nhân từng phần tử.


**Q4. What does `np.save()` do? | `np.save()` làm gì?**

A. Swaps rows and columns | Hoán đổi hàng và cột

B. Matrix multiplication | Phép nhân ma trận

C. Writes an array to an NPY file | Ghi mảng vào tệp NPY

D. The array's shape without changing its total element count | Hình dạng mảng mà không đổi số phần tử

**Đáp án: C**

**Giải thích:** NumPy lưu giá trị, shape và dtype ở định dạng NPY. Khác CSV văn bản, tệp NPY giữ thông tin riêng của NumPy để khôi phục đúng mảng.


**Q5. Which shape specifically has two rows and three columns? | Shape nào có đúng hai hàng và ba cột?**

A. `(3, 2)` | `(3, 2)`

B. `(2, 3)` | `(2, 3)`

C. `(6,)` | `(6,)`

D. `(2, 4)` | `(2, 4)`

**Đáp án: B**

**Giải thích:** Chiều thứ nhất là số hàng và chiều thứ hai là số cột: (2,3). Shape `(2,3)` có tổng sáu ô; `(3,2)` cũng sáu ô nhưng số hàng và cột đảo vị trí.


**Q6. What is the transpose shape of a `(2, 3)` matrix? | Chuyển vị ma trận `(2, 3)` có shape nào?**

A. `(2, 3)` | `(2, 3)`

B. `(2, 4)` | `(2, 4)`

C. `(3, 2)` | `(3, 2)`

D. `(6,)` | `(6,)`

**Đáp án: C**

**Giải thích:** Chuyển vị đảo kích thước hàng và cột. Ma trận `(2,3)` trở thành `(3,2)` sau `.T` vì mỗi cột cũ trở thành một hàng.


**Q7. What is the shape of `(2, 3) @ (3, 4)`? | Phép `(2, 3) @ (3, 4)` cho shape gì?**

A. `(3, 2)` | `(3, 2)`

B. `(2, 3)` | `(2, 3)`

C. `(2, 4)` | `(2, 4)`

D. `(6,)` | `(6,)`

**Đáp án: C**

**Giải thích:** Hai chiều trong cùng bằng 3, còn hai chiều ngoài là 2 và 4. Chiều chung bằng 3 được kết hợp khi nhân, còn hai chiều ngoài 2 và 4 được giữ trong kết quả.


**Q8. What shape has a one-dimensional array of six values? | Mảng một chiều có sáu giá trị có shape nào?**

A. `(3, 2)` | `(3, 2)`

B. `(2, 4)` | `(2, 4)`

C. `(2, 3)` | `(2, 3)`

D. `(6,)` | `(6,)`

**Đáp án: D**

**Giải thích:** Mảng phẳng sáu phần tử có một chiều độ dài sáu. Dấu phẩy trong `(6,)` biểu diễn shape một chiều; `(1,6)` mới có hai chiều.


**Q9. How does `reshape` differ from transpose? | reshape khác transpose ở đâu?**

A. Reshape regroups positions; transpose exchanges axes | Reshape nhóm lại vị trí; transpose đổi trục

B. Converts the array into Python lists or scalars | Chuyển mảng thành List hoặc số Python

C. `*` multiplies element-wise; `@` performs matrix multiplication | `*` nhân từng phần tử; `@` nhân ma trận

D. Reads the saved array | Đọc lại mảng đã lưu

**Đáp án: A**

**Giải thích:** reshape và transpose có thể cho cùng shape nhưng giá trị ở vị trí khác. Với `[[1,2,3],[4,5,6]]`, `reshape(3,2)` tạo các hàng `[1,2]`, `[3,4]`, `[5,6]`, còn `.T` cho `[1,4]`, `[2,5]`, `[3,6]`.


**Q10. How does `*` differ from `@` for numeric ndarrays? | `*` khác `@` thế nào với ndarray số?**

A. Reads the saved array | Đọc lại mảng đã lưu

B. `*` multiplies element-wise; `@` performs matrix multiplication | `*` nhân từng phần tử; `@` nhân ma trận

C. Reshape regroups positions; transpose exchanges axes | Reshape nhóm lại vị trí; transpose đổi trục

D. Converts the array into Python lists or scalars | Chuyển mảng thành List hoặc số Python

**Đáp án: B**

**Giải thích:** Dấu sao nhân theo phần tử, @ tuân quy tắc nhân ma trận. Với hai ma trận 2×2 toàn số một, `A * B` vẫn toàn số một, còn `A @ B` toàn số hai do cộng các tích theo hàng–cột.


**Q11. What does `np.load()` normally do for an NPY file? | `np.load()` làm gì với tệp NPY?**

A. Reads the saved array | Đọc lại mảng đã lưu

B. Reshape regroups positions; transpose exchanges axes | Reshape nhóm lại vị trí; transpose đổi trục

C. `*` multiplies element-wise; `@` performs matrix multiplication | `*` nhân từng phần tử; `@` nhân ma trận

D. Converts the array into Python lists or scalars | Chuyển mảng thành List hoặc số Python

**Đáp án: A**

**Giải thích:** load phục hồi mảng NumPy đã ghi. Với tệp NPY đáng tin cậy, `np.load(path)` khôi phục mảng; tránh bật pickle cho dữ liệu đối tượng chưa tin cậy.


**Q12. What does `array.tolist()` do? | `array.tolist()` làm gì?**

A. Converts the array into Python lists or scalars | Chuyển mảng thành List hoặc số Python

B. Reshape regroups positions; transpose exchanges axes | Reshape nhóm lại vị trí; transpose đổi trục

C. `*` multiplies element-wise; `@` performs matrix multiplication | `*` nhân từng phần tử; `@` nhân ma trận

D. Reads the saved array | Đọc lại mảng đã lưu

**Đáp án: A**

**Giải thích:** tolist chuyển biểu diễn dữ liệu trong bộ nhớ chứ không ghi tệp. Mảng hai chiều chuyển thành List lồng nhau, còn mảng không chiều chuyển thành giá trị vô hướng Python.


**Q13. What happens if you reshape six elements to `(4, 2)`? | Điều gì xảy ra nếu reshape sáu phần tử thành `(4, 2)`?**

A. `allow_pickle=False` | `allow_pickle=False`

B. Left columns and right rows | Số cột bên trái và số hàng bên phải

C. A ValueError due to incompatible element counts | Phát sinh ValueError vì số phần tử không khớp

D. Shape and dtype | Shape và dtype

**Đáp án: C**

**Giải thích:** Bảng 4×2 cần tám giá trị, không phải sáu. Shape `(4,2)` cần `4 × 2 = 8` ô, nên NumPy không thể phân bố đúng sáu phần tử hiện có vào shape này.


**Q14. What must match to multiply two matrices with `@`? | Muốn nhân hai ma trận bằng `@`, chiều nào phải khớp?**

A. `allow_pickle=False` | `allow_pickle=False`

B. Left columns and right rows | Số cột bên trái và số hàng bên phải

C. A ValueError due to incompatible element counts | Phát sinh ValueError vì số phần tử không khớp

D. Shape and dtype | Shape và dtype

**Đáp án: B**

**Giải thích:** Nhân ma trận yêu cầu hai chiều trong bằng nhau. Nếu `A` là `(m,n)` và `B` là `(n,p)`, phép nhân hợp lệ và trả shape `(m,p)`.


**Q15. Which option avoids loading pickled objects from an NPY file? | Tùy chọn nào tránh đọc đối tượng pickle trong file NPY?**

A. A ValueError due to incompatible element counts | Phát sinh ValueError vì số phần tử không khớp

B. Left columns and right rows | Số cột bên trái và số hàng bên phải

C. Shape and dtype | Shape và dtype

D. `allow_pickle=False` | `allow_pickle=False`

**Đáp án: D**

**Giải thích:** Tắt pickle an toàn hơn khi đọc dữ liệu số chưa tin cậy. Với `np.load(path, allow_pickle=False)`, mảng object cần pickle sẽ không được đọc, giúp giảm rủi ro chạy mã từ tệp không tin cậy.


**Q16. What does NPY preserve in addition to array values? | NPY lưu thêm gì ngoài các giá trị?**

A. `allow_pickle=False` | `allow_pickle=False`

B. A ValueError due to incompatible element counts | Phát sinh ValueError vì số phần tử không khớp

C. Shape and dtype | Shape và dtype

D. Left columns and right rows | Số cột bên trái và số hàng bên phải

**Đáp án: C**

**Giải thích:** NPY lưu thông tin để khôi phục cấu trúc và kiểu phần tử. Khác các dòng văn bản thường, shape và dtype được lưu để mảng số `(2,3)` khôi phục đúng cấu trúc.


**Q17. What is a 1-D dot product of two equal-length numeric vectors? | Tích vô hướng của hai vector một chiều bằng nhau độ dài là gì?**

A. The sum of pairwise products | Tổng các tích của từng cặp phần tử

B. A 3-by-3 identity matrix | Ma trận đơn vị 3×3

C. `dtype` | `dtype`

D. `shape` | `shape`

**Đáp án: A**

**Giải thích:** Tích vô hướng nhân các vị trí tương ứng rồi cộng kết quả. Với `[1,2]` và `[3,4]`, tích vô hướng bằng `1×3 + 2×4 = 11`, là một số đơn chứ không phải List.


**Q18. What does `np.eye(3)` create? | `np.eye(3)` tạo gì?**

A. `shape` | `shape`

B. The sum of pairwise products | Tổng các tích của từng cặp phần tử

C. `dtype` | `dtype`

D. A 3-by-3 identity matrix | Ma trận đơn vị 3×3

**Đáp án: D**

**Giải thích:** Ma trận đơn vị có 1 ở đường chéo và 0 ở vị trí khác. Đường chéo chính là `[1,1,1]`, còn sáu ô ngoài chéo đều bằng không; nó không phải ma trận toàn số một.


**Q19. Which property reports the array dimensions? | Thuộc tính nào cho biết kích thước các chiều?**

A. A 3-by-3 identity matrix | Ma trận đơn vị 3×3

B. The sum of pairwise products | Tổng các tích của từng cặp phần tử

C. `dtype` | `dtype`

D. `shape` | `shape`

**Đáp án: D**

**Giải thích:** shape liệt kê độ dài của từng trục mảng. Với mảng 2D ba hàng hai cột, `X.shape` là `(3,2)` chứ không phải kiểu dữ liệu.


**Q20. Which property reports element data type? | Thuộc tính nào cho biết kiểu phần tử?**

A. `shape` | `shape`

B. `dtype` | `dtype`

C. A 3-by-3 identity matrix | Ma trận đơn vị 3×3

D. The sum of pairwise products | Tổng các tích của từng cặp phần tử

**Đáp án: B**

**Giải thích:** dtype ghi kiểu số hoặc kiểu dữ liệu khác của phần tử. Ví dụ mảng số nguyên có dtype nguyên, mảng số thập phân có dtype thực; `shape` mới cho kích thước các chiều.

## 8. Nối bài tiếp theo

`ndarray → Reshape/Transpose → Matrix → Model Input`.
