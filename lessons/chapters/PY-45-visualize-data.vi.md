# PY-45 — Matplotlib: biểu đồ line, scatter và histogram


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Line chart** — biểu đồ đường; **Scatter plot** — biểu đồ phân tán.

`NumPy/Pandas → Visualization → EDA → PCA/ML`

Bài này hệ thống hóa kiến thức đã học thành các thao tác thực hành có đầu vào và đầu ra rõ ràng.

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

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Theo dõi doanh thu ba ngày

**Từ vựng trong mục:** **Figure** — hình biểu đồ; **Axis** — trục.

**Tình huống thực tế:** Cửa hàng ghi ngày 1,2,3 và doanh thu 10,15,12 nghìn đồng, một giá trị mỗi ngày. Muốn tạo biểu đồ đường để thấy chiều biến động và kiểm số điểm vẽ.

**Vì sao chọn cách giải này?** Biểu đồ đường phù hợp chuỗi có thứ tự thời gian; nhãn y nêu nghìn đồng, không chỉ số thô.

**Quy trình giải:**

1. Tạo hai List ngày và doanh thu cùng thứ tự.
2. Vẽ line chart, đặt tên hai trục.
3. In số điểm dữ liệu rồi đóng Figure.

```python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

days = [1, 2, 3]
revenue = [10, 15, 12]
plt.plot(days, revenue)
plt.xlabel('Day')
plt.ylabel('Revenue (thousand VND)')
print(len(revenue))
plt.close()
```

**Kết quả khi chạy:**

```text
3
```

Biểu đồ có ba mốc; doanh thu tăng ngày 2 rồi giảm ngày 3.

### Tình huống 2 — So số giờ học và điểm kiểm tra

**Từ vựng trong mục:** **Figure** — hình biểu đồ; **Axis** — trục.

**Tình huống thực tế:** Ba học viên học 2,4,6 giờ/tuần và đạt điểm 5,7,9/10 tương ứng. Trung tâm muốn xem mối liên hệ qua ba điểm độc lập.

**Vì sao chọn cách giải này?** Scatter ghép mỗi giờ học với điểm của cùng người mà không giả định đường nối theo thời gian.

**Quy trình giải:**

1. Tạo ba cặp x=giờ/tuần và y=điểm/10.
2. Vẽ scatter, ghi rõ trục.
3. In số điểm, đóng hình để giải phóng bộ nhớ.

```python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

hours = [2, 4, 6]
scores = [5, 7, 9]
plt.scatter(hours, scores)
plt.xlabel('Hours per week')
plt.ylabel('Score (out of 10)')
print(len(hours))
plt.close()
```

**Kết quả khi chạy:**

```text
3
```

Ba điểm mô tả ba học viên; không thể suy ra quan hệ nhân quả từ ba điểm.

### Tình huống 3 — Đếm phân bố điểm theo khoảng

**Từ vựng trong mục:** **Figure** — hình biểu đồ; **Axis** — trục.

**Tình huống thực tế:** Giáo viên có sáu điểm `[5,6,6,7,8,9]` trên thang 10. Cần đếm số học viên rơi vào bốn khoảng điểm định trước.

**Vì sao chọn cách giải này?** Histogram đếm theo bins; cần công bố biên khoảng để người đọc hiểu tần suất.

**Quy trình giải:**

1. Xác định bốn khoảng [5,6), [6,7), [7,8), [8,10].
2. Vẽ histogram và nhận số mẫu mỗi bin.
3. In tần suất rồi đóng Figure.

```python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

scores = [5, 6, 6, 7, 8, 9]
counts, edges, bars = plt.hist(scores, bins=[5, 6, 7, 8, 10])
print(counts.astype(int).tolist())
plt.close()
```

**Kết quả khi chạy:**

```text
[1, 2, 1, 2]
```

Bốn dải điểm lần lượt có 1, 2, 1, 2 học viên.

### Tình huống 4 — Lưu biểu đồ thành PNG

**Từ vựng trong mục:** **Figure** — hình biểu đồ; **Axis** — trục.

**Tình huống thực tế:** Nhân viên lập báo cáo cần tạo đồ thị hai tháng doanh thu 10 và 15 nghìn đồng và lưu hình trong một thư mục tạm, không bật cửa sổ màn hình.

