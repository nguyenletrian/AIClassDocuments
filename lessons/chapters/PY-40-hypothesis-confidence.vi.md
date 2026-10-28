# PY-40 — Kiểm định giả thuyết, p-value và khoảng tin cậy


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Null hypothesis** — giả thuyết không; **p-value** — giá trị p.

`CLT/SE → Hypothesis Testing → Confidence Interval → A/B Test`

**Học xong dùng để làm gì?** Đánh giá bằng chứng mẫu bằng p-value và khoảng tin cậy mà không kết luận chắc chắn quá mức.

**Kết nối kiến thức tiếp theo:** PY-41 chia dữ liệu train/test và đo chất lượng mô hình trên tập chưa dùng để học.

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

**No Note — Không chú thích**

```python
print('H0: population mean = 50')
print('H1: population mean != 50')
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Viết giả thuyết H0 và H1 của phép kiểm định trung bình tổng thể bằng 50.
# Dữ liệu: H0: mean quần thể =50; H1: mean khác 50 (kiểm định hai phía), chưa có dữ liệu hay p-value.
# H0 là giả thuyết gốc về trung bình TỔNG THỂ, không phải mean mẫu đã quan sát.
print('H0: population mean = 50')
# H1 đặt trung bình khác 50 theo cả hai chiều, nên là kiểm định hai phía; print chỉ mô tả, chưa chạy phép kiểm thống kê.
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

**No Note — Không chú thích**

```python
from scipy.stats import ttest_1samp

scores = [48, 52, 55, 49, 51, 47, 53]
p = ttest_1samp(scores, popmean=50).pvalue
print(round(float(p), 4))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tính p-value của kiểm định t một mẫu so với trung bình giả thuyết 50.
# Dữ liệu: 7 điểm học viên, H0 trung bình tổng thể bằng 50; không mặc định p-value là xác suất H0 đúng.
# ttest_1samp() dùng kiểm định t một mẫu khi so mean mẫu với mean giả thuyết.
from scipy.stats import ttest_1samp

# Bảy số điểm, mỗi số một học viên; giả định dữ liệu đủ phù hợp với kiểm định t.
scores = [48, 52, 55, 49, 51, 47, 53]
# popmean=50 là trung bình theo H0; mặc định alternative='two-sided' kiểm hai phía, trả đối tượng kết quả có statistic và pvalue.
# pvalue là mức xác suất thấy dữ liệu/kiểm định cực đoan ít nhất như hiện có NẾU H0 đúng, không phải P(H0 đúng|dữ liệu).
p = ttest_1samp(scores, popmean=50).pvalue
# float() chuyển scalar sang số Python, round(...,4) chỉ làm tròn p-value khi in.
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

**No Note — Không chú thích**

```python
from scipy.stats import ttest_1samp

values = [8, 9, 10, 11, 12]
result = ttest_1samp(values, popmean=10)
print(round(float(result.statistic), 3))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Đọc thống kê t của kiểm định một mẫu với trung bình giả thuyết 10.
# Dữ liệu: Năm giá trị [8,9,10,11,12], H0 trung bình tổng thể =10.
# SciPy trả kết quả kiểm định gồm statistic (t) và pvalue.
from scipy.stats import ttest_1samp

# Năm quan sát quanh mốc 10, mean mẫu cũng bằng 10.
values = [8, 9, 10, 11, 12]
# So mean mẫu với 10 qua t-statistic dùng độ lệch chuẩn mẫu và căn n; mặc định kiểm hai phía.
result = ttest_1samp(values, popmean=10)
# statistic là giá trị t đo chênh lệch đã chuẩn hóa, KHÔNG phải p-value.
# Chuyển giá trị t sang float Python rồi hiển thị ba chữ số thập phân.
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

**No Note — Không chú thích**

```python
import numpy as np
from scipy.stats import t, sem

days = np.array([2.0, 3.0, 3.0, 4.0, 2.0])
ci = t.interval(0.95, df=len(days) - 1, loc=days.mean(), scale=sem(days))
print(np.round(ci, 3).tolist())
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Xây khoảng tin cậy 95% cho mean của năm ngày bằng phân phối t.
# Dữ liệu: Năm thời lượng ngày [2,3,3,4,2], không biết độ lệch chuẩn tổng thể, dùng t với df=n−1.
# NumPy tạo ndarray và làm tròn hai mốc khoảng.
import numpy as np
# t là phân phối Student t, sem() ước lượng sai số chuẩn của trung bình mẫu.
from scipy.stats import t, sem

