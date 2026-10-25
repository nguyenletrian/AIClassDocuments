# PY-12 — File I/O, CSV và xử lý ngoại lệ

*DRAFT · Tài liệu tự học · Các mã và dữ liệu mẫu cần được kiểm tra trước khi công bố chính thức*

## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **File I/O** — đọc ghi file; **CSV** — dữ liệu phân cách.

`Dictionary → File/CSV → DataFrame → Dataset AI`

**Học xong dùng để làm gì?** Đọc CSV, ghi kết quả, xử lý lỗi chuyển kiểu và đóng file an toàn.

**Kết nối kiến thức tiếp theo:** PY-13 đưa bảng số liệu vào mảng NumPy để tính theo hàng/cột.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| File I/O | đọc ghi file | Lấy hoặc lưu dữ liệu trên đĩa |
| CSV | dữ liệu phân cách | Định dạng bảng dạng văn bản |
| Exception | ngoại lệ | Lỗi xuất hiện khi chạy chương trình |
| Context manager | quản lý ngữ cảnh | Tự đóng tài nguyên sau khối with |

## 3. Thư viện, hàm và tham số

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm/cú pháp | Giải thích và lý do dùng |
|---|---|
| `open(...,encoding='utf-8')` | Đọc/ghi Unicode và tự đóng bằng with |
| `csv.DictReader/DictWriter` | Đọc và ghi CSV theo tên cột thay vì vị trí |
| `try/except ValueError` | Bắt riêng lỗi dữ liệu nhập không hợp lệ |
| `Path.read_text()/write_text()` | Đọc/ghi file với đường dẫn kiểu Path |

## 4. Khái niệm liên quan

Một chương trình thực tế cần **lưu và đọc lại dữ liệu**, hiểu cấu trúc bảng CSV và xử lý đúng lỗi đầu vào. Bốn khái niệm File I/O, CSV, Exception và Context manager liên kết thành một quy trình: nhận dữ liệu → đọc/ghi an toàn → xử lý trường hợp bất thường.

### 4.1. File I/O — Đọc và ghi dữ liệu

**Từ vựng trong mục:** **File I/O** — đọc/ghi tệp; **Path** — đường dẫn.

**File I/O** (input/output) là việc đưa dữ liệu **từ tệp vào chương trình** hoặc **từ chương trình ra tệp**. Ví dụ hệ thống cần lưu trạng thái `Started` để lần chạy sau có thể đọc lại. Trong đoạn minh họa, `TemporaryDirectory()` tạo thư mục tạm, `Path` xác định đường dẫn `log.txt`, `write_text()` ghi và `read_text()` đọc. Dữ liệu chỉ tồn tại trong thư mục tạm trong suốt khối `with`, tránh để lại file rác.

```python
# Mục đích: Đọc và ghi dữ liệu.
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    file_path = Path(folder) / 'log.txt'
    file_path.write_text('Started', encoding='utf-8')
    print(file_path.read_text(encoding='utf-8'))
```

**Kết quả khi chạy:**

```text
Started
```

Đầu ra đúng chuỗi đã ghi. `encoding='utf-8'` hỗ trợ văn bản tiếng Việt; tệp tạm được xóa sau khi ra khỏi khối.

### 4.2. CSV — Bảng dữ liệu phân cách bằng dấu phẩy

**Từ vựng trong mục:** **CSV** — dữ liệu phân cách; **Row/column** — hàng/cột.

**CSV** lưu dữ liệu dạng văn bản: **mỗi dòng là một bản ghi**, các giá trị trên một dòng được tách bằng dấu phẩy. Ví dụ bảng sản phẩm có **hai cột** `name` (tên hàng) và `price` (giá) cùng **hai hàng** Pen/10 và Book/35. `csv.DictReader` coi hàng đầu là tên cột và đọc mỗi hàng sau thành Dictionary, giúp tra `row['name']` thay vì nhớ vị trí cột. Giá đọc từ CSV ban đầu là **chuỗi**, muốn tính toán phải chuyển kiểu sau.

```python
# Mục đích: Bảng dữ liệu phân cách bằng dấu phẩy.
import csv
from io import StringIO

csv_text = 'name,price\nPen,10\nBook,35\n'
rows = list(csv.DictReader(StringIO(csv_text)))
print(rows[1]['name'], rows[1]['price'])
```

**Kết quả khi chạy:**

```text
Book 35
```

Hàng dữ liệu thứ hai là Book, giá `35` đang ở dạng chuỗi; mã không tự đổi nó thành số nguyên.

### 4.3. Exception — Lỗi có thể xử lý

