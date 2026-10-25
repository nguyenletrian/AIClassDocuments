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
# Mục đích: Mô phỏng năm phép thử 0/1 với seed cố định để học cách tái lập thí nghiệm.
# Dữ liệu: Mỗi lượt nhận 0 hoặc 1; seed 42 để chạy lại dãy số giả ngẫu nhiên.
# NumPy cung cấp bộ sinh ngẫu nhiên và ndarray.
import numpy as np

# default_rng(42) tạo bộ sinh riêng với seed 42 để tái lập mô phỏng; không làm cho xác suất thực thay đổi.
rng = np.random.default_rng(42)
# integers(low,high,size) sinh 5 số nguyên 0 hoặc 1; cận trên 2 KHÔNG được lấy.
# tolist() chuyển mảng kết quả sang list Python để hiển thị.
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
# Mục đích: Liệt kê không gian mẫu sáu mặt của xúc xắc.
# Dữ liệu: Không gian mẫu là các mặt 1,2,3,4,5,6; giả định đồng khả năng.
# range(1,7) sinh từ 1 đến 6, không lấy số 7.
# set() lưu tập kết quả không trùng, đây là không gian mẫu.
space = set(range(1, 7))
# sorted() tạo danh sách tăng dần để in; set tự nó không bảo đảm thứ tự.
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
# Mục đích: Biểu diễn tập biến cố các mặt chẵn của xúc xắc.
# Dữ liệu: Biến cố mặt chẵn gồm 2,4,6 trên tổng sáu mặt.
# Tập set chỉ chứa các mặt chẵn 2,4,6; là một biến cố con của không gian mẫu.
even = {2, 4, 6}
# sorted() sắp tập thành list ổn định để hiển thị.
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
# Mục đích: Tính xác suất lý thuyết gieo mặt chẵn trong sáu mặt đồng khả năng.
# Dữ liệu: Ba mặt chẵn trên sáu mặt đồng khả năng; xác suất là 3/6.
# range(1,7) tạo sáu mặt; số 7 không nằm trong kết quả.
# set() tạo tập không gian mẫu gồm sáu kết quả.
space = set(range(1, 7))
# Set {2,4,6} là biến cố mặt chẵn với ba kết quả thuận lợi.
even = {2, 4, 6}
# len() đếm 3 mặt chẵn và 6 mặt toàn bộ; chỉ được coi là P=3/6 khi các mặt đồng khả năng.
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

**Tình huống thực tế:** Quầy sự kiện chuẩn bị **10 chiếc vé V01–V10**, mỗi vé được ghi màu **Xanh, Đỏ hoặc Vàng**. Có **4 vé Xanh**; mọi chiếc vé có cơ hội được rút như nhau, kể cả các vé cùng màu. Người tổ chức muốn biết cơ hội lấy **một vé Xanh** khi rút ngẫu nhiên một vé, và vì sao có ba tên màu **không có nghĩa** mỗi màu đều có cơ hội một phần ba.

**Vì sao chọn cách này?** **Không gian mẫu** trong bài gồm **10 chiếc vé riêng biệt**, không phải chỉ ba tên màu; mỗi vé là một khả năng được chọn. **Biến cố** là yêu cầu đang xét, ở đây **rút trúng vé Xanh**. Vì mọi chiếc vé đồng khả năng, chương trình đếm các dòng có màu Xanh bằng vòng `for`, rồi lấy **số vé Xanh so với cả 10 vé**. Bốn vé Xanh cho cơ hội **0,4**, không phải **1/3**, vì số vé của từng màu khác nhau. Phải xác định **đơn vị được rút** trước khi chọn mẫu số xác suất.

**Quy trình:**
1. Lưu màu trên mười vé theo thứ tự mã.
2. Xác định biến cố `vé Xanh`, đếm vé thuộc biến cố.
3. Chia số vé thuận lợi cho tổng số vé khi giả định mọi vé như nhau.

