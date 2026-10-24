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

A. Runs its body once regardless of the condition — Luôn chạy thân khối một lần bất kể điều kiện

B. Runs its indented body when the condition is true — Chạy thân khối thụt lề khi điều kiện đúng

C. Always runs every conditional branch — Luôn chạy mọi nhánh điều kiện

D. Runs its body only when the condition is false — Chỉ chạy thân khối khi điều kiện sai

**Q2. When is an `elif` condition checked? — Khi nào Python xét điều kiện `elif`?**

A. Even after a preceding branch has matched — Kể cả khi nhánh trước đã đúng

B. Before the preceding `if` is checked — Trước khi kiểm tra `if` đứng trước

C. After `else` has executed — Sau khi `else` chạy

D. Only if earlier branches in the same chain did not match — Chỉ khi các nhánh trước trong cùng chuỗi không khớp

**Q3. When does an `else` block run? — Khi nào khối `else` chạy?**

A. After any successful `elif` branch — Sau bất kỳ nhánh `elif` nào đúng

B. When no earlier condition in its chain was true — Khi mọi điều kiện trước trong cùng chuỗi đều sai

C. Only when a program raises an error — Chỉ khi chương trình phát sinh lỗi

D. Every time the initial `if` is true — Mỗi khi `if` đầu tiên đúng

**Q4. What is a nested `if`? — `if` lồng nhau là gì?**

A. Two `if` statements at the same indentation level — Hai lệnh `if` có cùng mức thụt lề

B. An `if` statement inside another conditional block — Một lệnh `if` bên trong khối điều kiện khác

C. A condition joined by `and` — Điều kiện kết hợp bởi `and`

D. An `else` branch following `if` — Nhánh `else` theo sau `if`

**Q5. Which keyword introduces another conditional test? — Từ khóa nào bổ sung một điều kiện tiếp theo?**

A. `elif` — `elif`

B. `in` — `in`

C. `if` — `if`

D. `else` — `else`

**Q6. Which keyword gives an unconditional fallback branch? — Từ khóa nào tạo nhánh còn lại không cần điều kiện?**

A. `if` — `if`

B. `else` — `else`

C. `in` — `in`

D. `elif` — `elif`

**Q7. Which keyword starts a conditional branch? — Từ khóa nào bắt đầu một nhánh điều kiện?**

A. `elif` — `elif`

B. `in` — `in`

C. `else` — `else`

D. `if` — `if`

**Q8. Which operator asks whether an item belongs to a list? — Toán tử nào kiểm tra phần tử có trong List?**

A. `if` — `if`

B. `elif` — `elif`

C. `in` — `in`

D. `else` — `else`

**Q9. What does `score >= 80` include? — Điều kiện `score >= 80` bao gồm gì?**

A. Only scores strictly above 80 — Chỉ điểm lớn hơn 80

B. Scores below 80 — Điểm thấp hơn 80

C. Only the score exactly equal to 80 — Chỉ điểm đúng bằng 80

D. Every score of at least 80, including 80 — Mọi điểm từ 80 trở lên, kể cả 80

**Q10. What is the difference between `=` and `==`? — Dấu `=` khác `==` ra sao?**

A. Both operators assign variables — Cả hai toán tử đều dùng gán biến

B. Both operators compare equality — Cả hai toán tử so sánh bằng nhau

C. `=` assigns; `==` compares equality — `=` để gán; `==` so sánh bằng nhau

D. `=` compares; `==` assigns — `=` để so sánh; `==` để gán

**Q11. What defines the body of an `if` in Python? — Điều gì xác định thân khối `if` trong Python?**

A. The order of imported libraries — Thứ tự thư viện được nhập

B. The variable name in the condition — Tên biến trong điều kiện

C. The indentation of following statements — Mức thụt lề của các câu lệnh theo sau

D. The number of printed statements — Số câu lệnh in ra

**Q12. How are cases checked in an `if/elif` chain? — Các trường hợp được xét theo thứ tự nào trong chuỗi `if/elif`?**

