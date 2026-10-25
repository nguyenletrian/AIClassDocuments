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

**No Note — Không chú thích**

```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    file_path = Path(folder) / 'log.txt'
    file_path.write_text('Started', encoding='utf-8')
    print(file_path.read_text(encoding='utf-8'))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Viết và đọc lại văn bản UTF-8 trong thư mục tạm, tự dọn sau khi dùng.
# Dữ liệu: Path tạo đường dẫn hệ điều hành; TemporaryDirectory() tạo thư mục tạm và xóa khi ra khỏi with.
# Path biểu diễn đường dẫn file dễ ghép bằng toán tử /.
from pathlib import Path
# TemporaryDirectory() tạo thư mục tạm, tự xóa sau khối with.
from tempfile import TemporaryDirectory

# with nhận đường dẫn tạm qua as folder và bảo đảm thư mục được dọn khi kết thúc.
with TemporaryDirectory() as folder:
    # Path(folder) / 'log.txt' ghép đường dẫn thư mục với tên file độc lập hệ điều hành.
    file_path = Path(folder) / 'log.txt'
    # write_text() tạo/ghi file; encoding='utf-8' giữ tiếng Việt và ký tự Unicode.
    file_path.write_text('Started', encoding='utf-8')
    # read_text(encoding='utf-8') đọc lại toàn bộ file thành chuỗi.
    # print() xuất nội dung vừa đọc để kiểm chứng ghi/đọc.
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

**No Note — Không chú thích**

```python
import csv
from io import StringIO

csv_text = 'name,price\nPen,10\nBook,35\n'
rows = list(csv.DictReader(StringIO(csv_text)))
print(rows[1]['name'], rows[1]['price'])
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Đọc dữ liệu CSV ở bộ nhớ thành các hàng dictionary theo tên cột.
# Dữ liệu: Chuỗi csv_text gồm tiêu đề name,price và hai hàng Pen/Book; CSV là văn bản phân cột bằng dấu phẩy.
# csv là thư viện chuẩn đọc/ghi bảng phân cách dấu phẩy.
import csv
# StringIO tạo file văn bản giả trong RAM, không tạo file thật.
from io import StringIO

# Ký tự \n trong chuỗi là xuống dòng: dòng đầu đặt tên các cột.
csv_text = 'name,price\nPen,10\nBook,35\n'
# DictReader đọc mỗi hàng thành dictionary, khóa lấy từ tiêu đề cột; list() thu toàn bộ hàng.
rows = list(csv.DictReader(StringIO(csv_text)))
# [1] lấy hàng thứ hai (Book), ['name']/['price'] lấy các ô theo tên cột; giá vẫn là chuỗi.
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

**No Note — Không chú thích**

```python
try:
    number = int('abc')
    print(number)
except ValueError:
    print('Invalid integer')
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Bắt ValueError khi chuyển một chuỗi không phải số thành int.
# Dữ liệu: Chuỗi abc không thể chuyển sang số nguyên; cần xử lý lỗi có kiểm soát.
# try chứa lệnh có thể thất bại, luồng chuyển sang except nếu gặp lỗi.
try:
    # int() yêu cầu chuỗi có biểu diễn số nguyên; 'abc' gây ValueError.
    number = int('abc')
    print(number)
# Bắt riêng ValueError để hiện thông báo mà không làm chương trình dừng bất ngờ.
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

**No Note — Không chú thích**

```python
from io import StringIO

with StringIO('abc') as stream:
    print(stream.read())

print(stream.closed)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Dùng with quản lý StringIO và kiểm tra luồng đã đóng.
# Dữ liệu: StringIO là luồng văn bản nằm trong RAM; with sẽ đóng luồng khi thoát.
# StringIO cung cấp luồng văn bản trong bộ nhớ.
from io import StringIO

# with gọi cơ chế đóng luồng khi ra khỏi khối, ngay cả khi có lỗi.
with StringIO('abc') as stream:
    # read() đọc hết nội dung còn lại từ con trỏ của luồng.
    print(stream.read())

