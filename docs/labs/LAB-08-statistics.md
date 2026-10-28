# LAB-08-statistics — Đề Anh đầy đủ, đề Việt đầy đủ, hướng giải, toàn bộ code có note

**Nguồn:** Word đã chuyển sang `labs/pythoclass/LAB-08-statistics/LAB.md`; code trong `labs/pythoclass/LAB-08-statistics/SOLUTION.py` có đối chiếu `DEMO.py` và giáo trình. Dữ liệu, lời giải và thuật toán được kế thừa nguyên tắc từ code đã có; không nhận nhầm lời giải tham khảo là demo cá nhân. Một lab chỉ xuất **một file**.

---

## ĐỀ BÀI SONG NGỮ — MỖI CÂU ENGLISH / TIẾNG VIỆT / GIẢI THÍCH

**Cách học:** Đọc yêu cầu tiếng Anh (English: tiếng Anh), xem bản dịch tiếng Việt ngay bên dưới, rồi tới giải thích/công thức. Các thuật ngữ quan trọng có nghĩa tiếng Việt trong ngoặc.

### Bối cảnh và dữ liệu — Original English

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

### Bối cảnh và dữ liệu — Tiếng Việt

# Bản dịch toàn bộ LAB LAB-08-statistics

Công ty ứng dụng di động phân tích thời gian sử dụng mỗi ngày của **50 người dùng**, tính bằng **phút/ngày**. Dữ liệu gốc giữ nguyên, gồm cả mốc 480 phút. Các bài cần dùng NumPy (thư viện tính toán mảng), Pandas (thư viện bảng dữ liệu), SciPy (thư viện tính toán khoa học) và Matplotlib (thư viện vẽ biểu đồ).

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

### Câu 1 — English → Tiếng Việt → Giải thích

**English — Nguyên đề:**

**Task 1 – Descriptive Statistics**
- Calculate mean, median, and mode.
- Find min, max, and range.
- Calculate **sample** variance and **sample** standard deviation.

**Tiếng Việt — Dịch ngay dưới đề Anh:**

**Bài 1**

Từ 50 người dùng và số phút sử dụng ứng dụng mỗi ngày, tính trung bình (mean (trung bình)), trung vị (median (trung vị)), mốt (mode (mốt)), nhỏ nhất, lớn nhất và khoảng biến thiên. Tính **phương sai mẫu** và **độ lệch chuẩn mẫu** (không dùng phương sai tổng thể).

**Giải thích từng bước và công thức:**

Dữ liệu 50 dòng được đưa nguyên vào `USAGE_MINUTES`. Dùng NumPy (thư viện tính toán mảng)/Pandas (thư viện bảng dữ liệu) tính các chỉ số; dùng `ddof=1` để phương sai chia cho n−1 chứ không phải n. Mode (mốt) được lấy bằng `.mode().iloc[0]`.

**Công thức / quy tắc liên quan:** Trung bình = (tổng 50 số phút)/50; range = max−min; phương sai mẫu \(s^2=\frac{1}{n-1}\sum_i(x_i-\bar x)^2\); độ lệch chuẩn mẫu \(s=\sqrt{s^2}\).

**Công thức/đối chiếu:** mean (trung bình)=Σx/n; range=max−min; phương sai mẫu s²=Σ(x−mean)²/(n−1), SD=√s²; dùng ddof=1.

**Ví dụ/lỗi thường gặp:** Giữ đủ 50 số phút, kể cả 480. Phương sai và độ lệch chuẩn **mẫu** chia cho n−1 (ddof=1), không chia n như tổng thể.

**Từ vựng chính:** Descriptive statistics (thống kê mô tả).

### Câu 2 — English → Tiếng Việt → Giải thích

**English — Nguyên đề:**

**Task 2 – Frequency Distribution and Histogram**
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

**Tiếng Việt — Dịch ngay dưới đề Anh:**

**Bài 2**

Chia thời gian dùng ứng dụng thành đúng 6 nhóm: 0–60, 60–120, 120–180, 180–240, 240–360, 360–500 phút/ngày. Dùng `pd.cut()` và `value_counts()` tạo bảng tần suất, `cumsum()` tính tần suất tích lũy, vẽ histogram (biểu đồ tần suất) có tiêu đề và nhãn trục. Quy định rõ dữ liệu nằm ở ranh giới 60/120/... được tính đúng một nhóm.