# Năm số ngày float, mỗi phần tử một quan sát.
days = np.array([2.0, 3.0, 3.0, 4.0, 2.0])
# interval(confidence,df,loc,scale) tìm hai cận của khoảng 95%; df=n−1=4; loc=mean mẫu; scale=sem(days) là sai số chuẩn SD_mẫu/√n, không phải SD dữ liệu.
ci = t.interval(0.95, df=len(days) - 1, loc=days.mean(), scale=sem(days))
# np.round(...,3) làm tròn hai cận để in; tolist() chuyển tuple/ndarray kết quả thành list Python; khoảng là đặc tính quy trình lấy mẫu, không phải xác suất mean cố định nằm trong một khoảng đã cho.
print(np.round(ci, 3).tolist())
```

**Kết quả khi chạy:**

```text
[1.761, 3.839]
```

Khoảng ước lượng mean theo t từ khoảng 1,761 đến 3,839 ngày; đây là khoảng cho trung bình quần thể.

## 5. Năm tình huống suy luận thống kê — từ kiểm định một mẫu đến Welch hai nhóm

### Tình huống 1 — Cấp 1: Kiểm định trung bình 10 bài thi so với mốc 50

**Từ vựng trong mục:** **Null hypothesis** — giả thuyết H₀; **p-value** — giá trị p; **Two-sided t-test** — kiểm định hai phía.

**Tình huống thực tế:** Giảng viên có **10 bài kiểm tra**, mỗi bài một điểm **trên thang 100**; điểm đều quanh 50. Nhà trường đưa **mốc tham khảo 50 điểm** và muốn xem số liệu có cho bằng chứng rằng **điểm trung bình của nhóm học viên tương tự khác 50** hay không. Nhóm dùng **kiểm định t hai phía** với ngưỡng quyết định **5%**, chứ không tìm cách chứng minh mốc 50 chắc chắn đúng.

**Vì sao chọn cách này?** **Giả thuyết không H₀** là mốc đang được thử, ở đây trung bình quần thể bằng **50 điểm**; **H₁ hai phía** là trung bình **khác 50**, có thể cao hơn hoặc thấp hơn. `ttest_1samp` dùng **10 điểm mẫu**, mức trung bình và độ phân tán của chúng để tính **p-value**: mức độ bất thường của kết quả như quan sát **nếu H₀ đúng**. So p-value với **α = 0,05** để quyết định có **bác bỏ H₀** hay chưa; p lớn không chứng minh H₀ chắc chắn đúng, và p nhỏ **không phải xác suất H₀ sai**. Với mẫu nhỏ cần xem giả định các điểm đủ độc lập và phân phối phù hợp.

**Quy trình:**
1. Ghi 10 điểm có cùng thang đo.
2. Dùng `ttest_1samp` với mốc 50 và kiểm định hai phía.
3. So p với α=0,05 và phát biểu 'không bác bỏ' hoặc 'bác bỏ', không gọi là chứng minh H₀.

**No Note — Không chú thích**

```python
from scipy.stats import ttest_1samp
scores = [48,49,50,51,52,48,49,50,51,52]
result = ttest_1samp(scores, popmean=50)
if len(scores) != 10:
    raise ValueError("Cần đúng 10 điểm học viên.")
print("Học viên:", len(scores))
print(f"Mean (điểm): {sum(scores)/len(scores):.2f}")
print(f"p-value: {result.pvalue:.4f}")
print("Bác bỏ H0 ở 0.05:", bool(result.pvalue < 0.05))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: So p-value kiểm định t của 10 điểm với ngưỡng ý nghĩa alpha=0.05.
# Dữ liệu: 10 điểm học viên quanh 50, giả thuyết trung bình tổng thể=50, kiểm hai phía.
# Kiểm định t một mẫu của SciPy trả statistic và pvalue.
from scipy.stats import ttest_1samp
# 10 điểm học viên, mỗi số một quan sát.
scores = [48,49,50,51,52,48,49,50,51,52]
# popmean=50 là mốc H0; mặc định hai phía, yêu cầu diễn giải dựa giả định phép t-test.
result = ttest_1samp(scores, popmean=50)
# len() đếm 10 quan sát trước khi kiểm định.
if len(scores) != 10:
    # ValueError ngừng xử lý nếu số người khác 10.
    raise ValueError("Cần đúng 10 điểm học viên.")
# len() đếm 10 quan sát trước khi kiểm định.
print("Học viên:", len(scores))
# len() đếm 10 quan sát trước khi kiểm định.
# Tổng điểm chia số học viên tính mean MẪU, khác mean=50 của H0.
print(f"Mean (điểm): {sum(scores)/len(scores):.2f}")
# pvalue biểu thị mức bất thường dưới H0, không phải xác suất H0 sai hay đúng.
print(f"p-value: {result.pvalue:.4f}")
# pvalue biểu thị mức bất thường dưới H0, không phải xác suất H0 sai hay đúng.
# So p với ngưỡng alpha=5%; True nghĩa bác bỏ H0 theo quy tắc đặt trước, False nghĩa chưa đủ bằng chứng bác bỏ (không chứng minh H0 đúng).
# bool() ép kết luận thành Boolean Python để print().
print("Bác bỏ H0 ở 0.05:", bool(result.pvalue < 0.05))
```

**Kết quả khi chạy:**

```text
Học viên: 10
Mean (điểm): 50.00
p-value: 1.0000
Bác bỏ H0 ở 0.05: False
```

p-value lớn không chứng minh mean quần thể **chính xác** 50; chỉ là bộ dữ liệu này chưa cung cấp bằng chứng để bác bỏ.

### Tình huống 2 — Cấp 2: Khoảng tin cậy t cho 12 thời gian giao hàng

**Từ vựng trong mục:** **Confidence interval** — khoảng tin cậy; **Standard error** — sai số chuẩn.

**Tình huống thực tế:** Đơn vị giao hàng ghi **12 thời gian giao**, tính bằng **ngày**, đa số từ 2,7 tới 3,3 ngày. Người quản lý muốn ước lượng **thời gian giao trung bình của nhiều chuyến tương tự** và mức bất định của con số ấy, nên yêu cầu **khoảng tin cậy 95%** cho **trung bình**, cùng số trung bình và sai số chuẩn. Họ không hỏi khoảng mà 95% **chuyến riêng lẻ** sẽ nằm trong đó.

**Vì sao chọn cách này?** **Khoảng tin cậy (CI)** ở đây nhằm ước lượng **trung bình quần thể**, không phải dự đoán thời gian của từng chuyến. Vì chỉ có **12 chuyến** và chưa biết độ lệch chuẩn quần thể, bài dùng **phân phối t** với **11 bậc tự do**, dựa trên độ phân tán mẫu. `sem(values)` tính **SE**, tức mức bất định của trung bình ước lượng, còn `t.interval(0.95, ...)` dựng khoảng hai phía quanh mean mẫu với mức 95%. Diễn giải theo **phương pháp lặp lại lấy mẫu**, khoảng được tạo bằng cách này có mục tiêu bao phủ trung bình thật trong 95% lần khi giả định đúng; không nói mỗi chuyến riêng lẻ có 95% khả năng nằm trong khoảng này.

**Quy trình:**
1. Tạo đủ 12 thời gian theo cùng đơn vị ngày.
2. Tính mean, SE bằng `sem`, khoảng t 95% với df=11.
3. In hai đầu khoảng và ý nghĩa cho trung bình.

**No Note — Không chú thích**

```python
import numpy as np
from scipy.stats import t, sem
values = np.array([2.8,3,2.9,3.1,3.2,2.7,3,2.8,3.1,2.9,3,3.3], dtype=float)
se = sem(values)
ci = t.interval(0.95, df=len(values)-1, loc=values.mean(), scale=se)
if len(values) != 12:
    raise ValueError("Cần 12 lượt đo thời gian giao.")
