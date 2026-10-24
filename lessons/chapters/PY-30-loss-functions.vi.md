# PY-30 — Loss: MSE, MAE, Huber, cross-entropy và KL


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **MSE** — sai số bình phương trung bình; **MAE** — sai số tuyệt đối trung bình.

`Dự đoán → Sai số → Loss → Tối ưu hóa`

Kiến thức này liên quan đến việc biểu diễn, đánh giá hoặc tối ưu tính toán phục vụ AI. Đọc ví dụ trước khi liên hệ tới mô hình phức tạp.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| MSE | sai số bình phương trung bình | Trung bình bình phương hiệu dự đoán và giá trị thật |
| MAE | sai số tuyệt đối trung bình | Trung bình trị tuyệt đối sai số |
| Cross-entropy | entropy chéo | Phạt dự đoán xác suất sai nhãn mạnh hơn |
| KL divergence | độ lệch KL | Đo sai khác một chiều giữa hai phân phối xác suất |

## 3. Hàm và cách gọi bằng Python

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm / tham số | Giải thích |
|---|---|
| `np.mean((y-pred)**2)` | MSE nhạy với sai số lớn do bình phương |
| `np.mean(np.abs(y-pred))` | MAE ít khuếch đại outlier hơn MSE |
| `np.where(abs_err<=delta,... )` | Huber phối hợp bình phương và tuyến tính |
| `-np.sum(y*np.log(probs))` | Cross-entropy trên xác suất có clip để tránh log(0) |

## 4. Khái niệm liên quan

**Nội dung chính:** loss đo mức sai giữa dự báo và mục tiêu. Bài học đi từ hai cách tính sai lệch trên số (**MSE**, **MAE**), tới cách kết hợp hai mức phạt (**Huber**), rồi sang loss trên **xác suất và phân phối** (**cross-entropy**, **KL**). Chọn loss phải dựa vào ý nghĩa dữ liệu và mức phạt cần thiết.

### 4.1. MSE — Sai số bình phương trung bình

**Từ vựng trong mục:** **MSE** — Mean Squared Error; **Residual** — sai lệch.

**Loss function** là hàm cho biết dự báo sai lệch đến mức nào so với mục tiêu, để ta đánh giá hoặc tối ưu mô hình. **MSE** lấy sai số `(dự báo−thực tế)`, bình phương từng sai số rồi **trung bình**. Với thực tế `[2,3]` và dự báo `[1,4]`, sai số là `[-1,+1]`, bình phương thành `[1,1]` và MSE bằng 1. Đơn vị MSE là **bình phương đơn vị đầu ra**, không phải cùng đơn vị như giá nhà.

```python
import numpy as np

y_true = np.array([2, 3])
y_pred = np.array([1, 4])
print(np.mean((y_true - y_pred) ** 2))
```

**Kết quả khi chạy:**

```text
1.0
```

MSE bằng 1 đơn vị bình phương. Sai số lớn được phạt mạnh hơn vì bình phương.

### 4.2. MAE — Sai số tuyệt đối trung bình

**Từ vựng trong mục:** **MAE** — Mean Absolute Error; **Absolute error** — sai số tuyệt đối.

**MAE** lấy trị tuyệt đối của từng sai số rồi chia cho số quan sát. Ví dụ thực tế `[10,20,30]` và dự báo `[9,19,50]` có sai lệch tuyệt đối `[1,1,20]`, nên MAE bằng `22/3≈7.333`. Khác MSE, MAE có **cùng đơn vị** với đầu ra và không bình phương để khuếch đại lỗi lớn. Nó không có nghĩa là loại bỏ ảnh hưởng của ngoại lệ hoàn toàn.

```python
import numpy as np

y_true = np.array([10, 20, 30])
y_pred = np.array([9, 19, 50])
print(round(float(np.mean(np.abs(y_true - y_pred))), 3))
```

**Kết quả khi chạy:**

```text
7.333
```

Sai lệch trung bình tuyệt đối khoảng 7,333 đơn vị đo.

### 4.3. Huber — Trộn bình phương và tuyến tính theo ngưỡng

**Từ vựng trong mục:** **Huber loss** — tổn thất Huber; **Delta** — ngưỡng.

**Huber** dùng mức phạt giống **bình phương** khi `|e|≤δ` và chuyển sang **tuyến tính** khi lỗi vượt δ. Với δ=1: lỗi có độ lớn 1 mất 0.5, độ lớn 2 mất 1.5, độ lớn 5 mất 4.5. Trung bình ba lỗi `[-1,2,5]` là `6.5/3≈2.167`. Huber là cách cân bằng giữa MSE nhạy với lỗi lớn và MAE tăng tuyến tính; δ quyết định điểm chuyển và mang cùng đơn vị với sai số.

