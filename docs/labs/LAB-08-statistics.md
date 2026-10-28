# Lab Session 8 — Thống kê thời gian dùng ứng dụng

**Word gốc:** `LAB SESSION 8.docx`. Bản đề tiếng Anh trích `labs/pythoclass/LAB-08-statistics/LAB.md`; code là các hàm đã có trong `SOLUTION.py`, được đối chiếu `DEMO.py` và các bài PY-17, PY-37..PY-40. Dữ liệu **50 người** được giữ nguyên; không dựng bộ dữ liệu mới hoặc giải theo thuật toán khác. Các hàm dùng chung trên một script tham khảo.

## English — Original problem and dataset

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

## Tiếng Việt — Bối cảnh và dữ liệu

Công ty ứng dụng di động muốn phân tích số phút mỗi ngày của **50 người dùng** để hiểu tần suất sử dụng, độ phân tán và đặc trưng thống kê. Đơn vị dữ liệu là **phút/ngày**. Các giá trị ví dụ gồm cả 480 phút; phải giữ lại để phát hiện ngoại lệ.

**Mã khởi tạo được trích từ script nguồn (đầy đủ 50 dòng):**

```python
import numpy as np
import pandas as pd
from scipy import stats
USAGE_MINUTES=np.array([
    35,45,50,55,60,65,70,75,80,85,
    90,95,100,105,110,115,120,120,125,130,
    135,140,145,150,155,160,165,170,175,180,
    185,190,195,200,205,210,215,220,225,230,
    240,250,260,270,280,290,300,320,350,480
],dtype=float)
```

## Bài 1 — Descriptive Statistics

### English — Original Word requirement

- Calculate mean, median, and mode.
- Find min, max, and range.
- Calculate **sample** variance and **sample** standard deviation.

### Tiếng Việt — Bản dịch

Từ 50 người dùng và số phút sử dụng ứng dụng mỗi ngày, tính trung bình (mean), trung vị (median), mốt (mode), nhỏ nhất, lớn nhất và khoảng biến thiên. Tính **phương sai mẫu** và **độ lệch chuẩn mẫu** (không dùng phương sai tổng thể).

### Bài giải — Trích code demo/giáo trình đã có

Nguồn: `labs/pythoclass/LAB-08-statistics/SOLUTION.py`, hàm `task01_descriptive()`. `DEMO.py` là code thực hành đối chiếu; đoạn trích bên dưới được ghi đúng xuất xứ là **lời giải tham khảo đã lưu**, không giả nhận demo giải đầy đủ bài.

```python
# Hàm task01_descriptive() lấy từ lời giải tham khảo hiện có.
def task01_descriptive(values):
    # ddof=1: SAMPLE variance/std rather than population versions.
    return {
        "mean":float(values.mean()),"median":float(np.median(values)),
        "mode":float(pd.Series(values).mode().iloc[0]),
        "minimum":float(values.min()),"maximum":float(values.max()),
        "range":float(np.ptp(values)),
        "sample_variance":float(values.var(ddof=1)),
        "sample_std":float(values.std(ddof=1)),
    }
```

### Giải thích quy trình giải và công thức

Dữ liệu 50 dòng được đưa nguyên vào `USAGE_MINUTES`. Dùng NumPy/Pandas tính các chỉ số; dùng `ddof=1` để phương sai chia cho n−1 chứ không phải n. Mode được lấy bằng `.mode().iloc[0]`.

**Công thức / quy tắc liên quan:** Trung bình = (tổng 50 số phút)/50; range = max−min; phương sai mẫu \(s^2=\frac{1}{n-1}\sum_i(x_i-\bar x)^2\); độ lệch chuẩn mẫu \(s=\sqrt{s^2}\).

## Bài 2 — Frequency Distribution and Histogram

### English — Original Word requirement

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

### Tiếng Việt — Bản dịch

Chia thời gian dùng ứng dụng thành đúng 6 nhóm: 0–60, 60–120, 120–180, 180–240, 240–360, 360–500 phút/ngày. Dùng `pd.cut()` và `value_counts()` tạo bảng tần suất, `cumsum()` tính tần suất tích lũy, vẽ histogram có tiêu đề và nhãn trục. Quy định rõ dữ liệu nằm ở ranh giới 60/120/... được tính đúng một nhóm.

### Bài giải — Trích code demo/giáo trình đã có

