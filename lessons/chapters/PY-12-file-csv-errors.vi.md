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
## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Đọc CSV sản phẩm

**Từ vựng trong mục:** **CSV** — dữ liệu CSV; **DictReader** — đọc theo tên cột.

**Tình huống thực tế:** Cửa hàng có bảng `name,price` gồm Pen giá 10 và Book giá 35 theo cùng đơn vị tiền. Hãy đọc CSV và in tên mặt hàng nằm ở **hàng dữ liệu thứ hai**.

**Vì sao chọn cách giải này?** `csv.DictReader` đọc theo tên cột và `rows[1]` lấy hàng dữ liệu thứ hai (vì chỉ số bắt đầu từ 0).

**Quy trình giải:**

1. Viết dữ liệu CSV với hàng tên cột và hai sản phẩm.
2. Đọc bằng `DictReader`, chuyển các hàng thành List.
3. Lấy `rows[1]['name']` và in ra.

```python
# Mục đích: Đọc CSV sản phẩm.
import csv
from io import StringIO

csv_text = 'name,price\nPen,10\nBook,35\n'
rows = list(csv.DictReader(StringIO(csv_text)))
print(rows[1]['name'])
```

**Kết quả khi chạy:**

```text
Book
```

`Book` thuộc hàng dữ liệu thứ hai; hàng tiêu đề không được tính là sản phẩm.

### Tình huống 2 — Lưu nhật ký ứng dụng

**Từ vựng trong mục:** **File I/O** — đọc ghi file; **UTF-8** — mã hóa văn bản.

**Tình huống thực tế:** Ứng dụng ghi trạng thái `Started` vào file nhật ký `log.txt` trong một thư mục tạm. Hãy đọc lại dòng trạng thái để xác minh đã lưu thành công.

**Vì sao chọn cách giải này?** `Path.write_text()` ghi văn bản UTF-8; `Path.read_text()` đọc lại, còn thư mục tạm bảo đảm ví dụ không để lại file.

**Quy trình giải:**

1. Tạo thư mục tạm và đường dẫn `log.txt`.
2. Ghi chữ `Started` vào file với UTF-8.
3. Đọc file và in trạng thái đã lưu.

```python
# Mục đích: Lưu nhật ký ứng dụng.
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

Nội dung đọc trùng dữ liệu đã ghi; file ví dụ được xóa khi thư mục tạm đóng.

### Tình huống 3 — Chặn dữ liệu nhập sai kiểu

**Từ vựng trong mục:** **Exception** — ngoại lệ; **ValueError** — lỗi giá trị.

**Tình huống thực tế:** Biểu mẫu chỉ nhận số nguyên nhưng khách nhập chuỗi `abc`. Hãy thử chuyển kiểu; nếu chuyển thất bại, in `None` để biểu thị chưa có số hợp lệ mà không làm chương trình dừng.

**Vì sao chọn cách giải này?** `int()` báo `ValueError` với chữ không phải số nguyên. `except ValueError` bắt lỗi này để gán `None` đúng trường hợp.

**Quy trình giải:**

1. Đặt `raw = 'abc'`.
2. Trong `try`, gọi `int(raw)` để chuyển số.
3. Nếu có `ValueError`, đặt số bằng `None`, rồi in kết quả.

```python
# Mục đích: Chặn dữ liệu nhập sai kiểu.
raw = 'abc'

try:
    number = int(raw)
except ValueError:
    number = None

print(number)
```

**Kết quả khi chạy:**

```text
None
```

`None` biểu thị chưa có giá trị số hợp lệ; nó không phải số 0.

### Tình huống 4 — Xuất báo cáo CSV

**Từ vựng trong mục:** **DictWriter** — ghi CSV theo tên cột; **Fieldnames** — tên cột.

**Tình huống thực tế:** Báo cáo bán hàng có ngày `2026-10-24` và doanh thu `1200` đơn vị tiền. Hãy tạo dữ liệu CSV có hai cột `date`, `revenue` và một dòng dữ liệu, rồi in nội dung file dạng văn bản.

**Vì sao chọn cách giải này?** `csv.DictWriter` bảo đảm giá trị được ghi đúng cột. `lineterminator='\n'` tạo dấu xuống dòng thống nhất trong ví dụ; `end=''` tránh `print()` thêm dòng trống.

**Quy trình giải:**

1. Tạo bộ đệm văn bản `StringIO`.
2. Định nghĩa tên hai cột và dùng `writeheader()` ghi tiêu đề.
3. Ghi bản ghi doanh thu rồi in nguyên nội dung bộ đệm.

```python
# Mục đích: Xuất báo cáo CSV.
import csv
from io import StringIO

buffer = StringIO()
writer = csv.DictWriter(
    buffer, fieldnames=['date', 'revenue'], lineterminator='\n'
)
writer.writeheader()
writer.writerow({'date': '2026-10-24', 'revenue': 1200})
print(buffer.getvalue(), end='')
```

**Kết quả khi chạy:**

```text
date,revenue
2026-10-24,1200
```

Dòng đầu chứa tên cột, dòng sau chứa giá trị. `revenue` ghi trong CSV là chữ biểu diễn số, không còn kiểu `int` khi đọc lại.

### Tình huống 5 — Báo lỗi khi thiếu file

**Từ vựng trong mục:** **FileNotFoundError** — lỗi không tìm thấy file; **Path** — đường dẫn.

**Tình huống thực tế:** Một dịch vụ cần đọc `missing.csv` nhưng tệp này chưa được tạo. Hãy in thông báo `File unavailable` thay vì để chương trình dừng vì lỗi thiếu file.

**Vì sao chọn cách giải này?** Dùng `FileNotFoundError` để xử lý riêng tình huống file không tồn tại; thư mục tạm đảm bảo tên tệp này chưa được tạo trong ví dụ.

**Quy trình giải:**

1. Tạo thư mục tạm và đường dẫn tới `missing.csv` chưa tồn tại.
2. Thử gọi `read_text()` trong `try`.
3. Khi phát sinh `FileNotFoundError`, in thông báo.

```python
# Mục đích: Báo lỗi khi thiếu file.
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    missing = Path(folder) / 'missing.csv'
    try:
        text = missing.read_text(encoding='utf-8')
    except FileNotFoundError:
        text = 'File unavailable'
    print(text)
```

**Kết quả khi chạy:**

```text
File unavailable
```

Tệp chưa tồn tại nên khối `except` xử lý lỗi một cách có kiểm soát.
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
