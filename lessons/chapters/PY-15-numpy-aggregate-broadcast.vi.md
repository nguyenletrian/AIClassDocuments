# PY-15 — NumPy tổng hợp, axis và broadcasting


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Aggregate** — phép tổng hợp; **Axis** — trục tính.

`Index/Slice → Aggregate/Broadcast → Vectorization → AI`

**Học xong dùng để làm gì?** Tính trung bình, tổng và biến đổi hàng loạt các cột số có shape tương thích.

**Kết nối kiến thức tiếp theo:** PY-16 đổi shape, chuyển vị và nhân ma trận để xử lý dữ liệu dạng khối.

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
# Mục đích: Tổng hợp từ nhiều giá trị.
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
# Mục đích: Tổng hợp theo hàng hoặc cột.
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
# Mục đích: Áp dụng phép toán theo chiều tương thích.
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
# Mục đích: Tính trực tiếp trên mảng.
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

## 5. Năm tình huống Aggregate/Broadcast — tăng từ tổng một chiều đến báo cáo nhiều cột

### Tình huống 1 — Cấp 1: Tổng hợp doanh thu 10 ngày bằng sum/min/max

**Từ vựng trong mục:** **Aggregate** — tổng hợp; **Sum** — tổng; **Mean** — trung bình.

**Tình huống thực tế:** Cửa hàng ghi doanh thu trong **10 ngày**, mỗi phần tử là tổng doanh thu của một ngày (nghìn đồng/ngày). Quản lý cần tổng 10 ngày, trung bình/ngày và doanh thu thấp nhất/cao nhất để kiểm tra nhanh biến động.

**Vì sao chọn cách này?** NumPy thực hiện `sum`, `mean`, `min`, `max` trên một mảng số; chưa cần vòng lặp riêng cho mỗi phép tính. Mỗi chỉ số mang ý nghĩa khác nhau và không nên lẫn đơn vị.

**Quy trình:**
1. Tạo mảng 10 số doanh thu theo ngày.
2. Tính tổng, trung bình, nhỏ nhất và lớn nhất bằng phép tổng hợp.
3. In số quan sát và số liệu theo đơn vị đã nêu.

```python
import numpy as np
sales = np.array([120,145,130,160,180,140,155,175,190,165], dtype=float)
if sales.shape != (10,):
    raise ValueError("Cần đủ 10 ngày bán hàng.")
print("Ngày:", sales.size)
print("Tổng (nghìn đồng):", int(sales.sum()))
print(f"Trung bình/ngày: {sales.mean():.1f}")
print("Thấp nhất:", int(sales.min()))
print("Cao nhất:", int(sales.max()))
```

**Kết quả khi chạy:**

```text
Ngày: 10
Tổng (nghìn đồng): 1560
Trung bình/ngày: 156.0
Thấp nhất: 120
Cao nhất: 190
```

Đây là tổng hợp dãy 1 chiều: chỉ có mười số doanh thu, chưa có hàng–cột để chọn `axis`.

### Tình huống 2 — Cấp 2: Phân biệt trung bình theo môn và theo học viên

**Từ vựng trong mục:** **Axis 0** — theo cột; **Axis 1** — theo hàng; **Argmax** — chỉ số cực đại.

**Tình huống thực tế:** Lớp có **12 học viên** H01…H12, mỗi hàng ghi điểm Toán, Văn, Python (thang 10). Giáo viên muốn ba điểm trung bình theo môn để điều chỉnh môn học, đồng thời tìm học viên có **điểm trung bình ba môn cao nhất**.

**Vì sao chọn cách này?** `mean(axis=0)` tạo ba giá trị cho ba môn, còn `mean(axis=1)` tạo 12 giá trị cho 12 học viên. `argmax` tìm vị trí người có trung bình cao nhất; hai trục giải đáp hai câu hỏi quản lý khác nhau.

**Quy trình:**
1. Tạo bảng `(12,3)` và xác định rõ nghĩa hàng/cột.
2. Tính trung bình cột bằng `axis=0`, tính trung bình hàng bằng `axis=1`.
3. Tìm học viên có trung bình cao nhất và in kết quả có nhãn.

