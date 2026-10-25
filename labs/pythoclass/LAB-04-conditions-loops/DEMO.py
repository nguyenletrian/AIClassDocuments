# coding: utf-8
# DEMO.py — original student practice code aligned with LAB-04-conditions-loops.
# Source: nguyenletrian/PythoClass (private). This is notebook/code provenance, NOT a complete tested solution.
# Read and run sections independently; interactive cells and exploratory snippets may not run sequentially.
# Original example student names (if present) are anonymized before entering the public destination.


# ========= BEGIN SOURCE: LABSession4.ipynb =========

# === Notebook cell 1 ===
num = input("Vui long nhap 3 so cach nhau = dau ")
listInput =  num.split(" ")
listInput = list(map(str,listInput))
listInput.sort()
for i in listInput:
    print(i)

# === Notebook cell 2 ===
month = int(input("Vui long nhap thang ban can check"))
quarter1 = [1,2,3]
quarter2 = [4,5,6]
quarter3 = [7,8,9]
quarter4 = [10,11,12]
if month in quarter1:
    print(f"Thang {month} thuoc quy I")
elif month in quarter2:
    print(f"Thang {month} thuoc quy II")
elif month in quarter3:
    print(f"Thang {month} thuoc quy III")
else:
    print(f"Thang {month} thuoc quy IV")


# === Notebook cell 3 ===
inputNumber = int(input("Vui long nhap thang can kiem tra"))
month = [1,2,3,4,5,6,7,8,9,10,11,12]
days = [31,28,31,30,31,30,31,31,30,31,30,31]
monthIndex = month.index(inputNumber)
monthDays = days[monthIndex]
print(f"Thang {inputNumber} co {monthDays} ngay")

# === Notebook cell 4 ===
inputNumber = int(input("Vui long nhap nam can kiem tra"))
if (inputNumber % 400 == 0) or (inputNumber % 4 == 0) and (inputNumber % 100 !=0):
    print(f"Nam {inputNumber} is leap year.")
else:
    print(f"Nam {inputNumber} is not leap year.")

# === Notebook cell 5 ===
# input

num4 = int(input("Enter a two-digit integer, e.g., 12"))        

# Step 1: Chuyển đổi hàng chục

hang_chuc = num4 // 10

if hang_chuc == 1:
    ten_hang_chuc = "muoi"
elif hang_chuc == 2:
    ten_hang_chuc = "hai muoi"
elif hang_chuc == 3:
    ten_hang_chuc = "ba muoi"
elif hang_chuc == 4:
    ten_hang_chuc = "bon muoi"
elif hang_chuc == 5:
    ten_hang_chuc = "nam muoi"
elif hang_chuc == 6:   
    ten_hang_chuc = "sau muoi"
elif hang_chuc == 7:
    ten_hang_chuc = "bay muoi"
elif hang_chuc == 8:
    ten_hang_chuc = "tam muoi"
else:
    ten_hang_chuc = "chin muoi"

# Step 2: Chuyen doi hang don vi
hang_don_vi = num4 % 10
if hang_don_vi == 0:
    ten_hang_don_vi= ""      # Lúc in cần thêm strip() để tránh dư khoảng trắng ở TH hang_don_vi ==0
elif hang_don_vi == 1:
    ten_hang_don_vi = "mot"
elif hang_don_vi == 2:
    ten_hang_don_vi = "hai"
elif hang_don_vi == 3:
    ten_hang_don_vi = "ba"
elif hang_don_vi == 4:
    ten_hang_don_vi = "bon"
elif hang_don_vi == 5:
    ten_hang_don_vi = "lam"
elif hang_don_vi == 6:   
    ten_hang_don_vi = "sau"
elif hang_don_vi == 7:
    ten_hang_don_vi = "bay"
elif hang_don_vi == 8:
    ten_hang_don_vi = "tam"
else:
    ten_hang_don_vi = "chin"

# Step 3: In giá trị

print (f"Output: {ten_hang_chuc} {ten_hang_don_vi}".strip())

# === Notebook cell 6 ===
numbers = input("Enter two positive integers are separated by a space:")
numbers = numbers.split(" ")
if int(numbers[0]) > int(numbers[1]):
    number01 = int(numbers[0])
    number02 = int(numbers[1])
else:
    number01 = int(numbers[1])
    number02 = int(numbers[0])
    