**Từ vựng trong mục:** **Exception** — ngoại lệ; **ValueError** — lỗi giá trị.

Khi chương trình nhận dữ liệu sai kiểu, không phải toàn bộ ứng dụng đều cần dừng. Chẳng hạn biểu mẫu yêu cầu số nguyên nhưng khách nhập `'abc'`; `int('abc')` sinh **`ValueError`**. Khối `try` chứa thao tác có thể lỗi, còn `except ValueError` chỉ bắt loại lỗi dự kiến và in thông báo. Không dùng `except:` quá rộng vì sẽ che mất những lỗi khác cần được sửa.

```python
# Mục đích: Lỗi có thể xử lý.
try:
    number = int('abc')
    print(number)
except ValueError:
    print('Invalid integer')
```

**Kết quả khi chạy:**

```text
Invalid integer
```

Chỉ nhánh `except` chạy, vì chuỗi `abc` không thể chuyển thành số nguyên.

### 4.4. Context manager — Tự quản lý tài nguyên

**Từ vựng trong mục:** **Context manager** — quản lý ngữ cảnh; **with** — khối sử dụng tài nguyên.

Khi mở file hoặc bộ đệm, ta cần **đóng tài nguyên** sau khi dùng, kể cả khi có lỗi. Cấu trúc `with ... as ...:` nhận một tài nguyên rồi tự đóng khi thoát khối. Ví dụ `StringIO` là bộ đệm văn bản trong bộ nhớ, có thao tác đọc giống file, không cần tạo file thật. Ta có thể kiểm tra `stream.closed` sau khối `with` để thấy nó đã đóng.

```python
# Mục đích: Tự quản lý tài nguyên.
from io import StringIO

with StringIO('abc') as stream:
    print(stream.read())

print(stream.closed)
```

**Kết quả khi chạy:**

```text
abc
True
```

Dòng đầu là nội dung đã đọc; `True` xác nhận bộ đệm được đóng sau khi ra khỏi `with`.
## 5. Năm tình huống File/CSV — từ đọc một bảng đến pipeline kiểm lỗi

### Tình huống 1 — Cấp 1: Đọc CSV 10 mặt hàng bằng DictReader

**Từ vựng trong mục:** **CSV** — bảng ngăn cách; **DictReader** — đọc theo tên cột.

**Tình huống thực tế:** Quầy văn phòng phẩm xuất **10 dòng** mặt hàng có cột `sku,name,price_vnd`, mỗi dòng là một sản phẩm và giá đồng/món. Nhân viên cần tra tên sản phẩm P08 và đếm số dòng dữ liệu, không coi hàng tiêu đề như một món hàng.

**Vì sao chọn cách này?** `csv.DictReader` hiểu tên cột, ít nhầm vị trí cột hơn chia chuỗi thủ công; `StringIO` giả lập một file CSV để chạy ví dụ mà không đòi máy học viên có dữ liệu bên ngoài.

**Quy trình:**
1. Tạo văn bản CSV gồm header và 10 hàng.
2. Đọc từng hàng qua `DictReader` thành list Dictionary.
3. Tra P08 và in số bản ghi.

```python
import csv
from io import StringIO
csv_text = """sku,name,price_vnd
P01,Bút,12000
P02,Vở,18000
P03,Thước,10000
P04,Tẩy,7000
P05,Giấy,25000
P06,Sổ,35000
P07,Bìa,9000
P08,Bút màu,42000
P09,Kẹp,8000
P10,Hộp,30000
"""
rows = list(csv.DictReader(StringIO(csv_text)))
match = None
for row in rows:
    if row["sku"] == "P08":
        match = row
        break
if match is None:
    raise ValueError("Không tìm thấy sản phẩm P08.")
if len(rows) != 10:
    raise ValueError("Cần đủ 10 sản phẩm CSV.")
print("Sản phẩm:", len(rows))
print("P08:", match["name"])
print("Giá P08 (đồng):", match["price_vnd"])
```

**Kết quả khi chạy:**

```text
Sản phẩm: 10
P08: Bút màu
Giá P08 (đồng): 42000
```

Giá trong CSV được đọc thành chuỗi; nếu cần tính tiền thì phải chuyển kiểu. Hàng `sku,name,price_vnd` là tiêu đề chứ không phải bản ghi thứ 11.

### Tình huống 2 — Cấp 2: Ghi 12 bước nhật ký Unicode trong thư mục tạm

**Từ vựng trong mục:** **File I/O** — đọc/ghi file; **UTF-8** — mã hóa văn bản; **Context manager** — quản lý tài nguyên.

