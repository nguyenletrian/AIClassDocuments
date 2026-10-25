# coding: utf-8
# DEMO.py — original student practice code aligned with LAB-08-statistics.
# Source: nguyenletrian/PythoClass (private). This is notebook/code provenance, NOT a complete tested solution.
# Read and run sections independently; interactive cells and exploratory snippets may not run sequentially.
# Original example student names (if present) are anonymized before entering the public destination.


# ========= BEGIN SOURCE: MON 2/2026-10-23.ipynb =========

# === Notebook cell 1 ===
""" 
THỐNG KẾ
- Thống kê mô tả
- Lấy mẫu, định lý giới hạn trung tâm
- Kiểm định lý thuyết
- khoảng tin cậy

Thống kê trong học máy là việc nghiên cứu, thu thập, phân tích, diễn giải dự liệu
giúp biết được độ biến động dữ liệu


Thống kê miêu tả:
....
mean: Trung bình
Trung vị 
Phân phối tần suất,
Tứ phương vị: Đo độ phân tán
Các đơn vị đo lường:
    range(max- min)
    variance: phương sai| đo lường mức độ phân tán của một tập dữ liệu
        phương nhỏ thì hầu hết dữ liệu gần trung bình
        lớn thì phân tán nhiều, xa trung bình
        polualtion variance, sample variance
    Độ lệch chuẩn bằng căng bậc 2 của phương sai
    
    



Thống kê suy diễn:



"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# THỐNG KÊ MIÊU TẢ:
# Khởi tạo dữ liệu điểm thi của 20 sinh viên
raw_scores = [40,45,80,83,50,55,89,100,5,60,88,70,54,58,87,88,70,54,58,70]
raw = sorted(raw_scores)
print("raw_scores: ",raw)

#Chuyển đổi danh sách này thành cấu trúc bảng
df = pd.DataFrame({"ExamScore":raw}) # Thông qua Dataframe để tính min max cho dễ

# Trích xuất riêng cột "ExamScore" ra để tiện tính toán
scores = df["ExamScore"]

print("Diem cua 20 sv la:",scores.tolist())

# Thống kế mô tả: Tìm mean, mode, median, min, max, range, variance, standard deviation
print("Mean: ",scores.mean())
print("Mode: ",scores.mode().tolist())
print("Min: ",scores.min())
print("Max:",scores.max())
print("Median: ",scores.median())
print("Range: ",scores.max() - scores.min())
print("Phuong sai: ",scores.var(ddof=1))
print("Do lech chuan: ",scores.std(ddof=1))

# Bản tuần suất và tần xuất tích luỹ

# Định nghĩa các vách ngăn (bin) để chia trục điểm từ 0 đến 100 thành 6 khoảng đều nhau
bins = [0,40,60,70,80,90,100]

# Đặt tên nhãn (labels) tương ứng để hiển thị cho 6 khoảng điểm trên
labels = ["0-40","40-60","60-70","70-80","80-90","90-100"]

# Dùng hàm pd.cut() để tự động xếp các điểm số vào các ô tương ứng
df["ScoreGroup"] = pd.cut(df["ExamScore"],bins=bins,labels=labels,include_lowest=True)
print("Bảng phân phối tần xuất")
print(df["ScoreGroup"].value_counts(sort=False))

# Tần xuất tích luỹ (Cumulative)
print("Bảng phân phối tần xuất tích luỹ")
print(df["ScoreGroup"].value_counts(sort=False).cumsum())


print("------------------------")
# tim tu phan vi & diem ngoai lai(IQR va Outliers)

# tinh moc tu phan vi thu nhat Q1 (25% sv co diem duoi' moc' nay)
Q1 = scores.quantile(0.25)

# tinh moc tu phan vi thu hai Q2
Q2 = scores.quantile(0.5)

# tinh moc tu phan vi thu hai Q3
Q3 = scores.quantile(0.75)

# khoang tu phan vi IQR: do do phan tan cua 50% luong du lieu o khuc giua
IQR = Q3 - Q1

# tinh ranh gioi de phat hien diem thap bat thuong
lower_bound = Q1 - 1.5*IQR

# tinh ranh gioi de phat hien diem cao bat thuong
upper_bound = Q3 + 1.5*IQR

# tim cac diem ngoai lai
outliers = df[(df["ExamScore"] < lower_bound) | (df["ExamScore"] > upper_bound)]

print("Q1: ", Q1)
print("Q2: ", Q2)
print("Q3: ", Q3)
print("IQR: ", IQR)
print("lower_bound: ", lower_bound)
print("upper_bound: ", upper_bound)
print("So luong diem ngoai lai: ", len(outliers))



print("--------------------------")
# Skewness: Đo lường độ lệch, hướng của tần xuất có đối xứng hay ko?
# Độ lệch dương, độ lệch âm
print("Do lech: ",scores.skew())# Độ lệch
print("Do nhon: ",scores.kurt())# Độ nhọn

# Trực quan hoá
plt.figure()

# Vẽ đồ thị histogram: Dùng để xem phân bổ tần xuất
plt.hist(scores,bins = bins)
# Hiển thị các cột mốc bin
plt.xticks(bins)

plt.title("Bieu do Histogram phan phoi diem thi")
plt.ylabel("So luong hoc sinh (Tan suat)")

plt.grid()
plt.show()



"""
Sampling    
Phương pháp lấy mẫu: Phướng pháp lấy mẫu ngẫu nhiên, hỗ hợp, hệ thống, cụm
Phương lấy mẫu phi xác xuất:
    -lấy mẫu theo
    -Lấy mẫu theo thuận tiện
    -Lây mâu theo mục đích
    -Lấy mẫu theo phương pháp quả cầu tuyết snowball

