# PY-04 — Câu lệnh điều kiện if, elif, else


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Condition** — điều kiện; **Branch** — nhánh.

`Toán tử → Điều kiện → Phân loại theo quy tắc`

**Học xong dùng để làm gì?** Tạo quy tắc quyết định như phân loại điểm, xác định mức ưu đãi và xử lý trường hợp không đạt điều kiện.

**Kết nối kiến thức tiếp theo:** Sang PY-05, lặp lại quy tắc này cho nhiều bản ghi thay vì viết từng câu điều kiện thủ công.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích dễ nhớ |
|---|---|---|
| Condition | điều kiện | Phép kiểm tra đúng hoặc sai |
| Branch | nhánh | Phần chương trình được chọn để chạy |
| Threshold | ngưỡng | Ranh giới để chuyển trạng thái |
| Nested if | điều kiện lồng | Kiểm tra bổ sung bên trong một nhánh |

## 3. Hàm và cú pháp Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cú pháp | Mục đích và lựa chọn liên quan |
|---|---|
| `if expression:` | Chỉ chạy nhánh nếu điều kiện đúng |
| `elif expression:` | Thử điều kiện tiếp theo khi nhánh trước không đúng |
| `else:` | Trường hợp còn lại không cần điều kiện mới |
| `in, and, or` | Kiểm tra thành viên hoặc kết hợp nhiều điều kiện |

## 4. Khái niệm liên quan

**Rẽ nhánh** giúp chương trình chọn hành động theo dữ liệu thay vì lúc nào cũng chạy mọi lệnh. Python xét điều kiện `if` trước; nếu sai mới xét các `elif` theo thứ tự, và dùng `else` khi không nhánh nào đúng. Nhờ vậy một giá trị đầu vào được xếp đúng một trạng thái trong cùng chuỗi nhánh.

### 4.1. If / elif / else — Cấu trúc rẽ nhánh

**Từ vựng trong mục:** **Condition** — điều kiện; **If / elif / else** — nếu / nếu khác / còn lại.

Giả sử một cảm biến có nhiệt độ 30 °C: từ 35 °C trở lên gọi là `Hot`, từ 20 đến dưới 35 °C gọi là `Warm`, còn thấp hơn gọi là `Cold`. Chương trình kiểm tra điều kiện từ trên xuống: `if` xét ngưỡng cao, `elif` xét ngưỡng tiếp theo khi nhánh trước sai, còn `else` nhận các trường hợp còn lại. Chỉ một nhánh trong chuỗi này được chạy.

```python
# Mục đích: Cấu trúc rẽ nhánh.
temperature = 30

if temperature >= 35:
    state = 'Hot'
elif temperature >= 20:
    state = 'Warm'
else:
    state = 'Cold'

print(state)
```

**Kết quả khi chạy:**

```text
Warm
```

Nhiệt độ 30 °C không đạt mức `Hot` nhưng đạt mức `Warm`, nên nhánh `elif` được chọn.

### 4.2. Branch — Nhánh lệnh

**Từ vựng trong mục:** **Branch** — nhánh; **Boolean** — đúng/sai.

Một nhánh là nhóm câu lệnh được thụt vào dưới `if` hoặc `else`; nó chỉ chạy khi chương trình chọn nhánh ấy. Ví dụ kho có `0` sản phẩm: nếu số lượng dương thì in `Còn hàng`, ngược lại in `Hết hàng`. Dấu `:` mở đầu nhánh; bốn dấu cách cho biết câu lệnh nào thuộc nhánh.

```python
# Mục đích: Nhánh lệnh.
stock = 0

if stock > 0:
    print('Còn hàng')
else:
    print('Hết hàng')
```

**Kết quả khi chạy:**

```text
Hết hàng
```

Vì `stock > 0` sai, chương trình bỏ nhánh `if` và chạy nhánh `else`.

### 4.3. Threshold — Ngưỡng

**Từ vựng trong mục:** **Threshold** — ngưỡng; **Comparison** — phép so sánh.

