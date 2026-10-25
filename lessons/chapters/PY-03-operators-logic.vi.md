# PY-03 — Toán tử số học, so sánh và logic


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Arithmetic** — số học; **Comparison** — so sánh.

`Kiểu dữ liệu → Toán tử → Điều kiện → Quy tắc nghiệp vụ`

**Học xong dùng để làm gì?** Tính tổng tiền, so sánh ngưỡng điểm và kết hợp nhiều điều kiện thành kết quả đúng/sai.

**Kết nối kiến thức tiếp theo:** Sang PY-04, dùng chính các phép so sánh và logic đó để quyết định chương trình đi nhánh nào.

## 2. English vocabulary — Từ vựng

| English | Nghĩa tiếng Việt | Giải thích |
|---|---|---|
| Arithmetic | số học | Phép cộng trừ nhân chia |
| Comparison | so sánh | So sánh hai giá trị |
| Logical | logic | Kết hợp các điều kiện |
| Bitwise | thao tác bit | Phép tính trên các bit của số nguyên |

## 3. Các hàm và tùy chọn Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cú pháp | Mục đích và ý nghĩa lựa chọn |
|---|---|
| `+, -, *, /` | Tính số học và tỷ lệ |
| `//, %, **` | Chia nguyên, lấy dư, lũy thừa |
| `==, !=, <=, >=, and, or` | So sánh và kết hợp điều kiện |
| `&, |, ^` | Chỉ dùng cho cờ bit hoặc toán bit được thiết kế rõ |


## 4. Khái niệm liên quan

**Toán tử (operator)** là dấu hoặc từ khóa thực hiện một thao tác trên dữ liệu. Với một đơn hàng, ta dùng toán tử số học để tính tiền, so sánh để kiểm tra ngưỡng, rồi dùng logic để ghép điều kiện. Toán tử bit cũng dùng ký hiệu nhưng xử lý các chữ số nhị phân thay vì điều kiện thông thường.

### 4.1. Arithmetic — Toán tử số học

**Từ vựng trong mục:** **Arithmetic** — số học; **Multiplication** — phép nhân.

Số học giúp tính từ các dữ liệu có sẵn: `+` cộng, `-` trừ, `*` nhân, `/` chia. Ví dụ cửa hàng bán 5 món, mỗi món 3 nghìn đồng: lấy số lượng nhân đơn giá để được tổng 15 nghìn đồng. Python còn có `//` chia lấy phần nguyên và `%` lấy phần dư khi chia thùng hoặc chia nhóm.

```python
# Mục đích: Toán tử số học.
print(5 * 3)
```

**Kết quả khi chạy:**

```text
15
```

Giá trị `15` là tổng tiền theo đơn vị nghìn đồng của ví dụ.

### 4.2. Comparison — Toán tử so sánh

**Từ vựng trong mục:** **Comparison** — so sánh; **Boolean** — đúng/sai.

So sánh trả lời một câu hỏi bằng `True` hoặc `False`. Nếu kho có 8 món và đơn hàng cần 5 món, điều kiện `8 >= 5` kiểm tra đủ hàng để giao không. Các dấu `>`, `<`, `>=`, `<=`, `==`, `!=` biểu diễn lớn hơn, nhỏ hơn, bằng hoặc khác nhau. Phân biệt `==` để kiểm tra với `=` để gán.

```python
# Mục đích: Toán tử so sánh.
print(8 >= 5)
```

**Kết quả khi chạy:**

```text
True
```

Kho có ít nhất 5 món nên điều kiện đủ hàng là đúng.

### 4.3. Logical — Toán tử logic

**Từ vựng trong mục:** **Logical** — logic; **AND** — và; **OR** — hoặc.

Sau khi có các điều kiện đúng/sai, `and` yêu cầu mọi điều kiện cùng đúng; `or` chỉ cần một điều kiện đúng; `not` đảo trạng thái. Ví dụ người dùng đã đăng nhập (`True`) nhưng chưa xác minh (`False`): nếu hệ thống bắt buộc cả hai thì `and` trả về `False`.

```python
# Mục đích: Toán tử logic.
print(True and False)
```

**Kết quả khi chạy:**

```text
False
```

Một trong hai điều kiện chưa đạt, nên không thỏa yêu cầu `and`.

### 4.4. Bitwise — Toán tử theo bit

**Từ vựng trong mục:** **Bitwise** — theo bit; **Binary** — nhị phân.

