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
# Mục đích: Vẽ đường nối ba mốc theo thứ tự, sau đó đọc lại dữ liệu trục x từ chính đối tượng đường vẽ.
# Dữ liệu: Ba mốc x=[1,2,3] và y=[10,15,12]; không lưu ảnh ra file, chỉ kiểm số điểm.
# Nhập thư viện Matplotlib để chọn backend trước khi nhập pyplot.
import matplotlib
# use('Agg') chọn backend Agg vẽ ảnh raster KHÔNG cần cửa sổ GUI, phù hợp Windows headless/CI; phải đặt TRƯỚC import pyplot.
matplotlib.use('Agg')
# Nhập thư viện Matplotlib để chọn backend trước khi nhập pyplot.
# pyplot là giao diện vẽ đồ thị dùng tên ngắn plt; các lệnh plt thao tác trên figure/axes hiện tại.
import matplotlib.pyplot as plt

# plt.plot(x,y) tạo Line2D nối ba cặp số theo THỨ TỰ x/y; không tự sắp hay nội suy thành dữ liệu quan sát mới.
plt.plot([1, 2, 3], [10, 15, 12])
# plt.gca() lấy Axes hiện tại (Get Current Axes); .lines là list các Line2D đã vẽ; [0] chọn đường đầu; .get_xdata() đọc ba tọa độ x gốc; len() đếm số tọa độ, không đếm số đoạn (2).
print(len(plt.gca().lines[0].get_xdata()))
# close() đóng figure hiện tại, giải phóng tài nguyên; không cần hiển thị cửa sổ với backend Agg.
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
# Mục đích: Vẽ scatter từ ba cặp x/y và đếm chính xác các điểm đã vẽ bằng get_offsets().
# Dữ liệu: Ba điểm (2,5), (4,7), (6,9), mỗi cặp là một quan sát độc lập.
# Nhập thư viện Matplotlib để chọn backend trước khi nhập pyplot.
import matplotlib
# use('Agg') chọn backend Agg vẽ ảnh raster KHÔNG cần cửa sổ GUI, phù hợp Windows headless/CI; phải đặt TRƯỚC import pyplot.
matplotlib.use('Agg')
# Nhập thư viện Matplotlib để chọn backend trước khi nhập pyplot.
# pyplot là giao diện vẽ đồ thị dùng tên ngắn plt; các lệnh plt thao tác trên figure/axes hiện tại.
import matplotlib.pyplot as plt

# scatter(x,y) vẽ điểm rời, không nối chúng thành đường như plot().
plt.scatter([2, 4, 6], [5, 7, 9])
# gca() lấy Axes hiện tại; collections[0] là PathCollection của scatter đầu tiên; get_offsets() trả mảng tọa độ shape (3,2); len() đếm BA điểm (hàng).
print(len(plt.gca().collections[0].get_offsets()))
# Đóng figure để tránh tích lũy đối tượng vẽ khi chạy nhiều ví dụ liên tiếp.
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
# Mục đích: Vẽ histogram với biên khoảng tự chọn, kiểm đếm tần suất ở mỗi khoảng.
# Dữ liệu: Sáu số đo 5,6,6,7,8,9; các mốc bins 5/6/7/8/10 tạo bốn khoảng.
# Nhập thư viện Matplotlib để chọn backend trước khi nhập pyplot.
import matplotlib
# use('Agg') chọn backend Agg vẽ ảnh raster KHÔNG cần cửa sổ GUI, phù hợp Windows headless/CI; phải đặt TRƯỚC import pyplot.
matplotlib.use('Agg')
# Nhập thư viện Matplotlib để chọn backend trước khi nhập pyplot.
# pyplot là giao diện vẽ đồ thị dùng tên ngắn plt; các lệnh plt thao tác trên figure/axes hiện tại.
import matplotlib.pyplot as plt

