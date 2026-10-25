# coding: utf-8
# DEMO.py — original student practice code aligned with LAB-05-06-gradient-descent.
# Source: nguyenletrian/PythoClass (private). This is notebook/code provenance, NOT a complete tested solution.
# Read and run sections independently; interactive cells and exploratory snippets may not run sequentially.
# Original example student names (if present) are anonymized before entering the public destination.


# ========= BEGIN SOURCE: MON 2/2026-10-19.ipynb =========

# === Notebook cell 1 ===
""" 
Các khái niệm về đạo hàm
Khi ta đang lái xe thì đồng hồ tốc độ sẽ tính theo từng giây
để tính tốc độ đạo hàm thì sẽ tính bằng s = f(t)
đạo hàm là nền tảng để tính lim (giới hạn)
đạo hàm sin(x) = cos(x)

ĐẠO HÀM TỪNG PHẦN
Giả sửa có 1 mô hình dự đoán giá nhà: p = f (x1,x2)
Hàm số này thay đổi dựa trên 2 tham số x1,x2
dự đoán giá nhà tăng và giảm theo từng theo số
mỗi lần tính thì giữ 1 biến = hằng số => đạo hàm = 1

cú pháp của đạo hàm từng phần
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

#partial Derivative - Đạo hàm riêng
x,y = sp.symbols("x y")
#Khai bao hàm 2 biến
f = x**2 + 3*x*y + y**2

#Đạo hàm riêng theo x
df_dx = sp.diff(f,x)
# Đạo hàm riêng theo y
df_dy = sp.diff(f,y)

print("f(x,y) = ",f)
print("Dao ham rieng theo X = ",df_dx)
print("Dao ham rieng theo y = ",df_dy)

# Tính giá hàm và đạo hàm tại 1 điểm (1,2)
point = {x:1,y:2}
print("f(1,2) =",f.subs(point))
print("df/dx tai (1,2) =",df_dx.subs(point))
print("df/dy tai (1,2) =",df_dy.subs(point))

# ĐẠO HÀM RIÊNG BẬT CAO
#f_xx: lấy đạo hàm theo x 2 lần
#f_yy: Lấy đạo hàm theo y 2 lần
#f_xy: Lấy đạo hàm theo x rồi theo y
#f_yx: Lấy đạo hàm theo y rồi theo x
f_xx = sp.diff(f,x,2)
f_yy = sp.diff(f,y,2)
f_xy = sp.diff(df_dx,y)
f_yx = sp.diff(df_dy,x)
print("f_xx = ",f_xx)
print("f_yy = ",f_yy)
print("f_xy = ",f_xy)
print("f_yx = ",f_yx)


## ỨNG DỤNG ĐẠO HÀM, ĐO LƯƠNG ĐỘ DỐC SLOPE - GRADIENT
"""
m = deltaY/deltaX = đạo hàm của Y chia cho đạo hàm của X trong đó y=f(x)
m là hệ số góc.
gradient dương -> hướng lên
gradient âm -> hướng xuống
gradient = 0 -> đường ngang
ví dụ: y = 2x+1 (2 là hệ số góc)
y = -3x + 2

Gradient Vector ### TÌM HỌC
Properties of Gradient Vectors
 - Direction of steepest Ascent
 - Prependicular to level Curves
 - Magniude is rate of change
 - Zero at Critical points
 
Gradient Descent
hàm mất mát càng thấp càng tốt
learning rate
"""
"""
 Gradient vector là vector gồm các đạo hàm riêng bậc 1
 Gradient cho biết hướng tăng nhanh nhất của hàm số
 Gradient desent sẽ đi ngược lại hướng của gradient để giảm hàm loss
