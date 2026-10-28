# Lab Session 4 — Điều kiện và vòng lặp

**Một file Word = một tài liệu:** `LAB Session 4.docx`. Bản đề tiếng Anh được lấy từ `labs/pythoclass/LAB-04-conditions-loops/LAB.md`. Các đoạn mã được trích từ `docs/labs/LAB-04-conditions-loops/SOLUTION_ANNOTATED.py`, là phiên bản chú thích dựa trên `labs/pythoclass/LAB-04-conditions-loops/SOLUTION.py` và đối chiếu code cũ trong `DEMO.py`, kiến thức PY-03, PY-04, PY-05. **Không viết lại một thuật toán mới để thay code đã có.**

**Hàm dùng chung trong file gốc:** `from math import isqrt`, `WORDS`, `leap_year()`, `task05_two_digit()`. Các đoạn code ở mỗi bài là trích đoạn của *cùng một chương trình*; cần giữ các hàm bổ trợ/import này khi chạy tổng thể.

## Bài 1 — Sorting numbers

### English — Original Word requirement

Write a program that inputs three real numbers and prints them in ascending order.

**Requirement:** Use only `if...else` statements.

**Example:** Input: `8.5 3.2 6.7` → Output: `3.2 6.7 8.5`

### Tiếng Việt — Dịch đề

Nhập ba số thực, dùng **chỉ lệnh `if...else`** để xếp chúng theo thứ tự tăng dần. Ví dụ `8.5 3.2 6.7` → `3.2 6.7 8.5`.

### Bài giải — Code đã được làm và chú thích

**Nguồn hàm:** `SOLUTION.py` / bản chú thích `SOLUTION_ANNOTATED.py`, hàm `task01_sort_three()`. Code demo cũ chỉ là phần thực hành ban đầu và có chỗ chưa hoàn chỉnh; không coi demo là lời giải đầy đủ.

```python
def task01_sort_three(a, b, c):
    # Branch when this validated condition is true.
    if a > b: a, b = b, a
    # Branch when this validated condition is true.
    if b > c: b, c = c, b
    # Branch when this validated condition is true.
    if a > b: a, b = b, a
    # Return the result for later reuse or testing instead of only printing it.
    return a, b, c

# Function: Check the 1..12 domain, then choose the correct quarter using if/elif/else.
```

### Giải thích quy trình giải và công thức

So sánh cặp `(a,b)`, `(b,c)`, rồi `(a,b)` và đổi chỗ khi cặp không đúng thứ tự. Đây là cách dùng điều kiện, không gọi `sort()`.

**Quy tắc / công thức:** Nếu `a > b` thì hoán đổi `a,b = b,a`; tương tự cho các cặp.

## Bài 2 — Quarter of the year

### English — Original Word requirement

Write a program that inputs a month (1–12) and determines which quarter of the year it belongs to.

**Example:** Input: `5` → Output: `Quarter 2`

**Requirement:** Use `if...elif...else` or `match...case`.

### Tiếng Việt — Dịch đề

Nhập tháng từ 1 đến 12, xác định quý tương ứng trong năm bằng `if...elif...else` hoặc `match...case`. Ví dụ tháng 5 thuộc Quý 2.

### Bài giải — Code đã được làm và chú thích

**Nguồn hàm:** `SOLUTION.py` / bản chú thích `SOLUTION_ANNOTATED.py`, hàm `task02_quarter()`. Code demo cũ chỉ là phần thực hành ban đầu và có chỗ chưa hoàn chỉnh; không coi demo là lời giải đầy đủ.

```python
def task02_quarter(month):
    # Reject out-of-range or missing inputs early instead of silently accepting them.
    if not 1 <= month <= 12: raise ValueError("Month must be 1..12")
    # Branch when this validated condition is true.
    if month <= 3: return 1
    # Handle an alternative choice only when earlier tests did not match.
    elif month <= 6: return 2
    # Handle an alternative choice only when earlier tests did not match.
    elif month <= 9: return 3
    # Run the fallback branch when no earlier condition applies.
    else: return 4

# Function: A leap year is divisible by 400, or by 4 and not by 100.
```

