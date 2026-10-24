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

### 4.1. Iteration

**Từ vựng trong mục:** **Iteration** — lần lặp.

Mỗi lần vòng lặp chạy một lượt gọi là một lần lặp. `range(2)` cho hai giá trị `0` và `1`, nên ví dụ in hai dòng tương ứng.

```python
for i in range(2): print(i)
```

**Kết quả khi chạy:**

```text
0
1
```

### 4.2. For loop

**Từ vựng trong mục:** **For loop** — vòng for.

Dùng `for` khi muốn lần lượt xử lý các giá trị trong một danh sách hoặc `range`. Ví dụ với `[1, 2]`, Python lần lượt in `1` rồi `2`.

```python
for x in [1,2]: print(x)
```

**Kết quả khi chạy:**

```text
1
2
```

### 4.3. While loop

**Từ vựng trong mục:** **While loop** — vòng while.

`while` tiếp tục chạy khi điều kiện còn đúng. Trong ví dụ `n` bắt đầu bằng 2, sau mỗi lượt giảm 1 nên vòng lặp kết thúc khi `n = 0`. Phải đảm bảo điều kiện có thể chuyển thành sai để tránh lặp mãi.

```python
n=2
while n>0:
    n-=1
```

**Kết quả khi chạy:** Không in ra màn hình. Biến `n` giảm từ `2` xuống `0`.

### 4.4. Break/continue

**Từ vựng trong mục:** **Break/continue** — dừng/bỏ qua.

`break` thoát hẳn vòng lặp, còn `continue` bỏ phần còn lại của lượt đang chạy rồi sang lượt sau. Ví dụ bỏ qua số `0` và in `1`, `2`.

```python
for x in [0,1,2]:
    if x==0: continue
    print(x)
```

**Kết quả khi chạy:**

```text
1
2
```

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
for value in orders: total+=value
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
    if x is None: continue
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

**Q1. What is an iteration? — Một lần lặp là gì?**

A. One pass through a loop — Một lượt chạy của vòng lặp

B. A complete Python file — Một file Python hoàn chỉnh

C. A string comparison — Phép so sánh chuỗi

D. A stored password — Mật khẩu đã lưu

**Q2. When is a for loop useful? — Khi nào nên dùng vòng for?**

A. When iterating over items — Khi duyệt lần lượt các phần tử

B. Only when connecting to the internet — Chỉ khi kết nối mạng

C. To replace every if statement — Để thay mọi câu if

D. To delete a list — Để xóa danh sách

**Q3. When does a while loop continue? — Khi nào vòng while tiếp tục chạy?**

A. While its condition is true — Khi điều kiện còn đúng

B. Only on the first iteration — Chỉ trong lượt đầu

C. After break executes — Sau khi break chạy

D. Only if a list is empty — Chỉ khi danh sách rỗng

**Q4. How do break and continue differ? — break khác continue thế nào?**

A. Both end the program — Cả hai kết thúc chương trình

B. break exits the loop; continue skips to the next iteration — break thoát vòng lặp; continue sang lượt kế tiếp

C. Both skip only one line — Cả hai chỉ bỏ qua một dòng

D. continue exits Python — continue thoát Python

**Q5. What does range(1, 4) produce? — range(1, 4) tạo những số nào?**

A. 1, 2, 3, 4 — 1, 2, 3, 4

B. 0, 1, 2, 3 — 0, 1, 2, 3

C. 1, 2, 3 — 1, 2, 3

D. 4 only — Chỉ số 4

**Q6. What does enumerate(items) provide? — enumerate(items) cung cấp gì?**

A. Only item names — Chỉ tên phần tử

B. Index and value — Vị trí và giá trị

C. Sorted values — Các giá trị đã sắp xếp

D. Only the last item — Chỉ phần tử cuối

**Q7. Which statement exits a loop early? — Lệnh nào dừng vòng lặp sớm?**

A. continue — continue

B. pass — pass

C. break — break

D. print — print

**Q8. Which statement skips the current item? — Lệnh nào bỏ qua phần còn lại của lượt hiện tại?**

A. continue — continue

B. break — break

C. return — return

D. input — input

**Q9. Why use a loop to sum three sales? — Vì sao dùng vòng lặp cộng doanh thu?**

A. To repeat accumulation for each sale — Để cộng dồn từng khoản bán

B. To erase sales data — Để xóa doanh thu

C. To round all amounts — Để làm tròn mọi khoản tiền

D. To hide the total — Để giấu tổng tiền

**Q10. Why skip None in temperature readings? — Vì sao bỏ qua None trong số đo nhiệt độ?**

A. None always means zero degrees — None luôn là 0 độ

B. None is a missing reading — None là lần đo thiếu dữ liệu

C. None is the highest temperature — None là nhiệt độ cao nhất

D. None must be converted to 100 — Phải đổi None thành 100

**Q11. Why use break after finding zero stock? — Vì sao dùng break sau khi tìm thấy hàng hết tồn?**

A. To stop once the first match is found — Để dừng khi gặp vị trí đầu tiên

