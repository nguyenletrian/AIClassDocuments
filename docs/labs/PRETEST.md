# PRETEST — Phân tích điểm, xác suất và Gradient Descent

**Nguồn:** Tệp `Pretest.docx` do chủ dự án tải trực tiếp lên cuộc trò chuyện; SHA-256 của bản gốc: `6ae75a33707108baa466546ff8a9457ac9090728db4bf481fdae623b2b6beaad`. Đề có một trang, năm hàng sinh viên và ba nhóm nhiệm vụ. Công thức ở Task 3 là **L(w) = (w − 4)²**, nằm trong đối tượng Equation của Word nên có thể bị mất khi chỉ đọc văn bản thuần.

**Nguồn phương pháp code:** AIClassDocuments PY-13 (mảng NumPy), PY-15 (thống kê/tính trên mảng), PY-34 (xác suất theo số trường hợp), PY-32 (quy tắc cập nhật Gradient Descent). Code cuối bài **áp dụng các cách làm đã học** vào đúng số liệu và hàm loss của Pretest; không giả nhận đây là một script Pretest đã có sẵn trong notebook demo.

---

## PART 1 — COMPLETE ORIGINAL ENGLISH ASSIGNMENT

# PRETEST

A teacher collects data from five students, including their study hours, attendance rate, and actual exam scores.

| Student | Study Hours | Attendance (%) | Actual Score |
|---|---:|---:|---:|
| Student A | 2 | 60 | 50 |
| Student B | 3 | 65 | 55 |
| Student C | 4 | 75 | 65 |
| Student D | 5 | 80 | 70 |
| Student E | 6 | 95 | 90 |

### Requirements

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

---

## PHẦN 2 — BẢN DỊCH TIẾNG VIỆT TOÀN BỘ ĐỀ

# BÀI KIỂM TRA ĐẦU VÀO — PRETEST

Một giáo viên thu thập dữ liệu của **năm học sinh**, gồm số giờ học, tỷ lệ tham gia lớp học và điểm thi thực tế.

| Học sinh | Số giờ học | Điểm danh (%) | Điểm thi thực tế |
|---|---:|---:|---:|
| Học sinh A | 2 | 60 | 50 |
| Học sinh B | 3 | 65 | 55 |
| Học sinh C | 4 | 75 | 65 |
| Học sinh D | 5 | 80 | 70 |
| Học sinh E | 6 | 95 | 90 |

### Yêu cầu

**Bài 1 — Phân tích và dự đoán kết quả học tập**

1. Tạo một ma trận NumPy tên là student_data chứa số giờ học, tỷ lệ điểm danh và điểm thi thực tế của năm học sinh theo bảng trên.
2. Sử dụng ma trận để tính **điểm trung bình** và **độ lệch chuẩn** của điểm thi thực tế.
3. Mô hình dự đoán đơn giản đã được định nghĩa:

   **Điểm dự đoán = 5 × số giờ học + 0,2 × tỷ lệ điểm danh + 10.**

   Sử dụng ma trận để tính điểm dự đoán cho cả năm học sinh.

**Bài 2 — Xác suất**

1. Tính xác suất một học sinh được chọn ngẫu nhiên có điểm thi thực tế **từ 70 trở lên**.
2. Tính xác suất học sinh có điểm thi thực tế **từ 70 trở lên**, với điều kiện học sinh đó học **ít nhất 4 giờ**.

**Bài 3 — Gradient Descent**

Một mô hình học máy sử dụng hàm mất mát:

\[
L(w) = (w - 4)^2
\]

1. Tính giá trị hàm mất mát khi **w = 2**.
2. Tính gradient (đạo hàm theo w) khi **w = 2**.
3. Thực hiện **một lần cập nhật** Gradient Descent với tốc độ học **α = 0,1** và giá trị khởi tạo **w = 2**.
4. Giải thích ngắn gọn tại sao Gradient Descent cập nhật tham số w.

---

## Quy trình giải chi tiết và các công thức liên quan

### Bài 1 — Tạo ma trận, thống kê và dự đoán điểm

**Bước 1 — Chuẩn bị ma trận.** Dựa trên ví dụ NumPy của PY-13, dùng np.array() tạo ma trận **5 hàng × 3 cột**; mỗi hàng là một học sinh, theo thứ tự giờ học, tỷ lệ điểm danh (%), điểm thực tế. Chọn dtype=float để các phép nhân và thống kê hoạt động thuận tiện.

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

