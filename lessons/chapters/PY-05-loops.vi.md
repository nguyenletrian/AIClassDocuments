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
# Mục đích: Tổng hợp doanh thu.
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
# Mục đích: Loại dòng trống.
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
# Mục đích: Tìm hàng hết tồn.
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
# Mục đích: Giới hạn kết nối.
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
# Mục đích: Lập bảng lịch học.
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
