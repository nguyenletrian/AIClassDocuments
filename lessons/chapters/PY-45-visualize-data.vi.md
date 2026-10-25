# PY-45 — Matplotlib: biểu đồ line, scatter và histogram


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Line chart** — biểu đồ đường; **Scatter plot** — biểu đồ phân tán.

`NumPy/Pandas → Visualization → EDA → PCA/ML`

**Học xong dùng để làm gì?** Dùng biểu đồ thể hiện phân phối, xu hướng và so sánh, ghi nhãn trục/đơn vị để đọc đúng kết quả.

**Kết nối kiến thức tiếp theo:** PY-46 tích hợp dữ liệu, xử lý, mô hình và trực quan hóa trong một dự án nhỏ.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| Line chart | biểu đồ đường | Biểu diễn thay đổi theo thứ tự thời gian |
| Scatter plot | biểu đồ phân tán | Mỗi cặp x,y tạo thành một điểm quan sát |
| Histogram | biểu đồ tần suất | Đếm số mẫu trong từng khoảng giá trị |
| Axis label | nhãn trục | Mô tả đại lượng và đơn vị trên trục |

## 3. Hàm và cách sử dụng

**Từ vựng trong mục:** **Function** — hàm; **Option** — tùy chọn.

| Cú pháp | Mục đích và lựa chọn |
|---|---|
| `plt.plot(x,y)` | Đường thay đổi theo thời gian; x,y có cùng số phần tử |
| `plt.scatter(x,y)` | Vẽ điểm từng mẫu từ hai đại lượng |
| `plt.hist(values,bins=...)` | Gom quan sát vào các khoảng (bins) |
| `plt.xlabel()/ylabel()/savefig()` | Ghi nhãn kèm đơn vị và lưu hình |

## 4. Khái niệm chính và liên quan

**Mạch kiến thức:** Khi đã có bảng số liệu, chọn biểu đồ phù hợp câu hỏi: line cho mốc có thứ tự, scatter cho cặp biến trên mỗi mẫu, histogram cho phân bố một biến số. Nhãn trục nối dữ liệu với ý nghĩa và đơn vị để người đọc không suy luận sai.

### 4.1. Line chart — Nối các mốc có thứ tự

**Từ vựng trong mục:** **Line chart — biểu đồ đường**.

Biểu đồ đường nối những điểm theo **thứ tự x**, thích hợp quan sát biến thiên doanh thu theo ngày. Ví dụ ba ngày 1,2,3 có doanh thu 10,15,12 nghìn đồng: trục x là ngày, trục y là nghìn đồng. Nối điểm cho thấy tăng rồi giảm; không có nghĩa tồn tại dữ liệu ở mọi thời điểm giữa hai ngày. `plt.plot(x,y)` yêu cầu hai dãy có cùng số phần tử.

```python
# Mục đích: Nối các mốc có thứ tự.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [10, 15, 12])
print(len(plt.gca().lines[0].get_xdata()))
plt.close()
```

**Kết quả khi chạy:**

```text
3
```

Biểu đồ đã nhận ba điểm, rồi đóng Figure; số 3 là số mốc, không phải doanh thu.

### 4.2. Scatter — Mỗi hàng là một cặp quan sát

**Từ vựng trong mục:** **Scatter plot — biểu đồ phân tán**.

Biểu đồ scatter đặt **mỗi mẫu thành một điểm (x,y)**. Ví dụ ba sinh viên học 2,4,6 giờ/tuần, có điểm 5,7,9: mỗi vị trí x ghép đúng điểm y của cùng học viên. Scatter giúp thấy liên hệ, nhưng không tự chứng minh học nhiều gây điểm cao. `plt.scatter` tạo các điểm riêng không nối đường như line chart.

```python
# Mục đích: Mỗi hàng là một cặp quan sát.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.scatter([2, 4, 6], [5, 7, 9])
print(len(plt.gca().collections[0].get_offsets()))
plt.close()
```

**Kết quả khi chạy:**

```text
3
```

Đã vẽ ba điểm đại diện ba sinh viên, giữ đúng cặp giờ học–điểm.

