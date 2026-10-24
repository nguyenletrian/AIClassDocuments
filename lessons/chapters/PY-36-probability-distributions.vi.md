# PY-36 — Phân phối nhị thức và phân phối chuẩn


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Random variable** — biến ngẫu nhiên; **Binomial** — phân phối nhị thức.

`Xác suất → Biến ngẫu nhiên → Phân phối → Thống kê`

Bài này kết nối dữ liệu thực nghiệm với cách tính xác suất, thống kê và các bước học máy.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Khái niệm |
|---|---|---|
| Random variable | biến ngẫu nhiên | Đại lượng có kết quả tùy phép thử |
| Binomial | phân phối nhị thức | Số thành công của n thử Bernoulli độc lập |
| Normal | phân phối chuẩn | Phân phối liên tục hình chuông với mean/std |
| PMF/PDF | hàm khối/mật độ | PMF cho biến rời rạc, PDF là mật độ cho biến liên tục |

## 3. Các hàm Python cần nhớ

| Hàm | Ý nghĩa |
|---|---|
| `binom.pmf(k, n, p)` | Xác suất **đúng** k thành công |
| `binom.cdf(k, n, p)` | Xác suất **không quá** k thành công |
| `norm.pdf(x, loc, scale)` | Mật độ chuẩn tại x, không phải xác suất tại điểm |
| `norm.cdf(x, loc, scale)` | Xác suất X ≤ x |
| `rng.normal(loc, scale, size)` | Lấy số mẫu giả ngẫu nhiên theo phân phối chuẩn |

## 4. Khái niệm chính và liên quan

**Mạch kiến thức:** Phép thử tạo kết quả; biến ngẫu nhiên biến kết quả thành số; phân phối cho khả năng từng giá trị. Nhị thức dành cho số lần thành công rời rạc, chuẩn cho biến liên tục; PMF, PDF và CDF trả lời những câu hỏi xác suất khác nhau.

### 4.1. Random variable — Chuyển kết quả thử thành con số

**Từ vựng:** **Random variable** — biến ngẫu nhiên; **Outcome** — kết quả thử.

Biến ngẫu nhiên X gán một giá trị số cho mỗi kết quả của phép thử. Ví dụ trong ba lần giao hàng, X là **số đơn đúng giờ** nên X có thể bằng 0, 1, 2 hoặc 3, không phải tên từng đơn. Một phép thử cụ thể chỉ tạo một giá trị X; **phân phối xác suất** mô tả khả năng của toàn bộ các giá trị đó. Mô phỏng sử dụng `seed` chỉ để có thể lặp lại kết quả.

```python
import numpy as np

rng = np.random.default_rng(42)
print(rng.binomial(n=3, p=0.8, size=5).tolist())
```

**Kết quả khi chạy:**

```text
[2, 3, 2, 2, 3]
```

Mỗi phần tử là số đơn đúng giờ trong một nhóm ba đơn; đây là năm lần thử giả lập.

### 4.2. Binomial — Đếm thành công từ các lần thử độc lập

**Từ vựng:** **Binomial** — nhị thức; **Bernoulli** — phép thử thành công/thất bại.

Phân phối nhị thức tính số lần **thành công trong n phép thử độc lập**, mỗi lần có cùng xác suất thành công p. Với 10 đơn hàng, xác suất giao đúng giờ từng đơn bằng 0,8, biến X đếm số đơn đúng giờ. `binom.pmf(8,10,0.8)` tính **đúng 8 đơn** đúng giờ; `binom.cdf(8,10,0.8)` lại tính **tối đa 8 đơn**. Không dùng nhị thức khi xác suất từng lần khác nhau hoặc các lần phụ thuộc mạnh mà không điều chỉnh mô hình.

```python
from scipy.stats import binom

print(round(float(binom.pmf(8, 10, 0.8)), 4))
```

**Kết quả khi chạy:**

```text
0.302
```

