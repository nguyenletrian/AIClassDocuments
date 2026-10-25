# coding: utf-8
# DEMO.py — original student practice code aligned with LAB-10-file-csv.
# Source: nguyenletrian/PythoClass (private). This is notebook/code provenance, NOT a complete tested solution.
# Read and run sections independently; interactive cells and exploratory snippets may not run sequentially.
# Original example student names (if present) are anonymized before entering the public destination.


# ========= BEGIN SOURCE: main.py =========

import pandas as pd

def inputHelper(data):            
    label = data["label"]
    formats = data["formats"]    
    inputTemp = input(label)    
    if inputTemp == "":
        return(None)    
    blocks =  inputTemp.split(";")  
                  
    # Check block
    if len(blocks) != len(formats):
        print("!!![ERROR] Input blocks is not correct!~")
            
    # Check type
    for i in range(len(formats)):
        if type(blocks[i]).__name__ != formats[i]:
            print("!!![ERROR] Input format is not corrects")              
    return(blocks)    
    
def displayAll():
    df = pd.read_csv("students.csv")
    print("""
==== DISPLAY ALL STUDENT =====""")
    students = df[" name"].values
    stt = 1
    for student in students:
        print(f"{stt}. {student}")
        stt += 1

def studentSearch():
    print("""
==== SEARCH STUDENT =====""")
    inputData = inputHelper({
        "label":"Please enter Student ID:",
        "formats":["str"]
    })
    if inputData:
        inputData = inputData[0]
        df = pd.read_csv("students.csv")
        result = df[df["student_id"] == inputData]
        if len(result)!=0:
            print(result)
        else:
            print("!!![ERROR] Student not found.")
        studentSearch()
    else:
        return
    
def studentAverage():
    print("""
==== STUDENT RESULT ====""")
    inputData = inputHelper({
        "label":"Please enter Student ID:",
        "formats":["str"]
    })
    if inputData:
        inputData = inputData[0]
        df = pd.read_csv("students.csv")
        result = df[(df["student_id"] == inputData)]
        if len(result)!=0:
            values = result.values
            print(f"""
Student name: {values[0][1]}
Python score: {values[0][3]}
Math score: {values[0][4]}
ML score: {values[0][5]}
Average score:{round((values[0][3] + values[0][4] + values[0][5])/3,2)}
Highest score:{max(values[0][3],values[0][4],values[0][5])}
Lowest score:{min(values[0][3],values[0][4],values[0][5])}
""")
        else:
            print("!!![ERROR] Student not found.")
        studentAverage()
    else:
        return

def analyzeSubject():
    print("""
==== SUBJECT PERFORMANCE ====""")
    df = pd.read_csv("students.csv")
    data = {
        "Average":[df["Python"].mean(),df["Math"].mean(),df["ML"].mean()],
        "Total":[df["Python"].sum(),df["Math"].sum(),df["ML"].sum()],
        "Highest":[df["Python"].max(),df["Math"].max(),df["ML"].max()],
        "Lowest":[df["Python"].min(),df["Math"].min(),df["ML"].min()],
    }
    dfShow = pd.DataFrame(data,index=["Python","Math","ML"])
    print(dfShow)


def analyzeClass():
    print("""
===== CLASS PERFORMANCE =====""")
    df = pd.read_csv("students.csv")
    studentCount =  df.groupby("class_name")["student_id"].count()
    pythonMean =  df.groupby("class_name")["Python"].mean()
    mathMean =  df.groupby("class_name")["Math"].mean()
    mlMean =  df.groupby("class_name")["ML"].mean()
    result = pd.merge(studentCount,pythonMean,on="class_name",how="outer")
    result = pd.merge(result,mathMean,on="class_name",how="outer")
    result = pd.merge(result,mlMean,on="class_name",how="outer")
    result["Overall Average"] = (result["Python"] + result["Math"] +  result["ML"])/3
    
    
    result.reset_index(inplace=True) #Trợ giúp của chat GPT ạ!~
    result.rename(columns={"student_id":"Students"}, inplace=True) #Trợ giúp của chat GPT ạ!~
    result.rename(columns={"class_name":"Class"}, inplace=True)
    
    result = result.round(2) # Trợ giúp của chat GPT ạ!~
    
    print(result)

def top3():
    print("""
===== TOP 3 STUDENTS =====""")
    df = pd.read_csv("students.csv")
    df["Average"] =   (df["Python"] + df["Math"] +  df["ML"])/3
    dfSorted = df.sort_values(by="Average",ascending=False)
    dfSorted.drop(columns=["Python","Math","ML"], inplace=True) # Trợ giúp của chat GPT ạ!~
    dfSorted.rename(columns={"class_name":"Class","student_id":"Student ID"}, inplace=True)
    dfSorted = dfSorted.round(2)
    
    print(dfSorted.head(3))    

