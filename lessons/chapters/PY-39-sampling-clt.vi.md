# PY-39 — Lấy mẫu, CLT và sai số chuẩn


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Population** — tổng thể; **Sample** — mẫu.

`Thống kê → Sampling → Central Limit Theorem → Confidence Interval`

**Học xong dùng để làm gì?** Ước lượng đặc trưng tổng thể từ mẫu, nhận biết sai số lấy mẫu và quy luật của trung bình mẫu.

**Kết nối kiến thức tiếp theo:** PY-40 dùng sai số đó để xây khoảng tin cậy và kiểm định giả thuyết.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Khái niệm |
|---|---|---|
| Population | tổng thể | Toàn bộ đối tượng cần nghiên cứu |
| Sample | mẫu | Nhóm con lấy từ tổng thể theo cách rõ ràng |
| CLT | định lý giới hạn trung tâm | Phân phối trung bình mẫu tiến gần chuẩn theo điều kiện thích hợp |
| Standard error | sai số chuẩn | Độ biến thiên của một thống kê giữa các mẫu |

## 3. Thư viện và hàm Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cách viết | Khi nào dùng, ý nghĩa tham số |
|---|---|
| `df.sample(n=,random_state=)` | Lấy mẫu có thể lặp, chú ý phương pháp lấy mẫu |
| `rng.choice(values,size=,replace=)` | Lấy mẫu thay thế hoặc không thay thế |
| `np.mean(samples,axis=1)` | Tính trung bình từng lần lấy mẫu |
| `s / np.sqrt(n)` | Ước lượng SE của mean từ std mẫu s |

## 4. Khái niệm chính và liên quan

**Mạch kiến thức:** Tổng thể là nhóm cần kết luận, mẫu là những quan sát thực sự lấy. Lặp lấy mẫu sinh ra nhiều trung bình mẫu; CLT giải thích xu hướng phân phối của chúng, còn sai số chuẩn đo mức dao động của thống kê giữa các mẫu.

### 4.1. Population — Toàn bộ nhóm cần nghiên cứu

**Từ vựng:** **Population** — tổng thể; **Unit** — đơn vị quan sát.

**Tổng thể** là toàn bộ các đối tượng mà ta muốn kết luận, như 100 hóa đơn của một cửa hàng trong một ngày. Mỗi hóa đơn là **một đơn vị quan sát**; các cột có thể là giá trị, thời gian, trạng thái giao. Nếu chỉ đo 5 hóa đơn, kết luận không tự mở rộng thành 100 hóa đơn mà không xem cách chọn mẫu. Trong ví dụ, tổng thể gồm đúng 100 mã 0–99, nên `len` bằng 100.

```python
# Mục đích: Toàn bộ nhóm cần nghiên cứu.
population = list(range(100))
print(len(population))
```

**Kết quả khi chạy:**

```text
100
```

Tổng thể có 100 mã hóa đơn; số lượng tổng thể là N=100.

### 4.2. Sample — Nhóm con lấy theo cách xác định

**Từ vựng:** **Sample** — mẫu; **Sampling** — lấy mẫu.

**Mẫu** là một phần các đối tượng được chọn từ tổng thể. Ví dụ từ 5 mã hóa đơn `[1,2,3,4,5]`, chọn 3 mã **không hoàn lại** nghĩa là mỗi mã xuất hiện tối đa một lần trong mẫu. `rng.choice(...,replace=False)` cho chọn mẫu giả ngẫu nhiên, seed giúp tái lập. Chọn ngẫu nhiên hợp lý hỗ trợ giảm thiên lệch chọn mẫu, nhưng nếu dữ liệu nguồn đã thiếu nhóm quan trọng thì seed không thể khắc phục.

```python
# Mục đích: Nhóm con lấy theo cách xác định.
import numpy as np

rng = np.random.default_rng(1)
sample = rng.choice([1, 2, 3, 4, 5], size=3, replace=False)
print(sample.tolist())
```

**Kết quả khi chạy:**

```text
[3, 2, 4]
```

Mẫu có ba mã khác nhau vì lấy không hoàn lại; đây là một kết quả ngẫu nhiên có thể tái lập.

### 4.3. CLT — Phân phối trung bình của các mẫu

**Từ vựng:** **CLT** — định lý giới hạn trung tâm; **Sampling distribution** — phân phối lấy mẫu.