### 4.3. Histogram — Đếm số đo rơi vào các khoảng

**Từ vựng trong mục:** **Histogram — biểu đồ tần suất; Bin — khoảng**.

Histogram dùng **một dãy số** và chia trục giá trị thành các **bins**, rồi đếm số quan sát trong mỗi khoảng. Sáu điểm `[5,6,6,7,8,9]` chia bốn bins đều từ 5 đến 9 tạo tần suất `[1,2,1,2]`. Khác biểu đồ cột cho các loại (A,B,C), histogram phù hợp biến số liên tục hoặc có thứ tự giá trị và phụ thuộc độ rộng bins.

```python
# Mục đích: Đếm số đo rơi vào các khoảng.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

counts, edges, bars = plt.hist([5, 6, 6, 7, 8, 9], bins=[5, 6, 7, 8, 10])
print(counts.astype(int).tolist())
plt.close()
```

**Kết quả khi chạy:**

```text
[1, 2, 1, 2]
```

Bốn khoảng chứa lần lượt 1, 2, 1, 2 quan sát; khoảng cuối bao gồm cận phải.

### 4.4. Axis labels — Ghi rõ biến và đơn vị

**Từ vựng trong mục:** **Axis label — nhãn trục; Figure — hình**.

**Nhãn trục** cho biết đang đo gì: `Time (hours)` ở trục ngang và `Temperature (°C)` ở trục dọc. Không ghi đơn vị, người xem dễ nhầm giờ với phút hoặc độ C với độ F. `xlabel`/`ylabel` chỉ đổi chữ trên Figure, không tự đổi dữ liệu. Có thể lưu hình bằng `savefig` rồi đóng `close` để không giữ Figure trong bộ nhớ.

```python
# Mục đích: Ghi rõ biến và đơn vị.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.plot([1, 2], [22, 24])
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (C)')
print(plt.gca().get_xlabel())
plt.close()
```

**Kết quả khi chạy:**

```text
Time (hours)
```

Trục x được gắn đúng ý nghĩa thời gian; phải đặt cả y và đơn vị trước khi gửi biểu đồ.

## 5. Năm tình huống Matplotlib — từ đường 10 ngày đến hai đồ thị 20 cảm biến

### Tình huống 1 — Cấp 1: Vẽ biểu đồ đường cho doanh thu của 10 ngày

**Từ vựng trong mục:** **Line chart** — đồ thị đường; **X-axis** — trục ngang; **Savefig** — lưu hình.

**Tình huống thực tế:** Một cửa hàng ghi **10 ngày doanh thu**, mỗi hàng là ngày 1–10 và tổng tiền bán (triệu đồng/ngày). Muốn quan sát xu hướng tăng/giảm theo **thứ tự thời gian**, cần vẽ đường nối 10 điểm, gắn tên trục kèm đơn vị và lưu PNG để đưa vào báo cáo.

**Vì sao chọn cách này?** Line chart phù hợp mốc thời gian có thứ tự; `plt.plot(days, revenues)` nối từng cặp đúng hàng. `savefig()` tạo file xem được bên ngoài Python; môi trường tự động dùng backend Agg nên không bật cửa sổ.

**Quy trình:**
1. Tạo 10 giá trị doanh thu tương ứng 10 ngày.
2. Vẽ biểu đồ đường, tiêu đề và nhãn trục có đơn vị.
3. Lưu `sales_10_days.png`, kiểm 10 điểm trong đường và file tồn tại.

```python
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

days = list(range(1,11))
revenues = [10,12,11,14,15,14,17,18,16,20]
fig, ax = plt.subplots()
ax.plot(days, revenues, marker="o")
ax.set(title="Sales over 10 days", xlabel="Day", ylabel="Revenue (million VND)")
fig.tight_layout()
path = Path("sales_10_days.png")
fig.savefig(path, dpi=130)
points = len(ax.lines[0].get_xdata())
plt.close(fig)
if len(revenues) != 10:
    raise ValueError("Cần đủ 10 ngày doanh thu.")
print("Ngày:", len(days))
print("Điểm đường:", points)
print("Doanh thu ngày 10 (triệu đồng):", revenues[-1])
print("Đã lưu PNG:", path.is_file() and path.stat().st_size > 0)
```

