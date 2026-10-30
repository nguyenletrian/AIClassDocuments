# -*- coding: utf-8 -*-
"""BỘ CODE GỐC TỔNG HỢP 10 LAB VÀ BÀI TẬP - AIClassDocuments.

Mỗi bài được đặt trong MỘT hàm run riêng, giữ nguyên logic từ code đã
xuất bản trong exports/print/*/*.md. Mỗi lần chỉ chạy bài được chọn.
Các biến/hàm "main", "validate", "add" của các bài không đè lên nhau.

Cách dùng:
    python AIClassDocuments-TongHop-10-Lab-BaiTap.py --list
    python AIClassDocuments-TongHop-10-Lab-BaiTap.py lab-04
    python AIClassDocuments-TongHop-10-Lab-BaiTap.py pretest
    python AIClassDocuments-TongHop-10-Lab-BaiTap.py assignment-01 --demo
    python AIClassDocuments-TongHop-10-Lab-BaiTap.py lab-05 --demo
    python AIClassDocuments-TongHop-10-Lab-BaiTap.py lab-07 --no-plot

Lab 10 dùng PythoClass/main.py: phải có students.csv trong thư mục làm việc.
Các bài dùng NumPy, Pandas, SciPy, SymPy hoặc scikit-learn cần cài thư viện.
Chương trình không tự cài thư viện, không tự chạy cả 10 bài.
"""
from __future__ import annotations

import sys


# ===========================================================================
# Assignment 01 — Dictionary | Nguồn: exports/print/exercises/ASSIGNMENT-01.md
# ===========================================================================

def run_assignment_01():
    """Chạy duy nhất Assignment 01 — Dictionary."""
    from collections import Counter
    import sys


    def validate(student_id, name, score):  # Xác thực mã, tên và điểm trước khi thay đổi dữ liệu.
        student_id = student_id.strip()
        name = name.strip()
        if not student_id or not name:
            raise ValueError("Student ID and name are required.")  # Thông báo lỗi khi dữ liệu không hợp lệ.
        try:
            score = float(score)
        except (ValueError, TypeError) as error:  # Bắt ngoại lệ (exception: lỗi) để thông báo rõ.
            raise ValueError("Score must be numeric.") from error  # Thông báo lỗi khi dữ liệu không hợp lệ.
        if not 0 <= score <= 10:
            raise ValueError("Score must be between 0 and 10.")  # Thông báo lỗi khi dữ liệu không hợp lệ.
        return student_id, name, score


    def add(students, student_id, name, score):  # Kiểm tra trùng mã trước khi thêm sinh viên.
        student_id, name, score = validate(student_id, name, score)  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.
        if student_id in students:
            raise ValueError(f"Duplicate student ID: {student_id}")  # Thông báo lỗi khi dữ liệu không hợp lệ.
        students[student_id] = {"name": name, "score": score}  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.


    def display(students):
        if not students:
            print("No students stored.")
        for student_id, record in students.items():  # Duyệt lần lượt dữ liệu bằng vòng lặp (loop: lặp).
            print(f"{student_id} | {record['name']} | "
                  f"{record['score']:g}/10 | {classify(record['score'])}")  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.


    def update(students, student_id, new_name, new_score):
        if student_id not in students:
            raise KeyError(f"Unknown student ID: {student_id}")  # Thông báo lỗi khi dữ liệu không hợp lệ.
        _, name, score = validate(student_id, new_name, new_score)  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.
        students[student_id] = {"name": name, "score": score}  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.


    def delete(students, student_id, confirmed=False):
        if student_id not in students:
            raise KeyError(f"Unknown student ID: {student_id}")  # Thông báo lỗi khi dữ liệu không hợp lệ.
        if not confirmed:
            return False
        del students[student_id]  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.
        return True


    def classify(score):
        if score >= 9:
            return "Excellent"
        if score >= 7:
            return "Good"
        if score >= 5:
            return "Average"
        return "Poor"


    def sort_by_score(students, descending=False):
        return sorted(
            students.items(),  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.
            key=lambda pair: pair[1]["score"],
            reverse=descending,
        )  # Đóng danh sách, biểu thức hoặc tập giá trị đang tạo.


    def statistics(students):  # Thống kê số lượng và phân loại điểm từ dữ liệu hiện có.
        if not students:
            return None
        scores = [item["score"] for item in students.values()]
        counts = Counter(classify(score) for score in scores)
        return {
            "highest": max(scores),  # Lưu trường tên khóa (key: khóa) và kết quả vào từ điển.
            "lowest": min(scores),  # Lưu trường tên khóa (key: khóa) và kết quả vào từ điển.
            "average": sum(scores) / len(scores),  # Lưu trường tên khóa (key: khóa) và kết quả vào từ điển.
            "classification_counts": dict(counts),  # Lưu trường tên khóa (key: khóa) và kết quả vào từ điển.
        }  # Đóng danh sách, biểu thức hoặc tập giá trị đang tạo.


    def sample_students():
        scores = [9.5, 8, 7.5, 6, 5.5, 4.5, 7, 9, 8.5, 6.5, 10, 5]
        students = {}
        for number, score in enumerate(scores, start=1):  # Duyệt lần lượt dữ liệu bằng vòng lặp (loop: lặp).
            add(students, f"S{number:03d}", f"Learner {number:02d}", score)  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.
        return students


    def run_demo():
        students = sample_students()
        if not (len(students) == 12): raise ValueError("Kết quả kiểm tra không đúng")  # Dùng if (nếu) thay lệnh kiểm tra assert trước đây; báo lỗi khi dữ liệu không đạt.
        add(students, "S013", "New Learner", 8)  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.
        update(students, "S013", "Updated Learner", 8.5)  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.
        if not (delete(students, "S013", confirmed=False) is False): raise ValueError("Kết quả kiểm tra không đúng")  # Dùng if (nếu) thay lệnh kiểm tra assert trước đây; báo lỗi khi dữ liệu không đạt.
        if not ("S013" in students): raise ValueError("Kết quả kiểm tra không đúng")  # Dùng if (nếu) thay lệnh kiểm tra assert trước đây; báo lỗi khi dữ liệu không đạt.
        if not (delete(students, "S013", confirmed=True) is True): raise ValueError("Kết quả kiểm tra không đúng")  # Dùng if (nếu) thay lệnh kiểm tra assert trước đây; báo lỗi khi dữ liệu không đạt.
        if not ("S013" not in students): raise ValueError("Kết quả kiểm tra không đúng")  # Dùng if (nếu) thay lệnh kiểm tra assert trước đây; báo lỗi khi dữ liệu không đạt.
        if not (len(students) == 12): raise ValueError("Kết quả kiểm tra không đúng")  # Dùng if (nếu) thay lệnh kiểm tra assert trước đây; báo lỗi khi dữ liệu không đạt.

        print("Ascending scores (first 4):", sort_by_score(students)[:4])
        print("Descending scores (first 4):",
              sort_by_score(students, descending=True)[:4])  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.
        print("Statistics:", statistics(students))
        print("Student list:")
        display(students)  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.


    def interactive_menu():  # Điều khiển các thao tác CRUD từ menu.
        students = sample_students()
        menu = "\n1.Display 2.Add 3.Update 4.Delete 5.Sort 6.Statistics 0.Exit"
        while True:  # Lặp khi điều kiện còn đúng, dừng khi sai.
            print(menu)
            action = input("Choose: ").strip()
            try:
                if action == "0":
                    break  # Thoát vòng lặp tại vị trí này.
                elif action == "1":  # Kiểm tra trường hợp thay thế sau nhánh trước.
                    display(students)  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.
                elif action == "2":  # Kiểm tra trường hợp thay thế sau nhánh trước.
                    add(students, input("ID: "), input("Name: "),  # Nhận input (dữ liệu nhập) rồi kiểm tra trước khi dùng.
                        input("Score [0,10]: "))  # Nhận input (dữ liệu nhập) rồi kiểm tra trước khi dùng.
                elif action == "3":  # Kiểm tra trường hợp thay thế sau nhánh trước.
                    key = input("ID to update: ").strip()
                    update(students, key, input("New name: "), input("New score: "))  # Nhận input (dữ liệu nhập) rồi kiểm tra trước khi dùng.
                elif action == "4":  # Kiểm tra trường hợp thay thế sau nhánh trước.
                    key = input("ID to delete: ").strip()
                    answer = input("Confirm deletion? [y/N]: ").strip().lower()
                    if not delete(students, key, confirmed=(answer == "y")):
                        print("Deletion cancelled.")
                elif action == "5":  # Kiểm tra trường hợp thay thế sau nhánh trước.
                    descending = input("Descending? [y/N]: ").strip().lower() == "y"
                    for key, item in sort_by_score(students, descending):  # Duyệt lần lượt dữ liệu bằng vòng lặp (loop: lặp).
                        print(key, item)
                elif action == "6":  # Kiểm tra trường hợp thay thế sau nhánh trước.
                    print(statistics(students))
                else:  # Xử lý trường hợp còn lại.
                    print("Unknown menu option.")
            except (ValueError, KeyError) as error:  # Bắt ngoại lệ (exception: lỗi) để thông báo rõ.
                print("Input error:", error)

    # Điểm bắt đầu chạy của bài gốc:
    if "--demo" in sys.argv:
        run_demo()  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.
    else:  # Xử lý trường hợp còn lại.
        interactive_menu()  # Tiếp tục thao tác theo cấu trúc dữ liệu và phép tính trong code đã học.