**Giả định được làm rõ:** Đề Word chỉ ghi “standard deviation”, **không chỉ định độ lệch chuẩn mẫu hay tổng thể**. Vì vậy lời giải lấy độ lệch chuẩn tổng thể trên đúng năm học sinh đang được phân tích. Nếu coi năm học sinh là *mẫu* đại diện cho nhóm lớn hơn, dùng np.std(scores, ddof=1), kết quả xấp xỉ **15,5724**. Code in cả hai để người học so sánh, nhưng giá trị đáp án chính là 13,9284.

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

### Bài 2 — Xác suất và xác suất có điều kiện

**Bước 1 — Liệt kê kết quả phù hợp.** Có năm học sinh và chọn ngẫu nhiên đều một người. Học sinh D (70 điểm) và E (90 điểm) thỏa điều kiện **điểm ≥ 70**, tổng cộng **2 người**.

\[
P(\text{điểm}\ge70)=\frac{2}{5}=\mathbf{0.4}=\mathbf{40\%}.
\]

**Bước 2 — Xét điều kiện số giờ.** Chỉ lấy học sinh **học ≥ 4 giờ**: C, D, E, nên mẫu số giờ còn **3 người**. Trong nhóm này, D và E đạt điểm ≥ 70 nên tử số là **2**.

\[
P(\text{điểm}\ge70\mid\text{giờ}\ge4)=\frac{2}{3}\approx\mathbf{0.6667}=\mathbf{66.67\%}.
\]

**Vì sao không dùng 2/5 lần nữa?** Với xác suất có điều kiện, không gian chọn bị giới hạn còn những người thỏa điều kiện học ít nhất 4 giờ. Ta dùng phép so sánh trên mảng kiểu Boolean giống kỹ thuật từ PY-34: scores >= 70, hours >= 4, kết hợp hai điều kiện bằng toán tử & và dùng np.count_nonzero() đếm kết quả True.

### Bài 3 — Một lần cập nhật Gradient Descent

**Bước 1 — Tính loss hiện tại.** Đề cho hàm mất mát **L(w)=(w−4)²**, một hàm bình phương có giá trị nhỏ nhất bằng 0 tại **w=4**. Khi w=2:

\[
L(2)=(2-4)^2=\mathbf{4}.
\]

**Bước 2 — Tính gradient.** Dùng quy tắc đạo hàm của hàm bình phương, tương tự ví dụ trong PY-32:

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

**Bước 4 — Giải thích ý nghĩa.** Gradient Descent điều chỉnh tham số w theo **hướng ngược gradient** để giảm giá trị loss. Ở đây gradient âm nên bước cập nhật khiến w tăng từ 2 lên 2,4, đến gần điểm tối ưu w=4. Ta có thể tự đối chiếu:

\[
L(2.4)=(2.4-4)^2=\mathbf{2.56}<4.
\]

Giá trị loss sau cập nhật chỉ là **phép kiểm tra bổ sung**; đề yêu cầu đúng một bước, không yêu cầu 1000 epoch hay dùng dữ liệu ở Bài 1 để huấn luyện.

---

## PHẦN 4 — TOÀN BỘ CODE PYTHON CÙNG CHÚ THÍCH

**Cách thực hành:** Cài NumPy nếu chưa có bằng lệnh pip install numpy, lưu toàn bộ script bên dưới thành pretest_solution.py và chạy python pretest_solution.py.

Mã tái sử dụng **cấu trúc mảng, cắt cột, thống kê, đếm biến cố và quy tắc cập nhật Gradient Descent từ các ví dụ đã học** (PY-13, PY-15, PY-34, PY-32), thay duy nhất dữ liệu/hàm mất mát để khớp Pretest. Các lệnh print cho phép học viên thấy kết quả ngay, còn assert kiểm tra kết quả có đúng các phép tính của đề.

