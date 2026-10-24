# PY-04 — Câu lệnh điều kiện if, elif, else


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Condition** — điều kiện; **Branch** — nhánh.

`Toán tử → Điều kiện → Phân loại theo quy tắc`

Ở bài trước, ta đã biết so sánh và nối các điều kiện. Bài này dùng `if`, `elif`, `else` để chương trình chọn việc cần làm dựa trên kết quả đúng hoặc sai.

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

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What does `if` do? — `if` dùng để làm gì?**

A. Runs its block when a condition is true — Chạy khối lệnh khi điều kiện đúng

B. When preceding branches have not matched — Khi các nhánh trước chưa đúng

C. When no earlier condition matched — Khi không điều kiện trước nào đúng

D. An if statement inside another block — Câu lệnh if nằm trong khối lệnh khác

**Q2. When is an `elif` condition checked? — Khi nào Python xét điều kiện `elif`?**

A. Runs its block when a condition is true — Chạy khối lệnh khi điều kiện đúng

B. When preceding branches have not matched — Khi các nhánh trước chưa đúng

C. When no earlier condition matched — Khi không điều kiện trước nào đúng

D. An if statement inside another block — Câu lệnh if nằm trong khối lệnh khác

**Q3. When does an `else` block run? — Khi nào khối `else` chạy?**

A. Runs its block when a condition is true — Chạy khối lệnh khi điều kiện đúng

B. When preceding branches have not matched — Khi các nhánh trước chưa đúng

C. When no earlier condition matched — Khi không điều kiện trước nào đúng

D. An if statement inside another block — Câu lệnh if nằm trong khối lệnh khác

**Q4. What is a nested `if`? — `if` lồng nhau là gì?**

A. Runs its block when a condition is true — Chạy khối lệnh khi điều kiện đúng

B. When preceding branches have not matched — Khi các nhánh trước chưa đúng

C. When no earlier condition matched — Khi không điều kiện trước nào đúng

D. An if statement inside another block — Câu lệnh if nằm trong khối lệnh khác

**Q5. Which keyword introduces another conditional test? — Từ khóa nào bổ sung một điều kiện tiếp theo?**

A. `elif` — `elif`

B. `else` — `else`

C. `if` — `if`

D. `in` — `in`

**Q6. Which keyword gives an unconditional fallback branch? — Từ khóa nào tạo nhánh còn lại không cần điều kiện?**

A. `elif` — `elif`

B. `else` — `else`

C. `if` — `if`

D. `in` — `in`

**Q7. Which keyword starts a conditional branch? — Từ khóa nào bắt đầu một nhánh điều kiện?**

A. `elif` — `elif`

B. `else` — `else`

C. `if` — `if`

D. `in` — `in`

**Q8. Which operator asks whether an item belongs to a list? — Toán tử nào kiểm tra phần tử có trong List?**

A. `elif` — `elif`

B. `else` — `else`

C. `if` — `if`

D. `in` — `in`

**Q9. What does `score >= 80` include? — Điều kiện `score >= 80` bao gồm gì?**

A. Scores equal to or above 80 — Điểm bằng hoặc lớn hơn 80

B. Assignment versus comparison — Phép gán và phép so sánh

C. Indentation — Thụt lề

D. Top to bottom — Từ trên xuống dưới

**Q10. What is the difference between `=` and `==`? — Dấu `=` khác `==` ra sao?**

A. Scores equal to or above 80 — Điểm bằng hoặc lớn hơn 80

B. Assignment versus comparison — Phép gán và phép so sánh

C. Indentation — Thụt lề

D. Top to bottom — Từ trên xuống dưới

**Q11. What defines the body of an `if` in Python? — Điều gì xác định thân khối `if` trong Python?**

A. Scores equal to or above 80 — Điểm bằng hoặc lớn hơn 80

B. Assignment versus comparison — Phép gán và phép so sánh

C. Indentation — Thụt lề

D. Top to bottom — Từ trên xuống dưới

**Q12. How are cases checked in an `if/elif` chain? — Các trường hợp được xét theo thứ tự nào trong chuỗi `if/elif`?**

A. Scores equal to or above 80 — Điểm bằng hoặc lớn hơn 80

B. Assignment versus comparison — Phép gán và phép so sánh

C. Indentation — Thụt lề

D. Top to bottom — Từ trên xuống dưới

**Q13. What does `True and False` evaluate to? — `True and False` bằng gì?**

A. `False` — `False`

B. `True` — `True`

C. `0` (the integer) — `0` (số nguyên)

D. `None` — `None`

**Q14. What does `True or False` evaluate to? — `True or False` bằng gì?**

A. `False` — `False`

B. `True` — `True`

C. `0` (the integer) — `0` (số nguyên)

D. `None` — `None`

**Q15. What does `not True` evaluate to? — `not True` bằng gì?**

A. `False` — `False`

B. `True` — `True`

C. `0` (the integer) — `0` (số nguyên)

D. `None` — `None`

**Q16. What does `5 % 2 == 0` evaluate to? — `5 % 2 == 0` có kết quả gì?**

A. `0` (the integer) — `0` (số nguyên)

