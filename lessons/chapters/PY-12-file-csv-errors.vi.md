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


**Q1. Which description matches File I/O? — Mô tả nào đúng với File I/O?**

A. A different concept described as Định dạng bảng dạng văn bản — Định dạng bảng dạng văn bản

B. The concept described as Lấy hoặc lưu dữ liệu trên đĩa — Lấy hoặc lưu dữ liệu trên đĩa

C. A different concept described as Lỗi xuất hiện khi chạy chương trình — Lỗi xuất hiện khi chạy chương trình

D. A different concept described as Tự đóng tài nguyên sau khối with — Tự đóng tài nguyên sau khối with


**Q2. Which description matches CSV? — Mô tả nào đúng với CSV?**

A. The concept described as Định dạng bảng dạng văn bản — Định dạng bảng dạng văn bản

B. A different concept described as Lỗi xuất hiện khi chạy chương trình — Lỗi xuất hiện khi chạy chương trình

C. A different concept described as Tự đóng tài nguyên sau khối with — Tự đóng tài nguyên sau khối with

D. A different concept described as Lấy hoặc lưu dữ liệu trên đĩa — Lấy hoặc lưu dữ liệu trên đĩa


**Q3. Which description matches Exception? — Mô tả nào đúng với Exception?**

A. A different concept described as Tự đóng tài nguyên sau khối with — Tự đóng tài nguyên sau khối with

B. A different concept described as Lấy hoặc lưu dữ liệu trên đĩa — Lấy hoặc lưu dữ liệu trên đĩa

C. A different concept described as Định dạng bảng dạng văn bản — Định dạng bảng dạng văn bản

D. The concept described as Lỗi xuất hiện khi chạy chương trình — Lỗi xuất hiện khi chạy chương trình


**Q4. Which description matches Context manager? — Mô tả nào đúng với Context manager?**

A. A different concept described as Lấy hoặc lưu dữ liệu trên đĩa — Lấy hoặc lưu dữ liệu trên đĩa

B. A different concept described as Định dạng bảng dạng văn bản — Định dạng bảng dạng văn bản

C. The concept described as Tự đóng tài nguyên sau khối with — Tự đóng tài nguyên sau khối with

D. A different concept described as Lỗi xuất hiện khi chạy chương trình — Lỗi xuất hiện khi chạy chương trình


**Q5. Which use matches open(...,encoding='utf-8')? — Công dụng nào đúng với open(...,encoding='utf-8')?**

A. Use a different operation to Đọc và ghi CSV theo tên cột thay vì vị trí — Đọc và ghi CSV theo tên cột thay vì vị trí

B. Use this syntax to Đọc/ghi Unicode và tự đóng bằng with — Đọc/ghi Unicode và tự đóng bằng with

C. Use a different operation to Bắt riêng lỗi dữ liệu nhập không hợp lệ — Bắt riêng lỗi dữ liệu nhập không hợp lệ

D. Use a different operation to Đọc/ghi file với đường dẫn kiểu Path — Đọc/ghi file với đường dẫn kiểu Path


**Q6. Which use matches csv.DictReader/DictWriter? — Công dụng nào đúng với csv.DictReader/DictWriter?**

A. Use this syntax to Đọc và ghi CSV theo tên cột thay vì vị trí — Đọc và ghi CSV theo tên cột thay vì vị trí

B. Use a different operation to Bắt riêng lỗi dữ liệu nhập không hợp lệ — Bắt riêng lỗi dữ liệu nhập không hợp lệ

C. Use a different operation to Đọc/ghi file với đường dẫn kiểu Path — Đọc/ghi file với đường dẫn kiểu Path

D. Use a different operation to Đọc/ghi Unicode và tự đóng bằng with — Đọc/ghi Unicode và tự đóng bằng with


**Q7. Which use matches try/except ValueError? — Công dụng nào đúng với try/except ValueError?**

A. Use a different operation to Đọc/ghi file với đường dẫn kiểu Path — Đọc/ghi file với đường dẫn kiểu Path

B. Use a different operation to Đọc/ghi Unicode và tự đóng bằng with — Đọc/ghi Unicode và tự đóng bằng with

C. Use a different operation to Đọc và ghi CSV theo tên cột thay vì vị trí — Đọc và ghi CSV theo tên cột thay vì vị trí

D. Use this syntax to Bắt riêng lỗi dữ liệu nhập không hợp lệ — Bắt riêng lỗi dữ liệu nhập không hợp lệ


**Q8. Which use matches Path.read_text()/write_text()? — Công dụng nào đúng với Path.read_text()/write_text()?**

A. Use a different operation to Đọc/ghi Unicode và tự đóng bằng with — Đọc/ghi Unicode và tự đóng bằng with

B. Use a different operation to Đọc và ghi CSV theo tên cột thay vì vị trí — Đọc và ghi CSV theo tên cột thay vì vị trí

C. Use this syntax to Đọc/ghi file với đường dẫn kiểu Path — Đọc/ghi file với đường dẫn kiểu Path