```python
import numpy as np

e = np.array([-1.0, 2.0, 5.0])
delta = 1.0
loss = np.where(
    np.abs(e) <= delta,
    0.5 * e ** 2,
    delta * (np.abs(e) - 0.5 * delta),
)
print(round(float(loss.mean()), 3))
```

**Kết quả khi chạy:**

```text
2.167
```

Tổn thất trung bình xấp xỉ 2,167 theo Huber δ=1; lỗi lớn không bị bình phương mãi.

### 4.4. Cross-entropy và KL — So nhãn hoặc phân phối

**Từ vựng trong mục:** **Cross-entropy** — entropy chéo; **KL divergence** — phân kỳ KL.

**Cross-entropy** đánh giá phân phối dự báo so với phân phối nhãn/đích. Với phân loại một nhãn đúng, dự báo xác suất cho nhãn đúng là 0.8 thì loss bằng `−ln(0.8)≈0.2231`: xác suất cho nhãn đúng càng thấp, phạt càng lớn. **KL divergence** `D_KL(P||Q)=Σ P_i ln(P_i/Q_i)` so sự khác nhau giữa **hai phân phối** P và Q; với `P=[0.5,0.5]`, `Q=[0.6,0.4]`, KL≈0.0204. KL **không đối xứng** và không phải khoảng cách hình học. Các xác suất trong log cần dương; trong code thực tế có thể clip hoặc xử lý giá trị 0 đúng quy ước.

```python
import numpy as np

p_true = 0.8
P = np.array([0.5, 0.5])
Q = np.array([0.6, 0.4])
print(round(float(-np.log(p_true)), 4))
print(round(float(np.sum(P * np.log(P / Q))), 4))
```

**Kết quả khi chạy:**

```text
0.2231
0.0204
```

Dòng đầu là cross-entropy của nhãn đúng; dòng sau là KL từ phân phối P sang Q. Hai số mang ý nghĩa khác nhau.

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Đánh giá sai số giá nhà bằng MSE

**Tình huống thực tế:** Hai căn nhà có giá thực tế `[100,200]` và dự báo `[110,170]`, tất cả cùng đơn vị triệu đồng. Cần đánh giá mô hình bằng mức phạt nhấn mạnh dự báo sai lớn.

**Vì sao chọn cách giải này?** Bình phương lỗi khiến dự báo sai 30 triệu bị phạt mạnh hơn lỗi 10 triệu.

**Quy trình giải:**

1. Tạo hai mảng giá thực tế và giá dự báo theo đúng thứ tự căn nhà.
2. Trừ, bình phương từng sai lệch, lấy trung bình.
3. In MSE; đơn vị là triệu đồng bình phương.

```python
import numpy as np

y_true = np.array([100, 200])
y_pred = np.array([110, 170])
print(np.mean((y_true - y_pred) ** 2))
```

**Kết quả khi chạy:**

```text
500.0
```

MSE bằng 500 (triệu đồng)², không phải sai số tiền trung bình 500 triệu.

### Tình huống 2 — Đo lỗi trung bình dễ hiểu bằng MAE

**Tình huống thực tế:** Ba kết quả thực tế `[10,20,30]` và dự báo `[9,19,50]` cùng đơn vị có một dự báo sai lớn ở vị trí cuối. Cần đo sai lệch trung bình theo đơn vị gốc.

**Vì sao chọn cách giải này?** MAE đo trị tuyệt đối nên dễ diễn giải theo cùng đơn vị; không bình phương lỗi lớn.

**Quy trình giải:**

1. Tạo mảng thực tế và dự báo cùng thứ tự.
2. Lấy trị tuyệt đối sai lệch theo từng quan sát rồi trung bình.
3. In kết quả làm tròn ba chữ số.

```python
import numpy as np

y_true = np.array([10, 20, 30])
y_pred = np.array([9, 19, 50])
print(round(float(np.mean(np.abs(y_true - y_pred))), 3))
```

**Kết quả khi chạy:**

```text
7.333
```

Độ lệch trung bình tuyệt đối khoảng 7.333 đơn vị gốc.

### Tình huống 3 — Áp dụng Huber cho số đo nhiễu

**Tình huống thực tế:** Ba sai số thiết bị là `[−1,2,5]` đơn vị đo. Dùng Huber với ngưỡng δ=1 để tăng phạt tuyến tính khi lỗi lớn.