**Kết quả khi chạy:**

```text
Ngày: 10
Điểm đường: 10
Doanh thu ngày 10 (triệu đồng): 20
Đã lưu PNG: True
```

Chạy code sẽ tạo **sales_10_days.png** trong thư mục làm việc. Điểm giữa hai ngày trên đường nối không có nghĩa cửa hàng đã ghi dữ liệu cho mọi thời khắc giữa hai ngày.

### Tình huống 2 — Cấp 2: Scatter 12 học viên để xem mối liên hệ giờ học–điểm

**Từ vựng trong mục:** **Scatter plot** — đồ thị phân tán; **Pair** — cặp quan sát.

**Tình huống thực tế:** Giảng viên có **12 học viên**, mỗi hàng lưu số giờ tự học (giờ/tuần) và điểm kiểm tra (thang 10). Cần đặt mỗi cặp (giờ, điểm) thành một dấu chấm; nếu hai học viên cùng số giờ thì vẫn là **hai bản ghi**, không được vô tình nối chúng thành đường thời gian.

**Vì sao chọn cách này?** `plt.scatter` vẽ từng quan sát riêng, có thể giúp thấy liên hệ xu hướng nhưng không chứng minh học nhiều **gây** điểm cao. Trục x/y ghi đơn vị tương ứng giúp không nhầm giờ với điểm.

**Quy trình:**
1. Ghi 12 giờ học và 12 điểm theo đúng cặp học viên.
2. Vẽ scatter với tên trục/đơn vị, không nối điểm.
3. Lưu `study_vs_score.png`, kiểm scatter thực sự chứa 12 hàng.

```python
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

hours = [1,2,2,3,3,4,4,5,5,6,7,8]
scores = [4,5,6,5,7,6,8,7,8,9,8,10]
fig, ax = plt.subplots()
points = ax.scatter(hours, scores)
ax.set(title="Study hours and score", xlabel="Study (hours/week)", ylabel="Score (0-10)")
ax.set_ylim(0, 11)
fig.tight_layout()
path = Path("study_vs_score.png")
fig.savefig(path, dpi=130)
count = len(points.get_offsets())
plt.close(fig)
if len(hours) != 12 or len(scores) != 12:
    raise ValueError("Cần đủ 12 học viên và 12 điểm.")
print("Học viên:", len(hours))
print("Điểm scatter:", count)
print("Đã lưu PNG:", path.is_file() and path.stat().st_size > 0)
```

**Kết quả khi chạy:**

```text
Học viên: 12
Điểm scatter: 12
Đã lưu PNG: True
```

Trùng vị trí scatter có thể che lên nhau; số điểm đếm từ dữ liệu nguồn và scatter không được hiểu là số vị trí **nhìn thấy bằng mắt**.

### Tình huống 3 — Cấp 3: Histogram 15 thời gian giao theo bốn khoảng phút

**Từ vựng trong mục:** **Histogram** — biểu đồ tần suất; **Bins** — các khoảng giá trị.

**Tình huống thực tế:** Một đơn vị giao nhận ghi **15 thời gian giao** (phút/chuyến). Người quản lý cần biết bao nhiêu chuyến nằm trong vùng 0–10, 10–20, 20–30, 30–40 phút để phân tích phân bố, thay vì nối thời gian các chuyến thành một đường dễ gây hiểu nhầm.

**Vì sao chọn cách này?** `plt.hist` chia trục phút thành **bins**, đếm số lượt trong từng khoảng. Cần xác định rõ bin trái đóng/phải mở (riêng bin cuối nhận cận phải) và tổng số lượt trong các cột phải bằng 15.

**Quy trình:**
1. Tạo 15 thời gian có số, định nghĩa ranh giới 0/10/20/30/40 phút.
2. Vẽ histogram, nhãn hai trục và lưu hình.
3. Kiểm tổng tần suất của bốn khoảng đúng 15 chuyến.

