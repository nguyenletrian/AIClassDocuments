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

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Xác suất ra mặt chẵn của xúc xắc · Cấp 1: Khái niệm và một phép đếm

**Tình huống thực tế:** Trò chơi sử dụng xúc xắc công bằng có sáu mặt đánh số 1 tới 6; người chơi thắng nếu ra mặt chẵn. Tính xác suất thắng trong một lần gieo.

**Vì sao chọn cách giải này?** Sáu mặt đồng khả năng nên xác suất cổ điển là số mặt chẵn chia sáu.

**Quy trình giải:**

1. Liệt kê không gian mẫu sáu mặt và biến cố {2,4,6}.
2. Đếm số kết quả thuận lợi, số kết quả có thể.
3. Chia hai số và in xác suất.

```python
# Mục đích: Xác suất ra mặt chẵn của xúc xắc.
space = set(range(1, 7))
even = {2, 4, 6}
print(len(even) / len(space))
```

**Kết quả khi chạy:**

```text
0.5
```

Xác suất thắng bằng 0.5 (50%) theo giả định xúc xắc công bằng.

**Bài thực hành nâng cấp — cấp 1/5:** Một lớp học có **10 thẻ/bản ghi** để rút ngẫu nhiên, mỗi thẻ mang số nguyên như code; thẻ `None` chưa có mã được loại khỏi không gian kết quả hợp lệ. Hãy liệt kê sample space và xác suất lấy số chẵn. Các mức sau tăng dữ liệu và thêm biến cố cần phối hợp, kiểm tra thiếu hoặc mô phỏng.

```python
import numpy as np
# Một dòng = 1 lá thẻ số trong hộp.
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
space = [x for x in values if x is not None]
result = sorted(space)
print("Số quan sát:",len(values))
print("Kết quả:",result)
```

**Đọc kết quả:** Dữ liệu ban đầu 10 hàng; mẫu số của phép xác suất phải đúng tập trường hợp có thể xảy ra theo điều kiện của bài.

### Tình huống 2 — Mô phỏng 1.000 lần tung đồng xu · Cấp 2: Xác suất cơ bản

**Tình huống thực tế:** Phòng thực hành mô phỏng 1.000 lần tung đồng xu công bằng, mã 1 là ngửa, mã 0 là sấp. Cần xem tỷ lệ ngửa quan sát được và hiểu vì sao nó có thể khác 0.5.

**Vì sao chọn cách giải này?** `default_rng(seed)` giúp kết quả tái lập và trung bình của dãy 0/1 bằng tỷ lệ mặt ngửa.

**Quy trình giải:**

1. Khởi tạo RNG seed 42.
2. Sinh 1.000 số 0 hoặc 1.
3. Tính tỷ lệ số 1 và làm tròn ba chữ số.

```python
# Mục đích: Mô phỏng 1.000 lần tung đồng xu.
import numpy as np

rng = np.random.default_rng(42)
tosses = rng.integers(0, 2, size=1000)
print(round(float(tosses.mean()), 3))
```

**Kết quả khi chạy:**

```text
0.509
```

Tỷ lệ mô phỏng khoảng 50.9%, không bắt buộc bằng xác suất lý thuyết 50%.

**Bài thực hành nâng cấp — cấp 2/5:** Một lớp học có **12 thẻ/bản ghi** để rút ngẫu nhiên, mỗi thẻ mang số nguyên như code; thẻ `None` chưa có mã được loại khỏi không gian kết quả hợp lệ. Hãy tính P(A) cho 12 lá thẻ và so với phép đếm. Các mức sau tăng dữ liệu và thêm biến cố cần phối hợp, kiểm tra thiếu hoặc mô phỏng.

```python
import numpy as np
# Một dòng = 1 lá thẻ số trong hộp.
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
space = [x for x in values if x is not None]
result = len([x for x in space if x%2==0])/len(space)
print("Số quan sát:",len(values))
print("Kết quả:",result)
```

**Đọc kết quả:** Dữ liệu ban đầu 12 hàng; mẫu số của phép xác suất phải đúng tập trường hợp có thể xảy ra theo điều kiện của bài.

### Tình huống 3 — Xác suất tổng hai xúc xắc bằng chín · Cấp 3: Sự kiện kết hợp

**Tình huống thực tế:** Hai xúc xắc công bằng được gieo độc lập. Mỗi kết quả là **cặp có thứ tự** `(a,b)`, mỗi giá trị từ 1 đến 6. Người chơi thắng nếu tổng hai mặt bằng 9.

**Vì sao chọn cách giải này?** Hai xúc xắc cho 6×6=36 cặp đồng khả năng, trong đó có bốn cặp cộng thành 9.

**Quy trình giải:**

1. Liệt kê mọi cặp a,b bằng hai vòng for.
2. Đếm những cặp có tổng bằng 9.
3. Chia cho 36 và làm tròn ba chữ số.

```python
# Mục đích: Xác suất tổng hai xúc xắc bằng chín.
pairs = [(a, b) for a in range(1, 7) for b in range(1, 7)]
valid = sum(a + b == 9 for a, b in pairs)
print(round(valid / len(pairs), 3))
```

**Kết quả khi chạy:**

```text
0.111
```

Có bốn cặp thắng trên 36 cặp, xác suất bằng khoảng 11.1%.

**Bài thực hành nâng cấp — cấp 3/5:** Một lớp học có **15 thẻ/bản ghi** để rút ngẫu nhiên, mỗi thẻ mang số nguyên như code; thẻ `None` chưa có mã được loại khỏi không gian kết quả hợp lệ. Hãy tính giao, hợp của hai sự kiện từ 15 lá thẻ. Các mức sau tăng dữ liệu và thêm biến cố cần phối hợp, kiểm tra thiếu hoặc mô phỏng.

