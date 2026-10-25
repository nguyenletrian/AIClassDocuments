# coding: utf-8
# DEMO.py — original student practice code aligned with LAB-07-probability.
# Source: nguyenletrian/PythoClass (private). This is notebook/code provenance, NOT a complete tested solution.
# Read and run sections independently; interactive cells and exploratory snippets may not run sequentially.
# Original example student names (if present) are anonymized before entering the public destination.


# ========= BEGIN SOURCE: MON 2/2026-10-21.ipynb =========

# === Notebook cell 1 ===
"""  
Xác xuất

Tính uncertainty: tính bất định trong xác xuất
0 -> 1 
0: Là sự kiện bất khả thi
1: trời chắc chắn sẽ mưa
0.6: 60% sẽ có mưa

Xác xuất là 1 công cụ để định lượng xác xuất thành 1 con số cụ thể
Xác xuất là 1 chỉ số đo lường khả năng xảy ra 1 sự kiện, được biểu diễn = 1 số từ 0:1

công thức = P(E) = số lượt đầu ra/tổng số lần thử

- Experiment: 1 phép thử có kết quả rõ ràng, ví dụ tung đồng xu
- Sample space: Tập hợp tất cả các kết quả có thể xảy ra của 1 phép thử
- Outcome: là kết quả của 1 phép thử
- Event: Là tập hợp con của không gian mẫu, đại diện cho 1 hoặc nhiều kết quả

Tìm xác xuất: xác định ko gian mẫu, tìm số lượng kết quả có thể có, tính xác xuất

Ví dụ:
TUng xuất sắc tính xác xuất bé hơn 5
Sampe space: S = {1,2,3,4,5,6}
A = {1,2,3,4}
P(A) = 4/6
m = 2/3

Ví dụ 2
Tung xuất sắc tính xác xuất tung 2 xuất sắc kết quả có tổng bằng chính
S = 36
A = (4,5),(5,4),(6,3),(3,6)
P(A) = 4/36


Có 3 loại không gian mẫu:
- Hữu hạn: Có thể đếm được và bị giới hạn
- Vô vạn: Các kết quả kéo dài mã mãi
- Liên tục: các kết quả có giá trị bất kỳ, là số thập phận, ví dụ 0->1

Rút 4 card trên 52 lá bài ko hoàn lại


Biến cố Event:
Là bất kỳ kết quả nào hoặc một tập các kết quả, là tập hợp con của không gian mẫu
Các dạng của kiến cố: ????
Biến cố không thể: Là biến cố không thể xảy ra, xác xuất = 0
Biến cố sure event: Là biến cố chắc chắn có thể xảy ra, xác xuất = 1
Biến cố độc lập: Kết quả xảy ra trước sẽ ko ảnh hưởng đến các kết quả còn lại.
Biến cố phụ thuộc:
Biến cố đơn: chỉ 1 kết quả từ ko gian mẫu
Biến cố phức: Có nhiều kết quả ra
Biến cố xung khắc: Nếu biến cố này xảy ra thì biến cố kia ko thể xảy ra
Biến cố véc cạn:
Biến cố đồng khả năng: Có cơ hội xảy ra như nhau.
"""

import numpy as np
import random
import matplotlib.pyplot as plt

# Cài đặt seed để kết quả các lần chạy giống nhau
np.random.seed(10)

# sample space, outcome, event
# Thí nghiệm tung đồng xu:
sample_space_coin ={"Head","Tail"}

# Tung đồng xu 1000 lần:
coin_toss = np.random.choice(["Head","Tail"],size=1000)

# Xác xuất thực nghiệm xuất hiện mặt head
p_head = np.mean(coin_toss=="Head")
print(p_head)


# Thí nghiệm tung xúc xắc
sample_space_dice = [1,2,3,4,5,6]
# Khai báo các biến cố event bằng tập hợp set
# Biến cố A là tập hợp các số chẳn (Biến cố phức)
A = {2,4,6}
# Biến cố B là tập hợp các số lớn hơn 3
B = {4,5,6}
#Biến cố C là mặt số 5 (Biến cố đơn)
C = {5}

# Tính xác xuất theo lý thuyến P(E) = n(E)/n(5)
# Xác xuất để ra được số chẳn
print("P(A)= ",len(A)/len(sample_space_dice))
print("P(B)= ",len(B)/len(sample_space_dice))
print("P(C)= ",len(C)/len(sample_space_dice))

# Mô phỏng tung xúc sắc 1000 lần
#dice_toss = np.random.randint(1,7,size=1000)
dice_toss = np.random.choice(sample_space_dice,size=1000)
# Xác xuất thực nghiệm xuất hiện mặt head
p_6 = np.mean(dice_toss==6)
print(p_6)


