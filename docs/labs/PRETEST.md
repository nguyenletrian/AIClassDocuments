# Pretest — Phân tích điểm, xác suất và Gradient Descent

## Đề bài tiếng Anh

### PRETEST

A teacher collects data from five students, including their study hours, attendance rate, and actual exam scores.

| Student | Study Hours | Attendance (%) | Actual Score |
|---|---:|---:|---:|
| Student A | 2 | 60 | 50 |
| Student B | 3 | 65 | 55 |
| Student C | 4 | 75 | 65 |
| Student D | 5 | 80 | 70 |
| Student E | 6 | 95 | 90 |

##### Requirements

**Task 1 – Student Performance Analysis and Prediction**

1. Create a NumPy matrix student_data containing study hours, attendance, and actual scores from the given dataset.
2. Use the matrix to calculate the mean and standard deviation of actual scores.
3. A simple prediction model is defined as:

   predicted_score = 5 * study_hours + 0.2 * attendance + 10

   Use the matrix to calculate the predicted scores for all five students.

**Task 2 – Probability**

1. Calculate the probability that a randomly selected student has an actual score greater than or equal to 70.
2. Calculate the probability that a student has an actual score greater than or equal to 70, given that the student studies at least 4 hours.

**Task 3 – Gradient Descent**

A machine learning model uses the loss function:

\[
L(w) = (w - 4)^2
\]

1. Calculate the loss when (w=2).
2. Calculate the gradient when (w=2).
3. Perform one Gradient Descent update using learning rate (α=0.1) and initial value (w=2).
4. Briefly explain why Gradient Descent updates the parameter (w).

## Đề bài tiếng Việt

### BÀI KIỂM TRA ĐẦU VÀO — PRETEST

Một giáo viên thu thập dữ liệu của **năm học sinh**, gồm số giờ học, tỷ lệ tham gia lớp học và điểm thi thực tế.

| Học sinh | Số giờ học | Điểm danh (%) | Điểm thi thực tế |
|---|---:|---:|---:|
| Học sinh A | 2 | 60 | 50 |
| Học sinh B | 3 | 65 | 55 |
| Học sinh C | 4 | 75 | 65 |
| Học sinh D | 5 | 80 | 70 |
| Học sinh E | 6 | 95 | 90 |

##### Yêu cầu

**Bài 1 — Phân tích và dự đoán kết quả học tập**

1. Tạo một ma trận NumPy (thư viện tính toán mảng) tên là student_data chứa số giờ học, tỷ lệ điểm danh và điểm thi thực tế của năm học sinh theo bảng trên.
2. Sử dụng ma trận để tính **điểm trung bình** và **độ lệch chuẩn** của điểm thi thực tế.
3. Mô hình dự đoán đơn giản đã được định nghĩa:

   **Điểm dự đoán = 5 × số giờ học + 0,2 × tỷ lệ điểm danh + 10.**

   Sử dụng ma trận để tính điểm dự đoán cho cả năm học sinh.

**Bài 2 — Xác suất**

1. Tính xác suất một học sinh được chọn ngẫu nhiên có điểm thi thực tế **từ 70 trở lên**.
2. Tính xác suất học sinh có điểm thi thực tế **từ 70 trở lên**, với điều kiện học sinh đó học **ít nhất 4 giờ**.

**Bài 3 — Gradient (độ dốc của hàm) Descent (thuật toán giảm độ dốc)**

Một mô hình học máy sử dụng hàm mất mát:

\[
L(w) = (w - 4)^2
\]

1. Tính giá trị hàm mất mát khi **w = 2**.
2. Tính gradient (đạo hàm theo w) khi **w = 2**.
3. Thực hiện **một lần cập nhật** Gradient Descent với tốc độ học **α = 0,1** và giá trị khởi tạo **w = 2**.
4. Giải thích ngắn gọn tại sao Gradient Descent cập nhật tham số w.

## Giải thích từng câu

### Câu 1

