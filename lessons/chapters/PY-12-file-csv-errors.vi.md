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

B. Reading only console input — Chỉ đọc đầu vào từ bàn phím

C. Modifying only in-memory lists — Chỉ sửa List trong bộ nhớ

D. Printing variables without saving files — In biến mà không lưu tệp

**Q2. What is the purpose of a file path? — Đường dẫn file dùng để làm gì?**

A. Storing the file's full contents — Lưu toàn bộ nội dung tệp

B. Guaranteeing the file can be opened — Bảo đảm có thể mở tệp

C. Specifying the encoding of every field — Chỉ định encoding cho mỗi trường

D. Identify a file location — Xác định vị trí một tệp

**Q3. What does `Path.read_text()` do? — `Path.read_text()` làm gì?**

A. Writing a text file — Ghi một tệp văn bản

B. Returning only the path's name — Chỉ trả tên đường dẫn

C. Parsing the file into CSV dictionaries — Phân tích tệp thành các Dictionary CSV

D. Read text content from a file — Đọc nội dung văn bản từ tệp

**Q4. What does `Path.write_text()` do? — `Path.write_text()` dùng để làm gì?**

A. Appending without changing old contents by default — Mặc định nối thêm và không sửa nội dung cũ

B. Only changing a file's name — Chỉ đổi tên tệp

C. Write text to a file — Ghi văn bản vào tệp

D. Reading text without changing the file — Đọc văn bản mà không đổi tệp

**Q5. Why specify `encoding='utf-8'` for text? — Vì sao dùng `encoding='utf-8'` với văn bản?**

A. Preventing all file read errors — Ngăn mọi lỗi đọc tệp

B. To encode Unicode text consistently — Để mã hóa chữ Unicode nhất quán

C. Automatically converting text to integer values — Tự chuyển văn bản sang số nguyên

D. Encrypting the file contents for privacy — Mã hóa bảo mật nội dung tệp

**Q6. How does a CSV file normally organize data? — CSV thông thường tổ chức dữ liệu ra sao?**

A. Only a list of Python dictionaries in memory — Chỉ danh sách Dictionary Python trong bộ nhớ

B. A fixed-width binary record format — Định dạng bản ghi nhị phân có độ dài cố định

C. A file that guarantees numerical columns — Tệp bảo đảm mọi cột đều là số

D. Rows of text with separated fields — Các dòng văn bản chứa trường dữ liệu được phân cách

**Q7. What does `csv.DictReader` use as dictionary keys? — `csv.DictReader` dùng gì làm khóa Dictionary?**

A. Values from the final CSV row — Giá trị hàng CSV cuối cùng

B. The full file path as every key — Toàn bộ đường dẫn tệp làm mọi khóa

C. CSV column names — Tên cột trong CSV

D. Numeric column indexes starting at zero — Chỉ số cột bằng số bắt đầu từ 0

**Q8. What type are values read by `csv.DictReader` by default? — Mặc định giá trị do `csv.DictReader` đọc có kiểu gì?**

A. Integers for fields containing digits — Số nguyên cho trường chứa chữ số

B. Floating-point values for decimals — Số thực cho trường chứa dấu thập phân

C. Booleans for empty and nonempty fields — Boolean cho trường rỗng và không rỗng

D. String — Chuỗi

**Q9. What does `csv.DictWriter.writeheader()` write? — `csv.DictWriter.writeheader()` ghi gì?**

A. The column-name header row — Hàng tiêu đề chứa tên các cột

B. All data rows in the file — Mọi hàng dữ liệu trong tệp

C. Only the first data record — Chỉ bản ghi dữ liệu đầu

D. A list of Python parameter names — Danh sách tên tham số Python

**Q10. Why prefer the CSV module over simply splitting every line by comma? — Vì sao nên dùng module CSV thay vì luôn tách chuỗi theo dấu phẩy?**

A. Guaranteed removal of empty fields — Bảo đảm xóa mọi trường rỗng

B. Automatic detection of missing files — Tự phát hiện tệp bị thiếu

C. It handles quoted fields and delimiters correctly — Nó xử lý đúng trường được đặt trong dấu nháy và dấu phân cách