Ngưỡng là ranh giới dùng để chia dữ liệu thành các nhóm. Chẳng hạn trung tâm yêu cầu từ 80 điểm trở lên để đạt mức B. Với điểm 85, `85 >= 80` là đúng. Dấu `>=` có nghĩa **lớn hơn hoặc bằng**, nên đúng cả khi điểm bằng chính mốc 80; điều này quan trọng khi phân loại các giá trị ở ranh giới.

```python
# Mục đích: Ngưỡng.
print(85 >= 80)
```

**Kết quả khi chạy:**

```text
True
```

Điểm 85 đạt ngưỡng 80. Nếu dùng `>` thì người đạt đúng 80 sẽ bị loại ngoài ý muốn.

### 4.4. Nested if — Điều kiện lồng nhau

**Từ vựng trong mục:** **Nested if** — điều kiện lồng; **Modulo** — chia lấy dư.

Đôi khi chỉ nên kiểm tra điều kiện thứ hai khi điều kiện đầu tiên đúng. Ví dụ chỉ phân loại số chẵn sau khi xác định số đó dương. `x > 0` mở nhánh ngoài; bên trong, `x % 2 == 0` hỏi phép chia cho 2 có dư 0 không. Với `x = 2`, cả hai điều kiện đúng nên in `even`.

```python
# Mục đích: Điều kiện lồng nhau.
x = 2

if x > 0:
    if x % 2 == 0:
        print('even')
```

**Kết quả khi chạy:**

```text
even
```

Số 2 vừa dương vừa chia hết cho 2, nên chương trình đi vào cả hai nhánh `if`.
## 5. Năm tình huống — quy tắc rẽ nhánh tăng dần

### Tình huống 1 — Cấp 1: Xác định đạt/chưa đạt của 10 học viên

**Từ vựng trong mục:** **If** — nếu; **Else** — nếu không; **Threshold** — ngưỡng.

**Tình huống thực tế:** Giáo vụ nhận **10 bài kiểm tra**, mỗi dòng là một học viên với điểm trên thang 100; từ **50 điểm** được tính là đạt. Cần phân loại từng người và in tổng số đạt, chưa đạt, xác nhận rằng điểm 50 thuộc nhóm đạt.

**Vì sao chọn cách này?** `if` chọn nhánh khi điều kiện đúng; `else` nhận phần còn lại. Một ngưỡng có hai kết quả, không cần `elif`. Ví dụ dùng vòng `for` chỉ để áp dụng cùng quy tắc cho đủ 10 học viên.

**Quy trình:**
1. Lưu mười điểm theo thứ tự học viên H01…H10.
2. Với từng điểm, chọn `Đạt` nếu từ 50 trở lên, còn lại `Chưa đạt`.
3. Cộng số lượng từng nhánh và in trạng thái học viên H02 ở đúng biên.

```python
points = [48,50,72,30,85,90,49,61,44,100]
passed = 0
failed = 0
for score in points:
    if score >= 50:
        passed += 1
    else:
        failed += 1
assert len(points) == 10
assert passed + failed == 10
print("Số học viên:", len(points))
print("Đạt:", passed)
print("Chưa đạt:", failed)
print("H02:", "Đạt" if points[1] >= 50 else "Chưa đạt")
```

**Kết quả khi chạy:**

```text
Số học viên: 10
Đạt: 6
Chưa đạt: 4
H02: Đạt
```

Quy tắc dùng `>=` nên giá trị 50 nằm trong nhóm đạt. Không có trường hợp vừa đạt vừa chưa đạt nếu hai nhánh được đặt chung trong một `if`/`else`.

### Tình huống 2 — Cấp 2: Phân ba mức tồn kho cho 12 SKU

**Từ vựng trong mục:** **Elif** — điều kiện khác; **Branch** — nhánh; **Stock** — tồn kho.