```python
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

minutes = [4,7,8,9,10,11,14,16,18,20,21,24,27,31,37]
fig, ax = plt.subplots()
counts, edges, bars = ax.hist(minutes, bins=[0,10,20,30,40], edgecolor="black")
ax.set(title="Delivery duration", xlabel="Duration (minutes)", ylabel="Number of trips")
fig.tight_layout()
path = Path("delivery_histogram.png")
fig.savefig(path, dpi=130)
plt.close(fig)
if len(minutes) != 15 or int(counts.sum()) != 15:
    raise ValueError("Cần đủ 15 chuyến trong các cột tần suất.")
print("Chuyến:", len(minutes))
print("Số khoảng:", len(counts))
print("Tần suất:", counts.astype(int).tolist())
print("Đã lưu PNG:", path.is_file() and path.stat().st_size > 0)
```

**Kết quả khi chạy:**

```text
Chuyến: 15
Số khoảng: 4
Tần suất: [4, 5, 4, 2]
Đã lưu PNG: True
```

Histogram khác biểu đồ cột danh mục: trục ngang biểu diễn **khoảng số phút**, không phải tên từng khách.

### Tình huống 4 — Cấp 4: Hai đường của 18 ngày: so sánh doanh thu hai chi nhánh

**Từ vựng trong mục:** **Legend** — chú giải; **Multiple series** — nhiều chuỗi; **Axis labels** — nhãn trục.

**Tình huống thực tế:** Doanh nghiệp có **18 ngày**, mỗi hàng lưu doanh thu (triệu đồng/ngày) của hai chi nhánh A/B cùng một ngày. Cần vẽ **hai đường** trên cùng trục thời gian, chú giải màu rõ ràng và lưu hình để so sánh, đồng thời kiểm không tráo ngày của A và B.

**Vì sao chọn cách này?** Biểu đồ đường đa chuỗi giúp so hình dạng hai dãy **cùng đơn vị** theo cùng mốc x. `legend()` phân biệt chi nhánh; thiếu chú giải sẽ khiến người xem không biết đường nào là A/B.

**Quy trình:**
1. Tạo 18 cặp doanh thu A/B, dùng chung dãy ngày 1–18.
2. Vẽ hai đường có label riêng, thêm legend và tên trục.
3. Lưu `branches_18_days.png` và kiểm mỗi đường có đúng 18 điểm.

```python
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

days = list(range(1,19))
branch_a = [10,12,14,13,15,17,16,18,20,19,21,23,22,24,26,25,27,29]
branch_b = [9,11,13,15,13,15,17,19,17,19,21,23,21,23,25,27,25,27]
fig, ax = plt.subplots()
ax.plot(days, branch_a, marker="o", label="Branch A")
ax.plot(days, branch_b, marker="s", label="Branch B")
ax.set(title="Branch revenue", xlabel="Day", ylabel="Revenue (million VND)")
ax.legend()
fig.tight_layout()
path = Path("branches_18_days.png")
fig.savefig(path, dpi=130)
count = []
for line in ax.lines:
    count.append(len(line.get_xdata()))
plt.close(fig)
if len(days) != 18 or len(branch_a) != 18 or len(branch_b) != 18:
    raise ValueError("Cần đủ 18 ngày và hai dãy doanh thu.")
print("Ngày:", len(days))
print("Đường:", len(count))
print("Điểm mỗi đường:", count)
print("A ngày 18:", branch_a[-1])
print("Đã lưu PNG:", path.is_file() and path.stat().st_size > 0)
```

**Kết quả khi chạy:**

```text
Ngày: 18
Đường: 2
Điểm mỗi đường: [18, 18]
A ngày 18: 29
Đã lưu PNG: True
```

Đồ thị cho thấy **xu hướng mô tả**, không tự chứng minh nguyên nhân doanh thu giữa hai chi nhánh chênh lệch.

### Tình huống 5 — Cấp 5: Vẽ hai biểu đồ cho 20 lượt cảm biến, tô điểm lệch chuẩn

**Từ vựng trong mục:** **Dashboard** — hai góc nhìn; **Residual** — sai lệch; **Highlight** — tô điểm cần xem.