**Vì sao chọn cách giải này?** Backend Agg và `savefig` cho phép tạo PNG không cần tương tác; kiểm tệp trước khi thoát thư mục tạm.

**Quy trình giải:**

1. Tạo Figure đường cho hai tháng.
2. Lưu PNG trong TemporaryDirectory.
3. Kiểm tệp tồn tại và đóng hình.

```python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    plt.plot([1, 2], [10, 15])
    path = Path(folder) / 'chart.png'
    plt.savefig(path)
    print(path.is_file())
    plt.close()
```

**Kết quả khi chạy:**

```text
True
```

File chart.png đã được tạo trong thư mục tạm và sẽ được xóa khi rời khối with.

### Tình huống 5 — Kiểm nhãn trên biểu đồ nhiệt độ

**Từ vựng trong mục:** **Figure** — hình biểu đồ; **Axis** — trục.

**Tình huống thực tế:** Ba thời điểm 1,2,3 giờ tương ứng 22,24,23 °C. Bộ phận kỹ thuật muốn người xem hiểu trục x là giờ và trục y là nhiệt độ Celsius.

**Vì sao chọn cách giải này?** `xlabel` và `ylabel` làm rõ biến/đơn vị thay vì để trục chỉ ghi số không có ngữ cảnh.

**Quy trình giải:**

1. Vẽ ba điểm nhiệt độ theo thời gian.
2. Gắn nhãn Time (hours), Temperature (C).
3. In hai nhãn để đối chiếu rồi đóng hình.

```python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [22, 24, 23])
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (C)')
print(plt.gca().get_xlabel(), plt.gca().get_ylabel())
plt.close()
```

**Kết quả khi chạy:**

```text
Time (hours) Temperature (C)
```

Hai trục có tên và đơn vị nhất quán với dữ liệu đầu vào.

## 6. Sai lầm thường gặp

- Dùng line chart để nối dữ liệu không có thứ tự có thể tạo cảm giác xu hướng giả.
- Scatter phải ghép đúng x và y của **cùng hàng mẫu**; không suy ra nhân quả chỉ từ mối tương quan.
- Histogram phụ thuộc `bins`; ghi biên khoảng khi báo cáo.
- Biểu đồ thiếu đơn vị dễ khiến người xem nhầm thời gian, tiền hoặc nhiệt độ.
- Lưu PNG không thay thế việc lưu bảng dữ liệu gốc và script tạo hình.
- `matplotlib` là thư viện ngoài; với máy không có màn hình có thể dùng backend Agg và `close()` sau khi vẽ.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Q1. What is a line chart best suited for? — Biểu đồ đường phù hợp gì?**

A. Showing changes across ordered positions — Thể hiện thay đổi theo các mốc có thứ tự

B. Individual paired x-y observations — Từng quan sát theo cặp x-y

C. Counts of numeric values within bins — Số quan sát số học trong từng khoảng

D. Naming variables and their units — Đặt tên đại lượng và đơn vị đo

**Q2. What does a scatter plot represent? — Scatter plot biểu diễn gì?**

A. Showing changes across ordered positions — Thể hiện thay đổi theo các mốc có thứ tự

B. Individual paired x-y observations — Từng quan sát theo cặp x-y

C. Counts of numeric values within bins — Số quan sát số học trong từng khoảng

D. Naming variables and their units — Đặt tên đại lượng và đơn vị đo

**Q3. What does a histogram represent? — Histogram biểu diễn gì?**

A. Showing changes across ordered positions — Thể hiện thay đổi theo các mốc có thứ tự

B. Individual paired x-y observations — Từng quan sát theo cặp x-y

C. Counts of numeric values within bins — Số quan sát số học trong từng khoảng

D. Naming variables and their units — Đặt tên đại lượng và đơn vị đo

**Q4. What are axis labels for? — Nhãn trục để làm gì?**

A. Showing changes across ordered positions — Thể hiện thay đổi theo các mốc có thứ tự

B. Individual paired x-y observations — Từng quan sát theo cặp x-y

C. Counts of numeric values within bins — Số quan sát số học trong từng khoảng

D. Naming variables and their units — Đặt tên đại lượng và đơn vị đo

