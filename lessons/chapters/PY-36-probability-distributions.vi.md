# PY-36 — Phân phối nhị thức và phân phối chuẩn

*DRAFT · Dữ liệu minh họa, các quy tắc khoa học chỉ áp dụng khi giả định được thỏa*

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

## 3. Hàm Python và tham số quan trọng

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm / cú pháp | Cách sử dụng |
|---|---|
| `scipy.stats.binom.pmf(k,n,p)` | P(X=k) cho số thành công rời rạc |
| `scipy.stats.binom.cdf(k,n,p)` | P(X<=k) trong mô hình nhị thức |
| `scipy.stats.norm.pdf(x,loc,scale)` | Mật độ tại x, không phải P(X=x) |
| `scipy.stats.norm.cdf(x,loc,scale)` | P(X<=x) với phân phối chuẩn |

## 4. Khái niệm liên quan, ví dụ nhỏ

### 4.1. Random variable

**Từ vựng trong mục:** **Random variable** — biến ngẫu nhiên.

Đại lượng có kết quả tùy phép thử. Trước khi tính, phân biệt điều kiện áp dụng và ý nghĩa của đầu vào.

```python
import numpy as np
print(np.random.default_rng(1).integers(0,2,5))
```

**Tự kiểm tra:** Random variable là gì? **Đáp án:** Đại lượng có kết quả tùy phép thử.

### 4.2. Binomial

**Từ vựng trong mục:** **Binomial** — phân phối nhị thức.

Số thành công của n thử Bernoulli độc lập. Trước khi tính, phân biệt điều kiện áp dụng và ý nghĩa của đầu vào.

```python
import scipy.stats as st
print(st.binom.pmf(3,10,.5))
```

**Tự kiểm tra:** Binomial là gì? **Đáp án:** Số thành công của n thử Bernoulli độc lập.

### 4.3. Normal

**Từ vựng trong mục:** **Normal** — phân phối chuẩn.

Phân phối liên tục hình chuông với mean/std. Trước khi tính, phân biệt điều kiện áp dụng và ý nghĩa của đầu vào.

```python
import scipy.stats as st
print(st.norm.cdf(0))
```

**Tự kiểm tra:** Normal là gì? **Đáp án:** Phân phối liên tục hình chuông với mean/std.

### 4.4. PMF/PDF

**Từ vựng trong mục:** **PMF/PDF** — hàm khối/mật độ.

PMF cho biến rời rạc, PDF là mật độ cho biến liên tục. Trước khi tính, phân biệt điều kiện áp dụng và ý nghĩa của đầu vào.

```python
import scipy.stats as st
print(st.binom.pmf(1,2,.5))
```

**Tự kiểm tra:** PMF/PDF là gì? **Đáp án:** PMF cho biến rời rạc, PDF là mật độ cho biến liên tục.

## 5. Năm tình huống thực tế

### Tình huống 1 — Tính số lần giao hàng đúng giờ

**Từ vựng trong mục:** **Random variable** — biến ngẫu nhiên.

**Vấn đề:** Tính số lần giao hàng đúng giờ.

**Vì sao chọn phương pháp này?** Nhị thức mô tả số đơn đạt trong n đơn độc lập cùng p. Không dùng kết quả mô phỏng làm bằng chứng thống kê khi thiếu đủ mẫu và giả định.

**Dữ liệu:** 10 đơn, xác suất mỗi đơn đúng giờ 0.8. Các số liệu là giả lập và đơn vị/thứ tự được nêu ngay tại đây; không suy ra kết luận cho người thật.

**Quy trình:** làm rõ giả định → mô tả biến cố/đặc trưng → chọn hàm → kiểm tra kết quả, giới hạn và độ nhạy.

```python
from scipy.stats import binom
print(round(binom.pmf(8,10,.8),4))
```

**Đọc kết quả:** Đối chiếu kết quả với ý nghĩa xác suất hoặc đơn vị đo; lưu ý sai số và cách lấy mẫu.

### Tình huống 2 — Tỷ lệ 3 lỗi hoặc ít hơn