Nguồn: `labs/pythoclass/LAB-08-statistics/SOLUTION.py`, hàm `task02_frequency()`, `save_plot()`. `DEMO.py` là code thực hành đối chiếu; đoạn trích bên dưới được ghi đúng xuất xứ là **lời giải tham khảo đã lưu**, không giả nhận demo giải đầy đủ bài.

```python
# Hàm task02_frequency() lấy từ lời giải tham khảo hiện có.
def task02_frequency(values):
    # Half-open bins [0,60), [60,120), ... so boundary values count exactly once.
    bins=[0,60,120,180,240,360,500]
    labels=["0–<60","60–<120","120–<180","180–<240","240–<360","360–<500"]
    groups=pd.cut(values,bins=bins,labels=labels,right=False,include_lowest=True)
    freq=pd.Series(groups).value_counts(sort=False)
    frame=pd.DataFrame({"frequency":freq})
    frame["cumulative"]=frame["frequency"].cumsum()
    assert frame["frequency"].sum()==len(values)
    return bins,frame

# Hàm save_plot() lấy từ lời giải tham khảo hiện có.
def save_plot(values,bins):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    output=Path(__file__).resolve().parent/"outputs"
    output.mkdir(exist_ok=True)
    fig,ax=plt.subplots()
    ax.hist(values,bins=bins,edgecolor="black")
    ax.set(xlabel="Daily app usage (minutes)",ylabel="Users",title="Daily usage of 50 users")
    ax.grid(True,axis="y")
    target=output/"usage_histogram.png"
    fig.savefig(target,dpi=140,bbox_inches="tight")
    plt.close(fig)
    print("Saved:",target)
```

### Giải thích quy trình giải và công thức

Các khoảng liên tiếp trong `bins=[0,60,120,180,240,360,500]`, `right=False` nghĩa là [0,60), [60,120),… Tránh một phút đúng 60 hoặc 120 bị tính hai lần. Lấy tần số của từng khoảng rồi cộng dồn; hình histogram dùng chức năng `save_plot` đã có.

**Công thức / quy tắc liên quan:** Tần suất lớp i = số quan sát thuộc lớp i; tần suất tích lũy ở lớp k = tổng tần suất của các lớp 1..k. Tổng tần số phải bằng 50.

## Bài 3 — Quartiles and Outlier Detection

### English — Original Word requirement

- Calculate Q1, Q2, Q3 and IQR.
- Calculate lower and upper bounds using **1.5 × IQR**.
- Identify usage times outside the bounds.

### Tiếng Việt — Bản dịch

Tính Q1, Q2, Q3 và IQR; xác định biên dưới và biên trên theo quy tắc `1.5 × IQR`, rồi liệt kê các thời gian nằm ngoài hai biên này.

### Bài giải — Trích code demo/giáo trình đã có

Nguồn: `labs/pythoclass/LAB-08-statistics/SOLUTION.py`, hàm `task03_outliers()`. `DEMO.py` là code thực hành đối chiếu; đoạn trích bên dưới được ghi đúng xuất xứ là **lời giải tham khảo đã lưu**, không giả nhận demo giải đầy đủ bài.

```python
# Hàm task03_outliers() lấy từ lời giải tham khảo hiện có.
def task03_outliers(values):
    q1,q2,q3=np.percentile(values,[25,50,75])
    iqr=q3-q1
    low,high=q1-1.5*iqr,q3+1.5*iqr
    unusual=values[(values<low)|(values>high)]
    return q1,q2,q3,iqr,low,high,unusual
```

### Giải thích quy trình giải và công thức

`np.percentile` lấy ba phân vị, dùng IQR làm thước đo độ trải rộng ít nhạy với ngoại lệ. Các điểm nhỏ hơn biên dưới hoặc lớn hơn biên trên được đánh dấu, không tự động xóa.

**Công thức / quy tắc liên quan:** \(IQR=Q3-Q1\); biên dưới \(Q1-1.5\,IQR\); biên trên \(Q3+1.5\,IQR\).

## Bài 4 — Sampling and Hypothesis Testing

### English — Original Word requirement

- Randomly select 10 users.
- Calculate sample mean and compare it with mean of all 50 users.
- Test the company's claim that **population mean usage is 120 minutes/day**, using a **one-sample t-test** at `α = 0.05`.
- Based on p-value, decide whether to reject or fail to reject `H₀`.

### Tiếng Việt — Bản dịch

Chọn ngẫu nhiên 10 người dùng, tính trung bình của mẫu 10 và so sánh với trung bình 50 người. Kiểm định giả thuyết công ty rằng trung bình tổng thể là **120 phút/ngày** bằng one-sample t-test, mức ý nghĩa α=0,05. Dựa vào p-value quyết định bác bỏ hay chưa đủ bằng chứng bác bỏ H0.