Xác suất đúng 8 trong 10 đơn đúng giờ khoảng 30,2% theo mô hình độc lập.

### 4.3. Normal — Phân phối liên tục quanh trung bình

**Từ vựng:** **Normal** — chuẩn; **Mean/standard deviation** — trung bình/độ lệch chuẩn.

Phân phối chuẩn có dạng chuông đối xứng quanh trung bình μ, với độ phân tán đo bằng σ (độ lệch chuẩn, σ>0). Ví dụ điểm cảm biến được **giả định** chuẩn với μ=100 và σ=15 (cùng đơn vị đo). Ngưỡng 115 cao hơn trung bình đúng một σ. `norm.cdf(115,loc=100,scale=15)` tính khả năng X **không vượt quá 115**, xấp xỉ 0,8413. Không nhầm giá trị CDF với mật độ tại điểm.

```python
from scipy.stats import norm

print(round(float(norm.cdf(115, loc=100, scale=15)), 4))
```

**Kết quả khi chạy:**

```text
0.8413
```

Khoảng 84,13% giá trị nằm từ phía âm vô hạn tới ngưỡng 115 theo giả định chuẩn.

### 4.4. PMF, PDF và CDF — Ba câu hỏi khác nhau

**Từ vựng:** **PMF** — khối xác suất; **PDF** — mật độ xác suất; **CDF** — xác suất tích lũy.

**PMF** cho biến rời rạc trả xác suất **bằng đúng** một giá trị, chẳng hạn P(X=1) khi X là số lần thành công. **PDF** cho biến liên tục trả *mật độ* tại x, **không phải P(X=x)** (với phân phối chuẩn, xác suất tại đúng một điểm là 0). **CDF** ở cả hai loại biến biểu diễn P(X≤x). Để tính xác suất trong một khoảng liên tục `(a,b]`, ta trừ CDF(b)−CDF(a).

```python
from scipy.stats import norm

probability = norm.cdf(1) - norm.cdf(-1)
print(round(float(probability), 4))
```

**Kết quả khi chạy:**

```text
0.6827
```

Theo chuẩn tắc N(0,1), khoảng −1 đến +1 chứa khoảng 68,27% xác suất.

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Đếm đúng tám đơn hàng giao đúng giờ

**Tình huống thực tế:** Một kho vận giả định mỗi đơn có xác suất 0,8 giao đúng giờ, độc lập với các đơn khác. Trong một nhóm 10 đơn, cần biết xác suất **chính xác tám đơn** đạt yêu cầu.

**Vì sao chọn cách giải này?** PMF nhị thức tính xác suất đúng k lần thành công trên n phép thử độc lập cùng xác suất p.

**Quy trình giải:**

1. Xác định thành công là đơn đúng giờ, n=10, p=0.8 và k=8.
2. Dùng `binom.pmf(k,n,p)`.
3. In xác suất và ghi rõ đây là đúng 8, không phải tối đa 8.

```python
from scipy.stats import binom

print(round(float(binom.pmf(8, 10, 0.8)), 4))
```

**Kết quả khi chạy:**

```text
0.302
```

Xác suất đúng tám đơn đúng giờ là khoảng 0,302 theo các giả định.

### Tình huống 2 — Xác suất có không quá ba lỗi

**Tình huống thực tế:** Nhà máy xét 10 linh kiện độc lập, xác suất lỗi mỗi chiếc 0,1. Bộ phận kiểm định muốn xác suất có từ 0 đến 3 chiếc lỗi, **bao gồm cả 3**.

**Vì sao chọn cách giải này?** CDF nhị thức cộng các xác suất P(X=0), P(X=1), P(X=2), P(X=3).

**Quy trình giải:**

1. Đặt X là số linh kiện lỗi, n=10 và p=0.1.
2. Tính `binom.cdf(3,10,0.1)`.
3. Làm tròn bốn chữ số và in kết quả.

