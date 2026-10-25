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

**Tình huống thực tế:** Giáo vụ đang chấm **10 bài kiểm tra**, mỗi bài có một điểm trên thang **0 đến 100**; điểm theo thứ tự gồm cả một bài đúng 50 điểm. Nhà trường quy định **từ 50 điểm là đạt**. Người phụ trách cần đếm bao nhiêu học viên đạt, bao nhiêu người chưa đạt, đồng thời xác nhận kết quả của học viên H02, người được 50 điểm.

**Vì sao chọn cách này?** `if` nghĩa là **nếu** điều kiện đúng thì thực hiện một nhóm lệnh; `else` nghĩa là **nếu không** thì đi sang nhóm lệnh còn lại. Vì trường chỉ có hai kết quả đạt/chưa đạt ở một ngưỡng, không cần `elif` (nhánh bổ sung). Chương trình đọc từng điểm bằng `for`, thử `score >= 50`, rồi tăng một trong hai bộ đếm; `>=` tính cả người đúng 50. Sau cùng, kiểm số đạt cộng số chưa đạt phải đúng 10 để bảo đảm không bỏ quên bài.

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
if len(points) != 10:
    raise ValueError("Phải có đúng 10 điểm học viên.")
if passed + failed != 10:
    raise ValueError("Tổng học viên đạt và chưa đạt phải bằng 10.")
print("Số học viên:", len(points))
print("Đạt:", passed)
print("Chưa đạt:", failed)
if points[1] >= 50:
    h02_result = "Đạt"
else:
    h02_result = "Chưa đạt"
print("H02:", h02_result)
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

**Tình huống thực tế:** Nhân viên kho cần kiểm tra **12 loại sản phẩm**. Mỗi loại có một số lượng còn lại trong kho, tính bằng **món**; có loại còn 0 món, loại còn 5 món và loại còn nhiều hơn. Kho dùng ba tên trạng thái: `Out` = hết hàng, `Low` = còn từ 1 đến 5 món, `OK` = còn từ 6 món trở lên. Nhân viên muốn biết có bao nhiêu loại nằm trong từng trạng thái.

**Vì sao chọn cách này?** Trước hết cần hiểu **trạng thái** là tên tóm tắt tình hình tồn kho của một loại hàng. Chương trình xét `quantity == 0` trước để đưa vào `Out`. Nếu không phải 0 thì xét `quantity <= 5` và đưa vào `Low`; phần còn lại tự động là `OK`. `elif` chỉ được thử khi nhánh phía trước không đúng, còn `else` nhận các trường hợp chưa rơi vào nhánh nào, vì vậy mỗi sản phẩm chỉ được đếm **một lần**. Nếu đặt điều kiện `<= 5` trước, lượng 0 cũng bị gộp nhầm vào nhóm gần hết.

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
if len(stocks) != 12:
    raise ValueError("Cần có đủ 12 mã sản phẩm.")
if sum(count.values()) != 12:
    raise ValueError("Phải phân loại đủ 12 mã vào ba mức tồn kho.")
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

**Tình huống thực tế:** Bộ phận chăm sóc có dữ liệu của **15 khách**. Mỗi người có số năm gắn bó (**năm**) và tổng tiền đã mua (**đồng**) để xét ba hạng ưu đãi: **Gold** khi từ 5 năm và từ 2.000.000 đồng; **Silver** khi từ 5 năm và từ 1.000.000 đến dưới 2.000.000 đồng; còn lại là **Standard**. Nhân viên cần thống kê số khách ở từng hạng, mỗi người chỉ được nằm trong một hạng.

**Vì sao chọn cách này?** Ba hạng không phải ba câu hỏi độc lập: mỗi khách phải nhận **một hạng cao nhất phù hợp**. Vì vậy chương trình thử Gold trước bằng hai điều kiện nối `and` (đều phải đúng). Nếu không đạt Gold mới thử Silver; người không đạt cả hai được gán Standard. Với khách 6 năm và 2.500.000 đồng, cả ngưỡng của Gold lẫn mức tối thiểu của Silver đều có thể đúng, nhưng chỉ Gold được chọn. Nếu dùng ba lệnh `if` riêng, một người có thể bị cộng vào nhiều hạng. Sau mỗi khách tăng đúng một bộ đếm và đối chiếu tổng 15.

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
if len(years) != 15 or len(spending) != 15:
    raise ValueError("Cần có đủ 15 cặp năm thành viên và chi tiêu.")
