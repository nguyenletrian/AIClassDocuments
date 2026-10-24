# PY-40 — Kiểm định giả thuyết, p-value và khoảng tin cậy


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Null hypothesis** — giả thuyết không; **p-value** — giá trị p.

`CLT/SE → Hypothesis Testing → Confidence Interval → A/B Test`

Kiến thức giúp sinh viên dùng Python để hiểu dữ liệu, đánh giá độ bất định và chuẩn bị dữ liệu cho AI.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Khái niệm |
|---|---|---|
| Null hypothesis | giả thuyết không | Phát biểu gốc đem kiểm định, ký hiệu H0 |
| p-value | giá trị p | Độ bất thường của dữ liệu nếu giả định H0 đúng |
| T-test | kiểm định t | Kiểm định trung bình khi phương sai tổng thể chưa biết |
| Confidence interval | khoảng tin cậy | Khoảng tính theo quy trình có mức bao phủ dài hạn xác định |

## 3. Hàm và công thức áp dụng

| Công cụ | Ý nghĩa |
|---|---|
| `ttest_1samp(values, popmean)` | Kiểm định t một mẫu so với trung bình giả thuyết |
| `sem(values)` | Sai số chuẩn của mean mẫu, mặc định theo SD mẫu |
| `t.interval(confidence, df, loc, scale)` | Khoảng t với mức tin cậy, bậc tự do, trung bình và SE |
| `pvalue < alpha` | Quy tắc bác bỏ H₀ nếu p nhỏ hơn mức ý nghĩa đã chọn |

## 4. Khái niệm chính và liên quan

**Mạch kiến thức:** Đầu tiên đặt giả thuyết H₀ và H₁. Kiểm định t tạo thống kê kiểm định và p-value dưới giả định H₀; so p với ngưỡng α để quyết định có bác bỏ hay không. Khoảng tin cậy dùng thống kê mẫu và sai số chuẩn để biểu diễn mức bất định của ước lượng theo quy trình bao phủ dài hạn.

### 4.1. Null hypothesis — Giả thuyết gốc cần kiểm định

**Từ vựng:** **Null hypothesis (H₀)** — giả thuyết không; **Alternative (H₁)** — giả thuyết đối.

**H₀** là phát biểu gốc để đối chiếu dữ liệu, thường là “trung bình μ=50 điểm”, còn H₁ có thể là “μ khác 50 điểm”. Không biết trước giả thuyết nào đúng; ta xem dữ liệu mẫu có **quá bất thường nếu H₀ đúng** hay không. H₀ là một phát biểu về quần thể, không phải câu hỏi liệu mean của bảy điểm đo có đúng bằng 50. Ví dụ in cặp giả thuyết rõ ràng trước khi tính.

```python
print('H0: population mean = 50')
print('H1: population mean != 50')
```

**Kết quả khi chạy:**

```text
H0: population mean = 50
H1: population mean != 50
```

Hai phát biểu về trung bình quần thể khác với giá trị trung bình của riêng một mẫu.

### 4.2. p-value — Độ bất thường dưới giả định H₀

**Từ vựng:** **p-value** — giá trị p; **Significance level (α)** — mức ý nghĩa.

**p-value** là xác suất (nếu H₀ đúng và mô hình kiểm định phù hợp) thấy một thống kê kiểm định **ít nhất cực đoan như đã quan sát**. Nó **không** phải xác suất H₀ đúng hoặc xác suất kết quả do ngẫu nhiên. Ví dụ bảy điểm `[48,52,55,49,51,47,53]`, kiểm định hai phía so μ=50 bằng t-test cho p≈0.5347. Với α=0.05, chưa đủ bằng chứng để bác bỏ H₀; không có nghĩa chứng minh μ=50.

```python
from scipy.stats import ttest_1samp

scores = [48, 52, 55, 49, 51, 47, 53]
p = ttest_1samp(scores, popmean=50).pvalue
print(round(float(p), 4))
```

**Kết quả khi chạy:**

```text
0.5347
```

p≈0,5347 lớn hơn 0,05; chưa đủ bằng chứng bác bỏ H₀ với kiểm định hai phía.

### 4.3. T-test — So trung bình mẫu với mốc cho trước

