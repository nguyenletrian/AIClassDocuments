# LAB Session 4 — English tasks with fully annotated solutions

## PART 1: CONDITIONAL STATEMENT

### Exercise 1 — Sorting numbers
Write a program that inputs three real numbers and prints them in ascending order.

**Requirement:** Use only `if...else` statements.

**Example:** Input: `8.5 3.2 6.7` → Output: `3.2 6.7 8.5`


**Annotated solution — runnable Python:**

```python
# Import the matching thoroughly commented function from this folder.
from SOLUTION_ANNOTATED import task01_sort_three

# Reproduce the provided example without interactive keyboard input.
print(task01_sort_three(8.5, 3.2, 6.7))
```

**Step-by-step explanation:** Three conditional swaps compare a/b, b/c and a/b, without built-in sorting. Read [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py) to see the complete function with comments explaining its branches, parameters and output.

### Exercise 2 — Quarter of the year
Write a program that inputs a month (1–12) and determines which quarter of the year it belongs to.

**Example:** Input: `5` → Output: `Quarter 2`

**Requirement:** Use `if...elif...else` or `match...case`.


**Annotated solution — runnable Python:**

```python
# Import the matching thoroughly commented function from this folder.
from SOLUTION_ANNOTATED import task02_quarter

# Reproduce the provided example without interactive keyboard input.
print('Quarter', task02_quarter(5))
```

**Step-by-step explanation:** The first three months form Quarter 1, then each next group of three forms a new quarter; an invalid month raises ValueError. Read [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py) to see the complete function with comments explaining its branches, parameters and output.

### Exercise 3 — Days in a month
Write a program that inputs a month. Determine the number of days in that month.

**Example:** Input: `3` → Output: `31 days`


**Annotated solution — runnable Python:**

```python
# Import the matching thoroughly commented function from this folder.
from SOLUTION_ANNOTATED import task03_month_days

# Reproduce the provided example without interactive keyboard input.
print(task03_month_days(2, year=2024), 'days')
```

**Step-by-step explanation:** A twelve-month lookup table provides normal day counts; leap-year February is handled separately. Read [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py) to see the complete function with comments explaining its branches, parameters and output.

### Exercise 4 — Leap year
Write a program that inputs a year and determines whether it is a leap year.

**Leap year rules:**
- A year divisible by 400 is a leap year.
- A year divisible by 4 but not divisible by 100 is a leap year.
- Otherwise, it is not a leap year.

**Examples:** `2024` → `Leap year`; `2023` → `Not a leap year`.


**Annotated solution — runnable Python:**

```python
# Import the matching thoroughly commented function from this folder.
from SOLUTION_ANNOTATED import task04_is_leap

# Reproduce the provided example without interactive keyboard input.
print(task04_is_leap(2024))
print(task04_is_leap(2023))
```

**Step-by-step explanation:** The century exception matters: 1900 is not a leap year but 2000 is. Read [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py) to see the complete function with comments explaining its branches, parameters and output.

### Exercise 5 — Number name (two digits)
Write a program that inputs a two-digit integer and prints its number name.

**Examples:** `12` → `muoi hai`; `25` → `hai muoi lam`.


**Annotated solution — runnable Python:**

```python
# Import the matching thoroughly commented function from this folder.
from SOLUTION_ANNOTATED import task05_two_digit

# Reproduce the provided example without interactive keyboard input.
print(task05_two_digit(12))
print(task05_two_digit(25))
```

**Step-by-step explanation:** Integer division // finds tens, divmod returns both tens and units; Vietnamese units may change pronunciation. Read [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py) to see the complete function with comments explaining its branches, parameters and output.

### Exercise 6 — Number name (three digits)
Write a program that inputs a three-digit integer and prints its number name.

**Example:** `123` → `mot tram hai muoi ba`.


**Annotated solution — runnable Python:**

```python
# Import the matching thoroughly commented function from this folder.
from SOLUTION_ANNOTATED import task06_three_digit

# Reproduce the provided example without interactive keyboard input.
print(task06_three_digit(123))
print(task06_three_digit(105))
```

**Step-by-step explanation:** The hundreds are separated from the remainder, which is spoken with the tens rule or 'linh' when needed. Read [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py) to see the complete function with comments explaining its branches, parameters and output.

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


**Annotated solution — runnable Python:**

```python
# Import the matching thoroughly commented function from this folder.
from SOLUTION_ANNOTATED import task07_electricity_bill

# Reproduce the provided example without interactive keyboard input.
print(task07_electricity_bill(120), 'VND')
```

