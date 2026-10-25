# PY-02 — Kiểu số, Boolean và chuỗi


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Integer** — số nguyên; **Float** — số thực.

`Biến → int/float/bool/str → Slicing → Xử lý văn bản`

**Học xong dùng để làm gì?** Phân biệt số và chữ khi đọc dữ liệu, đổi kiểu để tính tiền, số lượng hoặc điểm trung bình mà không ghép nhầm chuỗi.

**Kết nối kiến thức tiếp theo:** Sang PY-03, dùng toán tử tính toán và so sánh các giá trị đã có kiểu phù hợp.

## 2. English vocabulary — Từ vựng

| English | Nghĩa tiếng Việt | Giải thích |
|---|---|---|
| Integer | số nguyên | Giá trị không có phần thập phân |
| Float | số thực | Số có thể có phần lẻ |
| Boolean | giá trị logic | Giá trị True hoặc False |
| String | chuỗi | Dãy ký tự có thể cắt lát |

## 3. Các hàm và tùy chọn Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cú pháp | Mục đích và ý nghĩa lựa chọn |
|---|---|
| `str()/int()/float()` | Chuyển kiểu phù hợp trước khi xử lý |
| `strip()/lower()/upper()` | Dọn khoảng trắng và chuẩn hóa chữ |
| `split()/replace()` | Tách chuỗi hoặc thay thế đoạn văn bản |
| `s[start:stop]` | Cắt ký tự theo vị trí, không lấy chỉ số stop |


## 4. Khái niệm liên quan

**Kiểu dữ liệu (data type)** cho Python biết một giá trị biểu diễn điều gì và có thể thực hiện những phép toán nào. Số lượng món hàng thường là số nguyên, nhiệt độ có thể là số thực, điều kiện đạt/chưa đạt là Boolean, còn mã sản phẩm phải được giữ như chuỗi.

### 4.1. Integer — Số nguyên

**Từ vựng trong mục:** **Integer** — số nguyên; **Type** — kiểu dữ liệu.

`int` biểu diễn những số không có phần thập phân, ví dụ 5 sản phẩm hoặc 12 học viên. Dùng `int` khi cần đếm hoặc tính toán số lượng nguyên; khác với chuỗi `"5"`, số `5` thực hiện được phép cộng số học. Ở đây biến `n` giữ số 5 và `type(n)` kiểm tra kiểu.

**No Note — Không chú thích**

```python
n = 5
print(type(n))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Dùng type() để xác nhận biến n lưu số nguyên int.
# 5 không có dấu thập phân nên biến n thuộc kiểu int (số nguyên).
n = 5
# type(n) xác định kiểu dữ liệu của n; print() hiển thị kết quả <class 'int'>.
print(type(n))
```

**Kết quả khi chạy:**

```text
<class 'int'>
```

Kết quả cho biết `n` là số nguyên, không phải chuỗi.

### 4.2. Float — Số thực

**Từ vựng trong mục:** **Float** — số thực; **Decimal** — phần thập phân.

`float` lưu các số có phần thập phân, như 3,5 kg hàng hoặc nhiệt độ 36,5 °C. Nếu cần tính trên những số đo này, dùng số thực thay vì chữ. Trong ví dụ, `x` nhận `3.5` và `print()` hiển thị giá trị của nó.

**No Note — Không chú thích**

```python
x = 3.5
print(x)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Lưu và in giá trị x dạng số thực float.
# Số có phần thập phân được lưu dưới kiểu float.
x = 3.5
# print() hiển thị giá trị số thực, không thêm dấu nháy như khi in chuỗi.
print(x)
```

**Kết quả khi chạy:**

```text
3.5
```

Dấu chấm trong code biểu diễn phần thập phân; đơn vị đo phải được xác định theo bài toán.

### 4.3. Boolean — Giá trị đúng/sai

**Từ vựng trong mục:** **Boolean** — giá trị logic; **True/False** — đúng/sai.

`bool` chỉ có hai giá trị `True` và `False`, phù hợp với câu hỏi dạng “đã thanh toán chưa?” hoặc “đủ điều kiện chưa?”. Biến `ok = True` ở đây tượng trưng cho trạng thái kiểm tra đã đạt. Đây không phải chữ `"True"`: Python hiểu là giá trị logic.

**No Note — Không chú thích**

```python
ok = True
print(ok)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Thử kiểu Boolean: True biểu thị điều kiện đúng.
# True là giá trị Boolean đúng; phải viết hoa chữ T trong Python.
ok = True
# print() xuất True, không phải chuỗi ký tự 'True'.
print(ok)
```

**Kết quả khi chạy:**

```text
True
```

Đầu ra là giá trị logic `True`, không phải số 1 hoặc một thông báo khác.

### 4.4. String — Chuỗi ký tự

**Từ vựng trong mục:** **String** — chuỗi; **Slice** — cắt chuỗi.

`str` lưu dãy ký tự theo đúng thứ tự, kể cả chữ số nằm trong mã như `AB12` hoặc số điện thoại bắt đầu bằng 0. Với `code = 'AB12'`, các vị trí lần lượt là 0:A, 1:B, 2:1, 3:2. Cú pháp `[:2]` lấy ký tự ở vị trí 0 và 1, không lấy vị trí 2.

**No Note — Không chú thích**

```python
code = 'AB12'
print(code[:2])
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Lấy hai ký tự đầu của mã AB12 bằng phép cắt chuỗi.
# Mã chứa 4 ký tự dạng str (chuỗi), chưa phải số.
code = 'AB12'
# Cú pháp [bắt_đầu:kết_thúc] cắt chuỗi; [:2] lấy vị trí 0, 1, loại trừ vị trí 2 nên trả 'AB'.
print(code[:2])
```