**Từ vựng:** **T-test** — kiểm định t; **Standard error** — sai số chuẩn.

**T-test một mẫu** xét liệu trung bình của quần thể có thể khác một mốc μ₀ khi chưa biết phương sai quần thể. Thống kê t bằng `(mean_mẫu−μ₀)/SE`, với `SE=s/√n` và `s` là độ lệch chuẩn mẫu. Nếu mẫu `[8,9,10,11,12]` và μ₀=10, mean bằng mốc nên t=0 và p hai phía=1. Cần xét tính độc lập và mức phù hợp của phân phối/độ nhạy với ngoại lệ, nhất là mẫu nhỏ.

```python
from scipy.stats import ttest_1samp

values = [8, 9, 10, 11, 12]
result = ttest_1samp(values, popmean=10)
print(round(float(result.statistic), 3))
```

**Kết quả khi chạy:**

```text
0.0
```

Vì mean mẫu đúng bằng 10, thống kê kiểm định t=0.

### 4.4. Confidence interval — Khoảng tạo bởi quy trình suy luận

**Từ vựng:** **Confidence interval (CI)** — khoảng tin cậy; **Coverage** — tỷ lệ bao phủ.

**Khoảng tin cậy 95%** là khoảng được tạo bởi **một quy trình** sao cho trong các lần lấy mẫu lặp phù hợp, khoảng 95% các khoảng chứa tham số thật. Với một khoảng **đã tính**, μ thật là cố định; không diễn giải “xác suất 95% μ ở trong khoảng này” theo nghĩa tần suất. Ví dụ năm thời gian giao `[2,3,3,4,2]` ngày cho mean=2,8 và CI t 95% xấp xỉ `[1.761,3.839]` ngày. Mẫu nhỏ nên khoảng rộng và dựa vào giả định dữ liệu độc lập, phân phối phù hợp.

```python
import numpy as np
from scipy.stats import t, sem

days = np.array([2.0, 3.0, 3.0, 4.0, 2.0])
ci = t.interval(0.95, df=len(days) - 1, loc=days.mean(), scale=sem(days))
print(np.round(ci, 3).tolist())
```

**Kết quả khi chạy:**

```text
[1.761, 3.839]
```

Khoảng ước lượng mean theo t từ khoảng 1,761 đến 3,839 ngày; đây là khoảng cho trung bình quần thể.

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Kiểm định điểm trung bình so với chuẩn 50

**Tình huống thực tế:** Trung tâm có bảy điểm `[48,52,55,49,51,47,53]`, cùng thang 100 và giả định độc lập. Cần kiểm tra trung bình quần thể có khác chuẩn 50 theo kiểm định hai phía ở mức α=0.05 không.

**Vì sao chọn cách giải này?** T-test một mẫu so mean với mốc khi phương sai quần thể chưa biết.

**Quy trình giải:**

1. Đặt H₀: μ=50, H₁: μ≠50 và α=0.05 trước khi xem kết quả.
2. Tính `ttest_1samp` trên bảy điểm.
3. In p-value làm tròn và so với α.

```python
from scipy.stats import ttest_1samp

scores = [48, 52, 55, 49, 51, 47, 53]
p = ttest_1samp(scores, popmean=50).pvalue
print(round(float(p), 4))
```

**Kết quả khi chạy:**

```text
0.5347
```

Vì p lớn hơn 0,05 nên chưa đủ bằng chứng bác bỏ H₀; không khẳng định H₀ đúng.

### Tình huống 2 — Tính khoảng tin cậy thời gian giao

**Tình huống thực tế:** Năm đơn giao mất `[2,3,3,4,2]` ngày, giả định độc lập và mô hình suy luận t phù hợp. Doanh nghiệp muốn khoảng tin cậy 95% cho **trung bình số ngày** của tổng thể.

**Vì sao chọn cách giải này?** Khi chưa biết phương sai tổng thể và mẫu nhỏ, khoảng t dùng độ lệch chuẩn mẫu và n−1 bậc tự do.

**Quy trình giải:**

1. Tạo mảng năm số ngày và tính mean mẫu.
2. Tính SE qua `sem` và khoảng t với df=4.
3. In hai đầu mút làm tròn ba chữ số.

