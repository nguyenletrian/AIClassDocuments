# PY-01 — Biến, đầu vào và đầu ra trong Python


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Variable** — biến; **Input** — đầu vào.

`Chương trình → Biến → Kiểu dữ liệu → Điều kiện`

**Học xong dùng để làm gì?** Nhận tên, tuổi hoặc số lượng từ người dùng, lưu vào biến và in ra kết quả có thể kiểm tra.

**Kết nối kiến thức tiếp theo:** Sang PY-02, dùng kiểu số và chuỗi để dữ liệu trong biến được tính toán đúng thay vì chỉ hiển thị.

## 2. English vocabulary — Từ vựng

| English | Nghĩa tiếng Việt | Giải thích |
|---|---|---|
| Variable | biến | Tên dùng để tham chiếu một giá trị |
| Input | đầu vào | Thông tin đưa vào chương trình |
| Output | đầu ra | Thông tin chương trình tạo ra |
| Type | kiểu dữ liệu | Nhóm giá trị như str, int, float |

## 3. Các hàm và tùy chọn Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cú pháp | Mục đích và ý nghĩa lựa chọn |
|---|---|
| `print()` | Hiển thị kết quả, nhận nhiều giá trị phân cách bằng dấu phẩy |
| `input()` | Nhận văn bản từ bàn phím; kết quả luôn là chuỗi |
| `int()/float()` | Đổi chuỗi hợp lệ sang số trước khi tính toán |
| `type()` | Kiểm tra kiểu dữ liệu khi chưa rõ đầu vào |


## 4. Khái niệm liên quan

Một chương trình thường đi theo mạch **nhận thông tin → lưu vào biến → xử lý → đưa ra kết quả**. Bài này bắt đầu từ biến và cho thấy đầu vào, đầu ra và kiểu dữ liệu phối hợp ra sao trong mạch đó.

### 4.1. Variable — Biến

**Từ vựng trong mục:** **Variable** — biến; **Assignment** — phép gán.

Biến là tên để chương trình ghi nhớ một giá trị. Khi viết `total = 12`, Python gắn tên `total` với số `12`; dòng tiếp theo đọc lại giá trị qua tên đó. Biến giúp ta dùng lại dữ liệu và thay đổi dữ liệu ở một chỗ thay vì viết số trực tiếp khắp chương trình.

```python
# Mục đích: Biến.
total = 12
print(total)
```

**Kết quả khi chạy:**

```text
12
```

`total` là tên biến, còn `12` là giá trị được in ra.

### 4.2. Input — Đầu vào

**Từ vựng trong mục:** **Input** — đầu vào; **String** — chuỗi.

Đầu vào là dữ liệu chương trình nhận để xử lý: có thể từ bàn phím, biểu mẫu hoặc tệp. Ví dụ, biểu mẫu nhận tên khách `An`, ứng dụng lưu tên đó trong biến `name`. Để ví dụ tự chạy không cần gõ phím, ta mô phỏng dữ liệu đã nhận bằng một phép gán; khi nhận trực tiếp từ bàn phím, có thể dùng `input()`.

```python
# Mục đích: Đầu vào.
name = 'An'
print(name)
```

**Kết quả khi chạy:**

```text
An
```

Chương trình in đúng tên đã nhận. Biến có thể đến từ nhiều nguồn, không chỉ bàn phím.

### 4.3. Output — Đầu ra

**Từ vựng trong mục:** **Output** — đầu ra; **Print** — hiển thị.

Đầu ra là thông tin chương trình gửi ra ngoài sau khi xử lý. Đầu ra có thể xuất hiện trên màn hình, được lưu vào file hoặc gửi đến hệ thống khác. Trong bài căn bản, `print()` giúp nhìn thấy giá trị đang được tạo ra; chuỗi trong dấu nháy là nội dung cần hiển thị.

```python
# Mục đích: Đầu ra.
print('Xin chào')
```

**Kết quả khi chạy:**

```text
Xin chào
```