print("Chuyến:", len(values))
print(f"Mean (ngày): {values.mean():.3f}")
print(f"SE (ngày): {se:.3f}")
print(f"CI 95% (ngày): {ci[0]:.3f} – {ci[1]:.3f}")
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tính SE và CI 95% của thời gian giao trên 12 chuyến, dùng df=11.
# Dữ liệu: 12 số ngày giao (2.7..3.3), giả định quan sát độc lập và mean tổng thể chưa biết.
# NumPy array/mean() giữ thời gian kiểu số thực.
import numpy as np
# sem() cho SE của mean, t.interval() dùng Student t để dựng CI.
from scipy.stats import t, sem
# 12 ngày giao tính theo ngày, dtype=float để giữ số thập phân.
values = np.array([2.8,3,2.9,3.1,3.2,2.7,3,2.8,3.1,2.9,3,3.3], dtype=float)
# sem(values) mặc định ddof=1 (SD mẫu), rồi chia √n để ước lượng sai số chuẩn của mean.
se = sem(values)
# Khoảng hai phía mức tin cậy 95%; df=11; loc=mean ngày; scale=SE ngày, không phải độ lệch chuẩn các chuyến.
# len() đếm 12 chuyến, df lấy n−1.
# Mean thời gian của 12 chuyến, đơn vị ngày.
ci = t.interval(0.95, df=len(values)-1, loc=values.mean(), scale=se)
# len() đếm 12 chuyến, df lấy n−1.
if len(values) != 12:
    # Dừng khi số chuyến không bằng 12.
    raise ValueError("Cần 12 lượt đo thời gian giao.")
# len() đếm 12 chuyến, df lấy n−1.
print("Chuyến:", len(values))
# Mean thời gian của 12 chuyến, đơn vị ngày.
print(f"Mean (ngày): {values.mean():.3f}")
# f-string :.3f hiển thị sai số chuẩn ba chữ số thập phân (ngày).
print(f"SE (ngày): {se:.3f}")
# [0] là cận dưới của tuple CI, [1] là cận trên; :.3f định dạng khi in.
print(f"CI 95% (ngày): {ci[0]:.3f} – {ci[1]:.3f}")
```

**Kết quả khi chạy:**

```text
Chuyến: 12
Mean (ngày): 2.983
SE (ngày): 0.051
CI 95% (ngày): 2.872 – 3.094
```

Ý nghĩa 95% gắn với **quy trình lặp lấy mẫu tạo khoảng**, không diễn giải thành xác suất 95% cho tham số cố định nằm trong một khoảng đã có.

### Tình huống 3 — Cấp 3: Kiểm độ nhạy của kiểm định t với điểm ngoại lệ trong 15 mẫu

**Từ vựng trong mục:** **Outlier sensitivity** — nhạy với ngoại lệ; **Robust review** — rà soát chắc chắn.

**Tình huống thực tế:** Trung tâm khảo thí có **15 điểm bài kiểm tra trên thang 100**. **14 điểm quanh 49–51**, nhưng một bài được **70 điểm**, có thể là thành tích thật hoặc cần kiểm tra cách nhập. Nhóm muốn kiểm định trung bình có khác **mốc 50** không bằng đủ 15 bài, rồi thử tính thêm kết quả trên **14 bài đầu** để biết con số 70 ảnh hưởng kết luận thế nào. Bản gốc 15 bài vẫn phải được giữ nguyên.

**Vì sao chọn cách này?** **Kiểm tra độ nhạy** hỏi rằng kết quả phân tích **thay đổi bao nhiêu nếu một quan sát đặc biệt được xem riêng**. `ttest_1samp(scores, 50)` tính kiểm định hai phía trên **đủ 15 bài**, còn `scores[:-1]` tạo dữ liệu làm việc **14 bài đầu** để thử một phép so sánh phụ. Điểm 70 ảnh hưởng **cả trung bình và độ phân tán**, nên p-value có thể thay đổi, nhưng điểm 70 chưa phải nhập sai. Phải **giữ báo cáo chính của 15 bài**, giải thích lý do phân tích phụ và không chỉ công bố p-value mình thích; nếu cố xóa điểm cao để đạt ngưỡng, kết luận có thể bị thiên lệch.

**Quy trình:**
1. Lưu 15 điểm, chạy t-test đầy đủ.
2. Làm bản so sánh chỉ 14 điểm còn lại, không sửa dữ liệu gốc.
3. In mean và p của hai cách tính, báo lại số mẫu.

**No Note — Không chú thích**

```python
import numpy as np
from scipy.stats import ttest_1samp
scores = np.array([49,50,50,51,49,50,51,50,49,50,51,50,50,49,70], dtype=float)
full = ttest_1samp(scores, 50)
without_last = ttest_1samp(scores[:-1], 50)
if len(scores) != 15:
    raise ValueError("Cần 15 học viên khi so tác động ngoại lệ.")