# MENU()
def menu():
    choice = 0
    while True:
        print("""
================================
 STUDENT PERFORMANCE ANALYSIS
------------------------------------------------------
1. Display all students
2. Search for a student
3. Calculate student average
4. Analyze subject performance
5. Analyze class performance
6. Show top 3 students
7. Exit         
        """)
        # nhap lua chon
        inputData =input("Please select (1-7): ")
        if inputData.isnumeric():
            choice = int(inputData)
            if choice == 1:
                displayAll()
            elif choice == 2:
                studentSearch()
            elif choice == 3:
                studentAverage()
            elif choice == 4:
                analyzeSubject()
            elif choice == 5:
                analyzeClass()
            elif choice == 6:
                top3()
            elif choice == 7:
                break
            else:
                print("!!![ERROR] Please enter from 1 to 7")
        else:
            print("!!![ERROR] Please enter from 1 to 7")

# goi ham
menu()


# ========= END SOURCE: main.py =========


# ========= BEGIN SOURCE: 10. File IO.py =========

"""
# Cho
file_r = open("my_doc.txt","r") # To open for reading
file_w = open("new_report.txt","w") # To open for writing (overites) tạo mới nếu chưa có
file_a = open("log.txt","a") # To open for appeding, tạo mới nếu chưa có
file_b = open("log.txt","rb") #"wb"
# r+, w+ là cả ghi và đọc

#.read() Đọc hết nội dung
#.readline(): đọc 1 dòng mỗi lần
#.readlines(): đọc tất cả các dòng
with open("data.txt","r") as f:
    full_content = f.read() 
    f.seek(0) #Reset pointer Đưa lại dòng số 1
    first_line = f.readline() # line

with open ("poem.txt","w") as f:
    f.write("Roses are red,\n")
    f.write("Violets are blue,\n")
print("... Reading poem.txt")
    
#.close() để đóng file

#with open("filename","mode") as file_object: # mở và tự động đóng.

#.write(string): ghi file
#.writelines(list_of_strings) 1 mảng các chuỗi vào

"""

FIlE_NAME = "products.csv"

# Doc du lieu tu file và trả về danh sách đọc được
def read_products():
    # Tạo 1 biến kiểu list chứa tất cả sản phẩm đoc được từ file
    productList = []
    try:
        with open(FIlE_NAME,"r") as file:
            # Bỏ qua dòng đầu
            file.readline()
            # Đọc tiếp từ dòng số 2 trong file
            for line in file:
                data = line.strip() # Bỏ ký tự \n ở cuối mỗi dòng
                data = data.split(",")
                # Tạo sản phẩm theo dạng dictionary
                product = {
                    "id":data[0],
                    "name":data[1],
                    "price":data[2],
                }
                # Thêm sản phẩm vào list
                productList.append(product)
        return(productList)
    except FileNotFoundError: # Để trước vì nó là con của Exception
        print("File ko tim thay")
    except Exception as e: # Exception là cha của các lỗi
        print("Error: " + e)

# Hàm hiển thị sản phẩm
def display_product(products):
    # Kiểm tra nếu file rỗng (chưa có dữ liệu)
    if len(products) == 0:
        print("No products")
        return()
    # Nếu có dữ liệu thì in ra
    print("n\ ======================= Product list ====================")
    for p in products:
        print(f"ProductID: {p["id"]} --- ProductName: {p["name"]} --- Price:{p["price"]} ")
    

# Hàm thêm sản phẩm
def add_product(products):
    # Nhập product id
    product_id = input("Enter Product ID:")
    # Kiểm tra xem id này có tồn tại hay chưa?
    for p in products:
        if p["id"].lower() == product_id.lower():
            print("ID was duplicated")
            return()
    # Nhập tên
    product_name = input("Enter Product Name:")
    
    # Nhập giá
    try:
        product_price  = float(input("Enter price:"))
    except ValueError:
        print("Price must be number!!!")
    except Exception as e:
        print("Error: " + e)
        
    # Tạo sản phẩm theo dạng dictionary
    product = {"id":product_id,"name":product_name,"price":product_price}
    products.append(product)
    print("Produce added successfully")
    
        

# Hàm tìm kiếm sản phẩm:
def search_product(products):
    # Nhập ID để tìm kiếm
    product_id = input("Enter Product ID:")
    
    # Tạo 1 biến kiểu list để chứa các sản phẩm tìm thấy được
    found = []
    for p in products:
        if product_id.lower() in p["id"].lower():
            found.append(p)
    
    # Kiểm tra xem có tìm kiếm được hya ko
    if len(found) >0:
        display_product(found)
    else:
        print("No product found")
        
        