```python
import numpy as np
scores = np.array([[6,5,7],[7,6,9],[8,7,7],[9,8,9],[6,9,7],[7,5,9],[8,6,7],[9,7,9],[6,8,7],[7,9,9],[8,5,7],[9,6,9]], dtype=float)
by_subject = scores.mean(axis=0)
by_student = scores.mean(axis=1)
best = int(by_student.argmax())
if scores.shape != (12, 3):
    raise ValueError("Bảng phải có 12 học viên và 3 môn.")
print("Học viên:", scores.shape[0])
print(f"Toán: {by_subject[0]:.2f}")
print(f"Văn: {by_subject[1]:.2f}")
print(f"Python: {by_subject[2]:.2f}")
print("Điểm TB cao nhất:", f"H{best+1:02d}", f"{by_student[best]:.2f}")
```

**Kết quả khi chạy:**

```text
Học viên: 12
Toán: 7.50
Văn: 6.75
Python: 8.00
Điểm TB cao nhất: H04 8.67
```

Cả hai phép trung bình đều hợp lệ về toán nhưng **khác đối tượng**; khi chọn sai `axis`, báo cáo sẽ trả sai số lượng kết quả.

### Tình huống 3 — Cấp 3: Broadcast điểm cộng cho 15 học viên nhưng không vượt 10

**Từ vựng trong mục:** **Broadcasting** — cộng vector theo cột; **Clip** — giới hạn; **Vectorization** — tính hàng loạt.

**Tình huống thực tế:** Trường có **15 học viên**, mỗi hàng gồm điểm Toán và Python (thang 10). Quy định minh họa: Toán được cộng 1 điểm chuyên cần, Python được cộng 0,5 điểm; không môn nào vượt 10. Cần áp dụng đúng mức cộng cho từng cột và đếm học viên đạt điểm 10 ở ít nhất một môn.

**Vì sao chọn cách này?** Vector `[1,0.5]` có hai phần tử tương ứng hai cột, nên NumPy broadcast cùng vector cho **15 hàng**. `np.minimum(...,10)` chặn điểm vượt thang; cộng một số duy nhất cho cả hai môn là sai quy tắc.

**Quy trình:**
1. Tạo mảng 15 × 2 kiểu float và vector cộng theo môn.
2. Broadcast phép cộng cho mọi hàng rồi giới hạn bằng `np.minimum`.
3. Đếm số hàng có ít nhất một điểm đạt 10 và kiểm tra mảng gốc không bị sửa.

```python
import numpy as np
scores = np.array([[7,5],[8,6],[9,7],[10,8],[7,9],[8,10],[9,5],[10,6],[7,7],[8,8],[9,9],[10,10],[7,5],[8,6],[9,7]], dtype=float)
bonus = np.array([1.0, 0.5])
adjusted = np.minimum(scores + bonus, 10)
if scores.shape != (15, 2) or adjusted.shape != (15, 2):
    raise ValueError("Cần đúng 15 học viên với hai môn trước và sau cộng điểm.")
print("Học viên:", scores.shape[0])
print("Điểm H01 sau cộng:", f"{adjusted[0,0]:.1f}", f"{adjusted[0,1]:.1f}")
print("Đạt 10 ít nhất một môn:", int(np.any(adjusted == 10, axis=1).sum()))
print("Gốc H01:", f"{scores[0,0]:.1f}", f"{scores[0,1]:.1f}")
```

**Kết quả khi chạy:**

```text
Học viên: 15
Điểm H01 sau cộng: 8.0 5.5
Đạt 10 ít nhất một môn: 8
Gốc H01: 7.0 5.0
```

Đây là tính vector hóa theo cột: nhờ shape tương thích, cùng một vector hai mức cộng được áp dụng cho 15 học viên mà không phải viết 30 phép tính.

### Tình huống 4 — Cấp 4: Hiệu chỉnh 18 cảm biến ba kênh bằng broadcasting

**Từ vựng trong mục:** **Element-wise** — theo ô; **Calibration** — hiệu chỉnh; **nanmean** — trung bình bỏ ô thiếu.