D. Use a different operation to Bắt riêng lỗi dữ liệu nhập không hợp lệ — Bắt riêng lỗi dữ liệu nhập không hợp lệ


**Q9. What solves scenario 1? — Cách nào giải quyết tình huống 1?**

A. Another method is chosen because Quản lý tệp trong thư mục tạm để không để lại file học thử — Quản lý tệp trong thư mục tạm để không để lại file học thử

B. Choose the method because DictReader dùng tiêu đề cột để tránh tráo giá và tên — DictReader dùng tiêu đề cột để tránh tráo giá và tên

C. Another method is chosen because Chỉ bắt ValueError khi nhập không chuyển sang số được — Chỉ bắt ValueError khi nhập không chuyển sang số được

D. Another method is chosen because DictWriter giữ thứ tự tên cột rõ ràng — DictWriter giữ thứ tự tên cột rõ ràng


**Q10. What solves scenario 2? — Cách nào giải quyết tình huống 2?**

A. Choose the method because Quản lý tệp trong thư mục tạm để không để lại file học thử — Quản lý tệp trong thư mục tạm để không để lại file học thử

B. Another method is chosen because Chỉ bắt ValueError khi nhập không chuyển sang số được — Chỉ bắt ValueError khi nhập không chuyển sang số được

C. Another method is chosen because DictWriter giữ thứ tự tên cột rõ ràng — DictWriter giữ thứ tự tên cột rõ ràng

D. Another method is chosen because Bắt FileNotFoundError để chương trình không dừng không rõ nguyên nhân — Bắt FileNotFoundError để chương trình không dừng không rõ nguyên nhân


**Q11. What solves scenario 3? — Cách nào giải quyết tình huống 3?**

A. Another method is chosen because DictWriter giữ thứ tự tên cột rõ ràng — DictWriter giữ thứ tự tên cột rõ ràng

B. Another method is chosen because Bắt FileNotFoundError để chương trình không dừng không rõ nguyên nhân — Bắt FileNotFoundError để chương trình không dừng không rõ nguyên nhân

C. Another method is chosen because DictReader dùng tiêu đề cột để tránh tráo giá và tên — DictReader dùng tiêu đề cột để tránh tráo giá và tên

D. Choose the method because Chỉ bắt ValueError khi nhập không chuyển sang số được — Chỉ bắt ValueError khi nhập không chuyển sang số được


**Q12. What solves scenario 4? — Cách nào giải quyết tình huống 4?**

A. Another method is chosen because Bắt FileNotFoundError để chương trình không dừng không rõ nguyên nhân — Bắt FileNotFoundError để chương trình không dừng không rõ nguyên nhân

B. Another method is chosen because DictReader dùng tiêu đề cột để tránh tráo giá và tên — DictReader dùng tiêu đề cột để tránh tráo giá và tên

C. Choose the method because DictWriter giữ thứ tự tên cột rõ ràng — DictWriter giữ thứ tự tên cột rõ ràng

D. Another method is chosen because Quản lý tệp trong thư mục tạm để không để lại file học thử — Quản lý tệp trong thư mục tạm để không để lại file học thử


**Q13. What solves scenario 5? — Cách nào giải quyết tình huống 5?**

A. Another method is chosen because DictReader dùng tiêu đề cột để tránh tráo giá và tên — DictReader dùng tiêu đề cột để tránh tráo giá và tên

B. Choose the method because Bắt FileNotFoundError để chương trình không dừng không rõ nguyên nhân — Bắt FileNotFoundError để chương trình không dừng không rõ nguyên nhân

C. Another method is chosen because Quản lý tệp trong thư mục tạm để không để lại file học thử — Quản lý tệp trong thư mục tạm để không để lại file học thử

D. Another method is chosen because Chỉ bắt ValueError khi nhập không chuyển sang số được — Chỉ bắt ValueError khi nhập không chuyển sang số được


**Q14. Which data is used in scenario 1? — Tình huống 1 dùng dữ liệu nào?**

A. The described input Hai sản phẩm với hai cột name,price — Hai sản phẩm với hai cột name,price

B. Another input Một dòng log Started — Một dòng log Started

C. Another input Dữ liệu đầu vào 'abc' — Dữ liệu đầu vào 'abc'

D. Another input Ngày và doanh thu ví dụ — Ngày và doanh thu ví dụ


**Q15. Which data is used in scenario 2? — Tình huống 2 dùng dữ liệu nào?**

A. Another input Dữ liệu đầu vào 'abc' — Dữ liệu đầu vào 'abc'

B. Another input Ngày và doanh thu ví dụ — Ngày và doanh thu ví dụ

C. Another input Một tệp giả định không tồn tại — Một tệp giả định không tồn tại

D. The described input Một dòng log Started — Một dòng log Started


**Q16. Which data is used in scenario 3? — Tình huống 3 dùng dữ liệu nào?**