# Mô phỏng tung 2 xuất sắc cùng lúc
dice1 = np.random.choice(sample_space_dice,size=1000)
dice2 = np.random.choice(sample_space_dice,size=1000)

# Tính xác xuất để tổng 2 xuất sắc là 9 
total = dice1 + dice2 # lấy phần tử 1 của dice1 + phần tử thứ 1 của dice 2, cứ thế làm tới

p_sum_9 = np.mean(total == 9)
print("Xac xuat thuc nghiem p_sum_9")
print(p_sum_9)

""" 
Phần bù của biến cố A ký hiệu là ~
phần hiệu là A - B: ví dụ A = {2,4,6}, B {5,6} = > A - B = {2,4}
Phép hợp A ^ B = {2,4,6,5} = trong numpy là &


Xác xuất điều kiện: xác xuất của  biến cố A  khi biết được xác xuất biết cố B xảy ra.
P(A|B) = P(A giao ^ B)/P(B)
4/52 13/52  17/52 chia cho 13/52 = 
P (A giao B): Xác xuất vừa là K vữa là màu đỏ : 2/52
P (B): Xác xuất để lá đỏ là vừa là màu đỏ: 26/52

"""

# XÁC XUẤT CÓ ĐIỀU KIỆN

#Tìm xác xuất khi tung xúc sắc ra số lẽ, khi đã biết giá trị đó <=3

# Thiết lập số lần mô phỏng
n = 10000
# c1: Sử dụng vòng lặp for (tư duy lý thuyết)
print("C1: For")
# Biến cố A là tập hợp các số lẽ
A = {1,3,5}
# Biến cố B là tập hợp các số <=3
B = {1,2,3}

# Khởi tạo các biết đếm để đếm số lần xuất hiện
count_B = 0 # Đếm số lần kết quả <=3
count_A_and_B = 0 # Đếm số lần kết quả vừa là lẻ vừa nhỏ hơn = 3

# Tiến hành tung xúc sắc qua n lần
for i in range(n):
    outcome = random.randint(1,6)
    if outcome <=3:
        count_B += 1
        if (outcome % 2) !=0:
            count_A_and_B +=1

# Tính xác xuất có điều kiện thực nghiệm
# P(A|B) = P(A ^giao B) /P(B)
P_A_given_B = count_A_and_B / count_B
print("So lan bien co B xay ra: ",count_B)
print("So lan vua A vua B: ",count_A_and_B)
print("Xac xuat thuc nghiem P(A|B)",P_A_given_B)


### DÙNG NUMPY
rolls = np.random.choice([1,2,3,4,5,6],size=n)
#print(rolls)
#Khai báo các biến cố với dạng True/False
event_B = (rolls <=3 )
#print(event_B)
event_A_and_B = (rolls/2 !=0) & (rolls <=3)
#Tính xác xuất P(A|B)
p_B = np.mean(event_B)
p_A_and_B = np.mean(event_A_and_B)
p_A_given_B = p_A_and_B/p_B
print("Xac xuat B xay ra: ",p_B)
print("Xac xuat vua A vua B: ",p_A_and_B)
print("P(A|B): có sai ở đây!!!!!",p_A_given_B)


"""    
Các tính chất của xác xuất điều kiện ?????
Định lý Bayers Bayes' Theorem

Ví dụ người bệnh là 1% = 100/9900 (Tổng là 10000)
100 người đi xác nghiệm, tỷ lệ xét nghiệm dương tính là 99%
kết quả là 50% # NHỜ GPT HỎI LẠI

CÔNG THỨC ĐỊNH LÝ BAYERS
Xác xuất 1 người bị bệnh thực sự khi nhận giấy dương tính  = Xác xuất dương tính khi biết người đó có bệnh (nằm trong 1% người có bệnh) nhân với
Xác xuất người có bệnh

"""
# ty le benh nen : 1% dan so mac benh
p_D = 0.01 # Disease
p_H = 1 - p_D # Health
# do chinh xac xet nghiem 99%
p_pos_g_D = 0.99 # Duong tinh that (Positive given Disease)
p_pos_g_H = 1 - p_pos_g_D

# tong ty le duong tinh trong cong dong
# P(Postive) = P(Duong tinh that) + P(Duong tinh gia)
p_pos = (p_pos_g_D * p_D) + (p_pos_g_H * p_H)

# ap dung dinh ly Bayes de tim xac suat 
# 1 nguoi di kham benh bi benh that
# Disease given Postive
p_D_g_pos = (p_pos_g_D * p_D) / p_pos
print("p_pos: ", p_pos)
print("Ty le thuc su bi benh: ", p_D_g_pos)