**Từ vựng trong mục:** **Binomial** — phân phối nhị thức.

**Vấn đề:** Tỷ lệ 3 lỗi hoặc ít hơn.

**Vì sao chọn phương pháp này?** CDF cộng xác suất từ 0 đến 3 lỗi. Không dùng kết quả mô phỏng làm bằng chứng thống kê khi thiếu đủ mẫu và giả định.

**Dữ liệu:** 10 sản phẩm, lỗi độc lập p=0.1. Các số liệu là giả lập và đơn vị/thứ tự được nêu ngay tại đây; không suy ra kết luận cho người thật.

**Quy trình:** làm rõ giả định → mô tả biến cố/đặc trưng → chọn hàm → kiểm tra kết quả, giới hạn và độ nhạy.

```python
from scipy.stats import binom
print(round(binom.cdf(3,10,.1),4))
```

**Đọc kết quả:** Đối chiếu kết quả với ý nghĩa xác suất hoặc đơn vị đo; lưu ý sai số và cách lấy mẫu.

### Tình huống 3 — Điểm chuẩn của cảm biến

**Từ vựng trong mục:** **Normal** — phân phối chuẩn.

**Vấn đề:** Điểm chuẩn của cảm biến.

**Vì sao chọn phương pháp này?** CDF cho tỷ lệ thấp hơn một ngưỡng. Không dùng kết quả mô phỏng làm bằng chứng thống kê khi thiếu đủ mẫu và giả định.

**Dữ liệu:** Trung bình 100, độ lệch chuẩn 15, ngưỡng 115. Các số liệu là giả lập và đơn vị/thứ tự được nêu ngay tại đây; không suy ra kết luận cho người thật.

**Quy trình:** làm rõ giả định → mô tả biến cố/đặc trưng → chọn hàm → kiểm tra kết quả, giới hạn và độ nhạy.

```python
from scipy.stats import norm
print(norm.cdf(115,loc=100,scale=15))
```

**Đọc kết quả:** Đối chiếu kết quả với ý nghĩa xác suất hoặc đơn vị đo; lưu ý sai số và cách lấy mẫu.

### Tình huống 4 — Xem mật độ tại một điểm

**Từ vựng trong mục:** **PMF/PDF** — hàm khối/mật độ.

**Vấn đề:** Xem mật độ tại một điểm.

**Vì sao chọn phương pháp này?** PDF là mật độ, không phải xác suất tại đúng một điểm liên tục. Không dùng kết quả mô phỏng làm bằng chứng thống kê khi thiếu đủ mẫu và giả định.

**Dữ liệu:** Phân phối chuẩn mean=0,std=1 tại x=0. Các số liệu là giả lập và đơn vị/thứ tự được nêu ngay tại đây; không suy ra kết luận cho người thật.

**Quy trình:** làm rõ giả định → mô tả biến cố/đặc trưng → chọn hàm → kiểm tra kết quả, giới hạn và độ nhạy.

```python
from scipy.stats import norm
print(norm.pdf(0))
```

**Đọc kết quả:** Đối chiếu kết quả với ý nghĩa xác suất hoặc đơn vị đo; lưu ý sai số và cách lấy mẫu.

### Tình huống 5 — Sinh dữ liệu chuẩn mô phỏng

**Từ vựng trong mục:** **Random variable** — biến ngẫu nhiên.

**Vấn đề:** Sinh dữ liệu chuẩn mô phỏng.

**Vì sao chọn phương pháp này?** RNG dùng seed để kết quả minh họa lặp được. Không dùng kết quả mô phỏng làm bằng chứng thống kê khi thiếu đủ mẫu và giả định.

**Dữ liệu:** 5 mẫu chuẩn mean=0,std=1. Các số liệu là giả lập và đơn vị/thứ tự được nêu ngay tại đây; không suy ra kết luận cho người thật.

**Quy trình:** làm rõ giả định → mô tả biến cố/đặc trưng → chọn hàm → kiểm tra kết quả, giới hạn và độ nhạy.

