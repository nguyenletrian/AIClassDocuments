# LAB-04-conditions-loops — English brief, Vietnamese brief, method and full commented script

**Nguồn đề:** `PythoClass` Word (bản chép ở `labs/pythoclass/LAB-04-conditions-loops/LAB.md`). **Nguồn code:** bản giải/annotated có sẵn từ repo AIClassDocuments (không nhận là nguyên văn code demo nếu demo chưa đủ), đối chiếu `labs/pythoclass/LAB-04-conditions-loops/DEMO.py` và `SOLUTION.py`. **Một tài liệu duy nhất**, không chia đề/đáp án xen kẽ.

---

## PART 1 — COMPLETE ORIGINAL ENGLISH ASSIGNMENT

# LAB Session 4

## PART 1: CONDITIONAL STATEMENT

### Exercise 1 — Sorting numbers
Write a program that inputs three real numbers and prints them in ascending order.

**Requirement:** Use only `if...else` statements.

**Example:** Input: `8.5 3.2 6.7` → Output: `3.2 6.7 8.5`

### Exercise 2 — Quarter of the year
Write a program that inputs a month (1–12) and determines which quarter of the year it belongs to.

**Example:** Input: `5` → Output: `Quarter 2`

**Requirement:** Use `if...elif...else` or `match...case`.

### Exercise 3 — Days in a month
Write a program that inputs a month. Determine the number of days in that month.

**Example:** Input: `3` → Output: `31 days`

### Exercise 4 — Leap year
Write a program that inputs a year and determines whether it is a leap year.

**Leap year rules:**
- A year divisible by 400 is a leap year.
- A year divisible by 4 but not divisible by 100 is a leap year.
- Otherwise, it is not a leap year.

**Examples:** `2024` → `Leap year`; `2023` → `Not a leap year`.

### Exercise 5 — Number name (two digits)
Write a program that inputs a two-digit integer and prints its number name.

**Examples:** `12` → `muoi hai`; `25` → `hai muoi lam`.

### Exercise 6 — Number name (three digits)
Write a program that inputs a three-digit integer and prints its number name.

**Example:** `123` → `mot tram hai muoi ba`.

### Exercise 7 — Electricity bill
Write a program that inputs the amount of electricity consumed in kWh and calculates the electricity bill based on the following rates:

| Electricity usage | Price |
|---|---|
| 0–50 kWh | 1,800 VND/kWh |
| 51–100 kWh | 2,000 VND/kWh |
| 101–200 kWh | 2,500 VND/kWh |
| Above 200 kWh | 3,000 VND/kWh |

**Example in original Word:** Input `120` → Output `282000 VND`.


## PART 2: LOOP

### Exercise 8 — Sum from 1 to n
Input a positive integer `n` and calculate the sum of all integers from 1 to `n`.

**Example:** Input `10` → `Sum = 55`.

### Exercise 9 — Count digits
Input a positive integer and count the number of digits.

**Example:** `123456` → `Number of digits = 6`.

**Requirement:** Use a `while` loop.

### Exercise 10 — Prime number
Input a positive integer and determine whether it is prime.

**Example:** `17` → `17 is a prime number.`

### Exercise 11 — GCD
Input two positive integers and find their Greatest Common Divisor (GCD).

**Example:** `24 36` → `GCD = 12`.

### Exercise 12 — Rectangle pattern
Input integers `m` and `n`, then print a rectangle with `m` rows and `n` columns using `*`.

For `m = 4`, `n = 6`:

```text
******
******
******
******
```

**Requirement:** Use nested loops.

### Exercise 13 — Repeated-digit triangle
Input an integer `n` and print a number triangle. For `n = 5`:

```text
1
22
333
4444
55555
```

**Requirement:** Use nested loops.

### Exercise 14 — Consecutive-number triangle
Input an integer `n` and print a triangle containing consecutive numbers. For `n = 4`:

```text
1
2 3
4 5 6
7 8 9 10
```

**Requirement:** Use nested loops and a variable to track the current number.