A. By whichever condition is cheapest — Theo điều kiện tốn ít tính toán nhất

B. All branches run concurrently — Mọi nhánh chạy đồng thời

C. Top to bottom, stopping after the first match — Từ trên xuống, dừng tại nhánh đúng đầu tiên

D. From the last `elif` upward — Từ `elif` cuối lên trên

**Q13. What does `True and False` evaluate to? — `True and False` bằng gì?**

A. `False` (Boolean) — `False` (Boolean)

B. `0` (integer) — `0` (số nguyên)

C. `True` (Boolean) — `True` (Boolean)

D. `None` — `None`

**Q14. What does `True or False` evaluate to? — `True or False` bằng gì?**

A. `False` (Boolean) — `False` (Boolean)

B. `None` — `None`

C. `1` (integer) — `1` (số nguyên)

D. `True` (Boolean) — `True` (Boolean)

**Q15. What does `not True` evaluate to? — `not True` bằng gì?**

A. `0` (integer) — `0` (số nguyên)

B. `True` (Boolean) — `True` (Boolean)

C. `None` — `None`

D. `False` (Boolean) — `False` (Boolean)

**Q16. What does `5 % 2 == 0` evaluate to? — `5 % 2 == 0` có kết quả gì?**

A. `None` — `None`

B. `0` (integer) — `0` (số nguyên)

C. `True` (Boolean) — `True` (Boolean)

D. `False` (Boolean) — `False` (Boolean)

**Q17. How many branches run in one `if/elif/else` chain? — Có bao nhiêu nhánh chạy trong một chuỗi `if/elif/else`?**

A. Every `elif` plus `else` — Mọi nhánh `elif` và `else`

B. At most one branch, possibly none without `else` — Tối đa một nhánh, có thể không nhánh nào nếu thiếu `else`

C. Exactly two branches always — Luôn đúng hai nhánh

D. Every branch whose condition is true — Mọi nhánh có điều kiện đúng

**Q18. What happens if an `if` condition is false and there is no `else`? — Nếu `if` sai và không có `else` thì sao?**

A. The body is skipped and execution continues — Bỏ qua thân nhánh và tiếp tục chương trình

B. A `SyntaxError` is raised — Phát sinh `SyntaxError`

C. Python inserts and runs an implicit `else` — Python tự chèn và chạy `else`

D. The body runs once regardless — Thân nhánh vẫn chạy một lần

**Q19. How can two conditions both be required for access? — Cách nào yêu cầu đồng thời hai điều kiện để cho phép truy cập?**

A. Use `and` — Dùng `and`

B. Use `or` — Dùng `or`

C. Use `not` — Dùng `not`

D. Use `==` alone — Chỉ dùng `==`

**Q20. In one `if/elif` grade chain, which order correctly tests `score >= 90`, `score >= 80`, and `score >= 70` to select the highest applicable grade? — Trong một chuỗi `if/elif` phân loại điểm, cần xét `score >= 90`, `score >= 80`, `score >= 70` theo thứ tự nào để chọn mức cao nhất phù hợp?**

A. Test `>= 70` before `>= 90` — Xét `>= 70` trước `>= 90`

B. Use any order because all matches run — Thứ tự tùy ý vì mọi nhánh đúng đều chạy

C. Test `>= 90`, then `>= 80`, then `>= 70` — Xét `>= 90`, rồi `>= 80`, rồi `>= 70`