```python
import numpy as np
rng=np.random.default_rng(42)
print(rng.normal(loc=0,scale=1,size=5))
```

**Đọc kết quả:** Đối chiếu kết quả với ý nghĩa xác suất hoặc đơn vị đo; lưu ý sai số và cách lấy mẫu.

## 6. Những nhầm lẫn thường gặp

Xác suất có điều kiện cần mẫu nền; xác suất của phân phối liên tục tại một điểm không phải PDF; thống kê từ một nhóm nhỏ không tự chứng minh kết quả cho quần thể. Chú ý định nghĩa mean/std và giả định độc lập.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.


**Q1. What is Random variable? — Thuật ngữ Random variable là gì?**

A. Another concept means Số thành công của n thử Bernoulli độc lập — Số thành công của n thử Bernoulli độc lập

B. It means Đại lượng có kết quả tùy phép thử — Đại lượng có kết quả tùy phép thử

C. Another concept means Phân phối liên tục hình chuông với mean/std — Phân phối liên tục hình chuông với mean/std

D. Another concept means PMF cho biến rời rạc, PDF là mật độ cho biến liên tục — PMF cho biến rời rạc, PDF là mật độ cho biến liên tục


**Q2. What is Binomial? — Thuật ngữ Binomial là gì?**

A. It means Số thành công của n thử Bernoulli độc lập — Số thành công của n thử Bernoulli độc lập

B. Another concept means Phân phối liên tục hình chuông với mean/std — Phân phối liên tục hình chuông với mean/std

C. Another concept means PMF cho biến rời rạc, PDF là mật độ cho biến liên tục — PMF cho biến rời rạc, PDF là mật độ cho biến liên tục

D. Another concept means Đại lượng có kết quả tùy phép thử — Đại lượng có kết quả tùy phép thử


**Q3. What is Normal? — Thuật ngữ Normal là gì?**

A. Another concept means PMF cho biến rời rạc, PDF là mật độ cho biến liên tục — PMF cho biến rời rạc, PDF là mật độ cho biến liên tục

B. Another concept means Đại lượng có kết quả tùy phép thử — Đại lượng có kết quả tùy phép thử

C. Another concept means Số thành công của n thử Bernoulli độc lập — Số thành công của n thử Bernoulli độc lập

D. It means Phân phối liên tục hình chuông với mean/std — Phân phối liên tục hình chuông với mean/std


**Q4. What is PMF/PDF? — Thuật ngữ PMF/PDF là gì?**

A. Another concept means Đại lượng có kết quả tùy phép thử — Đại lượng có kết quả tùy phép thử

B. Another concept means Số thành công của n thử Bernoulli độc lập — Số thành công của n thử Bernoulli độc lập

C. It means PMF cho biến rời rạc, PDF là mật độ cho biến liên tục — PMF cho biến rời rạc, PDF là mật độ cho biến liên tục

D. Another concept means Phân phối liên tục hình chuông với mean/std — Phân phối liên tục hình chuông với mean/std


**Q5. What does scipy.stats.binom.pmf(k,n,p) calculate? — Hàm scipy.stats.binom.pmf(k,n,p) tính gì?**

A. Another calculation is P(X<=k) trong mô hình nhị thức — P(X<=k) trong mô hình nhị thức

B. It calculates P(X=k) cho số thành công rời rạc — P(X=k) cho số thành công rời rạc

C. Another calculation is Mật độ tại x, không phải P(X=x) — Mật độ tại x, không phải P(X=x)

D. Another calculation is P(X<=x) với phân phối chuẩn — P(X<=x) với phân phối chuẩn


**Q6. What does scipy.stats.binom.cdf(k,n,p) calculate? — Hàm scipy.stats.binom.cdf(k,n,p) tính gì?**

A. It calculates P(X<=k) trong mô hình nhị thức — P(X<=k) trong mô hình nhị thức

B. Another calculation is Mật độ tại x, không phải P(X=x) — Mật độ tại x, không phải P(X=x)

