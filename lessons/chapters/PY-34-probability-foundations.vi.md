# PY-34 — Xác suất, không gian mẫu và biến cố


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Experiment** — phép thử; **Sample space** — không gian mẫu.

`Logic/Tập hợp → Xác suất → Bayes → Dự đoán bất định`

**Học xong dùng để làm gì?** Tính xác suất một sự kiện xảy ra và kiểm tra quy tắc của không gian mẫu.

**Kết nối kiến thức tiếp theo:** PY-35 tính xác suất khi đã có thông tin điều kiện và cập nhật bằng Bayes.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Khái niệm |
|---|---|---|
| Experiment | phép thử | Thao tác có kết quả quan sát được |
| Sample space | không gian mẫu | Tập mọi kết quả khả dĩ |
| Event | biến cố | Nhóm kết quả được quan tâm |
| Probability | xác suất | Mức khả năng xảy ra một biến cố, từ 0 tới 1 |

## 3. Hàm Python và tham số quan trọng

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm / cú pháp | Cách sử dụng |
|---|---|
| `len(event)/len(space)` | Xác suất cổ điển khi kết quả đồng khả năng |
| `random.choice(values)` | Rút một phần tử ngẫu nhiên từ danh sách |
| `np.random.default_rng(seed)` | Tạo bộ sinh ngẫu nhiên tái lập |
| `np.mean(condition)` | Ước lượng tỷ lệ đúng trong mô phỏng |

## 4. Khái niệm chính và liên quan

**Mạch kiến thức:** Từ một phép thử ta xác định không gian mẫu chứa mọi kết quả, chọn một tập con là biến cố, rồi mới tính xác suất dựa trên giả định đồng khả năng hoặc dựa vào phân phối đã biết. Mô phỏng cho tần suất quan sát, không thay thế xác suất lý thuyết.

### 4.1. Experiment — Phép thử và kết quả ngẫu nhiên

**Từ vựng:** **Experiment** — phép thử; **Outcome** — kết quả.

**Phép thử ngẫu nhiên** là thao tác có những kết quả khả dĩ biết trước, nhưng không biết chắc kết quả của **một lần thử**. Tung một đồng xu công bằng là ví dụ: kết quả có thể là ngửa hoặc sấp; mỗi lần chỉ xuất hiện một mặt. Để minh họa mà không in kết quả thất thường, tạo số ngẫu nhiên bằng `np.random.default_rng(seed)` giúp **tái lập cùng chuỗi giả ngẫu nhiên**, nhưng seed không biến thử nghiệm thành không ngẫu nhiên trong lý thuyết.

```python
# Mục đích: Phép thử và kết quả ngẫu nhiên.
import numpy as np

rng = np.random.default_rng(42)
print(rng.integers(0, 2, size=5).tolist())
```

**Kết quả khi chạy:**

```text
[0, 1, 1, 0, 0]
```

Năm kết quả mô phỏng 0/1 với seed 42 tái lập được trong phiên bản NumPy tương thích.

### 4.2. Sample space — Liệt kê toàn bộ kết quả có thể

**Từ vựng:** **Sample space** — không gian mẫu; **Outcome** — phần tử mẫu.

**Không gian mẫu** Ω chứa toàn bộ kết quả có thể của phép thử. Với xúc xắc sáu mặt chuẩn, Ω=`{1,2,3,4,5,6}`; mỗi số chỉ là **một kết quả**, chưa phải xác suất. Đếm `len(Ω)=6` cho biết số trường hợp khả dĩ. Chỉ khi xúc xắc **công bằng** ta mới giả định cả sáu mặt đồng xác suất `1/6`. Set không bảo đảm thứ tự hiển thị nên in qua `sorted()`.

```python
# Mục đích: Liệt kê toàn bộ kết quả có thể.
space = set(range(1, 7))
print(sorted(space))
```

**Kết quả khi chạy:**

```text
[1, 2, 3, 4, 5, 6]
```

Không gian mẫu của một lần gieo có sáu mặt, được sắp thứ tự để dễ đọc.

### 4.3. Event — Một nhóm kết quả quan tâm

**Từ vựng:** **Event** — biến cố; **Subset** — tập con.