**Tình huống thực tế:** Trạm có **18 mẫu đo** gồm ba kênh nhiệt độ °C, độ ẩm % và áp suất kPa, mỗi hàng là một lượt; hai lượt thiếu riêng số áp suất. Theo biên bản hiệu chỉnh giả lập, phải **cộng 0,5 °C**, **trừ 2 điểm phần trăm độ ẩm**, **cộng 1 kPa** tương ứng ba cột. Cần áp dụng đúng độ lệch trên cả bảng và tính trung bình sau hiệu chỉnh cho từng kênh mà không biến ô thiếu thành số.

**Vì sao chọn cách này?** Vector độ lệch `(3,)` broadcast lên bảng `(18,3)`. `np.nan` giữ vị trí đo thiếu, còn `np.nanmean(axis=0)` cho trung bình có ý nghĩa theo từng đơn vị; không cộng bừa ba cột với nhau.

**Quy trình:**
1. Tạo mảng `(18,3)` số thực, chuyển ô áp suất thiếu thành NaN.
2. Tạo vector ba độ lệch và broadcast phép cộng theo cột.
3. Tính ba trung bình sau hiệu chỉnh, đếm chính xác hai ô thiếu.

```python
import numpy as np
raw = [[20,50,100],[22,53,105],[24,56,110],[26,59,115],[28,62,None],[20,65,105],[22,50,110],[24,53,115],[26,56,100],[28,59,105],[20,62,110],[22,65,115],[24,50,100],[26,53,105],[28,56,None],[20,59,115],[22,62,100],[24,65,105]]
rows = []
for temp, humidity, pressure in raw:
    if pressure is None:
        clean_pressure = np.nan
    else:
        clean_pressure = pressure
    rows.append([temp, humidity, clean_pressure])
measurements = np.array(rows, dtype=float)
calibration = np.array([0.5, -2.0, 1.0])
corrected = measurements + calibration
means = np.nanmean(corrected, axis=0)
if corrected.shape != (18, 3):
    raise ValueError("Cần đủ 18 lượt đo và 3 thông số.")
print("Số mẫu:", corrected.shape[0])
print("Thiếu áp suất:", int(np.isnan(corrected[:, 2]).sum()))
print(f"Nhiệt độ (°C): {means[0]:.2f}")
print(f"Độ ẩm (%): {means[1]:.2f}")
print(f"Áp suất (kPa): {means[2]:.2f}")
```

**Kết quả khi chạy:**

```text
Số mẫu: 18
Thiếu áp suất: 2
Nhiệt độ (°C): 24.17
Độ ẩm (%): 55.50
Áp suất (kPa): 108.19
```

Mỗi độ lệch có **đơn vị riêng** và tác động đúng cột. Khi áp suất thiếu, kết quả vẫn thiếu sau cộng vector — đúng hơn là giả định có số đo.

### Tình huống 5 — Cấp 5: Phát hành báo cáo 20 cửa hàng với giá/ưu đãi theo cột

**Từ vựng trong mục:** **Broadcasting** — mở rộng theo cột; **Aggregation** — tổng hợp; **Axis** — trục tính.

**Tình huống thực tế:** Chuỗi bán lẻ có **20 cửa hàng** C01…C20; mỗi hàng ghi số món bán thuộc ba nhóm A/B/C (món). Giá niêm yết giả lập theo nhóm lần lượt **10, 20, 30 nghìn đồng/món**; chương trình áp dụng tỷ lệ thanh toán lần lượt **100%, 90%, 80%**. Cần tính tổng tiền sau ưu đãi của **từng cửa hàng**, tổng của cả 20 cửa hàng và tìm mã cửa hàng có doanh thu lớn nhất. Không coi ba cột là ba cửa hàng.

**Vì sao chọn cách này?** NumPy tự broadcast vector đơn giá và vector tỷ lệ `(3,)` lên bảng số lượng `(20,3)` để tính tiền đúng từng nhóm. `sum(axis=1)` trả 20 tổng theo cửa hàng và `argmax()` chọn hàng cao nhất; đây là một quy trình nhiều bước nhưng không cần lặp thủ công trên từng ô.