# Thuộc tính closed là True sau khi with đóng tài nguyên.
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

**Tình huống thực tế:** Quầy văn phòng phẩm nhận bảng hàng xuất từ phần mềm dưới dạng **CSV**, tức văn bản có các cột ngăn bằng dấu phẩy. Trong ví dụ có **10 sản phẩm P01–P10**, mỗi dòng chứa mã `sku`, tên `name` và giá một món `price_vnd` tính bằng **đồng**. Nhân viên cần tìm tên và giá của P08 và xác nhận bảng có đúng 10 sản phẩm, không đếm dòng tiêu đề là hàng bán.

**Vì sao chọn cách này?** `csv.DictReader` đọc mỗi dòng CSV thành một **dictionary** lấy tên cột làm khóa, nên có thể hỏi `row['sku']` hoặc `row['name']` thay vì phải nhớ mã ở cột số mấy. Dòng `sku,name,price_vnd` được hiểu là **tiêu đề cột**, không phải một sản phẩm. `StringIO` tạo đối tượng giống file ngay trong bộ nhớ từ văn bản CSV mẫu, để ví dụ chạy mà không cần chuẩn bị tệp bên ngoài. Chương trình duyệt các dòng cho tới khi tìm thấy `P08`, đọc tên và giá của dòng đó, rồi đối chiếu số sản phẩm là 10.

**Quy trình:**
1. Tạo văn bản CSV gồm header và 10 hàng.
2. Đọc từng hàng qua `DictReader` thành list Dictionary.
3. Tra P08 và in số bản ghi.

**No Note — Không chú thích**

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

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Đọc CSV 10 sản phẩm, tìm hàng có mã P08 và in đơn giá.
# Dữ liệu: CSV gồm 10 hàng sku/name/price_vnd, mỗi hàng là một sản phẩm và giá đồng dạng chuỗi.
# csv xử lý bảng text, không tự đổi giá trong cột thành số.
import csv
# StringIO biến chuỗi CSV thành luồng có thể đọc.
from io import StringIO
# Nội dung nhiều dòng gồm tiêu đề sku,name,price_vnd và 10 sản phẩm; giá đơn vị đồng dạng text.
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
# DictReader trả từng hàng dict dùng tên cột làm khóa; list() giữ 10 hàng.
rows = list(csv.DictReader(StringIO(csv_text)))
match = None
# Duyệt từng hàng CSV để tìm theo mã SKU.
for row in rows:
    # Tra khóa sku của hàng; == so chính xác với mã P08.
    if row["sku"] == "P08":
        match = row
        # break dừng tìm ngay khi gặp SKU mong muốn.
        break
# is None cho biết chưa tìm được mã, thay vì giả định tồn tại.
if match is None:
    # ValueError báo dữ liệu không hợp lệ và dừng khi kiểm tra thất bại.
    raise ValueError("Không tìm thấy sản phẩm P08.")
# len() đếm bản ghi để đối chiếu số lượng kỳ vọng.
if len(rows) != 10:
    # ValueError báo dữ liệu không hợp lệ và dừng khi kiểm tra thất bại.
    raise ValueError("Cần đủ 10 sản phẩm CSV.")
# len() đếm bản ghi để đối chiếu số lượng kỳ vọng.
print("Sản phẩm:", len(rows))
print("P08:", match["name"])
# Giá được đọc dưới dạng chuỗi từ CSV; in như số nhưng chưa dùng int().
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

**Tình huống thực tế:** Giáo viên muốn kiểm tra việc lưu văn bản tiếng Việt có dấu. Một chương trình tạo **12 dòng nhật ký** mô phỏng các bước như `Khởi động`, `Đọc tập tin` và `Kết thúc`, mỗi dòng là một sự kiện. Bài cần ghi các dòng vào tệp tạm, đọc lại để xem dấu tiếng Việt có nguyên vẹn không, rồi cho biết số sự kiện và nội dung dòng đầu, dòng cuối mà không để tệp mẫu tồn tại lâu trên máy.