---

## PHẦN 2 — BẢN DỊCH TIẾNG VIỆT TOÀN BỘ ĐỀ

# LAB SESSION 4 — Câu lệnh điều kiện và vòng lặp

## PHẦN 1: CÂU LỆNH ĐIỀU KIỆN

### Bài 1 — Sắp xếp ba số
Nhập ba số thực và in ra theo thứ tự tăng dần. **Chỉ được dùng `if...else`**, không dùng hàm sắp xếp có sẵn. Ví dụ: `8.5 3.2 6.7` → `3.2 6.7 8.5`.

### Bài 2 — Quý trong năm
Nhập tháng từ 1–12 rồi xác định thuộc quý nào. Ví dụ: 5 → Quý 2. **Dùng `if...elif...else` hoặc `match...case`**.

### Bài 3 — Số ngày trong tháng
Nhập tháng và xác định số ngày trong tháng. Ví dụ tháng 3 có 31 ngày. Nếu xét tháng 2 và có năm, cần xét năm nhuận.

### Bài 4 — Năm nhuận
Nhập năm rồi xác định năm nhuận. Năm chia hết cho 400 là năm nhuận; hoặc chia hết cho 4 nhưng không chia hết cho 100. Các trường hợp khác không nhuận. Ví dụ 2024 nhuận, 2023 không nhuận.

### Bài 5 — Đọc số có hai chữ số
Nhập số nguyên hai chữ số, in cách đọc số bằng tiếng Việt. Ví dụ: 12 → `muoi hai`; 25 → `hai muoi lam`.

### Bài 6 — Đọc số có ba chữ số
Nhập số nguyên ba chữ số, in cách đọc bằng tiếng Việt. Ví dụ: 123 → `mot tram hai muoi ba`.

### Bài 7 — Tính tiền điện
Nhập lượng điện tiêu thụ (kWh), tính hóa đơn từ bảng giá:

| Lượng điện tiêu thụ | Đơn giá |
|---|---:|
| 0–50 kWh | 1.800 VND/kWh |
| 51–100 kWh | 2.000 VND/kWh |
| 101–200 kWh | 2.500 VND/kWh |
| Trên 200 kWh | 3.000 VND/kWh |

**Ví dụ trong Word:** 120 kWh → 282.000 VND. *Giá trị này được giữ nguyên khi dịch; lưu ý kiểm tra lại với phương pháp tính lũy tiến.*

## PHẦN 2: VÒNG LẶP

### Bài 8 — Tổng từ 1 đến n
Nhập số nguyên dương `n`, tính tổng các số nguyên từ 1 đến `n`. Ví dụ: 10 → 55.

### Bài 9 — Đếm chữ số
Nhập số nguyên dương, **dùng `while`** đếm số chữ số. Ví dụ 123456 có 6 chữ số.

### Bài 10 — Kiểm tra số nguyên tố
Nhập số nguyên dương và xác định có phải số nguyên tố không. Ví dụ 17 là số nguyên tố.

### Bài 11 — Ước chung lớn nhất
Nhập hai số nguyên dương, tính GCD. Ví dụ 24 và 36 → 12.

### Bài 12 — Hình chữ nhật dấu sao
Nhập `m`, `n`, dùng **vòng lặp lồng nhau** in hình chữ nhật `m` hàng, `n` cột bằng ký tự `*`. Với `m=4,n=6`:

```text
******
******
******
******
```

### Bài 13 — Tam giác chữ số lặp
Nhập `n`, dùng **vòng lặp lồng nhau** in tam giác. Với `n=5`:

```text
1
22
333
4444
55555
```

### Bài 14 — Tam giác số liên tiếp
Nhập `n`, dùng **vòng lặp lồng nhau** và biến đếm liên tục. Với `n=4`:

```text
1
2 3
4 5 6
7 8 9 10
```

---

## Quy trình giải chi tiết và các công thức liên quan