`print()` hiển thị dòng chữ; dấu nháy chỉ là cú pháp Python, không xuất hiện trong kết quả.

### 4.4. Type — Kiểu dữ liệu

**Từ vựng trong mục:** **Type** — kiểu dữ liệu; **Float** — số thực.

Cùng một biến có thể chứa chữ hoặc số, nhưng **kiểu dữ liệu** quyết định phép xử lý nào phù hợp. Chẳng hạn mã đơn `"0007"` là chuỗi (`str`) cần giữ số 0 đầu; giá trị `2.5` là số thực (`float`) có thể dùng để tính toán. Hàm `type()` cho biết kiểu của một giá trị.

```python
# Mục đích: Kiểu dữ liệu.
print(type(2.5))
```

**Kết quả khi chạy:**

```text
<class 'float'>
```

`float` báo đây là số thực, không phải chuỗi ký tự `"2.5"`.
## 5. Năm tình huống ứng dụng — từ cơ bản đến nâng cao

### Tình huống 1 — Cấp 1: Hiển thị danh sách đăng ký

**Từ vựng trong mục:** **Variable** — biến; **Output** — đầu ra.

**Tình huống thực tế:** Quầy ghi danh nhận **10 tên học viên** trong một buổi. Mỗi vị trí trong danh sách là một người; nhân viên cần in số người đã ghi, tên đầu tiên và tên cuối cùng để đối chiếu sổ.

**Vì sao chọn cách này?** Biến giữ lại dữ liệu, `print()` hiển thị thông tin và `len()` đếm tên. Ở đây chỉ đọc dữ liệu; cấu trúc list sẽ được học chi tiết ở PY-06.

**Quy trình:**
1. Ghi 10 tên theo thứ tự tiếp nhận.
2. Lưu số người vào biến riêng.
3. In ba thông tin có nhãn để dễ đọc.

```python
names = ["An","Bình","Chi","Dung","Hà","Khánh","Lan","Minh","Nam","Trang"]
student_count = len(names)
assert student_count == 10
print("Số học viên:", student_count)
print("Học viên đầu:", names[0])
print("Học viên cuối:", names[-1])
```

**Kết quả khi chạy:**

```text
Số học viên: 10
Học viên đầu: An
Học viên cuối: Trang
```

Mỗi phần tử là một học viên, không phải một ký tự. Chỉ số `0` là người đầu, `-1` là người cuối; chưa có phân loại hay tính toán nâng cao.

### Tình huống 2 — Cấp 2: Đổi chữ số thành tiền của 12 đơn

**Từ vựng trong mục:** **Input** — đầu vào; **Integer** — số nguyên; **Conversion** — chuyển kiểu.

**Tình huống thực tế:** Cửa hàng nhập **12 đơn hàng**; mỗi hàng biểu diễn một đơn, có mã, đơn giá (đồng/món) và số lượng (món). Hệ thống tiếp nhận giá, số lượng dưới dạng **chuỗi** để mô phỏng dữ liệu biểu mẫu. Cần đổi đúng kiểu và tính tổng tiền toàn bộ 12 đơn.

**Vì sao chọn cách này?** Không thể cộng tiền chính xác nếu giữ giá ở dạng chuỗi. `int()` biến chữ số thành số, sau đó nhân giá với số lượng. Vòng `for` là phần mở rộng để áp dụng cùng thao tác cho mọi đơn (sẽ học ở PY-05).

**Quy trình:**
1. Tạo 12 bản ghi chuỗi và in thử mẫu đầu.
2. Chuyển giá và số lượng bằng `int()` trước khi nhân.
3. Cộng tổng các giá trị đã đổi và xác nhận đủ 12 đơn.

