# Bộ đề ôn tập nền tảng AI theo 16 câu mẫu FPT Jetking

**Lưu ý:** Đây là tài liệu luyện tập do AIClassDocuments biên soạn từ bộ 936 câu đã có,
không phải đề thi chính thức hay dự đoán chính xác câu hỏi sẽ xuất hiện.
Đề 01 giữ nguyên 16 câu mẫu đã cung cấp; Đề 02–10 lấy 144 câu riêng biệt
từ các bài PY-24–PY-37, ưu tiên toán, tối ưu hóa, xác suất và thống kê.

**Cách làm:** Mỗi đề gồm 16 câu, 4 lựa chọn, mỗi câu 1 điểm; tự đặt khoảng 9 phút
để luyện tốc độ theo các câu mẫu. Đáp án và giải thích được giữ bên dưới mỗi câu.

## Đề 01 — 16 câu

**Q1. Given vectors u = [2, 3] and v = [4, 1], what is their dot product? | Cho hai vector u = [2, 3] và v = [4, 1], tích vô hướng của chúng bằng bao nhiêu?**

A. 8

B. 11

C. 14

D. 7

**Đáp án: B**

**Giải thích:** Tích vô hướng = 2 × 4 + 3 × 1 = 11. Python: sum(x * y for x, y in zip(u, v)).

**Q2. Given A = [[1, 2], [3, 4]] and B = [[5, 6], [7, 8]], what is the first-row, first-column element of AB? | Cho hai ma trận A và B như trên, phần tử hàng 1 cột 1 của tích AB bằng bao nhiêu?**

A. 19

B. 17

C. 23

D. 13

**Đáp án: A**

**Giải thích:** Lấy hàng đầu của A nhân vô hướng với cột đầu của B: 1 × 5 + 2 × 7 = 19.

**Q3. Solve the system: x + y = 5 and x - y = 1. What are x and y? | Giải hệ phương trình x + y = 5 và x - y = 1. Tìm x và y.**

A. x = 2, y = 3

B. x = 3, y = 2

C. x = 4, y = 1

D. x = 1, y = 4

**Đáp án: B**

**Giải thích:** Cộng hai phương trình được 2x = 6, nên x = 3; thay vào x + y = 5 được y = 2.

**Q4. If a square matrix has determinant zero, what can we conclude? | Nếu ma trận vuông có định thức bằng 0, có thể kết luận điều gì?**

A. It is always an identity matrix | Nó luôn là ma trận đơn vị

B. It must be diagonal | Nó bắt buộc là ma trận đường chéo

C. It is not invertible | Nó không có ma trận nghịch đảo

D. It contains only positive values | Nó chỉ chứa giá trị dương

**Đáp án: C**

**Giải thích:** Định thức bằng 0 nghĩa là ma trận suy biến, không khả nghịch; không suy ra ma trận đơn vị hoặc đường chéo.

**Q5. What is the derivative of f(x) = 3x^2 + 2x - 1? | Đạo hàm của hàm f(x) = 3x² + 2x - 1 là gì?**

A. 6x + 2

B. 3x + 2

C. 6x - 1

D. 3x^2 + 2

**Đáp án: A**

**Giải thích:** Đạo hàm từng hạng: 3x² thành 6x, 2x thành 2, hằng số -1 thành 0. Kết quả 6x + 2.

**Q6. Given f(x) = x^2 - 4x + 5, at which x is the derivative zero? | Với f(x) = x² - 4x + 5, tại giá trị x nào đạo hàm bằng 0?**

A. x = 1

B. x = 2

C. x = 3

D. x = 4

**Đáp án: B**

**Giải thích:** f'(x) = 2x - 4. Đặt 2x - 4 = 0, suy ra x = 2.

**Q7. Gradient descent uses theta_new = theta_old - learning_rate * gradient. If theta_old = 5, learning rate = 0.1, and gradient = 4, what is theta_new? | Gradient Descent dùng công thức cập nhật đã cho. Khi theta_old = 5, tốc độ học = 0,1 và gradient = 4, theta_new là bao nhiêu?**

A. 5.4

B. 4.6

C. 4.0

D. 5.0

**Đáp án: B**

**Giải thích:** theta_new = 5 - 0.1 × 4 = 4.6. Trừ gradient để đi theo hướng giảm hàm mất mát.

**Q8. What may happen if the learning rate in gradient descent is too large? | Điều gì có thể xảy ra nếu tốc độ học trong Gradient Descent quá lớn?**

A. The model always reaches the global minimum | Mô hình luôn đạt cực tiểu toàn cục

B. The training dataset automatically grows | Dữ liệu huấn luyện tự tăng

C. The loss may oscillate or diverge | Hàm mất mát có thể dao động hoặc phân kỳ

D. The gradient always becomes zero | Gradient luôn trở về 0

**Đáp án: C**

**Giải thích:** Bước cập nhật quá lớn có thể vượt qua điểm cực tiểu, khiến loss dao động hoặc tăng không giới hạn.

**Q9. For a fair coin, what is the probability of getting heads in one toss? | Với đồng xu công bằng, xác suất được mặt ngửa khi tung một lần là bao nhiêu?**

A. 0

B. 0.25

C. 0.5

D. 1

**Đáp án: C**

**Giải thích:** Đồng xu công bằng có hai kết quả đồng khả năng, nên xác suất mặt ngửa là 1 / 2 = 0.5.

**Q10. If P(A) = 0.4, what is P(not A)? | Nếu P(A) = 0,4, xác suất biến cố đối của A bằng bao nhiêu?**

A. 0.4

B. 0.6

C. 1.4

D. 0.2

**Đáp án: B**

**Giải thích:** Xác suất biến cố đối = 1 - P(A) = 1 - 0.4 = 0.6.

**Q11. What is the median of [2, 4, 4, 6, 9]? | Trung vị của dãy [2, 4, 4, 6, 9] là bao nhiêu?**

A. 2

B. 4

C. 6

D. 5

**Đáp án: B**

**Giải thích:** Dãy đã tăng dần và có 5 phần tử; giá trị ở vị trí giữa (thứ ba) là 4.

**Q12. A student's score is 85, the mean is 70, and the standard deviation is 10. What is the z-score? | Điểm một học sinh là 85, trung bình 70, độ lệch chuẩn 10. Điểm z bằng bao nhiêu?**

A. 0.5

B. 1.0

C. 1.5

D. 2.5

**Đáp án: C**

**Giải thích:** z = (giá trị - trung bình) / độ lệch chuẩn = (85 - 70) / 10 = 1.5.

**Q13. Conditional Probability and Bayes' Theorem: select not correct | Xác suất có điều kiện và định lý Bayes: chọn phát biểu KHÔNG đúng.**

A. P(A|B) = P(A intersection B) / P(B), provided P(B) > 0 | Công thức xác suất có điều kiện đúng khi P(B) > 0

B. If A and B are independent, P(A|B) = P(A), provided P(B) > 0 | Nếu A và B độc lập, biết B không đổi xác suất của A

C. P(A|B) always equals P(B|A) | P(A|B) luôn bằng P(B|A)

D. Bayes' theorem can calculate the probability of a hypothesis given observed evidence | Bayes giúp tính xác suất giả thuyết khi có bằng chứng

**Đáp án: C**

**Giải thích:** P(A|B) và P(B|A) nói chung khác nhau do mẫu số khác. Chỉ trong một số trường hợp đặc biệt chúng mới bằng nhau.

**Q14. What is the main purpose of Principal Component Analysis (PCA)? | Mục đích chính của phương pháp phân tích thành phần chính (PCA) là gì?**

A. To increase the number of features | Tăng số đặc trưng

B. To reduce dimensionality while retaining as much variance as possible | Giảm số chiều nhưng giữ nhiều phương sai nhất có thể

C. To replace numerical data with text | Thay số bằng văn bản

D. To guarantee perfect prediction accuracy | Đảm bảo dự đoán hoàn toàn chính xác

**Đáp án: B**

**Giải thích:** PCA tạo các trục trực giao ưu tiên phương sai lớn; giữ một số trục đầu để giảm chiều nhưng bảo toàn nhiều biến thiên.

**Q15. Given L(w) = (w - 3)^2, what is dL/dw when w = 5? | Cho L(w) = (w - 3)², đạo hàm theo w khi w = 5 bằng bao nhiêu?**

A. 2

B. 4

C. 6

D. 8

**Đáp án: B**

**Giải thích:** Đạo hàm là 2(w - 3); tại w = 5, kết quả 2 × 2 = 4.

**Q16. Events A and B are independent. If P(A) = 0.5 and P(B) = 0.4, what is P(A intersection B)? | Hai biến cố A, B độc lập. Nếu P(A) = 0,5 và P(B) = 0,4, xác suất giao hai biến cố là bao nhiêu?**

A. 0.9

B. 0.2

C. 0.4

D. 0.1

**Đáp án: B**

**Giải thích:** Với hai biến cố độc lập, P(A giao B) = P(A) × P(B) = 0.5 × 0.4 = 0.2.

## Đề 02 — 16 câu

**Q1. What is the norm of vector (3,4)? | Norm của vector (3,4) bằng bao nhiêu?**

A. 5 | 5

B. (0.6,0.8) | (0.6,0.8)

C. 11 | 11

D. 0 | 0

**Đáp án: A**

**Giải thích:** Độ dài Pythagoras là căn của 9+16.

**Q2. What is a matrix? | Ma trận là gì?**

A. A two-dimensional array of values | Bảng dữ liệu hai chiều

B. A matrix with rows and columns exchanged | Ma trận đổi vai trò hàng và cột

C. Rows of the left matrix with columns of the right | Hàng ma trận trái với cột ma trận phải

D. A scalar associated with a square matrix | Một số gắn với ma trận vuông

**Đáp án: A**

**Giải thích:** Ma trận sắp phần tử theo hàng và cột.

**Q3. Which tool solves a nonsingular square system? | Hàm nào giải hệ vuông không suy biến?**

A. `np.linalg.solve(A,b)` | `np.linalg.solve(A,b)`

B. `np.linalg.matrix_rank(A)` | `np.linalg.matrix_rank(A)`