if sum(counts.values()) != 15:
    raise ValueError("Phải phân hạng đủ 15 khách hàng.")
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

**Tình huống thực tế:** Trạm giám sát theo dõi **18 cảm biến nhiệt độ**, mỗi cảm biến có hai thông tin: đã kết nối hay chưa và số nhiệt độ tính bằng **°C**. Một số máy có thể mất kết nối, hoặc vẫn kết nối nhưng chưa gửi được số (`None`). Quy định phân loại là: mất kết nối `Offline`; vẫn kết nối nhưng thiếu nhiệt độ `Missing`; vẫn kết nối và nhiệt độ từ 80 °C `Hot`; các trường hợp còn lại `Normal`. Trực ca muốn biết số cảm biến của mỗi loại.

**Vì sao chọn cách này?** `None` là dấu hiệu **chưa có số đo**, không có nghĩa là 0 °C. Đồng thời một máy mất kết nối có thể vẫn lưu nhiệt độ của lần trước, nên phải xét `Offline` **trước tiên**. Nếu máy đang kết nối, xét tiếp có số đo hay không; chỉ khi nhiệt độ tồn tại mới được so với 80 °C. `if`/`elif`/`else` đảm bảo lần lượt một trong bốn trạng thái được chọn. So ngay `None >= 80` sẽ gây lỗi; coi `None` là số 0 sẽ giấu đi sự cố thiếu thông tin.

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
if len(temperatures) != 18 or len(online) != 18:
    raise ValueError("Phải có đủ 18 nhiệt độ và trạng thái kết nối.")
if sum(counts.values()) != 18:
    raise ValueError("Phải phân loại đủ 18 cảm biến.")
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

**Tình huống thực tế:** Cửa hàng có **20 đơn giao hàng O01 đến O20**. Mỗi đơn có số tiền (**đồng**), quãng đường giao (**km**) và thông tin còn hàng (`True`/`False`). Một số đơn bị thiếu tiền, thiếu km hoặc có tiền âm. Quy định: đơn thiếu/sai dữ liệu là `INVALID` (không hợp lệ); đơn hợp lệ nhưng hết hàng là `HOLD` (tạm giữ); đơn còn hàng trị giá từ 1.000.000 đồng là `FREE` (miễn phí giao); những đơn còn lại giao đến 5 km thu 15.000 đồng (`LOCAL`), xa hơn thu 30.000 đồng (`FAR`). Quản lý cần số đơn mỗi nhóm, tổng tiền phí giao thực thu và mã những đơn chưa thể giao.

**Vì sao chọn cách này?** Đây là **quy trình ưu tiên kiểm tra**, không phải năm nhóm tùy chọn ngang nhau. Trước hết phát hiện thiếu dữ liệu (`None`), tiền âm hoặc km âm để đưa vào `INVALID`; không thể quyết định phí khi chưa biết giá trị đúng. Với đơn hợp lệ, kiểm tra có hàng không; hết hàng thì `HOLD`. Chỉ đơn còn hàng mới xét miễn phí nếu đủ 1.000.000 đồng; nếu không, dùng mốc 5 km để chọn `LOCAL` hay `FAR`. Cách đi từ dữ liệu hợp lệ → có hàng → được miễn phí → khoảng cách giúp tránh tính phí sai hoặc giao đơn không thể thực hiện. Chỉ cộng 15.000 hay 30.000 đồng khi đơn thực sự thuộc nhóm thu phí; `INVALID`, `HOLD`, `FREE` có phí 0 trong báo cáo. Cuối cùng kiểm tổng các nhóm đúng 20.

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
        state = "INVALID"
        fee = 0
    elif not available:
        state = "HOLD"
        fee = 0
    elif amount >= 1000000:
        state = "FREE"
        fee = 0
    elif km <= 5:
        state = "LOCAL"
        fee = 15000
    else:
        state = "FAR"
        fee = 30000
    counts[state] += 1
    total_fee_vnd += fee
    if state in ("INVALID", "HOLD"):
        blocked_ids.append(f"O{idx:02d}")
if len(amount_vnd) != 20 or len(distance_km) != 20 or len(in_stock) != 20:
    raise ValueError("Phải có đúng 20 đơn, khoảng cách và cờ tồn kho.")
if sum(counts.values()) != 20:
    raise ValueError("Phải phân loại đủ 20 đơn giao.")
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