**Tình huống thực tế:** Kỹ sư có **20 lượt đo cảm biến** ở 20 mức đầu vào x. Quy tắc hiệu chuẩn tham khảo cho tín hiệu dự kiến `y=2x+5` (đơn vị đo); có một lượt thứ 18 cao hơn quy tắc 30 đơn vị. Cần **vẽ scatter cùng đường tham chiếu và tô điểm cần rà soát**, bên cạnh histogram các sai số dư. Lưu PNG để kiểm tra trực quan mà không xóa dữ liệu ngoại lệ.

**Vì sao chọn cách này?** Scatter đối chiếu từng điểm với đường chuẩn, còn histogram cho thấy phân bố các sai số trên cả 20 lượt. Tạo hai đồ thị cạnh nhau giúp người mới liên hệ **vị trí bất thường** với **tần suất sai số**; ngưỡng >10 đơn vị chỉ là mức kỹ thuật giả lập.

**Quy trình:**
1. Tạo 20 cặp x/y và đường tham chiếu theo quy định hiệu chuẩn.
2. Tìm sai số, gắn cờ nếu trị tuyệt đối >10, vẽ scatter và đường chuẩn.
3. Vẽ histogram sai số ở ô thứ hai, gắn nhãn/trục, lưu hình và báo số điểm lệch.

```python
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], dtype=float)
observed = np.array([7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,71,43,45], dtype=float)
reference = 2*x + 5
residual = observed - reference
flagged = np.abs(residual) > 10
fig, (left,right) = plt.subplots(1,2,figsize=(10,4))
left.scatter(x,observed,label="Observed")
left.plot(x,reference,label="Reference")
left.scatter(x[flagged],observed[flagged],marker="x",s=90,label="Review")
left.set(xlabel="Input level",ylabel="Signal (units)",title="Measured vs reference")
left.legend()
right.hist(residual,bins=[-1,1,10,20,40],edgecolor="black")
right.set(xlabel="Residual (units)",ylabel="Count",title="Residual distribution")
fig.tight_layout()
path = Path("sensor_review_20.png")
fig.savefig(path,dpi=130)
plt.close(fig)
if len(x) != 20 or len(observed) != 20:
    raise ValueError("Cần đủ 20 mức đầu vào và tín hiệu đo.")
print("Lượt đo:", len(x))
print("Biểu đồ trong hình:", 2)
print("Điểm cần kiểm:", int(flagged.sum()))
flagged_ids = []
for i in np.flatnonzero(flagged):
    flagged_ids.append(f"M{i+1:02d}")
print("Mã cần kiểm:", ", ".join(flagged_ids))
print("Đã lưu PNG:", path.is_file() and path.stat().st_size > 0)
```

**Kết quả khi chạy:**

```text
Lượt đo: 20
Biểu đồ trong hình: 2
Điểm cần kiểm: 1
Mã cần kiểm: M18
Đã lưu PNG: True
```

Điểm M18 vẫn có mặt trên biểu đồ và dữ liệu đầu vào. Vượt ngưỡng minh họa chỉ là lý do kiểm tra nguồn đo, **không kết luận cảm biến hỏng**.

## 6. Sai lầm thường gặp

- Dùng line chart để nối dữ liệu không có thứ tự có thể tạo cảm giác xu hướng giả.
- Scatter phải ghép đúng x và y của **cùng hàng mẫu**; không suy ra nhân quả chỉ từ mối tương quan.
- Histogram phụ thuộc `bins`; ghi biên khoảng khi báo cáo.
- Biểu đồ thiếu đơn vị dễ khiến người xem nhầm thời gian, tiền hoặc nhiệt độ.
- Lưu PNG không thay thế việc lưu bảng dữ liệu gốc và script tạo hình.
- `matplotlib` là thư viện ngoài; với máy không có màn hình có thể dùng backend Agg và `close()` sau khi vẽ.

## 7. Trắc nghiệm

**Q1. What is a line chart best suited for? | Biểu đồ đường phù hợp gì?**

A. Showing changes across ordered positions | Thể hiện thay đổi theo các mốc có thứ tự

B. Individual paired x-y observations | Từng quan sát theo cặp x-y