print("Học viên:", len(scores))
print(f"Mean đủ 15: {scores.mean():.3f}")
print(f"p đủ 15: {full.pvalue:.3f}")
print(f"p khi tạm xem 14: {without_last.pvalue:.3f}")
print("Vẫn giữ bản gốc:", len(scores) == 15)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: So tác động một điểm ngoại lệ lên kiểm định t khi xét 15 điểm rồi tạm bỏ điểm cuối.
# Dữ liệu: 15 học viên, điểm cuối 70 cao bất thường; nhóm 14 là thử độ nhạy, không được xóa dữ liệu gốc.
# NumPy tạo mảng và tính mean mẫu.
import numpy as np
# SciPy tính t-test một mẫu so với mốc H0.
from scipy.stats import ttest_1samp
# 15 điểm, trong đó điểm cuối 70 là giá trị ngoại lệ có thể ảnh hưởng cả mean và SD.
scores = np.array([49,50,50,51,49,50,51,50,49,50,51,50,50,49,70], dtype=float)
# Dùng popmean=50 theo vị trí thứ hai của hàm; mặc định alternative='two-sided'.
full = ttest_1samp(scores, 50)
# Slice [:-1] bỏ CHỈ phần tử cuối trong một view tạm gồm 14 điểm, mảng scores gốc vẫn có 15 điểm.
without_last = ttest_1samp(scores[:-1], 50)
# len() kiểm bảng gốc vẫn 15 học viên để không nhầm bản thử 14 là dữ liệu mới.
if len(scores) != 15:
    # Báo lỗi nếu thiếu dữ liệu ngoại lệ/không đủ học viên.
    raise ValueError("Cần 15 học viên khi so tác động ngoại lệ.")
# len() kiểm bảng gốc vẫn 15 học viên để không nhầm bản thử 14 là dữ liệu mới.
print("Học viên:", len(scores))
# Mean của toàn bộ 15 điểm, có thể bị điểm 70 kéo lên.
print(f"Mean đủ 15: {scores.mean():.3f}")
# p-value hai phía của toàn bộ 15 điểm; việc ngoại lệ thay mean và phương sai có thể thay p không theo chiều đơn giản.
print(f"p đủ 15: {full.pvalue:.3f}")
# p-value của 14 điểm khi tạm loại giá trị cuối để minh họa độ nhạy; không tự động hợp thức hóa việc loại dữ liệu.
print(f"p khi tạm xem 14: {without_last.pvalue:.3f}")
# len() kiểm bảng gốc vẫn 15 học viên để không nhầm bản thử 14 là dữ liệu mới.
print("Vẫn giữ bản gốc:", len(scores) == 15)
```

**Kết quả khi chạy:**

```text
Học viên: 15
Mean đủ 15: 51.267
p đủ 15: 0.364
p khi tạm xem 14: 0.720
Vẫn giữ bản gốc: True
```

Cùng bộ dữ liệu nhưng lựa chọn quan sát đem vào kiểm định có thể đổi p-value; việc loại mẫu phải có lý do dữ liệu minh bạch.

### Tình huống 4 — Cấp 4: Một p-value nhưng hai quyết định alpha từ 18 kết quả

**Từ vựng trong mục:** **Significance level** — mức ý nghĩa α; **Decision rule** — quy tắc quyết định.

**Tình huống thực tế:** Phòng đào tạo có **18 điểm kiểm tra thang 100**, mỗi điểm thuộc một học viên. Giảng viên đang kiểm **trung bình điểm có khác mốc 50** hay không. Nhóm phải xem **cùng một p-value** với hai mức ý nghĩa **0,05 (5%)** và **0,01 (1%)**, để hiểu vì sao mức yêu cầu bằng chứng khắt khe hơn có thể đưa tới quyết định khác dù dữ liệu không đổi.

**Vì sao chọn cách này?** **Mức ý nghĩa α** là ngưỡng nhóm nghiên cứu **đặt trước khi xem kết quả kiểm định**, biểu thị mức chấp nhận nguy cơ **bác bỏ H₀ khi H₀ thật sự đúng** theo quy trình. **p-value** được tính từ **18 điểm dữ liệu và cùng một kiểm định t hai phía**, nên **không đổi** khi chỉ đổi ngưỡng. Nếu p nằm giữa **0,01 và 0,05**, nó đủ nhỏ để bác bỏ ở 5% nhưng **chưa đủ nhỏ** để bác bỏ ở 1%. Hai quyết định không mâu thuẫn vì dùng **tiêu chuẩn bằng chứng khác nhau**; không chọn ngưỡng sau khi nhìn p-value để đạt kết luận thuận ý.

**Quy trình:**
1. Tạo 18 điểm và chạy kiểm định hai phía một mẫu.
2. Tính p một lần rồi so với cả hai α.
3. Báo quyết định ở từng ngưỡng và nhắc đây là bằng chứng, không phải xác suất H₀ đúng.

**No Note — Không chú thích**

```python
from scipy.stats import ttest_1samp
scores = [48,50,51,52,53,51,50,49,52,53,51,50,52,49,51,52,50,53]
p = float(ttest_1samp(scores, popmean=50).pvalue)
if len(scores) != 18:
    raise ValueError("Cần 18 điểm học viên khi so mức ý nghĩa.")
print("Học viên:", len(scores))
print(f"p-value: {p:.4f}")
print("Bác bỏ H0 ở 0.05:", p < 0.05)
print("Bác bỏ H0 ở 0.01:", p < 0.01)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: So cùng một p-value ở alpha=0.05 và alpha=0.01 để thấy ngưỡng quyết định khác nhau.
# Dữ liệu: 18 điểm học viên, H0 mean=50, alpha 5% và 1% do người nghiên cứu quyết định trước.
# ttest_1samp tính p-value hai phía so mean mẫu với mốc 50.
from scipy.stats import ttest_1samp
# 18 điểm cùng thang, mỗi số một học viên.
scores = [48,50,51,52,53,51,50,49,52,53,51,50,52,49,51,52,50,53]
# popmean=50 là giá trị H0, mặc định kiểm hai phía.
# Lấy pvalue từ kết quả t-test, không phải posterior của H0.
# float() đổi scalar p-value sang số Python.
p = float(ttest_1samp(scores, popmean=50).pvalue)
# len() xác minh 18 điểm trước khi kết luận.
if len(scores) != 18:
    # Dừng nếu thiếu số mẫu theo yêu cầu.
    raise ValueError("Cần 18 điểm học viên khi so mức ý nghĩa.")
