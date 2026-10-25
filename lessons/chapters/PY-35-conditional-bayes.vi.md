# PY-35 — Xác suất có điều kiện, Bayes và xác suất toàn phần


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Conditional probability** — xác suất có điều kiện; **Independence** — độc lập.

`Biến cố → Điều kiện → Bayes → Đánh giá mô hình AI`

**Học xong dùng để làm gì?** Cập nhật xác suất dựa trên kết quả xét nghiệm hoặc tín hiệu mới, phân biệt xác suất tiên nghiệm/hậu nghiệm.

**Kết nối kiến thức tiếp theo:** PY-36 mô tả mọi kết quả có thể xảy ra bằng phân phối xác suất.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Khái niệm |
|---|---|---|
| Conditional probability | xác suất có điều kiện | Khả năng A xảy ra khi biết B đã xảy ra |
| Independence | độc lập | Hai biến cố không ảnh hưởng xác suất của nhau |
| Bayes theorem | định lý Bayes | Cập nhật xác suất giả thuyết khi có bằng chứng |
| Total probability | xác suất toàn phần | Cộng xác suất qua các nhóm loại trừ và đủ |

## 3. Công thức và cách gọi bằng Python

**Từ vựng:** **Event** — biến cố; **Prior** — xác suất trước bằng chứng; **Posterior** — xác suất sau bằng chứng.

| Công thức / cú pháp | Cách hiểu |
|---|---|
| `P(A given B) = P(A and B) / P(B)` | Xác suất có điều kiện khi `P(B)>0` |
| `P(A and B) = P(A given B) * P(B)` | Quy tắc nhân xác suất |
| `posterior = likelihood * prior / evidence` | Bayes với xác suất bằng chứng khác 0 |
| `sum(group_share * group_rate)` | Xác suất toàn phần qua các nhóm rời và phủ đủ |

## 4. Khái niệm chính và liên quan

**Mạch kiến thức:** Trước hết xác định nhóm điều kiện B để tính P(A khi B). Khi hai biến cố độc lập, biết B không đổi xác suất của A. Khi có bằng chứng mới, Bayes tính lại xác suất giả thuyết; xác suất toàn phần giúp tính tỷ lệ chung từ các nhóm có tỷ trọng khác nhau.

### 4.1. Conditional probability — Thu hẹp mẫu nền

**Từ vựng:** **Conditional probability** — xác suất có điều kiện; **Conditioning event** — biến cố điều kiện.

**Xác suất có điều kiện** `P(A given B)` chỉ xét những trường hợp **B đã xảy ra**, không còn xét toàn bộ quần thể ban đầu. Ví dụ trong 100 khách **đã xem quảng cáo** có 20 người mua. Khi đó P(mua **khi đã xem**) = 20/100 = 0.2, không phải tỷ lệ mua của tất cả khách. Công thức `P(A given B) = P(A∩B)/P(B)` chỉ dùng khi `P(B)>0`. Tỷ lệ này **không tự chứng minh** xem quảng cáo đã gây ra hành vi mua.

**No Note — Không chú thích**

```python
seen = 100
bought = 20
print(bought / seen)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tính tỷ lệ mua trong tập người đã xem bằng cách lấy số mua chia số đã xem.
# Dữ liệu: 100 người đã xem trang và có 20 người mua trong nhóm đã xem; P(mua|xem)=20/100.
# Mẫu nền gồm 100 lượt ĐÃ XEM, không phải toàn bộ khách hàng trên hệ thống.
seen = 100
# Có 20 lượt mua TRONG nhóm đã xem.
bought = 20
# P(mua|đã xem) bằng số mua trong nhóm đã xem chia số người đã xem; 0.2 = 20%.
print(bought / seen)
```

**Kết quả khi chạy:**

```text
0.2
```

Trong nhóm 100 người đã xem quảng cáo, tỷ lệ mua quan sát được bằng 20%.

### 4.2. Independence — Không làm đổi xác suất của nhau

**Từ vựng:** **Independence** — độc lập; **Joint probability** — xác suất đồng thời.

Hai biến cố A và B **độc lập** nếu biết B xảy ra không đổi khả năng của A: `P(A given B)=P(A)` (khi P(B)>0). Tương đương `P(A∩B)=P(A)×P(B)`. Giả sử P(A)=0.5 và P(B)=0.4 thì nếu độc lập, P(cả A và B)=0.2. Trong dữ liệu thực, việc hai tỷ lệ gần nhau chưa tự chứng minh độc lập; cần biết cách lấy mẫu và đo sai số.

**No Note — Không chú thích**

```python
p_a = 0.5
p_b = 0.4
print(round(p_a * p_b, 3))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Nhân xác suất hai sự kiện chỉ khi giả định chúng độc lập.
# Dữ liệu: Hai sự kiện giả định độc lập với P(A)=0.5 và P(B)=0.4.
# Xác suất riêng của sự kiện A là 0.5 (50%).
p_a = 0.5
# Xác suất riêng của sự kiện B là 0.4 (40%).
p_b = 0.4
# Chỉ nhân P(A)×P(B) để ra P(A∩B) khi hai sự kiện ĐỘC LẬP; round(...,3) để in ba chữ số lẻ.
print(round(p_a * p_b, 3))
```

**Kết quả khi chạy:**

```text
0.2
```

Nếu hai biến cố độc lập thì giao của chúng có xác suất 0.2.

### 4.3. Bayes theorem — Cập nhật từ bằng chứng

**Từ vựng:** **Prior** — tỷ lệ nền trước bằng chứng; **Likelihood** — khả năng bằng chứng khi giả thuyết đúng; **Posterior** — xác suất sau bằng chứng.

Định lý **Bayes** trả lời “khi đã thấy **tín hiệu dương**, xác suất thực sự có lỗi là bao nhiêu?” Ví dụ chỉ 1% sản phẩm lỗi; máy báo dương với 99% hàng lỗi (**độ nhạy**) và 5% hàng không lỗi (**dương giả**). Trên 10.000 sản phẩm giả định có 100 lỗi: khoảng 99 dương thật, nhưng 495 dương giả từ 9.900 hàng tốt. Tổng dương là 594, nên xác suất lỗi khi máy báo dương là `99/594 ≈ 0.167`, **không phải 99%**. Tỷ lệ nền quyết định nhiều đến kết luận.

**No Note — Không chú thích**

```python
prior = 0.01
sensitivity = 0.99
false_positive = 0.05
positive = sensitivity * prior + false_positive * (1 - prior)
print(round(sensitivity * prior / positive, 3))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Cập nhật xác suất sự kiện hiếm sau kết quả xét nghiệm dương bằng Bayes.
# Dữ liệu: Tỷ lệ nền 1%, xét nghiệm phát hiện 99% ca có bệnh, báo dương giả 5% ở người không bệnh; dữ liệu chỉ để minh họa.
# prior là xác suất nền (1%) TRƯỚC khi biết kết quả xét nghiệm.
prior = 0.01
# Sensitivity = P(dương|thật sự có), ở đây 0.99.
sensitivity = 0.99
# False-positive rate = P(dương|thật sự không có), ở đây 0.05, khác tỷ lệ dự đoán dương sai tính theo cảnh báo.
false_positive = 0.05
# Luật xác suất toàn phần: P(dương) gồm dương thật trong nhóm có bệnh và dương giả trong nhóm không bệnh.
positive = sensitivity * prior + false_positive * (1 - prior)
# Bayes: P(có|dương)=P(dương|có)×P(có)/P(dương), không phải 0.99; round(...,3) chỉ làm tròn khi in.
print(round(sensitivity * prior / positive, 3))
```

**Kết quả khi chạy:**

```text
0.167
```

Sau tín hiệu dương, xác suất lỗi khoảng 16,7% theo các giả định đã nêu.

### 4.4. Total probability — Cộng qua các nhóm đầy đủ

**Từ vựng:** **Total probability** — xác suất toàn phần; **Partition** — phân hoạch.