**Q5. Which function draws a line? — Hàm nào vẽ đường?**

A. `plt.plot(x,y)` — `plt.plot(x,y)`

B. `plt.scatter(x,y)` — `plt.scatter(x,y)`

C. `plt.hist(values,bins=...)` — `plt.hist(values,bins=...)`

D. `plt.savefig(path)` — `plt.savefig(path)`

**Q6. Which function draws separate x-y points? — Hàm nào vẽ các điểm x-y riêng?**

A. `plt.plot(x,y)` — `plt.plot(x,y)`

B. `plt.scatter(x,y)` — `plt.scatter(x,y)`

C. `plt.hist(values,bins=...)` — `plt.hist(values,bins=...)`

D. `plt.savefig(path)` — `plt.savefig(path)`

**Q7. Which function draws histograms? — Hàm nào vẽ histogram?**

A. `plt.plot(x,y)` — `plt.plot(x,y)`

B. `plt.scatter(x,y)` — `plt.scatter(x,y)`

C. `plt.hist(values,bins=...)` — `plt.hist(values,bins=...)`

D. `plt.savefig(path)` — `plt.savefig(path)`

**Q8. Which function saves a figure? — Hàm nào lưu hình?**

A. `plt.plot(x,y)` — `plt.plot(x,y)`

B. `plt.scatter(x,y)` — `plt.scatter(x,y)`

C. `plt.hist(values,bins=...)` — `plt.hist(values,bins=...)`

D. `plt.savefig(path)` — `plt.savefig(path)`

**Q9. Why should x and y have matching observation counts? — Vì sao x và y phải có số quan sát tương ứng?**

A. Each x needs its matching y — Mỗi x cần y tương ứng

B. Closes the current Figure — Đóng Figure hiện tại

C. Horizontal-axis label — Nhãn trục ngang

D. Vertical-axis label — Nhãn trục dọc

**Q10. What does `plt.close()` do? — `plt.close()` làm gì?**

A. Each x needs its matching y — Mỗi x cần y tương ứng

B. Closes the current Figure — Đóng Figure hiện tại

C. Horizontal-axis label — Nhãn trục ngang

D. Vertical-axis label — Nhãn trục dọc

**Q11. What does `plt.xlabel()` set? — `plt.xlabel()` đặt gì?**

A. Each x needs its matching y — Mỗi x cần y tương ứng

B. Closes the current Figure — Đóng Figure hiện tại

C. Horizontal-axis label — Nhãn trục ngang

D. Vertical-axis label — Nhãn trục dọc

**Q12. What does `plt.ylabel()` set? — `plt.ylabel()` đặt gì?**

A. Each x needs its matching y — Mỗi x cần y tương ứng

B. Closes the current Figure — Đóng Figure hiện tại

C. Horizontal-axis label — Nhãn trục ngang

D. Vertical-axis label — Nhãn trục dọc

**Q13. How many markers represent three scatter records? — Ba bản ghi scatter tạo mấy điểm?**

A. Three — Ba

B. Yes, changing bins changes counts per interval — Có, đổi bins sẽ đổi số đếm theo khoảng

C. No, a categorical bar chart is clearer — Không, biểu đồ cột theo nhãn rõ hơn

D. No, association alone is insufficient — Không, chỉ liên hệ chưa đủ

**Q14. Do histogram counts depend on bin boundaries? — Số đếm histogram có phụ thuộc biên bins không?**

A. Three — Ba

B. Yes, changing bins changes counts per interval — Có, đổi bins sẽ đổi số đếm theo khoảng

C. No, a categorical bar chart is clearer — Không, biểu đồ cột theo nhãn rõ hơn

D. No, association alone is insufficient — Không, chỉ liên hệ chưa đủ

**Q15. Is a histogram appropriate for names A, B, C as categories? — Histogram có thích hợp trực tiếp cho nhãn A,B,C không?**

A. Three — Ba

B. Yes, changing bins changes counts per interval — Có, đổi bins sẽ đổi số đếm theo khoảng

C. No, a categorical bar chart is clearer — Không, biểu đồ cột theo nhãn rõ hơn

D. No, association alone is insufficient — Không, chỉ liên hệ chưa đủ

**Q16. Can scatter points establish causation? — Scatter có chứng minh quan hệ nhân quả không?**