### Giải thích quy trình giải và công thức

Kiểm tra tháng hợp lệ, sau đó xem tháng nằm ở 1–3, 4–6, 7–9 hay 10–12 để trả quý.

**Quy tắc / công thức:** Quý có thể xác định bằng `(month-1)//3 + 1` nhưng code nguồn thực hành `if/elif` đúng yêu cầu.

## Bài 3 — Days in a month

### English — Original Word requirement

Write a program that inputs a month. Determine the number of days in that month.

**Example:** Input: `3` → Output: `31 days`

### Tiếng Việt — Dịch đề

Nhập một tháng và cho biết tháng đó có bao nhiêu ngày. Ví dụ tháng 3 có 31 ngày. Cần xét riêng tháng 2 và năm nhuận nếu cung cấp năm.

### Bài giải — Code đã được làm và chú thích

**Nguồn hàm:** `SOLUTION.py` / bản chú thích `SOLUTION_ANNOTATED.py`, hàm `task03_month_days()`. Code demo cũ chỉ là phần thực hành ban đầu và có chỗ chưa hoàn chỉnh; không coi demo là lời giải đầy đủ.

```python
def task03_month_days(month, year=2026):
    # Prepare this intermediate value for the next calculation or validation.
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    # Reject out-of-range or missing inputs early instead of silently accepting them.
    if not 1 <= month <= 12: raise ValueError("Month must be 1..12")
    # Return the result for later reuse or testing instead of only printing it.
    return 29 if month == 2 and leap_year(year) else days[month-1]

# Function: Reject non-positive years and reuse the leap-year rule.
```

### Giải thích quy trình giải và công thức

Dùng danh sách ngày của 12 tháng. Nếu tháng 2 của năm nhuận thì lấy 29, không lấy 28. Mã này tham chiếu thêm `leap_year()` ở mã nguồn đã học.

**Quy tắc / công thức:** Năm nhuận: `year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)`.

## Bài 4 — Leap year

### English — Original Word requirement

Write a program that inputs a year and determines whether it is a leap year.

**Leap year rules:**
- A year divisible by 400 is a leap year.
- A year divisible by 4 but not divisible by 100 is a leap year.
- Otherwise, it is not a leap year.

**Examples:** `2024` → `Leap year`; `2023` → `Not a leap year`.

### Tiếng Việt — Dịch đề

Nhập năm và xác định năm nhuận: chia hết cho 400, hoặc chia hết cho 4 nhưng không chia hết cho 100. Ví dụ 2024 có nhuận, 2023 không nhuận.

### Bài giải — Code đã được làm và chú thích

**Nguồn hàm:** `SOLUTION.py` / bản chú thích `SOLUTION_ANNOTATED.py`, hàm `task04_is_leap()`. Code demo cũ chỉ là phần thực hành ban đầu và có chỗ chưa hoàn chỉnh; không coi demo là lời giải đầy đủ.

```python
def task04_is_leap(year):
    # Reject out-of-range or missing inputs early instead of silently accepting them.
    if year < 1: raise ValueError("Year must be positive")
    # Return the result for later reuse or testing instead of only printing it.
    return leap_year(year)

# Prepare this intermediate value for the next calculation or validation.
WORDS = ["khong","mot","hai","ba","bon","nam","sau","bay","tam","chin"]

# Function: Split tens and units to reproduce the source exercise's Vietnamese number words.
```

### Giải thích quy trình giải và công thức

Dùng toán tử `%` kiểm tra các trường hợp chia hết; điều kiện năm dương loại đầu vào không hợp lệ.

**Quy tắc / công thức:** Chia hết cho 400 **hoặc** chia hết cho 4 và **không** chia hết cho 100.

## Bài 5 — Number name (two digits)