**CLT** nói rằng dưới các điều kiện phù hợp như quan sát độc lập, cùng phân phối, phương sai hữu hạn, khi **cỡ mẫu n lớn**, phân phối của **trung bình mẫu** sau chuẩn hóa thường tiến gần dạng chuẩn, ngay cả khi dữ liệu gốc không chuẩn. Nó **không** nói dữ liệu gốc trở thành chuẩn hay từng mẫu đều có mean giống nhau. Mô phỏng 200 nhóm, mỗi nhóm 40 giá trị từ phân phối mũ mean lý thuyết 2, cho trung bình các mean gần 2.

```python
# Mục đích: Phân phối trung bình của các mẫu.
import numpy as np

rng = np.random.default_rng(1)
groups = rng.exponential(scale=2, size=(200, 40))
means = groups.mean(axis=1)
print(round(float(means.mean()), 3))
```

**Kết quả khi chạy:**

```text
2.011
```

200 trung bình mẫu xoay quanh giá trị kỳ vọng 2; một số mô phỏng không chứng minh CLT nhưng minh họa cách lấy mẫu lặp.

### 4.4. Standard error — Độ biến thiên của một ước lượng

**Từ vựng:** **Standard error (SE)** — sai số chuẩn; **Standard deviation (SD)** — độ lệch chuẩn.

**SD** mô tả độ phân tán của **quan sát riêng lẻ**, còn **SE của mean** mô tả mức dao động **giữa các trung bình mẫu** nếu lặp lấy mẫu cùng cách. Với n quan sát độc lập và ước lượng SD mẫu s, SE(mean) thường ước tính bằng `s/sqrt(n)` (trường hợp thích hợp). Năm điểm `[6,7,8,9,10]` có s≈1,581 điểm, nên SE≈0,707 điểm. Cỡ mẫu gấp 4 làm SE còn một nửa nếu độ phân tán giữ nguyên.

```python
# Mục đích: Độ biến thiên của một ước lượng.
import numpy as np

scores = np.array([6, 7, 8, 9, 10], dtype=float)
se = scores.std(ddof=1) / np.sqrt(len(scores))
print(round(float(se), 3))
```

**Kết quả khi chạy:**

```text
0.707
```

SE của trung bình mẫu xấp xỉ 0,707 điểm; nó không phải SD của từng điểm.

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Rút năm đơn trong hai mươi đơn để kiểm kê · Cấp 1: Lấy mẫu 5 lượt

**Tình huống thực tế:** Kho có đúng 20 đơn được gắn mã 1 đến 20; người kiểm kê chỉ đủ thời gian xem 5 đơn. Cần lấy mẫu không hoàn lại, mọi mã có cơ hội như nhau.

**Vì sao chọn cách giải này?** Lấy mẫu ngẫu nhiên không hoàn lại giúp chọn năm mã phân biệt; seed cố định chỉ phục vụ tái lập thử nghiệm.

**Quy trình giải:**

1. Tạo danh sách ID từ 1 đến 20.
2. Dùng `random.Random(42).sample` lấy năm ID không trùng.
3. In danh sách mã được chọn.

```python
# Mục đích: Rút năm đơn trong hai mươi đơn để kiểm kê.
import random

ids = list(range(1, 21))
print(random.Random(42).sample(ids, 5))
```

**Kết quả khi chạy:**

```text
[4, 1, 9, 8, 17]
```

Năm đơn được chọn không trùng nhau, nhưng kết quả không thay thế quy trình lấy mẫu thực tế của kho.

**Bài thực hành nâng cấp — cấp 1/5:** Cửa hàng ghi **10 ngày lưu lượng khách**, mỗi giá trị là số lượt đến cửa hàng/ngày. Hãy chọn 5 ngày không lặp từ 10 dòng. Các cấp tăng số ngày từ 10 đến 20, từ một mẫu đến phân phối của trung bình mẫu và khoảng ước lượng; `NaN` không phải ngày 0 khách.

```python
import numpy as np
# Mỗi hàng = một ngày đo lưu lượng khách, đơn vị lượt/ngày.
values = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125],dtype=float)
valid = values[np.isfinite(values)]
rng = np.random.default_rng(2026)
result = rng.choice(valid,size=5,replace=False).tolist()
print("Số ngày:",len(values))
print("Kết quả:",result)
```