**Biến cố** là một tập con của không gian mẫu. Khi gieo xúc xắc, biến cố `E = ra số chẵn` gồm `{2,4,6}`. Nó không phải một kết quả duy nhất: trong một lần gieo, E xảy ra nếu số được gieo **thuộc** Set E. Gọi `sorted(E)` để hiển thị rõ ba trường hợp; phép kiểm tra `4 in E` cho True.

```python
# Mục đích: Một nhóm kết quả quan tâm.
even = {2, 4, 6}
print(sorted(even))
```

**Kết quả khi chạy:**

```text
[2, 4, 6]
```

Biến cố ra số chẵn có ba kết quả thuận lợi trong sáu mặt xúc xắc.

### 4.4. Probability — Tỷ lệ khả năng dưới giả định

**Từ vựng:** **Probability** — xác suất; **Equally likely** — đồng khả năng.

**Xác suất** P(E) là số trong `[0,1]` đo khả năng của biến cố E. Khi các phần tử không gian mẫu **đồng khả năng**, `P(E)=số kết quả thuận lợi / số kết quả có thể`. Với xúc xắc công bằng, E là các mặt chẵn `{2,4,6}` nên `P(E)=3/6=0.5`. Nếu xúc xắc lệch, không thể dùng số mặt thuận lợi chia số mặt một cách máy móc: cần xác suất của từng mặt.

```python
# Mục đích: Tỷ lệ khả năng dưới giả định.
space = set(range(1, 7))
even = {2, 4, 6}
print(len(even) / len(space))
```

**Kết quả khi chạy:**

```text
0.5
```

Một lần gieo xúc xắc công bằng có xác suất 50% ra mặt chẵn.

## 5. Năm tình huống xác suất — từ vé đồng khả năng đến phân phối có trọng số

### Tình huống 1 — Cấp 1: Không gian mẫu gồm 10 vé quay thưởng có xác suất bằng nhau

**Từ vựng trong mục:** **Sample space** — không gian mẫu; **Event** — biến cố; **Equally likely** — đồng khả năng.

**Tình huống thực tế:** Quầy sự kiện chuẩn bị **10 vé** V01…V10, mỗi vé có màu Đỏ, Xanh hoặc Vàng và cơ hội được rút **bằng nhau**. Mỗi hàng là một chiếc vé cụ thể, không phải chỉ một loại màu. Người tổ chức cần tính xác suất rút trúng vé Xanh và đếm số kết quả thuận lợi.

**Vì sao chọn cách này?** Không gian mẫu gồm **10 vé**, kể cả khi hai vé cùng màu. Vì từng vé đồng khả năng, xác suất lấy vé Xanh bằng số vé Xanh chia tổng vé; không được chia 1/3 chỉ vì có ba màu.

**Quy trình:**
1. Lưu màu trên mười vé theo thứ tự mã.
2. Xác định biến cố `vé Xanh`, đếm vé thuộc biến cố.
3. Chia số vé thuận lợi cho tổng số vé khi giả định mọi vé như nhau.

```python
colors = ["Xanh","Đỏ","Xanh","Vàng","Đỏ","Xanh","Đỏ","Vàng","Xanh","Đỏ"]
blue = []
for i, color in enumerate(colors, 1):
    if color == "Xanh":
        blue.append(i)
if len(colors) != 10:
    raise ValueError("Cần đúng 10 vé theo màu.")
print("Vé:", len(colors))
print("Vé xanh:", len(blue))
print(f"P(rút xanh): {len(blue)/len(colors):.2f}")
```

**Kết quả khi chạy:**

```text
Vé: 10
Vé xanh: 4
P(rút xanh): 0.40
```

Nếu quay thưởng thiên vị một vé, phép đếm tỷ lệ này không còn là xác suất đúng; giả định đồng khả năng là điều kiện không thể bỏ qua.

### Tình huống 2 — Cấp 2: So tỷ lệ thực nghiệm từ 12 lần tung với lý thuyết

**Từ vựng trong mục:** **Frequency** — tần suất; **Probability** — xác suất; **Random experiment** — phép thử ngẫu nhiên.