**Vì sao chọn cách giải này?** Huber dùng phần bình phương ở lỗi nhỏ và phần tuyến tính ở lỗi lớn, tránh khuếch đại lỗi 5 quá mạnh.

**Quy trình giải:**

1. Lưu ba sai số và ngưỡng δ=1.
2. Dùng `np.where` tính hai nhánh của hàm Huber theo độ lớn lỗi.
3. Lấy trung bình và in sau làm tròn.

```python
import numpy as np

e = np.array([-1.0, 2.0, 5.0])
delta = 1.0
loss = np.where(
    np.abs(e) <= delta,
    0.5 * e ** 2,
    delta * (np.abs(e) - 0.5 * delta),
)
print(round(float(loss.mean()), 3))
```

**Kết quả khi chạy:**

```text
2.167
```

Loss Huber trung bình khoảng 2.167 cho ba sai số với δ=1.

### Tình huống 4 — Tính cross-entropy của nhãn đúng

**Tình huống thực tế:** Bộ phân loại đưa xác suất 0.8 cho nhãn đúng của một mẫu. Hãy tính mức phạt logarit cho dự báo này.

**Vì sao chọn cách giải này?** Với nhãn one-hot, cross-entropy bằng âm log xác suất của nhãn đúng.

**Quy trình giải:**

1. Lưu xác suất nhãn đúng 0.8, giá trị nằm trong (0,1].
2. Tính `-math.log(prob_true)`.
3. Làm tròn bốn chữ số và in loss.

```python
import math

prob_true = 0.8
print(round(-math.log(prob_true), 4))
```

**Kết quả khi chạy:**

```text
0.2231
```

Nếu mô hình tăng xác suất cho nhãn đúng về gần 1, loss giảm về gần 0.

### Tình huống 5 — So hai phân phối bằng KL divergence

**Tình huống thực tế:** Phân phối P là `[0.5,0.5]` và Q là `[0.6,0.4]` cho hai lớp; các tổng đều bằng 1. Cần đo P khác Q bao nhiêu theo chiều `D_KL(P||Q)`.

**Vì sao chọn cách giải này?** KL cân chênh lệch logarit theo xác suất P và phụ thuộc chiều so sánh, không phải khoảng cách đối xứng.

**Quy trình giải:**

1. Tạo hai phân phối dương, có tổng 1.
2. Tính `P * log(P/Q)` ở từng lớp rồi cộng.
3. In KL làm tròn bốn chữ số.

```python
import numpy as np

P = np.array([0.5, 0.5])
Q = np.array([0.6, 0.4])
print(round(float(np.sum(P * np.log(P / Q))), 4))
```

**Kết quả khi chạy:**

```text
0.0204
```

KL dương và nhỏ vì hai phân phối khá gần nhau, nhưng không đồng nhất.

## 6. Sai lầm thường gặp

- **MSE** có đơn vị đầu ra bình phương, **MAE** có đơn vị gốc; không đọc MSE như mức lệch tiền trung bình.
- Huber cần ngưỡng δ phù hợp đơn vị sai số; ngưỡng này quyết định khi nào chuyển từ phạt bình phương sang tuyến tính.
- Cross-entropy với nhãn đúng cần xác suất **của lớp đúng**, không phải điểm lớn nhất bất kỳ.
- `log(0)` không xác định; phải xử lý xác suất bằng công thức ổn định hoặc clip phù hợp khi dùng NumPy đơn giản.
- KL **bất đối xứng**, không phải khoảng cách Euclid và chỉ có nghĩa với các phân phối hợp lệ.
- Loss huấn luyện thấp không thay thế việc đánh giá trên tập validation/test độc lập.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Chỉ hỏi kiến thức lý thuyết, so sánh loss và đọc công thức, không hỏi dữ liệu tình huống.**

**Q1. What is MSE? — MSE là gì?**

A. Mean squared prediction error — Trung bình sai số dự báo bình phương

B. Mean absolute prediction error — Trung bình trị tuyệt đối sai số

C. Quadratic for small errors and linear for large — Bình phương lỗi nhỏ, tuyến tính lỗi lớn

D. Compare two probability distributions in a directed way — So hai phân phối xác suất có phân biệt chiều

**Q2. What is MAE? — MAE là gì?**

A. Mean squared prediction error — Trung bình sai số dự báo bình phương

B. Mean absolute prediction error — Trung bình trị tuyệt đối sai số

C. Quadratic for small errors and linear for large — Bình phương lỗi nhỏ, tuyến tính lỗi lớn

D. Compare two probability distributions in a directed way — So hai phân phối xác suất có phân biệt chiều

**Q3. What characterizes Huber loss? — Đặc trưng của Huber loss là gì?**

