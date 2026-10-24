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
## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Xếp loại điểm

**Từ vựng trong mục:** **Condition** — điều kiện.

**Tình huống thực tế:** Trung tâm đào tạo xếp điểm từ 90 trở lên là A, từ 80 đến dưới 90 là B, còn lại ghi `Other`. Một học viên đạt 85 điểm trên thang 100.

**Yêu cầu:** Viết chương trình in mức xếp loại của học viên.

**Vì sao chọn cách giải này?** Dùng `if` xét mốc cao nhất trước, `elif` xét mốc 80 khi chưa đạt 90; `else` xử lý các điểm còn lại.

**Quy trình giải:**

1. Lưu điểm `85`.
2. Kiểm tra điểm từ 90 trở lên.
3. Nếu không đạt, kiểm tra từ 80 trở lên.
4. In loại tương ứng.

```python
# Mục đích: Xếp loại điểm.
score=85
if score>=90:
    grade="A"
elif score>=80:
    grade="B"
else:
    grade="Other"
print(grade)
```

**Kết quả khi chạy:**

```text
B
```

**Kết quả:** `B` — 85 điểm đạt mức B theo quy tắc đã nêu.

### Tình huống 2 — Cảnh báo hàng gần hết

**Từ vựng trong mục:** **Branch** — nhánh.

**Tình huống thực tế:** Cửa hàng chia tồn kho thành ba trạng thái: hết hàng nếu số lượng không lớn hơn 0, gần hết nếu còn từ 1 đến 5 món, bình thường nếu còn trên 5 món. Một sản phẩm hiện còn 4 món.

**Yêu cầu:** Viết chương trình in trạng thái tồn kho bằng `Out`, `Low` hoặc `OK`.

**Vì sao chọn cách giải này?** Dùng `if`/`elif`/`else` để chỉ chọn một trong ba trạng thái; kiểm tra hết hàng trước khi kiểm tra gần hết.

**Quy trình giải:**

1. Lưu số lượng `qty = 4`.
2. Kiểm tra hết hàng (`qty <= 0`).
3. Nếu chưa hết, kiểm tra gần hết (`qty <= 5`).
4. In trạng thái phù hợp.

```python
# Mục đích: Cảnh báo hàng gần hết.
qty=4
if qty<=0:
    state="Out"
elif qty<=5:
    state="Low"
else:
    state="OK"
print(state)
```

**Kết quả khi chạy:**

```text
Low
```

**Kết quả:** `Low` — còn 4 món nên hàng đang gần hết.

### Tình huống 3 — Xét VIP

**Từ vựng trong mục:** **Threshold** — ngưỡng.

**Tình huống thực tế:** Cửa hàng chỉ công nhận VIP khi khách là thành viên ít nhất 5 năm và đã chi tối thiểu 1.000.000 đồng. Một khách đã tham gia 6 năm và chi 1.500.000 đồng.

**Yêu cầu:** In `VIP` nếu khách đạt cả hai điều kiện, ngược lại in `Regular`.

**Vì sao chọn cách giải này?** `and` nối hai phép so sánh; `if` chọn nhánh VIP khi cả hai đúng và `else` xử lý trường hợp còn lại.

**Quy trình giải:**

1. Lưu thời gian tham gia và tổng tiền đã chi.
2. So sánh từng giá trị với ngưỡng.
3. Kết hợp hai điều kiện bằng `and`.
4. In loại khách theo nhánh phù hợp.

```python
# Mục đích: Xét VIP.
years,paid=6,1500000
if years>=5 and paid>=1000000:
    print("VIP")
else:
    print("Regular")
```

**Kết quả khi chạy:**

```text
VIP
```

**Kết quả:** `VIP` — khách đạt cả hai ngưỡng quy định.

### Tình huống 4 — Kiểm tra cảm biến

**Từ vựng trong mục:** **Nested if** — điều kiện lồng.

**Tình huống thực tế:** Hệ thống giám sát nhận trạng thái kết nối `online = True` và nhiệt độ `82` °C. Khi thiết bị mất kết nối, màn hình phải hiển thị `Offline`; nếu kết nối, nhiệt độ từ 80 °C trở lên báo `Hot`, còn thấp hơn báo `Normal`.

**Yêu cầu:** Viết chương trình hiển thị đúng trạng thái thiết bị.

**Vì sao chọn cách giải này?** Kiểm tra kết nối bằng `if` trước; chỉ khi đang online mới xét nhiệt độ bằng biểu thức điều kiện. Không kết luận nhiệt độ của thiết bị đã mất kết nối.

**Quy trình giải:**

1. Lưu trạng thái online và nhiệt độ.
2. Nếu online, so sánh nhiệt độ với mốc 80 °C.
3. In `Hot` hoặc `Normal`; nếu offline, in `Offline`.

```python
# Mục đích: Kiểm tra cảm biến.
online,temp=True,82
if online:
    print("Hot" if temp>=80 else "Normal")
else:
    print("Offline")
```

**Kết quả khi chạy:**

```text
Hot
```

**Kết quả:** `Hot` — thiết bị đang kết nối và nhiệt độ 82 °C đạt ngưỡng cảnh báo.

### Tình huống 5 — Tính quý của tháng

**Từ vựng trong mục:** **Condition** — điều kiện.

**Tình huống thực tế:** Một phần mềm báo cáo cần đổi số tháng thành quý trong năm: tháng 1–3 là quý 1, 4–6 là quý 2, 7–9 là quý 3, 10–12 là quý 4. Tháng cần kiểm tra là tháng 10.

**Yêu cầu:** Viết chương trình in số quý của tháng đã cho; nếu tháng không thuộc khoảng 1–12, in `Invalid`.

**Vì sao chọn cách giải này?** Dùng `if` kiểm tra tháng hợp lệ trước, rồi phép chia nguyên `//` để xác định quý; `else` bắt tháng ngoài khoảng.

**Quy trình giải:**

1. Lưu tháng bằng `month = 10`.
2. Kiểm tra `1 <= month <= 12`.
3. Nếu hợp lệ, tính `(month - 1) // 3 + 1`; ngược lại báo `Invalid`.

```python
# Mục đích: Tính quý của tháng.
month=10
if 1<=month<=12:
    print((month-1)//3+1)
else:
    print("Invalid")
```

**Kết quả khi chạy:**

```text
4
```

**Kết quả:** `4` — tháng 10 thuộc quý 4.

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