# hist(data,bins=...) phân số đo vào bốn khoảng [5,6),[6,7),[7,8),[8,10]; khoảng CUỐI bao gồm biên phải 10. Hàm trả (counts,edges,bars): số lượt mỗi khoảng, các ranh giới, các hình cột.
counts, edges, bars = plt.hist([5, 6, 6, 7, 8, 9], bins=[5, 6, 7, 8, 10])
# counts là ndarray float số lượt trong mỗi bin; astype(int) đổi sang số nguyên để in, tolist() đổi ndarray thành list Python; không biến thành dữ liệu gốc.
print(counts.astype(int).tolist())
# Đóng figure sau khi lấy counts, tránh giữ figure dư trong RAM.
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
# Mục đích: Gắn nhãn trục có đơn vị cho đường nhiệt độ theo thời gian, rồi đọc lại nhãn đã đặt.
# Dữ liệu: Hai thời điểm 1,2 giờ, nhiệt độ 22,24°C; trục x giờ và trục y độ C.
# Nhập thư viện Matplotlib để chọn backend trước khi nhập pyplot.
import matplotlib
# use('Agg') chọn backend Agg vẽ ảnh raster KHÔNG cần cửa sổ GUI, phù hợp Windows headless/CI; phải đặt TRƯỚC import pyplot.
matplotlib.use('Agg')
# Nhập thư viện Matplotlib để chọn backend trước khi nhập pyplot.
# pyplot là giao diện vẽ đồ thị dùng tên ngắn plt; các lệnh plt thao tác trên figure/axes hiện tại.
import matplotlib.pyplot as plt

# Vẽ hai cặp (thời gian giờ, nhiệt độ °C), nối hai mốc theo thứ tự.
plt.plot([1, 2], [22, 24])
# xlabel() đặt tên TRỤC x, ghi rõ đơn vị giờ để người đọc không nhầm với ngày.
plt.xlabel('Time (hours)')
# ylabel() đặt tên TRỤC y, đơn vị nhiệt độ độ C (chữ C trong nhãn).
plt.ylabel('Temperature (C)')
# gca() lấy Axes hiện tại, get_xlabel() đọc CHUỖI tên trục x để xác nhận đã gắn; không đọc dữ liệu đường.
print(plt.gca().get_xlabel())
# Đóng figure sau sử dụng để thu hồi bộ nhớ.
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

**Tình huống thực tế:** Cửa hàng lưu **doanh thu của 10 ngày liên tiếp**, ngày 1 đến ngày 10, mỗi số là **triệu đồng/ngày**. Người quản lý muốn biết doanh thu biến động ra sao theo đúng **thứ tự thời gian** và đọc doanh thu ngày cuối, thay vì chỉ nhìn một bảng 10 số. Cần tạo **biểu đồ đường**, ghi tên trục và lưu hình **PNG** để chèn vào báo cáo.

**Vì sao chọn cách này?** **Biểu đồ đường (line chart)** phù hợp khi trục ngang có **thứ tự thời gian**; nối các điểm liên tiếp giúp thấy ngày nào tăng hoặc giảm so với ngày trước. `ax.plot(days, revenues, marker='o')` ghép đúng **10 cặp ngày–doanh thu**, `ax.set` đặt tên trục **ngày** và **triệu đồng**, còn `savefig` ghi thành **tệp PNG**. `matplotlib.use('Agg')` chọn cách vẽ **không cần mở cửa sổ**, giúp chạy trong môi trường kiểm thử tự động; `plt.close(fig)` giải phóng hình sau khi lưu. Đường nối chỉ là cách hiển thị xu hướng giữa các ngày đã đo, không có nghĩa có dữ liệu thực tế ở mọi thời điểm nằm giữa.

**Quy trình:**
1. Tạo 10 giá trị doanh thu tương ứng 10 ngày.
2. Vẽ biểu đồ đường, tiêu đề và nhãn trục có đơn vị.
3. Lưu `sales_10_days.png`, kiểm 10 điểm trong đường và file tồn tại.