A. Mean squared prediction error — Trung bình sai số dự báo bình phương

B. Mean absolute prediction error — Trung bình trị tuyệt đối sai số

C. Quadratic for small errors and linear for large — Bình phương lỗi nhỏ, tuyến tính lỗi lớn

D. Compare two probability distributions in a directed way — So hai phân phối xác suất có phân biệt chiều

**Q4. What is KL divergence used for? — KL divergence dùng để làm gì?**

A. Mean squared prediction error — Trung bình sai số dự báo bình phương

B. Mean absolute prediction error — Trung bình trị tuyệt đối sai số

C. Quadratic for small errors and linear for large — Bình phương lỗi nhỏ, tuyến tính lỗi lớn

D. Compare two probability distributions in a directed way — So hai phân phối xác suất có phân biệt chiều

**Q5. What does categorical cross-entropy penalize? — Categorical cross-entropy phạt điều gì?**

A. Low predicted probability for the correct label — Xác suất dự đoán thấp cho nhãn đúng

B. `mean((y-pred)**2)` — `mean((y-pred)**2)`

C. `mean(abs(y-pred))` — `mean(abs(y-pred))`

D. `delta` — `delta`

**Q6. Which formula computes MSE? — Công thức nào tính MSE?**

A. Low predicted probability for the correct label — Xác suất dự đoán thấp cho nhãn đúng

B. `mean((y-pred)**2)` — `mean((y-pred)**2)`

C. `mean(abs(y-pred))` — `mean(abs(y-pred))`

D. `delta` — `delta`

**Q7. Which formula computes MAE? — Công thức nào tính MAE?**

A. Low predicted probability for the correct label — Xác suất dự đoán thấp cho nhãn đúng

B. `mean((y-pred)**2)` — `mean((y-pred)**2)`

C. `mean(abs(y-pred))` — `mean(abs(y-pred))`

D. `delta` — `delta`

**Q8. Which parameter sets Huber's transition point? — Tham số nào đặt điểm chuyển Huber?**

A. Low predicted probability for the correct label — Xác suất dự đoán thấp cho nhãn đúng

B. `mean((y-pred)**2)` — `mean((y-pred)**2)`

C. `mean(abs(y-pred))` — `mean(abs(y-pred))`

D. `delta` — `delta`

**Q9. What does `−log(p_true)` represent for one correct class? — `−log(p_true)` biểu thị gì cho một nhãn đúng?**

A. Cross-entropy loss for that sample — Cross-entropy của mẫu đó

B. Nonnegative — Không âm

C. No, KL is asymmetric — Không, KL bất đối xứng

D. The distributions are identical — Hai phân phối giống nhau

**Q10. What is the sign of KL divergence for valid distributions? — KL divergence có dấu gì với phân phối hợp lệ?**

A. Cross-entropy loss for that sample — Cross-entropy của mẫu đó

B. Nonnegative — Không âm

C. No, KL is asymmetric — Không, KL bất đối xứng

D. The distributions are identical — Hai phân phối giống nhau

**Q11. Does swapping P and Q generally preserve KL? — Đổi chỗ P và Q có giữ nguyên KL không?**

A. Cross-entropy loss for that sample — Cross-entropy của mẫu đó

B. Nonnegative — Không âm

C. No, KL is asymmetric — Không, KL bất đối xứng

D. The distributions are identical — Hai phân phối giống nhau

**Q12. What does a zero KL divergence mean for valid finite distributions? — KL bằng 0 nghĩa là gì với các phân phối hữu hạn hợp lệ?**

A. Cross-entropy loss for that sample — Cross-entropy của mẫu đó

B. Nonnegative — Không âm

C. No, KL is asymmetric — Không, KL bất đối xứng

D. The distributions are identical — Hai phân phối giống nhau

**Q13. What is the unit of MSE when predictions are in meters? — Dự báo theo mét thì MSE có đơn vị gì?**

A. Square meters — Mét bình phương

B. Meters — Mét

C. MSE — MSE

D. Huber loss — Huber loss

**Q14. What is the unit of MAE when predictions are in meters? — Dự báo theo mét thì MAE có đơn vị gì?**

A. Square meters — Mét bình phương

B. Meters — Mét

C. MSE — MSE

D. Huber loss — Huber loss

**Q15. Which loss increases quadratically with error magnitude? — Loss nào tăng theo bình phương độ lớn lỗi?**

A. Square meters — Mét bình phương

B. Meters — Mét

C. MSE — MSE

D. Huber loss — Huber loss

**Q16. Which regression loss has a threshold between quadratic and linear penalties? — Loss hồi quy nào có ngưỡng chuyển bình phương sang tuyến tính?**