**Quy trình:**
1. Tạo mảng 20 × 3 số lượng theo thứ tự nhóm A/B/C.
2. Nhân với hai vector giá và tỷ lệ có thứ tự cột thống nhất.
3. Cộng `axis=1` để có 20 doanh thu; chọn cửa hàng cao nhất, cộng tổng toàn chuỗi và kiểm tra kích thước.

```python
import numpy as np
quantities = np.array([[1,2,1],[2,3,3],[3,4,5],[4,2,2],[1,3,4],[2,4,1],[3,2,3],[4,3,5],[1,4,2],[2,2,4],[3,3,1],[4,4,3],[1,2,5],[2,3,2],[3,4,4],[4,2,1],[1,3,3],[2,4,5],[3,2,2],[4,3,4]], dtype=float)
prices = np.array([10, 20, 30], dtype=float)  # nghìn đồng/món
pay_rates = np.array([1.0, 0.9, 0.8])
amounts = quantities * prices * pay_rates
per_shop = amounts.sum(axis=1)
peak = int(per_shop.argmax())
if amounts.shape != (20, 3) or per_shop.shape != (20,):
    raise ValueError("Cần đủ 20 cửa hàng, ba mặt hàng và doanh thu từng cửa hàng.")
print("Cửa hàng:", quantities.shape[0])
print(f"Tổng 20 cửa hàng (nghìn đồng): {per_shop.sum():.1f}")
print("Doanh thu lớn nhất:", f"C{peak+1:02d}", f"{per_shop[peak]:.1f}")
print(f"C01 (nghìn đồng): {per_shop[0]:.1f}")
```

**Kết quả khi chạy:**

```text
Cửa hàng: 20
Tổng 20 cửa hàng (nghìn đồng): 3002.0
Doanh thu lớn nhất: C03 222.0
C01 (nghìn đồng): 70.0
```

Đây là tổng hợp cao nhất: làm việc theo hàng và cột có đơn vị, áp giá/ưu đãi bằng broadcasting, rồi tổng hợp trên đúng trục. Dữ liệu minh họa không đại diện doanh thu thật.

## 6. Sai lầm thường gặp

- Với mảng hai chiều, `axis=0` tổng hợp **theo cột** (gom các hàng), còn `axis=1` tổng hợp **theo hàng** (gom các cột). Không đoán axis chỉ từ tên hàm.
- `sum`, `mean`, `max` có ý nghĩa khác nhau: tổng, trung bình và cực đại, không thể thay thế tùy tiện.
- Broadcasting chỉ hoạt động khi **shape tương thích**. Hai mảng có chiều không tương thích có thể phát sinh `ValueError`.
- Dấu `*` của NumPy nhân **từng phần tử**, không phải phép nhân ma trận `@`.
- Khi cộng điểm, phải áp dụng giới hạn tối đa nếu quy định yêu cầu, ví dụ `np.minimum(scores + 1, 10)`.

## 7. Trắc nghiệm

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is aggregation in NumPy? | Phép tổng hợp trong NumPy là gì?**

A. Reading every file in a folder | Đọc mọi file trong thư mục

B. Converting all arrays to strings | Đổi mọi mảng thành chuỗi

C. Creating a new class by inheritance | Tạo lớp con nhờ kế thừa

D. Combining multiple values into summary statistics | Kết hợp nhiều giá trị thành thống kê tổng hợp

**Đáp án: D**

**Giải thích:** Tổng hợp gộp nhiều giá trị số thành thống kê như `sum`, `mean` hoặc `max`. Với `[2, 4, 6]`, trung bình `4` tóm tắt ba giá trị thay vì giữ từng ô.


**Q2. How does `sum()` differ from `mean()`? | `sum()` khác `mean()` ra sao?**

A. Both always return the same result | Cả hai luôn bằng nhau

B. sum totals values; mean computes their average | sum cộng tổng; mean tính trung bình

C. sum sorts; mean deletes values | sum sắp xếp; mean xóa giá trị

D. mean returns the largest number | mean trả số lớn nhất

**Đáp án: B**

**Giải thích:** `sum` cộng tất cả giá trị được chọn, còn `mean` lấy tổng chia cho số giá trị. Với `[2, 4, 6]`, tổng bằng `12` nhưng trung bình bằng `4`; hai phép không thường bằng nhau.