**Giải thích từng bước và công thức:**

Các khoảng liên tiếp trong `bins=[0,60,120,180,240,360,500]`, `right=False` nghĩa là [0,60), [60,120),… Tránh một phút đúng 60 hoặc 120 bị tính hai lần. Lấy tần số của từng khoảng rồi cộng dồn; hình histogram (biểu đồ tần suất) dùng chức năng `save_plot` đã có.

**Công thức / quy tắc liên quan:** Tần suất lớp i = số quan sát thuộc lớp i; tần suất tích lũy ở lớp k = tổng tần suất của các lớp 1..k. Tổng tần số phải bằng 50.

**Công thức/đối chiếu:** Sáu nhóm: [0,60),[60,120),[120,180),[180,240),[240,360),[360,500). Tần suất tích lũy ở lớp i bằng tổng các tần số lớp 1..i.

**Ví dụ/lỗi thường gặp:** Nhóm khoảng theo [0,60), [60,120)... để số 60 không bị đếm hai lần. Tổng tần số phải bằng 50.

**Từ vựng chính:** Histogram (biểu đồ tần suất).

### Câu 3 — English → Tiếng Việt → Giải thích

**English — Nguyên đề:**

**Task 3 – Quartiles and Outlier Detection**
- Calculate Q1, Q2, Q3 and IQR.
- Calculate lower and upper bounds using **1.5 × IQR**.
- Identify usage times outside the bounds.

**Tiếng Việt — Dịch ngay dưới đề Anh:**

**Bài 3**

Tính Q1, Q2, Q3 và IQR; xác định biên dưới và biên trên theo quy tắc `1.5 × IQR`, rồi liệt kê các thời gian nằm ngoài hai biên này.

**Giải thích từng bước và công thức:**

`np.percentile` lấy ba phân vị, dùng IQR làm thước đo độ trải rộng ít nhạy với ngoại lệ. Các điểm nhỏ hơn biên dưới hoặc lớn hơn biên trên được đánh dấu, không tự động xóa.

**Công thức / quy tắc liên quan:** \(IQR=Q3-Q1\); biên dưới \(Q1-1.5\,IQR\); biên trên \(Q3+1.5\,IQR\).

**Công thức/đối chiếu:** IQR=Q3−Q1; biên dưới Q1−1,5×IQR, biên trên Q3+1,5×IQR; giữ các giá trị ngoại lệ để kiểm tra.

**Ví dụ/lỗi thường gặp:** IQR=Q3−Q1; biên dưới=Q1−1,5×IQR và biên trên=Q3+1,5×IQR. Không tự xóa ngoại lệ trước khi tính.

**Từ vựng chính:** Quartiles (tứ phân vị).

### Câu 4 — English → Tiếng Việt → Giải thích

**English — Nguyên đề:**

**Task 4 – Sampling and Hypothesis Testing**
- Randomly select 10 users.
- Calculate sample mean and compare it with mean of all 50 users.
- Test the company's claim that **population mean usage is 120 minutes/day**, using a **one-sample t-test** at `α = 0.05`.
- Based on p-value, decide whether to reject or fail to reject `H₀`.

**Tiếng Việt — Dịch ngay dưới đề Anh:**

**Bài 4**

Chọn ngẫu nhiên 10 người dùng, tính trung bình của mẫu 10 và so sánh với trung bình 50 người. Kiểm định giả thuyết công ty rằng trung bình tổng thể là **120 phút/ngày** bằng one-sample (mẫu) t-test, mức ý nghĩa α=0,05. Dựa vào p-value (giá trị xác suất kiểm định) quyết định bác bỏ hay chưa đủ bằng chứng bác bỏ H0.

**Giải thích từng bước và công thức:**

`default_rng(2026).choice(...,size=10,replace=False)` chọn 10 giá trị không lặp. Code kiểm định đã có gọi `ttest_1samp(values,popmean=120)`, tức dùng **toàn bộ 50 quan sát** cho phép kiểm định, còn mẫu 10 chỉ minh họa lấy mẫu. Đừng gọi nhầm t-test chỉ trên 10 quan sát. So sánh p-value (giá trị xác suất kiểm định) với 0,05.