**Tình huống thực tế:** Nhóm học viên ghi **12 kết quả tung đồng xu giả lập**, mỗi hàng là một lần: `N` nghĩa là ngửa, `S` là sấp. Giả định đồng xu công bằng cho xác suất lý thuyết P(ngửa)=0,5, nhưng số lần ngửa **quan sát** trên mẫu nhỏ không nhất thiết bằng một nửa. Cần tính tỷ lệ quan sát và so với 0,5.

**Vì sao chọn cách này?** Xác suất lý thuyết là mô hình dài hạn, còn tần suất trên 12 thử nghiệm là dữ liệu đã xảy ra; khác biệt ở một mẫu nhỏ không tự chứng minh đồng xu bị lệch.

**Quy trình:**
1. Lưu đúng 12 lượt kết quả.
2. Đếm ký hiệu N, lấy tỷ lệ chia 12.
3. In tỷ lệ quan sát và giả định lý thuyết để so sánh.

```python
observed = ["N","S","N","N","S","N","S","S","N","N","S","N"]
heads = 0
for item in observed:
    if item == "N":
        heads += 1
if len(observed) != 12:
    raise ValueError("Cần đủ 12 lượt quan sát tung đồng xu.")
print("Lượt tung:", len(observed))
print("Ngửa:", heads)
print(f"Tỷ lệ ngửa quan sát: {heads/len(observed):.3f}")
print("Xác suất lý thuyết: 0.500")
```

**Kết quả khi chạy:**

```text
Lượt tung: 12
Ngửa: 7
Tỷ lệ ngửa quan sát: 0.583
Xác suất lý thuyết: 0.500
```

Mẫu 12 lần chỉ minh họa **tần suất**, không thay thế toàn bộ xác suất lý thuyết của một đồng xu công bằng.

### Tình huống 3 — Cấp 3: Phân biệt 15 kết quả gieo hai xúc xắc với 36 khả năng

**Từ vựng trong mục:** **Outcome pair** — cặp kết quả; **Theoretical probability** — xác suất lý thuyết.

**Tình huống thực tế:** Nhóm QA ghi **15 lần gieo hai xúc xắc công bằng**, mỗi hàng là `(mặt xúc xắc 1, mặt xúc xắc 2)`. Quan tâm biến cố **tổng từ 9 trở lên**. Cần đếm trên 15 lượt đã ghi và tính xác suất lý thuyết từ **36 cặp mặt đồng khả năng**, rồi so hai giá trị.

**Vì sao chọn cách này?** Không gian mẫu lý thuyết của **một lần gieo hai xúc xắc** có 36 cặp, không phải 15 lượt quan sát. Phải giữ hai mẫu số khác nhau để không đánh đồng tần suất của mẫu với xác suất dựa trên 36 kết quả.

**Quy trình:**
1. Lưu 15 cặp kết quả được quan sát và đếm tổng >=9.
2. Liệt kê 36 cặp khả dĩ khi hai xúc xắc độc lập/công bằng.
3. Báo tỷ lệ quan sát và xác suất lý thuyết có nhãn riêng.

```python
from itertools import product
observations = [[1,1],[2,5],[3,6],[4,5],[6,6],[1,4],[5,5],[2,2],[4,6],[3,3],[6,2],[5,4],[1,6],[6,5],[2,4]]
space = list(product(range(1, 7), repeat=2))
observed_hits = 0
for a, b in observations:
    if a + b >= 9:
        observed_hits += 1
possible_hits = 0
for a, b in space:
    if a + b >= 9:
        possible_hits += 1
if len(observations) != 15 or len(space) != 36:
    raise ValueError("Cần 15 lượt quan sát và 36 khả năng khi tung hai xúc xắc.")
print("Lượt quan sát:", len(observations))
print("Quan sát tổng >=9:", observed_hits)
print(f"Tỷ lệ quan sát: {observed_hits/len(observations):.3f}")
print(f"Xác suất lý thuyết: {possible_hits/len(space):.3f}")
```

**Kết quả khi chạy:**

```text
Lượt quan sát: 15
Quan sát tổng >=9: 7
Tỷ lệ quan sát: 0.467
Xác suất lý thuyết: 0.278
```

Mười lăm lượt có thể có nhiều cặp lặp lại. Một phép thử có 36 cặp khả dĩ, còn bảng chỉ chứa 15 quan sát của những lần đã gieo.