```python
# Mục đích: Đếm vé màu xanh trong mười vé và tìm xác suất rút xanh.
# Dữ liệu: 10 vé có màu Xanh, Đỏ, Vàng; mỗi phần tử list là một vé, không phải một loại màu.
# Danh sách 10 vé, mỗi vị trí là một vé; màu trùng vẫn là hai vé riêng.
colors = ["Xanh","Đỏ","Xanh","Vàng","Đỏ","Xanh","Đỏ","Vàng","Xanh","Đỏ"]
# List rỗng để thu số thứ tự vé màu xanh.
blue = []
# enumerate(...,1) trả (số thứ tự từ 1,màu), khác chỉ số Python bắt đầu 0.
for i, color in enumerate(colors, 1):
    # Kiểm màu chính xác của từng vé, trả Boolean.
    if color == "Xanh":
        # append() lưu số thứ tự một vé xanh, không thêm màu duy nhất.
        blue.append(i)
# len() đếm tổng vé 10; len(blue) đếm số vé xanh.
if len(colors) != 10:
    # ValueError báo số lượt hoặc tính hợp lệ của phép thử không đạt điều kiện, tránh công bố xác suất sai.
    raise ValueError("Cần đúng 10 vé theo màu.")
# len() đếm tổng vé 10; len(blue) đếm số vé xanh.
print("Vé:", len(colors))
print("Vé xanh:", len(blue))
# len() đếm tổng vé 10; len(blue) đếm số vé xanh.
# Tỷ lệ vé xanh/tổng vé là xác suất nếu rút ngẫu nhiên đồng đều một vé; :.2f chỉ làm tròn khi in.
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

**Tình huống thực tế:** Lớp học có **12 kết quả tung đồng xu giả lập** theo thứ tự ghi nhận; `N` là **ngửa**, `S` là **sấp**. Trong mẫu này số lần ngửa không nhất thiết bằng số lần sấp, dù ta **giả định đồng xu công bằng** khi nói về xác suất lý thuyết. Học viên muốn đếm số lần ngửa đã thấy và so **tỷ lệ quan sát từ 12 lượt** với **xác suất lý thuyết 0,5**, không kết luận đồng xu hỏng chỉ từ một mẫu nhỏ.

**Vì sao chọn cách này?** **Xác suất lý thuyết** là cơ hội do mô hình đồng xu công bằng giả định, mỗi mặt có cùng khả năng. **Tần suất quan sát** là tỷ lệ thực sự nhìn thấy trong **12 lượt đã ghi**; mẫu nhỏ có thể lệch 0,5 do may rủi. Chương trình đếm mỗi chữ `N` rồi chia cho đúng **12 lượt**, sau đó in riêng con số **0,500** của giả định lý thuyết. Không lấy tỷ lệ thực nghiệm bằng chứng đồng xu chắc chắn thiên lệch hay hoàn toàn công bằng; cần nhiều bằng chứng hơn để đánh giá điều đó.

**Quy trình:**
1. Lưu đúng 12 lượt kết quả.
2. Đếm ký hiệu N, lấy tỷ lệ chia 12.
3. In tỷ lệ quan sát và giả định lý thuyết để so sánh.

```python
# Mục đích: Phân biệt tỷ lệ ngửa quan sát trong 12 lần tung và xác suất đồng xu công bằng.
# Dữ liệu: 12 kết quả N (ngửa) và S (sấp); tỷ lệ quan sát có thể lệch mức lý thuyết 0.5.
# 12 nhãn N/S là dữ liệu THỰC NGHIỆM, không phải số lần kỳ vọng lý thuyết.
observed = ["N","S","N","N","S","N","S","S","N","N","S","N"]
# Biến đếm lượt ngửa N, bắt đầu 0.
heads = 0
# Duyệt từng lần tung, không chỉ các nhãn khác nhau.
for item in observed:
    # So chính xác nhãn N để nhận lượt ngửa.
    if item == "N":
        # += 1 tăng số lần quan sát ngửa.
        heads += 1
# len() đếm 12 lần tung làm mẫu số của tỷ lệ thực nghiệm.
if len(observed) != 12:
    # ValueError báo số lượt hoặc tính hợp lệ của phép thử không đạt điều kiện, tránh công bố xác suất sai.
    raise ValueError("Cần đủ 12 lượt quan sát tung đồng xu.")
# len() đếm 12 lần tung làm mẫu số của tỷ lệ thực nghiệm.
print("Lượt tung:", len(observed))
print("Ngửa:", heads)
# len() đếm 12 lần tung làm mẫu số của tỷ lệ thực nghiệm.
# Số lượt ngửa trên 12 lượt là tần suất quan sát; khác xác suất lý thuyết 0.5 của xu công bằng.
print(f"Tỷ lệ ngửa quan sát: {heads/len(observed):.3f}")
# Số 0.500 được in sẵn theo GIẢ ĐỊNH xu công bằng, không được suy ra từ 12 lượt.
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

