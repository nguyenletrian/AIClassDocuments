# PY-12 — File I/O, CSV và xử lý ngoại lệ

*DRAFT · Tài liệu tự học · Các mã và dữ liệu mẫu cần được kiểm tra trước khi công bố chính thức*

## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **File I/O** — đọc ghi file; **CSV** — dữ liệu phân cách.

`Dictionary → File/CSV → DataFrame → Dataset AI`

Sau Dictionary, ta học cách đưa dữ liệu vào/ra tệp, lưu bảng CSV và xử lý lỗi đầu vào. Đây là nền tảng để làm việc với dữ liệu thật trước khi sử dụng Pandas hay mô hình AI.

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

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What does File I/O mean? — File I/O có nghĩa gì?**

A. Reading data from or writing data to files — Đọc dữ liệu từ hoặc ghi dữ liệu vào tệp

B. Sorting a list in memory — Sắp xếp List trong bộ nhớ

C. Drawing a plot — Vẽ một biểu đồ

D. Training a model — Huấn luyện mô hình

**Q2. What is the purpose of a file path? — Đường dẫn file dùng để làm gì?**

A. Compute a matrix rank — Tính hạng ma trận

B. Identify a file location — Xác định vị trí một tệp

C. Store a Boolean value — Lưu giá trị Boolean

D. Sort rows automatically — Tự sắp xếp các hàng

**Q3. What does `Path.read_text()` do? — `Path.read_text()` làm gì?**

A. Sort CSV by price — Sắp CSV theo giá

B. Convert the path into a function — Chuyển đường dẫn thành hàm

C. Read text content from a file — Đọc nội dung văn bản từ tệp

D. Create a pandas index — Tạo chỉ số Pandas

**Q4. What does `Path.write_text()` do? — `Path.write_text()` dùng để làm gì?**

A. Read and sort all CSV rows — Đọc và sắp mọi hàng CSV

B. Count class methods — Đếm phương thức lớp

C. Only check whether a file exists — Chỉ kiểm tra tệp tồn tại

D. Write text to a file — Ghi văn bản vào tệp

**Q5. Why specify `encoding='utf-8'` for text? — Vì sao dùng `encoding='utf-8'` với văn bản?**

A. To encode Unicode text consistently — Để mã hóa chữ Unicode nhất quán

B. To make all values integers — Để mọi giá trị thành số nguyên

C. To create three CSV columns — Để tạo ba cột CSV

D. To guarantee a file is secret — Để bảo đảm tệp bí mật

**Q6. How does a CSV file normally organize data? — CSV thông thường tổ chức dữ liệu ra sao?**

A. A database server connection — Kết nối máy chủ cơ sở dữ liệu

B. Rows of text with separated fields — Các dòng văn bản chứa trường dữ liệu được phân cách

C. Binary images with pixels — Ảnh nhị phân gồm điểm ảnh

D. Python classes only — Chỉ chứa lớp Python

**Q7. What does `csv.DictReader` use as dictionary keys? — `csv.DictReader` dùng gì làm khóa Dictionary?**

A. Names of Python packages — Tên gói Python

B. The current file size — Kích thước tệp hiện tại

C. CSV column names — Tên cột trong CSV

D. Always numbers 0, 1, 2 — Luôn là số 0, 1, 2

**Q8. What type are values read by `csv.DictReader` by default? — Mặc định giá trị do `csv.DictReader` đọc có kiểu gì?**

A. Integer — Số nguyên

B. Float — Số thực

C. Boolean — Giá trị logic

D. String — Chuỗi

**Q9. What does `csv.DictWriter.writeheader()` write? — `csv.DictWriter.writeheader()` ghi gì?**

A. The column-name header row — Hàng tiêu đề chứa tên các cột

B. The final record twice — Nhân đôi bản ghi cuối

C. An exception message — Thông báo ngoại lệ

D. A Python class definition — Định nghĩa lớp Python

**Q10. Why prefer the CSV module over simply splitting every line by comma? — Vì sao nên dùng module CSV thay vì luôn tách chuỗi theo dấu phẩy?**