**Bước 1 — Chuẩn bị ma trận.** Dựa trên ví dụ NumPy (thư viện tính toán mảng) của PY-13, dùng np.array() tạo ma trận **5 hàng × 3 cột**; mỗi hàng là một học sinh, theo thứ tự giờ học, tỷ lệ điểm danh (%), điểm thực tế. Chọn dtype=float để các phép nhân và thống kê hoạt động thuận tiện.

**Bước 2 — Lấy cột cần tính.** Cú pháp student_data[:, 2] lấy tất cả hàng ở cột thứ ba (chỉ số bắt đầu từ 0). Cột điểm thực tế là [50, 55, 65, 70, 90]. Tránh tính nhầm trên cột số giờ hoặc tỷ lệ điểm danh.

**Bước 3 — Tính trung bình.** Dùng np.mean() như bài PY-15:

\[
\bar{x} = \frac{50+55+65+70+90}{5} = \mathbf{66}.
\]

**Bước 4 — Tính độ lệch chuẩn.** Độ lệch chuẩn đo độ phân tán của điểm quanh trung bình:

\[
\sigma = \sqrt{\frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n}}.
\]

Thay dữ liệu vào, tổng bình phương độ lệch là **970**, do đó độ lệch chuẩn tổng thể bằng \(\sqrt{970/5}=\sqrt{194}\approx\mathbf{13{,}9284}\). Trong NumPy, đây là **np.std(scores, ddof=0)** (mặc định).

**Giả định được làm rõ:** Đề Word chỉ ghi “standard deviation (độ lệch chuẩn)”, **không chỉ định độ lệch chuẩn mẫu hay tổng thể**. Vì vậy lời giải lấy độ lệch chuẩn tổng thể trên đúng năm học sinh đang được phân tích. Nếu coi năm học sinh là *mẫu* đại diện cho nhóm lớn hơn, dùng np.std(scores, ddof=1), kết quả xấp xỉ **15,5724**. Code in cả hai để người học so sánh, nhưng giá trị đáp án chính là 13,9284.

**Bước 5 — Dự đoán bằng công thức đề cho.** Không huấn luyện mô hình mới; sử dụng nguyên biểu thức:

\[
\widehat{y}_i=5h_i+0.2a_i+10,
\]

trong đó \(h_i\) là số giờ học và \(a_i\) là tỷ lệ điểm danh ghi bằng số 60, 65, …, 95 (không tự chia thêm cho 100).

| Học sinh | Điểm thực tế | Điểm dự đoán theo đề |
|---|---:|---:|
| A | 50 | **32** |
| B | 55 | **38** |
| C | 65 | **45** |
| D | 70 | **51** |
| E | 90 | **59** |

Ví dụ A: 5 × 2 + 0,2 × 60 + 10 = **32**. NumPy cho phép tính đồng thời năm giá trị trên hai cột mảng, không cần chạy năm đoạn code giống nhau.

**Ví dụ/lỗi thường gặp:** Tạo ma trận 5×3, lấy cột điểm bằng [:,2]. Mean (trung bình)=66; độ lệch chuẩn tổng thể≈13,9284. Dự đoán A–E theo Word là 32,38,45,51,59.

**Từ vựng chính:** Student Performance (kết quả học tập).

### Câu 2

**Bước 1 — Liệt kê kết quả phù hợp.** Có năm học sinh và chọn ngẫu nhiên đều một người. Học sinh D (70 điểm) và E (90 điểm) thỏa điều kiện **điểm ≥ 70**, tổng cộng **2 người**.

\[
P(\text{điểm}\ge70)=\frac{2}{5}=\mathbf{0.4}=\mathbf{40\%}.
\]

**Bước 2 — Xét điều kiện số giờ.** Chỉ lấy học sinh **học ≥ 4 giờ**: C, D, E, nên mẫu số giờ còn **3 người**. Trong nhóm này, D và E đạt điểm ≥ 70 nên tử số là **2**.

\[
P(\text{điểm}\ge70\mid\text{giờ}\ge4)=\frac{2}{3}\approx\mathbf{0.6667}=\mathbf{66.67\%}.
\]