**Tình huống thực tế:** Cửa hàng có **12 mã sản phẩm**, mỗi dòng là số lượng còn lại (món). Quy tắc: số lượng `0` là `Out`, từ `1` đến `5` là `Low`, từ `6` trở lên là `OK`. Hãy đếm số SKU ở mỗi mức và kiểm tra lượng tồn `5` vẫn thuộc mức `Low`.

**Vì sao chọn cách này?** Thứ tự nhánh quan trọng: xét hết hàng trước, sau đó xét gần hết; các giá trị còn lại rơi vào `else`. Nhờ `elif`, mỗi SKU chỉ được đếm **một trạng thái**.

**Quy trình:**
1. Duyệt danh sách 12 giá trị tồn.
2. Dùng chuỗi `if` → `elif` → `else` theo ngưỡng.
3. Kiểm tra số lượng ba trạng thái cộng lại bằng 12.

```python
stocks = [0,1,4,7,12,5,3,0,8,2,16,5]
count = {"Out": 0, "Low": 0, "OK": 0}
for quantity in stocks:
    if quantity == 0:
        state = "Out"
    elif quantity <= 5:
        state = "Low"
    else:
        state = "OK"
    count[state] += 1
assert len(stocks) == 12
assert sum(count.values()) == 12
print("Out:", count["Out"])
print("Low:", count["Low"])
print("OK:", count["OK"])
```

**Kết quả khi chạy:**

```text
Out: 2
Low: 6
OK: 4
```

Cấp này khó hơn vì có ba nhánh không chồng lấn. Học viên có thể đối chiếu `0`, `5` và `6` để thấy ngưỡng được dùng nhất quán.

### Tình huống 3 — Cấp 3: Phân hạng 15 khách theo hai điều kiện

**Từ vựng trong mục:** **Nested condition** — điều kiện phối hợp; **Comparison** — so sánh; **Tier** — hạng.

**Tình huống thực tế:** Đội chăm sóc quản lý **15 khách hàng**; mỗi hàng có thời gian thành viên (năm) và chi tiêu tích lũy (đồng). Khách **Gold** nếu ít nhất 5 năm và đã chi từ 2.000.000 đồng, **Silver** nếu ít nhất 5 năm và chi từ 1.000.000 đến dưới 2.000.000 đồng; những khách khác là **Standard**. Cần thống kê từng hạng.

**Vì sao chọn cách này?** Nếu xét Silver trước, khách Gold cũng khớp điều kiện Silver và bị phân loại sai. Phải ưu tiên ngưỡng cao hơn, sau đó mới rẽ sang ngưỡng thấp; hai phép so sánh trong mỗi nhánh nối bằng `and`.

**Quy trình:**
1. Ghép 15 cặp năm và số tiền đúng khách.
2. Xét Gold trước, sau đó Silver rồi Standard.
3. Thống kê đúng một hạng mỗi khách và kiểm tra tổng 15.

```python
years = [1,5,6,8,2,5,10,3,7,5,9,6,2,4,8]
spending = [800000,1000000,900000,2000000,1800000,2500000,1100000,900000,500000,700000,3500000,1200000,1700000,4000000,1500000]
counts = {"Gold": 0, "Silver": 0, "Standard": 0}
for year, amount in zip(years, spending):
    if year >= 5 and amount >= 2000000:
        category = "Gold"
    elif year >= 5 and amount >= 1000000:
        category = "Silver"
    else:
        category = "Standard"
    counts[category] += 1
assert len(years) == len(spending) == 15
assert sum(counts.values()) == 15
print("Gold:", counts["Gold"])
print("Silver:", counts["Silver"])
print("Standard:", counts["Standard"])
```

**Kết quả khi chạy:**

```text
Gold: 3
Silver: 4
Standard: 8
```

Không suy ra khách Gold từ tiền chi tiêu đơn lẻ: khách cũng phải đáp ứng số năm. Đây là bài phối hợp hai cột với thứ tự ưu tiên nhánh.

### Tình huống 4 — Cấp 4: Cảnh báo nhiệt độ và mất kết nối của 18 cảm biến