```python
import numpy as np
from scipy.stats import t, sem

days = np.array([2.0, 3.0, 3.0, 4.0, 2.0])
ci = t.interval(0.95, df=len(days) - 1, loc=days.mean(), scale=sem(days))
print(np.round(ci, 3).tolist())
```

**Kết quả khi chạy:**

```text
[1.761, 3.839]
```

Khoảng t 95% ước lượng trung bình quần thể từ 1,761 đến 3,839 ngày.

### Tình huống 3 — Tính SE của thời gian giao trung bình

**Tình huống thực tế:** Với đúng năm thời gian giao `[2,3,3,4,2]` ngày, quản lý muốn báo sai số chuẩn của **ước lượng mean**, không phải mức phân tán từng đơn.

**Vì sao chọn cách giải này?** `sem` ước lượng độ biến thiên mean bằng SD mẫu chia căn cỡ mẫu.

**Quy trình giải:**

1. Dùng mảng năm số ngày.
2. Gọi `scipy.stats.sem` với ddof mẫu mặc định.
3. Làm tròn ba chữ số, ghi đơn vị ngày.

```python
from scipy.stats import sem

days = [2, 3, 3, 4, 2]
print(round(float(sem(days)), 3))
```

**Kết quả khi chạy:**

```text
0.374
```

SE ước lượng khoảng 0,374 ngày của mean, không phải std của thời gian từng đơn.

### Tình huống 4 — Ra quyết định với kiểm định hai phía

**Tình huống thực tế:** Dữ liệu năm số đo `[5,6,7,8,9]` được dùng kiểm định trung bình với mốc μ₀=6, α=0.05. Nhóm phân tích muốn chương trình đưa ra quyết định theo ngưỡng này.

**Vì sao chọn cách giải này?** So p-value với α là một quy tắc ra quyết định đã đặt trước, không coi p là xác suất H₀ đúng.

**Quy trình giải:**

1. Đặt H₀: μ=6 và α=0.05.
2. Tính p-value của t-test hai phía.
3. In quyết định bằng câu 'Reject H0' hoặc 'Fail to reject H0'.

```python
from scipy.stats import ttest_1samp

values = [5, 6, 7, 8, 9]
p = ttest_1samp(values, popmean=6).pvalue
print('Reject H0' if p < 0.05 else 'Fail to reject H0')
```

**Kết quả khi chạy:**

```text
Fail to reject H0
```

Không bác bỏ H₀ tại α=0.05, chứ không có nghĩa đã chứng minh μ=6.

### Tình huống 5 — Thấy vai trò của mức ý nghĩa alpha

**Tình huống thực tế:** Một phép kiểm định đã tính được p-value=0.04. Đội kiểm thử muốn so hai mức ý nghĩa **0.01 và 0.05** trên cùng bằng chứng, không thay đổi dữ liệu.

**Vì sao chọn cách giải này?** α là ngưỡng lựa chọn để quyết định bác bỏ H₀; thay α có thể đổi quyết định dù p giữ nguyên.

**Quy trình giải:**

1. Đặt p=0.04 đã tính sẵn.
2. So p với hai ngưỡng 0.01 và 0.05.
3. In ngưỡng và Boolean cho việc bác bỏ H₀.

```python
p = 0.04
for alpha in [0.01, 0.05]:
    print(alpha, p < alpha)
```

**Kết quả khi chạy:**

```text
0.01 False
0.05 True
```

Với α=0.01 chưa bác bỏ, với α=0.05 thì bác bỏ; không suy ra xác suất H₀ đúng là 4%.

## 6. Sai lầm thường gặp

- p-value không phải xác suất H₀ đúng; nó là xác suất của kết quả cực đoan dưới giả định H₀.
- Không bác bỏ H₀ **không** đồng nghĩa chấp nhận hay chứng minh H₀ đúng.
- α=0.05 là ngưỡng kiểm định lựa chọn trước, không phải ngưỡng hiệu quả thực tế.
- CI 95% có **tỷ lệ bao phủ dài hạn 95%** khi lặp quy trình, không phải xác suất 95% tham số cố định trong một khoảng đã quan sát.
- SE khác SD: SE nói về bất định của mean, SD nói về số đo riêng lẻ.
- T-test trên mẫu nhỏ nhạy với ngoại lệ/phụ thuộc; cần xem giả định và thiết kế lấy mẫu.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Q1. What is H0? — H₀ là gì?**