Nếu quần thể được chia thành các **nhóm rời nhau và phủ đủ**, xác suất chung là trung bình có trọng số của xác suất trong nhóm. Ví dụ 60% khách ở nhóm X, trong đó 80% ủng hộ, còn 40% ở nhóm Y với tỷ lệ ủng hộ 20%. Tỷ lệ chung là `0.6×0.8 + 0.4×0.2 = 0.56`. Không cộng trực tiếp 80% và 20%, vì hai nhóm có quy mô khác nhau. Tổng xác suất các nhóm phải bằng 1.

**No Note — Không chú thích**

```python
shares = [0.6, 0.4]
support = [0.8, 0.2]
total = 0
for share, probability in zip(shares, support):
    total += share * probability
print(round(total, 3))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Cộng tỷ lệ xảy ra của hai nhóm có trọng số để tính xác suất toàn phần.
# Dữ liệu: Hai nhóm chiếm tỷ trọng 60%/40%, tỷ lệ hỗ trợ 80%/20% tương ứng.
# Hai phần tỷ trọng 0.6 và 0.4 của hai nhóm, tổng phải bằng 1.
shares = [0.6, 0.4]
# Hai xác suất hỗ trợ riêng trong từng nhóm, theo đúng thứ tự shares.
support = [0.8, 0.2]
# Bắt đầu tổng đóng góp xác suất của các nhóm bằng 0.
total = 0
# zip() ghép phần tỷ trọng và xác suất hỗ trợ của CÙNG nhóm theo vị trí.
for share, probability in zip(shares, support):
    # Mỗi lượt lấy tỷ trọng nhóm × xác suất trong nhóm, += cộng lại thành xác suất toàn phần.
    total += share * probability
# round(...,3) làm tròn kết quả cuối chỉ để trình bày.
print(round(total, 3))
```

**Kết quả khi chạy:**

```text
0.56
```

Xác suất chung là 56%, được tính theo tỷ trọng mỗi nhóm.

## 5. Năm tình huống Xác suất có điều kiện — từ lọc nhóm đến Bayes theo dây chuyền

### Tình huống 1 — Cấp 1: Tính tỷ lệ mua có điều kiện từ 10 khách

**Từ vựng trong mục:** **Conditional probability** — xác suất có điều kiện; **Condition** — điều kiện.

**Tình huống thực tế:** Quầy giới thiệu hàng ghi **10 khách K01–K10**, mỗi người có hai trạng thái: **đã xem giới thiệu** sản phẩm hay chưa và **đã mua** hay chưa. Một số người không xem vẫn mua; một số người đã xem nhưng không mua. Nhân viên muốn biết **trong những khách đã xem, bao nhiêu phần đã mua**, chứ không hỏi tỷ lệ mua trong cả 10 khách và cũng chưa kết luận xem giới thiệu là nguyên nhân họ mua.

**Vì sao chọn cách này?** **Xác suất có điều kiện** nghĩa là ta chỉ xét cơ hội xảy ra một việc **trong một nhóm đã biết trước điều kiện**. Ở đây điều kiện là `viewed=True`, nên chương trình lọc khách **đã xem** trước, rồi mới đếm `bought=True` **trong nhóm ấy**. Mẫu số là **số khách đã xem**, không phải cả 10 người. Khách chưa xem nhưng vẫn mua không thuộc phép tính này, dù vẫn nằm trong dữ liệu gốc. Đây là **tỷ lệ ghi nhận từ bảng mẫu**, không chứng minh việc xem giới thiệu **gây ra** hành vi mua.

**Quy trình:**
1. Lưu cờ xem/mua cho cả 10 khách.
2. Chỉ lấy hàng `viewed=True` để xác định mẫu nền.
3. Đếm người mua trong nhóm đã xem và tính tỷ lệ có điều kiện.

**No Note — Không chú thích**

```python
records = [{"id":"K01","viewed":True,"bought":True},{"id":"K02","viewed":True,"bought":False},{"id":"K03","viewed":True,"bought":True},{"id":"K04","viewed":False,"bought":False},{"id":"K05","viewed":True,"bought":True},{"id":"K06","viewed":True,"bought":False},{"id":"K07","viewed":True,"bought":False},{"id":"K08","viewed":False,"bought":True},{"id":"K09","viewed":True,"bought":False},{"id":"K10","viewed":False,"bought":False}]
viewed = []
for row in records:
    if row["viewed"]:
        viewed.append(row)
bought_after_viewing = 0
for row in viewed:
    if row["bought"]:
        bought_after_viewing += 1
if len(records) != 10 or not viewed:
    raise ValueError("Cần 10 khách và ít nhất một khách đã xem.")
print("Khách:", len(records))
print("Đã xem:", len(viewed))
print("Mua trong nhóm xem:", bought_after_viewing)
print(f"P(mua|đã xem): {bought_after_viewing/len(viewed):.3f}")
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Đếm P(mua | đã xem) trong 10 hồ sơ thay vì lấy toàn bộ 10 người làm mẫu số.
# Dữ liệu: Mười khách có cờ viewed và bought; có khách mua mà chưa ghi nhận viewed, nên chỉ tính trong nhóm viewed.
# 10 dictionary khách, mỗi bản ghi có hai cờ viewed/bought; có người mua nhưng không viewed.
records = [{"id":"K01","viewed":True,"bought":True},{"id":"K02","viewed":True,"bought":False},{"id":"K03","viewed":True,"bought":True},{"id":"K04","viewed":False,"bought":False},{"id":"K05","viewed":True,"bought":True},{"id":"K06","viewed":True,"bought":False},{"id":"K07","viewed":True,"bought":False},{"id":"K08","viewed":False,"bought":True},{"id":"K09","viewed":True,"bought":False},{"id":"K10","viewed":False,"bought":False}]
# Danh sách sẽ chỉ chứa hồ sơ đã xem, là MẪU ĐIỀU KIỆN.
viewed = []
# Duyệt một lượt toàn bộ 10 khách để lọc nhóm xem.
for row in records:
    # Tra cờ đã xem True/False từ dictionary, không dựa vào cờ mua.
    if row["viewed"]:
        # append() giữ toàn bộ dict của khách đã xem để xét mua trong nhóm này.
        viewed.append(row)
# Biến đếm số khách mua TRONG nhóm đã xem.
bought_after_viewing = 0
# Chỉ duyệt các khách thỏa viewed=True, không lấy 10 khách làm mẫu số.
for row in viewed:
    # Đọc cờ mua của khách thuộc nhóm đã xem.
    if row["bought"]:
        # +=1 tăng số khách vừa xem vừa mua.
        bought_after_viewing += 1
# Kiểm đủ 10 khách đầu vào.
# List rỗng được xem là False; not viewed bắt thiếu nhóm điều kiện, tránh chia 0.
if len(records) != 10 or not viewed:
    # ValueError báo thiếu mẫu hợp lệ hoặc nhóm điều kiện rỗng; không nên tiếp tục chia cho số mẫu sai.
    raise ValueError("Cần 10 khách và ít nhất một khách đã xem.")
print("Khách:", len(records))
print("Đã xem:", len(viewed))
print("Mua trong nhóm xem:", bought_after_viewing)
# Lấy số mua trong nhóm đã xem chia CHỈ số khách đã xem; :.3f hiển thị xác suất ba chữ số thập phân.
print(f"P(mua|đã xem): {bought_after_viewing/len(viewed):.3f}")
```

**Kết quả khi chạy:**

```text
Khách: 10
Đã xem: 7
Mua trong nhóm xem: 3
P(mua|đã xem): 0.429
```

Đây là tỷ lệ trên **10 khách mẫu giả lập**, không phải kết quả chứng minh quan hệ nhân quả của quảng cáo.

### Tình huống 2 — Cấp 2: Kiểm tra độc lập trong bảng 12 lượt với bốn tổ hợp

**Từ vựng trong mục:** **Independence** — độc lập; **Joint probability** — xác suất đồng thời.