```python
from scipy.stats import binom

print(round(float(binom.cdf(3, 10, 0.1)), 4))
```

**Kết quả khi chạy:**

```text
0.9872
```

Theo mô hình, xác suất có tối đa ba linh kiện lỗi khoảng 98,72%.

### Tình huống 3 — Tỷ lệ đo cảm biến dưới ngưỡng

**Tình huống thực tế:** Một cảm biến có phép đo được giả định chuẩn với trung bình 100, độ lệch chuẩn 15 đơn vị đo. Ngưỡng theo dõi là 115; cần tính tỷ lệ phép đo không vượt ngưỡng.

**Vì sao chọn cách giải này?** CDF chuẩn cộng xác suất của mọi giá trị từ dưới ngưỡng đến ngưỡng.

**Quy trình giải:**

1. Gán μ=100, σ=15 và ngưỡng 115 cùng đơn vị.
2. Gọi `norm.cdf` với `loc=100`, `scale=15`.
3. In xác suất đến bốn chữ số thập phân.

```python
from scipy.stats import norm

print(round(float(norm.cdf(115, loc=100, scale=15)), 4))
```

**Kết quả khi chạy:**

```text
0.8413
```

Khoảng 84,13% phép đo không vượt 115 nếu giả định phân phối chuẩn phù hợp.

### Tình huống 4 — Phân biệt mật độ tại điểm và xác suất

**Tình huống thực tế:** Mô hình độ lệch chuẩn tắc X~N(0,1). Nhà phân tích cần xem **mật độ** ở x=0, không phải tỷ lệ quan sát bằng chính xác 0.

**Vì sao chọn cách giải này?** PDF chuẩn cho chiều cao đường cong tại điểm; xác suất của điểm đơn lẻ trong biến liên tục bằng 0.

**Quy trình giải:**

1. Chọn phân phối chuẩn tắc μ=0, σ=1.
2. Tính `norm.pdf(0)`.
3. In mật độ và tránh diễn giải như tỷ lệ sự kiện X=0.

```python
from scipy.stats import norm

print(round(float(norm.pdf(0)), 4))
```

**Kết quả khi chạy:**

```text
0.3989
```

0,3989 là mật độ tại 0, **không phải 39,89% xác suất có giá trị đúng bằng 0**.

### Tình huống 5 — Tạo năm mẫu cảm biến chuẩn để thử code

**Tình huống thực tế:** Lập trình viên muốn năm số thử để kiểm tra luồng dữ liệu cảm biến giả lập N(0,1), có thể tạo lại khi học viên chạy đúng môi trường.

**Vì sao chọn cách giải này?** Bộ sinh NumPy với seed giúp kiểm tra cùng chuỗi dữ liệu trong phiên bản tương thích.

**Quy trình giải:**

1. Tạo `default_rng(42)`.
2. Sinh năm mẫu chuẩn trung bình 0, độ lệch chuẩn 1.
3. Làm tròn ba chữ số và chuyển List để in ổn định.

```python
import numpy as np

rng = np.random.default_rng(42)
samples = rng.normal(loc=0, scale=1, size=5)
print(np.round(samples, 3).tolist())
```

**Kết quả khi chạy:**

```text
[0.305, -1.04, 0.75, 0.941, -1.951]
```

Đây là năm giá trị giả lập, không phải minh chứng rằng dữ liệu cảm biến thực tế tuân phân phối chuẩn.

## 6. Sai lầm thường gặp

- PMF tính xác suất đúng một giá trị **rời rạc**; PDF là mật độ cho biến liên tục, không phải P(X=x).
- CDF là P(X≤x), khác PMF tại k và PDF tại x.
- Mô hình nhị thức cần n lần thử độc lập với p giống nhau; thay điều kiện có thể làm kết quả sai.
- `scale` là độ lệch chuẩn dương, không phải phương sai.
- Seed cố định cho mô phỏng có thể tái lập trong môi trường tương thích; không bảo đảm thống kê mẫu bằng lý thuyết.
- Xác suất dưới mô hình không chứng minh quy trình thực tế đúng giả định.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Q1. What is a random variable? — Biến ngẫu nhiên là gì?**

