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

## 5. Năm tình huống lấy mẫu/CLT — từ mẫu không hoàn lại đến bootstrap

### Tình huống 1 — Cấp 1: Chọn 10 hóa đơn không hoàn lại từ tổng thể 40

**Từ vựng trong mục:** **Population** — tổng thể; **Sample** — mẫu; **Without replacement** — không hoàn lại.

**Tình huống thực tế:** Kiểm toán viên có danh sách **40 hóa đơn của cả ca**, giá trị từ **100 đến 139 nghìn đồng**, mỗi số tương ứng một hóa đơn. Nhân viên chỉ đủ sức kiểm tra **10 hóa đơn**, nên chọn ngẫu nhiên **10 phiếu khác nhau**, không lấy một phiếu hai lần. Họ muốn xem **số tiền trung bình của 10 phiếu được chọn** có gần **mức trung bình đã biết của cả 40 phiếu** không và hiểu vì sao có thể lệch dù cách lấy mẫu đúng.

**Vì sao chọn cách này?** **Tổng thể** là cả **40 hóa đơn** mà quản lý muốn mô tả, còn **mẫu** chỉ là **10 hóa đơn được chọn** để kiểm tra. `rng.choice(population, size=10, replace=False)` chọn **không hoàn lại**, bảo đảm không xem hai lần cùng một phiếu. `default_rng(31)` đặt **seed 31** để người khác chạy lại ví dụ có thể đối chiếu danh sách đã chọn. `sample.mean()` đo trung bình mẫu, còn `population.mean()` đo trung bình cả 40 khoản; hai số **không buộc bằng nhau** vì mẫu chỉ là một phần. Kết quả gần nhau giúp minh họa phương pháp, chưa bảo đảm mọi lần chọn 10 phiếu đều đại diện tốt.

**Quy trình:**
1. Tạo 40 giá trị hóa đơn làm tổng thể, chọn 10 không hoàn lại.
2. Kiểm tính duy nhất bằng Set và tính mean mẫu.
3. So mean mẫu với mean tổng thể để thấy sai lệch lấy mẫu.

```python
import numpy as np
population = np.arange(100, 140)
rng = np.random.default_rng(31)
sample = rng.choice(population, size=10, replace=False)
if len(sample) != 10 or len(set(sample)) != 10:
    raise ValueError("Cần chọn đủ 10 hóa đơn không trùng.")
print("Tổng thể:", len(population))
print("Hóa đơn chọn:", len(sample))
print(f"Mean mẫu (nghìn đồng): {sample.mean():.1f}")
print(f"Mean tổng thể (nghìn đồng): {population.mean():.1f}")
```

**Kết quả khi chạy:**

```text
Tổng thể: 40
Hóa đơn chọn: 10
Mean mẫu (nghìn đồng): 122.0
Mean tổng thể (nghìn đồng): 119.5
```

Chọn mẫu ngẫu nhiên không có nghĩa mean luôn bằng mean tổng thể; một lần rút 10 đơn chỉ cung cấp một ước lượng.

### Tình huống 2 — Cấp 2: Chia mẫu 12 phiếu theo hai tầng kho

**Từ vựng trong mục:** **Stratified sampling** — lấy mẫu phân tầng; **Allocation** — phân bổ cỡ mẫu.

**Tình huống thực tế:** Kho có **60 phiếu kiểm hàng**, chia đều **30 phiếu nhóm A** và **30 phiếu nhóm B**. Nhân viên chỉ xem được **12 phiếu** nhưng cần bảo đảm nhóm nào cũng có đại diện, nên kế hoạch là rút **6 mã khác nhau ở A và 6 mã khác nhau ở B**. Họ muốn xác nhận danh sách 12 mã không có trùng lặp và không vô tình chọn cả 12 từ cùng một nhóm.