if number01 > 0 and number02 > 0:
    gcd = 0
    while True:
        sodu = number01 % number02
        if sodu == 0:
            gcd = number02
            break
        else:
            number01 = number02
            number02 = sodu

    print("GCD =", gcd)
else:
    print(f"{number01} or {number02} is not a positive integer")

# ========= END SOURCE: LABSession4.ipynb =========


# ========= BEGIN SOURCE: 4.Condition.ipynb =========

# === Notebook cell 1 ===
#Kiem tra cho nhap 1 so, kiem tra xem so do co phai so chan hay ko
num = input("Vui long nhap 1 so")
if num != "":
    num = int(num)   
    if (num % 2) == 0:
        print(f"{num} là số chẵn")
    else:
        print(f"{num} là số lẽ")
else:
    print("Khong hop le")


# === Notebook cell 2 ===
# Cho nhap 1 diem, xuat ra phan loai dua tren diem
mark = float(input("Nhap diem cua sinh vien"))
if mark >= 90:
    print("Grade A")
elif mark >= 80:
    print("Grade B")
elif mark >= 70:
    print("Grade C")
elif mark >= 60:
    print("Grade D")
else:
    print("Grade E")
print("End")

# === Notebook cell 3 ===
a = 5
b = 3
if a >= 5:
    print("ok")
if b >= 3:
    print("yes")
else:
    print("no")

# === Notebook cell 4 ===
# VIP: revenue >= 1000 và year >=5
revenue = 1000
year = 5
if revenue >= 1000 and year >= 5:
    print("VIP")
else:
    print("Not VIP")

# === Notebook cell 5 ===
# VIP: revenue >= 1000 và year >=5
revenue = 1000
year = 5
if revenue >= 1000:
    if year >= 5:
        print("VIP")
    else:
        print("Not VIP beacuse not enough year")
else:
    print("Not VIP because not enough revenue")

# ========= END SOURCE: 4.Condition.ipynb =========


# ========= BEGIN SOURCE: 5.Loop.ipynb =========

# === Notebook cell 1 ===
count = 1
while count <= 5:
    print(count)
    count += 1

# === Notebook cell 2 ===
# in 10 lan chu hello dung while
count = 1
while count <= 10:
    print(f"Hello {count}")
    count += 1
print("End")

# === Notebook cell 3 ===
# Print range
for i in range(1,6): #từ 1 đến 5 , nếu chỉ truyền vào 1 tham số 6 thì nó sẽ chạy từ 0-5
    print(i)

# === Notebook cell 4 ===
# Print chuỗi
for char in "Hello python":
    print(char)

# === Notebook cell 5 ===
# In cac phan tu trong list
number = [1,2,3,4,5]
for item in number:
    print(item)


# === Notebook cell 6 ===
list = ["Vy","Tuan","Khoa"]
for s in list:
    print(s)
print(s)

# === Notebook cell 7 ===
for i in range(1,4):
    for j in range(1,3):
        print(i,j)

# === Notebook cell 8 ===
for i in range(1,4):
    for j in range(1,3):
        print(i,j)

# === Notebook cell 9 ===
count = 4
for i in range(0,count):
    print("*  " * (count))

# === Notebook cell 10 ===
#Break
for i in range(1,10):
    if i ==5:
        break
    print(i)

# === Notebook cell 11 ===
# PASS
for i in range(1,4):
    pass #Code to be added later
print("Loop completed")

# === Notebook cell 12 ===
# CONTINUE
for i in range(1,6):
    if i == 3:
        continue
    print(i)

# === Notebook cell 13 ===
# ELSE
for i in range(1,6):
    if i == 10:
        break
    print(i)
else:
    print("Loop completed successfully")

# === Notebook cell 14 ===
# Else: Chỉ chạy khi vòng for ko bị break
number = [1,2,3,4,5,6]
findNumber = 3
for i in number:
    if i == findNumber:
        print(f"{findNumber} có ton tai trong danh sach")
        break
else:
    print(f"{findNumber} khong ton tai trong danh sach")

# === Notebook cell 15 ===
for i in range(1,5):
    for j in range(1, 5):
        if j > i :
            continue
        print(j,end=" ")
    print()

# === Notebook cell 16 ===
for i in range(7):
    listTemp = range(1,i)
    print((" ").join(map(str,listTemp)))

# === Notebook cell 17 ===
t = ""
for i in range(1, 5):
    t += str(i) + " "
    print(t)
    

# ========= END SOURCE: 5.Loop.ipynb =========