A. A numerical quantity assigned to random outcomes — Đại lượng số gắn với kết quả ngẫu nhiên

B. Successes in independent same-p trials — Số thành công trong các lần thử độc lập cùng p

C. A continuous symmetric bell-shaped density — Mật độ liên tục dạng chuông đối xứng

D. Probability mass at a discrete value — Xác suất ở một giá trị rời rạc

**Q2. What does binomial X count? — Biến nhị thức X đếm gì?**

A. A numerical quantity assigned to random outcomes — Đại lượng số gắn với kết quả ngẫu nhiên

B. Successes in independent same-p trials — Số thành công trong các lần thử độc lập cùng p

C. A continuous symmetric bell-shaped density — Mật độ liên tục dạng chuông đối xứng

D. Probability mass at a discrete value — Xác suất ở một giá trị rời rạc

**Q3. What characterizes a normal distribution? — Phân phối chuẩn có đặc điểm gì?**

A. A numerical quantity assigned to random outcomes — Đại lượng số gắn với kết quả ngẫu nhiên

B. Successes in independent same-p trials — Số thành công trong các lần thử độc lập cùng p

C. A continuous symmetric bell-shaped density — Mật độ liên tục dạng chuông đối xứng

D. Probability mass at a discrete value — Xác suất ở một giá trị rời rạc

**Q4. What is a PMF? — PMF là gì?**

A. A numerical quantity assigned to random outcomes — Đại lượng số gắn với kết quả ngẫu nhiên

B. Successes in independent same-p trials — Số thành công trong các lần thử độc lập cùng p

C. A continuous symmetric bell-shaped density — Mật độ liên tục dạng chuông đối xứng

D. Probability mass at a discrete value — Xác suất ở một giá trị rời rạc

**Q5. What is a PDF? — PDF là gì?**

A. Density, not point probability, for continuous data — Mật độ, không phải xác suất tại điểm liên tục

B. Probability that X is at most x — Xác suất X nhỏ hơn hoặc bằng x

C. Probability of exactly k successes — Xác suất đúng k lần thành công

D. Probability of k or fewer successes — Xác suất tối đa k lần thành công

**Q6. What is a CDF? — CDF là gì?**

A. Density, not point probability, for continuous data — Mật độ, không phải xác suất tại điểm liên tục

B. Probability that X is at most x — Xác suất X nhỏ hơn hoặc bằng x

C. Probability of exactly k successes — Xác suất đúng k lần thành công

D. Probability of k or fewer successes — Xác suất tối đa k lần thành công

**Q7. What does binom.pmf(k,n,p) compute? — binom.pmf(k,n,p) tính gì?**

A. Density, not point probability, for continuous data — Mật độ, không phải xác suất tại điểm liên tục

B. Probability that X is at most x — Xác suất X nhỏ hơn hoặc bằng x

C. Probability of exactly k successes — Xác suất đúng k lần thành công

D. Probability of k or fewer successes — Xác suất tối đa k lần thành công

**Q8. What does binom.cdf(k,n,p) compute? — binom.cdf(k,n,p) tính gì?**

A. Density, not point probability, for continuous data — Mật độ, không phải xác suất tại điểm liên tục

B. Probability that X is at most x — Xác suất X nhỏ hơn hoặc bằng x

C. Probability of exactly k successes — Xác suất đúng k lần thành công

D. Probability of k or fewer successes — Xác suất tối đa k lần thành công

**Q9. What condition is essential for a simple binomial model? — Điều kiện quan trọng của nhị thức đơn giản là gì?**

A. Independent trials with constant success probability — Các lần thử độc lập cùng xác suất thành công