**Tình huống thực tế:** Đội kiểm thử ghi **15 lượt tung hai xúc xắc**, mỗi lượt có hai mặt hiện lên từ 1 đến 6. Họ quan tâm tình huống **tổng hai mặt ít nhất là 9**. Cần tính một tỷ lệ dựa trên **15 lượt thực sự ghi được**, rồi so với xác suất lý thuyết khi xét **đủ 36 cặp mặt** có thể xuất hiện trong một lần tung hai xúc xắc công bằng.

**Vì sao chọn cách này?** Mỗi lượt tung **hai xúc xắc** tạo một **cặp có thứ tự**: ví dụ (3,6) và (6,3) là hai kết quả khác nhau của hai viên được phân biệt. `itertools.product(range(1, 7), repeat=2)` liệt kê **36 cặp khả dĩ** của **một lượt**, từ đó đếm bao nhiêu cặp có tổng ít nhất 9 để tính xác suất lý thuyết. Danh sách `observations` lại chỉ có **15 lượt đã quan sát**, nên phải đếm trường hợp đạt trong danh sách ấy và chia cho **15**, không chia cho 36. Hai mẫu số trả lời hai câu hỏi khác nhau; một mẫu nhỏ không buộc phải khớp chính xác lý thuyết.

**Quy trình:**
1. Lưu 15 cặp kết quả được quan sát và đếm tổng >=9.
2. Liệt kê 36 cặp khả dĩ khi hai xúc xắc độc lập/công bằng.
3. Báo tỷ lệ quan sát và xác suất lý thuyết có nhãn riêng.

