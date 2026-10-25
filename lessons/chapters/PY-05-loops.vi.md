# PY-05 — Vòng lặp for, while, break và continue


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Iteration** — lần lặp; **For loop** — vòng for.

`Điều kiện → Vòng lặp → Xử lý hàng loạt`

**Học xong dùng để làm gì?** Tự động tính toán hoặc kiểm tra nhiều dòng dữ liệu bằng for/while, tránh sao chép cùng thao tác.

**Kết nối kiến thức tiếp theo:** Sang PY-06, lưu nhiều giá trị trong List để vòng lặp có dữ liệu thực tế mà xử lý.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích dễ nhớ |
|---|---|---|
| Iteration | lần lặp | Một lượt thực hiện trong quá trình lặp |
| For loop | vòng for | Lặp qua từng phần tử trong một nhóm |
| While loop | vòng while | Lặp khi một điều kiện còn đúng |
| Break/continue | dừng/bỏ qua | Dừng hẳn vòng lặp hoặc bỏ qua lượt hiện tại |

## 3. Hàm và cú pháp Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cú pháp | Mục đích và lựa chọn liên quan |
|---|---|
| `range(start,stop)` | Tạo chỉ số nguyên, không bao gồm stop |
| `enumerate(iterable)` | Lấy đồng thời vị trí và giá trị |
| `break` | Dừng sớm khi đã tìm thấy |
| `continue` | Bỏ qua dữ liệu của một lượt lặp |

## 4. Khái niệm liên quan

**Vòng lặp** cho phép chương trình thực hiện một công việc nhiều lần mà không phải sao chép cùng câu lệnh. Một lần thực hiện được gọi là **lần lặp**. Dùng `for` khi duyệt các phần tử đã có; dùng `while` khi còn phải lặp theo một điều kiện. Hai lệnh `break` và `continue` kiểm soát cách vòng lặp kết thúc hoặc bỏ qua một lượt.

### 4.1. Loop / Iteration — Vòng lặp và lần lặp

**Từ vựng trong mục:** **Loop** — vòng lặp; **Iteration** — lần lặp.

Ví dụ cần đánh số hai lượt kiểm tra liên tiếp. Thay vì viết hai lần `print()`, ta dùng `for` và `range(2)` để Python lần lượt cấp giá trị 0 và 1 cho biến `i`. Mỗi lần thân vòng lặp chạy là một **lần lặp**; ở ví dụ có hai lần lặp và hai dòng được in ra.

```python
# Mục đích: Vòng lặp và lần lặp.
for i in range(2):
    print(i)
```

**Kết quả khi chạy:**

```text
0
1
```

`range(2)` bắt đầu từ 0 và dừng trước 2, nên in 0 rồi 1.

### 4.2. For loop — Duyệt từng phần tử

**Từ vựng trong mục:** **For loop** — vòng `for`; **Iterable** — dữ liệu duyệt được.

Khi có sẵn danh sách `[1, 2]` đại diện hai mã số, `for` lấy từng phần tử theo thứ tự rồi chạy thân vòng lặp. Biến `x` lần lượt nhận 1 rồi 2; nếu danh sách có thêm phần tử, code không cần thêm một câu `print()` riêng cho phần tử mới.

```python
# Mục đích: Duyệt từng phần tử.
for x in [1, 2]:
    print(x)
```

**Kết quả khi chạy:**

```text
1
2
```

Mỗi phần tử tạo ra một dòng đầu ra, theo thứ tự đã lưu trong danh sách.

### 4.3. While loop — Lặp khi điều kiện còn đúng

**Từ vựng trong mục:** **While loop** — vòng `while`; **Condition** — điều kiện.

`while` kiểm tra một điều kiện **trước mỗi lượt**. Ví dụ số việc còn lại là `n = 2`; mỗi lượt hoàn thành một việc nên giảm `n` đi 1. Khi `n` bằng 0 thì `n > 0` sai, vòng lặp dừng. Điều kiện phải có cơ hội trở thành sai để tránh lặp vô hạn.

```python
# Mục đích: Lặp khi điều kiện còn đúng.
n = 2

while n > 0:
    n -= 1

print(n)
```

**Kết quả khi chạy:**

```text
0
```

Hai lượt giảm từ 2 xuống 1 rồi 0; câu `print` bên ngoài vòng lặp cho thấy giá trị cuối cùng.

