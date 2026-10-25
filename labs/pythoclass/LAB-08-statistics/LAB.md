# LAB SESSION 8

## Problem Description
A mobile application company wants to analyze users' daily app usage time to understand usage patterns, data variability, and statistical characteristics.

You are given daily app usage time for **50 users**, measured in **minutes per day**.

## Dataset

```python
usage_minutes = [
    35, 45, 50, 55, 60, 65, 70, 75, 80, 85,
    90, 95, 100, 105, 110, 115, 120, 120, 125, 130,
    135, 140, 145, 150, 155, 160, 165, 170, 175, 180,
    185, 190, 195, 200, 205, 210, 215, 220, 225, 230,
    240, 250, 260, 270, 280, 290, 300, 320, 350, 480
]
```

## Requirements

### Task 1 – Descriptive Statistics
- Calculate mean, median, and mode.
- Find min, max, and range.
- Calculate **sample** variance and **sample** standard deviation.

### Task 2 – Frequency Distribution and Histogram
Divide usage into the six groups below:

| Group | Usage time (minutes/day) |
|---|---|
| 1 | 0–60 |
| 2 | 60–120 |
| 3 | 120–180 |
| 4 | 180–240 |
| 5 | 240–360 |
| 6 | 360–500 |

- Use `pd.cut()` and `value_counts()` to create a frequency distribution table.
- Calculate cumulative frequency using `cumsum()`.
- Create a histogram with title and axis labels.

### Task 3 – Quartiles and Outlier Detection
- Calculate Q1, Q2, Q3 and IQR.
- Calculate lower and upper bounds using **1.5 × IQR**.
- Identify usage times outside the bounds.

### Task 4 – Sampling and Hypothesis Testing
- Randomly select 10 users.
- Calculate sample mean and compare it with mean of all 50 users.
- Test the company's claim that **population mean usage is 120 minutes/day**, using a **one-sample t-test** at `α = 0.05`.
- Based on p-value, decide whether to reject or fail to reject `H₀`.

### Task 5 – Conclusion
Write a short conclusion (3–5 sentences) about:
- Typical daily app usage time.
- Variability and presence of outliers.
- Hypothesis-test result.
- One recommendation for the company.

*Chuyển từ `LAB SESSION 8.docx` sang Markdown.*