C. `np.column_stack((A,b))` | `np.column_stack((A,b))`

D. `np.linalg.lstsq(A,b,rcond=None)` | `np.linalg.lstsq(A,b,rcond=None)`

**Đáp án: A**

**Giải thích:** solve dùng cho ma trận hệ số vuông, không suy biến.

**Q4. What is a determinant? | Định thức là gì?**

A. A two-dimensional array of values | Bảng dữ liệu hai chiều

B. A matrix with rows and columns exchanged | Ma trận đổi vai trò hàng và cột

C. Rows of the left matrix with columns of the right | Hàng ma trận trái với cột ma trận phải

D. A scalar associated with a square matrix | Một số gắn với ma trận vuông

**Đáp án: D**

**Giải thích:** Định thức hỗ trợ kiểm tra tính khả nghịch.

**Q5. What is the derivative of x²? | Đạo hàm của x² là gì?**

A. `2*x` | `2*x`

B. Zero | Bằng 0

C. 6 | 6

D. 4 | 4

**Đáp án: A**

**Giải thích:** Quy tắc đạo hàm lũy thừa cho 2x.

**Q6. What is a stationary point? | Điểm dừng là gì?**

A. First partial derivatives of vector outputs | Các đạo hàm riêng bậc một của đầu ra vector

B. Second partial derivatives of a scalar output | Các đạo hàm riêng bậc hai của đầu ra vô hướng

C. A differentiable point where the gradient is zero | Điểm khả vi có gradient bằng 0

D. Classifying local behavior near stationary points | Phân loại hành vi cục bộ gần điểm dừng

**Đáp án: C**

**Giải thích:** Điểm dừng có các đạo hàm riêng bậc một bằng 0.

**Q7. Which expression is a gradient-descent update? | Biểu thức nào cập nhật theo gradient descent?**

A. `sp.diff(f,x)` | `sp.diff(f,x)`

B. `w = w - lr*gradient` | `w = w - lr*gradient`

C. `np.mean((pred-y)**2)` | `np.mean((pred-y)**2)`

D. A `for` loop | Vòng lặp `for`

**Đáp án: B**

**Giải thích:** Trừ gradient nhằm giảm loss cục bộ.

**Q8. What is a partial derivative? | Đạo hàm riêng là gì?**

A. Change rate in one variable while others are held fixed | Tốc độ thay đổi theo một biến khi giữ các biến khác cố định

B. A vector of partial derivatives | Vector gồm các đạo hàm riêng

C. A factor controlling an optimization update step | Hệ số điều khiển độ lớn bước cập nhật tối ưu

D. One pass through the training dataset | Một lượt đi qua tập dữ liệu train

**Đáp án: A**

**Giải thích:** Chỉ thay một biến và giữ biến khác cố định.

**Q9. When does counting favorable outcomes over total outcomes work? | Khi nào chia số trường hợp thuận lợi cho tổng số trường hợp là đúng?**

A. When outcomes are equally likely | Khi các kết quả đồng khả năng

B. n values of zero or one | n giá trị 0 hoặc 1

C. Reproducible pseudorandom sequences | Chuỗi giả ngẫu nhiên tái lập

D. Fraction of True values | Tỷ lệ các phần tử True

**Đáp án: A**

**Giải thích:** Đếm cổ điển đòi hỏi các kết quả đồng khả năng.

**Q10. What is a random experiment? | Phép thử ngẫu nhiên là gì?**

A. A repeatable procedure with uncertain individual outcome | Thao tác lặp được nhưng kết quả mỗi lần không chắc chắn

B. Set of all possible outcomes | Tập tất cả kết quả có thể

C. A subset of the sample space | Một tập con của không gian mẫu

D. A measure between zero and one of an event's chance | Thước đo từ 0 đến 1 cho khả năng biến cố

**Đáp án: A**

**Giải thích:** Phép thử có thể sinh kết quả khác nhau.

**Q11. What does mean calculate? | Mean tính gì?**

A. Sum divided by observation count | Tổng chia số quan sát

B. Middle ranked value after sorting | Giá trị ở giữa sau khi sắp

C. Squared dispersion around the mean | Độ phân tán bình phương quanh mean

D. Spread in original measurement units | Độ phân tán cùng đơn vị gốc

**Đáp án: A**

**Giải thích:** Mọi quan sát góp vào trung bình.

**Q12. What characterizes a normal distribution? | Phân phối chuẩn có đặc điểm gì?**

A. A numerical quantity assigned to random outcomes | Đại lượng số gắn với kết quả ngẫu nhiên

B. Successes in independent same-p trials | Số thành công trong các lần thử độc lập cùng p

C. A continuous symmetric bell-shaped density | Mật độ liên tục dạng chuông đối xứng

D. Probability mass at a discrete value | Xác suất ở một giá trị rời rạc

**Đáp án: C**

**Giải thích:** Được xác định bởi trung bình và độ lệch chuẩn. Hai tham số có ý nghĩa khác nhau: mean xác định tâm và độ lệch chuẩn dương quyết định độ phân tán.

**Q13. What is conditional probability? | Xác suất có điều kiện là gì?**

A. Probability of A given B has occurred | Xác suất A khi biết B đã xảy ra

B. One event does not change the probability of the other | Biến cố này không đổi xác suất của biến cố kia

C. A posterior from evidence, likelihood and prior | Xác suất sau bằng chứng từ likelihood và prior

D. Overall chance weighted over a partition | Xác suất chung theo trọng số một phân hoạch

**Đáp án: A**

**Giải thích:** Nó thu hẹp mẫu nền về nhóm B.

**Q14. What does covariance describe? | Hiệp phương sai mô tả gì?**

A. `A @ v = λ*v` with v nonzero | `A @ v = λ*v` với v khác không

B. Scaling along a corresponding eigenvector | Hệ số co giãn theo vector riêng tương ứng

C. How two variables vary together | Hai biến cùng biến thiên ra sao

D. A covariance eigenvector with high eigenvalue | Vector riêng hiệp phương sai có trị riêng lớn

**Đáp án: C**

**Giải thích:** Hiệp phương sai đo sự biến thiên cùng nhau.

**Q15. What is MSE? | MSE là gì?**

A. Mean squared prediction error | Trung bình sai số dự báo bình phương

B. Mean absolute prediction error | Trung bình trị tuyệt đối sai số

C. Quadratic for small errors and linear for large | Bình phương lỗi nhỏ, tuyến tính lỗi lớn

D. Compare two probability distributions in a directed way | So hai phân phối xác suất có phân biệt chiều

**Đáp án: A**

**Giải thích:** MSE lấy trung bình bình phương sai lệch.

**Q16. What is independence of events? | Độc lập giữa hai biến cố là gì?**

A. Probability of A given B has occurred | Xác suất A khi biết B đã xảy ra

B. One event does not change the probability of the other | Biến cố này không đổi xác suất của biến cố kia

C. A posterior from evidence, likelihood and prior | Xác suất sau bằng chứng từ likelihood và prior

D. Overall chance weighted over a partition | Xác suất chung theo trọng số một phân hoạch

**Đáp án: B**

**Giải thích:** Độc lập nghĩa là biến cố này không đổi xác suất biến cố kia.

## Đề 03 — 16 câu

**Q1. What is the dot product (1,2)·(3,4)? | Tích vô hướng (1,2)·(3,4) bằng bao nhiêu?**

A. 5 | 5

B. (0.6,0.8) | (0.6,0.8)

C. 11 | 11

D. 0 | 0

**Đáp án: C**

**Giải thích:** Tính 1×3 + 2×4.

**Q2. What does matrix multiplication combine? | Phép nhân ma trận kết hợp gì?**

A. A two-dimensional array of values | Bảng dữ liệu hai chiều

B. A matrix with rows and columns exchanged | Ma trận đổi vai trò hàng và cột

C. Rows of the left matrix with columns of the right | Hàng ma trận trái với cột ma trận phải

D. A scalar associated with a square matrix | Một số gắn với ma trận vuông

**Đáp án: C**

**Giải thích:** Mỗi ô kết quả là tích vô hướng một hàng với một cột.

**Q3. If the residual is exactly zero, what is true? | Nếu sai số dư bằng 0 thì điều gì đúng?**

A. Every equation is satisfied | Mọi phương trình đều được thỏa

B. The sum of squared residuals | Tổng bình phương sai số dư

C. Whether a candidate solution approximately satisfies the system | Nghiệm thử có thỏa hệ gần đúng hay không

D. Ranks of A and its augmented matrix | Hạng của A và ma trận mở rộng

**Đáp án: A**

**Giải thích:** Sai số dư bằng 0 nghĩa là Ax=b.

**Q4. Which attribute returns the transpose of a 2-D ndarray? | Thuộc tính nào cho chuyển vị mảng 2-D?**

A. `@` | `@`

B. `.T` | `.T`

C. `np.linalg.det(A)` | `np.linalg.det(A)`

D. `np.linalg.inv(A)` | `np.linalg.inv(A)`

**Đáp án: B**

**Giải thích:** T là thuộc tính chuyển vị tiện dụng.

**Q5. What is the derivative of a constant? | Đạo hàm của một hằng số là gì?**

A. `2*x` | `2*x`

B. Zero | Bằng 0

C. 6 | 6

D. 4 | 4

**Đáp án: B**

**Giải thích:** Hằng số không đổi theo biến.

**Q6. What is Hessian of x²+y²? | Hessian của x²+y² là gì?**

A. `[[2,0],[0,2]]` | `[[2,0],[0,2]]`

B. `[[2,0],[0,-2]]` | `[[2,0],[0,-2]]`

C. `(3,2)` | `(3,2)`

D. `[[1,1],[y,x]]` | `[[1,1],[y,x]]`

**Đáp án: A**

**Giải thích:** Đạo hàm bậc hai của mỗi hạng bình phương bằng 2.

**Q7. What is ∂(x²+3xy)/∂x? | Đạo hàm riêng theo x của x²+3xy là gì?**

A. `2*x+3*y` | `2*x+3*y`

B. `[2*x,2*y]` | `[2*x,2*y]`