### 4.4. Break / continue — Dừng hoặc bỏ qua

**Từ vựng trong mục:** **Break** — dừng vòng lặp; **Continue** — bỏ qua lượt hiện tại.

`continue` bỏ phần còn lại của **lượt đang chạy** nhưng vẫn xét lượt tiếp theo. `break` thoát khỏi **toàn bộ vòng lặp hiện tại**. Ví dụ duyệt `[0, 1, 2, 3]`: bỏ qua 0, in 1 và 2, rồi dừng khi gặp 3. Hai lệnh có tác dụng khác nhau dù đều làm một số dòng không được thực hiện.

```python
# Mục đích: Dừng hoặc bỏ qua.
for x in [0, 1, 2, 3]:
    if x == 0:
        continue
    if x == 3:
        break
    print(x)
```

**Kết quả khi chạy:**

```text
1
2
```

Số 0 bị bỏ qua bởi `continue`; khi đến 3, `break` dừng hẳn nên không in 3.
## 5. Năm tình huống vòng lặp — từ đơn giản đến kết hợp

### Tình huống 1 — Cấp 1: Cộng doanh số của 10 đơn bằng for

**Từ vựng trong mục:** **For loop** — vòng lặp for; **Accumulator** — biến cộng dồn.

**Tình huống thực tế:** Cuối ca, thu ngân cần tổng kết **10 đơn bán hàng**. Danh sách lưu số tiền của từng đơn, theo đơn vị **nghìn đồng**: 120, 80, 200, 150, 90, 70, 180, 210, 130 và 160. Mỗi số là tiền của đúng một đơn. Người quản lý chỉ cần biết có bao nhiêu đơn và tổng số tiền cả ca để so với sổ thu ngân.

**Vì sao chọn cách này?** `for` có nghĩa là **làm lần lượt cho từng phần tử**: chương trình lấy tiền đơn đầu, đơn thứ hai... đến đơn thứ mười. Biến `total` ban đầu bằng 0; mỗi lần đọc một đơn thì cộng số tiền ấy vào tổng đang có. Cách này phù hợp khi đã có danh sách 10 đơn và giúp không phải viết 10 phép cộng riêng. `len(orders)` đếm số đơn, còn `total` là tổng doanh số **nghìn đồng**, nên không được nhầm số đơn với số tiền.

**Quy trình:**
1. Khởi tạo `total = 0` trước khi lặp.
2. Với từng giá trị, cộng vào `total`.
3. Kiểm tra đủ 10 dòng và in tổng tiền.

```python
orders = [120,80,200,150,90,70,180,210,130,160]
total = 0
for amount in orders:
    total += amount
if len(orders) != 10:
    raise ValueError("Cần đủ 10 đơn bán hàng.")
print("Số đơn:", len(orders))
print("Doanh số (nghìn đồng):", total)
```

**Kết quả khi chạy:**

```text
Số đơn: 10
Doanh số (nghìn đồng): 1390
```

Mỗi lượt lặp đưa vào tổng **một đơn**; tổng chỉ đúng nếu biến cộng dồn được đặt ngoài vòng lặp và không bị đặt về 0 sau mỗi dòng.

### Tình huống 2 — Cấp 2: Dùng continue bỏ hai lượt đo trống trong 12 lượt

**Từ vựng trong mục:** **Continue** — bỏ qua lượt lặp; **Missing** — số liệu thiếu; **Average** — trung bình.

**Tình huống thực tế:** Trạm thời tiết ghi **12 lượt nhiệt độ** tính bằng **°C**, mỗi lượt ứng với một phút. Ở lượt thứ 3 và thứ 8, thiết bị không gửi được kết quả nên bảng ghi `None`; đây là thông tin thiếu chứ không phải 0 °C. Người trực muốn đếm số lượt có kết quả, số lượt thiếu và nhiệt độ trung bình của các lượt có số.

**Vì sao chọn cách này?** `continue` nghĩa là **bỏ phần còn lại của lượt lặp hiện tại rồi chuyển sang lượt kế tiếp**. Khi gặp `None`, chương trình tăng số lượt thiếu và chuyển qua phút sau, không cộng hay đếm lượt này là nhiệt độ hợp lệ. Các giá trị có số được cộng vào `total` và tăng `valid_count`; cuối cùng lấy tổng nhiệt độ chia cho **số lượt có giá trị**, không chia cho cả 12. Nếu thay `None` bằng 0 thì sẽ làm thấp nhiệt độ trung bình và che giấu hai lần thiết bị mất tín hiệu.