### English — Original Word requirement

Write a program that inputs a two-digit integer and prints its number name.

**Examples:** `12` → `muoi hai`; `25` → `hai muoi lam`.

### Tiếng Việt — Dịch đề

Nhập số nguyên có **hai chữ số** và in cách đọc bằng chữ tiếng Việt. Ví dụ 12 → `muoi hai`, 25 → `hai muoi lam` (không đổi các mẫu nguồn).

### Bài giải — Code đã được làm và chú thích

**Nguồn hàm:** `SOLUTION.py` / bản chú thích `SOLUTION_ANNOTATED.py`, hàm `task05_two_digit()`. Code demo cũ chỉ là phần thực hành ban đầu và có chỗ chưa hoàn chỉnh; không coi demo là lời giải đầy đủ.

```python
def task05_two_digit(n):
    # Reject out-of-range or missing inputs early instead of silently accepting them.
    if not 10 <= n <= 99: raise ValueError("Expected two-digit integer")
    tens, unit = divmod(n,10)
    # Branch when this validated condition is true.
    if tens == 1:
        # Prepare this intermediate value for the next calculation or validation.
        head = "muoi"
    # Run the fallback branch when no earlier condition applies.
    else:
        # Prepare this intermediate value for the next calculation or validation.
        head = WORDS[tens] + " muoi"
    # Branch when this validated condition is true.
    if unit == 0: return head
    # Branch when this validated condition is true.
    if unit == 5: return head + " lam"
    # Branch when this validated condition is true.
    if unit == 1 and tens > 1: return head + " mot"
    # Return the result for later reuse or testing instead of only printing it.
    return head + " " + WORDS[unit]

# Function: Split hundreds and the remaining two digits, handling zero tens.
```

### Giải thích quy trình giải và công thức

Tách hàng chục và đơn vị, chọn từ đọc thích hợp trong danh sách từ đã có (`WORDS`). Một số trường hợp đặc biệt như số 25 đọc `lam`.

**Quy tắc / công thức:** `tens = n // 10`, `units = n % 10`.

## Bài 6 — Number name (three digits)

### English — Original Word requirement

Write a program that inputs a three-digit integer and prints its number name.

**Example:** `123` → `mot tram hai muoi ba`.

### Tiếng Việt — Dịch đề

Nhập số nguyên có **ba chữ số** và in cách đọc bằng chữ tiếng Việt. Ví dụ 123 → `mot tram hai muoi ba`.

### Bài giải — Code đã được làm và chú thích

**Nguồn hàm:** `SOLUTION.py` / bản chú thích `SOLUTION_ANNOTATED.py`, hàm `task06_three_digit()`. Code demo cũ chỉ là phần thực hành ban đầu và có chỗ chưa hoàn chỉnh; không coi demo là lời giải đầy đủ.

```python
def task06_three_digit(n):
    # Reject out-of-range or missing inputs early instead of silently accepting them.
    if not 100 <= n <= 999: raise ValueError("Expected three-digit integer")
    hundred, rest = divmod(n,100)
    # Prepare this intermediate value for the next calculation or validation.
    head = WORDS[hundred] + " tram"
    # Branch when this validated condition is true.
    if rest == 0: return head
    # Branch when this validated condition is true.
    if rest < 10:
        # Return the result for later reuse or testing instead of only printing it.
        return head + " linh " + ("nam" if rest == 5 else WORDS[rest])
    # Return the result for later reuse or testing instead of only printing it.
    return head + " " + task05_two_digit(rest)

# Function: Calculate tiered billing progressively rather than multiplying the full usage by one rate.
```

### Giải thích quy trình giải và công thức

Tách hàng trăm và phần dư. Nếu phần dư nhỏ hơn 10 dùng cách đọc `linh`, còn lại gọi lại hàm đọc hai chữ số; cần dùng `WORDS` và `task05_two_digit` đã được định nghĩa chung.