```python
orders = [
    ("O01", "11000", "2"),
    ("O02", "12000", "3"),
    ("O03", "13000", "1"),
    ("O04", "14000", "2"),
    ("O05", "15000", "3"),
    ("O06", "16000", "1"),
    ("O07", "17000", "2"),
    ("O08", "18000", "3"),
    ("O09", "19000", "1"),
    ("O10", "20000", "2"),
    ("O11", "21000", "3"),
    ("O12", "22000", "1"),
]
total_vnd = 0
for order_id, raw_price, raw_quantity in orders:
    price_vnd = int(raw_price)
    quantity = int(raw_quantity)
    total_vnd += price_vnd * quantity
assert len(orders) == 12
print("Số đơn:", len(orders))
print("Tổng tiền (đồng):", total_vnd)
```

**Kết quả khi chạy:**

```text
Số đơn: 12
Tổng tiền (đồng): 392000
```

Mỗi hàng là **một đơn**; phép nhân tính tiền từng đơn, phép cộng gom 12 đơn. Các đơn có số lượng khác nhau nên không thể lấy một đơn mẫu rồi nhân 12.

### Tình huống 3 — Cấp 3: Định dạng bản tin từ 15 cảm biến

**Từ vựng trong mục:** **Float** — số thực; **F-string** — chuỗi định dạng; **Precision** — số chữ số thập phân.

**Tình huống thực tế:** Trung tâm giám sát nhận **15 nhiệt độ** (°C), mỗi hàng tương ứng một cảm biến mã T01…T15. Nhân viên cần một bản tin thống nhất hiển thị mã và nhiệt độ đến **một chữ số thập phân**, kèm số cảm biến đã nhận.

**Vì sao chọn cách này?** Biến lưu giá trị kiểu `float`; f-string định dạng `:.1f` để mọi dòng có cùng cách đọc. Danh sách kết quả được tạo từ từng cảm biến, thay vì viết thủ công 15 dòng không thống nhất.

**Quy trình:**
1. Lưu đủ 15 giá trị °C theo thứ tự cảm biến.
2. Tạo tên mã theo vị trí và đưa nhiệt độ vào chuỗi định dạng.
3. In số lượng và hai dòng kiểm mẫu; các dòng còn lại được tạo cùng quy tắc.

```python
temperatures = [26.2,27,28.5,29.1,30,27.5,28.2,29.9,31.1,30.5,29,28.4,27.7,30.2,29.6]
reports = []
for index, temperature in enumerate(temperatures, 1):
    reports.append(f"T{index:02d}: {temperature:.1f} °C")
assert len(reports) == 15
print("Số cảm biến:", len(reports))
print("Dòng đầu:", reports[0])
print("Dòng cuối:", reports[-1])
```

**Kết quả khi chạy:**

```text
Số cảm biến: 15
Dòng đầu: T01: 26.2 °C
Dòng cuối: T15: 29.6 °C
```

Tất cả 15 bản tin đã được tạo; hiển thị hai dòng biên để kiểm tra định dạng. Chữ số `.1f` điều khiển **cách in**, không làm thay đổi nguồn dữ liệu ban đầu.

### Tình huống 4 — Cấp 4: Báo số đo chưa gửi từ 18 lượt nhập

**Từ vựng trong mục:** **Missing value** — giá trị thiếu; **Type** — kiểu dữ liệu; **Validation** — kiểm tra hợp lệ.

**Tình huống thực tế:** Trạm đo nhận **18 dòng** dữ liệu nhiệt độ (°C) qua ô nhập liệu; mỗi dòng là một lượt đo. Có một chuỗi rỗng và một mã `N/A` do thiết bị mất tín hiệu. Cần báo có bao nhiêu số hợp lệ, bao nhiêu lượt chưa có dữ liệu và nhiệt độ trung bình từ **chỉ lượt hợp lệ**.

**Vì sao chọn cách này?** Chuỗi trống hoặc `N/A` không phải 0 °C, vì vậy cần tách trước khi chuyển sang `float`. Việc kiểm tra đầu vào và vòng lặp là phần mở rộng, mục tiêu bài này vẫn là nhận đầu vào → lưu bằng biến đúng kiểu → in kết quả.