**Quy trình:**
1. Khởi tạo tổng, số lượt hợp lệ và số lượt thiếu.
2. Duyệt 12 giá trị; nếu `None` thì tăng số thiếu rồi `continue`.
3. Chia tổng cho **số lượt hợp lệ**, không phải 12.

```python
readings = [27,28,None,29,30,31,28,None,27,32,30,29]
total = 0
valid_count = 0
missing_count = 0
for temperature in readings:
    if temperature is None:
        missing_count += 1
        continue
    total += temperature
    valid_count += 1
if len(readings) != 12 or valid_count + missing_count != 12:
    raise ValueError("Phải đối chiếu đủ 12 lượt nhiệt độ, kể cả dữ liệu thiếu.")
print("Hợp lệ:", valid_count)
print("Thiếu:", missing_count)
print(f"Trung bình: {total / valid_count:.1f} °C")
```

**Kết quả khi chạy:**

```text
Hợp lệ: 10
Thiếu: 2
Trung bình: 29.1 °C
```

Vòng lặp đã đọc 12 lượt nhưng chỉ 10 lượt được tính trung bình. Nếu chia cho 12, thiết bị sẽ cho kết quả thấp hơn thực tế.

### Tình huống 3 — Cấp 3: Tìm điểm hết hàng đầu tiên trong 15 kệ

**Từ vựng trong mục:** **Enumerate** — duyệt kèm vị trí; **Break** — dừng vòng lặp.

**Tình huống thực tế:** Người quản lý đi kiểm kê **15 kệ K01 đến K15** theo thứ tự từ đầu kho tới cuối kho. Mỗi kệ có một số món đang còn; một kệ có **0 món** nghĩa là đã hết hàng. Họ cần tìm **mã kệ đầu tiên** hết hàng để giao nhân viên đi bổ sung ngay, không cần liệt kê mọi kệ trống.

**Vì sao chọn cách này?** `enumerate(stocks, 1)` giúp đọc cùng lúc **vị trí kệ** và **số món trên kệ**, bắt đầu đếm từ 1 để khớp K01, K02... Khi gặp tồn kho bằng 0, chương trình tạo mã kệ đó rồi dùng `break`. `break` là **thoát hẳn vòng lặp**, khác `continue` chỉ bỏ một lượt và vẫn tiếp tục. Vì yêu cầu chỉ tìm kệ trống đầu tiên, dừng ngay sẽ không vô tình chọn kệ trống thứ hai ở phía sau.

**Quy trình:**
1. Ghi 15 số lượng theo thứ tự kệ.
2. Duyệt cùng số thứ tự; khi gặp `0`, lưu mã kệ và thoát vòng.
3. In vị trí đầu tiên rồi kiểm tra đúng là kệ trống.

```python
stocks = [12,8,7,5,3,4,9,1,0,6,0,2,8,10,4]
first_empty = None
for shelf_number, amount in enumerate(stocks, 1):
    if amount == 0:
        first_empty = f"K{shelf_number:02d}"
        break
if len(stocks) != 15:
    raise ValueError("Cần kiểm kê đủ 15 kệ.")
if first_empty is None:
    raise ValueError("Không tìm thấy kệ trống cần báo cáo.")
if stocks[int(first_empty[1:]) - 1] != 0:
    raise ValueError("Kệ được chọn phải có tồn kho bằng 0.")
print("Số kệ kiểm kê:", len(stocks))
print("Kệ hết hàng đầu:", first_empty)
```

**Kết quả khi chạy:**

```text
Số kệ kiểm kê: 15
Kệ hết hàng đầu: K09
```

K09 trống sớm hơn 1 kệ trống còn lại, nhưng chương trình chủ động dừng trước; đây là lý do dùng `break` thay vì lặp hết toàn bộ danh sách.

### Tình huống 4 — Cấp 4: Dùng while giới hạn số lần kết nối của 18 thiết bị

**Từ vựng trong mục:** **While** — lặp theo điều kiện; **Retry** — thử lại; **Termination** — điều kiện dừng.