**Từ vựng trong mục:** **Validation** — kiểm tra đầu vào; **Online** — kết nối; **Missing** — thiếu số đo.

**Tình huống thực tế:** Trạm giám sát có **18 cảm biến**, mỗi dòng gồm nhiệt độ (°C hoặc `None`) và trạng thái kết nối. Hệ thống ưu tiên `Offline` khi mất kết nối; nếu online nhưng chưa có số đo thì `Missing`; nếu online có nhiệt độ **từ 80 °C** thì `Hot`, ngược lại `Normal`. Hãy đếm số cảm biến của bốn trạng thái.

**Vì sao chọn cách này?** Kiểm tra mất kết nối **trước** khi so nhiệt độ, vì một thiết bị đã offline có thể còn giữ số đo cũ. Phải xử lý `None` trước phép `>=` để tránh lỗi kiểu và không biến mất dữ liệu thành bình thường.

**Quy trình:**
1. Ghép đủ 18 cặp kết nối/nhiệt độ.
2. Phân nhánh theo độ ưu tiên: offline → thiếu → nóng → bình thường.
3. Đếm từng trạng thái, kiểm tra tổng bằng 18.

```python
temperatures = [26,35,80,81,79,20,None,85,95,32,80,70,90,None,18,40,79,88]
online = [True,True,True,True,False,True,True,True,False,True,True,True,True,True,True,True,False,True]
counts = {"Offline": 0, "Missing": 0, "Hot": 0, "Normal": 0}
for active, temp in zip(online, temperatures):
    if not active:
        state = "Offline"
    elif temp is None:
        state = "Missing"
    elif temp >= 80:
        state = "Hot"
    else:
        state = "Normal"
    counts[state] += 1
assert len(temperatures) == len(online) == 18
assert sum(counts.values()) == 18
for state in ("Offline", "Missing", "Hot", "Normal"):
    print(state + ":", counts[state])
```

**Kết quả khi chạy:**

```text
Offline: 3
Missing: 2
Hot: 6
Normal: 7
```

Những trạng thái này loại trừ nhau theo thứ tự: số đo 80 °C được báo Hot nếu thiết bị online; một thiết bị offline với số đo 95 °C **không bị đọc nhầm là hiện đang Hot**.

### Tình huống 5 — Cấp 5: Ra quyết định giao 20 đơn: kiểm dữ liệu, tồn kho và phí

**Từ vựng trong mục:** **Decision tree** — cây quyết định; **Validation** — kiểm tra hợp lệ; **Priority** — thứ tự xét.

**Tình huống thực tế:** Cửa hàng có **20 đơn giao**, mỗi hàng gồm mã O01…O20, giá trị đơn (đồng), khoảng cách giao (km) và cờ có hàng trong kho. Nếu thiếu/sai số tiền hoặc km thì `INVALID`; nếu hợp lệ nhưng hết hàng thì `HOLD`; nếu có hàng và đơn **từ 1.000.000 đồng** thì `FREE`; các đơn khác giao **không quá 5 km** phí 15.000 đồng (`LOCAL`) hoặc xa hơn phí 30.000 đồng (`FAR`). Hãy in số đơn mỗi loại, tổng phí và mã chưa thể giao.

**Vì sao chọn cách này?** Đây là quy trình rẽ nhánh nhiều tầng: nếu ưu tiên kiểm khuyến mại trước kiểm lỗi thì phiếu âm tiền có thể lọt vào báo cáo. Phải kiểm hợp lệ → khả năng giao → ưu đãi → vùng giao, và chỉ tính phí của đơn giao có thu phí.

**Quy trình:**
1. Đọc 20 đơn và kiểm tra giá trị/ khoảng cách trước khi so ngưỡng.
2. Dùng chuỗi `if`/`elif`/`else` theo đúng ưu tiên; đồng thời lưu phí cho từng đơn.
3. Đối chiếu tổng năm trạng thái bằng 20 và báo mã `HOLD`/`INVALID` cần xử lý.