D. Write independent `if` statements to select a single grade — Viết các `if` độc lập để chọn duy nhất một nhóm

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | An `if` evaluates its condition, then executes its indented body only if that condition is truthy. For example, with `x = 5`, `if x > 3:` enters its body; an `else` is not required. | `if` đánh giá điều kiện rồi chỉ chạy thân khối được thụt lề nếu điều kiện có giá trị đúng. Ví dụ với `x = 5`, `if x > 3:` sẽ chạy thân khối; không bắt buộc phải có `else`. |
| Q2 | **D** | Python checks an `elif` only after the preceding `if` or `elif` conditions in the same chain did not match. Once a preceding branch matches, later `elif` tests are skipped, preventing multiple branches from running. | Python chỉ xét `elif` khi những điều kiện `if` hoặc `elif` đứng trước trong cùng chuỗi đều không khớp. Khi một nhánh trước đã đúng, các `elif` sau không được kiểm tra, nên không có nhiều nhánh cùng chạy. |
| Q3 | **B** | `else` is the fallback branch without its own condition. It executes only when no earlier `if` or `elif` condition in that chain was truthy; it does not run after a successful branch. | `else` là nhánh dự phòng không có điều kiện riêng. Nó chỉ chạy khi mọi điều kiện `if` hoặc `elif` đứng trước trong cùng chuỗi đều sai, không chạy sau nhánh đã khớp. |
| Q4 | **B** | A nested `if` is a conditional inside another conditional's body, so the inner test occurs only if execution reaches that block. This differs from two separate top-level `if` statements, which can both run. | `if` lồng nhau là câu lệnh điều kiện nằm trong thân một câu lệnh điều kiện khác nên điều kiện trong chỉ được xét khi chương trình đi vào khối đó. Nó khác hai câu `if` độc lập, vốn có thể cùng chạy. |
| Q5 | **A** | `elif` means an additional conditional branch attached to an earlier `if`. Unlike `else`, it has its own condition, such as `elif score >= 80:`. | `elif` mở thêm một nhánh có điều kiện nối với `if` trước đó. Khác `else`, nhánh này có điều kiện riêng, ví dụ `elif score >= 80:`. |
| Q6 | **B** | `else` names the unconditional fallback in an `if/elif/else` chain; Python reaches it only when earlier conditions are false. You cannot write `else condition:` because `else` does not take a condition. | `else` là nhánh dự phòng không ghi điều kiện trong chuỗi `if/elif/else`; Python chỉ vào đó khi các điều kiện trước sai. Không thể viết `else condition:` vì `else` không nhận điều kiện. |
| Q7 | **D** | The initial conditional branch starts with `if`, followed by an expression and a colon. `elif` can follow that `if`, but cannot start a new chain on its own. | Nhánh điều kiện đầu tiên dùng `if`, tiếp theo là biểu thức và dấu hai chấm. `elif` chỉ có thể nối sau một `if` trước đó, không tự mở đầu chuỗi mới. |
| Q8 | **C** | `in` checks membership: `3 in [1, 3]` evaluates to `True`. By contrast, `if`, `elif`, and `else` are control-flow keywords, not operators for membership. | `in` kiểm tra phần tử thuộc tập hợp: `3 in [1, 3]` là `True`. Trong khi đó `if`, `elif`, `else` là từ khóa điều khiển luồng, không phải toán tử kiểm tra phần tử. |
| Q9 | **D** | `>=` includes the threshold itself, so `score >= 80` is true for 80, 81, and higher values. The strict comparison `score > 80` would incorrectly exclude exactly 80. | `>=` bao gồm chính giá trị ngưỡng, nên `score >= 80` đúng với 80, 81 và các giá trị lớn hơn. Dùng so sánh nghiêm ngặt `score > 80` sẽ loại đúng điểm 80. |
| Q10 | **C** | `=` assigns a value, as in `score = 80`, whereas `==` compares values and yields a Boolean, as in `score == 80`. They are not interchangeable within an `if` condition. | `=` gán giá trị như `score = 80`, còn `==` so sánh và trả Boolean như `score == 80`. Không thể thay hai toán tử cho nhau trong điều kiện `if`. |
| Q11 | **C** | Indentation identifies which statements belong to the `if` body, conventionally four spaces per level. The colon finishes the header, but only the following correctly indented lines are inside the branch. | Thụt lề xác định câu lệnh nào thuộc thân `if`, thông thường bốn dấu cách cho mỗi cấp. Dấu hai chấm kết thúc dòng điều kiện, còn các dòng thụt lề đúng sau đó mới nằm trong nhánh. |
| Q12 | **C** | Python tests branches from top to bottom and executes the first one whose condition is true. If scores of 95 also satisfy `>= 80`, placing `>= 80` before `>= 90` will choose the lower grade prematurely. | Python xét nhánh từ trên xuống và chạy nhánh đầu tiên có điều kiện đúng. Nếu điểm 95 cũng thỏa `>= 80`, đặt `>= 80` trước `>= 90` sẽ chọn mức điểm thấp hơn quá sớm. |
| Q13 | **A** | `and` with Boolean operands is `True` only when both operands are `True`. Since the second operand is `False`, `True and False` yields Boolean `False`, not integer `0`. | `and` với hai toán hạng Boolean chỉ trả `True` khi cả hai đều `True`. Vì vế thứ hai là `False`, `True and False` cho Boolean `False`, không phải số nguyên `0`. |
| Q14 | **D** | `or` with Boolean operands requires only one true side; the left side is `True`, so `True or False` is Boolean `True`. This is not the same type as the integer `1`. | `or` với toán hạng Boolean chỉ cần một vế đúng; vế trái là `True` nên `True or False` cho Boolean `True`. Kết quả không cùng kiểu với số nguyên `1`. |
| Q15 | **D** | `not` reverses the truth value of its operand, so `not True` evaluates to Boolean `False`. An integer `0` is falsy in a condition but is not the value returned here. | `not` đảo giá trị logic của toán hạng, nên `not True` cho Boolean `False`. Số nguyên `0` cũng được xem là sai trong điều kiện nhưng không phải giá trị trả về ở đây. |
| Q16 | **D** | The remainder `5 % 2` is `1`; comparing `1 == 0` is therefore false. The whole expression returns Boolean `False`, which indicates that five is not even. | Phần dư `5 % 2` là `1`; vì vậy so sánh `1 == 0` là sai. Toàn bộ biểu thức trả về Boolean `False`, nghĩa là 5 không phải số chẵn. |
| Q17 | **B** | In one `if/elif/else` chain, execution selects at most one branch: the first matching one, or `else` when none match. If no `else` is present and all conditions fail, zero branches run. | Trong một chuỗi `if/elif/else`, chương trình chạy tối đa một nhánh: nhánh đúng đầu tiên hoặc `else` khi không nhánh nào đúng. Nếu không có `else` và mọi điều kiện đều sai thì không nhánh nào chạy. |
| Q18 | **A** | When the `if` condition is false, its body is simply skipped. If no `else` follows, execution continues after the conditional; this is valid Python, not a syntax error. | Khi điều kiện `if` sai, thân nhánh đó được bỏ qua. Nếu không có `else`, chương trình tiếp tục sau khối điều kiện; đây là Python hợp lệ, không phải lỗi cú pháp. |
| Q19 | **A** | Logical `and` requires both conditions to hold, such as `has_ticket and age >= 18`. Using `or` would admit anyone satisfying only one of the conditions, which does not enforce both requirements. | Phép `and` bắt buộc đồng thời hai điều kiện như `has_ticket and age >= 18`. Dùng `or` sẽ chấp nhận người chỉ thỏa một điều kiện, nên không đảm bảo đủ cả hai yêu cầu. |
| Q20 | **C** | A chain selects its first matching branch; test the most restrictive grade threshold first, such as `>= 90` before `>= 80` and `>= 70`. Starting with `>= 70` would classify a score of 95 too early. | Chuỗi điều kiện chọn nhánh đúng đầu tiên; hãy xét ngưỡng điểm cao nhất trước, ví dụ `>= 90`, rồi `>= 80`, `>= 70`. Nếu bắt đầu từ `>= 70`, điểm 95 sẽ bị xếp nhóm quá sớm. |

## 8. Nối sang bài tiếp theo

`Toán tử → Điều kiện → Phân loại theo quy tắc`.