**Vì sao chọn cách này?** **Lấy mẫu phân tầng** nghĩa là chia tổng thể thành các nhóm có ý nghĩa **trước khi rút**, rồi rút trong từng nhóm thay vì rút cả 60 phiếu chung không kiểm soát. Hai tầng A/B đều có 30 phiếu nên kế hoạch **mỗi tầng 6 phiếu** vừa đảm bảo hiện diện, vừa giữ tỷ lệ chọn giống tỷ lệ tổng thể. `rng.choice(..., replace=False)` rút không trùng **trong mỗi tầng**; mã A và B cũng khác tiền tố, nên có thể kiểm tra danh sách chung không trùng. `default_rng(12)` giúp tái lập lần rút; phương pháp này không tự sửa dữ liệu ghi sai ở từng phiếu.

**Quy trình:**
1. Tạo 30 ID A và 30 ID B.
2. Chọn 6 từ mỗi nhóm với seed cố định và không hoàn lại.
3. Ghép 12 ID và xác minh đủ hai nhóm, không lặp.

```python
import numpy as np
rng = np.random.default_rng(12)
A = []
B = []
for i in range(1, 31):
    A.append(f"A{i:02d}")
    B.append(f"B{i:02d}")
selected_a = rng.choice(A, 6, replace=False).tolist()
selected_b = rng.choice(B, 6, replace=False).tolist()
selection = selected_a + selected_b
if len(selection) != 12 or len(set(selection)) != 12:
    raise ValueError("Cần đúng 12 phiếu chọn, không trùng ID.")
print("Tổng thể:", len(A)+len(B))
print("Phiếu lấy:", len(selection))
print("Nhóm A/B:", len(selected_a), len(selected_b))
print("Có trùng ID:", len(selection) != len(set(selection)))
```

**Kết quả khi chạy:**

```text
Tổng thể: 60
Phiếu lấy: 12
Nhóm A/B: 6 6
Có trùng ID: False
```

Phân tầng đảm bảo đại diện từng khu vực **theo thiết kế**, nhưng không tự giải quyết dữ liệu nguồn sai hoặc khung lấy mẫu thiếu phiếu.

### Tình huống 3 — Cấp 3: Mô phỏng 15 lần lấy mẫu để quan sát CLT

**Từ vựng trong mục:** **Sampling distribution** — phân phối trung bình mẫu; **CLT** — định lý giới hạn trung tâm.

**Tình huống thực tế:** Nhóm dịch vụ muốn hiểu **thời gian xử lý** tính bằng **phút** khi các lượt riêng lẻ thường rất ngắn nhưng đôi lúc kéo dài. Họ tạo **15 bộ mẫu giả lập độc lập**, mỗi bộ gồm **40 thời gian**, theo phân phối mũ có mức trung bình lý thuyết **2 phút**. Họ muốn tính **trung bình của từng bộ**, rồi so độ dao động của **15 số trung bình** với độ dao động của tất cả **600 thời gian đơn lẻ**, chứ không gọi mỗi lượt thời gian là một trung bình mẫu.

**Vì sao chọn cách này?** **Định lý giới hạn trung tâm (CLT)** nói về cách **phân phối các trung bình mẫu** có xu hướng gần hình chuông hơn khi mỗi mẫu đủ lớn và các điều kiện phù hợp, **không có nghĩa từng thời gian xử lý sẽ thành phân phối chuẩn**. `rng.exponential(scale=2, size=(15, 40))` tạo **15 hàng mẫu**, mỗi hàng **40 thời gian giả lập** có phân phối lệch phải và mức trung bình lý thuyết 2 phút. `mean(axis=1)` lấy một trung bình **cho từng hàng**, tạo đúng 15 trung bình. So độ lệch chuẩn của 15 trung bình với độ lệch chuẩn các thời gian đơn lẻ cho thấy trung bình thường dao động ít hơn. **Seed 12** giúp tái lập; 15 bộ mẫu chỉ là minh họa nhỏ, không đủ kiểm chứng hoàn toàn hình dạng phân phối.