Định lý giới hạn trung tâm: Central limit theorem, mẫu > 30

"""
np.random.seed(42)
print("------")
# Sampling và central limit theorem

# Khởi tạo kích thước của tổng thế
poluation_size = 5000

# Khởi tạo dữ liệu tổng thể (dữ liệuy bị lệch nặng)
scores_raw = np.random.exponential(scale=15,size = poluation_size)

# Ép dữ liệu về tối thiểu là 0 và tối đa là 100
scores = np.clip(scores_raw,0,100)

# Tạo số giờ học ngẫu nhiên (phân bố đều)
study_hours = np.random.uniform(1,20,poluation_size)

# Tạo DataFrame từ điểm thi, số giờ học
df = pd.DataFrame({
    "ExamScore":scores,
    "StydyHours":study_hours
})

# Lấy ngẫu nhiên 1 mấu gồm 10 sinh viên (mẫu nhỏ)
sample = df.sample(n=10,random_state=42)
print(sample[["ExamScore","StydyHours"]])
print(f"Mean of Sample: {sample["ExamScore"].mean():.2f}")
print(f"Mean of population: {df["ExamScore"].mean():.2f}")


# Áp dụng định lý giới hạn trung trâm
sample_size = 40 # Nên chọn n > 30 để thoả mãn điều kiện của CLT, các mẫu phải độc lập với nhau

num_loop = 1000 # lấy 1 ngàn lần, các mẫu độc lập với nmhau

# Khởi tạo 1 danh sách rỗng để chứa kết quả trung bình của từng mẫu
sample_mean_list = []

# Chạy vòng lặp 1000 lần đối với 1000 mẫu
for i in range(num_loop):
    # Rút ngẫu nhiên n = 40 sinh viên từ tổng thể
    sample_scores = np.random.choice(scores,size=sample_size,replace=True)
    # Tính giá trị trung bình của mẫu vừa chọn
    current_mean = sample_scores.mean()
    # Thêm giá trị trung bình này vào ds để gom kết quả
    sample_mean_list.append(current_mean)

# Chuyển danh sách list sang thành dạng numpy để tính toán
sample_mean = np.array(sample_mean_list)


# Đối chiếu dữ liệu giữa tổng thể và nhóm dữ liệu
print(f"Mean of population: {scores.mean(): .2f}")
print(f"Mean of sample: {sample_mean.mean(): .2f}")

# Tính sai số chuẩn theo lý thuyết SE = sigma/căn(n) của tổng thể
std_err = scores.std(ddof=0)/np.sqrt(poluation_size)
print(f"Standard error population: {std_err: .2f}")

# Tính sai số chuẩn theo lý thuyết SE = sigma/căn(n) của mẫu
std_err = scores.std(ddof=1)/np.sqrt(sample_size)
print(f"Standard error population: {std_err: .2f}")
    
    
# Tính độ lệch chuẩn thực tế của 1000 trung bình mẫu
print(f"Thực tế SR: {sample_mean.std(ddof=1): .2f}")

# Trực quan hoá
# vẽ đồ thị 1: phân phối tổng thể ban đầu là 5000
plt.figure()

# Vẽ đồ thị histogram: Dùng để xem phân bổ tần xuất
plt.hist(scores,bins = 40)
# Hiển thị các cột mốc bin
plt.xticks(bins)

plt.title("Biểu đồ  histpgr,a ợama ợppso đoeer, tjo")
plt.xlabel("Khoang diem so bins")
plt.ylabel("So luong hoc sinh (Tan suat)")
plt.grid()
plt.show()



# vẽ đồ thị 2: Phân phối theo các trung bình mẫu
plt.figure()

# Vẽ đồ thị histogram: Dùng để xem phân bổ tần xuất
plt.hist(sample_mean,bins = 50)
# Hiển thị các cột mốc bin
plt.xticks(bins)

plt.title("Biểu đồ  histpgr,a ợama ợppso đoeer, tjo")
plt.xlabel("Khoang diem so bins")
plt.ylabel("So luong hoc sinh (Tan suat)")
plt.grid()
plt.show()



"""    
Hypothesis testing
How does Hypothesis testing work?
Null Hypothesis H0: Tôi có thể tung 10 lần đều ra mặt ngửa
Alternative Hypothesis H1:
Z-Test: Mẫu đã biết số lượng và lớn
T-Test: Mẫu chưa biết số lượng hoặc nhỏ
Chi-square test
"""
import scipy.stats as stats
from statsmodels.stats.weightstats import ztest

# Đặt ra giả quyết H0: Điểm thi trung bình của sinh viên là 50 điểm
mu_h0 = 14

z_stat, z_p_val = ztest(sample_mean,value=mu_h0)
print("Gia tri z-statistic: ",z_stat)
print("Gia tri p-value: ",z_p_val)

alpha = 0.05 # giá trị để so sánh với p_value
if z_p_val < alpha:
    print("Bac bo H0, Diem trung bình thuc te khac ",mu_h0)
else:
    print("Chua du co so de bac bo H0")
    


## T-TEST mẫu nhỏ hơn 30, chưa biết độ lệch chuẩn của tổng thể
import scipy.stats as stats
t_stat,t_p_val = stats.ttest_1samp(sample["ExamScore"],popmean=mu_h0)

print("Gia tri t-statistic: ",t_stat)
print("Gia tri p-value: ",t_p_val)

alpha = 0.05 # giá trị để so sánh với p_value
if t_p_val < alpha:
    print("Bac bo H0, Diem trung bình thuc te khac ",mu_h0)
else:
    print("Chua du co so de bac bo H0")
    

"""
Confidence Intervals
Khoản tin cậy

"""
sample_data = sample["ExamScore"].to_numpy()
n = len(sample_data)
sample_mean = sample_data.mean()
print("n: ",n)
print("Mean tren mau: ",sample_mean)

# Sử dụng hàm thống kê để tụ động tính các công thức
lower,upper = stats.t.interval(confidence = 0.95, df = n-1 , loc = sample_mean, scale=stats.sem(sample_data))
print("Khoang tin cay: ",lower," den ",upper)



"""
Correlation and covariance  

"""



# ========= END SOURCE: MON 2/2026-10-23.ipynb =========