**Quy tắc / công thức:** `hundreds = n // 100`, `rest = n % 100`.

## Bài 7 — Electricity bill

### English — Original Word requirement

Write a program that inputs the amount of electricity consumed in kWh and calculates the electricity bill based on the following rates:

| Electricity usage | Price |
|---|---|
| 0–50 kWh | 1,800 VND/kWh |
| 51–100 kWh | 2,000 VND/kWh |
| 101–200 kWh | 2,500 VND/kWh |
| Above 200 kWh | 3,000 VND/kWh |

**Example in original Word:** Input `120` → Output `282000 VND`.

> **Ghi chú hiệu đính:** Nếu giá điện được tính **lũy tiến từng bậc**, 120 kWh cho kết quả **240,000 VND**. Ví dụ `282000` trong Word không khớp bảng giá; `SOLUTION.py` tính lũy tiến và có kiểm tra kết quả. Số liệu ví dụ gốc được giữ ở đây để đối chiếu.

### Tiếng Việt — Dịch đề

Nhập số điện tiêu thụ (kWh), tính tiền điện theo bảng giá: 0–50 kWh: 1.800 VND/kWh; 51–100: 2.000; 101–200: 2.500; trên 200: 3.000. **Ví dụ Word ghi 120 kWh → 282.000 VND nhưng không khớp bảng giá; cách tính lũy tiến đúng theo bảng là 240.000 VND.** Giữ cả hai số để so sánh.

### Bài giải — Code đã được làm và chú thích

**Nguồn hàm:** `SOLUTION.py` / bản chú thích `SOLUTION_ANNOTATED.py`, hàm `task07_electricity_bill()`. Code demo cũ chỉ là phần thực hành ban đầu và có chỗ chưa hoàn chỉnh; không coi demo là lời giải đầy đủ.

```python
def task07_electricity_bill(kwh):
    """Progressive tiers, in VND; note Word's 282000 example is inconsistent."""
    # Reject out-of-range or missing inputs early instead of silently accepting them.
    if kwh < 0: raise ValueError("Usage cannot be negative")
    # Prepare this intermediate value for the next calculation or validation.
    remaining = float(kwh)
    # Prepare this intermediate value for the next calculation or validation.
    total = 0.0
    # Process each element of the input collection in order.
    for width, rate in ((50,1800),(50,2000),(100,2500)):
        # Prepare this intermediate value for the next calculation or validation.
        amount = min(remaining,width)
        total += amount * rate
        remaining -= amount
        # Branch when this validated condition is true.
        if remaining <= 0: return total
    # Return the result for later reuse or testing instead of only printing it.
    return total + remaining * 3000

# PART 2: LOOP
# Function: Use an inclusive for-loop to accumulate integers from 1 through n.
```

### Giải thích quy trình giải và công thức

Không nhân tất cả kWh với mức giá cao nhất. Lần lượt tính 50 kWh ở bậc 1, 50 kWh tiếp theo bậc 2, phần còn lại 20 kWh bậc 3.

**Quy tắc / công thức:** `50×1.800 + 50×2.000 + 20×2.500 = 240.000 VND`. Số 282.000 VND trong Word không suy ra từ bảng giá.

## Bài 8 — Sum from 1 to n

### English — Original Word requirement

Input a positive integer `n` and calculate the sum of all integers from 1 to `n`.

**Example:** Input `10` → `Sum = 55`.

### Tiếng Việt — Dịch đề

Nhập số nguyên dương `n`, dùng vòng lặp tính tổng các số từ 1 đến `n`. Ví dụ `n=10` → 55.

### Bài giải — Code đã được làm và chú thích

**Nguồn hàm:** `SOLUTION.py` / bản chú thích `SOLUTION_ANNOTATED.py`, hàm `task08_sum_to_n()`. Code demo cũ chỉ là phần thực hành ban đầu và có chỗ chưa hoàn chỉnh; không coi demo là lời giải đầy đủ.