B. Center and spread — Trung tâm và độ phân tán

C. Zero — Bằng 0

D. Strictly positive standard deviation — Độ lệch chuẩn phải lớn hơn 0

**Q10. What do mean and standard deviation determine for normal? — Mean và std xác định gì trong chuẩn?**

A. Independent trials with constant success probability — Các lần thử độc lập cùng xác suất thành công

B. Center and spread — Trung tâm và độ phân tán

C. Zero — Bằng 0

D. Strictly positive standard deviation — Độ lệch chuẩn phải lớn hơn 0

**Q11. What is P(X=x) for a continuous normal variable? — P(X=x) với biến chuẩn liên tục bằng bao nhiêu?**

A. Independent trials with constant success probability — Các lần thử độc lập cùng xác suất thành công

B. Center and spread — Trung tâm và độ phân tán

C. Zero — Bằng 0

D. Strictly positive standard deviation — Độ lệch chuẩn phải lớn hơn 0

**Q12. Which quantity must be positive for norm.pdf scale? — scale của norm.pdf cần điều kiện nào?**

A. Independent trials with constant success probability — Các lần thử độc lập cùng xác suất thành công

B. Center and spread — Trung tâm và độ phân tán

C. Zero — Bằng 0

D. Strictly positive standard deviation — Độ lệch chuẩn phải lớn hơn 0

**Q13. What does norm.cdf(0) equal for N(0,1)? — norm.cdf(0) với N(0,1) bằng gì?**

A. 0.5 — 0.5

B. CDF(b) minus CDF(a) — CDF(b) trừ CDF(a)

C. No, sampling noise remains — Không, vẫn có dao động lấy mẫu

D. From 0 to 1 inclusive — Từ 0 đến 1 gồm hai đầu

**Q14. How do you calculate normal P(a<X≤b)? — Tính P(a<X≤b) cho chuẩn bằng gì?**

A. 0.5 — 0.5

B. CDF(b) minus CDF(a) — CDF(b) trừ CDF(a)

C. No, sampling noise remains — Không, vẫn có dao động lấy mẫu

D. From 0 to 1 inclusive — Từ 0 đến 1 gồm hai đầu

**Q15. Does fixed RNG seed force sample mean to equal μ? — Seed cố định có buộc mean mẫu bằng μ?**

A. 0.5 — 0.5

B. CDF(b) minus CDF(a) — CDF(b) trừ CDF(a)

C. No, sampling noise remains — Không, vẫn có dao động lấy mẫu

D. From 0 to 1 inclusive — Từ 0 đến 1 gồm hai đầu

**Q16. What is the range of probabilities? — Xác suất nằm trong đoạn nào?**

A. 0.5 — 0.5

B. CDF(b) minus CDF(a) — CDF(b) trừ CDF(a)

C. No, sampling noise remains — Không, vẫn có dao động lấy mẫu

D. From 0 to 1 inclusive — Từ 0 đến 1 gồm hai đầu

**Q17. Can a continuous PDF exceed 1 at a point? — PDF liên tục có thể lớn hơn 1 tại một điểm không?**

A. Yes; only its total integral must be one — Có; chỉ tích phân toàn miền phải bằng một

B. The distribution becomes wider — Phân phối trải rộng hơn

C. Point probabilities behave differently — Xác suất tại một điểm có ý nghĩa khác nhau

D. Cumulative probability up to x — Xác suất tích lũy tới x

**Q18. What happens when standard deviation of normal increases? — Std phân phối chuẩn tăng sẽ thế nào?**

A. Yes; only its total integral must be one — Có; chỉ tích phân toàn miền phải bằng một

B. The distribution becomes wider — Phân phối trải rộng hơn

C. Point probabilities behave differently — Xác suất tại một điểm có ý nghĩa khác nhau

D. Cumulative probability up to x — Xác suất tích lũy tới x