**Tình huống thực tế:** Đội kiểm thử tạo **12 bản ghi đúng/sai giả lập** cho hai hành vi: **A = dùng ứng dụng**, **B = đọc email**. Cả bốn trường hợp — có cả hai, chỉ A, chỉ B, không có cái nào — đều xuất hiện **đúng ba lần**. Nhóm muốn kiểm xem trong bảng cân bằng này, biết người đó có B có làm tỷ lệ A khác đi hay không, và so tỷ lệ có cả hai hành vi với các tỷ lệ riêng.

**Vì sao chọn cách này?** **Độc lập** trong xác suất nghĩa là biết biến cố B xảy ra **không làm thay đổi cơ hội xảy ra A** trong mô hình đang xét. Bài cố ý tạo **12 lượt** với đúng **ba lượt ở mỗi trong bốn tổ hợp**, nên có thể đếm riêng số lần A, B và **cả hai**. Chương trình lấy các tỷ lệ đó theo **cùng mẫu số 12**, rồi đối chiếu tỷ lệ cả hai với **tích hai tỷ lệ riêng**; chúng khớp trong bảng đã được thiết kế cân bằng. Điều đó xác minh thuộc tính của **dữ liệu giả lập này**, không chứng minh mọi hành vi dùng app và đọc email của khách hàng thật đều độc lập.

**Quy trình:**
1. Tạo 12 hàng với bốn tổ hợp lặp đều.
2. Tính P(A), P(B), P(A∩B) từ số dòng.
3. So giao với tích và in kết luận trên bảng này.

**No Note — Không chú thích**

```python
records = [{"a":True,"b":True},{"a":True,"b":False},{"a":False,"b":True},{"a":False,"b":False},{"a":True,"b":True},{"a":True,"b":False},{"a":False,"b":True},{"a":False,"b":False},{"a":True,"b":True},{"a":True,"b":False},{"a":False,"b":True},{"a":False,"b":False}]
n = len(records)
a_count = 0
b_count = 0
both_count = 0
for row in records:
    if row["a"]:
        a_count += 1
    if row["b"]:
        b_count += 1
    if row["a"] and row["b"]:
        both_count += 1
p_a = a_count / n
p_b = b_count / n
p_both = both_count / n
if n != 12:
    raise ValueError("Cần đúng 12 lượt kiểm tra tính độc lập.")
print("Lượt kiểm:", n)
print(f"P(A): {p_a:.2f}")
print(f"P(B): {p_b:.2f}")
print(f"P(cả hai): {p_both:.2f}")
print("Khớp quy tắc độc lập:", abs(p_both-p_a*p_b) < 1e-12)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Kiểm tính độc lập giữa A và B bằng cách so P(A∩B) với P(A)×P(B) từ 12 lượt.
# Dữ liệu: 12 kết quả cờ A/B Boolean; mỗi hàng là một phép thử đồng thời hai biến cố.
# 12 lượt cùng hai cờ sự kiện A/B, cho phép đếm giao và từng biến cố.
records = [{"a":True,"b":True},{"a":True,"b":False},{"a":False,"b":True},{"a":False,"b":False},{"a":True,"b":True},{"a":True,"b":False},{"a":False,"b":True},{"a":False,"b":False},{"a":True,"b":True},{"a":True,"b":False},{"a":False,"b":True},{"a":False,"b":False}]
# len() đếm số phép thử chung, là mẫu số cho P(A), P(B), P(A∩B).
n = len(records)
# Bắt đầu đếm số lượt biến cố A đúng.
a_count = 0
# Bắt đầu đếm số lượt biến cố B đúng.
b_count = 0
# Bắt đầu đếm số lượt CẢ A và B đúng.
both_count = 0
# Duyệt từng lượt, đọc cả hai cờ cùng một bản ghi.
for row in records:
    # Truy cập cờ sự kiện A của lượt đang xét.
    if row["a"]:
        a_count += 1
    # Truy cập cờ sự kiện B của lượt đang xét.
    if row["b"]:
        b_count += 1
    # Truy cập cờ sự kiện A của lượt đang xét.
    # Truy cập cờ sự kiện B của lượt đang xét.
    # AND chỉ đúng khi A và B cùng xảy ra: biến cố giao A∩B.
    if row["a"] and row["b"]:
        both_count += 1
# Tần suất xuất hiện của A trên 12 lượt, dùng như xác suất thực nghiệm.
p_a = a_count / n
# Tần suất xuất hiện của B trên 12 lượt.
p_b = b_count / n
# Tần suất giao A∩B trên cùng 12 lượt.
p_both = both_count / n
if n != 12:
    # ValueError báo thiếu mẫu hợp lệ hoặc nhóm điều kiện rỗng; không nên tiếp tục chia cho số mẫu sai.
    raise ValueError("Cần đúng 12 lượt kiểm tra tính độc lập.")
print("Lượt kiểm:", n)
print(f"P(A): {p_a:.2f}")
print(f"P(B): {p_b:.2f}")
print(f"P(cả hai): {p_both:.2f}")
# So P(A∩B) với tích P(A)P(B); abs() lấy độ lệch, 1e-12 là dung sai số thực, chỉ chứng tỏ bảng minh họa khớp quy tắc, KHÔNG chứng minh độc lập trong quần thể.
print("Khớp quy tắc độc lập:", abs(p_both-p_a*p_b) < 1e-12)
```

**Kết quả khi chạy:**

```text
Lượt kiểm: 12
P(A): 0.50
P(B): 0.50
P(cả hai): 0.25
Khớp quy tắc độc lập: True
```

Kết quả khớp công thức **trên bảng giả lập được xây dựng**; với dữ liệu khảo sát ngẫu nhiên cần kiểm định thống kê và kích thước mẫu phù hợp.

### Tình huống 3 — Cấp 3: Áp Bayes cho 15 sản phẩm có nhãn lỗi và cảnh báo

**Từ vựng trong mục:** **Prior** — tỷ lệ nền; **Likelihood** — xác suất cảnh báo có điều kiện; **Posterior** — tỷ lệ sau cảnh báo.

**Tình huống thực tế:** Nhà máy kiểm tra **15 sản phẩm P01–P15** bằng một máy báo lỗi. Mỗi sản phẩm có **tình trạng lỗi thật** do kiểm tra đối chiếu và cờ **máy cảnh báo**. Có **3 sản phẩm lỗi thật**, nhưng máy có thể **bỏ sót lỗi** hoặc **báo nhầm hàng tốt**. Nhân viên muốn biết **nếu máy đã cảnh báo, xác suất sản phẩm thật sự lỗi là bao nhiêu**, rồi đối chiếu tính theo Bayes với phép đếm trực tiếp sản phẩm lỗi trong nhóm được cảnh báo.

**Vì sao chọn cách này?** Máy **cảnh báo** không đồng nghĩa sản phẩm **thực sự lỗi**, vì có thể báo nhầm hàng tốt; cũng có sản phẩm lỗi mà máy không cảnh báo. **Bayes** giúp đổi câu hỏi từ **'hàng lỗi thì máy báo đúng bao nhiêu?'** sang **'máy báo thì hàng thật sự lỗi bao nhiêu?'**. Đầu tiên tính **tỷ lệ lỗi nền** trong 15 sản phẩm, **độ nhạy** là tỷ lệ máy báo trong hàng lỗi và **tỷ lệ dương giả** là tỷ lệ máy báo trong hàng tốt. Các phần ấy được kết hợp để xét đúng **nhóm có cảnh báo**, rồi đối chiếu với cách đếm trực tiếp **hàng vừa cảnh báo vừa lỗi thật** chia cho **tất cả hàng có cảnh báo**. Mẫu 15 sản phẩm chỉ để học phương pháp; không dùng kết quả này thay độ chính xác của máy trên cả nhà máy.

**Quy trình:**
1. Tách 15 sản phẩm thành nhóm lỗi và tốt, đồng thời đếm cờ dương.
2. Tính prior, sensitivity, false-positive rate từ bảng.
3. Dùng Bayes để tính posterior, đối chiếu số sản phẩm lỗi trong nhóm dương.

**No Note — Không chú thích**