D. Automatic type conversion for numeric fields — Tự chuyển kiểu các trường số

**Q11. What is an exception in Python? — Ngoại lệ trong Python là gì?**

A. A valid program's printed result — Kết quả in của chương trình hợp lệ

B. A Python List indexing rule — Quy tắc chỉ số List Python

C. An error or abnormal condition raised during execution — Lỗi hoặc tình huống bất thường phát sinh khi chạy

D. A normal CSV header — Hàng tiêu đề CSV bình thường

**Q12. What does `int('abc')` raise? — `int('abc')` phát sinh lỗi gì?**

A. Returns integer zero without error — Trả số nguyên 0 mà không lỗi

B. `ValueError` — `ValueError`

C. `TypeError` for every string input — `TypeError` cho mọi đầu vào chuỗi

D. `FileNotFoundError` from integer parsing — `FileNotFoundError` do phân tích số nguyên

**Q13. What does `except ValueError` catch? — `except ValueError` xử lý loại lỗi nào?**

A. Only successful integer conversion events — Chỉ sự kiện chuyển số nguyên thành công

B. Value conversion errors — Lỗi chuyển giá trị không hợp lệ

C. Every exception raised anywhere in the program — Mọi ngoại lệ ở bất kỳ đâu trong chương trình

D. Only file access permission errors — Chỉ lỗi quyền truy cập tệp

**Q14. Which exception commonly indicates a missing file? — Ngoại lệ nào thường báo tệp không tồn tại?**

A. `FileNotFoundError` — `FileNotFoundError`

B. `KeyError` — `KeyError`

C. `ValueError` — `ValueError`

D. `ZeroDivisionError` — `ZeroDivisionError`

**Q15. What does a `with` block provide for a file? — Khối `with` hỗ trợ việc gì khi dùng file?**

A. Automatic creation of missing file parents — Tự tạo thư mục cha còn thiếu

B. Automatic resource cleanup on exit — Tự dọn dẹp và đóng tài nguyên khi ra khỏi khối

C. Automatic CSV sorting on block exit — Tự sắp CSV khi thoát khối

D. Automatic numeric conversion of read values — Tự chuyển giá trị đã đọc thành số

**Q16. What is `StringIO` useful for? — `StringIO` hữu ích cho việc gì?**

A. File-like text operations in memory — Đọc ghi văn bản như file ngay trong bộ nhớ

B. A binary-only byte buffer — Bộ đệm chỉ có byte nhị phân

C. Permanent storage that survives process exit — Nơi lưu bền vững sau khi tiến trình kết thúc

D. An API that parses only PNG files — API chỉ phân tích ảnh PNG

**Q17. What is the difference between `write` mode and append mode? — Chế độ ghi `w` và nối thêm `a` khác nhau thế nào?**

A. Both modes always reject nonexistent files — Cả hai luôn từ chối tệp không tồn tại

B. `w` replaces contents; `a` adds to the end — `w` thay nội dung; `a` nối thêm cuối tệp

C. `w` appends and `a` overwrites — `w` nối thêm còn `a` ghi đè

D. Both modes are read-only — Cả hai chế độ chỉ đọc

**Q18. Why is a bare `except:` often a poor choice? — Vì sao thường không nên dùng `except:` không chỉ rõ lỗi?**

A. It guarantees a readable error trace — Bảo đảm cung cấp traceback dễ đọc

B. It automatically retries the failing operation — Tự thử lại thao tác bị lỗi

C. It can hide unexpected programming errors — Nó có thể che các lỗi lập trình không lường trước

D. It catches no exceptions at all — Không bắt bất kỳ ngoại lệ nào

**Q19. What does `print(text, end='')` change? — `print(text, end='')` thay đổi điều gì?**

A. Deletes newlines inside the input string — Xóa dấu xuống dòng trong chuỗi đầu vào

B. Stops all output after the first character — Dừng in sau ký tự đầu

C. Changes the value into an integer — Đổi giá trị thành số nguyên

D. It avoids adding the default newline — Nó không tự thêm dấu xuống dòng mặc định