**Tình huống thực tế:** Một chương trình quản lý lớp ghi **12 sự kiện vận hành** bằng tiếng Việt, mỗi hàng là một dòng nhật ký. Giáo viên cần xác minh các dấu tiếng Việt không hỏng sau khi ghi và đọc lại, đồng thời không để file mẫu trong thư mục làm việc.

**Vì sao chọn cách này?** `TemporaryDirectory` tạo nơi thử nghiệm tự xóa; `Path.write_text`/`read_text` kèm UTF-8 bảo đảm văn bản được ghi/đọc nhất quán. `with` giải phóng tài nguyên sau khi dùng.

**Quy trình:**
1. Tạo 12 chuỗi sự kiện và ghép bằng ký tự xuống dòng.
2. Ghi nhật ký UTF-8 trong thư mục tạm, sau đó đọc lại.
3. So sánh nội dung và đếm dòng để bảo đảm không mất dữ liệu.

```python
from pathlib import Path
from tempfile import TemporaryDirectory
events = ["Khởi động","Đọc tập tin","Kết nối nội bộ","Tải dữ liệu","Kiểm kiểu","Chuẩn hóa","Lưu nháp","Chạy báo cáo","Xác nhận","Ghi nhận","Sao lưu","Kết thúc"]
with TemporaryDirectory() as temp:
    path = Path(temp) / "log.txt"
    path.write_text("\n".join(events) + "\n", encoding="utf-8")
    readback = path.read_text(encoding="utf-8").splitlines()
    if readback != events:
        raise ValueError("Nội dung ghi và đọc lại phải trùng nhau.")
    print("Sự kiện:", len(readback))
    print("Đầu:", readback[0])
    print("Cuối:", readback[-1])
```

**Kết quả khi chạy:**

```text
Sự kiện: 12
Đầu: Khởi động
Cuối: Kết thúc
```

Chính xác 12 dòng đã được đọc lại. Kiểu dữ liệu là chuỗi, không phải thời gian thực từ hệ điều hành; đây là nhật ký giả lập.

### Tình huống 3 — Cấp 3: Bắt ValueError khi nhập 15 số lượng dạng chữ

**Từ vựng trong mục:** **try/except** — thử/bắt lỗi; **ValueError** — lỗi giá trị; **Conversion** — đổi kiểu.

**Tình huống thực tế:** Cửa hàng nhận **15 dòng số lượng điều chỉnh kho** ở dạng chuỗi, một dòng cho một mã R01…R15. Cho phép số nguyên âm để biểu diễn hàng bị trả lại/điều chỉnh giảm trong ví dụ; riêng chữ `abc`, số thập phân `12.5` và chuỗi rỗng không phải số nguyên. Cần cộng các giá trị đổi được và ghi mã nhập sai, không để một lỗi dừng toàn bộ chương trình.

**Vì sao chọn cách này?** `int()` hỗ trợ số nguyên âm và `0`, nhưng từ chối các chuỗi khác không đúng kiểu. `try/except ValueError` chỉ bắt lỗi chuyển kiểu mong đợi, không che lấp mọi loại lỗi khác.

**Quy trình:**
1. Duyệt 15 chuỗi, mỗi lượt thử chuyển bằng `int`.
2. Nếu lỗi, ghi mã dòng; nếu đúng, cộng vào tổng.
3. Xác nhận số hợp lệ cộng số lỗi bằng 15.

```python
raw_quantities = ["12","8","0","-3","15","abc","6","7","9","10","12.5","5","4","","18"]
converted, invalid = [], []
for i, raw in enumerate(raw_quantities, 1):
    try:
        converted.append(int(raw))
    except ValueError:
        invalid.append(f"R{i:02d}")
if len(raw_quantities) != 15 or len(converted) + len(invalid) != 15:
    raise ValueError("Cần kiểm tra đủ 15 dòng số lượng.")
print("Dòng nhận:", len(raw_quantities))
print("Hợp lệ:", len(converted))
print("Tổng điều chỉnh:", sum(converted))
print("Cần sửa:", ", ".join(invalid))
```

**Kết quả khi chạy:**

```text
Dòng nhận: 15
Hợp lệ: 12
Tổng điều chỉnh: 91
Cần sửa: R06, R11, R14
```

Giá trị -3 được chấp nhận vì bài toán cho phép điều chỉnh âm; với số lượng hàng tồn kho thực tế có thể cần quy tắc chặn âm riêng. Không nhầm `0` với dữ liệu thiếu.

### Tình huống 4 — Cấp 4: Đọc 18 đơn giá, bỏ dòng lỗi và xuất CSV sạch

**Từ vựng trong mục:** **DictWriter** — ghi CSV theo cột; **Schema** — cấu trúc cột; **Validation** — kiểm tra.