**Q3. What does `max()` return? | `max()` trả về gì?**

A. The arithmetic average | Trung bình cộng

B. The sum of every negative value | Tổng các số âm

C. The largest value overall or along a specified axis | Giá trị lớn nhất toàn mảng hoặc theo trục được chỉ định

D. The number of columns only | Chỉ số cột

**Đáp án: C**

**Giải thích:** `max` chọn giá trị lớn nhất của mảng hoặc riêng theo trục được chỉ định. Với `[[1, 7], [5, 3]]`, cực đại toàn mảng là `7`, khác `mean` dùng để tính trung bình.


**Q4. In a 2-D array, what does `sum(axis=0)` return? | Trong mảng hai chiều, `sum(axis=0)` trả về gì?**

A. One sum per row | Một tổng cho mỗi hàng

B. One sum per column | Một tổng cho mỗi cột

C. Only the first row | Chỉ hàng đầu

D. A boolean mask | Mặt nạ Boolean

**Đáp án: B**

**Giải thích:** Với mảng 2D, `axis=0` gộp theo chiều hàng và để lại mỗi cột một kết quả. Với `[[1, 2], [3, 4]]`, tổng cột là `[4, 6]`, không phải tổng hàng `[3, 7]`.


**Q5. In a 2-D array, what does `sum(axis=1)` return? | Trong mảng hai chiều, `sum(axis=1)` trả về gì?**

A. The data type of values | Kiểu dữ liệu

B. One sum per column | Một tổng cho mỗi cột

C. Only a scalar index | Chỉ một chỉ số

D. One sum per row | Một tổng cho mỗi hàng

**Đáp án: D**

**Giải thích:** `axis=1` gộp các cột trong từng hàng. Với `[[1, 2], [3, 4]]`, `sum(axis=1)` cho tổng hàng `[3, 7]`; `axis=0` lại cho tổng theo cột.


**Q6. What does broadcasting allow? | Broadcasting cho phép làm gì?**

A. Automatically converting all arrays to CSV | Tự chuyển mọi mảng thành CSV

B. Operating on arrays with compatible shapes | Thực hiện phép toán trên các mảng có shape tương thích

C. Replacing a function with a class | Thay hàm bằng lớp

D. Using any shapes without restrictions | Dùng mọi shape không giới hạn

**Đáp án: B**

**Giải thích:** Broadcasting ghép các chiều có kích thước tương thích để tính theo phần tử mà không phải viết vòng lặp Python. Ví dụ ma trận `(2,3)` cộng được vector `(3,)` trên các hàng, nhưng vector `(2,)` không khớp chiều cuối bằng 3.


**Q7. Why does `a + 1` work on a numeric ndarray? | Vì sao `a + 1` hoạt động với ndarray số?**

A. The array is converted to a string | Mảng bị chuyển thành chuỗi

B. Only the first element is changed | Chỉ phần tử đầu thay đổi

C. The scalar broadcasts to every array element | Số 1 được broadcast tới từng phần tử

D. It performs matrix multiplication | Nó nhân ma trận

**Đáp án: C**

**Giải thích:** Số đơn không có trục mảng gây xung đột nên NumPy broadcast nó tới mọi phần tử. Với `a=[2,4]`, `a + 1` cho `[3,5]`, không phải nhân ma trận hay chỉ sửa phần tử đầu.


**Q8. Which pair of trailing dimensions is broadcast-compatible? | Hai chiều cuối nào tương thích broadcasting?**

A. Only both zero | Chỉ khi cùng bằng 0

B. Equal sizes or one size equal to 1 | Bằng nhau hoặc một chiều có kích thước 1

C. Always 2 and 3 | Luôn là 2 và 3

D. Any unrelated positive sizes | Hai số dương bất kỳ

**Đáp án: B**

**Giải thích:** NumPy đối chiếu các chiều từ phải sang trái: mỗi cặp phải bằng nhau hoặc một bên có kích thước `1`. Vì vậy chiều `3` và `1` tương thích, còn `3` và `2` trên cùng trục thường không tương thích.


**Q9. What happens for incompatible broadcast shapes? | Điều gì xảy ra khi hai shape không tương thích broadcasting?**