```python
# Mục đích: Vẽ biểu đồ đường doanh thu 10 ngày, lưu PNG và kiểm đủ 10 điểm dữ liệu.
# Dữ liệu: 10 ngày, doanh thu từng ngày đơn vị triệu VND; lưu ảnh sales_10_days.png vào thư mục làm việc hiện tại.
# Nhập thư viện Matplotlib để chọn backend trước khi nhập pyplot.
import matplotlib
# use('Agg') chuyển sang backend Agg không cần cửa sổ màn hình, tạo ảnh raster để lưu file; gọi TRƯỚC pyplot.
matplotlib.use("Agg")
# Nhập thư viện Matplotlib để chọn backend trước khi nhập pyplot.
# pyplot là giao diện vẽ đồ thị dùng tên ngắn plt; các lệnh plt thao tác trên figure/axes hiện tại.
import matplotlib.pyplot as plt
# Path cho thao tác tên file ảnh theo hệ điều hành và kiểm sự tồn tại/kích thước file.
from pathlib import Path

# range(1,11) tạo ngày 1..10, không lấy ngày 11; list() hiện thực dãy.
days = list(range(1,11))
# 10 giá trị doanh thu triệu đồng, khớp cùng vị trí với days.
revenues = [10,12,11,14,15,14,17,18,16,20]
# subplots() tạo (fig,ax): Figure là khung ảnh toàn bộ, Axes là vùng dữ liệu để vẽ.
fig, ax = plt.subplots()
# ax.plot() nối dữ liệu theo ngày; marker='o' thêm chấm tròn ngay các mốc quan sát, không thêm ngày mới.
ax.plot(days, revenues, marker="o")
# ax.set() đặt cùng lúc tiêu đề và nhãn trục; xlabel Day, ylabel Revenue (million VND) nêu đơn vị.
ax.set(title="Sales over 10 days", xlabel="Day", ylabel="Revenue (million VND)")
# tight_layout() điều chỉnh khoảng cách để tiêu đề/nhãn trục ít bị cắt khi lưu PNG.
fig.tight_layout()
# Path() là đường dẫn TƯƠNG ĐỐI theo cwd, không phải đường dẫn tuyệt đối hoặc thư mục tạm.
path = Path("sales_10_days.png")
# savefig() ghi ảnh PNG tới path; dpi=130 là mật độ điểm ảnh mỗi inch khi raster hóa, không phải số điểm dữ liệu.
fig.savefig(path, dpi=130)
# ax.lines chứa các Line2D; [0] là đường đầu, get_xdata() trả dãy ngày, len() đếm 10 tọa độ.
points = len(ax.lines[0].get_xdata())
# close(fig) đóng ĐÚNG Figure fig đã lưu để giải phóng tài nguyên dù file PNG vẫn còn trên đĩa.
plt.close(fig)
# Kiểm đủ 10 ngày doanh thu theo kịch bản; cũng nên giữ days khớp khi tạo dữ liệu khác.
if len(revenues) != 10:
    # Ném ValueError khi thiếu giá trị doanh thu, ngăn báo cáo số liệu chưa đủ.
    raise ValueError("Cần đủ 10 ngày doanh thu.")
print("Ngày:", len(days))
print("Điểm đường:", points)
# [-1] lấy phần tử cuối list doanh thu (ngày 10), không phải số ngày.
print("Doanh thu ngày 10 (triệu đồng):", revenues[-1])
# is_file() kiểm đường dẫn là file; stat().st_size đo byte >0 xác nhận file ảnh có nội dung, không chứng minh nội dung đẹp hay đúng ngữ nghĩa.
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

**Tình huống thực tế:** Giáo viên ghi **12 cặp dữ liệu học viên**. Mỗi người có **số giờ tự học (giờ/tuần)** và **điểm kiểm tra trên thang 10**, ví dụ hai học viên có cùng 2 giờ nhưng đạt điểm khác nhau. Giáo viên muốn quan sát điểm có xu hướng tăng khi giờ học tăng không, mà vẫn giữ **một dấu chấm cho mỗi người**; bảng không có chuỗi thời gian để nối các học viên thành đường.

**Vì sao chọn cách này?** **Scatter plot (biểu đồ phân tán)** đặt **một dấu chấm cho từng học viên**, với trục x là **giờ/tuần** và trục y là **điểm trên thang 10**. `ax.scatter(hours, scores)` tạo đúng 12 vị trí; hai học viên có cùng giờ học nhưng khác điểm vẫn là **hai quan sát**, không nên nối chúng thành đường thời gian. Tên trục kèm đơn vị giúp tránh việc hiểu 4 giờ như 4 điểm. Nếu các chấm có xu hướng đi lên, đó chỉ là **mối liên hệ trong mẫu**, chưa chứng minh tự học nhiều là **nguyên nhân duy nhất** khiến điểm cao.

**Quy trình:**
1. Ghi 12 giờ học và 12 điểm theo đúng cặp học viên.
2. Vẽ scatter với tên trục/đơn vị, không nối điểm.
3. Lưu `study_vs_score.png`, kiểm scatter thực sự chứa 12 hàng.

```python
# Mục đích: Vẽ scatter giữa giờ học và điểm của 12 học viên rồi lưu file PNG.
# Dữ liệu: 12 cặp (giờ học/tuần, điểm 0–10), có người trùng giờ học nhưng điểm khác nhau.
# Nhập thư viện Matplotlib để chọn backend trước khi nhập pyplot.
import matplotlib
# use('Agg') chuyển sang backend Agg không cần cửa sổ màn hình, tạo ảnh raster để lưu file; gọi TRƯỚC pyplot.
matplotlib.use("Agg")
# Nhập thư viện Matplotlib để chọn backend trước khi nhập pyplot.
# pyplot là giao diện vẽ đồ thị dùng tên ngắn plt; các lệnh plt thao tác trên figure/axes hiện tại.
import matplotlib.pyplot as plt
# Path() quản lý đường dẫn file ảnh và kiểm file đã ghi.
from pathlib import Path