"""
gradient = sp.Matrix([df_dx,df_dy])
gradient_at_point = gradient.subs(point)
print(gradient_at_point)



# === Notebook cell 2 ===
"""  
Demo gradient descent:
F(w) = w**2
Tìm giá trị w để hàm số F(w) nhỏ nhất (hàm loss nhỏ nhất)
Cộng thức cập nhật: w = w - learning_rate * grdient
Khởi tạo giá trị w ban đầu
"""
# Khởi tạo giá trị w ban đầu
w = 10
learning_rate = 0.1
for i in range(10):
    #Tính độ dốc (gradient) tại vị trí w hiện tại
    gradient = 2*w # Đạo hàm bậc 1 theo w
    # Cập nhật w di ngược hướng với độ dốc
    w = w - learning_rate * gradient
    #Print w sau mỗi vòng lập
    print(f"loop {i+1}: w={w}")




# === Notebook cell 3 ===
"""
Trực quan hoá
"""
w = 10 # Giá trị ban đầu
learning_rate = 0.1 # Tốc độ học (alpha)
history = [] # Danh sách lưu lại các điểm w để vẽ đồ thị
for i in range(20):
    #Tính độ dốc (gradient) tại vị trí w hiện tại
    loss = 2*w # Đạo hàm bậc 1 theo w
    # Lưu toạ độ (w,loss) vào history
    history.append((w,loss))
    # Cập nhật w di ngược hướng với độ dốc
    w = w - learning_rate * loss

# Vẽ đồ thị y = x**2
# Tạo 200 điểm cách đều từ -10 đến 10
x = np.linspace(-10,10,200)
# Hàm số
y = x**2
# Tạo khung để vẽ
plt.figure()
# Vẽ đồ thì hàm số dựa trên rừng điểm
plt.plot(x,y,label="F(w) = w2")
# Duyệt history và vẽ các điểm chấm tròn
for i,(w_value,loss_value) in enumerate(history):
    plt.scatter(w_value,loss_value)
plt.xlabel("Tham so w")
plt.ylabel("Ham mat mat loss")
plt.title("Truc quan hoa qua trinh dich chuyen cua gradinet descent")
plt.legend()
plt.grid()
plt.show()


# === Notebook cell 4 ===
# So sánh các tốc độ học bằng đồ thị
learning_rates = [0.01,0.1,0.5,0.95]
# Tạo khung để vẽ
plt.figure()
for lr in learning_rates:
    # Khởi tạo w, reset lại sau mỗi lần mất learning rate
    w = 10
    history = [] # Danh sách lưu lại các điểm w để vẽ đồ thị
    for i in range(20):
        #Tính độ dốc (gradient) tại vị trí w hiện tại
        loss = 2*w # Đạo hàm bậc 1 theo w
        # Lưu toạ độ (w,loss) vào history
        history.append(w)
        # Cập nhật w di ngược hướng với độ dốc
        w = w - lr * loss
    # Vẽ đường biểu diễn sự thay đổi w qua các vòng lặp 1
    plt.plot(range(20),history,marker='o',label=f"learning rate ={lr}")
plt.xlabel("Số vòng lặp")
plt.ylabel("Giá trị của w")
plt.title("Anh huong của learning rate với sự hội tụ của w")
plt.legend()
plt.grid()
plt.show()


# === Notebook cell 5 ===
"""    
Ma trận Jacobian: ma trận sử dụng đạo hàm riêng bậc 1 của 1 hàm có nhiều đầu vào và nhiều đầu ra
trong thực tế sẽ có nhiều đầu vào và nhiều đầu ra
để tính ảnh hưởng của các đầu vào với các đầu ra thì phải dùng matraajn Jacobian
Mỗi đầu ra thứ nhất sẽ ảnh hưởng như thế nào nếu lần lượt đầu vào thay đổi
j(x) 
"""

"""    
Thể tích y1 = x1/x2
Khối lượng riêng y2 = x2/x1
"""
# khai báo biết đầu vào: x1 là nhiệt độ (Kelvin), x2 = áp suât (atmosphere)
x1, x2 = sp. symbols("x1 x2")
#Khai báo hàm
y1 = x1/x2
y2 = x2/x1
#Gom các hàm đầu ra thành 1 ma trận
F = sp.Matrix([y1,y2])
inputs = sp.Matrix([x1,x2])

# tính ma trận Jacobian
jacob = F.jacobian(inputs)
sp.pprint(jacob)

# Giả sử hiện tại: nhiệt độ x1 = 300k, áp xuất x2 = 2atm
x1_val = 300
x2_val = 2
y1_val = x1_val/x2_val
y2_val = x2_val/x1_val
print("The tich: ",y1_val)
print("Khoi luong riêng: ",y2_val)

#Tính giá trị của ma trận Jacobian để đo độ nhạy thực tế
jacob_point = {x1:x1_val,x2:x2_val}
jacob_val = jacob.subs(jacob_point)
print("Ma trận jacob")
sp.pprint(jacob_val)

# === Notebook cell 6 ===
"""    
Ma trận Hessian: Ma trận riêng bậc 2 : nhiều thông số, nhưng chỉ có 1 đầu ra
Hessian chưa các đạo hàm riêng bậc 2 của 1 hàm vô hướng (1 đầu ra)
Hessian giúp nghiên cứu độ cong của hàm loss
"""
#Khai báo biến
x,y = sp.symbols("x y")
# Khai báo hàm số F(x,y) = x^2 - y^2
F = x**2 - y**2
# Tính đạo hàm bậc 1 của F theo X
grad_x = sp.diff(F,x)
# Tính đạo hàm bậc 1 của F theo Y
grad_y = sp.diff(F,y)
print("grad_x: ",grad_x)
print("grad_y: ",grad_y)
# Để tìm điểm tới hạn thì giải hệ phương trình grad_x=0 va grad_y = 0
critical_point = sp.solve([grad_x,grad_y],(x,y))
print("Diem toi han: ",critical_point)

# Thay toạ độ x,y vào hàm F để tính giá trị z (Loss)
z = F.subs(critical_point)
print(z)

# Lập ma trận hession chứa các đạo hàm bậc 2 của F
hessian_matrix =sp.Matrix([[sp.diff(grad_x,x),sp.diff(grad_x,y)],[sp.diff(grad_y,x),sp.diff(grad_y,y)]])
sp.pprint(hessian_matrix)

# Tính định thức của Hession
"""    
det H < 0: Điểm cực trị là điểm yên ngựa
det H > 0: Có thể điểm cực đại hoặc cực tiêu
    Xét tại vị trí (0,0) của ma trận hessian > 0: cực tiểu
    Xét tại vị trí (0,0) của ma trận hessian < 0: cực đại