```python
amount_vnd = [350000,530000,710000,890000,None,1250000,350000,530000,710000,890000,1070000,1250000,-5000,530000,710000,890000,1070000,1250000,350000,530000]
distance_km = [1,2,3,4,5,6,7,None,1,2,3,4,5,6,7,8,1,2,3,4]
in_stock = [True,True,False,True,True,True,True,True,True,False,True,True,True,True,True,True,True,False,True,True]
counts = {"INVALID": 0, "HOLD": 0, "FREE": 0, "LOCAL": 0, "FAR": 0}
blocked_ids = []
total_fee_vnd = 0
for idx, (amount, km, available) in enumerate(zip(amount_vnd, distance_km, in_stock), 1):
    if amount is None or km is None or amount < 0 or km < 0:
        state, fee = "INVALID", 0
    elif not available:
        state, fee = "HOLD", 0
    elif amount >= 1000000:
        state, fee = "FREE", 0
    elif km <= 5:
        state, fee = "LOCAL", 15000
    else:
        state, fee = "FAR", 30000
    counts[state] += 1
    total_fee_vnd += fee
    if state in ("INVALID", "HOLD"):
        blocked_ids.append(f"O{idx:02d}")
assert len(amount_vnd) == len(distance_km) == len(in_stock) == 20
assert sum(counts.values()) == 20
for name in ("INVALID", "HOLD", "FREE", "LOCAL", "FAR"):
    print(name + ":", counts[name])
print("Phí thu (đồng):", total_fee_vnd)
print("Cần xử lý:", ", ".join(blocked_ids))
```

**Kết quả khi chạy:**

```text
INVALID: 3
HOLD: 3
FREE: 4
LOCAL: 6
FAR: 4
Phí thu (đồng): 210000
Cần xử lý: O03, O05, O08, O10, O13, O18
```

Mỗi đơn chỉ rơi vào **một trạng thái** và phí giao chỉ thu khi đã xác định có thể giao. Điều kiện biên 1.000.000 đồng và 5 km được xử lý bằng `>=`/`<=`, trong khi thiếu dữ liệu được tách trước khi so sánh.

## 6. Nhầm lẫn dễ gặp

- Phải đặt dấu `:` sau `if`, `elif`, `else` và thụt các lệnh trong nhánh.
- Nếu một `if`/`elif` đã đúng, các nhánh sau trong cùng chuỗi sẽ không chạy.
- `else` không có điều kiện riêng. Không nhầm `=` (gán giá trị) với `==` (so sánh bằng nhau).
- Khi chia khoảng điểm hay nhiệt độ, phải chọn đúng `>=`, `>`, `<=` để không xếp nhầm giá trị tại ngưỡng.

## 7. Trắc nghiệm

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What does `if` do? | `if` dùng để làm gì?**

A. Always runs every conditional branch | Luôn chạy mọi nhánh điều kiện

B. Runs its body only when the condition is false | Chỉ chạy thân khối khi điều kiện sai

C. Runs its body once regardless of the condition | Luôn chạy thân khối một lần bất kể điều kiện

D. Runs its indented body when the condition is true | Chạy thân khối thụt lề khi điều kiện đúng

**Đáp án: D**

**Giải thích:** `if` đánh giá điều kiện rồi chỉ chạy thân khối được thụt lề nếu điều kiện có giá trị đúng. Ví dụ với `x = 5`, `if x > 3:` sẽ chạy thân khối; không bắt buộc phải có `else`.


**Q2. When is an `elif` condition checked? | Khi nào Python xét điều kiện `elif`?**

A. Even after a preceding branch has matched | Kể cả khi nhánh trước đã đúng

B. Before the preceding `if` is checked | Trước khi kiểm tra `if` đứng trước

C. After `else` has executed | Sau khi `else` chạy

D. Only if earlier branches in the same chain did not match | Chỉ khi các nhánh trước trong cùng chuỗi không khớp

**Đáp án: D**