A. A ValueError is generally raised | Thường phát sinh ValueError

B. NumPy always returns None | NumPy luôn trả None

C. NumPy silently discards extra rows | NumPy tự bỏ hàng thừa

D. A CSV file is created | Một file CSV được tạo

**Đáp án: A**

**Giải thích:** Shape không tương thích không thể ghép cho phép toán theo phần tử, nên NumPy thường gây `ValueError`. Ví dụ cộng `(2,3)` với `(2,)` lỗi vì hai chiều cuối 3 và 2 không khớp.


**Q10. What is vectorization? | Vectorization là gì?**

A. Removing all calculations | Loại bỏ mọi phép tính

B. Applying numerical operations to arrays directly | Áp dụng phép toán số trực tiếp lên mảng

C. Turning every number into a set | Biến mọi số thành Set

D. Manually printing each item | Tự in từng phần tử

**Đáp án: B**

**Giải thích:** Vector hóa áp dụng phép toán trực tiếp trên mảng NumPy thay vì viết vòng lặp Python qua từng phần tử. Ví dụ `a * 2` nhân mọi ô số, còn tổng hợp như `a.sum()` gộp chúng thành một thống kê.


**Q11. What does NumPy `a * b` do for equal-shaped numeric arrays? | NumPy `a * b` làm gì với hai mảng số cùng shape?**

A. Multiply corresponding elements | Nhân các phần tử cùng vị trí

B. Concatenate the arrays | Nối hai mảng

C. Always compute matrix multiplication | Luôn nhân ma trận

D. Compare the shapes only | Chỉ so sánh shape

**Đáp án: A**

**Giải thích:** Với mảng số NumPy, `*` nhân các ô tương ứng và có thể dùng broadcasting. Vì vậy hai mảng `[2,3]` và `[4,5]` nhân theo phần tử cho `[8,15]`; phép nhân ma trận dùng `@`.


**Q12. Which operator is used for matrix multiplication? | Toán tử nào dùng để nhân ma trận?**

A. `and` | `and`

B. `%` | `%`

C. `@` | `@`

D. `*` alone | Chỉ `*`

**Đáp án: C**

**Giải thích:** Toán tử `@` thực hiện nhân ma trận theo quy tắc đại số tuyến tính, kết hợp hàng với cột. Khác `*`, nó không chỉ nhân các phần tử ở cùng vị trí.


**Q13. For finite numeric array values, what does `np.minimum(a, 10)` do? | Với mảng chứa các giá trị số hữu hạn, `np.minimum(a, 10)` làm gì?**

A. Sum all values and multiply by 10 | Cộng tổng rồi nhân 10

B. Select the largest value only | Chỉ chọn số lớn nhất

C. Remove every element below 10 | Xóa mọi phần tử dưới 10

D. Cap each value at 10 | Giới hạn mỗi giá trị tối đa 10

**Đáp án: D**

**Giải thích:** Với giá trị số hữu hạn, `np.minimum(a, 10)` so từng ô với 10 rồi lấy số nhỏ hơn. Vì vậy `[8,12]` thành `[8,10]`; nó không xóa phần tử nhỏ hơn 10.


**Q14. How does `np.min()` differ from `np.minimum()`? | `np.min()` khác `np.minimum()` thế nào?**

A. min performs sorting descending | min sắp xếp giảm dần

B. Both always return the same shape | Cả hai luôn trả cùng shape

C. min reduces values; minimum compares values element-wise | min tổng hợp lấy cực tiểu; minimum so từng phần tử

D. minimum reads files; min writes files | minimum đọc file, min ghi file

**Đáp án: C**

**Giải thích:** `np.min(a)` mặc định gộp nhiều giá trị thành một cực tiểu, hoặc lấy cực tiểu theo trục được chọn. `np.minimum(a,b)` so từng ô tương ứng có thể dùng broadcasting và thường trả mảng kết quả.


**Q15. For shape `(2,3)`, what is the shape of `sum(axis=1)`? | Với shape `(2,3)`, `sum(axis=1)` có shape nào?**

A. `(2,3)` | `(2,3)`

B. `(1,3)` | `(1,3)`

C. `(3,)` | `(3,)`