A. It encrypts each file — Nó mã hóa bảo mật mọi tệp

B. It handles quoted fields and delimiters correctly — Nó xử lý đúng trường được đặt trong dấu nháy và dấu phân cách

C. It converts every field to a float — Nó đổi mọi trường thành số thực

D. It removes all empty rows automatically — Nó tự bỏ mọi dòng rỗng

**Q11. What is an exception in Python? — Ngoại lệ trong Python là gì?**

A. A CSV row header — Hàng tiêu đề CSV

B. A list slicing operator — Toán tử cắt List

C. An error or abnormal condition raised during execution — Lỗi hoặc tình huống bất thường phát sinh khi chạy

D. A guaranteed successful result — Một kết quả chắc chắn thành công

**Q12. What does `int('abc')` raise? — `int('abc')` phát sinh lỗi gì?**

A. `FileNotFoundError` — `FileNotFoundError`

B. `ZeroDivisionError` — `ZeroDivisionError`

C. No error; returns zero — Không lỗi và trả về 0

D. `ValueError` — `ValueError`

**Q13. What does `except ValueError` catch? — `except ValueError` xử lý loại lỗi nào?**

A. Value conversion errors — Lỗi chuyển giá trị không hợp lệ

B. All file permission failures — Mọi lỗi quyền truy cập tệp

C. Every possible error — Mọi lỗi có thể xảy ra

D. Only successful conversions — Chỉ khi chuyển kiểu thành công

**Q14. Which exception commonly indicates a missing file? — Ngoại lệ nào thường báo tệp không tồn tại?**

A. `TypeError` always — Luôn `TypeError`

B. `FileNotFoundError` — `FileNotFoundError`

C. `ValueError` only — Chỉ `ValueError`

D. `KeyError` only — Chỉ `KeyError`

**Q15. What does a `with` block provide for a file? — Khối `with` hỗ trợ việc gì khi dùng file?**

A. Automatic sorting — Tự sắp xếp

B. Automatic internet download — Tự tải từ Internet

C. Automatic resource cleanup on exit — Tự dọn dẹp và đóng tài nguyên khi ra khỏi khối

D. Automatic numeric conversion — Tự chuyển toàn bộ số

**Q16. What is `StringIO` useful for? — `StringIO` hữu ích cho việc gì?**

A. Operating a camera sensor — Điều khiển cảm biến camera

B. Reading only images — Chỉ đọc ảnh

C. Turning a set into a tuple — Biến Set thành Tuple

D. File-like text operations in memory — Đọc ghi văn bản như file ngay trong bộ nhớ

**Q17. What is the difference between `write` mode and append mode? — Chế độ ghi `w` và nối thêm `a` khác nhau thế nào?**

A. `w` replaces contents; `a` adds to the end — `w` thay nội dung; `a` nối thêm cuối tệp

B. Both only read existing content — Cả hai chỉ đọc nội dung

C. `a` always deletes files — `a` luôn xóa tệp

D. `w` only opens network sockets — `w` chỉ mở socket mạng

**Q18. Why is a bare `except:` often a poor choice? — Vì sao thường không nên dùng `except:` không chỉ rõ lỗi?**

A. It converts errors into CSV — Nó chuyển lỗi thành CSV

B. It can hide unexpected programming errors — Nó có thể che các lỗi lập trình không lường trước

C. It never catches any error — Nó không bắt được lỗi nào

D. It prevents file creation — Nó ngăn tạo file

**Q19. What does `print(text, end='')` change? — `print(text, end='')` thay đổi điều gì?**

A. It closes every open file — Nó đóng mọi file đang mở

B. It converts text to numbers — Nó chuyển chữ thành số

C. It avoids adding the default newline — Nó không tự thêm dấu xuống dòng mặc định

D. It removes existing newlines from text — Nó xóa mọi dấu xuống dòng có sẵn trong text

**Q20. Which distinction between `csv.reader` and `csv.DictReader` is correct? — `csv.reader` khác `csv.DictReader` ở điểm nào?**