**Giải thích:** Python chỉ xét `elif` khi những điều kiện `if` hoặc `elif` đứng trước trong cùng chuỗi đều không khớp. Khi một nhánh trước đã đúng, các `elif` sau không được kiểm tra, nên không có nhiều nhánh cùng chạy.


**Q3. When does an `else` block run? | Khi nào khối `else` chạy?**

A. Every time the initial `if` is true | Mỗi khi `if` đầu tiên đúng

B. After any successful `elif` branch | Sau bất kỳ nhánh `elif` nào đúng

C. When no earlier condition in its chain was true | Khi mọi điều kiện trước trong cùng chuỗi đều sai

D. Only when a program raises an error | Chỉ khi chương trình phát sinh lỗi

**Đáp án: C**

**Giải thích:** `else` là nhánh dự phòng không có điều kiện riêng. Nó chỉ chạy khi mọi điều kiện `if` hoặc `elif` đứng trước trong cùng chuỗi đều sai, không chạy sau nhánh đã khớp.


**Q4. What is a nested `if`? | `if` lồng nhau là gì?**

A. An `if` statement inside another conditional block | Một lệnh `if` bên trong khối điều kiện khác

B. A condition joined by `and` | Điều kiện kết hợp bởi `and`

C. An `else` branch following `if` | Nhánh `else` theo sau `if`

D. Two `if` statements at the same indentation level | Hai lệnh `if` có cùng mức thụt lề

**Đáp án: A**

**Giải thích:** `if` lồng nhau là câu lệnh điều kiện nằm trong thân một câu lệnh điều kiện khác nên điều kiện trong chỉ được xét khi chương trình đi vào khối đó. Nó khác hai câu `if` độc lập, vốn có thể cùng chạy.


**Q5. Which keyword introduces another conditional test? | Từ khóa nào bổ sung một điều kiện tiếp theo?**

A. `if` | `if`

B. `else` | `else`

C. `elif` | `elif`

D. `in` | `in`

**Đáp án: C**

**Giải thích:** `elif` mở thêm một nhánh có điều kiện nối với `if` trước đó. Khác `else`, nhánh này có điều kiện riêng, ví dụ `elif score >= 80:`.


**Q6. Which keyword gives an unconditional fallback branch? | Từ khóa nào tạo nhánh còn lại không cần điều kiện?**

A. `in` | `in`

B. `elif` | `elif`

C. `if` | `if`

D. `else` | `else`

**Đáp án: D**

**Giải thích:** `else` là nhánh dự phòng không ghi điều kiện trong chuỗi `if/elif/else`; Python chỉ vào đó khi các điều kiện trước sai. Không thể viết `else condition:` vì `else` không nhận điều kiện.


**Q7. Which keyword starts a conditional branch? | Từ khóa nào bắt đầu một nhánh điều kiện?**

A. `else` | `else`

B. `if` | `if`

C. `elif` | `elif`

D. `in` | `in`

**Đáp án: B**

**Giải thích:** Nhánh điều kiện đầu tiên dùng `if`, tiếp theo là biểu thức và dấu hai chấm. `elif` chỉ có thể nối sau một `if` trước đó, không tự mở đầu chuỗi mới.


**Q8. Which operator asks whether an item belongs to a list? | Toán tử nào kiểm tra phần tử có trong List?**

A. `if` | `if`

B. `elif` | `elif`

C. `in` | `in`

D. `else` | `else`

**Đáp án: C**

**Giải thích:** `in` kiểm tra phần tử thuộc tập hợp: `3 in [1, 3]` là `True`. Trong khi đó `if`, `elif`, `else` là từ khóa điều khiển luồng, không phải toán tử kiểm tra phần tử.


**Q9. What does `score >= 80` include? | Điều kiện `score >= 80` bao gồm gì?**

A. Only the score exactly equal to 80 | Chỉ điểm đúng bằng 80

B. Every score of at least 80, including 80 | Mọi điểm từ 80 trở lên, kể cả 80

C. Only scores strictly above 80 | Chỉ điểm lớn hơn 80