```python
def task08_sum_to_n(n):
    # Reject out-of-range or missing inputs early instead of silently accepting them.
    if n <= 0: raise ValueError("n must be positive")
    # Prepare this intermediate value for the next calculation or validation.
    total=0
    # Iterate the exact number of steps specified by the exercise.
    for value in range(1,n+1): total += value
    # Return the result for later reuse or testing instead of only printing it.
    return total

# Function: Use a while-loop and integer division to remove one digit per iteration.
```

### Giải thích quy trình giải và công thức

Tạo biến tổng ban đầu bằng 0, sau đó cộng từng giá trị của `range(1,n+1)`.

**Quy tắc / công thức:** Tổng `1+2+⋯+n = n(n+1)/2`, nhưng code nguồn dùng vòng lặp đúng yêu cầu.

## Bài 9 — Count digits

### English — Original Word requirement

Input a positive integer and count the number of digits.

**Example:** `123456` → `Number of digits = 6`.

**Requirement:** Use a `while` loop.

### Tiếng Việt — Dịch đề

Nhập số nguyên dương, **dùng `while`** để đếm số chữ số. Ví dụ 123456 có 6 chữ số.

### Bài giải — Code đã được làm và chú thích

**Nguồn hàm:** `SOLUTION.py` / bản chú thích `SOLUTION_ANNOTATED.py`, hàm `task09_count_digits()`. Code demo cũ chỉ là phần thực hành ban đầu và có chỗ chưa hoàn chỉnh; không coi demo là lời giải đầy đủ.

```python
def task09_count_digits(n):
    # Reject out-of-range or missing inputs early instead of silently accepting them.
    if n <= 0: raise ValueError("n must be positive")
    # Prepare this intermediate value for the next calculation or validation.
    count=0
    # Repeat this operation until the stopping condition becomes false.
    while n:
        count += 1
        n //= 10
    # Return the result for later reuse or testing instead of only printing it.
    return count

# Function: Only test divisors from 2 through integer square root to detect compositeness.
```

### Giải thích quy trình giải và công thức

Mỗi lượt dùng phép chia nguyên cho 10 để bỏ chữ số tận cùng, rồi tăng biến đếm; tiếp tục khi số vẫn lớn hơn 0.

**Quy tắc / công thức:** `n //= 10` sau mỗi lượt, số lần lặp là số chữ số.

## Bài 10 — Prime number

### English — Original Word requirement

Input a positive integer and determine whether it is prime.

**Example:** `17` → `17 is a prime number.`

### Tiếng Việt — Dịch đề

Nhập số nguyên dương và kiểm tra nó có phải số nguyên tố hay không. Ví dụ 17 là số nguyên tố.

### Bài giải — Code đã được làm và chú thích

**Nguồn hàm:** `SOLUTION.py` / bản chú thích `SOLUTION_ANNOTATED.py`, hàm `task10_is_prime()`. Code demo cũ chỉ là phần thực hành ban đầu và có chỗ chưa hoàn chỉnh; không coi demo là lời giải đầy đủ.

```python
def task10_is_prime(n):
    # Branch when this validated condition is true.
    if n <= 1: return False
    # Iterate the exact number of steps specified by the exercise.
    for divisor in range(2,isqrt(n)+1):
        # Branch when this validated condition is true.
        if n % divisor == 0: return False
    # Return the result for later reuse or testing instead of only printing it.
    return True

# Function: Use Euclid's remainder algorithm until the second argument reaches zero.
```

### Giải thích quy trình giải và công thức

Số nguyên tố phải lớn hơn 1. Thử ước số từ 2 đến căn bậc hai nguyên; nếu tìm thấy ước thì không nguyên tố.

**Quy tắc / công thức:** Chỉ cần thử ước `d ≤ √n`, vì một cặp thừa số của hợp số luôn có ít nhất một số không vượt √n.

## Bài 11 — GCD

### English — Original Word requirement

Input two positive integers and find their Greatest Common Divisor (GCD).

