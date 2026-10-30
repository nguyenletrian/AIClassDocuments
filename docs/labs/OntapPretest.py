"""
Pretest - phân tích điểm, xác xuất và Gradient Descent

## Đề bài tiếng Anh
### PRETEST

A teacher collects data from five students, including their study
hours, attendance rate, and actual exam scores.

| Student | Study Hours | Attendance (%) | Actual Score|
StudentA 2 60 50
StudentB 3 65 55
StudentC 4 75 65
StudentD 5 80 70
StudentE 6 95 90

#### Requirements
**Task 1 - Student Performance Analysis and Prediction**
1. Create a Numpy matrix student_data containning study hours,
attendance and actual scores from the given dataset.
2. Use the matrix to calculate the mean and standard deviation of
actual scores.
3. A simple prediction model is defined as:
predicted_score =  5 * study_hours + 0.2 * attendance + 10
use the matrix to calculate the predicted scores for all students.

** Task 2 - Probability**
1. Calculate the probability that a randomly selected student has
an actual score greater than or equal to 70
2. Calculate the probability that a student has an actual score
greater than or equal to 70, given that student studies at least 4 hours.

** Task 3 - Gradient Descent **
A machine learning model uses the loss function:
L(w) = (w-4)^2
1. Calculate the loss when (w=2).
2. Calculate the gradientn when (w=2)
3. Perform on Gradient Descent update using learning rate
(alpha =0.1) and initial value (w=2).
4. Briefly explain why gradient Descent update the paramater (w)

## Đề bài tiếng Việt
###  Bài kiểm tra đầu vào - Pretest
Một giáo viên thu thập dữ liệu của 5 học sinh, gồm số giờ học,
tỷ lệ tham gia lớp học và điểm thi thực tế.

### YÊU CẦU

**Bài 1 - Phân tích và dự đoán kết quản học tập**
1. Tạo một ma trận Numpy (thư viện tính toán mảng) tên là
student_data chứa số giờ học, tỷ lệ điểm danh và điểm khi thực tế
của 5 học sinh theo bảng trên.
2. Sử dụng ma trận để tính **điểm trung bình** và **Độ lệch chuẩn**
của điểm thi thực tế.
3. Mô hình dự đoán đơn giản đã được định nghĩa:
Điểm dự đoán = 5 x số giờ học + 0,2 x tỷ lệ điểm danh + 10
Sử dụng ma trận để tính điểm dự đoán cho cả năm học sinh

** Bài 2 - Xác suất**
1.Tính xác suất của một học sinh được chọn ngẫu nhiên có điểm thi
thực tế từ 70 điểm trở lên
2.Tính xác suất học sinh có điểm thi thực tế từ 70 trở lên, với
điều kiện học sinh đó học ít nhất 4 giờ..

** Bài 3 - Gradient (độ dốc của hàm) Descent (thuật toán giảm
độ dốc)
Một mô hình học máy sử dụng hàm mất mát:
L(w) = (w - 4) ^ 2
1. Tính giá trị hàm mất mát khi w=2
2. Tính gradient (đạo hầm theo w) khi w =2
3. Thực hiện một lần cập nhật Gradient Descent với tốc độ học
alpha = 0,1 và giá trị khởi tạo w=2
4. Giải thích ngắn gọn tại sao Gradient Descent cập nhật thông số w

## Giải thích từng câu
### Câu 1 - Phân tích điểm và dự đoán
Mục tiêu: Dùng bảng của năm học sinh để tính trung bình, độ lệch
chuẩn của điểm thực tế, sau đó dự đoán điểm bằng biểu thức được
đề cung cấp. Không tự huấn luyện mô hình.
Vì sao phải làm theo thứ tự này? Cần chuyển bảng thành mảng số
trước, lấy đúng cột điểm để thống kê, rồi lấy cột giờ học và
điểm danh để dự đoán. Nếu trộn các cột, kết quả sẽ sai dù cú pháp
python đúng
QUY TRÌNH GIẢI:
1. Tạo mảng có năm hàng, 3 cột. Mỗi hàng là một học sinh; các cột
lần lượt là giờ học, tỷ lệ điểm danh và điểm thi. 'dtype=float'
yêu cầu lưu dạng số thực để thuận tiện tính toán.
2. Lấy cột điểm thực tế bằng 'data[:,2]'. Dấu ':' chọn tất cả hàng,
số '2' chọt cột thứ 3 vì python đếm cột từ 0.
3. Dùng 'np.mean(scores)' tính trung bình. Dùng 'np.std(scores,ddof)'
để tính độ lệch chuẩn của toàn bộ nhóm năm học sinh. Đề không
nêu mẫu hay tổng thể, nên cũng tính thêm "ddof=1" để so sánh
trường hợp xem 5 học sinh là mẫu
4. Tính đồng thời điểm dự đoán theo hệ số đề cho; không đổi 60%
thành 0.6 vì biểu thức của đề sử dụng trực tiếp giá trị điểm danh
60,65
"""
#Công thức viết bằng python:
import numpy as np
data = np.array([
    [2,60,50],
    [3,65,55],
    [4,75,65],
    [5,80,70],
    [6,95,90],
],dtype=float)
hours = data[:,0]
attendance = data[:,1]
scores = data[:,2]
mean_score = np.mean(scores)
sd_population = np.std(scores,ddof=0) # Độ lệch chuẩn tổng thể
sd_sample = np.std(scores,ddof=1) # Độ lêch chuẩn mẫu
predicted = 5 * hours + 0.2 * attendance + 10 #[32,38,45,51,59]

"""
giải thích hàm, toán tử và tham số: np.array tạo mảng,dtype=float
chọn kiểu số thưc. np.mean để lấy trung bình. np.std đo độ phân tán
ddof=0 chia phương sai cho số quan sát n, còn dd0f chia cho n-1.
Phép * nhân từng phần tử trong mảng Numpy, data[:,0] lấy giờ học,
data[:,1] lấy điểm danh, data[:,2] lấy điểm thực tế.

Ví dụ và kết quả đối chiếu: Trung bình 66, độ lệch chuẩn tổng thể
khoảng 13...

Câu 2 - xác xuất và xác xuất có điều kiện
Mục tiêu: Tìm xác xuất đạt ít nhất 70 điểm khi chọ bất kỳ học sinh
nào; sau đó tìm xác suất đạt ít nhất 70 điểm nếu đã biết học sinh
đó học ít nhất 4 giờ.
Tại sao phải giải khác nhau? câu đầu xét đủ 5 học sinh, trong đó
D và E đạt 70 điểm trở lên. Câu sau chỉ xét nhóm C,D,E, gồm
3 học sinh học từ 4 giờ; trong nhóm đó D và E đạt ít nhất 70 diểm.
Xác suất có điều kiện phải dùng đúng số người trong nhóm được biết
trước mẫu số.

Quy trình giải
1. Só sánh mảng diểm với 70 để tạo các giá trị đúng/sai; dùng
np.count_nonzero đếm số học sinh đạt.
2. lấy số đạt chia cho tổng số
3. So sánh giờ học với 4 để chọn nhóm điều kiện; lấy & lấy kết hợp
2 điều kiện để đếm người vừa học đủ giờ vừa đạt điểm.
4. Lấy số người thỏa cả 2 chia cho só người học từ 4 giờ, phải
kiểm tra mẫu số khác 0.

Công thức python:
at_least_70 = scores >=70
count_pas = np.count_nonzero(at_least_70)

"""