**Tình huống thực tế:** Một hệ thống nhận **18 dòng giá** P01…P18 qua CSV, đơn vị đồng/món; P06 ghi `bad` và P12 bỏ trống. Bộ phận kế toán cần tạo báo cáo CSV mới chỉ chứa dòng giá hợp lệ, đếm số dòng đã loại và tính tổng đơn giá; không được tự thay giá lỗi thành 0.

**Vì sao chọn cách này?** `DictReader` giữ mã và cột giá trong mỗi hàng; sau khi kiểm tra `isdigit()`, `DictWriter` tạo bảng sạch có header theo tên cột thống nhất. Dùng `StringIO` để không phụ thuộc tập tin bên ngoài.

**Quy trình:**
1. Đọc 18 hàng CSV và kiểm tra chuỗi giá chỉ gồm chữ số.
2. Dòng hợp lệ được chuyển sang `int` rồi đưa vào danh sách mới; dòng lỗi ghi mã.
3. Dùng `DictWriter` xuất dữ liệu sạch và đọc lại để đếm.

```python
import csv
from io import StringIO
raw_prices = ["10000","11000","12000","13000","14000","bad","16000","17000","18000","19000","20000","","22000","23000","24000","25000","26000","27000"]
source = StringIO()
writer = csv.DictWriter(source, fieldnames=["sku", "price_vnd"], lineterminator="\n")
writer.writeheader()
for i, price in enumerate(raw_prices, 1):
    writer.writerow({"sku": f"P{i:02d}", "price_vnd": price})
source.seek(0)
cleaned, errors = [], []
for row in csv.DictReader(source):
    if row["price_vnd"].isdigit():
        cleaned.append({"sku": row["sku"], "price_vnd": int(row["price_vnd"])})
    else:
        errors.append(row["sku"])
output = StringIO()
writer = csv.DictWriter(output, fieldnames=["sku", "price_vnd"], lineterminator="\n")
writer.writeheader()
writer.writerows(cleaned)
output.seek(0)
written = list(csv.DictReader(output))
if len(raw_prices) != 18 or len(cleaned) + len(errors) != 18:
    raise ValueError("Cần đối chiếu đủ 18 dòng CSV.")
print("Dòng đầu vào:", len(raw_prices))
print("Dòng CSV sạch:", len(written))
print("Cần sửa:", ", ".join(errors))
total_price = 0
for row in cleaned:
    total_price += row["price_vnd"]
print("Tổng đơn giá (đồng):", total_price)
```

**Kết quả khi chạy:**

```text
Dòng đầu vào: 18
Dòng CSV sạch: 16
Cần sửa: P06, P12
Tổng đơn giá (đồng): 297000
```

Đây là **tổng các đơn giá** của mẫu để kiểm tra chuyển kiểu, không phải doanh thu: doanh thu cần số lượng bán tương ứng.

### Tình huống 5 — Cấp 5: Pipeline đọc 20 giao dịch, phát hiện giá sai và ID trùng

**Từ vựng trong mục:** **CSV pipeline** — quy trình CSV; **Exception** — ngoại lệ; **Atomic report** — báo cáo một lần ghi.

**Tình huống thực tế:** Phòng kế toán cần xử lý **20 hàng** giao dịch, mỗi hàng gồm mã đơn và số tiền (đồng) trong một file CSV tạm. Một dòng có giá `bad`, một dòng trống giá, một dòng lặp mã O05 dù giá hợp lệ. Muốn tạo báo cáo CSV **chỉ gồm mã duy nhất và giá hợp lệ**, ghi lỗi theo số dòng và đối chiếu số tiền; không sửa CSV nguồn.

**Vì sao chọn cách này?** Đọc file qua `with open(..., encoding='utf-8', newline='')`, kiểm tra giá trước khi cộng và từ chối mã trùng để tránh nhân đôi doanh thu. File đầu ra tách khỏi đầu vào, ghi xong đọc lại để đối chiếu; thư mục tạm bảo đảm ví dụ độc lập.

**Quy trình:**
1. Tạo file CSV với đủ 20 dòng và header trong thư mục tạm.
2. Đọc từng hàng: kiểm tra mã trùng, giá đúng kiểu; ghi lỗi theo vị trí.
3. Ghi file sạch bằng `DictWriter`, đọc lại kiểm tra số dòng và tổng doanh thu.