**Vì sao chọn cách này?** Mã hóa **UTF-8** là cách lưu chữ dưới dạng byte mà vẫn hỗ trợ ký tự tiếng Việt như ă, ê, ơ và dấu thanh. Khi `write_text(..., encoding='utf-8')` ghi nhật ký thì `read_text()` cũng phải dùng UTF-8 để đọc lại nhất quán, tránh chữ bị sai. `TemporaryDirectory()` tạo một **thư mục dùng thử**, rồi tự dọn khi thoát khối `with`, nên máy học viên không bị giữ lại tệp `log.txt`. Chương trình so từng dòng đọc lại với 12 sự kiện ban đầu: không chỉ đếm dòng mà còn xác nhận nội dung không bị thay đổi.

**Quy trình:**
1. Tạo 12 chuỗi sự kiện và ghép bằng ký tự xuống dòng.
2. Ghi nhật ký UTF-8 trong thư mục tạm, sau đó đọc lại.
3. So sánh nội dung và đếm dòng để bảo đảm không mất dữ liệu.

**No Note — Không chú thích**

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

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Ghi rồi đọc lại 12 sự kiện log trong thư mục tạm bằng UTF-8.
# Dữ liệu: 12 chuỗi sự kiện từ khởi động đến kết thúc, mỗi sự kiện ghi thành một dòng log.
# Path ghép đường dẫn tệp theo cách phù hợp hệ điều hành.
from pathlib import Path
# Thư mục tạm tránh ghi tệp vào vị trí người dùng thật.
from tempfile import TemporaryDirectory
events = ["Khởi động","Đọc tập tin","Kết nối nội bộ","Tải dữ liệu","Kiểm kiểu","Chuẩn hóa","Lưu nháp","Chạy báo cáo","Xác nhận","Ghi nhận","Sao lưu","Kết thúc"]
# with tự dọn file và thư mục khi kết thúc khối.
with TemporaryDirectory() as temp:
    # Ghép đường dẫn tạm với log.txt bằng / của Path.
    path = Path(temp) / "log.txt"
    # join(events) ghép các sự kiện bằng xuống dòng; + '\n' thêm kết thúc dòng cuối.
    # write_text(encoding='utf-8') ghi chuỗi Unicode vào file.
    path.write_text("\n".join(events) + "\n", encoding="utf-8")
    # read_text() trả chuỗi; splitlines() tách thành list dòng, bỏ dấu kết thúc dòng.
    readback = path.read_text(encoding="utf-8").splitlines()
    # So từng dòng đã đọc với list gốc; != báo lỗi khi dữ liệu bị sai.
    if readback != events:
        # ValueError báo dữ liệu không hợp lệ và dừng khi kiểm tra thất bại.
        raise ValueError("Nội dung ghi và đọc lại phải trùng nhau.")
    # len() đếm bản ghi để đối chiếu số lượng kỳ vọng.
    print("Sự kiện:", len(readback))
    # [0] là sự kiện đầu, [-1] là sự kiện cuối.
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

**Tình huống thực tế:** Nhân viên kho nhận **15 ô nhập số lượng điều chỉnh** cho các mã R01–R15; dữ liệu từ biểu mẫu đều là **chuỗi** như `"12"`, `"-3"` hoặc `"0"`. Đây là chênh lệch điều chỉnh nên có thể có giá trị âm hoặc bằng 0. Một số ô lại chứa `abc`, `12.5` hoặc để trống. Người quản lý muốn cộng các số nguyên đổi được, đếm lượt hợp lệ và liệt kê mã cần nhập lại mà không để một ô sai làm dừng toàn bộ báo cáo.

