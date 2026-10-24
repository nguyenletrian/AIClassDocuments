# PY-05 — Vòng lặp for, while, break và continue


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Iteration** — lần lặp; **For loop** — vòng for.

`Điều kiện → Vòng lặp → Xử lý hàng loạt`

Bài trước dùng `if` để chọn việc cần làm. Bài này dùng vòng lặp để xử lý nhiều dữ liệu mà không phải viết đi viết lại cùng một lệnh.

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
## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Tổng hợp doanh thu

**Từ vựng trong mục:** **Iteration** — lần lặp.

**Tình huống thực tế:** Một cửa hàng ghi ba khoản tiền bán hàng trong ngày là 120, 80 và 200 nghìn đồng.

**Yêu cầu:** Dùng vòng lặp tính tổng doanh thu trong ngày (đơn vị: nghìn đồng).

**Vì sao chọn cách giải này?** Vòng `for` lấy từng khoản tiền và cộng dồn vào `total`, giúp dùng lại cách tính khi số đơn hàng tăng.

**Quy trình giải:**

1. Lưu ba khoản tiền trong `orders`.
2. Đặt `total = 0`.
3. Dùng `for` cộng từng khoản vào `total` và in tổng.

```python
orders=[120,80,200]
total=0
for value in orders:
    total+=value
print(total)
```

**Kết quả khi chạy:**

```text
400
```

**Kết quả:** `400` nghìn đồng, tương đương 400.000 đồng.

### Tình huống 2 — Loại dòng trống

**Từ vựng trong mục:** **For loop** — vòng for.

**Tình huống thực tế:** Một trạm đo nhiệt độ nhận bốn lần đọc `[30, None, 35, 33]` °C. `None` nghĩa là lần đo không có số liệu, không phải 0 °C.

**Yêu cầu:** Dùng vòng lặp tạo danh sách chỉ chứa các nhiệt độ đo được.

**Vì sao chọn cách giải này?** Dùng `continue` để bỏ qua phần tử `None`, còn các giá trị số được đưa vào danh sách `valid`.

**Quy trình giải:**

1. Tạo danh sách dữ liệu và danh sách `valid` rỗng.
2. Duyệt từng giá trị bằng `for`.
3. Gặp `None` thì bỏ qua lượt này; còn lại thêm vào `valid`.
4. In danh sách kết quả.

```python
data=[30,None,35,33]
valid=[]
for x in data:
    if x is None:
        continue
    valid.append(x)
print(valid)
```

**Kết quả khi chạy:**

```text
[30, 35, 33]
```

**Kết quả:** `[30, 35, 33]` — chỉ còn ba lần đo có số liệu.

### Tình huống 3 — Tìm hàng hết tồn

**Từ vựng trong mục:** **While loop** — vòng while.

**Tình huống thực tế:** Kho có bốn vị trí hàng, số lượng theo thứ tự là `[5, 3, 0, 4]`. Vị trí đầu tiên được đánh số `0`. Nhân viên muốn tìm vị trí đầu tiên đã hết hàng.

**Yêu cầu:** In vị trí đầu tiên có số lượng bằng `0`, rồi dừng tìm kiếm.

**Vì sao chọn cách giải này?** `enumerate()` cung cấp cả vị trí và số lượng; `break` dừng vòng lặp ngay khi tìm thấy vị trí hết hàng đầu tiên.

**Quy trình giải:**

1. Duyệt danh sách bằng `enumerate(stocks)`.
2. Kiểm tra số lượng tại từng vị trí.
3. Khi gặp `0`, in vị trí và dùng `break` để dừng.

```python
stocks=[5,3,0,4]
for i,x in enumerate(stocks):
    if x==0:
        print("Hết hàng:",i)
        break
```

**Kết quả khi chạy:**

```text
Hết hàng: 2
```

**Kết quả:** `Hết hàng: 2` — vị trí thứ ba trong danh sách (chỉ số 2) đã hết hàng.

### Tình huống 4 — Giới hạn kết nối

**Từ vựng trong mục:** **Break/continue** — dừng/bỏ qua.

**Tình huống thực tế:** Ứng dụng thử kết nối máy chủ tối đa ba lần. Trong ví dụ mô phỏng, lần thử thứ nhất thất bại và lần thứ hai kết nối thành công.

**Yêu cầu:** Viết vòng lặp dừng khi kết nối thành công hoặc đã thử đủ ba lần, rồi in số lần thử và trạng thái kết nối.