**Vì sao không dùng 2/5 lần nữa?** Với xác suất có điều kiện, không gian chọn bị giới hạn còn những người thỏa điều kiện học ít nhất 4 giờ. Ta dùng phép so sánh trên mảng kiểu Boolean giống kỹ thuật từ PY-34: scores >= 70, hours >= 4, kết hợp hai điều kiện bằng toán tử & và dùng np.count_nonzero() đếm kết quả True.

**Ví dụ/lỗi thường gặp:** Hai người D,E đạt ≥70 điểm nên 2/5. Trong nhóm học ≥4 giờ chỉ có C,D,E nên xác suất có điều kiện là 2/3.

**Từ vựng chính:** Probability (xác suất).

### Câu 3

**Bước 1 — Tính loss (hàm mất mát) hiện tại.** Đề cho hàm mất mát **L(w)=(w−4)²**, một hàm bình phương có giá trị nhỏ nhất bằng 0 tại **w=4**. Khi w=2:

\[
L(2)=(2-4)^2=\mathbf{4}.
\]

**Bước 2 — Tính gradient (độ dốc của hàm).** Dùng quy tắc đạo hàm của hàm bình phương, tương tự ví dụ trong PY-32:

\[
\frac{dL}{dw}=2(w-4),\qquad
\left.\frac{dL}{dw}\right|_{w=2}=2(2-4)=\mathbf{-4}.
\]

Gradient âm nghĩa là ở w=2, nếu tăng w một lượng nhỏ thì loss giảm. Đây là độ dốc của hàm mất mát đối với tham số w, không phải xác suất hay sai số dự đoán ở Bài 1.

**Bước 3 — Cập nhật đúng MỘT lần.** Sử dụng công thức đã học:

\[
w_{\text{new}}=w_{\text{old}}-\alpha\,\frac{dL}{dw}
=2-0.1(-4)=\mathbf{2.4}.
\]

**Bước 4 — Giải thích ý nghĩa.** Gradient Descent (thuật toán giảm độ dốc) điều chỉnh tham số w theo **hướng ngược gradient** để giảm giá trị loss. Ở đây gradient âm nên bước cập nhật khiến w tăng từ 2 lên 2,4, đến gần điểm tối ưu w=4. Ta có thể tự đối chiếu:

\[
L(2.4)=(2.4-4)^2=\mathbf{2.56}<4.
\]

Giá trị loss sau cập nhật chỉ là **phép kiểm tra bổ sung**; đề yêu cầu đúng một bước, không yêu cầu 1000 epoch hay dùng dữ liệu ở Bài 1 để huấn luyện.

**Ví dụ/lỗi thường gặp:** Loss (hàm mất mát) L(w)=(w−4)² khi w=2 bằng 4; gradient (độ dốc của hàm)=−4; cập nhật một lần với α=0,1 cho w=2,4, loss giảm còn 2,56.

**Từ vựng chính:** Gradient Descent (thuật toán giảm độ dốc).


## Code Python