**Quy trình:**
1. Duyệt lần lượt 18 chuỗi, bỏ khoảng trắng ở hai đầu.
2. Chỉ chuyển `float` cho chuỗi thực sự mang số; ghi lại lượt thiếu.
3. Tính trung bình các giá trị nhận được và in bảng tóm tắt.

```python
raw_readings = [" 26.0 ","27.5","28.0","","29.0"," 30.5","31.0","28.7","27.3","26.9","30.0","N/A","29.8","28.5","27.0","31.2","30.6","29.4"]
valid_temperatures = []
missing_count = 0
for raw in raw_readings:
    value = raw.strip()
    if value in ("", "N/A"):
        missing_count += 1
        continue
    valid_temperatures.append(float(value))
average_celsius = sum(valid_temperatures) / len(valid_temperatures)
assert len(raw_readings) == 18
print("Hợp lệ:", len(valid_temperatures))
print("Thiếu:", missing_count)
print(f"Trung bình: {average_celsius:.2f} °C")
```

**Kết quả khi chạy:**

```text
Hợp lệ: 16
Thiếu: 2
Trung bình: 28.84 °C
```

Đọc đúng số lượt hợp lệ trước khi tính trung bình; nếu đưa hai mã mất tín hiệu vào như 0 °C thì kết quả sẽ bị kéo thấp giả tạo.

### Tình huống 5 — Cấp 5: Tạo báo cáo 20 phiếu thanh toán và đối chiếu đầu vào

**Từ vựng trong mục:** **Input** — đầu vào; **Conversion** — chuyển kiểu; **Report** — báo cáo.

**Tình huống thực tế:** Cửa hàng tổng kết **20 phiếu** cuối ngày; mỗi dòng có mã phiếu O01…O20, giá (đồng/món) ở dạng chữ và số lượng (món) ở dạng chữ. Hai phiếu O07 và O18 có giá `?` do nhân viên chưa nhập. Cần in số phiếu, số phiếu tính tiền được, tổng tiền và danh sách mã cần bổ sung dữ liệu; tuyệt đối không coi `?` là 0 đồng.

**Vì sao chọn cách này?** Kết hợp lưu biến, chuyển kiểu và định dạng đầu ra giúp chương trình tự kiểm tra trước khi báo cáo. Vòng lặp, `isdigit()` và `continue` là phần mở rộng có thể đọc lại sau PY-04/PY-05.

**Quy trình:**
1. Ghi đầy đủ 20 phiếu và giữ mã gồm hai chữ số cuối.
2. Kiểm tra giá có phải chữ số trước khi chuyển `int`; ghi lại mã phiếu lỗi.
3. Tính tổng chỉ trên phiếu hợp lệ, xác nhận số lượng phiếu rồi in báo cáo.

```python
raw_prices = ["12000","14000","16000","18000","20000","22000","?","26000","28000","30000","32000","34000","36000","38000","40000","42000","44000","?","48000","50000"]
raw_quantities = ["1","2","3","4","1","2","3","4","1","2","3","4","1","2","3","4","1","2","3","4"]
orders = [(f"O{i:02d}", raw_prices[i - 1], raw_quantities[i - 1]) for i in range(1, 21)]
total_vnd = 0
missing_ids = []
paid_count = 0
for order_id, raw_price, raw_qty in orders:
    if not raw_price.isdigit():
        missing_ids.append(order_id)
        continue
    total_vnd += int(raw_price) * int(raw_qty)
    paid_count += 1
assert paid_count + len(missing_ids) == len(orders) == 20
print("Số phiếu:", len(orders))
print("Phiếu hợp lệ:", paid_count)
print("Tổng tiền (đồng):", total_vnd)
print("Cần bổ sung:", ", ".join(missing_ids))
```

**Kết quả khi chạy:**

```text
Số phiếu: 20
Phiếu hợp lệ: 18
Tổng tiền (đồng): 1436000
Cần bổ sung: O07, O18
```

Đây là mức tổng hợp: hệ thống vừa tính tiền vừa trả lời **vì sao** có hai phiếu không thể đưa vào kết quả. Mã đơn được giữ dạng chuỗi để số 0 ở đầu không biến mất.

