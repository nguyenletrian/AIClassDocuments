"""12 monthly sales records: if/elif, for, calendar validation."""
REVENUE = [16,19,20,24,31,28,26,29,36,33,38,41]  # million VND
def quarter(month):
    if month not in range(1, 13):
        raise ValueError("Month must be 1..12")
    return (month - 1) // 3 + 1
def leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
def days(month, year):
    d = (31,28,31,30,31,30,31,31,30,31,30,31)
    if month not in range(1,13): raise ValueError("Invalid month")
    return 29 if month == 2 and leap(year) else d[month-1]
def main():
    assert len(REVENUE) == 12
    for m, value in enumerate(REVENUE,1):
        print(f"Month {m:02}: Q{quarter(m)}, {value} million VND")
    print("Total:",sum(REVENUE),"months >25:",sum(x>25 for x in REVENUE))
    assert days(2,2028)==29 and days(2,2026)==28
if __name__ == "__main__":
    main()