A. Both always return float arrays — Cả hai luôn trả mảng số thực

B. DictReader writes files but cannot read — DictReader chỉ ghi mà không đọc

C. reader always validates all values — reader luôn kiểm tra mọi giá trị

D. reader yields field lists; DictReader uses column keys — reader trả danh sách trường; DictReader dùng khóa theo tên cột

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | I/O stands for input/output; files can receive and provide data.~I/O là nhập/xuất; tệp có thể là nơi nhận và cung cấp dữ liệu. | undefined |
| Q2 | **B** | Path identifies where a file or directory is located.~Đường dẫn cho biết tệp hoặc thư mục nằm ở đâu. | undefined |
| Q3 | **C** | read_text returns the file's text contents, given a suitable encoding.~read_text trả về nội dung chữ của tệp với mã hóa phù hợp. | undefined |
| Q4 | **D** | write_text writes the supplied text and replaces prior contents by default.~write_text ghi văn bản và mặc định thay nội dung cũ. | undefined |
| Q5 | **A** | Explicit UTF-8 helps preserve Vietnamese and other Unicode characters.~Chỉ rõ UTF-8 giúp lưu và đọc đúng tiếng Việt và ký tự Unicode. | undefined |
| Q6 | **B** | CSV stores tabular records as text, often with a header row.~CSV biểu diễn bản ghi dạng bảng bằng văn bản, thường có hàng tiêu đề. | undefined |
| Q7 | **C** | DictReader commonly takes keys from the header fields.~DictReader thường lấy tên khóa từ hàng tiêu đề CSV. | undefined |
| Q8 | **D** | CSV is text, so numeric-looking cells must be converted explicitly.~CSV là văn bản nên ô trông giống số vẫn cần chuyển kiểu rõ ràng. | undefined |
| Q9 | **A** | writeheader emits the field names defined for the writer.~writeheader ghi các tên trường đã cấu hình cho bộ ghi. | undefined |
| Q10 | **B** | A comma inside a quoted CSV field is data, not a separator.~Dấu phẩy trong một trường CSV có dấu nháy là dữ liệu, không phải dấu tách trường. | undefined |
| Q11 | **C** | Exceptions report exceptional execution conditions and may be handled.~Ngoại lệ báo trạng thái bất thường khi chạy và có thể được xử lý. | undefined |
| Q12 | **D** | The string is not a valid integer representation.~Chuỗi abc không phải biểu diễn số nguyên hợp lệ. | undefined |
| Q13 | **A** | A specific exception handler does not indiscriminately swallow other errors.~Bắt đúng loại ValueError tránh che mất các lỗi khác không liên quan. | undefined |
| Q14 | **B** | The missing path raises FileNotFoundError on file access.~Truy cập một tệp không tồn tại thường phát sinh FileNotFoundError. | undefined |
| Q15 | **C** | The context manager closes the file even if an exception occurs inside.~Trình quản lý ngữ cảnh đóng file kể cả khi có ngoại lệ trong khối. | undefined |
| Q16 | **D** | StringIO lets text readers and writers work without a physical file.~StringIO cho phép xử lý văn bản như file mà không cần tạo tệp trên đĩa. | undefined |
| Q17 | **A** | Mode w truncates existing content, while a appends new data.~Chế độ w cắt nội dung cũ, còn a bổ sung cuối tệp. | undefined |
| Q18 | **B** | Catch errors that the code intentionally knows how to handle.~Chỉ nên bắt những loại lỗi chương trình có cách xử lý cụ thể. | undefined |
| Q19 | **C** | The end argument controls what print appends after its contents.~Tham số end điều khiển ký tự được print thêm vào cuối nội dung. | undefined |
| Q20 | **D** | DictReader makes column-name lookups easier than positional lists.~DictReader giúp tra cứu theo tên cột thay vì chỉ theo vị trí. | undefined |

## 8. Nối sang bài tiếp theo

`Dictionary → File/CSV → DataFrame → Dataset AI`.