B. To count all products — Để đếm mọi sản phẩm

C. To sort stock values — Để sắp xếp số lượng

D. To restart the search — Để tìm lại từ đầu

**Q12. Why limit the while connection attempts? — Vì sao giới hạn số lần thử kết nối?**

A. To ensure the loop terminates — Để vòng lặp có thể kết thúc

B. To make every attempt succeed — Để mọi lần thử đều thành công

C. To remove the need for a condition — Để bỏ điều kiện

D. To hide connection status — Để giấu trạng thái kết nối

**Q13. Why use nested loops for student schedules? — Vì sao dùng vòng lặp lồng nhau cho lịch học?**

A. To combine each student with each day — Để ghép từng học viên với từng ngày

B. To print only the last student — Để chỉ in người cuối

C. To delete the days — Để xóa các ngày

D. To stop after one pair — Để dừng sau một cặp

**Q14. What is the sales total for [120, 80, 200]? — Tổng [120, 80, 200] là bao nhiêu?**

A. 200 — 200

B. 300 — 300

C. 400 — 400

D. 480 — 480

**Q15. What remains after skipping None? — Còn gì sau khi bỏ qua None?**

A. [30, 35, 33] — [30, 35, 33]

B. [30, None, 35, 33] — [30, None, 35, 33]

C. [None] — [None]

D. [] — []

**Q16. What is the index of the first zero in [5, 3, 0, 4]? — Vị trí đầu tiên có số 0 là chỉ số nào?**

A. 0 — 0

B. 1 — 1

C. 2 — 2

D. 3 — 3

**Q17. How many attempts occur in the connection simulation? — Mô phỏng kết nối thử bao nhiêu lần?**

A. 1 — 1

B. 2 — 2

C. 3 — 3

D. Unlimited — Không giới hạn

**Q18. How many schedule lines are printed? — Lịch học in ra bao nhiêu dòng?**

A. 2 — 2

B. 3 — 3

C. 5 — 5

D. 6 — 6

**Q19. What can cause an infinite while loop? — Điều gì có thể khiến while lặp mãi?**

A. A condition that never becomes false — Điều kiện không bao giờ sai

B. A list with two items — Danh sách có hai phần tử

C. Using print — Dùng print

D. Using range(2) — Dùng range(2)

**Q20. What does continue do inside a for loop? — continue làm gì trong vòng for?**

A. Stops the Python process — Dừng chương trình Python

B. Restarts the entire program — Khởi động lại toàn bộ chương trình

C. Skips to the next iteration — Chuyển sang lượt lặp sau

D. Deletes the iterable — Xóa tập phần tử

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | A loop can execute several iterations. | Một vòng lặp có thể chạy nhiều lượt. |
| Q2 | **A** | for processes items from an iterable. | for dùng để duyệt các phần tử. |
| Q3 | **A** | while checks its condition before each iteration. | while kiểm tra điều kiện trước mỗi lượt. |
| Q4 | **B** | break stops the loop, while continue advances to the next iteration. | break dừng vòng lặp, continue chuyển sang lượt tiếp theo. |
| Q5 | **C** | The stop value 4 is excluded. | Giá trị dừng 4 không được lấy. |
| Q6 | **B** | enumerate yields an index alongside each item. | enumerate trả về vị trí và giá trị mỗi phần tử. |
| Q7 | **C** | break exits the innermost enclosing loop. | break thoát vòng lặp gần nhất chứa nó. |
| Q8 | **A** | continue moves to the next loop iteration. | continue chuyển sang lượt lặp tiếp theo. |
| Q9 | **A** | The same addition works for any number of sales. | Cùng một phép cộng dùng được cho nhiều khoản bán. |
| Q10 | **B** | Missing readings should not be treated as measured temperatures. | Không nên coi số liệu thiếu là nhiệt độ đo được. |
| Q11 | **A** | The task asks only for the first empty position. | Bài yêu cầu tìm vị trí hết hàng đầu tiên. |
| Q12 | **A** | A retry limit prevents indefinite attempts. | Giới hạn lượt thử tránh lặp mãi. |
| Q13 | **A** | The inner loop visits every day for each student. | Vòng trong duyệt từng ngày cho mỗi học viên. |
| Q14 | **C** | 120 + 80 + 200 = 400. | 120 + 80 + 200 = 400. |
| Q15 | **A** | continue skips the None item. | continue bỏ qua phần tử None. |
| Q16 | **C** | Python indexes start at zero. | Chỉ số Python bắt đầu từ 0. |
| Q17 | **B** | The simulated connection succeeds on attempt 2. | Mô phỏng kết nối thành công ở lần thứ hai. |
| Q18 | **D** | Two students times three days gives six lines. | Hai học viên nhân ba ngày tạo sáu dòng. |
| Q19 | **A** | A while loop needs a way to stop. | Vòng while cần có điều kiện dừng. |
| Q20 | **C** | continue does not exit the loop. | continue không thoát cả vòng lặp. |

## 8. Nối sang bài tiếp theo

`Điều kiện → Vòng lặp → Xử lý hàng loạt`.