C. Counts of numeric values within bins | Số quan sát số học trong từng khoảng

D. Naming variables and their units | Đặt tên đại lượng và đơn vị đo

**Đáp án: A**

**Giải thích:** Nối các mốc cho xu hướng, không đảm bảo có số đo giữa các mốc. Nếu dữ liệu là các loại không có thứ tự, biểu đồ cột phù hợp hơn việc nối đường.


**Q2. What does a scatter plot represent? | Scatter plot biểu diễn gì?**

A. Showing changes across ordered positions | Thể hiện thay đổi theo các mốc có thứ tự

B. Individual paired x-y observations | Từng quan sát theo cặp x-y

C. Counts of numeric values within bins | Số quan sát số học trong từng khoảng

D. Naming variables and their units | Đặt tên đại lượng và đơn vị đo

**Đáp án: B**

**Giải thích:** Mỗi điểm là x và y của cùng một bản ghi. Mảng x và y phải cùng thứ tự bản ghi, nếu không các điểm ghép sẽ sai.


**Q3. What does a histogram represent? | Histogram biểu diễn gì?**

A. Showing changes across ordered positions | Thể hiện thay đổi theo các mốc có thứ tự

B. Individual paired x-y observations | Từng quan sát theo cặp x-y

C. Counts of numeric values within bins | Số quan sát số học trong từng khoảng

D. Naming variables and their units | Đặt tên đại lượng và đơn vị đo

**Đáp án: C**

**Giải thích:** Histogram chia khoảng giá trị số, không giống biểu đồ cột loại. Đổi biên bins sẽ đổi số đếm; khi so histogram cần nêu rõ khoảng chia.


**Q4. What are axis labels for? | Nhãn trục để làm gì?**

A. Showing changes across ordered positions | Thể hiện thay đổi theo các mốc có thứ tự

B. Individual paired x-y observations | Từng quan sát theo cặp x-y

C. Counts of numeric values within bins | Số quan sát số học trong từng khoảng

D. Naming variables and their units | Đặt tên đại lượng và đơn vị đo

**Đáp án: D**

**Giải thích:** Nhãn tránh nhầm đơn vị thời gian, nhiệt độ hay tiền. Con số trên trục thiếu đơn vị khiến người xem không rõ ý nghĩa đo lường.


**Q5. Which function draws a line? | Hàm nào vẽ đường?**

A. `plt.plot(x,y)` | `plt.plot(x,y)`

B. `plt.scatter(x,y)` | `plt.scatter(x,y)`

C. `plt.hist(values,bins=...)` | `plt.hist(values,bins=...)`

D. `plt.savefig(path)` | `plt.savefig(path)`

**Đáp án: A**

**Giải thích:** plot nối điểm theo thứ tự đầu vào mặc định. Hàm vẽ đòi x,y tương ứng nhưng không tự kiểm dữ liệu có đúng ý nghĩa thực tế.


**Q6. Which function draws separate x-y points? | Hàm nào vẽ các điểm x-y riêng?**

A. `plt.plot(x,y)` | `plt.plot(x,y)`

B. `plt.scatter(x,y)` | `plt.scatter(x,y)`

C. `plt.hist(values,bins=...)` | `plt.hist(values,bins=...)`

D. `plt.savefig(path)` | `plt.savefig(path)`

**Đáp án: B**

**Giải thích:** scatter tạo dấu chấm riêng cho từng cặp quan sát. Đây là lựa chọn phù hợp khi các điểm là quan sát rời, không phải chuỗi thời gian cần nối.


**Q7. Which function draws histograms? | Hàm nào vẽ histogram?**

A. `plt.plot(x,y)` | `plt.plot(x,y)`

B. `plt.scatter(x,y)` | `plt.scatter(x,y)`

C. `plt.hist(values,bins=...)` | `plt.hist(values,bins=...)`

D. `plt.savefig(path)` | `plt.savefig(path)`

**Đáp án: C**

**Giải thích:** hist đếm trong từng khoảng rồi vẽ cột các khoảng số. `bins` xác định biên hoặc số khoảng; thay đổi tham số này làm thay đổi bản tóm tắt phân bố.