**Luồng giải chung:** Đọc yêu cầu và dữ liệu đầu vào → xác thực kiểu và miền giá trị → chọn cấu trúc dữ liệu/điều kiện/vòng lặp đã học → tính toán hoặc cập nhật → kiểm tra kết quả bằng ví dụ đề → xử lý trường hợp rỗng/sai. Các hàm trong phần code bên dưới là một chương trình hoàn chỉnh và có thể chạy cùng nhau.

### Bài 1 — Cách thực hiện

So sánh cặp `(a,b)`, `(b,c)`, rồi `(a,b)` và đổi chỗ khi cặp không đúng thứ tự. Đây là cách dùng điều kiện, không gọi `sort()`.

**Quy tắc / công thức:** Nếu `a > b` thì hoán đổi `a,b = b,a`; tương tự cho các cặp.

**Điểm cần kiểm tra:** dùng `if/elif/else` đúng các bài điều kiện và so sánh hai số.

### Bài 2 — Cách thực hiện

Kiểm tra tháng hợp lệ, sau đó xem tháng nằm ở 1–3, 4–6, 7–9 hay 10–12 để trả quý.

**Quy tắc / công thức:** Quý có thể xác định bằng `(month-1)//3 + 1` nhưng code nguồn thực hành `if/elif` đúng yêu cầu.

**Điểm cần kiểm tra:** quy tắc năm nhuận và số ngày tháng 2.

### Bài 3 — Cách thực hiện

Dùng danh sách ngày của 12 tháng. Nếu tháng 2 của năm nhuận thì lấy 29, không lấy 28. Mã này tham chiếu thêm `leap_year()` ở mã nguồn đã học.

**Quy tắc / công thức:** Năm nhuận: `year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)`.

**Điểm cần kiểm tra:** tách chữ số bằng phép chia nguyên `//` và chia dư `%`.

### Bài 4 — Cách thực hiện

Dùng toán tử `%` kiểm tra các trường hợp chia hết; điều kiện năm dương loại đầu vào không hợp lệ.

**Quy tắc / công thức:** Chia hết cho 400 **hoặc** chia hết cho 4 và **không** chia hết cho 100.

**Điểm cần kiểm tra:** tiền điện lũy tiến: `50×1800 + 50×2000 + 20×2500 = 240000 VND` cho 120 kWh; đề Word ghi 282000, không khớp.

### Bài 5 — Cách thực hiện

Tách hàng chục và đơn vị, chọn từ đọc thích hợp trong danh sách từ đã có (`WORDS`). Một số trường hợp đặc biệt như số 25 đọc `lam`.

**Quy tắc / công thức:** `tens = n // 10`, `units = n % 10`.

**Điểm cần kiểm tra:** vòng lặp `for`/ `while`, nguyên tố đến `√n`, Euclid `gcd(a,b)=gcd(b,a%b)`.

### Bài 6 — Cách thực hiện

Tách hàng trăm và phần dư. Nếu phần dư nhỏ hơn 10 dùng cách đọc `linh`, còn lại gọi lại hàm đọc hai chữ số; cần dùng `WORDS` và `task05_two_digit` đã được định nghĩa chung.

**Quy tắc / công thức:** `hundreds = n // 100`, `rest = n % 100`.

**Điểm cần kiểm tra:** vòng lặp lồng nhau tạo đúng số dòng/cột và số chữ số.

### Bài 7 — Cách thực hiện

Không nhân tất cả kWh với mức giá cao nhất. Lần lượt tính 50 kWh ở bậc 1, 50 kWh tiếp theo bậc 2, phần còn lại 20 kWh bậc 3.

**Quy tắc / công thức:** `50×1.800 + 50×2.000 + 20×2.500 = 240.000 VND`. Số 282.000 VND trong Word không suy ra từ bảng giá.

**Điểm cần kiểm tra:** vòng lặp lồng nhau tạo đúng số dòng/cột và số chữ số.

### Bài 8 — Cách thực hiện

Tạo biến tổng ban đầu bằng 0, sau đó cộng từng giá trị của `range(1,n+1)`.