**Q19. Why distinguish discrete and continuous variables? — Vì sao phân biệt biến rời rạc và liên tục?**

A. Yes; only its total integral must be one — Có; chỉ tích phân toàn miền phải bằng một

B. The distribution becomes wider — Phân phối trải rộng hơn

C. Point probabilities behave differently — Xác suất tại một điểm có ý nghĩa khác nhau

D. Cumulative probability up to x — Xác suất tích lũy tới x

**Q20. What does norm.cdf(x,loc,scale) return? — norm.cdf(x,loc,scale) trả gì?**

A. Yes; only its total integral must be one — Có; chỉ tích phân toàn miền phải bằng một

B. The distribution becomes wider — Phân phối trải rộng hơn

C. Point probabilities behave differently — Xác suất tại một điểm có ý nghĩa khác nhau

D. Cumulative probability up to x — Xác suất tích lũy tới x

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | It maps outcomes to numbers. A random variable is not the outcome itself: it assigns a number, such as a count of on-time deliveries, to each possible outcome. | Nó biến kết quả phép thử thành số. Biến ngẫu nhiên không phải toàn bộ kết quả thử; nó gán một con số, chẳng hạn số đơn đúng giờ, cho mỗi kết quả có thể. |
| Q2 | **B** | Each trial has success or failure. The binomial X ranges from zero to n; it does not count how many different outcomes a single trial has. | Mỗi lần thử có hai kết quả thành công hoặc thất bại. Biến nhị thức X nhận từ 0 đến n; nó đếm số lần đạt, không đếm số loại kết quả của một phép thử. |
| Q3 | **C** | It is specified by mean and standard deviation. Its two parameters have different units: the mean locates the bell and the positive standard deviation controls spread. | Được xác định bởi trung bình và độ lệch chuẩn. Hai tham số có ý nghĩa khác nhau: mean xác định tâm và độ lệch chuẩn dương quyết định độ phân tán. |
| Q4 | **D** | PMF returns probability for a discrete outcome. For binomial X, PMF at k answers exactly k successes, while CDF at k also includes all counts below k. | PMF tính xác suất đúng một kết quả rời rạc. Với X nhị thức, PMF tại k trả đúng k lần thành công; CDF tại k tính cả mọi số lần ít hơn k. |
| Q5 | **A** | Continuous intervals require integrating density. For example, a PDF value of 0.4 is not a 40% chance of observing exactly that real number. | Xác suất khoảng liên tục tính từ diện tích dưới mật độ. Chẳng hạn giá trị PDF bằng 0,4 không nghĩa là có 40% xác suất nhận đúng số thực ấy. |
| Q6 | **B** | CDF includes all outcomes at or below the threshold. The CDF combines all earlier outcomes; for a continuous variable interval probabilities use differences of CDFs. | CDF cộng xác suất đến ngưỡng đã cho. CDF cộng xác suất tới ngưỡng; với biến liên tục, xác suất một khoảng được tính bằng hiệu hai CDF. |
| Q7 | **C** | PMF is an exact-count probability. The argument n is the number of trials and p the probability per trial; pmf returns a single count's probability. | PMF cho xác suất đúng số lần thành công. Đối số n là số lần thử, p là xác suất mỗi lần; pmf trả xác suất của đúng một số lần thành công. |
| Q8 | **D** | CDF sums counts from zero through k. For example P(X≤2) adds P(X=0), P(X=1), and P(X=2), not only P(X=2). | CDF cộng từ 0 tới k. Ví dụ P(X≤2) cộng P(X=0), P(X=1), P(X=2), chứ không chỉ P(X=2). |
| Q9 | **A** | Dependencies invalidate the simple assumptions. If delivery outcomes share the same disruption or their success probabilities differ, a simple binomial may be unsuitable. | Phụ thuộc giữa lần thử làm sai giả định mô hình. Nếu đơn giao cùng chịu một sự cố hoặc xác suất đúng giờ khác nhau, mô hình nhị thức đơn giản có thể không phù hợp. |
| Q10 | **B** | Mean locates the bell and std sets its width. Changing the standard deviation spreads or compresses the bell without requiring a change in its center. | Trung bình định vị và độ lệch chuẩn xác định độ rộng. Đổi độ lệch chuẩn làm chuông rộng/hẹp nhưng không nhất thiết thay tâm của phân phối. |
| Q11 | **C** | A single point has zero probability mass. Probability for an interval comes from area under the PDF; an isolated point has zero area. | Một điểm đơn có xác suất bằng 0. Xác suất trong khoảng là diện tích dưới PDF; một điểm riêng lẻ không có diện tích. |
| Q12 | **D** | A nonpositive scale is not a valid normal std. For SciPy, `scale` denotes sigma rather than sigma squared; passing variance by mistake changes the whole curve. | Độ lệch chuẩn không dương không hợp lệ. Trong SciPy, `scale` là sigma chứ không phải sigma bình phương; truyền phương sai sẽ làm sai toàn bộ phân phối. |
| Q13 | **A** | The standard normal is symmetric around zero. Half the mass lies on each side of mean zero in a symmetric standard normal. | Chuẩn tắc đối xứng quanh 0. Chuẩn tắc đối xứng quanh trung bình 0 nên mỗi phía chứa một nửa xác suất. |
| Q14 | **B** | Cumulative differences give interval probability. For example, P(−1<X≤1) is `norm.cdf(1)-norm.cdf(-1)`, about 0.6827. | Hiệu xác suất tích lũy cho xác suất đoạn. Ví dụ P(−1<X≤1) bằng `norm.cdf(1)-norm.cdf(-1)`, xấp xỉ 0,6827. |
| Q15 | **C** | A seed reproduces samples, not exact theoretical moments. A seeded simulation can be reproducible while its average still differs from the theoretical expected value. | Seed lặp được mẫu, không đảm bảo đúng moment lý thuyết. Mô phỏng cố định seed có thể lặp lại nhưng trung bình mẫu vẫn lệch so với kỳ vọng lý thuyết. |
| Q16 | **D** | Probabilities cannot be negative or exceed one. The endpoints 0 and 1 correspond to impossible and certain events, respectively. | Xác suất không âm và không vượt một. Hai đầu 0 và 1 tương ứng biến cố không thể và chắc chắn. |
| Q17 | **A** | Density height need not itself be a probability. A narrow normal curve can have a PDF peak above one while its integrated area still equals one. | Chiều cao mật độ không phải xác suất. Đường chuẩn có độ lệch chuẩn nhỏ có thể có đỉnh PDF cao hơn 1 nhưng tổng diện tích vẫn bằng 1. |
| Q18 | **B** | The same total area spreads over a wider range. A larger sigma does not automatically move the mean; it spreads values farther from the same center. | Cùng tổng diện tích được trải ra trên miền rộng hơn. Sigma lớn hơn không tự làm dịch mean; nó khiến số đo phân tán xa hơn quanh cùng tâm. |
| Q19 | **C** | PMF probabilities differ from PDF densities. A count like X=3 can have positive point probability, unlike the exact equality of a continuous measurement. | PMF là xác suất còn PDF là mật độ. Số đếm như X=3 có xác suất tại điểm dương, còn biến đo liên tục có xác suất bằng đúng một giá trị là 0. |
| Q20 | **D** | It is P(X≤x) under a normal model. Do not use the PDF's height when the question asks P(X≤x); `cdf` is the appropriate cumulative tool. | Nó là P(X≤x) theo phân phối chuẩn. Không lấy chiều cao PDF nếu câu hỏi là P(X≤x); cần dùng `cdf` để tính xác suất tích lũy. |

## 8. Liên hệ bài tiếp theo

`Xác suất → Biến ngẫu nhiên → Phân phối → Thống kê`.