# ===========================================================================
# Lab 04 — Điều kiện và vòng lặp | Nguồn: exports/print/labs/LAB-04.md
# ===========================================================================

def run_lab_04():
    """Chạy duy nhất Lab 04 — Điều kiện và vòng lặp."""
    from math import isqrt

    def task01_sort_three(a, b, c):  # So sánh và đổi chỗ để sắp xếp ba số.
        if a > b: a, b = b, a
        if b > c: b, c = c, b
        if a > b: a, b = b, a
        return a, b, c

    def task02_quarter(month):
        if not 1 <= month <= 12: raise ValueError("Month must be 1..12")
        if month <= 3: return 1
        elif month <= 6: return 2  # Xét điều kiện tiếp theo nếu nhánh trước không thỏa.
        elif month <= 9: return 3  # Xét điều kiện tiếp theo nếu nhánh trước không thỏa.
        else: return 4  # Xử lý trường hợp ngược lại hoặc còn lại.

    def leap_year(year):
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

    def task03_month_days(month, year=2026):
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        if not 1 <= month <= 12: raise ValueError("Month must be 1..12")
        return 29 if month == 2 and leap_year(year) else days[month-1]

    def task04_is_leap(year):
        if year < 1: raise ValueError("Year must be positive")
        return leap_year(year)

    WORDS = ["khong","mot","hai","ba","bon","nam","sau","bay","tam","chin"]

    def task05_two_digit(n):
        if not 10 <= n <= 99: raise ValueError("Expected two-digit integer")
        tens, unit = divmod(n,10)
        if tens == 1:
            head = "muoi"
        else:  # Xử lý trường hợp ngược lại hoặc còn lại.
            head = WORDS[tens] + " muoi"
        if unit == 0: return head
        if unit == 5: return head + " lam"
        if unit == 1 and tens > 1: return head + " mot"
        return head + " " + WORDS[unit]

    def task06_three_digit(n):
        if not 100 <= n <= 999: raise ValueError("Expected three-digit integer")
        hundred, rest = divmod(n,100)
        head = WORDS[hundred] + " tram"
        if rest == 0: return head
        if rest < 10:
            return head + " linh " + ("nam" if rest == 5 else WORDS[rest])
        return head + " " + task05_two_digit(rest)

    def task07_electricity_bill(kwh):  # Tính lần lượt từng bậc giá, không áp một giá cho toàn bộ điện.
        if kwh < 0: raise ValueError("Usage cannot be negative")
        remaining = float(kwh)
        total = 0.0
        for width, rate in ((50,1800),(50,2000),(100,2500)):
            amount = min(remaining,width)
            total += amount * rate
            remaining -= amount
            if remaining <= 0: return total
        return total + remaining * 3000

    def task08_sum_to_n(n):
        if n <= 0: raise ValueError("n must be positive")
        total=0
        for value in range(1,n+1): total += value
        return total

    def task09_count_digits(n):
        if n <= 0: raise ValueError("n must be positive")
        count=0
        while n:  # Tiếp tục vòng lặp khi điều kiện còn đúng.
            count += 1
            n //= 10
        return count

    def task10_is_prime(n):  # Chỉ thử ước tới căn bậc hai của n.
        if n <= 1: return False
        for divisor in range(2,isqrt(n)+1):
            if n % divisor == 0: return False
        return True

    def task11_gcd(a,b):  # Thuật toán Euclid lấy phần dư liên tiếp.
        if a<=0 or b<=0: raise ValueError("Both numbers must be positive")
        while b:  # Tiếp tục vòng lặp khi điều kiện còn đúng.
            a,b=b,a%b
        return a

    def task12_rectangle(rows,cols):
        if rows <= 0 or cols <= 0: raise ValueError("Rows/cols must be positive")
        output=[]
        for _ in range(rows):
            line=""
            for _ in range(cols):
                line += "*"
            output.append(line)  # Thêm phần tử vào cuối danh sách bằng append (thêm cuối).
        return "\n".join(output)

    def task13_repeated_triangle(n):
        if n <= 0: raise ValueError("n must be positive")
        output=[]
        for i in range(1,n+1):
            line=""
            for _ in range(i):
                line += str(i)
            output.append(line)  # Thêm phần tử vào cuối danh sách bằng append (thêm cuối).
        return "\n".join(output)

    def task14_consecutive_triangle(n):  # Vòng lặp lồng nhau tạo từng dòng của hình.
        if n <= 0: raise ValueError("n must be positive")
        rows=[]
        current=1
        for i in range(1,n+1):
            values=[]
            for _ in range(i):
                values.append(str(current))  # Thêm phần tử vào cuối danh sách bằng append (thêm cuối).
                current += 1
            rows.append(" ".join(values))  # Thêm phần tử vào cuối danh sách bằng append (thêm cuối).
        return "\n".join(rows)

    def main():
        if not (task01_sort_three(8.5,3.2,6.7)==(3.2,6.7,8.5)): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (task02_quarter(5)==2): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (task03_month_days(2,2024)==29): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (task04_is_leap(2024) and not task04_is_leap(2023)): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (task05_two_digit(25)=="hai muoi lam"): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (task06_three_digit(123)=="mot tram hai muoi ba"): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (task07_electricity_bill(120)==240000): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (task08_sum_to_n(10)==55): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (task09_count_digits(123456)==6): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (task10_is_prime(17) and not task10_is_prime(1)): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (task11_gcd(24,36)==12): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (task12_rectangle(4,6)=="******\n******\n******\n******"): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (task13_repeated_triangle(5)=="1\n22\n333\n4444\n55555"): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (task14_consecutive_triangle(4)=="1\n2 3\n4 5 6\n7 8 9 10"): raise ValueError("Kiểm tra dữ liệu không đạt")
        print("PASS: 14 exercises")
        print("Example electricity 120 kWh:",task07_electricity_bill(120),"VND")
        print("Pattern:",task14_consecutive_triangle(4),sep="\n")

    # Điểm bắt đầu chạy của bài gốc:
    main()