C. `2*w` | `2*w`

D. 2.4 | 2.4

**Đáp án: A**

**Giải thích:** Lấy đạo hàm x² và xy theo x.

**Q8. What is a gradient? | Gradient là gì?**

A. Change rate in one variable while others are held fixed | Tốc độ thay đổi theo một biến khi giữ các biến khác cố định

B. A vector of partial derivatives | Vector gồm các đạo hàm riêng

C. A factor controlling an optimization update step | Hệ số điều khiển độ lớn bước cập nhật tối ưu

D. One pass through the training dataset | Một lượt đi qua tập dữ liệu train

**Đáp án: B**

**Giải thích:** Các đạo hàm riêng hợp thành một vector.

**Q9. What does `rng.integers(0,2,size=n)` generate? | `rng.integers(0,2,size=n)` tạo gì?**

A. When outcomes are equally likely | Khi các kết quả đồng khả năng

B. n values of zero or one | n giá trị 0 hoặc 1

C. Reproducible pseudorandom sequences | Chuỗi giả ngẫu nhiên tái lập

D. Fraction of True values | Tỷ lệ các phần tử True

**Đáp án: B**

**Giải thích:** Cận trên 2 không lấy 2, chỉ còn 0 và 1.

**Q10. What is a sample space? | Không gian mẫu là gì?**

A. A repeatable procedure with uncertain individual outcome | Thao tác lặp được nhưng kết quả mỗi lần không chắc chắn

B. Set of all possible outcomes | Tập tất cả kết quả có thể

C. A subset of the sample space | Một tập con của không gian mẫu

D. A measure between zero and one of an event's chance | Thước đo từ 0 đến 1 cho khả năng biến cố

**Đáp án: B**

**Giải thích:** Không gian mẫu chứa mọi kết quả khả dĩ.

**Q11. What is median? | Median là gì?**

A. Sum divided by observation count | Tổng chia số quan sát

B. Middle ranked value after sorting | Giá trị ở giữa sau khi sắp

C. Squared dispersion around the mean | Độ phân tán bình phương quanh mean

D. Spread in original measurement units | Độ phân tán cùng đơn vị gốc

**Đáp án: B**

**Giải thích:** Trung vị dựa trên thứ tự, không dựa trên tổng độ lớn.

**Q12. What do mean and standard deviation determine for normal? | Mean và std xác định gì trong chuẩn?**

A. Independent trials with constant success probability | Các lần thử độc lập cùng xác suất thành công

B. Center and spread | Trung tâm và độ phân tán

C. Zero | Bằng 0

D. Strictly positive standard deviation | Độ lệch chuẩn phải lớn hơn 0

**Đáp án: B**

**Giải thích:** Trung bình định vị và độ lệch chuẩn xác định độ rộng. Đổi độ lệch chuẩn làm chuông rộng/hẹp nhưng không nhất thiết thay tâm của phân phối.

**Q13. What does Bayes' theorem compute? | Định lý Bayes tính gì?**

A. Probability of A given B has occurred | Xác suất A khi biết B đã xảy ra

B. One event does not change the probability of the other | Biến cố này không đổi xác suất của biến cố kia

C. A posterior from evidence, likelihood and prior | Xác suất sau bằng chứng từ likelihood và prior

D. Overall chance weighted over a partition | Xác suất chung theo trọng số một phân hoạch

**Đáp án: C**

**Giải thích:** Bayes cập nhật tỷ lệ nền từ bằng chứng.

**Q14. What is a principal direction in PCA? | Hướng chính trong PCA là gì?**

A. `A @ v = λ*v` with v nonzero | `A @ v = λ*v` với v khác không

B. Scaling along a corresponding eigenvector | Hệ số co giãn theo vector riêng tương ứng

C. How two variables vary together | Hai biến cùng biến thiên ra sao

D. A covariance eigenvector with high eigenvalue | Vector riêng hiệp phương sai có trị riêng lớn

**Đáp án: D**

**Giải thích:** Vector riêng hiệp phương sai nổi bật mang phương sai lớn nhất.

**Q15. Which formula computes MSE? | Công thức nào tính MSE?**

A. Low predicted probability for the correct label | Xác suất dự đoán thấp cho nhãn đúng

B. `mean((y-pred)**2)` | `mean((y-pred)**2)`

C. `mean(abs(y-pred))` | `mean(abs(y-pred))`

D. `delta` | `delta`

**Đáp án: B**

**Giải thích:** Bình phương từng sai lệch trước khi trung bình.

**Q16. Which equation expresses event independence? | Đẳng thức nào mô tả biến cố độc lập?**

A. `P(A and B)/P(B)` when P(B)>0 | `P(A và B)/P(B)` khi P(B)>0

B. `P(A and B)=P(A)*P(B)` | `P(A và B)=P(A)*P(B)`

C. `likelihood*prior/evidence` | `likelihood*prior/evidence`

D. Disjoint and exhaustive | Rời nhau và phủ đủ

**Đáp án: B**

**Giải thích:** Độc lập khi xác suất giao bằng tích hai xác suất.

## Đề 04 — 16 câu

**Q1. What is the dot product of (1,0) and (0,1)? | Tích vô hướng của (1,0) và (0,1) là bao nhiêu?**

A. 5 | 5

B. (0.6,0.8) | (0.6,0.8)

C. 11 | 11

D. 0 | 0

**Đáp án: D**

**Giải thích:** Cả hai tích thành phần đều bằng không.

**Q2. What is the shape of a matrix with two rows and three columns? | Ma trận hai hàng ba cột có shape gì?**

A. `(2, 3)` | `(2, 3)`

B. `(3, 2)` | `(3, 2)`

C. `(2, 1)` | `(2, 1)`

D. `(3, 3)` | `(3, 3)`

**Đáp án: A**

**Giải thích:** Shape ghi số hàng trước số cột.

**Q3. What does a rank-deficient square matrix imply? | Ma trận vuông thiếu hạng gợi ý điều gì?**

A. Three equations or observations | Ba phương trình hoặc quan sát

B. Coefficients of two unknowns | Hệ số của hai ẩn

C. The right-hand-side values | Các giá trị vế phải

D. It cannot have a unique solution for every b | Không thể có nghiệm duy nhất với mọi b

**Đáp án: D**

**Giải thích:** Thiếu hạng đầy đủ khiến không bảo đảm nghiệm duy nhất.

**Q4. Which function computes a square matrix determinant? | Hàm nào tính định thức ma trận vuông?**

A. `@` | `@`

B. `.T` | `.T`

C. `np.linalg.det(A)` | `np.linalg.det(A)`

D. `np.linalg.inv(A)` | `np.linalg.inv(A)`

**Đáp án: C**

**Giải thích:** det trả định thức dạng số.

**Q5. What is the slope of x² at x=3? | Độ dốc của x² tại x=3 là gì?**

A. `2*x` | `2*x`

B. Zero | Bằng 0

C. 6 | 6

D. 4 | 4

**Đáp án: C**

**Giải thích:** 2 nhân 3 bằng sáu.

**Q6. What is Hessian of x²−y²? | Hessian của x²−y² là gì?**

A. `[[2,0],[0,2]]` | `[[2,0],[0,2]]`

B. `[[2,0],[0,-2]]` | `[[2,0],[0,-2]]`

C. `(3,2)` | `(3,2)`

D. `[[1,1],[y,x]]` | `[[1,1],[y,x]]`

**Đáp án: B**

**Giải thích:** Độ cong theo y bằng âm 2.

**Q7. What is the gradient of x²+y²? | Gradient của x²+y² là gì?**

A. `2*x+3*y` | `2*x+3*y`

B. `[2*x,2*y]` | `[2*x,2*y]`

C. `2*w` | `2*w`

D. 2.4 | 2.4

**Đáp án: B**

**Giải thích:** Mỗi đạo hàm bằng hai lần tọa độ.

**Q8. What is a learning rate? | Learning rate là gì?**

A. Change rate in one variable while others are held fixed | Tốc độ thay đổi theo một biến khi giữ các biến khác cố định

B. A vector of partial derivatives | Vector gồm các đạo hàm riêng

C. A factor controlling an optimization update step | Hệ số điều khiển độ lớn bước cập nhật tối ưu

D. One pass through the training dataset | Một lượt đi qua tập dữ liệu train

**Đáp án: C**

**Giải thích:** Nó nhân mức độ cập nhật.

**Q9. What does `default_rng(seed)` provide? | `default_rng(seed)` cung cấp gì?**

A. When outcomes are equally likely | Khi các kết quả đồng khả năng

B. n values of zero or one | n giá trị 0 hoặc 1

C. Reproducible pseudorandom sequences | Chuỗi giả ngẫu nhiên tái lập

D. Fraction of True values | Tỷ lệ các phần tử True

**Đáp án: C**

**Giải thích:** Seed điều khiển chuỗi giả ngẫu nhiên tái lập.

**Q10. What is an event? | Biến cố là gì?**

A. A repeatable procedure with uncertain individual outcome | Thao tác lặp được nhưng kết quả mỗi lần không chắc chắn

B. Set of all possible outcomes | Tập tất cả kết quả có thể

C. A subset of the sample space | Một tập con của không gian mẫu

D. A measure between zero and one of an event's chance | Thước đo từ 0 đến 1 cho khả năng biến cố

**Đáp án: C**

**Giải thích:** Biến cố là một nhóm kết quả.

**Q11. What is mode? | Mode là gì?**

A. Most frequent observed value | Giá trị xuất hiện nhiều nhất

B. Divide sum of squares by n | Chia tổng bình phương cho n

C. Divide by n−1 | Chia cho n−1

D. Frequency per distinct label | Tần suất từng nhãn khác nhau

**Đáp án: A**

**Giải thích:** Yếu vị dùng được cho nhãn lẫn số.

**Q12. What is P(X=x) for a continuous normal variable? | P(X=x) với biến chuẩn liên tục bằng bao nhiêu?**

A. Independent trials with constant success probability | Các lần thử độc lập cùng xác suất thành công

B. Center and spread | Trung tâm và độ phân tán

C. Zero | Bằng 0