Máy tính biểu diễn số nguyên bằng các bit `0` và `1`. Toán tử `&` so từng vị trí bit và chỉ giữ `1` khi hai phía cùng có `1`. Số 5 là `0101`, số 3 là `0011`; phần chung chỉ còn `0001`, tương ứng số 1. Đây là phép xử lý số nguyên theo bit, **khác** `and` dùng để nối điều kiện logic.

```python
# Mục đích: Toán tử theo bit.
print(5 & 3)
```

**Kết quả khi chạy:**

```text
1
```

Số `1` là kết quả phép AND theo bit giữa 5 và 3.
## 5. Năm tình huống ứng dụng — từ phép toán đến quy tắc tổng hợp

### Tình huống 1 — Cấp 1: Tính giảm giá cho 10 mặt hàng

**Từ vựng trong mục:** **Arithmetic** — toán tử số học; **Discount** — giảm giá.

**Tình huống thực tế:** Quầy đồ dùng học tập có **10 mặt hàng**, mỗi phần tử trong bảng giá là giá của một món, đơn vị **nghìn đồng**; giá lần lượt là 100, 150, 200, 250, 300, 120, 180, 220, 400 và 160. Hôm nay tất cả cùng giảm 10%. Cần tính tổng giá gốc và tổng tiền sau ưu đãi nếu khách mua một món mỗi loại.

**Vì sao chọn cách này?** Phép nhân theo tỷ lệ 90% cho biết giá sau giảm; dùng tổng sau giảm của đủ 10 mặt hàng, không áp giảm hai lần. Đây là phép toán số học trực tiếp, chưa cần nhánh ưu tiên.

**Quy trình:**
1. Lưu 10 đơn giá và tỷ lệ giảm 10%.
2. Lấy 90% của mỗi giá rồi cộng tổng.
3. So sánh tổng trước/sau giảm.

```python
prices = [100,150,200,250,300,120,180,220,400,160]
discount = 0.10
original = sum(prices)
after_discount = sum(price * (1 - discount) for price in prices)
assert len(prices) == 10
print("Mặt hàng:", len(prices))
print("Gốc (nghìn đồng):", original)
print("Sau giảm (nghìn đồng):", round(after_discount))
```

**Kết quả khi chạy:**

```text
Mặt hàng: 10
Gốc (nghìn đồng): 2080
Sau giảm (nghìn đồng): 1872
```

Đầu vào là **giá từng mặt hàng**, không phải số lượng bán. Mức giảm 10% áp dụng như nhau nên có thể đối chiếu với 90% tổng tiền gốc.

### Tình huống 2 — Cấp 2: So hai điều kiện VIP của 12 khách

**Từ vựng trong mục:** **Comparison** — so sánh; **Logical AND** — phép và.

**Tình huống thực tế:** Chương trình xét **12 khách hàng**; mỗi hàng gồm mã C01…C12, số năm gắn bó (năm) và tổng mua hàng (đồng). Cửa hàng chỉ xếp VIP khi khách có **ít nhất 5 năm** và đã chi **từ 1.000.000 đồng**. Hãy trả về mã tất cả khách đạt chuẩn và tổng số VIP, lưu ý người chỉ đạt một trong hai ngưỡng không được tính.

**Vì sao chọn cách này?** Toán tử `>=` bảo toàn các trường hợp nằm đúng biên. Hai điều kiện buộc đúng cùng lúc nên phải dùng `and`, không dùng `or`.

**Quy trình:**
1. Ghép năm thành viên với số tiền của đúng khách ở cùng hàng.
2. So hai ngưỡng bằng `>=` và nối bằng `and`.
3. Liệt kê đủ khách đạt và đếm kết quả.

```python
years = [2,5,6,4,8,5,1,9,3,7,5,2]
spending_vnd = [1200000,900000,1400000,2200000,1800000,1000000,700000,850000,1500000,3000000,990000,1600000]
customers = [(f"C{i:02d}", years[i-1], spending_vnd[i-1]) for i in range(1, 13)]
vip_ids = [code for code, member_years, spending in customers
           if member_years >= 5 and spending >= 1000000]
assert len(customers) == 12
print("Số khách:", len(customers))
print("VIP:", len(vip_ids))
print("Mã VIP:", ", ".join(vip_ids))
```

**Kết quả khi chạy:**

```text
Số khách: 12
VIP: 4
Mã VIP: C03, C05, C06, C10
```

Mẫu C06 nằm **đúng cả hai ngưỡng** nên vẫn là VIP; C02 chỉ đạt năm thành viên nhưng chưa đủ tiền nên không thuộc danh sách.