# ===========================================================================
# Lab 05 — Danh sách sinh viên | Nguồn: exports/print/labs/LAB-05.md
# ===========================================================================

def run_lab_05():
    """Chạy duy nhất Lab 05 — Danh sách sinh viên."""
    import sys

    def validate(student_id,name,score):  # Bảo đảm mã, tên và điểm hợp lệ trước khi thao tác.
        sid=student_id.strip()
        name=name.strip()
        if not sid or not name: raise ValueError("ID and name are required")
        try: score=float(score)
        except ValueError as e: raise ValueError("Score must be numeric") from e
        if not 0<=score<=10: raise ValueError("Score must be in 0..10")
        return {"id":sid,"name":name,"score":score}

    def add(students,student_id,name,score):
        data=validate(student_id,name,score)
        if any(item["id"]==data["id"] for item in students):
            raise ValueError("Duplicate student ID")  # Chủ động báo lỗi đầu vào thay vì chấp nhận dữ liệu sai.
        students.append(data)  # Thêm phần tử vào cuối danh sách bằng append (thêm cuối).

    def find_by_name(students,name):  # Tìm theo tên sau khi chuẩn hóa chuỗi.
        query=name.strip().casefold()
        if not query: return []
        return [s for s in students if query in s["name"].casefold()]

    def delete_by_id(students,student_id):
        for index,s in enumerate(students):
            if s["id"]==student_id:
                return students.pop(index)
        raise KeyError(student_id)  # Chủ động báo lỗi đầu vào thay vì chấp nhận dữ liệu sai.

    def sorted_by_score(students,descending=False):  # Xếp thứ tự theo điểm bằng khóa so sánh.
        return sorted(students,key=lambda s:s["score"],reverse=descending)

    def statistics(students):
        if not students: return None
        return {"highest":max(students,key=lambda s:s["score"]),
                "lowest":min(students,key=lambda s:s["score"]),  # Gắn tên trường (key: khóa) với giá trị trong từ điển.
                "average":sum(s["score"] for s in students)/len(students)}  # Gắn tên trường (key: khóa) với giá trị trong từ điển.

    def show(students):
        for s in students:
            print(f'{s["id"]} | {s["name"]} | {s["score"]:g}/10')

    def sample():
        students=[]
        grades=[5,6,7,8,9,10,5.5,6.5,7.5,8.5,9.5,4]
        for i,score in enumerate(grades,1):
            add(students,f"S{i:03}",f"Learner {i:02}",score)
        return students

    def run_demo():
        students=sample()
        if not (len(students)==12): raise ValueError("Kiểm tra dữ liệu không đạt")
        add(students,"S013","Learner 13",7)
        if not (len(find_by_name(students,"learner"))==13): raise ValueError("Kiểm tra dữ liệu không đạt")
        removed=delete_by_id(students,"S013")
        if not (removed["id"]=="S013" and len(students)==12): raise ValueError("Kiểm tra dữ liệu không đạt")
        print("Sorted:",[(s["id"],s["score"]) for s in sorted_by_score(students)])
        print("Statistics:",statistics(students))
        show(students)

    def interactive():  # Menu cho phép thực hiện nhiều thao tác liên tiếp.
        students=sample()
        while True:  # Tiếp tục vòng lặp khi điều kiện còn đúng.
            print("\n1.Add 2.Display 3.Search 4.Delete 5.Sort 6.Statistics 0.Exit")
            c=input("Choice: ").strip()
            try:
                if c=="0":break
                elif c=="1": add(students,input("ID: "),input("Name: "),input("Score: "))  # Xét điều kiện tiếp theo nếu nhánh trước không thỏa.
                elif c=="2":show(students)  # Xét điều kiện tiếp theo nếu nhánh trước không thỏa.
                elif c=="3":show(find_by_name(students,input("Name to search: ")))  # Xét điều kiện tiếp theo nếu nhánh trước không thỏa.
                elif c=="4":delete_by_id(students,input("ID: ").strip())  # Xét điều kiện tiếp theo nếu nhánh trước không thỏa.
                elif c=="5":  # Xét điều kiện tiếp theo nếu nhánh trước không thỏa.
                    show(sorted_by_score(students,input("Descending? [y/N] ").lower()=="y"))  # Nhận input (dữ liệu nhập) để xử lý và kiểm tra.
                elif c=="6":print(statistics(students))  # Xét điều kiện tiếp theo nếu nhánh trước không thỏa.
                else:print("Unknown menu option")  # Xử lý trường hợp ngược lại hoặc còn lại.
            except (ValueError,KeyError) as exc:
                print("Error:",exc)

    # Điểm bắt đầu chạy của bài gốc:
    run_demo() if "--demo" in sys.argv else interactive()


# ===========================================================================
# Lab 05–06 — Hồi quy và Gradient Descent | Nguồn: exports/print/labs/LAB-05-06.md
# ===========================================================================

def run_lab_05_06():
    """Chạy duy nhất Lab 05–06 — Hồi quy và Gradient Descent."""
    import sys
    from pathlib import Path
    import numpy as np
    import sympy as sp

    X = np.array([1,2,3,4,5,6,7,8], dtype=float)
    Y = np.array([35,40,50,55,65,70,80,85], dtype=float)

    def predict(x,w,b):
        return w*x+b

    def compute_loss(y_true,y_pred):  # MSE là trung bình bình phương sai số dự đoán.
        return float(np.mean((y_true-y_pred)**2))

    def task01_dataset():
        if not (X.shape == Y.shape == (8,)): raise ValueError("Kiểm tra dữ liệu không đạt")
        return {"hours":X.tolist(),"scores":Y.tolist()}

    def task02_initial_model():
        guesses = predict(X,0.0,0.0)
        initial_loss = compute_loss(Y,guesses)
        return guesses,initial_loss

    def task03_symbolic_single():  # Dùng SymPy để tìm đạo hàm, không đoán gradient.
        w,b=sp.symbols("w b",real=True)
        loss=(2*w+b-5)**2
        variables=(w,b)
        gradient=sp.Matrix([sp.diff(loss,v) for v in variables])
        hessian=sp.hessian(loss,variables)
        return loss,gradient,hessian

    def task04_train(learning_rate=0.01,epochs=1000):  # Lặp cập nhật w và b theo chiều ngược gradient.
        w=b=0.0
        history=[]
        n=X.size
        for _ in range(epochs):
            residual=predict(X,w,b)-Y
            dw=(2/n)*np.dot(X,residual)
            db=(2/n)*residual.sum()  # Đếm hoặc cộng phần tử để tính tổng/tỷ lệ.
            w-=learning_rate*dw
            b-=learning_rate*db
            history.append(compute_loss(Y,predict(X,w,b)))  # Thêm phần tử vào cuối danh sách bằng append (thêm cuối).
        return w,b,np.array(history)

    def task05_symbolic_full(trained_w,trained_b):  # So sánh gradient và Hessian khi mô hình có hai tham số.
        w,b=sp.symbols("w b",real=True)
        values=[sp.Integer(int(x)) for x in X]
        targets=[sp.Integer(int(y)) for y in Y]
        n=len(values)
        full_loss=sum((yi-w*xi-b)**2 for xi,yi in zip(values,targets))/n
        gradient=sp.Matrix([sp.diff(full_loss,w),sp.diff(full_loss,b)])
        hessian=sp.hessian(full_loss,(w,b))
        gradient_at=gradient.subs({w:trained_w,b:trained_b}).evalf()
        eigvals=np.linalg.eigvalsh(np.asarray(hessian,dtype=float))
        return gradient,hessian,gradient_at,eigvals

    def save_plots(w,b,losses):
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        root=Path(__file__).resolve().parent/"outputs"
        root.mkdir(exist_ok=True)
        fig,ax=plt.subplots()
        ax.scatter(X,Y,label="Observed scores")
        ax.plot(X,predict(X,w,b),label="Fitted prediction")
        ax.set(xlabel="Study hours",ylabel="Exam score (points)",title="Hours vs. exam scores")
        ax.grid(True)
        ax.legend()
        fig.savefig(root/"hours_vs_scores.png",dpi=140,bbox_inches="tight")
        plt.close(fig)  # Đóng biểu đồ sau khi dùng để giải phóng bộ nhớ.
        fig,ax=plt.subplots()
        ax.plot(np.arange(1,len(losses)+1),losses)
        ax.set(xlabel="Epoch",ylabel="MSE (squared score units)",title="Gradient Descent Training")
        ax.grid(True)
        fig.savefig(root/"loss_curve.png",dpi=140,bbox_inches="tight")
        plt.close(fig)  # Đóng biểu đồ sau khi dùng để giải phóng bộ nhớ.
        print("Wrote",root/"hours_vs_scores.png","and",root/"loss_curve.png")

    def main():
        task01_dataset()
        initial_preds,initial_mse=task02_initial_model()
        example_loss,example_grad,example_hessian=task03_symbolic_single()
        w,b,history=task04_train(learning_rate=0.01,epochs=1000)
        full_grad,full_hessian,at_final,eigenvalues=task05_symbolic_full(w,b)
        final_mse=compute_loss(Y,predict(X,w,b))
        if not (history.shape==(1000,)): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (final_mse < initial_mse): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (all(eigenvalues > 0)): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (np.isclose(final_mse,history[-1])): raise ValueError("Kiểm tra dữ liệu không đạt")
        print("Initial predictions:",initial_preds)
        print("Initial MSE:",round(initial_mse,3))
        print("Single-sample symbolic loss:",example_loss)
        print("Single-sample gradient:",example_grad,"Hessian:",example_hessian)
        print(f"Trained w={w:.6f}, b={b:.6f}, final MSE={final_mse:.6f}")
        print("Full gradient:",full_grad)
        print("Full Hessian:",full_hessian)
        print("Gradient evaluated at trained parameters:",at_final)
        print("Hessian eigenvalues:",eigenvalues)
        if "--no-plot" not in sys.argv:
            save_plots(w,b,history)

    # Điểm bắt đầu chạy của bài gốc:
    main()


