# coding: utf-8
# DEMO.py — original student practice code aligned with ASSIGNMENT-01-student-dictionary.
# Source: nguyenletrian/PythoClass (private). This is notebook/code provenance, NOT a complete tested solution.
# Read and run sections independently; interactive cells and exploratory snippets may not run sequentially.
# Original example student names (if present) are anonymized before entering the public destination.


# ========= BEGIN SOURCE: Assignment1.py =========

data = {
    "FGS00001":{"name":"Student 01","score":10},
    "FGS00002":{"name":"Student 02","score":9},
    "FGS00003":{"name":"Student 03","score":8},
    "FGS00004":{"name":"Student 04","score":7},
    "FGS00005":{"name":"Student 05","score":6},
    "FGS00006":{"name":"Student 06","score":5},
    "FGS00007":{"name":"Student 07","score":4}
}

### HELPER LAY SET DIEM
def getSetScore():    
    setScore = set()
    for vals in data.values():
        setScore.add(int(vals["score"]))
    return(setScore)

### HIEN THI SINH VIEN ###
def showAll():
    print("""          
******************** DANH SACH SINH VIEN ********************""")
    stt = 1
    for id,vals in data.items():
        extraSpace = (25 - len(vals["name"])) * " "
        print(f"{stt}. {id}  {vals["name"]}{extraSpace}  {vals["score"]}")
        stt += 1
    print("")
    return

### THEM SINH VIEN
def add():
    global data
    print("""          
*************************** THEM SINH VIEN ********************************
- Thong tin nhap vao cach nhau bang dau ";". Vi du: FGS00008;Phan The Duy;3
  Trong do FGS00008 la MSSV, Phan The Duy la ten, 3 la diem so.
- Diem so phai <=0 va >=10 va la so nguyen.
- De trong thong tin va enter de quay lai menu chinh.
*************************** THEM SINH VIEN ********************************""")
    # Clear info
    info = None
    
    # Yeu cau nhap thong tin dau vao
    inputData = input("Thong tin sinh vien: ")
    
    # Neu de trong se dua ve menu chinh
    if inputData == "":
        print("!!! [Chuyen huong]: Quay lai menu chinh")
        print("")
        return
        
    # Check du lieu nhap co dung block khong
    info = inputData.split(";")
    if len(info) != 3:
        print("!!! [Bao loi]: Du lieu nhap vao khong hop le.")
        add()
    
    # Xu ly du lieu nhap vao
    id = info[0].strip()
    name = info[1].strip()
    score = info[2].strip()
    
    # Check diem so co hop le hay khong
    if score.isnumeric():
        score = int(score)
        if score < 0 or score >10:
            print("!!! [Bao loi]: Diem so nhap vao khong hop le.")
            add()
    else:
        print("!!! [Bao loi]: Diem so nhap vao khong hop le.")
        add()
    
    # Kiem tra ID ton tai hay chua
    if id in data:
        print("!!! [Bao loi]: Ma so sinh vien da ton tai.")
        add()
    
    # Them sinh vien vao data    
    data[id]={"name":name,"score":score}
    print("!!! [Thanh cong] Da them sinh vien thanh cong.")        
    add()


### CAP NHAT THONG TIN SINH VIEN
def update():
    global data
    print("""          
************************** CAP NHAT THONG TIN *****************************
- Thong tin nhap vao cach nhau bang dau ";". Vi du: FGS00008;Phan The Duy;3
  Trong do FGS00008 la MSSV, Phan The Duy la ten, 3 la diem so
- Diem so phai <=0 va >=10 va la so nguyen.
- De trong thong tin va enter de quay lai menu chinh.
************************** CAP NHAT THONG TIN *****************************""")
    
    # Yeu cau nhap thong tin dau vao
    inputData = input("Thong tin sinh vien: ")
    
    # Neu de trong se dua ve menu chinh
    if inputData == "":
        print("!!! [Chuyen huong]: Quay lai menu chinh")
        print("")
        return
        
    # Check du lieu nhap co dung block khong
    info = inputData.split(";")
    if len(info) != 3:
        print("!!! [Bao loi]: Du lieu nhap vao khong hop le.")
        update()
    
    # Xu ly du lieu nhap vao
    id = info[0].strip()
    name = info[1].strip()
    score = info[2].strip()
    
    # Check diem so co hop le hay khong
    if score.isnumeric():
        score = int(score)
        if score < 0 or score >10:
            print("!!! [Bao loi]: Diem so nhap vao khong hop le.")
            update()
    else:
        print("!!! [Bao loi]: Diem so nhap vao khong hop le.")
        update()
    
    # Kiem tra ID ton tai hay chua
    if id not in data:
        print("!!! [Bao loi]: Ma so sinh vien khong ton tai.")
        update()
    
    # Cap nhat thong tin sinh vien
    data[id]={"name":name,"score":score}
    print("!!! [Thanh cong] Cap nhat sinh vien thanh cong.")        
    update()