## 6. Những nhầm lẫn thường gặp

- `input()` nhận chữ; cần đổi sang `int()` hoặc `float()` khi muốn tính toán với số. Chuỗi không hợp lệ có thể gây `ValueError`.
- Mã đơn `0007` phải lưu dạng chuỗi nếu cần giữ hai số `0` ở đầu.
- `print()` in kết quả, còn `type()` xem kiểu dữ liệu; hai hàm có nhiệm vụ khác nhau.

## 7. Trắc nghiệm

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a variable in Python? | Biến trong Python là gì?**

A. A name referring to a value | Tên tham chiếu đến một giá trị

B. Information produced by a program | Thông tin do chương trình tạo ra

C. Data received for processing | Dữ liệu được nhận để xử lý

D. How a value is represented and used | Cách biểu diễn và sử dụng một giá trị

**Đáp án: A**

**Giải thích:** Biến Python là tên được liên kết với đối tượng, chẳng hạn `age = 20`. Biến khác dữ liệu đầu vào hay kết quả in ra; dùng `age` sau đó sẽ truy cập giá trị đang được gán.


**Q2. What is program input? | Đầu vào chương trình là gì?**

A. Information produced by a program | Thông tin do chương trình tạo ra

B. How a value is represented and used | Cách biểu diễn và sử dụng một giá trị

C. A name referring to a value | Tên tham chiếu đến một giá trị

D. Data received for processing | Dữ liệu được nhận để xử lý

**Đáp án: D**

**Giải thích:** Đầu vào là dữ liệu chương trình nhận, ví dụ văn bản người dùng nhập cho `input()`. Chương trình có thể xử lý văn bản rồi tạo đầu ra; đầu vào không phải kết quả chương trình.


**Q3. What is program output? | Đầu ra chương trình là gì?**

A. How a value is represented and used | Cách biểu diễn và sử dụng một giá trị

B. Information produced by a program | Thông tin do chương trình tạo ra

C. Data received for processing | Dữ liệu được nhận để xử lý

D. A name referring to a value | Tên tham chiếu đến một giá trị

**Đáp án: B**

**Giải thích:** Đầu ra là thông tin chương trình đưa ra ngoài, ví dụ dòng chữ do `print(5)` hiển thị. Nó khác đầu vào do người dùng cung cấp và khác biến dùng để tham chiếu giá trị trong chương trình.


**Q4. What does a data type describe? | Kiểu dữ liệu mô tả điều gì?**

A. Information produced by a program | Thông tin do chương trình tạo ra

B. How a value is represented and used | Cách biểu diễn và sử dụng một giá trị

C. A name referring to a value | Tên tham chiếu đến một giá trị

D. Data received for processing | Dữ liệu được nhận để xử lý

**Đáp án: B**

**Giải thích:** Kiểu dữ liệu quyết định ý nghĩa giá trị và các phép toán phù hợp: `3` thuộc kiểu `int`, còn `'3'` thuộc `str`. Vì vậy `3 + 2` là phép cộng số, còn `'3' + '2'` nối văn bản.


**Q5. Which function prints a value? | Hàm nào in một giá trị?**

A. `int()` | `int()`

B. `type()` | `type()`

C. `input()` | `input()`

D. `print()` | `print()`

**Đáp án: D**

**Giải thích:** `print()` ghi biểu diễn của giá trị ra đầu ra chuẩn; chẳng hạn `print(5)` hiển thị `5`. Hàm này không nhận câu trả lời người dùng như `input()`.


**Q6. Which function reads keyboard input? | Hàm nào đọc dữ liệu bàn phím?**

A. `input()` | `input()`

B. `int()` | `int()`

C. `type()` | `type()`

D. `print()` | `print()`

**Đáp án: A**

**Giải thích:** `input()` nhận một dòng người dùng gõ và trả về văn bản không kèm ký tự xuống dòng cuối. Dù người dùng gõ `12`, kết quả vẫn là chuỗi `'12'`, không tự đổi thành số nguyên `12`.


