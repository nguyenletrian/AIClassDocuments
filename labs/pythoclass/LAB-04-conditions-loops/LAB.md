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

> **Ghi chú hiệu đính:** Nếu giá điện được tính **lũy tiến từng bậc**, 120 kWh cho kết quả **240,000 VND**. Ví dụ `282000` trong Word không khớp bảng giá; `SOLUTION.py` tính lũy tiến và có kiểm tra kết quả. Số liệu ví dụ gốc được giữ ở đây để đối chiếu.

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

*Đề được chuyển từ `LAB Session 4.docx` sang Markdown; các ví dụ được đặt trong khối văn bản để không lỗi định dạng.*