```python
records = [{"id":"P01","defective":False,"positive":True},{"id":"P02","defective":True,"positive":True},{"id":"P03","defective":False,"positive":False},{"id":"P04","defective":False,"positive":True},{"id":"P05","defective":False,"positive":False},{"id":"P06","defective":False,"positive":False},{"id":"P07","defective":True,"positive":True},{"id":"P08","defective":False,"positive":False},{"id":"P09","defective":False,"positive":False},{"id":"P10","defective":False,"positive":True},{"id":"P11","defective":False,"positive":False},{"id":"P12","defective":True,"positive":False},{"id":"P13","defective":False,"positive":False},{"id":"P14","defective":False,"positive":False},{"id":"P15","defective":False,"positive":False}]
n = len(records)
defects = []
good = []
positive = []
for row in records:
    if row["defective"]:
        defects.append(row)
    else:
        good.append(row)
    if row["positive"]:
        positive.append(row)
prior = len(defects)/n
true_positive_count = 0
for row in defects:
    if row["positive"]:
        true_positive_count += 1
false_positive_count = 0
for row in good:
    if row["positive"]:
        false_positive_count += 1
sensitivity = true_positive_count / len(defects)
false_positive = false_positive_count / len(good)
evidence = sensitivity*prior+false_positive*(1-prior)
posterior = sensitivity*prior/evidence
if n != 15 or not positive:
    raise ValueError("Cần 15 sản phẩm và ít nhất một cảnh báo.")
print("Sản phẩm:", n)
print("Lỗi thật:", len(defects))
print("Máy cảnh báo:", len(positive))
print(f"P(lỗi|cảnh báo): {posterior:.3f}")
defects_among_positive = 0
for row in positive:
    if row["defective"]:
        defects_among_positive += 1
print("Khớp kiểm đếm:", abs(posterior - defects_among_positive / len(positive)) < 1e-12)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tính P(lỗi | cảnh báo) của 15 sản phẩm bằng Bayes, rồi đối chiếu kiểm đếm trực tiếp.
# Dữ liệu: 15 sản phẩm, hai cờ defective (lỗi thật) và positive (máy cảnh báo), gồm cả cảnh báo nhầm.
# 15 sản phẩm, defective là lỗi thật, positive là máy cảnh báo; hai cờ có thể không trùng nhau.
records = [{"id":"P01","defective":False,"positive":True},{"id":"P02","defective":True,"positive":True},{"id":"P03","defective":False,"positive":False},{"id":"P04","defective":False,"positive":True},{"id":"P05","defective":False,"positive":False},{"id":"P06","defective":False,"positive":False},{"id":"P07","defective":True,"positive":True},{"id":"P08","defective":False,"positive":False},{"id":"P09","defective":False,"positive":False},{"id":"P10","defective":False,"positive":True},{"id":"P11","defective":False,"positive":False},{"id":"P12","defective":True,"positive":False},{"id":"P13","defective":False,"positive":False},{"id":"P14","defective":False,"positive":False},{"id":"P15","defective":False,"positive":False}]
n = len(records)
# List chứa sản phẩm lỗi THỰC, là mẫu điều kiện để tính sensitivity.
defects = []
# List chứa sản phẩm không lỗi thực, là mẫu điều kiện tính tỷ lệ dương giả.
good = []
# List chứa mọi sản phẩm bị cảnh báo, gồm cả cảnh báo đúng và sai.
positive = []
# Đọc từng sản phẩm để phân nhóm.
for row in records:
    # True nghĩa sản phẩm có lỗi thật, không phụ thuộc kết luận máy.
    if row["defective"]:
        # append() lưu hàng vào tập lỗi thực.
        defects.append(row)
    else:
        # append() lưu hàng vào tập không lỗi.
        good.append(row)
    # True nghĩa máy cảnh báo dương; có thể là cảnh báo nhầm.
    if row["positive"]:
        # append() lưu tất cả hàng máy cảnh báo.
        positive.append(row)
# prior là tỷ lệ lỗi nền trong 15 sản phẩm, chưa xét cảnh báo.
prior = len(defects)/n
# Đếm dương tính THẬT trong nhóm defective.
true_positive_count = 0
# Chỉ duyệt các sản phẩm đã biết lỗi thật để tính sensitivity.
for row in defects:
    # True nghĩa máy cảnh báo dương; có thể là cảnh báo nhầm.
    if row["positive"]:
        # Tăng số sản phẩm lỗi thật được máy cảnh báo.
        true_positive_count += 1
# Đếm dương tính GIẢ trong nhóm không lỗi.
false_positive_count = 0
# Chỉ duyệt các sản phẩm thật sự tốt để tính false-positive rate.
for row in good:
    # True nghĩa máy cảnh báo dương; có thể là cảnh báo nhầm.
    if row["positive"]:
        # Tăng số sản phẩm không lỗi nhưng bị cảnh báo.
        false_positive_count += 1
# Sensitivity = P(cảnh báo|lỗi), mẫu số là các sản phẩm LỖI THẬT.
sensitivity = true_positive_count / len(defects)
# False-positive rate = P(cảnh báo|không lỗi), mẫu số là sản phẩm KHÔNG lỗi.
false_positive = false_positive_count / len(good)
# P(cảnh báo) theo xác suất toàn phần từ hai nhóm lỗi/không lỗi.
evidence = sensitivity*prior+false_positive*(1-prior)
# Bayes: P(lỗi|cảnh báo)=P(cảnh báo|lỗi)×P(lỗi)/P(cảnh báo).
posterior = sensitivity*prior/evidence
if n != 15 or not positive:
    # ValueError báo thiếu mẫu hợp lệ hoặc nhóm điều kiện rỗng; không nên tiếp tục chia cho số mẫu sai.
    raise ValueError("Cần 15 sản phẩm và ít nhất một cảnh báo.")
print("Sản phẩm:", n)
print("Lỗi thật:", len(defects))
print("Máy cảnh báo:", len(positive))
print(f"P(lỗi|cảnh báo): {posterior:.3f}")
# Đếm số sản phẩm lỗi THẬT bên trong nhóm bị cảnh báo để kiểm độc lập kết quả Bayes.
defects_among_positive = 0
# Duyệt chính nhóm máy cảnh báo, không phải toàn bộ sản phẩm.
for row in positive:
    # True nghĩa sản phẩm có lỗi thật, không phụ thuộc kết luận máy.
    if row["defective"]:
        # Tăng số cảnh báo trúng lỗi thật.
        defects_among_positive += 1
# Tỷ lệ lỗi trực tiếp trong nhóm bị cảnh báo, phải gần posterior Bayes.
# abs() so Bayes với phép đếm trực tiếp, 1e-12 cho dung sai số thực.
print("Khớp kiểm đếm:", abs(posterior - defects_among_positive / len(positive)) < 1e-12)
```

**Kết quả khi chạy:**

```text
Sản phẩm: 15
Lỗi thật: 3
Máy cảnh báo: 5
P(lỗi|cảnh báo): 0.400
Khớp kiểm đếm: True
```

Không được suy ra độ tin cậy của một máy kiểm hàng thật chỉ từ **15 sản phẩm ví dụ**; tỷ lệ nền khi triển khai thực tế có thể rất khác.

### Tình huống 4 — Cấp 4: Xác suất toàn phần từ 18 khách ở ba nhóm có quy mô khác nhau

**Từ vựng trong mục:** **Total probability** — xác suất toàn phần; **Partition** — phân hoạch; **Weighted rate** — tỷ lệ có trọng số.

**Tình huống thực tế:** Khảo sát ghi **18 khách C01–C18**, chia vào đúng một trong ba nhóm địa bàn **A (9 người), B (6 người), C (3 người)**. Mỗi người có trạng thái **đã mua/chưa mua**. Quản lý muốn tính **tỷ lệ mua chung của 18 khách** bằng cách tổng hợp tỷ lệ từng nhóm, sau đó đối chiếu với việc đếm trực tiếp số người đã mua; không được lấy trung bình đều ba nhóm vì số người rất khác nhau.