# ===========================================================================
# Lab 07 — Xác suất | Nguồn: exports/print/labs/LAB-07.md
# ===========================================================================

def run_lab_07():
    """Chạy duy nhất Lab 07 — Xác suất."""
    from pathlib import Path
    import sys
    import numpy as np
    from scipy.stats import binom

    SEED=2026
    TRIALS=5000

    def task01_cards():  # Dùng giao/hợp tập hợp để đếm biến cố.
        space=set(range(1,11))
        a={x for x in space if x%2==0}
        b={x for x in space if x>6}
        return {
            "space":sorted(space),"A":sorted(a),"B":sorted(b),  # Gắn tên trường (key: khóa) với giá trị trong từ điển.
            "P(A)":len(a)/len(space),  # Gắn tên trường (key: khóa) với giá trị trong từ điển.
            "P(B)":len(b)/len(space),  # Gắn tên trường (key: khóa) với giá trị trong từ điển.
            "P(A and B)":len(a&b)/len(space),  # Gắn tên trường (key: khóa) với giá trị trong từ điển.
            "P(A or B)":len(a|b)/len(space),  # Gắn tên trường (key: khóa) với giá trị trong từ điển.
        }  # Đóng danh sách, mảng hoặc nhóm tham số đang xây dựng.

    def task02_free_throws():  # Mô phỏng phép thử ngẫu nhiên với seed để tái lập.
        rng=np.random.default_rng(SEED)
        single=rng.random(TRIALS)<0.7
        first=rng.random(TRIALS)<0.7
        second=rng.random(TRIALS)<0.6
        both=first & second
        either=first | second
        return {
            "experimental_single":single.mean(),  # Gắn tên trường (key: khóa) với giá trị trong từ điển.
            "experimental_both":both.mean(),  # Gắn tên trường (key: khóa) với giá trị trong từ điển.
            "experimental_either":either.mean(),  # Gắn tên trường (key: khóa) với giá trị trong từ điển.
            "theoretical_single":0.7,  # Gắn tên trường (key: khóa) với giá trị trong từ điển.
            "theoretical_both":0.7*0.6,  # Gắn tên trường (key: khóa) với giá trị trong từ điển.
            "theoretical_either":1-(1-0.7)*(1-0.6),  # Gắn tên trường (key: khóa) với giá trị trong từ điển.
        }  # Đóng danh sách, mảng hoặc nhóm tham số đang xây dựng.

    def task03_conditional_days():
        A=set(range(5))
        B=set(range(4))
        theoretical=len(A&B)/len(B)
        rng=np.random.default_rng(SEED+1)
        drawn=rng.integers(0,7,size=TRIALS)
        given_b=np.isin(drawn,list(B))
        joint=np.isin(drawn,list(A&B))
        experimental=float(joint.sum()/given_b.sum())  # Đếm hoặc cộng phần tử để tính tổng/tỷ lệ.
        return theoretical,experimental

    def task04_bayes():  # Kết hợp xác suất nền và độ nhạy để tính posterior.
        p_spam=0.30
        p_flag_given_spam=0.90
        p_flag_given_clean=0.05
        p_flag=p_spam*p_flag_given_spam+(1-p_spam)*p_flag_given_clean
        posterior=p_spam*p_flag_given_spam/p_flag
        return p_flag,posterior

    def task05_binomial():  # Phân phối nhị thức: số lần thành công trong n lượt độc lập.
        k=np.arange(0,9)
        probs=binom.pmf(k,n=8,p=0.75)  # Dùng hàm xác suất/kiểm định đúng tham số của đề.
        return k,probs,float(binom.pmf(6,n=8,p=0.75)),float(probs[6:].sum())

    def save_plot(k,probs):
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        folder=Path(__file__).resolve().parent/"outputs"
        folder.mkdir(exist_ok=True)
        fig,ax=plt.subplots()
        ax.bar(k,probs)
        ax.set(xlabel="Number of resolved requests (k)",ylabel="P(X=k)",title="Binomial(n=8, p=0.75)")
        ax.set_xticks(k)
        ax.grid(True,axis="y")
        target=folder/"binomial_distribution.png"
        fig.savefig(target,dpi=140,bbox_inches="tight")
        plt.close(fig)  # Đóng biểu đồ sau khi dùng để giải phóng bộ nhớ.
        print("Saved:",target)

    def main():
        cards=task01_cards()
        simulated=task02_free_throws()
        cond_theory,cond_exp=task03_conditional_days()
        p_flag,p_actual_spam=task04_bayes()
        k,prob,p_exact,p_at_least=task05_binomial()
        if not (cards["P(A)"]==0.5): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (cards["P(B)"]==0.4): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (cards["P(A and B)"]==0.2): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (cards["P(A or B)"]==0.7): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (cond_theory==1.0): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (abs(simulated["experimental_single"]-0.7)<0.04): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (np.isclose(p_flag,0.305)): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (np.isclose(prob.sum(),1)): raise ValueError("Kiểm tra dữ liệu không đạt")
        print("Task 1:",cards)
        print("Task 2:",simulated)
        print("Task 3 P(A|B), theoretical/experimental:",cond_theory,cond_exp)
        print("Task 4 P(flag), P(spam|flag):",round(p_flag,5),round(p_actual_spam,5))
        print("Task 5 P(X=6), P(X>=6):",round(p_exact,6),round(p_at_least,6))
        if "--no-plot" not in sys.argv:
            save_plot(k,prob)

    # Điểm bắt đầu chạy của bài gốc:
    main()