**Kết quả khi chạy:**

```text
AB
```

Hai ký tự đầu được tách ra mà chuỗi ban đầu vẫn giữ nguyên.
## 5. Năm tình huống ứng dụng — tăng dần mức độ

### Tình huống 1 — Cấp 1: Chuẩn hóa mười địa chỉ liên hệ

**Từ vựng trong mục:** **String** — chuỗi; **Strip** — bỏ khoảng trắng; **Lower** — chữ thường.

**Tình huống thực tế:** Một nhóm hỗ trợ muốn gửi thông báo cho **10 tài khoản thử nghiệm**. Danh sách email được nhập với khoảng trắng ở đầu hoặc cuối và chữ hoa không thống nhất, như `  Member01@Example.INVALID  `. Mỗi dòng là một địa chỉ; nhóm cần nhận lại danh sách có cách viết thống nhất, số địa chỉ và địa chỉ đầu/ cuối sau khi xử lý.

**Vì sao chọn cách này?** `strip()` bỏ khoảng trắng **chỉ ở hai đầu** chuỗi, còn `lower()` đổi chữ hoa thành chữ thường. Ví dụ `" Member01@Example.INVALID "` trở thành `member01@example.invalid`, nên cùng một địa chỉ sẽ có cách viết nhất quán khi đối chiếu. Vòng `for` tạo danh sách đã xử lý từng dòng để dễ nhìn bước làm. Lưu ý đây mới là **chuẩn hóa cách viết**, không phải kiểm tra một email có tồn tại hoặc nhận được thư hay không; đuôi `.invalid` dùng cho dữ liệu minh họa.

**Quy trình:**
1. Lưu mười chuỗi email thử nghiệm.
2. Bỏ khoảng trắng biên rồi chuyển thành chữ thường.
3. In số email và hai email mẫu đã chuẩn hóa.

**No Note — Không chú thích**

```python
raw_emails = ["  Member01@Example.INVALID  ","  Member02@Example.INVALID  ","  Member03@Example.INVALID  ","  Member04@Example.INVALID  ","  Member05@Example.INVALID  ","  Member06@Example.INVALID  ","  Member07@Example.INVALID  ","  Member08@Example.INVALID  ","  Member09@Example.INVALID  ","  Member10@Example.INVALID  "]
cleaned = []
for email in raw_emails:
    normalized_email = email.strip().lower()
    cleaned.append(normalized_email)
if len(cleaned) != 10:
    raise ValueError("Phải chuẩn hóa đủ 10 địa chỉ email.")
print("Số email:", len(cleaned))
print("Đầu:", cleaned[0])
print("Cuối:", cleaned[-1])
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Chuẩn hóa 10 email: xóa khoảng trắng thừa và đổi về chữ thường.
# 10 chuỗi email ví dụ có khoảng trắng thừa và chữ hoa; mỗi phần tử là một địa chỉ.
raw_emails = ["  Member01@Example.INVALID  ","  Member02@Example.INVALID  ","  Member03@Example.INVALID  ","  Member04@Example.INVALID  ","  Member05@Example.INVALID  ","  Member06@Example.INVALID  ","  Member07@Example.INVALID  ","  Member08@Example.INVALID  ","  Member09@Example.INVALID  ","  Member10@Example.INVALID  "]
# Danh sách rỗng lưu email sau khi chuẩn hóa theo thứ tự đầu vào.
cleaned = []
# Vòng for lấy từng email làm đầu vào cho chuỗi thao tác làm sạch.
for email in raw_emails:
    # strip() bỏ khoảng trắng hai đầu; lower() đổi tất cả chữ cái thành chữ thường; gọi nối tiếp để làm cả hai bước.
    normalized_email = email.strip().lower()
    # append() đưa email đã làm sạch vào cuối danh sách.
    cleaned.append(normalized_email)
# len() đếm số email sau khi xử lý; != kiểm tra có thiếu/thừa so với 10 đầu vào.
if len(cleaned) != 10:
    # ValueError báo dữ liệu đầu vào sai số lượng và ngừng chương trình.
    raise ValueError("Phải chuẩn hóa đủ 10 địa chỉ email.")
print("Số email:", len(cleaned))
# [0] truy cập địa chỉ đầu tiên sau chuẩn hóa.
print("Đầu:", cleaned[0])
# [-1] truy cập địa chỉ cuối cùng, không cần tự tính chỉ số.
print("Cuối:", cleaned[-1])
```

**Kết quả khi chạy:**

```text
Số email: 10
Đầu: member01@example.invalid
Cuối: member10@example.invalid
```

Toàn bộ 10 email đã được chuyển đổi. Miền `.invalid` được dùng có chủ đích cho dữ liệu minh họa, không phải tài khoản thật.

### Tình huống 2 — Cấp 2: Tách nhãn sản phẩm trong 12 dòng nhập liệu

**Từ vựng trong mục:** **Split** — tách chuỗi; **Delimiter** — dấu phân cách; **Normalization** — chuẩn hóa.

**Tình huống thực tế:** Thư viện có **12 dòng ghi tên môn học** trên các thẻ đăng ký. Mỗi dòng chứa **hai nhãn** ngăn bằng dấu phẩy, ví dụ `python, AI`, nên 12 thẻ tạo ra nhiều hơn 12 lượt ghi nhãn. Nhân viên muốn biết từng môn như Python, AI, SQL xuất hiện bao nhiêu lần, dù người nhập có dùng chữ hoa hoặc khoảng trắng khác nhau.