D. Strictly positive standard deviation | Độ lệch chuẩn phải lớn hơn 0

**Đáp án: C**

**Giải thích:** Một điểm đơn có xác suất bằng 0. Xác suất trong khoảng là diện tích dưới PDF; một điểm riêng lẻ không có diện tích.

**Q13. Which formula gives P(A given B)? | Công thức P(A khi biết B) là gì?**

A. `P(A and B)/P(B)` when P(B)>0 | `P(A và B)/P(B)` khi P(B)>0

B. `P(A and B)=P(A)*P(B)` | `P(A và B)=P(A)*P(B)`

C. `likelihood*prior/evidence` | `likelihood*prior/evidence`

D. Disjoint and exhaustive | Rời nhau và phủ đủ

**Đáp án: A**

**Giải thích:** Lấy xác suất giao chia xác suất biến cố điều kiện.

**Q14. What is the shape of a covariance matrix for three features? | Ma trận covariance cho ba đặc trưng có shape gì?**

A. `(3,3)` | `(3,3)`

B. Columns of the second returned array | Các cột của mảng trả về thứ hai

C. v and −v describe the same eigendirection | v và −v biểu diễn cùng trục riêng

D. No variance along that direction | Không biến thiên theo hướng đó

**Đáp án: A**

**Giải thích:** Mỗi đặc trưng ghép với từng đặc trưng.

**Q15. Which formula computes MAE? | Công thức nào tính MAE?**

A. Low predicted probability for the correct label | Xác suất dự đoán thấp cho nhãn đúng

B. `mean((y-pred)**2)` | `mean((y-pred)**2)`

C. `mean(abs(y-pred))` | `mean(abs(y-pred))`

D. `delta` | `delta`

**Đáp án: C**

**Giải thích:** Lấy trị tuyệt đối từng sai lệch rồi trung bình.

**Q16. What condition is required for total probability groups? | Các nhóm dùng xác suất toàn phần phải thế nào?**

A. `P(A and B)/P(B)` when P(B)>0 | `P(A và B)/P(B)` khi P(B)>0

B. `P(A and B)=P(A)*P(B)` | `P(A và B)=P(A)*P(B)`

C. `likelihood*prior/evidence` | `likelihood*prior/evidence`

D. Disjoint and exhaustive | Rời nhau và phủ đủ

**Đáp án: D**

**Giải thích:** Nhóm phải không giao nhau và phủ toàn bộ.

## Đề 05 — 16 câu

**Q1. What is the dot product of two nonzero perpendicular vectors? | Tích vô hướng của hai vector khác không vuông góc là gì?**

A. Zero | Bằng không

B. That its norm is nonzero | Norm khác không

C. The result can be physically misleading | Kết quả có thể sai ý nghĩa vật lý

D. They must have equal lengths | Chúng phải có cùng số phần tử

**Đáp án: A**

**Giải thích:** Hai hướng trực giao có tích vô hướng bằng không.

**Q2. What is the transpose shape of a (2,3) matrix? | Chuyển vị ma trận (2,3) có shape gì?**

A. `(2, 3)` | `(2, 3)`

B. `(3, 2)` | `(3, 2)`

C. `(2, 1)` | `(2, 1)`

D. `(3, 3)` | `(3, 3)`

**Đáp án: B**

**Giải thích:** Hàng và cột đổi vai trò.

**Q3. What should be compared to diagnose inconsistency of a system? | Để xét hệ vô nghiệm cần so sánh gì?**

A. Every equation is satisfied | Mọi phương trình đều được thỏa

B. The sum of squared residuals | Tổng bình phương sai số dư

C. Whether a candidate solution approximately satisfies the system | Nghiệm thử có thỏa hệ gần đúng hay không

D. Ranks of A and its augmented matrix | Hạng của A và ma trận mở rộng

**Đáp án: D**

**Giải thích:** Hạng A khác hạng [A, b] cho biết hệ vô nghiệm.

**Q4. Which function computes a nonsingular matrix inverse? | Hàm nào tính nghịch đảo ma trận khả nghịch?**

A. `@` | `@`

B. `.T` | `.T`

C. `np.linalg.det(A)` | `np.linalg.det(A)`

D. `np.linalg.inv(A)` | `np.linalg.inv(A)`

**Đáp án: D**

**Giải thích:** inv tính nghịch đảo khi ma trận khả nghịch.

**Q5. What is the limit of (x²−4)/(x−2) at x=2? | Giới hạn của (x²−4)/(x−2) khi x→2 là gì?**

A. `2*x` | `2*x`

B. Zero | Bằng 0

C. 6 | 6

D. 4 | 4

**Đáp án: D**

**Giải thích:** Rút gọn gần điểm còn x+2.

**Q6. What are stationary coordinates for (x−3)²+(y−2)²? | Tọa độ dừng của (x−3)²+(y−2)² là gì?**

A. `[[2,0],[0,2]]` | `[[2,0],[0,2]]`

B. `[[2,0],[0,-2]]` | `[[2,0],[0,-2]]`

C. `(3,2)` | `(3,2)`

D. `[[1,1],[y,x]]` | `[[1,1],[y,x]]`

**Đáp án: C**

**Giải thích:** Cả hai bình phương nhỏ nhất khi sai khác bằng 0.

**Q7. For loss w², what is its derivative? | Đạo hàm loss w² là gì?**

A. `2*x+3*y` | `2*x+3*y`

B. `[2*x,2*y]` | `[2*x,2*y]`

C. `2*w` | `2*w`

D. 2.4 | 2.4

**Đáp án: C**

**Giải thích:** Dùng quy tắc lũy thừa cho w².

**Q8. What is an epoch in training? | Epoch trong huấn luyện là gì?**

A. Change rate in one variable while others are held fixed | Tốc độ thay đổi theo một biến khi giữ các biến khác cố định

B. A vector of partial derivatives | Vector gồm các đạo hàm riêng

C. A factor controlling an optimization update step | Hệ số điều khiển độ lớn bước cập nhật tối ưu

D. One pass through the training dataset | Một lượt đi qua tập dữ liệu train

**Đáp án: D**

**Giải thích:** Một epoch xử lý hết dữ liệu train một lượt.

**Q9. What does `np.mean(mask)` compute for Boolean mask? | `np.mean(mask)` tính gì với mặt nạ Boolean?**

A. When outcomes are equally likely | Khi các kết quả đồng khả năng

B. n values of zero or one | n giá trị 0 hoặc 1

C. Reproducible pseudorandom sequences | Chuỗi giả ngẫu nhiên tái lập

D. Fraction of True values | Tỷ lệ các phần tử True

**Đáp án: D**

**Giải thích:** True tính như 1, False tính như 0.

**Q10. What is probability? | Xác suất là gì?**

A. A repeatable procedure with uncertain individual outcome | Thao tác lặp được nhưng kết quả mỗi lần không chắc chắn

B. Set of all possible outcomes | Tập tất cả kết quả có thể

C. A subset of the sample space | Một tập con của không gian mẫu

D. A measure between zero and one of an event's chance | Thước đo từ 0 đến 1 cho khả năng biến cố

**Đáp án: D**

**Giải thích:** Xác suất trong đoạn 0 đến 1.

**Q11. What is mean of 2,3,4? | Mean của 2,3,4 là bao nhiêu?**

A. 3 | 3

B. 4 | 4

C. 2/3 | 2/3

D. 1 | 1

**Đáp án: A**

**Giải thích:** Tổng 9 chia 3 bằng 3.

**Q12. What does norm.cdf(0) equal for N(0,1)? | norm.cdf(0) với N(0,1) bằng gì?**

A. 0.5 | 0.5

B. CDF(b) minus CDF(a) | CDF(b) trừ CDF(a)

C. No, sampling noise remains | Không, vẫn có dao động lấy mẫu

D. From 0 to 1 inclusive | Từ 0 đến 1 gồm hai đầu

**Đáp án: A**

**Giải thích:** Chuẩn tắc đối xứng quanh 0. Chuẩn tắc đối xứng quanh trung bình 0 nên mỗi phía chứa một nửa xác suất.

**Q13. Which rule gives posterior after a positive signal? | Quy tắc nào tính posterior khi tín hiệu dương?**

A. `P(A and B)/P(B)` when P(B)>0 | `P(A và B)/P(B)` khi P(B)>0

B. `P(A and B)=P(A)*P(B)` | `P(A và B)=P(A)*P(B)`

C. `likelihood*prior/evidence` | `likelihood*prior/evidence`

D. Disjoint and exhaustive | Rời nhau và phủ đủ

**Đáp án: C**

**Giải thích:** Bayes chuẩn hóa likelihood nhân prior bằng xác suất bằng chứng.

**Q14. What does a zero covariance eigenvalue suggest? | Trị riêng covariance bằng 0 gợi ý gì?**

A. `(3,3)` | `(3,3)`

B. Columns of the second returned array | Các cột của mảng trả về thứ hai

C. v and −v describe the same eigendirection | v và −v biểu diễn cùng trục riêng

D. No variance along that direction | Không biến thiên theo hướng đó

**Đáp án: D**

**Giải thích:** Trị riêng 0 nghĩa là không có phương sai theo trục đó.

**Q15. What does `−log(p_true)` represent for one correct class? | `−log(p_true)` biểu thị gì cho một nhãn đúng?**

A. Cross-entropy loss for that sample | Cross-entropy của mẫu đó

B. Nonnegative | Không âm

C. No, KL is asymmetric | Không, KL bất đối xứng

D. The distributions are identical | Hai phân phối giống nhau

**Đáp án: A**

**Giải thích:** Với one-hot, chỉ còn hạng log của lớp đúng.

**Q16. What is the total with group shares 0.6,0.4 and rates 0.8,0.2? | Tỷ lệ chung từ nhóm 0.6/0.4 với xác suất 0.8/0.2 là gì?**

A. 0.2 | 0.2

B. 0.56 | 0.56

C. 0.3 | 0.3

D. No; base rate and false positives also matter | Không; còn tỷ lệ nền và dương giả

**Đáp án: B**

**Giải thích:** 0.6×0.8+0.4×0.2 bằng 0.56.