**Vì sao chọn cách giải này?** `while` phù hợp vì chưa biết cần thử bao nhiêu lượt. Điều kiện `attempts < 3 and not connected` ngăn vòng lặp chạy mãi và dừng sớm khi kết nối được.

**Quy trình giải:**

1. Đặt số lần thử bằng 0, trạng thái kết nối là `False`.
2. Trong khi chưa đạt giới hạn và chưa kết nối, tăng số lần thử.
3. Mô phỏng kết nối thành công ở lần thứ hai.
4. In số lần đã thử và trạng thái.

```python
attempts,connected=0,False
while attempts<3 and not connected:
    attempts+=1
    connected=(attempts==2)
print(attempts,connected)
```

**Kết quả khi chạy:**

```text
2 True
```

**Kết quả:** `2 True` — chương trình thử hai lần rồi dừng vì đã kết nối. Đây là mô phỏng, không tạo kết nối mạng thật.

### Tình huống 5 — Lập bảng lịch học

**Từ vựng trong mục:** **Iteration** — lần lặp.

**Tình huống thực tế:** Trung tâm đào tạo có hai học viên `An`, `Lan`; mỗi người cần lịch học cho ngày 1, 2 và 3.

**Yêu cầu:** In từng cặp tên học viên và ngày học, tổng cộng sáu dòng.

**Vì sao chọn cách giải này?** Dùng hai vòng `for` lồng nhau: vòng ngoài chọn học viên, vòng trong chọn từng ngày cho học viên đó.

**Quy trình giải:**

1. Tạo danh sách hai học viên.
2. Duyệt từng học viên bằng vòng `for` ngoài.
3. Với mỗi học viên, lặp `range(1, 4)` để lấy ngày 1, 2, 3.
4. In tên và ngày.

```python
students=["An","Lan"]
for student in students:
    for day in range(1,4):
        print(student,day)
```

**Kết quả khi chạy:**

```text
An 1
An 2
An 3
Lan 1
Lan 2
Lan 3
```

**Kết quả:** Sáu dòng: `An 1`, `An 2`, `An 3`, `Lan 1`, `Lan 2`, `Lan 3`.

## 6. Nhầm lẫn dễ gặp

- `range(1, 4)` tạo `1, 2, 3`, không chứa `4`.
- `break` dừng toàn bộ vòng lặp hiện tại, còn `continue` chỉ bỏ qua phần còn lại của một lượt.
- Với `while`, phải thay đổi biến hoặc trạng thái để vòng lặp có thể kết thúc.
- `enumerate()` mặc định đếm vị trí từ 0; dùng `start=1` nếu muốn đếm từ 1.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What does a `for` loop normally iterate over? — Vòng `for` thường duyệt qua gì?**

A. An iterable of items — Một đối tượng có thể duyệt

B. While its condition remains true — Khi điều kiện của nó còn đúng

C. One execution of a loop body — Một lượt thực thi thân vòng lặp

D. A loop inside another loop — Một vòng lặp nằm trong vòng khác

**Q2. When does a `while` loop repeat? — Khi nào vòng `while` tiếp tục lặp?**

A. An iterable of items — Một đối tượng có thể duyệt

B. While its condition remains true — Khi điều kiện của nó còn đúng

C. One execution of a loop body — Một lượt thực thi thân vòng lặp

D. A loop inside another loop — Một vòng lặp nằm trong vòng khác

**Q3. What is an iteration? — Một lần lặp là gì?**

A. An iterable of items — Một đối tượng có thể duyệt

B. While its condition remains true — Khi điều kiện của nó còn đúng

C. One execution of a loop body — Một lượt thực thi thân vòng lặp

D. A loop inside another loop — Một vòng lặp nằm trong vòng khác

**Q4. What are nested loops? — Vòng lặp lồng nhau là gì?**

A. An iterable of items — Một đối tượng có thể duyệt

B. While its condition remains true — Khi điều kiện của nó còn đúng

C. One execution of a loop body — Một lượt thực thi thân vòng lặp

D. A loop inside another loop — Một vòng lặp nằm trong vòng khác

**Q5. What does `break` do inside a loop? — `break` làm gì trong vòng lặp?**

A. Exits the innermost enclosing loop — Thoát khỏi vòng lặp bao gần nhất

B. Skips the rest of the current iteration — Bỏ phần còn lại của lượt lặp hiện tại

C. Nothing; it is a placeholder statement — Không làm gì; đó là câu lệnh giữ chỗ

D. When the loop ends without `break` — Khi vòng lặp kết thúc mà không gặp `break`

**Q6. What does `continue` do? — `continue` có tác dụng gì?**