```python
import csv
from pathlib import Path
from tempfile import TemporaryDirectory
rows = [{"order_id":"O01","amount_vnd":"20000"},{"order_id":"O02","amount_vnd":"30000"},{"order_id":"O03","amount_vnd":"40000"},{"order_id":"O04","amount_vnd":"50000"},{"order_id":"O05","amount_vnd":"60000"},{"order_id":"O06","amount_vnd":"20000"},{"order_id":"O07","amount_vnd":"30000"},{"order_id":"O08","amount_vnd":"bad"},{"order_id":"O09","amount_vnd":"50000"},{"order_id":"O10","amount_vnd":"60000"},{"order_id":"O11","amount_vnd":"20000"},{"order_id":"O12","amount_vnd":"30000"},{"order_id":"O05","amount_vnd":"40000"},{"order_id":"O14","amount_vnd":"50000"},{"order_id":"O15","amount_vnd":"60000"},{"order_id":"O16","amount_vnd":"20000"},{"order_id":"O17","amount_vnd":""},{"order_id":"O18","amount_vnd":"40000"},{"order_id":"O19","amount_vnd":"50000"},{"order_id":"O20","amount_vnd":"60000"}]
with TemporaryDirectory() as folder:
    incoming = Path(folder) / "incoming.csv"
    cleaned = Path(folder) / "validated.csv"
    with incoming.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["order_id", "amount_vnd"])
        writer.writeheader()
        writer.writerows(rows)
    seen, valid, errors = set(), [], []
    with incoming.open("r", encoding="utf-8", newline="") as f:
        for line_number, row in enumerate(csv.DictReader(f), 1):
            key = row["order_id"]
            if key in seen:
                errors.append(f"D{line_number:02d}:trùng")
            elif not row["amount_vnd"].isdigit():
                errors.append(f"D{line_number:02d}:giá")
            else:
                seen.add(key)
                valid.append(row)
    with cleaned.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["order_id", "amount_vnd"])
        writer.writeheader()
        writer.writerows(valid)
    with cleaned.open("r", encoding="utf-8", newline="") as f:
        exported = list(csv.DictReader(f))
    if len(rows) != 20 or len(exported) + len(errors) != 20:
        raise ValueError("Cần đối chiếu đủ 20 dòng hóa đơn.")
    print("Đầu vào:", len(rows))
    print("Đã xuất:", len(exported))
    print("Lỗi:", ", ".join(errors))
    total_amount = 0
    for row in exported:
        total_amount += int(row["amount_vnd"])
    print("Tổng tiền (đồng):", total_amount)
```

**Kết quả khi chạy:**

```text
Đầu vào: 20
Đã xuất: 17
Lỗi: D08:giá, D13:trùng, D17:giá
Tổng tiền (đồng): 690000
```

Mỗi mã chỉ được ghi một lần trong báo cáo; hàng lỗi được lưu để xử lý lại, không biến mất âm thầm. Ví dụ dùng file tạm để an toàn và không thao tác trên hồ sơ thật.

## 6. Sai lầm thường gặp

- Khi đọc CSV bằng `DictReader`, dữ liệu **mặc định là chuỗi**; muốn cộng tiền cần chuyển kiểu số hợp lệ.
- Không nhầm **hàng tiêu đề CSV** với hàng dữ liệu đầu tiên. `rows[0]` là sản phẩm đầu trong ví dụ, không phải dòng `name,price`.
- Dùng `encoding='utf-8'` với dữ liệu tiếng Việt để tránh lỗi hiển thị do mã hóa.
- Nên dùng `with` khi làm việc với file để đóng tài nguyên ngay cả khi có ngoại lệ.
- Chỉ bắt lỗi dự kiến như `ValueError` hay `FileNotFoundError`; `except:` chung chung có thể che lỗi lập trình.
- `print(text)` sẽ tự thêm ký tự xuống dòng; nếu `text` đã kết thúc bằng `\n`, màn hình có thể thêm một dòng trống.

## 7. Trắc nghiệm

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What does File I/O mean? | File I/O có nghĩa gì?**

A. Reading data from or writing data to files | Đọc dữ liệu từ hoặc ghi dữ liệu vào tệp

B. Drawing a plot | Vẽ một biểu đồ

C. Sorting a list in memory | Sắp xếp List trong bộ nhớ

D. Training a model | Huấn luyện mô hình

**Đáp án: A**

**Giải thích:** Nhập/xuất tệp là đọc dữ liệu từ tệp đã lưu hoặc ghi dữ liệu vào tệp. Ví dụ đọc CSV cung cấp các hàng đầu vào, còn lưu báo cáo tạo đầu ra tệp; chỉ sắp xếp trong bộ nhớ chưa phải thao tác I/O tệp.


**Q2. What is the purpose of a file path? | Đường dẫn file dùng để làm gì?**