C. Another calculation is P(X<=x) với phân phối chuẩn — P(X<=x) với phân phối chuẩn

D. Another calculation is P(X=k) cho số thành công rời rạc — P(X=k) cho số thành công rời rạc


**Q7. What does scipy.stats.norm.pdf(x,loc,scale) calculate? — Hàm scipy.stats.norm.pdf(x,loc,scale) tính gì?**

A. Another calculation is P(X<=x) với phân phối chuẩn — P(X<=x) với phân phối chuẩn

B. Another calculation is P(X=k) cho số thành công rời rạc — P(X=k) cho số thành công rời rạc

C. Another calculation is P(X<=k) trong mô hình nhị thức — P(X<=k) trong mô hình nhị thức

D. It calculates Mật độ tại x, không phải P(X=x) — Mật độ tại x, không phải P(X=x)


**Q8. What does scipy.stats.norm.cdf(x,loc,scale) calculate? — Hàm scipy.stats.norm.cdf(x,loc,scale) tính gì?**

A. Another calculation is P(X=k) cho số thành công rời rạc — P(X=k) cho số thành công rời rạc

B. Another calculation is P(X<=k) trong mô hình nhị thức — P(X<=k) trong mô hình nhị thức

C. It calculates P(X<=x) với phân phối chuẩn — P(X<=x) với phân phối chuẩn

D. Another calculation is Mật độ tại x, không phải P(X=x) — Mật độ tại x, không phải P(X=x)


**Q9. Why use this method in scenario 1? — Vì sao chọn phương pháp trong tình huống 1?**

A. CDF cộng xác suất từ 0 đến 3 lỗi — CDF cộng xác suất từ 0 đến 3 lỗi

B. Nhị thức mô tả số đơn đạt trong n đơn độc lập cùng p — Nhị thức mô tả số đơn đạt trong n đơn độc lập cùng p

C. CDF cho tỷ lệ thấp hơn một ngưỡng — CDF cho tỷ lệ thấp hơn một ngưỡng

D. PDF là mật độ, không phải xác suất tại đúng một điểm liên tục — PDF là mật độ, không phải xác suất tại đúng một điểm liên tục


**Q10. Why use this method in scenario 2? — Vì sao chọn phương pháp trong tình huống 2?**

A. CDF cộng xác suất từ 0 đến 3 lỗi — CDF cộng xác suất từ 0 đến 3 lỗi

B. CDF cho tỷ lệ thấp hơn một ngưỡng — CDF cho tỷ lệ thấp hơn một ngưỡng

C. PDF là mật độ, không phải xác suất tại đúng một điểm liên tục — PDF là mật độ, không phải xác suất tại đúng một điểm liên tục

D. RNG dùng seed để kết quả minh họa lặp được — RNG dùng seed để kết quả minh họa lặp được


**Q11. Why use this method in scenario 3? — Vì sao chọn phương pháp trong tình huống 3?**

A. PDF là mật độ, không phải xác suất tại đúng một điểm liên tục — PDF là mật độ, không phải xác suất tại đúng một điểm liên tục

B. RNG dùng seed để kết quả minh họa lặp được — RNG dùng seed để kết quả minh họa lặp được

C. Nhị thức mô tả số đơn đạt trong n đơn độc lập cùng p — Nhị thức mô tả số đơn đạt trong n đơn độc lập cùng p

D. CDF cho tỷ lệ thấp hơn một ngưỡng — CDF cho tỷ lệ thấp hơn một ngưỡng


**Q12. Why use this method in scenario 4? — Vì sao chọn phương pháp trong tình huống 4?**

A. RNG dùng seed để kết quả minh họa lặp được — RNG dùng seed để kết quả minh họa lặp được

B. Nhị thức mô tả số đơn đạt trong n đơn độc lập cùng p — Nhị thức mô tả số đơn đạt trong n đơn độc lập cùng p

C. PDF là mật độ, không phải xác suất tại đúng một điểm liên tục — PDF là mật độ, không phải xác suất tại đúng một điểm liên tục