A. Exits the innermost enclosing loop — Thoát khỏi vòng lặp bao gần nhất

B. Skips the rest of the current iteration — Bỏ phần còn lại của lượt lặp hiện tại

C. Nothing; it is a placeholder statement — Không làm gì; đó là câu lệnh giữ chỗ

D. When the loop ends without `break` — Khi vòng lặp kết thúc mà không gặp `break`

**Q7. What does `pass` do? — `pass` làm gì?**

A. Exits the innermost enclosing loop — Thoát khỏi vòng lặp bao gần nhất

B. Skips the rest of the current iteration — Bỏ phần còn lại của lượt lặp hiện tại

C. Nothing; it is a placeholder statement — Không làm gì; đó là câu lệnh giữ chỗ

D. When the loop ends without `break` — Khi vòng lặp kết thúc mà không gặp `break`

**Q8. When does a loop's `else` execute? — `else` của vòng lặp chạy khi nào?**

A. Exits the innermost enclosing loop — Thoát khỏi vòng lặp bao gần nhất

B. Skips the rest of the current iteration — Bỏ phần còn lại của lượt lặp hiện tại

C. Nothing; it is a placeholder statement — Không làm gì; đó là câu lệnh giữ chỗ

D. When the loop finishes without `break` — Khi vòng lặp kết thúc mà không gặp `break`

**Q9. What does `range(1, 4)` represent? — `range(1, 4)` biểu diễn gì?**

A. Numbers 1, 2, 3 — Các số 1, 2, 3

B. Index-item pairs — Các cặp chỉ số và phần tử

C. Pairs corresponding items from two iterables — Ghép phần tử cùng vị trí của hai dãy

D. An iterator in reverse order — Bộ duyệt theo thứ tự đảo ngược

**Q10. What does `enumerate(items)` provide? — `enumerate(items)` cung cấp gì?**

A. Numbers 1, 2, 3 — Các số 1, 2, 3

B. Index-item pairs — Các cặp chỉ số và phần tử

C. Pairs corresponding items from two iterables — Ghép phần tử cùng vị trí của hai dãy

D. An iterator in reverse order — Bộ duyệt theo thứ tự đảo ngược

**Q11. What does `zip(a, b)` do? — `zip(a, b)` làm gì?**

A. Numbers 1, 2, 3 — Các số 1, 2, 3

B. Index-item pairs — Các cặp chỉ số và phần tử

C. Pairs corresponding items from two iterables — Ghép phần tử cùng vị trí của hai dãy

D. An iterator in reverse order — Bộ duyệt theo thứ tự đảo ngược

**Q12. What does `reversed(items)` provide for a sequence? — `reversed(items)` cung cấp gì cho một dãy?**

A. Numbers 1, 2, 3 — Các số 1, 2, 3

B. Index-item pairs — Các cặp chỉ số và phần tử

C. Pairs corresponding items from two iterables — Ghép phần tử cùng vị trí của hai dãy

D. An iterator in reverse order — Bộ duyệt theo thứ tự đảo ngược

**Q13. How many iterations does `range(3)` produce? — `range(3)` cho mấy lượt lặp?**

A. 3 — 3

B. 2, 4, 6 — 2, 4, 6

C. 0 — 0

D. `[(1, 'a')]` — `[(1, 'a')]`

**Q14. What does `range(2, 7, 2)` yield? — `range(2, 7, 2)` cho những số nào?**

A. 3 — 3

B. 2, 4, 6 — 2, 4, 6

C. 0 — 0

D. `[(1, 'a')]` — `[(1, 'a')]`

**Q15. What does `enumerate(['a','b'])` start indexing from? — `enumerate(['a','b'])` bắt đầu chỉ số từ đâu?**

A. 3 — 3

B. 2, 4, 6 — 2, 4, 6

C. 0 — 0

D. `[(1, 'a')]` — `[(1, 'a')]`

**Q16. What does `list(zip([1,2], ['a']))` contain? — `list(zip([1,2], ['a']))` gồm gì?**

A. 3 — 3

B. 2, 4, 6 — 2, 4, 6

C. 0 — 0

D. `[(1, 'a')]` — `[(1, 'a')]`

**Q17. What is a common cause of an infinite `while` loop? — Nguyên nhân thường gặp khiến `while` lặp vô hạn là gì?**

A. The stopping condition never becomes false — Điều kiện dừng không bao giờ thành sai

B. Use `continue` for the invalid item — Dùng `continue` ở phần tử không hợp lệ

C. Use `break` after finding the match — Dùng `break` sau khi tìm thấy

