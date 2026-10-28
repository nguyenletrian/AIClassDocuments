# LAB-08-statistics — Đề Anh đầy đủ, đề Việt đầy đủ, hướng giải, toàn bộ code có note

**Nguồn:** Word đã chuyển sang `labs/pythoclass/LAB-08-statistics/LAB.md`; code trong `labs/pythoclass/LAB-08-statistics/SOLUTION.py` có đối chiếu `DEMO.py` và giáo trình. Dữ liệu, lời giải và thuật toán được kế thừa nguyên tắc từ code đã có; không nhận nhầm lời giải tham khảo là demo cá nhân. Một lab chỉ xuất **một file**.

---

## PART 1 — COMPLETE ORIGINAL ENGLISH ASSIGNMENT

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

---

## PHẦN 2 — BẢN DỊCH TIẾNG VIỆT TOÀN BỘ ĐỀ

# Bản dịch toàn bộ LAB LAB-08-statistics

Công ty ứng dụng di động phân tích thời gian sử dụng mỗi ngày của **50 người dùng**, tính bằng **phút/ngày**. Dữ liệu gốc giữ nguyên, gồm cả mốc 480 phút. Các bài cần dùng NumPy, Pandas, SciPy và Matplotlib.

## Dữ liệu 50 người (phút/ngày)

```python
usage_minutes = [
    35, 45, 50, 55, 60, 65, 70, 75, 80, 85,
    90, 95, 100, 105, 110, 115, 120, 120, 125, 130,
    135, 140, 145, 150, 155, 160, 165, 170, 175, 180,
    185, 190, 195, 200, 205, 210, 215, 220, 225, 230,
    240, 250, 260, 270, 280, 290, 300, 320, 350, 480
]
```

## Toàn bộ yêu cầu

### Bài 1

Từ 50 người dùng và số phút sử dụng ứng dụng mỗi ngày, tính trung bình (mean), trung vị (median), mốt (mode), nhỏ nhất, lớn nhất và khoảng biến thiên. Tính **phương sai mẫu** và **độ lệch chuẩn mẫu** (không dùng phương sai tổng thể).

### Bài 2

Chia thời gian dùng ứng dụng thành đúng 6 nhóm: 0–60, 60–120, 120–180, 180–240, 240–360, 360–500 phút/ngày. Dùng `pd.cut()` và `value_counts()` tạo bảng tần suất, `cumsum()` tính tần suất tích lũy, vẽ histogram có tiêu đề và nhãn trục. Quy định rõ dữ liệu nằm ở ranh giới 60/120/... được tính đúng một nhóm.

### Bài 3

Tính Q1, Q2, Q3 và IQR; xác định biên dưới và biên trên theo quy tắc `1.5 × IQR`, rồi liệt kê các thời gian nằm ngoài hai biên này.

### Bài 4

Chọn ngẫu nhiên 10 người dùng, tính trung bình của mẫu 10 và so sánh với trung bình 50 người. Kiểm định giả thuyết công ty rằng trung bình tổng thể là **120 phút/ngày** bằng one-sample t-test, mức ý nghĩa α=0,05. Dựa vào p-value quyết định bác bỏ hay chưa đủ bằng chứng bác bỏ H0.

### Bài 5

Viết kết luận ngắn 3–5 câu về mức sử dụng điển hình, độ biến thiên/ngoại lệ, kết quả kiểm định và một khuyến nghị cho công ty. Không mặc định dữ liệu mô phỏng là bằng chứng về toàn bộ người dùng thực.

**Bảng nhóm tần suất từ Word:** 0–60, 60–120, 120–180, 180–240, 240–360, 360–500 phút/ngày (6 nhóm).

---

## Quy trình giải chi tiết và các công thức liên quan

**Phương pháp chung:** Đọc điều kiện và số liệu đúng từ Word → biểu diễn bằng cấu trúc/mảng NumPy/Pandas → chạy hàm tính toán hay mô phỏng đã học → kiểm tra kết quả lý thuyết và trường hợp đặc biệt → trình bày bằng số và biểu đồ. Đây là lời giải đã có trong repo, không thay đổi thuật toán khi viết giáo trình.

### Bài 1 — Quy trình và công thức