**Đọc kết quả:** Tổng 10 ngày; lấy mẫu có thể thay đổi theo seed, vì thế dùng `default_rng(2026)` để kiểm tra lặp lại. Khoảng bootstrap là ước lượng, không là đảm bảo tuyệt đối.

### Tình huống 2 — Thử biến thiên trung bình với nguồn lệch phải · Cấp 2: So sánh hai mean

**Tình huống thực tế:** Một quá trình giả lập có thời gian chờ tuân phân phối mũ với trung bình 2 phút. Nhóm phân tích lấy 200 mẫu độc lập, mỗi mẫu gồm 40 thời gian chờ, để quan sát phân phối các mean.

**Vì sao chọn cách giải này?** Lấy nhiều nhóm rồi tính mean từng nhóm giúp minh họa biến thiên của trung bình mẫu trong CLT.

**Quy trình giải:**

1. Sinh bảng 200×40 số từ phân phối mũ có mean lý thuyết 2 phút.
2. Lấy mean theo từng hàng, được 200 trung bình mẫu.
3. In trung bình và SD giữa các mean sau làm tròn.

```python
# Mục đích: Thử biến thiên trung bình với nguồn lệch phải.
import numpy as np

rng = np.random.default_rng(1)
groups = rng.exponential(scale=2, size=(200, 40))
means = groups.mean(axis=1)
print(round(float(means.mean()), 3), round(float(means.std(ddof=1)), 3))
```

**Kết quả khi chạy:**

```text
2.011 0.333
```

Các mean dao động quanh 2 phút; độ phân tán thực nghiệm giữa chúng khoảng 0,333 phút.

**Bài thực hành nâng cấp — cấp 2/5:** Cửa hàng ghi **12 ngày lưu lượng khách**, mỗi giá trị là số lượt đến cửa hàng/ngày. Hãy so mean của 6 ngày lấy mẫu và 12 ngày gốc. Các cấp tăng số ngày từ 10 đến 20, từ một mẫu đến phân phối của trung bình mẫu và khoảng ước lượng; `NaN` không phải ngày 0 khách.

```python
import numpy as np
# Mỗi hàng = một ngày đo lưu lượng khách, đơn vị lượt/ngày.
values = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135],dtype=float)
valid = values[np.isfinite(values)]
rng = np.random.default_rng(2026)
result = {'sample_mean':round(float(rng.choice(valid,size=6,replace=False).mean()),2),'all_mean':round(float(valid.mean()),2)}
print("Số ngày:",len(values))
print("Kết quả:",result)
```

**Đọc kết quả:** Tổng 12 ngày; lấy mẫu có thể thay đổi theo seed, vì thế dùng `default_rng(2026)` để kiểm tra lặp lại. Khoảng bootstrap là ước lượng, không là đảm bảo tuyệt đối.

### Tình huống 3 — Ước lượng sai số chuẩn của điểm trung bình · Cấp 3: Phân phối của sample mean

**Tình huống thực tế:** Trung tâm có năm điểm `[6,7,8,9,10]` cùng thang điểm. Muốn báo SE cho **trung bình mẫu**, không phải độ phân tán của từng học viên.

**Vì sao chọn cách giải này?** SE ước lượng bằng SD mẫu `ddof=1` chia căn cỡ mẫu khi giả định lấy mẫu độc lập phù hợp.

**Quy trình giải:**

1. Tạo mảng năm điểm.
2. Tính SD mẫu và chia cho căn của 5.
3. In SE sau làm tròn ba chữ số.

```python
# Mục đích: Ước lượng sai số chuẩn của điểm trung bình.
import numpy as np

scores = np.array([6, 7, 8, 9, 10], dtype=float)
print(round(float(scores.std(ddof=1) / np.sqrt(len(scores))), 3))
```

**Kết quả khi chạy:**

```text
0.707
```

SE ước lượng khoảng 0,707 điểm. Mẫu chỉ có năm người nên còn bất định cao.

**Bài thực hành nâng cấp — cấp 3/5:** Cửa hàng ghi **15 ngày lưu lượng khách**, mỗi giá trị là số lượt đến cửa hàng/ngày. Hãy lấy 200 mẫu độc lập có hoàn lại rồi so trung bình. Các cấp tăng số ngày từ 10 đến 20, từ một mẫu đến phân phối của trung bình mẫu và khoảng ước lượng; `NaN` không phải ngày 0 khách.