```python
import numpy as np
# Một dòng = 1 lá thẻ số trong hộp.
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
space = [x for x in values if x is not None]
result = {'A':len({x for x in space if x%2==0})/len(space),'B':len({x for x in space if x>6})/len(space),'both':len({x for x in space if x%2==0 and x>6})/len(space),'either':len({x for x in space if x%2==0 or x>6})/len(space)}
print("Số quan sát:",len(values))
print("Kết quả:",result)
```

**Đọc kết quả:** Dữ liệu ban đầu 15 hàng; mẫu số của phép xác suất phải đúng tập trường hợp có thể xảy ra theo điều kiện của bài.

### Tình huống 4 — Ước lượng tỷ lệ sự kiện hiếm · Cấp 4: Trường hợp không đủ dữ liệu

**Tình huống thực tế:** Một ứng dụng giả lập 10.000 lượt, mỗi lượt có xác suất 0.2 phát sinh sự kiện và các lượt độc lập. Đội phân tích cần biết tỷ lệ thực tế trong một lần mô phỏng.

**Vì sao chọn cách giải này?** So sánh số ngẫu nhiên đều với 0.2 mô phỏng Bernoulli; trung bình Boolean là tỷ lệ sự kiện xảy ra.

**Quy trình giải:**

1. Khởi tạo RNG seed 1, sinh 10.000 số trong [0,1).
2. Đánh dấu sự kiện khi số nhỏ hơn 0.2.
3. Lấy trung bình và làm tròn ba chữ số.

```python
# Mục đích: Ước lượng tỷ lệ sự kiện hiếm.
import numpy as np

rng = np.random.default_rng(1)
events = rng.random(10000) < 0.2
print(round(float(events.mean()), 3))
```

**Kết quả khi chạy:**

```text
0.2
```

Tỷ lệ mô phỏng gần 20% theo giả định; seed cho kết quả có thể tái lập.

**Bài thực hành nâng cấp — cấp 4/5:** Một lớp học có **18 thẻ/bản ghi** để rút ngẫu nhiên, mỗi thẻ mang số nguyên như code; thẻ `None` chưa có mã được loại khỏi không gian kết quả hợp lệ. Hãy loại thẻ chưa rõ mã trước khi đếm xác suất. Các mức sau tăng dữ liệu và thêm biến cố cần phối hợp, kiểm tra thiếu hoặc mô phỏng.

```python
import numpy as np
# Một dòng = 1 lá thẻ số trong hộp.
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, 17, 18]
space = [x for x in values if x is not None]
result = {'valid':len(space),'unknown':sum(x is None for x in values),'p_even':sum(x%2==0 for x in space)/len(space)}
print("Số quan sát:",len(values))
print("Kết quả:",result)
```

**Đọc kết quả:** Dữ liệu ban đầu 18 hàng; mẫu số của phép xác suất phải đúng tập trường hợp có thể xảy ra theo điều kiện của bài.

### Tình huống 5 — So mô phỏng ít lượt và nhiều lượt · Cấp 5: Mô phỏng hoặc tổng hợp

**Tình huống thực tế:** Một đồng xu công bằng được mô phỏng hai nhóm liên tiếp: 100 lượt rồi 10.000 lượt, cùng bộ sinh seed 7. Cần so độ chênh lệch tỷ lệ mặt ngửa so với 0.5.

**Vì sao chọn cách giải này?** Số lượt lớn thường cho ước lượng ổn định hơn về mặt thống kê, nhưng không đảm bảo từng lần chạy đều gần hơn.

**Quy trình giải:**

1. Khởi tạo một RNG cố định seed 7.
2. Lần lượt sinh 100 và 10.000 lần, mỗi lần tính tỷ lệ mã 1.
3. In kích thước và tỷ lệ làm tròn ba chữ số.

```python
# Mục đích: So mô phỏng ít lượt và nhiều lượt.
import numpy as np

rng = np.random.default_rng(7)
for count in [100, 10000]:
    tosses = rng.integers(0, 2, size=count)
    print(count, round(float(tosses.mean()), 3))
```

**Kết quả khi chạy:**

```text
100 0.56
10000 0.493
```

Mẫu lớn ở lần chạy này gần 0.5 hơn, nhưng đó là quan sát mô phỏng chứ không phải định luật đúng cho mọi lần.

**Bài thực hành nâng cấp — cấp 5/5:** Một lớp học có **20 thẻ/bản ghi** để rút ngẫu nhiên, mỗi thẻ mang số nguyên như code; thẻ `None` chưa có mã được loại khỏi không gian kết quả hợp lệ. Hãy dùng mô phỏng bốc thẻ để đối chiếu xác suất lý thuyết. Các mức sau tăng dữ liệu và thêm biến cố cần phối hợp, kiểm tra thiếu hoặc mô phỏng.

```python
import numpy as np
# Một dòng = 1 lá thẻ số trong hộp.
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, 17, 18, 19, None]
space = [x for x in values if x is not None]
result = {'theory':sum(x%2==0 for x in space)/len(space),'simulation':round(float((np.random.default_rng(2026).choice(space,size=5000)%2==0).mean()),3),'samples':len(values)}
print("Số quan sát:",len(values))
print("Kết quả:",result)
```

**Đọc kết quả:** Dữ liệu ban đầu 20 hàng; mẫu số của phép xác suất phải đúng tập trường hợp có thể xảy ra theo điều kiện của bài.

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