Dữ liệu 50 dòng được đưa nguyên vào `USAGE_MINUTES`. Dùng NumPy/Pandas tính các chỉ số; dùng `ddof=1` để phương sai chia cho n−1 chứ không phải n. Mode được lấy bằng `.mode().iloc[0]`.

**Công thức / quy tắc liên quan:** Trung bình = (tổng 50 số phút)/50; range = max−min; phương sai mẫu \(s^2=\frac{1}{n-1}\sum_i(x_i-\bar x)^2\); độ lệch chuẩn mẫu \(s=\sqrt{s^2}\).

**Công thức/đối chiếu:** mean=Σx/n; range=max−min; phương sai mẫu s²=Σ(x−mean)²/(n−1), SD=√s²; dùng ddof=1.

### Bài 2 — Quy trình và công thức

Các khoảng liên tiếp trong `bins=[0,60,120,180,240,360,500]`, `right=False` nghĩa là [0,60), [60,120),… Tránh một phút đúng 60 hoặc 120 bị tính hai lần. Lấy tần số của từng khoảng rồi cộng dồn; hình histogram dùng chức năng `save_plot` đã có.

**Công thức / quy tắc liên quan:** Tần suất lớp i = số quan sát thuộc lớp i; tần suất tích lũy ở lớp k = tổng tần suất của các lớp 1..k. Tổng tần số phải bằng 50.

**Công thức/đối chiếu:** Sáu nhóm: [0,60),[60,120),[120,180),[180,240),[240,360),[360,500). Tần suất tích lũy ở lớp i bằng tổng các tần số lớp 1..i.

### Bài 3 — Quy trình và công thức

`np.percentile` lấy ba phân vị, dùng IQR làm thước đo độ trải rộng ít nhạy với ngoại lệ. Các điểm nhỏ hơn biên dưới hoặc lớn hơn biên trên được đánh dấu, không tự động xóa.

**Công thức / quy tắc liên quan:** \(IQR=Q3-Q1\); biên dưới \(Q1-1.5\,IQR\); biên trên \(Q3+1.5\,IQR\).

**Công thức/đối chiếu:** IQR=Q3−Q1; biên dưới Q1−1,5×IQR, biên trên Q3+1,5×IQR; giữ các giá trị ngoại lệ để kiểm tra.

### Bài 4 — Quy trình và công thức

`default_rng(2026).choice(...,size=10,replace=False)` chọn 10 giá trị không lặp. Code kiểm định đã có gọi `ttest_1samp(values,popmean=120)`, tức dùng **toàn bộ 50 quan sát** cho phép kiểm định, còn mẫu 10 chỉ minh họa lấy mẫu. Đừng gọi nhầm t-test chỉ trên 10 quan sát. So sánh p-value với 0,05.

**Công thức / quy tắc liên quan:** \(H_0:\mu=120\), \(H_1:\mu\ne120\); \(t=(\bar x-120)/(s/\sqrt n)\). Nếu p<0,05: bác bỏ H0; nếu p≥0,05: chưa đủ bằng chứng bác bỏ, không khẳng định H0 đúng.

**Công thức/đối chiếu:** 10 người được chọn không hoàn lại, nhưng t-test trong code nguồn chạy **trên toàn bộ 50 giá trị**. H0: μ=120; H1: μ≠120; t=(mean−120)/(s/√n); α=0,05.

### Bài 5 — Quy trình và công thức

Hàm `task05_conclusion` của code tham khảo in bốn ý: dùng median đại diện mức điển hình, SD và số điểm ngoại lệ để mô tả độ biến thiên, đọc p-value cho kiểm định, và đề xuất xem xét phiên dùng dài cùng lời nhắc nghỉ. Điều này đáp ứng 3–5 câu của đề.

**Công thức / quy tắc liên quan:** Kết luận được tạo từ các chỉ số đã tính ở 4 bài trước, không có công thức mới. 480 phút là dữ liệu nguồn, cần để thuật toán outlier đánh giá thay vì sửa số.

**Công thức/đối chiếu:** Kết luận 3–5 câu: median, độ lệch chuẩn và ngoại lệ, p-value/t-test, một khuyến nghị. p≥0,05 nghĩa là chưa đủ bằng chứng bác bỏ H0.

---

## PHẦN 4 — TOÀN BỘ CODE PYTHON CÙNG CHÚ THÍCH