A. A null hypothesis subjected to statistical testing — Giả thuyết không được đem kiểm định

B. Probability of equally or more extreme test results under H0 — Xác suất thống kê cực đoan bằng hoặc hơn khi H₀ đúng

C. Test a population mean against a specified value — Kiểm định trung bình quần thể với một mốc

D. An interval from a procedure with 95% long-run coverage — Khoảng từ quy trình có mức bao phủ dài hạn 95%

**Q2. What does p-value mean? — p-value nghĩa là gì?**

A. A null hypothesis subjected to statistical testing — Giả thuyết không được đem kiểm định

B. Probability of equally or more extreme test results under H0 — Xác suất thống kê cực đoan bằng hoặc hơn khi H₀ đúng

C. Test a population mean against a specified value — Kiểm định trung bình quần thể với một mốc

D. An interval from a procedure with 95% long-run coverage — Khoảng từ quy trình có mức bao phủ dài hạn 95%

**Q3. What is a one-sample t-test for? — T-test một mẫu dùng để làm gì?**

A. A null hypothesis subjected to statistical testing — Giả thuyết không được đem kiểm định

B. Probability of equally or more extreme test results under H0 — Xác suất thống kê cực đoan bằng hoặc hơn khi H₀ đúng

C. Test a population mean against a specified value — Kiểm định trung bình quần thể với một mốc

D. An interval from a procedure with 95% long-run coverage — Khoảng từ quy trình có mức bao phủ dài hạn 95%

**Q4. What is a 95% confidence interval? — Khoảng tin cậy 95% là gì?**

A. A null hypothesis subjected to statistical testing — Giả thuyết không được đem kiểm định

B. Probability of equally or more extreme test results under H0 — Xác suất thống kê cực đoan bằng hoặc hơn khi H₀ đúng

C. Test a population mean against a specified value — Kiểm định trung bình quần thể với một mốc

D. An interval from a procedure with 95% long-run coverage — Khoảng từ quy trình có mức bao phủ dài hạn 95%

**Q5. What does alpha represent? — α đại diện cho gì?**

A. A preselected significance threshold — Ngưỡng mức ý nghĩa được chọn trước

B. Reject H0 at that significance level — Bác bỏ H₀ ở mức ý nghĩa đó

C. Fail to reject H0 — Chưa đủ bằng chứng bác bỏ H₀

D. Compare one sample mean with mu0 — So mean một mẫu với mốc mu0

**Q6. What does p<alpha typically imply? — p<α thường dẫn tới gì?**

A. A preselected significance threshold — Ngưỡng mức ý nghĩa được chọn trước

B. Reject H0 at that significance level — Bác bỏ H₀ ở mức ý nghĩa đó

C. Fail to reject H0 — Chưa đủ bằng chứng bác bỏ H₀

D. Compare one sample mean with mu0 — So mean một mẫu với mốc mu0

**Q7. What does p≥alpha imply? — p≥α thường kết luận gì?**

A. A preselected significance threshold — Ngưỡng mức ý nghĩa được chọn trước

B. Reject H0 at that significance level — Bác bỏ H₀ ở mức ý nghĩa đó

C. Fail to reject H0 — Chưa đủ bằng chứng bác bỏ H₀

D. Compare one sample mean with mu0 — So mean một mẫu với mốc mu0

**Q8. What is `ttest_1samp(x,popmean=mu0)` for? — `ttest_1samp(x,popmean=mu0)` dùng làm gì?**

A. A preselected significance threshold — Ngưỡng mức ý nghĩa được chọn trước

B. Reject H0 at that significance level — Bác bỏ H₀ ở mức ý nghĩa đó

C. Fail to reject H0 — Chưa đủ bằng chứng bác bỏ H₀

D. Compare one sample mean with mu0 — So mean một mẫu với mốc mu0

**Q9. How is a one-sample t statistic formed? — Thống kê t một mẫu có dạng gì?**