**Quy trình:**
1. Tạo ma trận 15×40 theo cùng seed để tái lập.
2. Tính một mean cho mỗi trong 15 hàng.
3. So SD của 15 mean với SD của tất cả thời gian đơn lẻ và in mean chung.

```python
import numpy as np
rng = np.random.default_rng(12)
samples = rng.exponential(scale=2, size=(15, 40))
means = samples.mean(axis=1)
if samples.shape != (15, 40) or means.shape != (15,):
    raise ValueError("Cần 15 lần lấy mẫu, mỗi lần 40 quan sát.")
print("Lần lấy mẫu:", len(means))
print("Quan sát mỗi lần:", samples.shape[1])
print(f"Mean của các mean (phút): {means.mean():.3f}")
print("SD mean nhỏ hơn SD dữ liệu:", bool(means.std(ddof=1) < samples.ravel().std(ddof=1)))
```

**Kết quả khi chạy:**

```text
Lần lấy mẫu: 15
Quan sát mỗi lần: 40
Mean của các mean (phút): 2.082
SD mean nhỏ hơn SD dữ liệu: True
```

**15 bản ghi là 15 lần lấy mẫu**, không phải 15 phép đo đơn lẻ; mỗi bản ghi chứa 40 phép đo bên trong.

### Tình huống 4 — Cấp 4: Tính SE từ 18 điểm và tránh so hai mẫu không tương đương

**Từ vựng trong mục:** **Standard error** — sai số chuẩn; **Sample SD** — độ lệch chuẩn mẫu.

**Tình huống thực tế:** Giảng viên có **18 điểm thực hành** trên **thang 30 điểm**, một số tương ứng một học viên. Để hiểu độ chính xác của **trung bình điểm**, giáo viên thử tính **sai số chuẩn SE** từ **9 học viên đầu tiên**, rồi từ **cả 18 người**. Hai tập không có đúng cùng mức phân tán điểm, nên cần xem cả số người và độ trải rộng của điểm trước khi kết luận về sự khác nhau của SE.

**Vì sao chọn cách này?** **SE (sai số chuẩn của trung bình)** mô tả **mức trung bình mẫu có thể thay đổi giữa những lần chọn mẫu tương tự**, khác với **độ lệch chuẩn SD** mô tả các điểm **của từng học viên** trải rộng đến đâu. `std(ddof=1)` ước lượng SD từ các điểm trong mẫu; chương trình tính SE từ SD ấy và **số người** của từng nhóm. Khi số người tăng mà mức phân tán giữ tương đương, SE thường giảm; nhưng chín người đầu và 18 người trong ví dụ có **SD khác nhau**, nên không thể chỉ nhìn cỡ mẫu rồi suy ra chắc chắn mức SE nào. Đây là phép minh họa từ điểm thang 30, không có dữ liệu quần thể thật để xác nhận độ chính xác tuyệt đối.

**Quy trình:**
1. Tạo 18 điểm gốc, lấy thêm tập con 9 điểm đầu.
2. Tính std mẫu (ddof=1) và SE cho cả hai tập.
3. Báo cả hai SE kèm số người và giải thích giới hạn so sánh.

```python
import numpy as np
scores = np.array([8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], dtype=float)
first9 = scores[:9]
se9 = first9.std(ddof=1)/np.sqrt(len(first9))
se18 = scores.std(ddof=1)/np.sqrt(len(scores))
if len(scores) != 18:
    raise ValueError("Cần đủ 18 điểm học viên.")
print("Tất cả học viên:", len(scores))
print("Nhóm con:", len(first9))
print(f"SE 9 người (điểm): {se9:.3f}")
print(f"SE 18 người (điểm): {se18:.3f}")
print("SE của hai nhóm khác nhau:", bool(not np.isclose(se9, se18)))
```

**Kết quả khi chạy:**