### Tình huống 3 — Cấp 3: Đóng thùng 15 mã hàng, tính cả số dư

**Từ vựng trong mục:** **Integer division** — chia nguyên; **Modulo** — chia lấy dư; **Check** — đối chiếu.

**Tình huống thực tế:** Kho có **15 mã hàng**, mỗi hàng thể hiện số món tồn kho của một SKU. Một thùng chỉ chứa **6 món cùng mã** để không trộn loại. Hãy tính tổng số thùng đầy và tổng món còn rời; kiểm tra lại bằng cách cộng món trong thùng với món rời.

**Vì sao chọn cách này?** Chia nguyên `//` đếm thùng đủ sáu món trên từng SKU; phép `%` đếm số món chưa đóng đầy. Không được cộng tất cả tồn kho rồi chia 6 một lần, vì mỗi thùng chỉ nhận một mã.

**Quy trình:**
1. Tính `stock // 6` và `stock % 6` cho từng SKU.
2. Cộng hai kết quả theo 15 SKU.
3. Xác minh `6 × tổng thùng + món rời` bằng tổng hàng gốc.

```python
stocks = [16,23,34,7,12,5,31,42,18,27,15,9,35,14,20]
box_size = 6
full_boxes = sum(stock // box_size for stock in stocks)
loose_items = sum(stock % box_size for stock in stocks)
assert len(stocks) == 15
assert full_boxes * box_size + loose_items == sum(stocks)
print("Số SKU:", len(stocks))
print("Thùng đầy:", full_boxes)
print("Món rời:", loose_items)
```

**Kết quả khi chạy:**

```text
Số SKU: 15
Thùng đầy: 45
Món rời: 38
```

Số dư được giữ **riêng cho từng mã hàng**. Điều kiện đối chiếu bằng `assert` giúp phát hiện nếu một bước tính đã làm mất hàng.

### Tình huống 4 — Cấp 4: Đọc cờ bit của 18 thiết bị, phân biệt mất tín hiệu

**Từ vựng trong mục:** **Bitwise AND** — phép và theo bit; **Mask** — mặt nạ bit; **Missing** — thiếu dữ liệu.

**Tình huống thực tế:** Hệ thống nhận **18 trạng thái thiết bị**, một hàng là mã cờ nhị phân của thiết bị; bit `0b0010` báo cảnh báo, bit `0b1000` báo có kết nối gửi dữ liệu. Thiết bị thứ 17 chưa gửi trạng thái (`None`). Hãy đếm số thiết bị báo cảnh báo và số thiết bị có cờ gửi, đồng thời báo bao nhiêu giá trị thiếu.

**Vì sao chọn cách này?** Bitwise `&` chỉ kiểm tra đúng bit được chọn, không nhầm với `and` (kết hợp biểu thức Boolean). Trước khi làm phép bit, cần bỏ `None` vì đó là mất tín hiệu chứ không phải trạng thái `0`.

**Quy trình:**
1. Đọc 18 giá trị cờ, tách những dòng chưa gửi.
2. Dùng `status & mask` để kiểm tra từng bit trên dữ liệu hợp lệ.
3. Đếm riêng cảnh báo, gửi tín hiệu và trạng thái thiếu.

```python
flags = [10,2,0,8,3,11,1,10,14,2,0,9,10,12,3,11,None,2]
valid = [status for status in flags if status is not None]
warning_count = sum((status & 0b0010) != 0 for status in valid)
sending_count = sum((status & 0b1000) != 0 for status in valid)
assert len(flags) == 18
print("Trạng thái hợp lệ:", len(valid))
print("Cảnh báo:", warning_count)
print("Đang gửi:", sending_count)
print("Thiếu:", len(flags) - len(valid))
```

**Kết quả khi chạy:**

```text
Trạng thái hợp lệ: 17
Cảnh báo: 11
Đang gửi: 9
Thiếu: 1
```

Một thiết bị có thể vừa cảnh báo vừa đang gửi, nên hai tập không loại trừ nhau. Trường hợp thiết bị mất tín hiệu cần được xử lý riêng, không gán trạng thái mặc định không có cảnh báo.

### Tình huống 5 — Cấp 5: Xếp thứ tự xử lý 20 đơn hàng bằng nhiều quy tắc

**Từ vựng trong mục:** **Logical OR** — phép hoặc; **Logical AND** — phép và; **Boolean** — đúng/sai.