**Tình huống thực tế:** Đội kỹ thuật thử kết nối **18 thiết bị D01 đến D18**. Đây là dữ liệu mô phỏng: với mỗi thiết bị, một số từ 1 đến 3 chỉ lần thử mà kết nối sẽ thành công; số 0 hoặc 4 nghĩa là không thành công trong ba lần đầu. Mỗi thiết bị được phép thử **tối đa ba lần**. Nhóm cần biết có bao nhiêu thiết bị kết nối được, bao nhiêu thất bại và tổng số lần đã thử.

**Vì sao chọn cách này?** `while` nghĩa là **còn đúng điều kiện thì còn thử tiếp**; nó hợp với việc chưa biết mỗi thiết bị sẽ thành công ở lần thứ mấy. Biến `attempts` bắt đầu từ 0 và tăng sau mỗi lần thử. Vòng lặp chỉ tiếp tục khi **chưa thử đủ 3 lần** `and` **chưa kết nối được**; nếu một điều kiện không còn đúng thì dừng. Các mã 0 và 4 là giả định mô phỏng rằng ba lần đầu đều thất bại, không phải kết quả kết nối thực tế. Đặt giới hạn ba lần giúp tránh vòng chạy mãi và cho phép cộng tổng số lượt thử của mọi thiết bị.

**Quy trình:**
1. Duyệt 18 thiết bị, mỗi thiết bị khởi tạo lại số lần thử và cờ kết nối.
2. Trong `while`, tăng số lần thử; mô phỏng thành công đúng lượt được cấu hình.
3. Cộng kết quả thành công/thất bại và tổng lượt thử; dùng `if` kiểm tra không thiết bị nào vượt 3 lần.

```python
success_on_try = [0,2,3,1,4,0,1,2,4,1,0,3,4,2,3,0,4,3]
success_count = 0
failed_count = 0
total_attempts = 0
for planned in success_on_try:
    attempts = 0
    connected = False
    while attempts < 3 and not connected:
        attempts += 1
        connected = (planned == attempts)
    total_attempts += attempts
    if connected:
        success_count += 1
    else:
        failed_count += 1
    if attempts > 3:
        raise RuntimeError("Mỗi thiết bị chỉ được thử kết nối tối đa 3 lần.")
if len(success_on_try) != 18:
    raise ValueError("Cần đúng 18 thiết bị để thống kê.")
if success_count + failed_count != 18:
    raise ValueError("Tổng thiết bị thành công và thất bại phải bằng 18.")
print("Thiết bị:", len(success_on_try))
print("Kết nối được:", success_count)
print("Thất bại:", failed_count)
print("Tổng lượt thử:", total_attempts)
```

**Kết quả khi chạy:**

```text
Thiết bị: 18
Kết nối được: 10
Thất bại: 8
Tổng lượt thử: 45
```

Độ khó nằm ở điều kiện dừng của **vòng lặp lồng trong quá trình xử lý 18 thiết bị**. Khi một thiết bị thất bại, lần sau bắt đầu lại với số lượt thử bằng 0; không được dùng chung cờ `connected` giữa hai thiết bị.

### Tình huống 5 — Cấp 5: Lập lịch hai ca cho 20 học viên và tổng hợp điểm danh

**Từ vựng trong mục:** **Nested loop** — vòng lặp lồng; **Continue** — bỏ lượt; **Validation** — kiểm tra dữ liệu.

**Tình huống thực tế:** Trung tâm có **20 học viên H01 đến H20**, mỗi người đăng ký hai ca thực hành là **Sáng** và **Chiều**. Như vậy có 40 lượt học theo lịch trước khi điểm danh. Ba học viên H04, H11 và H19 vắng đúng ca Chiều, nhưng vẫn đi học ca Sáng. Giáo vụ muốn lập danh sách lượt có mặt, biết có bao nhiêu lượt vắng và đếm số lượt có mặt của từng ca, bảo đảm không ghi trùng một học viên trong cùng một ca.

**Vì sao chọn cách này?** Vòng `for` **bên ngoài** chọn lần lượt 20 học viên; vòng `for` **bên trong** chọn hai ca của đúng học viên ấy, nên mỗi người tạo hai lượt dự kiến. Chương trình chỉ dùng `continue` khi gặp ba cặp cụ thể (H04, Chiều), (H11, Chiều), (H19, Chiều); vì thế ca Sáng của họ không bị xóa. Một **cặp (mã học viên, ca)** xác định một lượt duy nhất: ví dụ H04-Sáng và H04-Chiều là hai lượt khác nhau. Chuyển danh sách cặp thành `set` giúp kiểm tra có trùng lượt không; số lượt có mặt cộng số lượt vắng phải bằng 40, nếu không thì lịch đang bị ghi thiếu hoặc ghi thừa.