# List 12 giờ học/tuần, mỗi vị trí là một học viên.
hours = [1,2,2,3,3,4,4,5,5,6,7,8]
# List 12 điểm 0–10 cùng vị trí với giờ học tương ứng.
scores = [4,5,6,5,7,6,8,7,8,9,8,10]
# Tạo Figure fig và vùng vẽ Axes ax để chỉnh nhãn/lưu.
fig, ax = plt.subplots()
# scatter() tạo PathCollection các chấm rời; `points` lưu đối tượng scatter, không phải list tọa độ số.
points = ax.scatter(hours, scores)
# Đặt tiêu đề và nhãn trục; x là giờ/tuần, y là điểm 0–10.
ax.set(title="Study hours and score", xlabel="Study (hours/week)", ylabel="Score (0-10)")
# set_ylim(ymin,ymax) khóa khoảng HIỂN THỊ trục y 0..11 để thấy cả điểm 10, không thay scores.
ax.set_ylim(0, 11)
# Chỉnh bố cục để tránh nhãn bị cắt ở mép PNG.
fig.tight_layout()
# Tên file tương đối so với thư mục làm việc hiện tại.
path = Path("study_vs_score.png")
# Lưu scatter thành PNG với dpi=130, không ảnh hưởng số học viên.
fig.savefig(path, dpi=130)
# PathCollection.get_offsets() trả tọa độ điểm shape (12,2); len() đếm 12 cặp thay vì đếm pixel ảnh.
count = len(points.get_offsets())
# Đóng figure để giải phóng đối tượng giao diện/đồ họa sau khi lưu.
plt.close(fig)
# or báo lỗi nếu MỘT trong hai list thiếu 12 phần tử; số học viên và điểm phải đồng bộ.
if len(hours) != 12 or len(scores) != 12:
    # Dừng trước khi báo cáo khi số lượt học không đủ.
    raise ValueError("Cần đủ 12 học viên và 12 điểm.")
print("Học viên:", len(hours))
print("Điểm scatter:", count)
# Kiểm có file PNG thật và số byte >0; không chỉ kiểm có tên file.
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

**Tình huống thực tế:** Đội giao nhận có **15 thời gian giao hàng**, tính bằng **phút/chuyến**, từ 4 đến 37 phút. Trưởng nhóm muốn biết có bao nhiêu chuyến thuộc từng **khoảng thời gian 0–10, 10–20, 20–30 và 30–40 phút** để hiểu phân bố nhanh/chậm. Họ không cần xem chuyến số mấy xảy ra trước; cần biểu đồ có tổng số lượt trong các cột vẫn bằng 15.