**Q7. Which function finds a value's type? | Hàm nào kiểm tra kiểu giá trị?**

A. `input()` | `input()`

B. `print()` | `print()`

C. `type()` | `type()`

D. `int()` | `int()`

**Đáp án: C**

**Giải thích:** `type(value)` trả về lớp/kiểu của đối tượng: `type(3)` là `int` còn `type('3')` là `str`. Hàm kiểm tra kiểu chứ không chuyển đổi giá trị.


**Q8. Which function converts valid decimal digits to an integer? | Hàm nào đổi chuỗi chữ số hợp lệ thành số nguyên?**

A. `int()` | `int()`

B. `print()` | `print()`

C. `type()` | `type()`

D. `input()` | `input()`

**Đáp án: A**

**Giải thích:** `int()` phân tích chuỗi biểu diễn số nguyên hợp lệ nên `int('012')` cho số nguyên `12`; số 0 đầu không được giữ lại. Chuỗi `'12.5'` không phải chuỗi số nguyên thập phân hợp lệ và gây `ValueError`.


**Q9. Which type represents a count of whole items? | Kiểu nào biểu diễn số lượng món nguyên?**

A. `str` | `str`

B. `float` | `float`

C. `int` | `int`

D. `bool` | `bool`

**Đáp án: C**

**Giải thích:** `int` biểu diễn số lượng nguyên như 4 vé hoặc 0 lỗi, không có phần lẻ. `float` phù hợp số đo có thể có phần thập phân, không cần thiết cho số đếm các đơn vị nguyên vẹn.


**Q10. Which type suits a measurement with fractions? | Kiểu nào phù hợp với số đo có phần lẻ?**

A. `int` | `int`

B. `float` | `float`

C. `bool` | `bool`

D. `str` | `str`

**Đáp án: B**

**Giải thích:** `float` biểu diễn giá trị số có thể chứa phần lẻ, ví dụ 2,5 mét. Khác số đếm nguyên, số đo có thể nằm giữa hai số nguyên; số thập phân dạng dấu phẩy động đôi khi chỉ là xấp xỉ.


**Q11. Which type preserves a leading zero in an identifier? | Kiểu nào giữ số 0 đầu mã định danh?**

A. `str` | `str`

B. `bool` | `bool`

C. `float` | `float`

D. `int` | `int`

**Đáp án: A**

**Giải thích:** Mã định danh như `'007'` nên lưu bằng `str` vì mọi ký tự, kể cả hai số 0 đầu, đều có ý nghĩa. Đổi sang `int` được `7` và làm mất định dạng mã.


**Q12. Which type stores a true/false state? | Kiểu nào lưu trạng thái đúng/sai?**

A. `bool` | `bool`

B. `int` | `int`

C. `str` | `str`

D. `float` | `float`

**Đáp án: A**

**Giải thích:** `bool` có hai giá trị logic `True` và `False`, thích hợp biểu diễn trạng thái như có được phép truy cập hay không. Đây không phải kiểu đo lường số hay nhãn văn bản.


**Q13. What does `x = 5` do? | `x = 5` thực hiện điều gì?**

A. Tests whether `x` equals `5` | Kiểm tra `x` có bằng `5` không

B. Adds `5` to the old value of `x` | Cộng `5` vào giá trị cũ của `x`

C. Displays `5` without storing it | Hiển thị `5` mà không gán

D. Assigns the integer `5` to `x` | Gán số nguyên `5` cho `x`

**Đáp án: D**

**Giải thích:** Dấu bằng đơn gán tên `x` cho số nguyên `5`, không kiểm tra bằng nhau và cũng không cộng thêm số. Muốn so sánh `x` có bằng `5` thì dùng `x == 5`.


**Q14. What is the type of `input()`'s return value? | Giá trị trả về của `input()` có kiểu nào?**

A. An integer when only digits are typed | Số nguyên nếu chỉ nhập chữ số

B. A floating-point number by default | Số thực theo mặc định