**Quy trình:**
1. Tạo 20 mã học viên và hai ca mỗi ngày.
2. Duyệt vòng lặp lồng; khi trùng ca vắng, tăng số vắng rồi `continue`.
3. Kiểm tra số lượt dự kiến 40 = lượt hợp lệ + lượt vắng, các cặp ca không trùng.

```python
students = ["H01","H02","H03","H04","H05","H06","H07","H08","H09","H10","H11","H12","H13","H14","H15","H16","H17","H18","H19","H20"]
sessions = ["Sáng", "Chiều"]
absent_afternoon = ["H04","H11","H19"]
schedule = []
absent_count = 0
for student in students:
    for session in sessions:
        if student in absent_afternoon and session == "Chiều":
            absent_count += 1
            continue
        schedule.append((student, session))
if len(students) != 20:
    raise ValueError("Cần đúng 20 học viên.")
if len(schedule) != len(set(schedule)):
    raise ValueError("Không được trùng cặp học viên và ca học.")
if len(students) * len(sessions) != len(schedule) + absent_count:
    raise ValueError("Lượt có mặt và lượt vắng phải khớp 40 lượt dự kiến.")
print("Học viên:", len(students))
print("Lượt dự kiến:", len(students) * len(sessions))
print("Lượt có mặt:", len(schedule))
print("Lượt vắng:", absent_count)
morning_count = 0
afternoon_count = 0
for student, session in schedule:
    if session == "Sáng":
        morning_count += 1
    elif session == "Chiều":
        afternoon_count += 1
print("Ca Sáng:", morning_count)
print("Ca Chiều:", afternoon_count)
```

**Kết quả khi chạy:**

```text
Học viên: 20
Lượt dự kiến: 40
Lượt có mặt: 37
Lượt vắng: 3
Ca Sáng: 20
Ca Chiều: 17
```

Đây là bài tổng hợp: học viên được ghép với từng ca, ngoại lệ chỉ áp dụng cho đúng ca, rồi kiểm chứng 40 lượt dự kiến. Một học viên vẫn có thể xuất hiện trong **hai dòng khác nhau** mà không phải trùng lịch.

## 6. Nhầm lẫn dễ gặp

- `range(1, 4)` tạo `1, 2, 3`, không chứa `4`.
- `break` dừng toàn bộ vòng lặp hiện tại, còn `continue` chỉ bỏ qua phần còn lại của một lượt.
- Với `while`, phải thay đổi biến hoặc trạng thái để vòng lặp có thể kết thúc.
- `enumerate()` mặc định đếm vị trí từ 0; dùng `start=1` nếu muốn đếm từ 1.

## 7. Trắc nghiệm

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What does a `for` loop normally iterate over? | Vòng `for` thường duyệt qua gì?**

A. Only dictionary keys | Chỉ khóa của dictionary

B. Successive items from an iterable | Các phần tử liên tiếp của đối tượng duyệt được

C. Only a Boolean condition | Chỉ một điều kiện Boolean

D. Always index-value pairs | Luôn là cặp chỉ số-giá trị

**Đáp án: B**

**Giải thích:** Vòng `for` lần lượt lấy phần tử từ đối tượng duyệt được, ví dụ các giá trị `0`, `1`, `2` của `range(3)`. Cách hoạt động này khác `while` kiểm tra lại điều kiện ở mỗi lượt.


**Q2. When does a `while` loop repeat? | Khi nào vòng `while` tiếp tục lặp?**

A. Always for a predetermined count | Luôn theo số lượt đã xác định

B. Until exactly one iteration has completed | Chỉ đến khi chạy xong đúng một lượt

C. As long as its condition remains true | Chừng nào điều kiện vẫn đúng

D. Only when iterating over a list | Chỉ khi duyệt một list

**Đáp án: C**

**Giải thích:** Vòng `while` kiểm tra điều kiện trước mỗi lượt và chỉ lặp khi điều kiện còn đúng. Ví dụ `while n < 3:` dừng khi `n` đạt 3 nếu thân vòng lặp tăng `n` sau mỗi lượt.


**Q3. What is an iteration? | Một lần lặp là gì?**