```python
import numpy as np
# Mỗi hàng = một ngày đo lưu lượng khách, đơn vị lượt/ngày.
values = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150],dtype=float)
valid = values[np.isfinite(values)]
rng = np.random.default_rng(2026)
result = {'bootstrap_means_avg':round(float(np.mean([rng.choice(valid,size=5,replace=True).mean() for _ in range(200)])),2),'all_mean':round(float(valid.mean()),2)}
print("Số ngày:",len(values))
print("Kết quả:",result)
```

**Đọc kết quả:** Tổng 15 ngày; lấy mẫu có thể thay đổi theo seed, vì thế dùng `default_rng(2026)` để kiểm tra lặp lại. Khoảng bootstrap là ước lượng, không là đảm bảo tuyệt đối.

### Tình huống 4 — Xem tác động của số người đo lên SE · Cấp 4: Bootstrap khi dữ liệu thiếu

**Tình huống thực tế:** Độ lệch chuẩn quần thể được giả định cố định σ=10 điểm. So hai nghiên cứu dùng n=25 và n=100 người, trong điều kiện lấy mẫu độc lập thích hợp.

**Vì sao chọn cách giải này?** SE của trung bình theo công thức σ/sqrt(n), nên n tăng bốn lần khiến SE giảm một nửa.

**Quy trình giải:**

1. Đặt sigma=10.
2. Với n=25 và n=100, chia sigma cho căn n.
3. In từng cỡ mẫu cùng SE, giữ đơn vị điểm.

```python
# Mục đích: Xem tác động của số người đo lên SE.
import numpy as np

sigma = 10
for n in [25, 100]:
    print(n, sigma / np.sqrt(n))
```

**Kết quả khi chạy:**

```text
25 2.0
100 1.0
```

Cỡ mẫu 100 cho SE 1 điểm, một nửa của SE khi n=25.

**Bài thực hành nâng cấp — cấp 4/5:** Cửa hàng ghi **18 ngày lưu lượng khách**, mỗi giá trị là số lượt đến cửa hàng/ngày. Hãy thực hiện bootstrap sau khi loại ngày chưa ghi. Các cấp tăng số ngày từ 10 đến 20, từ một mẫu đến phân phối của trung bình mẫu và khoảng ước lượng; `NaN` không phải ngày 0 khách.

```python
import numpy as np
# Mỗi hàng = một ngày đo lưu lượng khách, đơn vị lượt/ngày.
values = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, np.nan, 160, 165],dtype=float)
valid = values[np.isfinite(values)]
rng = np.random.default_rng(2026)
result = {'bootstrap_mean':round(float(np.mean([rng.choice(valid,size=len(valid),replace=True).mean() for _ in range(500)])),2),'missing':len(values)-len(valid)}
print("Số ngày:",len(values))
print("Kết quả:",result)
```

**Đọc kết quả:** Tổng 18 ngày; lấy mẫu có thể thay đổi theo seed, vì thế dùng `default_rng(2026)` để kiểm tra lặp lại. Khoảng bootstrap là ước lượng, không là đảm bảo tuyệt đối.

### Tình huống 5 — Chọn khách từ bảng dữ liệu để khảo sát · Cấp 5: Khoảng tin cậy từ 1000 lần lặp

**Tình huống thực tế:** Cửa hàng có bảng 10 khách, ID từ 0 tới 9. Nhóm chăm sóc khách muốn rút 3 ID không trùng từ DataFrame để mời khảo sát.

**Vì sao chọn cách giải này?** `DataFrame.sample` chọn hàng; `random_state` giữ ví dụ có kết quả xác định và có thể sắp ID trước khi in.

**Quy trình giải:**

1. Tạo bảng một cột `id` với 10 khách.
2. Lấy ba hàng bằng `.sample(n=3,random_state=42)`.
3. Chỉ lấy ID, sắp tăng để đầu ra dễ đối chiếu.

```python
# Mục đích: Chọn khách từ bảng dữ liệu để khảo sát.
import pandas as pd

customers = pd.DataFrame({'id': list(range(10))})
sampled = customers.sample(n=3, random_state=42)
print(sorted(sampled['id'].tolist()))
```

**Kết quả khi chạy:**

```text
[1, 5, 8]
```

Mẫu gồm ba ID khác nhau; cố định seed làm ví dụ tái lập, không bảo đảm tính đại diện của mọi nhóm khách.