## Đề 06 — 16 câu

**Q1. What is the unit vector in the direction (3,4)? | Vector đơn vị theo hướng (3,4) là gì?**

A. 5 | 5

B. (0.6,0.8) | (0.6,0.8)

C. 11 | 11

D. 0 | 0

**Đáp án: B**

**Giải thích:** Chia mỗi thành phần cho độ dài năm.

**Q2. What shape results from (2,3) @ (3,1)? | Phép (2,3) @ (3,1) cho shape gì?**

A. `(2, 3)` | `(2, 3)`

B. `(3, 2)` | `(3, 2)`

C. `(2, 1)` | `(2, 1)`

D. `(3, 3)` | `(3, 3)`

**Đáp án: C**

**Giải thích:** Hai chiều trong bằng 3; giữ hai chiều ngoài.

**Q3. What does least squares minimize? | Bình phương tối thiểu làm nhỏ nhất gì?**

A. Every equation is satisfied | Mọi phương trình đều được thỏa

B. The sum of squared residuals | Tổng bình phương sai số dư

C. Whether a candidate solution approximately satisfies the system | Nghiệm thử có thỏa hệ gần đúng hay không

D. Ranks of A and its augmented matrix | Hạng của A và ma trận mở rộng

**Đáp án: B**

**Giải thích:** Bình phương sai lệch làm lỗi lớn bị phạt mạnh.

**Q4. When is a square matrix invertible? | Khi nào ma trận vuông khả nghịch?**

A. Its determinant is nonzero | Định thức khác không

B. 3 | 3

C. Identity matrix | Ma trận đơn vị

D. `np.allclose(A, B)` | `np.allclose(A, B)`

**Đáp án: A**

**Giải thích:** Định thức khác 0 tương đương khả nghịch.

**Q5. What does a derivative unit become for distance over time? | Đạo hàm quãng đường theo thời gian có đơn vị gì?**

A. The two-sided limit does not exist | Giới hạn hai phía không tồn tại

B. Distance per unit time | Khoảng cách trên mỗi đơn vị thời gian

C. Sampling spacing and numerical scheme | Khoảng cách mẫu và cách lấy sai phân

D. Yes, if nearby values approach one number | Có, nếu giá trị lân cận tiến đến cùng một số

**Đáp án: B**

**Giải thích:** Quãng đường chia thời gian cho đơn vị vận tốc.

**Q6. What does a positive-definite Hessian at a stationary point indicate? | Hessian xác định dương tại điểm dừng biểu thị gì?**

A. A strict local minimum | Cực tiểu địa phương nghiêm ngặt

B. A strict local maximum | Cực đại địa phương nghiêm ngặt

C. A saddle point | Điểm yên ngựa

D. The simple second-derivative test is inconclusive | Phép kiểm đạo hàm bậc hai đơn giản chưa kết luận

**Đáp án: A**

**Giải thích:** Độ cong dương mọi hướng cho cực tiểu địa phương nghiêm ngặt.

**Q7. If w=3, lr=0.1 and grad=6, what is next w? | Nếu w=3, lr=0.1 và gradient=6, w mới là gì?**

A. `2*x+3*y` | `2*x+3*y`

B. `[2*x,2*y]` | `[2*x,2*y]`

C. `2*w` | `2*w`

D. 2.4 | 2.4

**Đáp án: D**

**Giải thích:** 3−0.1×6=2.4.

**Q8. Which tool differentiates f with respect to x symbolically? | Hàm nào đạo hàm ký hiệu f theo x?**

A. `sp.diff(f,x)` | `sp.diff(f,x)`

B. `w = w - lr*gradient` | `w = w - lr*gradient`

C. `np.mean((pred-y)**2)` | `np.mean((pred-y)**2)`

D. A `for` loop | Vòng lặp `for`

**Đáp án: A**

**Giải thích:** diff tính đạo hàm ký hiệu.

**Q9. What is P(even) for a fair six-sided die? | Xác suất mặt chẵn của xúc xắc công bằng sáu mặt?**

A. `1/2` | `1/2`

B. 36 | 36

C. 4 | 4

D. Zero | Bằng 0

**Đáp án: A**

**Giải thích:** Ba trong sáu mặt là số chẵn.

**Q10. What is P(not A) in terms of P(A)? | P(không A) theo P(A) là gì?**

A. One | Bằng 1

B. `1-P(A)` | `1-P(A)`

C. No, sampling variation occurs | Không, có dao động do lấy mẫu

D. One die's result does not change probabilities of the other | Kết quả một xúc xắc không đổi xác suất của xúc xắc kia

**Đáp án: B**

**Giải thích:** Biến cố và biến cố đối có tổng xác suất 1.

**Q11. What is median of 2,4,100? | Median của 2,4,100 là bao nhiêu?**

A. 3 | 3

B. 4 | 4

C. 2/3 | 2/3

D. 1 | 1

**Đáp án: B**

**Giải thích:** Bốn nằm giữa dãy đã sắp.

**Q12. How do you calculate normal P(a<X≤b)? | Tính P(a<X≤b) cho chuẩn bằng gì?**

A. 0.5 | 0.5

B. CDF(b) minus CDF(a) | CDF(b) trừ CDF(a)

C. No, sampling noise remains | Không, vẫn có dao động lấy mẫu

D. From 0 to 1 inclusive | Từ 0 đến 1 gồm hai đầu

**Đáp án: B**

**Giải thích:** Hiệu xác suất tích lũy cho xác suất đoạn. Ví dụ P(−1<X≤1) bằng `norm.cdf(1)-norm.cdf(-1)`, xấp xỉ 0,6827.

**Q13. What does prior mean? | Prior có nghĩa gì?**

A. Probability before current evidence | Xác suất trước khi có bằng chứng hiện tại

B. Probability of evidence under a hypothesis | Xác suất bằng chứng khi giả thuyết đúng

C. Updated hypothesis probability after evidence | Xác suất giả thuyết được cập nhật sau bằng chứng

D. Probability of positive signal when no defect exists | Xác suất báo dương khi thực tế không có lỗi

**Đáp án: A**

**Giải thích:** Prior là xác suất nền.

**Q14. How does PCA choose its first component? | PCA chọn thành phần đầu ra sao?**

A. By largest explained variance | Theo phương sai giải thích lớn nhất

B. Variance of one feature | Phương sai của một đặc trưng

C. Two | Hai

D. `A @ v` approximately equals `λ*v` | `A @ v` xấp xỉ `λ*v`

**Đáp án: A**

**Giải thích:** Thành phần đầu tương ứng phương sai cao nhất.

**Q15. What is the unit of MSE when predictions are in meters? | Dự báo theo mét thì MSE có đơn vị gì?**

A. Square meters | Mét bình phương

B. Meters | Mét

C. MSE | MSE

D. Huber loss | Huber loss

**Đáp án: A**

**Giải thích:** Bình phương sai lệch mét cho đơn vị m².

**Q16. If P(A)=0.5 and P(B)=0.6 and they are independent, what is P(A and B)? | Nếu A, B độc lập có xác suất 0.5 và 0.6 thì P(A và B) là gì?**

A. 0.2 | 0.2

B. 0.56 | 0.56

C. 0.3 | 0.3

D. No; base rate and false positives also matter | Không; còn tỷ lệ nền và dương giả

**Đáp án: C**

**Giải thích:** Với biến cố độc lập, 0.5×0.6=0.3.

## Đề 07 — 16 câu

**Q1. What must be true to compute a 1-D dot product? | Muốn tính tích vô hướng của hai vector 1-D cần điều kiện gì?**

A. Zero | Bằng không

B. That its norm is nonzero | Norm khác không

C. The result can be physically misleading | Kết quả có thể sai ý nghĩa vật lý

D. They must have equal lengths | Chúng phải có cùng số phần tử

**Đáp án: D**

**Giải thích:** Từng thành phần được ghép theo vị trí tương ứng.

**Q2. What is the shape of `np.eye(3)`? | `np.eye(3)` tạo ma trận shape nào?**

A. `(2, 3)` | `(2, 3)`

B. `(3, 2)` | `(3, 2)`

C. `(2, 1)` | `(2, 1)`

D. `(3, 3)` | `(3, 3)`

**Đáp án: D**

**Giải thích:** Ma trận đơn vị bậc 3 là ma trận vuông.

**Q3. What happens when rows of A are multiples of each other? | Nếu các hàng A là bội nhau thì sao?**

A. It contains known target values | Nó chứa giá trị mục tiêu đã biết

B. They add no new independent direction | Chúng không bổ sung hướng độc lập mới

C. When observations outnumber unknowns or do not fit exactly | Khi nhiều quan sát hơn ẩn hoặc không khớp chính xác

D. Prediction is lower than actual | Dự báo thấp hơn thực tế

**Đáp án: B**

**Giải thích:** Hàng tỷ lệ chỉ lặp thông tin tuyến tính.

**Q4. What is determinant of [[2,1],[1,2]]? | Định thức [[2,1],[1,2]] bằng gì?**

A. Its determinant is nonzero | Định thức khác không

B. 3 | 3

C. Identity matrix | Ma trận đơn vị

D. `np.allclose(A, B)` | `np.allclose(A, B)`

**Đáp án: B**

**Giải thích:** Định thức 2×2 bằng 2×2−1×1.

**Q5. What determines finite-difference accuracy? | Độ chính xác sai phân hữu hạn phụ thuộc gì?**

A. The two-sided limit does not exist | Giới hạn hai phía không tồn tại

B. Distance per unit time | Khoảng cách trên mỗi đơn vị thời gian

C. Sampling spacing and numerical scheme | Khoảng cách mẫu và cách lấy sai phân

D. Yes, if nearby values approach one number | Có, nếu giá trị lân cận tiến đến cùng một số

**Đáp án: C**

**Giải thích:** Khoảng lấy mẫu ảnh hưởng độ dốc ước lượng.

**Q6. What does a negative-definite Hessian at a stationary point indicate? | Hessian xác định âm tại điểm dừng biểu thị gì?**

A. A strict local minimum | Cực tiểu địa phương nghiêm ngặt

