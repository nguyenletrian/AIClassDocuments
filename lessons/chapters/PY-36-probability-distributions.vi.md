# PY-36 — Phân phối nhị thức và phân phối chuẩn


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Random variable** — biến ngẫu nhiên; **Binomial** — phân phối nhị thức.

`Xác suất → Biến ngẫu nhiên → Phân phối → Thống kê`

**Học xong dùng để làm gì?** Mô tả xác suất của các mức số đếm hay kết quả đo và xem độ tập trung/phân tán của biến ngẫu nhiên.

**Kết nối kiến thức tiếp theo:** PY-37 tính trung bình và độ lệch chuẩn trực tiếp từ dữ liệu quan sát.

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
# Mục đích: Chuyển kết quả thử thành con số.
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
# Mục đích: Đếm thành công từ các lần thử độc lập.
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
# Mục đích: Phân phối liên tục quanh trung bình.
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
# Mục đích: Ba câu hỏi khác nhau.
from scipy.stats import norm

probability = norm.cdf(1) - norm.cdf(-1)
print(round(float(probability), 4))
```

**Kết quả khi chạy:**

```text
0.6827
```

Theo chuẩn tắc N(0,1), khoảng −1 đến +1 chứa khoảng 68,27% xác suất.

## 5. Năm tình huống phân phối — từ PMF nhị thức đến mô phỏng nhiều lô

### Tình huống 1 — Cấp 1: So 10 đơn đúng hạn với phân phối nhị thức

**Từ vựng trong mục:** **Bernoulli** — phép thử hai kết quả; **Binomial PMF** — xác suất đúng k thành công.

**Tình huống thực tế:** Một đơn vị giao nhận theo dõi **10 đơn hàng**; mỗi bản ghi 1 nếu đúng giờ và 0 nếu trễ. Chính sách dự báo giả định **mỗi đơn độc lập, xác suất đúng hạn bằng 0,8**, giống nhau giữa các đơn. Cần đếm số đơn đúng giờ trong bảng rồi tính khả năng nhận **đúng số đơn ấy** theo mô hình nhị thức.

**Vì sao chọn cách này?** Nhị thức phù hợp khi có số lần thử cố định, hai kết quả và cùng xác suất; `binom.pmf` hỏi **đúng k**, khác tỷ lệ thực nghiệm `k/10`. Một ngày có tỷ lệ 80% không chứng minh giả định độc lập.

**Quy trình:**
1. Đếm mười cờ thực tế và xác định số thành công k.
2. Tính xác suất nhị thức cho đúng k trong mười đơn.
3. In số đơn và xác suất để tránh nhầm PMF với phần trăm quan sát.

```python
from scipy.stats import binom
observed = [1,1,0,1,1,1,0,1,1,1]
count = sum(observed)
prob = binom.pmf(count, n=10, p=0.8)
assert len(observed) == 10
print("Đơn:", len(observed))
print("Đúng hạn:", count)
print(f"P(đúng số này): {prob:.4f}")
```

**Kết quả khi chạy:**

```text
Đơn: 10
Đúng hạn: 8
P(đúng số này): 0.3020
```

Xác suất 0,3020 là kết quả của **mô hình đã giả định**, không phải xác suất một đơn bất kỳ được giao đúng hạn.

### Tình huống 2 — Cấp 2: Tính xác suất không quá hai lỗi trong 12 linh kiện

**Từ vựng trong mục:** **Binomial CDF** — xác suất tích lũy; **Threshold** — ngưỡng.

**Tình huống thực tế:** Trạm lắp ráp ghi **12 linh kiện**, mỗi linh kiện có cờ lỗi 1/0; ba chiếc đang được đánh dấu lỗi. Giả sử ở một lô tương tự mỗi linh kiện lỗi độc lập với xác suất 0,1. Quản đốc muốn biết khả năng có **tối đa hai linh kiện lỗi trong một lô 12 chiếc**, đồng thời so số lỗi của lô đang quan sát.

**Vì sao chọn cách này?** `binom.cdf(2,12,0.1)` cộng xác suất từ 0 đến 2 lỗi, không phải xác suất **đúng hai lỗi**; kết quả dự báo theo mô hình khác việc đếm ba lỗi đã xảy ra.

**Quy trình:**
1. Lưu 12 cờ lỗi và đếm lỗi quan sát.
2. Dùng `binom.cdf` cho biến cố số lỗi không vượt 2.
3. Phân biệt số lỗi thật với xác suất mô hình.

```python
from scipy.stats import binom
faults = [1,0,0,0,1,0,0,0,1,0,0,0]
probability = binom.cdf(2, n=len(faults), p=0.1)
assert len(faults) == 12
print("Linh kiện:", len(faults))
print("Lỗi quan sát:", sum(faults))
print(f"P(không quá 2 lỗi): {probability:.4f}")
```

**Kết quả khi chạy:**

```text
Linh kiện: 12
Lỗi quan sát: 3
P(không quá 2 lỗi): 0.8891
```

Một lô đã có ba lỗi không thay đổi cách tính xác suất của **lô tương lai dưới giả định**; muốn cập nhật xác suất lỗi p cần nhiều dữ liệu hơn.

### Tình huống 3 — Cấp 3: Tỷ lệ quan sát dưới ngưỡng so với phân phối chuẩn của 15 số đo

**Từ vựng trong mục:** **Normal CDF** — xác suất tích lũy chuẩn; **Empirical rate** — tần suất quan sát.

**Tình huống thực tế:** Trạm nhiệt có **15 phép đo** °C, mỗi hàng là một số đo đã quan sát. Kỹ sư giả định mô hình chuẩn có trung bình 100 °C và độ lệch chuẩn 10 °C; cần tính xác suất lý thuyết **không vượt 110 °C**, đồng thời xem tỷ lệ đo thực tế ≤110 °C trên 15 mẫu.

**Vì sao chọn cách này?** `norm.cdf` tính diện tích xác suất đến ngưỡng, còn số đo thực tế phải **đếm**. Hai đại lượng có mẫu số/nguồn khác nhau; không thể dùng `norm.pdf(110)` như xác suất dưới ngưỡng.

**Quy trình:**
1. Nhập 15 giá trị °C và đếm mẫu ≤110.
2. Tính CDF tại 110 với μ=100, σ=10.
3. Báo tỷ lệ đo và xác suất giả định cùng nhãn riêng.

```python
import numpy as np
from scipy.stats import norm
celsius = np.array([90,95,101,103,110,104,96,98,111,93,106,99,109,102,97], dtype=float)
empirical = np.mean(celsius <= 110)
theoretical = norm.cdf(110, loc=100, scale=10)
assert len(celsius) == 15
print("Lượt đo:", len(celsius))
print("Đo ≤110:", int((celsius <= 110).sum()))
print(f"Tỷ lệ đo: {empirical:.3f}")
print(f"CDF mô hình: {theoretical:.4f}")
```

**Kết quả khi chạy:**

```text
Lượt đo: 15
Đo ≤110: 14
Tỷ lệ đo: 0.933
CDF mô hình: 0.8413
```

Việc 14/15 phép đo đạt ngưỡng không chứng minh dữ liệu thực sự phân phối chuẩn; μ và σ ở đây là giả định minh họa.

### Tình huống 4 — Cấp 4: Phân biệt mật độ và xác suất khoảng trên 18 mức cảm biến

**Từ vựng trong mục:** **PDF** — mật độ; **CDF interval** — xác suất trong khoảng.

**Tình huống thực tế:** Bộ hiệu chuẩn ghi **18 mức tín hiệu** (đơn vị cảm biến), mỗi hàng một lượt; muốn đánh giá khoảng chấp nhận **90 đến 110** dưới mô hình chuẩn μ=100, σ=10. Cần đếm mẫu thực tế trong khoảng, tính xác suất theo CDF, và in riêng PDF tại 100 để nhắc rằng mật độ tại điểm **không phải** xác suất một điểm.

**Vì sao chọn cách này?** Biến chuẩn là liên tục, nên xác suất tại đúng một giá trị bằng 0; xác suất trong khoảng lấy bằng **hiệu hai CDF**, còn PDF chỉ là độ cao đường mật độ.

**Quy trình:**
1. Tạo 18 số đo có cùng đơn vị.
2. Đếm số đo trong khoảng 90–110 (kể cả hai biên).
3. Tính xác suất khoảng bằng CDF và mật độ tại 100 bằng PDF.

```python
import numpy as np
from scipy.stats import norm
values = np.array([84,88,90,92,94,95,97,98,99,100,101,102,103,105,108,110,113,117], dtype=float)
observed = int(((values >= 90) & (values <= 110)).sum())
interval = norm.cdf(110, 100, 10) - norm.cdf(90, 100, 10)
density = norm.pdf(100, 100, 10)
assert values.shape == (18,)
print("Lượt đo:", len(values))
print("Trong khoảng:", observed)
print(f"Xác suất mô hình: {interval:.4f}")
print(f"Mật độ tại 100: {density:.4f}")
```

**Kết quả khi chạy:**

```text
Lượt đo: 18
Trong khoảng: 14
Xác suất mô hình: 0.6827
Mật độ tại 100: 0.0399
```

PDF có đơn vị **nghịch đảo đơn vị cảm biến**, trong khi xác suất khoảng không mang đơn vị và nằm trong [0,1].

### Tình huống 5 — Cấp 5: Lặp 20 lô thử và đối chiếu phân phối số thành công

**Từ vựng trong mục:** **Sampling distribution** — phân phối kết quả thử; **PMF normalization** — tổng xác suất bằng một.

**Tình huống thực tế:** Đội vận hành mô phỏng **20 lô**, mỗi hàng là số đơn đúng giờ trong **10 đơn độc lập** của lô đó; giả định xác suất đúng giờ 0,7 cho mọi đơn. Cần đối chiếu số thành công trung bình từ 20 lô với kỳ vọng lý thuyết, kiểm tra **toàn bộ 11 giá trị** k=0…10 trong PMF tạo tổng xác suất 1. Trình bày mô phỏng có seed để tái lập.

**Vì sao chọn cách này?** `rng.binomial` tạo **20 quan sát về số lần thành công**, mỗi quan sát trong [0,10], còn `binom.pmf` mô tả phân phối của **một lô**. Tổng xác suất 11 giá trị phải bằng 1, không phải 20.

**Quy trình:**
1. Mô phỏng 20 lô có 10 lần thử/lô bằng seed cố định.
2. Tính số trung bình quan sát và kỳ vọng 10×0,7.
3. Liệt kê xác suất PMF từ 0 đến 10 rồi đối chiếu tổng.

```python
import numpy as np
from scipy.stats import binom
rng = np.random.default_rng(42)
counts = rng.binomial(n=10, p=0.7, size=20)
possible = np.arange(11)
probabilities = binom.pmf(possible, n=10, p=0.7)
assert counts.shape == (20,) and np.all((counts >= 0) & (counts <= 10))
print("Lô mô phỏng:", len(counts))
print("Đơn mỗi lô:", 10)
print("Kỳ vọng mỗi lô:", f"{10*0.7:.1f}")
print("PMF có 11 giá trị:", len(probabilities))
print("Tổng PMF bằng 1:", bool(np.isclose(probabilities.sum(), 1)))
```

**Kết quả khi chạy:**

```text
Lô mô phỏng: 20
Đơn mỗi lô: 10
Kỳ vọng mỗi lô: 7.0
PMF có 11 giá trị: 11
Tổng PMF bằng 1: True
```

20 là số **lô mô phỏng**, không phải n=20 trong từng phép thử nhị thức. Đối với các đơn phụ thuộc nhau, mô hình nhị thức này có thể không phù hợp.

## 6. Sai lầm thường gặp

- PMF tính xác suất đúng một giá trị **rời rạc**; PDF là mật độ cho biến liên tục, không phải P(X=x).
- CDF là P(X≤x), khác PMF tại k và PDF tại x.
- Mô hình nhị thức cần n lần thử độc lập với p giống nhau; thay điều kiện có thể làm kết quả sai.
- `scale` là độ lệch chuẩn dương, không phải phương sai.
- Seed cố định cho mô phỏng có thể tái lập trong môi trường tương thích; không bảo đảm thống kê mẫu bằng lý thuyết.
- Xác suất dưới mô hình không chứng minh quy trình thực tế đúng giả định.

## 7. Trắc nghiệm

**Q1. What is a random variable? | Biến ngẫu nhiên là gì?**

A. A numerical quantity assigned to random outcomes | Đại lượng số gắn với kết quả ngẫu nhiên

B. Successes in independent same-p trials | Số thành công trong các lần thử độc lập cùng p

C. A continuous symmetric bell-shaped density | Mật độ liên tục dạng chuông đối xứng

D. Probability mass at a discrete value | Xác suất ở một giá trị rời rạc

**Đáp án: A**

**Giải thích:** Nó biến kết quả phép thử thành số. Biến ngẫu nhiên không phải toàn bộ kết quả thử; nó gán một con số, chẳng hạn số đơn đúng giờ, cho mỗi kết quả có thể.


**Q2. What does binomial X count? | Biến nhị thức X đếm gì?**

A. A numerical quantity assigned to random outcomes | Đại lượng số gắn với kết quả ngẫu nhiên

B. Successes in independent same-p trials | Số thành công trong các lần thử độc lập cùng p

C. A continuous symmetric bell-shaped density | Mật độ liên tục dạng chuông đối xứng

D. Probability mass at a discrete value | Xác suất ở một giá trị rời rạc

**Đáp án: B**

**Giải thích:** Mỗi lần thử có hai kết quả thành công hoặc thất bại. Biến nhị thức X nhận từ 0 đến n; nó đếm số lần đạt, không đếm số loại kết quả của một phép thử.


**Q3. What characterizes a normal distribution? | Phân phối chuẩn có đặc điểm gì?**

A. A numerical quantity assigned to random outcomes | Đại lượng số gắn với kết quả ngẫu nhiên

B. Successes in independent same-p trials | Số thành công trong các lần thử độc lập cùng p

C. A continuous symmetric bell-shaped density | Mật độ liên tục dạng chuông đối xứng

D. Probability mass at a discrete value | Xác suất ở một giá trị rời rạc

**Đáp án: C**

**Giải thích:** Được xác định bởi trung bình và độ lệch chuẩn. Hai tham số có ý nghĩa khác nhau: mean xác định tâm và độ lệch chuẩn dương quyết định độ phân tán.


**Q4. What is a PMF? | PMF là gì?**

A. A numerical quantity assigned to random outcomes | Đại lượng số gắn với kết quả ngẫu nhiên

B. Successes in independent same-p trials | Số thành công trong các lần thử độc lập cùng p

C. A continuous symmetric bell-shaped density | Mật độ liên tục dạng chuông đối xứng

D. Probability mass at a discrete value | Xác suất ở một giá trị rời rạc

**Đáp án: D**

**Giải thích:** PMF tính xác suất đúng một kết quả rời rạc. Với X nhị thức, PMF tại k trả đúng k lần thành công; CDF tại k tính cả mọi số lần ít hơn k.


**Q5. What is a PDF? | PDF là gì?**

A. Density, not point probability, for continuous data | Mật độ, không phải xác suất tại điểm liên tục

B. Probability that X is at most x | Xác suất X nhỏ hơn hoặc bằng x

C. Probability of exactly k successes | Xác suất đúng k lần thành công

D. Probability of k or fewer successes | Xác suất tối đa k lần thành công

**Đáp án: A**

**Giải thích:** Xác suất khoảng liên tục tính từ diện tích dưới mật độ. Chẳng hạn giá trị PDF bằng 0,4 không nghĩa là có 40% xác suất nhận đúng số thực ấy.


**Q6. What is a CDF? | CDF là gì?**

A. Density, not point probability, for continuous data | Mật độ, không phải xác suất tại điểm liên tục

B. Probability that X is at most x | Xác suất X nhỏ hơn hoặc bằng x

C. Probability of exactly k successes | Xác suất đúng k lần thành công

D. Probability of k or fewer successes | Xác suất tối đa k lần thành công

**Đáp án: B**

**Giải thích:** CDF cộng xác suất đến ngưỡng đã cho. CDF cộng xác suất tới ngưỡng; với biến liên tục, xác suất một khoảng được tính bằng hiệu hai CDF.


**Q7. What does binom.pmf(k,n,p) compute? | binom.pmf(k,n,p) tính gì?**

A. Density, not point probability, for continuous data | Mật độ, không phải xác suất tại điểm liên tục

B. Probability that X is at most x | Xác suất X nhỏ hơn hoặc bằng x

C. Probability of exactly k successes | Xác suất đúng k lần thành công

D. Probability of k or fewer successes | Xác suất tối đa k lần thành công

**Đáp án: C**

**Giải thích:** PMF cho xác suất đúng số lần thành công. Đối số n là số lần thử, p là xác suất mỗi lần; pmf trả xác suất của đúng một số lần thành công.


**Q8. What does binom.cdf(k,n,p) compute? | binom.cdf(k,n,p) tính gì?**

A. Density, not point probability, for continuous data | Mật độ, không phải xác suất tại điểm liên tục

B. Probability that X is at most x | Xác suất X nhỏ hơn hoặc bằng x

C. Probability of exactly k successes | Xác suất đúng k lần thành công

D. Probability of k or fewer successes | Xác suất tối đa k lần thành công

**Đáp án: D**

**Giải thích:** CDF cộng từ 0 tới k. Ví dụ P(X≤2) cộng P(X=0), P(X=1), P(X=2), chứ không chỉ P(X=2).


**Q9. What condition is essential for a simple binomial model? | Điều kiện quan trọng của nhị thức đơn giản là gì?**

A. Independent trials with constant success probability | Các lần thử độc lập cùng xác suất thành công

B. Center and spread | Trung tâm và độ phân tán

C. Zero | Bằng 0

D. Strictly positive standard deviation | Độ lệch chuẩn phải lớn hơn 0

**Đáp án: A**

**Giải thích:** Phụ thuộc giữa lần thử làm sai giả định mô hình. Nếu đơn giao cùng chịu một sự cố hoặc xác suất đúng giờ khác nhau, mô hình nhị thức đơn giản có thể không phù hợp.


**Q10. What do mean and standard deviation determine for normal? | Mean và std xác định gì trong chuẩn?**

A. Independent trials with constant success probability | Các lần thử độc lập cùng xác suất thành công

B. Center and spread | Trung tâm và độ phân tán

C. Zero | Bằng 0

D. Strictly positive standard deviation | Độ lệch chuẩn phải lớn hơn 0

**Đáp án: B**

**Giải thích:** Trung bình định vị và độ lệch chuẩn xác định độ rộng. Đổi độ lệch chuẩn làm chuông rộng/hẹp nhưng không nhất thiết thay tâm của phân phối.


**Q11. What is P(X=x) for a continuous normal variable? | P(X=x) với biến chuẩn liên tục bằng bao nhiêu?**

A. Independent trials with constant success probability | Các lần thử độc lập cùng xác suất thành công

B. Center and spread | Trung tâm và độ phân tán

C. Zero | Bằng 0

D. Strictly positive standard deviation | Độ lệch chuẩn phải lớn hơn 0

**Đáp án: C**

**Giải thích:** Một điểm đơn có xác suất bằng 0. Xác suất trong khoảng là diện tích dưới PDF; một điểm riêng lẻ không có diện tích.


**Q12. Which quantity must be positive for norm.pdf scale? | scale của norm.pdf cần điều kiện nào?**

A. Independent trials with constant success probability | Các lần thử độc lập cùng xác suất thành công

B. Center and spread | Trung tâm và độ phân tán

C. Zero | Bằng 0

D. Strictly positive standard deviation | Độ lệch chuẩn phải lớn hơn 0

**Đáp án: D**

**Giải thích:** Độ lệch chuẩn không dương không hợp lệ. Trong SciPy, `scale` là sigma chứ không phải sigma bình phương; truyền phương sai sẽ làm sai toàn bộ phân phối.


**Q13. What does norm.cdf(0) equal for N(0,1)? | norm.cdf(0) với N(0,1) bằng gì?**

A. 0.5 | 0.5

B. CDF(b) minus CDF(a) | CDF(b) trừ CDF(a)

C. No, sampling noise remains | Không, vẫn có dao động lấy mẫu

D. From 0 to 1 inclusive | Từ 0 đến 1 gồm hai đầu

**Đáp án: A**

**Giải thích:** Chuẩn tắc đối xứng quanh 0. Chuẩn tắc đối xứng quanh trung bình 0 nên mỗi phía chứa một nửa xác suất.


**Q14. How do you calculate normal P(a<X≤b)? | Tính P(a<X≤b) cho chuẩn bằng gì?**

A. 0.5 | 0.5

B. CDF(b) minus CDF(a) | CDF(b) trừ CDF(a)

C. No, sampling noise remains | Không, vẫn có dao động lấy mẫu

D. From 0 to 1 inclusive | Từ 0 đến 1 gồm hai đầu

**Đáp án: B**

**Giải thích:** Hiệu xác suất tích lũy cho xác suất đoạn. Ví dụ P(−1<X≤1) bằng `norm.cdf(1)-norm.cdf(-1)`, xấp xỉ 0,6827.


**Q15. Does fixed RNG seed force sample mean to equal μ? | Seed cố định có buộc mean mẫu bằng μ?**

A. 0.5 | 0.5

B. CDF(b) minus CDF(a) | CDF(b) trừ CDF(a)

C. No, sampling noise remains | Không, vẫn có dao động lấy mẫu

D. From 0 to 1 inclusive | Từ 0 đến 1 gồm hai đầu

**Đáp án: C**

**Giải thích:** Seed lặp được mẫu, không đảm bảo đúng moment lý thuyết. Mô phỏng cố định seed có thể lặp lại nhưng trung bình mẫu vẫn lệch so với kỳ vọng lý thuyết.


**Q16. What is the range of probabilities? | Xác suất nằm trong đoạn nào?**

A. 0.5 | 0.5

B. CDF(b) minus CDF(a) | CDF(b) trừ CDF(a)

C. No, sampling noise remains | Không, vẫn có dao động lấy mẫu

D. From 0 to 1 inclusive | Từ 0 đến 1 gồm hai đầu

**Đáp án: D**

**Giải thích:** Xác suất không âm và không vượt một. Hai đầu 0 và 1 tương ứng biến cố không thể và chắc chắn.


**Q17. Can a continuous PDF exceed 1 at a point? | PDF liên tục có thể lớn hơn 1 tại một điểm không?**

A. Yes; only its total integral must be one | Có; chỉ tích phân toàn miền phải bằng một

B. The distribution becomes wider | Phân phối trải rộng hơn

C. Point probabilities behave differently | Xác suất tại một điểm có ý nghĩa khác nhau

D. Cumulative probability up to x | Xác suất tích lũy tới x

**Đáp án: A**

**Giải thích:** Chiều cao mật độ không phải xác suất. Đường chuẩn có độ lệch chuẩn nhỏ có thể có đỉnh PDF cao hơn 1 nhưng tổng diện tích vẫn bằng 1.


**Q18. What happens when standard deviation of normal increases? | Std phân phối chuẩn tăng sẽ thế nào?**

A. Yes; only its total integral must be one | Có; chỉ tích phân toàn miền phải bằng một

B. The distribution becomes wider | Phân phối trải rộng hơn

C. Point probabilities behave differently | Xác suất tại một điểm có ý nghĩa khác nhau

D. Cumulative probability up to x | Xác suất tích lũy tới x

**Đáp án: B**

**Giải thích:** Cùng tổng diện tích được trải ra trên miền rộng hơn. Sigma lớn hơn không tự làm dịch mean; nó khiến số đo phân tán xa hơn quanh cùng tâm.


**Q19. Why distinguish discrete and continuous variables? | Vì sao phân biệt biến rời rạc và liên tục?**

A. Yes; only its total integral must be one | Có; chỉ tích phân toàn miền phải bằng một

B. The distribution becomes wider | Phân phối trải rộng hơn

C. Point probabilities behave differently | Xác suất tại một điểm có ý nghĩa khác nhau

D. Cumulative probability up to x | Xác suất tích lũy tới x

**Đáp án: C**

**Giải thích:** PMF là xác suất còn PDF là mật độ. Số đếm như X=3 có xác suất tại điểm dương, còn biến đo liên tục có xác suất bằng đúng một giá trị là 0.


**Q20. What does norm.cdf(x,loc,scale) return? | norm.cdf(x,loc,scale) trả gì?**

A. Yes; only its total integral must be one | Có; chỉ tích phân toàn miền phải bằng một

B. The distribution becomes wider | Phân phối trải rộng hơn

C. Point probabilities behave differently | Xác suất tại một điểm có ý nghĩa khác nhau

D. Cumulative probability up to x | Xác suất tích lũy tới x

**Đáp án: D**

**Giải thích:** Nó là P(X≤x) theo phân phối chuẩn. Không lấy chiều cao PDF nếu câu hỏi là P(X≤x); cần dùng `cdf` để tính xác suất tích lũy.

## 8. Liên hệ bài tiếp theo

`Xác suất → Biến ngẫu nhiên → Phân phối → Thống kê`.