A. A Boolean test before the loop | Phép kiểm tra Boolean trước vòng lặp

B. Two loops inside each other | Hai vòng lặp lồng nhau

C. One pass through the loop body | Một lượt thực hiện thân vòng lặp

D. A collection that can be iterated | Một tập hợp có thể duyệt

**Đáp án: C**

**Giải thích:** Một lần lặp là một lượt chạy thân vòng lặp. Với `for x in range(3):`, thân vòng lặp chạy ba lần, lần lượt `x` bằng 0, 1, 2.


**Q4. What are nested loops? | Vòng lặp lồng nhau là gì?**

A. A loop that runs exactly once | Một vòng chỉ chạy đúng một lần

B. Two loops written one after another | Hai vòng lặp viết nối tiếp nhau

C. A `for` and `while` with the same variable | `for` và `while` dùng cùng một biến

D. A loop placed inside another loop's body | Một vòng đặt trong thân vòng khác

**Đáp án: D**

**Giải thích:** Vòng lặp lồng nhau đặt một vòng trong thân vòng khác. Nếu vòng ngoài có 2 phần tử và vòng trong có 3 phần tử, thân vòng trong có thể chạy 2 nhân 3 bằng 6 lần, ứng với từng cặp kết hợp.


**Q5. What does `break` do inside a loop? | `break` làm gì trong vòng lặp?**

A. Skips only the current iteration's remaining statements | Chỉ bỏ qua các lệnh còn lại của lượt hiện tại

B. Does nothing and continues with the next statement | Không làm gì rồi chạy lệnh tiếp

C. Immediately exits the entire Python process | Thoát toàn bộ tiến trình Python

D. Immediately exits the innermost enclosing loop | Thoát ngay vòng lặp bao gần nhất

**Đáp án: D**

**Giải thích:** `break` kết thúc ngay vòng lặp bao gần nhất đang chạy. Với vòng lặp lồng nhau, nó không tự kết thúc mọi vòng ngoài; `continue` thì vẫn để vòng lặp tiếp tục.


**Q6. What does `continue` do? | `continue` có tác dụng gì?**

A. Skips the remaining body and moves toward the next iteration | Bỏ phần thân còn lại và chuyển tới lượt kế tiếp

B. Restarts the complete program | Khởi động lại toàn bộ chương trình

C. Exits the current loop completely | Kết thúc hẳn vòng lặp hiện tại

D. Acts as a no-op placeholder | Là câu lệnh giữ chỗ không thao tác

**Đáp án: A**

**Giải thích:** `continue` bỏ qua những câu lệnh còn lại trong lượt hiện tại rồi tiếp tục theo loại vòng lặp. Với `for`, chương trình lấy phần tử kế tiếp; với `while`, nó kiểm tra lại điều kiện.


**Q7. What does `pass` do? | `pass` làm gì?**

A. Skips the remainder of the iteration | Bỏ phần còn lại của lượt lặp

B. Rechecks the condition without running later statements | Kiểm tra lại điều kiện mà bỏ qua các lệnh sau

C. Performs no operation and then continues normally | Không thao tác gì rồi tiếp tục bình thường

D. Leaves the loop | Rời khỏi vòng lặp

**Đáp án: C**

**Giải thích:** `pass` là câu lệnh hợp lệ nhưng không làm gì, hữu ích để giữ chỗ cho thân khối bắt buộc. Khác `continue`, nó không bỏ qua những câu lệnh phía sau trong cùng lượt lặp.


**Q8. When does a loop's `else` execute? | `else` của vòng lặp chạy khi nào?**

A. Every time a loop body executes | Mỗi khi thân vòng lặp chạy

B. When the loop finishes normally without `break` | Khi vòng lặp kết thúc bình thường mà không gặp `break`

C. Only when `break` was executed | Chỉ khi đã chạy `break`

D. At the start of the first iteration | Khi bắt đầu lượt lặp đầu

**Đáp án: B**

**Giải thích:** `else` của vòng lặp chạy sau khi vòng lặp kết thúc bình thường: `for` duyệt hết phần tử hoặc điều kiện `while` thành sai. Nó bị bỏ qua nếu `break` kết thúc vòng lặp, khác `else` dự phòng của `if`.


**Q9. What does `range(1, 4)` represent? | `range(1, 4)` biểu diễn gì?**

A. Values 1, 2, 3 | Các giá trị 1, 2, 3