### Tình huống 4 — Cấp 4: Ước lượng biến cố hợp và giao từ 18 lượt tiếp cận

**Từ vựng trong mục:** **Union** — phép hợp; **Intersection** — phép giao; **Inclusion–exclusion** — bao hàm–loại trừ.

**Tình huống thực tế:** Một chiến dịch ghi **18 khách hàng** U01…U18, mỗi hàng có cờ đã dùng ứng dụng (`app`) và đã nhận email (`email`). Xét khách chọn đều ngẫu nhiên trong chính **18 người của bảng minh họa**; cần ước lượng xác suất thuộc ít nhất một kênh, xác suất thuộc cả hai, và kiểm tra công thức bao hàm–loại trừ.

**Vì sao chọn cách này?** Biến cố app/email có thể xảy ra đồng thời trên cùng người. Cộng hai tỷ lệ mà không trừ phần giao sẽ đếm người dùng cả hai hai lần.

**Quy trình:**
1. Đếm số khách có từng cờ và số khách có cả hai.
2. Dùng `app or email` cho biến cố hợp, `app and email` cho giao.
3. So xác suất hợp trực tiếp với công thức hợp bằng hai tỷ lệ trừ giao.

```python
records = [{"id":"U01","app":False,"email":False},{"id":"U02","app":True,"email":True},{"id":"U03","app":True,"email":True},{"id":"U04","app":False,"email":True},{"id":"U05","app":True,"email":False},{"id":"U06","app":True,"email":True},{"id":"U07","app":False,"email":True},{"id":"U08","app":True,"email":True},{"id":"U09","app":True,"email":False},{"id":"U10","app":False,"email":True},{"id":"U11","app":True,"email":True},{"id":"U12","app":True,"email":True},{"id":"U13","app":False,"email":False},{"id":"U14","app":True,"email":True},{"id":"U15","app":True,"email":True},{"id":"U16","app":False,"email":True},{"id":"U17","app":True,"email":False},{"id":"U18","app":True,"email":True}]
app = 0
email = 0
both = 0
either = 0
for row in records:
    if row["app"]:
        app += 1
    if row["email"]:
        email += 1
    if row["app"] and row["email"]:
        both += 1
    if row["app"] or row["email"]:
        either += 1
if len(records) != 18 or app + email - both != either:
    raise ValueError("Cần 18 khách và phép đếm hợp tập hợp phải nhất quán.")
print("Khách:", len(records))
print("Cả hai kênh:", both)
print("Ít nhất một kênh:", either)
print(f"P(hợp): {either/len(records):.3f}")
print("Kiểm công thức:", either == app+email-both)
```

**Kết quả khi chạy:**

```text
Khách: 18
Cả hai kênh: 9
Ít nhất một kênh: 16
P(hợp): 0.889
Kiểm công thức: True
```

Đây là xác suất **khi chọn đều một khách từ danh sách 18 người này**, không tự suy ra tỷ lệ của tất cả khách ngoài danh sách.

### Tình huống 5 — Cấp 5: Hai mươi kết quả không đồng khả năng: xác suất có trọng số

**Từ vựng trong mục:** **Weighted outcome** — kết quả có trọng số; **Sampling distribution** — phân phối chọn; **Monte Carlo** — mô phỏng ngẫu nhiên.

**Tình huống thực tế:** Máy kiểm tra nhận **20 loại trạng thái** S01…S20, mỗi trạng thái mang trọng số xuất hiện từ 1 tới 20 (trọng số không phải số lần đo); trong mô phỏng này xác suất tỷ lệ với trọng số. Nhóm muốn biết xác suất xảy ra một trong **năm trạng thái S16–S20**, và đối chiếu 5.000 lượt rút mô phỏng có seed cố định. Không được chia đơn thuần 5/20 vì các trạng thái không đồng khả năng.

**Vì sao chọn cách này?** Phải chuẩn hóa 20 trọng số thành một phân phối có tổng 1 rồi cộng xác suất của đúng năm trạng thái. `default_rng(42)` giúp tái lập mô phỏng; tỷ lệ quan sát chỉ **xấp xỉ** xác suất lý thuyết chứ không được yêu cầu bằng chính xác.