**Quy tắc / công thức:** Tổng `1+2+⋯+n = n(n+1)/2`, nhưng code nguồn dùng vòng lặp đúng yêu cầu.

**Điểm cần kiểm tra:** vòng lặp lồng nhau tạo đúng số dòng/cột và số chữ số.

### Bài 9 — Cách thực hiện

Mỗi lượt dùng phép chia nguyên cho 10 để bỏ chữ số tận cùng, rồi tăng biến đếm; tiếp tục khi số vẫn lớn hơn 0.

**Quy tắc / công thức:** `n //= 10` sau mỗi lượt, số lần lặp là số chữ số.

**Điểm cần kiểm tra:** vòng lặp lồng nhau tạo đúng số dòng/cột và số chữ số.

### Bài 10 — Cách thực hiện

Số nguyên tố phải lớn hơn 1. Thử ước số từ 2 đến căn bậc hai nguyên; nếu tìm thấy ước thì không nguyên tố.

**Quy tắc / công thức:** Chỉ cần thử ước `d ≤ √n`, vì một cặp thừa số của hợp số luôn có ít nhất một số không vượt √n.

**Điểm cần kiểm tra:** vòng lặp lồng nhau tạo đúng số dòng/cột và số chữ số.

### Bài 11 — Cách thực hiện

Thực hiện thuật toán Euclid bằng phần dư; thay cặp số cho đến khi số thứ hai bằng 0.

**Quy tắc / công thức:** `gcd(a,b) = gcd(b, a % b)` khi `b != 0`.

**Điểm cần kiểm tra:** vòng lặp lồng nhau tạo đúng số dòng/cột và số chữ số.

### Bài 12 — Cách thực hiện

Vòng ngoài tạo hàng, vòng trong nối từng dấu `*`; ghép các hàng bằng xuống dòng.

**Quy tắc / công thức:** Số ký tự `*` in ra bằng `m × n`.

**Điểm cần kiểm tra:** vòng lặp lồng nhau tạo đúng số dòng/cột và số chữ số.

### Bài 13 — Cách thực hiện

Vòng ngoài chọn số hàng `i`, vòng trong lặp lại ký tự `str(i)` đúng `i` lần.

**Quy tắc / công thức:** Hàng i có i ký tự; tổng số ký tự là `n(n+1)/2`.

**Điểm cần kiểm tra:** vòng lặp lồng nhau tạo đúng số dòng/cột và số chữ số.

### Bài 14 — Cách thực hiện

Biến `current` bắt đầu từ 1; vòng trong in số rồi tăng biến này trước khi sang hàng khác.

**Quy tắc / công thức:** Hàng i có i số; số cuối tam giác n hàng là `n(n+1)/2`.

**Điểm cần kiểm tra:** vòng lặp lồng nhau tạo đúng số dòng/cột và số chữ số.


---

## PHẦN 4 — TOÀN BỘ CODE PYTHON CÙNG CHÚ THÍCH

**Nguồn code:** `labs/pythoclass/LAB-04-conditions-loops/SOLUTION.py` và phiên bản chú thích đã có trong lịch sử dự án. Code giữ nguyên logic thực hành; `#` trong file dùng để giải thích từng đoạn. Sao chép **nguyên khối** sau vào một file `lab_solution.py` trong môi trường Python; chạy bằng `python lab_solution.py --demo` nếu là lab menu, hoặc `python lab_solution.py` để thực hiện lệnh tương tác/kiểm thử. Các đường dẫn, nguồn dữ liệu đi kèm vẫn cần tuân theo hướng dẫn trong script.