**Bài thực hành nâng cấp — cấp 5/5:** Cửa hàng ghi **20 ngày lưu lượng khách**, mỗi giá trị là số lượt đến cửa hàng/ngày. Hãy ước lượng khoảng 95% của mean bằng 1000 bootstrap mẫu. Các cấp tăng số ngày từ 10 đến 20, từ một mẫu đến phân phối của trung bình mẫu và khoảng ước lượng; `NaN` không phải ngày 0 khách.

```python
import numpy as np
# Mỗi hàng = một ngày đo lưu lượng khách, đơn vị lượt/ngày.
values = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, np.nan, 160, 165, 170, np.nan],dtype=float)
valid = values[np.isfinite(values)]
rng = np.random.default_rng(2026)
result = {'mean':round(float(valid.mean()),2),'CI_95':np.percentile([rng.choice(valid,size=len(valid),replace=True).mean() for _ in range(1000)],[2.5,97.5]).round(2).tolist(),'missing':len(values)-len(valid)}
print("Số ngày:",len(values))
print("Kết quả:",result)
```

**Đọc kết quả:** Tổng 20 ngày; lấy mẫu có thể thay đổi theo seed, vì thế dùng `default_rng(2026)` để kiểm tra lặp lại. Khoảng bootstrap là ước lượng, không là đảm bảo tuyệt đối.

## 6. Sai lầm thường gặp

- CLT nói về phân phối của **trung bình mẫu** dưới các điều kiện thích hợp, không biến dữ liệu gốc thành chuẩn.
- SD mô tả số đo cá thể, SE mô tả mức biến thiên ước lượng giữa các mẫu.
- Công thức SE≈s/√n cần giả định lấy mẫu phù hợp; phụ thuộc, chọn mẫu không ngẫu nhiên và quần thể hữu hạn có thể cần điều chỉnh.
- Seed giúp tái lập phép mô phỏng, **không** sửa thiên lệch chọn mẫu hoặc bảo đảm mẫu đại diện.
- Cỡ mẫu lớn thường giảm SE, nhưng không sửa được sai lệch có hệ thống.
- Không kết luận mọi mẫu sẽ gần trung bình thật hay một ngưỡng n cố định đúng cho mọi phân phối.

## 7. Trắc nghiệm

**Q1. What is a population? | Tổng thể là gì?**

A. All units in the target group | Toàn bộ đơn vị của nhóm cần nghiên cứu

B. A selected subset of the population | Một nhóm con được chọn từ tổng thể

C. Approximate sampling distribution of sample means | Phân phối gần đúng của các trung bình mẫu

D. Sampling variability of an estimator | Độ biến thiên của thống kê ước lượng qua các mẫu

**Đáp án: A**

**Giải thích:** Kết luận dự kiến hướng đến tổng thể.


**Q2. What is a sample? | Mẫu là gì?**

A. All units in the target group | Toàn bộ đơn vị của nhóm cần nghiên cứu

B. A selected subset of the population | Một nhóm con được chọn từ tổng thể

C. Approximate sampling distribution of sample means | Phân phối gần đúng của các trung bình mẫu

D. Sampling variability of an estimator | Độ biến thiên của thống kê ước lượng qua các mẫu

**Đáp án: B**

**Giải thích:** Mẫu chứa một phần quan sát.


**Q3. What does CLT describe? | CLT mô tả gì?**

A. All units in the target group | Toàn bộ đơn vị của nhóm cần nghiên cứu

B. A selected subset of the population | Một nhóm con được chọn từ tổng thể

C. Approximate sampling distribution of sample means | Phân phối gần đúng của các trung bình mẫu

D. Sampling variability of an estimator | Độ biến thiên của thống kê ước lượng qua các mẫu

**Đáp án: C**

**Giải thích:** CLT nói về mean qua nhiều mẫu, không nói mọi giá trị gốc thành chuẩn.


**Q4. What is standard error? | SE là gì?**

A. All units in the target group | Toàn bộ đơn vị của nhóm cần nghiên cứu

B. A selected subset of the population | Một nhóm con được chọn từ tổng thể

C. Approximate sampling distribution of sample means | Phân phối gần đúng của các trung bình mẫu

D. Sampling variability of an estimator | Độ biến thiên của thống kê ước lượng qua các mẫu

**Đáp án: D**

**Giải thích:** SE mô tả độ bất định của thống kê.


**Q5. What does `replace=False` mean when sampling? | `replace=False` khi lấy mẫu nghĩa là gì?**