D. `(2,)` | `(2,)`

**Đáp án: D**

**Giải thích:** Ma trận shape `(2,3)` có hai hàng, mỗi hàng gồm ba số. `sum(axis=1)` cộng ba cột trong từng hàng, để lại hai tổng với shape `(2,)`.


**Q16. For shape `(2,3)`, what is the shape of `mean(axis=0)`? | Với shape `(2,3)`, `mean(axis=0)` có shape nào?**

A. `(3,2)` | `(3,2)`

B. `(2,3)` | `(2,3)`

C. `(2,)` | `(2,)`

D. `(3,)` | `(3,)`

**Đáp án: D**

**Giải thích:** Với mảng `(2,3)`, `mean(axis=0)` lấy trung bình qua hai hàng cho từng cột. Còn lại ba trung bình cột, nên shape kết quả mặc định là `(3,)`, không phải `(2,)`.


**Q17. Which expression adds a distinct offset to each column of a `(2,3)` matrix? | Biểu thức nào cộng một giá trị riêng cho mỗi cột của ma trận (2,3)?**

A. `X + np.array([1,2,3])` | `X + np.array([1,2,3])`

B. `X.shape + 1` | `X.shape + 1`

C. `X @ np.array([1,2,3])` | `X @ np.array([1,2,3])`

D. `X + np.array([1,2])` | `X + np.array([1,2])`

**Đáp án: A**

**Giải thích:** Vector bù dài ba khớp chiều cuối gồm ba cột của ma trận `(2,3)`. Broadcasting cộng `[1,2,3]` vào cả hai hàng, mỗi cột một mức riêng; vector dài hai không khớp chiều ba.


**Q18. Which statement about broadcasting is correct? | Phát biểu nào đúng về broadcasting?**

A. It may apply a smaller operand without physically copying it | Nó có thể áp toán hạng nhỏ mà không cần sao chép vật lý

B. It permanently changes the array shape in every case | Nó luôn thay shape vĩnh viễn

C. It always duplicates the entire array in memory first | Nó luôn sao chép toàn mảng trước

D. It requires writing explicit for loops | Nó bắt buộc viết vòng for

**Đáp án: A**

**Giải thích:** Broadcasting có thể tái sử dụng toán hạng nhỏ trên các chiều tương thích mà không cần nhân bản vật lý toàn bộ dữ liệu trước. Nó khác việc phải viết vòng lặp hoặc đổi shape của đầu vào vĩnh viễn.


**Q19. How do aggregation and vectorization differ? | Aggregation khác vectorization thế nào?**

A. Aggregation summarizes values; vectorization operates over arrays | Aggregation tổng hợp giá trị; vectorization tính trực tiếp trên mảng

B. Both mean sorting only | Cả hai chỉ là sắp xếp

C. Aggregation never uses NumPy | Aggregation không bao giờ dùng NumPy

D. Vectorization must reduce to one number | Vectorization luôn phải trả một số

**Đáp án: A**

**Giải thích:** Tổng hợp gộp các giá trị thành thống kê, thường giảm một trục, còn phép toán vector hóa tính trực tiếp trên nhiều ô. Ví dụ `a.mean()` tóm tắt dữ liệu, còn `a * 2` biến đổi từng phần tử.


**Q20. Why should data meaning be known before choosing `axis`? | Vì sao phải hiểu ý nghĩa dữ liệu trước khi chọn `axis`?**

A. It avoids specifying array shape | Nó giúp khỏi nêu shape

B. It ensures every value is positive | Nó bảo đảm mọi giá trị dương

C. It determines whether rows or columns answer the question | Nó quyết định cần tổng hợp theo hàng hay cột

D. It changes Python syntax rules | Nó đổi quy tắc cú pháp Python

**Đáp án: C**

**Giải thích:** Chọn trục đúng phụ thuộc ý nghĩa hàng và cột. Nếu hàng là học viên, cột là môn, `mean(axis=0)` tính trung bình từng môn qua học viên, còn `mean(axis=1)` tính trung bình các môn của mỗi học viên.

## 8. Nối bài tiếp theo

`Index/Slice → Aggregate/Broadcast → Vectorization → AI`.
