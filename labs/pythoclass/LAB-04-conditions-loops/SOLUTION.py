"""LAB SESSION 4 — Solutions for all 14 Word exercises.

Each task has a named function. Run as a script for sample inputs and checks.
"""
from math import isqrt

# PART 1: CONDITIONAL STATEMENT
def task01_sort_three(a, b, c):
    if a > b: a, b = b, a
    if b > c: b, c = c, b
    if a > b: a, b = b, a
    return a, b, c

def task02_quarter(month):
    if not 1 <= month <= 12: raise ValueError("Month must be 1..12")
    if month <= 3: return 1
    elif month <= 6: return 2
    elif month <= 9: return 3
    else: return 4

def leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def task03_month_days(month, year=2026):
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if not 1 <= month <= 12: raise ValueError("Month must be 1..12")
    return 29 if month == 2 and leap_year(year) else days[month-1]

def task04_is_leap(year):
    if year < 1: raise ValueError("Year must be positive")
    return leap_year(year)

WORDS = ["khong","mot","hai","ba","bon","nam","sau","bay","tam","chin"]

def task05_two_digit(n):
    if not 10 <= n <= 99: raise ValueError("Expected two-digit integer")
    tens, unit = divmod(n,10)
    if tens == 1:
        head = "muoi"
    else:
        head = WORDS[tens] + " muoi"
    if unit == 0: return head
    if unit == 5: return head + " lam"
    if unit == 1 and tens > 1: return head + " mot"
    return head + " " + WORDS[unit]

def task06_three_digit(n):
    if not 100 <= n <= 999: raise ValueError("Expected three-digit integer")
    hundred, rest = divmod(n,100)
    head = WORDS[hundred] + " tram"
    if rest == 0: return head
    if rest < 10:
        return head + " linh " + ("nam" if rest == 5 else WORDS[rest])
    return head + " " + task05_two_digit(rest)

def task07_electricity_bill(kwh):
    """Progressive tiers, in VND; note Word's 282000 example is inconsistent."""
    if kwh < 0: raise ValueError("Usage cannot be negative")
    remaining = float(kwh)
    total = 0.0
    for width, rate in ((50,1800),(50,2000),(100,2500)):
        amount = min(remaining,width)
        total += amount * rate
        remaining -= amount
        if remaining <= 0: return total
    return total + remaining * 3000

# PART 2: LOOP
def task08_sum_to_n(n):
    if n <= 0: raise ValueError("n must be positive")
    total=0
    for value in range(1,n+1): total += value
    return total

def task09_count_digits(n):
    if n <= 0: raise ValueError("n must be positive")
    count=0
    while n:
        count += 1
        n //= 10
    return count

def task10_is_prime(n):
    if n <= 1: return False
    for divisor in range(2,isqrt(n)+1):
        if n % divisor == 0: return False
    return True

def task11_gcd(a,b):
    if a<=0 or b<=0: raise ValueError("Both numbers must be positive")
    while b:
        a,b=b,a%b
    return a

def task12_rectangle(rows,cols):
    if rows <= 0 or cols <= 0: raise ValueError("Rows/cols must be positive")
    output=[]
    for _ in range(rows):
        line=""
        for _ in range(cols):
            line += "*"
        output.append(line)
    return "\n".join(output)

def task13_repeated_triangle(n):
    if n <= 0: raise ValueError("n must be positive")
    output=[]
    for i in range(1,n+1):
        line=""
        for _ in range(i):
            line += str(i)
        output.append(line)
    return "\n".join(output)

def task14_consecutive_triangle(n):
    if n <= 0: raise ValueError("n must be positive")
    rows=[]
    current=1
    for i in range(1,n+1):
        values=[]
        for _ in range(i):
            values.append(str(current))
            current += 1
        rows.append(" ".join(values))
    return "\n".join(rows)

def main():
    assert task01_sort_three(8.5,3.2,6.7)==(3.2,6.7,8.5)
    assert task02_quarter(5)==2
    assert task03_month_days(2,2024)==29
    assert task04_is_leap(2024) and not task04_is_leap(2023)
    assert task05_two_digit(25)=="hai muoi lam"
    assert task06_three_digit(123)=="mot tram hai muoi ba"
    assert task07_electricity_bill(120)==240000
    assert task08_sum_to_n(10)==55
    assert task09_count_digits(123456)==6
    assert task10_is_prime(17) and not task10_is_prime(1)
    assert task11_gcd(24,36)==12
    assert task12_rectangle(4,6)=="******\n******\n******\n******"
    assert task13_repeated_triangle(5)=="1\n22\n333\n4444\n55555"
    assert task14_consecutive_triangle(4)=="1\n2 3\n4 5 6\n7 8 9 10"
    print("PASS: 14 exercises")
    print("Example electricity 120 kWh:",task07_electricity_bill(120),"VND")
    print("Pattern:",task14_consecutive_triangle(4),sep="\n")

if __name__=="__main__":
    main()