**Quy trình:**
1. Tạo 20 trạng thái với trọng số 1–20, chuẩn hóa thành xác suất.
2. Cộng trọng số 5 trạng thái quan tâm rồi chia tổng.
3. Lấy 5.000 mẫu có seed 42, kiểm tần suất gần xác suất có trọng số.

```python
import numpy as np
weights = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], dtype=float)
probs = weights / weights.sum()
theoretical = float(probs[15:].sum())
rng = np.random.default_rng(42)
sampled = rng.choice(np.arange(20), size=5000, p=probs)
frequency = float(np.mean(sampled >= 15))
if len(weights) != 20 or not np.isclose(probs.sum(), 1):
    raise ValueError("Cần 20 trọng số và tổng xác suất bằng 1.")
print("Trạng thái:", len(weights))
print(f"P(S16–S20): {theoretical:.3f}")
print("Đồng khả năng 5/20:", f"{5/20:.3f}")
print("Mô phỏng gần lý thuyết:", abs(frequency-theoretical) < 0.03)
```

**Kết quả khi chạy:**

```text
Trạng thái: 20
P(S16–S20): 0.429
Đồng khả năng 5/20: 0.250
Mô phỏng gần lý thuyết: True
```

Tần suất 5.000 lượt phụ thuộc seed và có dao động ngẫu nhiên; **20 bản ghi** ở đây là các trạng thái khả dĩ, không phải 20 lượt mẫu.

## 6. Sai lầm thường gặp

- Phép thử không giống biến cố: phép thử tạo kết quả, biến cố là nhóm kết quả được quan tâm.
- Công thức số kết quả thuận lợi chia tổng kết quả chỉ đúng với các kết quả **đồng khả năng**.
- Trong mô phỏng, tỷ lệ quan sát có thể khác xác suất thật ngay cả khi seed cố định.
- `np.random.default_rng(seed)` giúp tái lập trong môi trường tương thích, không đảm bảo mẫu luôn đúng tỷ lệ lý thuyết.
- Set không có thứ tự cố định, nên in bằng `sorted` nếu cần đối chiếu đầu ra.
- Khi số mẫu tăng, độ dao động của ước lượng thường giảm, không bắt buộc mỗi lần chạy đều gần hơn.

## 7. Trắc nghiệm

**Q1. What is a random experiment? | Phép thử ngẫu nhiên là gì?**

A. A repeatable procedure with uncertain individual outcome | Thao tác lặp được nhưng kết quả mỗi lần không chắc chắn

B. Set of all possible outcomes | Tập tất cả kết quả có thể

C. A subset of the sample space | Một tập con của không gian mẫu

D. A measure between zero and one of an event's chance | Thước đo từ 0 đến 1 cho khả năng biến cố

**Đáp án: A**

**Giải thích:** Phép thử có thể sinh kết quả khác nhau.


**Q2. What is a sample space? | Không gian mẫu là gì?**

A. A repeatable procedure with uncertain individual outcome | Thao tác lặp được nhưng kết quả mỗi lần không chắc chắn

B. Set of all possible outcomes | Tập tất cả kết quả có thể

C. A subset of the sample space | Một tập con của không gian mẫu

D. A measure between zero and one of an event's chance | Thước đo từ 0 đến 1 cho khả năng biến cố

**Đáp án: B**

**Giải thích:** Không gian mẫu chứa mọi kết quả khả dĩ.


**Q3. What is an event? | Biến cố là gì?**

A. A repeatable procedure with uncertain individual outcome | Thao tác lặp được nhưng kết quả mỗi lần không chắc chắn

B. Set of all possible outcomes | Tập tất cả kết quả có thể

C. A subset of the sample space | Một tập con của không gian mẫu

D. A measure between zero and one of an event's chance | Thước đo từ 0 đến 1 cho khả năng biến cố

**Đáp án: C**

**Giải thích:** Biến cố là một nhóm kết quả.


**Q4. What is probability? | Xác suất là gì?**

A. A repeatable procedure with uncertain individual outcome | Thao tác lặp được nhưng kết quả mỗi lần không chắc chắn