**Q20. Which distinction between `csv.reader` and `csv.DictReader` is correct? — `csv.reader` khác `csv.DictReader` ở điểm nào?**

A. reader yields field lists; DictReader uses column keys — reader trả danh sách trường; DictReader dùng khóa theo tên cột

B. `reader` returns dictionary mappings, while `DictReader` yields lists — `reader` trả Dictionary còn `DictReader` trả List

C. `reader` always infers numeric types — `reader` luôn suy luận kiểu số

D. `DictReader` discards the header and cannot use names — `DictReader` bỏ tiêu đề và không dùng được tên

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | File I/O transfers data between a running program and files. Reading loads saved information; writing persists new information beyond the current process. | File I/O trao đổi dữ liệu giữa chương trình và tệp. Đọc lấy thông tin đã lưu, còn ghi giúp lưu kết quả sau khi tiến trình kết thúc. |
| Q2 | **D** | A path identifies where a file or directory can be found, such as `data/scores.csv`. A path is a location reference, not the file's contents or proof that it exists. | Đường dẫn chỉ nơi tìm tệp hoặc thư mục, ví dụ `data/scores.csv`. Đường dẫn không phải nội dung và cũng không bảo đảm tệp tồn tại. |
| Q3 | **D** | `Path.read_text()` decodes file bytes and returns a text string. It needs a readable file and appropriate encoding; it does not parse CSV records automatically. | `Path.read_text()` giải mã byte của tệp và trả về chuỗi văn bản. Cần tệp đọc được cùng encoding phù hợp; hàm không tự phân tích các bản ghi CSV. |
| Q4 | **C** | `Path.write_text(text)` writes text and replaces existing file contents by default. Adding to an existing report instead requires an append operation. | `Path.write_text(text)` ghi văn bản và mặc định thay nội dung tệp đang có. Muốn nối thêm vào báo cáo cũ cần dùng thao tác ghi nối. |
| Q5 | **B** | Explicit UTF-8 consistently represents Unicode characters, including Vietnamese diacritics, across systems. An encoding is a text representation, not encryption or access control. | UTF-8 tường minh giúp biểu diễn nhất quán ký tự Unicode và dấu tiếng Việt giữa các hệ thống. Encoding là cách biểu diễn văn bản, không phải cơ chế mã hóa bảo mật hoặc phân quyền. |
| Q6 | **D** | CSV contains records in rows with fields separated by delimiters, often including a header. Quoted fields may contain commas, which a CSV parser handles correctly. | CSV lưu bản ghi theo hàng với các trường ngăn bằng dấu phân cách, thường có hàng tiêu đề. Trường có dấu nháy có thể chứa dấu phẩy và bộ phân tích CSV xử lý đúng trường hợp đó. |
| Q7 | **C** | By default, `csv.DictReader` uses the header field names as dictionary keys for each subsequent row. For `name,score`, row dictionaries have keys `name` and `score`, not automatic numeric indexes. | Mặc định `csv.DictReader` dùng tên trường của hàng tiêu đề làm khóa cho Dictionary ở các hàng sau. Với `name,score`, khóa là `name` và `score`, không phải chỉ số số tự sinh. |
| Q8 | **D** | Ordinary CSV fields are read as text by `DictReader`, even when they contain digits. A `score` cell containing 9 becomes `'9'`, so calculations require `int()` or `float()` as appropriate. | Các trường CSV thông thường được `DictReader` đọc thành văn bản, kể cả khi chứa chữ số. Ô `score` là 9 sẽ thành `'9'`, nên tính toán cần chuyển bằng `int()` hoặc `float()` khi thích hợp. |
| Q9 | **A** | `DictWriter.writeheader()` writes the configured field names as a CSV header row. Actual records must be written separately using `writerow()` or `writerows()`. | `DictWriter.writeheader()` ghi tên các trường đã cấu hình thành hàng tiêu đề CSV. Các bản ghi dữ liệu cần được ghi riêng bằng `writerow()` hoặc `writerows()`. |
| Q10 | **C** | The CSV parser respects quoted delimiters: `"An, Binh",9` contains two fields, not three. Naively calling `.split(',')` would incorrectly separate the name field. | Bộ phân tích CSV tôn trọng dấu phân cách trong dấu nháy: `"An, Binh",9` chỉ có hai trường, không phải ba. Gọi `.split(',')` đơn giản sẽ tách sai tên. |
| Q11 | **C** | An exception signals an abnormal condition during execution, such as invalid conversion or a missing file. A matching `try/except` can handle it; otherwise execution may be interrupted. | Ngoại lệ báo điều kiện bất thường trong lúc chạy, như chuyển kiểu sai hoặc thiếu tệp. Khối `try/except` phù hợp có thể xử lý; nếu không, chương trình có thể bị ngắt. |
| Q12 | **B** | `int('abc')` raises `ValueError` because the letters cannot represent a decimal integer. The function exists and the argument is a string, so this is not a missing-name error. | `int('abc')` gây `ValueError` vì chữ cái không biểu diễn số nguyên thập phân. Hàm có tồn tại và đối số là chuỗi, nên đây không phải lỗi thiếu tên. |
| Q13 | **B** | `except ValueError` catches `ValueError` and its subclasses from the associated `try` block. It is suitable for invalid numeric conversion, but not automatically for every missing-file failure. | `except ValueError` bắt `ValueError` và ngoại lệ con từ khối `try` tương ứng. Nó hợp với chuyển số sai, nhưng không tự bắt mọi lỗi thiếu tệp. |
| Q14 | **A** | `FileNotFoundError` commonly signals that the requested path does not refer to an existing file. This differs from `PermissionError`, where access may be denied even though the file exists. | `FileNotFoundError` thường báo không có tệp tại đường dẫn yêu cầu. Nó khác `PermissionError`, khi tệp có thể tồn tại nhưng chương trình không được truy cập. |
| Q15 | **B** | `with` manages a file resource and closes it on exit, including when an exception occurs inside the block. It does not automatically convert CSV text to integers or sort records. | `with` quản lý tài nguyên tệp và đóng khi thoát khối, kể cả khi thân khối phát sinh ngoại lệ. Nó không tự đổi dữ liệu CSV thành số hay sắp xếp bản ghi. |
| Q16 | **A** | `StringIO` supplies a file-like text stream in memory, useful for CSV tests without creating a disk file. It is separate from binary streams such as `BytesIO`. | `StringIO` cung cấp luồng văn bản giống tệp trong bộ nhớ, hữu ích để thử CSV không cần tạo tệp trên đĩa. Nó khác luồng byte nhị phân như `BytesIO`. |
| Q17 | **B** | Opening in mode `'w'` truncates existing content, while mode `'a'` adds data at the end. Use append for a growing log so previous entries remain intact. | Mở bằng chế độ `'w'` sẽ cắt nội dung cũ, còn `'a'` thêm dữ liệu vào cuối. Dùng nối thêm cho nhật ký tăng dần để giữ bản ghi trước đó. |
| Q18 | **C** | Bare `except:` catches too broadly, potentially hiding programming mistakes and intercepting interrupts. Prefer named exception classes when the program has a meaningful recovery strategy. | `except:` không nêu loại lỗi bắt quá rộng, có thể che lỗi lập trình và cả thao tác ngắt. Nên bắt lớp ngoại lệ cụ thể khi chương trình có cách phục hồi phù hợp. |
| Q19 | **D** | `print(text, end='')` suppresses the newline normally appended by `print`. Newlines already contained inside `text` remain unchanged. | `print(text, end='')` bỏ ký tự xuống dòng mà `print` mặc định thêm vào cuối. Dấu xuống dòng vốn có trong `text` vẫn giữ nguyên. |
| Q20 | **A** | `csv.reader` yields each record as a list of strings; `DictReader` maps column names to values. Column names help distinguish fields even if their order changes. | `csv.reader` trả mỗi bản ghi dưới dạng List các chuỗi; `DictReader` ánh xạ tên cột đến giá trị. Tra theo tên cột giúp phân biệt trường ngay cả khi thứ tự cột thay đổi. |

## 8. Nối sang bài tiếp theo

`Dictionary → File/CSV → DataFrame → Dataset AI`.