**Vì sao chọn cách này?** **Xác suất toàn phần** giúp gộp các nhóm **không trùng nhau và bao phủ đủ dữ liệu** để biết tỷ lệ chung. Trong ví dụ, A có 9 khách, B có 6 và C có 3, nên mỗi nhóm phải đóng góp theo **số người thực sự thuộc nhóm đó**, không phải mỗi nhóm được tính ngang một phần ba. Chương trình đếm số người mua ở mỗi nhóm, tính tỷ lệ mua của nhóm, sau đó lấy **tỷ trọng nhóm trong 18 khách** để tổng hợp. Kết quả được đối chiếu với số **người mua thật trong cả bảng chia 18**. Lấy trung bình đều ba tỷ lệ sẽ dễ làm nhóm C chỉ có ba người ảnh hưởng mạnh ngang nhóm A chín người.

**Quy trình:**
1. Đếm kích thước và số mua của từng nhóm từ 18 hàng.
2. Tính tỷ trọng nhóm và tỷ lệ mua có điều kiện trong từng nhóm.
3. Cộng tỷ lệ có trọng số; đối chiếu tỷ lệ mua trực tiếp trên 18 khách.

**No Note — Không chú thích**

```python
records = [{"id":"C01","area":"A","bought":True},{"id":"C02","area":"A","bought":True},{"id":"C03","area":"A","bought":True},{"id":"C04","area":"A","bought":True},{"id":"C05","area":"A","bought":True},{"id":"C06","area":"A","bought":True},{"id":"C07","area":"A","bought":False},{"id":"C08","area":"A","bought":False},{"id":"C09","area":"A","bought":False},{"id":"C10","area":"B","bought":True},{"id":"C11","area":"B","bought":True},{"id":"C12","area":"B","bought":False},{"id":"C13","area":"B","bought":False},{"id":"C14","area":"B","bought":False},{"id":"C15","area":"B","bought":False},{"id":"C16","area":"C","bought":True},{"id":"C17","area":"C","bought":False},{"id":"C18","area":"C","bought":False}]
n = len(records)
areas = ("A", "B", "C")
overall = 0.0
for area in areas:
    subset = []
    bought_count = 0
    for row in records:
        if row["area"] == area:
            subset.append(row)
            if row["bought"]:
                bought_count += 1
    overall += (len(subset) / n) * (bought_count / len(subset))
all_bought_count = 0
for row in records:
    if row["bought"]:
        all_bought_count += 1
direct = all_bought_count / n
unique_ids = set()
for row in records:
    unique_ids.add(row["id"])
if len(records) != 18 or len(unique_ids) != 18:
    raise ValueError("Cần đủ 18 khách với mã duy nhất.")
print("Khách:", n)
group_counts = []
for group in areas:
    count = 0
    for row in records:
        if row["area"] == group:
            count += 1
    group_counts.append(count)
print("Nhóm A/B/C:", *group_counts)
print(f"Tỷ lệ mua toàn phần: {overall:.3f}")
print("Khớp đếm trực tiếp:", abs(overall-direct) < 1e-12)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tính xác suất mua toàn phần trên 18 khách bằng cách cộng tỷ lệ có trọng số theo vùng.
# Dữ liệu: 18 khách chia các vùng A,B,C, mỗi vùng có tỷ lệ mua và quy mô khác nhau.
# 18 khách có id, area A/B/C và bought True/False; quy mô từng vùng khác nhau.
records = [{"id":"C01","area":"A","bought":True},{"id":"C02","area":"A","bought":True},{"id":"C03","area":"A","bought":True},{"id":"C04","area":"A","bought":True},{"id":"C05","area":"A","bought":True},{"id":"C06","area":"A","bought":True},{"id":"C07","area":"A","bought":False},{"id":"C08","area":"A","bought":False},{"id":"C09","area":"A","bought":False},{"id":"C10","area":"B","bought":True},{"id":"C11","area":"B","bought":True},{"id":"C12","area":"B","bought":False},{"id":"C13","area":"B","bought":False},{"id":"C14","area":"B","bought":False},{"id":"C15","area":"B","bought":False},{"id":"C16","area":"C","bought":True},{"id":"C17","area":"C","bought":False},{"id":"C18","area":"C","bought":False}]
# Tổng 18 khách là mẫu số của tỷ trọng vùng.
n = len(records)
# Tuple tên ba vùng dùng để duyệt đủ các nhóm loại trừ nhau.
areas = ("A", "B", "C")
# Biến tích lũy xác suất mua toàn phần, bắt đầu từ 0.
overall = 0.0
# Duyệt từng vùng A,B,C, tính tỷ lệ mua riêng trước khi gộp.
for area in areas:
    # Mẫu nền chỉ gồm những khách của vùng đang xét.
    subset = []
    # Đếm số khách mua trong vùng hiện tại.
    bought_count = 0
    for row in records:
        # So tên vùng trong từng dict, chọn đúng hồ sơ thuộc vùng.
        if row["area"] == area:
            # append() thêm khách vùng hiện tại, dùng len(subset) làm mẫu số cho tỷ lệ mua vùng.
            subset.append(row)
            # Cờ Boolean cho biết khách có mua hay không.
            if row["bought"]:
                # Đếm người mua trong nhóm vùng tương ứng.
                bought_count += 1
    # Xác suất toàn phần: tỷ trọng vùng × P(mua|vùng), cộng cả ba vùng, KHÔNG lấy trung bình các tỷ lệ vùng ngang nhau.
    overall += (len(subset) / n) * (bought_count / len(subset))
# Đếm số khách mua trong vùng hiện tại.
# Đếm trực tiếp tất cả người mua để đối chiếu cách tính phân nhóm.
all_bought_count = 0
for row in records:
    # Cờ Boolean cho biết khách có mua hay không.
    if row["bought"]:
        # Đếm người mua trong nhóm vùng tương ứng.
        # Tăng số mua trên toàn bộ 18 hồ sơ.
        all_bought_count += 1
# direct là tỷ lệ mua từ toàn bộ khách, cần khớp overall đã gộp vùng.
direct = all_bought_count / n
# Set lưu ID duy nhất để phát hiện mã khách bị lặp.
unique_ids = set()
for row in records:
    # add() thêm ID, không nhân đôi khi ID đã tồn tại.
    unique_ids.add(row["id"])
# Kiểm 18 mã khách riêng biệt, không chỉ 18 hàng.
if len(records) != 18 or len(unique_ids) != 18:
    # ValueError báo thiếu mẫu hợp lệ hoặc nhóm điều kiện rỗng; không nên tiếp tục chia cho số mẫu sai.
    raise ValueError("Cần đủ 18 khách với mã duy nhất.")
print("Khách:", n)
# List chứa số lượng khách từng nhóm, đúng thứ tự areas.
group_counts = []
# Duyệt các vùng để đếm mỗi nhóm.
for group in areas:
    count = 0
    for row in records:
        if row["area"] == group:
            count += 1
    # append() giữ số khách của vùng tương ứng.
    group_counts.append(count)
# Dấu * giải nén các số đếm thành ba đối số print riêng.
print("Nhóm A/B/C:", *group_counts)
print(f"Tỷ lệ mua toàn phần: {overall:.3f}")
# abs() kiểm chênh xác suất hai cách tính gần 0, tránh sai số dấu phẩy động.
print("Khớp đếm trực tiếp:", abs(overall-direct) < 1e-12)
```

**Kết quả khi chạy:**

```text
Khách: 18
Nhóm A/B/C: 9 6 3
Tỷ lệ mua toàn phần: 0.500
Khớp đếm trực tiếp: True
```

Ví dụ này minh họa **trung bình có trọng số**; nếu chỉ cộng ba tỷ lệ chia 3, mỗi nhóm bị xem như có cùng quy mô, dễ dẫn đến kết luận sai.

### Tình huống 5 — Cấp 5: Bayes hai dây chuyền: phân biệt tỷ lệ nền với độ chính xác cảnh báo

**Từ vựng trong mục:** **Posterior** — tỷ lệ lỗi sau tín hiệu; **Evidence** — xác suất tín hiệu; **Base-rate effect** — ảnh hưởng tỷ lệ nền.