**Công thức / quy tắc liên quan:** \(H_0:\mu=120\), \(H_1:\mu\ne120\); \(t=(\bar x-120)/(s/\sqrt n)\). Nếu p<0,05: bác bỏ H0; nếu p≥0,05: chưa đủ bằng chứng bác bỏ, không khẳng định H0 đúng.

**Công thức/đối chiếu:** 10 người được chọn không hoàn lại, nhưng t-test trong code nguồn chạy **trên toàn bộ 50 giá trị**. H0: μ=120; H1: μ≠120; t=(mean (trung bình)−120)/(s/√n); α=0,05.

**Ví dụ/lỗi thường gặp:** Lấy 10 mẫu không hoàn lại, nhưng t-test trong code nguồn dùng 50 quan sát. So sánh p-value (giá trị xác suất kiểm định) với 0,05 trước khi kết luận.

**Từ vựng chính:** Hypothesis testing (kiểm định giả thuyết).

### Câu 5 — English → Tiếng Việt → Giải thích

**English — Nguyên đề:**

**Task 5 – Conclusion**
Write a short conclusion (3–5 sentences) about:
- Typical daily app usage time.
- Variability and presence of outliers.
- Hypothesis-test result.
- One recommendation for the company.

**Tiếng Việt — Dịch ngay dưới đề Anh:**

**Bài 5**

Viết kết luận ngắn 3–5 câu về mức sử dụng điển hình, độ biến thiên/ngoại lệ, kết quả kiểm định và một khuyến nghị cho công ty. Không mặc định dữ liệu mô phỏng là bằng chứng về toàn bộ người dùng thực.

**Bảng nhóm tần suất từ Word:** 0–60, 60–120, 120–180, 180–240, 240–360, 360–500 phút/ngày (6 nhóm).

**Giải thích từng bước và công thức:**

Hàm `task05_conclusion` của code tham khảo in bốn ý: dùng median (trung vị) đại diện mức điển hình, SD và số điểm ngoại lệ để mô tả độ biến thiên, đọc p-value (giá trị xác suất kiểm định) cho kiểm định, và đề xuất xem xét phiên dùng dài cùng lời nhắc nghỉ. Điều này đáp ứng 3–5 câu của đề.

**Công thức / quy tắc liên quan:** Kết luận được tạo từ các chỉ số đã tính ở 4 bài trước, không có công thức mới. 480 phút là dữ liệu nguồn, cần để thuật toán outlier (ngoại lệ) đánh giá thay vì sửa số.

**Công thức/đối chiếu:** Kết luận 3–5 câu: median, độ lệch chuẩn và ngoại lệ, p-value/t-test, một khuyến nghị. p≥0,05 nghĩa là chưa đủ bằng chứng bác bỏ H0.

**Ví dụ/lỗi thường gặp:** Đối chiếu median (trung vị), SD, ngoại lệ và kiểm định khi viết 3–5 câu. Không suy rộng số liệu mô phỏng thành kết luận cho mọi người dùng.

**Từ vựng chính:** Conclusion (kết luận).

---

## TOÀN BỘ CODE PYTHON — CHÚ THÍCH NGAY SAU TỪNG DÒNG

**Hướng dẫn:** Chú thích nằm cùng dòng, sau câu lệnh và dấu `#`; không đặt comment riêng trên dòng phía trước. Các câu lệnh kiểm tra dùng `if` (nếu) và `raise ValueError` (báo lỗi dữ liệu), không dùng `assert`. Thuật toán và số liệu giữ như code đã học, các dòng trắng chỉ chia nhóm lệnh.