**Step-by-step explanation:** Progressive billing: 50×1,800 + 50×2,000 + 20×2,500 = 240,000 VND. The original Word example 282,000 VND contradicts its own rate table and is not silently adopted. Read [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py) to see the complete function with comments explaining its branches, parameters and output.

### Exercise 8 — Sum from 1 to n
Input a positive integer `n` and calculate the sum of all integers from 1 to `n`.

**Example:** Input `10` → `Sum = 55`.


**Annotated solution — runnable Python:**

```python
# Import the matching thoroughly commented function from this folder.
from SOLUTION_ANNOTATED import task08_sum_to_n

# Reproduce the provided example without interactive keyboard input.
print('Sum =', task08_sum_to_n(10))
```

**Step-by-step explanation:** range(1, n+1) includes n; a running total accumulates each value. Read [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py) to see the complete function with comments explaining its branches, parameters and output.

### Exercise 9 — Count digits
Input a positive integer and count the number of digits.

**Example:** `123456` → `Number of digits = 6`.

**Requirement:** Use a `while` loop.


**Annotated solution — runnable Python:**

```python
# Import the matching thoroughly commented function from this folder.
from SOLUTION_ANNOTATED import task09_count_digits

# Reproduce the provided example without interactive keyboard input.
print('Number of digits =', task09_count_digits(123456))
```

**Step-by-step explanation:** The mandatory while loop removes one decimal digit each time with integer division by 10. Read [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py) to see the complete function with comments explaining its branches, parameters and output.

### Exercise 10 — Prime number
Input a positive integer and determine whether it is prime.

**Example:** `17` → `17 is a prime number.`


**Annotated solution — runnable Python:**

```python
# Import the matching thoroughly commented function from this folder.
from SOLUTION_ANNOTATED import task10_is_prime

# Reproduce the provided example without interactive keyboard input.
print(task10_is_prime(17))
```

**Step-by-step explanation:** Composite divisors come in pairs: it suffices to check integers up to isqrt(n); 1 is not prime. Read [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py) to see the complete function with comments explaining its branches, parameters and output.

### Exercise 11 — GCD
Input two positive integers and find their Greatest Common Divisor (GCD).

**Example:** `24 36` → `GCD = 12`.


**Annotated solution — runnable Python:**

```python
# Import the matching thoroughly commented function from this folder.
from SOLUTION_ANNOTATED import task11_gcd

# Reproduce the provided example without interactive keyboard input.
print('GCD =', task11_gcd(24, 36))
```

**Step-by-step explanation:** Euclid's algorithm repeatedly replaces (a,b) with (b,a % b) until b is zero. Read [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py) to see the complete function with comments explaining its branches, parameters and output.

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


**Annotated solution — runnable Python:**

```python
# Import the matching thoroughly commented function from this folder.
from SOLUTION_ANNOTATED import task12_rectangle

# Reproduce the provided example without interactive keyboard input.
print(task12_rectangle(4, 6))
```

**Step-by-step explanation:** The outer loop creates each row and the inner loop appends one asterisk per column. Read [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py) to see the complete function with comments explaining its branches, parameters and output.

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


**Annotated solution — runnable Python:**

```python
# Import the matching thoroughly commented function from this folder.
from SOLUTION_ANNOTATED import task13_repeated_triangle

# Reproduce the provided example without interactive keyboard input.
print(task13_repeated_triangle(5))
```

**Step-by-step explanation:** Each row uses nested loops to repeat the row number i times. Read [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py) to see the complete function with comments explaining its branches, parameters and output.

### Exercise 14 — Consecutive-number triangle
Input an integer `n` and print a triangle containing consecutive numbers. For `n = 4`:

```text
1
2 3
4 5 6
7 8 9 10
```

**Requirement:** Use nested loops and a variable to track the current number.

*Source: existing English transcription of `LAB Session 4.docx` in `labs/pythoclass/LAB-04-conditions-loops/LAB.md`. The original Word example for electricity cost is preserved and its mathematical inconsistency is explained. This export adds a solution directly after each of the 14 exercises.*

**Annotated solution — runnable Python:**

```python
# Import the matching thoroughly commented function from this folder.
from SOLUTION_ANNOTATED import task14_consecutive_triangle

# Reproduce the provided example without interactive keyboard input.
print(task14_consecutive_triangle(4))
```

**Step-by-step explanation:** A counter advances after every printed number so rows have 1,2,3,4 terms. Read [SOLUTION_ANNOTATED.py](SOLUTION_ANNOTATED.py) to see the complete function with comments explaining its branches, parameters and output.