D. CDF cộng xác suất từ 0 đến 3 lỗi — CDF cộng xác suất từ 0 đến 3 lỗi


**Q13. Why use this method in scenario 5? — Vì sao chọn phương pháp trong tình huống 5?**

A. Nhị thức mô tả số đơn đạt trong n đơn độc lập cùng p — Nhị thức mô tả số đơn đạt trong n đơn độc lập cùng p

B. RNG dùng seed để kết quả minh họa lặp được — RNG dùng seed để kết quả minh họa lặp được

C. CDF cộng xác suất từ 0 đến 3 lỗi — CDF cộng xác suất từ 0 đến 3 lỗi

D. CDF cho tỷ lệ thấp hơn một ngưỡng — CDF cho tỷ lệ thấp hơn một ngưỡng


**Q14. Which input is from scenario 1? — Dữ liệu nào thuộc tình huống 1?**

A. The input is 10 đơn, xác suất mỗi đơn đúng giờ 0.8 — 10 đơn, xác suất mỗi đơn đúng giờ 0.8

B. Another input is 10 sản phẩm, lỗi độc lập p=0.1 — 10 sản phẩm, lỗi độc lập p=0.1

C. Another input is Trung bình 100, độ lệch chuẩn 15, ngưỡng 115 — Trung bình 100, độ lệch chuẩn 15, ngưỡng 115

D. Another input is Phân phối chuẩn mean=0,std=1 tại x=0 — Phân phối chuẩn mean=0,std=1 tại x=0


**Q15. Which input is from scenario 2? — Dữ liệu nào thuộc tình huống 2?**

A. Another input is Trung bình 100, độ lệch chuẩn 15, ngưỡng 115 — Trung bình 100, độ lệch chuẩn 15, ngưỡng 115

B. Another input is Phân phối chuẩn mean=0,std=1 tại x=0 — Phân phối chuẩn mean=0,std=1 tại x=0

C. Another input is 5 mẫu chuẩn mean=0,std=1 — 5 mẫu chuẩn mean=0,std=1

D. The input is 10 sản phẩm, lỗi độc lập p=0.1 — 10 sản phẩm, lỗi độc lập p=0.1


**Q16. Which input is from scenario 3? — Dữ liệu nào thuộc tình huống 3?**

A. Another input is Phân phối chuẩn mean=0,std=1 tại x=0 — Phân phối chuẩn mean=0,std=1 tại x=0

B. Another input is 5 mẫu chuẩn mean=0,std=1 — 5 mẫu chuẩn mean=0,std=1

C. The input is Trung bình 100, độ lệch chuẩn 15, ngưỡng 115 — Trung bình 100, độ lệch chuẩn 15, ngưỡng 115

D. Another input is 10 đơn, xác suất mỗi đơn đúng giờ 0.8 — 10 đơn, xác suất mỗi đơn đúng giờ 0.8


**Q17. Which input is from scenario 4? — Dữ liệu nào thuộc tình huống 4?**

A. Another input is 5 mẫu chuẩn mean=0,std=1 — 5 mẫu chuẩn mean=0,std=1

B. The input is Phân phối chuẩn mean=0,std=1 tại x=0 — Phân phối chuẩn mean=0,std=1 tại x=0

C. Another input is 10 đơn, xác suất mỗi đơn đúng giờ 0.8 — 10 đơn, xác suất mỗi đơn đúng giờ 0.8

D. Another input is 10 sản phẩm, lỗi độc lập p=0.1 — 10 sản phẩm, lỗi độc lập p=0.1


**Q18. Which input is from scenario 5? — Dữ liệu nào thuộc tình huống 5?**

A. The input is 5 mẫu chuẩn mean=0,std=1 — 5 mẫu chuẩn mean=0,std=1

B. Another input is 10 đơn, xác suất mỗi đơn đúng giờ 0.8 — 10 đơn, xác suất mỗi đơn đúng giờ 0.8

C. Another input is 10 sản phẩm, lỗi độc lập p=0.1 — 10 sản phẩm, lỗi độc lập p=0.1