**Example:** `24 36` → `GCD = 12`.

### Tiếng Việt — Dịch đề

Nhập hai số nguyên dương, tính **ước chung lớn nhất (GCD)**. Ví dụ 24 và 36 có GCD bằng 12.

### Bài giải — Code đã được làm và chú thích

**Nguồn hàm:** `SOLUTION.py` / bản chú thích `SOLUTION_ANNOTATED.py`, hàm `task11_gcd()`. Code demo cũ chỉ là phần thực hành ban đầu và có chỗ chưa hoàn chỉnh; không coi demo là lời giải đầy đủ.

```python
def task11_gcd(a,b):
    # Reject out-of-range or missing inputs early instead of silently accepting them.
    if a<=0 or b<=0: raise ValueError("Both numbers must be positive")
    # Repeat this operation until the stopping condition becomes false.
    while b:
        a,b=b,a%b
    # Return the result for later reuse or testing instead of only printing it.
    return a

# Function: Build a rectangle of asterisks using nested loops for rows and columns.
```

### Giải thích quy trình giải và công thức

Thực hiện thuật toán Euclid bằng phần dư; thay cặp số cho đến khi số thứ hai bằng 0.

**Quy tắc / công thức:** `gcd(a,b) = gcd(b, a % b)` khi `b != 0`.

## Bài 12 — Rectangle pattern

### English — Original Word requirement

Input integers `m` and `n`, then print a rectangle with `m` rows and `n` columns using `*`.

For `m = 4`, `n = 6`:

```text
******
******
******
******
```

**Requirement:** Use nested loops.

### Tiếng Việt — Dịch đề

Nhập `m`, `n`, **dùng vòng lặp lồng nhau** để in hình chữ nhật có `m` dòng, `n` cột ký tự `*`. Mẫu 4 dòng × 6 cột như đề.

### Bài giải — Code đã được làm và chú thích

**Nguồn hàm:** `SOLUTION.py` / bản chú thích `SOLUTION_ANNOTATED.py`, hàm `task12_rectangle()`. Code demo cũ chỉ là phần thực hành ban đầu và có chỗ chưa hoàn chỉnh; không coi demo là lời giải đầy đủ.

```python
def task12_rectangle(rows,cols):
    # Reject out-of-range or missing inputs early instead of silently accepting them.
    if rows <= 0 or cols <= 0: raise ValueError("Rows/cols must be positive")
    # Prepare this intermediate value for the next calculation or validation.
    output=[]
    # Iterate the exact number of steps specified by the exercise.
    for _ in range(rows):
        # Prepare this intermediate value for the next calculation or validation.
        line=""
        # Iterate the exact number of steps specified by the exercise.
        for _ in range(cols):
            line += "*"
        # Add the new element to a list while retaining insertion order.
        output.append(line)
    # Return the result for later reuse or testing instead of only printing it.
    return "\n".join(output)

# Function: Build one line per integer with the integer repeated its row number of times.
```

### Giải thích quy trình giải và công thức

Vòng ngoài tạo hàng, vòng trong nối từng dấu `*`; ghép các hàng bằng xuống dòng.

**Quy tắc / công thức:** Số ký tự `*` in ra bằng `m × n`.

## Bài 13 — Repeated-digit triangle

### English — Original Word requirement

Input an integer `n` and print a number triangle. For `n = 5`:

```text
1
22
333
4444
55555
```

**Requirement:** Use nested loops.

### Tiếng Việt — Dịch đề

Nhập `n`, **dùng vòng lặp lồng nhau** để in tam giác chữ số: hàng 1 là `1`, hàng 2 là `22`, …, hàng 5 là `55555`.

### Bài giải — Code đã được làm và chú thích

**Nguồn hàm:** `SOLUTION.py` / bản chú thích `SOLUTION_ANNOTATED.py`, hàm `task13_repeated_triangle()`. Code demo cũ chỉ là phần thực hành ban đầu và có chỗ chưa hoàn chỉnh; không coi demo là lời giải đầy đủ.