# len() xác minh 18 điểm trước khi kết luận.
print("Học viên:", len(scores))
# p-value hiển thị 4 số thập phân, quyết định dùng giá trị p gốc không làm tròn.
print(f"p-value: {p:.4f}")
# Với alpha=0.05: bác bỏ H0 nếu p nhỏ hơn 0.05; ngưỡng cao hơn dễ bác bỏ hơn.
print("Bác bỏ H0 ở 0.05:", p < 0.05)
# Với alpha=0.01: cần bằng chứng mạnh hơn (p nhỏ hơn 0.01); dùng CÙNG p, không chạy kiểm định khác.
print("Bác bỏ H0 ở 0.01:", p < 0.01)
```

**Kết quả khi chạy:**

```text
Học viên: 18
p-value: 0.0146
Bác bỏ H0 ở 0.05: True
Bác bỏ H0 ở 0.01: False
```

Chưa bác bỏ ở α=0,01 **không đồng nghĩa** chứng minh H₀ đúng; điều đó chỉ phản ánh ngưỡng bằng chứng khắt khe hơn.

### Tình huống 5 — Cấp 5: So hai nhóm 10+10 bằng Welch t-test và CI chênh lệch

**Từ vựng trong mục:** **Welch t-test** — kiểm định hai mẫu không cần giả định phương sai bằng nhau; **Difference CI** — khoảng chênh lệch mean.

**Tình huống thực tế:** Trung tâm tổ chức kiểm tra kỹ năng cho **20 học viên**, chia **hai nhóm độc lập A và B, mỗi nhóm 10 người**, điểm trên thang **100**. Nhóm B có điểm nhìn chung cao hơn A. Người đánh giá muốn biết **trung bình B cao hơn A bao nhiêu điểm**, kiểm định liệu trung bình của hai nhóm quần thể có thể khác nhau hay không và lập **khoảng tin cậy 95% cho chênh lệch B trừ A**. Hai nhóm là những người khác nhau, không phải một người làm bài trước rồi làm lại.

**Vì sao chọn cách này?** **Hai mẫu độc lập** nghĩa là mỗi học viên thuộc **A hoặc B**, không có ghép cặp cùng người; vì vậy không dùng kiểm định cặp trước–sau. `ttest_ind(B, A, equal_var=False)` thực hiện **Welch t-test**, kiểm trung bình quần thể hai nhóm mà **không buộc phương sai bằng nhau**. Chương trình tính **chênh lệch trung bình B–A**, rồi **SE cho hiệu** từ độ phân tán và số người của cả hai nhóm, cùng **bậc tự do Welch** để dựng **CI 95% cho hiệu trung bình**. Khoảng không chứa **0** là bằng chứng chênh lệch theo mức tin cậy đang xét; nó **không phải khoảng chứa điểm của 95% học viên** và cũng không chứng minh nhóm B tốt hơn vì một nguyên nhân cụ thể.

**Quy trình:**
1. Tạo hai nhóm 10 điểm, kiểm không trộn thứ tự giữa nhóm.
2. Chạy `ttest_ind(..., equal_var=False)` và tính SE hiệu mean.
3. Tạo khoảng t Welch 95% cho B–A, báo chênh lệch, p và hai đầu khoảng.

**No Note — Không chú thích**

```python
import numpy as np
from scipy.stats import ttest_ind, t
A = np.array([45,47,46,49,48,47,46,50,49,48], dtype=float)
B = np.array([50,52,51,54,53,52,51,55,54,53], dtype=float)
result = ttest_ind(B, A, equal_var=False)
va = A.var(ddof=1)/len(A)
vb = B.var(ddof=1)/len(B)
se = np.sqrt(va + vb)
df = (va+vb)**2/(va**2/(len(A)-1)+vb**2/(len(B)-1))
difference = B.mean()-A.mean()
ci = t.interval(0.95, df=df, loc=difference, scale=se)
if len(A) + len(B) != 20:
    raise ValueError("Cần đủ 20 học viên chia hai nhóm.")
print("Học viên:", len(A)+len(B))
print("Nhóm A/B:", len(A), len(B))
print(f"Chênh lệch B-A (điểm): {difference:.2f}")
print(f"p-value: {result.pvalue:.6f}")
print(f"CI 95% (điểm): {ci[0]:.3f} – {ci[1]:.3f}")
print("CI không chứa 0:", not (ci[0] <= 0 <= ci[1]))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Dùng Welch t-test so mean hai nhóm 10 người và tính khoảng tin cậy cho chênh lệch B-A.
# Dữ liệu: Nhóm A/B mỗi nhóm 10 điểm; quan tâm chênh lệch trung bình điểm B trừ A, không giả định hai nhóm có cùng phương sai.
# NumPy tính mean, var, sqrt và số mẫu cho hai nhóm.
import numpy as np
# ttest_ind() so hai nhóm độc lập, t.interval() xây CI từ trung bình, SE và bậc tự do.
from scipy.stats import ttest_ind, t
# 10 điểm nhóm A, dtype=float giữ số liệu số thực.
A = np.array([45,47,46,49,48,47,46,50,49,48], dtype=float)
# 10 điểm nhóm B, cùng thang với A; giả định hai nhóm độc lập.
B = np.array([50,52,51,54,53,52,51,55,54,53], dtype=float)
# Welch t-test: equal_var=False KHÔNG áp giả định phương sai hai nhóm bằng nhau; B trước A để chênh theo chiều B−A; mặc định kiểm hai phía.
result = ttest_ind(B, A, equal_var=False)
# ddof=1 lấy phương sai mẫu (chia nA−1); chia tiếp số người nA tạo phần đóng góp vào phương sai của hiệu mean.
va = A.var(ddof=1)/len(A)
# Phương sai mẫu B /nB là phần đóng góp riêng, không trộn hai nhóm bằng một phương sai chung.
vb = B.var(ddof=1)/len(B)
# sqrt(va+vb) là standard error của hiệu trung bình hai nhóm ĐỘC LẬP.
se = np.sqrt(va + vb)
# Công thức Welch–Satterthwaite cho bậc tự do hiệu dụng, có thể không nguyên; khác nA+nB−2 khi giả phương sai bằng nhau.
df = (va+vb)**2/(va**2/(len(A)-1)+vb**2/(len(B)-1))
# difference tính điểm trung bình nhóm B trừ A, dấu dương nghĩa B cao hơn A.
difference = B.mean()-A.mean()
# CI hai phía 95% dùng Student t, df Welch, loc=ước lượng B−A, scale=SE của chênh lệch, đơn vị điểm.
ci = t.interval(0.95, df=df, loc=difference, scale=se)
# Xác minh có 20 học viên ở hai nhóm, mỗi người chỉ thuộc một nhóm theo giả định.
if len(A) + len(B) != 20:
    # Báo thiếu số mẫu để tránh so hai nhóm không đúng kích thước.
    raise ValueError("Cần đủ 20 học viên chia hai nhóm.")