Sao chép toàn bộ khối sau vào `lab_solution.py`; cài thư viện như yêu cầu bài (`numpy`, `scipy`, `matplotlib`, `pandas`). Chạy `python lab_solution.py --no-plot` để xem kết quả trên terminal; chạy không có `--no-plot` để tạo hình bằng code đã có. Chú thích được thêm vào các hàm, quy trình và câu lệnh quan trọng, **không đổi logic**.

```python
"""LAB SESSION 8 — descriptive statistics, 6 bins, IQR, sample and t-test."""
from pathlib import Path
import sys
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

# Thống kê trung bình, trung vị, mốt và phương sai/SD mẫu.
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

# Chia số phút thành sáu khoảng không chồng biên.
def task02_frequency(values):
    # Half-open bins [0,60), [60,120), ... so boundary values count exactly once.
    bins=[0,60,120,180,240,360,500]
    labels=["0–<60","60–<120","120–<180","180–<240","240–<360","360–<500"]
    # Phân loại mỗi phút vào đúng một nhóm, không đếm hai lần ở ranh giới.
    groups=pd.cut(values,bins=bins,labels=labels,right=False,include_lowest=True)
    freq=pd.Series(groups).value_counts(sort=False)
    frame=pd.DataFrame({"frequency":freq})
    frame["cumulative"]=frame["frequency"].cumsum()
    assert frame["frequency"].sum()==len(values)
    return bins,frame

# Dùng phân vị Q1/Q3 và quy tắc 1.5×IQR.
def task03_outliers(values):
    # Tính ba phân vị trước khi lập IQR.
    q1,q2,q3=np.percentile(values,[25,50,75])
    iqr=q3-q1
    low,high=q1-1.5*iqr,q3+1.5*iqr
    unusual=values[(values<low)|(values>high)]
    return q1,q2,q3,iqr,low,high,unusual

# Lấy 10 mẫu minh họa và kiểm định t với đủ 50 số.
def task04_sample_and_test(values):
    # Cố định seed để chạy lại được cùng chuỗi ngẫu nhiên.
    rng=np.random.default_rng(2026)
    sample=rng.choice(values,size=10,replace=False)
    # T-test thực hiện trên 50 số liệu đầu vào.
    result=stats.ttest_1samp(values,popmean=120.0)
    return sample,float(sample.mean()),float(result.statistic),float(result.pvalue)

# In bốn ý kết luận theo đúng kết quả thống kê.
def task05_conclusion(descriptive,outliers,pvalue):
    typical=descriptive["median"]
    decision="reject H0" if pvalue<0.05 else "fail to reject H0"
    print(f"Typical use is around median {typical:.1f} minutes/day.")
    print(f"Sample SD is {descriptive['sample_std']:.1f} minutes, with {len(outliers)} IQR outlier(s).")
    print(f"One-sample t-test vs 120 min/day: p={pvalue:.6g}; {decision} at alpha=0.05.")
    print("Recommendation: study long-duration sessions separately and design user-friendly break reminders.")

# Vẽ histogram theo sáu bin từ bảng đề gốc.
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

# Chạy năm yêu cầu, khẳng định kích thước dữ liệu và p-value.
def main():
    assert USAGE_MINUTES.shape==(50,)
    desc=task01_descriptive(USAGE_MINUTES)
    bins,freq=task02_frequency(USAGE_MINUTES)
    q1,q2,q3,iqr,lo,hi,outliers=task03_outliers(USAGE_MINUTES)
    sample,sample_mean,t,p=task04_sample_and_test(USAGE_MINUTES)
    assert len(sample)==10
    assert 0<=p<=1
    print("Descriptive:",desc)
    print("Frequency:\n",freq.to_string())
    print(f"Q1={q1:.2f}, Q2={q2:.2f}, Q3={q3:.2f}, IQR={iqr:.2f}")
    print(f"Outlier limits [{lo:.2f},{hi:.2f}], values:",outliers.tolist())
    print("Sample of 10:",sample.tolist(),"sample mean:",round(sample_mean,2))
    print("t:",round(t,4),"p:",round(p,6))
    task05_conclusion(desc,outliers,p)
    if "--no-plot" not in sys.argv:
        save_plot(USAGE_MINUTES,bins)
if __name__=="__main__":
    main()
```
