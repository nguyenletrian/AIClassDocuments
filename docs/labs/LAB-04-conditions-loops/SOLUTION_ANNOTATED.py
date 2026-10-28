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