B. Set of all possible outcomes | Tập tất cả kết quả có thể

C. A subset of the sample space | Một tập con của không gian mẫu

D. A measure between zero and one of an event's chance | Thước đo từ 0 đến 1 cho khả năng biến cố

**Đáp án: D**

**Giải thích:** Xác suất trong đoạn 0 đến 1.


**Q5. When does counting favorable outcomes over total outcomes work? | Khi nào chia số trường hợp thuận lợi cho tổng số trường hợp là đúng?**

A. When outcomes are equally likely | Khi các kết quả đồng khả năng

B. n values of zero or one | n giá trị 0 hoặc 1

C. Reproducible pseudorandom sequences | Chuỗi giả ngẫu nhiên tái lập

D. Fraction of True values | Tỷ lệ các phần tử True

**Đáp án: A**

**Giải thích:** Đếm cổ điển đòi hỏi các kết quả đồng khả năng.


**Q6. What does `rng.integers(0,2,size=n)` generate? | `rng.integers(0,2,size=n)` tạo gì?**

A. When outcomes are equally likely | Khi các kết quả đồng khả năng

B. n values of zero or one | n giá trị 0 hoặc 1

C. Reproducible pseudorandom sequences | Chuỗi giả ngẫu nhiên tái lập

D. Fraction of True values | Tỷ lệ các phần tử True

**Đáp án: B**

**Giải thích:** Cận trên 2 không lấy 2, chỉ còn 0 và 1.


**Q7. What does `default_rng(seed)` provide? | `default_rng(seed)` cung cấp gì?**

A. When outcomes are equally likely | Khi các kết quả đồng khả năng

B. n values of zero or one | n giá trị 0 hoặc 1

C. Reproducible pseudorandom sequences | Chuỗi giả ngẫu nhiên tái lập

D. Fraction of True values | Tỷ lệ các phần tử True

**Đáp án: C**

**Giải thích:** Seed điều khiển chuỗi giả ngẫu nhiên tái lập.


**Q8. What does `np.mean(mask)` compute for Boolean mask? | `np.mean(mask)` tính gì với mặt nạ Boolean?**

A. When outcomes are equally likely | Khi các kết quả đồng khả năng

B. n values of zero or one | n giá trị 0 hoặc 1

C. Reproducible pseudorandom sequences | Chuỗi giả ngẫu nhiên tái lập

D. Fraction of True values | Tỷ lệ các phần tử True

**Đáp án: D**

**Giải thích:** True tính như 1, False tính như 0.


**Q9. What is P(even) for a fair six-sided die? | Xác suất mặt chẵn của xúc xắc công bằng sáu mặt?**

A. `1/2` | `1/2`

B. 36 | 36

C. 4 | 4

D. Zero | Bằng 0

**Đáp án: A**

**Giải thích:** Ba trong sáu mặt là số chẵn.


**Q10. How many outcomes are possible with two ordered six-sided dice? | Hai xúc xắc sáu mặt theo cặp có thứ tự có bao nhiêu kết quả?**

A. `1/2` | `1/2`

B. 36 | 36

C. 4 | 4

D. Zero | Bằng 0

**Đáp án: B**

**Giải thích:** Hai xúc xắc có 6×6 cặp có thứ tự.


**Q11. How many ordered pairs of dice sum to nine? | Bao nhiêu cặp có thứ tự của hai xúc xắc có tổng 9?**

A. `1/2` | `1/2`

B. 36 | 36

C. 4 | 4

D. Zero | Bằng 0

**Đáp án: C**

**Giải thích:** Bốn cặp là (3,6), (4,5), (5,4), (6,3).


**Q12. What is the probability of the empty event? | Xác suất biến cố rỗng là gì?**

A. `1/2` | `1/2`

B. 36 | 36

C. 4 | 4

D. Zero | Bằng 0

**Đáp án: D**

**Giải thích:** Biến cố không thể có xác suất 0.


**Q13. What is the probability of the entire sample space? | Xác suất của cả không gian mẫu là gì?**

A. One | Bằng 1

B. `1-P(A)` | `1-P(A)`

C. No, sampling variation occurs | Không, có dao động do lấy mẫu