# ===========================================================================
# Lab 08 — Thống kê | Nguồn: exports/print/labs/LAB-08.md
# ===========================================================================

def run_lab_08():
    """Chạy duy nhất Lab 08 — Thống kê."""
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

    def task01_descriptive(values):  # Tính trung bình, trung vị, mode và độ phân tán.
        return {
            "mean":float(values.mean()),"median":float(np.median(values)),
            "mode":float(pd.Series(values).mode().iloc[0]),
            "minimum":float(values.min()),"maximum":float(values.max()),
            "range":float(np.ptp(values)),
            "sample_variance":float(values.var(ddof=1)),
            "sample_std":float(values.std(ddof=1)),
        }

    def task02_frequency(values):  # Chia thời lượng thành các khoảng và đếm theo nhóm.
        bins=[0,60,120,180,240,360,500]
        labels=["0–<60","60–<120","120–<180","180–<240","240–<360","360–<500"]
        groups=pd.cut(values,bins=bins,labels=labels,right=False,include_lowest=True)
        freq=pd.Series(groups).value_counts(sort=False)
        frame=pd.DataFrame({"frequency":freq})
        frame["cumulative"]=frame["frequency"].cumsum()
        if not (frame["frequency"].sum()==len(values)): raise ValueError("Kiểm tra không đạt")
        return bins,frame

    def task03_outliers(values):  # Dùng quy tắc IQR để đánh dấu giá trị bất thường.
        q1,q2,q3=np.percentile(values,[25,50,75])
        iqr=q3-q1
        low,high=q1-1.5*iqr,q3+1.5*iqr
        unusual=values[(values<low)|(values>high)]
        return q1,q2,q3,iqr,low,high,unusual

    def task04_sample_and_test(values):  # Rút mẫu ngẫu nhiên trước khi làm t-test.
        rng=np.random.default_rng(2026)  # Rút mẫu ngẫu nhiên; seed (hạt giống) giúp tái lập.
        sample=rng.choice(values,size=10,replace=False)  # Rút mẫu ngẫu nhiên; seed (hạt giống) giúp tái lập.
        result=stats.ttest_1samp(values,popmean=120.0)  # Tính thống kê theo hàm/tham số đã học.
        return sample,float(sample.mean()),float(result.statistic),float(result.pvalue)

    def task05_conclusion(descriptive,outliers,pvalue):  # Viết nhận xét dựa trên kết quả, không suy diễn nhân quả.
        typical=descriptive["median"]
        decision="reject H0" if pvalue<0.05 else "fail to reject H0"
        print(f"Typical use is around median {typical:.1f} minutes/day.")
        print(f"Sample SD is {descriptive['sample_std']:.1f} minutes, with {len(outliers)} IQR outlier(s).")
        print(f"One-sample t-test vs 120 min/day: p={pvalue:.6g}; {decision} at alpha=0.05.")
        print("Recommendation: study long-duration sessions separately and design user-friendly break reminders.")

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
        fig.savefig(target,dpi=140,bbox_inches="tight")  # Vẽ/lưu biểu đồ (plot: đồ thị) để diễn giải kết quả.
        plt.close(fig)  # Đóng biểu đồ để tránh giữ tài nguyên.
        print("Saved:",target)

    def main():
        if not (USAGE_MINUTES.shape==(50,)): raise ValueError("Kiểm tra không đạt")
        desc=task01_descriptive(USAGE_MINUTES)
        bins,freq=task02_frequency(USAGE_MINUTES)
        q1,q2,q3,iqr,lo,hi,outliers=task03_outliers(USAGE_MINUTES)
        sample,sample_mean,t,p=task04_sample_and_test(USAGE_MINUTES)
        if not (len(sample)==10): raise ValueError("Kiểm tra không đạt")
        if not (0<=p<=1): raise ValueError("Kiểm tra không đạt")
        print("Descriptive:",desc)
        print("Frequency:\n",freq.to_string())
        print(f"Q1={q1:.2f}, Q2={q2:.2f}, Q3={q3:.2f}, IQR={iqr:.2f}")
        print(f"Outlier limits [{lo:.2f},{hi:.2f}], values:",outliers.tolist())
        print("Sample of 10:",sample.tolist(),"sample mean:",round(sample_mean,2))
        print("t:",round(t,4),"p:",round(p,6))
        task05_conclusion(desc,outliers,p)
        if "--no-plot" not in sys.argv:
            save_plot(USAGE_MINUTES,bins)

    # Điểm bắt đầu chạy của bài gốc:
    main()


# ===========================================================================
# Lab 10 — CSV và phân tích điểm | Nguồn: exports/print/labs/LAB-10.md
# ===========================================================================

def run_lab_10():
    """Chạy duy nhất Lab 10 — CSV và phân tích điểm."""
    import pandas as pd  # Pandas (thư viện xử lý bảng dữ liệu) với tên ngắn pd.

    def inputHelper(data):  # Đọc đầu vào; chú ý kiểm tra kiểu bên dưới chưa chuyển chuỗi sang số.
        label = data["label"]
        formats = data["formats"]
        inputTemp = input(label)
        if inputTemp == "":
            return(None)
        blocks =  inputTemp.split(";")  # Tách chuỗi đầu vào tại dấu chấm phẩy.
                      

        if len(blocks) != len(formats):
            print("!!![ERROR] Input blocks is not correct!~")
                

        for i in range(len(formats)):
            if type(blocks[i]).__name__ != formats[i]:  # LƯU Ý: split trả chuỗi nên so kiểu bằng tên không thực sự xác thực dữ liệu.
                print("!!![ERROR] Input format is not corrects")
        return(blocks)
        
    def displayAll():  # In danh sách tên theo cột có khoảng trắng đầu trong CSV gốc.
        df = pd.read_csv("students.csv")  # Đọc students.csv ở thư mục chạy hiện tại thành DataFrame.
        print("""
    ==== DISPLAY ALL STUDENT =====""")
        students = df[" name"].values  # Lấy cột ' name' có dấu cách đầu theo CSV gốc PythoClass.
        stt = 1
        for student in students:
            print(f"{stt}. {student}")
            stt += 1

    def studentSearch():  # Lọc theo mã sinh viên.
        print("""
    ==== SEARCH STUDENT =====""")
        inputData = inputHelper({
            "label":"Please enter Student ID:",
            "formats":["str"]
        })
        if inputData:
            inputData = inputData[0]
            df = pd.read_csv("students.csv")  # Đọc students.csv ở thư mục chạy hiện tại thành DataFrame.
            result = df[df["student_id"] == inputData]
            if len(result)!=0:
                print(result)
            else:
                print("!!![ERROR] Student not found.")
            studentSearch()  # Gọi lại chính hàm tìm kiếm; lặp nhiều có thể tạo đệ quy quá sâu.
        else:
            return
        
    def studentAverage():  # Tính trung bình ba môn cho một sinh viên.
        print("""
    ==== STUDENT RESULT ====""")
        inputData = inputHelper({
            "label":"Please enter Student ID:",
            "formats":["str"]
        })
        if inputData:
            inputData = inputData[0]
            df = pd.read_csv("students.csv")  # Đọc students.csv ở thư mục chạy hiện tại thành DataFrame.
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
            studentAverage()  # Gọi lại hàm tính điểm; lặp nhiều có thể tạo đệ quy quá sâu.
        else:
            return

    def analyzeSubject():  # Thống kê theo từng cột môn học.
        print("""
    ==== SUBJECT PERFORMANCE ====""")
        df = pd.read_csv("students.csv")  # Đọc students.csv ở thư mục chạy hiện tại thành DataFrame.
        data = {
            "Average":[df["Python"].mean(),df["Math"].mean(),df["ML"].mean()],
            "Total":[df["Python"].sum(),df["Math"].sum(),df["ML"].sum()],
            "Highest":[df["Python"].max(),df["Math"].max(),df["ML"].max()],
            "Lowest":[df["Python"].min(),df["Math"].min(),df["ML"].min()],
        }
        dfShow = pd.DataFrame(data,index=["Python","Math","ML"])
        print(dfShow)


    def analyzeClass():  # groupby/merge tổng hợp kết quả theo lớp.
        print("""
    ===== CLASS PERFORMANCE =====""")
        df = pd.read_csv("students.csv")  # Đọc students.csv ở thư mục chạy hiện tại thành DataFrame.
        studentCount =  df.groupby("class_name")["student_id"].count()  # Nhóm theo lớp và đếm mã sinh viên.
        pythonMean =  df.groupby("class_name")["Python"].mean()
        mathMean =  df.groupby("class_name")["Math"].mean()
        mlMean =  df.groupby("class_name")["ML"].mean()
        result = pd.merge(studentCount,pythonMean,on="class_name",how="outer")  # Ghép các thống kê theo khóa class_name.
        result = pd.merge(result,mathMean,on="class_name",how="outer")  # Ghép các thống kê theo khóa class_name.
        result = pd.merge(result,mlMean,on="class_name",how="outer")  # Ghép các thống kê theo khóa class_name.
        result["Overall Average"] = (result["Python"] + result["Math"] +  result["ML"])/3  # Trung bình chung từ trung bình ba môn.
        
        
        result.reset_index(inplace=True)
        result.rename(columns={"student_id":"Students"}, inplace=True)
        result.rename(columns={"class_name":"Class"}, inplace=True)
        
        result = result.round(2)
        
        print(result)

    def top3():  # Chức năng 6: xếp hạng ba sinh viên có điểm trung bình cao nhất.
        print("""
    ===== TOP 3 STUDENTS =====""")
        df = pd.read_csv("students.csv")  # Đọc students.csv ở thư mục chạy hiện tại thành DataFrame.
        df["Average"] =   (df["Python"] + df["Math"] +  df["ML"])/3
        dfSorted = df.sort_values(by="Average",ascending=False)
        dfSorted.drop(columns=["Python","Math","ML"], inplace=True)
        dfSorted.rename(columns={"class_name":"Class","student_id":"Student ID"}, inplace=True)
        dfSorted = dfSorted.round(2)
        
        print(dfSorted.head(3))  # Chỉ hiển thị ba hàng đứng đầu.

    # MENU()
    def menu():  # Bảy lựa chọn của main.py gốc, không phải sáu chức năng của đề Word.
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

            inputData =input("Please select (1-7): ")
            if inputData.isnumeric():
                choice = int(inputData)
                if choice == 1:
                    displayAll()
                elif choice == 2:
                    studentSearch()  # Gọi lại chính hàm tìm kiếm; lặp nhiều có thể tạo đệ quy quá sâu.
                elif choice == 3:
                    studentAverage()  # Gọi lại hàm tính điểm; lặp nhiều có thể tạo đệ quy quá sâu.
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