"""


# === Notebook cell 7 ===
# Áp dụng tối ưu hoá: dự đoán giá nhà
x = 100
# Giá thực tế (triệu đồng)
y_true = 900

#Khởi tạo ngẫu nhiên trọng số ban đầu của mô hình (AI chưa học)
w = 2
b =  50
learning_rate = 0.00005

# Chạy 5 vòng lặp (epches) # Khái niệm chạy vòng lặp để huấn luyện
for epoch in range(1,6):
    # Hàm dự đoán
    y_pred = w*x + b
    # Hàm loss MSE
    loss = (y_true - y_pred) ** 2
    # Tính gradient (đạo hàm theo hàm loss) và cập nhật trọng số
    df_dw = -2*x*(y_true - y_pred)
    df_db = -2*(y_true - y_pred)
    
    #Cập nhật trọng số
    w = w - learning_rate * df_dw
    b = b - learning_rate * df_db
    
    # in kết quả của từng vòng
    print(f"Vong {epoch}")
    print(f"Du doan: {y_pred}")
    print(f"Do loi: {loss}")
    print(f"w: {w}")


# === Notebook cell 8 ===
## Áp dụng cho 100 ngôi nhà
# giả lập dữ liệu random
np.random.seed(2) # Đảm bảo dữ liệu giống nhau sau mỗi lần chạy
N = 100
#Tạo ngẫu nhiên diện tích 30-150 m2
x = np.random.uniform(30,150,N)

# tạo 1 trọng số nhiễu
noise = np.random.normal(0,20,N)

#Nhà nhà thực tế:
y_true = 8 * x + 50 + noise


#Khởi tạo ngẫu nhiên trọng số ban đầu của mô hình (AI chưa học)
w = 2
b =  10
learning_rate = 0.00005


# Chạy 5 vòng lặp (epches) # Khái niệm chạy vòng lặp để huấn luyện
for epoch in range(1,101):
    # Hàm dự đoán
    y_pred = w*x + b
    # Hàm loss MSE #mean square error
    #loss = (y_true - y_pred) ** 2
    loss = np.mean((y_true - y_pred) ** 2)
    
    # Tính gradient (đạo hàm theo hàm loss) và cập nhật trọng số
    #df_dw = -2*x*(y_true - y_pred)
    #df_db = -2*(y_true - y_pred)
    
    df_dw = -2*np.mean(x*(y_true- y_pred))
    df_db = -2*np.mean((y_true - y_pred))
    
    #Cập nhật trọng số
    w = w - learning_rate * df_dw
    b = b - learning_rate * df_db
    
    # in kết quả của từng vòng
    if epoch == 1 or epoch % 10 == 0:
        print(f"Vong {epoch}")
        print(f"Do loi: {loss}")
        print(f"w: {w}")
        print(f"b: {b}")
        
print("Ket qua sau huan luyen: w={w},b={b}")

# ========= END SOURCE: MON 2/2026-10-19.ipynb =========


# ========= BEGIN SOURCE: MON 2/2026-10-16-2.ipynb =========

# === Notebook cell 1 ===
""" 
Giới hạn của hàm là giá trị chúng ta tiến tới nhưng ko bao giờ tiến tới giá trị đó,
giúp chúng ta hiểu được điều gì xảy ra khi các input đầu vào 
lim f(x) = L
x -> a