D. Another input is Trung bình 100, độ lệch chuẩn 15, ngưỡng 115 — Trung bình 100, độ lệch chuẩn 15, ngưỡng 115


**Q19. What must a statistical report mention? — Báo cáo thống kê cần nêu gì?**

A. Only plot colors — Chỉ màu biểu đồ

B. Only a filename — Chỉ tên tệp

C. Only code line count — Chỉ số dòng code

D. Assumptions, units and sample size — Giả định, đơn vị và kích thước mẫu


**Q20. What makes a numerical result reliable? — Điều gì làm kết quả số đáng tin?**

A. Assuming all data independent — Cho rằng mọi dữ liệu độc lập

B. Deleting verification — Xóa bước xác minh

C. Checking assumptions and edge cases — Kiểm tra giả định và trường hợp biên

D. Ignoring missing inputs — Bỏ dữ liệu thiếu mà không đánh giá

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | It means Đại lượng có kết quả tùy phép thử | Đại lượng có kết quả tùy phép thử |
| Q2 | **A** | It means Số thành công của n thử Bernoulli độc lập | Số thành công của n thử Bernoulli độc lập |
| Q3 | **D** | It means Phân phối liên tục hình chuông với mean/std | Phân phối liên tục hình chuông với mean/std |
| Q4 | **C** | It means PMF cho biến rời rạc, PDF là mật độ cho biến liên tục | PMF cho biến rời rạc, PDF là mật độ cho biến liên tục |
| Q5 | **B** | It calculates P(X=k) cho số thành công rời rạc | P(X=k) cho số thành công rời rạc |
| Q6 | **A** | It calculates P(X<=k) trong mô hình nhị thức | P(X<=k) trong mô hình nhị thức |
| Q7 | **D** | It calculates Mật độ tại x, không phải P(X=x) | Mật độ tại x, không phải P(X=x) |
| Q8 | **C** | It calculates P(X<=x) với phân phối chuẩn | P(X<=x) với phân phối chuẩn |
| Q9 | **B** | Nhị thức mô tả số đơn đạt trong n đơn độc lập cùng p | Nhị thức mô tả số đơn đạt trong n đơn độc lập cùng p |
| Q10 | **A** | CDF cộng xác suất từ 0 đến 3 lỗi | CDF cộng xác suất từ 0 đến 3 lỗi |
| Q11 | **D** | CDF cho tỷ lệ thấp hơn một ngưỡng | CDF cho tỷ lệ thấp hơn một ngưỡng |
| Q12 | **C** | PDF là mật độ, không phải xác suất tại đúng một điểm liên tục | PDF là mật độ, không phải xác suất tại đúng một điểm liên tục |
| Q13 | **B** | RNG dùng seed để kết quả minh họa lặp được | RNG dùng seed để kết quả minh họa lặp được |
| Q14 | **A** | The input is 10 đơn, xác suất mỗi đơn đúng giờ 0.8 | 10 đơn, xác suất mỗi đơn đúng giờ 0.8 |
| Q15 | **D** | The input is 10 sản phẩm, lỗi độc lập p=0.1 | 10 sản phẩm, lỗi độc lập p=0.1 |
| Q16 | **C** | The input is Trung bình 100, độ lệch chuẩn 15, ngưỡng 115 | Trung bình 100, độ lệch chuẩn 15, ngưỡng 115 |
| Q17 | **B** | The input is Phân phối chuẩn mean=0,std=1 tại x=0 | Phân phối chuẩn mean=0,std=1 tại x=0 |
| Q18 | **A** | The input is 5 mẫu chuẩn mean=0,std=1 | 5 mẫu chuẩn mean=0,std=1 |
| Q19 | **D** | Assumptions, units and sample size | Giả định, đơn vị và kích thước mẫu |
| Q20 | **C** | Checking assumptions and edge cases | Kiểm tra giả định và trường hợp biên |

## 8. Liên hệ bài tiếp theo

`Xác suất → Biến ngẫu nhiên → Phân phối → Thống kê`.