A. (sample mean−mu0)/SE — (mean mẫu−mu0)/SE

B. Standard error of the mean — Sai số chuẩn của trung bình

C. Lower and upper endpoints of a t interval — Hai đầu dưới/trên của khoảng t

D. n−1 — n−1

**Q10. What does `scipy.stats.sem` estimate? — `scipy.stats.sem` ước lượng gì?**

A. (sample mean−mu0)/SE — (mean mẫu−mu0)/SE

B. Standard error of the mean — Sai số chuẩn của trung bình

C. Lower and upper endpoints of a t interval — Hai đầu dưới/trên của khoảng t

D. n−1 — n−1

**Q11. What does t.interval return? — t.interval trả gì?**

A. (sample mean−mu0)/SE — (mean mẫu−mu0)/SE

B. Standard error of the mean — Sai số chuẩn của trung bình

C. Lower and upper endpoints of a t interval — Hai đầu dưới/trên của khoảng t

D. n−1 — n−1

**Q12. What degrees of freedom are usual for one-sample t inference? — Bậc tự do thông dụng của t một mẫu là gì?**

A. (sample mean−mu0)/SE — (mean mẫu−mu0)/SE

B. Standard error of the mean — Sai số chuẩn của trung bình

C. Lower and upper endpoints of a t interval — Hai đầu dưới/trên của khoảng t

D. n−1 — n−1

**Q13. Is p-value equal to P(H0 is true)? — p-value có bằng P(H₀ đúng) không?**

A. No; p is conditional on H0 — Không; p được tính khi giả định H₀ đúng

B. It does not reject at the matching alpha — Không bác bỏ với alpha tương ứng

C. Rejecting a true null hypothesis — Bác bỏ H₀ khi H₀ thực sự đúng

D. Failing to reject a false H0 — Không bác bỏ H₀ khi H₀ sai

**Q14. If a confidence interval covers a null value, what often happens in a matching two-sided test? — Nếu CI chứa mốc H₀ thì kiểm định hai phía tương ứng thường thế nào?**

A. No; p is conditional on H0 — Không; p được tính khi giả định H₀ đúng

B. It does not reject at the matching alpha — Không bác bỏ với alpha tương ứng

C. Rejecting a true null hypothesis — Bác bỏ H₀ khi H₀ thực sự đúng

D. Failing to reject a false H0 — Không bác bỏ H₀ khi H₀ sai

**Q15. What is a type I error? — Sai lầm loại I là gì?**

A. No; p is conditional on H0 — Không; p được tính khi giả định H₀ đúng

B. It does not reject at the matching alpha — Không bác bỏ với alpha tương ứng

C. Rejecting a true null hypothesis — Bác bỏ H₀ khi H₀ thực sự đúng

D. Failing to reject a false H0 — Không bác bỏ H₀ khi H₀ sai

**Q16. What is a type II error? — Sai lầm loại II là gì?**

A. No; p is conditional on H0 — Không; p được tính khi giả định H₀ đúng

B. It does not reject at the matching alpha — Không bác bỏ với alpha tương ứng

C. Rejecting a true null hypothesis — Bác bỏ H₀ khi H₀ thực sự đúng

D. Failing to reject a false H0 — Không bác bỏ H₀ khi H₀ sai

**Q17. Does a 95% CI say the fixed parameter has 95% probability of lying in this realized interval? — CI 95% có nghĩa xác suất tham số cố định trong khoảng đã tính là 95%?**

A. No; 95% describes repeated-interval coverage — Không; 95% mô tả tỷ lệ bao phủ khi lặp

B. Strong dependence or problematic extreme data in small samples — Phụ thuộc mạnh hoặc dữ liệu cực đoan trong mẫu nhỏ

C. It becomes wider — Trở nên rộng hơn

D. No; effect size and context still matter — Không; còn kích thước tác động và bối cảnh

**Q18. What can violate simple t-test assumptions? — Điều gì có thể vi phạm giả định t-test đơn giản?**

A. No; 95% describes repeated-interval coverage — Không; 95% mô tả tỷ lệ bao phủ khi lặp

B. Strong dependence or problematic extreme data in small samples — Phụ thuộc mạnh hoặc dữ liệu cực đoan trong mẫu nhỏ