**Vì sao chọn cách này?** `int()` đổi một chuỗi chứa **số nguyên** thành số để tính toán, nên nhận `"12"`, `"0"` và `"-3"`. Nhưng `abc`, `12.5` và chuỗi rỗng không có dạng số nguyên hợp lệ nên `int()` báo `ValueError`. `try` cho phép thử chuyển kiểu trên từng dòng, còn `except ValueError` ghi lại mã lỗi rồi tiếp tục xử lý các dòng sau. Chỉ bắt loại lỗi **được dự đoán từ đầu vào** này, không dùng một lệnh bắt mọi lỗi khiến các vấn đề lập trình khác bị che giấu. Cuối cùng tổng điều chỉnh được tính từ các dòng đổi thành công.

**Quy trình:**
1. Duyệt 15 chuỗi, mỗi lượt thử chuyển bằng `int`.
2. Nếu lỗi, ghi mã dòng; nếu đúng, cộng vào tổng.
3. Xác nhận số hợp lệ cộng số lỗi bằng 15.

**No Note — Không chú thích**

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

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Thử chuyển 15 chuỗi số lượng thành int và thu thập mã dòng bị lỗi.
# Dữ liệu: 15 lượng hàng dạng chuỗi; -3 là int hợp lệ nhưng âm, 12.5/abc/rỗng không chuyển int được.
raw_quantities = ["12","8","0","-3","15","abc","6","7","9","10","12.5","5","4","","18"]
converted, invalid = [], []
# enumerate(...,1) gắn dòng R01..R15 với từng chuỗi đầu vào.
for i, raw in enumerate(raw_quantities, 1):
    # try bắt đầu thử chuyển chuỗi thành số nguyên.
    try:
        # int() chấp nhận số nguyên có dấu như -3, nhưng không nhận '12.5', 'abc' hay chuỗi rỗng.
        converted.append(int(raw))
    # Bắt đúng lỗi chuyển đổi mà không làm mất các dòng hợp lệ.
    except ValueError:
        # append() lưu mã dòng lỗi; f-string :02d luôn có hai chữ số.
        invalid.append(f"R{i:02d}")
# len() đếm bản ghi để đối chiếu số lượng kỳ vọng.
if len(raw_quantities) != 15 or len(converted) + len(invalid) != 15:
    # ValueError báo dữ liệu không hợp lệ và dừng khi kiểm tra thất bại.
    raise ValueError("Cần kiểm tra đủ 15 dòng số lượng.")
# len() đếm bản ghi để đối chiếu số lượng kỳ vọng.
print("Dòng nhận:", len(raw_quantities))
# len() đếm bản ghi để đối chiếu số lượng kỳ vọng.
print("Hợp lệ:", len(converted))
# sum() cộng các giá trị chuyển được, bao gồm -3 vì tiêu chí chỉ kiểm cú pháp int.
print("Tổng điều chỉnh:", sum(converted))
# join() ghép các mã bằng dấu phẩy và khoảng trắng.
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

**Tình huống thực tế:** Kế toán nhận **18 dòng giá sản phẩm P01–P18** trong bảng CSV, mỗi giá là **đồng/món** và đang được ghi dưới dạng chữ. Mã P06 có giá `bad`, mã P12 không có giá. Họ cần xuất một bảng CSV khác chỉ còn các dòng giá hợp lệ, báo số dòng bị loại và tổng các đơn giá được đọc thành công; không sửa bảng nguồn hoặc tự coi giá thiếu là 0 đồng.

**Vì sao chọn cách này?** `DictReader` đọc CSV theo tên cột để giữ đúng mã sản phẩm và chuỗi giá. `isdigit()` trong ví dụ dùng để kiểm tra giá có toàn **chữ số thập phân** hay không; chuỗi `bad` hoặc rỗng không đạt, nên đưa mã vào danh sách lỗi. Giá hợp lệ được đổi thành `int` rồi ghi sang file CSV mới bằng `DictWriter`, có dòng tiêu đề rõ ràng. `StringIO` giúp mô phỏng cả file đầu vào lẫn đầu ra trong bộ nhớ. Tính tổng từ các dòng đã được xác minh, không thay giá lỗi bằng 0 vì như vậy báo cáo sẽ thiếu doanh thu mà không cảnh báo.