**Vì sao chọn cách này?** Dấu phẩy đang có nhiệm vụ ngăn hai nhãn trong một dòng, vì vậy `split(',')` tách dòng thành từng phần. Sau đó `strip()` xóa khoảng trắng thừa và `lower()` giúp `Python` và `python` được đếm là **cùng một nhãn**. Dictionary `counts` lưu số lần xuất hiện của từng nhãn; mỗi khi gặp nhãn, tăng số đếm lên một. Không thể đếm số dòng thay cho số nhãn, vì một dòng chứa tới hai nhãn.

**Quy trình:**
1. Duyệt đủ 12 dòng, tách mỗi dòng thành hai nhãn.
2. Chuẩn hóa nhãn trước khi đưa vào bảng đếm.
3. In tổng dòng và số lần xuất hiện của từng nhãn theo thứ tự chữ cái.

**No Note — Không chú thích**

```python
raw_labels = ["python, AI","SQL, python","math, data","Python, SQL","AI, data","math, python","data, SQL","AI, Math","python, data","SQL, AI","Math, SQL","Python, AI"]
counts = {}
for text in raw_labels:
    for part in text.split(","):
        label = part.strip().lower()
        counts[label] = counts.get(label, 0) + 1
if len(raw_labels) != 12:
    raise ValueError("Phải có đủ 12 dòng nhãn sản phẩm.")
print("Số dòng:", len(raw_labels))
for label in sorted(counts):
    print(label, counts[label])
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tách 12 dòng nhãn sản phẩm, đếm số lần xuất hiện của từng nhãn.
# Mỗi chuỗi là một dòng gắn hai nhãn phân cách bởi dấu phẩy; 12 dòng có thể viết hoa/thường lẫn nhau.
raw_labels = ["python, AI","SQL, python","math, data","Python, SQL","AI, data","math, python","data, SQL","AI, Math","python, data","SQL, AI","Math, SQL","Python, AI"]
# Dictionary (từ điển) ánh xạ tên nhãn sang số lần xuất hiện, ban đầu chưa có nhãn nào.
counts = {}
# Duyệt từng dòng; vòng for bên trong xử lý từng nhãn của dòng.
for text in raw_labels:
    # split(',') tách chuỗi tại mỗi dấu phẩy và trả danh sách các phần nhãn.
    for part in text.split(","):
        # strip() loại khoảng trắng cạnh nhãn; lower() gộp 'Python' và 'python' thành một nhãn.
        label = part.strip().lower()
        # get(label, 0) đọc số đếm hiện có hoặc lấy 0 nếu nhãn chưa gặp; cộng 1 và ghi lại vào dictionary.
        counts[label] = counts.get(label, 0) + 1
# Xác nhận đã nhận đủ 12 dòng nguồn, không phải 12 nhãn.
if len(raw_labels) != 12:
    # raise ValueError báo lỗi nếu số dòng nguồn bị sai.
    raise ValueError("Phải có đủ 12 dòng nhãn sản phẩm.")
print("Số dòng:", len(raw_labels))
# sorted(counts) lấy các khóa nhãn theo thứ tự chữ cái để in báo cáo ổn định.
for label in sorted(counts):
    # counts[label] tra số lần xuất hiện của nhãn; print in tên nhãn và số lượng.
    print(label, counts[label])
```

**Kết quả khi chạy:**

```text
Số dòng: 12
ai 5
data 4
math 4
python 6
sql 5
```

Mỗi dòng đóng góp hai nhãn, tổng tất cả số đếm phải bằng 24. Đây là sự khác biệt giữa dữ liệu gốc có nhiều cách viết và từ vựng đã chuẩn hóa.

### Tình huống 3 — Cấp 3: Giữ số 0 ở đầu của 15 mã đơn hàng

**Từ vựng trong mục:** **Identifier** — mã định danh; **Slice** — cắt chuỗi; **Integer** — số nguyên.

**Tình huống thực tế:** Kho nhận **15 mã đơn hàng** gồm đúng **5 chữ số**, ví dụ `00001`. Đây là **mã nhận diện** dùng để tìm đơn, không phải số lượng, và lúc nhập có thể có khoảng trắng ở hai đầu. Người quản lý muốn kiểm tra từng mã còn đủ 5 chữ số, đồng thời hiển thị mã đầu và cuối mà vẫn giữ số 0 ở đầu.

**Vì sao chọn cách này?** Chữ số 0 đầu tiên trong `00001` là **một phần của mã**. Nếu đổi sang số nguyên `int`, chương trình sẽ chỉ còn `1`, làm mất dạng mã khi đối chiếu chứng từ. Giữ mã là **chuỗi**, dùng `strip()` bỏ khoảng trắng, `isdigit()` kiểm tra có đúng toàn chữ số, rồi `len()` kiểm tra đúng năm ký tự. Slicing như `code[:3]` chỉ lấy một phần ký tự để xem, không đổi mã gốc.

**Quy trình:**
1. Lưu 15 mã chuỗi.
2. Bỏ khoảng trắng và kiểm tra mã chỉ có năm chữ số.
3. In các mẫu đầu/cuối cùng ba ký tự đầu của mã đầu.

**No Note — Không chú thích**