C. A Boolean indicating whether input exists | Boolean cho biết có đầu vào hay không

D. A string, even if it contains digits | Chuỗi, kể cả khi chỉ chứa chữ số

**Đáp án: D**

**Giải thích:** `input()` luôn trả về `str` chứa nội dung được nhập, ví dụ `'42'`. Nếu cần tính toán số, hãy dùng `int(input())` hoặc phép đổi kiểu phù hợp khi đầu vào hợp lệ.


**Q15. What does `float('2.5')` produce? | `float('2.5')` tạo ra gì?**

A. The string `'2.5'` | Chuỗi `'2.5'`

B. The integer `2` | Số nguyên `2`

C. The floating-point number `2.5` | Số thực `2.5`

D. `ValueError` for any decimal point | `ValueError` nếu có dấu thập phân

**Đáp án: C**

**Giải thích:** `float('2.5')` chuyển văn bản `'2.5'` thành giá trị số thực `2.5`. Kết quả không còn là chuỗi có dấu nháy và không cắt phần lẻ thành số nguyên `2`.


**Q16. What does `int('abc')` raise? | `int('abc')` phát sinh gì?**

A. `TypeError` | `TypeError`

B. `ValueError` | `ValueError`

C. The integer `0` | Số nguyên `0`

D. `NameError` | `NameError`

**Đáp án: B**

**Giải thích:** `int('abc')` phát sinh `ValueError` vì các chữ cái không tạo thành số nguyên hệ mười hợp lệ. Hàm vẫn tồn tại và nhận được chuỗi, nên đây là lỗi giá trị chuyển đổi chứ không phải `NameError`.


**Q17. What does `print(2, 3)` display by default? | `print(2, 3)` mặc định hiển thị gì?**

A. `2,3` | `2,3`

B. `2 3` | `2 3`

C. `(2, 3)` | `(2, 3)`

D. `23` | `23`

**Đáp án: B**

**Giải thích:** Mặc định `print` ngăn cách các đối số bằng một dấu cách: `print(2, 3)` hiển thị `2 3`. Nó không dính hai số thành `23` và không in dạng tuple `(2, 3)`.


**Q18. If `x = 2` is followed by `x = 4` on the next line, what is the final value of `x`? | Nếu `x = 2` rồi `x = 4` ở dòng tiếp theo, giá trị cuối của `x` là gì?**

A. `ValueError` | `ValueError`

B. `2` | `2`

C. `4` | `4`

D. `6` | `6`

**Đáp án: C**

**Giải thích:** Lệnh đầu gán `x` bằng `2`, lệnh tiếp theo gán lại chính tên đó bằng `4`. Vì vậy giá trị cuối là `4`, không phải tổng `6` hay giá trị cũ `2`.


**Q19. Which Python type does `type(2.0)` identify? | `type(2.0)` xác định kiểu Python nào?**

A. `int` | `int`

B. `bool` | `bool`

C. `float` | `float`

D. `str` | `str`

**Đáp án: C**

**Giải thích:** Literal `2.0` là đối tượng số thực, nên `type(2.0)` xác định kiểu `float` (hiển thị `<class 'float'>`). Trong khi đó `type(2)` là `int`; dấu thập phân làm thay đổi kiểu literal.


**Q20. What does `print('Hi')` display? | `print('Hi')` hiển thị gì?**

A. `hi` | `hi`

B. `None` | `None`

C. `'Hi'` including the quotes | `'Hi'` gồm cả dấu nháy

D. `Hi` without quotes | `Hi` không có dấu nháy

**Đáp án: D**

**Giải thích:** Dấu nháy dùng để bao chuỗi trong mã nguồn chứ không phải ký tự thuộc nội dung chuỗi. Vì vậy `print('Hi')` hiển thị `Hi` rồi xuống dòng, không in dấu nháy hoặc chữ thường `hi`.

## 8. Nối sang bài kế tiếp

`Chương trình → Biến → Kiểu dữ liệu → Điều kiện`.