**Vì sao chọn cách này?** **Histogram (biểu đồ tần suất theo khoảng)** chia trục thời gian giao thành những **khoảng (bins)** rồi đếm **số chuyến** thuộc mỗi khoảng, không nối từng chuyến theo thứ tự. `ax.hist(minutes, bins=[0,10,20,30,40])` tạo **bốn cột**; với các khoảng kề nhau của Matplotlib, mốc 10 đi vào khoảng **10–20**, còn khoảng cuối nhận cả mốc phải 40. Cần kiểm `counts.sum()` bằng **15**, vì nếu một số nằm ngoài toàn bộ các khoảng thì có thể không được đếm. Trục ngang vẫn là **phút**, còn độ cao cột là **số lượt**, không phải doanh thu hoặc tổng phút.

**Quy trình:**
1. Tạo 15 thời gian có số, định nghĩa ranh giới 0/10/20/30/40 phút.
2. Vẽ histogram, nhãn hai trục và lưu hình.
3. Kiểm tổng tần suất của bốn khoảng đúng 15 chuyến.

```python
# Mục đích: Vẽ histogram 15 thời gian giao hàng trong bốn khoảng 0–10,10–20,20–30,30–40 phút.
# Dữ liệu: 15 chuyến giao phút, histogram đếm số chuyến theo khoảng, không biểu diễn trình tự thời gian.
# Nhập thư viện Matplotlib để chọn backend trước khi nhập pyplot.
import matplotlib
# use('Agg') chuyển sang backend Agg không cần cửa sổ màn hình, tạo ảnh raster để lưu file; gọi TRƯỚC pyplot.
matplotlib.use("Agg")
# Nhập thư viện Matplotlib để chọn backend trước khi nhập pyplot.
# pyplot là giao diện vẽ đồ thị dùng tên ngắn plt; các lệnh plt thao tác trên figure/axes hiện tại.
import matplotlib.pyplot as plt
# Dùng Path để đặt tên ảnh PNG và xác minh file được tạo.
from pathlib import Path

# List 15 độ dài chuyến giao hàng, đơn vị phút.
minutes = [4,7,8,9,10,11,14,16,18,20,21,24,27,31,37]
# Tạo Figure và Axes mới để không trộn biểu đồ với bài khác.
fig, ax = plt.subplots()
# hist() chia vào bốn khoảng [0,10),[10,20),[20,30),[30,40] (khoảng cuối gồm biên phải). Trả counts=tần suất, edges=mốc biên, bars=hình cột; edgecolor='black' vẽ viền đen, không đổi số liệu.
counts, edges, bars = ax.hist(minutes, bins=[0,10,20,30,40], edgecolor="black")
# Đặt tên biểu đồ, nhãn x là phút, y là số chuyến (tần suất), không phải mật độ khi không đặt density=True.
ax.set(title="Delivery duration", xlabel="Duration (minutes)", ylabel="Number of trips")
# Canh bố cục để nhãn/tiêu đề hiển thị đầy đủ.
fig.tight_layout()
# Tên PNG tương đối trong cwd hiện tại.
path = Path("delivery_histogram.png")
# Ghi histogram ra file PNG với dpi=130.
fig.savefig(path, dpi=130)
# Đóng figure sau lưu để không giữ ảnh dư trong bộ nhớ.
plt.close(fig)
# len() đếm 15 chuyến nguồn; counts.sum() cộng TẤT CẢ tần suất các bin, phải đủ 15 (các bin bao trùm mọi số đo).
if len(minutes) != 15 or int(counts.sum()) != 15:
    # Dừng nếu có lượt ngoài bin hoặc thiếu bản ghi.
    raise ValueError("Cần đủ 15 chuyến trong các cột tần suất.")
print("Chuyến:", len(minutes))
# Có một phần tử counts cho mỗi KHOẢNG, tức 4 khoảng, khác len(edges)=5 mốc biên.
print("Số khoảng:", len(counts))
# counts là ndarray số thực, astype(int) chuyển đếm lượt thành số nguyên để in; tolist() chuyển thành list Python.
print("Tần suất:", counts.astype(int).tolist())
# Kiểm ảnh PNG tồn tại và lớn hơn 0 byte.
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

**Tình huống thực tế:** Doanh nghiệp theo dõi **18 ngày liên tiếp**, mỗi ngày ghi doanh thu của **chi nhánh A và chi nhánh B** trên cùng ngày, cùng đơn vị **triệu đồng/ngày**. Giám đốc muốn so xu hướng tăng giảm của **hai chi nhánh trên chung một trục thời gian**, xem A đạt bao nhiêu vào ngày 18, và lưu hình có **chú giải nhận diện hai đường** để người xem không nhầm.

**Vì sao chọn cách này?** **Biểu đồ nhiều đường** là cách so hai dãy có **cùng mốc thời gian và đơn vị đo**: doanh thu A và B trên đủ 18 ngày. Hai lệnh `ax.plot(days, branch_a, label='Branch A')` và tương tự cho B dùng **cùng mảng ngày**, tránh làm lệch hàng dữ liệu. `ax.legend()` hiện **chú giải** để biết đường nào thuộc chi nhánh nào; các kiểu dấu khác nhau cũng hỗ trợ phân biệt điểm. Chương trình kiểm cả **hai đường đều có 18 điểm**, in doanh thu A ngày cuối rồi `savefig` lưu PNG. Đồ thị cho biết xu hướng quan sát, không chứng minh nguyên nhân khiến doanh thu chi nhánh nào đó tăng.

**Quy trình:**
1. Tạo 18 cặp doanh thu A/B, dùng chung dãy ngày 1–18.
2. Vẽ hai đường có label riêng, thêm legend và tên trục.
3. Lưu `branches_18_days.png` và kiểm mỗi đường có đúng 18 điểm.

```python
# Mục đích: So hai đường doanh thu trong 18 ngày, thêm legend và kiểm mỗi đường có đủ 18 điểm.
# Dữ liệu: 18 ngày, hai dãy doanh thu Branch A/B tính triệu VND; cả hai dùng cùng trục ngày.
# Nhập thư viện Matplotlib để chọn backend trước khi nhập pyplot.
import matplotlib
# use('Agg') chuyển sang backend Agg không cần cửa sổ màn hình, tạo ảnh raster để lưu file; gọi TRƯỚC pyplot.
matplotlib.use("Agg")
# Nhập thư viện Matplotlib để chọn backend trước khi nhập pyplot.
# pyplot là giao diện vẽ đồ thị dùng tên ngắn plt; các lệnh plt thao tác trên figure/axes hiện tại.
import matplotlib.pyplot as plt
# Path biểu diễn file xuất đồ thị theo đường dẫn tương đối.
from pathlib import Path