```python
raw_codes = ["  00001  ","  00002  ","  00003  ","  00004  ","  00005  ","  00006  ","  00007  ","  00008  ","  00009  ","  00010  ","  00011  ","  00012  ","  00013  ","  00014  ","  00015  "]
codes = []
for code in raw_codes:
    cleaned_code = code.strip()
    codes.append(cleaned_code)
valid = True
for code in codes:
    if not code.isdigit() or len(code) != 5:
        valid = False
        break
if len(codes) != 15:
    raise ValueError("Phải kiểm tra đủ 15 mã đơn hàng.")
print("Số mã:", len(codes))
print("Đều hợp lệ:", valid)
print("Mã đầu:", codes[0], "| đầu mã:", codes[0][:3])
print("Mã cuối:", codes[-1])
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Làm sạch và kiểm tra 15 mã số vẫn giữ đủ năm ký tự, kể cả số 0 đầu.
# 15 mã số dạng chuỗi có các số 0 đầu và khoảng trắng thừa; giữ kiểu chuỗi để không mất số 0.
raw_codes = ["  00001  ","  00002  ","  00003  ","  00004  ","  00005  ","  00006  ","  00007  ","  00008  ","  00009  ","  00010  ","  00011  ","  00012  ","  00013  ","  00014  ","  00015  "]
# Danh sách lưu mã đã làm sạch, vẫn là chuỗi.
codes = []
for code in raw_codes:
    # strip() bỏ khoảng trắng đầu/cuối nhưng bảo toàn '00001'.
    cleaned_code = code.strip()
    # append() thêm mã sạch vào danh sách.
    codes.append(cleaned_code)
# Giả định các mã hợp lệ; gặp mã lỗi thì chuyển cờ valid thành False.
valid = True
for code in codes:
    # isdigit() kiểm tra tất cả ký tự là chữ số; len() phải bằng 5; not và or bắt mọi trường hợp sai.
    if not code.isdigit() or len(code) != 5:
        valid = False
        # break dừng vòng kiểm tra ngay khi tìm thấy mã không hợp lệ.
        break
# Đảm bảo đã xử lý đủ 15 mã từ nguồn.
if len(codes) != 15:
    # Báo ValueError nếu thiếu hoặc thừa mã nguồn.
    raise ValueError("Phải kiểm tra đủ 15 mã đơn hàng.")
print("Số mã:", len(codes))
print("Đều hợp lệ:", valid)
# [0] lấy mã đầu, [:3] cắt ba ký tự đầu ở vị trí 0, 1, 2; không biến mã thành số.
print("Mã đầu:", codes[0], "| đầu mã:", codes[0][:3])
# [-1] là mã cuối danh sách.
print("Mã cuối:", codes[-1])
```

**Kết quả khi chạy:**

```text
Số mã: 15
Đều hợp lệ: True
Mã đầu: 00001 | đầu mã: 000
Mã cuối: 00015
```

Đủ 15 mã được giữ nguyên 5 ký tự. Nếu dùng phép đổi sang số nguyên, thông tin định danh `00001` sẽ thành `1` và không còn đúng định dạng.

### Tình huống 4 — Cấp 4: Làm sạch 18 giá đọc từ CSV

**Từ vựng trong mục:** **Float** — số thực; **Conversion** — đổi kiểu; **Invalid input** — đầu vào sai.

**Tình huống thực tế:** Nhà cung cấp gửi bảng **18 đơn giá** tính bằng **nghìn đồng/món**, tương ứng lần lượt các mã P01 đến P18. Mỗi giá đang được lưu ở dạng chữ để mô phỏng nội dung đọc từ CSV; dòng P03 ghi `bad`, dòng P14 để trống. Nhân viên cần cộng tổng các giá có thể đọc thành số, đếm các giá hợp lệ và báo đúng mã phải sửa; không được cộng các dòng lỗi như số 0.

**Vì sao chọn cách này?** Không phải chuỗi nào cũng đổi được thành số: `"12.5"` là giá có thể đọc, còn `bad` hoặc chuỗi rỗng là thông tin cần sửa. Chương trình làm sạch khoảng trắng rồi kiểm tra xem nội dung có chữ số và nhiều nhất một dấu chấm trước khi dùng `float()`. Phải **tách mã lỗi** và chỉ cộng các giá hợp lệ; nếu cố đổi `bad`, chương trình có thể dừng vì lỗi. Giá ở đây có đơn vị nghìn đồng, vì vậy tổng cũng là nghìn đồng, không tự hiểu thành đồng.

**Quy trình:**
1. Gán 18 mã giá theo thứ tự.
2. Bỏ khoảng trắng, kiểm tra định dạng số thập phân không âm.
3. Đổi số hợp lệ thành `float`, ghi lại ID không hợp lệ rồi cộng các giá trị hợp lệ.

**No Note — Không chú thích**