**Q8. Which function saves a figure? | Hàm nào lưu hình?**

A. `plt.plot(x,y)` | `plt.plot(x,y)`

B. `plt.scatter(x,y)` | `plt.scatter(x,y)`

C. `plt.hist(values,bins=...)` | `plt.hist(values,bins=...)`

D. `plt.savefig(path)` | `plt.savefig(path)`

**Đáp án: D**

**Giải thích:** savefig ghi hình đã vẽ ra tệp PNG. Phải lưu trước khi đóng Figure và kiểm đường dẫn cùng quyền ghi.


**Q9. Why should x and y have matching observation counts? | Vì sao x và y phải có số quan sát tương ứng?**

A. Each x needs its matching y | Mỗi x cần y tương ứng

B. Closes the current Figure | Đóng Figure hiện tại

C. Horizontal-axis label | Nhãn trục ngang

D. Vertical-axis label | Nhãn trục dọc

**Đáp án: A**

**Giải thích:** Không ghép được cặp khi thiếu phần tử tương ứng. Dãy lệch chiều có thể gây lỗi hoặc ghép sai đối tượng quan sát.


**Q10. What does `plt.close()` do? | `plt.close()` làm gì?**

A. Each x needs its matching y | Mỗi x cần y tương ứng

B. Closes the current Figure | Đóng Figure hiện tại

C. Horizontal-axis label | Nhãn trục ngang

D. Vertical-axis label | Nhãn trục dọc

**Đáp án: B**

**Giải thích:** Đóng giúp giải phóng tài nguyên và tránh mở nhiều hình. Nên đóng Figure sau khi xuất, nhất là trong vòng lặp tạo nhiều tệp.


**Q11. What does `plt.xlabel()` set? | `plt.xlabel()` đặt gì?**

A. Each x needs its matching y | Mỗi x cần y tương ứng

B. Closes the current Figure | Đóng Figure hiện tại

C. Horizontal-axis label | Nhãn trục ngang

D. Vertical-axis label | Nhãn trục dọc

**Đáp án: C**

**Giải thích:** Nó chỉ đổi chữ, không tự đổi dữ liệu hoặc đơn vị. Nhãn có ích nên ghi cả đại lượng và đơn vị như ngày hay giờ.


**Q12. What does `plt.ylabel()` set? | `plt.ylabel()` đặt gì?**

A. Each x needs its matching y | Mỗi x cần y tương ứng

B. Closes the current Figure | Đóng Figure hiện tại

C. Horizontal-axis label | Nhãn trục ngang

D. Vertical-axis label | Nhãn trục dọc

**Đáp án: D**

**Giải thích:** Nó mô tả y và nên kèm đơn vị. Trục nhiệt độ nên ghi rõ Celsius hoặc Fahrenheit, không chỉ ghi 'value'.


**Q13. How many markers represent three scatter records? | Ba bản ghi scatter tạo mấy điểm?**

A. Three | Ba

B. Yes, changing bins changes counts per interval | Có, đổi bins sẽ đổi số đếm theo khoảng

C. No, a categorical bar chart is clearer | Không, biểu đồ cột theo nhãn rõ hơn

D. No, association alone is insufficient | Không, chỉ liên hệ chưa đủ

**Đáp án: A**

**Giải thích:** Mỗi hàng tạo một điểm. Mỗi điểm tương ứng một sinh viên, không phải mỗi cột đặc trưng tạo một điểm.


**Q14. Do histogram counts depend on bin boundaries? | Số đếm histogram có phụ thuộc biên bins không?**

A. Three | Ba

B. Yes, changing bins changes counts per interval | Có, đổi bins sẽ đổi số đếm theo khoảng

C. No, a categorical bar chart is clearer | Không, biểu đồ cột theo nhãn rõ hơn

D. No, association alone is insufficient | Không, chỉ liên hệ chưa đủ

**Đáp án: B**

**Giải thích:** Cùng dữ liệu có thể được nhóm khác nhau. Chiều cao histogram thường là số lượng mẫu, không mặc nhiên là xác suất nếu chưa chuẩn hóa.