D. One die's result does not change probabilities of the other | Kết quả một xúc xắc không đổi xác suất của xúc xắc kia

**Đáp án: A**

**Giải thích:** Biến cố chắc chắn có xác suất 1.


**Q14. What is P(not A) in terms of P(A)? | P(không A) theo P(A) là gì?**

A. One | Bằng 1

B. `1-P(A)` | `1-P(A)`

C. No, sampling variation occurs | Không, có dao động do lấy mẫu

D. One die's result does not change probabilities of the other | Kết quả một xúc xắc không đổi xác suất của xúc xắc kia

**Đáp án: B**

**Giải thích:** Biến cố và biến cố đối có tổng xác suất 1.


**Q15. Does a simulation always equal the true probability exactly? | Tỷ lệ mô phỏng có luôn bằng xác suất thật?**

A. One | Bằng 1

B. `1-P(A)` | `1-P(A)`

C. No, sampling variation occurs | Không, có dao động do lấy mẫu

D. One die's result does not change probabilities of the other | Kết quả một xúc xắc không đổi xác suất của xúc xắc kia

**Đáp án: C**

**Giải thích:** Mẫu hữu hạn dao động quanh xác suất nền.


**Q16. What does independence of two dice mean? | Hai xúc xắc độc lập nghĩa là gì?**

A. One | Bằng 1

B. `1-P(A)` | `1-P(A)`

C. No, sampling variation occurs | Không, có dao động do lấy mẫu

D. One die's result does not change probabilities of the other | Kết quả một xúc xắc không đổi xác suất của xúc xắc kia

**Đáp án: D**

**Giải thích:** Độc lập nghĩa là một kết quả không đổi xác suất của biến cố còn lại.


**Q17. Why is printing a Set directly fragile for sample output? | Vì sao in trực tiếp Set khó đối chiếu đầu ra mẫu?**

A. Display order is not promised | Thứ tự hiển thị không được đảm bảo

B. That empirical frequency equals theoretical probability | Tần suất thực nghiệm đúng bằng xác suất lý thuyết

C. It tends to reduce sampling variability | Thường làm giảm dao động lấy mẫu

D. Its faces do not have equal probabilities | Các mặt không đồng xác suất

**Đáp án: A**

**Giải thích:** Set không bảo đảm thứ tự in.


**Q18. What does a fixed RNG seed not guarantee? | Seed RNG cố định không bảo đảm điều gì?**

A. Display order is not promised | Thứ tự hiển thị không được đảm bảo

B. That empirical frequency equals theoretical probability | Tần suất thực nghiệm đúng bằng xác suất lý thuyết

C. It tends to reduce sampling variability | Thường làm giảm dao động lấy mẫu

D. Its faces do not have equal probabilities | Các mặt không đồng xác suất

**Đáp án: B**

**Giải thích:** Seed giúp lặp lại mô phỏng nhưng không loại dao động.


**Q19. How does larger sample size generally affect estimate variability? | Tăng số mẫu thường ảnh hưởng độ dao động ước lượng thế nào?**

A. Display order is not promised | Thứ tự hiển thị không được đảm bảo

B. That empirical frequency equals theoretical probability | Tần suất thực nghiệm đúng bằng xác suất lý thuyết

C. It tends to reduce sampling variability | Thường làm giảm dao động lấy mẫu

D. Its faces do not have equal probabilities | Các mặt không đồng xác suất

**Đáp án: C**

**Giải thích:** Mẫu lớn thường ổn định tần suất tương đối hơn.


**Q20. Why can't a biased die use simple favorable-count ratios? | Vì sao xúc xắc lệch không dùng phép đếm mặt đơn giản?**

A. Display order is not promised | Thứ tự hiển thị không được đảm bảo

B. That empirical frequency equals theoretical probability | Tần suất thực nghiệm đúng bằng xác suất lý thuyết

C. It tends to reduce sampling variability | Thường làm giảm dao động lấy mẫu

D. Its faces do not have equal probabilities | Các mặt không đồng xác suất

**Đáp án: D**

**Giải thích:** Xác suất không đều cần cộng theo trọng số.

## 8. Liên hệ bài tiếp theo

`Logic/Tập hợp → Xác suất → Bayes → Dự đoán bất định`.