```python
raw_prices = ["12.5","8.0","bad","7.5","13.0","10.0","19.5","6.5","11.0","15.5","9.0","16.0","20.0","","10.5","14.5","8.5","12.0"]
valid_prices = []
invalid_ids = []
for index, raw in enumerate(raw_prices, 1):
    clean = raw.strip()
    if not clean.replace(".", "", 1).isdigit():
        invalid_ids.append(f"P{index:02d}")
        continue
    valid_prices.append(float(clean))
if len(raw_prices) != 18:
    raise ValueError("Phải có đúng 18 chuỗi đơn giá.")
print("Giá hợp lệ:", len(valid_prices))
print("Giá lỗi:", ", ".join(invalid_ids))
print(f"Tổng giá (nghìn đồng): {sum(valid_prices):.1f}")
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Phát hiện các chuỗi đơn giá không hợp lệ trong 18 phiếu và cộng giá hợp lệ.
# 18 đơn giá ở dạng chuỗi, đơn vị nghìn đồng; 'bad' và chuỗi rỗng là dữ liệu lỗi.
raw_prices = ["12.5","8.0","bad","7.5","13.0","10.0","19.5","6.5","11.0","15.5","9.0","16.0","20.0","","10.5","14.5","8.5","12.0"]
# Lưu các số thực đã được xác minh để cộng, tách khỏi chuỗi không hợp lệ.
valid_prices = []
# Lưu mã dòng lỗi theo thứ tự xuất hiện.
invalid_ids = []
# enumerate(..., 1) đánh số dòng từ 1, giúp mã P01 tương ứng giá đầu tiên.
for index, raw in enumerate(raw_prices, 1):
    # strip() xóa khoảng trắng hai đầu trước khi kiểm tra chuỗi.
    clean = raw.strip()
    # replace('.', '', 1) xóa tối đa một dấu chấm thập phân; isdigit() kiểm tra phần còn lại là chữ số; not tìm chuỗi sai. Đây là quy tắc minh họa cho giá không âm, chưa xử lý dấu âm hay định dạng số tổng quát.
    if not clean.replace(".", "", 1).isdigit():
        # append() lưu mã giá lỗi; f-string :02d tạo số thứ tự hai chữ số như P03.
        invalid_ids.append(f"P{index:02d}")
        # continue bỏ phiếu giá lỗi, không gọi float() với chuỗi không chuyển được.
        continue
    # float() chuyển chuỗi thập phân sang số thực; append() thêm vào danh sách hợp lệ.
    valid_prices.append(float(clean))
# Kiểm tra đúng 18 dòng đầu vào, gồm cả giá lỗi.
if len(raw_prices) != 18:
    # ValueError thông báo thiếu/thừa dòng trong bộ dữ liệu.
    raise ValueError("Phải có đúng 18 chuỗi đơn giá.")
print("Giá hợp lệ:", len(valid_prices))
# join() ghép danh sách mã lỗi bằng dấu phẩy và khoảng trắng.
print("Giá lỗi:", ", ".join(invalid_ids))
# sum() cộng toàn bộ giá hợp lệ; :.1f hiển thị kết quả với một chữ số sau dấu thập phân, đơn vị nghìn đồng.
print(f"Tổng giá (nghìn đồng): {sum(valid_prices):.1f}")
```

**Kết quả khi chạy:**

```text
Giá hợp lệ: 16
Giá lỗi: P03, P14
Tổng giá (nghìn đồng): 194.0
```

Đây là tổng **16 đơn giá mẫu**, không phải doanh thu; để tính doanh thu còn cần số lượng bán tương ứng. Quy tắc kiểm tra ký tự chỉ phù hợp với định dạng số không âm đơn giản của bài.

### Tình huống 5 — Cấp 5: Chuẩn hóa, kiểm tra và che 20 mã hồ sơ

**Từ vựng trong mục:** **Boolean** — đúng/sai; **String validation** — kiểm tra chuỗi; **Masking** — che thông tin.

**Tình huống thực tế:** Hệ thống nhận **20 mã hồ sơ thử nghiệm**. Mã đúng có dạng `ID-` rồi tới **bốn chữ số**, chẳng hạn `ID-0001`; khoảng trắng đầu/cuối không mang ý nghĩa của mã. Trong dữ liệu có mã sai tiền tố, mã thiếu chữ số và mã xuất hiện hai lần. Nhân viên cần đếm số mã hợp lệ duy nhất, tách danh sách lỗi và trùng, sau đó hiển thị một mã dưới dạng che bớt phần đầu khi báo cáo.

**Vì sao chọn cách này?** Đầu tiên `strip().upper()` đưa mọi mã về cách viết thống nhất, rồi chương trình kiểm tra phần tiền tố `ID-` và bốn chữ số cuối. Một mã xuất hiện lần thứ hai là **trùng**, khác với mã nhập sai định dạng; nên chia chúng thành các nhóm riêng. Set `seen` ghi nhớ mã đã gặp: trước khi thêm mã mới, kiểm tra nó đã có trong set chưa. Việc chỉ hiển thị hai chữ số cuối giúp báo cáo không đưa nguyên mã ra màn hình; đây là ví dụ **che bớt ký tự**, chưa phải giải pháp bảo mật dữ liệu đầy đủ.

**Quy trình:**
1. Chuẩn hóa 20 chuỗi, tách tiền tố và hậu tố.
2. Xác nhận độ dài và chữ số, kiểm tra mã đã xuất hiện chưa.
3. Chỉ giữ mã hợp lệ, báo mã sai/trùng và in một mã đã che.

**No Note — Không chú thích**