# Hàm lưu vào file:
def save_product(products):
    try:
        with open(FIlE_NAME,"w") as file:
            # Ghi lại dòng đầu tiên
            file.write("ProductID,ProductName,Price\n")
            
            # Ghi các dòng tiếp theo dự vào danh sách products
            for p in products:
                line = f"{p["id"]},{p["name"]},{p["price"]}\n"
                file.write(line)
            print("Write sucessfully.")
    except Exception as e:
        print("Error: ",e)

#Main Menu
def main():
    # Đọc dữ liệu khi chương trình chạy, gọi hàm read_product
    products = read_products()
    
    
    while True:
        print("""
==== MENU ==== 
1. Display all products
2. Add product
3. Search product by id
4. Save products to file.
5. Exit program
==== MENU ====             
""")
        choice = input("Enter your choice:")
        if choice == "1":
            display_product(products)
        elif choice == "2":
            add_product(products)
        elif choice == "3":
            search_product(products)
        elif choice == "4":
            save_product(products)
        elif choice == "5":
            print("Exit program")
            break
        else:
            print("Wrong choice, Enter 1-5")

main()
            
        

# ========= END SOURCE: 10. File IO.py =========


# ========= BEGIN SOURCE: Demo/10_fileio.py =========

FILE_NAME = "products.csv"

# doc du lieu tu file va tra ve ds doc duoc
def read_products():
    # tao 1 bien kieu list chua tat ca san pham doc duoc tu file
    productList = []

    try:
        with open(FILE_NAME, "r") as file:
            # bo qua dong dau
            file.readline()
            # doc tiep tu dong so 2
            for line in file:
                line = line.strip() # bo ky tu \n o cuoi moi!~ dong

                # cat chuoi thanh mang
                data = line.split(",")
                # tao san pham theo dang dictionary
                product = {
                    "id": data[0],
                    "name": data[1],
                    "price": data[2]
                }

                # them san pham vao list
                productList.append(product)
    except FileNotFoundError:
        print("File ko tim thay")
    except Exception as e:
        print("Error: ", e)

    # print(productList) 
    return productList     
          

# ham hien thi san pham
def display_product(products):
    # kiem tra neu file rong(chua co du lieu)
    if len(products) == 0:
        print("No products")
        return

    # neu co du lieu thi in ra 
    print("\n ----------------Product List-----------------")
    for p in products:
        print(f"ProductID: {p['id']}   ---  ProductName: {p['name']}   ---   Price: {p['price']}")

# ham them san pham
def add_product(products):
    try:
        # cho nhap product id
        product_id = input("Enter Product ID:")
        # kiem tra xem id nay co ton tai hay chua?
        for p in products:
            if p['id'].lower() == product_id.lower():
                print("Id was duplicated")
                return

        # nhap ten
        product_name = input("Enter Product Name:")
        # nhap gia
        product_price = float(input("Enter price:"))
        # tao san pham theo dang dictionary
        product = {"id": product_id, "name": product_name, "price": product_price}
        # them san pham vao danh sach
        products.append(product)
        print("Product added succesfully")
    except ValueError:
        print("Price must be number!!!!")

# ham tim kiem san pham
def search_product(products):
    # nhap id de tim kiem
    product_id = input("Enter Product ID:")

    # tao 1 bien kieu list de chua cac san pham tim thay duoc
    found = []
    for p in products:
        if product_id.lower() in p['id'].lower():
            found.append(p)

    # kiem tra xem co tim kiem duoc hay ko
    if len(found) > 0:
        display_product(found)
    else:
        print("No product found")


# ham luu vao file
def save_products(products):
    try:
        with open(FILE_NAME, 'w') as file:
                # ghi lai dong`` dau` tien
                file.write("ProductID,ProductName,Price\n")
        
                # ghi cac dong tiep theo dua vao ds
                for p in products:
                    line = p['id'] + "," + p['name'] + "," + str(p['price']) + "\n"
                    file.write(line)
        
                print("Write successfully")
    except Exception as e:
        print("Error: ", e)


# Main Menu
def main():
    # doc du lieu khi chuong trinh chay, goi ham readproducts()
    products = read_products()

    while True:
        print("********************MENU*********************")
        print("1. Display all products")
        print("2. Add product")
        print("3. Search product by id")
        print("4. Save products to file")
        print("5. Exit program")
        print("********************MENU*********************")

        choice = input("Enter your choice:")
        if choice == "1":
            display_product(products)
        elif choice == "2":
            add_product(products)
        elif choice == "3":
            search_product(products)
        elif choice == "4":
            save_products(products)
        elif choice == "5":
            print("Exit program")
            break
        else:
            print("Wrong choice. Enter 1-5")

# goi ham main
main()




# ========= END SOURCE: Demo/10_fileio.py =========