A. Items cannot be selected twice in one sample | Không chọn lặp một phần tử trong cùng mẫu

B. Reproducible pseudorandom selection | Chọn giả ngẫu nhiên có thể lặp

C. Computes one mean per row | Tính một trung bình cho mỗi hàng

D. Three randomly sampled rows | Ba hàng được chọn ngẫu nhiên

**Đáp án: A**

**Giải thích:** Lấy mẫu không hoàn lại.


**Q6. What does a random seed enable? | Seed ngẫu nhiên cho phép gì?**

A. Items cannot be selected twice in one sample | Không chọn lặp một phần tử trong cùng mẫu

B. Reproducible pseudorandom selection | Chọn giả ngẫu nhiên có thể lặp

C. Computes one mean per row | Tính một trung bình cho mỗi hàng

D. Three randomly sampled rows | Ba hàng được chọn ngẫu nhiên

**Đáp án: B**

**Giải thích:** Nó kiểm soát chuỗi có thể tái tạo.


**Q7. What does `mean(axis=1)` do on a 2-D sample table? | `mean(axis=1)` trên bảng mẫu 2-D làm gì?**

A. Items cannot be selected twice in one sample | Không chọn lặp một phần tử trong cùng mẫu

B. Reproducible pseudorandom selection | Chọn giả ngẫu nhiên có thể lặp

C. Computes one mean per row | Tính một trung bình cho mỗi hàng

D. Three randomly sampled rows | Ba hàng được chọn ngẫu nhiên

**Đáp án: C**

**Giải thích:** Mỗi hàng có thể là một lần lấy mẫu.


**Q8. What does `df.sample(n=3)` select? | `df.sample(n=3)` chọn gì?**

A. Items cannot be selected twice in one sample | Không chọn lặp một phần tử trong cùng mẫu

B. Reproducible pseudorandom selection | Chọn giả ngẫu nhiên có thể lặp

C. Computes one mean per row | Tính một trung bình cho mỗi hàng

D. Three randomly sampled rows | Ba hàng được chọn ngẫu nhiên

**Đáp án: D**

**Giải thích:** Mặc định hàm lấy hàng của DataFrame.


**Q9. What does sample SD measure? | SD mẫu đo gì?**

A. Spread of individual values | Độ phân tán giá trị từng quan sát

B. Spread among hypothetical sample means | Độ phân tán giữa các mean mẫu giả định

C. s/sqrt(n) | s/sqrt(n)

D. It halves | Giảm một nửa

**Đáp án: A**

**Giải thích:** SD khác bất định của mean mẫu.


**Q10. What does the SE of a mean measure? | SE của mean đo gì?**

A. Spread of individual values | Độ phân tán giá trị từng quan sát

B. Spread among hypothetical sample means | Độ phân tán giữa các mean mẫu giả định

C. s/sqrt(n) | s/sqrt(n)

D. It halves | Giảm một nửa

**Đáp án: B**

**Giải thích:** Lấy mẫu lặp gây biến thiên trung bình.


**Q11. What is a common estimated SE formula? | Công thức ước lượng SE thường dùng?**

A. Spread of individual values | Độ phân tán giá trị từng quan sát

B. Spread among hypothetical sample means | Độ phân tán giữa các mean mẫu giả định

C. s/sqrt(n) | s/sqrt(n)

D. It halves | Giảm một nửa

**Đáp án: C**

**Giải thích:** Công thức phù hợp trong các giả định lấy mẫu độc lập thường gặp.


**Q12. How does SE change when n quadruples and sigma is fixed? | SE đổi sao khi n gấp bốn, sigma giữ nguyên?**

A. Spread of individual values | Độ phân tán giá trị từng quan sát

B. Spread among hypothetical sample means | Độ phân tán giữa các mean mẫu giả định

C. s/sqrt(n) | s/sqrt(n)

D. It halves | Giảm một nửa

**Đáp án: D**

**Giải thích:** Căn bậc hai của bốn là hai.


**Q13. Does CLT assert that raw data become normally distributed? | CLT có nói dữ liệu gốc thành phân phối chuẩn không?**

A. No, it concerns standardized sample means | Không, nói về mean mẫu được chuẩn hóa

B. No; sampling design matters | Không; thiết kế lấy mẫu mới quan trọng

C. It decreases for the sample mean under assumptions | Giảm đối với mean mẫu nếu giả định phù hợp