```python
import numpy as np  # Nạp thư viện (import: nạp vào) để có các hàm đã học.

STUDENT_NAMES = ["Student A", "Student B", "Student C", "Student D", "Student E"]  # Tính hoặc cập nhật biến STUDENT_NAMES từ công thức bên phải.

student_data = np.array([  # Khởi tạo mảng NumPy với số liệu theo đúng đề.
    [2, 60, 50],  # Tạo hoặc tiếp tục cấu trúc dữ liệu đang khai báo.
    [3, 65, 55],  # Tạo hoặc tiếp tục cấu trúc dữ liệu đang khai báo.
    [4, 75, 65],  # Tạo hoặc tiếp tục cấu trúc dữ liệu đang khai báo.
    [5, 80, 70],  # Tạo hoặc tiếp tục cấu trúc dữ liệu đang khai báo.
    [6, 95, 90],  # Tạo hoặc tiếp tục cấu trúc dữ liệu đang khai báo.
], dtype=float)  # Đóng mảng, danh sách hoặc nhóm tham số.


def task1_student_performance(data):  # Định nghĩa hàm (function: hàm) để gom và gọi lại các bước.
    if data.shape != (5, 3):  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
        raise ValueError("Expected the original 5-student x 3-column table.")  # Báo lỗi khi đầu vào không hợp lệ.

    study_hours = data[:, 0]  # Tính hoặc cập nhật biến study_hours từ công thức bên phải.
    attendance = data[:, 1]  # Tính hoặc cập nhật biến attendance từ công thức bên phải.
    actual_scores = data[:, 2]  # Tính hoặc cập nhật biến actual_scores từ công thức bên phải.

    mean_score = float(np.mean(actual_scores))  # Tính trung bình cộng các giá trị hợp lệ.

    population_sd = float(np.std(actual_scores, ddof=0))  # Tính độ lệch chuẩn để đo sự phân tán.
    sample_sd = float(np.std(actual_scores, ddof=1))  # Tính độ lệch chuẩn để đo sự phân tán.

    predicted_scores = 5 * study_hours + 0.2 * attendance + 10  # Tính hoặc cập nhật biến predicted_scores từ công thức bên phải.
    return mean_score, population_sd, sample_sd, predicted_scores  # Trả kết quả (return: trả về) cho nơi gọi hàm.


def task2_probabilities(data):  # Định nghĩa hàm (function: hàm) để gom và gọi lại các bước.
    scores = data[:, 2]  # Tính hoặc cập nhật biến scores từ công thức bên phải.
    hours = data[:, 0]  # Tính hoặc cập nhật biến hours từ công thức bên phải.

    at_least_70 = scores >= 70  # Tính hoặc cập nhật biến at_least_70 từ công thức bên phải.
    at_least_4_hours = hours >= 4  # Tính hoặc cập nhật biến at_least_4_hours từ công thức bên phải.
    both_conditions = at_least_70 & at_least_4_hours  # Tính hoặc cập nhật biến both_conditions từ công thức bên phải.

    probability_70 = float(np.count_nonzero(at_least_70) / len(scores))  # Đếm hoặc cộng phần tử để tính tổng và xác suất.

    denominator = int(np.count_nonzero(at_least_4_hours))  # Đếm hoặc cộng phần tử để tính tổng và xác suất.
    if denominator == 0:  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
        raise ValueError("No students meet the given study-hours condition.")  # Báo lỗi khi đầu vào không hợp lệ.
    conditional_probability = float(  # Tính hoặc cập nhật biến conditional_probability từ công thức bên phải.
        np.count_nonzero(both_conditions) / denominator  # Đếm hoặc cộng phần tử để tính tổng và xác suất.
    )  # Đóng mảng, danh sách hoặc nhóm tham số.
    return probability_70, conditional_probability  # Trả kết quả (return: trả về) cho nơi gọi hàm.


def task3_gradient_descent(initial_w=2.0, learning_rate=0.1):  # Định nghĩa hàm (function: hàm) để gom và gọi lại các bước.
    loss_before = (initial_w - 4) ** 2  # Tính hoặc cập nhật biến loss_before từ công thức bên phải.

    gradient = 2 * (initial_w - 4)  # Tính hoặc cập nhật biến gradient từ công thức bên phải.

    updated_w = initial_w - learning_rate * gradient  # Tính hoặc cập nhật biến updated_w từ công thức bên phải.

    loss_after = (updated_w - 4) ** 2  # Tính hoặc cập nhật biến loss_after từ công thức bên phải.
    return loss_before, gradient, updated_w, loss_after  # Trả kết quả (return: trả về) cho nơi gọi hàm.


def main():  # Định nghĩa hàm (function: hàm) để gom và gọi lại các bước.
    mean, pop_sd, sample_sd, predicted = task1_student_performance(student_data)  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
    print("TASK 1 — STUDENT PERFORMANCE")  # In kết quả (output: kết quả) để đối chiếu với đề.
    print("Actual-score mean:", f"{mean:.2f}")  # In kết quả (output: kết quả) để đối chiếu với đề.
    print("Population SD (NumPy default, ddof=0):", f"{pop_sd:.6f}")  # In kết quả (output: kết quả) để đối chiếu với đề.
    print("Sample SD (comparison only, ddof=1):", f"{sample_sd:.6f}")  # In kết quả (output: kết quả) để đối chiếu với đề.
    print("Student | actual score | predicted score")  # In kết quả (output: kết quả) để đối chiếu với đề.
    for name, actual, prediction in zip(  # Duyệt từng phần tử qua vòng lặp (loop: vòng lặp).
        STUDENT_NAMES, student_data[:, 2], predicted  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
    ):  # Đóng mảng, danh sách hoặc nhóm tham số.
        print(f"{name} | {actual:.0f} | {prediction:.0f}")  # In kết quả (output: kết quả) để đối chiếu với đề.

    p70, p70_given_4h = task2_probabilities(student_data)  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
    print("TASK 2 — PROBABILITY")  # In kết quả (output: kết quả) để đối chiếu với đề.
    print("P(actual score >= 70):", f"{p70:.6f}")  # In kết quả (output: kết quả) để đối chiếu với đề.
    print("P(actual score >= 70 | hours >= 4):", f"{p70_given_4h:.6f}")  # In kết quả (output: kết quả) để đối chiếu với đề.

    loss, derivative, new_w, new_loss = task3_gradient_descent()  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
    print("TASK 3 — GRADIENT DESCENT")  # In kết quả (output: kết quả) để đối chiếu với đề.
    print("L(2):", f"{loss:.2f}")  # In kết quả (output: kết quả) để đối chiếu với đề.
    print("Gradient at w=2:", f"{derivative:.2f}")  # In kết quả (output: kết quả) để đối chiếu với đề.
    print("Updated w after one step:", f"{new_w:.2f}")  # In kết quả (output: kết quả) để đối chiếu với đề.
    print("Loss after one update (extra check):", f"{new_loss:.2f}")  # In kết quả (output: kết quả) để đối chiếu với đề.

    if not (student_data.shape == (5, 3)): raise ValueError("Kiểm tra không đạt")  # Kiểm tra bằng if (nếu), báo lỗi nếu kết quả không phù hợp.
    if not (np.isclose(mean, 66.0)): raise ValueError("Kiểm tra không đạt")  # Kiểm tra bằng if (nếu), báo lỗi nếu kết quả không phù hợp.
    if not (np.isclose(pop_sd, np.sqrt(194.0))): raise ValueError("Kiểm tra không đạt")  # Kiểm tra bằng if (nếu), báo lỗi nếu kết quả không phù hợp.
    if not (np.allclose(predicted, [32, 38, 45, 51, 59])): raise ValueError("Kiểm tra không đạt")  # Kiểm tra bằng if (nếu), báo lỗi nếu kết quả không phù hợp.
    if not (np.isclose(p70, 2 / 5)): raise ValueError("Kiểm tra không đạt")  # Kiểm tra bằng if (nếu), báo lỗi nếu kết quả không phù hợp.
    if not (np.isclose(p70_given_4h, 2 / 3)): raise ValueError("Kiểm tra không đạt")  # Kiểm tra bằng if (nếu), báo lỗi nếu kết quả không phù hợp.
    if not (np.isclose(loss, 4.0)): raise ValueError("Kiểm tra không đạt")  # Kiểm tra bằng if (nếu), báo lỗi nếu kết quả không phù hợp.
    if not (np.isclose(derivative, -4.0)): raise ValueError("Kiểm tra không đạt")  # Kiểm tra bằng if (nếu), báo lỗi nếu kết quả không phù hợp.
    if not (np.isclose(new_w, 2.4)): raise ValueError("Kiểm tra không đạt")  # Kiểm tra bằng if (nếu), báo lỗi nếu kết quả không phù hợp.
    if not (new_loss < loss): raise ValueError("Kiểm tra không đạt")  # Kiểm tra bằng if (nếu), báo lỗi nếu kết quả không phù hợp.


if __name__ == "__main__":  # Kiểm tra điều kiện (condition: điều kiện), thực hiện nhánh khi đúng.
    main()  # Tiếp tục bước xử lý dữ liệu đúng như code tham khảo.
```