```python
raw_ids = [" ID-0001 "," ID-0002 "," ID-0003 "," ID-0004 "," ID-0005 "," ID-0006 ","X-0007"," ID-0008 "," ID-0009 "," ID-0010 "," ID-0011 "," ID-0004 "," ID-0013 "," ID-0014 "," ID-0015 "," ID-0016 "," ID-0017 "," ID- "," ID-0019 "," ID-0020 "]
accepted = []
invalid = []
duplicates = []
seen = set()
for raw in raw_ids:
    code = raw.strip().upper()
    suffix = code[3:]
    if not (code.startswith("ID-") and len(suffix) == 4 and suffix.isdigit()):
        invalid.append(code)
    elif code in seen:
        duplicates.append(code)
    else:
        seen.add(code)
        accepted.append(code)
if len(raw_ids) != 20:
    raise ValueError("Phải có đúng 20 mã hồ sơ để kiểm tra.")
print("Đầu vào:", len(raw_ids))
print("Hợp lệ duy nhất:", len(accepted))
print("Sai định dạng:", len(invalid))
print("Trùng:", duplicates)
print("Mã đầu đã che:", "ID-**" + accepted[0][-2:])
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Kiểm tra 20 mã hồ sơ: đúng định dạng, không trùng và chỉ hiển thị một phần mã.
# 20 mã hồ sơ dạng chuỗi; có mã sai tiền tố, mã rút ngắn và mã lặp cần phát hiện.
raw_ids = [" ID-0001 "," ID-0002 "," ID-0003 "," ID-0004 "," ID-0005 "," ID-0006 ","X-0007"," ID-0008 "," ID-0009 "," ID-0010 "," ID-0011 "," ID-0004 "," ID-0013 "," ID-0014 "," ID-0015 "," ID-0016 "," ID-0017 "," ID- "," ID-0019 "," ID-0020 "]
accepted = []
invalid = []
duplicates = []
# set() tạo tập hợp lưu mã đã gặp, giúp kiểm tra trùng nhanh bằng toán tử in.
seen = set()
# Kiểm tra lần lượt từng mã gốc, giữ thứ tự báo cáo.
for raw in raw_ids:
    # strip() bỏ khoảng trắng; upper() đổi chữ cái thành viết hoa để chuẩn hóa tiền tố.
    code = raw.strip().upper()
    # [3:] lấy mọi ký tự từ vị trí 3 trở đi sau tiền tố ba ký tự 'ID-'.
    suffix = code[3:]
    # startswith('ID-') kiểm tra tiền tố; len()==4 kiểm tra 4 ký tự hậu tố; isdigit() đảm bảo toàn chữ số; and đòi đủ điều kiện, not nhận diện mã sai.
    if not (code.startswith("ID-") and len(suffix) == 4 and suffix.isdigit()):
        # append() ghi riêng mã không đúng định dạng, chưa đưa vào danh sách hợp lệ.
        invalid.append(code)
    # in kiểm tra mã đã xuất hiện trong tập seen; elif chỉ chạy khi định dạng đã hợp lệ.
    elif code in seen:
        # Ghi mã trùng vào danh sách để rà soát.
        duplicates.append(code)
    else:
        # add() thêm mã hợp lệ mới vào tập để phát hiện lần xuất hiện sau.
        seen.add(code)
        # append() giữ danh sách mã hợp lệ duy nhất theo thứ tự ban đầu.
        accepted.append(code)
# Xác nhận đầu vào đủ 20 hồ sơ, kể cả mã sai.
if len(raw_ids) != 20:
    # Dừng và báo ValueError nếu số hồ sơ không đủ.
    raise ValueError("Phải có đúng 20 mã hồ sơ để kiểm tra.")
print("Đầu vào:", len(raw_ids))
print("Hợp lệ duy nhất:", len(accepted))
print("Sai định dạng:", len(invalid))
print("Trùng:", duplicates)
# accepted[0] là mã hợp lệ đầu, [-2:] lấy hai ký tự cuối; nối với 'ID-**' để che phần giữa khi hiển thị.
print("Mã đầu đã che:", "ID-**" + accepted[0][-2:])
```

**Kết quả khi chạy:**

```text
Đầu vào: 20
Hợp lệ duy nhất: 17
Sai định dạng: 2
Trùng: ['ID-0004']
Mã đầu đã che: ID-**01
```

20 đầu vào được chia thành 17 mã hợp lệ duy nhất, hai mã sai và một bản sao; phép che chỉ giảm khả năng lộ mã trong bản tin, **không phải mã hóa hay biện pháp bảo mật hoàn chỉnh**.

## 6. Những nhầm lẫn thường gặp

- `int("12.5")` gây lỗi vì chuỗi này không viết theo dạng số nguyên; dùng `float("12.5")` nếu cần số có phần thập phân.
- Không chuyển mã đơn hoặc số điện thoại sang `int` nếu cần giữ số `0` ở đầu.
- `strip()` chỉ bỏ khoảng trắng ở hai đầu chuỗi; `lower()` không tự kiểm tra email hợp lệ.
- `s[:3]` lấy ba ký tự đầu (vị trí 0, 1, 2), không lấy ký tự ở vị trí 3.

## 7. Trắc nghiệm

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. Which description best defines an integer in Python? | Mô tả nào đúng nhất về số nguyên trong Python?**

A. An ordered sequence of characters | Dãy ký tự có thứ tự

B. A negative, zero, or positive integer without a fractional part | Số nguyên âm, số 0 hoặc số nguyên dương không có phần lẻ

C. A true/false value | Một giá trị đúng/sai

D. A floating-point number | Số thực dấu phẩy động

**Đáp án: B**

**Giải thích:** Kiểu `int` của Python lưu chính xác các số nguyên âm, số 0 và số nguyên dương như `-3`, `0`, `12`. Không loại số âm khỏi kiểu này; khác với `int`, `float` biểu diễn số dấu phẩy động, kể cả `2.0`.


**Q2. What is a float? | Float là kiểu dữ liệu nào?**

A. A whole number without a fractional part | Số không có phần thập phân

B. A floating-point number | Số thực dấu phẩy động

C. A true/false value | Một giá trị đúng/sai

D. An ordered sequence of characters | Dãy ký tự có thứ tự

**Đáp án: B**

**Giải thích:** `float` là kiểu số dấu phẩy động trong Python, ví dụ `1.5` và `2.0`. Ngay cả `2.0` dù có giá trị toán học nguyên vẫn là `float` chứ không phải `int`.