# ===========================================================================
# Pretest — Ôn tập | Nguồn: exports/print/exercises/PRETEST.md
# ===========================================================================

def run_pretest():
    """Chạy duy nhất Pretest — Ôn tập."""
    import numpy as np

    STUDENT_NAMES = ["Student A", "Student B", "Student C", "Student D", "Student E"]

    student_data = np.array([
        [2, 60, 50],
        [3, 65, 55],
        [4, 75, 65],
        [5, 80, 70],
        [6, 95, 90],
    ], dtype=float)


    def task1_student_performance(data):  # Phân tích bảng 5 sinh viên và so sánh dự đoán với thực tế.
        if data.shape != (5, 3):
            raise ValueError("Expected the original 5-student x 3-column table.")

        study_hours = data[:, 0]
        attendance = data[:, 1]
        actual_scores = data[:, 2]

        mean_score = float(np.mean(actual_scores))  # Tính trung bình cộng các giá trị hợp lệ.

        population_sd = float(np.std(actual_scores, ddof=0))  # Tính độ lệch chuẩn để đo sự phân tán.
        sample_sd = float(np.std(actual_scores, ddof=1))  # Tính độ lệch chuẩn để đo sự phân tán.

        predicted_scores = 5 * study_hours + 0.2 * attendance + 10
        return mean_score, population_sd, sample_sd, predicted_scores


    def task2_probabilities(data):  # Đếm số điều kiện đúng bằng Boolean và tính xác suất.
        scores = data[:, 2]
        hours = data[:, 0]

        at_least_70 = scores >= 70
        at_least_4_hours = hours >= 4
        both_conditions = at_least_70 & at_least_4_hours

        probability_70 = float(np.count_nonzero(at_least_70) / len(scores))  # Đếm hoặc cộng phần tử để tính tổng và xác suất.

        denominator = int(np.count_nonzero(at_least_4_hours))  # Đếm hoặc cộng phần tử để tính tổng và xác suất.
        if denominator == 0:
            raise ValueError("No students meet the given study-hours condition.")
        conditional_probability = float(
            np.count_nonzero(both_conditions) / denominator  # Đếm hoặc cộng phần tử để tính tổng và xác suất.
        )
        return probability_70, conditional_probability


    def task3_gradient_descent(initial_w=2.0, learning_rate=0.1):  # Thực hiện đúng một bước cập nhật tham số w.
        loss_before = (initial_w - 4) ** 2

        gradient = 2 * (initial_w - 4)

        updated_w = initial_w - learning_rate * gradient

        loss_after = (updated_w - 4) ** 2
        return loss_before, gradient, updated_w, loss_after


    def main():
        mean, pop_sd, sample_sd, predicted = task1_student_performance(student_data)
        print("TASK 1 — STUDENT PERFORMANCE")
        print("Actual-score mean:", f"{mean:.2f}")
        print("Population SD (NumPy default, ddof=0):", f"{pop_sd:.6f}")
        print("Sample SD (comparison only, ddof=1):", f"{sample_sd:.6f}")
        print("Student | actual score | predicted score")
        for name, actual, prediction in zip(
            STUDENT_NAMES, student_data[:, 2], predicted
        ):
            print(f"{name} | {actual:.0f} | {prediction:.0f}")

        p70, p70_given_4h = task2_probabilities(student_data)
        print("TASK 2 — PROBABILITY")
        print("P(actual score >= 70):", f"{p70:.6f}")
        print("P(actual score >= 70 | hours >= 4):", f"{p70_given_4h:.6f}")

        loss, derivative, new_w, new_loss = task3_gradient_descent()
        print("TASK 3 — GRADIENT DESCENT")
        print("L(2):", f"{loss:.2f}")
        print("Gradient at w=2:", f"{derivative:.2f}")
        print("Updated w after one step:", f"{new_w:.2f}")
        print("Loss after one update (extra check):", f"{new_loss:.2f}")

        if not (student_data.shape == (5, 3)): raise ValueError("Kiểm tra không đạt")
        if not (np.isclose(mean, 66.0)): raise ValueError("Kiểm tra không đạt")
        if not (np.isclose(pop_sd, np.sqrt(194.0))): raise ValueError("Kiểm tra không đạt")
        if not (np.allclose(predicted, [32, 38, 45, 51, 59])): raise ValueError("Kiểm tra không đạt")
        if not (np.isclose(p70, 2 / 5)): raise ValueError("Kiểm tra không đạt")
        if not (np.isclose(p70_given_4h, 2 / 3)): raise ValueError("Kiểm tra không đạt")
        if not (np.isclose(loss, 4.0)): raise ValueError("Kiểm tra không đạt")
        if not (np.isclose(derivative, -4.0)): raise ValueError("Kiểm tra không đạt")
        if not (np.isclose(new_w, 2.4)): raise ValueError("Kiểm tra không đạt")
        if not (new_loss < loss): raise ValueError("Kiểm tra không đạt")

    # Điểm bắt đầu chạy của bài gốc:
    main()