A. Compute a matrix rank | Tính hạng ma trận

B. Sort rows automatically | Tự sắp xếp các hàng

C. Store a Boolean value | Lưu giá trị Boolean

D. Identify a file location | Xác định vị trí một tệp

**Đáp án: D**

**Giải thích:** Đường dẫn chỉ vị trí tệp hay thư mục, ví dụ `data/scores.csv`. Đường dẫn tương đối được hiểu theo thư mục làm việc, còn đường dẫn tuyệt đối xác định vị trí tính từ gốc hệ thống tệp.


**Q3. What does `Path.read_text()` do? | `Path.read_text()` làm gì?**

A. Convert the path into a function | Chuyển đường dẫn thành hàm

B. Sort CSV by price | Sắp CSV theo giá

C. Read text content from a file | Đọc nội dung văn bản từ tệp

D. Create a pandas index | Tạo chỉ số Pandas

**Đáp án: C**

**Giải thích:** `Path.read_text(encoding='utf-8')` đọc tệp văn bản và trả nội dung dưới dạng chuỗi Python. Nó không tự phân tách cột CSV hay biến đường dẫn thành hàm; giải mã có thể lỗi nếu chọn sai encoding.


**Q4. What does `Path.write_text()` do? | `Path.write_text()` dùng để làm gì?**

A. Read and sort all CSV rows | Đọc và sắp mọi hàng CSV

B. Only check whether a file exists | Chỉ kiểm tra tệp tồn tại

C. Count class methods | Đếm phương thức lớp

D. Write text to a file | Ghi văn bản vào tệp

**Đáp án: D**

**Giải thích:** `Path.write_text(text, encoding='utf-8')` ghi chuỗi vào tệp và thông thường thay nội dung trước đó. Muốn nối thêm, cần chế độ mở tệp phù hợp như `'a'`; `write_text` không phải thao tác chỉ kiểm tra tệp tồn tại.


**Q5. Why specify `encoding='utf-8'` for text? | Vì sao dùng `encoding='utf-8'` với văn bản?**

A. To encode and decode Unicode text consistently | Để mã hóa và giải mã chữ Unicode nhất quán

B. To guarantee a file is secret | Để bảo đảm tệp bí mật

C. To make all values integers | Để mọi giá trị thành số nguyên

D. To create three CSV columns | Để tạo ba cột CSV

**Đáp án: A**

**Giải thích:** UTF-8 quy định cách mã hóa ký tự Unicode thành byte khi ghi và giải mã byte thành ký tự khi đọc. Chỉ rõ UTF-8 nhất quán giúp giữ đúng chữ `Tiếng Việt`; nó không mã hóa bảo mật hoặc bảo đảm tệp bí mật.


**Q6. How does a CSV file normally organize data? | CSV thông thường tổ chức dữ liệu ra sao?**

A. Rows of text with separated fields | Các dòng văn bản chứa trường dữ liệu được phân cách

B. Binary images with pixels | Ảnh nhị phân gồm điểm ảnh

C. A database server connection | Kết nối máy chủ cơ sở dữ liệu

D. Python classes only | Chỉ chứa lớp Python

**Đáp án: A**

**Giải thích:** CSV lưu dữ liệu dạng bảng bằng các bản ghi có trường phân cách, thường có hàng đầu ghi tên cột. Mỗi hàng dữ liệu là một bản ghi, mỗi cột là một trường; văn bản trong dấu nháy có thể chứa dấu phẩy mà không tạo cột mới.


**Q7. What does `csv.DictReader` use as dictionary keys? | `csv.DictReader` dùng gì làm khóa Dictionary?**

A. CSV column names | Tên cột trong CSV

B. Names of Python packages | Tên gói Python

C. The current file size | Kích thước tệp hiện tại

D. Always numbers 0, 1, 2 | Luôn là số 0, 1, 2

**Đáp án: A**

**Giải thích:** Mặc định `csv.DictReader` lấy tên trường ở hàng CSV đầu tiên làm khóa từ điển. Với tiêu đề `name,age`, các hàng sau có khóa `'name'` và `'age'`; truyền `fieldnames=` tường minh sẽ thay cách lấy tiêu đề mặc định.


**Q8. For a well-formed CSV row with all fields present, what type does `csv.DictReader` return for field values by default? | Với hàng CSV đủ các trường đúng cấu trúc, mặc định `csv.DictReader` trả giá trị ô thuộc kiểu gì?**

A. String | Chuỗi

B. Float | Số thực

C. Integer | Số nguyên

D. Boolean | Giá trị logic

**Đáp án: A**