```python
from pathlib import Path  # Nạp thư viện (import: nạp vào) để có các hàm đã học.
import sys  # Nạp thư viện (import: nạp vào) để có các hàm đã học.
import numpy as np  # Nạp thư viện (import: nạp vào) để có các hàm đã học.
import pandas as pd  # Nạp thư viện (import: nạp vào) để có các hàm đã học.
from scipy import stats  # Nạp thư viện (import: nạp vào) để có các hàm đã học.

USAGE_MINUTES=np.array([  # Khởi tạo mảng NumPy với số liệu theo đúng đề.
    35,45,50,55,60,65,70,75,80,85,  # Giữ nguyên giá trị số trong dữ liệu đề bài.
    90,95,100,105,110,115,120,120,125,130,  # Giữ nguyên giá trị số trong dữ liệu đề bài.
    135,140,145,150,155,160,165,170,175,180,  # Giữ nguyên giá trị số trong dữ liệu đề bài.
    185,190,195,200,205,210,215,220,225,230,  # Giữ nguyên giá trị số trong dữ liệu đề bài.
    240,250,260,270,280,290,300,320,350,480  # Giữ nguyên giá trị số trong dữ liệu đề bài.
],dtype=float)  # Đóng mảng, danh sách hoặc nhóm tham số.

def task01_descriptive(values):  # Định nghĩa hàm (function: hàm) để gom và gọi lại các bước.
    return {  # Trả kết quả (return: trả về) cho nơi gọi hàm.
        "mean":float(values.mean()),"median":float(np.median(values)),  # Gắn khóa (key: tên trường) với giá trị trong từ điển.
        "mode":float(pd.Series(values).mode().iloc[0]),  # Gắn khóa (key: tên trường) với giá trị trong từ điển.
        "minimum":float(values.min()),"maximum":float(values.max()),  # Gắn khóa (key: tên trường) với giá trị trong từ điển.
        "range":float(np.ptp(values)),  # Gắn khóa (key: tên trường) với giá trị trong từ điển.
        "sample_variance":float(values.var(ddof=1)),  # Gắn khóa (key: tên trường) với giá trị trong từ điển.
        "sample_std":float(values.std(ddof=1)),  # Gắn khóa (key: tên trường) với giá trị trong từ điển.
    }  # Đóng mảng, danh sách hoặc nhóm tham số.

def task02_frequency(values):  # Định nghĩa hàm (function: hàm) để gom và gọi lại các bước.
    bins=[0,60,120,180,240,360,500]  # Tính hoặc cập nhật biến bins từ công thức bên phải.
    labels=["0–<60","60–<120","120–<180","180–<240","240–<360","360–<500"]  # Tính hoặc cập nhật biến labels từ công thức bên phải.
    groups=pd.cut(values,bins=bins,labels=labels,right=False,include_lowest=True)  # Tính hoặc cập nhật biến groups từ công thức bên phải.
    freq=pd.Series(groups).value_counts(sort=False)  # Tính hoặc cập nhật biến freq từ công thức bên phải.
    frame=pd.DataFrame({"frequency":freq})  # Tính hoặc cập nhật biến frame từ công thức bên phải.
    frame["cumulative"]=frame["frequency"].cumsum()  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
    if not (frame["frequency"].sum()==len(values)): raise ValueError("Kiểm tra không đạt")  # Kiểm tra bằng if (nếu), báo lỗi nếu kết quả không phù hợp.
    return bins,frame  # Trả kết quả (return: trả về) cho nơi gọi hàm.

def task03_outliers(values):  # Định nghĩa hàm (function: hàm) để gom và gọi lại các bước.
    q1,q2,q3=np.percentile(values,[25,50,75])  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
    iqr=q3-q1  # Tính hoặc cập nhật biến iqr từ công thức bên phải.
    low,high=q1-1.5*iqr,q3+1.5*iqr  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
    unusual=values[(values<low)|(values>high)]  # Tính hoặc cập nhật biến unusual từ công thức bên phải.
    return q1,q2,q3,iqr,low,high,unusual  # Trả kết quả (return: trả về) cho nơi gọi hàm.

def task04_sample_and_test(values):  # Định nghĩa hàm (function: hàm) để gom và gọi lại các bước.
    rng=np.random.default_rng(2026)  # Rút mẫu ngẫu nhiên; seed (hạt giống) giúp tái lập.
    sample=rng.choice(values,size=10,replace=False)  # Rút mẫu ngẫu nhiên; seed (hạt giống) giúp tái lập.
    result=stats.ttest_1samp(values,popmean=120.0)  # Tính thống kê theo hàm/tham số đã học.
    return sample,float(sample.mean()),float(result.statistic),float(result.pvalue)  # Trả kết quả (return: trả về) cho nơi gọi hàm.

def task05_conclusion(descriptive,outliers,pvalue):  # Định nghĩa hàm (function: hàm) để gom và gọi lại các bước.
    typical=descriptive["median"]  # Tính hoặc cập nhật biến typical từ công thức bên phải.
    decision="reject H0" if pvalue<0.05 else "fail to reject H0"  # Tính hoặc cập nhật biến decision từ công thức bên phải.
    print(f"Typical use is around median {typical:.1f} minutes/day.")  # In kết quả (output: kết quả) để đối chiếu với đề.
    print(f"Sample SD is {descriptive['sample_std']:.1f} minutes, with {len(outliers)} IQR outlier(s).")  # In kết quả (output: kết quả) để đối chiếu với đề.
    print(f"One-sample t-test vs 120 min/day: p={pvalue:.6g}; {decision} at alpha=0.05.")  # In kết quả (output: kết quả) để đối chiếu với đề.
    print("Recommendation: study long-duration sessions separately and design user-friendly break reminders.")  # In kết quả (output: kết quả) để đối chiếu với đề.

def save_plot(values,bins):  # Định nghĩa hàm (function: hàm) để gom và gọi lại các bước.
    import matplotlib  # Nạp thư viện (import: nạp vào) để có các hàm đã học.
    matplotlib.use("Agg")  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
    import matplotlib.pyplot as plt  # Nạp thư viện (import: nạp vào) để có các hàm đã học.
    output=Path(__file__).resolve().parent/"outputs"  # Tính hoặc cập nhật biến output từ công thức bên phải.
    output.mkdir(exist_ok=True)  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
    fig,ax=plt.subplots()  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
    ax.hist(values,bins=bins,edgecolor="black")  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
    ax.set(xlabel="Daily app usage (minutes)",ylabel="Users",title="Daily usage of 50 users")  # Đặt nhãn, lưới hoặc chú giải cho biểu đồ.
    ax.grid(True,axis="y")  # Đặt nhãn, lưới hoặc chú giải cho biểu đồ.
    target=output/"usage_histogram.png"  # Tính hoặc cập nhật biến target từ công thức bên phải.
    fig.savefig(target,dpi=140,bbox_inches="tight")  # Vẽ/lưu biểu đồ (plot: đồ thị) để diễn giải kết quả.
    plt.close(fig)  # Đóng biểu đồ để tránh giữ tài nguyên.
    print("Saved:",target)  # In kết quả (output: kết quả) để đối chiếu với đề.

def main():  # Định nghĩa hàm (function: hàm) để gom và gọi lại các bước.
    if not (USAGE_MINUTES.shape==(50,)): raise ValueError("Kiểm tra không đạt")  # Kiểm tra bằng if (nếu), báo lỗi nếu kết quả không phù hợp.
    desc=task01_descriptive(USAGE_MINUTES)  # Tính hoặc cập nhật biến desc từ công thức bên phải.
    bins,freq=task02_frequency(USAGE_MINUTES)  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
    q1,q2,q3,iqr,lo,hi,outliers=task03_outliers(USAGE_MINUTES)  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
    sample,sample_mean,t,p=task04_sample_and_test(USAGE_MINUTES)  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
    if not (len(sample)==10): raise ValueError("Kiểm tra không đạt")  # Kiểm tra bằng if (nếu), báo lỗi nếu kết quả không phù hợp.
    if not (0<=p<=1): raise ValueError("Kiểm tra không đạt")  # Kiểm tra bằng if (nếu), báo lỗi nếu kết quả không phù hợp.
    print("Descriptive:",desc)  # In kết quả (output: kết quả) để đối chiếu với đề.
    print("Frequency:\n",freq.to_string())  # In kết quả (output: kết quả) để đối chiếu với đề.
    print(f"Q1={q1:.2f}, Q2={q2:.2f}, Q3={q3:.2f}, IQR={iqr:.2f}")  # In kết quả (output: kết quả) để đối chiếu với đề.
    print(f"Outlier limits [{lo:.2f},{hi:.2f}], values:",outliers.tolist())  # In kết quả (output: kết quả) để đối chiếu với đề.
    print("Sample of 10:",sample.tolist(),"sample mean:",round(sample_mean,2))  # In kết quả (output: kết quả) để đối chiếu với đề.
    print("t:",round(t,4),"p:",round(p,6))  # In kết quả (output: kết quả) để đối chiếu với đề.
    task05_conclusion(desc,outliers,p)  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
    if "--no-plot" not in sys.argv:  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
        save_plot(USAGE_MINUTES,bins)  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
if __name__=="__main__":  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
    main()  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
```