# ===========================================================================
# Math 02 — Tập hợp và Jaccard | Nguồn: exports/print/exercises/LAB-MATH-02.md
# ===========================================================================

def run_math_02():
    """Chạy duy nhất Math 02 — Tập hợp và Jaccard."""
    """Lab Math 02 — set operations, Jaccard similarity and student graphs.

    Reconstructed and improved from PythoClass/2. Math/labs2.ipynb.
    Run: python SOLUTION_ANNOTATED.py
    All example names are synthetic; no user input is required.
    """
    from itertools import combinations  # Generate unordered pairs without repetition.

    # Map each synthetic student to a SET of subjects: duplicates are impossible.
    # The subject choices reproduce the patterns in the owner's six-row demo.
    STUDENTS = {
        "Student A": {"Python", "AI", "Math"},
        "Student B": {"Python", "AI", "SQL"},
        "Student C": {"Python", "SQL"},
        "Student D": {"Java", "Web"},
        "Student E": {"Python", "AI", "Math"},
        "Student F": {"AI", "Math", "Python"},
    }


    def analyse_interests(students):  # Tổng hợp môn học chung và tìm theo điều kiện logic.
        """Task 1: compute unique subjects and the two requested filters."""
        # set().union(*iterable) joins every subject set into one unique collection.
        all_subjects = set().union(*students.values())
        # 'and' keeps people who study BOTH Python and AI.
        python_and_ai = [name for name, subjects in students.items()
                         if "Python" in subjects and "AI" in subjects]
        # 'or' keeps people who study AT LEAST ONE of Python and Math.
        python_or_math = [name for name, subjects in students.items()
                          if "Python" in subjects or "Math" in subjects]
        # Sorting gives reproducible output even though sets have no fixed order.
        return sorted(all_subjects), python_and_ai, python_or_math


    def compare_students(students, first, second):
        """Task 2: inspect intersection, union and directional difference."""
        # Reject unknown identifiers before attempting dictionary indexing.
        if first not in students or second not in students:
            raise ValueError("Both student names must exist.")  # Báo lỗi nếu dữ liệu không đúng điều kiện.
        if first == second:
            raise ValueError("Choose two distinct students.")  # Báo lỗi nếu dữ liệu không đúng điều kiện.
        left, right = students[first], students[second]
        return {
            "shared": sorted(left & right),  # Subjects common to BOTH students.
            "combined": sorted(left | right),  # Subjects studied by EITHER student.
            "only_first": sorted(left - right),  # Subjects absent from second.
        }


    def jaccard_similarity(left, right):  # Jaccard = số phần tử giao chia số phần tử hợp.
        """Task 3: fraction of unique shared subjects among unique subjects."""
        both = left & right  # Set intersection.
        either = left | right  # Set union.
        # Two empty sets have no shared subjects here; choose 0 rather than /0.
        return len(both) / len(either) if either else 0.0


    def most_similar_pair(students):  # combinations tránh xét lại cặp A-B dưới tên B-A.
        """Task 4: compare all unordered pairs, preserving first winning tie."""
        best_pair = None
        best_score = -1.0  # Lower than every legal Jaccard value [0, 1].
        for first, second in combinations(students, 2):  # Duyệt qua các phần tử hoặc cặp phần tử.
            score = jaccard_similarity(students[first], students[second])
            if score > best_score:
                best_pair, best_score = (first, second), score
        return best_pair, best_score


    def recommend_partners(students, student, threshold=0.5):
        """Task 5: return everyone other than student with similarity >= limit."""
        if student not in students:
            raise ValueError("Unknown student.")  # Báo lỗi nếu dữ liệu không đúng điều kiện.
        if not 0.0 <= threshold <= 1.0:
            raise ValueError("Threshold must be between 0 and 1.")  # Báo lỗi nếu dữ liệu không đúng điều kiện.
        matches = []
        for other, subjects in students.items():  # Duyệt qua các phần tử hoặc cặp phần tử.
            if other == student:  # Never recommend a student to themselves.
                continue
            score = jaccard_similarity(students[student], subjects)
            if score >= threshold:  # Inclusive as in the original notebook.
                matches.append((other, score))
        # Rank by similarity, then alphabetically when scores are identical.
        return sorted(matches, key=lambda item: (-item[1], item[0]))


    def build_graph(students, threshold=0.5):  # Tạo danh sách kề hai chiều cho cạnh vô hướng.
        """Task 6: symmetric adjacency list; isolated vertices remain visible."""
        if not 0.0 <= threshold <= 1.0:
            raise ValueError("Threshold must be between 0 and 1.")  # Báo lỗi nếu dữ liệu không đúng điều kiện.
        graph = {name: [] for name in students}  # Every student becomes a node.
        for first, second in combinations(students, 2):  # Duyệt qua các phần tử hoặc cặp phần tử.
            score = jaccard_similarity(students[first], students[second])
            if score >= threshold:
                graph[first].append(second)  # Undirected edge in both directions.
                graph[second].append(first)
        return {name: sorted(neighbors) for name, neighbors in graph.items()}


    def main():
        """Show each result and assert easy-to-check reference expectations."""
        subjects, both, either = analyse_interests(STUDENTS)
        print("Task 1 - All subjects:", ", ".join(subjects))
        print("Python AND AI:", ", ".join(both))
        print("Python OR Math:", ", ".join(either))

        compared = compare_students(STUDENTS, "Student A", "Student B")
        print("Task 2 - Common:", compared["shared"])
        print("Union:", compared["combined"])
        print("Only Student A:", compared["only_first"])

        score = jaccard_similarity(STUDENTS["Student A"], STUDENTS["Student E"])
        print("Task 3 - Jaccard(A, E):", f"{score:.2f}")
        if not (score == 1.0): raise ValueError("Kiểm tra dữ liệu không đạt")  # These two students have identical interest sets.

        pair, highest = most_similar_pair(STUDENTS)
        print("Task 4 - Best pair:", pair, "score", f"{highest:.2f}")
        if not (highest == 1.0): raise ValueError("Kiểm tra dữ liệu không đạt")  # Duplicate interest sets give perfect similarity.

        matches = recommend_partners(STUDENTS, "Student A", threshold=0.5)
        print("Task 5 - Partners:", matches)
        if not (all(s >= 0.5 for _, s in matches)): raise ValueError("Kiểm tra dữ liệu không đạt")

        graph = build_graph(STUDENTS, threshold=0.5)
        print("Task 6 - Student graph:")
        for name, neighbors in graph.items():  # Duyệt qua các phần tử hoặc cặp phần tử.
            print(f"  {name}: {', '.join(neighbors) if neighbors else 'No connections'}")
        if not (graph["Student D"] == []): raise ValueError("Kiểm tra dữ liệu không đạt")  # Java/Web shares none of these subjects.

    # Điểm bắt đầu chạy của bài gốc:
    main()  # Do not run the sample automatically when imported.


# ===========================================================================
# Math 03–04 — Ma trận và PCA | Nguồn: exports/print/exercises/LAB-MATH-03-04.md
# ===========================================================================