D. Use nested loops — Dùng vòng lặp lồng nhau

**Q18. How can a loop ignore invalid data and continue processing? — Làm sao bỏ qua dữ liệu lỗi nhưng vẫn xử lý phần tử sau?**

A. The stopping condition never becomes false — Điều kiện dừng không bao giờ thành sai

B. Use `continue` for the invalid item — Dùng `continue` ở phần tử không hợp lệ

C. Use `break` after finding the match — Dùng `break` sau khi tìm thấy

D. Use nested loops — Dùng vòng lặp lồng nhau

**Q19. How can a search stop immediately after a match? — Làm sao dừng tìm kiếm ngay khi đã thấy phần tử phù hợp?**

A. The stopping condition never becomes false — Điều kiện dừng không bao giờ thành sai

B. Use `continue` for the invalid item — Dùng `continue` ở phần tử không hợp lệ

C. Use `break` after finding the match — Dùng `break` sau khi tìm thấy

D. Use nested loops — Dùng vòng lặp lồng nhau

**Q20. How do you traverse every combination of two small collections? — Làm sao duyệt mọi kết hợp của hai nhóm nhỏ?**

A. The stopping condition never becomes false — Điều kiện dừng không bao giờ thành sai

B. Use `continue` for the invalid item — Dùng `continue` ở phần tử không hợp lệ

C. Use `break` after finding the match — Dùng `break` sau khi tìm thấy

D. Use nested loops — Dùng vòng lặp lồng nhau

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | for obtains successive items from an iterable. | for lần lượt lấy phần tử từ dữ liệu duyệt được. |
| Q2 | **B** | while rechecks the condition before each iteration. | while kiểm tra điều kiện trước mỗi lần lặp. |
| Q3 | **C** | Iteration means one pass through the loop body. | Một lần lặp là một lượt chạy thân vòng lặp. |
| Q4 | **D** | The inner loop runs as part of the outer loop's body. | Vòng trong chạy bên trong thân vòng ngoài. |
| Q5 | **A** | break leaves the current enclosing loop immediately. | break thoát ngay vòng lặp hiện tại. |
| Q6 | **B** | continue moves directly toward the next iteration. | continue chuyển tới lượt lặp kế tiếp. |
| Q7 | **C** | pass is syntactically valid but performs no operation. | pass hợp lệ về cú pháp nhưng không thực hiện thao tác. |
| Q8 | **D** | The loop's `else` runs only when the loop finishes normally, including a `for` that exhausts its iterable or a `while` whose condition turns false. A `break` skips that `else`; this differs from an `if` statement's `else`. | `else` của vòng lặp chỉ chạy khi vòng lặp kết thúc bình thường, như `for` duyệt hết phần tử hoặc điều kiện `while` thành sai. `break` khiến bỏ qua `else` đó; quy tắc này khác `else` của câu lệnh `if`. |
| Q9 | **A** | The stop argument is exclusive. | Giá trị stop không được lấy. |
| Q10 | **B** | enumerate yields an index alongside each item. | enumerate đưa ra chỉ số kèm từng phần tử. |
| Q11 | **C** | zip advances both iterables together, stopping at the shorter one by default. | zip duyệt hai dãy đồng thời, mặc định dừng theo dãy ngắn hơn. |
| Q12 | **D** | reversed traverses an eligible sequence backwards. | reversed duyệt dãy theo chiều ngược. |
| Q13 | **A** | The generated values are 0, 1 and 2. | Giá trị nhận được là 0, 1 và 2. |
| Q14 | **B** | The step is two and the stop seven is excluded. | Bước nhảy bằng hai và không lấy mốc 7. |
| Q15 | **C** | enumerate uses zero as its default starting index. | enumerate mặc định đánh chỉ số từ 0. |
| Q16 | **D** | zip stops when the shorter input runs out. | zip dừng khi dãy ngắn hơn hết phần tử. |
| Q17 | **A** | Without progress toward stopping, while may repeat forever. | Không có thay đổi hướng tới điều kiện dừng có thể khiến while lặp mãi. |
| Q18 | **B** | continue skips only the current iteration. | continue chỉ bỏ lượt hiện tại. |
| Q19 | **C** | break prevents unnecessary subsequent iterations. | break tránh duyệt tiếp các lượt không cần thiết. |
| Q20 | **D** | For each outer item, the inner loop processes the second collection. | Với mỗi phần tử vòng ngoài, vòng trong duyệt nhóm thứ hai. |

## 8. Nối sang bài tiếp theo

`Điều kiện → Vòng lặp → Xử lý hàng loạt`.