D. Scores below 80 | Điểm thấp hơn 80

**Đáp án: B**

**Giải thích:** `>=` bao gồm chính giá trị ngưỡng, nên `score >= 80` đúng với 80, 81 và các giá trị lớn hơn. Dùng so sánh nghiêm ngặt `score > 80` sẽ loại đúng điểm 80.


**Q10. What is the difference between `=` and `==`? | Dấu `=` khác `==` ra sao?**

A. `=` assigns; `==` compares equality | `=` để gán; `==` so sánh bằng nhau

B. `=` compares; `==` assigns | `=` để so sánh; `==` để gán

C. Both operators assign variables | Cả hai toán tử đều dùng gán biến

D. Both operators compare equality | Cả hai toán tử so sánh bằng nhau

**Đáp án: A**

**Giải thích:** `=` gán giá trị như `score = 80`, còn `==` so sánh và trả Boolean như `score == 80`. Không thể thay hai toán tử cho nhau trong điều kiện `if`.


**Q11. What defines the body of an `if` in Python? | Điều gì xác định thân khối `if` trong Python?**

A. The indentation of following statements | Mức thụt lề của các câu lệnh theo sau

B. The number of printed statements | Số câu lệnh in ra

C. The order of imported libraries | Thứ tự thư viện được nhập

D. The variable name in the condition | Tên biến trong điều kiện

**Đáp án: A**

**Giải thích:** Thụt lề xác định câu lệnh nào thuộc thân `if`, thông thường bốn dấu cách cho mỗi cấp. Dấu hai chấm kết thúc dòng điều kiện, còn các dòng thụt lề đúng sau đó mới nằm trong nhánh.


**Q12. How are cases checked in an `if/elif` chain? | Các trường hợp được xét theo thứ tự nào trong chuỗi `if/elif`?**

A. All branches run concurrently | Mọi nhánh chạy đồng thời

B. Top to bottom, stopping after the first match | Từ trên xuống, dừng tại nhánh đúng đầu tiên

C. From the last `elif` upward | Từ `elif` cuối lên trên

D. By whichever condition is cheapest | Theo điều kiện tốn ít tính toán nhất

**Đáp án: B**

**Giải thích:** Python xét nhánh từ trên xuống và chạy nhánh đầu tiên có điều kiện đúng. Nếu điểm 95 cũng thỏa `>= 80`, đặt `>= 80` trước `>= 90` sẽ chọn mức điểm thấp hơn quá sớm.


**Q13. What does `True and False` evaluate to? | `True and False` bằng gì?**

A. `0` (integer) | `0` (số nguyên)

B. `True` (Boolean) | `True` (Boolean)

C. `None` | `None`

D. `False` (Boolean) | `False` (Boolean)

**Đáp án: D**

**Giải thích:** `and` với hai toán hạng Boolean chỉ trả `True` khi cả hai đều `True`. Vì vế thứ hai là `False`, `True and False` cho Boolean `False`, không phải số nguyên `0`.


**Q14. What does `True or False` evaluate to? | `True or False` bằng gì?**

A. `None` | `None`

B. `1` (integer) | `1` (số nguyên)

C. `True` (Boolean) | `True` (Boolean)

D. `False` (Boolean) | `False` (Boolean)

**Đáp án: C**

**Giải thích:** `or` với toán hạng Boolean chỉ cần một vế đúng; vế trái là `True` nên `True or False` cho Boolean `True`. Kết quả không cùng kiểu với số nguyên `1`.


**Q15. What does `not True` evaluate to? | `not True` bằng gì?**

A. `0` (integer) | `0` (số nguyên)

B. `True` (Boolean) | `True` (Boolean)

C. `None` | `None`

D. `False` (Boolean) | `False` (Boolean)

**Đáp án: D**

**Giải thích:** `not` đảo giá trị logic của toán hạng, nên `not True` cho Boolean `False`. Số nguyên `0` cũng được xem là sai trong điều kiện nhưng không phải giá trị trả về ở đây.