A. Three — Ba

B. Yes, changing bins changes counts per interval — Có, đổi bins sẽ đổi số đếm theo khoảng

C. No, a categorical bar chart is clearer — Không, biểu đồ cột theo nhãn rõ hơn

D. No, association alone is insufficient — Không, chỉ liên hệ chưa đủ

**Q17. What does backend Agg help with? — Backend Agg giúp gì?**

A. Rendering images without a GUI window — Kết xuất hình không cần cửa sổ GUI

B. Order and units of the time axis — Thứ tự và đơn vị trục thời gian

C. Array of bin counts — Mảng số lượng theo mỗi bin

D. No, it is a rendered image — Không, nó là ảnh được kết xuất

**Q18. What should be checked before interpreting a time plot? — Trước khi đọc biểu đồ thời gian cần kiểm gì?**

A. Rendering images without a GUI window — Kết xuất hình không cần cửa sổ GUI

B. Order and units of the time axis — Thứ tự và đơn vị trục thời gian

C. Array of bin counts — Mảng số lượng theo mỗi bin

D. No, it is a rendered image — Không, nó là ảnh được kết xuất

**Q19. What does `plt.hist` return first? — `plt.hist` trả gì ở vị trí đầu?**

A. Rendering images without a GUI window — Kết xuất hình không cần cửa sổ GUI

B. Order and units of the time axis — Thứ tự và đơn vị trục thời gian

C. Array of bin counts — Mảng số lượng theo mỗi bin

D. No, it is a rendered image — Không, nó là ảnh được kết xuất

**Q20. Does a saved PNG retain an editable dataset automatically? — PNG lưu hình có tự chứa bảng dữ liệu có thể sửa không?**

A. Rendering images without a GUI window — Kết xuất hình không cần cửa sổ GUI

B. Order and units of the time axis — Thứ tự và đơn vị trục thời gian

C. Array of bin counts — Mảng số lượng theo mỗi bin