A. Another input Ngày và doanh thu ví dụ — Ngày và doanh thu ví dụ

B. Another input Một tệp giả định không tồn tại — Một tệp giả định không tồn tại

C. The described input Dữ liệu đầu vào 'abc' — Dữ liệu đầu vào 'abc'

D. Another input Hai sản phẩm với hai cột name,price — Hai sản phẩm với hai cột name,price


**Q17. Which data is used in scenario 4? — Tình huống 4 dùng dữ liệu nào?**

A. Another input Một tệp giả định không tồn tại — Một tệp giả định không tồn tại

B. The described input Ngày và doanh thu ví dụ — Ngày và doanh thu ví dụ

C. Another input Hai sản phẩm với hai cột name,price — Hai sản phẩm với hai cột name,price

D. Another input Một dòng log Started — Một dòng log Started


**Q18. Which data is used in scenario 5? — Tình huống 5 dùng dữ liệu nào?**

A. The described input Một tệp giả định không tồn tại — Một tệp giả định không tồn tại

B. Another input Hai sản phẩm với hai cột name,price — Hai sản phẩm với hai cột name,price

C. Another input Một dòng log Started — Một dòng log Started

D. Another input Dữ liệu đầu vào 'abc' — Dữ liệu đầu vào 'abc'


**Q19. What must be clear before computing? — Cần hiểu gì trước khi tính?**

A. Only font color — Chỉ màu chữ

B. Only filename length — Chỉ độ dài tên file

C. Only number of comments — Chỉ số comment

D. Input meaning and units — Ý nghĩa và đơn vị dữ liệu


**Q20. What should follow a successful demo? — Sau khi demo chạy đúng nên làm gì?**

A. Assume it works for all data — Cho rằng luôn đúng với mọi dữ liệu

B. Remove input validation — Xóa kiểm tra đầu vào

C. Verify output and unusual inputs — Kiểm tra đầu ra và giá trị biên

D. Ignore unexpected results — Bỏ qua kết quả bất thường

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | The concept described as Lấy hoặc lưu dữ liệu trên đĩa | Lấy hoặc lưu dữ liệu trên đĩa |
| Q2 | **A** | The concept described as Định dạng bảng dạng văn bản | Định dạng bảng dạng văn bản |
| Q3 | **D** | The concept described as Lỗi xuất hiện khi chạy chương trình | Lỗi xuất hiện khi chạy chương trình |
| Q4 | **C** | The concept described as Tự đóng tài nguyên sau khối with | Tự đóng tài nguyên sau khối with |
| Q5 | **B** | Use this syntax to Đọc/ghi Unicode và tự đóng bằng with | Đọc/ghi Unicode và tự đóng bằng with |
| Q6 | **A** | Use this syntax to Đọc và ghi CSV theo tên cột thay vì vị trí | Đọc và ghi CSV theo tên cột thay vì vị trí |
| Q7 | **D** | Use this syntax to Bắt riêng lỗi dữ liệu nhập không hợp lệ | Bắt riêng lỗi dữ liệu nhập không hợp lệ |
| Q8 | **C** | Use this syntax to Đọc/ghi file với đường dẫn kiểu Path | Đọc/ghi file với đường dẫn kiểu Path |
| Q9 | **B** | Choose the method because DictReader dùng tiêu đề cột để tránh tráo giá và tên | DictReader dùng tiêu đề cột để tránh tráo giá và tên |
| Q10 | **A** | Choose the method because Quản lý tệp trong thư mục tạm để không để lại file học thử | Quản lý tệp trong thư mục tạm để không để lại file học thử |
| Q11 | **D** | Choose the method because Chỉ bắt ValueError khi nhập không chuyển sang số được | Chỉ bắt ValueError khi nhập không chuyển sang số được |
| Q12 | **C** | Choose the method because DictWriter giữ thứ tự tên cột rõ ràng | DictWriter giữ thứ tự tên cột rõ ràng |
| Q13 | **B** | Choose the method because Bắt FileNotFoundError để chương trình không dừng không rõ nguyên nhân | Bắt FileNotFoundError để chương trình không dừng không rõ nguyên nhân |
| Q14 | **A** | The described input Hai sản phẩm với hai cột name,price | Hai sản phẩm với hai cột name,price |
| Q15 | **D** | The described input Một dòng log Started | Một dòng log Started |
| Q16 | **C** | The described input Dữ liệu đầu vào 'abc' | Dữ liệu đầu vào 'abc' |
| Q17 | **B** | The described input Ngày và doanh thu ví dụ | Ngày và doanh thu ví dụ |
| Q18 | **A** | The described input Một tệp giả định không tồn tại | Một tệp giả định không tồn tại |
| Q19 | **D** | Input meaning and units | Ý nghĩa và đơn vị dữ liệu |
| Q20 | **C** | Verify output and unusual inputs | Kiểm tra đầu ra và giá trị biên |

## 8. Nối sang bài tiếp theo

`Dictionary → File/CSV → DataFrame → Dataset AI`.