**Tình huống thực tế:** Nhà máy thử **20 sản phẩm M01–M20**, gồm **12 từ dây chuyền A** và **8 từ dây chuyền B**. Mỗi sản phẩm có kết luận **lỗi thật** và dấu **máy cảnh báo dương**, nhưng cảnh báo có thể đúng hoặc sai. Nhóm chất lượng cần tính xác suất **lỗi thật khi đã có cảnh báo trên toàn nhà máy**, rồi tính riêng **trong nhóm cảnh báo ở dây chuyền B**, để xem vì sao thay đổi nhóm đang xét có thể làm kết quả khác nhau.

**Vì sao chọn cách này?** **Xác suất hậu nghiệm (posterior)** là cơ hội sản phẩm lỗi **sau khi đã biết máy báo cảnh báo**. Với toàn bộ 20 sản phẩm, Bayes dùng **tỷ lệ lỗi nền**, **tỷ lệ cảnh báo trên hàng lỗi** và **tỷ lệ cảnh báo nhầm trên hàng tốt** của **toàn nhà máy**, rồi đối chiếu với **số hàng lỗi thật trong nhóm cảnh báo**. Khi đổi sang **chỉ dây chuyền B**, mẫu số trở thành **những sản phẩm B có cảnh báo**, không còn là tất cả cảnh báo từ cả A và B. Vì B có tỷ lệ lỗi/cảnh báo khác, tỷ lệ lỗi sau cảnh báo có thể khác kết quả chung; đây không phải mâu thuẫn. Đừng lấy **độ nhạy** (cơ hội báo khi đã lỗi) thay cho **posterior** (cơ hội lỗi khi đã báo), và đừng dùng tỷ lệ của nhóm toàn nhà máy để phát biểu về B.

**Quy trình:**
1. Lưu 20 hàng đầy đủ mã, dây chuyền, cờ lỗi và cờ cảnh báo.
2. Tính prior, sensitivity, false positive và evidence trên cả 20 hàng; dùng Bayes.
3. Tính tỷ lệ lỗi trong nhóm B bị cảnh báo, báo hai kết quả và kiểm bằng đếm trực tiếp.

**No Note — Không chú thích**

```python
records = [{"id":"M01","line":"A","defective":False,"positive":True},{"id":"M02","line":"A","defective":True,"positive":True},{"id":"M03","line":"A","defective":False,"positive":False},{"id":"M04","line":"A","defective":False,"positive":False},{"id":"M05","line":"A","defective":False,"positive":False},{"id":"M06","line":"A","defective":False,"positive":True},{"id":"M07","line":"A","defective":False,"positive":False},{"id":"M08","line":"A","defective":False,"positive":False},{"id":"M09","line":"A","defective":True,"positive":True},{"id":"M10","line":"A","defective":False,"positive":False},{"id":"M11","line":"A","defective":False,"positive":False},{"id":"M12","line":"A","defective":False,"positive":False},{"id":"M13","line":"B","defective":True,"positive":True},{"id":"M14","line":"B","defective":True,"positive":True},{"id":"M15","line":"B","defective":False,"positive":False},{"id":"M16","line":"B","defective":False,"positive":False},{"id":"M17","line":"B","defective":True,"positive":False},{"id":"M18","line":"B","defective":False,"positive":True},{"id":"M19","line":"B","defective":False,"positive":False},{"id":"M20","line":"B","defective":False,"positive":False}]
n = len(records)
defects = []
good = []
positive = []
for row in records:
    if row["defective"]:
        defects.append(row)
    else:
        good.append(row)
    if row["positive"]:
        positive.append(row)
prior = len(defects)/n
true_positive_count = 0
for row in defects:
    if row["positive"]:
        true_positive_count += 1
false_positive_count = 0
for row in good:
    if row["positive"]:
        false_positive_count += 1
sensitivity = true_positive_count / len(defects)
false_positive = false_positive_count / len(good)
p_positive = sensitivity*prior + false_positive*(1-prior)
posterior = sensitivity*prior/p_positive
positive_b = []
for row in records:
    if row["line"] == "B" and row["positive"]:
        positive_b.append(row)
positive_b_defects = 0
for row in positive_b:
    if row["defective"]:
        positive_b_defects += 1
b_rate = positive_b_defects / len(positive_b)
if len(records) != 20 or not positive_b:
    raise ValueError("Cần đủ 20 sản phẩm và cảnh báo ở dây chuyền B.")
print("Sản phẩm:", n)
print("Lỗi thật:", len(defects))
print("Cảnh báo:", len(positive))
print(f"P(lỗi|cảnh báo) toàn nhà máy: {posterior:.3f}")
print(f"P(lỗi|cảnh báo, B): {b_rate:.3f}")
defects_among_positive = 0
for row in positive:
    if row["defective"]:
        defects_among_positive += 1
print("Bayes khớp đếm:", abs(posterior - defects_among_positive / len(positive)) < 1e-12)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tính Bayes trên 20 sản phẩm và so xác suất lỗi khi cảnh báo trên toàn nhà máy với riêng dây chuyền B.
# Dữ liệu: 20 sản phẩm từ hai dây chuyền A/B; lỗi thật và cảnh báo không đồng nhất, cần điều kiện hóa theo nhóm.
# 20 sản phẩm từ line A/B; defective là lỗi thật, positive là máy báo động, hai cờ độc lập với nhãn line.
records = [{"id":"M01","line":"A","defective":False,"positive":True},{"id":"M02","line":"A","defective":True,"positive":True},{"id":"M03","line":"A","defective":False,"positive":False},{"id":"M04","line":"A","defective":False,"positive":False},{"id":"M05","line":"A","defective":False,"positive":False},{"id":"M06","line":"A","defective":False,"positive":True},{"id":"M07","line":"A","defective":False,"positive":False},{"id":"M08","line":"A","defective":False,"positive":False},{"id":"M09","line":"A","defective":True,"positive":True},{"id":"M10","line":"A","defective":False,"positive":False},{"id":"M11","line":"A","defective":False,"positive":False},{"id":"M12","line":"A","defective":False,"positive":False},{"id":"M13","line":"B","defective":True,"positive":True},{"id":"M14","line":"B","defective":True,"positive":True},{"id":"M15","line":"B","defective":False,"positive":False},{"id":"M16","line":"B","defective":False,"positive":False},{"id":"M17","line":"B","defective":True,"positive":False},{"id":"M18","line":"B","defective":False,"positive":True},{"id":"M19","line":"B","defective":False,"positive":False},{"id":"M20","line":"B","defective":False,"positive":False}]
# Mẫu số của prior toàn nhà máy là 20 sản phẩm.
n = len(records)
# Nhóm sản phẩm lỗi thật của cả hai dây chuyền.
defects = []
# Nhóm sản phẩm không lỗi thật.
good = []
# Nhóm sản phẩm bị máy cảnh báo bất kể lỗi thật.
positive = []
# Duyệt từng sản phẩm của cả hai dây chuyền.
for row in records:
    # Cờ lỗi thật; khác cờ positive của máy.
    if row["defective"]:
        # Gom sản phẩm lỗi thật.
        defects.append(row)
    else:
        # Gom sản phẩm tốt.
        good.append(row)
    # Cờ máy cảnh báo, có thể đúng hoặc sai.
    if row["positive"]:
        # Gom mọi cảnh báo để kiểm Bayes.
        positive.append(row)
# Prior lỗi nền dựa trên tất cả 20 sản phẩm, chưa xét cảnh báo/line.
prior = len(defects)/n
# Đếm sản phẩm lỗi thật có máy cảnh báo.
true_positive_count = 0
# Chỉ đọc nhóm lỗi thật khi ước lượng sensitivity.
for row in defects:
    # Cờ máy cảnh báo, có thể đúng hoặc sai.
    if row["positive"]:
        # Tăng số cảnh báo đúng trong nhóm lỗi thật.
        true_positive_count += 1
# Đếm cảnh báo sai trong nhóm không lỗi.
false_positive_count = 0
# Duyệt nhóm không lỗi để tính false-positive rate.
for row in good:
    # Cờ máy cảnh báo, có thể đúng hoặc sai.
    if row["positive"]:
        # Tăng số sản phẩm tốt nhưng bị cảnh báo.
        false_positive_count += 1
# Sensitivity P(cảnh báo|lỗi), mẫu số các hàng defective True.
sensitivity = true_positive_count / len(defects)
# False-positive rate P(cảnh báo|không lỗi), mẫu số các hàng defective False.
false_positive = false_positive_count / len(good)
# P(cảnh báo) tính theo xác suất toàn phần trong cả hai nhóm lỗi/không lỗi.
p_positive = sensitivity*prior + false_positive*(1-prior)
# Bayes toàn nhà máy: P(lỗi|cảnh báo), chưa điều kiện hóa riêng theo dây chuyền.
posterior = sensitivity*prior/p_positive
# List chứa sản phẩm của CHỈ dây chuyền B và đang có cảnh báo.
positive_b = []
# Duyệt từng sản phẩm của cả hai dây chuyền.
for row in records:
    # Cờ máy cảnh báo, có thể đúng hoặc sai.
    # and yêu cầu đồng thời line B và positive True; mẫu điều kiện riêng khác toàn nhà máy.
    if row["line"] == "B" and row["positive"]:
        # append() lưu cảnh báo trong dây chuyền B.
        positive_b.append(row)
# Đếm số cảnh báo B có lỗi thật.
positive_b_defects = 0
# Chỉ xét những sản phẩm line B có positive True.
# Duyệt nhóm cảnh báo toàn nhà máy.
for row in positive_b:
    # Cờ lỗi thật; khác cờ positive của máy.
    if row["defective"]:
        # Tăng số sản phẩm lỗi thật trong nhóm cảnh báo B.
        positive_b_defects += 1
# P(lỗi|cảnh báo, B): lấy số lỗi thật TRONG cảnh báo B chia số cảnh báo B.
b_rate = positive_b_defects / len(positive_b)
# Nếu nhóm cảnh báo B rỗng, không thể tính tỷ lệ có điều kiện và phải báo lỗi.
if len(records) != 20 or not positive_b:
    # ValueError báo thiếu mẫu hợp lệ hoặc nhóm điều kiện rỗng; không nên tiếp tục chia cho số mẫu sai.
    raise ValueError("Cần đủ 20 sản phẩm và cảnh báo ở dây chuyền B.")
print("Sản phẩm:", n)
print("Lỗi thật:", len(defects))
print("Cảnh báo:", len(positive))
print(f"P(lỗi|cảnh báo) toàn nhà máy: {posterior:.3f}")
print(f"P(lỗi|cảnh báo, B): {b_rate:.3f}")
# Đếm lỗi thật trong tất cả cảnh báo, dùng kiểm kết quả Bayes toàn nhà máy.
defects_among_positive = 0
# Duyệt nhóm cảnh báo toàn nhà máy.
for row in positive:
    # Cờ lỗi thật; khác cờ positive của máy.
    if row["defective"]:
        # Tăng số lỗi thật có máy cảnh báo.
        defects_among_positive += 1
# Phép đếm trực tiếp tỷ lệ lỗi trên nhóm cảnh báo toàn nhà máy, đối chiếu posterior.
# So Bayes với tần suất đếm trực tiếp, dung sai 1e-12 giúp tránh sai số float.
print("Bayes khớp đếm:", abs(posterior - defects_among_positive / len(positive)) < 1e-12)
```