"""    
Biến ngẫu nhiên RANDOM VARIABLES
Số lượng khách hàng đến thăm quán ca phề mỗi ngày trong 1 tuần
có thể là liên tục hoặc rời rạc
variate: biến lượng

1.
Số lượng giao dịch rút tiền mặt tại một cây ATM trong một giờ là loại biến ngẫu nhiên nào?
A. Biến ngẫu nhiên liên tục
B. Biến ngẫu nhiên hỗn hợp
C. Không phải biến ngẫu nhiên
D. Biến ngẫu nhiên rời rạc

Thời gian (tính bằng phút) mà một khách hàng phải chờ đợi để được nhân viên ngân hàng phục vụ là loại biến ngẫu nhiên nào?

Mức tiêu thụ điện năng hằng tháng (tính bằng kWh, có thể có phần thập phân) của một hộ gia đình là biến ngẫu nhiên gì?

Số lượng tài khoản thanh toán bị khóa do hoạt động đáng ngờ tại một ngân hàng trong một ngày là biến ngẫu nhiên gì?

Trong các đại lượng sau đây liên quan đến hoạt động của một siêu thị, đại lượng nào là biến ngẫu nhiên liên tục?
A. Số lượng khách hàng bước vào siêu thị trong một giờ
B. Khối lượng của một quả dưa hấu được cân tại quầy tính tiền
C. Số lượng nhân viên đang làm việc tại ca trực
D. Số lượng mặt hàng có trong giỏ hàng của một khách



####### Xem tài liệu!~ có những kiến thức lạ lắm

"""
# 
from scipy.stats import binom # Phân phối nhị thức

# Phân phối nhị thức (Binomial cho biến ngẫu nhiên rời rạc)
# Số lần thử nghiệm
n = 10
# Tung đồng xu xác xuất của mặt head
p = 0.5

# tạo biến ngẫu nhiên X chứa danh sách tất cả các số lần xuất hiện của head có thể xảy ra khi tung 10 lần
# x = [0,1,2,3,4,5,6,7,8,9,10] # tập hợp kết quả có thể đạt được trong 10 lần đó, ví dụ 10 lần được 0 lần, 10 lần được 1 lần....
x_values = np.arange(0,n+1) 

# tính giá trị PMF (Hàm khối xác xuất)
pmf_values = binom.pmf(x_values,n,p)

# vẽ đồ thị
plt.figure()

# Vẽ biểu đồ cột để trực quan hoá biến rời rạc
plt.bar(x_values,pmf_values)

plt.title("Phan phoi nhi thuc bieu dien PMF")
plt.xlabel("So lan xuat hien mat head")
plt.ylabel("Xac suat tai P(X) = x")

# Hiện thị đầy đủ các cột mốc từ 0 đến 10 trên trục X
plt.xticks(x_values)
plt.grid()
plt.show()




"""
Phân phối chuẩn normal dùng cho biến ngẫu nhiên liên tục

"""
from scipy.stats import norm

# Giá trình trung bình chiều cao của nam giới
mu = 170

# Độ lệch chuẩn = 5 cm
sigma = 5

# tạo 1 dãy liên tục cho X
x_val = np.linspace(150,190,500) #500 chia đều cho khảong đó

# Tính xác xuất PDF (mật độ xác xuất)
pdf_values = norm.pdf(x_val,mu,sigma)


# vẽ đồ thị
plt.figure()

# Vẽ biểu đồ cột để trực quan hoá biến rời rạc
plt.plot(x_val,pdf_values,label="Duong cong pdf")

plt.title("Phân phối chuẩn bieu diễn PMF")
plt.xlabel("Chiều cao Nam giới")
plt.ylabel("Mật độ xác suât (Density)")
plt.legend()
plt.grid()
plt.show()

#Law of total probability
# Examples on law of total Probability (contd.)
# Xác xuất toàn phần dùng để tính tương lai



### Law of total probality - Công thức xác xuất toàn phần
#Demo bằng numpy
# Mang xác suất tỷ lệ ủng hộ ứng cử viên [Nhóm X, Nhóm Y]
P_Group = np.array([0.6,0.4])

# Mang tỷ lệ ủng hộ chính sách P(P|X), P(P|Y)
P_Policy_given_Group = np.array([0.7,0.2])

# Tính xác suất đồng thời
P_Joint = P_Policy_given_Group * P_Group 

# Áp dụng công thức xác xuất toàn phần bằng nam np.sum()
P_P = np.sum(P_Joint)

print(f"Ty lệ người thuộc nhóm X vừa ủng hộ chính sách: {P_Joint[0]}")
print(f"Ty lệ người thuộc nhóm Y vừa ủng hộ chính sách: {P_Joint[1]}")
print(f"Ty lệ người ngẫu nhiên ủng hộ chính sách: {P_P}")

# ========= END SOURCE: MON 2/2026-10-21.ipynb =========