# Tạo ngày từ 1 tới 18, không lấy 19.
days = list(range(1,19))
# 18 số doanh thu chi nhánh A, đơn vị triệu VND.
branch_a = [10,12,14,13,15,17,16,18,20,19,21,23,22,24,26,25,27,29]
# 18 số doanh thu chi nhánh B, theo đúng thứ tự ngày như A.
branch_b = [9,11,13,15,13,15,17,19,17,19,21,23,21,23,25,27,25,27]
# Tạo Figure và Axes riêng cho biểu đồ hai đường.
fig, ax = plt.subplots()
# Vẽ đường A, marker='o' dùng điểm tròn, label đặt tên đường để legend tra được.
ax.plot(days, branch_a, marker="o", label="Branch A")
# Vẽ đường B, marker='s' là ô vuông, hai đường dùng chung trục x nhưng phân biệt nhãn.
ax.plot(days, branch_b, marker="s", label="Branch B")
# Đặt tiêu đề và nhãn đơn vị trục doanh thu triệu VND.
ax.set(title="Branch revenue", xlabel="Day", ylabel="Revenue (million VND)")
# legend() hiển thị chú giải lấy từ label của mỗi Line2D, không tự tạo dữ liệu.
ax.legend()
# Điều chỉnh khoảng cách nhãn và vùng hình trước khi lưu.
fig.tight_layout()
# Tên file PNG của biểu đồ hai chi nhánh trong cwd.
path = Path("branches_18_days.png")
# Lưu file ảnh PNG ở độ phân giải dpi=130.
fig.savefig(path, dpi=130)
# List rỗng ghi số mốc dữ liệu trên mỗi đường, không lưu tổng pixel.
count = []
# ax.lines là danh sách hai đối tượng Line2D đã vẽ; lặp qua từng đường.
for line in ax.lines:
    # get_xdata() lấy dãy x của Line2D tương ứng; len() đếm 18 ngày trên đường đó.
    # append() thêm số điểm của mỗi Line2D vào list để đối chiếu.
    count.append(len(line.get_xdata()))