**Quy trình:**
1. Đọc 18 hàng CSV và kiểm tra chuỗi giá chỉ gồm chữ số.
2. Dòng hợp lệ được chuyển sang `int` rồi đưa vào danh sách mới; dòng lỗi ghi mã.
3. Dùng `DictWriter` xuất dữ liệu sạch và đọc lại để đếm.

**No Note — Không chú thích**

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

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Làm sạch 18 giá từ CSV ở bộ nhớ, chỉ xuất dòng giá nguyên hợp lệ.
# Dữ liệu: 18 giá hàng chuỗi VND; bad và chuỗi rỗng là sai, các dòng còn lại thuộc một SKU.
# csv cung cấp DictWriter/DictReader để xuất và đọc bảng có tên cột.
import csv
# StringIO lưu CSV trong RAM, không tạo file trên ổ đĩa.
from io import StringIO
raw_prices = ["10000","11000","12000","13000","14000","bad","16000","17000","18000","19000","20000","","22000","23000","24000","25000","26000","27000"]
# Tạo luồng văn bản rỗng để ghi CSV đầu vào.
source = StringIO()
# DictWriter ghi từng dict theo thứ tự fieldnames; lineterminator='\n' cố định dấu xuống dòng.
writer = csv.DictWriter(source, fieldnames=["sku", "price_vnd"], lineterminator="\n")
# Ghi dòng đầu tên cột sku,price_vnd.
writer.writeheader()
# Đánh số giá bắt đầu từ 1 để tạo SKU P01..P18.
for i, price in enumerate(raw_prices, 1):
    # writerow() ghi một dictionary thành một dòng CSV.
    writer.writerow({"sku": f"P{i:02d}", "price_vnd": price})
# seek(0) đưa con trỏ về đầu trước khi đọc lại, nếu không sẽ không đọc được hàng.
source.seek(0)
cleaned, errors = [], []
# DictReader duyệt các hàng theo tên khóa, cột price_vnd vẫn ở dạng chuỗi.
for row in csv.DictReader(source):
    # isdigit() chỉ nhận chuỗi toàn chữ số, loại bad/rỗng; int() đổi chuỗi hợp lệ thành số.
    if row["price_vnd"].isdigit():
        # append() giữ dict đã làm sạch, bảo toàn mã SKU.
        cleaned.append({"sku": row["sku"], "price_vnd": int(row["price_vnd"])})
    else:
        # append() lưu mã có giá lỗi để báo cáo.
        errors.append(row["sku"])
# Luồng CSV đầu ra riêng với nguồn, tránh chồng ghi dữ liệu thô.
output = StringIO()
# Ghi cột đúng thứ tự như CSV nguồn; dấu dòng \n.
writer = csv.DictWriter(output, fieldnames=["sku", "price_vnd"], lineterminator="\n")
# Ghi dòng đầu tên cột sku,price_vnd.
writer.writeheader()
# writerows() ghi toàn bộ hàng hợp lệ; khác writerow() ghi một hàng.
writer.writerows(cleaned)
# Đặt lại con trỏ để kiểm thử đọc bản CSV vừa xuất.
output.seek(0)
# Đọc lại file giả đầu ra để đối chiếu số dòng.
written = list(csv.DictReader(output))
# len() đếm bản ghi để đối chiếu số lượng kỳ vọng.
if len(raw_prices) != 18 or len(cleaned) + len(errors) != 18:
    # ValueError báo dữ liệu không hợp lệ và dừng khi kiểm tra thất bại.
    raise ValueError("Cần đối chiếu đủ 18 dòng CSV.")