B. Values 1, 2, 3, 4 | Các giá trị 1, 2, 3, 4

C. Values 1, 3 | Các giá trị 1, 3

D. Values 0, 1, 2, 3 | Các giá trị 0, 1, 2, 3

**Đáp án: A**

**Giải thích:** `range(1, 4)` biểu diễn các số 1, 2, 3 vì mốc dừng 4 không được lấy. Nếu muốn bao gồm 4, cần đặt mốc dừng là 5.


**Q10. What does `enumerate(items)` provide? | `enumerate(items)` cung cấp gì?**

A. Pairs sorted by item value | Các cặp được sắp theo giá trị

B. Pairs of index and item | Các cặp chỉ số và phần tử

C. Only the items, without their indexes | Chỉ các phần tử, không kèm chỉ số

D. Only the indexes, without items | Chỉ chỉ số, không kèm phần tử

**Đáp án: B**

**Giải thích:** `enumerate(items)` tạo các cặp chỉ số và phần tử, mặc định bắt đầu từ chỉ số 0. Với `['a', 'b']`, khi duyệt sẽ nhận `(0, 'a')` rồi `(1, 'b')`; hàm không sắp xếp danh sách.


**Q11. What does `zip(a, b)` do? | `zip(a, b)` làm gì?**

A. Pairs elements at corresponding positions | Ghép phần tử ở cùng vị trí

B. Concatenates both inputs into one sequence | Nối hai đầu vào thành một dãy

C. Sorts the inputs together | Sắp xếp hai đầu vào cùng nhau

D. Generates every possible pair | Tạo mọi cặp kết hợp

**Đáp án: A**

**Giải thích:** `zip(a, b)` ghép phần tử ở cùng vị trí, ví dụ `list(zip([1, 2], ['x', 'y']))` cho `[(1, 'x'), (2, 'y')]`. Mặc định hàm dừng khi dãy ngắn nhất hết phần tử, chứ không tạo mọi cặp kết hợp.


**Q12. What does `reversed(items)` provide for a sequence? | `reversed(items)` cung cấp gì cho một dãy?**

A. Always returns a fully materialized list | Luôn trả về list đã tạo sẵn

B. Provides an iterator in reverse positional order | Cung cấp iterator theo thứ tự vị trí đảo ngược

C. Sorts elements from largest to smallest | Sắp phần tử từ lớn đến nhỏ

D. Preserves the original order | Giữ nguyên thứ tự ban đầu

**Đáp án: B**

**Giải thích:** `reversed()` cung cấp bộ duyệt ngược thứ tự vị trí của dãy phù hợp. Với `[3, 1, 2]`, nó cho `2, 1, 3`, không phải sắp xếp số giảm dần `3, 2, 1`.


**Q13. How many iterations does a complete `for` loop over `range(3)` execute? | Vòng `for` duyệt hết `range(3)` thực hiện bao nhiêu lượt lặp?**

A. 3 iterations | 3 lượt lặp

B. 4 iterations | 4 lượt lặp

C. 0 iterations | 0 lượt lặp

D. 2 iterations | 2 lượt lặp

**Đáp án: A**

**Giải thích:** `range(3)` tạo các giá trị `0`, `1`, `2`: bắt đầu mặc định từ 0 và không lấy mốc dừng 3. Vòng `for` duyệt hết sẽ chạy thân đúng ba lượt; đây là số lượt lặp, không có nghĩa dãy chứa giá trị 3.


**Q14. What does `range(2, 7, 2)` yield? | `range(2, 7, 2)` cho những số nào?**

A. 3, 5 | 3, 5

B. 2, 4, 6 | 2, 4, 6

C. 2, 3, 4, 5, 6 | 2, 3, 4, 5, 6

D. 2, 4, 6, 8 | 2, 4, 6, 8

**Đáp án: B**

**Giải thích:** `range(start, stop, step)` bắt đầu tại 2, mỗi lượt cộng thêm 2 và không lấy giá trị đạt hoặc vượt mốc dừng 7. Vì vậy dãy là 2, 4, 6, không phải 2, 4, 6, 8.


**Q15. What does `enumerate(['a','b'])` start indexing from? | `enumerate(['a','b'])` bắt đầu chỉ số từ đâu?**

A. The number of items | Số phần tử

B. -1 | -1

C. 0 | 0

D. 1 | 1

**Đáp án: C**