```python
"""PRETEST — Student analysis, probabilities and one Gradient Descent step.

Adaptation of techniques already taught in AIClassDocuments:
- PY-13: NumPy arrays/matrices and column indexing
- PY-15: mean(), std() and vectorized operations
- PY-34: probability as event count divided by sample-space count
- PY-32: gradient = derivative; w_new = w_old - learning_rate * gradient
The dataset and loss function are copied faithfully from the uploaded Word.
Run: python pretest_solution.py (requires numpy).
"""

# NumPy supports a 2D matrix and operations on full columns without manual loops.
import numpy as np

# The row order matches the original Word table, Student A through Student E.
STUDENT_NAMES = ["Student A", "Student B", "Student C", "Student D", "Student E"]

# student_data: five rows (students) and three columns:
# column 0 = study hours; column 1 = attendance (%) ; column 2 = actual score.
# dtype=float allows multiplication, means and standard deviation.
student_data = np.array([
    [2, 60, 50],   # Student A: 2 hours, 60% attendance, score 50.
    [3, 65, 55],   # Student B: 3 hours, 65% attendance, score 55.
    [4, 75, 65],   # Student C: 4 hours, 75% attendance, score 65.
    [5, 80, 70],   # Student D: 5 hours, 80% attendance, score 70.
    [6, 95, 90],   # Student E: 6 hours, 95% attendance, score 90.
], dtype=float)


def task1_student_performance(data):
    """Calculate statistics and predictions from the three-column matrix."""
    # Check that there are exactly five students and three numeric features.
    if data.shape != (5, 3):
        raise ValueError("Expected the original 5-student x 3-column table.")

    # [:, 0] means 'all rows of column 0' (study hours).
    study_hours = data[:, 0]
    # [:, 1] selects the percentage attendance column.
    attendance = data[:, 1]
    # [:, 2] selects actual exam scores: 50, 55, 65, 70, 90.
    actual_scores = data[:, 2]

    # NumPy mean() adds five actual scores and divides by their count.
    mean_score = float(np.mean(actual_scores))

    # The Word does not specify sample vs. population standard deviation.
    # ddof=0 is the NumPy default: population SD, divisor n = 5.
    population_sd = float(np.std(actual_scores, ddof=0))
    # ddof=1 gives sample SD, divisor n-1 = 4, for comparison only.
    sample_sd = float(np.std(actual_scores, ddof=1))

    # Use EXACTLY the prediction model given in Pretest.docx.
    # Elementwise operations produce one prediction for each student.
    predicted_scores = 5 * study_hours + 0.2 * attendance + 10
    return mean_score, population_sd, sample_sd, predicted_scores


def task2_probabilities(data):
    """Calculate P(score >= 70) and P(score >= 70 | hours >= 4)."""
    scores = data[:, 2]
    hours = data[:, 0]

    # Boolean arrays are True when the corresponding condition is satisfied.
    at_least_70 = scores >= 70                 # D and E: two students.
    at_least_4_hours = hours >= 4             # C, D and E: three students.
    both_conditions = at_least_70 & at_least_4_hours

    # Probability = favorable student count / all five students.
    probability_70 = float(np.count_nonzero(at_least_70) / len(scores))

    # Conditional probability uses ONLY the three students with >= 4 hours.
    denominator = int(np.count_nonzero(at_least_4_hours))
    if denominator == 0:                      # Avoid dividing by zero.
        raise ValueError("No students meet the given study-hours condition.")
    conditional_probability = float(
        np.count_nonzero(both_conditions) / denominator
    )
    return probability_70, conditional_probability


def task3_gradient_descent(initial_w=2.0, learning_rate=0.1):
    """One exact gradient step for L(w) = (w - 4)^2, not multiple epochs."""
    # Given loss function: distance between current w and target 4, squared.
    loss_before = (initial_w - 4) ** 2

    # Derivative: d[(w-4)^2]/dw = 2*(w-4), so at w=2 it is -4.
    gradient = 2 * (initial_w - 4)

    # Move OPPOSITE the gradient; negative gradient means increase w.
    updated_w = initial_w - learning_rate * gradient

    # Optional check: evaluate the same loss after this ONE update.
    loss_after = (updated_w - 4) ** 2
    return loss_before, gradient, updated_w, loss_after


def main():
    """Display and check the results of the three source Word tasks."""
    mean, pop_sd, sample_sd, predicted = task1_student_performance(student_data)
    print("TASK 1 — STUDENT PERFORMANCE")
    print("Actual-score mean:", f"{mean:.2f}")
    print("Population SD (NumPy default, ddof=0):", f"{pop_sd:.6f}")
    print("Sample SD (comparison only, ddof=1):", f"{sample_sd:.6f}")
    print("Student | actual score | predicted score")
    # zip() pairs each student name with the same row's actual and predicted.
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

    # The values below are independently determined from the source table.
    assert student_data.shape == (5, 3)
    assert np.isclose(mean, 66.0)
    assert np.isclose(pop_sd, np.sqrt(194.0))
    assert np.allclose(predicted, [32, 38, 45, 51, 59])
    assert np.isclose(p70, 2 / 5)
    assert np.isclose(p70_given_4h, 2 / 3)
    assert np.isclose(loss, 4.0)
    assert np.isclose(derivative, -4.0)
    assert np.isclose(new_w, 2.4)
    assert new_loss < loss


if __name__ == "__main__":
    # Run the complete solution only when invoked as the main Python file.
    main()
```