B. A strict local maximum | Cực đại địa phương nghiêm ngặt

C. A saddle point | Điểm yên ngựa

D. The simple second-derivative test is inconclusive | Phép kiểm đạo hàm bậc hai đơn giản chưa kết luận

**Đáp án: B**

**Giải thích:** Độ cong âm mọi hướng cho cực đại địa phương nghiêm ngặt.

**Q7. Why record loss history? | Vì sao lưu lịch sử loss?**

A. To inspect optimization progress | Để xem tiến trình tối ưu

B. Each error must use its correct sample | Mỗi sai số cần đúng cặp quan sát

C. No, generalization needs validation | Không, cần kiểm chứng trên dữ liệu mới

D. Steepest increase | Hướng tăng nhanh nhất

**Đáp án: A**

**Giải thích:** Lịch sử cho thấy xu hướng giảm hoặc bất ổn.

**Q8. Which formula is MSE? | Công thức nào là MSE?**

A. `sp.diff(f,x)` | `sp.diff(f,x)`

B. `w = w - lr*gradient` | `w = w - lr*gradient`

C. `np.mean((pred-y)**2)` | `np.mean((pred-y)**2)`

D. A `for` loop | Vòng lặp `for`

**Đáp án: C**

**Giải thích:** MSE trung bình bình phương sai số.

**Q9. How many outcomes are possible with two ordered six-sided dice? | Hai xúc xắc sáu mặt theo cặp có thứ tự có bao nhiêu kết quả?**

A. `1/2` | `1/2`

B. 36 | 36

C. 4 | 4

D. Zero | Bằng 0

**Đáp án: B**

**Giải thích:** Hai xúc xắc có 6×6 cặp có thứ tự.

**Q10. Does a simulation always equal the true probability exactly? | Tỷ lệ mô phỏng có luôn bằng xác suất thật?**

A. One | Bằng 1

B. `1-P(A)` | `1-P(A)`

C. No, sampling variation occurs | Không, có dao động do lấy mẫu

D. One die's result does not change probabilities of the other | Kết quả một xúc xắc không đổi xác suất của xúc xắc kia

**Đáp án: C**

**Giải thích:** Mẫu hữu hạn dao động quanh xác suất nền.

**Q11. Which statistic resists large outliers better? | Thống kê nào ít nhạy với ngoại lệ cực lớn hơn?**

A. Squared input units | Bình phương đơn vị dữ liệu

B. Original input units | Đơn vị gốc của dữ liệu

C. Median | Trung vị

D. Mode | Yếu vị

**Đáp án: C**

**Giải thích:** Giá trị cực lớn ít tác động vị trí giữa.

**Q12. What is the range of probabilities? | Xác suất nằm trong đoạn nào?**

A. 0.5 | 0.5

B. CDF(b) minus CDF(a) | CDF(b) trừ CDF(a)

C. No, sampling noise remains | Không, vẫn có dao động lấy mẫu

D. From 0 to 1 inclusive | Từ 0 đến 1 gồm hai đầu

**Đáp án: D**

**Giải thích:** Xác suất không âm và không vượt một. Hai đầu 0 và 1 tương ứng biến cố không thể và chắc chắn.

**Q13. What does likelihood mean? | Likelihood biểu thị gì?**

A. Probability before current evidence | Xác suất trước khi có bằng chứng hiện tại

B. Probability of evidence under a hypothesis | Xác suất bằng chứng khi giả thuyết đúng

C. Updated hypothesis probability after evidence | Xác suất giả thuyết được cập nhật sau bằng chứng

D. Probability of positive signal when no defect exists | Xác suất báo dương khi thực tế không có lỗi

**Đáp án: B**

**Giải thích:** Likelihood xét bằng chứng khi giả thuyết đúng.

**Q14. What does a covariance diagonal entry represent? | Ô đường chéo covariance biểu thị gì?**

A. By largest explained variance | Theo phương sai giải thích lớn nhất

B. Variance of one feature | Phương sai của một đặc trưng

C. Two | Hai

D. `A @ v` approximately equals `λ*v` | `A @ v` xấp xỉ `λ*v`

**Đáp án: B**

**Giải thích:** Hiệp phương sai của biến với chính nó là phương sai.

**Q15. What is the unit of MAE when predictions are in meters? | Dự báo theo mét thì MAE có đơn vị gì?**

A. Square meters | Mét bình phương

B. Meters | Mét

C. MSE | MSE

D. Huber loss | Huber loss

**Đáp án: B**

**Giải thích:** Sai lệch tuyệt đối giữ đơn vị gốc.

**Q16. If an alert has 99% sensitivity, does that mean 99% of alerts are true defects? | Độ nhạy 99% có nghĩa 99% cảnh báo là lỗi thật không?**

A. 0.2 | 0.2

B. 0.56 | 0.56

C. 0.3 | 0.3

D. No; base rate and false positives also matter | Không; còn tỷ lệ nền và dương giả

**Đáp án: D**

**Giải thích:** Độ nhạy và posterior xét hai nhóm mẫu nền khác nhau.

## Đề 08 — 16 câu

**Q1. What does multiplying a vector by a scalar do? | Nhân vector với scalar làm gì?**

A. Scales every component | Nhân từng thành phần với scalar

B. Subtract corresponding components | Trừ các thành phần cùng vị trí

C. Euclidean distance between a and b | Khoảng cách Euclid giữa a và b

D. To multiply each weight by its intended feature | Để trọng số nhân đúng đặc trưng tương ứng

**Đáp án: A**

**Giải thích:** Nhân scalar làm đổi độ lớn từng thành phần.

**Q2. Which operator performs matrix multiplication? | Toán tử nào thực hiện nhân ma trận?**

A. `@` | `@`

B. `.T` | `.T`

C. `np.linalg.det(A)` | `np.linalg.det(A)`

D. `np.linalg.inv(A)` | `np.linalg.inv(A)`

**Đáp án: A**

**Giải thích:** @ thực hiện đúng quy tắc nhân ma trận.

**Q3. What does `np.allclose(A@x,b)` check? | `np.allclose(A@x,b)` kiểm tra gì?**

A. Every equation is satisfied | Mọi phương trình đều được thỏa

B. The sum of squared residuals | Tổng bình phương sai số dư

C. Whether a candidate solution approximately satisfies the system | Nghiệm thử có thỏa hệ gần đúng hay không

D. Ranks of A and its augmented matrix | Hạng của A và ma trận mở rộng

**Đáp án: C**

**Giải thích:** allclose so kết quả trong ngưỡng sai số số học.

**Q4. What does `A @ inv(A)` approximate? | `A @ inv(A)` gần bằng gì?**

A. Its determinant is nonzero | Định thức khác không

B. 3 | 3

C. Identity matrix | Ma trận đơn vị

D. `np.allclose(A, B)` | `np.allclose(A, B)`

**Đáp án: C**

**Giải thích:** Nhân ma trận với nghịch đảo bằng I trong tính toán chính xác.

**Q5. How does a derivative differ from an average slope? | Đạo hàm khác độ dốc trung bình thế nào?**

A. It describes a local infinitesimal change | Nó mô tả độ thay đổi cục bộ rất nhỏ

B. 2 | 2

C. `sympy.diff` | `sympy.diff`

D. It often uses one-sided differences | Nó thường dùng sai phân một phía

**Đáp án: A**

**Giải thích:** Độ dốc tức thời là đại lượng giới hạn cục bộ.

**Q6. What do mixed-sign Hessian eigenvalues indicate at a stationary point? | Trị riêng Hessian trái dấu ở điểm dừng biểu thị gì?**

A. A strict local minimum | Cực tiểu địa phương nghiêm ngặt

B. A strict local maximum | Cực đại địa phương nghiêm ngặt

C. A saddle point | Điểm yên ngựa

D. The simple second-derivative test is inconclusive | Phép kiểm đạo hàm bậc hai đơn giản chưa kết luận

**Đáp án: C**

**Giải thích:** Một số hướng tăng và hướng khác giảm.

**Q7. Why pair features and targets in the same order? | Vì sao cần ghép x và y cùng thứ tự?**

A. To inspect optimization progress | Để xem tiến trình tối ưu

B. Each error must use its correct sample | Mỗi sai số cần đúng cặp quan sát

C. No, generalization needs validation | Không, cần kiểm chứng trên dữ liệu mới

D. Steepest increase | Hướng tăng nhanh nhất

**Đáp án: B**

**Giải thích:** Hàng ghép sai làm sai số vô nghĩa.

**Q8. Which Python construct repeats optimization steps? | Cấu trúc Python nào lặp các bước tối ưu?**

A. `sp.diff(f,x)` | `sp.diff(f,x)`

B. `w = w - lr*gradient` | `w = w - lr*gradient`

C. `np.mean((pred-y)**2)` | `np.mean((pred-y)**2)`

D. A `for` loop | Vòng lặp `for`

**Đáp án: D**

**Giải thích:** for lặp các bước cập nhật.

**Q9. How many ordered pairs of dice sum to nine? | Bao nhiêu cặp có thứ tự của hai xúc xắc có tổng 9?**

A. `1/2` | `1/2`

B. 36 | 36

C. 4 | 4

D. Zero | Bằng 0

**Đáp án: C**

**Giải thích:** Bốn cặp là (3,6), (4,5), (5,4), (6,3).

**Q10. What does independence of two dice mean? | Hai xúc xắc độc lập nghĩa là gì?**

A. One | Bằng 1

B. `1-P(A)` | `1-P(A)`

C. No, sampling variation occurs | Không, có dao động do lấy mẫu

D. One die's result does not change probabilities of the other | Kết quả một xúc xắc không đổi xác suất của xúc xắc kia

**Đáp án: D**

**Giải thích:** Độc lập nghĩa là một kết quả không đổi xác suất của biến cố còn lại.

**Q11. Which statistic is useful for categorical labels? | Thống kê nào phù hợp nhãn phân loại?**

A. Squared input units | Bình phương đơn vị dữ liệu

B. Original input units | Đơn vị gốc của dữ liệu

C. Median | Trung vị