### Bài giải — Trích code demo/giáo trình đã có

Nguồn: `labs/pythoclass/LAB-08-statistics/SOLUTION.py`, hàm `task04_sample_and_test()`. `DEMO.py` là code thực hành đối chiếu; đoạn trích bên dưới được ghi đúng xuất xứ là **lời giải tham khảo đã lưu**, không giả nhận demo giải đầy đủ bài.

```python
# Hàm task04_sample_and_test() lấy từ lời giải tham khảo hiện có.
def task04_sample_and_test(values):
    rng=np.random.default_rng(2026)
    sample=rng.choice(values,size=10,replace=False)
    result=stats.ttest_1samp(values,popmean=120.0)
    return sample,float(sample.mean()),float(result.statistic),float(result.pvalue)
```

### Giải thích quy trình giải và công thức

`default_rng(2026).choice(...,size=10,replace=False)` chọn 10 giá trị không lặp. Code kiểm định đã có gọi `ttest_1samp(values,popmean=120)`, tức dùng **toàn bộ 50 quan sát** cho phép kiểm định, còn mẫu 10 chỉ minh họa lấy mẫu. Đừng gọi nhầm t-test chỉ trên 10 quan sát. So sánh p-value với 0,05.

**Công thức / quy tắc liên quan:** \(H_0:\mu=120\), \(H_1:\mu\ne120\); \(t=(\bar x-120)/(s/\sqrt n)\). Nếu p<0,05: bác bỏ H0; nếu p≥0,05: chưa đủ bằng chứng bác bỏ, không khẳng định H0 đúng.

## Bài 5 — Conclusion

### English — Original Word requirement

Write a short conclusion (3–5 sentences) about:
- Typical daily app usage time.
- Variability and presence of outliers.
- Hypothesis-test result.
- One recommendation for the company.

### Tiếng Việt — Bản dịch

Viết kết luận ngắn 3–5 câu về mức sử dụng điển hình, độ biến thiên/ngoại lệ, kết quả kiểm định và một khuyến nghị cho công ty. Không mặc định dữ liệu mô phỏng là bằng chứng về toàn bộ người dùng thực.

### Bài giải — Trích code demo/giáo trình đã có

Nguồn: `labs/pythoclass/LAB-08-statistics/SOLUTION.py`, hàm `task05_conclusion()`. `DEMO.py` là code thực hành đối chiếu; đoạn trích bên dưới được ghi đúng xuất xứ là **lời giải tham khảo đã lưu**, không giả nhận demo giải đầy đủ bài.

```python
# Hàm task05_conclusion() lấy từ lời giải tham khảo hiện có.
def task05_conclusion(descriptive,outliers,pvalue):
    typical=descriptive["median"]
    decision="reject H0" if pvalue<0.05 else "fail to reject H0"
    print(f"Typical use is around median {typical:.1f} minutes/day.")
    print(f"Sample SD is {descriptive['sample_std']:.1f} minutes, with {len(outliers)} IQR outlier(s).")
    print(f"One-sample t-test vs 120 min/day: p={pvalue:.6g}; {decision} at alpha=0.05.")
    print("Recommendation: study long-duration sessions separately and design user-friendly break reminders.")
```

### Giải thích quy trình giải và công thức

Hàm `task05_conclusion` của code tham khảo in bốn ý: dùng median đại diện mức điển hình, SD và số điểm ngoại lệ để mô tả độ biến thiên, đọc p-value cho kiểm định, và đề xuất xem xét phiên dùng dài cùng lời nhắc nghỉ. Điều này đáp ứng 3–5 câu của đề.

**Công thức / quy tắc liên quan:** Kết luận được tạo từ các chỉ số đã tính ở 4 bài trước, không có công thức mới. 480 phút là dữ liệu nguồn, cần để thuật toán outlier đánh giá thay vì sửa số.

## Chạy và kiểm chứng bài giải đã học

Script tham khảo chạy `python SOLUTION.py --no-plot` từ `labs/pythoclass/LAB-08-statistics`, in kết quả thống kê, tần suất, 1.5×IQR, t và p-value. Nếu bỏ `--no-plot`, hàm `save_plot()` của code đã có lưu histogram. **Không thêm file output riêng** trong phần tài liệu Word giải đã xuất; tất cả nằm trong `LAB-08-statistics.md`.