def run_math_03_04():
    """Chạy duy nhất Math 03–04 — Ma trận và PCA."""
    """Lab Math 03-04 — store evaluation using matrices, linear systems and PCA.

    Adapted from 2. Math/labs3_4.ipynb. Run:
        python SOLUTION_ANNOTATED.py

    Requires numpy and scikit-learn; prints results without opening a GUI.
    """
    import numpy as np  # Arrays, descriptive statistics and matrix multiplication.
    from sklearn.preprocessing import StandardScaler  # Scale each feature.
    from sklearn.decomposition import PCA  # Reduce correlated features to 2 axes.

    # Rows A-H represent stores. Each column has a specified real-world unit:
    # Orders (count), Customers (count), Revenue (currency units), Employees (count).
    STORE_NAMES = np.array(list("ABCDEFGH"))
    STORE_DATA = np.array([
        [300, 400, 100000, 20],
        [400, 500, 140000, 25],
        [200, 200, 70000, 15],
        [500, 600, 180000, 30],
        [350, 450, 115000, 22],
        [450, 550, 160000, 28],
        [250, 300, 85000, 18],
        [600, 700, 210000, 35],
    ], dtype=float)  # Shape (8,4), with numeric values compatible with NumPy.

    # A and b are supplied evaluation coefficients and observed benchmark scores.
    EQUATION_MATRIX = np.array([[3, 4, 10], [4, 5, 14], [2, 2, 7]], dtype=float)
    EQUATION_SCORES = np.array([135, 182, 86], dtype=float)


    def task1_explore(stores=STORE_DATA):  # Tám cửa hàng, mỗi cửa hàng có bốn đặc trưng.
        """Inspect matrix dimensions, customer counts and mean customer traffic."""
        if stores.ndim != 2 or stores.shape[1] != 4:
            raise ValueError("Expect a matrix with four store features.")  # Báo lỗi nếu dữ liệu không đúng điều kiện.
        customers = stores[:, 1]  # ':' means all rows; index 1 is Customers.
        mean_customers = float(np.mean(customers))  # Mean over all eight stores.
        return stores.shape, customers, mean_customers


    def task2_weights(A=EQUATION_MATRIX, b=EQUATION_SCORES):  # Giải A @ w = b để tìm trọng số, không nhân từng phần tử.
        """Solve A @ w = b for weights of Orders, Customers and Revenue."""
        # np.linalg.solve avoids manually computing the matrix inverse.
        if A.shape != (3, 3) or b.shape != (3,):
            raise ValueError("Expected a 3x3 matrix and a three-element score vector.")  # Báo lỗi nếu dữ liệu không đúng điều kiện.
        if np.linalg.matrix_rank(A) < 3:  # A singular matrix has no unique answer.
            raise ValueError("The benchmark system has no unique solution.")  # Báo lỗi nếu dữ liệu không đúng điều kiện.
        weights = np.linalg.solve(A, b)
        if not (np.allclose(A @ weights, b)): raise ValueError("Kiểm tra dữ liệu không đạt")  # Reconstruct the input equations.
        return weights


    def task3_rank(stores=STORE_DATA, names=STORE_NAMES, weights=None):  # Đổi thang đo rồi tính điểm và xếp hạng cửa hàng.
        """Build dimensionless components, combine weights, rank all stores."""
        if weights is None:
            weights = task2_weights()
        # Scale columns as in the original notebook before applying weights.
        components = np.column_stack((
            stores[:, 0] / 100,  # One score unit per 100 orders.
            stores[:, 1] / 100,  # One score unit per 100 customers.
            stores[:, 2] / 10000,  # One score unit per 10,000 revenue units.
        ))
        totals = components @ weights  # (8x3) @ (3,) -> eight store scores.
        ranked = sorted(zip(names.tolist(), totals.tolist()),
                        key=lambda pair: (-pair[1], pair[0]))
        winner_index = int(np.argmax(totals))  # Index of highest score.
        return components, totals, ranked, names[winner_index]


    def task4_pca(stores=STORE_DATA):  # Chuẩn hóa trước khi giảm xuống hai thành phần chính.
        """Standardize four columns, then project stores onto two PCA axes."""
        # Different units (currency, people) must not bias distance by magnitude.
        scaler = StandardScaler()  # By default centers and scales each column.
        standardized = scaler.fit_transform(stores)
        # PCA finds directions containing the largest variation in scaled data.
        pca = PCA(n_components=2)  # We want a shape of (8 stores, 2 axes).
        projected = pca.fit_transform(standardized)
        retained = pca.explained_variance_ratio_  # Fraction on each retained axis.
        if not (projected.shape == (stores.shape[0], 2)): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (np.allclose(standardized.mean(axis=0), 0, atol=1e-12)): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (np.allclose(standardized.var(axis=0), 1, atol=1e-12)): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (np.isfinite(projected).all()): raise ValueError("Kiểm tra dữ liệu không đạt")
        return standardized, projected, retained


    def main():
        """Print intermediate results for every English task and check shapes."""
        shape, customers, mean_customers = task1_explore()
        print("Task 1 - Store matrix shape:", shape)
        print("Customers:", customers.astype(int).tolist())
        print("Mean customers:", round(mean_customers, 2))

        weights = task2_weights()
        print("Task 2 - Weights:", np.round(weights, 6).tolist())

        components, scores, ranking, best = task3_rank(weights=weights)
        print("Task 3 - Component matrix shape:", components.shape)
        print("Scores:", np.round(scores, 2).tolist())
        print("Ranking:", [(name, round(score, 2)) for name, score in ranking])
        print("Best store:", best)

        standardized, projection, ratios = task4_pca()
        print("Task 4 - Standardized shape:", standardized.shape)
        print("PCA projected shape:", projection.shape)
        print("Explained variance fractions:", np.round(ratios, 4).tolist())
        print("Total variance retained:", f"{ratios.sum() * 100:.2f}%")
        if not (len(ranking) == len(STORE_NAMES)): raise ValueError("Kiểm tra dữ liệu không đạt")
        if not (projection.shape == (8, 2)): raise ValueError("Kiểm tra dữ liệu không đạt")

    # Điểm bắt đầu chạy của bài gốc:
    main()  # Execute this demonstration only when launched as a script.


RUNNERS = {
    "assignment-01": (run_assignment_01, "Assignment 01 — Dictionary"),
    "lab-04": (run_lab_04, "Lab 04 — Điều kiện và vòng lặp"),
    "lab-05": (run_lab_05, "Lab 05 — Danh sách sinh viên"),
    "lab-05-06": (run_lab_05_06, "Lab 05–06 — Hồi quy và Gradient Descent"),
    "lab-07": (run_lab_07, "Lab 07 — Xác suất"),
    "lab-08": (run_lab_08, "Lab 08 — Thống kê"),
    "lab-10": (run_lab_10, "Lab 10 — CSV và phân tích điểm"),
    "pretest": (run_pretest, "Pretest — Ôn tập"),
    "math-02": (run_math_02, "Math 02 — Tập hợp và Jaccard"),
    "math-03-04": (run_math_03_04, "Math 03–04 — Ma trận và PCA"),
}


def main():
    """Hiển thị danh sách hoặc chạy một bài theo mã lựa chọn."""
    if len(sys.argv) == 1 or sys.argv[1] in ("--list", "-l", "--help", "-h"):
        print("AIClassDocuments - 10 bai Lab / bai tap\n")
        print("Chon 1 ma bai de chay: ")
        for code, (_, label) in RUNNERS.items():
            print(f"  {code:16s} {label}")
        print("\nVi du: python AIClassDocuments-TongHop-10-Lab-BaiTap.py lab-04")
        print("Them --demo cho Assignment 01 va Lab 05 de chay khong can nhap.")
        print("Them --no-plot cho Lab 05-06, 07, 08 de khong tao hinh.")
        print("Lab 10 can students.csv trong thu muc dang chay.")
        return
    code = sys.argv[1].lower()
    if code not in RUNNERS:
        raise SystemExit(f"Khong co bai '{code}'. Dung --list de xem ma bai.")
    runner, label = RUNNERS[code]
    print(f"=== {label} ===")
    runner()


if __name__ == "__main__":
    main()
