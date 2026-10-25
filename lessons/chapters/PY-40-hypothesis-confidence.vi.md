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

```python
# Mục đích: Giả thuyết gốc cần kiểm định.
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
# Mục đích: Độ bất thường dưới giả định H₀.
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
# Mục đích: So trung bình mẫu với mốc cho trước.
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
# Mục đích: Khoảng tạo bởi quy trình suy luận.
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

## 5. Năm tình huống suy luận thống kê — từ kiểm định một mẫu đến Welch hai nhóm

### Tình huống 1 — Cấp 1: Kiểm định trung bình 10 bài thi so với mốc 50

**Từ vựng trong mục:** **Null hypothesis** — giả thuyết H₀; **p-value** — giá trị p; **Two-sided t-test** — kiểm định hai phía.

**Tình huống thực tế:** Giảng viên có **10 bài kiểm tra**, mỗi bài một điểm **trên thang 100**; điểm đều quanh 50. Nhà trường đưa **mốc tham khảo 50 điểm** và muốn xem số liệu có cho bằng chứng rằng **điểm trung bình của nhóm học viên tương tự khác 50** hay không. Nhóm dùng **kiểm định t hai phía** với ngưỡng quyết định **5%**, chứ không tìm cách chứng minh mốc 50 chắc chắn đúng.

**Vì sao chọn cách này?** **Giả thuyết không H₀** là mốc đang được thử, ở đây trung bình quần thể bằng **50 điểm**; **H₁ hai phía** là trung bình **khác 50**, có thể cao hơn hoặc thấp hơn. `ttest_1samp` dùng **10 điểm mẫu**, mức trung bình và độ phân tán của chúng để tính **p-value**: mức độ bất thường của kết quả như quan sát **nếu H₀ đúng**. So p-value với **α = 0,05** để quyết định có **bác bỏ H₀** hay chưa; p lớn không chứng minh H₀ chắc chắn đúng, và p nhỏ **không phải xác suất H₀ sai**. Với mẫu nhỏ cần xem giả định các điểm đủ độc lập và phân phối phù hợp.

**Quy trình:**
1. Ghi 10 điểm có cùng thang đo.
2. Dùng `ttest_1samp` với mốc 50 và kiểm định hai phía.
3. So p với α=0,05 và phát biểu 'không bác bỏ' hoặc 'bác bỏ', không gọi là chứng minh H₀.

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

B. Probability of equally or more extreme test results under H0 | Xác suất thống kê cực đoan bằng hoặc hơn khi H₀ đúng

C. Test a population mean against a specified value | Kiểm định trung bình quần thể với một mốc

D. An interval from a procedure with 95% long-run coverage | Khoảng từ quy trình có mức bao phủ dài hạn 95%

**Đáp án: A**

**Giải thích:** Đó là giả định gốc của kiểm định. Ví dụ H₀: μ=50 nói về mean quần thể; không đòi mean mẫu quan sát phải đúng 50.


**Q2. What does p-value mean? | p-value nghĩa là gì?**

A. A null hypothesis subjected to statistical testing | Giả thuyết không được đem kiểm định

B. Probability of equally or more extreme test results under H0 | Xác suất thống kê cực đoan bằng hoặc hơn khi H₀ đúng

C. Test a population mean against a specified value | Kiểm định trung bình quần thể với một mốc

D. An interval from a procedure with 95% long-run coverage | Khoảng từ quy trình có mức bao phủ dài hạn 95%

**Đáp án: B**

**Giải thích:** Nó được tính với điều kiện mô hình H₀ đúng. p-value được tính từ thống kê kiểm định và phân phối dưới H₀, chứ không trực tiếp gán xác suất cho H₀.


**Q3. What is a one-sample t-test for? | T-test một mẫu dùng để làm gì?**

A. A null hypothesis subjected to statistical testing | Giả thuyết không được đem kiểm định

B. Probability of equally or more extreme test results under H0 | Xác suất thống kê cực đoan bằng hoặc hơn khi H₀ đúng

C. Test a population mean against a specified value | Kiểm định trung bình quần thể với một mốc

D. An interval from a procedure with 95% long-run coverage | Khoảng từ quy trình có mức bao phủ dài hạn 95%

**Đáp án: C**

**Giải thích:** Nó dùng trung bình và ước lượng phương sai mẫu. Khác kiểm định hai mẫu, t-test một mẫu so trung bình một mẫu với mốc cố định.


**Q4. What is a 95% confidence interval? | Khoảng tin cậy 95% là gì?**

A. A null hypothesis subjected to statistical testing | Giả thuyết không được đem kiểm định

B. Probability of equally or more extreme test results under H0 | Xác suất thống kê cực đoan bằng hoặc hơn khi H₀ đúng

C. Test a population mean against a specified value | Kiểm định trung bình quần thể với một mốc

D. An interval from a procedure with 95% long-run coverage | Khoảng từ quy trình có mức bao phủ dài hạn 95%

**Đáp án: D**

**Giải thích:** Bao phủ được hiểu qua những lần lấy mẫu lặp. Mức bao phủ 95% thuộc quy trình qua nhiều mẫu; một CI đã tính cần báo hai đầu mút và giả định đi kèm.


**Q5. What does alpha represent? | α đại diện cho gì?**

A. A preselected significance threshold | Ngưỡng mức ý nghĩa được chọn trước

B. Reject H0 at that significance level | Bác bỏ H₀ ở mức ý nghĩa đó

C. Fail to reject H0 | Chưa đủ bằng chứng bác bỏ H₀

D. Compare one sample mean with mu0 | So mean một mẫu với mốc mu0

**Đáp án: A**

**Giải thích:** α điều khiển quy tắc bác bỏ. Chọn alpha sau khi nhìn p-value có thể làm sai ý nghĩa kiểm soát báo động nhầm dự kiến.


**Q6. What does p<alpha typically imply? | p<α thường dẫn tới gì?**

A. A preselected significance threshold | Ngưỡng mức ý nghĩa được chọn trước

B. Reject H0 at that significance level | Bác bỏ H₀ ở mức ý nghĩa đó

C. Fail to reject H0 | Chưa đủ bằng chứng bác bỏ H₀

D. Compare one sample mean with mu0 | So mean một mẫu với mốc mu0

**Đáp án: B**

**Giải thích:** Kết quả bất thường dưới giả thuyết gốc. Bác bỏ cung cấp bằng chứng chống H₀ dưới mô hình, không đo xác suất H₀ sai.


**Q7. What does p≥alpha imply? | p≥α thường kết luận gì?**

A. A preselected significance threshold | Ngưỡng mức ý nghĩa được chọn trước

B. Reject H0 at that significance level | Bác bỏ H₀ ở mức ý nghĩa đó

C. Fail to reject H0 | Chưa đủ bằng chứng bác bỏ H₀

D. Compare one sample mean with mu0 | So mean một mẫu với mốc mu0

**Đáp án: C**

**Giải thích:** Không bác bỏ không phải chứng minh H₀. Mẫu nhỏ có thể bỏ sót tác động thật; 'không bác bỏ' khác với 'đã xác nhận bằng nhau'.


**Q8. What is `ttest_1samp(x,popmean=mu0)` for? | `ttest_1samp(x,popmean=mu0)` dùng làm gì?**

A. A preselected significance threshold | Ngưỡng mức ý nghĩa được chọn trước

B. Reject H0 at that significance level | Bác bỏ H₀ ở mức ý nghĩa đó

C. Fail to reject H0 | Chưa đủ bằng chứng bác bỏ H₀

D. Compare one sample mean with mu0 | So mean một mẫu với mốc mu0

**Đáp án: D**

**Giải thích:** Nó chạy kiểm định t một mẫu. Đối tượng trả về có thống kê kiểm định và p-value; lấy `.pvalue` khi cần quyết định.


**Q9. How is a one-sample t statistic formed? | Thống kê t một mẫu có dạng gì?**

A. (sample mean−mu0)/SE | (mean mẫu−mu0)/SE

B. Standard error of the mean | Sai số chuẩn của trung bình

C. Lower and upper endpoints of a t interval | Hai đầu dưới/trên của khoảng t

D. n−1 | n−1

**Đáp án: A**

**Giải thích:** Nó chuẩn hóa độ lệch của mean so với mốc. Chênh hai điểm chỉ có ý nghĩa kiểm định khi so với độ bất định lấy mẫu của mean.


**Q10. What does `scipy.stats.sem` estimate? | `scipy.stats.sem` ước lượng gì?**

A. (sample mean−mu0)/SE | (mean mẫu−mu0)/SE

B. Standard error of the mean | Sai số chuẩn của trung bình

C. Lower and upper endpoints of a t interval | Hai đầu dưới/trên của khoảng t

D. n−1 | n−1

**Đáp án: B**

**Giải thích:** Nó ước lượng độ dao động của mean mẫu. SE có xu hướng giảm khi n tăng dưới giả định phù hợp, còn SD của từng điểm không nhất thiết giảm.


**Q11. What does t.interval return? | t.interval trả gì?**

A. (sample mean−mu0)/SE | (mean mẫu−mu0)/SE

B. Standard error of the mean | Sai số chuẩn của trung bình

C. Lower and upper endpoints of a t interval | Hai đầu dưới/trên của khoảng t

D. n−1 | n−1

**Đáp án: C**

**Giải thích:** Khoảng phụ thuộc mức tin cậy, df, vị trí và độ rộng. Scale lớn làm khoảng rộng; loc là ước lượng trung tâm chứ không phải phần trăm tin cậy.


**Q12. What degrees of freedom are usual for one-sample t inference? | Bậc tự do thông dụng của t một mẫu là gì?**

A. (sample mean−mu0)/SE | (mean mẫu−mu0)/SE

B. Standard error of the mean | Sai số chuẩn của trung bình

C. Lower and upper endpoints of a t interval | Hai đầu dưới/trên của khoảng t

D. n−1 | n−1

**Đáp án: D**

**Giải thích:** Ước lượng phương sai mẫu làm mất một bậc tự do. Thống kê t ước lượng phương sai từ mẫu nên thường còn n−1 bậc tự do.


**Q13. Is p-value equal to P(H0 is true)? | p-value có bằng P(H₀ đúng) không?**

A. No; p is conditional on H0 | Không; p được tính khi giả định H₀ đúng

B. It does not reject at the matching alpha | Không bác bỏ với alpha tương ứng

C. Rejecting a true null hypothesis | Bác bỏ H₀ khi H₀ thực sự đúng

D. Failing to reject a false H0 | Không bác bỏ H₀ khi H₀ sai

**Đáp án: A**

**Giải thích:** p theo tần suất không phải posterior. Nhầm p với P(H₀|dữ liệu) là đảo chiều điều kiện; kiểm định tần suất xét mức cực đoan của dữ liệu khi H₀ đúng.


**Q14. If a confidence interval covers a null value, what often happens in a matching two-sided test? | Nếu CI chứa mốc H₀ thì kiểm định hai phía tương ứng thường thế nào?**

A. No; p is conditional on H0 | Không; p được tính khi giả định H₀ đúng

B. It does not reject at the matching alpha | Không bác bỏ với alpha tương ứng

C. Rejecting a true null hypothesis | Bác bỏ H₀ khi H₀ thực sự đúng

D. Failing to reject a false H0 | Không bác bỏ H₀ khi H₀ sai

**Đáp án: B**

**Giải thích:** Các quy trình tương ứng thường thống nhất dưới cùng giả định. Sự tương ứng cần kiểm định hai phía, mức tin cậy và giả định phù hợp; không đúng với mọi loại kiểm định và khoảng.


**Q15. What is a type I error? | Sai lầm loại I là gì?**

A. No; p is conditional on H0 | Không; p được tính khi giả định H₀ đúng

B. It does not reject at the matching alpha | Không bác bỏ với alpha tương ứng

C. Rejecting a true null hypothesis | Bác bỏ H₀ khi H₀ thực sự đúng

D. Failing to reject a false H0 | Không bác bỏ H₀ khi H₀ sai

**Đáp án: C**

**Giải thích:** Alpha kiểm soát lỗi loại I dưới giả định kiểm định. Sai lầm loại I là báo dương sai; alpha được chọn trước để kiểm soát xác suất lỗi này dưới giả định H₀.


**Q16. What is a type II error? | Sai lầm loại II là gì?**

A. No; p is conditional on H0 | Không; p được tính khi giả định H₀ đúng

B. It does not reject at the matching alpha | Không bác bỏ với alpha tương ứng

C. Rejecting a true null hypothesis | Bác bỏ H₀ khi H₀ thực sự đúng

D. Failing to reject a false H0 | Không bác bỏ H₀ khi H₀ sai

**Đáp án: D**

**Giải thích:** Nó khác lỗi bác bỏ H₀ đúng. Power bằng một trừ xác suất sai lầm loại II dưới giả thuyết đối cụ thể, liên quan đến thiết kế cỡ mẫu.


**Q17. Does a 95% CI say the fixed parameter has 95% probability of lying in this realized interval? | CI 95% có nghĩa xác suất tham số cố định trong khoảng đã tính là 95%?**

A. No; 95% describes repeated-interval coverage | Không; 95% mô tả tỷ lệ bao phủ khi lặp

B. Strong dependence or problematic extreme data in small samples | Phụ thuộc mạnh hoặc dữ liệu cực đoan trong mẫu nhỏ

C. It becomes wider | Trở nên rộng hơn

D. No; effect size and context still matter | Không; còn kích thước tác động và bối cảnh

**Đáp án: A**

**Giải thích:** Trong diễn giải tần suất, tham số cố định và khoảng thay đổi theo mẫu. Phát biểu xác suất áp dụng cho quy trình tạo khoảng ngẫu nhiên trước lấy mẫu, không phải μ cố định sau khi quan sát một CI.


**Q18. What can violate simple t-test assumptions? | Điều gì có thể vi phạm giả định t-test đơn giản?**

A. No; 95% describes repeated-interval coverage | Không; 95% mô tả tỷ lệ bao phủ khi lặp

B. Strong dependence or problematic extreme data in small samples | Phụ thuộc mạnh hoặc dữ liệu cực đoan trong mẫu nhỏ

C. It becomes wider | Trở nên rộng hơn

D. No; effect size and context still matter | Không; còn kích thước tác động và bối cảnh

**Đáp án: B**

**Giải thích:** Suy luận cần mô hình lấy mẫu phù hợp. Mẫu rất nhỏ, ngoại lệ nặng hoặc phụ thuộc có thể khiến p-value và CI báo ra thiếu tin cậy.


**Q19. What happens to CI width if SE grows with other inputs fixed? | SE tăng khi yếu tố khác giữ nguyên thì CI rộng ra sao?**

A. No; 95% describes repeated-interval coverage | Không; 95% mô tả tỷ lệ bao phủ khi lặp

B. Strong dependence or problematic extreme data in small samples | Phụ thuộc mạnh hoặc dữ liệu cực đoan trong mẫu nhỏ

C. It becomes wider | Trở nên rộng hơn

D. No; effect size and context still matter | Không; còn kích thước tác động và bối cảnh

**Đáp án: C**

**Giải thích:** Bất định cao làm khoảng rộng hơn. Trong khoảng t, SE tăng làm biên `t_critical × SE` tăng, khiến hai đầu mút cách mean xa hơn.


**Q20. Is statistical significance identical to practical importance? | Ý nghĩa thống kê có giống giá trị thực tiễn không?**

A. No; 95% describes repeated-interval coverage | Không; 95% mô tả tỷ lệ bao phủ khi lặp

B. Strong dependence or problematic extreme data in small samples | Phụ thuộc mạnh hoặc dữ liệu cực đoan trong mẫu nhỏ

C. It becomes wider | Trở nên rộng hơn

D. No; effect size and context still matter | Không; còn kích thước tác động và bối cảnh

**Đáp án: D**

**Giải thích:** p nhỏ không chứng minh hiệu quả thực tế lớn. Ngoài p-value cần báo kích thước tác động và độ bất định; tác động rất nhỏ có thể có ý nghĩa thống kê nhưng không hữu ích thực tế.

## 8. Liên hệ bài kế tiếp

`CLT/SE → Hypothesis Testing → Confidence Interval → A/B Test`.