**Kết quả khi chạy:**

```text
Sản phẩm: 20
Lỗi thật: 5
Cảnh báo: 7
P(lỗi|cảnh báo) toàn nhà máy: 0.571
P(lỗi|cảnh báo, B): 0.667
Bayes khớp đếm: True
```

Đây là tỷ lệ kinh nghiệm trên **20 sản phẩm giả lập**, không đủ cỡ mẫu để đánh giá máy trong sản xuất thật. Tập điều kiện thay đổi thì **posterior có thể thay đổi**.

## 6. Sai lầm thường gặp

- P(A khi B) và P(B khi A) có **hai mẫu nền khác nhau**, không được tráo hai xác suất.
- Độ nhạy của máy kiểm không phải xác suất sản phẩm thực sự lỗi sau cảnh báo; phải tính cả tỷ lệ nền và dương giả.
- Xác suất có điều kiện cần mẫu số P(B) lớn hơn 0.
- Các nhóm trong xác suất toàn phần phải rời nhau và phủ toàn bộ quần thể.
- Quan sát khách mua sau khi thấy quảng cáo không tự chứng minh quảng cáo gây ra mua hàng.
- Kiểm tra độc lập trên dữ liệu khảo sát cần xét sai số và cách lấy mẫu, không chỉ so hai số xấp xỉ.

## 7. Trắc nghiệm

**Q1. What is conditional probability? | Xác suất có điều kiện là gì?**

A. Probability of A given B has occurred | Xác suất A khi biết B đã xảy ra

B. One event does not change the probability of the other | Biến cố này không đổi xác suất của biến cố kia

C. A posterior from evidence, likelihood and prior | Xác suất sau bằng chứng từ likelihood và prior

D. Overall chance weighted over a partition | Xác suất chung theo trọng số một phân hoạch

**Đáp án: A**

**Giải thích:** Nó thu hẹp mẫu nền về nhóm B.


**Q2. What is independence of events? | Độc lập giữa hai biến cố là gì?**

A. Probability of A given B has occurred | Xác suất A khi biết B đã xảy ra

B. One event does not change the probability of the other | Biến cố này không đổi xác suất của biến cố kia

C. A posterior from evidence, likelihood and prior | Xác suất sau bằng chứng từ likelihood và prior

D. Overall chance weighted over a partition | Xác suất chung theo trọng số một phân hoạch

**Đáp án: B**

**Giải thích:** Độc lập nghĩa là biến cố này không đổi xác suất biến cố kia.


**Q3. What does Bayes' theorem compute? | Định lý Bayes tính gì?**

A. Probability of A given B has occurred | Xác suất A khi biết B đã xảy ra

B. One event does not change the probability of the other | Biến cố này không đổi xác suất của biến cố kia

C. A posterior from evidence, likelihood and prior | Xác suất sau bằng chứng từ likelihood và prior

D. Overall chance weighted over a partition | Xác suất chung theo trọng số một phân hoạch

**Đáp án: C**

**Giải thích:** Bayes cập nhật tỷ lệ nền từ bằng chứng.


**Q4. What does total probability calculate? | Xác suất toàn phần tính gì?**

A. Probability of A given B has occurred | Xác suất A khi biết B đã xảy ra

B. One event does not change the probability of the other | Biến cố này không đổi xác suất của biến cố kia

C. A posterior from evidence, likelihood and prior | Xác suất sau bằng chứng từ likelihood và prior

D. Overall chance weighted over a partition | Xác suất chung theo trọng số một phân hoạch

**Đáp án: D**

**Giải thích:** Xác suất toàn phần dùng tỷ trọng của từng nhóm.


**Q5. Which formula gives P(A given B)? | Công thức P(A khi biết B) là gì?**

A. `P(A and B)/P(B)` when P(B)>0 | `P(A và B)/P(B)` khi P(B)>0

B. `P(A and B)=P(A)*P(B)` | `P(A và B)=P(A)*P(B)`

C. `likelihood*prior/evidence` | `likelihood*prior/evidence`

D. Disjoint and exhaustive | Rời nhau và phủ đủ

**Đáp án: A**

**Giải thích:** Lấy xác suất giao chia xác suất biến cố điều kiện.


**Q6. Which equation expresses event independence? | Đẳng thức nào mô tả biến cố độc lập?**

A. `P(A and B)/P(B)` when P(B)>0 | `P(A và B)/P(B)` khi P(B)>0

B. `P(A and B)=P(A)*P(B)` | `P(A và B)=P(A)*P(B)`

C. `likelihood*prior/evidence` | `likelihood*prior/evidence`

D. Disjoint and exhaustive | Rời nhau và phủ đủ