**Tình huống thực tế:** Điều phối viên có **20 đơn hàng** O01…O20; mỗi hàng gồm giá trị đơn (đồng), số ngày trễ (ngày) và cờ còn hàng trong kho (`True`/`False`). Đơn được ưu tiên nếu **giá trị từ 2.000.000 đồng hoặc trễ từ 3 ngày**, **đồng thời còn hàng**. Cần trả số đơn ưu tiên, danh sách mã và tổng giá trị các đơn được phép ưu tiên; đơn chưa có hàng phải đứng ngoài danh sách dù tiền cao.

**Vì sao chọn cách này?** Dùng ngoặc quanh hai điều kiện `or` trước khi kết hợp với `and` để quy tắc kinh doanh không đổi do thứ tự ưu tiên toán tử. Đây là một quyết định tổng hợp nhiều cột, không phải chỉ so một con số.

**Quy trình:**
1. Ghép dữ liệu theo đúng mã đơn và xác nhận ba cột đồng hàng.
2. Tính `(giá trị >= ngưỡng or ngày trễ >= ngưỡng) and có hàng`.
3. Lọc 20 đơn, tính tổng tiền thuộc nhóm ưu tiên và kiểm tra mọi đơn chọn được đều còn hàng.

```python
amount_vnd = [500000,900000,1300000,1700000,2100000,2500000,500000,900000,1300000,1700000,2100000,2500000,500000,900000,1300000,1700000,2100000,2500000,500000,900000]
late_days = [0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4]
in_stock = [True,True,True,False,True,True,True,True,True,True,True,False,True,True,True,True,True,False,True,True]
orders = [(f"O{i:02d}", amount_vnd[i-1], late_days[i-1], in_stock[i-1])
          for i in range(1, 21)]
priority = [(code, amount) for code, amount, delay, available in orders
            if (amount >= 2000000 or delay >= 3) and available]
priority_ids = [code for code, amount in priority]
assert len(orders) == 20
assert all(next(v for c, p, d, v in orders if c == code) for code in priority_ids)
print("Số đơn:", len(orders))
print("Ưu tiên:", len(priority))
print("Mã ưu tiên:", ", ".join(priority_ids))
print("Giá trị ưu tiên (đồng):", sum(amount for code, amount in priority))
```

**Kết quả khi chạy:**

```text
Số đơn: 20
Ưu tiên: 10
Mã ưu tiên: O05, O06, O09, O10, O11, O14, O15, O17, O19, O20
Giá trị ưu tiên (đồng): 15400000
```

Ba cột là thuộc tính của **một đơn**, không phải ba danh sách độc lập để so riêng. Với kho hết hàng, điều kiện `and available` ngăn hệ thống ưu tiên những đơn chưa thể xử lý.

## 6. Những nhầm lẫn thường gặp

- `=` dùng để gán giá trị, còn `==` dùng để so sánh bằng nhau.
- `and` và `or` kiểm tra điều kiện; `&` và `|` thao tác trên các bit, không thay thế tùy tiện cho nhau.
- `/` cho kết quả chia thông thường, `//` lấy phần nguyên theo hướng làm tròn xuống, `%` lấy số dư.
- Với giá tiền cần tính chính xác đến từng đồng, nên cân nhắc dùng số nguyên đồng hoặc `Decimal` thay vì dựa vào số thực cho phép tính tiền phức tạp.

## 7. Trắc nghiệm

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. Which operator performs multiplication? | Toán tử nào thực hiện phép nhân?**

A. `*` | `*`

B. `&` | `&`

C. `==` | `==`

D. `and` | `and`

**Đáp án: A**

**Giải thích:** `*` nhân các số, ví dụ `3 * 4` cho `12`. `==` so sánh giá trị, `and` kết hợp điều kiện logic, còn `&` thực hiện AND theo bit trên số nguyên.


**Q2. Which operator tests equality? | Toán tử nào kiểm tra bằng nhau?**

A. `*` | `*`

B. `==` | `==`

C. `&` | `&`

D. `and` | `and`

**Đáp án: B**

**Giải thích:** `==` kiểm tra hai giá trị có bằng nhau và tạo Boolean, ví dụ `2 == 2` là `True`. Một dấu `=` dùng để gán giá trị cho tên, chứ không so sánh.


**Q3. Which Python keyword performs short-circuit logical AND? | Từ khóa Python nào thực hiện phép VÀ logic có đánh giá ngắn mạch?**

A. `==` | `==`

B. `&` | `&`

C. `and` | `and`

D. `*` | `*`