Liên tục, 1 hàm ngay tại 1 điểm bất kỳ ko bị interrupt, và tồn tại giới hạn
lim của f(x)
"""


""" 
#limit: giới hạn
"""
def f_limit(x):
    return(
        (x**2 - 4)/(x-2)        
    )
# Cho x tiến tới 2: lim(x->2) f(x)
values = [1.9,1.99,1.9999,2.001,2.01,2.1]
for val in values:
    print(f"x = {val} -> f(x)= {f_limit(val)}")
    

# Tính giới hạn bằng sympy
# Khai báo biến toán học x
import sympy as sp
x = sp.symbols("x")
fx = (x**2 -4)/(x-2)
limit_value=(sp.limit(fx,x,2))
print("Gioi hạn giai tich khi x->2 la:",limit_value)

# Tính liên tục: continuity:
"""
f(x) = x^2: hàm liên tục
f(x) = 1/x: Hàm ko liên tục
"""
"""
###Vẽ hàm ko liên tục va liên tục
x1 = np.linspace(-10,-0.01,100)
x2 = np.linspace(0.01,10,100)
y1 =1/x1
y2 = 1/x2
plt.figure()
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.ylim(-10,10)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("No continuity function: f(x) = 1/x")
plt.grid()
plt.show()
"""

""" 
Derivatives 
Đào hàm là độ dốc, là cách tối ưu hoá mô hình
cách tính đạo hàm là quá trình tìm kiếm quá trình thay đổi hoặc độ đốc của,
Đạo hàm quan trọng trong ML,  
constant rule: hàm số có hằng số: luôn luôn =0
powe rule = x5 = 5x^4
sum rule đạo hàm của f(x) + g(x) = 
x^5 + 2x = 5x^4 + 2x^1
difference rule
product rule: quy tác nhân
Quotine rule: quy tắc chia
chain rule: quy tắc chuỗi, đạo hàm trong đạo hàm
"""

""" 
derivative: đạo hàm
cho biết tốc độ thay đổi của hàm số theo x
"""
import sympy as sp

# Khai báo biến toán học X
x =sp.symbols("x")

# Khai báo hàm số
f = x**2

#Tính đạo hàm bằng sympy
df =sp.diff(f,x)
print("f(x)=",f)
print("f'(x)=",df)


# tính giá trị của đạo hàm tại x=2
d_at_2 = df.subs(x,2)
print("gia ti f'(2)=",d_at_2) #tính độ dốc tại điểm đó

""" 
### differentaion rules: các quy tác tính đạo hàm

"""
x= sp.symbols("x")

#1.constaint rule
f = 5
print("f(x)=",f)
print("f'(x)=",sp.diff(f,x))

# 2. power rule
f = x**5
print("f(x)=",f)
print("f'(x)=",sp.diff(f,x))

# 3. sum rule
f = x**5 + 2*x
print("f(x)=",f)
print("f'(x)=",sp.diff(f,x))

# 4.difference rude
f = x**5 - 2*x
print("f(x)=",f)
print("f'(x)=",sp.diff(f,x))

#5. product rude:
f = x*(x+2)
print("f(x)=",f)
print("f'(x)=",sp.diff(f,x))

#6. quotient rule()
f = x**2/(x+1)
print("f(x)=",f)
print("f'(x)=",sp.diff(f,x))

#7. chain rule: đạo hàm hàm hợp:
f = (2*x + 3)**3


""" 
Đường tiếp tuyếtn: tangent line
f(x) = x2
tangent line: y = f'(x0)(x-x0) + f(x0)
"""
x = np.linspace(0,5,100)
f = x**2

#Xác định điểm tiếp tục trên đồ thị A(x0,y0)
x0 = 2
y0 = x0**2

# tính đạo hàm tại điểm x0 để tìm hệ số góc
slope = 2 * x0

#lập phương trình đường tiếp tuyến
tangent = slope*(x-x0) + y0
print(f"Tiếp điểm A:",({x0},{y0}))
print(f"He so goc: {slope}")

#ve do thi
plt.figure()

# ve duong cong cua ham so f(x)
plt.plot(x,f,label="Hàm so f(x) = x^2")
# ve duong tiep tuyen
plt.plot(x,tangent,label="Duong tiep tuyen")

plt.xlabel("x")
plt.ylabel("y")




# ========= END SOURCE: MON 2/2026-10-16-2.ipynb =========