**Q3. What is a Boolean? | Boolean là gì?**

A. A true/false value | Một giá trị đúng/sai

B. A floating-point number | Số thực dấu phẩy động

C. An ordered sequence of characters | Dãy ký tự có thứ tự

D. A whole number without a fractional part | Số không có phần thập phân

**Đáp án: A**

**Giải thích:** Boolean biểu diễn một trong hai trạng thái `True` hoặc `False`, thường dùng trong điều kiện như `3 > 2`. Vai trò của nó khác việc lưu số hoặc dãy ký tự có thứ tự.


**Q4. What is a string? | Chuỗi là gì?**

A. An ordered sequence of characters | Dãy ký tự có thứ tự

B. A whole number without a fractional part | Số không có phần thập phân

C. A floating-point number | Số thực dấu phẩy động

D. A true/false value | Một giá trị đúng/sai

**Đáp án: A**

**Giải thích:** Chuỗi (`str`) là dãy ký tự Unicode có thứ tự, chẳng hạn `'Python'`. Chuỗi chữ số như `'12'` vẫn là văn bản nên cộng với chuỗi khác sẽ nối chữ, không phải cộng số.


**Q5. What does `strip()` normally remove? | `strip()` thường loại bỏ gì?**

A. Whitespace at both ends | Khoảng trắng ở hai đầu

B. Text converted to lowercase | Văn bản chuyển sang chữ thường

C. Text converted to uppercase | Văn bản chuyển sang chữ hoa

D. Substitutes matching text | Thay các đoạn chữ khớp mẫu

**Đáp án: A**

**Giải thích:** Khi không truyền tham số, `strip()` bỏ khoảng trắng ở đầu và cuối, không xóa khoảng trắng giữa chuỗi. Ví dụ `'  a b  '.strip()` thành `'a b'` và giữ dấu cách giữa `a` và `b`.


**Q6. What does `lower()` return? | `lower()` trả về gì?**

A. Substitutes matching text | Thay các đoạn chữ khớp mẫu

B. Text converted to uppercase | Văn bản chuyển sang chữ hoa

C. Text converted to lowercase | Văn bản chuyển sang chữ thường

D. Whitespace at both ends | Khoảng trắng ở hai đầu

**Đáp án: C**

**Giải thích:** `lower()` trả về bản sao chữ thường, nên `'PyThOn'.lower()` được `'python'`. Hàm không sửa chuỗi gốc tại chỗ vì chuỗi là bất biến.


**Q7. What does `upper()` return? | `upper()` trả về gì?**

A. Whitespace at both ends | Khoảng trắng ở hai đầu

B. Substitutes matching text | Thay các đoạn chữ khớp mẫu

C. Text converted to lowercase | Văn bản chuyển sang chữ thường

D. Text converted to uppercase | Văn bản chuyển sang chữ hoa

**Đáp án: D**

**Giải thích:** `upper()` trả về chữ hoa, ví dụ `'ab'.upper()` là `'AB'`. Khác `lower()`, nó đổi chữ cái về dạng hoa; ký tự như chữ số vẫn giữ nguyên.


**Q8. What does `replace(old, new)` do? | `replace(old, new)` có tác dụng gì?**

A. Whitespace at both ends | Khoảng trắng ở hai đầu

B. Text converted to uppercase | Văn bản chuyển sang chữ hoa

C. Text converted to lowercase | Văn bản chuyển sang chữ thường

D. Substitutes matching text | Thay các đoạn chữ khớp mẫu

**Đáp án: D**

**Giải thích:** `replace(old, new)` trả về chuỗi mới sau khi thay các đoạn khớp; `'aba'.replace('a', 'x')` được `'xbx'`. Hàm không sửa chuỗi gốc và không chỉ đơn thuần đổi hoa/thường.


**Q9. What does `'a,b'.split(',')` return? | `'a,b'.split(',')` trả về gì?**

A. `['a', 'b']` | `['a', 'b']`

B. `'ab'` | `'ab'`

C. `('a', 'b')` | `('a', 'b')`

D. `['a,b']` | `['a,b']`

**Đáp án: A**

**Giải thích:** `split(',')` tách văn bản tại mỗi dấu phẩy và trả về danh sách các chuỗi con: `'a,b'` thành `['a', 'b']`. Dấu phẩy là dấu phân cách nên bị bỏ đi; kết quả là list chứ không phải một chuỗi.


**Q10. What does `'ABCD'[1:3]` yield? | `'ABCD'[1:3]` cho kết quả gì?**

A. `'CD'` | `'CD'`

B. `'AB'` | `'AB'`

C. `'BC'` | `'BC'`

D. `'BCD'` | `'BCD'`

**Đáp án: C**

**Giải thích:** Chỉ số chuỗi bắt đầu từ 0, nên trong `'ABCD'`, vị trí 1 và 2 là `B` và `C`. Lát cắt `[1:3]` lấy vị trí 1 nhưng không lấy mốc dừng 3, cho `'BC'`.


**Q11. What does `len('Python')` yield? | `len('Python')` trả về gì?**

A. `5` | `5`

B. `7` | `7`

C. `'6'` (string) | `'6'` (chuỗi)

D. `6` (integer) | `6` (số nguyên)

**Đáp án: D**

**Giải thích:** `len()` đếm số ký tự trong chuỗi: `P`, `y`, `t`, `h`, `o`, `n` là sáu ký tự. Hàm trả về số nguyên `6`, không phải chuỗi `'6'`; chữ hoa/thường không đổi số lượng.