# len() đếm bản ghi để đối chiếu số lượng kỳ vọng.
print("Dòng đầu vào:", len(raw_prices))
# len() đếm bản ghi để đối chiếu số lượng kỳ vọng.
print("Dòng CSV sạch:", len(written))
# join() ghép các mã bằng dấu phẩy và khoảng trắng.
print("Cần sửa:", ", ".join(errors))
total_price = 0
for row in cleaned:
    # Giá trong cleaned đã là số int; += cộng đồng của mỗi SKU.
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

**Tình huống thực tế:** Phòng kế toán phải xử lý **20 dòng giao dịch CSV**. Mỗi dòng có mã đơn và tiền thanh toán tính bằng **đồng**: dòng thứ 8 ghi `bad`, dòng thứ 17 để trống số tiền, dòng thứ 13 dùng lại mã O05 của dòng thứ 5. Một dòng trùng mã có thể khiến kế toán cộng tiền hai lần. Nhân viên cần tạo file báo cáo chỉ có mã không trùng và tiền hợp lệ, đồng thời ghi rõ **số dòng và nguyên nhân lỗi**, rồi kiểm tra tổng tiền của những dòng đã xuất.

**Vì sao chọn cách này?** **Pipeline xử lý CSV** nghĩa là đi qua nhiều bước có thứ tự: ghi dữ liệu đầu vào → đọc từng dòng → kiểm tra → ghi file kết quả → đọc lại để đối chiếu. Chương trình dùng `seen` (set mã đã gặp) để từ chối mã xuất hiện lần thứ hai, trước khi cộng tiền; với dòng `bad` hoặc trống, `isdigit()` xác định tiền không hợp lệ. `enumerate(..., 1)` đánh số các **dòng dữ liệu** bắt đầu từ 1 để ghi lỗi `D08:giá`, `D13:trùng`... chính xác. `with open(..., encoding='utf-8', newline='')` giúp file được đóng sau khi dùng và đọc/ghi CSV đúng cách; `TemporaryDirectory` dọn các tệp mô phỏng. Đầu ra được đọc lại để xác nhận chỉ những dòng hợp lệ mới được cộng.

**Quy trình:**
1. Tạo file CSV với đủ 20 dòng và header trong thư mục tạm.
2. Đọc từng hàng: kiểm tra mã trùng, giá đúng kiểu; ghi lỗi theo vị trí.
3. Ghi file sạch bằng `DictWriter`, đọc lại kiểm tra số dòng và tổng doanh thu.