D. Mode | Yếu vị

**Đáp án: D**

**Giải thích:** Lấy trung bình mã chữ không có ý nghĩa số học.

**Q12. What happens when standard deviation of normal increases? | Std phân phối chuẩn tăng sẽ thế nào?**

A. Yes; only its total integral must be one | Có; chỉ tích phân toàn miền phải bằng một

B. The distribution becomes wider | Phân phối trải rộng hơn

C. Point probabilities behave differently | Xác suất tại một điểm có ý nghĩa khác nhau

D. Cumulative probability up to x | Xác suất tích lũy tới x

**Đáp án: B**

**Giải thích:** Cùng tổng diện tích được trải ra trên miền rộng hơn. Sigma lớn hơn không tự làm dịch mean; nó khiến số đo phân tán xa hơn quanh cùng tâm.

**Q13. What does posterior mean? | Posterior là gì?**

A. Probability before current evidence | Xác suất trước khi có bằng chứng hiện tại

B. Probability of evidence under a hypothesis | Xác suất bằng chứng khi giả thuyết đúng

C. Updated hypothesis probability after evidence | Xác suất giả thuyết được cập nhật sau bằng chứng

D. Probability of positive signal when no defect exists | Xác suất báo dương khi thực tế không có lỗi

**Đáp án: C**

**Giải thích:** Posterior đã tính đến bằng chứng quan sát.

**Q14. Does an eigenvalue always mean variance? | Trị riêng có luôn mang nghĩa phương sai không?**

A. Rows are samples and columns are features | Hàng là mẫu và cột là đặc trưng

B. Only when the matrix is an appropriate covariance matrix | Chỉ khi ma trận là covariance phù hợp

C. One principal-component feature per sample | Một đặc trưng thành phần chính cho mỗi mẫu

D. Feature scales and units | Thang đo và đơn vị các đặc trưng

**Đáp án: B**

**Giải thích:** Diễn giải phương sai cần ma trận hiệp phương sai.

**Q15. Which loss increases quadratically with error magnitude? | Loss nào tăng theo bình phương độ lớn lỗi?**

A. Square meters | Mét bình phương

B. Meters | Mét

C. MSE | MSE

D. Huber loss | Huber loss

**Đáp án: C**

**Giải thích:** MSE bình phương độ lớn lỗi.

**Q16. Why does Bayes need the base rate? | Vì sao Bayes cần tỷ lệ nền?**

A. Rare cases can yield many false alarms among positives | Sự kiện hiếm có thể làm dương giả chiếm nhiều trong cảnh báo

B. The formula divides by P(B) | Vì công thức chia cho P(B)

C. That viewing ads caused purchases | Việc xem quảng cáo gây ra hành vi mua

D. They condition on different reference groups | Chúng xét trên hai nhóm điều kiện khác nhau

**Đáp án: A**

**Giải thích:** Sự kiện hiếm có thể khiến phần lớn cảnh báo là dương giả.

## Đề 09 — 16 câu

**Q1. How is vector subtraction performed? | Phép trừ vector được thực hiện thế nào?**

A. Scales every component | Nhân từng thành phần với scalar

B. Subtract corresponding components | Trừ các thành phần cùng vị trí

C. Euclidean distance between a and b | Khoảng cách Euclid giữa a và b

D. To multiply each weight by its intended feature | Để trọng số nhân đúng đặc trưng tương ứng

**Đáp án: B**

**Giải thích:** Phép trừ vector diễn ra theo từng thành phần.

**Q2. Which dimensions must match for A @ B? | Nhân A @ B cần các chiều nào bằng nhau?**

A. Columns of A and rows of B | Số cột A và số hàng B

B. Element-wise multiplication | Nhân theo từng phần tử

C. `np.linalg.solve(A, b)` | `np.linalg.solve(A, b)`

D. A linear algebra error | Lỗi đại số tuyến tính

**Đáp án: A**

**Giải thích:** Nhân ma trận yêu cầu hai chiều trong trùng.

**Q3. What does the final column of an augmented matrix represent? | Cột cuối của ma trận mở rộng biểu diễn gì?**

A. Three equations or observations | Ba phương trình hoặc quan sát

B. Coefficients of two unknowns | Hệ số của hai ẩn

C. The right-hand-side values | Các giá trị vế phải

D. It cannot have a unique solution for every b | Không thể có nghiệm duy nhất với mọi b

**Đáp án: C**

**Giải thích:** Ma trận mở rộng ghi các vế phải ở cột cuối.

**Q4. How do you test approximate equality of float arrays? | Kiểm tra hai mảng float gần bằng nhau bằng gì?**

A. Its determinant is nonzero | Định thức khác không

B. 3 | 3

C. Identity matrix | Ma trận đơn vị

D. `np.allclose(A, B)` | `np.allclose(A, B)`

**Đáp án: D**

**Giải thích:** allclose chấp nhận sai số dấu phẩy động nhỏ.

**Q5. What is the derivative of 2x+3? | Đạo hàm của 2x+3 là gì?**

A. It describes a local infinitesimal change | Nó mô tả độ thay đổi cục bộ rất nhỏ

B. 2 | 2

C. `sympy.diff` | `sympy.diff`

D. It often uses one-sided differences | Nó thường dùng sai phân một phía

**Đáp án: B**

**Giải thích:** Hệ số của x cho đạo hàm bằng 2.

**Q6. What if a Hessian has a zero eigenvalue at a stationary point? | Nếu Hessian có trị riêng 0 tại điểm dừng thì sao?**

A. A strict local minimum | Cực tiểu địa phương nghiêm ngặt

B. A strict local maximum | Cực đại địa phương nghiêm ngặt

C. A saddle point | Điểm yên ngựa

D. The simple second-derivative test is inconclusive | Phép kiểm đạo hàm bậc hai đơn giản chưa kết luận

**Đáp án: D**

**Giải thích:** Trị riêng 0 cần kiểm tra sâu hơn.

**Q7. Does falling training loss guarantee test accuracy? | Loss train giảm có đảm bảo độ chính xác test?**

A. To inspect optimization progress | Để xem tiến trình tối ưu

B. Each error must use its correct sample | Mỗi sai số cần đúng cặp quan sát

C. No, generalization needs validation | Không, cần kiểm chứng trên dữ liệu mới

D. Steepest increase | Hướng tăng nhanh nhất

**Đáp án: C**

**Giải thích:** Cần dữ liệu độc lập để đo tổng quát hóa.

**Q8. Why might a large learning rate fail? | Vì sao learning rate lớn dễ thất bại?**

A. Updates can overshoot or diverge | Bước cập nhật có thể vượt cực tiểu hoặc phân kỳ

B. It can make convergence slow | Nó có thể làm hội tụ chậm

C. Locally reduce the objective | Giảm hàm mục tiêu về mặt cục bộ

D. No, minibatches can cause multiple updates | Không, nhiều minibatch có thể tạo nhiều lần cập nhật

**Đáp án: A**

**Giải thích:** Bước lớn có thể vượt qua cực tiểu liên tục.

**Q9. What is the probability of the empty event? | Xác suất biến cố rỗng là gì?**

A. `1/2` | `1/2`

B. 36 | 36

C. 4 | 4

D. Zero | Bằng 0

**Đáp án: D**

**Giải thích:** Biến cố không thể có xác suất 0.

**Q10. What does a fixed RNG seed not guarantee? | Seed RNG cố định không bảo đảm điều gì?**

A. Display order is not promised | Thứ tự hiển thị không được đảm bảo

B. That empirical frequency equals theoretical probability | Tần suất thực nghiệm đúng bằng xác suất lý thuyết

C. It tends to reduce sampling variability | Thường làm giảm dao động lấy mẫu

D. Its faces do not have equal probabilities | Các mặt không đồng xác suất

**Đáp án: B**

**Giải thích:** Seed giúp lặp lại mô phỏng nhưng không loại dao động.

**Q11. Does std equal standard error? | Std có giống sai số chuẩn không?**

A. No, std measures spread of individual values | Không, std đo độ phân tán quan sát

B. Yes, large outliers can pull it up | Có, ngoại lệ lớn kéo mean lên

C. Different denominators give different results | Mẫu số khác nhau cho kết quả khác

D. Summary statistics can lose meaning | Thống kê tổng hợp có thể mất ý nghĩa

**Đáp án: A**

**Giải thích:** SE đo độ biến thiên của thống kê ước lượng.

**Q12. Why distinguish discrete and continuous variables? | Vì sao phân biệt biến rời rạc và liên tục?**

A. Yes; only its total integral must be one | Có; chỉ tích phân toàn miền phải bằng một

B. The distribution becomes wider | Phân phối trải rộng hơn

C. Point probabilities behave differently | Xác suất tại một điểm có ý nghĩa khác nhau

D. Cumulative probability up to x | Xác suất tích lũy tới x

**Đáp án: C**

**Giải thích:** PMF là xác suất còn PDF là mật độ. Số đếm như X=3 có xác suất tại điểm dương, còn biến đo liên tục có xác suất bằng đúng một giá trị là 0.

**Q13. What is a false-positive rate? | Tỷ lệ dương giả là gì?**

A. Probability before current evidence | Xác suất trước khi có bằng chứng hiện tại

B. Probability of evidence under a hypothesis | Xác suất bằng chứng khi giả thuyết đúng

C. Updated hypothesis probability after evidence | Xác suất giả thuyết được cập nhật sau bằng chứng

D. Probability of positive signal when no defect exists | Xác suất báo dương khi thực tế không có lỗi

**Đáp án: D**

**Giải thích:** Dương giả là cảnh báo dương ở trường hợp không lỗi.

**Q14. What does `PCA(n_components=1)` preserve? | `PCA(n_components=1)` giữ lại gì?**

A. Rows are samples and columns are features | Hàng là mẫu và cột là đặc trưng

B. Only when the matrix is an appropriate covariance matrix | Chỉ khi ma trận là covariance phù hợp

C. One principal-component feature per sample | Một đặc trưng thành phần chính cho mỗi mẫu

D. Feature scales and units | Thang đo và đơn vị các đặc trưng

**Đáp án: C**