**Q12. What does `'A'.join(['x','y'])` yield? | `'A'.join(['x','y'])` tạo gì?**

A. `['x', 'A', 'y']` | `['x', 'A', 'y']`

B. `'xyA'` | `'xyA'`

C. `'xAy'` | `'xAy'`

D. `'Axy'` | `'Axy'`

**Đáp án: C**

**Giải thích:** `join()` chèn chuỗi đứng trước dấu chấm vào giữa các phần tử: `'A'.join(['x','y'])` cho `'xAy'`. Nó không thêm `A` ở đầu toàn danh sách hoặc sau phần tử cuối.


**Q13. What does `int('12')` create? | `int('12')` tạo ra gì?**

A. `ValueError` | `ValueError`

B. `12` (integer) | `12` (số nguyên)

C. `12.0` (float) | `12.0` (số thực)

D. `'12'` (string) | `'12'` (chuỗi)

**Đáp án: B**

**Giải thích:** `int('12')` đổi chuỗi số nguyên hợp lệ thành số nguyên `12` để có thể tính toán. Kết quả không còn là văn bản `'12'` và cũng không phải số thực `12.0`.


**Q14. What does `float('1.5')` create? | `float('1.5')` tạo ra gì?**

A. `ValueError` | `ValueError`

B. `1` (integer) | `1` (số nguyên)

C. `'1.5'` (string) | `'1.5'` (chuỗi)

D. `1.5` (float) | `1.5` (số thực)

**Đáp án: D**

**Giải thích:** `float('1.5')` chuyển văn bản số hợp lệ thành số thực `1.5`. Nó giữ phần lẻ thay vì cắt thành số nguyên `1`, và chuỗi hợp lệ này không gây lỗi.


**Q15. What does `str(12)` create? | `str(12)` tạo gì?**

A. `['1', '2']` | `['1', '2']`

B. `'12'` (string) | `'12'` (chuỗi)

C. `12.0` (float) | `12.0` (số thực)

D. `12` (integer) | `12` (số nguyên)

**Đáp án: B**

**Giải thích:** `str(12)` tạo biểu diễn văn bản `'12'`, phù hợp làm nhãn hoặc nối chuỗi. Kết quả không còn là số nguyên `12`: `'12' + '3'` tạo `'123'`, không phải tổng số `15`.


**Q16. What does `bool('False')` return? | `bool('False')` trả về gì?**

A. `True` | `True`

B. `False` | `False`

C. `ValueError` | `ValueError`

D. `'False'` (string) | `'False'` (chuỗi)

**Đáp án: A**

**Giải thích:** `bool()` kiểm tra tính đúng/sai của giá trị, không đọc nghĩa chữ `True` hay `False` trong văn bản. Do chuỗi `'False'` không rỗng nên `bool('False')` bằng `True`; với chuỗi, chỉ chuỗi rỗng được xem là sai.


**Q17. What is true of Python strings? | Điều nào đúng về chuỗi Python?**

A. Strings are unordered collections | Chuỗi là tập hợp không có thứ tự

B. Strings store only numbers | Chuỗi chỉ lưu số

C. Strings are immutable | Chuỗi không thể sửa trực tiếp từng ký tự

D. Strings can be changed in place with `s[0] = 'x'` | Có thể đổi chuỗi tại chỗ bằng `s[0] = 'x'`

**Đáp án: C**

**Giải thích:** Chuỗi là bất biến: gán `s[0] = 'x'` gây `TypeError`, kể cả khi `s` không rỗng. Các phép như `replace()` tạo chuỗi mới thay vì sửa từng ký tự của chuỗi cũ.


**Q18. What does `s[-1]` select for a nonempty string? | `s[-1]` lấy gì khi chuỗi không rỗng?**

A. The first character | Ký tự đầu

B. Always raises `IndexError` | Luôn gây `IndexError`

C. The final two characters | Hai ký tự cuối

D. The last character | Ký tự cuối

**Đáp án: D**

**Giải thích:** Chỉ số `-1` đếm từ cuối và lấy ký tự cuối của chuỗi không rỗng. Với `s = 'cat'`, `s[-1]` là `'t'`, còn `s[0]` lấy `'c'`.


**Q19. What does `'Ab' == 'ab'` evaluate to? | `'Ab' == 'ab'` có giá trị gì?**

A. `'False'` (string) | `'False'` (chuỗi)

B. `True` (Boolean) | `True` (Boolean)

C. `False` (Boolean) | `False` (Boolean)

D. `0` (integer) | `0` (số nguyên)

**Đáp án: C**

**Giải thích:** So sánh chuỗi xét từng ký tự và phân biệt chữ hoa/thường: `'A'` khác `'a'` nên `'Ab' == 'ab'` cho Boolean `False`. Nếu đổi cả hai chuỗi về chữ thường trước khi so sánh thì kết quả sẽ khác.


**Q20. What is the result of `'4' + '2'`? | `'4' + '2'` cho kết quả gì?**

A. `TypeError` | `TypeError`

B. `'42'` (string) | `'42'` (chuỗi)

C. `'6'` (string) | `'6'` (chuỗi)

D. `6` (integer) | `6` (số nguyên)

**Đáp án: B**

**Giải thích:** Cả hai toán hạng đều là chuỗi nên `+` nối theo thứ tự: `'4' + '2'` được `'42'`. Muốn cộng số, cần đổi kiểu trước, ví dụ `int('4') + int('2')` cho số nguyên `6`.

## 8. Nối sang bài kế tiếp

`Biến → int/float/bool/str → Slicing → Xử lý văn bản`.