**No Note — Không chú thích**

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

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Kiểm tra 20 hóa đơn CSV thật trong thư mục tạm, loại mã trùng và giá lỗi.
# Dữ liệu: 20 dict hóa đơn (order_id, amount_vnd chuỗi); có một mã lặp O05, giá bad và rỗng.
# csv hỗ trợ đọc/ghi file bảng có cột tên.
import csv
# Path cung cấp đường dẫn file để kết hợp với thư mục tạm.
from pathlib import Path
# TemporaryDirectory bảo đảm không để lại incoming.csv/validated.csv sau with.
from tempfile import TemporaryDirectory
rows = [{"order_id":"O01","amount_vnd":"20000"},{"order_id":"O02","amount_vnd":"30000"},{"order_id":"O03","amount_vnd":"40000"},{"order_id":"O04","amount_vnd":"50000"},{"order_id":"O05","amount_vnd":"60000"},{"order_id":"O06","amount_vnd":"20000"},{"order_id":"O07","amount_vnd":"30000"},{"order_id":"O08","amount_vnd":"bad"},{"order_id":"O09","amount_vnd":"50000"},{"order_id":"O10","amount_vnd":"60000"},{"order_id":"O11","amount_vnd":"20000"},{"order_id":"O12","amount_vnd":"30000"},{"order_id":"O05","amount_vnd":"40000"},{"order_id":"O14","amount_vnd":"50000"},{"order_id":"O15","amount_vnd":"60000"},{"order_id":"O16","amount_vnd":"20000"},{"order_id":"O17","amount_vnd":""},{"order_id":"O18","amount_vnd":"40000"},{"order_id":"O19","amount_vnd":"50000"},{"order_id":"O20","amount_vnd":"60000"}]
# with tạo thư mục và tự xóa cả hai file khi ra khỏi khối.
with TemporaryDirectory() as folder:
    # Phép / ghép thư mục và tên file .csv.
    incoming = Path(folder) / "incoming.csv"
    # Phép / ghép thư mục và tên file .csv.
    cleaned = Path(folder) / "validated.csv"
    # open('w') ghi mới, encoding='utf-8' giữ Unicode; newline='' tránh dòng trống khi module csv tự quản xuống dòng.
    with incoming.open("w", encoding="utf-8", newline="") as f:
        # DictWriter gắn khóa dict với thứ tự cột order_id,amount_vnd.
        writer = csv.DictWriter(f, fieldnames=["order_id", "amount_vnd"])
        # Ghi tiêu đề cột trước dữ liệu.
        writer.writeheader()
        # writerows() ghi nhiều hàng dictionary qua CSV.
        writer.writerows(rows)
    # set() lưu mã đã xuất hiện, valid lưu dict hợp lệ, errors lưu nhãn lỗi.
    seen, valid, errors = set(), [], []
    # open('r') đọc lại UTF-8; newline='' để thư viện csv phân tích đúng kết thúc dòng.
    with incoming.open("r", encoding="utf-8", newline="") as f:
        # DictReader trả dict theo cột; enumerate(...,1) đánh số dòng dữ liệu bắt đầu 1 (không gồm header).
        for line_number, row in enumerate(csv.DictReader(f), 1):
            key = row["order_id"]
            # Toán tử in kiểm tra mã đã gặp; phát hiện dòng trùng.
            if key in seen:
                # append() lưu thông tin dòng hỏng; :02d in số dòng thành hai chữ số.
                errors.append(f"D{line_number:02d}:trùng")
            # isdigit() yêu cầu tất cả ký tự là chữ số; loại bad và chuỗi rỗng, chưa nhận số âm/thập phân.
            elif not row["amount_vnd"].isdigit():
                # append() lưu thông tin dòng hỏng; :02d in số dòng thành hai chữ số.
                errors.append(f"D{line_number:02d}:giá")
            else:
                # add() ghi mã của dòng hợp lệ vào set để lần sau bắt trùng.
                seen.add(key)
                # append() ghi hàng hợp lệ, giữ thứ tự gốc.
                valid.append(row)
    # Mở CSV đích để ghi các hàng đã kiểm tra.
    with cleaned.open("w", encoding="utf-8", newline="") as f:
        # DictWriter gắn khóa dict với thứ tự cột order_id,amount_vnd.
        writer = csv.DictWriter(f, fieldnames=["order_id", "amount_vnd"])
        # Ghi tiêu đề cột trước dữ liệu.
        writer.writeheader()
        # writerows() ghi nhiều hàng dictionary qua CSV.
        writer.writerows(valid)
    # Đọc file kết quả để xác minh xuất thành công.
    with cleaned.open("r", encoding="utf-8", newline="") as f:
        # list() gom các hàng CSV đã xuất để so đếm.
        exported = list(csv.DictReader(f))
    # len() đếm bản ghi để đối chiếu số lượng kỳ vọng.
    if len(rows) != 20 or len(exported) + len(errors) != 20:
        # ValueError báo dữ liệu không hợp lệ và dừng khi kiểm tra thất bại.
        raise ValueError("Cần đối chiếu đủ 20 dòng hóa đơn.")
    # len() đếm bản ghi để đối chiếu số lượng kỳ vọng.
    print("Đầu vào:", len(rows))
    # len() đếm bản ghi để đối chiếu số lượng kỳ vọng.
    print("Đã xuất:", len(exported))
    # join() ghép các mã bằng dấu phẩy và khoảng trắng.
    print("Lỗi:", ", ".join(errors))
    total_amount = 0
    for row in exported:
        # Giá CSV vốn là chuỗi; int() chuyển sang số trước khi cộng tổng đồng.
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