```python
def task13_repeated_triangle(n):
    # Reject out-of-range or missing inputs early instead of silently accepting them.
    if n <= 0: raise ValueError("n must be positive")
    # Prepare this intermediate value for the next calculation or validation.
    output=[]
    # Iterate the exact number of steps specified by the exercise.
    for i in range(1,n+1):
        # Prepare this intermediate value for the next calculation or validation.
        line=""
        # Iterate the exact number of steps specified by the exercise.
        for _ in range(i):
            line += str(i)
        # Add the new element to a list while retaining insertion order.
        output.append(line)
    # Return the result for later reuse or testing instead of only printing it.
    return "\n".join(output)

# Function: Generate consecutive increasing numbers, updating the counter after each cell.
```

### Giải thích quy trình giải và công thức

Vòng ngoài chọn số hàng `i`, vòng trong lặp lại ký tự `str(i)` đúng `i` lần.

**Quy tắc / công thức:** Hàng i có i ký tự; tổng số ký tự là `n(n+1)/2`.

## Bài 14 — Consecutive-number triangle

### English — Original Word requirement

Input an integer `n` and print a triangle containing consecutive numbers. For `n = 4`:

```text
1
2 3
4 5 6
7 8 9 10
```

**Requirement:** Use nested loops and a variable to track the current number.

### Tiếng Việt — Dịch đề

Nhập `n`, **dùng vòng lặp lồng nhau** và một biến đếm liên tục để in tam giác số tăng dần. Với `n=4`: dòng 1 là `1`, dòng 2 `2 3`, dòng 3 `4 5 6`, dòng 4 `7 8 9 10`.

### Bài giải — Code đã được làm và chú thích

**Nguồn hàm:** `SOLUTION.py` / bản chú thích `SOLUTION_ANNOTATED.py`, hàm `task14_consecutive_triangle()`. Code demo cũ chỉ là phần thực hành ban đầu và có chỗ chưa hoàn chỉnh; không coi demo là lời giải đầy đủ.

```python
def task14_consecutive_triangle(n):
    # Reject out-of-range or missing inputs early instead of silently accepting them.
    if n <= 0: raise ValueError("n must be positive")
    # Prepare this intermediate value for the next calculation or validation.
    rows=[]
    # Prepare this intermediate value for the next calculation or validation.
    current=1
    # Iterate the exact number of steps specified by the exercise.
    for i in range(1,n+1):
        # Prepare this intermediate value for the next calculation or validation.
        values=[]
        # Iterate the exact number of steps specified by the exercise.
        for _ in range(i):
            # Add the new element to a list while retaining insertion order.
            values.append(str(current))
            current += 1
        # Add the new element to a list while retaining insertion order.
        rows.append(" ".join(values))
    # Return the result for later reuse or testing instead of only printing it.
    return "\n".join(rows)

# Function: Execute all fourteen reference examples and assert expected results before printing a summary.
```

### Giải thích quy trình giải và công thức

Biến `current` bắt đầu từ 1; vòng trong in số rồi tăng biến này trước khi sang hàng khác.

**Quy tắc / công thức:** Hàng i có i số; số cuối tam giác n hàng là `n(n+1)/2`.

## Lưu ý quan trọng về đề Word

Ở bài 7, đề đưa ví dụ **120 kWh → 282000 VND**, trong khi phép tính lũy tiến theo chính bảng giá trong đề là **240000 VND**. Tài liệu giữ số gốc trong phần tiếng Anh, giải thích sai khác và không âm thầm thay đổi số liệu.

**Xuất bản:** chỉ một file `LAB-04-conditions-loops.md` chứa cả đề tiếng Anh, bản dịch tiếng Việt, code nguồn và giải thích từng bài. Mã được trích từ repo hiện có; để chạy phải ghép tất cả hàm với các import/hàm phụ trợ như ở file tham chiếu.