B. `True` — `True`

C. `None` — `None`

D. `False` (the Boolean) — `False` (kiểu Boolean)

**Q17. How many branches run in one `if/elif/else` chain? — Có bao nhiêu nhánh chạy trong một chuỗi `if/elif/else`?**

A. At most one branch — Tối đa một nhánh

B. Its body is skipped — Thân nhánh if bị bỏ qua

C. Use `and` — Dùng `and`

D. Order mutually exclusive threshold branches carefully — Sắp xếp nhánh ngưỡng không chồng lấn cẩn thận

**Q18. What happens if an `if` condition is false and there is no `else`? — Nếu `if` sai và không có `else` thì sao?**

A. At most one branch — Tối đa một nhánh

B. Its body is skipped — Thân nhánh if bị bỏ qua

C. Use `and` — Dùng `and`

D. Order mutually exclusive threshold branches carefully — Sắp xếp nhánh ngưỡng không chồng lấn cẩn thận

**Q19. How can two conditions both be required for access? — Cách nào yêu cầu đồng thời hai điều kiện để cho phép truy cập?**

A. At most one branch — Tối đa một nhánh

B. Its body is skipped — Thân nhánh if bị bỏ qua

C. Use `and` — Dùng `and`

D. Order mutually exclusive threshold branches carefully — Sắp xếp nhánh ngưỡng không chồng lấn cẩn thận

**Q20. What helps prevent overlapping grade categories? — Điều gì giúp tránh các nhóm điểm chồng lấn?**

A. At most one branch — Tối đa một nhánh

B. Its body is skipped — Thân nhánh if bị bỏ qua

C. Use `and` — Dùng `and`

D. Order mutually exclusive threshold branches carefully — Sắp xếp nhánh ngưỡng không chồng lấn cẩn thận

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | if evaluates a condition to choose a branch. | if đánh giá điều kiện để chọn nhánh lệnh. |
| Q2 | **B** | An elif is tried only if earlier conditions in the chain failed. | elif chỉ được xét khi các điều kiện trước đó trong chuỗi chưa đúng. |
| Q3 | **C** | else is the fallback of the same if/elif chain. | else là nhánh dự phòng của chuỗi if/elif. |
| Q4 | **D** | Nested conditions let an inner test depend on an outer branch. | Điều kiện lồng cho phép kiểm tra bên trong phụ thuộc nhánh ngoài. |
| Q5 | **A** | elif adds another condition after an if. | elif bổ sung điều kiện sau if. |
| Q6 | **B** | else has no condition of its own in an if chain. | else không có điều kiện riêng trong chuỗi if. |
| Q7 | **C** | if introduces the initial condition. | if mở đầu phép kiểm tra điều kiện. |
| Q8 | **D** | The membership operator checks whether the item appears in a collection. | Toán tử in kiểm tra phần tử có thuộc tập dữ liệu không. |
| Q9 | **A** | The >= operator includes its threshold. | Dấu >= bao gồm cả mốc 80. |
| Q10 | **B** | One equals assigns, double equals checks equality. | Một dấu bằng để gán; hai dấu bằng kiểm tra bằng nhau. |
| Q11 | **C** | Statements at the same indentation level belong to the branch. | Các lệnh thụt cùng mức thuộc cùng khối. |
| Q12 | **D** | Python checks branches in written order and selects the first match. | Python xét theo thứ tự viết và chọn nhánh đầu tiên đúng. |
| Q13 | **A** | and requires all conditions to be true. | and yêu cầu tất cả điều kiện đều đúng. |
| Q14 | **B** | or only needs one true condition. | or chỉ cần một điều kiện đúng. |
| Q15 | **A** | The `not` operator negates its operand: `True` becomes the Boolean `False`. This differs from numeric zero (`0`) even though `0` is falsy when used as a condition. | Toán tử `not` phủ định toán hạng: `True` trở thành Boolean `False`. Kết quả khác số nguyên `0`, dù `0` cũng được xem là sai khi dùng làm điều kiện. |
| Q16 | **D** | `5 % 2` is `1`, and comparing `1 == 0` yields Boolean `False`; five is therefore odd. The result is not integer `0` or `None`, even though those can be falsy. | `5 % 2` bằng `1`, so sánh `1 == 0` cho Boolean `False`; vậy 5 là số lẻ. Kết quả không phải số nguyên `0` hay `None`, dù các giá trị đó có thể được xem là sai trong điều kiện. |
| Q17 | **A** | Only the first matching branch runs. | Chỉ nhánh đầu tiên thỏa điều kiện được chạy. |
| Q18 | **B** | A false if without an else simply does not run its body. | Nếu if sai và không có else thì thân if không chạy. |
| Q19 | **C** | Logical AND requires both conditions to hold. | AND yêu cầu cả hai điều kiện đều đúng. |
| Q20 | **D** | A descending threshold order makes the first matching category unambiguous. | Xét các ngưỡng từ cao xuống giúp chọn nhóm đầu tiên khớp rõ ràng. |

## 8. Nối sang bài tiếp theo

`Toán tử → Điều kiện → Phân loại theo quy tắc`.
