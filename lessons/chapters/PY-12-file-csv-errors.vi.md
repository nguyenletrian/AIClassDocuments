# PY-12 — File I/O, CSV và xử lý ngoại lệ

## 1. Vị trí trong chuỗi kiến thức

`Dictionary → File/CSV → DataFrame → Dataset AI`

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| File I/O | đọc ghi file | Lấy hoặc lưu dữ liệu trên đĩa |
| CSV | dữ liệu phân cách | Định dạng bảng dạng văn bản |
| Exception | ngoại lệ | Lỗi xuất hiện khi chạy chương trình |
| Context manager | quản lý ngữ cảnh | Tự đóng tài nguyên sau khối with |

## 3. Thư viện, hàm và tham số

| Hàm/cú pháp | Giải thích và lý do dùng |
|---|---|
| `open(...,encoding='utf-8')` | Đọc/ghi Unicode và tự đóng bằng with |
| `csv.DictReader/DictWriter` | Đọc và ghi CSV theo tên cột thay vì vị trí |
| `try/except ValueError` | Bắt riêng lỗi dữ liệu nhập không hợp lệ |
| `Path.read_text()/write_text()` | Đọc/ghi file với đường dẫn kiểu Path |

## 4. Khái niệm và ví dụ nhỏ

### 4.1. File I/O

Lấy hoặc lưu dữ liệu trên đĩa.

```python
from pathlib import Path
print(Path('x.csv').suffix)
```

### 4.2. CSV

Định dạng bảng dạng văn bản.

```python
import csv
print(csv.__name__)
```

### 4.3. Exception

Lỗi xuất hiện khi chạy chương trình.

```python
try:
    int('x')
except ValueError:
    print('Bad input')
```

### 4.4. Context manager

Tự đóng tài nguyên sau khối with.

```python
import io
with io.StringIO('abc') as f:print(f.read())
```

## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Đọc CSV sản phẩm

**Vấn đề:** Đọc CSV sản phẩm.

**Vì sao chọn cách giải?** DictReader dùng tiêu đề cột để tránh tráo giá và tên.

**Dữ liệu:** Hai sản phẩm với hai cột name,price.

```python
import csv,io
csv_text="name,price\nPen,10\nBook,35\n"
rows=list(csv.DictReader(io.StringIO(csv_text)))
print(rows[1]["name"])
```

### Tình huống 2 — Lưu nhật ký ứng dụng

**Vấn đề:** Lưu nhật ký ứng dụng.

**Vì sao chọn cách giải?** Quản lý tệp trong thư mục tạm để không để lại file học thử.

**Dữ liệu:** Một dòng log Started.

```python
from pathlib import Path
from tempfile import TemporaryDirectory
with TemporaryDirectory() as folder:
    p=Path(folder)/"log.txt"
    p.write_text("Started\n",encoding="utf-8")
    print(p.read_text(encoding="utf-8"))
```

### Tình huống 3 — Chặn nhập sai kiểu

**Vấn đề:** Chặn nhập sai kiểu.

**Vì sao chọn cách giải?** Chỉ bắt ValueError khi nhập không chuyển sang số được.

**Dữ liệu:** Dữ liệu đầu vào 'abc'.

```python
raw="abc"
try:
    number=int(raw)
except ValueError:
    number=None
print(number)
```

### Tình huống 4 — Xuất CSV báo cáo

**Vấn đề:** Xuất CSV báo cáo.

**Vì sao chọn cách giải?** DictWriter giữ thứ tự tên cột rõ ràng.

**Dữ liệu:** Ngày và doanh thu ví dụ.

```python
import csv,io
b=io.StringIO()
w=csv.DictWriter(b,fieldnames=["date","revenue"])
w.writeheader();w.writerow({"date":"2026-10-24","revenue":1200})
print(b.getvalue())
```

### Tình huống 5 — Báo lỗi file thiếu

**Vấn đề:** Báo lỗi file thiếu.

**Vì sao chọn cách giải?** Bắt FileNotFoundError để chương trình không dừng không rõ nguyên nhân.

**Dữ liệu:** Một tệp giả định không tồn tại.

```python
from pathlib import Path
try:
    text=Path("__missing_example__.csv").read_text()
except FileNotFoundError:
    text="File unavailable"
print(text)
```

## 6. Sai lầm thường gặp

- Cần chú ý thứ tự xử lý, kiểu dữ liệu và đơn vị đo. Trường hợp rỗng/thiếu dữ liệu phải có cách xử lý rõ ràng.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ


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