```python
"""Fully annotated English solution for LAB-04-conditions-loops.
Source methods and executable statements are preserved from the reviewed
labs/pythoclass reference implementation; explanatory comments are added.
"""

"""LAB SESSION 4 — Solutions for all 14 Word exercises.

Each task has a named function. Run as a script for sample inputs and checks.
"""
# Bring integer-square-root utility into scope, avoiding floating-point rounding.
from math import isqrt

# PART 1: CONDITIONAL STATEMENT
# Function: Sort three real numbers only with conditional comparisons and swaps, never built-in sort().
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
def leap_year(year):
    # Return the result for later reuse or testing instead of only printing it.
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

# Function: Select the month from a 12-element day table, except leap-year February.
def task03_month_days(month, year=2026):
    # Prepare this intermediate value for the next calculation or validation.
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    # Reject out-of-range or missing inputs early instead of silently accepting them.
    if not 1 <= month <= 12: raise ValueError("Month must be 1..12")
    # Return the result for later reuse or testing instead of only printing it.
    return 29 if month == 2 and leap_year(year) else days[month-1]

# Function: Reject non-positive years and reuse the leap-year rule.
def task04_is_leap(year):
    # Reject out-of-range or missing inputs early instead of silently accepting them.
    if year < 1: raise ValueError("Year must be positive")
    # Return the result for later reuse or testing instead of only printing it.
    return leap_year(year)

# Prepare this intermediate value for the next calculation or validation.
WORDS = ["khong","mot","hai","ba","bon","nam","sau","bay","tam","chin"]

# Function: Split tens and units to reproduce the source exercise's Vietnamese number words.
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
def task11_gcd(a,b):
    # Reject out-of-range or missing inputs early instead of silently accepting them.
    if a<=0 or b<=0: raise ValueError("Both numbers must be positive")
    # Repeat this operation until the stopping condition becomes false.
    while b:
        a,b=b,a%b
    # Return the result for later reuse or testing instead of only printing it.
    return a

# Function: Build a rectangle of asterisks using nested loops for rows and columns.
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
def main():
    # Verify the expected outcome and fail the demo if a regression occurs.
    assert task01_sort_three(8.5,3.2,6.7)==(3.2,6.7,8.5)
    # Verify the expected outcome and fail the demo if a regression occurs.
    assert task02_quarter(5)==2
    # Verify the expected outcome and fail the demo if a regression occurs.
    assert task03_month_days(2,2024)==29
    # Verify the expected outcome and fail the demo if a regression occurs.
    assert task04_is_leap(2024) and not task04_is_leap(2023)
    # Verify the expected outcome and fail the demo if a regression occurs.
    assert task05_two_digit(25)=="hai muoi lam"
    # Verify the expected outcome and fail the demo if a regression occurs.
    assert task06_three_digit(123)=="mot tram hai muoi ba"
    # Verify the expected outcome and fail the demo if a regression occurs.
    assert task07_electricity_bill(120)==240000
    # Verify the expected outcome and fail the demo if a regression occurs.
    assert task08_sum_to_n(10)==55
    # Verify the expected outcome and fail the demo if a regression occurs.
    assert task09_count_digits(123456)==6
    # Verify the expected outcome and fail the demo if a regression occurs.
    assert task10_is_prime(17) and not task10_is_prime(1)
    # Verify the expected outcome and fail the demo if a regression occurs.
    assert task11_gcd(24,36)==12
    # Verify the expected outcome and fail the demo if a regression occurs.
    assert task12_rectangle(4,6)=="******\n******\n******\n******"
    # Verify the expected outcome and fail the demo if a regression occurs.
    assert task13_repeated_triangle(5)=="1\n22\n333\n4444\n55555"
    # Verify the expected outcome and fail the demo if a regression occurs.
    assert task14_consecutive_triangle(4)=="1\n2 3\n4 5 6\n7 8 9 10"
    # Show a human-readable result to the learner.
    print("PASS: 14 exercises")
    # Show a human-readable result to the learner.
    print("Example electricity 120 kWh:",task07_electricity_bill(120),"VND")
    # Show a human-readable result to the learner.
    print("Pattern:",task14_consecutive_triangle(4),sep="\n")

if __name__=="__main__":
    main()
```

**Lưu ý:** Nếu demo gốc chỉ thể hiện một phần, code đầy đủ được lấy từ lời giải tham khảo đã được lưu/kiểm tra, không phải phần tự sáng tác ở tài liệu này.