**Đáp án: B**

**Giải thích:** Độc lập khi xác suất giao bằng tích hai xác suất.


**Q7. Which rule gives posterior after a positive signal? | Quy tắc nào tính posterior khi tín hiệu dương?**

A. `P(A and B)/P(B)` when P(B)>0 | `P(A và B)/P(B)` khi P(B)>0

B. `P(A and B)=P(A)*P(B)` | `P(A và B)=P(A)*P(B)`

C. `likelihood*prior/evidence` | `likelihood*prior/evidence`

D. Disjoint and exhaustive | Rời nhau và phủ đủ

**Đáp án: C**

**Giải thích:** Bayes chuẩn hóa likelihood nhân prior bằng xác suất bằng chứng.


**Q8. What condition is required for total probability groups? | Các nhóm dùng xác suất toàn phần phải thế nào?**

A. `P(A and B)/P(B)` when P(B)>0 | `P(A và B)/P(B)` khi P(B)>0

B. `P(A and B)=P(A)*P(B)` | `P(A và B)=P(A)*P(B)`

C. `likelihood*prior/evidence` | `likelihood*prior/evidence`

D. Disjoint and exhaustive | Rời nhau và phủ đủ

**Đáp án: D**

**Giải thích:** Nhóm phải không giao nhau và phủ toàn bộ.


**Q9. What does prior mean? | Prior có nghĩa gì?**

A. Probability before current evidence | Xác suất trước khi có bằng chứng hiện tại

B. Probability of evidence under a hypothesis | Xác suất bằng chứng khi giả thuyết đúng

C. Updated hypothesis probability after evidence | Xác suất giả thuyết được cập nhật sau bằng chứng

D. Probability of positive signal when no defect exists | Xác suất báo dương khi thực tế không có lỗi

**Đáp án: A**

**Giải thích:** Prior là xác suất nền.


**Q10. What does likelihood mean? | Likelihood biểu thị gì?**

A. Probability before current evidence | Xác suất trước khi có bằng chứng hiện tại

B. Probability of evidence under a hypothesis | Xác suất bằng chứng khi giả thuyết đúng

C. Updated hypothesis probability after evidence | Xác suất giả thuyết được cập nhật sau bằng chứng

D. Probability of positive signal when no defect exists | Xác suất báo dương khi thực tế không có lỗi

**Đáp án: B**

**Giải thích:** Likelihood xét bằng chứng khi giả thuyết đúng.


**Q11. What does posterior mean? | Posterior là gì?**

A. Probability before current evidence | Xác suất trước khi có bằng chứng hiện tại

B. Probability of evidence under a hypothesis | Xác suất bằng chứng khi giả thuyết đúng

C. Updated hypothesis probability after evidence | Xác suất giả thuyết được cập nhật sau bằng chứng

D. Probability of positive signal when no defect exists | Xác suất báo dương khi thực tế không có lỗi

**Đáp án: C**

**Giải thích:** Posterior đã tính đến bằng chứng quan sát.


**Q12. What is a false-positive rate? | Tỷ lệ dương giả là gì?**

A. Probability before current evidence | Xác suất trước khi có bằng chứng hiện tại

B. Probability of evidence under a hypothesis | Xác suất bằng chứng khi giả thuyết đúng

C. Updated hypothesis probability after evidence | Xác suất giả thuyết được cập nhật sau bằng chứng

D. Probability of positive signal when no defect exists | Xác suất báo dương khi thực tế không có lỗi

**Đáp án: D**

**Giải thích:** Dương giả là cảnh báo dương ở trường hợp không lỗi.


**Q13. What is P(A given B) if 20 of 100 B cases have A? | P(A khi B) là gì nếu 20 trên 100 ca B có A?**

A. 0.2 | 0.2

B. 0.56 | 0.56

C. 0.3 | 0.3

D. No; base rate and false positives also matter | Không; còn tỷ lệ nền và dương giả

**Đáp án: A**

**Giải thích:** 20 chia 100 bằng 0.2.


**Q14. What is the total with group shares 0.6,0.4 and rates 0.8,0.2? | Tỷ lệ chung từ nhóm 0.6/0.4 với xác suất 0.8/0.2 là gì?**

A. 0.2 | 0.2

B. 0.56 | 0.56

C. 0.3 | 0.3

D. No; base rate and false positives also matter | Không; còn tỷ lệ nền và dương giả

**Đáp án: B**

**Giải thích:** 0.6×0.8+0.4×0.2 bằng 0.56.


**Q15. If P(A)=0.5 and P(B)=0.6 and they are independent, what is P(A and B)? | Nếu A, B độc lập có xác suất 0.5 và 0.6 thì P(A và B) là gì?**

A. 0.2 | 0.2

B. 0.56 | 0.56

C. 0.3 | 0.3

D. No; base rate and false positives also matter | Không; còn tỷ lệ nền và dương giả

**Đáp án: C**

**Giải thích:** Với biến cố độc lập, 0.5×0.6=0.3.


**Q16. If an alert has 99% sensitivity, does that mean 99% of alerts are true defects? | Độ nhạy 99% có nghĩa 99% cảnh báo là lỗi thật không?**

A. 0.2 | 0.2

B. 0.56 | 0.56

C. 0.3 | 0.3

D. No; base rate and false positives also matter | Không; còn tỷ lệ nền và dương giả

**Đáp án: D**

**Giải thích:** Độ nhạy và posterior xét hai nhóm mẫu nền khác nhau.


**Q17. Why does Bayes need the base rate? | Vì sao Bayes cần tỷ lệ nền?**

A. Rare cases can yield many false alarms among positives | Sự kiện hiếm có thể làm dương giả chiếm nhiều trong cảnh báo

B. The formula divides by P(B) | Vì công thức chia cho P(B)

C. That viewing ads caused purchases | Việc xem quảng cáo gây ra hành vi mua

D. They condition on different reference groups | Chúng xét trên hai nhóm điều kiện khác nhau

**Đáp án: A**

**Giải thích:** Sự kiện hiếm có thể khiến phần lớn cảnh báo là dương giả.


**Q18. Why must P(B)>0 for P(A given B)? | Vì sao cần P(B)>0 khi tính P(A khi B)?**

A. Rare cases can yield many false alarms among positives | Sự kiện hiếm có thể làm dương giả chiếm nhiều trong cảnh báo

B. The formula divides by P(B) | Vì công thức chia cho P(B)

C. That viewing ads caused purchases | Việc xem quảng cáo gây ra hành vi mua

D. They condition on different reference groups | Chúng xét trên hai nhóm điều kiện khác nhau

**Đáp án: B**

**Giải thích:** Chia cho 0 không xác định.


**Q19. What does an observational conditional purchase rate not prove? | Tỷ lệ mua có điều kiện trong quan sát không chứng minh gì?**

A. Rare cases can yield many false alarms among positives | Sự kiện hiếm có thể làm dương giả chiếm nhiều trong cảnh báo

B. The formula divides by P(B) | Vì công thức chia cho P(B)

C. That viewing ads caused purchases | Việc xem quảng cáo gây ra hành vi mua

D. They condition on different reference groups | Chúng xét trên hai nhóm điều kiện khác nhau

**Đáp án: C**

**Giải thích:** Liên hệ quan sát không tự chứng minh nhân quả.


**Q20. What distinguishes P(A given B) from P(B given A)? | P(A khi B) khác P(B khi A) ở đâu?**

A. Rare cases can yield many false alarms among positives | Sự kiện hiếm có thể làm dương giả chiếm nhiều trong cảnh báo

B. The formula divides by P(B) | Vì công thức chia cho P(B)

C. That viewing ads caused purchases | Việc xem quảng cáo gây ra hành vi mua

D. They condition on different reference groups | Chúng xét trên hai nhóm điều kiện khác nhau

**Đáp án: D**

**Giải thích:** Đảo điều kiện làm thay đổi mẫu số.

## 8. Liên hệ bài tiếp theo

`Biến cố → Điều kiện → Bayes → Đánh giá mô hình AI`.