**Đáp án: C**

**Giải thích:** Từ khóa `and` thực hiện phép VÀ logic ngắn mạch: nếu vế trái sai, Python không đánh giá vế phải. Ký hiệu `&` thực hiện AND theo bit trên số nguyên và kể cả dùng với Boolean cũng không đánh giá ngắn mạch.


**Q4. Which operator performs bitwise AND on integers? | Toán tử nào thực hiện AND theo bit trên số nguyên?**

A. `and` | `and`

B. `==` | `==`

C. `*` | `*`

D. `&` | `&`

**Đáp án: D**

**Giải thích:** Với số nguyên, `&` thực hiện AND trên từng bit: `5 & 3` đối chiếu `0101` và `0011`, được `0001` (`1`). Đây không phải phép nhân thông thường hay từ khóa logic `and`.


**Q5. What does `7 // 2` return? | `7 // 2` trả về gì?**

A. `1` | `1`

B. `3.5` | `3.5`

C. `3` | `3`

D. `8` | `8`

**Đáp án: C**

**Giải thích:** `//` thực hiện chia lấy sàn: `7 / 2` bằng `3.5`, làm tròn xuống được `3`. Với thương âm, làm tròn xuống nghĩa là về âm vô cực nên `-7 // 2` bằng `-4`.


**Q6. What does `7 % 2` return? | `7 % 2` trả về gì?**

A. `1` | `1`

B. `3.5` | `3.5`

C. `3` | `3`

D. `8` | `8`

**Đáp án: A**

**Giải thích:** `%` trả phần dư theo phép chia lấy sàn: `7 = 2 * 3 + 1`, nên `7 % 2` bằng `1`. Nó không phải thương `3` hay kết quả chia thực `3.5`.


**Q7. What does `2 ** 3` return? | `2 ** 3` trả về gì?**

A. `3` | `3`

B. `1` | `1`

C. `3.5` | `3.5`

D. `8` | `8`

**Đáp án: D**

**Giải thích:** `**` là phép lũy thừa: `2 ** 3` nhân 2 với chính nó ba lần, cho `8`. Một dấu `*` là phép nhân, còn `^` trong Python là XOR theo bit, không phải lũy thừa.


**Q8. What does `7 / 2` return? | `7 / 2` trả về gì?**

A. `3.5` | `3.5`

B. `3` | `3`

C. `1` | `1`

D. `8` | `8`

**Đáp án: A**

**Giải thích:** Trong Python 3, `/` chia thực nên `7 / 2` trả về số thực `3.5`. Toán tử `//` lấy sàn thương được `3`, còn `%` trả phần dư `1`.


**Q9. What is `True and False`? | `True and False` bằng gì?**

A. `True` (Boolean) | `True` (Boolean)

B. `None` | `None`

C. `0` (integer) | `0` (số nguyên)

D. `False` (Boolean) | `False` (Boolean)

**Đáp án: D**

**Giải thích:** `and` Boolean yêu cầu cả hai vế đều đúng, nhưng vế thứ hai là `False`. Vì thế `True and False` cho Boolean `False`, không phải số nguyên `0` hay `None`.


**Q10. What is `False or True`? | `False or True` bằng gì?**

A. `1` (integer) | `1` (số nguyên)

B. `True` (Boolean) | `True` (Boolean)

C. `False` (Boolean) | `False` (Boolean)

D. `None` | `None`

**Đáp án: B**

**Giải thích:** `or` Boolean đúng nếu có ít nhất một vế đúng; vế phải của `False or True` là `True`. Kết quả ở đây là Boolean `True`, không phải số nguyên `1`, dù `True` có thể hoạt động như 1 trong một số phép số học.


**Q11. What does `not True` produce? | `not True` cho kết quả gì?**

A. `0` (integer) | `0` (số nguyên)

B. `None` | `None`

C. `False` (Boolean) | `False` (Boolean)

D. `True` (Boolean) | `True` (Boolean)

**Đáp án: C**

**Giải thích:** `not` đảo giá trị logic nên `not True` thành Boolean `False`. Ngược lại `not False` là `True`; số nguyên không là giá trị thuộc kiểu khác.


**Q12. What does `5 & 3` produce? | `5 & 3` tạo ra gì?**

A. `False` (Boolean) | `False` (Boolean)

B. `5` (integer) | `5` (số nguyên)

C. `True` (Boolean) | `True` (Boolean)

D. `1` (integer) | `1` (số nguyên)

**Đáp án: D**