**Q15. Is a histogram appropriate for names A, B, C as categories? | Histogram có thích hợp trực tiếp cho nhãn A,B,C không?**

A. Three | Ba

B. Yes, changing bins changes counts per interval | Có, đổi bins sẽ đổi số đếm theo khoảng

C. No, a categorical bar chart is clearer | Không, biểu đồ cột theo nhãn rõ hơn

D. No, association alone is insufficient | Không, chỉ liên hệ chưa đủ

**Đáp án: C**

**Giải thích:** Histogram cần khoảng số thay vì tên loại. Cột phân loại so các nhóm tên; histogram dùng khoảng liên tục trên trục số.


**Q16. Can scatter points establish causation? | Scatter có chứng minh quan hệ nhân quả không?**

A. Three | Ba

B. Yes, changing bins changes counts per interval | Có, đổi bins sẽ đổi số đếm theo khoảng

C. No, a categorical bar chart is clearer | Không, biểu đồ cột theo nhãn rõ hơn

D. No, association alone is insufficient | Không, chỉ liên hệ chưa đủ

**Đáp án: D**

**Giải thích:** Biến khác hoặc cách lấy mẫu có thể tạo cùng xu hướng. Cần xem cách thiết kế nghiên cứu và yếu tố gây nhiễu trước khi nói một biến gây ra biến kia.


**Q17. What does backend Agg help with? | Backend Agg giúp gì?**

A. Rendering images without a GUI window | Kết xuất hình không cần cửa sổ GUI

B. Order and units of the time axis | Thứ tự và đơn vị trục thời gian

C. Array of bin counts | Mảng số lượng theo mỗi bin

D. No, it is a rendered image | Không, nó là ảnh được kết xuất

**Đáp án: A**

**Giải thích:** Agg phù hợp chạy script hàng loạt hoặc lưu hình trên server. Agg đặc biệt hữu ích cho kiểm thử tự động không cần màn hình đồ họa.


**Q18. What should be checked before interpreting a time plot? | Trước khi đọc biểu đồ thời gian cần kiểm gì?**

A. Rendering images without a GUI window | Kết xuất hình không cần cửa sổ GUI

B. Order and units of the time axis | Thứ tự và đơn vị trục thời gian

C. Array of bin counts | Mảng số lượng theo mỗi bin

D. No, it is a rendered image | Không, nó là ảnh được kết xuất

**Đáp án: B**

**Giải thích:** Sai thứ tự hoặc đơn vị khiến xu hướng bị hiểu sai. Nếu ngày bị xếp sai, đường nối có thể khiến người xem tưởng thời gian đi ngược.


**Q19. What does `plt.hist` return first? | `plt.hist` trả gì ở vị trí đầu?**

A. Rendering images without a GUI window | Kết xuất hình không cần cửa sổ GUI

B. Order and units of the time axis | Thứ tự và đơn vị trục thời gian

C. Array of bin counts | Mảng số lượng theo mỗi bin

D. No, it is a rendered image | Không, nó là ảnh được kết xuất

**Đáp án: C**

**Giải thích:** Giá trị trả về đầu là tần suất, phần sau là biên và đối tượng vẽ. Mảng biên trả về giúp xác định giá trị nào đóng góp vào từng khoảng đếm.


**Q20. Does a saved PNG retain an editable dataset automatically? | PNG lưu hình có tự chứa bảng dữ liệu có thể sửa không?**

A. Rendering images without a GUI window | Kết xuất hình không cần cửa sổ GUI

B. Order and units of the time axis | Thứ tự và đơn vị trục thời gian

C. Array of bin counts | Mảng số lượng theo mỗi bin

D. No, it is a rendered image | Không, nó là ảnh được kết xuất

**Đáp án: D**

**Giải thích:** Muốn tính lại và sửa biểu đồ cần lưu dữ liệu gốc riêng. Cần lưu script, nhãn và bảng số gốc để tái tạo lại biểu đồ khi cần.

## 8. Nối sang bài tiếp

`NumPy/Pandas → Visualization → EDA → PCA/ML`.