D. A systematically unrepresentative sample | Mẫu không đại diện một cách có hệ thống

**Đáp án: A**

**Giải thích:** Tổng thể lệch vẫn có thể lệch.


**Q14. Is a sample necessarily representative because a seed is fixed? | Có seed cố định thì mẫu chắc chắn đại diện không?**

A. No, it concerns standardized sample means | Không, nói về mean mẫu được chuẩn hóa

B. No; sampling design matters | Không; thiết kế lấy mẫu mới quan trọng

C. It decreases for the sample mean under assumptions | Giảm đối với mean mẫu nếu giả định phù hợp

D. A systematically unrepresentative sample | Mẫu không đại diện một cách có hệ thống

**Đáp án: B**

**Giải thích:** Seed chỉ lặp cách chọn.


**Q15. What often happens to sampling variability as n grows? | n tăng thì dao động lấy mẫu thường thế nào?**

A. No, it concerns standardized sample means | Không, nói về mean mẫu được chuẩn hóa

B. No; sampling design matters | Không; thiết kế lấy mẫu mới quan trọng

C. It decreases for the sample mean under assumptions | Giảm đối với mean mẫu nếu giả định phù hợp

D. A systematically unrepresentative sample | Mẫu không đại diện một cách có hệ thống

**Đáp án: C**

**Giải thích:** SE thường tỷ lệ nghịch căn n.


**Q16. What is the impact of selection bias? | Thiên lệch chọn mẫu gây gì?**

A. No, it concerns standardized sample means | Không, nói về mean mẫu được chuẩn hóa

B. No; sampling design matters | Không; thiết kế lấy mẫu mới quan trọng

C. It decreases for the sample mean under assumptions | Giảm đối với mean mẫu nếu giả định phù hợp

D. A systematically unrepresentative sample | Mẫu không đại diện một cách có hệ thống

**Đáp án: D**

**Giải thích:** Tăng mẫu không tự sửa cách chọn sai.


**Q17. Does n=40 guarantee a good normal approximation in every problem? | n=40 có bảo đảm xấp xỉ chuẩn tốt ở mọi bài toán không?**

A. No, underlying assumptions and tails matter | Không, còn phụ thuộc giả định và đuôi phân phối

B. Uses n−1 in variance denominator | Dùng n−1 ở mẫu số phương sai

C. Standard deviation | Độ lệch chuẩn

D. Clearly defined sampling assumptions | Giả định lấy mẫu được xác định rõ

**Đáp án: A**

**Giải thích:** Không có ngưỡng cỡ mẫu đúng cho mọi trường hợp.


**Q18. What does `ddof=1` change in SD? | `ddof=1` đổi gì trong SD?**

A. No, underlying assumptions and tails matter | Không, còn phụ thuộc giả định và đuôi phân phối

B. Uses n−1 in variance denominator | Dùng n−1 ở mẫu số phương sai

C. Standard deviation | Độ lệch chuẩn

D. Clearly defined sampling assumptions | Giả định lấy mẫu được xác định rõ

**Đáp án: B**

**Giải thích:** Đây là quy ước cho ước lượng phương sai mẫu.


**Q19. Which quantity stays in original units, SD or variance? | Đại lượng nào giữ đơn vị gốc, SD hay variance?**

A. No, underlying assumptions and tails matter | Không, còn phụ thuộc giả định và đuôi phân phối

B. Uses n−1 in variance denominator | Dùng n−1 ở mẫu số phương sai

C. Standard deviation | Độ lệch chuẩn

D. Clearly defined sampling assumptions | Giả định lấy mẫu được xác định rõ

**Đáp án: C**

**Giải thích:** Phương sai có đơn vị bình phương.


**Q20. What is a prerequisite for repeated-sampling inference? | Điều kiện quan trọng của suy luận từ lấy mẫu lặp?**

A. No, underlying assumptions and tails matter | Không, còn phụ thuộc giả định và đuôi phân phối

B. Uses n−1 in variance denominator | Dùng n−1 ở mẫu số phương sai

C. Standard deviation | Độ lệch chuẩn

D. Clearly defined sampling assumptions | Giả định lấy mẫu được xác định rõ

**Đáp án: D**

**Giải thích:** Sự phụ thuộc và cách chọn mẫu ảnh hưởng SE.

## 8. Liên hệ bài kế tiếp

`Thống kê → Sampling → Central Limit Theorem → Confidence Interval`.