**Giải thích:** Hai số nguyên là `5 = 0101` và `3 = 0011` ở hệ nhị phân bốn bit. Toán tử `&` chỉ giữ vị trí có cả hai bit bằng 1, cho `0001`, tức số nguyên `1`, không phải Boolean `True`.


**Q13. Which operator tests that two values differ? | Toán tử nào kiểm tra hai giá trị khác nhau?**

A. `!=` | `!=`

B. `>=` | `>=`

C. `=` | `=`

D. `in` | `in`

**Đáp án: A**

**Giải thích:** `!=` kiểm tra hai giá trị có khác nhau: `3 != 4` là `True`, còn `3 != 3` là `False`. Nó đối lập với `==` dùng để kiểm tra bằng nhau.


**Q14. Which operator means 'at least'? | Toán tử nào biểu diễn 'lớn hơn hoặc bằng'?**

A. `!=` | `!=`

B. `in` | `in`

C. `>=` | `>=`

D. `=` | `=`

**Đáp án: C**

**Giải thích:** `>=` nghĩa là lớn hơn hoặc bằng, nên `5 >= 5` và `6 >= 5` đều là `True`. Trường hợp bằng ngưỡng rất quan trọng: dùng `>` sẽ loại đúng giá trị 5.


**Q15. Which operator checks membership in a collection? | Toán tử nào kiểm tra phần tử thuộc một tập dữ liệu?**

A. `!=` | `!=`

B. `in` | `in`

C. `>=` | `>=`

D. `=` | `=`

**Đáp án: B**

**Giải thích:** Toán tử `in` kiểm tra phần tử có thuộc tập hợp: `2 in [1, 2, 3]` là `True`, còn `4 in [1, 2, 3]` là `False`. Nó không gán giá trị hay so sánh độ lớn.


**Q16. Which operator assigns a new value to a variable? | Toán tử nào gán giá trị mới cho biến?**

A. `>=` | `>=`

B. `!=` | `!=`

C. `=` | `=`

D. `in` | `in`

**Đáp án: C**

**Giải thích:** Toán tử gán `=` liên kết tên với giá trị, như `total = 10`. Muốn so sánh hai giá trị thì dùng `==`; dùng `=` trong điều kiện so sánh thông thường sẽ sai cú pháp.


**Q17. Which result comes from `3 > 5`? | `3 > 5` trả về gì?**

A. `0` (integer) | `0` (số nguyên)

B. `False` (Boolean) | `False` (Boolean)

C. `True` (Boolean) | `True` (Boolean)

D. `None` | `None`

**Đáp án: B**

**Giải thích:** `>` kiểm tra lớn hơn nghiêm ngặt, mà 3 nhỏ hơn 5 nên `3 > 5` cho Boolean `False`. Kết quả là giá trị logic, không phải số nguyên `0`.


**Q18. What result comes from `2 + 3 * 4`? | `2 + 3 * 4` bằng bao nhiêu?**

A. `9` | `9`

B. `14` | `14`

C. `False` | `False`

D. `20` | `20`

**Đáp án: B**

**Giải thích:** Phép nhân có độ ưu tiên cao hơn cộng: tính `3 * 4 = 12` trước, rồi `2 + 12 = 14`. Thêm ngoặc như `(2 + 3) * 4` sẽ đổi kết quả thành `20`.


**Q19. What does `True or False` return? | `True or False` trả về gì?**

A. `True` (Boolean) | `True` (Boolean)

B. `1` (integer) | `1` (số nguyên)

C. `False` (Boolean) | `False` (Boolean)

D. `None` | `None`

**Đáp án: A**

**Giải thích:** `or` đúng khi ít nhất một toán hạng Boolean đúng; vì vế trái là `True` nên `True or False` trả `True`. Với đầu vào Boolean, đây là Boolean `True`, không phải số nguyên `1`.


**Q20. What does `5 ^ 3` return for integers? | `5 ^ 3` trả về gì với số nguyên?**

A. `5` | `5`

B. `2` | `2`

C. `15` | `15`

D. `6` | `6`

**Đáp án: D**

**Giải thích:** `^` là XOR theo bit, không phải lũy thừa: `5 = 0101` và `3 = 0011` khác nhau tại các vị trí bit `0100` và `0010`, cho `0110` = `6`. Lũy thừa phải dùng `**`, không dùng `^`.

## 8. Nối sang bài kế tiếp

`Kiểu dữ liệu → Toán tử → Điều kiện → Quy tắc nghiệp vụ`.