print("Học viên:", len(A)+len(B))
print("Nhóm A/B:", len(A), len(B))
print(f"Chênh lệch B-A (điểm): {difference:.2f}")
# p-value Welch kiểm H0 hai nhóm có mean bằng nhau, không phải xác suất H0 đúng.
print(f"p-value: {result.pvalue:.6f}")
# [0] và [1] là cận dưới/trên CI, in ba chữ số thập phân.
print(f"CI 95% (điểm): {ci[0]:.3f} – {ci[1]:.3f}")
# [0] và [1] là cận dưới/trên CI, in ba chữ số thập phân.
# Kiểm số 0 (không chênh lệch) nằm trong khoảng; not đảo để báo CI không chứa 0, tương ứng bác bỏ ở mức 0.05 cho kiểm hai phía theo giả định chuẩn.
print("CI không chứa 0:", not (ci[0] <= 0 <= ci[1]))
```

**Kết quả khi chạy:**

```text
Học viên: 20
Nhóm A/B: 10 10
Chênh lệch B-A (điểm): 5.00
p-value: 0.000001
CI 95% (điểm): 3.514 – 6.486
CI không chứa 0: True
```

Chênh lệch nhóm trong mẫu có thể do nhiều yếu tố khác ngoài cách dạy; kiểm định không tự chứng minh tác động nhân quả.

## 6. Sai lầm thường gặp

- p-value không phải xác suất H₀ đúng; nó là xác suất của kết quả cực đoan dưới giả định H₀.
- Không bác bỏ H₀ **không** đồng nghĩa chấp nhận hay chứng minh H₀ đúng.
- α=0.05 là ngưỡng kiểm định lựa chọn trước, không phải ngưỡng hiệu quả thực tế.
- CI 95% có **tỷ lệ bao phủ dài hạn 95%** khi lặp quy trình, không phải xác suất 95% tham số cố định trong một khoảng đã quan sát.
- SE khác SD: SE nói về bất định của mean, SD nói về số đo riêng lẻ.
- T-test trên mẫu nhỏ nhạy với ngoại lệ/phụ thuộc; cần xem giả định và thiết kế lấy mẫu.

## 7. Trắc nghiệm

**Q1. What is H0? | H₀ là gì?**

A. A null hypothesis subjected to statistical testing | Giả thuyết không được đem kiểm định

B. An interval from a procedure with 95% long-run coverage | Khoảng từ quy trình có mức bao phủ dài hạn 95%

C. Probability of equally or more extreme test results under H0 | Xác suất thống kê cực đoan bằng hoặc hơn khi H₀ đúng

D. Test a population mean against a specified value | Kiểm định trung bình quần thể với một mốc

**Đáp án: A**

**Giải thích:** Đó là giả định gốc của kiểm định. Ví dụ H₀: μ=50 nói về mean quần thể; không đòi mean mẫu quan sát phải đúng 50.


**Q2. What does p-value mean? | p-value nghĩa là gì?**

A. Probability of equally or more extreme test results under H0 | Xác suất thống kê cực đoan bằng hoặc hơn khi H₀ đúng

B. Test a population mean against a specified value | Kiểm định trung bình quần thể với một mốc

C. An interval from a procedure with 95% long-run coverage | Khoảng từ quy trình có mức bao phủ dài hạn 95%

D. A null hypothesis subjected to statistical testing | Giả thuyết không được đem kiểm định

**Đáp án: A**

**Giải thích:** Nó được tính với điều kiện mô hình H₀ đúng. p-value được tính từ thống kê kiểm định và phân phối dưới H₀, chứ không trực tiếp gán xác suất cho H₀.


**Q3. What is a one-sample t-test for? | T-test một mẫu dùng để làm gì?**

A. A null hypothesis subjected to statistical testing | Giả thuyết không được đem kiểm định

B. Test a population mean against a specified value | Kiểm định trung bình quần thể với một mốc

C. Probability of equally or more extreme test results under H0 | Xác suất thống kê cực đoan bằng hoặc hơn khi H₀ đúng

D. An interval from a procedure with 95% long-run coverage | Khoảng từ quy trình có mức bao phủ dài hạn 95%

**Đáp án: B**

**Giải thích:** Nó dùng trung bình và ước lượng phương sai mẫu. Khác kiểm định hai mẫu, t-test một mẫu so trung bình một mẫu với mốc cố định.


**Q4. What is a 95% confidence interval? | Khoảng tin cậy 95% là gì?**

A. A null hypothesis subjected to statistical testing | Giả thuyết không được đem kiểm định

B. Test a population mean against a specified value | Kiểm định trung bình quần thể với một mốc

C. An interval from a procedure with 95% long-run coverage | Khoảng từ quy trình có mức bao phủ dài hạn 95%

D. Probability of equally or more extreme test results under H0 | Xác suất thống kê cực đoan bằng hoặc hơn khi H₀ đúng

**Đáp án: C**

**Giải thích:** Bao phủ được hiểu qua những lần lấy mẫu lặp. Mức bao phủ 95% thuộc quy trình qua nhiều mẫu; một CI đã tính cần báo hai đầu mút và giả định đi kèm.


**Q5. A hypothesis test has p-value = 0.03 and significance level α = 0.05. What is the usual decision? | Kiểm định có p-value = 0.03 và mức ý nghĩa α = 0.05. Thường đưa ra quyết định nào?**

A. Set p-value to zero | Đặt p-value bằng 0

B. Accept H0 as proven | Chứng minh H0 đúng

C. Double the sample size automatically | Tự động tăng gấp đôi mẫu

D. Reject H0 | Bác bỏ H0

**Đáp án: D**

**Giải thích:** Vì 0.03 < 0.05, dữ liệu đủ bằng chứng để bác bỏ H0 ở mức ý nghĩa đã chọn; không chứng minh H1 chắc chắn đúng.


**Q6. A hypothesis test has p-value = 0.15 and α = 0.05. Which statement is appropriate? | Kiểm định có p-value = 0.15 và α = 0.05. Phát biểu nào phù hợp?**

A. Reject H0 | Bác bỏ H0

B. H0 is proven true | H0 đã được chứng minh đúng

C. Fail to reject H0 | Chưa đủ bằng chứng để bác bỏ H0

D. The sample mean must equal zero | Trung bình mẫu phải bằng 0

**Đáp án: C**

**Giải thích:** 0.15 ≥ 0.05 nên chưa đủ bằng chứng bác bỏ H0. Điều này không có nghĩa đã chứng minh H0 đúng.


**Q7. A 95% two-sided confidence interval contains the null value. What normally happens in the matching two-sided test at α = 0.05? | Khoảng tin cậy 95% hai phía chứa giá trị giả thuyết H0. Trong kiểm định hai phía tương ứng với α = 0.05, thường kết luận gì?**

A. H0 is definitely true | H0 chắc chắn đúng

B. Reject H0 | Bác bỏ H0

C. Fail to reject H0 | Chưa bác bỏ H0

D. The p-value is exactly 0 | p-value chính xác bằng 0

**Đáp án: C**

**Giải thích:** Với cùng mô hình và giả định, khi giá trị H0 nằm trong khoảng tin cậy 95% thì kiểm định hai phía tương ứng ở mức 5% không bác bỏ H0.


**Q8. Which description of a p-value is correct? | Mô tả nào đúng về p-value?**

A. Probability of observing results this extreme or more if H0 were true | Xác suất gặp kết quả cực đoan bằng hoặc hơn nếu H0 đúng

B. Probability H0 is true | Xác suất H0 đúng

C. Probability H1 is true | Xác suất H1 đúng

D. Probability the data were measured correctly | Xác suất dữ liệu được đo đúng

**Đáp án: A**

**Giải thích:** p-value xét mức độ bất thường của dữ liệu theo giả định H0 đúng, không phải xác suất H0 đúng.


**Q9. How is a one-sample t statistic formed? | Thống kê t một mẫu có dạng gì?**

A. n−1 | n−1

B. Lower and upper endpoints of a t interval | Hai đầu dưới/trên của khoảng t

C. (sample mean−mu0)/SE | (mean mẫu−mu0)/SE

D. Standard error of the mean | Sai số chuẩn của trung bình

**Đáp án: C**

**Giải thích:** Nó chuẩn hóa độ lệch của mean so với mốc. Chênh hai điểm chỉ có ý nghĩa kiểm định khi so với độ bất định lấy mẫu của mean.


**Q10. What does `scipy.stats.sem` estimate? | `scipy.stats.sem` ước lượng gì?**

A. n−1 | n−1

B. Lower and upper endpoints of a t interval | Hai đầu dưới/trên của khoảng t

C. (sample mean−mu0)/SE | (mean mẫu−mu0)/SE

D. Standard error of the mean | Sai số chuẩn của trung bình

**Đáp án: D**

**Giải thích:** Nó ước lượng độ dao động của mean mẫu. SE có xu hướng giảm khi n tăng dưới giả định phù hợp, còn SD của từng điểm không nhất thiết giảm.


**Q11. What does t.interval return? | t.interval trả gì?**

A. Lower and upper endpoints of a t interval | Hai đầu dưới/trên của khoảng t

B. (sample mean−mu0)/SE | (mean mẫu−mu0)/SE

C. Standard error of the mean | Sai số chuẩn của trung bình

D. n−1 | n−1

**Đáp án: A**

**Giải thích:** Khoảng phụ thuộc mức tin cậy, df, vị trí và độ rộng. Scale lớn làm khoảng rộng; loc là ước lượng trung tâm chứ không phải phần trăm tin cậy.


**Q12. What degrees of freedom are usual for one-sample t inference? | Bậc tự do thông dụng của t một mẫu là gì?**

A. n−1 | n−1

B. (sample mean−mu0)/SE | (mean mẫu−mu0)/SE

C. Lower and upper endpoints of a t interval | Hai đầu dưới/trên của khoảng t

D. Standard error of the mean | Sai số chuẩn của trung bình

**Đáp án: A**

**Giải thích:** Ước lượng phương sai mẫu làm mất một bậc tự do. Thống kê t ước lượng phương sai từ mẫu nên thường còn n−1 bậc tự do.


**Q13. Is p-value equal to P(H0 is true)? | p-value có bằng P(H₀ đúng) không?**

A. No; p is conditional on H0 | Không; p được tính khi giả định H₀ đúng

B. Failing to reject a false H0 | Không bác bỏ H₀ khi H₀ sai

C. It does not reject at the matching alpha | Không bác bỏ với alpha tương ứng

D. Rejecting a true null hypothesis | Bác bỏ H₀ khi H₀ thực sự đúng

**Đáp án: A**

**Giải thích:** p theo tần suất không phải posterior. Nhầm p với P(H₀|dữ liệu) là đảo chiều điều kiện; kiểm định tần suất xét mức cực đoan của dữ liệu khi H₀ đúng.


**Q14. If a confidence interval covers a null value, what often happens in a matching two-sided test? | Nếu CI chứa mốc H₀ thì kiểm định hai phía tương ứng thường thế nào?**

A. Rejecting a true null hypothesis | Bác bỏ H₀ khi H₀ thực sự đúng

B. No; p is conditional on H0 | Không; p được tính khi giả định H₀ đúng

C. Failing to reject a false H0 | Không bác bỏ H₀ khi H₀ sai

D. It does not reject at the matching alpha | Không bác bỏ với alpha tương ứng

**Đáp án: D**

**Giải thích:** Các quy trình tương ứng thường thống nhất dưới cùng giả định. Sự tương ứng cần kiểm định hai phía, mức tin cậy và giả định phù hợp; không đúng với mọi loại kiểm định và khoảng.


**Q15. What is a type I error? | Sai lầm loại I là gì?**

A. Rejecting a true null hypothesis | Bác bỏ H₀ khi H₀ thực sự đúng

B. No; p is conditional on H0 | Không; p được tính khi giả định H₀ đúng

C. Failing to reject a false H0 | Không bác bỏ H₀ khi H₀ sai

D. It does not reject at the matching alpha | Không bác bỏ với alpha tương ứng

**Đáp án: A**

**Giải thích:** Alpha kiểm soát lỗi loại I dưới giả định kiểm định. Sai lầm loại I là báo dương sai; alpha được chọn trước để kiểm soát xác suất lỗi này dưới giả định H₀.


**Q16. What is a type II error? | Sai lầm loại II là gì?**

A. It does not reject at the matching alpha | Không bác bỏ với alpha tương ứng

B. Rejecting a true null hypothesis | Bác bỏ H₀ khi H₀ thực sự đúng

C. No; p is conditional on H0 | Không; p được tính khi giả định H₀ đúng

D. Failing to reject a false H0 | Không bác bỏ H₀ khi H₀ sai

**Đáp án: D**

**Giải thích:** Nó khác lỗi bác bỏ H₀ đúng. Power bằng một trừ xác suất sai lầm loại II dưới giả thuyết đối cụ thể, liên quan đến thiết kế cỡ mẫu.


**Q17. Does a 95% CI say the fixed parameter has 95% probability of lying in this realized interval? | CI 95% có nghĩa xác suất tham số cố định trong khoảng đã tính là 95%?**

A. No; 95% describes repeated-interval coverage | Không; 95% mô tả tỷ lệ bao phủ khi lặp

B. No; effect size and context still matter | Không; còn kích thước tác động và bối cảnh

C. Strong dependence or problematic extreme data in small samples | Phụ thuộc mạnh hoặc dữ liệu cực đoan trong mẫu nhỏ

D. It becomes wider | Trở nên rộng hơn

**Đáp án: A**

**Giải thích:** Trong diễn giải tần suất, tham số cố định và khoảng thay đổi theo mẫu. Phát biểu xác suất áp dụng cho quy trình tạo khoảng ngẫu nhiên trước lấy mẫu, không phải μ cố định sau khi quan sát một CI.


**Q18. What can violate simple t-test assumptions? | Điều gì có thể vi phạm giả định t-test đơn giản?**

A. No; 95% describes repeated-interval coverage | Không; 95% mô tả tỷ lệ bao phủ khi lặp

B. No; effect size and context still matter | Không; còn kích thước tác động và bối cảnh

C. It becomes wider | Trở nên rộng hơn

D. Strong dependence or problematic extreme data in small samples | Phụ thuộc mạnh hoặc dữ liệu cực đoan trong mẫu nhỏ

**Đáp án: D**

**Giải thích:** Suy luận cần mô hình lấy mẫu phù hợp. Mẫu rất nhỏ, ngoại lệ nặng hoặc phụ thuộc có thể khiến p-value và CI báo ra thiếu tin cậy.


**Q19. What happens to CI width if SE grows with other inputs fixed? | SE tăng khi yếu tố khác giữ nguyên thì CI rộng ra sao?**

A. Strong dependence or problematic extreme data in small samples | Phụ thuộc mạnh hoặc dữ liệu cực đoan trong mẫu nhỏ

B. No; 95% describes repeated-interval coverage | Không; 95% mô tả tỷ lệ bao phủ khi lặp

C. No; effect size and context still matter | Không; còn kích thước tác động và bối cảnh

D. It becomes wider | Trở nên rộng hơn

**Đáp án: D**

**Giải thích:** Bất định cao làm khoảng rộng hơn. Trong khoảng t, SE tăng làm biên `t_critical × SE` tăng, khiến hai đầu mút cách mean xa hơn.


**Q20. Is statistical significance identical to practical importance? | Ý nghĩa thống kê có giống giá trị thực tiễn không?**

A. No; 95% describes repeated-interval coverage | Không; 95% mô tả tỷ lệ bao phủ khi lặp

B. Strong dependence or problematic extreme data in small samples | Phụ thuộc mạnh hoặc dữ liệu cực đoan trong mẫu nhỏ

C. No; effect size and context still matter | Không; còn kích thước tác động và bối cảnh

D. It becomes wider | Trở nên rộng hơn

**Đáp án: C**

**Giải thích:** p nhỏ không chứng minh hiệu quả thực tế lớn. Ngoài p-value cần báo kích thước tác động và độ bất định; tác động rất nhỏ có thể có ý nghĩa thống kê nhưng không hữu ích thực tế.

## 8. Liên hệ bài kế tiếp

`CLT/SE → Hypothesis Testing → Confidence Interval → A/B Test`.