**Giải thích:** Với hàng CSV đúng cấu trúc, `csv.DictReader` trả dữ liệu ô dưới dạng chuỗi, nên ô `12` thành `'12'` chứ không phải số nguyên `12`. Cột bị thiếu có thể tạo `None` theo mặc định; muốn tính toán số vẫn phải đổi kiểu rõ ràng.


**Q9. What does `csv.DictWriter.writeheader()` write? | `csv.DictWriter.writeheader()` ghi gì?**

A. A Python class definition | Định nghĩa lớp Python

B. The column-name header row | Hàng tiêu đề chứa tên các cột

C. An exception message | Thông báo ngoại lệ

D. The final record twice | Nhân đôi bản ghi cuối

**Đáp án: B**

**Giải thích:** `csv.DictWriter.writeheader()` ghi một hàng chứa các tên trường đã cấu hình theo thứ tự. Nó không ghi toàn bộ bản ghi dữ liệu; các bản ghi cần dùng riêng `writerow()` hoặc `writerows()`.


**Q10. Why prefer the CSV module over simply splitting every line by comma? | Vì sao nên dùng module CSV thay vì luôn tách chuỗi theo dấu phẩy?**

A. It encrypts each file | Nó mã hóa bảo mật mọi tệp

B. It converts every field to a float | Nó đổi mọi trường thành số thực

C. It removes all empty rows automatically | Nó tự bỏ mọi dòng rỗng

D. It handles quoted fields and delimiters correctly | Nó xử lý đúng trường được đặt trong dấu nháy và dấu phân cách

**Đáp án: D**