### XOA SINH VIEN
def delete():
    global data
    print("""          
************* XOA THONG TIN SINH VIEN ***************
- Yeu cau thong tin nhap vao la MSSV. Vi du: FGS00007
- De trong thong tin va enter de quay lai menu chinh.
************* XOA THONG TIN SINH VIEN ***************""")
    
    # Clear inputConfirm
    inputConfirm = None
    
    # Yeu cau nhap thong tin dau vao
    inputData = input("Ma so sinh vien: ")
    
    # Neu de trong se dua ve menu chinh
    if inputData == "":
        print("!!! [Chuyen huong]: Quay lai menu chinh")
        print("")
        return
        
    # Xu ly du lieu nhap vao
    id = inputData.strip()
    
    # Kiem tra ID ton tai hay chua
    if id not in data:
        print("!!! [Bao loi]: Ma so sinh vien khong ton tai.")
        delete()
    
    # xac nhan xoa
    inputConfirm = input("Xac nhan xoa!? (Y/N): ")
    if inputConfirm.lower() == "y":   
        del data[id]
        print("!!! [Thanh cong] Xoa thong tin sinh vien thanh cong.")        
        delete()
    else:
        print("!!! [Bao loi] Da huy thao tac xoa thong tin sinh vien.")
        delete()



### LOC SINH VIEN THEO DIEM SO
def sort(sortType):
    # LAY CaC GIA TRI DIEM
    setScore = getSetScore()
    
    # XU LY TANG/GIAM
    if sortType == "desc":
        print("""          
********* DANH SACH SINH VIEN VOI DIEM SO TANG DAN **********""")        
        listScore = sorted(setScore)
    else:
        print("""          
********* DANH SACH SINH VIEN VOI DIEM SO GIAM DAN **********""")
        listScore = sorted(setScore,reverse=True)
    
    # HIEN THI DANH SACH
    stt = 1
    for score in listScore:
        for id,vals in data.items():
            if int(vals["score"]) == score:
                extraSpace = (25 - len(vals["name"])) * " "
                print(f"{stt}. {id}  {vals["name"]}{extraSpace}  {vals["score"]}")
                stt += 1
    print("")
    return          

### THONG KE NANG CAO
def statistic():
    # HELPER LAY TEN BANG DIEM
    def getNamesByScore(score):
        names = [] 
        for id,vals in data.items():
            if int(vals["score"]) == int(score):
                names.append(vals["name"])
        return(names)

    # HELPER XEP LOAI
    def classify(score):
        score = int(score)
        if score in [5,6]:
            return("Average")
        elif score in [7,8]:
            return("Good")
        elif score in [9,10]:
            return("Excellent")
        else:
            return("Poor")    
    
         
    # LAY DIEM LON NHAT NHO NHAT
    setScore = getSetScore()
    maxScore = max(setScore)
    minScore = min(setScore)
    maxNames = (", ").join(getNamesByScore(maxScore))
    minNames = (", ").join(getNamesByScore(minScore))
    
    # TONG SO MOI XEP LOAI, THU THAP DIEM SO DE TINH TRUN BINH
    scores = []
    poorCount = 0
    goodCount = 0
    excellentCount = 0
    averageCount = 0
    for vals in data.values():
        scores.append(int(vals["score"]))
        if classify(vals["score"]) == "Poor":
            poorCount += 1
        elif classify(vals["score"]) == "Good":
            goodCount += 1
        elif classify(vals["score"]) == "Excellent":
            excellentCount += 1
        else:
            averageCount += 1
    
    # DIEM TRUNG BINH
    average = round(sum(scores)/len(scores),1)
    
    # IN RA
    print("""          
********* THONG KE NANG CAO **********""")
    print(f"- Sinh vien có diem cao nhat: {maxNames.upper()} ({maxScore} diem)")
    print(f"- Sinh vien có diem thap nhat: {minNames.upper()} ({minScore} diem)")
    print(f"- Diem trung bình: {average}.")  
    print(f"- Sinh vien dat loai Yeu: {poorCount} sinh vien.")
    print(f"- Sinh vien dat loai Trung binh: {averageCount} sinh vien.")  
    print(f"- Sinh vien dat loai Kha: {goodCount} sinh vien.")  
    print(f"- Sinh vien dat loai Gioi: {excellentCount} sinh vien.")
    print("")               
    
# MENU()
def menu():
    # khai bao bien lua chon
    choice = 0
    while True:
        print("*********** MENU **************")
        print("1. Them sinh vien")
        print("2. Hien thi danh sach sinh vien")
        print("3. Cap nhat thong tin")
        print("4. Xoa thong tin sinh vien")
        print("5. Danh sach theo diem giam dan")
        print("6. Danh sach theo diem tang dan")
        print("7. Thong ke nang cao")
        print("*********** MENU **************")
        # nhap lua chon
        choice = int(input("Nhap lua chon(1-7): "))
        if choice == 1:
            add()
        elif choice == 2:
            showAll()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
        elif choice == 5:
            sort("asc")
        elif choice == 6:
            sort("desc")
        elif choice == 7:
            statistic()
        else:
            print("Chi nhap 1-7")

# goi ham
menu()


# ========= END SOURCE: Assignment1.py =========