**Q16. What does `5 % 2 == 0` evaluate to? | `5 % 2 == 0` có kết quả gì?**

A. `False` (Boolean) | `False` (Boolean)

B. `None` | `None`

C. `0` (integer) | `0` (số nguyên)

D. `True` (Boolean) | `True` (Boolean)

**Đáp án: A**

**Giải thích:** Phần dư `5 % 2` là `1`; vì vậy so sánh `1 == 0` là sai. Toàn bộ biểu thức trả về Boolean `False`, nghĩa là 5 không phải số chẵn.


**Q17. How many branches run in one `if/elif/else` chain? | Có bao nhiêu nhánh chạy trong một chuỗi `if/elif/else`?**

A. Every branch whose condition is true | Mọi nhánh có điều kiện đúng

B. Every `elif` plus `else` | Mọi nhánh `elif` và `else`

C. At most one branch, possibly none without `else` | Tối đa một nhánh, có thể không nhánh nào nếu thiếu `else`

D. Exactly two branches always | Luôn đúng hai nhánh

**Đáp án: C**

**Giải thích:** Trong một chuỗi `if/elif/else`, chương trình chạy tối đa một nhánh: nhánh đúng đầu tiên hoặc `else` khi không nhánh nào đúng. Nếu không có `else` và mọi điều kiện đều sai thì không nhánh nào chạy.


**Q18. What happens if an `if` condition is false and there is no `else`? | Nếu `if` sai và không có `else` thì sao?**

A. The body runs once regardless | Thân nhánh vẫn chạy một lần

B. The body is skipped and execution continues | Bỏ qua thân nhánh và tiếp tục chương trình

C. A `SyntaxError` is raised | Phát sinh `SyntaxError`

D. Python inserts and runs an implicit `else` | Python tự chèn và chạy `else`

**Đáp án: B**

**Giải thích:** Khi điều kiện `if` sai, thân nhánh đó được bỏ qua. Nếu không có `else`, chương trình tiếp tục sau khối điều kiện; đây là Python hợp lệ, không phải lỗi cú pháp.


**Q19. How can two conditions both be required for access? | Cách nào yêu cầu đồng thời hai điều kiện để cho phép truy cập?**

A. Use `==` alone | Chỉ dùng `==`

B. Use `and` | Dùng `and`

C. Use `or` | Dùng `or`

D. Use `not` | Dùng `not`

**Đáp án: B**

**Giải thích:** Phép `and` bắt buộc đồng thời hai điều kiện như `has_ticket and age >= 18`. Dùng `or` sẽ chấp nhận người chỉ thỏa một điều kiện, nên không đảm bảo đủ cả hai yêu cầu.


**Q20. In one `if/elif` grade chain, which order correctly tests `score >= 90`, `score >= 80`, and `score >= 70` to select the highest applicable grade? | Trong một chuỗi `if/elif` phân loại điểm, cần xét `score >= 90`, `score >= 80`, `score >= 70` theo thứ tự nào để chọn mức cao nhất phù hợp?**

A. Test `>= 90`, then `>= 80`, then `>= 70` | Xét `>= 90`, rồi `>= 80`, rồi `>= 70`

B. Write independent `if` statements to select a single grade | Viết các `if` độc lập để chọn duy nhất một nhóm

C. Test `>= 70` before `>= 90` | Xét `>= 70` trước `>= 90`

D. Use any order because all matches run | Thứ tự tùy ý vì mọi nhánh đúng đều chạy

**Đáp án: A**

**Giải thích:** Chuỗi điều kiện chọn nhánh đúng đầu tiên; hãy xét ngưỡng điểm cao nhất trước, ví dụ `>= 90`, rồi `>= 80`, `>= 70`. Nếu bắt đầu từ `>= 70`, điểm 95 sẽ bị xếp nhóm quá sớm.

## 8. Nối sang bài tiếp theo

`Toán tử → Điều kiện → Phân loại theo quy tắc`.