**Giải thích:** Dữ liệu sau chiếu còn một cột, vẫn giữ số hàng.

**Q15. Which loss is easier to interpret in the original output units? | Loss nào dễ đọc theo đơn vị đầu ra ban đầu?**

A. To avoid log(0) and numerical infinities | Để tránh log(0) và vô cực số học

B. MAE | MAE

C. No, evaluate on held-out data | Không, cần đánh giá trên dữ liệu độc lập

D. Predicted probability assigned to the true class | Xác suất dự báo dành cho lớp đúng

**Đáp án: B**

**Giải thích:** MAE báo sai số trung bình cùng đơn vị đo.

**Q16. Why must P(B)>0 for P(A given B)? | Vì sao cần P(B)>0 khi tính P(A khi B)?**

A. Rare cases can yield many false alarms among positives | Sự kiện hiếm có thể làm dương giả chiếm nhiều trong cảnh báo

B. The formula divides by P(B) | Vì công thức chia cho P(B)

C. That viewing ads caused purchases | Việc xem quảng cáo gây ra hành vi mua

D. They condition on different reference groups | Chúng xét trên hai nhóm điều kiện khác nhau

**Đáp án: B**

**Giải thích:** Chia cho 0 không xác định.

## Đề 10 — 16 câu

**Q1. What does `np.linalg.norm(a-b)` measure? | `np.linalg.norm(a-b)` đo điều gì?**

A. Scales every component | Nhân từng thành phần với scalar

B. Subtract corresponding components | Trừ các thành phần cùng vị trí

C. Euclidean distance between a and b | Khoảng cách Euclid giữa a và b

D. To multiply each weight by its intended feature | Để trọng số nhân đúng đặc trưng tương ứng

**Đáp án: C**

**Giải thích:** Norm của độ dịch chuyển cho khoảng cách.

**Q2. What does `A * B` do for compatible NumPy arrays? | `A * B` trên mảng NumPy tương thích làm gì?**

A. Columns of A and rows of B | Số cột A và số hàng B

B. Element-wise multiplication | Nhân theo từng phần tử

C. `np.linalg.solve(A, b)` | `np.linalg.solve(A, b)`

D. A linear algebra error | Lỗi đại số tuyến tính

**Đáp án: B**

**Giải thích:** Dấu sao nhân phần tử tương ứng có broadcasting.

**Q3. When is `lstsq` useful? | Khi nào `lstsq` hữu ích?**

A. It contains known target values | Nó chứa giá trị mục tiêu đã biết

B. They add no new independent direction | Chúng không bổ sung hướng độc lập mới

C. When observations outnumber unknowns or do not fit exactly | Khi nhiều quan sát hơn ẩn hoặc không khớp chính xác

D. Prediction is lower than actual | Dự báo thấp hơn thực tế

**Đáp án: C**

**Giải thích:** Bình phương tối thiểu tìm cách khớp tốt nhất khi hệ không thỏa hết.

**Q4. What happens to a singular matrix when using `np.linalg.inv`? | Dùng `np.linalg.inv` với ma trận suy biến thường gây gì?**

A. Columns of A and rows of B | Số cột A và số hàng B

B. Element-wise multiplication | Nhân theo từng phần tử

C. `np.linalg.solve(A, b)` | `np.linalg.solve(A, b)`

D. A linear algebra error | Lỗi đại số tuyến tính

**Đáp án: D**

**Giải thích:** Ma trận suy biến không có nghịch đảo.

**Q5. Which tool calculates symbolic derivatives? | Công cụ nào tính đạo hàm ký hiệu?**

A. It describes a local infinitesimal change | Nó mô tả độ thay đổi cục bộ rất nhỏ

B. 2 | 2

C. `sympy.diff` | `sympy.diff`

D. It often uses one-sided differences | Nó thường dùng sai phân một phía

**Đáp án: C**

**Giải thích:** SymPy hỗ trợ đạo hàm ký hiệu bằng diff.

**Q6. Why isn't zero gradient alone sufficient to prove a minimum? | Vì sao gradient 0 chưa đủ chứng minh cực tiểu?**

A. `(3,3)` | `(3,3)`

B. Sensitivities of one output to each input | Độ nhạy của một đầu ra theo từng đầu vào

C. How each output responds to one input | Các đầu ra đáp ứng với một đầu vào

D. It can also occur at a maximum or saddle | Nó còn xuất hiện ở cực đại hoặc yên ngựa

**Đáp án: D**

**Giải thích:** Cực đại và yên ngựa cũng có thể có gradient 0.

**Q7. Which direction does a gradient point locally? | Gradient hướng theo phía nào về mặt cục bộ?**

A. To inspect optimization progress | Để xem tiến trình tối ưu

B. Each error must use its correct sample | Mỗi sai số cần đúng cặp quan sát

C. No, generalization needs validation | Không, cần kiểm chứng trên dữ liệu mới

D. Steepest increase | Hướng tăng nhanh nhất

**Đáp án: D**

**Giải thích:** Gradient hướng tăng cục bộ nhanh nhất.

**Q8. Why might a very small learning rate be inefficient? | Vì sao learning rate quá nhỏ kém hiệu quả?**

A. Updates can overshoot or diverge | Bước cập nhật có thể vượt cực tiểu hoặc phân kỳ

B. It can make convergence slow | Nó có thể làm hội tụ chậm

C. Locally reduce the objective | Giảm hàm mục tiêu về mặt cục bộ

D. No, minibatches can cause multiple updates | Không, nhiều minibatch có thể tạo nhiều lần cập nhật

**Đáp án: B**

**Giải thích:** Bước quá nhỏ khiến tối ưu chậm.

**Q9. What is the probability of the entire sample space? | Xác suất của cả không gian mẫu là gì?**

A. One | Bằng 1

B. `1-P(A)` | `1-P(A)`

C. No, sampling variation occurs | Không, có dao động do lấy mẫu

D. One die's result does not change probabilities of the other | Kết quả một xúc xắc không đổi xác suất của xúc xắc kia

**Đáp án: A**

**Giải thích:** Biến cố chắc chắn có xác suất 1.

**Q10. How does larger sample size generally affect estimate variability? | Tăng số mẫu thường ảnh hưởng độ dao động ước lượng thế nào?**

A. Display order is not promised | Thứ tự hiển thị không được đảm bảo

B. That empirical frequency equals theoretical probability | Tần suất thực nghiệm đúng bằng xác suất lý thuyết

C. It tends to reduce sampling variability | Thường làm giảm dao động lấy mẫu

D. Its faces do not have equal probabilities | Các mặt không đồng xác suất

**Đáp án: C**

**Giải thích:** Mẫu lớn thường ổn định tần suất tương đối hơn.

**Q11. Can mean lie above most observations? | Mean có thể lớn hơn phần lớn quan sát không?**

A. No, std measures spread of individual values | Không, std đo độ phân tán quan sát

B. Yes, large outliers can pull it up | Có, ngoại lệ lớn kéo mean lên

C. Different denominators give different results | Mẫu số khác nhau cho kết quả khác

D. Summary statistics can lose meaning | Thống kê tổng hợp có thể mất ý nghĩa

**Đáp án: B**

**Giải thích:** Mean phụ thuộc tổng các giá trị.

**Q12. What does norm.cdf(x,loc,scale) return? | norm.cdf(x,loc,scale) trả gì?**

A. Yes; only its total integral must be one | Có; chỉ tích phân toàn miền phải bằng một

B. The distribution becomes wider | Phân phối trải rộng hơn

C. Point probabilities behave differently | Xác suất tại một điểm có ý nghĩa khác nhau

D. Cumulative probability up to x | Xác suất tích lũy tới x

**Đáp án: D**

**Giải thích:** Nó là P(X≤x) theo phân phối chuẩn. Không lấy chiều cao PDF nếu câu hỏi là P(X≤x); cần dùng `cdf` để tính xác suất tích lũy.

**Q13. What is P(A given B) if 20 of 100 B cases have A? | P(A khi B) là gì nếu 20 trên 100 ca B có A?**

A. 0.2 | 0.2

B. 0.56 | 0.56

C. 0.3 | 0.3

D. No; base rate and false positives also matter | Không; còn tỷ lệ nền và dương giả

**Đáp án: A**

**Giải thích:** 20 chia 100 bằng 0.2.

**Q14. What should be considered before comparing PCA variances across features? | Cần lưu ý gì trước khi so phương sai PCA giữa đặc trưng?**

A. Rows are samples and columns are features | Hàng là mẫu và cột là đặc trưng

B. Only when the matrix is an appropriate covariance matrix | Chỉ khi ma trận là covariance phù hợp

C. One principal-component feature per sample | Một đặc trưng thành phần chính cho mỗi mẫu

D. Feature scales and units | Thang đo và đơn vị các đặc trưng

**Đáp án: D**

**Giải thích:** Đặc trưng có thang lớn có thể lấn át PCA nếu chưa chuẩn hóa.

**Q15. Does a lower training loss guarantee better unseen-data performance? | Training loss thấp có bảo đảm dự đoán tốt trên dữ liệu mới?**

A. To avoid log(0) and numerical infinities | Để tránh log(0) và vô cực số học

B. MAE | MAE

C. No, evaluate on held-out data | Không, cần đánh giá trên dữ liệu độc lập

D. Predicted probability assigned to the true class | Xác suất dự báo dành cho lớp đúng

**Đáp án: C**

**Giải thích:** Khả năng tổng quát cần kiểm chứng bằng dữ liệu độc lập.

**Q16. What distinguishes P(A given B) from P(B given A)? | P(A khi B) khác P(B khi A) ở đâu?**

A. Rare cases can yield many false alarms among positives | Sự kiện hiếm có thể làm dương giả chiếm nhiều trong cảnh báo

B. The formula divides by P(B) | Vì công thức chia cho P(B)

C. That viewing ads caused purchases | Việc xem quảng cáo gây ra hành vi mua

D. They condition on different reference groups | Chúng xét trên hai nhóm điều kiện khác nhau

**Đáp án: D**

**Giải thích:** Đảo điều kiện làm thay đổi mẫu số.