A. Square meters — Mét bình phương

B. Meters — Mét

C. MSE — MSE

D. Huber loss — Huber loss

**Q17. Why clip predicted probabilities before a naive log implementation? — Vì sao clip xác suất trước khi lấy log bằng công thức đơn giản?**

A. To avoid log(0) and numerical infinities — Để tránh log(0) và vô cực số học

B. MAE — MAE

C. No, evaluate on held-out data — Không, cần đánh giá trên dữ liệu độc lập

D. Predicted probability assigned to the true class — Xác suất dự báo dành cho lớp đúng

**Q18. Which loss is easier to interpret in the original output units? — Loss nào dễ đọc theo đơn vị đầu ra ban đầu?**

A. To avoid log(0) and numerical infinities — Để tránh log(0) và vô cực số học

B. MAE — MAE

C. No, evaluate on held-out data — Không, cần đánh giá trên dữ liệu độc lập

D. Predicted probability assigned to the true class — Xác suất dự báo dành cho lớp đúng

**Q19. Does a lower training loss guarantee better unseen-data performance? — Training loss thấp có bảo đảm dự đoán tốt trên dữ liệu mới?**

A. To avoid log(0) and numerical infinities — Để tránh log(0) và vô cực số học

B. MAE — MAE

C. No, evaluate on held-out data — Không, cần đánh giá trên dữ liệu độc lập

D. Predicted probability assigned to the true class — Xác suất dự báo dành cho lớp đúng

**Q20. For one-hot labels, what information matters in cross-entropy? — Với nhãn one-hot, điều gì quyết định cross-entropy?**

A. To avoid log(0) and numerical infinities — Để tránh log(0) và vô cực số học

B. MAE — MAE

C. No, evaluate on held-out data — Không, cần đánh giá trên dữ liệu độc lập

D. Predicted probability assigned to the true class — Xác suất dự báo dành cho lớp đúng

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | MSE averages squared deviations. | MSE lấy trung bình bình phương sai lệch. |
| Q2 | **B** | MAE averages absolute deviations. | MAE lấy trung bình độ lệch tuyệt đối. |
| Q3 | **C** | Huber changes penalty growth past a threshold. | Huber đổi tốc độ tăng mức phạt sau một ngưỡng. |
| Q4 | **D** | KL uses a directed log-ratio between distributions. | KL dùng tỷ số logarit theo một chiều giữa các phân phối. |
| Q5 | **A** | The true class should receive high probability. | Lớp đúng cần được gán xác suất cao. |
| Q6 | **B** | Square each residual before averaging. | Bình phương từng sai lệch trước khi trung bình. |
| Q7 | **C** | Take absolute values of residuals before averaging. | Lấy trị tuyệt đối từng sai lệch rồi trung bình. |
| Q8 | **D** | Delta separates the two Huber regions. | Delta phân chia hai miền của Huber. |
| Q9 | **A** | With one-hot labels, only the true-class log term remains. | Với one-hot, chỉ còn hạng log của lớp đúng. |
| Q10 | **B** | KL is nonnegative by Gibbs' inequality. | KL không âm theo bất đẳng thức Gibbs. |
| Q11 | **C** | D(P‖Q) and D(Q‖P) can differ. | D(P‖Q) và D(Q‖P) có thể khác. |
| Q12 | **D** | KL is zero only when distributions agree appropriately. | KL bằng 0 khi các phân phối trùng nhau trong điều kiện phù hợp. |
| Q13 | **A** | Squaring a meter-valued residual yields m². | Bình phương sai lệch mét cho đơn vị m². |
| Q14 | **B** | Absolute errors keep the original unit. | Sai lệch tuyệt đối giữ đơn vị gốc. |
| Q15 | **C** | MSE squares error magnitudes. | MSE bình phương độ lớn lỗi. |
| Q16 | **D** | Huber transitions at delta. | Huber chuyển miền tại delta. |
| Q17 | **A** | Zero probabilities cause log singularities in naive formulas. | Xác suất 0 gây kỳ dị log trong công thức số học đơn giản. |
| Q18 | **B** | MAE reports average error in the same measurement unit. | MAE báo sai số trung bình cùng đơn vị đo. |
| Q19 | **C** | Generalization requires held-out validation. | Khả năng tổng quát cần kiểm chứng bằng dữ liệu độc lập. |
| Q20 | **D** | The negative log-likelihood uses the true-class score. | Âm log-likelihood dùng xác suất lớp đúng. |

## 8. Bài tiếp theo

`Dự đoán → Sai số → Loss → Tối ưu hóa`.