```text
Tất cả học viên: 18
Nhóm con: 9
SE 9 người (điểm): 0.913
SE 18 người (điểm): 1.258
SE của hai nhóm khác nhau: True
```

SE của 18 người **lớn hơn** trong dữ liệu cụ thể này vì độ phân tán cũng lớn hơn. Để chỉ quan sát tác động n, cần giữ độ phân tán như nhau.

### Tình huống 5 — Cấp 5: Bootstrap từ 20 phiếu giao để đo dao động trung bình

**Từ vựng trong mục:** **Bootstrap** — lấy mẫu lặp có hoàn lại; **Percentile interval** — khoảng phân vị.

**Tình huống thực tế:** Đơn vị vận chuyển có **20 thời gian hoàn tất phiếu giao**, tính bằng **phút**, từ 30 đến 55. Người quản lý muốn hình dung **trung bình của 20 phiếu có thể dao động bao nhiêu** nếu khảo sát những bộ mẫu tương tự. Vì chưa có dữ liệu bổ sung, nhóm dựng **2.000 mẫu bootstrap giả lập**, mỗi mẫu gồm **20 lần chọn lại từ đúng 20 phiếu hiện có, cho phép chọn trùng**, rồi xem vùng trung bình thấp/cao của 2.000 mẫu.

**Vì sao chọn cách này?** **Bootstrap** là cách **rút lại từ mẫu đã có**, tạo nhiều bộ mẫu giả để xem một thống kê như trung bình có thể biến động. `replace=True` cho phép cùng một phiếu xuất hiện **nhiều lần trong một bộ 20 lượt**, đúng chủ đích bootstrap chứ không phải lỗi trùng hồ sơ; nếu không hoàn lại, mọi bộ đủ 20 phiếu sẽ giống hệt bộ ban đầu về trung bình. `rng.choice(..., size=(2000, 20))` tạo **2.000 bộ giả lập**, rồi `mean(axis=1)` cho 2.000 trung bình; `np.quantile` lấy **mốc 2,5% và 97,5%** để tạo khoảng percentile minh họa. **Seed 18** cho kết quả tái lập, còn số 2.000 là số lượt mô phỏng được chọn để ổn định ước lượng chứ không phải có 2.000 phiếu thật hoặc bảo đảm khoảng luôn bao phủ đúng 95%.

**Quy trình:**
1. Tạo 20 phiếu có thời gian hợp lệ.
2. Rút 2.000 hàng mẫu, mỗi hàng chứa 20 giá trị có hoàn lại.
3. Tính mean của 2.000 hàng và hai phân vị biên, kiểm mean gốc ở trong khoảng minh họa.

```python
import numpy as np
minutes = np.array([30,32,33,34,35,36,38,39,40,41,42,43,44,45,46,47,49,50,51,55], dtype=float)
rng = np.random.default_rng(18)
bootstrap = rng.choice(minutes, size=(2000, len(minutes)), replace=True)
means = bootstrap.mean(axis=1)
low, high = np.quantile(means, [0.025, 0.975])
if len(minutes) != 20 or bootstrap.shape != (2000, 20):
    raise ValueError("Cần 20 phiếu và 2000 lượt lấy mẫu bootstrap.")
print("Phiếu gốc:", len(minutes))
print("Mẫu bootstrap:", len(means))
print(f"Mean gốc (phút): {minutes.mean():.2f}")
print(f"Khoảng bootstrap (phút): {low:.2f} – {high:.2f}")
print("Mean gốc trong khoảng:", bool(low <= minutes.mean() <= high))
```

**Kết quả khi chạy:**

```text
Phiếu gốc: 20
Mẫu bootstrap: 2000
Mean gốc (phút): 41.50
Khoảng bootstrap (phút): 38.65 – 44.45
Mean gốc trong khoảng: True
```

Đây là **ước lượng bất định từ mẫu quan sát**, không phải khoảng chứa 95% thời gian giao của từng phiếu.

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
