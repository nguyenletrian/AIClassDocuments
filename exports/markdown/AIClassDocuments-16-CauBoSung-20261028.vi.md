# 16 câu bổ sung: Đại số tuyến tính, đạo hàm, xác suất, thống kê và PCA

16 câu từ bộ đề mới (28/10/2026). Câu tiếng Anh được giữ nguyên; bản dịch tiếng Việt, đáp án và giải thích được bổ sung.

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