```python
# Mục đích: Đếm biến cố tổng hai xúc xắc từ 9 trở lên trong 15 quan sát và 36 khả năng lý thuyết.
# Dữ liệu: 15 lượt gieo cặp xúc xắc; không gian lý thuyết gồm 6×6=36 cặp có thứ tự.
# product() sinh tất cả tổ hợp có thứ tự từ các nhóm lựa chọn.
from itertools import product
# 15 cặp xúc xắc được quan sát thực tế, không đại diện toàn bộ 36 khả năng.
observations = [[1,1],[2,5],[3,6],[4,5],[6,6],[1,4],[5,5],[2,2],[4,6],[3,3],[6,2],[5,4],[1,6],[6,5],[2,4]]
# repeat=2 tạo hai vị trí xúc xắc từ 1..6, có 6×6=36 cặp có thứ tự; list() hiện thực iterator.
space = list(product(range(1, 7), repeat=2))
observed_hits = 0
# Tách hai mặt của từng lượt quan sát.
for a, b in observations:
    # Biến cố tổng của HAI mặt ít nhất bằng 9, so từng cặp.
    if a + b >= 9:
        # Tăng số lần biến cố xuất hiện trong dữ liệu 15 lượt.
        observed_hits += 1
possible_hits = 0
# Duyệt TOÀN BỘ 36 khả năng để đếm theo lý thuyết.
for a, b in space:
    # Biến cố tổng của HAI mặt ít nhất bằng 9, so từng cặp.
    if a + b >= 9:
        # Đếm số kết quả thuận lợi trong không gian 36 cặp.
        possible_hits += 1
# len() đếm số lượt quan sát thực nghiệm, ở đây 15.
# len() đếm số cặp lý thuyết, phải bằng 36.
if len(observations) != 15 or len(space) != 36:
    # ValueError báo số lượt hoặc tính hợp lệ của phép thử không đạt điều kiện, tránh công bố xác suất sai.
    raise ValueError("Cần 15 lượt quan sát và 36 khả năng khi tung hai xúc xắc.")
# len() đếm số lượt quan sát thực nghiệm, ở đây 15.
print("Lượt quan sát:", len(observations))
print("Quan sát tổng >=9:", observed_hits)
# len() đếm số lượt quan sát thực nghiệm, ở đây 15.
# Tỷ lệ quan sát có thể lệch xác suất lý thuyết vì chỉ có 15 lượt.
print(f"Tỷ lệ quan sát: {observed_hits/len(observations):.3f}")
# len() đếm số cặp lý thuyết, phải bằng 36.
# Đếm kết quả thuận lợi trên 36 cặp đồng khả năng, cho xác suất lý thuyết.
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

**Tình huống thực tế:** Chiến dịch marketing ghi **18 khách U01–U18**, mỗi người có hai trạng thái đúng/sai: đã dùng **ứng dụng** và đã nhận **email**. Một khách có thể dùng cả hai kênh. Khi chọn ngẫu nhiên một khách trong đúng 18 người của bảng, quản lý muốn biết cơ hội khách ấy thuộc **ít nhất một kênh**, cơ hội thuộc **cả hai kênh**, và kiểm tra rằng số người dùng hai kênh không bị cộng trùng.

**Vì sao chọn cách này?** **Biến cố hợp** là khách xuất hiện ở **ít nhất một** trong hai nhóm ứng dụng/email; **biến cố giao** là khách có ở **cả hai nhóm**. `or` kiểm hợp, `and` kiểm giao trên **từng người**, tránh nhầm giữa các khách. Để tính số người thuộc hợp, lấy **số người dùng app cộng số người nhận email**, rồi **trừ phần giao một lần**, vì người thuộc cả hai đã bị cộng hai lần. Chương trình cũng đếm trực tiếp bằng `or` để kiểm lại, sau đó chia theo **18 khách được chọn đồng khả năng trong bảng**. Đây là xác suất theo **mẫu 18 người**, không mặc nhiên suy ra toàn bộ khách hàng ngoài chiến dịch.

**Quy trình:**
1. Đếm số khách có từng cờ và số khách có cả hai.
2. Dùng `app or email` cho biến cố hợp, `app and email` cho giao.
3. So xác suất hợp trực tiếp với công thức hợp bằng hai tỷ lệ trừ giao.

```python
# Mục đích: Tính xác suất khách dùng ít nhất một kênh app/email bằng nguyên lý cộng-trừ giao.
# Dữ liệu: 18 hồ sơ khách có hai cờ Boolean app/email; khách dùng hai kênh không được đếm hai lần.
# 18 dictionary, mỗi hồ sơ khách có hai cờ dùng app/email, có thể cùng True.
records = [{"id":"U01","app":False,"email":False},{"id":"U02","app":True,"email":True},{"id":"U03","app":True,"email":True},{"id":"U04","app":False,"email":True},{"id":"U05","app":True,"email":False},{"id":"U06","app":True,"email":True},{"id":"U07","app":False,"email":True},{"id":"U08","app":True,"email":True},{"id":"U09","app":True,"email":False},{"id":"U10","app":False,"email":True},{"id":"U11","app":True,"email":True},{"id":"U12","app":True,"email":True},{"id":"U13","app":False,"email":False},{"id":"U14","app":True,"email":True},{"id":"U15","app":True,"email":True},{"id":"U16","app":False,"email":True},{"id":"U17","app":True,"email":False},{"id":"U18","app":True,"email":True}]
# Đếm người dùng app theo hồ sơ, không phải số lượt truy cập.
app = 0
# Đếm người dùng email.
email = 0
# Đếm phần giao, khách dùng CẢ app và email.
both = 0
# Đếm phần hợp, khách dùng ít nhất một kênh.
either = 0
# Duyệt từng khách một lần.
for row in records:
    # Tra cờ Boolean của app; True nghĩa khách dùng app.
    if row["app"]:
        app += 1
    # Tra cờ Boolean của email; True nghĩa khách dùng email.
    if row["email"]:
        email += 1
    # Tra cờ Boolean của app; True nghĩa khách dùng app.
    # Tra cờ Boolean của email; True nghĩa khách dùng email.
    # and True khi cả hai cờ cùng đúng, chính là giao A∩B.
    if row["app"] and row["email"]:
        both += 1
    # Tra cờ Boolean của app; True nghĩa khách dùng app.
    # Tra cờ Boolean của email; True nghĩa khách dùng email.
    # or True khi có ít nhất một cờ đúng, chính là hợp A∪B.
    if row["app"] or row["email"]:
        either += 1
# Nguyên lý cộng-trừ giao: cộng hai nhóm rồi trừ khách đã bị đếm hai lần.
if len(records) != 18 or app + email - both != either:
    # ValueError báo số lượt hoặc tính hợp lệ của phép thử không đạt điều kiện, tránh công bố xác suất sai.
    raise ValueError("Cần 18 khách và phép đếm hợp tập hợp phải nhất quán.")
print("Khách:", len(records))
print("Cả hai kênh:", both)
print("Ít nhất một kênh:", either)
# Số khách thuộc hợp chia tổng 18 khách cho xác suất thực nghiệm dùng ít nhất một kênh.
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