D. No, it is a rendered image — Không, nó là ảnh được kết xuất

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | Connecting ordered points shows a trend, not necessarily a measured value between points. For unordered categories, a separate bar chart is clearer than a connecting line. | Nối các mốc cho xu hướng, không đảm bảo có số đo giữa các mốc. Nếu dữ liệu là các loại không có thứ tự, biểu đồ cột phù hợp hơn việc nối đường. |
| Q2 | **B** | Each point comes from matching x and y of the same record. The x and y arrays must represent the same records in corresponding positions. | Mỗi điểm là x và y của cùng một bản ghi. Mảng x và y phải cùng thứ tự bản ghi, nếu không các điểm ghép sẽ sai. |
| Q3 | **C** | Histogram groups numeric values by boundaries, unlike a categorical bar chart. Different bin edges can change counts, so report bins whenever comparing histograms. | Histogram chia khoảng giá trị số, không giống biểu đồ cột loại. Đổi biên bins sẽ đổi số đếm; khi so histogram cần nêu rõ khoảng chia. |
| Q4 | **D** | Labels prevent confusing time, temperature or currency units. A scale without its unit makes the plotted numbers ambiguous to readers. | Nhãn tránh nhầm đơn vị thời gian, nhiệt độ hay tiền. Con số trên trục thiếu đơn vị khiến người xem không rõ ý nghĩa đo lường. |
| Q5 | **A** | plot connects points in input order by default. The plotting function expects matched x and y positions and does not verify the real-world meaning of data. | plot nối điểm theo thứ tự đầu vào mặc định. Hàm vẽ đòi x,y tương ứng nhưng không tự kiểm dữ liệu có đúng ý nghĩa thực tế. |
| Q6 | **B** | scatter creates separate markers for each paired observation. It is the right choice when points are separate observations rather than a connected time series. | scatter tạo dấu chấm riêng cho từng cặp quan sát. Đây là lựa chọn phù hợp khi các điểm là quan sát rời, không phải chuỗi thời gian cần nối. |
| Q7 | **C** | hist computes bin counts then draws bars for numeric intervals. `bins` defines interval boundaries or count; changing it changes the grouped summary. | hist đếm trong từng khoảng rồi vẽ cột các khoảng số. `bins` xác định biên hoặc số khoảng; thay đổi tham số này làm thay đổi bản tóm tắt phân bố. |
| Q8 | **D** | savefig writes the rendered figure to a file such as PNG. Saving occurs before closing the Figure; check the target path and access permissions. | savefig ghi hình đã vẽ ra tệp PNG. Phải lưu trước khi đóng Figure và kiểm đường dẫn cùng quyền ghi. |
| Q9 | **A** | Mismatched pairs cannot represent a valid table of points. Mismatched lengths raise an error or invalidate the intended observation pairing. | Không ghép được cặp khi thiếu phần tử tương ứng. Dãy lệch chiều có thể gây lỗi hoặc ghép sai đối tượng quan sát. |
| Q10 | **B** | Closing releases figure resources and avoids accumulating open plots. Close a Figure after exporting it, especially inside a loop producing many files. | Đóng giúp giải phóng tài nguyên và tránh mở nhiều hình. Nên đóng Figure sau khi xuất, nhất là trong vòng lặp tạo nhiều tệp. |
| Q11 | **C** | It changes text, not the x data or its units automatically. For meaningful axes, include both quantity and unit such as Day or hours. | Nó chỉ đổi chữ, không tự đổi dữ liệu hoặc đơn vị. Nhãn có ích nên ghi cả đại lượng và đơn vị như ngày hay giờ. |
| Q12 | **D** | It describes y values and should include units. A temperature axis should say Celsius or Fahrenheit rather than only 'value'. | Nó mô tả y và nên kèm đơn vị. Trục nhiệt độ nên ghi rõ Celsius hoặc Fahrenheit, không chỉ ghi 'value'. |
| Q13 | **A** | Each row maps to one point. One marker per student is different from one marker per feature column. | Mỗi hàng tạo một điểm. Mỗi điểm tương ứng một sinh viên, không phải mỗi cột đặc trưng tạo một điểm. |
| Q14 | **B** | The same observations can be grouped differently. Histogram heights describe sample counts, not necessarily probabilities unless normalized. | Cùng dữ liệu có thể được nhóm khác nhau. Chiều cao histogram thường là số lượng mẫu, không mặc nhiên là xác suất nếu chưa chuẩn hóa. |
| Q15 | **C** | Histogram expects numeric ranges rather than category names. Categorical bars compare named groups, while histogram bins occupy intervals on a numeric axis. | Histogram cần khoảng số thay vì tên loại. Cột phân loại so các nhóm tên; histogram dùng khoảng liên tục trên trục số. |
| Q16 | **D** | Other variables or selection can explain observed patterns. Check study design and confounders before claiming one variable causes another. | Biến khác hoặc cách lấy mẫu có thể tạo cùng xu hướng. Cần xem cách thiết kế nghiên cứu và yếu tố gây nhiễu trước khi nói một biến gây ra biến kia. |
| Q17 | **A** | Agg supports batch scripts or server-side saved images. Agg is especially useful for automated tests that should not require a desktop display. | Agg phù hợp chạy script hàng loạt hoặc lưu hình trên server. Agg đặc biệt hữu ích cho kiểm thử tự động không cần màn hình đồ họa. |
| Q18 | **B** | Incorrect ordering or mismatched units distorts trends. If dates are out of order, a connected line can misleadingly suggest backward time. | Sai thứ tự hoặc đơn vị khiến xu hướng bị hiểu sai. Nếu ngày bị xếp sai, đường nối có thể khiến người xem tưởng thời gian đi ngược. |
| Q19 | **C** | The first return value records frequencies; following outputs hold edges and artists. The returned edges clarify which values contribute to each reported bin count. | Giá trị trả về đầu là tần suất, phần sau là biên và đối tượng vẽ. Mảng biên trả về giúp xác định giá trị nào đóng góp vào từng khoảng đếm. |
| Q20 | **D** | Store raw data separately for recalculation and reproducibility. Keep the script, labels and numeric source table to regenerate the visualization later. | Muốn tính lại và sửa biểu đồ cần lưu dữ liệu gốc riêng. Cần lưu script, nhãn và bảng số gốc để tái tạo lại biểu đồ khi cần. |

## 8. Nối sang bài tiếp

`NumPy/Pandas → Visualization → EDA → PCA/ML`.