# Đóng figure sau khi đọc các đường và lưu file, tránh rò rỉ bộ nhớ đồ họa.
plt.close(fig)
# or yêu cầu cả ba dãy ngày/A/B có đúng 18 phần tử.
if len(days) != 18 or len(branch_a) != 18 or len(branch_b) != 18:
    # Báo lỗi nếu bất kỳ dãy nào thiếu mốc, không tiếp tục báo cáo.
    raise ValueError("Cần đủ 18 ngày và hai dãy doanh thu.")
print("Ngày:", len(days))
print("Đường:", len(count))
print("Điểm mỗi đường:", count)
# [-1] là doanh thu ngày 18 của A, không phải doanh thu trung bình.
print("A ngày 18:", branch_a[-1])
# Xác minh file hình đã được ghi thực và không rỗng.
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

**Tình huống thực tế:** Trạm hiệu chuẩn lưu **20 lượt đo tín hiệu**, mỗi lượt có mức đầu vào x và mức tín hiệu thực tế. Quy tắc tham chiếu giả lập là **tín hiệu kỳ vọng tăng hai đơn vị cho mỗi một mức x và bắt đầu từ 5 đơn vị**. Lượt **M18** cao hơn tham chiếu 30 đơn vị, còn các lượt khác khớp. Kỹ thuật viên muốn một hình gồm **biểu đồ điểm đo so với đường tham chiếu** và **histogram sai số**, đồng thời đánh dấu mã cần rà soát mà không tự xóa lượt khác thường.

**Vì sao chọn cách này?** **Sai số dư (residual)** là số đo **thực tế trừ mức dự kiến** ở **cùng một x**. Chương trình tạo **hai biểu đồ cạnh nhau**: bên trái `scatter` cho 20 điểm thực tế cùng đường tham chiếu, đồng thời tô dấu những điểm có **độ lớn sai số vượt 10 đơn vị**; bên phải `hist` gom sai số thành các khoảng để nhìn số lượt sai lệch nhỏ/lớn. Với dữ liệu này, **M18** có sai số +30 nên bị gắn cờ, nhưng chưa kết luận cảm biến hỏng: cần xem lại phép đo. `np.flatnonzero(flagged)` trả vị trí chỉ số **bắt đầu từ 0**, phải cộng 1 để ra mã M01…; `plt.subplots(1,2)` và `savefig` cho một PNG báo cáo, `Agg` tránh yêu cầu màn hình. Histogram bổ sung góc nhìn về **tần suất sai số**, không thay bảng đo hay xóa ngoại lệ.

**Quy trình:**
1. Tạo 20 cặp x/y và đường tham chiếu theo quy định hiệu chuẩn.
2. Tìm sai số, gắn cờ nếu trị tuyệt đối >10, vẽ scatter và đường chuẩn.
3. Vẽ histogram sai số ở ô thứ hai, gắn nhãn/trục, lưu hình và báo số điểm lệch.