**Giải thích:** Bộ đọc CSV hiểu trường có dấu nháy và quy tắc escape nên dấu phẩy trong ``"An, Binh"` vẫn thuộc một trường. Tách máy móc bằng `line.split(',')` sẽ chia sai giá trị có dấu nháy thành hai trường.


**Q11. What is an exception in Python? | Ngoại lệ trong Python là gì?**

A. A CSV row header | Hàng tiêu đề CSV

B. A guaranteed successful result | Một kết quả chắc chắn thành công

C. An error or abnormal condition raised during execution | Lỗi hoặc tình huống bất thường phát sinh khi chạy

D. A list slicing operator | Toán tử cắt List

**Đáp án: C**

**Giải thích:** Ngoại lệ báo tình huống bất thường khi chương trình chạy, như đổi kiểu thất bại hoặc thiếu tệp. Mã có thể bắt ngoại lệ dự kiến để xử lý; ngoại lệ không được bắt thường làm gián đoạn thao tác hiện tại.


**Q12. What does `int('abc')` raise? | `int('abc')` phát sinh lỗi gì?**

A. No error; returns zero | Không lỗi và trả về 0

B. `ValueError` | `ValueError`

C. `FileNotFoundError` | `FileNotFoundError`

D. `ZeroDivisionError` | `ZeroDivisionError`

**Đáp án: B**

**Giải thích:** `int('abc')` phát sinh `ValueError` vì các ký tự không biểu diễn số nguyên thập phân hợp lệ. Hàm `int` có tồn tại và nhận chuỗi, nên đây không phải lỗi thiếu tệp hoặc chia cho không.


**Q13. Which exceptions does `except ValueError:` handle? | `except ValueError:` xử lý những ngoại lệ nào?**

A. Every possible error | Mọi lỗi có thể xảy ra

B. `ValueError` exceptions, including invalid conversions | Ngoại lệ `ValueError`, kể cả lỗi đổi kiểu không hợp lệ

C. Only successful conversions | Chỉ khi chuyển kiểu thành công

D. All file permission failures | Mọi lỗi quyền truy cập tệp

**Đáp án: B**

**Giải thích:** `except ValueError:` bắt ngoại lệ kiểu `ValueError` và các kiểu con, trong đó có lỗi đổi số như `int('abc')`. Nó không bắt `FileNotFoundError` không liên quan hay mọi lỗi khác; vì vậy cần chọn nhánh bắt phù hợp với rủi ro của mã.


**Q14. Which exception commonly indicates a missing file? | Ngoại lệ nào thường báo tệp không tồn tại?**

A. `TypeError` always | Luôn `TypeError`

B. `ValueError` only | Chỉ `ValueError`

C. `KeyError` only | Chỉ `KeyError`

D. `FileNotFoundError` | `FileNotFoundError`

**Đáp án: D**

**Giải thích:** Mở một đường dẫn không tồn tại để đọc thường gây `FileNotFoundError`. Lỗi này khác `PermissionError`, khi tệp có thể tồn tại nhưng quyền truy cập bị từ chối; hai trường hợp cần cách xử lý khác nhau.


**Q15. What does a `with` block provide for a file? | Khối `with` hỗ trợ việc gì khi dùng file?**

A. Automatic numeric conversion | Tự chuyển toàn bộ số

B. Automatic sorting | Tự sắp xếp

C. Automatic resource cleanup on exit | Tự dọn dẹp và đóng tài nguyên khi ra khỏi khối

D. Automatic internet download | Tự tải từ Internet

**Đáp án: C**

**Giải thích:** Trình quản lý ngữ cảnh tệp như `with open(path) as f:` đóng tệp khi thoát khỏi khối, kể cả khi có ngoại lệ. Nó quản lý dọn dẹp tài nguyên, không tự sắp xếp dữ liệu hoặc đổi các ô thành số.


**Q16. What is `StringIO` useful for? | `StringIO` hữu ích cho việc gì?**

A. Reading only images | Chỉ đọc ảnh

B. Operating a camera sensor | Điều khiển cảm biến camera

C. File-like text operations in memory | Đọc ghi văn bản như file ngay trong bộ nhớ

D. Turning a set into a tuple | Biến Set thành Tuple

**Đáp án: C**

**Giải thích:** `io.StringIO` cung cấp luồng văn bản trong bộ nhớ với thao tác tương tự tệp như `read()` và `write()`. Nó hữu ích khi thử bộ đọc CSV với chuỗi mẫu nhỏ mà không phải tạo tệp vật lý.


**Q17. What is the difference between `write` mode and append mode? | Chế độ ghi `w` và nối thêm `a` khác nhau thế nào?**

A. Both only read existing content | Cả hai chỉ đọc nội dung

B. `w` replaces contents; `a` adds to the end | `w` thay nội dung; `a` nối thêm cuối tệp

C. `a` always deletes files | `a` luôn xóa tệp

D. `w` only opens network sockets | `w` chỉ mở socket mạng

**Đáp án: B**

**Giải thích:** Mở tệp có sẵn bằng chế độ `'w'` sẽ xóa nội dung cũ trước khi ghi, còn `'a'` nối dữ liệu mới vào cuối. Ví dụ tệp đang chứa `A`, ghi `B` bằng `'w'` được `B`, còn bằng `'a'` được `AB`.


**Q18. Why is a bare `except:` often a poor choice? | Vì sao thường không nên dùng `except:` không chỉ rõ lỗi?**

A. It prevents file creation | Nó ngăn tạo file

B. It never catches any error | Nó không bắt được lỗi nào

C. It can hide unexpected programming errors | Nó có thể che các lỗi lập trình không lường trước

D. It converts errors into CSV | Nó chuyển lỗi thành CSV

**Đáp án: C**

**Giải thích:** `except:` không ghi loại sẽ bắt phạm vi ngoại lệ quá rộng, kể cả các tín hiệu ngắt thường nên được chuyển tiếp. Nên dùng `except ValueError:` hoặc loại lỗi cụ thể để những bug không dự kiến vẫn lộ ra.


**Q19. What does `print(text, end='')` change? | `print(text, end='')` thay đổi điều gì?**

A. It closes every open file | Nó đóng mọi file đang mở

B. It removes existing newlines from text | Nó xóa mọi dấu xuống dòng có sẵn trong text

C. It converts text to numbers | Nó chuyển chữ thành số

D. It avoids adding the default newline | Nó không tự thêm dấu xuống dòng mặc định

**Đáp án: D**

**Giải thích:** Tham số `end` quy định chuỗi mà `print()` thêm vào sau các đối số; mặc định là xuống dòng `\n`. Với `end=''`, `print('A', end='')` không thêm dòng mới, nhưng cũng không xóa ký tự xuống dòng vốn có trong chuỗi.


**Q20. Which distinction between `csv.reader` and `csv.DictReader` is correct? | `csv.reader` khác `csv.DictReader` ở điểm nào?**

A. reader always validates all values | reader luôn kiểm tra mọi giá trị

B. reader yields field lists; DictReader uses column keys | reader trả danh sách trường; DictReader dùng khóa theo tên cột

C. Both always return float arrays | Cả hai luôn trả mảng số thực

D. DictReader writes files but cannot read | DictReader chỉ ghi mà không đọc

**Đáp án: B**

**Giải thích:** `csv.reader` trả mỗi bản ghi thành List chuỗi trường, ví dụ `['An', '9']`. `csv.DictReader` gắn trường với tên cột như `{'name': 'An', 'score': '9'}`, giúp tra theo tên thay vì chỉ số vị trí.

## 8. Nối sang bài tiếp theo

`Dictionary → File/CSV → DataFrame → Dataset AI`.