**Giải thích:** `enumerate()` mặc định bắt đầu chỉ số bằng `0` nếu không truyền `start`. Với `['a', 'b']`, cặp đầu là `(0, 'a')`; `enumerate(items, start=1)` mới bắt đầu từ 1.


**Q16. What does `list(zip([1,2], ['a']))` contain? | `list(zip([1,2], ['a']))` gồm gì?**

A. `[(1, 'a'), (2, 'a')]` | `[(1, 'a'), (2, 'a')]`

B. `[(1, 2), ('a',)]` | `[(1, 2), ('a',)]`

C. `[(1, 'a'), (2, None)]` | `[(1, 'a'), (2, None)]`

D. `[(1, 'a')]` | `[(1, 'a')]`

**Đáp án: D**

**Giải thích:** `zip()` lấy một phần tử từ mỗi dãy ở một lượt và dừng khi dãy ngắn hơn hết. Vì vậy `list(zip([1,2], ['a']))` chỉ chứa `[(1, 'a')]`, không có cặp chứa 2.


**Q17. What is a common cause of an infinite `while` loop? | Nguyên nhân thường gặp khiến `while` lặp vô hạn là gì?**

A. A function containing `pass` is never called | Một hàm có `pass` không được gọi

B. A `break` is reached in the first iteration | Gặp `break` ở lượt đầu

C. A `for` loop exhausts a finite iterable | `for` duyệt hết một dãy hữu hạn

D. The `while` condition stays true and no exit is reached | Điều kiện `while` luôn đúng và không gặp lối thoát

**Đáp án: D**

**Giải thích:** Vòng `while` có thể lặp vô hạn khi điều kiện luôn đúng, ví dụ `while n < 3:` không bao giờ thay đổi `n` và không gặp `break`. Cần cập nhật biến hướng tới điều kiện sai hoặc chủ động có lối thoát.


**Q18. How can a loop ignore invalid data and continue processing? | Làm sao bỏ qua dữ liệu lỗi nhưng vẫn xử lý phần tử sau?**

A. Use `continue` for that invalid item | Dùng `continue` với phần tử lỗi

B. Use `return` to exit the whole function | Dùng `return` thoát toàn bộ hàm

C. Use only `pass` in the invalid-data branch | Chỉ dùng `pass` trong nhánh dữ liệu lỗi

D. Use `break` when the invalid item appears | Dùng `break` khi gặp phần tử lỗi

**Đáp án: A**

**Giải thích:** Dùng `continue` khi cần bỏ qua một phần tử không hợp lệ nhưng vẫn xử lý các phần tử sau. `break` sẽ kết thúc vòng lặp, còn chỉ dùng `pass` không ngăn những lệnh phía sau xử lý phần tử lỗi.


**Q19. How can a search stop immediately after a match? | Làm sao dừng tìm kiếm ngay khi đã thấy phần tử phù hợp?**

A. Use `pass` after the match | Dùng `pass` sau khi khớp

B. Use `continue` after the match | Dùng `continue` sau khi khớp

C. Use `else` instead of checking | Dùng `else` thay kiểm tra

D. Use `break` after the match | Dùng `break` sau khi khớp

**Đáp án: D**

**Giải thích:** Dùng `break` ngay khi tìm thấy phần tử cần tìm vì không cần kiểm tra những phần tử còn lại. `continue` chỉ chuyển tới phần tử tiếp theo, còn `pass` không dừng việc tìm kiếm.


**Q20. How do you traverse every combination of two small collections? | Làm sao duyệt mọi kết hợp của hai nhóm nhỏ?**

A. Use `enumerate()` on one collection | Dùng `enumerate()` trên một nhóm

B. Use two separate, nonnested loops | Dùng hai vòng độc lập không lồng nhau

C. Use one loop nested inside the other | Đặt một vòng lồng bên trong vòng còn lại

D. Use `zip()` on the two collections | Dùng `zip()` trên hai nhóm

**Đáp án: C**

**Giải thích:** Muốn duyệt mọi cặp kết hợp của hai nhóm, đặt vòng duyệt nhóm thứ hai bên trong vòng duyệt nhóm thứ nhất. Với 2 phần tử ngoài và 3 phần tử trong, ta được 6 cặp; `zip()` chỉ ghép phần tử cùng vị trí.

## 8. Nối sang bài tiếp theo

`Điều kiện → Vòng lặp → Xử lý hàng loạt`.