C. It becomes wider — Trở nên rộng hơn

D. No; effect size and context still matter — Không; còn kích thước tác động và bối cảnh

**Q19. What happens to CI width if SE grows with other inputs fixed? — SE tăng khi yếu tố khác giữ nguyên thì CI rộng ra sao?**

A. No; 95% describes repeated-interval coverage — Không; 95% mô tả tỷ lệ bao phủ khi lặp

B. Strong dependence or problematic extreme data in small samples — Phụ thuộc mạnh hoặc dữ liệu cực đoan trong mẫu nhỏ

C. It becomes wider — Trở nên rộng hơn

D. No; effect size and context still matter — Không; còn kích thước tác động và bối cảnh

**Q20. Is statistical significance identical to practical importance? — Ý nghĩa thống kê có giống giá trị thực tiễn không?**

A. No; 95% describes repeated-interval coverage — Không; 95% mô tả tỷ lệ bao phủ khi lặp

B. Strong dependence or problematic extreme data in small samples — Phụ thuộc mạnh hoặc dữ liệu cực đoan trong mẫu nhỏ

C. It becomes wider — Trở nên rộng hơn

D. No; effect size and context still matter — Không; còn kích thước tác động và bối cảnh

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | It is the reference assumption for the test. For example H0: μ=50 concerns the population mean, not an obligation for the observed sample mean to equal 50. | Đó là giả định gốc của kiểm định. Ví dụ H₀: μ=50 nói về mean quần thể; không đòi mean mẫu quan sát phải đúng 50. |
| Q2 | **B** | It conditions on the null model. The p-value is derived from the chosen test statistic and null distribution, not from directly assigning a probability to the null hypothesis. | Nó được tính với điều kiện mô hình H₀ đúng. p-value được tính từ thống kê kiểm định và phân phối dưới H₀, chứ không trực tiếp gán xác suất cho H₀. |
| Q3 | **C** | It uses the sample mean and estimated variance. It is distinct from a two-sample test: the one-sample version compares a single sample mean to a fixed reference. | Nó dùng trung bình và ước lượng phương sai mẫu. Khác kiểm định hai mẫu, t-test một mẫu so trung bình một mẫu với mốc cố định. |
| Q4 | **D** | Coverage describes repeated procedures. The 95% coverage describes the method over repeated samples, so a realized CI should be reported with its endpoints and assumptions. | Bao phủ được hiểu qua những lần lấy mẫu lặp. Mức bao phủ 95% thuộc quy trình qua nhiều mẫu; một CI đã tính cần báo hai đầu mút và giả định đi kèm. |
| Q5 | **A** | It controls the rejection rule. Choosing alpha after seeing a p-value can distort the intended false-positive control. | α điều khiển quy tắc bác bỏ. Chọn alpha sau khi nhìn p-value có thể làm sai ý nghĩa kiểm soát báo động nhầm dự kiến. |
| Q6 | **B** | The result is unusual under the null assumption. Rejection provides evidence against H0 under the model; it does not measure the probability H0 is false. | Kết quả bất thường dưới giả thuyết gốc. Bác bỏ cung cấp bằng chứng chống H₀ dưới mô hình, không đo xác suất H₀ sai. |
| Q7 | **C** | Nonrejection is not proof of H0. A small sample may fail to detect a real effect; 'not rejected' is not the same as 'verified equal'. | Không bác bỏ không phải chứng minh H₀. Mẫu nhỏ có thể bỏ sót tác động thật; 'không bác bỏ' khác với 'đã xác nhận bằng nhau'. |
| Q8 | **D** | It implements a one-sample t-test. The returned object includes a test statistic and p-value; read `.pvalue` explicitly for the decision. | Nó chạy kiểm định t một mẫu. Đối tượng trả về có thống kê kiểm định và p-value; lấy `.pvalue` khi cần quyết định. |
| Q9 | **A** | It standardizes the observed mean difference. A difference of 2 points only matters statistically relative to the mean's estimated sampling uncertainty. | Nó chuẩn hóa độ lệch của mean so với mốc. Chênh hai điểm chỉ có ý nghĩa kiểm định khi so với độ bất định lấy mẫu của mean. |
| Q10 | **B** | It estimates variability of the sample mean. SE decreases as sample size grows under suitable sampling assumptions, whereas individual-score SD need not. | Nó ước lượng độ dao động của mean mẫu. SE có xu hướng giảm khi n tăng dưới giả định phù hợp, còn SD của từng điểm không nhất thiết giảm. |
| Q11 | **C** | The interval depends on confidence, df, loc and scale. A larger scale yields wider endpoints; loc is the estimated center, not a confidence percentage. | Khoảng phụ thuộc mức tin cậy, df, vị trí và độ rộng. Scale lớn làm khoảng rộng; loc là ước lượng trung tâm chứ không phải phần trăm tin cậy. |
| Q12 | **D** | Estimating sample variance consumes one degree. The t statistic uses the sample variance estimate, leaving n−1 independent degrees of freedom. | Ước lượng phương sai mẫu làm mất một bậc tự do. Thống kê t ước lượng phương sai từ mẫu nên thường còn n−1 bậc tự do. |
| Q13 | **A** | A frequentist p-value is not a posterior probability. Confusing p with P(H0&#124;data) reverses the conditioning; the frequentist test instead evaluates data extremeness under H0. | p theo tần suất không phải posterior. Nhầm p với P(H₀&#124;dữ liệu) là đảo chiều điều kiện; kiểm định tần suất xét mức cực đoan của dữ liệu khi H₀ đúng. |
| Q14 | **B** | Matched procedures often agree under shared assumptions. This correspondence requires matching two-sided tests, confidence level and assumptions; it does not hold for arbitrary tests and intervals. | Các quy trình tương ứng thường thống nhất dưới cùng giả định. Sự tương ứng cần kiểm định hai phía, mức tin cậy và giả định phù hợp; không đúng với mọi loại kiểm định và khoảng. |
| Q15 | **C** | Alpha bounds type I error under test assumptions. Type I error is a false positive; alpha is the preselected bound or rate under the null-model assumptions. | Alpha kiểm soát lỗi loại I dưới giả định kiểm định. Sai lầm loại I là báo dương sai; alpha được chọn trước để kiểm soát xác suất lỗi này dưới giả định H₀. |
| Q16 | **D** | It differs from rejecting a true H0. Power equals one minus the probability of type II error under a specified alternative, linking errors to sample design. | Nó khác lỗi bác bỏ H₀ đúng. Power bằng một trừ xác suất sai lầm loại II dưới giả thuyết đối cụ thể, liên quan đến thiết kế cỡ mẫu. |
| Q17 | **A** | The frequentist parameter is fixed, interval random before sampling. The probability statement applies to a random interval procedure before sampling, rather than to the fixed unknown μ after observing one CI. | Trong diễn giải tần suất, tham số cố định và khoảng thay đổi theo mẫu. Phát biểu xác suất áp dụng cho quy trình tạo khoảng ngẫu nhiên trước lấy mẫu, không phải μ cố định sau khi quan sát một CI. |
| Q18 | **B** | Inference relies on a credible sampling model. With very small samples, heavy outliers or dependence can make the reported p-value and CI misleading. | Suy luận cần mô hình lấy mẫu phù hợp. Mẫu rất nhỏ, ngoại lệ nặng hoặc phụ thuộc có thể khiến p-value và CI báo ra thiếu tin cậy. |
| Q19 | **C** | More uncertainty produces a broader interval. In a t interval, greater SE expands the margin `t_critical × SE`, making both endpoints farther from the mean. | Bất định cao làm khoảng rộng hơn. Trong khoảng t, SE tăng làm biên `t_critical × SE` tăng, khiến hai đầu mút cách mean xa hơn. |
| Q20 | **D** | Small p does not prove a large useful effect. Report effect size and uncertainty as well as p-value; a tiny effect can be statistically detectable but not practically useful. | p nhỏ không chứng minh hiệu quả thực tế lớn. Ngoài p-value cần báo kích thước tác động và độ bất định; tác động rất nhỏ có thể có ý nghĩa thống kê nhưng không hữu ích thực tế. |

## 8. Liên hệ bài kế tiếp

`CLT/SE → Hypothesis Testing → Confidence Interval → A/B Test`.