**Tình huống thực tế:** Máy kiểm thử có **20 loại trạng thái S01–S20** nhưng **không xuất hiện đều như nhau**. Mỗi trạng thái được gán **trọng số 1 đến 20**: trọng số càng lớn thì cơ hội được rút càng cao; đây là **mức ưu tiên mô phỏng**, không phải số lần đo. Nhóm muốn biết xác suất rút một trạng thái trong **S16–S20**, rồi dùng **5.000 lần rút giả lập** với **seed 42** để xem tỷ lệ mô phỏng có gần xác suất lý thuyết không.

**Vì sao chọn cách này?** Vì **20 trạng thái có trọng số khác nhau**, không thể coi mỗi trạng thái có cơ hội như nhau. **Chuẩn hóa** là chia từng trọng số cho **tổng trọng số**, tạo một **phân phối xác suất** có tổng bằng 1. Chương trình cộng riêng phần xác suất của **năm trạng thái S16–S20** để có xác suất lý thuyết; cách lấy 5/20 sẽ sai vì bỏ qua trọng số. `np.random.default_rng(42)` dùng **seed 42** để lần chạy lại cùng code cho kết quả mô phỏng tái lập được; `rng.choice(..., size=5000, p=probs)` rút **5.000 lần có trọng số** nhằm nhìn tần suất dài hạn hơn 20 lượt, chứ **không phải có thêm 5.000 mẫu dữ liệu thật**. Tần suất gần lý thuyết là điều có thể kỳ vọng, **không bắt buộc trùng hoàn toàn** và không dùng 5.000 như một hằng số toán học.

**Quy trình:**
1. Tạo 20 trạng thái với trọng số 1–20, chuẩn hóa thành xác suất.
2. Cộng trọng số 5 trạng thái quan tâm rồi chia tổng.
3. Lấy 5.000 mẫu có seed 42, kiểm tần suất gần xác suất có trọng số.

```python
# Mục đích: Lấy mẫu từ 20 trạng thái có xác suất không đều và so tần suất mô phỏng với lý thuyết.
# Dữ liệu: 20 trạng thái có trọng số 1..20; chỉ số 15..19 ứng với S16..S20, 5.000 lần rút thử.
# NumPy tạo phân phối trọng số và thực hiện mô phỏng rút ngẫu nhiên.
import numpy as np
# 20 trọng số 1..20 theo trạng thái S01..S20, dtype=float cho phép chia để chuẩn hóa.
weights = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], dtype=float)
# weights.sum() cộng tất cả trọng số; chia từng trọng số cho tổng để được xác suất có tổng 1.
probs = weights / weights.sum()
# [15:] lấy chỉ số từ 15 đến cuối, tức năm trạng thái S16..S20; .sum() tính xác suất lý thuyết.
theoretical = float(probs[15:].sum())
# Generator với seed 42 giúp chạy lại thí nghiệm mô phỏng.
rng = np.random.default_rng(42)
# arange(20) tạo chỉ số 0..19, không chứa 20.
# choice(các_trạng_thái,size=5000,p=probs) chọn 5.000 lần có hoàn lại theo phân phối trọng số, KHÔNG đồng khả năng.
sampled = rng.choice(np.arange(20), size=5000, p=probs)
# Tạo mask Boolean cho các trạng thái có chỉ số 15..19.
# mean() trên mask True/False là tỷ lệ lượt mô phỏng rơi vào S16..S20.
frequency = float(np.mean(sampled >= 15))
# isclose() kiểm tổng xác suất gần 1 trong dung sai số thực, tránh so == tuyệt đối.
if len(weights) != 20 or not np.isclose(probs.sum(), 1):
    # ValueError báo số lượt hoặc tính hợp lệ của phép thử không đạt điều kiện, tránh công bố xác suất sai.
    raise ValueError("Cần 20 trọng số và tổng xác suất bằng 1.")
print("Trạng thái:", len(weights))
print(f"P(S16–S20): {theoretical:.3f}")
# Tỷ lệ 5/20 giả sử đồng khả năng, dùng so với phân phối thực tế có trọng số không đều.
print("Đồng khả năng 5/20:", f"{5/20:.3f}")
# abs() lấy độ lệch mô phỏng-lý thuyết; 0.03 là ngưỡng chấp nhận minh họa, KHÔNG bảo đảm mọi lần mô phỏng đều đạt.
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