```python
# Mục đích: Tạo hình hai biểu đồ: đo so chuẩn với điểm bất thường và histogram sai lệch trên 20 lượt.
# Dữ liệu: 20 cặp x/observed, chuẩn reference=2x+5; lượt M18 có độ lệch lớn, cảnh báo khi |residual|>10.
# Nhập thư viện Matplotlib để chọn backend trước khi nhập pyplot.
import matplotlib
# use('Agg') chuyển sang backend Agg không cần cửa sổ màn hình, tạo ảnh raster để lưu file; gọi TRƯỚC pyplot.
matplotlib.use("Agg")
# Nhập thư viện Matplotlib để chọn backend trước khi nhập pyplot.
# pyplot là giao diện vẽ đồ thị dùng tên ngắn plt; các lệnh plt thao tác trên figure/axes hiện tại.
import matplotlib.pyplot as plt
# Path đặt tên PNG và cung cấp is_file()/stat() để kiểm kết quả lưu.
from pathlib import Path

# NumPy giúp tính reference, residual và mask cảnh báo đồng thời trên 20 mẫu.
import numpy as np
# Tạo x mảng float từ 1 đến 20, mỗi phần tử là mức đầu vào tương ứng một lượt đo.
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], dtype=float)
# 20 tín hiệu thực đo, cùng thứ tự với x; một giá trị 71 cao bất thường ở lượt 18.
observed = np.array([7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,71,43,45], dtype=float)
# NumPy broadcast phép nhân và cộng cho mọi x để dựng đường chuẩn y=2x+5.
reference = 2*x + 5
# Trừ THEO TỪNG VỊ TRÍ để tạo residual (đo trừ chuẩn), giữ đơn vị của tín hiệu.
residual = observed - reference
# abs() bỏ dấu sai số, >10 tạo mask True cho lượt đo cách đường chuẩn hơn 10 đơn vị.
flagged = np.abs(residual) > 10
# subplots(1,2) tạo MỘT Figure có hai Axes nằm ngang; figsize=(10,4) đặt kích thước hình theo inch, không phải số quan sát.
fig, (left,right) = plt.subplots(1,2,figsize=(10,4))
# Vẽ 20 điểm đo trên Axes trái; label dùng cho legend.
left.scatter(x,observed,label="Observed")
# Vẽ đường tham chiếu y=2x+5 để so với các chấm quan sát.
left.plot(x,reference,label="Reference")
# Boolean indexing chỉ lấy các điểm có mask True; marker='x' là dấu nhân, s=90 là diện tích marker tính pt², không phải giới hạn số điểm.
left.scatter(x[flagged],observed[flagged],marker="x",s=90,label="Review")
# Đặt nhãn và đơn vị biểu đồ trái: input và signal.
left.set(xlabel="Input level",ylabel="Signal (units)",title="Measured vs reference")
# Hiện chú giải Observed/Reference/Review theo label từng đối tượng.
left.legend()
# Histogram residual chia vào bốn khoảng từ -1 tới 40; bins là các BIÊN do người soạn chọn, edgecolor vẽ viền đen; cần bảo đảm dữ liệu nằm trong phạm vi này.
right.hist(residual,bins=[-1,1,10,20,40],edgecolor="black")
# Nhãn biểu đồ phải là residual (đơn vị tín hiệu) và Count (số lượt trong từng khoảng).
right.set(xlabel="Residual (units)",ylabel="Count",title="Residual distribution")
# Căn cả hai Axes để nhãn không chồng khi lưu.
fig.tight_layout()
# Tên PNG tương đối so với working directory.
path = Path("sensor_review_20.png")
# Ghi Figure chứa cả hai đồ thị ra PNG với dpi=130.
fig.savefig(path,dpi=130)
# Đóng Figure sau ghi, thu hồi bộ nhớ; file PNG không bị xóa.
plt.close(fig)
# Kiểm đủ 20 mức đầu vào và 20 số đo theo cùng thứ tự.
if len(x) != 20 or len(observed) != 20:
    # Dừng nếu thiếu số đo để tránh đánh dấu sai.
    raise ValueError("Cần đủ 20 mức đầu vào và tín hiệu đo.")
print("Lượt đo:", len(x))
print("Biểu đồ trong hình:", 2)
# sum() trên mask Boolean đếm các giá trị True (lượt cảnh báo); int() đổi sang số nguyên Python.
print("Điểm cần kiểm:", int(flagged.sum()))
flagged_ids = []
# flatnonzero() trả chỉ số 0-based của các ô True trong mask phẳng, dùng tìm mã lượt cần kiểm.
for i in np.flatnonzero(flagged):
    # Chỉ số NumPy bắt đầu từ 0 nên +1 ra số lượt, :02d định dạng M01..M20.
    # append() lưu mã của lượt cảnh báo vào list.
    flagged_ids.append(f"M{i+1:02d}")
# join() ghép các mã cần kiểm bằng dấu phẩy/không gian.
print("Mã cần kiểm:", ", ".join(flagged_ids))
# Kiểm PNG đã tồn tại và có dữ liệu byte >0, không chỉ giả định savefig luôn thành công.
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
