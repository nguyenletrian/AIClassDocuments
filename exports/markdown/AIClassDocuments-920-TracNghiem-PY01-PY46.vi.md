# AIClassDocuments — Bộ 920 câu trắc nghiệm Python và AI

46 bài PY-01–PY-46 · Song ngữ Anh–Việt · Có đáp án và giải thích.

Nội dung được trích nguyên văn từ mục 7 của từng bài trên nhánh main, không viết lại câu hỏi hay đáp án.

## PY-01 — PY-01 — Biến, đầu vào và đầu ra trong Python

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a variable in Python? | Biến trong Python là gì?**

A. A name referring to a value | Tên tham chiếu đến một giá trị

B. Information produced by a program | Thông tin do chương trình tạo ra

C. Data received for processing | Dữ liệu được nhận để xử lý

D. How a value is represented and used | Cách biểu diễn và sử dụng một giá trị

**Đáp án: A**

**Giải thích:** Biến Python là tên được liên kết với đối tượng, chẳng hạn `age = 20`. Biến khác dữ liệu đầu vào hay kết quả in ra; dùng `age` sau đó sẽ truy cập giá trị đang được gán.

**Q2. What is program input? | Đầu vào chương trình là gì?**

A. Information produced by a program | Thông tin do chương trình tạo ra

B. How a value is represented and used | Cách biểu diễn và sử dụng một giá trị

C. A name referring to a value | Tên tham chiếu đến một giá trị

D. Data received for processing | Dữ liệu được nhận để xử lý

**Đáp án: D**

**Giải thích:** Đầu vào là dữ liệu chương trình nhận, ví dụ văn bản người dùng nhập cho `input()`. Chương trình có thể xử lý văn bản rồi tạo đầu ra; đầu vào không phải kết quả chương trình.

**Q3. What is program output? | Đầu ra chương trình là gì?**

A. How a value is represented and used | Cách biểu diễn và sử dụng một giá trị

B. Information produced by a program | Thông tin do chương trình tạo ra

C. Data received for processing | Dữ liệu được nhận để xử lý

D. A name referring to a value | Tên tham chiếu đến một giá trị

**Đáp án: B**

**Giải thích:** Đầu ra là thông tin chương trình đưa ra ngoài, ví dụ dòng chữ do `print(5)` hiển thị. Nó khác đầu vào do người dùng cung cấp và khác biến dùng để tham chiếu giá trị trong chương trình.

**Q4. What does a data type describe? | Kiểu dữ liệu mô tả điều gì?**

A. Information produced by a program | Thông tin do chương trình tạo ra

B. How a value is represented and used | Cách biểu diễn và sử dụng một giá trị

C. A name referring to a value | Tên tham chiếu đến một giá trị

D. Data received for processing | Dữ liệu được nhận để xử lý

**Đáp án: B**

**Giải thích:** Kiểu dữ liệu quyết định ý nghĩa giá trị và các phép toán phù hợp: `3` thuộc kiểu `int`, còn `'3'` thuộc `str`. Vì vậy `3 + 2` là phép cộng số, còn `'3' + '2'` nối văn bản.

**Q5. Which function prints a value? | Hàm nào in một giá trị?**

A. `int()` | `int()`

B. `type()` | `type()`

C. `input()` | `input()`

D. `print()` | `print()`

**Đáp án: D**

**Giải thích:** `print()` ghi biểu diễn của giá trị ra đầu ra chuẩn; chẳng hạn `print(5)` hiển thị `5`. Hàm này không nhận câu trả lời người dùng như `input()`.

**Q6. Which function reads keyboard input? | Hàm nào đọc dữ liệu bàn phím?**

A. `input()` | `input()`

B. `int()` | `int()`

C. `type()` | `type()`

D. `print()` | `print()`

**Đáp án: A**

**Giải thích:** `input()` nhận một dòng người dùng gõ và trả về văn bản không kèm ký tự xuống dòng cuối. Dù người dùng gõ `12`, kết quả vẫn là chuỗi `'12'`, không tự đổi thành số nguyên `12`.

**Q7. Which function finds a value's type? | Hàm nào kiểm tra kiểu giá trị?**

A. `input()` | `input()`

B. `print()` | `print()`

C. `type()` | `type()`

D. `int()` | `int()`

**Đáp án: C**

**Giải thích:** `type(value)` trả về lớp/kiểu của đối tượng: `type(3)` là `int` còn `type('3')` là `str`. Hàm kiểm tra kiểu chứ không chuyển đổi giá trị.

**Q8. Which function converts valid decimal digits to an integer? | Hàm nào đổi chuỗi chữ số hợp lệ thành số nguyên?**

A. `int()` | `int()`

B. `print()` | `print()`

C. `type()` | `type()`

D. `input()` | `input()`

**Đáp án: A**

**Giải thích:** `int()` phân tích chuỗi biểu diễn số nguyên hợp lệ nên `int('012')` cho số nguyên `12`; số 0 đầu không được giữ lại. Chuỗi `'12.5'` không phải chuỗi số nguyên thập phân hợp lệ và gây `ValueError`.

**Q9. Which type represents a count of whole items? | Kiểu nào biểu diễn số lượng món nguyên?**

A. `str` | `str`

B. `float` | `float`

C. `int` | `int`

D. `bool` | `bool`

**Đáp án: C**

**Giải thích:** `int` biểu diễn số lượng nguyên như 4 vé hoặc 0 lỗi, không có phần lẻ. `float` phù hợp số đo có thể có phần thập phân, không cần thiết cho số đếm các đơn vị nguyên vẹn.

**Q10. Which type suits a measurement with fractions? | Kiểu nào phù hợp với số đo có phần lẻ?**

A. `int` | `int`

B. `float` | `float`

C. `bool` | `bool`

D. `str` | `str`

**Đáp án: B**

**Giải thích:** `float` biểu diễn giá trị số có thể chứa phần lẻ, ví dụ 2,5 mét. Khác số đếm nguyên, số đo có thể nằm giữa hai số nguyên; số thập phân dạng dấu phẩy động đôi khi chỉ là xấp xỉ.

**Q11. Which type preserves a leading zero in an identifier? | Kiểu nào giữ số 0 đầu mã định danh?**

A. `str` | `str`

B. `bool` | `bool`

C. `float` | `float`

D. `int` | `int`

**Đáp án: A**

**Giải thích:** Mã định danh như `'007'` nên lưu bằng `str` vì mọi ký tự, kể cả hai số 0 đầu, đều có ý nghĩa. Đổi sang `int` được `7` và làm mất định dạng mã.

**Q12. Which type stores a true/false state? | Kiểu nào lưu trạng thái đúng/sai?**

A. `bool` | `bool`

B. `int` | `int`

C. `str` | `str`

D. `float` | `float`

**Đáp án: A**

**Giải thích:** `bool` có hai giá trị logic `True` và `False`, thích hợp biểu diễn trạng thái như có được phép truy cập hay không. Đây không phải kiểu đo lường số hay nhãn văn bản.

**Q13. What does `x = 5` do? | `x = 5` thực hiện điều gì?**

A. Tests whether `x` equals `5` | Kiểm tra `x` có bằng `5` không

B. Adds `5` to the old value of `x` | Cộng `5` vào giá trị cũ của `x`

C. Displays `5` without storing it | Hiển thị `5` mà không gán

D. Assigns the integer `5` to `x` | Gán số nguyên `5` cho `x`

**Đáp án: D**

**Giải thích:** Dấu bằng đơn gán tên `x` cho số nguyên `5`, không kiểm tra bằng nhau và cũng không cộng thêm số. Muốn so sánh `x` có bằng `5` thì dùng `x == 5`.

**Q14. What is the type of `input()`'s return value? | Giá trị trả về của `input()` có kiểu nào?**

A. An integer when only digits are typed | Số nguyên nếu chỉ nhập chữ số

B. A floating-point number by default | Số thực theo mặc định

C. A Boolean indicating whether input exists | Boolean cho biết có đầu vào hay không

D. A string, even if it contains digits | Chuỗi, kể cả khi chỉ chứa chữ số

**Đáp án: D**

**Giải thích:** `input()` luôn trả về `str` chứa nội dung được nhập, ví dụ `'42'`. Nếu cần tính toán số, hãy dùng `int(input())` hoặc phép đổi kiểu phù hợp khi đầu vào hợp lệ.

**Q15. What does `float('2.5')` produce? | `float('2.5')` tạo ra gì?**

A. The string `'2.5'` | Chuỗi `'2.5'`

B. The integer `2` | Số nguyên `2`

C. The floating-point number `2.5` | Số thực `2.5`

D. `ValueError` for any decimal point | `ValueError` nếu có dấu thập phân

**Đáp án: C**

**Giải thích:** `float('2.5')` chuyển văn bản `'2.5'` thành giá trị số thực `2.5`. Kết quả không còn là chuỗi có dấu nháy và không cắt phần lẻ thành số nguyên `2`.

**Q16. What does `int('abc')` raise? | `int('abc')` phát sinh gì?**

A. `TypeError` | `TypeError`

B. `ValueError` | `ValueError`

C. The integer `0` | Số nguyên `0`

D. `NameError` | `NameError`

**Đáp án: B**

**Giải thích:** `int('abc')` phát sinh `ValueError` vì các chữ cái không tạo thành số nguyên hệ mười hợp lệ. Hàm vẫn tồn tại và nhận được chuỗi, nên đây là lỗi giá trị chuyển đổi chứ không phải `NameError`.

**Q17. What does `print(2, 3)` display by default? | `print(2, 3)` mặc định hiển thị gì?**

A. `2,3` | `2,3`

B. `2 3` | `2 3`

C. `(2, 3)` | `(2, 3)`

D. `23` | `23`

**Đáp án: B**

**Giải thích:** Mặc định `print` ngăn cách các đối số bằng một dấu cách: `print(2, 3)` hiển thị `2 3`. Nó không dính hai số thành `23` và không in dạng tuple `(2, 3)`.

**Q18. If `x = 2` is followed by `x = 4` on the next line, what is the final value of `x`? | Nếu `x = 2` rồi `x = 4` ở dòng tiếp theo, giá trị cuối của `x` là gì?**

A. `ValueError` | `ValueError`

B. `2` | `2`

C. `4` | `4`

D. `6` | `6`

**Đáp án: C**

**Giải thích:** Lệnh đầu gán `x` bằng `2`, lệnh tiếp theo gán lại chính tên đó bằng `4`. Vì vậy giá trị cuối là `4`, không phải tổng `6` hay giá trị cũ `2`.

**Q19. Which Python type does `type(2.0)` identify? | `type(2.0)` xác định kiểu Python nào?**

A. `int` | `int`

B. `bool` | `bool`

C. `float` | `float`

D. `str` | `str`

**Đáp án: C**

**Giải thích:** Literal `2.0` là đối tượng số thực, nên `type(2.0)` xác định kiểu `float` (hiển thị `<class 'float'>`). Trong khi đó `type(2)` là `int`; dấu thập phân làm thay đổi kiểu literal.

**Q20. What does `print('Hi')` display? | `print('Hi')` hiển thị gì?**

A. `hi` | `hi`

B. `None` | `None`

C. `'Hi'` including the quotes | `'Hi'` gồm cả dấu nháy

D. `Hi` without quotes | `Hi` không có dấu nháy

**Đáp án: D**

**Giải thích:** Dấu nháy dùng để bao chuỗi trong mã nguồn chứ không phải ký tự thuộc nội dung chuỗi. Vì vậy `print('Hi')` hiển thị `Hi` rồi xuống dòng, không in dấu nháy hoặc chữ thường `hi`.

## PY-02 — PY-02 — Kiểu số, Boolean và chuỗi

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

## PY-03 — PY-03 — Toán tử số học, so sánh và logic

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. Which operator performs multiplication? | Toán tử nào thực hiện phép nhân?**

A. `*` | `*`

B. `&` | `&`

C. `==` | `==`

D. `and` | `and`

**Đáp án: A**

**Giải thích:** `*` nhân các số, ví dụ `3 * 4` cho `12`. `==` so sánh giá trị, `and` kết hợp điều kiện logic, còn `&` thực hiện AND theo bit trên số nguyên.

**Q2. Which operator tests equality? | Toán tử nào kiểm tra bằng nhau?**

A. `*` | `*`

B. `==` | `==`

C. `&` | `&`

D. `and` | `and`

**Đáp án: B**

**Giải thích:** `==` kiểm tra hai giá trị có bằng nhau và tạo Boolean, ví dụ `2 == 2` là `True`. Một dấu `=` dùng để gán giá trị cho tên, chứ không so sánh.

**Q3. Which Python keyword performs short-circuit logical AND? | Từ khóa Python nào thực hiện phép VÀ logic có đánh giá ngắn mạch?**

A. `==` | `==`

B. `&` | `&`

C. `and` | `and`

D. `*` | `*`

**Đáp án: C**

**Giải thích:** Từ khóa `and` thực hiện phép VÀ logic ngắn mạch: nếu vế trái sai, Python không đánh giá vế phải. Ký hiệu `&` thực hiện AND theo bit trên số nguyên và kể cả dùng với Boolean cũng không đánh giá ngắn mạch.

**Q4. Which operator performs bitwise AND on integers? | Toán tử nào thực hiện AND theo bit trên số nguyên?**

A. `and` | `and`

B. `==` | `==`

C. `*` | `*`

D. `&` | `&`

**Đáp án: D**

**Giải thích:** Với số nguyên, `&` thực hiện AND trên từng bit: `5 & 3` đối chiếu `0101` và `0011`, được `0001` (`1`). Đây không phải phép nhân thông thường hay từ khóa logic `and`.

**Q5. What does `7 // 2` return? | `7 // 2` trả về gì?**

A. `1` | `1`

B. `3.5` | `3.5`

C. `3` | `3`

D. `8` | `8`

**Đáp án: C**

**Giải thích:** `//` thực hiện chia lấy sàn: `7 / 2` bằng `3.5`, làm tròn xuống được `3`. Với thương âm, làm tròn xuống nghĩa là về âm vô cực nên `-7 // 2` bằng `-4`.

**Q6. What does `7 % 2` return? | `7 % 2` trả về gì?**

A. `1` | `1`

B. `3.5` | `3.5`

C. `3` | `3`

D. `8` | `8`

**Đáp án: A**

**Giải thích:** `%` trả phần dư theo phép chia lấy sàn: `7 = 2 * 3 + 1`, nên `7 % 2` bằng `1`. Nó không phải thương `3` hay kết quả chia thực `3.5`.

**Q7. What does `2 ** 3` return? | `2 ** 3` trả về gì?**

A. `3` | `3`

B. `1` | `1`

C. `3.5` | `3.5`

D. `8` | `8`

**Đáp án: D**

**Giải thích:** `**` là phép lũy thừa: `2 ** 3` nhân 2 với chính nó ba lần, cho `8`. Một dấu `*` là phép nhân, còn `^` trong Python là XOR theo bit, không phải lũy thừa.

**Q8. What does `7 / 2` return? | `7 / 2` trả về gì?**

A. `3.5` | `3.5`

B. `3` | `3`

C. `1` | `1`

D. `8` | `8`

**Đáp án: A**

**Giải thích:** Trong Python 3, `/` chia thực nên `7 / 2` trả về số thực `3.5`. Toán tử `//` lấy sàn thương được `3`, còn `%` trả phần dư `1`.

**Q9. What is `True and False`? | `True and False` bằng gì?**

A. `True` (Boolean) | `True` (Boolean)

B. `None` | `None`

C. `0` (integer) | `0` (số nguyên)

D. `False` (Boolean) | `False` (Boolean)

**Đáp án: D**

**Giải thích:** `and` Boolean yêu cầu cả hai vế đều đúng, nhưng vế thứ hai là `False`. Vì thế `True and False` cho Boolean `False`, không phải số nguyên `0` hay `None`.

**Q10. What is `False or True`? | `False or True` bằng gì?**

A. `1` (integer) | `1` (số nguyên)

B. `True` (Boolean) | `True` (Boolean)

C. `False` (Boolean) | `False` (Boolean)

D. `None` | `None`

**Đáp án: B**

**Giải thích:** `or` Boolean đúng nếu có ít nhất một vế đúng; vế phải của `False or True` là `True`. Kết quả ở đây là Boolean `True`, không phải số nguyên `1`, dù `True` có thể hoạt động như 1 trong một số phép số học.

**Q11. What does `not True` produce? | `not True` cho kết quả gì?**

A. `0` (integer) | `0` (số nguyên)

B. `None` | `None`

C. `False` (Boolean) | `False` (Boolean)

D. `True` (Boolean) | `True` (Boolean)

**Đáp án: C**

**Giải thích:** `not` đảo giá trị logic nên `not True` thành Boolean `False`. Ngược lại `not False` là `True`; số nguyên không là giá trị thuộc kiểu khác.

**Q12. What does `5 & 3` produce? | `5 & 3` tạo ra gì?**

A. `False` (Boolean) | `False` (Boolean)

B. `5` (integer) | `5` (số nguyên)

C. `True` (Boolean) | `True` (Boolean)

D. `1` (integer) | `1` (số nguyên)

**Đáp án: D**

**Giải thích:** Hai số nguyên là `5 = 0101` và `3 = 0011` ở hệ nhị phân bốn bit. Toán tử `&` chỉ giữ vị trí có cả hai bit bằng 1, cho `0001`, tức số nguyên `1`, không phải Boolean `True`.

**Q13. Which operator tests that two values differ? | Toán tử nào kiểm tra hai giá trị khác nhau?**

A. `!=` | `!=`

B. `>=` | `>=`

C. `=` | `=`

D. `in` | `in`

**Đáp án: A**

**Giải thích:** `!=` kiểm tra hai giá trị có khác nhau: `3 != 4` là `True`, còn `3 != 3` là `False`. Nó đối lập với `==` dùng để kiểm tra bằng nhau.

**Q14. Which operator means 'at least'? | Toán tử nào biểu diễn 'lớn hơn hoặc bằng'?**

A. `!=` | `!=`

B. `in` | `in`

C. `>=` | `>=`

D. `=` | `=`

**Đáp án: C**

**Giải thích:** `>=` nghĩa là lớn hơn hoặc bằng, nên `5 >= 5` và `6 >= 5` đều là `True`. Trường hợp bằng ngưỡng rất quan trọng: dùng `>` sẽ loại đúng giá trị 5.

**Q15. Which operator checks membership in a collection? | Toán tử nào kiểm tra phần tử thuộc một tập dữ liệu?**

A. `!=` | `!=`

B. `in` | `in`

C. `>=` | `>=`

D. `=` | `=`

**Đáp án: B**

**Giải thích:** Toán tử `in` kiểm tra phần tử có thuộc tập hợp: `2 in [1, 2, 3]` là `True`, còn `4 in [1, 2, 3]` là `False`. Nó không gán giá trị hay so sánh độ lớn.

**Q16. Which operator assigns a new value to a variable? | Toán tử nào gán giá trị mới cho biến?**

A. `>=` | `>=`

B. `!=` | `!=`

C. `=` | `=`

D. `in` | `in`

**Đáp án: C**

**Giải thích:** Toán tử gán `=` liên kết tên với giá trị, như `total = 10`. Muốn so sánh hai giá trị thì dùng `==`; dùng `=` trong điều kiện so sánh thông thường sẽ sai cú pháp.

**Q17. Which result comes from `3 > 5`? | `3 > 5` trả về gì?**

A. `0` (integer) | `0` (số nguyên)

B. `False` (Boolean) | `False` (Boolean)

C. `True` (Boolean) | `True` (Boolean)

D. `None` | `None`

**Đáp án: B**

**Giải thích:** `>` kiểm tra lớn hơn nghiêm ngặt, mà 3 nhỏ hơn 5 nên `3 > 5` cho Boolean `False`. Kết quả là giá trị logic, không phải số nguyên `0`.

**Q18. What result comes from `2 + 3 * 4`? | `2 + 3 * 4` bằng bao nhiêu?**

A. `9` | `9`

B. `14` | `14`

C. `False` | `False`

D. `20` | `20`

**Đáp án: B**

**Giải thích:** Phép nhân có độ ưu tiên cao hơn cộng: tính `3 * 4 = 12` trước, rồi `2 + 12 = 14`. Thêm ngoặc như `(2 + 3) * 4` sẽ đổi kết quả thành `20`.

**Q19. What does `True or False` return? | `True or False` trả về gì?**

A. `True` (Boolean) | `True` (Boolean)

B. `1` (integer) | `1` (số nguyên)

C. `False` (Boolean) | `False` (Boolean)

D. `None` | `None`

**Đáp án: A**

**Giải thích:** `or` đúng khi ít nhất một toán hạng Boolean đúng; vì vế trái là `True` nên `True or False` trả `True`. Với đầu vào Boolean, đây là Boolean `True`, không phải số nguyên `1`.

**Q20. What does `5 ^ 3` return for integers? | `5 ^ 3` trả về gì với số nguyên?**

A. `5` | `5`

B. `2` | `2`

C. `15` | `15`

D. `6` | `6`

**Đáp án: D**

**Giải thích:** `^` là XOR theo bit, không phải lũy thừa: `5 = 0101` và `3 = 0011` khác nhau tại các vị trí bit `0100` và `0010`, cho `0110` = `6`. Lũy thừa phải dùng `**`, không dùng `^`.

## PY-04 — PY-04 — Câu lệnh điều kiện if, elif, else

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What does `if` do? | `if` dùng để làm gì?**

A. Always runs every conditional branch | Luôn chạy mọi nhánh điều kiện

B. Runs its body only when the condition is false | Chỉ chạy thân khối khi điều kiện sai

C. Runs its body once regardless of the condition | Luôn chạy thân khối một lần bất kể điều kiện

D. Runs its indented body when the condition is true | Chạy thân khối thụt lề khi điều kiện đúng

**Đáp án: D**

**Giải thích:** `if` đánh giá điều kiện rồi chỉ chạy thân khối được thụt lề nếu điều kiện có giá trị đúng. Ví dụ với `x = 5`, `if x > 3:` sẽ chạy thân khối; không bắt buộc phải có `else`.

**Q2. When is an `elif` condition checked? | Khi nào Python xét điều kiện `elif`?**

A. Even after a preceding branch has matched | Kể cả khi nhánh trước đã đúng

B. Before the preceding `if` is checked | Trước khi kiểm tra `if` đứng trước

C. After `else` has executed | Sau khi `else` chạy

D. Only if earlier branches in the same chain did not match | Chỉ khi các nhánh trước trong cùng chuỗi không khớp

**Đáp án: D**

**Giải thích:** Python chỉ xét `elif` khi những điều kiện `if` hoặc `elif` đứng trước trong cùng chuỗi đều không khớp. Khi một nhánh trước đã đúng, các `elif` sau không được kiểm tra, nên không có nhiều nhánh cùng chạy.

**Q3. When does an `else` block run? | Khi nào khối `else` chạy?**

A. Every time the initial `if` is true | Mỗi khi `if` đầu tiên đúng

B. After any successful `elif` branch | Sau bất kỳ nhánh `elif` nào đúng

C. When no earlier condition in its chain was true | Khi mọi điều kiện trước trong cùng chuỗi đều sai

D. Only when a program raises an error | Chỉ khi chương trình phát sinh lỗi

**Đáp án: C**

**Giải thích:** `else` là nhánh dự phòng không có điều kiện riêng. Nó chỉ chạy khi mọi điều kiện `if` hoặc `elif` đứng trước trong cùng chuỗi đều sai, không chạy sau nhánh đã khớp.

**Q4. What is a nested `if`? | `if` lồng nhau là gì?**

A. An `if` statement inside another conditional block | Một lệnh `if` bên trong khối điều kiện khác

B. A condition joined by `and` | Điều kiện kết hợp bởi `and`

C. An `else` branch following `if` | Nhánh `else` theo sau `if`

D. Two `if` statements at the same indentation level | Hai lệnh `if` có cùng mức thụt lề

**Đáp án: A**

**Giải thích:** `if` lồng nhau là câu lệnh điều kiện nằm trong thân một câu lệnh điều kiện khác nên điều kiện trong chỉ được xét khi chương trình đi vào khối đó. Nó khác hai câu `if` độc lập, vốn có thể cùng chạy.

**Q5. Which keyword introduces another conditional test? | Từ khóa nào bổ sung một điều kiện tiếp theo?**

A. `if` | `if`

B. `else` | `else`

C. `elif` | `elif`

D. `in` | `in`

**Đáp án: C**

**Giải thích:** `elif` mở thêm một nhánh có điều kiện nối với `if` trước đó. Khác `else`, nhánh này có điều kiện riêng, ví dụ `elif score >= 80:`.

**Q6. Which keyword gives an unconditional fallback branch? | Từ khóa nào tạo nhánh còn lại không cần điều kiện?**

A. `in` | `in`

B. `elif` | `elif`

C. `if` | `if`

D. `else` | `else`

**Đáp án: D**

**Giải thích:** `else` là nhánh dự phòng không ghi điều kiện trong chuỗi `if/elif/else`; Python chỉ vào đó khi các điều kiện trước sai. Không thể viết `else condition:` vì `else` không nhận điều kiện.

**Q7. Which keyword starts a conditional branch? | Từ khóa nào bắt đầu một nhánh điều kiện?**

A. `else` | `else`

B. `if` | `if`

C. `elif` | `elif`

D. `in` | `in`

**Đáp án: B**

**Giải thích:** Nhánh điều kiện đầu tiên dùng `if`, tiếp theo là biểu thức và dấu hai chấm. `elif` chỉ có thể nối sau một `if` trước đó, không tự mở đầu chuỗi mới.

**Q8. Which operator asks whether an item belongs to a list? | Toán tử nào kiểm tra phần tử có trong List?**

A. `if` | `if`

B. `elif` | `elif`

C. `in` | `in`

D. `else` | `else`

**Đáp án: C**

**Giải thích:** `in` kiểm tra phần tử thuộc tập hợp: `3 in [1, 3]` là `True`. Trong khi đó `if`, `elif`, `else` là từ khóa điều khiển luồng, không phải toán tử kiểm tra phần tử.

**Q9. What does `score >= 80` include? | Điều kiện `score >= 80` bao gồm gì?**

A. Only the score exactly equal to 80 | Chỉ điểm đúng bằng 80

B. Every score of at least 80, including 80 | Mọi điểm từ 80 trở lên, kể cả 80

C. Only scores strictly above 80 | Chỉ điểm lớn hơn 80

D. Scores below 80 | Điểm thấp hơn 80

**Đáp án: B**

**Giải thích:** `>=` bao gồm chính giá trị ngưỡng, nên `score >= 80` đúng với 80, 81 và các giá trị lớn hơn. Dùng so sánh nghiêm ngặt `score > 80` sẽ loại đúng điểm 80.

**Q10. What is the difference between `=` and `==`? | Dấu `=` khác `==` ra sao?**

A. `=` assigns; `==` compares equality | `=` để gán; `==` so sánh bằng nhau

B. `=` compares; `==` assigns | `=` để so sánh; `==` để gán

C. Both operators assign variables | Cả hai toán tử đều dùng gán biến

D. Both operators compare equality | Cả hai toán tử so sánh bằng nhau

**Đáp án: A**

**Giải thích:** `=` gán giá trị như `score = 80`, còn `==` so sánh và trả Boolean như `score == 80`. Không thể thay hai toán tử cho nhau trong điều kiện `if`.

**Q11. What defines the body of an `if` in Python? | Điều gì xác định thân khối `if` trong Python?**

A. The indentation of following statements | Mức thụt lề của các câu lệnh theo sau

B. The number of printed statements | Số câu lệnh in ra

C. The order of imported libraries | Thứ tự thư viện được nhập

D. The variable name in the condition | Tên biến trong điều kiện

**Đáp án: A**

**Giải thích:** Thụt lề xác định câu lệnh nào thuộc thân `if`, thông thường bốn dấu cách cho mỗi cấp. Dấu hai chấm kết thúc dòng điều kiện, còn các dòng thụt lề đúng sau đó mới nằm trong nhánh.

**Q12. How are cases checked in an `if/elif` chain? | Các trường hợp được xét theo thứ tự nào trong chuỗi `if/elif`?**

A. All branches run concurrently | Mọi nhánh chạy đồng thời

B. Top to bottom, stopping after the first match | Từ trên xuống, dừng tại nhánh đúng đầu tiên

C. From the last `elif` upward | Từ `elif` cuối lên trên

D. By whichever condition is cheapest | Theo điều kiện tốn ít tính toán nhất

**Đáp án: B**

**Giải thích:** Python xét nhánh từ trên xuống và chạy nhánh đầu tiên có điều kiện đúng. Nếu điểm 95 cũng thỏa `>= 80`, đặt `>= 80` trước `>= 90` sẽ chọn mức điểm thấp hơn quá sớm.

**Q13. What does `True and False` evaluate to? | `True and False` bằng gì?**

A. `0` (integer) | `0` (số nguyên)

B. `True` (Boolean) | `True` (Boolean)

C. `None` | `None`

D. `False` (Boolean) | `False` (Boolean)

**Đáp án: D**

**Giải thích:** `and` với hai toán hạng Boolean chỉ trả `True` khi cả hai đều `True`. Vì vế thứ hai là `False`, `True and False` cho Boolean `False`, không phải số nguyên `0`.

**Q14. What does `True or False` evaluate to? | `True or False` bằng gì?**

A. `None` | `None`

B. `1` (integer) | `1` (số nguyên)

C. `True` (Boolean) | `True` (Boolean)

D. `False` (Boolean) | `False` (Boolean)

**Đáp án: C**

**Giải thích:** `or` với toán hạng Boolean chỉ cần một vế đúng; vế trái là `True` nên `True or False` cho Boolean `True`. Kết quả không cùng kiểu với số nguyên `1`.

**Q15. What does `not True` evaluate to? | `not True` bằng gì?**

A. `0` (integer) | `0` (số nguyên)

B. `True` (Boolean) | `True` (Boolean)

C. `None` | `None`

D. `False` (Boolean) | `False` (Boolean)

**Đáp án: D**

**Giải thích:** `not` đảo giá trị logic của toán hạng, nên `not True` cho Boolean `False`. Số nguyên `0` cũng được xem là sai trong điều kiện nhưng không phải giá trị trả về ở đây.

**Q16. What does `5 % 2 == 0` evaluate to? | `5 % 2 == 0` có kết quả gì?**

A. `False` (Boolean) | `False` (Boolean)

B. `None` | `None`

C. `0` (integer) | `0` (số nguyên)

D. `True` (Boolean) | `True` (Boolean)

**Đáp án: A**

**Giải thích:** Phần dư `5 % 2` là `1`; vì vậy so sánh `1 == 0` là sai. Toàn bộ biểu thức trả về Boolean `False`, nghĩa là 5 không phải số chẵn.

**Q17. How many branches run in one `if/elif/else` chain? | Có bao nhiêu nhánh chạy trong một chuỗi `if/elif/else`?**

A. Every branch whose condition is true | Mọi nhánh có điều kiện đúng

B. Every `elif` plus `else` | Mọi nhánh `elif` và `else`

C. At most one branch, possibly none without `else` | Tối đa một nhánh, có thể không nhánh nào nếu thiếu `else`

D. Exactly two branches always | Luôn đúng hai nhánh

**Đáp án: C**

**Giải thích:** Trong một chuỗi `if/elif/else`, chương trình chạy tối đa một nhánh: nhánh đúng đầu tiên hoặc `else` khi không nhánh nào đúng. Nếu không có `else` và mọi điều kiện đều sai thì không nhánh nào chạy.

**Q18. What happens if an `if` condition is false and there is no `else`? | Nếu `if` sai và không có `else` thì sao?**

A. The body runs once regardless | Thân nhánh vẫn chạy một lần

B. The body is skipped and execution continues | Bỏ qua thân nhánh và tiếp tục chương trình

C. A `SyntaxError` is raised | Phát sinh `SyntaxError`

D. Python inserts and runs an implicit `else` | Python tự chèn và chạy `else`

**Đáp án: B**

**Giải thích:** Khi điều kiện `if` sai, thân nhánh đó được bỏ qua. Nếu không có `else`, chương trình tiếp tục sau khối điều kiện; đây là Python hợp lệ, không phải lỗi cú pháp.

**Q19. How can two conditions both be required for access? | Cách nào yêu cầu đồng thời hai điều kiện để cho phép truy cập?**

A. Use `==` alone | Chỉ dùng `==`

B. Use `and` | Dùng `and`

C. Use `or` | Dùng `or`

D. Use `not` | Dùng `not`

**Đáp án: B**

**Giải thích:** Phép `and` bắt buộc đồng thời hai điều kiện như `has_ticket and age >= 18`. Dùng `or` sẽ chấp nhận người chỉ thỏa một điều kiện, nên không đảm bảo đủ cả hai yêu cầu.

**Q20. In one `if/elif` grade chain, which order correctly tests `score >= 90`, `score >= 80`, and `score >= 70` to select the highest applicable grade? | Trong một chuỗi `if/elif` phân loại điểm, cần xét `score >= 90`, `score >= 80`, `score >= 70` theo thứ tự nào để chọn mức cao nhất phù hợp?**

A. Test `>= 90`, then `>= 80`, then `>= 70` | Xét `>= 90`, rồi `>= 80`, rồi `>= 70`

B. Write independent `if` statements to select a single grade | Viết các `if` độc lập để chọn duy nhất một nhóm

C. Test `>= 70` before `>= 90` | Xét `>= 70` trước `>= 90`

D. Use any order because all matches run | Thứ tự tùy ý vì mọi nhánh đúng đều chạy

**Đáp án: A**

**Giải thích:** Chuỗi điều kiện chọn nhánh đúng đầu tiên; hãy xét ngưỡng điểm cao nhất trước, ví dụ `>= 90`, rồi `>= 80`, `>= 70`. Nếu bắt đầu từ `>= 70`, điểm 95 sẽ bị xếp nhóm quá sớm.

## PY-05 — PY-05 — Vòng lặp for, while, break và continue

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What does a `for` loop normally iterate over? | Vòng `for` thường duyệt qua gì?**

A. Only dictionary keys | Chỉ khóa của dictionary

B. Successive items from an iterable | Các phần tử liên tiếp của đối tượng duyệt được

C. Only a Boolean condition | Chỉ một điều kiện Boolean

D. Always index-value pairs | Luôn là cặp chỉ số-giá trị

**Đáp án: B**

**Giải thích:** Vòng `for` lần lượt lấy phần tử từ đối tượng duyệt được, ví dụ các giá trị `0`, `1`, `2` của `range(3)`. Cách hoạt động này khác `while` kiểm tra lại điều kiện ở mỗi lượt.

**Q2. When does a `while` loop repeat? | Khi nào vòng `while` tiếp tục lặp?**

A. Always for a predetermined count | Luôn theo số lượt đã xác định

B. Until exactly one iteration has completed | Chỉ đến khi chạy xong đúng một lượt

C. As long as its condition remains true | Chừng nào điều kiện vẫn đúng

D. Only when iterating over a list | Chỉ khi duyệt một list

**Đáp án: C**

**Giải thích:** Vòng `while` kiểm tra điều kiện trước mỗi lượt và chỉ lặp khi điều kiện còn đúng. Ví dụ `while n < 3:` dừng khi `n` đạt 3 nếu thân vòng lặp tăng `n` sau mỗi lượt.

**Q3. What is an iteration? | Một lần lặp là gì?**

A. A Boolean test before the loop | Phép kiểm tra Boolean trước vòng lặp

B. Two loops inside each other | Hai vòng lặp lồng nhau

C. One pass through the loop body | Một lượt thực hiện thân vòng lặp

D. A collection that can be iterated | Một tập hợp có thể duyệt

**Đáp án: C**

**Giải thích:** Một lần lặp là một lượt chạy thân vòng lặp. Với `for x in range(3):`, thân vòng lặp chạy ba lần, lần lượt `x` bằng 0, 1, 2.

**Q4. What are nested loops? | Vòng lặp lồng nhau là gì?**

A. A loop that runs exactly once | Một vòng chỉ chạy đúng một lần

B. Two loops written one after another | Hai vòng lặp viết nối tiếp nhau

C. A `for` and `while` with the same variable | `for` và `while` dùng cùng một biến

D. A loop placed inside another loop's body | Một vòng đặt trong thân vòng khác

**Đáp án: D**

**Giải thích:** Vòng lặp lồng nhau đặt một vòng trong thân vòng khác. Nếu vòng ngoài có 2 phần tử và vòng trong có 3 phần tử, thân vòng trong có thể chạy 2 nhân 3 bằng 6 lần, ứng với từng cặp kết hợp.

**Q5. What does `break` do inside a loop? | `break` làm gì trong vòng lặp?**

A. Skips only the current iteration's remaining statements | Chỉ bỏ qua các lệnh còn lại của lượt hiện tại

B. Does nothing and continues with the next statement | Không làm gì rồi chạy lệnh tiếp

C. Immediately exits the entire Python process | Thoát toàn bộ tiến trình Python

D. Immediately exits the innermost enclosing loop | Thoát ngay vòng lặp bao gần nhất

**Đáp án: D**

**Giải thích:** `break` kết thúc ngay vòng lặp bao gần nhất đang chạy. Với vòng lặp lồng nhau, nó không tự kết thúc mọi vòng ngoài; `continue` thì vẫn để vòng lặp tiếp tục.

**Q6. What does `continue` do? | `continue` có tác dụng gì?**

A. Skips the remaining body and moves toward the next iteration | Bỏ phần thân còn lại và chuyển tới lượt kế tiếp

B. Restarts the complete program | Khởi động lại toàn bộ chương trình

C. Exits the current loop completely | Kết thúc hẳn vòng lặp hiện tại

D. Acts as a no-op placeholder | Là câu lệnh giữ chỗ không thao tác

**Đáp án: A**

**Giải thích:** `continue` bỏ qua những câu lệnh còn lại trong lượt hiện tại rồi tiếp tục theo loại vòng lặp. Với `for`, chương trình lấy phần tử kế tiếp; với `while`, nó kiểm tra lại điều kiện.

**Q7. What does `pass` do? | `pass` làm gì?**

A. Skips the remainder of the iteration | Bỏ phần còn lại của lượt lặp

B. Rechecks the condition without running later statements | Kiểm tra lại điều kiện mà bỏ qua các lệnh sau

C. Performs no operation and then continues normally | Không thao tác gì rồi tiếp tục bình thường

D. Leaves the loop | Rời khỏi vòng lặp

**Đáp án: C**

**Giải thích:** `pass` là câu lệnh hợp lệ nhưng không làm gì, hữu ích để giữ chỗ cho thân khối bắt buộc. Khác `continue`, nó không bỏ qua những câu lệnh phía sau trong cùng lượt lặp.

**Q8. When does a loop's `else` execute? | `else` của vòng lặp chạy khi nào?**

A. Every time a loop body executes | Mỗi khi thân vòng lặp chạy

B. When the loop finishes normally without `break` | Khi vòng lặp kết thúc bình thường mà không gặp `break`

C. Only when `break` was executed | Chỉ khi đã chạy `break`

D. At the start of the first iteration | Khi bắt đầu lượt lặp đầu

**Đáp án: B**

**Giải thích:** `else` của vòng lặp chạy sau khi vòng lặp kết thúc bình thường: `for` duyệt hết phần tử hoặc điều kiện `while` thành sai. Nó bị bỏ qua nếu `break` kết thúc vòng lặp, khác `else` dự phòng của `if`.

**Q9. What does `range(1, 4)` represent? | `range(1, 4)` biểu diễn gì?**

A. Values 1, 2, 3 | Các giá trị 1, 2, 3

B. Values 1, 2, 3, 4 | Các giá trị 1, 2, 3, 4

C. Values 1, 3 | Các giá trị 1, 3

D. Values 0, 1, 2, 3 | Các giá trị 0, 1, 2, 3

**Đáp án: A**

**Giải thích:** `range(1, 4)` biểu diễn các số 1, 2, 3 vì mốc dừng 4 không được lấy. Nếu muốn bao gồm 4, cần đặt mốc dừng là 5.

**Q10. What does `enumerate(items)` provide? | `enumerate(items)` cung cấp gì?**

A. Pairs sorted by item value | Các cặp được sắp theo giá trị

B. Pairs of index and item | Các cặp chỉ số và phần tử

C. Only the items, without their indexes | Chỉ các phần tử, không kèm chỉ số

D. Only the indexes, without items | Chỉ chỉ số, không kèm phần tử

**Đáp án: B**

**Giải thích:** `enumerate(items)` tạo các cặp chỉ số và phần tử, mặc định bắt đầu từ chỉ số 0. Với `['a', 'b']`, khi duyệt sẽ nhận `(0, 'a')` rồi `(1, 'b')`; hàm không sắp xếp danh sách.

**Q11. What does `zip(a, b)` do? | `zip(a, b)` làm gì?**

A. Pairs elements at corresponding positions | Ghép phần tử ở cùng vị trí

B. Concatenates both inputs into one sequence | Nối hai đầu vào thành một dãy

C. Sorts the inputs together | Sắp xếp hai đầu vào cùng nhau

D. Generates every possible pair | Tạo mọi cặp kết hợp

**Đáp án: A**

**Giải thích:** `zip(a, b)` ghép phần tử ở cùng vị trí, ví dụ `list(zip([1, 2], ['x', 'y']))` cho `[(1, 'x'), (2, 'y')]`. Mặc định hàm dừng khi dãy ngắn nhất hết phần tử, chứ không tạo mọi cặp kết hợp.

**Q12. What does `reversed(items)` provide for a sequence? | `reversed(items)` cung cấp gì cho một dãy?**

A. Always returns a fully materialized list | Luôn trả về list đã tạo sẵn

B. Provides an iterator in reverse positional order | Cung cấp iterator theo thứ tự vị trí đảo ngược

C. Sorts elements from largest to smallest | Sắp phần tử từ lớn đến nhỏ

D. Preserves the original order | Giữ nguyên thứ tự ban đầu

**Đáp án: B**

**Giải thích:** `reversed()` cung cấp bộ duyệt ngược thứ tự vị trí của dãy phù hợp. Với `[3, 1, 2]`, nó cho `2, 1, 3`, không phải sắp xếp số giảm dần `3, 2, 1`.

**Q13. How many iterations does a complete `for` loop over `range(3)` execute? | Vòng `for` duyệt hết `range(3)` thực hiện bao nhiêu lượt lặp?**

A. 3 iterations | 3 lượt lặp

B. 4 iterations | 4 lượt lặp

C. 0 iterations | 0 lượt lặp

D. 2 iterations | 2 lượt lặp

**Đáp án: A**

**Giải thích:** `range(3)` tạo các giá trị `0`, `1`, `2`: bắt đầu mặc định từ 0 và không lấy mốc dừng 3. Vòng `for` duyệt hết sẽ chạy thân đúng ba lượt; đây là số lượt lặp, không có nghĩa dãy chứa giá trị 3.

**Q14. What does `range(2, 7, 2)` yield? | `range(2, 7, 2)` cho những số nào?**

A. 3, 5 | 3, 5

B. 2, 4, 6 | 2, 4, 6

C. 2, 3, 4, 5, 6 | 2, 3, 4, 5, 6

D. 2, 4, 6, 8 | 2, 4, 6, 8

**Đáp án: B**

**Giải thích:** `range(start, stop, step)` bắt đầu tại 2, mỗi lượt cộng thêm 2 và không lấy giá trị đạt hoặc vượt mốc dừng 7. Vì vậy dãy là 2, 4, 6, không phải 2, 4, 6, 8.

**Q15. What does `enumerate(['a','b'])` start indexing from? | `enumerate(['a','b'])` bắt đầu chỉ số từ đâu?**

A. The number of items | Số phần tử

B. -1 | -1

C. 0 | 0

D. 1 | 1

**Đáp án: C**

**Giải thích:** `enumerate()` mặc định bắt đầu chỉ số bằng `0` nếu không truyền `start`. Với `['a', 'b']`, cặp đầu là `(0, 'a')`; `enumerate(items, start=1)` mới bắt đầu từ 1.

**Q16. What does `list(zip([1,2], ['a']))` contain? | `list(zip([1,2], ['a']))` gồm gì?**

A. `[(1, 'a'), (2, 'a')]` | `[(1, 'a'), (2, 'a')]`

B. `[(1, 2), ('a',)]` | `[(1, 2), ('a',)]`

C. `[(1, 'a'), (2, None)]` | `[(1, 'a'), (2, None)]`

D. `[(1, 'a')]` | `[(1, 'a')]`

**Đáp án: D**

**Giải thích:** `zip()` lấy một phần tử từ mỗi dãy ở một lượt và dừng khi dãy ngắn hơn hết. Vì vậy `list(zip([1,2], ['a']))` chỉ chứa `[(1, 'a')]`, không có cặp chứa 2.

**Q17. What is a common cause of an infinite `while` loop? | Nguyên nhân thường gặp khiến `while` lặp vô hạn là gì?**

A. A function containing `pass` is never called | Một hàm có `pass` không được gọi

B. A `break` is reached in the first iteration | Gặp `break` ở lượt đầu

C. A `for` loop exhausts a finite iterable | `for` duyệt hết một dãy hữu hạn

D. The `while` condition stays true and no exit is reached | Điều kiện `while` luôn đúng và không gặp lối thoát

**Đáp án: D**

**Giải thích:** Vòng `while` có thể lặp vô hạn khi điều kiện luôn đúng, ví dụ `while n < 3:` không bao giờ thay đổi `n` và không gặp `break`. Cần cập nhật biến hướng tới điều kiện sai hoặc chủ động có lối thoát.

**Q18. How can a loop ignore invalid data and continue processing? | Làm sao bỏ qua dữ liệu lỗi nhưng vẫn xử lý phần tử sau?**

A. Use `continue` for that invalid item | Dùng `continue` với phần tử lỗi

B. Use `return` to exit the whole function | Dùng `return` thoát toàn bộ hàm

C. Use only `pass` in the invalid-data branch | Chỉ dùng `pass` trong nhánh dữ liệu lỗi

D. Use `break` when the invalid item appears | Dùng `break` khi gặp phần tử lỗi

**Đáp án: A**

**Giải thích:** Dùng `continue` khi cần bỏ qua một phần tử không hợp lệ nhưng vẫn xử lý các phần tử sau. `break` sẽ kết thúc vòng lặp, còn chỉ dùng `pass` không ngăn những lệnh phía sau xử lý phần tử lỗi.

**Q19. How can a search stop immediately after a match? | Làm sao dừng tìm kiếm ngay khi đã thấy phần tử phù hợp?**

A. Use `pass` after the match | Dùng `pass` sau khi khớp

B. Use `continue` after the match | Dùng `continue` sau khi khớp

C. Use `else` instead of checking | Dùng `else` thay kiểm tra

D. Use `break` after the match | Dùng `break` sau khi khớp

**Đáp án: D**

**Giải thích:** Dùng `break` ngay khi tìm thấy phần tử cần tìm vì không cần kiểm tra những phần tử còn lại. `continue` chỉ chuyển tới phần tử tiếp theo, còn `pass` không dừng việc tìm kiếm.

**Q20. How do you traverse every combination of two small collections? | Làm sao duyệt mọi kết hợp của hai nhóm nhỏ?**

A. Use `enumerate()` on one collection | Dùng `enumerate()` trên một nhóm

B. Use two separate, nonnested loops | Dùng hai vòng độc lập không lồng nhau

C. Use one loop nested inside the other | Đặt một vòng lồng bên trong vòng còn lại

D. Use `zip()` on the two collections | Dùng `zip()` trên hai nhóm

**Đáp án: C**

**Giải thích:** Muốn duyệt mọi cặp kết hợp của hai nhóm, đặt vòng duyệt nhóm thứ hai bên trong vòng duyệt nhóm thứ nhất. Với 2 phần tử ngoài và 3 phần tử trong, ta được 6 cặp; `zip()` chỉ ghép phần tử cùng vị trí.

## PY-06 — PY-06 — List, chỉ số, cắt danh sách và sắp xếp

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a Python List? | List trong Python là gì?**

A. A mapping of keys to values | Ánh xạ từ khóa sang giá trị

B. An ordered, mutable collection | Tập hợp có thứ tự và có thể sửa

C. An unordered collection of unique items | Tập hợp không thứ tự gồm phần tử duy nhất

D. An immutable sequence of items | Dãy phần tử bất biến

**Đáp án: B**

**Giải thích:** List trong Python là tập hợp có thứ tự và có thể thay đổi, nên mỗi phần tử có vị trí và có thể được sửa sau khi tạo. Ví dụ `[10, 20]` chứa hai phần tử theo thứ tự xác định; set không hỗ trợ chỉ số vị trí.

**Q2. What is the index of the first list element? | Chỉ số của phần tử List đầu tiên là gì?**

A. `0` | `0`

B. `-1` | `-1`

C. `len(a)` | `len(a)`

D. `1` | `1`

**Đáp án: A**

**Giải thích:** Chỉ số List bắt đầu từ `0`, vì vậy `a[0]` lấy phần tử đầu và `a[1]` lấy phần tử thứ hai. Chỉ số âm `-1` mang nghĩa khác: phần tử cuối.

**Q3. For a List `a`, what does `a[:2]` return? | Với `a` là một List, `a[:2]` trả về gì?**

A. Items from index 2 to the end | Các phần tử từ chỉ số 2 đến cuối

B. A new list of the first two items | List mới gồm hai phần tử đầu

C. A new list of the last two items | List mới gồm hai phần tử cuối

D. Only item at index 2 | Chỉ phần tử tại chỉ số 2

**Đáp án: B**

**Giải thích:** Lát cắt `a[:2]` mặc định bắt đầu tại chỉ số 0 và dừng trước chỉ số 2, tạo List mới gồm hai phần tử đầu. Với `[4, 5, 6]`, kết quả là `[4, 5]`, không phải phần tử tại chỉ số 2.

**Q4. What does 'mutable' mean for a list? | List có tính mutable nghĩa là gì?**

A. Its contents can be changed after creation | Có thể sửa nội dung sau khi tạo

B. Its elements cannot be changed | Không thể sửa các phần tử

C. Every element must have the same type | Mọi phần tử phải cùng kiểu

D. Its elements sort automatically | Các phần tử được tự động sắp xếp

**Đáp án: A**

**Giải thích:** Mutable nghĩa là có thể thay, thêm hoặc xóa phần tử trên List hiện có. Ví dụ gán `a = [1, 2]` rồi thực hiện `a[0] = 9` làm `a` thành `[9, 2]`; tuple không cho phép gán phần tử như vậy.

**Q5. What does `append(x)` do? | `append(x)` làm gì?**

A. Inserts `x` before the first item | Chèn `x` trước phần tử đầu

B. Removes the final element and returns it | Xóa phần tử cuối và trả về

C. Adds `x` as a single final item | Thêm `x` thành một phần tử cuối

D. Adds every element of `x` separately | Thêm riêng từng phần tử của `x`

**Đáp án: C**

**Giải thích:** `append(x)` thêm toàn bộ `x` thành đúng một phần tử cuối List và sửa List tại chỗ. Vì vậy thêm `[2, 3]` bằng `append` vào `[1]` tạo phần tử List lồng nhau, không thêm từng số; muốn thêm từng số thì dùng `extend()`.

**Q6. What does `extend(items)` do? | `extend(items)` làm gì?**

A. Deletes items matching `items` | Xóa phần tử khớp `items`

B. Appends the iterable as one nested item | Thêm cả iterable thành một phần tử lồng

C. Adds the individual elements from `items` | Thêm từng phần tử từ `items`

D. Replaces the first element with `items` | Thay phần tử đầu bằng `items`

**Đáp án: C**

**Giải thích:** `extend(items)` duyệt đối số và thêm từng phần tử riêng vào List hiện có. Với `a = [1]`, `a.extend([2, 3])` tạo `[1, 2, 3]`, còn `append([2, 3])` sẽ tạo `[1, [2, 3]]`.

**Q7. What does `insert(0, x)` do? | `insert(0, x)` làm gì?**

A. Replaces the first element with `x` | Thay phần tử đầu bằng `x`

B. Inserts `x` at the front, shifting the others | Chèn `x` vào đầu, đẩy các phần tử khác sang phải

C. Removes the first element | Xóa phần tử đầu

D. Adds `x` at the end | Thêm `x` vào cuối

**Đáp án: B**

**Giải thích:** `insert(0, x)` chèn `x` trước phần tử đầu tiên và đẩy các phần tử cũ sang phải. Ví dụ chèn `9` vào đầu `[1, 2]` cho `[9, 1, 2]`, không ghi đè số `1`.

**Q8. What does `pop(0)` do on a nonempty list? | `pop(0)` làm gì với List không rỗng?**

A. Removes and returns the last item | Xóa và trả phần tử cuối

B. Returns the first item without removing it | Trả phần tử đầu nhưng không xóa

C. Deletes the first occurrence of the value zero | Xóa lần xuất hiện đầu của giá trị không

D. Removes and returns the first item | Xóa và trả phần tử đầu

**Đáp án: D**

**Giải thích:** `pop(0)` xóa phần tử đầu của List không rỗng và trả chính phần tử đã xóa. Với `[7, 8]`, kết quả trả về là `7` và List còn `[8]`; chỉ đọc `a[0]` thì không xóa phần tử nào.

**Q9. What does `remove(x)` do? | `remove(x)` dùng để làm gì?**

A. Deletes every matching value | Xóa tất cả giá trị khớp

B. Returns a sorted copy | Trả bản sao đã sắp xếp

C. Deletes the first matching value | Xóa giá trị khớp đầu tiên

D. Deletes the item at index `x` | Xóa phần tử tại chỉ số `x`

**Đáp án: C**

**Giải thích:** `remove(x)` xóa lần xuất hiện đầu tiên có giá trị bằng `x`; nó tìm theo giá trị chứ không xem `x` là chỉ số. Với `[2, 3, 2]`, `remove(2)` còn `[3, 2]`, và giá trị không tồn tại sẽ gây `ValueError`.

**Q10. What does `del a[1]` do? | `del a[1]` có tác dụng gì?**

A. Returns the removed item | Trả về phần tử đã xóa

B. Deletes the item whose value is `1` | Xóa phần tử có giá trị bằng `1`

C. Deletes the item at index one | Xóa phần tử có chỉ số 1

D. Replaces the item at index one with `None` | Thay phần tử chỉ số 1 bằng `None`

**Đáp án: C**

**Giải thích:** `del a[1]` xóa phần tử tại chỉ số 1, tức phần tử thứ hai vì chỉ số bắt đầu từ 0. Khác `remove(1)`, lệnh này dùng vị trí; khác `pop(1)`, câu lệnh `del` không trả về giá trị bị xóa.

**Q11. What does `a.sort()` return? | `a.sort()` trả về gì?**

A. The sorted indexes | Các chỉ số đã sắp xếp

B. A new sorted list | List mới đã sắp xếp

C. The same list as a return value | Trả về chính List đó

D. `None` | `None`

**Đáp án: D**

**Giải thích:** `a.sort()` sắp List tại chỗ và trả về `None`, nên chính List cũ nhận thứ tự mới. Gán `result = a.sort()` sẽ cho `None`, không phải List mới đã sắp; muốn List riêng thì dùng `sorted(a)`.

**Q12. What does `sorted(a)` do? | `sorted(a)` làm gì?**

A. Reverses the original list in place | Đảo List gốc tại chỗ

B. Produces a set of unique items | Tạo Set các phần tử duy nhất

C. Creates a new sorted list | Tạo List mới đã sắp xếp

D. Sorts `a` in place and returns `None` | Sắp `a` tại chỗ và trả `None`

**Đáp án: C**

**Giải thích:** `sorted(a)` trả về List mới đã sắp xếp và không đổi thứ tự List gốc. Nếu `a = [3, 1]`, `sorted(a)` là `[1, 3]` còn `a` vẫn `[3, 1]`, khác `a.sort()`.

**Q13. What does `a[-1]` read from a nonempty list? | `a[-1]` lấy gì từ List không rỗng?**

A. The last element | Phần tử cuối

B. The first element | Phần tử đầu

C. The number of elements | Số phần tử

D. An `IndexError` for every nonempty list | Luôn có `IndexError` với List không rỗng

**Đáp án: A**

**Giải thích:** Chỉ số `-1` chỉ phần tử cuối của List không rỗng, bất kể List dài bao nhiêu. Với `[4, 7, 9]`, `a[-1]` là `9`; còn `len(a)` đếm đủ ba phần tử.

**Q14. What does `len(a)` report? | `len(a)` cho biết gì?**

A. The number of distinct values | Số giá trị khác nhau

B. The list's memory size in bytes | Kích thước List tính theo byte

C. The final valid index | Chỉ số hợp lệ cuối

D. The number of elements | Số phần tử

**Đáp án: D**

**Giải thích:** `len(a)` trả về số phần tử ở cấp ngoài của List; một List lồng trong được tính là một phần tử. Với `[1, [2, 3]]`, độ dài là `2`, không phải `3` và không phải chỉ số cuối `1`.

**Q15. What happens for `a[10]` on a two-item list? | `a[10]` sẽ thế nào nếu List có hai phần tử?**

A. The last list element | Phần tử cuối List

B. `None` | `None`

C. The integer `0` | Số nguyên `0`

D. `IndexError` | `IndexError`

**Đáp án: D**

**Giải thích:** List gồm hai phần tử chỉ có chỉ số dương hợp lệ `0` và `1`; đọc `a[10]` vượt giới hạn nên gây `IndexError`. Python không tự trả `None` hoặc mở rộng List khi đọc chỉ số không có.

**Q16. What does `a[1] = 5` do? | `a[1] = 5` làm gì?**

A. Changes the first item to `5` | Thay phần tử đầu thành `5`

B. Replaces the second element with `5` | Thay phần tử thứ hai bằng `5`

C. Inserts a new element at index 1 | Chèn phần tử mới tại chỉ số 1

D. Adds `5` to the end | Thêm `5` vào cuối

**Đáp án: B**

**Giải thích:** `a[1] = 5` thay phần tử hiện có tại chỉ số 1 thành `5`, miễn chỉ số đó tồn tại. Với `[8, 9]`, kết quả là `[8, 5]`; lệnh không chèn thêm phần tử hay sửa chỉ số 0.

**Q17. Which operation sorts a list in place? | Thao tác nào sắp xếp ngay List gốc?**

A. `a.sort()` | `a.sort()`

B. `sorted(a)` | `sorted(a)`

C. `a.reverse()` | `a.reverse()`

D. `reversed(a)` | `reversed(a)`

**Đáp án: A**

**Giải thích:** `a.sort()` sắp xếp ngay trên List gốc nên đọc `a` sau đó thấy thứ tự mới. `sorted(a)` trả List khác, còn `reverse()` chỉ đảo vị trí hiện có, không tính thứ tự sắp xếp.

**Q18. Which expression sorts without mutating the original? | Biểu thức nào sắp xếp mà không sửa List gốc?**

A. `sorted(a)` | `sorted(a)`

B. `a.reverse()` | `a.reverse()`

C. `a.extend(sorted(a))` | `a.extend(sorted(a))`

D. `a.sort()` | `a.sort()`

**Đáp án: A**

**Giải thích:** `sorted(a)` tạo List mới theo thứ tự sắp xếp và giữ nguyên `a`. Ngược lại `a.sort()` sửa trực tiếp `a` và trả `None`, nên không thể dùng thay nhau khi cần giữ dữ liệu gốc.

**Q19. What does `reverse=True` mean in a numeric sort? | `reverse=True` có ý nghĩa gì khi sắp xếp số?**

A. Reverse each number's digits | Đảo chữ số trong từng số

B. Ascending order | Thứ tự tăng dần

C. Random element order | Thứ tự phần tử ngẫu nhiên

D. Descending numeric order | Thứ tự số giảm dần

**Đáp án: D**

**Giải thích:** Trong phép sắp số mặc định tăng dần, `reverse=True` đảo thứ tự thành giảm dần. Với `[3, 1, 2]`, `sorted(a, reverse=True)` cho `[3, 2, 1]`, không đơn thuần đảo thứ tự vị trí gốc.

**Q20. How do `append([3,4])` and `extend([3,4])` differ? | `append([3,4])` và `extend([3,4])` khác gì?**

A. Both operations sort the existing list | Cả hai đều sắp xếp List

B. `append` adds one nested list; `extend` adds two elements | `append` thêm một List con; `extend` thêm hai phần tử

C. Both operations create the same flat list | Cả hai tạo cùng List phẳng

D. `append` adds both separately and `extend` nests them | `append` thêm riêng còn `extend` lồng List

**Đáp án: B**

**Giải thích:** `append([3, 4])` thêm nguyên List con thành một phần tử, còn `extend([3, 4])` thêm riêng hai số nguyên. Bắt đầu từ `[1, 2]`, hai kết quả lần lượt là `[1, 2, [3, 4]]` và `[1, 2, 3, 4]`.

## PY-07 — PY-07 — Tuple, Set và các phép toán tập hợp

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a tuple? | Tuple là gì?**

A. An ordered mutable sequence | Dãy có thứ tự và có thể sửa

B. An unordered collection of unique items | Tập hợp không thứ tự của phần tử duy nhất

C. A key-to-value mapping | Ánh xạ khóa–giá trị

D. An ordered immutable collection | Tập hợp có thứ tự và bất biến

**Đáp án: D**

**Giải thích:** Tuple là dãy có thứ tự và bất biến: `(2, 3)` giữ tọa độ đầu trước tọa độ sau, nhưng không cho phép gán lại từng phần tử. List cũng có thứ tự nhưng có thể sửa các phần tử.

**Q2. What is a set? | Set là gì?**

A. An ordered collection of key-value entries | Tập hợp có thứ tự các cặp khóa–giá trị

B. A collection that always keeps duplicates | Tập hợp luôn giữ giá trị trùng

C. A collection of unique hashable members | Tập hợp gồm phần tử có thể băm và không trùng

D. A sequence accessed by positional indexes | Dãy truy cập bằng chỉ số vị trí

**Đáp án: C**

**Giải thích:** Set chứa các phần tử có thể băm và không trùng nhau, đồng thời không hỗ trợ truy cập theo chỉ số vị trí. Tạo `set([1, 1, 2])` chỉ còn hai phần tử `1` và `2`, khác List vốn giữ phần tử lặp.

**Q3. What does set union collect? | Phép hợp Set lấy gì?**

A. Only members of the first set not in the second | Chỉ phần tử tập đầu mà không thuộc tập sau

B. Distinct members appearing in either set | Phần tử khác nhau thuộc ít nhất một tập

C. Only members appearing in exactly one set | Chỉ phần tử thuộc đúng một tập

D. Only members common to both sets | Chỉ phần tử chung của hai tập

**Đáp án: B**

**Giải thích:** Phép hợp lấy mỗi phần tử khác nhau xuất hiện trong ít nhất một tập. Với `{1, 2}` và `{2, 3}`, hợp chứa `{1, 2, 3}`; phép giao chỉ giữ phần tử chung `2`.

**Q4. What does set intersection collect? | Phép giao Set lấy gì?**

A. Only members of the first set | Chỉ phần tử tập đầu

B. Members occurring in exactly one set | Phần tử xuất hiện đúng một tập

C. Only members shared by both sets | Chỉ phần tử chung của cả hai tập

D. All distinct members of either set | Mọi phần tử khác nhau thuộc ít nhất một tập

**Đáp án: C**

**Giải thích:** Phép giao chỉ giữ phần tử có mặt ở cả hai tập. Với `{1, 2}` và `{2, 3}`, giao là `{2}`; tập này nhỏ hơn phép hợp `{1, 2, 3}`.

**Q5. Which expression constructs a two-element tuple? | Biểu thức nào tạo Tuple có hai phần tử?**

A. `(2, 3)` | `(2, 3)`

B. `[2, 3]` | `[2, 3]`

C. `{2, 3}` | `{2, 3}`

D. `{2: 3}` | `{2: 3}`

**Đáp án: A**

**Giải thích:** `(2, 3)` là Tuple gồm hai phần tử có thứ tự với các giá trị phân cách bằng dấu phẩy. Ngược lại, `{2, 3}` là Set và `[2, 3]` là List có thể sửa.

**Q6. Which expression constructs a nonempty set? | Biểu thức nào tạo Set không rỗng?**

A. `[2, 3]` | `[2, 3]`

B. `{2: 3}` | `{2: 3}`

C. `(2, 3)` | `(2, 3)`

D. `{2, 3}` | `{2, 3}`

**Đáp án: D**

**Giải thích:** `{2, 3}` tạo Set không rỗng gồm hai số nguyên khác nhau. Dấu ngoặc tròn tạo Tuple và ngoặc vuông tạo List, còn ngoặc nhọn rỗng `{}` tạo Dictionary.

**Q7. Which expression constructs an empty set? | Biểu thức nào tạo Set rỗng?**

A. `[]` | `[]`

B. `set()` | `set()`

C. `()` | `()`

D. `{}` | `{}`

**Đáp án: B**

**Giải thích:** `set()` tạo Set rỗng. Ký hiệu gần giống `{}` lại là Dictionary rỗng, vì vậy không thể dùng cặp ngoặc nhọn trống để tạo Set không có phần tử.

**Q8. Which expression constructs an empty dictionary? | Biểu thức nào tạo Dictionary rỗng?**

A. `set()` | `set()`

B. `[]` | `[]`

C. `()` | `()`

D. `{}` | `{}`

**Đáp án: D**

**Giải thích:** `{}` biểu diễn Dictionary rỗng, tức ánh xạ khóa–giá trị chưa có mục nào. Muốn tạo Set rỗng phải dùng `set()`; List và Tuple rỗng lần lượt là `[]` và `()`.

**Q9. What does `a | b` do for sets? | `a | b` làm gì với hai Set?**

A. Set difference from `a` to `b` | Hiệu Set từ `a` trừ `b`

B. Symmetric difference | Hiệu đối xứng

C. Set union | Phép hợp Set

D. Set intersection | Phép giao Set

**Đáp án: C**

**Giải thích:** Với Set, `a | b` thực hiện phép hợp, giữ phần tử khác nhau thuộc `a`, `b` hoặc cả hai. Nếu `a={1,2}` và `b={2,3}`, kết quả chứa 1, 2, 3, khác giao vốn chỉ giữ 2.

**Q10. What does `a & b` do for sets? | `a & b` làm gì với hai Set?**

A. Set intersection | Phép giao Set

B. Set difference | Phép hiệu Set

C. Symmetric difference | Hiệu đối xứng

D. Set union | Phép hợp Set

**Đáp án: A**

**Giải thích:** `a & b` là phép giao Set, chỉ giữ giá trị xuất hiện ở cả hai tập. Với `{1,2}` và `{2,3}`, kết quả là `{2}`; nó không lấy mọi phần tử khác nhau như phép hợp.

**Q11. What does `a - b` do for sets? | `a - b` làm gì với hai Set?**

A. Members in `a` but not in `b` | Phần tử thuộc `a` nhưng không thuộc `b`

B. Members in exactly one input | Phần tử thuộc đúng một tập

C. Set union | Phép hợp Set

D. Set intersection | Phép giao Set

**Đáp án: A**

**Giải thích:** `a - b` chỉ giữ phần tử thuộc `a` mà không thuộc `b`, nên thứ tự hai vế quan trọng: `{1,2} - {2,3}` cho `{1}`. Đảo hai vế lại được `{3}`, khác hiệu đối xứng giữ cả 1 và 3.

**Q12. What does `a ^ b` do for sets? | `a ^ b` làm gì với hai Set?**

A. Set union | Phép hợp Set

B. Set intersection | Phép giao Set

C. Members of `a` only | Chỉ phần tử của `a`

D. Members in exactly one of the sets | Phần tử thuộc đúng một trong hai tập

**Đáp án: D**

**Giải thích:** `a ^ b` tính hiệu đối xứng: lấy phần tử có mặt đúng ở một trong hai tập. Với `{1,2}` và `{2,3}`, kết quả chứa 1 và 3 nhưng loại phần tử chung 2.

**Q13. What is the length of `set([1,1,2])`? | `set([1,1,2])` có bao nhiêu phần tử?**

A. `2` | `2`

B. `3` | `3`

C. `1` | `1`

D. `ValueError` | `ValueError`

**Đáp án: A**

**Giải thích:** Tạo Set sẽ loại giá trị trùng, vì vậy `set([1,1,2])` chỉ còn phần tử 1 và 2. Độ dài do đó bằng số nguyên `2`, không phải ba vị trí của List gốc.

**Q14. What happens when assigning `t[0] = 9` on a tuple? | Gán `t[0] = 9` trên Tuple sẽ thế nào?**

A. A `TypeError` is raised | Phát sinh `TypeError`

B. A new tuple is created automatically | Tự động tạo Tuple mới

C. An `IndexError` is always raised | Luôn phát sinh `IndexError`

D. The tuple's first item changes to 9 | Phần tử đầu Tuple đổi thành 9

**Đáp án: A**

**Giải thích:** Tuple không cho phép gán lại từng phần tử nên `t[0] = 9` trên Tuple gây `TypeError`. Khác với List, việc gán vào một chỉ số hợp lệ được cho phép.

**Q15. How do you test membership in a set? | Làm sao kiểm tra một giá trị thuộc Set?**

A. `s[x]` | `s[x]`

B. `x in s` | `x in s`

C. `x == s` | `x == s`

D. `s.index(x)` | `s.index(x)`

**Đáp án: B**

**Giải thích:** Dùng `x in s` để kiểm tra phần tử, kết quả là Boolean. Với `s={1,3}`, `3 in s` là `True` và `2 in s` là `False`; Set không có phương thức `.index()` theo vị trí.

**Q16. Is order of printed set elements guaranteed? | Thứ tự phần tử in từ Set có được bảo đảm không?**

A. Always sorted in ascending order | Luôn theo thứ tự tăng dần

B. Always insertion order | Luôn theo thứ tự thêm vào

C. Always a new random permutation | Luôn tạo hoán vị ngẫu nhiên mới

D. No fixed display order is guaranteed | Không bảo đảm thứ tự hiển thị cố định

**Đáp án: D**

**Giải thích:** Set không bảo đảm thứ tự khi hiển thị hay duyệt các phần tử. Dù một lần chạy in `{1, 2, 3}`, không nên phụ thuộc thứ tự đó ở các lần sau; sắp xếp Set là thao tác riêng.

**Q17. Which built-in immutable ordered sequence best represents a fixed coordinate pair `(x, y)`? | Kiểu dãy có thứ tự và bất biến nào phù hợp nhất biểu diễn cặp tọa độ cố định `(x, y)`?**

A. Dictionary | Dictionary

B. Tuple | Tuple

C. List | List

D. Set | Set

**Đáp án: B**

**Giải thích:** Một cặp có thứ tự và bất biến như `(x, y)` phù hợp tọa độ cố định vì vị trí thứ nhất và thứ hai có ý nghĩa riêng. Set không truy cập theo vị trí, còn List cho phép gán lại phần tử.

**Q18. Which built-in collection directly keeps only distinct tags? | Kiểu tập hợp nào trực tiếp chỉ giữ những nhãn khác nhau?**

A. String, which holds one sequence of characters | String lưu dãy ký tự

B. Tuple, which retains duplicates | Tuple giữ nguyên các phần tử trùng

C. Set, which retains distinct tags | Set chỉ giữ nhãn khác nhau

D. List, which retains duplicates | List giữ nguyên các phần tử trùng

**Đáp án: C**

**Giải thích:** Set trực tiếp loại nhãn trùng vì mỗi giá trị chỉ xuất hiện một lần. Với nhãn `['red', 'red', 'blue']`, tạo Set giữ hai nhãn khác nhau `red` và `blue`, nhưng không bảo đảm thứ tự.

**Q19. Which method checks whether sets share no elements? | Phương thức nào kiểm tra hai Set không có phần tử chung?**

A. `union()` | `union()`

B. `isdisjoint()` | `isdisjoint()`

C. `intersection()` | `intersection()`

D. `issubset()` | `issubset()`

**Đáp án: B**

**Giải thích:** `a.isdisjoint(b)` trả `True` khi và chỉ khi hai Set không có phần tử chung. Với `{1,2}` và `{3}`, kết quả là `True`, còn `{1,2}` và `{2,4}` cho `False`.

**Q20. Which function creates a sorted list from a set of comparable numbers? | Hàm nào tạo List đã sắp từ một Set chứa các số có thể so sánh?**

A. `list(s)` without ordering | `list(s)` không sắp xếp

B. `reversed(s)` | `reversed(s)`

C. `sorted(s)` | `sorted(s)`

D. `s.sort()` | `s.sort()`

**Đáp án: C**

**Giải thích:** `sorted(s)` trả về List mới đã sắp xếp, ví dụ `sorted({3,1,2})` cho `[1,2,3]`. Nó không tạo thứ tự cố định cho Set gốc, vốn vẫn là tập không có thứ tự vị trí.

## PY-08 — PY-08 — Dictionary: khóa, giá trị và thêm sửa xóa

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a dictionary? | Dictionary là gì?**

A. An unordered collection of unique values only | Tập không thứ tự chỉ gồm giá trị duy nhất

B. An immutable pair of numbers | Cặp số bất biến

C. A mapping from hashable keys to values | Ánh xạ từ khóa có thể băm sang giá trị

D. A sequence with numeric positions only | Dãy chỉ truy cập bằng vị trí số

**Đáp án: C**

**Giải thích:** Dictionary ánh xạ các khóa khác nhau, có thể băm, tới giá trị tương ứng, ví dụ `{'name':'An', 'score':9}`. Bạn truy cập giá trị qua khóa thay vì chỉ số vị trí như List.

**Q2. What does a dictionary key do? | Khóa Dictionary có vai trò gì?**

A. Specifies the dictionary's length | Xác định độ dài Dictionary

B. Stores all keys as values | Lưu mọi khóa thành giá trị

C. Sorts the stored values | Sắp xếp các giá trị đã lưu

D. Identifies an entry for lookup | Xác định mục để tra cứu

**Đáp án: D**

**Giải thích:** Khóa xác định một mục để tra cứu, cập nhật hoặc xóa giá trị. Trong `{'age': 20}`, khóa `'age'` dẫn đến giá trị `20`; khóa không đồng nghĩa với giá trị đi kèm.

**Q3. What is a dictionary value? | Giá trị Dictionary là gì?**

A. The key's index position | Vị trí chỉ số của khóa

B. Data associated with a key | Dữ liệu gắn với khóa

C. Always a second dictionary | Luôn là Dictionary thứ hai

D. A name used only in a `for` loop | Tên chỉ dùng trong vòng `for`

**Đáp án: B**

**Giải thích:** Giá trị Dictionary là dữ liệu lưu dưới một khóa, chẳng hạn số `20` dưới khóa `'age'`. Giá trị có thể thuộc nhiều kiểu kể cả List hoặc Dictionary, trong khi khóa phải là đối tượng có thể băm.

**Q4. What is a nested dictionary? | Dictionary lồng nhau là gì?**

A. A dictionary stored inside another dictionary | Dictionary được lưu trong Dictionary khác

B. A list nested inside a set | List lồng trong Set

C. A set of duplicate keys | Set gồm khóa trùng

D. A dictionary with only numeric keys | Dictionary chỉ có khóa số

**Đáp án: A**

**Giải thích:** Dictionary lồng nhau là Dictionary được lưu làm giá trị trong Dictionary khác. Ví dụ `{'A': {'score': 9}}` gom trường `score` dưới khóa `'A'`, và hai lần truy cập ngoặc vuông sẽ lấy được con số.

**Q5. What does `d['x']` do when x exists? | `d['x']` làm gì khi khóa x tồn tại?**

A. Always returns `None` | Luôn trả `None`

B. Retrieves the value stored under `'x'` | Lấy giá trị lưu dưới khóa `'x'`

C. Returns `'x'` as a string | Trả chuỗi `'x'`

D. Deletes the entry for `'x'` | Xóa mục có khóa `'x'`

**Đáp án: B**

**Giải thích:** Khi khóa `'x'` tồn tại, `d['x']` lấy giá trị gắn với khóa đó. Khác `d.get('x')`, truy cập ngoặc vuông sẽ gây `KeyError` nếu khóa không tồn tại.

**Q6. What does `d.get('x')` return if x is absent? | `d.get('x')` trả về gì nếu thiếu khóa x?**

A. `KeyError` | `KeyError`

B. `None` by default | Mặc định là `None`

C. The empty dictionary `{}` | Dictionary rỗng `{}`

D. The string `'x'` | Chuỗi `'x'`

**Đáp án: B**

**Giải thích:** Khi không cung cấp mặc định, `d.get('x')` trả `None` nếu thiếu khóa thay vì gây `KeyError`. Cách này giúp xử lý dữ liệu thiếu, nhưng bản thân `None` cũng có thể là giá trị được lưu thật.

**Q7. What does `d.get('x', 0)` return if x is absent? | `d.get('x', 0)` trả về gì nếu thiếu x?**

A. The integer `0` | Số nguyên `0`

B. A newly inserted entry | Một mục mới được thêm

C. The string `'0'` | Chuỗi `'0'`

D. `None` | `None`

**Đáp án: A**

**Giải thích:** Đối số thứ hai của `get` là giá trị dự phòng khi không tìm thấy khóa, nên `d.get('x', 0)` trả số nguyên `0` nếu thiếu `'x'`. Lệnh không tạo khóa đó và không ghi đè giá trị đang có.

**Q8. What does `d['missing']` raise? | `d['missing']` phát sinh gì khi thiếu khóa?**

A. `0` | `0`

B. An empty list | List rỗng

C. `KeyError` | `KeyError`

D. `None` | `None`

**Đáp án: C**

**Giải thích:** Truy cập trực tiếp `d['missing']` gây `KeyError` khi không có khóa. Với dữ liệu tùy chọn, `get` có thể trả giá trị dự phòng; sự khác biệt này quyết định có xem việc thiếu khóa là lỗi hay không.

**Q9. What does `d.items()` provide? | `d.items()` cung cấp gì?**

A. A sorted list of keys | List khóa đã sắp

B. A view of key-value pairs | View của các cặp khóa–giá trị

C. Only a view of values | Chỉ view các giá trị

D. Only a view of keys | Chỉ view các khóa

**Đáp án: B**

**Giải thích:** `d.items()` trả một view động của các cặp khóa–giá trị, thường duyệt bằng `for key, value in d.items()`. Nó khác `keys()` chỉ đưa ra khóa và `values()` chỉ đưa ra giá trị.

**Q10. What does `d.keys()` provide? | `d.keys()` cung cấp gì?**

A. A view of values | View các giá trị

B. A list of keys sorted automatically | List khóa tự sắp

C. A view of pairs | View các cặp khóa–giá trị

D. A view of dictionary keys | View của các khóa Dictionary

**Đáp án: D**

**Giải thích:** `d.keys()` cung cấp view động của các khóa Dictionary. Với `{'a': 1}`, khi duyệt view này nhận `'a'`, không phải giá trị `1` hay cả cặp khóa–giá trị.

**Q11. What does `d.values()` provide? | `d.values()` cung cấp gì?**

A. A view of dictionary values | View các giá trị Dictionary

B. A dictionary copy | Bản sao Dictionary

C. A view of keys | View các khóa

D. A view of key-value pairs | View các cặp khóa–giá trị

**Đáp án: A**

**Giải thích:** `d.values()` trả view động của các giá trị đang lưu. Với `{'a': 1, 'b': 2}`, khi duyệt thu được 1 và 2; muốn kèm khóa tương ứng thì dùng `items()`.

**Q12. What does `d.pop('x', None)` do if x is present? | `d.pop('x', None)` làm gì nếu x tồn tại?**

A. Returns the value without deletion | Trả giá trị nhưng không xóa

B. Removes the key but always returns `None` | Xóa khóa nhưng luôn trả `None`

C. Deletes every dictionary entry | Xóa mọi mục Dictionary

D. Removes `'x'` and returns its former value | Xóa `'x'` và trả giá trị cũ

**Đáp án: D**

**Giải thích:** Khi `'x'` tồn tại, `d.pop('x', None)` xóa mục tương ứng và trả về giá trị cũ. Đối số `None` chỉ là giá trị dự phòng nếu không có khóa; nó không ép kết quả luôn thành `None`.

**Q13. What does `d['x'] = 5` do if x already exists? | `d['x'] = 5` làm gì khi x đã tồn tại?**

A. Replaces the value associated with `'x'` | Thay giá trị gắn với `'x'`

B. Adds a second duplicate `'x'` key | Thêm khóa `'x'` trùng thứ hai

C. Deletes the key `'x'` | Xóa khóa `'x'`

D. Tests whether `'x'` exists | Kiểm tra `'x'` tồn tại không

**Đáp án: A**

**Giải thích:** Gán `d['x'] = 5` khi khóa `'x'` đã tồn tại sẽ thay giá trị của mục đó thành `5`. Lệnh không tạo thêm một khóa `'x'` thứ hai vì mỗi khóa Dictionary là duy nhất.

**Q14. What does `d['new'] = 5` do if new is absent? | `d['new'] = 5` làm gì khi khóa new chưa có?**

A. Deletes an absent key | Xóa một khóa không tồn tại

B. Returns the total dictionary length | Trả tổng độ dài Dictionary

C. Replaces an unrelated existing key | Thay một khóa cũ không liên quan

D. Inserts a new key-value entry | Thêm một mục khóa–giá trị mới

**Đáp án: D**

**Giải thích:** Gán `d['new'] = 5` khi chưa có khóa sẽ thêm cặp `'new'` ánh xạ tới 5. Cùng cú pháp gán này lại cập nhật giá trị nếu khóa đã tồn tại.

**Q15. What does `del d['x']` do for an existing key? | `del d['x']` làm gì với khóa đang tồn tại?**

A. Deletes that key and its value | Xóa khóa đó cùng giá trị

B. Deletes the entire dictionary | Xóa toàn bộ Dictionary

C. Leaves the entry intact and returns its value | Giữ nguyên mục và trả giá trị

D. Replaces its value with `None` | Thay giá trị bằng `None`

**Đáp án: A**

**Giải thích:** `del d['x']` xóa khóa có sẵn cùng giá trị tương ứng khỏi Dictionary. Khác `pop`, câu lệnh `del` không trả về giá trị đã xóa.

**Q16. What does `'x' in d` test? | `'x' in d` kiểm tra gì?**

A. Whether `'x'` is a numeric index | `'x'` có phải chỉ số số hay không

B. Whether any key maps to `'x'` | Có khóa nào ánh xạ tới `'x'` không

C. Whether `'x'` is a dictionary key | `'x'` có là khóa Dictionary không

D. Whether `'x'` appears in values only | `'x'` có nằm trong các giá trị hay không

**Đáp án: C**

**Giải thích:** Với Dictionary, `in` mặc định kiểm tra khóa: `'x' in {'x': 3}` là `True`, còn `3 in {'x': 3}` là `False`. Muốn kiểm tra giá trị thay vì khóa, hãy xét thành viên trong `d.values()`.

**Q17. May a List be a normal dictionary key? | Có thể dùng List làm khóa Dictionary thông thường không?**

A. Yes, if the list has two elements | Có, nếu List có hai phần tử

B. Yes, if list values are distinct | Có, nếu các giá trị List khác nhau

C. No, lists are unhashable | Không, List không thể băm

D. Yes, every list is hashable | Có, mọi List đều có thể băm

**Đáp án: C**

**Giải thích:** List có thể thay đổi nên không thể băm và không dùng làm khóa Dictionary thông thường. Thử `{[1,2]: 'x'}` gây `TypeError`; một Tuple chứa các số có thể băm thì dùng được.

**Q18. Can a tuple of integers be a dictionary key? | Tuple chứa số nguyên có thể làm khóa Dictionary không?**

A. No, all tuples are unhashable | Không, mọi Tuple đều không thể băm

B. Yes, a tuple of integers is hashable | Có, Tuple chứa số nguyên có thể băm

C. Only if the tuple has one element | Chỉ nếu Tuple có một phần tử

D. Only if the tuple is empty | Chỉ nếu Tuple rỗng

**Đáp án: B**

**Giải thích:** Tuple chỉ chứa số nguyên có thể băm nên dùng làm khóa Dictionary, ví dụ `{(1,2): 'point'}`. Không phải mọi Tuple đều dùng được: Tuple chứa List cũng không thể băm vì một phần tử bên trong không thể băm.

**Q19. How do you access the score in `d['A']` when it is a nested dictionary? | Lấy điểm trong Dictionary con `d['A']` thế nào?**

A. `d['A', 'score']` | `d['A', 'score']`

B. `d['score']['A']` | `d['score']['A']`

C. `d.get('A', 'score')` | `d.get('A', 'score')`

D. `d['A']['score']` | `d['A']['score']`

**Đáp án: D**

**Giải thích:** `d['A']['score']` trước tiên lấy Dictionary con dưới khóa `'A'`, rồi tra mục `'score'` trong đó. Với `d={'A':{'score':9}}`, biểu thức trả 9; nếu thiếu một trong các khóa thì cách truy cập trực tiếp gây `KeyError`.

**Q20. What must be unique within one dictionary? | Điều gì phải duy nhất trong một Dictionary?**

A. Dictionary values | Các giá trị Dictionary

B. Both all keys and all values must be unique | Cả khóa và giá trị đều phải duy nhất

C. Dictionary keys | Các khóa Dictionary

D. Neither keys nor values must be unique | Cả khóa lẫn giá trị đều không cần duy nhất

**Đáp án: C**

**Giải thích:** Các khóa là duy nhất trong một Dictionary; gán lại cùng một khóa sẽ cập nhật mục cũ thay vì tạo thêm bản sao. Giá trị có thể lặp ở nhiều khóa nên tính duy nhất áp dụng cho khóa chứ không phải giá trị.

## PY-09 — PY-09 — Hàm, return, lambda và phạm vi biến

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a Python function? | Hàm Python là gì?**

A. Only a variable declared at module level | Chỉ biến khai báo ở cấp module

B. Only code that prints text | Chỉ mã in văn bản

C. Only a loop executed once | Chỉ vòng lặp chạy một lần

D. Reusable callable code that can accept inputs | Phần mã có thể gọi lại, có thể nhận đầu vào

**Đáp án: D**

**Giải thích:** Hàm Python là phần mã có thể gọi lại nhiều lần, có thể nhận đầu vào và trả kết quả. Hàm thường có thể định nghĩa bằng `def`, còn `lambda` cũng tạo hàm từ một biểu thức; không phải mọi hàm đều bắt buộc có tên.

**Q2. What is a parameter? | Tham số là gì?**

A. A value supplied by the caller | Giá trị truyền từ nơi gọi

B. A name declared in a function's definition | Tên khai báo trong định nghĩa hàm

C. The value printed by a function | Giá trị được hàm in ra

D. A variable always declared global | Biến luôn được khai báo toàn cục

**Đáp án: B**

**Giải thích:** Tham số là tên khai báo trong định nghĩa hàm để nhận đầu vào. Trong `def double(x):`, `x` là tham số, còn số `3` trong `double(3)` là đối số được truyền khi gọi.

**Q3. What is an argument? | Đối số là gì?**

A. The name in the function definition | Tên trong định nghĩa hàm

B. A keyword beginning a function body | Từ khóa bắt đầu thân hàm

C. A value supplied in a function call | Giá trị truyền khi gọi hàm

D. The result returned by a function | Kết quả hàm trả về

**Đáp án: C**

**Giải thích:** Đối số là giá trị thực tế được truyền vào khi gọi hàm. Với `double(3)`, số nguyên `3` là đối số gắn vào tham số `x`; tên tham số xuất hiện trong phần định nghĩa.

**Q4. What is a return value? | Giá trị trả về là gì?**

A. A result sent back to the caller | Kết quả gửi về nơi gọi

B. A parameter name | Tên tham số

C. The function's source-code text | Văn bản mã nguồn hàm

D. A displayed message from `print` | Thông báo hiển thị bởi `print`

**Đáp án: A**

**Giải thích:** Giá trị trả về là thông tin hàm gửi về nơi gọi qua câu lệnh `return`. Khác `print` dùng để hiển thị, `return` giúp mã gọi hàm tiếp tục sử dụng kết quả tính toán.

**Q5. Which keyword defines a normal function? | Từ khóa nào định nghĩa hàm thông thường?**

A. `return` | `return`

B. `lambda` | `lambda`

C. `if` | `if`

D. `def` | `def`

**Đáp án: D**

**Giải thích:** `def` mở đầu định nghĩa hàm có tên, tiếp theo là tham số, dấu hai chấm và thân hàm thụt lề. `lambda` tạo biểu thức hàm, còn `return` dùng bên trong thân để trả kết quả.

**Q6. Which keyword sends a value back to the caller? | Từ khóa nào trả giá trị về nơi gọi?**

A. `lambda` | `lambda`

B. `if` | `if`

C. `def` | `def`

D. `return` | `return`

**Đáp án: D**

**Giải thích:** `return` kết thúc lần gọi hàm hiện tại và chuyển giá trị đã chỉ ra về nơi gọi. Với `return x * 2`, nơi gọi nhận giá trị gấp đôi; `print(x * 2)` chỉ hiển thị rồi trả `None`.

**Q7. Which keyword defines a short anonymous function expression? | Từ khóa nào tạo biểu thức hàm ngắn không tên?**

A. `def` | `def`

B. `return` | `return`

C. `lambda` | `lambda`

D. `if` | `if`

**Đáp án: C**

**Giải thích:** `lambda` tạo hàm từ một biểu thức, chẳng hạn `lambda x: x * 2`. Hàm có thể gán cho tên hoặc truyền làm đối số, khác `def` mở định nghĩa hàm theo dạng câu lệnh.

**Q8. Which keyword supplies a conditional branch inside a function? | Từ khóa nào tạo nhánh điều kiện bên trong hàm?**

A. `lambda` | `lambda`

B. `if` | `if`

C. `def` | `def`

D. `return` | `return`

**Đáp án: B**

**Giải thích:** `if` mở nhánh điều kiện bên trong hàm, giúp hàm chọn đường thực thi theo đầu vào. Bản thân `if` không tạo hàm và cũng không trả giá trị về nơi gọi.

**Q9. What does a default parameter provide? | Tham số mặc định có tác dụng gì?**

A. A value calculated only after the function returns | Giá trị chỉ tính sau khi hàm trả về

B. A value that must be supplied for every call | Giá trị bắt buộc phải truyền ở mọi lần gọi

C. A fallback value used when the caller omits an argument | Giá trị dự phòng khi nơi gọi không truyền đối số

D. A value that overrides every explicit argument | Giá trị ghi đè mọi đối số truyền vào

**Đáp án: C**

**Giải thích:** Giá trị mặc định của tham số được dùng khi nơi gọi bỏ qua đối số đó; với `def greet(name='An')`, `greet()` dùng `'An'`. Nếu gọi `greet('Binh')` thì giá trị truyền vào thay mặc định, vì vậy đây là dự phòng chứ không phải giá trị bắt buộc.

**Q10. What is a keyword argument? | Đối số theo tên là gì?**

A. An argument supplied using its parameter's name | Đối số truyền bằng tên tham số

B. A local variable defined outside the function | Biến cục bộ định nghĩa ngoài hàm

C. A function name passed without calling | Tên hàm được truyền mà không gọi

D. An argument always matched only by position | Đối số luôn ghép bằng vị trí

**Đáp án: A**

**Giải thích:** Đối số theo tên nêu rõ tên tham số lúc gọi, ví dụ `greet(name='An')`. Nó khác đối số theo vị trí như `greet('An')`, vốn ghép với tham số dựa trên vị trí truyền vào.

**Q11. What does `sorted(rows, key=func)` use `func` for? | Trong `sorted(rows, key=func)`, func dùng để làm gì?**

A. Filtering out all false-valued items before sorting | Loại mọi phần tử có giá trị sai trước khi sắp

B. Computing a sort key for each item | Tính khóa sắp xếp cho từng phần tử

C. Replacing every row with `None` | Thay mỗi hàng bằng `None`

D. Printing each row during sorting | In từng hàng trong lúc sắp

**Đáp án: B**

**Giải thích:** Trong `sorted(rows, key=func)`, `func` tính giá trị khóa so sánh cho từng phần tử; phép sắp xếp dùng các khóa đó. Ví dụ `key=len` sẽ ưu tiên chuỗi ngắn trước theo độ dài thay vì thứ tự chữ cái.

**Q12. What does `filter(test, items)` keep? | `filter(test, items)` giữ gì?**

A. Only items whose test result is false | Chỉ phần tử có kết quả kiểm tra sai

B. Items in descending order | Phần tử theo thứ tự giảm dần

C. Items for which `test(item)` is truthy | Phần tử mà `test(item)` có giá trị đúng

D. All items, regardless of the test | Mọi phần tử, bất kể phép kiểm tra

**Đáp án: C**

**Giải thích:** `filter(test, items)` chọn phần tử mà `test(item)` có giá trị đúng, trả iterator trong Python 3. Với `filter(lambda x: x > 0, [-1,2])`, chuyển sang `list` được `[2]`, không phải mọi phần tử ban đầu.

**Q13. What is a local variable? | Biến cục bộ là gì?**

A. Any name defined at module level | Bất kỳ tên nào khai báo cấp module

B. A name automatically shared by every function | Tên tự chia sẻ cho mọi hàm

C. A name that can never change value | Tên không bao giờ đổi giá trị

D. A name bound within a function's local scope | Tên được gán trong phạm vi cục bộ hàm

**Đáp án: D**

**Giải thích:** Biến cục bộ là tên được gán trong phạm vi cục bộ của hàm, như `total` gán trong `def add():`. Nó không tự tồn tại ngoài hàm, khác tên toàn cục khai báo ở cấp module.

**Q14. What is a global variable? | Biến toàn cục là gì?**

A. A name bound at module level | Tên được gán ở cấp module

B. A name that exists only inside a class | Tên chỉ tồn tại trong class

C. A name inaccessible to all functions | Tên mọi hàm đều không truy cập được

D. A name created only by `lambda` | Tên chỉ do `lambda` tạo

**Đáp án: A**

**Giải thích:** Biến toàn cục là tên được gán ở cấp module và thường có thể đọc trong hàm nếu không bị che khuất. Muốn gán lại chính biến toàn cục từ trong hàm thường phải khai báo `global`, khác việc chỉ đọc giá trị.

**Q15. What is a lambda expression limited to? | Nội dung của lambda bị giới hạn như thế nào?**

A. A complete `try/except` statement block | Khối câu lệnh `try/except` đầy đủ

B. A single expression | Một biểu thức

C. Only a numeric literal | Chỉ một literal số

D. A series of ordinary statements | Chuỗi các câu lệnh thông thường

**Đáp án: B**

**Giải thích:** Thân `lambda` trong Python chỉ chứa một biểu thức và giá trị biểu thức trở thành kết quả hàm. Nó không chứa khối nhiều câu lệnh thông thường như chuỗi lệnh `for` và gán; cần dùng `def` trong trường hợp đó.

**Q16. What is a closure? | Closure là gì?**

A. A function forced to return `None` | Hàm bị buộc trả `None`

B. A function that prints its enclosing scope | Hàm in phạm vi bao ngoài

C. A function that discards all free variables | Hàm loại bỏ mọi biến tự do

D. A function whose enclosing names remain accessible | Hàm vẫn truy cập được tên của phạm vi bao ngoài

**Đáp án: D**

**Giải thích:** Closure là hàm vẫn truy cập được các tên thuộc phạm vi bao ngoài, kể cả sau khi hàm ngoài đã trả về. Nó giữ liên kết tham chiếu tới các tên đó chứ không nhất thiết chụp cố định giá trị tại một thời điểm.

**Q17. When a function reaches its end without executing `return`, what value does it return? | Khi hàm chạy đến cuối mà không thực hiện `return`, nó trả giá trị nào?**

A. `None` | `None`

B. An empty string `''` | Chuỗi rỗng `''`

C. The last local variable | Biến cục bộ cuối

D. `NameError` | `NameError`

**Đáp án: A**

**Giải thích:** Nếu hàm chạy đến cuối mà không có `return` tường minh, Python ngầm trả `None`. Hàm vẫn có thể in thông báo nhưng việc in không biến thông báo đó thành giá trị trả về.

**Q18. What does `print()` do instead of returning a useful result? | `print()` làm gì thay vì trả một kết quả để tính tiếp?**

A. Displays output while returning `None` | Hiển thị đầu ra và trả `None`

B. Returns a tuple with the printed text | Trả Tuple chứa văn bản đã in

C. Raises `TypeError` whenever called | Mỗi khi gọi đều gây `TypeError`

D. Always returns the printed string | Luôn trả chuỗi đã in

**Đáp án: A**

**Giải thích:** `print()` đưa văn bản ra đầu ra chuẩn và giá trị trả về là `None`. Ví dụ `result = print('Hi')` hiển thị `Hi` nhưng lưu `None` vào `result`; dùng `return` trong hàm nếu mã phía sau cần kết quả.

**Q19. What does a function's `return a, b` actually return? | `return a, b` thực chất trả gì?**

A. The result of adding `a` and `b` | Kết quả cộng `a` với `b`

B. A tuple containing both values | Tuple chứa cả hai giá trị

C. A list containing both values | List chứa cả hai giá trị

D. The two values as separate function return objects | Hai giá trị thành hai đối tượng trả về riêng

**Đáp án: B**

**Giải thích:** Biểu thức trả về có các giá trị cách nhau bằng dấu phẩy đóng gói chúng thành Tuple, nên `return a, b` trả `(a, b)`. Nơi gọi có thể giải nén ra hai tên, nhưng hàm thực tế trả một đối tượng Tuple.

**Q20. What happens when code outside a function reads an undefined local name? | Đọc biến cục bộ không tồn tại ở ngoài hàm gây gì?**

A. The most recent printed value is used | Dùng giá trị vừa được in

B. The local name is exported automatically | Tên cục bộ tự xuất ra ngoài

C. `NameError` for the undefined name | `NameError` vì tên chưa được định nghĩa

D. `None` is silently substituted | Tự thay bằng `None`

**Đáp án: C**

**Giải thích:** Tên cục bộ chỉ được gán bên trong hàm không tự tồn tại ở phạm vi module. Đọc tên chưa được định nghĩa ở ngoài gây `NameError`; cần trả về tường minh hoặc lưu vào liên kết có thể truy cập.

## PY-10 — PY-10 — Class, Object, constructor và đóng gói

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a class in Python OOP? | Class trong OOP Python là gì?**

A. Only a built-in Python function | Chỉ một hàm Python có sẵn

B. A template defining object state and behavior | Khuôn mẫu định nghĩa trạng thái và hành vi đối tượng

C. A concrete instance created from a class | Instance cụ thể được tạo từ class

D. A value stored in one object | Giá trị lưu trong một đối tượng

**Đáp án: B**

**Giải thích:** Class định nghĩa cấu trúc dùng chung cho các đối tượng, gồm thuộc tính và phương thức. Ví dụ class `Student` có thể định nghĩa trường tên và phương thức `display()`; từng sinh viên là một instance của class đó.

**Q2. What is an object or instance? | Object hay instance là gì?**

A. A statement defining a new class | Câu lệnh định nghĩa class mới

B. A concrete instance of a class | Instance cụ thể của class

C. An attribute name only | Chỉ tên thuộc tính

D. A block of import statements | Khối lệnh import

**Đáp án: B**

**Giải thích:** Object hay instance là giá trị cụ thể được tạo từ class. Hai instance `Student` có thể chạy cùng các phương thức nhưng có giá trị `name` khác nhau, vì thế class không đồng nghĩa với một đối tượng.

**Q3. What is an attribute? | Attribute là gì?**

A. A method invocation | Lời gọi phương thức

B. Data or a value associated with an object | Dữ liệu hoặc giá trị gắn với đối tượng

C. A syntax token beginning every class | Token cú pháp bắt đầu mọi class

D. A class declaration | Câu lệnh khai báo class

**Đáp án: B**

**Giải thích:** Attribute là dữ liệu hoặc giá trị gắn với đối tượng được truy cập qua tên, như `student.name`. Nó biểu diễn trạng thái hay đặc điểm, còn phương thức được gọi để thực hiện hành vi.

**Q4. What is an instance method? | Phương thức đối tượng là gì?**

A. An object stored in a list | Đối tượng được lưu trong List

B. A value that cannot be called | Giá trị không thể gọi

C. A class-defined function operating on an instance | Hàm định nghĩa trong class thao tác trên instance

D. A class with no methods | Class không có phương thức

**Đáp án: C**

**Giải thích:** Phương thức instance là hàm định nghĩa trong class và nhận đối tượng làm đối số đầu khi gọi qua instance. Với `student.show()`, phương thức có thể đọc `self.name`; thuộc tính như `student.name` là dữ liệu, không phải lời gọi phương thức.

**Q5. Which syntax begins a class definition? | Cú pháp nào mở đầu định nghĩa class?**

A. `__init__` | `__init__`

B. `self` | `self`

C. `class Student:` | `class Student:`

D. `Student()` | `Student()`

**Đáp án: C**

**Giải thích:** `class Student:` mở đầu định nghĩa class; các lệnh thụt lề bên dưới tạo thân class. Gọi `Student()` là thao tác khác: tạo instance sau khi class phù hợp đã được định nghĩa.

**Q6. If `Student` requires no constructor arguments, which expression creates a Student instance? | Nếu `Student` không yêu cầu đối số khởi tạo, biểu thức nào tạo một instance Student?**

A. `Student()` | `Student()`

B. `def Student:` | `def Student:`

C. `self.Student` | `self.Student`

D. `class Student:` | `class Student:`

**Đáp án: A**

**Giải thích:** Gọi `Student()` tạo instance nếu class có thể khởi tạo mà không cần đối số bắt buộc. Nếu `__init__` yêu cầu đầu vào khác thì phải truyền chúng khi gọi, không được cho rằng ngoặc trống luôn hợp lệ.

**Q7. Which special method initializes instance attributes? | Phương thức đặc biệt nào khởi tạo thuộc tính đối tượng?**

A. `__repr__` | `__repr__`

B. `__newstate__` | `__newstate__`

C. `__str__` | `__str__`

D. `__init__` | `__init__`

**Đáp án: D**

**Giải thích:** `__init__` khởi tạo instance vừa được tạo, thường gán thuộc tính như `self.name = name`. Python tạo đối tượng trước rồi mới gọi hàm khởi tạo; bản thân `__init__` không thực hiện cấp phát đối tượng.

**Q8. What does `self` refer to in an instance method? | `self` trong phương thức đối tượng chỉ gì?**

A. The class object, never an instance | Đối tượng class, không bao giờ là instance

B. The first attribute value | Giá trị thuộc tính đầu tiên

C. A newly created unrelated object | Đối tượng khác vừa được tạo

D. The instance receiving the method call | Instance nhận lời gọi phương thức

**Đáp án: D**

**Giải thích:** Trong phương thức instance thông thường, `self` chỉ đối tượng cụ thể nhận lời gọi. Vì vậy `a.show()` và `b.show()` có thể đọc các thuộc tính khác nhau qua `self` dù cùng định nghĩa class.

**Q9. What does `self.name = name` do? | `self.name = name` làm gì?**

A. Stores `name` on the current instance | Lưu `name` trên instance hiện tại

B. Sets the same name on all instances | Đặt cùng tên trên mọi instance

C. Changes the class's name | Đổi tên class

D. Calls a method named `name` | Gọi phương thức tên `name`

**Đáp án: A**

**Giải thích:** `self.name = name` gán giá trị tham số `name` cho thuộc tính của instance hiện tại. Vì vậy mỗi đối tượng có thể mang tên khác nhau; lệnh không tạo một thuộc tính cấp class được dùng chung.

**Q10. What does `__str__` normally customize? | `__str__` thường tùy chỉnh điều gì?**

A. The readable string representation of an object | Biểu diễn chuỗi dễ đọc của đối tượng

B. The list of all class attributes | Danh sách mọi thuộc tính class

C. The class inheritance hierarchy | Hệ phân cấp kế thừa class

D. The instance's constructor arguments | Các đối số khởi tạo instance

**Đáp án: A**

**Giải thích:** `__str__` điều khiển chuỗi dễ đọc trả về từ `str(obj)` và thường được `print(obj)` hiển thị. Phương thức này phải trả một chuỗi thay vì tự in trực tiếp; nó khác `__init__` dùng để khởi tạo trạng thái.

**Q11. What does `raise ValueError(...)` do? | `raise ValueError(...)` làm gì?**

A. Raises an exception for an invalid value | Phát sinh ngoại lệ cho giá trị không hợp lệ

B. Marks an attribute private | Đánh dấu thuộc tính riêng tư

C. Converts invalid values to `None` | Chuyển giá trị sai thành `None`

D. Silently ignores invalid data | Lặng lẽ bỏ qua dữ liệu sai

**Đáp án: A**

**Giải thích:** `raise ValueError(...)` báo giá trị đầu vào không hợp lệ và ngắt luồng bình thường bằng một ngoại lệ. Ví dụ setter có thể từ chối tuổi âm thay vì lặng lẽ lưu trạng thái không hợp lý.

**Q12. What does the prefix `_value` conventionally mean? | Tiền tố `_value` theo quy ước có nghĩa gì?**

A. A constant that cannot be changed | Hằng không thể thay đổi

B. An attribute invisible to external code | Thuộc tính mã ngoài không thể thấy

C. An internal-use detail by convention | Chi tiết sử dụng nội bộ theo quy ước

D. An automatically encrypted value | Giá trị được tự động mã hóa

**Đáp án: C**

**Giải thích:** Một dấu gạch dưới đầu tên như `_value` theo quy ước đánh dấu chi tiết nội bộ. Python không thực thi tính riêng tư chỉ nhờ cách đặt tên này, nên mã bên ngoài vẫn có thể đọc thuộc tính nếu nó tồn tại.

**Q13. What is encapsulation? | Đóng gói trong OOP là gì?**

A. Copying every attribute into a global variable | Sao chép mọi thuộc tính sang biến toàn cục

B. Converting methods into strings | Chuyển phương thức thành chuỗi

C. Creating a new instance on every access | Tạo instance mới mỗi lần truy cập

D. Grouping related data and methods | Gom dữ liệu và phương thức liên quan

**Đáp án: D**

**Giải thích:** Đóng gói gom dữ liệu và các thao tác liên quan vào cùng class hoặc giao diện đối tượng. Ví dụ phương thức của `BankAccount` có thể cập nhật số dư kèm kiểm tra thay vì để mọi nơi gọi tự sửa các biến rời rạc.

**Q14. Why validate values in a setter method? | Vì sao kiểm tra dữ liệu trong setter?**

A. To make every instance share its private data | Buộc mọi instance chia sẻ dữ liệu riêng

B. To prevent all future method calls | Ngăn mọi lời gọi phương thức sau đó

C. To bypass all input validation | Bỏ qua toàn bộ kiểm tra dữ liệu

D. To validate inputs and preserve valid object state | Kiểm tra đầu vào và giữ trạng thái hợp lệ

**Đáp án: D**

**Giải thích:** Setter kiểm tra dữ liệu trước khi thay đổi trạng thái đối tượng, giúp giữ các ràng buộc như tuổi không được âm. Nếu thiếu kiểm tra, nơi gọi có thể lưu giá trị sai khiến phương thức khác hoạt động không đúng.

**Q15. How do two instances of the same class relate? | Hai đối tượng cùng class có quan hệ gì?**

A. They always share all instance attribute values | Chúng luôn dùng chung mọi giá trị thuộc tính instance

B. They cannot invoke the same methods | Chúng không thể gọi cùng phương thức

C. They share class behavior but can have different states | Chúng chia sẻ hành vi class nhưng có trạng thái khác nhau

D. They are the same object in memory | Chúng là cùng một đối tượng trong bộ nhớ

**Đáp án: C**

**Giải thích:** Các instance cùng class dùng chung định nghĩa phương thức nhưng có thể chứa các thuộc tính instance riêng. Nếu `a.name='An'` và `b.name='Binh'`, sửa `a.name` không tự thay đổi `b.name`.

**Q16. What is a class attribute? | Thuộc tính cấp class là gì?**

A. A method's local variable | Biến cục bộ của phương thức

B. An attribute defined on the class and found by lookup | Thuộc tính định nghĩa trên class và được tìm bằng tra cứu

C. An attribute defined on an object instance only | Thuộc tính chỉ định nghĩa trên instance

D. A required parameter of `__init__` | Tham số bắt buộc của `__init__`

**Đáp án: B**

**Giải thích:** Thuộc tính cấp class được khai báo trên class thay vì riêng từng instance và được tìm thấy khi tra cứu qua class hoặc instance. Instance có thể che khuất thuộc tính đó bằng giá trị riêng, nên đây không phải trường luôn đồng bộ vĩnh viễn.

**Q17. What does `obj.method()` do? | `obj.method()` làm gì?**

A. Invokes a method on `obj` | Gọi phương thức trên `obj`

B. Returns the object's class without invoking anything | Trả class của đối tượng mà không gọi gì

C. Always creates a new instance | Luôn tạo instance mới

D. Always deletes an attribute | Luôn xóa thuộc tính

**Đáp án: A**

**Giải thích:** `obj.method()` tìm và gọi phương thức có tên trên `obj`, thông thường truyền instance đó làm `self`. Chỉ đọc `obj.attribute` thì lấy giá trị, không tự gọi phương thức.

**Q18. When the attribute exists, what does `obj.attribute` read? | Khi thuộc tính tồn tại, `obj.attribute` đọc gì?**

A. Creates a new method automatically | Tự tạo phương thức mới

B. Reads the named attribute on `obj` | Đọc thuộc tính có tên trên `obj`

C. Invokes every method of the object | Gọi mọi phương thức của đối tượng

D. Returns `True` only for class attributes | Chỉ trả `True` với thuộc tính cấp class

**Đáp án: B**

**Giải thích:** `obj.attribute` truy cập giá trị của thuộc tính có tên nếu nó tồn tại. Khác `obj.method()`, biểu thức không gọi hàm; nếu thiếu thuộc tính, Python thông thường phát sinh `AttributeError`.

**Q19. What does `isinstance(obj, Student)` check? | `isinstance(obj, Student)` kiểm tra gì?**

A. The object's exact class only, excluding subclasses | Chỉ class chính xác, loại class con

B. Whether the object has a method named `Student` | Đối tượng có phương thức tên `Student` không

C. Whether the object is a `Student` or its subclass | Đối tượng thuộc `Student` hay class con không

D. The class name as a string | Tên class ở dạng chuỗi

**Đáp án: C**

**Giải thích:** `isinstance(obj, Student)` đúng khi `obj` thuộc class `Student` hoặc một class con của nó. Ngược lại, `type(obj) is Student` chỉ kiểm tra class thực tế chính xác và loại các instance của class con.

**Q20. What does `type(obj)` return? | `type(obj)` trả về gì?**

A. Whether a class membership test is true | Phép kiểm tra thuộc class có đúng không

B. The object itself with unchanged type | Chính đối tượng và kiểu không đổi

C. A Boolean checking only its attributes | Boolean chỉ kiểm tra thuộc tính

D. The object's actual runtime class | Class thực tế của đối tượng khi chạy

**Đáp án: D**

**Giải thích:** `type(obj)` trả về class thực tế của đối tượng lúc chạy, chẳng hạn `Student`. `isinstance(obj, Student)` thì trả Boolean về quan hệ thuộc class và có thể chấp nhận instance của class con.

## PY-11 — PY-11 — Kế thừa, đa hình và lớp trừu tượng ABC

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What does class inheritance primarily enable? | Kế thừa lớp chủ yếu giúp gì?**

A. Convert a class into a file | Chuyển lớp thành tệp

B. Reuse and extend behavior of a parent class | Dùng lại và mở rộng hành vi của lớp cha

C. Copy every object in memory | Sao chép mọi đối tượng trong bộ nhớ

D. Prevent all method calls | Ngăn mọi lời gọi phương thức

**Đáp án: B**

**Giải thích:** Kế thừa giúp lớp con dùng lại phương thức của lớp cha và bổ sung hành vi riêng. Ví dụ `Dog(Animal)` có thể kế thừa `eat()` rồi thêm `bark()`; kế thừa không sao chép mọi đối tượng đã tạo.

**Q2. What does `class Dog(Animal):` express? | `class Dog(Animal):` thể hiện điều gì?**

A. Dog inherits from Animal | Dog kế thừa Animal

B. Dog is a function inside Animal | Dog là hàm trong Animal

C. Animal inherits from Dog | Animal kế thừa Dog

D. Dog is an instance of Animal | Dog là đối tượng tạo từ Animal

**Đáp án: A**

**Giải thích:** Trong `class Dog(Animal):`, `Dog` là lớp con còn `Animal` là lớp cơ sở. Cú pháp khai báo quan hệ kế thừa, không tạo đối tượng `Dog` mới hay một hàm bên trong `Animal`.

**Q3. Why call `super().__init__(name)` in a subclass? | Vì sao lớp con gọi `super().__init__(name)`?**

A. To delete the parent class | Để xóa lớp cha

B. To replace every attribute with None | Để thay mọi thuộc tính bằng None

C. To make the child an abstract class | Để biến lớp con thành lớp trừu tượng

D. To initialize inherited parent state | Để khởi tạo dữ liệu chung từ lớp cha

**Đáp án: D**

**Giải thích:** `super().__init__(name)` chuyển việc khởi tạo cho lớp kế tiếp trong thứ tự phân giải phương thức, thường là lớp cha. Nếu hàm đó gán `self.name`, lớp con dùng được thuộc tính ấy mà không phải viết lặp phần khởi tạo.

**Q4. Which statement best describes polymorphism? | Câu nào mô tả đúng đa hình?**

A. A child class cannot override methods | Lớp con không thể ghi đè phương thức

B. All methods must have different names | Mọi phương thức phải có tên khác nhau

C. Different objects respond to the same method call | Các đối tượng khác nhau xử lý cùng một lời gọi phương thức

D. All objects must store identical values | Mọi đối tượng phải có giá trị giống nhau

**Đáp án: C**

**Giải thích:** Đa hình cho phép mã gọi cùng một thao tác trên nhiều đối tượng tương thích. Chẳng hạn `dog.sound()` và `cat.sound()` có thể cho âm thanh khác nhau dù đều gọi `sound()`.

**Q5. What is method overriding? | Ghi đè phương thức là gì?**

A. Removing every inherited attribute | Xóa mọi thuộc tính kế thừa

B. Calling the parent method unchanged | Gọi nguyên phương thức lớp cha

C. Defining a same-named method in a subclass | Định nghĩa lại phương thức cùng tên ở lớp con

D. Changing a local variable only | Chỉ thay đổi một biến cục bộ

**Đáp án: C**

**Giải thích:** Ghi đè xảy ra khi lớp con định nghĩa phương thức trùng tên với phương thức kế thừa. Gọi trên đối tượng lớp con thường chọn bản của lớp con, nhưng phương thức gốc của lớp cha vẫn tồn tại.

**Q6. What does `@abstractmethod` mark? | `@abstractmethod` đánh dấu điều gì?**

A. A property unique to integers | Thuộc tính riêng của số nguyên

B. A method that can never be called | Phương thức không bao giờ được gọi

C. A method that prints automatically | Phương thức tự động in

D. A method subclasses must implement to become concrete | Phương thức lớp con phải triển khai để có thể khởi tạo

**Đáp án: D**

**Giải thích:** Khi lớp dùng cơ chế ABC của Python, `@abstractmethod` đánh dấu yêu cầu mà lớp con cụ thể phải đáp ứng. Phương thức trừu tượng vẫn có thể có phần thân; hạn chế nằm ở việc tạo đối tượng từ lớp còn yêu cầu trừu tượng chưa hoàn thành.

**Q7. Is inheriting from `ABC` alone enough to require an override? | Chỉ kế thừa `ABC` có buộc ghi đè phương thức không?**

A. Yes, every method becomes abstract | Có, mọi phương thức đều trừu tượng

B. No, an abstract method must be declared | Không, cần khai báo phương thức trừu tượng

C. Yes, all subclass methods are deleted | Có, mọi phương thức lớp con bị xóa

D. No, ABC forbids inheritance | Không, ABC cấm kế thừa

**Đáp án: B**

**Giải thích:** Kế thừa `ABC` bật cơ chế lớp trừu tượng nhưng không tự khiến mọi phương thức thành trừu tượng. Khai báo `@abstractmethod` phía trên `def area(self):` mới đặt ra yêu cầu trừu tượng cụ thể.

**Q8. What happens if an abstract method is left unimplemented? | Điều gì xảy ra nếu phương thức trừu tượng chưa được cài đặt?**

A. The concrete instance cannot be created | Không thể tạo đối tượng từ lớp còn phương thức trừu tượng

B. The method automatically sends an email | Phương thức tự gửi email

C. The base class is erased | Lớp cha bị xóa

D. Python silently returns zero | Python âm thầm trả về 0

**Đáp án: A**

**Giải thích:** Nếu lớp con vẫn còn phương thức trừu tượng, Python từ chối tạo instance và báo `TypeError`. Cài đặt đầy đủ các phương thức bắt buộc mới giúp lớp có thể khởi tạo; chỉ kế thừa tên phương thức là chưa đủ.

**Q9. What does `isinstance(obj, Parent)` check? | `isinstance(obj, Parent)` kiểm tra gì?**

A. Whether obj is an instance of Parent or its subclasses | obj có thuộc Parent hoặc lớp con hay không

B. Whether obj is a string | obj có phải chuỗi không

C. Whether Parent has no methods | Parent có rỗng phương thức không

D. Whether obj has been printed | obj đã được in hay chưa

**Đáp án: A**

**Giải thích:** `isinstance(obj, Parent)` kiểm tra đối tượng thuộc `Parent` hoặc lớp con tương thích và trả Boolean. Với `Child(Parent)` thông thường, `isinstance(Child(), Parent)` là `True`, khác phép kiểm tra chính xác `type(obj) is Parent`.

**Q10. If a child overrides `fee()`, which version runs on `Child().fee()`? | Nếu lớp con ghi đè `fee()`, `Child().fee()` chạy bản nào?**

A. The parent's version in every case | Luôn bản của lớp cha

B. Neither version | Không chạy bản nào

C. The child's version | Bản của lớp con

D. Both versions automatically | Tự động chạy cả hai bản

**Đáp án: C**

**Giải thích:** Tra cứu phương thức trên instance ưu tiên bản ghi đè ở `Child` trước phương thức cùng tên được kế thừa. Vì vậy `Child().fee()` chạy bản lớp con; bản lớp cha chỉ chạy thêm nếu phương thức ghi đè chủ động gọi nó.

**Q11. Can a child access an inherited attribute set in the parent initializer? | Lớp con có thể dùng thuộc tính khởi tạo ở lớp cha không?**

A. Only if the attribute is named `class` | Chỉ khi tên thuộc tính là class

B. Yes, if the parent initialization is performed | Có, nếu đã thực hiện khởi tạo lớp cha

C. No, inherited fields are always hidden | Không, thuộc tính kế thừa luôn bị ẩn

D. Only for integer attributes | Chỉ với thuộc tính số nguyên

**Đáp án: B**

**Giải thích:** Lớp con đọc được thuộc tính instance đã được phần khởi tạo thích hợp tạo ra. Nếu `Parent.__init__` gán `self.name`, lớp con gọi `super().__init__(name)` sẽ dùng được `self.name`; bỏ bước cần thiết có thể khiến thuộc tính chưa tồn tại.

**Q12. Must polymorphic objects share exactly the same class? | Đối tượng đa hình có bắt buộc cùng một class không?**

A. Yes, they must be identical objects | Có, phải là cùng một đối tượng

B. Yes, inheritance is forbidden | Có, không được kế thừa

C. No, they can provide the same expected method | Không, có thể thuộc các lớp khác nhau nhưng cùng phương thức

D. No, methods must all be absent | Không, không được có phương thức

**Đáp án: C**

**Giải thích:** Đa hình dựa vào giao diện thao tác chung, không yêu cầu các đối tượng cùng lớp cụ thể. Hàm gọi `obj.sound()` có thể làm việc với `Dog` và `Cat` nếu cả hai cung cấp phương thức đó, dù cách triển khai khác nhau.

**Q13. What does `self` refer to inside an instance method? | `self` trong phương thức đối tượng chỉ gì?**

A. Every object in the program | Toàn bộ đối tượng của chương trình

B. The current object receiving the call | Đối tượng hiện tại đang nhận lời gọi

C. Only the parent class definition | Chỉ phần định nghĩa lớp cha

D. The name of the Python module | Tên module Python

**Đáp án: B**

**Giải thích:** Trong phương thức instance thông thường, `self` là đối tượng cụ thể đang nhận lời gọi. Vì vậy `self.name` của `dog1` có thể khác `self.name` của `dog2`; `self` không phải lớp cha hay module.

**Q14. Does overriding a method erase it from the parent class? | Ghi đè phương thức có xóa bản lớp cha không?**

A. Yes, it deletes all parent code | Có, xóa toàn bộ code lớp cha

B. Yes, it deletes the class name | Có, xóa tên lớp

C. Only when `print()` is used | Chỉ khi dùng print

D. No, the parent method still exists | Không, phương thức của lớp cha vẫn tồn tại

**Đáp án: D**

**Giải thích:** Ghi đè ở lớp con thay đổi phương thức được dùng bởi đối tượng lớp con chứ không xóa định nghĩa trên `Parent`. `Parent().fee()` vẫn dùng bản của cha, còn `Child().fee()` có thể dùng bản ghi đè.

**Q15. How can an override call the parent's implementation? | Phương thức ghi đè gọi bản của lớp cha bằng gì?**

A. `super().method()` | `super().method()`

B. `None.method()` | `None.method()`

C. `print(super)` only | Chỉ `print(super)`

D. `del Parent` | `del Parent`

**Đáp án: A**

**Giải thích:** Trong phương thức ghi đè, `super().method()` chuyển lời gọi tới bản kế tiếp trong thứ tự phân giải phương thức, thường là lớp cha. Nó không gọi tùy ý một lớp bất kỳ; với đa kế thừa, lớp kế tiếp có thể khác lớp cha trực tiếp.

**Q16. Can an abstract class define ordinary implemented methods? | Lớp trừu tượng có thể có phương thức thông thường đã triển khai không?**

A. No, it cannot define attributes | Không, không thể có thuộc tính

B. No, it must only contain pass | Không, chỉ được chứa pass

C. Only when it has no subclasses | Chỉ khi không có lớp con

D. Yes, it can provide reusable behavior too | Có, nó vẫn có thể cung cấp hành vi dùng chung

**Đáp án: D**

**Giải thích:** Lớp trừu tượng có thể vừa có hàm hỗ trợ đã cài đặt vừa có yêu cầu trừu tượng. Chẳng hạn lớp cung cấp `describe()` nhưng buộc lớp con triển khai `area()`; trừu tượng không có nghĩa mọi phương thức phải rỗng.

**Q17. What is the relation between overriding and polymorphism? | Ghi đè liên quan gì đến đa hình?**

A. They both mean deleting attributes | Cả hai đều là xóa thuộc tính

B. Overriding can provide distinct behavior for a common call | Ghi đè tạo hành vi khác nhau cho cùng lời gọi

C. They only apply to CSV files | Chúng chỉ áp dụng cho CSV

D. Overriding prevents polymorphism | Ghi đè ngăn đa hình

**Đáp án: B**

**Giải thích:** Ghi đè là một cách thực hiện đa hình: các lớp con cung cấp thân hàm khác nhau cho cùng tên phương thức. Mã có thể gọi `shape.area()` mà không cần tự chọn hàm riêng cho từng loại hình.

**Q18. Which part of `class Child(Parent):` names the superclass? | Trong `class Child(Parent):`, đâu là tên lớp cha?**

A. `class` | `class`

B. `Child` | `Child`

C. `Parent` | `Parent`

D. `:` | `:`

**Đáp án: C**

**Giải thích:** Trong dòng `class Child(Parent):`, tên bên trong ngoặc là lớp cơ sở `Parent`. Lớp mới đang được khai báo là `Child`; dấu hai chấm mở đầu phần thân lớp được thụt lề.

**Q19. What is a good reason to create a shared base class? | Khi nào nên tạo lớp cha chung?**

A. To avoid using any methods | Để không cần phương thức

B. Every object is unrelated | Mọi đối tượng hoàn toàn không liên quan

C. To make all values constant | Để mọi giá trị là hằng số

D. Several subclasses share data or behavior | Nhiều lớp con có chung dữ liệu hoặc hành vi

**Đáp án: D**

**Giải thích:** Lớp cha chung hữu ích khi nhiều lớp con có trạng thái hoặc hành vi giống nhau. Ví dụ `Car` và `Bike` có thể dùng chung giao diện `Vehicle` thay vì lặp định nghĩa cùng hợp đồng phương thức ở từng lớp.

**Q20. Which error may follow if a child skips necessary parent initialization? | Nếu lớp con bỏ khởi tạo lớp cha cần thiết, điều gì có thể xảy ra?**

A. An expected inherited instance attribute may be missing | Một thuộc tính đối tượng cần thiết có thể chưa được tạo

B. All integers turn into strings | Mọi số nguyên biến thành chuỗi

C. Python automatically runs CSV conversion | Python tự chuyển CSV

D. Every method prints twice | Mọi phương thức in hai lần

**Đáp án: A**

**Giải thích:** Nếu lớp con ghi đè `__init__` mà bỏ phần khởi tạo cần thiết của cha, các trường dự kiến có thể chưa được tạo. Đọc `self.name` sau đó có thể gây `AttributeError`; Python không tự gọi hàm khởi tạo cha đã bị ghi đè.

## PY-12 — PY-12 — File I/O, CSV và xử lý ngoại lệ

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

## PY-13 — PY-13 — NumPy ndarray, shape, dtype và axis

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a NumPy `ndarray`? | `ndarray` của NumPy là gì?**

A. A class inheritance rule | Quy tắc kế thừa lớp

B. A Python exception | Một ngoại lệ Python

C. A single text file | Một tệp văn bản đơn

D. An array for data with a common dtype | Mảng dữ liệu có kiểu phần tử chung

**Đáp án: D**

**Giải thích:** `ndarray` lưu phần tử theo một hay nhiều chiều có chỉ số và một `dtype` chung. Ví dụ `np.array([1, 2, 3])` là mảng số một chiều, không phải tệp hay ngoại lệ Python.

**Q2. What does `shape=(3, 2)` mean for a 2-D array? | `shape=(3, 2)` nghĩa là gì với mảng hai chiều?**

A. Only three total elements | Chỉ có ba phần tử

B. Three rows and two columns | Ba hàng và hai cột

C. Two rows and three columns | Hai hàng và ba cột

D. Three dimensions and two values | Ba chiều và hai giá trị

**Đáp án: B**

**Giải thích:** Với mảng hai chiều, `shape` ghi `(số_hàng, số_cột)`. Vì vậy `(3, 2)` là ba quan sát ở các hàng và hai đặc trưng ở các cột, tổng cộng sáu ô dữ liệu.

**Q3. What is the size of an array with shape `(3, 2)`? | Mảng có shape `(3, 2)` chứa bao nhiêu phần tử?**

A. 5 | 5

B. 6 | 6

C. 3 | 3

D. 2 | 2

**Đáp án: B**

**Giải thích:** `size` của ndarray đếm toàn bộ phần tử và bằng tích các kích thước trong `shape`. Với `(3, 2)`, tính `3 × 2 = 6`; cộng hai kích thước lại sẽ cho số phần tử sai.

**Q4. What does `ndim` report? | Thuộc tính `ndim` cho biết gì?**

A. The data type of an element | Kiểu phần tử

B. The number of rows only | Chỉ số hàng

C. The number of array dimensions | Số chiều của mảng

D. The maximum array value | Giá trị lớn nhất

**Đáp án: C**

**Giải thích:** `ndim` cho số trục/chiều, không phải số giá trị được lưu. Ma trận có shape `(3, 2)` có `ndim == 2` dù `size == 6`.

**Q5. What does `dtype` describe? | `dtype` mô tả gì?**

A. The file's extension | Phần mở rộng của file

B. The data type of array elements | Kiểu dữ liệu của các phần tử

C. The mean of all entries | Trung bình các phần tử

D. The array's row count | Số hàng

**Đáp án: B**

**Giải thích:** `dtype` mô tả kiểu và cách biểu diễn chung của các phần tử mảng, như `int64` hoặc `float64`. Nó khác `shape`, vốn cho biết số phần tử trên từng trục.

**Q6. Why specify `dtype=float` when storing decimal scores? | Vì sao dùng `dtype=float` khi lưu điểm có phần lẻ?**

A. To preserve fractional values | Để giữ giá trị có phần thập phân

B. To force integer truncation | Để ép cắt về số nguyên

C. To delete missing records | Để xóa bản ghi thiếu

D. To change rows into columns | Để đổi hàng thành cột

**Đáp án: A**

**Giải thích:** `dtype=float` yêu cầu NumPy lưu giá trị dưới dạng dấu phẩy động để điểm như `8.5` giữ được phần lẻ. Nếu đổi sang kiểu nguyên, phần lẻ có thể bị bỏ trong quá trình chuyển kiểu.

**Q7. For a 2-D array, what does `mean(axis=0)` return? | Với mảng hai chiều, `mean(axis=0)` trả về gì?**

A. Only the first cell | Chỉ ô đầu tiên

B. One mean per column | Một giá trị trung bình cho mỗi cột

C. The original array unchanged | Mảng gốc không đổi

D. One mean per row | Một giá trị trung bình cho mỗi hàng

**Đáp án: B**

**Giải thích:** Với mảng 2D, `axis=0` gộp theo chiều hàng và để lại một kết quả cho từng cột. Với `[[1, 3], [5, 7]]`, `mean(axis=0)` được `[3., 5.]`, không phải các trung bình theo hàng.

**Q8. For a 2-D array, what does `sum(axis=1)` produce? | Với mảng hai chiều, `sum(axis=1)` tạo gì?**

A. A list of column names | List tên cột

B. The shape tuple only | Chỉ tuple shape

C. One sum per column | Một tổng cho mỗi cột

D. One sum per row | Một tổng cho mỗi hàng

**Đáp án: D**

**Giải thích:** `sum(axis=1)` cộng các cột trong từng hàng. Với `[[1, 3], [5, 7]]`, tổng theo hàng là `4` và `12`, tạo kết quả một chiều gồm hai giá trị.

**Q9. Which statement correctly distinguishes `shape` and `size`? | Đâu là điểm khác nhau giữa `shape` và `size`?**

A. shape lists dimensions; size counts elements | shape ghi kích thước từng chiều; size đếm phần tử

B. size gives dtype; shape gives values | size cho kiểu dữ liệu; shape cho giá trị

C. They are always identical numbers | Chúng luôn là cùng một số

D. Both change elements automatically | Cả hai tự đổi phần tử

**Đáp án: A**

**Giải thích:** `shape` là tuple chỉ độ dài từng chiều, còn `size` là một số đếm toàn bộ phần tử. Mảng có shape `(3, 2)` gồm hai chiều và `size == 6`; hai thuộc tính này không tự sắp xếp lại dữ liệu.

**Q10. What does `np.array([1, 2, 3])` create? | `np.array([1, 2, 3])` tạo ra gì?**

A. A one-dimensional NumPy array | Một mảng NumPy một chiều

B. A class named Array | Lớp tên Array

C. A CSV file on disk | File CSV trên đĩa

D. A two-column table | Bảng hai cột

**Đáp án: A**

**Giải thích:** `np.array([1, 2, 3])` tạo ndarray có shape `(3,)`, nghĩa là một chiều chứa ba phần tử. Đây không phải bảng hai cột, vì bảng đó cần cấu trúc hai chiều.

**Q11. What does `np.zeros((2, 3))` create? | `np.zeros((2, 3))` tạo gì?**

A. A 2×3 table of missing strings | Bảng 2×3 gồm chuỗi thiếu

B. A 3×2 array of ones | Mảng 3×2 toàn số 1

C. A 2×3 array initialized to zeros | Mảng 2×3 được khởi tạo toàn số 0

D. An empty array with no elements | Mảng rỗng không có phần tử

**Đáp án: C**

**Giải thích:** `np.zeros((2, 3))` tạo hai hàng và ba cột, mọi ô khởi tạo bằng không. Mặc định các ô thuộc kiểu số thực, không phải chuỗi thiếu dữ liệu hay mảng không có phần tử.

**Q12. How is `np.ones((2, 2))` different from `np.zeros((2, 2))`? | `np.ones((2, 2))` khác `np.zeros((2, 2))` thế nào?**

A. It has four dimensions | Nó có bốn chiều

B. It cannot be used in arithmetic | Nó không thể tính toán

C. It always creates a CSV file | Nó luôn tạo file CSV

D. It initializes entries to one instead of zero | Nó khởi tạo giá trị 1 thay cho 0

**Đáp án: D**

**Giải thích:** `np.ones((2, 2))` và `np.zeros((2, 2))` cùng shape và có bốn ô số. Hàm thứ nhất điền `1`, hàm thứ hai điền `0`; không hàm nào tạo bốn chiều.

**Q13. How do NumPy array and Python List differ in numeric operations? | Mảng NumPy khác List Python về phép toán số như thế nào?**

A. A NumPy array stores only strings | Mảng NumPy chỉ lưu chuỗi

B. A List always multiplies elements element-wise | List luôn nhân từng phần tử

C. A List cannot hold numbers | List không chứa được số

D. NumPy enables element-wise numerical operations | NumPy hỗ trợ phép toán số theo từng phần tử

**Đáp án: D**

**Giải thích:** Với ndarray số, `a * 2` nhân từng phần tử lên hai: `[1, 2]` thành `[2, 4]`. Ngược lại, `[1, 2] * 2` của List Python lặp dãy thành `[1, 2, 1, 2]`.

**Q14. For an array with rows as learners and columns as subjects, what does axis=0 average? | Nếu hàng là học viên và cột là môn, `axis=0` tính trung bình theo gì?**

A. Only the last subject | Chỉ môn cuối

B. Each learner across subjects | Từng học viên qua các môn

C. Each subject across learners | Từng môn qua các học viên

D. Only the first learner | Chỉ học viên đầu

**Đáp án: C**

**Giải thích:** Nếu mỗi hàng là một học viên và mỗi cột là một môn, `mean(axis=0)` tính trung bình qua các học viên cho từng môn riêng. Có hai môn thì được hai trung bình; `axis=1` lại tính trung bình các môn của từng học viên.

**Q15. How many dimensions does a two-dimensional score table have? | Bảng điểm hai chiều có `ndim` bằng bao nhiêu?**

A. The total number of scores | Tổng số điểm

B. 3 | 3

C. 2 | 2

D. 1 | 1

**Đáp án: C**

**Giải thích:** Bảng điểm sắp theo hàng và cột có hai trục, dù có bao nhiêu hàng. Vì vậy `ndim` bằng `2`; tổng số ô điểm cần đọc từ `size`.

**Q16. Which code accesses array shape without computing new values? | Cú pháp nào lấy shape mà không tính thêm dữ liệu?**

A. `X.sort()` | `X.sort()`

B. `X.shape` | `X.shape`

C. `X.delete()` | `X.delete()`

D. `X.write()` | `X.write()`

**Đáp án: B**

**Giải thích:** `X.shape` đọc thuộc tính ndarray, trả tuple kích thước các chiều mà không sửa giá trị. Với bảng ba hàng hai cột, kết quả là `(3, 2)`; `X.sort()` thì thay đổi thứ tự phần tử.

**Q17. Which code counts all array entries? | Cú pháp nào đếm tổng số phần tử mảng?**

A. `X.shape[0]` in every case | Luôn `X.shape[0]`

B. `X.dtype` | `X.dtype`

C. `X.size` | `X.size`

D. `X.mean()` | `X.mean()`

**Đáp án: C**

**Giải thích:** `X.size` đếm phần tử qua toàn bộ các chiều. Với mảng `(3, 2)`, kết quả là `6`, còn `X.shape[0]` chỉ trả số hàng là `3`.

**Q18. For finite floating-point values within the target integer range, what does NumPy `.astype(int)` do to their fractional parts? | Với giá trị dấu phẩy động hữu hạn nằm trong phạm vi kiểu số nguyên đích, NumPy `.astype(int)` xử lý phần lẻ thế nào?**

A. It discards fractional parts toward zero | Bỏ phần lẻ theo hướng về số 0

B. It rounds every value to the nearest integer | Làm tròn mọi giá trị về số nguyên gần nhất

C. It preserves fractional parts unchanged | Giữ nguyên toàn bộ phần lẻ

D. It forces the shape to become `(1, 1)` | Buộc shape chuyển thành `(1, 1)`

**Đáp án: A**

**Giải thích:** Với số thực hữu hạn thuộc phạm vi kiểu nguyên đích, `.astype(int)` bỏ phần lẻ theo hướng về không chứ không làm tròn gần nhất. Vì vậy `[2.9, -2.9]` đổi thành số nguyên `[2, -2]` và vẫn giữ shape một chiều ban đầu.

**Q19. What is the output shape of `X.mean(axis=0)` for `X.shape == (3,2)`? | Nếu `X.shape == (3,2)`, `X.mean(axis=0)` có shape nào?**

A. `(2,)` | `(2,)`

B. `(3,)` | `(3,)`

C. `(3,2)` | `(3,2)`

D. `(1,3)` | `(1,3)`

**Đáp án: A**

**Giải thích:** Ma trận `(3, 2)` gồm ba hàng và hai cột. `mean(axis=0)` gộp ba hàng, để lại một trung bình cho mỗi cột nên shape mặc định là `(2,)`, không phải `(3,)`.

**Q20. Why label the meaning of each row and column? | Vì sao phải nêu rõ ý nghĩa từng hàng, cột?**

A. To convert a matrix into text | Để chuyển ma trận thành chữ

B. To change dtype automatically | Để tự đổi dtype

C. To avoid all numeric calculations | Để tránh mọi phép tính

D. To interpret aggregated results correctly | Để hiểu đúng kết quả tổng hợp

**Đáp án: D**

**Giải thích:** Nhãn hàng và cột cho biết giá trị tổng hợp đang đo cái gì chứ không chỉ cách tính. Nếu hàng là học viên và cột là môn, `mean(axis=0)` trả điểm trung bình từng môn; hiểu ngược cấu trúc sẽ trả lời câu hỏi khác.

## PY-14 — PY-14 — NumPy indexing, slicing, boolean và fancy indexing

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. Where does Python/NumPy indexing begin? | Chỉ số Python/NumPy bắt đầu từ đâu?**

A. -2 | -2

B. 0 | 0

C. The number of dimensions | Số chiều của mảng

D. 1 | 1

**Đáp án: B**

**Giải thích:** Chỉ số bắt đầu từ không: `a[0]` là phần tử đầu, còn `a[1]` là phần tử thứ hai. Chỉ số âm đếm ngược từ cuối.

**Q2. For a 2-D array, what does `X[1, 0]` select? | Trong mảng hai chiều, `X[1, 0]` chọn gì?**

A. Every row, first column | Mọi hàng, cột đầu

B. Row 2, column 1 | Hàng thứ hai, cột đầu tiên

C. All columns of the first row | Mọi cột của hàng đầu

D. Row 1, column 2 | Hàng đầu, cột thứ hai

**Đáp án: B**

**Giải thích:** Mảng 2D được truy cập theo `X[hàng, cột]`, với chỉ số bắt đầu từ không. Vì thế `X[1, 0]` là hàng hai, cột một.

**Q3. What does `a[-1]` mean for a nonempty 1-D array? | `a[-1]` nghĩa là gì với mảng một chiều không rỗng?**

A. An invalid index in all cases | Chỉ số luôn không hợp lệ

B. The last element | Phần tử cuối

C. All negative values | Mọi giá trị âm

D. The first element | Phần tử đầu

**Đáp án: B**

**Giải thích:** Với mảng không rỗng, chỉ số `-1` lấy phần tử cuối; ở `[4, 6, 8]` đó là `8`. Ngược lại, chỉ số `0` lấy phần tử đầu.

**Q4. Which endpoint does a slice `a[1:4]` exclude? | Slice `a[1:4]` không lấy vị trí nào?**

A. Index 3 | Chỉ số 3

B. Index 1 | Chỉ số 1

C. Index 4 | Chỉ số 4

D. Index 2 | Chỉ số 2

**Đáp án: C**

**Giải thích:** Chỉ số dừng của slice không được lấy: `a[1:4]` chọn vị trí 1, 2, 3 nếu có. Vị trí 4 không thuộc lát cắt.

**Q5. What does `X[:, 0]` select? | `X[:, 0]` lấy gì?**

A. Only the top-left value always | Luôn chỉ ô góc trên trái

B. All columns in the first row | Mọi cột ở hàng đầu

C. Only rows with value zero | Chỉ hàng có giá trị 0

D. All rows in the first column | Mọi hàng ở cột đầu

**Đáp án: D**

**Giải thích:** Trong `X[:, 0]`, dấu `:` chọn mọi hàng và `0` chọn cột đầu. Kết quả là dữ liệu theo cột, khác `X[0, :]` lấy một hàng.

**Q6. What does `X[0, :]` select? | `X[0, :]` lấy gì?**

A. All columns of the first row | Mọi cột của hàng đầu

B. The last row | Hàng cuối

C. All rows of the first column | Mọi hàng của cột đầu

D. The diagonal | Đường chéo

**Đáp án: A**

**Giải thích:** `X[0, :]` cố định hàng số không và giữ mọi cột. Với `[[1,2],[3,4]]`, kết quả là hàng đầu `[1,2]`, không phải cột đầu.

**Q7. What does a Boolean mask contain? | Mặt nạ Boolean chứa gì?**

A. Only positive integers | Chỉ số nguyên dương

B. Random floating-point numbers | Số thực ngẫu nhiên

C. Only column names | Chỉ tên cột

D. True/False values indicating which entries to keep | Giá trị True/False cho biết phần tử nào được giữ

**Đáp án: D**

**Giải thích:** Mặt nạ Boolean chứa các vị trí `True` và `False`, thường sinh từ phép so sánh. Với `[4, 8]`, điều kiện `a >= 7` chỉ chọn phần tử thứ hai.

**Q8. What is selected by `a[a >= 7]`? | `a[a >= 7]` chọn gì?**

A. All entries smaller than 7 | Mọi phần tử nhỏ hơn 7

B. Only the element at index 7 | Chỉ phần tử chỉ số 7

C. Elements at least 7 | Các phần tử từ 7 trở lên

D. The first seven entries | Bảy phần tử đầu

**Đáp án: C**

**Giải thích:** Biểu thức so giá trị với ngưỡng 7 rồi giữ phần tử thỏa điều kiện. Với `[4, 7, 9]`, kết quả là `[7, 9]`, không phải phần tử có chỉ số 7.

**Q9. What does `a[[0, 2]]` illustrate? | `a[[0, 2]]` minh họa điều gì?**

A. A logical AND operation | Phép AND logic

B. Slicing one continuous range | Cắt một đoạn liên tục

C. Fancy indexing with selected positions | Fancy indexing chọn các vị trí cụ thể

D. A matrix transpose | Chuyển vị ma trận

**Đáp án: C**

**Giải thích:** `a[[0, 2]]` dùng mảng chỉ số nguyên để chọn các vị trí cụ thể. Nó có thể lấy phần tử đầu và thứ ba không liền nhau, khác với lát cắt liên tục.

**Q10. What is the difference between slicing and fancy indexing? | Slicing khác fancy indexing ở điểm nào?**

A. Both always select entire matrices | Cả hai luôn lấy cả ma trận

B. Slicing requires Boolean values only | Slicing chỉ dùng Boolean

C. Slices describe ranges; fancy indexing specifies index arrays | Slice chỉ đoạn, fancy indexing chỉ mảng vị trí

D. Fancy indexing never uses integers | Fancy indexing không dùng số nguyên

**Đáp án: C**

**Giải thích:** Slice xác định dãy chỉ số có quy luật như `a[1:6:2]`; fancy indexing nguyên chỉ vị trí tùy ý như `a[[5, 1, 5]]`. Fancy indexing có thể lặp hoặc đổi thứ tự vị trí.

**Q11. In NumPy, basic slicing generally returns what? | Basic slicing của NumPy thường trả về gì?**

A. A view of the original data | View chia sẻ dữ liệu với mảng gốc

B. A guaranteed independent copy | Luôn là bản sao độc lập

C. A plain Python set | Một Set Python

D. A new CSV file | File CSV mới

**Đáp án: A**

**Giải thích:** Basic slicing thường trả view chia sẻ bộ nhớ nền. Sửa `part = a[1:3]` có thể ảnh hưởng giá trị gốc tương ứng; hãy dùng `.copy()` khi cần dữ liệu độc lập.

**Q12. Does advanced integer-array indexing generally return a view? | Indexing bằng mảng số nguyên nâng cao thường tạo view không?**

A. Yes, it always shares memory | Có, luôn chia sẻ bộ nhớ

B. No, it generally returns a copy | Không, thường trả bản sao

C. It converts the source to strings | Nó chuyển nguồn thành chuỗi

D. It only returns None | Nó chỉ trả None

**Đáp án: B**

**Giải thích:** Indexing nâng cao bằng số nguyên thường sao chép dữ liệu được chọn thay vì tạo view. Sửa `b = a[[0,2]]` thường không đổi `a`; gán trực tiếp `a[[0,2]] = ...` là thao tác khác.

**Q13. How do you keep source data unchanged before assignment? | Làm sao giữ mảng gốc không đổi trước khi gán?**

A. Make an explicit `copy()` | Tạo bản sao bằng `copy()`

B. Use `del X` first | Xóa X trước

C. Always modify a slice directly | Luôn sửa trực tiếp slice

D. Replace every value with zero | Thay mọi giá trị bằng 0

**Đáp án: A**

**Giải thích:** Lệnh `b = a.copy()` tạo bộ nhớ riêng trước khi sửa. Sau đó gán `b[0] = 9` không đổi `a[0]`, khác với sửa view dùng chung dữ liệu.

**Q14. For shape (3,2), what does `X[:, 1]` return? | Nếu shape là (3,2), `X[:, 1]` trả về gì?**

A. Three values from the second column | Ba giá trị ở cột thứ hai

B. Two values from the first row | Hai giá trị của hàng đầu

C. An array with five values | Mảng năm giá trị

D. One value in the center | Một giá trị giữa bảng

**Đáp án: A**

**Giải thích:** Mảng `(3,2)` có ba hàng hai cột. `X[:, 1]` lấy cột thứ hai qua cả ba hàng, cho kết quả có shape `(3,)`.

**Q15. What does `X[:, [0, 2]]` mean when X has three columns? | `X[:, [0, 2]]` nghĩa là gì nếu X có ba cột?**

A. First two rows, all columns | Hai hàng đầu, mọi cột

B. The sum of columns zero and two | Tổng hai cột 0 và 2

C. All rows and the first and third columns | Mọi hàng, cột thứ nhất và thứ ba

D. Only the second column | Chỉ cột thứ hai

**Đáp án: C**

**Giải thích:** Với ba cột, chỉ số `[0,2]` xác định cột thứ nhất và thứ ba. Dấu hai chấm giữ mọi hàng; biểu thức chọn hai cột chứ không cộng giá trị của chúng.

**Q16. What is the effect of `a[:3]`? | `a[:3]` có tác dụng gì?**

A. Take up to the first three entries | Lấy tối đa ba phần tử đầu

B. Take index 3 alone | Chỉ lấy phần tử số 3

C. Sort entries descending | Sắp phần tử giảm dần

D. Remove the first three entries | Xóa ba phần tử đầu

**Đáp án: A**

**Giải thích:** Bỏ start nghĩa là mặc định từ không, còn chỉ số dừng 3 không được lấy. Vì vậy `a[:3]` lấy tối đa ba phần tử đầu ngay cả khi mảng ngắn hơn; nó không xóa chúng.

**Q17. Which operation filters entire rows based on the first column? | Lệnh nào lọc cả hàng theo điều kiện ở cột đầu?**

A. `X.shape` | `X.shape`

B. `X[:, 0]` alone | Chỉ `X[:, 0]`

C. `X[0, 0]` | `X[0, 0]`

D. `X[X[:, 0] >= 8]` | `X[X[:, 0] >= 8]`

**Đáp án: D**

**Giải thích:** `X[:,0] >= 8` tạo một Boolean cho mỗi hàng bằng cách xét giá trị cột đầu. Dùng mask này để lấy từ `X` sẽ giữ nguyên các hàng thỏa điều kiện, không chỉ phần tử cột đầu.

**Q18. What happens when a scalar index is beyond array bounds? | Khi chỉ số phần tử vượt giới hạn mảng thì sao?**

A. It silently creates a new row | Nó âm thầm tạo hàng mới

B. NumPy raises IndexError | NumPy báo IndexError

C. It converts the array to a dictionary | Nó chuyển mảng thành Dictionary

D. It always returns zero | Nó luôn trả 0

**Đáp án: B**

**Giải thích:** Chỉ số đơn vượt phạm vi một trục mảng gây `IndexError`. Với mảng dài ba phần tử, chỉ số 3 không hợp lệ vì vị trí dương cuối là 2; truy cập không tự mở rộng mảng.

**Q19. How does `X[mask]` differ from `X[[0,2]]`? | `X[mask]` khác `X[[0,2]]` ra sao?**

A. Both necessarily select the same rows | Cả hai luôn lấy cùng hàng

B. A mask automatically sorts values | Mask tự sắp xếp giá trị

C. Indices always compare values to a threshold | Chỉ số luôn so giá trị với ngưỡng

D. A mask selects by condition; indices select by position | Mask chọn theo điều kiện; chỉ số chọn theo vị trí

**Đáp án: D**

**Giải thích:** Mask Boolean đánh dấu vị trí vượt qua phép kiểm tra, còn mảng chỉ số nguyên nêu thẳng các vị trí. Mask dựa trên điều kiện và `X[[0,2]]` không nhất thiết chọn cùng hàng.

**Q20. Why state what rows and columns represent? | Vì sao cần nêu rõ ý nghĩa hàng và cột?**

A. To make all arrays immutable | Để mọi mảng bất biến

B. To force arrays into 1-D | Để buộc mảng thành một chiều

C. To avoid using dtype | Để tránh dtype

D. To select the intended data without swapping dimensions | Để chọn đúng dữ liệu và không đảo chiều

**Đáp án: D**

**Giải thích:** Ý nghĩa từng trục quyết định lát cắt nào trả lời đúng vấn đề. Nếu hàng là học viên và cột là môn, `X[:,0]` lấy điểm môn đầu của mọi học viên, còn `X[0,:]` lấy điểm các môn của học viên đầu.

## PY-15 — PY-15 — NumPy tổng hợp, axis và broadcasting

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is aggregation in NumPy? | Phép tổng hợp trong NumPy là gì?**

A. Reading every file in a folder | Đọc mọi file trong thư mục

B. Converting all arrays to strings | Đổi mọi mảng thành chuỗi

C. Creating a new class by inheritance | Tạo lớp con nhờ kế thừa

D. Combining multiple values into summary statistics | Kết hợp nhiều giá trị thành thống kê tổng hợp

**Đáp án: D**

**Giải thích:** Tổng hợp gộp nhiều giá trị số thành thống kê như `sum`, `mean` hoặc `max`. Với `[2, 4, 6]`, trung bình `4` tóm tắt ba giá trị thay vì giữ từng ô.

**Q2. How does `sum()` differ from `mean()`? | `sum()` khác `mean()` ra sao?**

A. Both always return the same result | Cả hai luôn bằng nhau

B. sum totals values; mean computes their average | sum cộng tổng; mean tính trung bình

C. sum sorts; mean deletes values | sum sắp xếp; mean xóa giá trị

D. mean returns the largest number | mean trả số lớn nhất

**Đáp án: B**

**Giải thích:** `sum` cộng tất cả giá trị được chọn, còn `mean` lấy tổng chia cho số giá trị. Với `[2, 4, 6]`, tổng bằng `12` nhưng trung bình bằng `4`; hai phép không thường bằng nhau.

**Q3. What does `max()` return? | `max()` trả về gì?**

A. The arithmetic average | Trung bình cộng

B. The sum of every negative value | Tổng các số âm

C. The largest value overall or along a specified axis | Giá trị lớn nhất toàn mảng hoặc theo trục được chỉ định

D. The number of columns only | Chỉ số cột

**Đáp án: C**

**Giải thích:** `max` chọn giá trị lớn nhất của mảng hoặc riêng theo trục được chỉ định. Với `[[1, 7], [5, 3]]`, cực đại toàn mảng là `7`, khác `mean` dùng để tính trung bình.

**Q4. In a 2-D array, what does `sum(axis=0)` return? | Trong mảng hai chiều, `sum(axis=0)` trả về gì?**

A. One sum per row | Một tổng cho mỗi hàng

B. One sum per column | Một tổng cho mỗi cột

C. Only the first row | Chỉ hàng đầu

D. A boolean mask | Mặt nạ Boolean

**Đáp án: B**

**Giải thích:** Với mảng 2D, `axis=0` gộp theo chiều hàng và để lại mỗi cột một kết quả. Với `[[1, 2], [3, 4]]`, tổng cột là `[4, 6]`, không phải tổng hàng `[3, 7]`.

**Q5. In a 2-D array, what does `sum(axis=1)` return? | Trong mảng hai chiều, `sum(axis=1)` trả về gì?**

A. The data type of values | Kiểu dữ liệu

B. One sum per column | Một tổng cho mỗi cột

C. Only a scalar index | Chỉ một chỉ số

D. One sum per row | Một tổng cho mỗi hàng

**Đáp án: D**

**Giải thích:** `axis=1` gộp các cột trong từng hàng. Với `[[1, 2], [3, 4]]`, `sum(axis=1)` cho tổng hàng `[3, 7]`; `axis=0` lại cho tổng theo cột.

**Q6. What does broadcasting allow? | Broadcasting cho phép làm gì?**

A. Automatically converting all arrays to CSV | Tự chuyển mọi mảng thành CSV

B. Operating on arrays with compatible shapes | Thực hiện phép toán trên các mảng có shape tương thích

C. Replacing a function with a class | Thay hàm bằng lớp

D. Using any shapes without restrictions | Dùng mọi shape không giới hạn

**Đáp án: B**

**Giải thích:** Broadcasting ghép các chiều có kích thước tương thích để tính theo phần tử mà không phải viết vòng lặp Python. Ví dụ ma trận `(2,3)` cộng được vector `(3,)` trên các hàng, nhưng vector `(2,)` không khớp chiều cuối bằng 3.

**Q7. Why does `a + 1` work on a numeric ndarray? | Vì sao `a + 1` hoạt động với ndarray số?**

A. The array is converted to a string | Mảng bị chuyển thành chuỗi

B. Only the first element is changed | Chỉ phần tử đầu thay đổi

C. The scalar broadcasts to every array element | Số 1 được broadcast tới từng phần tử

D. It performs matrix multiplication | Nó nhân ma trận

**Đáp án: C**

**Giải thích:** Số đơn không có trục mảng gây xung đột nên NumPy broadcast nó tới mọi phần tử. Với `a=[2,4]`, `a + 1` cho `[3,5]`, không phải nhân ma trận hay chỉ sửa phần tử đầu.

**Q8. Which pair of trailing dimensions is broadcast-compatible? | Hai chiều cuối nào tương thích broadcasting?**

A. Only both zero | Chỉ khi cùng bằng 0

B. Equal sizes or one size equal to 1 | Bằng nhau hoặc một chiều có kích thước 1

C. Always 2 and 3 | Luôn là 2 và 3

D. Any unrelated positive sizes | Hai số dương bất kỳ

**Đáp án: B**

**Giải thích:** NumPy đối chiếu các chiều từ phải sang trái: mỗi cặp phải bằng nhau hoặc một bên có kích thước `1`. Vì vậy chiều `3` và `1` tương thích, còn `3` và `2` trên cùng trục thường không tương thích.

**Q9. What happens for incompatible broadcast shapes? | Điều gì xảy ra khi hai shape không tương thích broadcasting?**

A. A ValueError is generally raised | Thường phát sinh ValueError

B. NumPy always returns None | NumPy luôn trả None

C. NumPy silently discards extra rows | NumPy tự bỏ hàng thừa

D. A CSV file is created | Một file CSV được tạo

**Đáp án: A**

**Giải thích:** Shape không tương thích không thể ghép cho phép toán theo phần tử, nên NumPy thường gây `ValueError`. Ví dụ cộng `(2,3)` với `(2,)` lỗi vì hai chiều cuối 3 và 2 không khớp.

**Q10. What is vectorization? | Vectorization là gì?**

A. Removing all calculations | Loại bỏ mọi phép tính

B. Applying numerical operations to arrays directly | Áp dụng phép toán số trực tiếp lên mảng

C. Turning every number into a set | Biến mọi số thành Set

D. Manually printing each item | Tự in từng phần tử

**Đáp án: B**

**Giải thích:** Vector hóa áp dụng phép toán trực tiếp trên mảng NumPy thay vì viết vòng lặp Python qua từng phần tử. Ví dụ `a * 2` nhân mọi ô số, còn tổng hợp như `a.sum()` gộp chúng thành một thống kê.

**Q11. What does NumPy `a * b` do for equal-shaped numeric arrays? | NumPy `a * b` làm gì với hai mảng số cùng shape?**

A. Multiply corresponding elements | Nhân các phần tử cùng vị trí

B. Concatenate the arrays | Nối hai mảng

C. Always compute matrix multiplication | Luôn nhân ma trận

D. Compare the shapes only | Chỉ so sánh shape

**Đáp án: A**

**Giải thích:** Với mảng số NumPy, `*` nhân các ô tương ứng và có thể dùng broadcasting. Vì vậy hai mảng `[2,3]` và `[4,5]` nhân theo phần tử cho `[8,15]`; phép nhân ma trận dùng `@`.

**Q12. Which operator is used for matrix multiplication? | Toán tử nào dùng để nhân ma trận?**

A. `and` | `and`

B. `%` | `%`

C. `@` | `@`

D. `*` alone | Chỉ `*`

**Đáp án: C**

**Giải thích:** Toán tử `@` thực hiện nhân ma trận theo quy tắc đại số tuyến tính, kết hợp hàng với cột. Khác `*`, nó không chỉ nhân các phần tử ở cùng vị trí.

**Q13. For finite numeric array values, what does `np.minimum(a, 10)` do? | Với mảng chứa các giá trị số hữu hạn, `np.minimum(a, 10)` làm gì?**

A. Sum all values and multiply by 10 | Cộng tổng rồi nhân 10

B. Select the largest value only | Chỉ chọn số lớn nhất

C. Remove every element below 10 | Xóa mọi phần tử dưới 10

D. Cap each value at 10 | Giới hạn mỗi giá trị tối đa 10

**Đáp án: D**

**Giải thích:** Với giá trị số hữu hạn, `np.minimum(a, 10)` so từng ô với 10 rồi lấy số nhỏ hơn. Vì vậy `[8,12]` thành `[8,10]`; nó không xóa phần tử nhỏ hơn 10.

**Q14. How does `np.min()` differ from `np.minimum()`? | `np.min()` khác `np.minimum()` thế nào?**

A. min performs sorting descending | min sắp xếp giảm dần

B. Both always return the same shape | Cả hai luôn trả cùng shape

C. min reduces values; minimum compares values element-wise | min tổng hợp lấy cực tiểu; minimum so từng phần tử

D. minimum reads files; min writes files | minimum đọc file, min ghi file

**Đáp án: C**

**Giải thích:** `np.min(a)` mặc định gộp nhiều giá trị thành một cực tiểu, hoặc lấy cực tiểu theo trục được chọn. `np.minimum(a,b)` so từng ô tương ứng có thể dùng broadcasting và thường trả mảng kết quả.

**Q15. For shape `(2,3)`, what is the shape of `sum(axis=1)`? | Với shape `(2,3)`, `sum(axis=1)` có shape nào?**

A. `(2,3)` | `(2,3)`

B. `(1,3)` | `(1,3)`

C. `(3,)` | `(3,)`

D. `(2,)` | `(2,)`

**Đáp án: D**

**Giải thích:** Ma trận shape `(2,3)` có hai hàng, mỗi hàng gồm ba số. `sum(axis=1)` cộng ba cột trong từng hàng, để lại hai tổng với shape `(2,)`.

**Q16. For shape `(2,3)`, what is the shape of `mean(axis=0)`? | Với shape `(2,3)`, `mean(axis=0)` có shape nào?**

A. `(3,2)` | `(3,2)`

B. `(2,3)` | `(2,3)`

C. `(2,)` | `(2,)`

D. `(3,)` | `(3,)`

**Đáp án: D**

**Giải thích:** Với mảng `(2,3)`, `mean(axis=0)` lấy trung bình qua hai hàng cho từng cột. Còn lại ba trung bình cột, nên shape kết quả mặc định là `(3,)`, không phải `(2,)`.

**Q17. Which expression adds a distinct offset to each column of a `(2,3)` matrix? | Biểu thức nào cộng một giá trị riêng cho mỗi cột của ma trận (2,3)?**

A. `X + np.array([1,2,3])` | `X + np.array([1,2,3])`

B. `X.shape + 1` | `X.shape + 1`

C. `X @ np.array([1,2,3])` | `X @ np.array([1,2,3])`

D. `X + np.array([1,2])` | `X + np.array([1,2])`

**Đáp án: A**

**Giải thích:** Vector bù dài ba khớp chiều cuối gồm ba cột của ma trận `(2,3)`. Broadcasting cộng `[1,2,3]` vào cả hai hàng, mỗi cột một mức riêng; vector dài hai không khớp chiều ba.

**Q18. Which statement about broadcasting is correct? | Phát biểu nào đúng về broadcasting?**

A. It may apply a smaller operand without physically copying it | Nó có thể áp toán hạng nhỏ mà không cần sao chép vật lý

B. It permanently changes the array shape in every case | Nó luôn thay shape vĩnh viễn

C. It always duplicates the entire array in memory first | Nó luôn sao chép toàn mảng trước

D. It requires writing explicit for loops | Nó bắt buộc viết vòng for

**Đáp án: A**

**Giải thích:** Broadcasting có thể tái sử dụng toán hạng nhỏ trên các chiều tương thích mà không cần nhân bản vật lý toàn bộ dữ liệu trước. Nó khác việc phải viết vòng lặp hoặc đổi shape của đầu vào vĩnh viễn.

**Q19. How do aggregation and vectorization differ? | Aggregation khác vectorization thế nào?**

A. Aggregation summarizes values; vectorization operates over arrays | Aggregation tổng hợp giá trị; vectorization tính trực tiếp trên mảng

B. Both mean sorting only | Cả hai chỉ là sắp xếp

C. Aggregation never uses NumPy | Aggregation không bao giờ dùng NumPy

D. Vectorization must reduce to one number | Vectorization luôn phải trả một số

**Đáp án: A**

**Giải thích:** Tổng hợp gộp các giá trị thành thống kê, thường giảm một trục, còn phép toán vector hóa tính trực tiếp trên nhiều ô. Ví dụ `a.mean()` tóm tắt dữ liệu, còn `a * 2` biến đổi từng phần tử.

**Q20. Why should data meaning be known before choosing `axis`? | Vì sao phải hiểu ý nghĩa dữ liệu trước khi chọn `axis`?**

A. It avoids specifying array shape | Nó giúp khỏi nêu shape

B. It ensures every value is positive | Nó bảo đảm mọi giá trị dương

C. It determines whether rows or columns answer the question | Nó quyết định cần tổng hợp theo hàng hay cột

D. It changes Python syntax rules | Nó đổi quy tắc cú pháp Python

**Đáp án: C**

**Giải thích:** Chọn trục đúng phụ thuộc ý nghĩa hàng và cột. Nếu hàng là học viên, cột là môn, `mean(axis=0)` tính trung bình từng môn qua học viên, còn `mean(axis=1)` tính trung bình các môn của mỗi học viên.

## PY-16 — PY-16 — NumPy reshape, transpose, ma trận và lưu file

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What does `reshape()` change? | `reshape()` thay đổi điều gì?**

A. The array's shape without changing its total element count | Hình dạng mảng mà không đổi số phần tử

B. Writes an array to an NPY file | Ghi mảng vào tệp NPY

C. Swaps rows and columns | Hoán đổi hàng và cột

D. Matrix multiplication | Phép nhân ma trận

**Đáp án: A**

**Giải thích:** reshape bố trí lại cùng các phần tử theo kích thước mới. Với sáu phần tử, đổi `(2,3)` thành `(3,2)` hợp lệ, nhưng đổi thành `(4,2)` thì không.

**Q2. What does `.T` do to a 2-D array? | `.T` làm gì với mảng 2-D?**

A. The array's shape without changing its total element count | Hình dạng mảng mà không đổi số phần tử

B. Writes an array to an NPY file | Ghi mảng vào tệp NPY

C. Matrix multiplication | Phép nhân ma trận

D. Swaps rows and columns | Hoán đổi hàng và cột

**Đáp án: D**

**Giải thích:** Chuyển vị tráo hai trục của ma trận. Với `[[1,2,3],[4,5,6]]`, chuyển vị tạo ba hàng lần lượt là `[1,4]`, `[2,5]`, `[3,6]`.

**Q3. What does `A @ B` mean for compatible matrices? | `A @ B` nghĩa là gì với các ma trận tương thích?**

A. Swaps rows and columns | Hoán đổi hàng và cột

B. Matrix multiplication | Phép nhân ma trận

C. The array's shape without changing its total element count | Hình dạng mảng mà không đổi số phần tử

D. Writes an array to an NPY file | Ghi mảng vào tệp NPY

**Đáp án: B**

**Giải thích:** Toán tử @ tuân theo quy tắc nhân ma trận chứ không nhân riêng từng ô. Nếu `A` có shape `(2,3)` và `B` là `(3,4)`, thì `A @ B` có shape `(2,4)`; dấu `*` lại nhân từng phần tử.

**Q4. What does `np.save()` do? | `np.save()` làm gì?**

A. Swaps rows and columns | Hoán đổi hàng và cột

B. Matrix multiplication | Phép nhân ma trận

C. Writes an array to an NPY file | Ghi mảng vào tệp NPY

D. The array's shape without changing its total element count | Hình dạng mảng mà không đổi số phần tử

**Đáp án: C**

**Giải thích:** NumPy lưu giá trị, shape và dtype ở định dạng NPY. Khác CSV văn bản, tệp NPY giữ thông tin riêng của NumPy để khôi phục đúng mảng.

**Q5. Which shape specifically has two rows and three columns? | Shape nào có đúng hai hàng và ba cột?**

A. `(3, 2)` | `(3, 2)`

B. `(2, 3)` | `(2, 3)`

C. `(6,)` | `(6,)`

D. `(2, 4)` | `(2, 4)`

**Đáp án: B**

**Giải thích:** Chiều thứ nhất là số hàng và chiều thứ hai là số cột: (2,3). Shape `(2,3)` có tổng sáu ô; `(3,2)` cũng sáu ô nhưng số hàng và cột đảo vị trí.

**Q6. What is the transpose shape of a `(2, 3)` matrix? | Chuyển vị ma trận `(2, 3)` có shape nào?**

A. `(2, 3)` | `(2, 3)`

B. `(2, 4)` | `(2, 4)`

C. `(3, 2)` | `(3, 2)`

D. `(6,)` | `(6,)`

**Đáp án: C**

**Giải thích:** Chuyển vị đảo kích thước hàng và cột. Ma trận `(2,3)` trở thành `(3,2)` sau `.T` vì mỗi cột cũ trở thành một hàng.

**Q7. What is the shape of `(2, 3) @ (3, 4)`? | Phép `(2, 3) @ (3, 4)` cho shape gì?**

A. `(3, 2)` | `(3, 2)`

B. `(2, 3)` | `(2, 3)`

C. `(2, 4)` | `(2, 4)`

D. `(6,)` | `(6,)`

**Đáp án: C**

**Giải thích:** Hai chiều trong cùng bằng 3, còn hai chiều ngoài là 2 và 4. Chiều chung bằng 3 được kết hợp khi nhân, còn hai chiều ngoài 2 và 4 được giữ trong kết quả.

**Q8. What shape has a one-dimensional array of six values? | Mảng một chiều có sáu giá trị có shape nào?**

A. `(3, 2)` | `(3, 2)`

B. `(2, 4)` | `(2, 4)`

C. `(2, 3)` | `(2, 3)`

D. `(6,)` | `(6,)`

**Đáp án: D**

**Giải thích:** Mảng phẳng sáu phần tử có một chiều độ dài sáu. Dấu phẩy trong `(6,)` biểu diễn shape một chiều; `(1,6)` mới có hai chiều.

**Q9. How does `reshape` differ from transpose? | reshape khác transpose ở đâu?**

A. Reshape regroups positions; transpose exchanges axes | Reshape nhóm lại vị trí; transpose đổi trục

B. Converts the array into Python lists or scalars | Chuyển mảng thành List hoặc số Python

C. `*` multiplies element-wise; `@` performs matrix multiplication | `*` nhân từng phần tử; `@` nhân ma trận

D. Reads the saved array | Đọc lại mảng đã lưu

**Đáp án: A**

**Giải thích:** reshape và transpose có thể cho cùng shape nhưng giá trị ở vị trí khác. Với `[[1,2,3],[4,5,6]]`, `reshape(3,2)` tạo các hàng `[1,2]`, `[3,4]`, `[5,6]`, còn `.T` cho `[1,4]`, `[2,5]`, `[3,6]`.

**Q10. How does `*` differ from `@` for numeric ndarrays? | `*` khác `@` thế nào với ndarray số?**

A. Reads the saved array | Đọc lại mảng đã lưu

B. `*` multiplies element-wise; `@` performs matrix multiplication | `*` nhân từng phần tử; `@` nhân ma trận

C. Reshape regroups positions; transpose exchanges axes | Reshape nhóm lại vị trí; transpose đổi trục

D. Converts the array into Python lists or scalars | Chuyển mảng thành List hoặc số Python

**Đáp án: B**

**Giải thích:** Dấu sao nhân theo phần tử, @ tuân quy tắc nhân ma trận. Với hai ma trận 2×2 toàn số một, `A * B` vẫn toàn số một, còn `A @ B` toàn số hai do cộng các tích theo hàng–cột.

**Q11. What does `np.load()` normally do for an NPY file? | `np.load()` làm gì với tệp NPY?**

A. Reads the saved array | Đọc lại mảng đã lưu

B. Reshape regroups positions; transpose exchanges axes | Reshape nhóm lại vị trí; transpose đổi trục

C. `*` multiplies element-wise; `@` performs matrix multiplication | `*` nhân từng phần tử; `@` nhân ma trận

D. Converts the array into Python lists or scalars | Chuyển mảng thành List hoặc số Python

**Đáp án: A**

**Giải thích:** load phục hồi mảng NumPy đã ghi. Với tệp NPY đáng tin cậy, `np.load(path)` khôi phục mảng; tránh bật pickle cho dữ liệu đối tượng chưa tin cậy.

**Q12. What does `array.tolist()` do? | `array.tolist()` làm gì?**

A. Converts the array into Python lists or scalars | Chuyển mảng thành List hoặc số Python

B. Reshape regroups positions; transpose exchanges axes | Reshape nhóm lại vị trí; transpose đổi trục

C. `*` multiplies element-wise; `@` performs matrix multiplication | `*` nhân từng phần tử; `@` nhân ma trận

D. Reads the saved array | Đọc lại mảng đã lưu

**Đáp án: A**

**Giải thích:** tolist chuyển biểu diễn dữ liệu trong bộ nhớ chứ không ghi tệp. Mảng hai chiều chuyển thành List lồng nhau, còn mảng không chiều chuyển thành giá trị vô hướng Python.

**Q13. What happens if you reshape six elements to `(4, 2)`? | Điều gì xảy ra nếu reshape sáu phần tử thành `(4, 2)`?**

A. `allow_pickle=False` | `allow_pickle=False`

B. Left columns and right rows | Số cột bên trái và số hàng bên phải

C. A ValueError due to incompatible element counts | Phát sinh ValueError vì số phần tử không khớp

D. Shape and dtype | Shape và dtype

**Đáp án: C**

**Giải thích:** Bảng 4×2 cần tám giá trị, không phải sáu. Shape `(4,2)` cần `4 × 2 = 8` ô, nên NumPy không thể phân bố đúng sáu phần tử hiện có vào shape này.

**Q14. What must match to multiply two matrices with `@`? | Muốn nhân hai ma trận bằng `@`, chiều nào phải khớp?**

A. `allow_pickle=False` | `allow_pickle=False`

B. Left columns and right rows | Số cột bên trái và số hàng bên phải

C. A ValueError due to incompatible element counts | Phát sinh ValueError vì số phần tử không khớp

D. Shape and dtype | Shape và dtype

**Đáp án: B**

**Giải thích:** Nhân ma trận yêu cầu hai chiều trong bằng nhau. Nếu `A` là `(m,n)` và `B` là `(n,p)`, phép nhân hợp lệ và trả shape `(m,p)`.

**Q15. Which option avoids loading pickled objects from an NPY file? | Tùy chọn nào tránh đọc đối tượng pickle trong file NPY?**

A. A ValueError due to incompatible element counts | Phát sinh ValueError vì số phần tử không khớp

B. Left columns and right rows | Số cột bên trái và số hàng bên phải

C. Shape and dtype | Shape và dtype

D. `allow_pickle=False` | `allow_pickle=False`

**Đáp án: D**

**Giải thích:** Tắt pickle an toàn hơn khi đọc dữ liệu số chưa tin cậy. Với `np.load(path, allow_pickle=False)`, mảng object cần pickle sẽ không được đọc, giúp giảm rủi ro chạy mã từ tệp không tin cậy.

**Q16. What does NPY preserve in addition to array values? | NPY lưu thêm gì ngoài các giá trị?**

A. `allow_pickle=False` | `allow_pickle=False`

B. A ValueError due to incompatible element counts | Phát sinh ValueError vì số phần tử không khớp

C. Shape and dtype | Shape và dtype

D. Left columns and right rows | Số cột bên trái và số hàng bên phải

**Đáp án: C**

**Giải thích:** NPY lưu thông tin để khôi phục cấu trúc và kiểu phần tử. Khác các dòng văn bản thường, shape và dtype được lưu để mảng số `(2,3)` khôi phục đúng cấu trúc.

**Q17. What is a 1-D dot product of two equal-length numeric vectors? | Tích vô hướng của hai vector một chiều bằng nhau độ dài là gì?**

A. The sum of pairwise products | Tổng các tích của từng cặp phần tử

B. A 3-by-3 identity matrix | Ma trận đơn vị 3×3

C. `dtype` | `dtype`

D. `shape` | `shape`

**Đáp án: A**

**Giải thích:** Tích vô hướng nhân các vị trí tương ứng rồi cộng kết quả. Với `[1,2]` và `[3,4]`, tích vô hướng bằng `1×3 + 2×4 = 11`, là một số đơn chứ không phải List.

**Q18. What does `np.eye(3)` create? | `np.eye(3)` tạo gì?**

A. `shape` | `shape`

B. The sum of pairwise products | Tổng các tích của từng cặp phần tử

C. `dtype` | `dtype`

D. A 3-by-3 identity matrix | Ma trận đơn vị 3×3

**Đáp án: D**

**Giải thích:** Ma trận đơn vị có 1 ở đường chéo và 0 ở vị trí khác. Đường chéo chính là `[1,1,1]`, còn sáu ô ngoài chéo đều bằng không; nó không phải ma trận toàn số một.

**Q19. Which property reports the array dimensions? | Thuộc tính nào cho biết kích thước các chiều?**

A. A 3-by-3 identity matrix | Ma trận đơn vị 3×3

B. The sum of pairwise products | Tổng các tích của từng cặp phần tử

C. `dtype` | `dtype`

D. `shape` | `shape`

**Đáp án: D**

**Giải thích:** shape liệt kê độ dài của từng trục mảng. Với mảng 2D ba hàng hai cột, `X.shape` là `(3,2)` chứ không phải kiểu dữ liệu.

**Q20. Which property reports element data type? | Thuộc tính nào cho biết kiểu phần tử?**

A. `shape` | `shape`

B. `dtype` | `dtype`

C. A 3-by-3 identity matrix | Ma trận đơn vị 3×3

D. The sum of pairwise products | Tổng các tích của từng cặp phần tử

**Đáp án: B**

**Giải thích:** dtype ghi kiểu số hoặc kiểu dữ liệu khác của phần tử. Ví dụ mảng số nguyên có dtype nguyên, mảng số thập phân có dtype thực; `shape` mới cho kích thước các chiều.

## PY-17 — PY-17 — Pandas Series, DataFrame và đọc CSV

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a Pandas Series? | Pandas Series là gì?**

A. Parse tabular CSV data into a DataFrame | Đọc dữ liệu CSV thành DataFrame

B. One field across multiple records | Một thuộc tính qua nhiều bản ghi

C. A two-dimensional labeled table | Bảng dữ liệu hai chiều có nhãn

D. A one-dimensional labeled data structure | Cấu trúc dữ liệu một chiều có nhãn

**Đáp án: D**

**Giải thích:** Series liên kết từng giá trị với một nhãn index. Ví dụ `pd.Series([5,6], index=['a','b'])` gắn nhãn `'a'`, `'b'` cho các giá trị, khác với List không có hệ nhãn riêng.

**Q2. What is a Pandas DataFrame? | Pandas DataFrame là gì?**

A. A one-dimensional labeled data structure | Cấu trúc dữ liệu một chiều có nhãn

B. A two-dimensional labeled table | Bảng dữ liệu hai chiều có nhãn

C. Parse tabular CSV data into a DataFrame | Đọc dữ liệu CSV thành DataFrame

D. One field across multiple records | Một thuộc tính qua nhiều bản ghi

**Đáp án: B**

**Giải thích:** DataFrame tổ chức bản ghi thành hàng và trường thành cột. Bảng gồm ba quan sát và hai trường có shape `(3,2)`; Series lại là cấu trúc một chiều có nhãn.

**Q3. What does a column represent? | Một cột trong bảng thể hiện gì?**

A. A one-dimensional labeled data structure | Cấu trúc dữ liệu một chiều có nhãn

B. One field across multiple records | Một thuộc tính qua nhiều bản ghi

C. A two-dimensional labeled table | Bảng dữ liệu hai chiều có nhãn

D. Parse tabular CSV data into a DataFrame | Đọc dữ liệu CSV thành DataFrame

**Đáp án: B**

**Giải thích:** Cột lưu cùng một thuộc tính ở các hàng. Nếu các hàng là đơn hàng, cột `price` ghi giá của từng đơn và cần xác định rõ đơn vị tiền tệ.

**Q4. What is the purpose of `pd.read_csv()`? | `pd.read_csv()` dùng để làm gì?**

A. A one-dimensional labeled data structure | Cấu trúc dữ liệu một chiều có nhãn

B. One field across multiple records | Một thuộc tính qua nhiều bản ghi

C. A two-dimensional labeled table | Bảng dữ liệu hai chiều có nhãn

D. Parse tabular CSV data into a DataFrame | Đọc dữ liệu CSV thành DataFrame

**Đáp án: D**

**Giải thích:** read_csv đọc các trường được phân cách cùng hàng tên cột. Ví dụ hàng tiêu đề CSV `name,score` tạo tên cột tương ứng, nhưng các ô số sai định dạng vẫn có thể cần làm sạch sau khi đọc.

**Q5. What does `pd.Series([1,2])` return? | `pd.Series([1,2])` trả về gì?**

A. A Series containing column x | Series chứa cột x

B. A Series with default index 0,1 | Series có index mặc định 0,1

C. A DataFrame containing one column | DataFrame có một cột

D. A tuple with row and column counts | Tuple gồm số hàng và số cột

**Đáp án: B**

**Giải thích:** Không chỉ định nhãn thì Pandas tự gán chỉ số nguyên. Không truyền index, hai giá trị nhận nhãn `0` và `1`; kết quả là Series chứ không phải DataFrame một cột.

**Q6. What does `df[['x']]` return? | `df[['x']]` trả về gì?**

A. A DataFrame containing one column | DataFrame có một cột

B. A tuple with row and column counts | Tuple gồm số hàng và số cột

C. A Series containing column x | Series chứa cột x

D. A Series with default index 0,1 | Series có index mặc định 0,1

**Đáp án: A**

**Giải thích:** Hai lớp ngoặc vuông chọn danh sách cột và giữ dạng bảng. Nếu `df` có năm hàng, `df[['x']]` giữ kết quả hai chiều với shape `(5,1)`, khác `df['x']`.

**Q7. When DataFrame column labels are unique, what does `df['x']` return? | Khi tên cột DataFrame không trùng nhau, `df['x']` trả về gì?**

A. A tuple with row and column counts | Tuple gồm số hàng và số cột

B. A Series containing column x | Series chứa cột x

C. A DataFrame containing one column | DataFrame có một cột

D. A Series with default index 0,1 | Series có index mặc định 0,1

**Đáp án: B**

**Giải thích:** Tra cứu một cột bằng ngoặc đơn trả Series. Với tên cột không trùng, `df['x']` là Series một chiều; hai lớp ngoặc vuông thì trả DataFrame.

**Q8. What does `df.shape` return? | `df.shape` trả về gì?**

A. A Series with default index 0,1 | Series có index mặc định 0,1

B. A DataFrame containing one column | DataFrame có một cột

C. A Series containing column x | Series chứa cột x

D. A tuple with row and column counts | Tuple gồm số hàng và số cột

**Đáp án: D**

**Giải thích:** Shape cho biết hai kích thước của DataFrame. Với DataFrame bốn bản ghi và ba trường, `df.shape` là `(4,3)`, không phải số ô không thiếu.

**Q9. What does `df.head(3)` show? | `df.head(3)` hiển thị gì?**

A. Columns, non-null counts and data types | Các cột, số ô không thiếu và kiểu dữ liệu

B. Data types of columns | Kiểu dữ liệu của các cột

C. The first three rows | Ba hàng đầu

D. Descriptive statistics such as mean and quartiles | Thống kê mô tả như trung bình và các tứ phân vị

**Đáp án: C**

**Giải thích:** head lấy số hàng đầu theo đối số. Nếu DataFrame chỉ có hai hàng, `head(3)` trả hai hàng đó chứ không tạo thêm hàng giả.

**Q10. What does `df.dtypes` describe? | `df.dtypes` mô tả gì?**

A. Descriptive statistics such as mean and quartiles | Thống kê mô tả như trung bình và các tứ phân vị

B. The first three rows | Ba hàng đầu

C. Data types of columns | Kiểu dữ liệu của các cột

D. Columns, non-null counts and data types | Các cột, số ô không thiếu và kiểu dữ liệu

**Đáp án: C**

**Giải thích:** Mỗi cột có thể mang dtype riêng. Cột `price` có thể có dtype thực, còn `name` mang kiểu văn bản; `dtypes` không tính thống kê mô tả.

**Q11. What does `df.info()` primarily summarize? | `df.info()` chủ yếu tóm tắt gì?**

A. The first three rows | Ba hàng đầu

B. Data types of columns | Kiểu dữ liệu của các cột

C. Descriptive statistics such as mean and quartiles | Thống kê mô tả như trung bình và các tứ phân vị

D. Columns, non-null counts and data types | Các cột, số ô không thiếu và kiểu dữ liệu

**Đáp án: D**

**Giải thích:** info cho biết cấu trúc và mức độ đầy đủ của bảng. Nó hiển thị tên cột, số giá trị không thiếu, dtype và bộ nhớ; khác thao tác xem trước hàng dữ liệu bằng `head()`.

**Q12. What does `df.describe()` commonly provide for numeric columns? | `df.describe()` thường cung cấp gì cho cột số?**

A. Descriptive statistics such as mean and quartiles | Thống kê mô tả như trung bình và các tứ phân vị

B. The first three rows | Ba hàng đầu

C. Columns, non-null counts and data types | Các cột, số ô không thiếu và kiểu dữ liệu

D. Data types of columns | Kiểu dữ liệu của các cột

**Đáp án: A**

**Giải thích:** describe tính những thống kê cơ bản cho cột số. Với số `[2,4,6]`, trung bình bằng 4 và các tứ phân vị cho biết mức phân tán; `head()` chỉ hiển thị hàng dữ liệu gốc.

**Q13. What is an index in a DataFrame? | Index của DataFrame là gì?**

A. Column labels | Các tên cột

B. One observation or record | Một quan sát hoặc bản ghi

C. Labels identifying rows | Các nhãn xác định hàng

D. Index labels | Nhãn index

**Đáp án: C**

**Giải thích:** Index tách với các cột thông thường trừ khi được chuyển đổi. Index có thể là nhãn như mã học viên và tách khỏi các cột dữ liệu thường, trừ khi được đưa trở lại thành cột.

**Q14. How are Series values aligned during arithmetic? | Pandas căn các giá trị Series khi tính toán bằng gì?**

A. Labels identifying rows | Các nhãn xác định hàng

B. One observation or record | Một quan sát hoặc bản ghi

C. Index labels | Nhãn index

D. Column labels | Các tên cột

**Đáp án: C**

**Giải thích:** Pandas ghép giá trị theo các nhãn index tương ứng. Nếu hai Series sắp nhãn theo thứ tự khác nhau, Pandas ghép giá trị cùng nhãn trước khi cộng chứ không cộng máy móc theo vị trí.

**Q15. What does `df.columns` contain? | `df.columns` chứa gì?**

A. One observation or record | Một quan sát hoặc bản ghi

B. Index labels | Nhãn index

C. Column labels | Các tên cột

D. Labels identifying rows | Các nhãn xác định hàng

**Đáp án: C**

**Giải thích:** Thuộc tính columns liệt kê tên trường. Với các cột `name` và `age`, `list(df.columns)` trả danh sách tên cột, không phải nhãn hàng.

**Q16. What is a DataFrame row usually intended to represent? | Mỗi hàng DataFrame thường nên biểu diễn gì?**

A. One observation or record | Một quan sát hoặc bản ghi

B. Column labels | Các tên cột

C. Index labels | Nhãn index

D. Labels identifying rows | Các nhãn xác định hàng

**Đáp án: A**

**Giải thích:** Ý nghĩa hàng nhất quán giúp hiểu đúng các phép tổng hợp. Một hàng có thể là một học viên, giao dịch hoặc lần đo, nhưng cần định nghĩa nhất quán để hiểu đúng thống kê.

**Q17. What does `df['price'] * df['qty']` calculate? | `df['price'] * df['qty']` tính gì?**

A. An element-wise product aligned by index | Tích từng phần tử được căn theo index

B. To interpret the data and calculations correctly | Để hiểu đúng dữ liệu và phép tính

C. A numeric column may be parsed as text | Cột số có thể bị đọc thành chữ

D. Two named columns | Hai cột được nêu tên

**Đáp án: A**

**Giải thích:** Giá và lượng tương ứng được nhân ở từng bản ghi. Nếu cùng một hàng có giá 10 đô la và số lượng 3 món, tích là 30 đô la, không phải tổng của nhiều hàng.

**Q18. What does `df[['a','b']]` select? | `df[['a','b']]` chọn gì?**

A. A numeric column may be parsed as text | Cột số có thể bị đọc thành chữ

B. An element-wise product aligned by index | Tích từng phần tử được căn theo index

C. To interpret the data and calculations correctly | Để hiểu đúng dữ liệu và phép tính

D. Two named columns | Hai cột được nêu tên

**Đáp án: D**

**Giải thích:** Danh sách tên cho phép lấy nhiều cột. Kết quả vẫn là DataFrame chứa `a` và `b` theo thứ tự đã nêu, còn `df['a']` thường trả Series.

**Q19. What is a frequent risk when loading CSV numeric data? | Nguy cơ thường gặp khi đọc số từ CSV là gì?**

A. A numeric column may be parsed as text | Cột số có thể bị đọc thành chữ

B. Two named columns | Hai cột được nêu tên

C. An element-wise product aligned by index | Tích từng phần tử được căn theo index

D. To interpret the data and calculations correctly | Để hiểu đúng dữ liệu và phép tính

**Đáp án: A**

**Giải thích:** Giá trị không hợp lệ có thể khiến Pandas không nhận kiểu số. Ô như `'unknown'` nằm trong cột số có thể khiến kiểu bị suy ra thành văn bản/object, nên phải kiểm tra và đổi kiểu trước khi tính.

**Q20. Why define what each row and column means? | Vì sao cần nêu ý nghĩa từng hàng và cột?**

A. A numeric column may be parsed as text | Cột số có thể bị đọc thành chữ

B. To interpret the data and calculations correctly | Để hiểu đúng dữ liệu và phép tính

C. An element-wise product aligned by index | Tích từng phần tử được căn theo index

D. Two named columns | Hai cột được nêu tên

**Đáp án: B**

**Giải thích:** Ý nghĩa hàng và cột quyết định cách diễn giải kết quả. Nếu hàng là giao dịch và cột gồm giá cùng số lượng, nêu rõ đơn vị giúp tránh nhân nhầm trường và hiểu sai doanh thu.

## PY-18 — PY-18 — Pandas: missing values, duplicates và kiểu dữ liệu

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a missing value? | Giá trị thiếu là gì?**

A. Replacing missing entries with chosen estimates | Thay ô thiếu bằng giá trị ước lượng đã chọn

B. Checking types and rules before analysis | Kiểm tra kiểu và quy tắc trước khi phân tích

C. An absent or unknown data entry | Ô dữ liệu chưa có giá trị xác định

D. A record repeated under a defined matching rule | Bản ghi lặp theo tiêu chí đối chiếu xác định

**Đáp án: C**

**Giải thích:** Thiếu nghĩa là chưa có giá trị quan sát hợp lệ ở ô đó. Trong Pandas, `NaN` và `None` có thể biểu thị ô thiếu; giá trị thiếu khác một số 0 đã được đo thật.

**Q2. What is a duplicate record? | Bản ghi trùng là gì?**

A. A record repeated under a defined matching rule | Bản ghi lặp theo tiêu chí đối chiếu xác định

B. Checking types and rules before analysis | Kiểm tra kiểu và quy tắc trước khi phân tích

C. An absent or unknown data entry | Ô dữ liệu chưa có giá trị xác định

D. Replacing missing entries with chosen estimates | Thay ô thiếu bằng giá trị ước lượng đã chọn

**Đáp án: A**

**Giải thích:** Nhận diện trùng phụ thuộc các trường dùng làm tiêu chí. Hai hàng cùng mã khách có thể là hai đơn riêng, nên phải xác định tiêu chí trùng trước khi xóa dữ liệu.

**Q3. What is imputation? | Điền khuyết là gì?**

A. An absent or unknown data entry | Ô dữ liệu chưa có giá trị xác định

B. Checking types and rules before analysis | Kiểm tra kiểu và quy tắc trước khi phân tích

C. Replacing missing entries with chosen estimates | Thay ô thiếu bằng giá trị ước lượng đã chọn

D. A record repeated under a defined matching rule | Bản ghi lặp theo tiêu chí đối chiếu xác định

**Đáp án: C**

**Giải thích:** Điền khuyết dùng giá trị lựa chọn chứ không coi đó là dữ liệu đã đo thật. Điền tuổi thiếu bằng trung vị của tập train là phép ước lượng, không chứng minh tuổi thật bằng trung vị đó.

**Q4. What is data validation? | Kiểm tra dữ liệu hợp lệ là gì?**

A. A record repeated under a defined matching rule | Bản ghi lặp theo tiêu chí đối chiếu xác định

B. An absent or unknown data entry | Ô dữ liệu chưa có giá trị xác định

C. Checking types and rules before analysis | Kiểm tra kiểu và quy tắc trước khi phân tích

D. Replacing missing entries with chosen estimates | Thay ô thiếu bằng giá trị ước lượng đã chọn

**Đáp án: C**

**Giải thích:** Kiểm tra hợp lệ phát hiện sai kiểu và giá trị vượt phạm vi. Với trường tuổi, bước kiểm tra có thể yêu cầu giá trị số không âm và loại chuỗi không hợp lệ.

**Q5. What does `isna()` identify? | `isna()` phát hiện gì?**

A. Missing entries | Các ô thiếu

B. Turns invalid numeric text into NaN | Chuyển chữ không đổi được sang số thành NaN

C. Repeated rows after the first occurrence | Các hàng lặp sau lần xuất hiện đầu

D. Replaces missing entries with a value | Thay ô thiếu bằng giá trị cho trước

**Đáp án: A**

**Giải thích:** isna trả mặt nạ Boolean đánh dấu giá trị thiếu. Với `[2, NaN]`, `isna()` đánh dấu `[False, True]`; hàm xác định chỗ thiếu mà không xóa dữ liệu.

**Q6. What does `duplicated()` mark by default? | `duplicated()` mặc định đánh dấu gì?**

A. Turns invalid numeric text into NaN | Chuyển chữ không đổi được sang số thành NaN

B. Repeated rows after the first occurrence | Các hàng lặp sau lần xuất hiện đầu

C. Replaces missing entries with a value | Thay ô thiếu bằng giá trị cho trước

D. Missing entries | Các ô thiếu

**Đáp án: B**

**Giải thích:** duplicated xét toàn hàng nếu không chỉ định subset. Với hai hàng giống nhau, hàng đầu thường nhận `False`, hàng sau nhận `True`; `subset=` thay đổi các cột dùng để xét trùng.

**Q7. What does `fillna(value)` do? | `fillna(value)` làm gì?**

A. Turns invalid numeric text into NaN | Chuyển chữ không đổi được sang số thành NaN

B. Missing entries | Các ô thiếu

C. Repeated rows after the first occurrence | Các hàng lặp sau lần xuất hiện đầu

D. Replaces missing entries with a value | Thay ô thiếu bằng giá trị cho trước

**Đáp án: D**

**Giải thích:** fillna thay ô thiếu mà giữ các giá trị hợp lệ. Với điểm thiếu, `df.fillna(0)` mặc định trả DataFrame đã điền mà không đổi `df` nếu chưa gán kết quả hoặc yêu cầu sửa tại chỗ.

**Q8. What does `pd.to_numeric(..., errors='coerce')` do with invalid text? | `to_numeric(..., errors='coerce')` xử lý chuỗi không phải số thế nào?**

A. Replaces missing entries with a value | Thay ô thiếu bằng giá trị cho trước

B. Turns invalid numeric text into NaN | Chuyển chữ không đổi được sang số thành NaN

C. Repeated rows after the first occurrence | Các hàng lặp sau lần xuất hiện đầu

D. Missing entries | Các ô thiếu

**Đáp án: B**

**Giải thích:** Cơ chế coerce đánh dấu lỗi chuyển kiểu là thiếu chứ không đoán số. Khi đổi kiểu số, chuỗi `'bad'` trở thành dấu thiếu, còn chuỗi hợp lệ như `'12'` được chuyển thành số 12.

**Q9. What does `dropna()` normally remove? | `dropna()` mặc định xóa gì?**

A. Rows containing missing data | Các hàng chứa dữ liệu thiếu

B. The middle value after sorting, or mean of the two middle values | Giá trị giữa khi sắp, hoặc trung bình hai giá trị giữa

C. Raise an exception on invalid input | Báo ngoại lệ khi đầu vào không hợp lệ

D. The first occurrence of each distinct row | Lần xuất hiện đầu của từng hàng khác nhau

**Đáp án: A**

**Giải thích:** DataFrame.dropna mặc định bỏ hàng có ít nhất một ô thiếu. Với DataFrame có ô thiếu, `dropna()` mặc định bỏ hàng chứa ít nhất một ô thiếu; nó không tự điền các ô đó.

**Q10. What does `drop_duplicates()` normally keep? | `drop_duplicates()` thường giữ gì?**

A. The middle value after sorting, or mean of the two middle values | Giá trị giữa khi sắp, hoặc trung bình hai giá trị giữa

B. The first occurrence of each distinct row | Lần xuất hiện đầu của từng hàng khác nhau

C. Rows containing missing data | Các hàng chứa dữ liệu thiếu

D. Raise an exception on invalid input | Báo ngoại lệ khi đầu vào không hợp lệ

**Đáp án: B**

**Giải thích:** Mặc định các lần lặp sau của cùng hàng sẽ bị bỏ. Với các hàng A, A, B, mặc định giữ A đầu và B, không giữ A cuối trừ khi đặt `keep='last'`.

**Q11. What is the median? | Trung vị là gì?**

A. Raise an exception on invalid input | Báo ngoại lệ khi đầu vào không hợp lệ

B. The first occurrence of each distinct row | Lần xuất hiện đầu của từng hàng khác nhau

C. Rows containing missing data | Các hàng chứa dữ liệu thiếu

D. The middle value after sorting, or mean of the two middle values | Giá trị giữa khi sắp, hoặc trung bình hai giá trị giữa

**Đáp án: D**

**Giải thích:** Trung vị ít nhạy với giá trị cực đoan hơn trung bình cộng. Với dãy đã sắp `[1,2,100]`, trung vị là 2 còn trung bình lớn hơn 34; nếu số phần tử chẵn thì lấy trung bình hai số ở giữa.

**Q12. What is the meaning of `errors='raise'` in numeric conversion? | `errors='raise'` khi đổi sang số có nghĩa gì?**

A. Rows containing missing data | Các hàng chứa dữ liệu thiếu

B. The middle value after sorting, or mean of the two middle values | Giá trị giữa khi sắp, hoặc trung bình hai giá trị giữa

C. The first occurrence of each distinct row | Lần xuất hiện đầu của từng hàng khác nhau

D. Raise an exception on invalid input | Báo ngoại lệ khi đầu vào không hợp lệ

**Đáp án: D**

**Giải thích:** Raise làm lỗi lộ rõ thay vì chuyển âm thầm thành thiếu. Dùng `pd.to_numeric(['bad'], errors='raise')` báo lỗi, còn `errors='coerce'` trả dấu giá trị số bị thiếu.

**Q13. What is data leakage in train/test preprocessing? | Data leakage khi chuẩn bị train/test là gì?**

A. Zero may have a different real-world meaning | Số 0 có thể mang ý nghĩa thực tế khác

B. To audit and reverse cleaning decisions | Để đối chiếu và phục hồi quyết định xử lý

C. Records with shared IDs may still represent distinct events | Hai dòng cùng ID vẫn có thể là sự kiện khác nhau

D. Using information from test data while fitting preprocessing | Dùng thông tin của test khi học tham số tiền xử lý

**Đáp án: D**

**Giải thích:** Thống kê tiền xử lý phải học chỉ từ tập train. Tính trung vị điền khuyết trên cả train và test làm thông tin của tập đánh giá lọt vào giai đoạn chuẩn bị mô hình.

**Q14. Why is replacing every missing value with zero risky? | Vì sao thay mọi ô thiếu bằng 0 là rủi ro?**

A. To audit and reverse cleaning decisions | Để đối chiếu và phục hồi quyết định xử lý

B. Using information from test data while fitting preprocessing | Dùng thông tin của test khi học tham số tiền xử lý

C. Zero may have a different real-world meaning | Số 0 có thể mang ý nghĩa thực tế khác

D. Records with shared IDs may still represent distinct events | Hai dòng cùng ID vẫn có thể là sự kiện khác nhau

**Đáp án: C**

**Giải thích:** Tuổi chưa nhập không tự đồng nghĩa tuổi bằng 0. Số lượng hàng thiếu nghĩa là chưa biết, còn số lượng 0 nói rõ không có món nào; thay hai trường hợp cho nhau sẽ đổi ý nghĩa.

**Q15. Why check key columns before removing duplicates? | Vì sao phải xem cột khóa trước khi xóa trùng?**

A. Records with shared IDs may still represent distinct events | Hai dòng cùng ID vẫn có thể là sự kiện khác nhau

B. Using information from test data while fitting preprocessing | Dùng thông tin của test khi học tham số tiền xử lý

C. Zero may have a different real-world meaning | Số 0 có thể mang ý nghĩa thực tế khác

D. To audit and reverse cleaning decisions | Để đối chiếu và phục hồi quyết định xử lý

**Đáp án: A**

**Giải thích:** Quy tắc nghiệp vụ xác định hai dòng có thực sự trùng không. Hai giao dịch của cùng khách hàng có thể là hai sự kiện hợp lệ khác nhau dù trùng một mã định danh.

**Q16. Why preserve the original raw data while cleaning? | Vì sao nên giữ dữ liệu gốc khi làm sạch?**

A. Zero may have a different real-world meaning | Số 0 có thể mang ý nghĩa thực tế khác

B. To audit and reverse cleaning decisions | Để đối chiếu và phục hồi quyết định xử lý

C. Records with shared IDs may still represent distinct events | Hai dòng cùng ID vẫn có thể là sự kiện khác nhau

D. Using information from test data while fitting preprocessing | Dùng thông tin của test khi học tham số tiền xử lý

**Đáp án: B**

**Giải thích:** Bản gốc giúp kiểm tra từng phép biến đổi. Giữ bản nguồn không đổi giúp so sánh trước/sau và xem xét lại các quyết định làm sạch chưa đúng.

**Q17. What does a Boolean missing-value mask contain? | Mặt nạ dữ liệu thiếu chứa gì?**

A. True and False values | Các giá trị True và False

B. Original retained-row labels remain | Nhãn index của hàng được giữ vẫn còn

C. Choose a justified missing-data treatment | Chọn cách xử lý dữ liệu thiếu có cơ sở

D. Rebuilds sequential indices without retaining old index as a column | Đánh lại index tuần tự, không giữ index cũ thành cột

**Đáp án: A**

**Giải thích:** Mỗi vị trí cho biết ô dữ liệu có thiếu hay không. Một ô mask là `True` nếu đầu vào tương ứng bị thiếu và `False` nếu không; mask không phải danh sách giá trị thay thế.

**Q18. What happens to index labels after `drop_duplicates()` by default? | Sau `drop_duplicates()`, index mặc định thay đổi thế nào?**

A. True and False values | Các giá trị True và False

B. Choose a justified missing-data treatment | Chọn cách xử lý dữ liệu thiếu có cơ sở

C. Rebuilds sequential indices without retaining old index as a column | Đánh lại index tuần tự, không giữ index cũ thành cột

D. Original retained-row labels remain | Nhãn index của hàng được giữ vẫn còn

**Đáp án: D**

**Giải thích:** Xóa hàng trùng không tự đánh lại index cho hàng còn lại. Xóa các hàng mang nhãn 1 và 3 không tự đánh lại nhãn còn lại; phải reset index riêng nếu muốn nhãn liên tiếp.

**Q19. What does `reset_index(drop=True)` do? | `reset_index(drop=True)` làm gì?**

A. Original retained-row labels remain | Nhãn index của hàng được giữ vẫn còn

B. Choose a justified missing-data treatment | Chọn cách xử lý dữ liệu thiếu có cơ sở

C. Rebuilds sequential indices without retaining old index as a column | Đánh lại index tuần tự, không giữ index cũ thành cột

D. True and False values | Các giá trị True và False

**Đáp án: C**

**Giải thích:** Đánh lại nhãn hàng giúp bảng đã xử lý dễ đọc hơn. Sau khi bỏ hàng, `reset_index(drop=True)` tạo nhãn `0,1,2,...` mà không đưa index cũ thành cột mới.

**Q20. What should happen after coercing invalid numeric text to NaN? | Sau khi chuyển chuỗi số sai thành NaN cần làm gì?**

A. Rebuilds sequential indices without retaining old index as a column | Đánh lại index tuần tự, không giữ index cũ thành cột

B. Choose a justified missing-data treatment | Chọn cách xử lý dữ liệu thiếu có cơ sở

C. Original retained-row labels remain | Nhãn index của hàng được giữ vẫn còn

D. True and False values | Các giá trị True và False

**Đáp án: B**

**Giải thích:** Coerce phát hiện lỗi, không khôi phục được giá trị thực chưa biết. Sau khi coerce, hãy đếm số ô bị thiếu rồi quyết định loại bỏ, từ chối hay điền khuyết theo yêu cầu bài toán.

## PY-19 — PY-19 — Pandas: lọc, groupby, merge và sắp xếp

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What does a Boolean filter do? | Lọc Boolean làm gì?**

A. Integer positions | Vị trí số nguyên

B. Groups records sharing a key | Gom bản ghi có chung khóa

C. Keeps rows matching a condition | Giữ hàng thỏa điều kiện

D. Index labels | Nhãn index

**Đáp án: C**

**Giải thích:** Mặt nạ Boolean xác định hàng cần giữ. Với `df[df['score'] >= 8]`, chỉ những bản ghi đạt ngưỡng điểm được giữ lại; các hàng khác bị lọc, không phải được gộp thống kê.

**Q2. What does `loc` use to select rows? | `loc` chọn hàng bằng gì?**

A. Keeps rows matching a condition | Giữ hàng thỏa điều kiện

B. Integer positions | Vị trí số nguyên

C. Groups records sharing a key | Gom bản ghi có chung khóa

D. Index labels | Nhãn index

**Đáp án: D**

**Giải thích:** loc chọn theo nhãn hàng. Nếu DataFrame có nhãn hàng `'A'`, `df.loc['A']` chọn theo nhãn đó dù hàng không nằm ở vị trí đầu.

**Q3. What does `iloc` use to select rows? | `iloc` chọn hàng bằng gì?**

A. Integer positions | Vị trí số nguyên

B. Keeps rows matching a condition | Giữ hàng thỏa điều kiện

C. Groups records sharing a key | Gom bản ghi có chung khóa

D. Index labels | Nhãn index

**Đáp án: A**

**Giải thích:** iloc chọn theo vị trí đếm từ 0. `df.iloc[0]` chọn hàng đầu theo vị trí; hàng có nhãn `0` không nhất thiết nằm đầu sau khi sắp xếp dữ liệu.

**Q4. What does `groupby` do? | `groupby` làm gì?**

A. Index labels | Nhãn index

B. Keeps rows matching a condition | Giữ hàng thỏa điều kiện

C. Groups records sharing a key | Gom bản ghi có chung khóa

D. Integer positions | Vị trí số nguyên

**Đáp án: C**

**Giải thích:** Phân nhóm gom các hàng có chung một trường. Với các thành phố `HN`, `HN`, `HCM`, groupby theo thành phố tạo hai nhóm để tổng hợp mà không tự loại các thành phố còn lại.

**Q5. What is the join key in `merge`? | Khóa ghép trong `merge` là gì?**

A. A sale total per city | Tổng doanh thu theo từng vùng

B. Descending order | Thứ tự giảm dần

C. A shared field used to match rows | Trường chung để ghép các hàng

D. All rows from the left table | Mọi hàng bảng trái

**Đáp án: C**

**Giải thích:** Các hàng được ghép khi khóa phù hợp. Nếu hai bảng đều có `customer_id`, các hàng có mã khớp có thể ghép với nhau; vẫn cần xem kiểu dữ liệu và khóa trùng.

**Q6. What does `how='left'` retain? | `how='left'` giữ gì?**

A. Descending order | Thứ tự giảm dần

B. A shared field used to match rows | Trường chung để ghép các hàng

C. A sale total per city | Tổng doanh thu theo từng vùng

D. All rows from the left table | Mọi hàng bảng trái

**Đáp án: D**

**Giải thích:** Ghép trái không bỏ hàng bên trái chưa khớp. Left join giữ mọi bản ghi bảng trái kể cả khi bảng phải không khớp và điền giá trị thiếu phía phải; nhiều hàng phải cùng khớp có thể làm tăng số hàng kết quả.

**Q7. What does `groupby('city')['sale'].sum()` return? | `groupby('city')['sale'].sum()` trả gì?**

A. A shared field used to match rows | Trường chung để ghép các hàng

B. A sale total per city | Tổng doanh thu theo từng vùng

C. Descending order | Thứ tự giảm dần

D. All rows from the left table | Mọi hàng bảng trái

**Đáp án: B**

**Giải thích:** sum cộng giá trị sale theo từng vùng. Nếu `HN` có doanh thu 10, 15 và `HCM` có 8, tổng từng thành phố lần lượt là 25 và 8, không chỉ một tổng toàn bảng.

**Q8. What does `ascending=False` mean in sorting? | `ascending=False` khi sắp xếp nghĩa là gì?**

A. All rows from the left table | Mọi hàng bảng trái

B. A shared field used to match rows | Trường chung để ghép các hàng

C. Descending order | Thứ tự giảm dần

D. A sale total per city | Tổng doanh thu theo từng vùng

**Đáp án: C**

**Giải thích:** False chuyển sang thứ tự giảm dần. Sắp điểm `[3,1,2]` với `ascending=False` cho `[3,2,1]`, không giữ thứ tự gốc.

**Q9. What distinguishes `loc` from `iloc`? | `loc` khác `iloc` ở đâu?**

A. Retains selected rows versus grouping by key | Giữ hàng được chọn so với gom theo khóa

B. First two rows versus last two | Hai hàng đầu so với hai hàng cuối

C. Labels versus positions | Nhãn so với vị trí

D. Matching rows only versus all left rows | Chỉ hàng khớp so với mọi hàng trái

**Đáp án: C**

**Giải thích:** Nhãn 7 không nhất thiết nằm ở vị trí 7. Nhãn `'7'` có thể nằm tại vị trí đầu, nên `loc['7']` và `iloc[7]` có thể chọn các hàng khác nhau hoặc gây lỗi.

**Q10. How does filtering differ from grouping? | Lọc khác phân nhóm như thế nào?**

A. Matching rows only versus all left rows | Chỉ hàng khớp so với mọi hàng trái

B. Labels versus positions | Nhãn so với vị trí

C. First two rows versus last two | Hai hàng đầu so với hai hàng cuối

D. Retains selected rows versus grouping by key | Giữ hàng được chọn so với gom theo khóa

**Đáp án: D**

**Giải thích:** Lọc bỏ hàng không khớp; nhóm tổ chức bản ghi. Lọc chỉ giữ bản ghi thỏa điều kiện, còn phân nhóm tổ chức bản ghi theo khóa để có thể tính tổng từng nhóm bằng `sum()`.

**Q11. How does `head(2)` differ from `tail(2)`? | `head(2)` khác `tail(2)` thế nào?**

A. Retains selected rows versus grouping by key | Giữ hàng được chọn so với gom theo khóa

B. First two rows versus last two | Hai hàng đầu so với hai hàng cuối

C. Labels versus positions | Nhãn so với vị trí

D. Matching rows only versus all left rows | Chỉ hàng khớp so với mọi hàng trái

**Đáp án: B**

**Giải thích:** Hai hàm lấy dữ liệu ở hai đầu bảng. Với năm hàng, `head(2)` lấy hai hàng đầu, còn `tail(2)` lấy hàng thứ tư và thứ năm theo thứ tự hiện tại.

**Q12. How does an inner join differ from a left join? | Inner join khác left join thế nào?**

A. First two rows versus last two | Hai hàng đầu so với hai hàng cuối

B. Matching rows only versus all left rows | Chỉ hàng khớp so với mọi hàng trái

C. Retains selected rows versus grouping by key | Giữ hàng được chọn so với gom theo khóa

D. Labels versus positions | Nhãn so với vị trí

**Đáp án: B**

**Giải thích:** Inner join bỏ hàng trái không ghép được. Nếu một khách trong bảng trái không có hàng ghép bên phải, inner join bỏ khách đó, còn left join giữ lại với các trường phải bị thiếu.

**Q13. What risk comes from duplicate right-side join keys? | Khóa ghép bảng phải bị trùng gây nguy cơ gì?**

A. Unexpected row multiplication | Nhân số hàng ngoài ý muốn

B. Ascending order | Thứ tự tăng dần

C. Unique right-side join keys | Khóa ghép bảng phải duy nhất

D. Rebuilds sequential row labels | Đánh lại nhãn hàng liên tiếp

**Đáp án: A**

**Giải thích:** Mỗi hàng phải khớp thêm có thể nhân dữ liệu trái. Một khóa trái khớp hai hàng phải có thể sinh hai hàng ghép, làm tổng bị phóng đại nếu không dự kiến khóa trùng.

**Q14. What does `validate='many_to_one'` check? | `validate='many_to_one'` kiểm tra gì?**

A. Rebuilds sequential row labels | Đánh lại nhãn hàng liên tiếp

B. Unique right-side join keys | Khóa ghép bảng phải duy nhất

C. Unexpected row multiplication | Nhân số hàng ngoài ý muốn

D. Ascending order | Thứ tự tăng dần

**Đáp án: B**

**Giải thích:** Nhiều hàng trái được phép ghép một hàng phải. Kiểm tra này cho phép nhiều hàng trái có cùng khóa nhưng yêu cầu phía phải tối đa một hàng cho mỗi khóa, nếu không Pandas báo lỗi kiểm chứng merge.

**Q15. What does `reset_index(drop=True)` change? | `reset_index(drop=True)` thay đổi gì?**

A. Ascending order | Thứ tự tăng dần

B. Unique right-side join keys | Khóa ghép bảng phải duy nhất

C. Unexpected row multiplication | Nhân số hàng ngoài ý muốn

D. Rebuilds sequential row labels | Đánh lại nhãn hàng liên tiếp

**Đáp án: D**

**Giải thích:** Đánh lại index loại bỏ nhãn hàng cũ. Sau khi lọc còn nhãn `[2,5]`, `reset_index(drop=True)` đánh nhãn lại `[0,1]` mà không giữ nhãn cũ thành cột.

**Q16. What does `ascending=True` request? | `ascending=True` yêu cầu gì?**

A. Ascending order | Thứ tự tăng dần

B. Unique right-side join keys | Khóa ghép bảng phải duy nhất

C. Unexpected row multiplication | Nhân số hàng ngoài ý muốn

D. Rebuilds sequential row labels | Đánh lại nhãn hàng liên tiếp

**Đáp án: A**

**Giải thích:** Tăng dần là hướng sắp xếp mặc định. Khi sắp tăng dần, các số 1, 2, 3 theo đúng thứ tự đó; `ascending=False` chuyển sang giảm dần.

**Q17. What does `df.iloc[0]` select? | `df.iloc[0]` chọn gì?**

A. The first row by position | Hàng đầu theo vị trí

B. Keys must have compatible representations | Khóa cần biểu diễn tương thích

C. Rows within each group | Số hàng trong từng nhóm

D. Matching rows in named columns a and b | Hàng phù hợp ở hai cột a và b

**Đáp án: A**

**Giải thích:** Vị trí đầu tiên mang số 0. `iloc[0]` chọn vị trí không bất kể nhãn hàng là gì; thao tác thường trả một Series đại diện cho hàng đầu.

**Q18. What does `df.loc[mask, ['a','b']]` select? | `df.loc[mask, ['a','b']]` chọn gì?**

A. Rows within each group | Số hàng trong từng nhóm

B. The first row by position | Hàng đầu theo vị trí

C. Keys must have compatible representations | Khóa cần biểu diễn tương thích

D. Matching rows in named columns a and b | Hàng phù hợp ở hai cột a và b

**Đáp án: D**

**Giải thích:** Mask lọc hàng, danh sách tên lọc cột. Mask Boolean chọn các hàng đạt điều kiện, còn `['a','b']` giới hạn kết quả ở đúng hai cột có tên đó.

**Q19. What does `groupby('type').size()` count? | `groupby('type').size()` đếm gì?**

A. Rows within each group | Số hàng trong từng nhóm

B. Matching rows in named columns a and b | Hàng phù hợp ở hai cột a và b

C. The first row by position | Hàng đầu theo vị trí

D. Keys must have compatible representations | Khóa cần biểu diễn tương thích

**Đáp án: A**

**Giải thích:** size đếm số hàng ở mỗi nhóm. Khác `count()` trên một cột có giá trị thiếu, `size()` của nhóm vẫn đếm hàng ngay cả khi ô ở cột khác bị thiếu.

**Q20. Why check types of columns used as merge keys? | Vì sao cần kiểm tra kiểu cột khóa khi merge?**

A. Rows within each group | Số hàng trong từng nhóm

B. Keys must have compatible representations | Khóa cần biểu diễn tương thích

C. Matching rows in named columns a and b | Hàng phù hợp ở hai cột a và b

D. The first row by position | Hàng đầu theo vị trí

**Đáp án: B**

**Giải thích:** Kiểu khóa khác nhau hoặc sai có thể cản trở ghép đúng. Khóa chuỗi `'001'` không có biểu diễn giống số `1`, nên cần chuẩn hóa kiểu và định dạng trước khi ghép dữ liệu.

## PY-20 — PY-20 — Logic mệnh đề, bảng chân trị và quy tắc đếm

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a proposition? | Mệnh đề là gì?**

A. A table of all input truth-value combinations | Bảng các tổ hợp giá trị đúng/sai đầu vào

B. The logical conditional 'if p then q' | Điều kiện logic 'nếu p thì q'

C. A statement that is either true or false | Phát biểu có thể xác định đúng hoặc sai

D. Multiply choice counts across sequential stages when each earlier choice permits the stated number of later choices | Nhân số cách chọn qua các bước khi mỗi lựa chọn trước cho phép đúng số cách ở bước sau

**Đáp án: C**

**Giải thích:** Mệnh đề có một giá trị đúng/sai xác định. Ví dụ `2 + 2 = 4` là mệnh đề đúng, còn câu hỏi như `Mấy giờ rồi?` không tự khẳng định một giá trị đúng hay sai.

**Q2. What is a truth table? | Bảng chân trị là gì?**

A. Multiply the numbers of sequential independent choices | Nhân số lựa chọn qua các bước kết hợp đầy đủ

B. A statement that is either true or false | Phát biểu có thể xác định đúng hoặc sai

C. A table of all input truth-value combinations | Bảng các tổ hợp giá trị đúng/sai đầu vào

D. The logical conditional 'if p then q' | Điều kiện logic 'nếu p thì q'

**Đáp án: C**

**Giải thích:** Bảng chân trị liệt kê các khả năng Boolean. Với hai mệnh đề p và q, bốn hàng là (T,T), (T,F), (F,T), (F,F); bảng xét mọi cách gán giá trị.

**Q3. What is logical implication `p ⇒ q`? | Phép kéo theo `p ⇒ q` là gì?**

A. The logical conditional 'if p then q' | Điều kiện logic 'nếu p thì q'

B. A statement that is either true or false | Phát biểu có thể xác định đúng hoặc sai

C. Multiply the numbers of sequential independent choices | Nhân số lựa chọn qua các bước kết hợp đầy đủ

D. A table of all input truth-value combinations | Bảng các tổ hợp giá trị đúng/sai đầu vào

**Đáp án: A**

**Giải thích:** Kéo theo chỉ sai khi tiền đề đúng, kết luận sai. Phép kéo theo đòi khi tiền đề p đúng thì kết luận q không được sai; khi p sai, kéo theo vật chất vẫn đúng bất kể q.

**Q4. What is the multiplication counting principle? | Nguyên lý nhân trong đếm là gì?**

A. A statement that is either true or false | Phát biểu có thể xác định đúng hoặc sai

B. A table of all input truth-value combinations | Bảng các tổ hợp giá trị đúng/sai đầu vào

C. The logical conditional 'if p then q' | Điều kiện logic 'nếu p thì q'

D. Multiply stage-choice counts when each earlier choice permits the same stated number of valid continuations | Nhân số cách chọn mỗi bước khi mọi lựa chọn trước đều cho phép cùng số cách đi tiếp hợp lệ

**Đáp án: D**

**Giải thích:** Nếu bước đầu có m cách và mỗi cách có đúng n lựa chọn nối tiếp thì có m×n kết quả hoàn chỉnh. Quy tắc đếm theo từng bước này không đòi các biến cố độc lập về xác suất. Nếu có hai cách chọn áo và mỗi áo đều ghép được với ba quần, tổng cộng `2 × 3 = 6` bộ; không cần giả thiết độc lập xác suất.

**Q5. When is `p and q` true? | Khi nào `p and q` đúng?**

A. Reverses the truth value of p | Đảo giá trị đúng/sai của p

B. When p is true and q is false | Khi p đúng và q sai

C. When at least one of p or q is true | Khi có ít nhất một trong p hoặc q đúng

D. When both p and q are true | Khi p và q đều đúng

**Đáp án: D**

**Giải thích:** AND cần cả hai điều kiện đúng. Nếu p đúng nhưng q sai thì `p and q` sai; một điều kiện đúng chưa đủ cho phép AND.

**Q6. When is `p or q` true? | Khi nào `p or q` đúng?**

A. Reverses the truth value of p | Đảo giá trị đúng/sai của p

B. When p is true and q is false | Khi p đúng và q sai

C. When at least one of p or q is true | Khi có ít nhất một trong p hoặc q đúng

D. When both p and q are true | Khi p và q đều đúng

**Đáp án: C**

**Giải thích:** OR bao hàm chấp nhận một hoặc cả hai điều kiện đúng. Đây là OR bao hàm: p và q có thể cùng đúng, khác XOR chỉ đúng khi đúng một vế.

**Q7. What does `not p` do? | `not p` làm gì?**

A. When p is true and q is false | Khi p đúng và q sai

B. Reverses the truth value of p | Đảo giá trị đúng/sai của p

C. When both p and q are true | Khi p và q đều đúng

D. When at least one of p or q is true | Khi có ít nhất một trong p hoặc q đúng

**Đáp án: B**

**Giải thích:** NOT phủ định giá trị Boolean. Nếu p=True thì `not p=False`; nếu p=False thì phủ định trở thành True.

**Q8. When is `p ⇒ q` false? | Khi nào `p ⇒ q` sai?**

A. When both p and q are true | Khi p và q đều đúng

B. When at least one of p or q is true | Khi có ít nhất một trong p hoặc q đúng

C. When p is true and q is false | Khi p đúng và q sai

D. Reverses the truth value of p | Đảo giá trị đúng/sai của p

**Đáp án: C**

**Giải thích:** Tiền đề đúng nhưng kết luận sai làm phép kéo theo sai. Với p=True và q=False, `(not p) or q` thành `(False or False)`, nên phép kéo theo sai.

**Q9. How many rows does a truth table with two variables have? | Bảng chân trị hai biến có mấy hàng?**

A. 8 | 8

B. 16 | 16

C. 2 | 2

D. 4 | 4

**Đáp án: D**

**Giải thích:** Hai biến có hai trạng thái mỗi biến, tạo 2² trường hợp. Mỗi biến Boolean có hai giá trị, tạo `2 × 2 = 4` tổ hợp chứ không chỉ hai tổ hợp.

**Q10. How many rows does a truth table with three variables have? | Bảng chân trị ba biến có mấy hàng?**

A. 2 | 2

B. 4 | 4

C. 16 | 16

D. 8 | 8

**Đáp án: D**

**Giải thích:** Ba lựa chọn nhị phân tạo 2³ tổ hợp. Ba biến Boolean tạo `2 × 2 × 2 = 8` cách gán đầu vào cho bảng chân trị.

**Q11. How many rows does a truth table with one variable have? | Bảng chân trị một biến có mấy hàng?**

A. 4 | 4

B. 8 | 8

C. 2 | 2

D. 16 | 16

**Đáp án: C**

**Giải thích:** Một biến Boolean có True và False. Hai hàng ứng với biến duy nhất nhận True và False; bảng có `2^1 = 2` hàng.

**Q12. How many rows does a truth table with four variables have? | Bảng chân trị bốn biến có mấy hàng?**

A. 16 | 16

B. 4 | 4

C. 2 | 2

D. 8 | 8

**Đáp án: A**

**Giải thích:** Bốn biến Boolean tạo 2⁴ khả năng. Mỗi biến Boolean thêm vào nhân đôi số hàng, nên bốn biến cần `2^4 = 16` tổ hợp.

**Q13. Which expression is equivalent to implication `p ⇒ q`? | Biểu thức nào tương đương `p ⇒ q`?**

A. `False` | `False`

B. `(not p) or q` | `(not p) or q`

C. `(True, False)` | `(True, False)`

D. `True` | `True`

**Đáp án: B**

**Giải thích:** Biểu thức chỉ sai khi p=True, q=False. Cả `p ⇒ q` và `(not p) or q` chỉ sai khi p=True, q=False nên bảng chân trị của chúng trùng nhau.

**Q14. Which input pair makes `p ⇒ q` false? | Cặp p, q nào làm `p ⇒ q` sai?**

A. `(True, False)` | `(True, False)`

B. `(not p) or q` | `(not p) or q`

C. `True` | `True`

D. `False` | `False`

**Đáp án: A**

**Giải thích:** Tiền đề đúng và kết luận sai là trường hợp duy nhất làm phép kéo theo sai. Thứ tự cặp là `(p, q)`, nên `(True, False)` có tiền đề đúng và kết luận sai như yêu cầu.

**Q15. What is `True and False`? | `True and False` bằng gì?**

A. `True` | `True`

B. `False` | `False`

C. `(not p) or q` | `(not p) or q`

D. `(True, False)` | `(True, False)`

**Đáp án: B**

**Giải thích:** AND sai nếu có một vế sai. Kết quả là Boolean `False`, không phải số nguyên 0; vế thứ hai sai trong khi AND cần cả hai đúng.

**Q16. What is `False or True`? | `False or True` bằng gì?**

A. `True` | `True`

B. `(True, False)` | `(True, False)`

C. `False` | `False`

D. `(not p) or q` | `(not p) or q`

**Đáp án: A**

**Giải thích:** OR đúng khi có một vế đúng. Vì có một vế đúng, OR bao hàm trả Boolean `True`; `False and True` thì lại sai.

**Q17. When does the addition counting principle apply directly? | Khi nào có thể áp dụng trực tiếp nguyên lý cộng?**

A. All ordered pairs taking one element from each input | Mọi cặp có thứ tự gồm một phần tử từ mỗi nguồn

B. When alternatives are disjoint | Khi các phương án thay thế không trùng nhau

C. When some outcomes belong to more than one counted group | Khi một kết quả nằm trong nhiều nhóm được đếm

D. When each step has the stated choices for every earlier selection | Khi mỗi bước có đủ số lựa chọn với mọi lựa chọn trước đó

**Đáp án: B**

**Giải thích:** Các nhóm không trùng có thể cộng mà không đếm lặp. Nếu năm kết quả chỉ thuộc nhóm A và ba kết quả chỉ thuộc nhóm B, tổng có `5 + 3 = 8` phương án không đếm trùng.

**Q18. When can choices be counted by multiplying options? | Khi nào có thể đếm bằng phép nhân?**

A. When each step has the stated choices for every earlier selection | Khi mỗi bước có đủ số lựa chọn với mọi lựa chọn trước đó

B. When alternatives are disjoint | Khi các phương án thay thế không trùng nhau

C. All ordered pairs taking one element from each input | Mọi cặp có thứ tự gồm một phần tử từ mỗi nguồn

D. When some outcomes belong to more than one counted group | Khi một kết quả nằm trong nhiều nhóm được đếm

**Đáp án: A**

**Giải thích:** Nguyên lý nhân yêu cầu số nhánh lựa chọn phù hợp ở từng bước. Nếu mỗi lựa chọn bước đầu đều có đúng ba cách đi tiếp thì nhân số cách mỗi bước; khi số nhánh thay đổi phải cộng số cách theo từng nhánh cẩn thận.

**Q19. What does `itertools.product(A, B)` generate? | `itertools.product(A, B)` tạo gì?**

A. When each step has the stated choices for every earlier selection | Khi mỗi bước có đủ số lựa chọn với mọi lựa chọn trước đó

B. All ordered pairs taking one element from each input | Mọi cặp có thứ tự gồm một phần tử từ mỗi nguồn

C. When alternatives are disjoint | Khi các phương án thay thế không trùng nhau

D. When some outcomes belong to more than one counted group | Khi một kết quả nằm trong nhiều nhóm được đếm

**Đáp án: B**

**Giải thích:** product liệt kê tích Descartes. Với `A=[1,2]` và `B=['x','y']`, product tạo `(1,'x')`, `(1,'y')`, `(2,'x')`, `(2,'y')`, không chỉ ghép vị trí tương ứng.

**Q20. When should overlapping alternatives be adjusted during counting? | Khi nào cần điều chỉnh phần giao khi đếm?**

A. All ordered pairs taking one element from each input | Mọi cặp có thứ tự gồm một phần tử từ mỗi nguồn

B. When each step has the stated choices for every earlier selection | Khi mỗi bước có đủ số lựa chọn với mọi lựa chọn trước đó

C. When alternatives are disjoint | Khi các phương án thay thế không trùng nhau

D. When some outcomes belong to more than one counted group | Khi một kết quả nằm trong nhiều nhóm được đếm

**Đáp án: D**

**Giải thích:** Nhóm có giao nhau không được đếm trùng. Với hai nhóm có giao, công thức `|A ∪ B| = |A| + |B| − |A ∩ B|` trừ phần được tính hai lần.

## PY-21 — PY-21 — Tập hợp, bao hàm–loại trừ và phân hoạch

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What does a union contain? | Phép hợp chứa gì?**

A. Elements in at least one set | Phần tử thuộc ít nhất một tập

B. Elements common to both sets | Phần tử có ở cả hai tập

C. Elements in A but not in B | Phần tử thuộc A nhưng không thuộc B

D. Nonempty disjoint parts covering the original set | Các phần không rỗng, rời nhau và phủ đủ tập gốc

**Đáp án: A**

**Giải thích:** Hợp chứa các phần tử khác nhau của hai tập.

**Q2. What does an intersection contain? | Phép giao chứa gì?**

A. Elements in at least one set | Phần tử thuộc ít nhất một tập

B. Elements common to both sets | Phần tử có ở cả hai tập

C. Elements in A but not in B | Phần tử thuộc A nhưng không thuộc B

D. Nonempty disjoint parts covering the original set | Các phần không rỗng, rời nhau và phủ đủ tập gốc

**Đáp án: B**

**Giải thích:** Giao chỉ giữ phần tử chung của hai tập.

**Q3. What is set difference A−B? | Hiệu tập hợp A−B là gì?**

A. Elements in at least one set | Phần tử thuộc ít nhất một tập

B. Elements common to both sets | Phần tử có ở cả hai tập

C. Elements in A but not in B | Phần tử thuộc A nhưng không thuộc B

D. Nonempty disjoint parts covering the original set | Các phần không rỗng, rời nhau và phủ đủ tập gốc

**Đáp án: C**

**Giải thích:** Hiệu A−B loại phần tử của B ra khỏi A.

**Q4. What defines a partition of a set? | Điều gì xác định một phân hoạch?**

A. Elements in at least one set | Phần tử thuộc ít nhất một tập

B. Elements common to both sets | Phần tử có ở cả hai tập

C. Elements in A but not in B | Phần tử thuộc A nhưng không thuộc B

D. Nonempty disjoint parts covering the original set | Các phần không rỗng, rời nhau và phủ đủ tập gốc

**Đáp án: D**

**Giải thích:** Mọi phần không giao nhau và hợp bằng tập gốc.

**Q5. Which operator computes union for sets? | Toán tử nào tính phép hợp Set?**

A. `a | b` | `a | b`

B. `a & b` | `a & b`

C. `a ^ b` | `a ^ b`

D. `a.isdisjoint(b)` | `a.isdisjoint(b)`

**Đáp án: A**

**Giải thích:** Dấu `|` biểu diễn phép hợp tập hợp.

**Q6. Which operator computes intersection? | Toán tử nào tính phép giao?**

A. `a | b` | `a | b`

B. `a & b` | `a & b`

C. `a ^ b` | `a ^ b`

D. `a.isdisjoint(b)` | `a.isdisjoint(b)`

**Đáp án: B**

**Giải thích:** Dấu & giữ các phần tử chung.

**Q7. Which operator computes symmetric difference? | Toán tử nào tính hiệu đối xứng?**

A. `a | b` | `a | b`

B. `a & b` | `a & b`

C. `a ^ b` | `a ^ b`

D. `a.isdisjoint(b)` | `a.isdisjoint(b)`

**Đáp án: C**

**Giải thích:** Hiệu đối xứng giữ phần tử chỉ ở một bên.

**Q8. Which method checks that two sets do not overlap? | Phương thức nào kiểm tra hai Set không trùng nhau?**

A. `a | b` | `a | b`

B. `a & b` | `a & b`

C. `a ^ b` | `a ^ b`

D. `a.isdisjoint(b)` | `a.isdisjoint(b)`

**Đáp án: D**

**Giải thích:** isdisjoint đúng khi phần giao rỗng.

**Q9. Why does inclusion–exclusion subtract an intersection? | Vì sao bao hàm–loại trừ phải trừ phần giao?**

A. To correct double counting | Để sửa việc đếm trùng

B. Distinct elements in either set | Số phần tử khác nhau ở ít nhất một tập

C. When the sets share no members | Khi hai tập không có phần tử chung

D. An ordered List of its elements | List chứa các phần tử được sắp thứ tự

**Đáp án: A**

**Giải thích:** Phần tử giao đã được tính trong cả hai số đếm.

**Q10. What does `len(a | b)` count? | `len(a | b)` đếm gì?**

A. To correct double counting | Để sửa việc đếm trùng

B. Distinct elements in either set | Số phần tử khác nhau ở ít nhất một tập

C. When the sets share no members | Khi hai tập không có phần tử chung

D. An ordered List of its elements | List chứa các phần tử được sắp thứ tự

**Đáp án: B**

**Giải thích:** Hợp tự loại phần trùng của các nhóm.

**Q11. When is `a.isdisjoint(b)` True? | Khi nào `a.isdisjoint(b)` bằng True?**

A. To correct double counting | Để sửa việc đếm trùng

B. Distinct elements in either set | Số phần tử khác nhau ở ít nhất một tập

C. When the sets share no members | Khi hai tập không có phần tử chung

D. An ordered List of its elements | List chứa các phần tử được sắp thứ tự

**Đáp án: C**

**Giải thích:** Hai tập rời có phần giao rỗng.

**Q12. What does `sorted(my_set)` produce? | `sorted(my_set)` tạo gì?**

A. To correct double counting | Để sửa việc đếm trùng

B. Distinct elements in either set | Số phần tử khác nhau ở ít nhất một tập

C. When the sets share no members | Khi hai tập không có phần tử chung

D. An ordered List of its elements | List chứa các phần tử được sắp thứ tự

**Đáp án: D**

**Giải thích:** sorted tạo List và không sửa Set gốc.

**Q13. How many distinct values are in `{1,1,2}`? | `{1,1,2}` có mấy phần tử khác nhau?**

A. 2 | 2

B. 4 | 4

C. Every part is nonempty and the union covers the original set | Mỗi phần không rỗng và hợp phủ đủ tập gốc

D. No element is shared | Không có phần tử chung

**Đáp án: A**

**Giải thích:** Giá trị trùng chỉ xuất hiện một lần trong Set.

**Q14. If |A|=3, |B|=2, |A∩B|=1, what is |A∪B|? | Nếu |A|=3, |B|=2, |A∩B|=1 thì |A∪B| bằng bao nhiêu?**

A. 2 | 2

B. 4 | 4

C. Every part is nonempty and the union covers the original set | Mỗi phần không rỗng và hợp phủ đủ tập gốc

D. No element is shared | Không có phần tử chung

**Đáp án: B**

**Giải thích:** Dùng công thức 3+2−1=4.

**Q15. Which two conditions besides disjointness are needed to verify a nonempty partition? | Ngoài rời nhau, cần kiểm tra gì để xác nhận các phần không rỗng là phân hoạch?**

A. 2 | 2

B. 4 | 4

C. Every part is nonempty and the union covers the original set | Mỗi phần không rỗng và hợp phủ đủ tập gốc

D. No element is shared | Không có phần tử chung

**Đáp án: C**

**Giải thích:** Phân hoạch phải phủ đủ phần tử gốc và không có phần rỗng.

**Q16. What does the empty intersection mean? | Phần giao rỗng nghĩa là gì?**

A. 2 | 2

B. 4 | 4

C. Every part is nonempty and the union covers the original set | Mỗi phần không rỗng và hợp phủ đủ tập gốc

D. No element is shared | Không có phần tử chung

**Đáp án: D**

**Giải thích:** Giao rỗng biểu thị hai tập rời nhau.

**Q17. What does A∪A equal? | A∪A bằng gì?**

A. A | A

B. Empty set | Tập rỗng

C. No fixed order is promised | Không bảo đảm thứ tự cố định

D. Related records or future information may cross splits | Bản ghi liên quan hoặc thông tin tương lai có thể lọt qua hai tập

**Đáp án: A**

**Giải thích:** Hợp một tập với chính nó không thêm phần tử.

**Q18. What does A∩∅ equal? | A∩∅ bằng gì?**

A. A | A

B. Empty set | Tập rỗng

C. No fixed order is promised | Không bảo đảm thứ tự cố định

D. Related records or future information may cross splits | Bản ghi liên quan hoặc thông tin tương lai có thể lọt qua hai tập

**Đáp án: B**

**Giải thích:** Tập rỗng không có phần tử nào chung với A nên phép giao rỗng.

**Q19. Is set iteration order guaranteed? | Thứ tự duyệt Set có được đảm bảo không?**

A. A | A

B. Empty set | Tập rỗng

C. No fixed order is promised | Không bảo đảm thứ tự cố định

D. Related records or future information may cross splits | Bản ghi liên quan hoặc thông tin tương lai có thể lọt qua hai tập

**Đáp án: C**

**Giải thích:** Set Python không phải dãy có thứ tự.

**Q20. Why can two data splits with disjoint IDs still leak information? | Vì sao hai tập dữ liệu không trùng ID vẫn có thể rò rỉ thông tin?**

A. A | A

B. A itself | Chính tập A

C. No fixed order is promised | Không bảo đảm thứ tự cố định

D. Related records or future information may cross splits | Bản ghi liên quan hoặc thông tin tương lai có thể lọt qua hai tập

**Đáp án: D**

**Giải thích:** ID không trùng chưa loại được mọi nguồn rò rỉ.

## PY-22 — PY-22 — Hoán vị, tổ hợp và tam giác Pascal

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. When should permutations be used? | Khi nào dùng hoán vị/chỉnh hợp?**

A. When order matters | Khi thứ tự quan trọng

B. When order does not matter | Khi thứ tự không quan trọng

C. The product 1×2×…×n | Tích 1×2×…×n

D. The number of unordered k-subsets from n distinct items | Số nhóm k phần tử không xét thứ tự từ n phần tử khác nhau

**Đáp án: A**

**Giải thích:** Đổi thứ tự người được chọn tạo cách sắp khác.

**Q2. When should combinations be used? | Khi nào dùng tổ hợp?**

A. When order matters | Khi thứ tự quan trọng

B. When order does not matter | Khi thứ tự không quan trọng

C. The product 1×2×…×n | Tích 1×2×…×n

D. The number of unordered k-subsets from n distinct items | Số nhóm k phần tử không xét thứ tự từ n phần tử khác nhau

**Đáp án: B**

**Giải thích:** Nhóm không đổi khi thành viên đổi chỗ.

**Q3. What is factorial n!? | Giai thừa n! là gì?**

A. When order matters | Khi thứ tự quan trọng

B. When order does not matter | Khi thứ tự không quan trọng

C. The product 1×2×…×n | Tích 1×2×…×n

D. The number of unordered k-subsets from n distinct items | Số nhóm k phần tử không xét thứ tự từ n phần tử khác nhau

**Đáp án: C**

**Giải thích:** Giai thừa đếm cách sắp xếp n phần tử phân biệt.

**Q4. What is a binomial coefficient C(n,k)? | Hệ số nhị thức C(n,k) là gì?**

A. When order matters | Khi thứ tự quan trọng

B. When order does not matter | Khi thứ tự không quan trọng

C. The product 1×2×…×n | Tích 1×2×…×n

D. The number of unordered k-subsets from n distinct items | Số nhóm k phần tử không xét thứ tự từ n phần tử khác nhau

**Đáp án: D**

**Giải thích:** C(n,k) còn là hệ số trong khai triển (a+b)^n.

**Q5. Which function counts ordered selections? | Hàm nào đếm cách chọn có thứ tự?**

A. `math.perm(n, k)` | `math.perm(n, k)`

B. `math.comb(n, k)` | `math.comb(n, k)`

C. `math.factorial(n)` | `math.factorial(n)`

D. `itertools.permutations(items)` | `itertools.permutations(items)`

**Đáp án: A**

**Giải thích:** perm đếm cách chọn có thứ tự không lặp.

**Q6. Which function counts unordered selections? | Hàm nào đếm cách chọn không thứ tự?**

A. `math.perm(n, k)` | `math.perm(n, k)`

B. `math.comb(n, k)` | `math.comb(n, k)`

C. `math.factorial(n)` | `math.factorial(n)`

D. `itertools.permutations(items)` | `itertools.permutations(items)`

**Đáp án: B**

**Giải thích:** comb đếm các nhóm khác nhau, không xét sắp xếp.

**Q7. Which function calculates n!? | Hàm nào tính n!?**

A. `math.perm(n, k)` | `math.perm(n, k)`

B. `math.comb(n, k)` | `math.comb(n, k)`

C. `math.factorial(n)` | `math.factorial(n)`

D. `itertools.permutations(items)` | `itertools.permutations(items)`

**Đáp án: C**

**Giải thích:** factorial nhân các số nguyên từ một tới n.

**Q8. Which function lists all ordered arrangements? | Hàm nào liệt kê các cách sắp xếp có thứ tự?**

A. `math.perm(n, k)` | `math.perm(n, k)`

B. `math.comb(n, k)` | `math.comb(n, k)`

C. `math.factorial(n)` | `math.factorial(n)`

D. `itertools.permutations(items)` | `itertools.permutations(items)`

**Đáp án: D**

**Giải thích:** Không truyền r, permutations liệt kê toàn bộ thứ tự.

**Q9. What is the value of 0!? | 0! bằng bao nhiêu?**

A. 1 | 1

B. 6 | 6

C. 10 pairs | 10 cặp

D. 12 pairs | 12 cặp

**Đáp án: A**

**Giải thích:** Dãy rỗng có một cách sắp xếp.

**Q10. How many full orderings of three distinct items exist? | Ba phần tử phân biệt có bao nhiêu thứ tự đầy đủ?**

A. 1 | 1

B. 6 | 6

C. 10 pairs | 10 cặp

D. 12 pairs | 12 cặp

**Đáp án: B**

**Giải thích:** 3! = 3×2×1 = 6.

**Q11. How many unordered pairs can be chosen from five distinct items? | Chọn cặp không thứ tự từ năm phần tử có bao nhiêu cách?**

A. 1 | 1

B. 6 | 6

C. 10 pairs | 10 cặp

D. 12 pairs | 12 cặp

**Đáp án: C**

**Giải thích:** Chọn hai từ năm không xét thứ tự có C(5,2)=10 cặp.

**Q12. How many ordered pairs can be formed from four distinct items without repetition? | Từ bốn phần tử phân biệt có bao nhiêu cặp có thứ tự không lặp?**

A. 1 | 1

B. 6 | 6

C. 10 pairs | 10 cặp

D. 12 pairs | 12 cặp

**Đáp án: D**

**Giải thích:** 4×3 = 12.

**Q13. What identity relates combinations and permutations? | Công thức nào liên hệ tổ hợp và chỉnh hợp?**

A. P(n,k)=C(n,k)×k! | P(n,k)=C(n,k)×k!

B. 1 | 1

C. n | n

D. Each inner entry sums two entries directly above | Mỗi ô bên trong bằng tổng hai ô ngay phía trên

**Đáp án: A**

**Giải thích:** Mỗi nhóm k người có k! cách sắp.

**Q14. What is C(n,0)? | C(n,0) bằng gì?**

A. P(n,k)=C(n,k)×k! | P(n,k)=C(n,k)×k!

B. 1 | 1

C. n | n

D. Each inner entry sums two entries directly above | Mỗi ô bên trong bằng tổng hai ô ngay phía trên

**Đáp án: B**

**Giải thích:** Có một cách chọn tập rỗng.

**Q15. What is C(n,n−1)? | C(n,n−1) bằng gì?**

A. P(n,k)=C(n,k)×k! | P(n,k)=C(n,k)×k!

B. 1 | 1

C. n | n

D. Each inner entry sums two entries directly above | Mỗi ô bên trong bằng tổng hai ô ngay phía trên

**Đáp án: C**

**Giải thích:** Chọn n−1 từ n tương đương chọn một phần tử bỏ lại nên có n cách.

**Q16. How are entries in Pascal's triangle obtained? | Các ô trong tam giác Pascal được tạo ra sao?**

A. P(n,k)=C(n,k)×k! | P(n,k)=C(n,k)×k!

B. 1 | 1

C. n | n

D. Each inner entry sums two entries directly above | Mỗi ô bên trong bằng tổng hai ô ngay phía trên

**Đáp án: D**

**Giải thích:** Hệ thức Pascal cộng hai hệ số ở hàng trước.

**Q17. What does `itertools.combinations(items,2)` list? | `itertools.combinations(items,2)` liệt kê gì?**

A. Unordered two-item groups | Nhóm hai phần tử không xét thứ tự

B. Ordered two-item arrangements | Cặp hai phần tử có thứ tự

C. It returns zero | Hàm trả về 0

D. The number grows factorially | Số cách tăng theo giai thừa

**Đáp án: A**

**Giải thích:** Hàm tạo mỗi cặp khác nhau đúng một lần.

**Q18. What does `itertools.permutations(items,2)` list? | `itertools.permutations(items,2)` liệt kê gì?**

A. Unordered two-item groups | Nhóm hai phần tử không xét thứ tự

B. Ordered two-item arrangements | Cặp hai phần tử có thứ tự

C. It returns zero | Hàm trả về 0

D. The number grows factorially | Số cách tăng theo giai thừa

**Đáp án: B**

**Giải thích:** Đổi thứ tự hai phần tử tạo kết quả khác.

**Q19. What happens if k>n in `math.comb(n,k)` for nonnegative integers? | Nếu k>n trong math.comb với số nguyên không âm thì sao?**

A. Unordered two-item groups | Nhóm hai phần tử không xét thứ tự

B. Ordered two-item arrangements | Cặp hai phần tử có thứ tự

C. It returns zero | Hàm trả về 0

D. The number grows factorially | Số cách tăng theo giai thừa

**Đáp án: C**

**Giải thích:** Không thể chọn k phần tử nếu tổng phần tử ít hơn k.

**Q20. Why avoid materializing all permutations for large n? | Vì sao tránh liệt kê toàn bộ hoán vị khi n lớn?**

A. Unordered two-item groups | Nhóm hai phần tử không xét thứ tự

B. Ordered two-item arrangements | Cặp hai phần tử có thứ tự

C. It returns zero | Hàm trả về 0

D. The number grows factorially | Số cách tăng theo giai thừa

**Đáp án: D**

**Giải thích:** n! tăng nhanh khiến không thể lưu hoặc in hết.

## PY-23 — PY-23 — Đồ thị, danh sách kề và Jaccard similarity

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a graph? | Đồ thị là gì?**

A. A collection of vertices and edges | Tập các đỉnh và cạnh

B. An entity or node in the network | Một đối tượng hoặc nút trong mạng

C. A relationship connecting two vertices | Quan hệ nối hai đỉnh

D. A mapping from each vertex to its neighbors | Ánh xạ mỗi đỉnh tới các đỉnh kề

**Đáp án: A**

**Giải thích:** Đồ thị mô tả quan hệ giữa các đối tượng.

**Q2. What is a vertex? | Đỉnh trong đồ thị là gì?**

A. A collection of vertices and edges | Tập các đỉnh và cạnh

B. An entity or node in the network | Một đối tượng hoặc nút trong mạng

C. A relationship connecting two vertices | Quan hệ nối hai đỉnh

D. A mapping from each vertex to its neighbors | Ánh xạ mỗi đỉnh tới các đỉnh kề

**Đáp án: B**

**Giải thích:** Mỗi đỉnh đại diện một đối tượng.

**Q3. What is an edge? | Cạnh của đồ thị là gì?**

A. A collection of vertices and edges | Tập các đỉnh và cạnh

B. An entity or node in the network | Một đối tượng hoặc nút trong mạng

C. A relationship connecting two vertices | Quan hệ nối hai đỉnh

D. A mapping from each vertex to its neighbors | Ánh xạ mỗi đỉnh tới các đỉnh kề

**Đáp án: C**

**Giải thích:** Cạnh biểu diễn kết nối giữa các đỉnh.

**Q4. What is an adjacency list? | Danh sách kề là gì?**

A. A collection of vertices and edges | Tập các đỉnh và cạnh

B. An entity or node in the network | Một đối tượng hoặc nút trong mạng

C. A relationship connecting two vertices | Quan hệ nối hai đỉnh

D. A mapping from each vertex to its neighbors | Ánh xạ mỗi đỉnh tới các đỉnh kề

**Đáp án: D**

**Giải thích:** Danh sách kề lưu các kết nối của từng đỉnh.

**Q5. What does a directed edge A→B assert? | Cạnh có hướng A→B cho biết gì?**

A. A connection from A to B | Kết nối đi từ A đến B

B. A connection without direction | Kết nối không phân biệt chiều

C. The neighbors stored for An | Những đỉnh kề được lưu cho An

D. A sequence of connected vertices | Chuỗi các đỉnh nối tiếp nhau

**Đáp án: A**

**Giải thích:** Chiều kết nối quan trọng; B→A không tự tồn tại.

**Q6. What does an undirected edge mean? | Cạnh vô hướng có ý nghĩa gì?**

A. A connection from A to B | Kết nối đi từ A đến B

B. A connection without direction | Kết nối không phân biệt chiều

C. The neighbors stored for An | Những đỉnh kề được lưu cho An

D. A sequence of connected vertices | Chuỗi các đỉnh nối tiếp nhau

**Đáp án: B**

**Giải thích:** Quan hệ vô hướng đi được theo cả hai chiều.

**Q7. What does `graph['An']` return in an adjacency dictionary? | `graph['An']` trong Dictionary kề trả gì?**

A. A connection from A to B | Kết nối đi từ A đến B

B. A connection without direction | Kết nối không phân biệt chiều

C. The neighbors stored for An | Những đỉnh kề được lưu cho An

D. A sequence of connected vertices | Chuỗi các đỉnh nối tiếp nhau

**Đáp án: C**

**Giải thích:** Giá trị của khóa đỉnh chứa các nút lân cận.

**Q8. What does a path in a graph describe? | Đường đi trong đồ thị biểu diễn gì?**

A. A connection from A to B | Kết nối đi từ A đến B

B. A connection without direction | Kết nối không phân biệt chiều

C. The neighbors stored for An | Những đỉnh kề được lưu cho An

D. A sequence of connected vertices | Chuỗi các đỉnh nối tiếp nhau

**Đáp án: D**

**Giải thích:** Hai đỉnh liên tiếp trên đường đi phải có cạnh nối.

**Q9. What is Jaccard similarity for sets A and B? | Jaccard giữa hai Set A, B bằng gì?**

A. Intersection size divided by union size | Số phần tử giao chia số phần tử hợp

B. 1 | 1

C. 0 | 0

D. A zero union denominator | Mẫu số hợp bằng 0

**Đáp án: A**

**Giải thích:** Jaccard so phần chung với toàn bộ phần tử khác nhau.

**Q10. What is Jaccard for two identical nonempty sets? | Jaccard của hai Set giống nhau và không rỗng là gì?**

A. Intersection size divided by union size | Số phần tử giao chia số phần tử hợp

B. 1 | 1

C. 0 | 0

D. A zero union denominator | Mẫu số hợp bằng 0

**Đáp án: B**

**Giải thích:** Phép giao bằng phép hợp.

**Q11. What is Jaccard for two disjoint nonempty sets? | Jaccard của hai Set không giao nhau, không rỗng là gì?**

A. Intersection size divided by union size | Số phần tử giao chia số phần tử hợp

B. 1 | 1

C. 0 | 0

D. A zero union denominator | Mẫu số hợp bằng 0

**Đáp án: C**

**Giải thích:** Phép giao không có phần tử nào.

**Q12. What must be handled before computing Jaccard on two empty sets? | Cần xử lý gì trước khi tính Jaccard cho hai Set rỗng?**

A. Intersection size divided by union size | Số phần tử giao chia số phần tử hợp

B. 1 | 1

C. 0 | 0

D. A zero union denominator | Mẫu số hợp bằng 0

**Đáp án: D**

**Giải thích:** Nếu không xử lý sẽ chia cho 0.

**Q13. What does `nx.Graph()` create? | `nx.Graph()` tạo gì?**

A. An undirected NetworkX graph | Đồ thị vô hướng NetworkX

B. A directed NetworkX graph | Đồ thị có hướng NetworkX

C. A path with fewest edges | Đường đi có ít cạnh nhất

D. Install and import the package | Cài và import thư viện

**Đáp án: A**

**Giải thích:** Graph tạo cạnh vô hướng theo mặc định.

**Q14. What does `nx.DiGraph()` create? | `nx.DiGraph()` tạo gì?**

A. An undirected NetworkX graph | Đồ thị vô hướng NetworkX

B. A directed NetworkX graph | Đồ thị có hướng NetworkX

C. A path with fewest edges | Đường đi có ít cạnh nhất

D. Install and import the package | Cài và import thư viện

**Đáp án: B**

**Giải thích:** DiGraph phân biệt chiều cạnh.

**Q15. What does `nx.shortest_path()` find on an unweighted graph? | `nx.shortest_path()` tìm gì trên đồ thị không trọng số?**

A. An undirected NetworkX graph | Đồ thị vô hướng NetworkX

B. A directed NetworkX graph | Đồ thị có hướng NetworkX

C. A path with fewest edges | Đường đi có ít cạnh nhất

D. Install and import the package | Cài và import thư viện

**Đáp án: C**

**Giải thích:** Đường ngắn nhất không trọng số có ít cạnh nhất.

**Q16. What is required to use NetworkX in Python? | Để dùng NetworkX trong Python cần gì?**

A. An undirected NetworkX graph | Đồ thị vô hướng NetworkX

B. A directed NetworkX graph | Đồ thị có hướng NetworkX

C. A path with fewest edges | Đường đi có ít cạnh nhất

D. Install and import the package | Cài và import thư viện

**Đáp án: D**

**Giải thích:** NetworkX không thuộc thư viện chuẩn Python.

**Q17. How can neighbor display order be made consistent? | Làm sao in danh sách các đỉnh kề theo thứ tự ổn định?**

A. Call `sorted()` on neighbor sets | Gọi `sorted()` trên Set đỉnh kề

B. No valid route can be returned | Không có tuyến đường hợp lệ để trả về

C. To identify each graph entity unambiguously | Để xác định từng đối tượng không mơ hồ

D. Jaccard compares sets; shortest path follows graph edges | Jaccard so hai tập; đường ngắn nhất đi theo cạnh

**Đáp án: A**

**Giải thích:** Set không bảo đảm thứ tự khi in.

**Q18. What happens if no path exists between two vertices? | Nếu không có đường nối hai đỉnh thì sao?**

A. Call `sorted()` on neighbor sets | Gọi `sorted()` trên Set đỉnh kề

B. No valid route can be returned | Không có tuyến đường hợp lệ để trả về

C. To identify each graph entity unambiguously | Để xác định từng đối tượng không mơ hồ

D. Jaccard compares sets; shortest path follows graph edges | Jaccard so hai tập; đường ngắn nhất đi theo cạnh

**Đáp án: B**

**Giải thích:** Thuật toán tìm đường cần xử lý hai đỉnh không liên thông.

**Q19. Why should node names be unique? | Vì sao tên đỉnh nên duy nhất?**

A. Call `sorted()` on neighbor sets | Gọi `sorted()` trên Set đỉnh kề

B. No valid route can be returned | Không có tuyến đường hợp lệ để trả về

C. To identify each graph entity unambiguously | Để xác định từng đối tượng không mơ hồ

D. Jaccard compares sets; shortest path follows graph edges | Jaccard so hai tập; đường ngắn nhất đi theo cạnh

**Đáp án: C**

**Giải thích:** Mã đỉnh trùng khiến các đối tượng bị nhập làm một.

**Q20. What distinguishes Jaccard from graph shortest path? | Jaccard khác đường đi ngắn nhất ở đâu?**

A. Call `sorted()` on neighbor sets | Gọi `sorted()` trên Set đỉnh kề

B. No valid route can be returned | Không có tuyến đường hợp lệ để trả về

C. To identify each graph entity unambiguously | Để xác định từng đối tượng không mơ hồ

D. Jaccard compares sets; shortest path follows graph edges | Jaccard so hai tập; đường ngắn nhất đi theo cạnh

**Đáp án: D**

**Giải thích:** Hai công cụ trả lời hai loại câu hỏi khác nhau.

## PY-24 — PY-24 — Scalar, vector, norm, đơn vị và dot product

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a scalar? | Scalar là gì?**

A. One numeric value | Một giá trị số

B. Sum of pairwise component products | Tổng tích các cặp thành phần tương ứng

C. An ordered list of components | Dãy thành phần có thứ tự

D. Square root of the sum of squared components | Căn của tổng bình phương các thành phần

**Đáp án: A**

**Giải thích:** Scalar không gồm nhiều thành phần tọa độ.

**Q2. What is a vector? | Vector là gì?**

A. Square root of the sum of squared components | Căn của tổng bình phương các thành phần

B. One numeric value | Một giá trị số

C. Sum of pairwise component products | Tổng tích các cặp thành phần tương ứng

D. An ordered list of components | Dãy thành phần có thứ tự

**Đáp án: D**

**Giải thích:** Vị trí từng thành phần biểu thị tọa độ hoặc đặc trưng.

**Q3. What is Euclidean norm? | Norm Euclid là gì?**

A. An ordered list of components | Dãy thành phần có thứ tự

B. Sum of pairwise component products | Tổng tích các cặp thành phần tương ứng

C. Square root of the sum of squared components | Căn của tổng bình phương các thành phần

D. One numeric value | Một giá trị số

**Đáp án: C**

**Giải thích:** Norm L2 đo độ dài theo Euclid.

**Q4. What is the dot product? | Tích vô hướng là gì?**

A. Sum of pairwise component products | Tổng tích các cặp thành phần tương ứng

B. An ordered list of components | Dãy thành phần có thứ tự

C. One numeric value | Một giá trị số

D. Square root of the sum of squared components | Căn của tổng bình phương các thành phần

**Đáp án: A**

**Giải thích:** Tích vô hướng cho một số từ hai vector cùng số thành phần.

**Q5. Given u = [1, 4] and v = [3, 2], what is u · v? | Cho u = [1, 4] và v = [3, 2], tích vô hướng u · v bằng bao nhiêu?**

A. 9 | 9

B. 11 | 11

C. 14 | 14

D. 8 | 8

**Đáp án: B**

**Giải thích:** Tính các tích cùng vị trí rồi cộng: 1 × 3 + 4 × 2 = 11. Không cộng riêng từng vector trước khi nhân.

**Q6. What is the length of vector (6, 8)? | Độ dài vector (6, 8) là bao nhiêu?**

A. 10 | 10

B. 8 | 8

C. 14 | 14

D. 100 | 100

**Đáp án: A**

**Giải thích:** Độ dài Euclid là căn bậc hai của 6² + 8² = 100, nên bằng 10.

**Q7. If u = (2, −1), what is −2u? | Nếu u = (2, −1), vector −2u bằng bao nhiêu?**

A. (−4, 2) | (−4, 2)

B. (−2, 1) | (−2, 1)

C. (4, −2) | (4, −2)

D. (−4, −2) | (−4, −2)

**Đáp án: A**

**Giải thích:** Nhân từng tọa độ của u với −2: −2 × 2 = −4 và −2 × (−1) = 2.

**Q8. Given a = (2, 1) and b = (−1, 2), what is their dot product? | Cho a = (2, 1) và b = (−1, 2), tích vô hướng bằng bao nhiêu?**

A. 1 | 1

B. 0 | 0

C. 4 | 4

D. 3 | 3

**Đáp án: B**

**Giải thích:** 2 × (−1) + 1 × 2 = 0. Hai vector khác không có tích vô hướng bằng 0 thì vuông góc.

**Q9. What is the norm of vector (3,4)? | Norm của vector (3,4) bằng bao nhiêu?**

A. 0 | 0

B. 11 | 11

C. 5 | 5

D. (0.6,0.8) | (0.6,0.8)

**Đáp án: C**

**Giải thích:** Độ dài Pythagoras là căn của 9+16.

**Q10. What is the unit vector in the direction (3,4)? | Vector đơn vị theo hướng (3,4) là gì?**

A. 5 | 5

B. (0.6,0.8) | (0.6,0.8)

C. 11 | 11

D. 0 | 0

**Đáp án: B**

**Giải thích:** Chia mỗi thành phần cho độ dài năm.

**Q11. What is the dot product (1,2)·(3,4)? | Tích vô hướng (1,2)·(3,4) bằng bao nhiêu?**

A. 5 | 5

B. 11 | 11

C. (0.6,0.8) | (0.6,0.8)

D. 0 | 0

**Đáp án: B**

**Giải thích:** Tính 1×3 + 2×4.

**Q12. What is the dot product of (1,0) and (0,1)? | Tích vô hướng của (1,0) và (0,1) là bao nhiêu?**

A. (0.6,0.8) | (0.6,0.8)

B. 0 | 0

C. 5 | 5

D. 11 | 11

**Đáp án: B**

**Giải thích:** Cả hai tích thành phần đều bằng không.

**Q13. What is the dot product of two nonzero perpendicular vectors? | Tích vô hướng của hai vector khác không vuông góc là gì?**

A. That its norm is nonzero | Norm khác không

B. Zero | Bằng không

C. They must have equal lengths | Chúng phải có cùng số phần tử

D. The result can be physically misleading | Kết quả có thể sai ý nghĩa vật lý

**Đáp án: B**

**Giải thích:** Hai hướng trực giao có tích vô hướng bằng không.

**Q14. What must be checked before normalizing a vector? | Cần kiểm tra gì trước khi chuẩn hóa vector?**

A. They must have equal lengths | Chúng phải có cùng số phần tử

B. Zero | Bằng không

C. The result can be physically misleading | Kết quả có thể sai ý nghĩa vật lý

D. That its norm is nonzero | Norm khác không

**Đáp án: D**

**Giải thích:** Chia cho norm bằng không không xác định.

**Q15. What happens if coordinate units are mixed in a distance calculation? | Nếu đơn vị tọa độ không thống nhất khi tính khoảng cách thì sao?**

A. They must have equal lengths | Chúng phải có cùng số phần tử

B. That its norm is nonzero | Norm khác không

C. The result can be physically misleading | Kết quả có thể sai ý nghĩa vật lý

D. Zero | Bằng không

**Đáp án: C**

**Giải thích:** Tính norm có ý nghĩa khi đơn vị phù hợp.

**Q16. What must be true to compute a 1-D dot product? | Muốn tính tích vô hướng của hai vector 1-D cần điều kiện gì?**

A. That its norm is nonzero | Norm khác không

B. They must have equal lengths | Chúng phải có cùng số phần tử

C. Zero | Bằng không

D. The result can be physically misleading | Kết quả có thể sai ý nghĩa vật lý

**Đáp án: B**

**Giải thích:** Từng thành phần được ghép theo vị trí tương ứng.

**Q17. What does multiplying a vector by a scalar do? | Nhân vector với scalar làm gì?**

A. To multiply each weight by its intended feature | Để trọng số nhân đúng đặc trưng tương ứng

B. Subtract corresponding components | Trừ các thành phần cùng vị trí

C. Scales every component | Nhân từng thành phần với scalar

D. Euclidean distance between a and b | Khoảng cách Euclid giữa a và b

**Đáp án: C**

**Giải thích:** Nhân scalar làm đổi độ lớn từng thành phần.

**Q18. How is vector subtraction performed? | Phép trừ vector được thực hiện thế nào?**

A. Scales every component | Nhân từng thành phần với scalar

B. Euclidean distance between a and b | Khoảng cách Euclid giữa a và b

C. To multiply each weight by its intended feature | Để trọng số nhân đúng đặc trưng tương ứng

D. Subtract corresponding components | Trừ các thành phần cùng vị trí

**Đáp án: D**

**Giải thích:** Phép trừ vector diễn ra theo từng thành phần.

**Q19. What does `np.linalg.norm(a-b)` measure? | `np.linalg.norm(a-b)` đo điều gì?**

A. To multiply each weight by its intended feature | Để trọng số nhân đúng đặc trưng tương ứng

B. Subtract corresponding components | Trừ các thành phần cùng vị trí

C. Scales every component | Nhân từng thành phần với scalar

D. Euclidean distance between a and b | Khoảng cách Euclid giữa a và b

**Đáp án: D**

**Giải thích:** Norm của độ dịch chuyển cho khoảng cách.

**Q20. Why are feature weights paired with values in the same order? | Vì sao trọng số cần cùng thứ tự với các giá trị?**

A. Euclidean distance between a and b | Khoảng cách Euclid giữa a và b

B. To multiply each weight by its intended feature | Để trọng số nhân đúng đặc trưng tương ứng

C. Scales every component | Nhân từng thành phần với scalar

D. Subtract corresponding components | Trừ các thành phần cùng vị trí

**Đáp án: B**

**Giải thích:** Sai thứ tự tạo ra tích vô hướng khác.

## PY-25 — PY-25 — Ma trận, chuyển vị, nhân ma trận và định thức

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a matrix? | Ma trận là gì?**

A. Rows of the left matrix with columns of the right | Hàng ma trận trái với cột ma trận phải

B. A two-dimensional array of values | Bảng dữ liệu hai chiều

C. A scalar associated with a square matrix | Một số gắn với ma trận vuông

D. A matrix with rows and columns exchanged | Ma trận đổi vai trò hàng và cột

**Đáp án: B**

**Giải thích:** Ma trận sắp phần tử theo hàng và cột.

**Q2. What is the transpose of a matrix? | Chuyển vị của ma trận là gì?**

A. A matrix with rows and columns exchanged | Ma trận đổi vai trò hàng và cột

B. A two-dimensional array of values | Bảng dữ liệu hai chiều

C. Rows of the left matrix with columns of the right | Hàng ma trận trái với cột ma trận phải

D. A scalar associated with a square matrix | Một số gắn với ma trận vuông

**Đáp án: A**

**Giải thích:** Chuyển vị hoán đổi các trục ma trận.

**Q3. What does matrix multiplication combine? | Phép nhân ma trận kết hợp gì?**

A. Rows of the left matrix with columns of the right | Hàng ma trận trái với cột ma trận phải

B. A two-dimensional array of values | Bảng dữ liệu hai chiều

C. A matrix with rows and columns exchanged | Ma trận đổi vai trò hàng và cột

D. A scalar associated with a square matrix | Một số gắn với ma trận vuông

**Đáp án: A**

**Giải thích:** Mỗi ô kết quả là tích vô hướng một hàng với một cột.

**Q4. What is a determinant? | Định thức là gì?**

A. Rows of the left matrix with columns of the right | Hàng ma trận trái với cột ma trận phải

B. A two-dimensional array of values | Bảng dữ liệu hai chiều

C. A scalar associated with a square matrix | Một số gắn với ma trận vuông

D. A matrix with rows and columns exchanged | Ma trận đổi vai trò hàng và cột

**Đáp án: C**

**Giải thích:** Định thức hỗ trợ kiểm tra tính khả nghịch.

**Q5. Let A = [[2, 1], [0, 3]] and B = [[1, 4], [5, 2]]. What is element (row 1, column 2) of AB? | Cho A và B như trên. Phần tử hàng 1, cột 2 của AB là bao nhiêu?**

A. 8 | 8

B. 12 | 12

C. 6 | 6

D. 10 | 10

**Đáp án: D**

**Giải thích:** Nhân hàng 1 của A với cột 2 của B: 2 × 4 + 1 × 2 = 10.

**Q6. What is the determinant of [[3, 1], [2, 1]]? | Định thức của ma trận [[3, 1], [2, 1]] bằng bao nhiêu?**

A. 2 | 2

B. 1 | 1

C. 5 | 5

D. 0 | 0

**Đáp án: B**

**Giải thích:** Với ma trận 2 × 2, lấy tích đường chéo chính trừ đường chéo phụ: 3 × 1 − 1 × 2 = 1.

**Q7. A square matrix has determinant 0. Which statement is correct? | Một ma trận vuông có định thức bằng 0. Phát biểu nào đúng?**

A. It must be diagonal | Nó bắt buộc là ma trận đường chéo

B. All entries are zero | Mọi phần tử đều bằng 0

C. It has no inverse | Nó không có ma trận nghịch đảo

D. It is the identity matrix | Nó là ma trận đơn vị

**Đáp án: C**

**Giải thích:** Định thức 0 nghĩa là ma trận suy biến và không khả nghịch; các kết luận khác không nhất thiết đúng.

**Q8. If A has shape (2, 3) and B has shape (3, 4), what is the shape of AB? | Nếu A có kích thước (2, 3), B có kích thước (3, 4), AB có kích thước nào?**

A. (4, 2) | (4, 2)

B. (2, 4) | (2, 4)

C. (2, 3) | (2, 3)

D. (3, 3) | (3, 3)

**Đáp án: B**

**Giải thích:** Hai chiều ở giữa (3 và 3) phải khớp; ma trận kết quả lấy số hàng của A và số cột của B: (2, 4).

**Q9. Which operator performs matrix multiplication? | Toán tử nào thực hiện nhân ma trận?**

A. `@` | `@`

B. `np.linalg.inv(A)` | `np.linalg.inv(A)`

C. `.T` | `.T`

D. `np.linalg.det(A)` | `np.linalg.det(A)`

**Đáp án: A**

**Giải thích:** @ thực hiện đúng quy tắc nhân ma trận.

**Q10. Which attribute returns the transpose of a 2-D ndarray? | Thuộc tính nào cho chuyển vị mảng 2-D?**

A. `@` | `@`

B. `np.linalg.det(A)` | `np.linalg.det(A)`

C. `.T` | `.T`

D. `np.linalg.inv(A)` | `np.linalg.inv(A)`

**Đáp án: C**

**Giải thích:** T là thuộc tính chuyển vị tiện dụng.

**Q11. Which function computes a square matrix determinant? | Hàm nào tính định thức ma trận vuông?**

A. `@` | `@`

B. `.T` | `.T`

C. `np.linalg.det(A)` | `np.linalg.det(A)`

D. `np.linalg.inv(A)` | `np.linalg.inv(A)`

**Đáp án: C**

**Giải thích:** det trả định thức dạng số.

**Q12. Which function computes a nonsingular matrix inverse? | Hàm nào tính nghịch đảo ma trận khả nghịch?**

A. `np.linalg.inv(A)` | `np.linalg.inv(A)`

B. `.T` | `.T`

C. `np.linalg.det(A)` | `np.linalg.det(A)`

D. `@` | `@`

**Đáp án: A**

**Giải thích:** inv tính nghịch đảo khi ma trận khả nghịch.

**Q13. When is a square matrix invertible? | Khi nào ma trận vuông khả nghịch?**

A. `np.allclose(A, B)` | `np.allclose(A, B)`

B. Identity matrix | Ma trận đơn vị

C. Its determinant is nonzero | Định thức khác không

D. 3 | 3

**Đáp án: C**

**Giải thích:** Định thức khác 0 tương đương khả nghịch.

**Q14. What is determinant of [[2,1],[1,2]]? | Định thức [[2,1],[1,2]] bằng gì?**

A. Identity matrix | Ma trận đơn vị

B. 3 | 3

C. `np.allclose(A, B)` | `np.allclose(A, B)`

D. Its determinant is nonzero | Định thức khác không

**Đáp án: B**

**Giải thích:** Định thức 2×2 bằng 2×2−1×1.

**Q15. What does `A @ inv(A)` approximate? | `A @ inv(A)` gần bằng gì?**

A. Its determinant is nonzero | Định thức khác không

B. 3 | 3

C. Identity matrix | Ma trận đơn vị

D. `np.allclose(A, B)` | `np.allclose(A, B)`

**Đáp án: C**

**Giải thích:** Nhân ma trận với nghịch đảo bằng I trong tính toán chính xác.

**Q16. How do you test approximate equality of float arrays? | Kiểm tra hai mảng float gần bằng nhau bằng gì?**

A. Identity matrix | Ma trận đơn vị

B. `np.allclose(A, B)` | `np.allclose(A, B)`

C. Its determinant is nonzero | Định thức khác không

D. 3 | 3

**Đáp án: B**

**Giải thích:** allclose chấp nhận sai số dấu phẩy động nhỏ.

**Q17. Which dimensions must match for A @ B? | Nhân A @ B cần các chiều nào bằng nhau?**

A. Columns of A and rows of B | Số cột A và số hàng B

B. Element-wise multiplication | Nhân theo từng phần tử

C. `np.linalg.solve(A, b)` | `np.linalg.solve(A, b)`

D. A linear algebra error | Lỗi đại số tuyến tính

**Đáp án: A**

**Giải thích:** Nhân ma trận yêu cầu hai chiều trong trùng.

**Q18. What does `A * B` do for compatible NumPy arrays? | `A * B` trên mảng NumPy tương thích làm gì?**

A. A linear algebra error | Lỗi đại số tuyến tính

B. `np.linalg.solve(A, b)` | `np.linalg.solve(A, b)`

C. Columns of A and rows of B | Số cột A và số hàng B

D. Element-wise multiplication | Nhân theo từng phần tử

**Đáp án: D**

**Giải thích:** Dấu sao nhân phần tử tương ứng có broadcasting.

**Q19. What is preferred to solve Ax=b numerically? | Để giải hệ Ax=b bằng NumPy nên ưu tiên gì?**

A. Element-wise multiplication | Nhân theo từng phần tử

B. Columns of A and rows of B | Số cột A và số hàng B

C. A linear algebra error | Lỗi đại số tuyến tính

D. `np.linalg.solve(A, b)` | `np.linalg.solve(A, b)`

**Đáp án: D**

**Giải thích:** Giải trực tiếp thường tốt hơn tính nghịch đảo rồi nhân.

**Q20. What happens to a singular matrix when using `np.linalg.inv`? | Dùng `np.linalg.inv` với ma trận suy biến thường gây gì?**

A. Columns of A and rows of B | Số cột A và số hàng B

B. A linear algebra error | Lỗi đại số tuyến tính

C. Element-wise multiplication | Nhân theo từng phần tử

D. `np.linalg.solve(A, b)` | `np.linalg.solve(A, b)`

**Đáp án: B**

**Giải thích:** Ma trận suy biến không có nghịch đảo.

## PY-26 — PY-26 — Hệ phương trình tuyến tính, rank và nghiệm

**Các câu hỏi chỉ kiểm tra khái niệm và cách áp dụng kiến thức, không yêu cầu nhớ tình huống thực hành.**

**Q1. What is a linear system? | Hệ tuyến tính là gì?**

A. The coefficients multiplying the unknowns | Các hệ số nhân với từng ẩn

B. The number of linearly independent rows or columns | Số hàng hoặc cột độc lập tuyến tính

C. `A @ x - b` | `A @ x - b`

D. Several linear equations sharing unknowns | Nhiều phương trình tuyến tính chung các ẩn

**Đáp án: D**

**Giải thích:** Các phương trình cùng chứa các ẩn cần giải.

**Q2. What does the rank of a matrix measure? | Rank của ma trận đo gì?**

A. The number of linearly independent rows or columns | Số hàng hoặc cột độc lập tuyến tính

B. `A @ x - b` | `A @ x - b`

C. Several linear equations sharing unknowns | Nhiều phương trình tuyến tính chung các ẩn

D. The coefficients multiplying the unknowns | Các hệ số nhân với từng ẩn

**Đáp án: A**

**Giải thích:** Rank đếm hướng độc lập, không chỉ số hàng.

**Q3. What does a coefficient matrix contain? | Ma trận hệ số chứa gì?**

A. The number of linearly independent rows or columns | Số hàng hoặc cột độc lập tuyến tính

B. Several linear equations sharing unknowns | Nhiều phương trình tuyến tính chung các ẩn

C. The coefficients multiplying the unknowns | Các hệ số nhân với từng ẩn

D. `A @ x - b` | `A @ x - b`

**Đáp án: C**

**Giải thích:** Ma trận chứa hệ số số học của từng ẩn.

**Q4. What is the residual vector for Ax=b? | Vector sai số dư của Ax=b là gì?**

A. The number of linearly independent rows or columns | Số hàng hoặc cột độc lập tuyến tính

B. `A @ x - b` | `A @ x - b`

C. The coefficients multiplying the unknowns | Các hệ số nhân với từng ẩn

D. Several linear equations sharing unknowns | Nhiều phương trình tuyến tính chung các ẩn

**Đáp án: B**

**Giải thích:** Lấy Ax trừ b cho độ lệch từng phương trình.

**Q5. Solve x + y = 7 and x − y = 3. What are x and y? | Giải hệ x + y = 7 và x − y = 3. Tìm x và y.**

A. x = 2, y = 5 | x = 2, y = 5

B. x = 7, y = 0 | x = 7, y = 0

C. x = 5, y = 2 | x = 5, y = 2

D. x = 4, y = 3 | x = 4, y = 3

**Đáp án: C**

**Giải thích:** Cộng hai phương trình: 2x = 10 nên x = 5; thay vào x + y = 7 được y = 2.

**Q6. What can be concluded about x + y = 3 and x + y = 5? | Hệ x + y = 3 và x + y = 5 có kết luận gì?**

A. A unique solution | Có nghiệm duy nhất

B. Exactly two solutions | Có đúng hai nghiệm

C. The solution is (3, 5) | Nghiệm là (3, 5)

D. No solution | Vô nghiệm

**Đáp án: D**

**Giải thích:** Cùng một tổng x + y không thể đồng thời bằng 3 và 5, nên hai phương trình mâu thuẫn.

**Q7. What is the determinant of [[1, 2], [2, 4]]? | Định thức của [[1, 2], [2, 4]] là bao nhiêu?**

A. 0 | 0

B. 8 | 8

C. 4 | 4

D. 2 | 2

**Đáp án: A**

**Giải thích:** 1 × 4 − 2 × 2 = 0; hàng thứ hai gấp đôi hàng thứ nhất, nên ma trận thiếu hạng.

**Q8. Does (x, y) = (2, 1) solve x + 2y = 4 and 3x + y = 7? | Cặp (x, y) = (2, 1) có giải đúng hệ x + 2y = 4 và 3x + y = 7 không?**

A. No, both equations fail | Không, cả hai đều sai

B. No, the second equation fails | Không, phương trình sau sai

C. No, the first equation fails | Không, phương trình đầu sai

D. Yes, both equations hold | Có, cả hai đều đúng

**Đáp án: D**

**Giải thích:** Thế x = 2, y = 1: 2 + 2 × 1 = 4 và 3 × 2 + 1 = 7, nên đây là một nghiệm.

**Q9. For Ax=b with A shape (3,2), what do the rows represent? | Với A shape (3,2), các hàng biểu diễn gì?**

A. The right-hand-side values | Các giá trị vế phải

B. Coefficients of two unknowns | Hệ số của hai ẩn

C. It cannot have a unique solution for every b | Không thể có nghiệm duy nhất với mọi b

D. Three equations or observations | Ba phương trình hoặc quan sát

**Đáp án: D**

**Giải thích:** Ba hàng tương ứng ba quan sát hoặc phương trình.

**Q10. For Ax=b with A shape (3,2), what do the columns represent? | Với A shape (3,2), các cột biểu diễn gì?**

A. Three equations or observations | Ba phương trình hoặc quan sát

B. The right-hand-side values | Các giá trị vế phải

C. It cannot have a unique solution for every b | Không thể có nghiệm duy nhất với mọi b

D. Coefficients of two unknowns | Hệ số của hai ẩn

**Đáp án: D**

**Giải thích:** Hai cột là hệ số của hai ẩn ở từng phương trình.

**Q11. What does the final column of an augmented matrix represent? | Cột cuối của ma trận mở rộng biểu diễn gì?**

A. It cannot have a unique solution for every b | Không thể có nghiệm duy nhất với mọi b

B. Coefficients of two unknowns | Hệ số của hai ẩn

C. Three equations or observations | Ba phương trình hoặc quan sát

D. The right-hand-side values | Các giá trị vế phải

**Đáp án: D**

**Giải thích:** Ma trận mở rộng ghi các vế phải ở cột cuối.

**Q12. What does a rank-deficient square matrix imply? | Ma trận vuông thiếu hạng gợi ý điều gì?**

A. It cannot have a unique solution for every b | Không thể có nghiệm duy nhất với mọi b

B. Coefficients of two unknowns | Hệ số của hai ẩn

C. Three equations or observations | Ba phương trình hoặc quan sát

D. The right-hand-side values | Các giá trị vế phải

**Đáp án: A**

**Giải thích:** Thiếu hạng đầy đủ khiến không bảo đảm nghiệm duy nhất.

**Q13. If the residual is exactly zero, what is true? | Nếu sai số dư bằng 0 thì điều gì đúng?**

A. Ranks of A and its augmented matrix | Hạng của A và ma trận mở rộng

B. Whether a candidate solution approximately satisfies the system | Nghiệm thử có thỏa hệ gần đúng hay không

C. The sum of squared residuals | Tổng bình phương sai số dư

D. Every equation is satisfied | Mọi phương trình đều được thỏa

**Đáp án: D**

**Giải thích:** Sai số dư bằng 0 nghĩa là Ax=b.

**Q14. What does least squares minimize? | Bình phương tối thiểu làm nhỏ nhất gì?**

A. Ranks of A and its augmented matrix | Hạng của A và ma trận mở rộng

B. Every equation is satisfied | Mọi phương trình đều được thỏa

C. The sum of squared residuals | Tổng bình phương sai số dư

D. Whether a candidate solution approximately satisfies the system | Nghiệm thử có thỏa hệ gần đúng hay không

**Đáp án: C**

**Giải thích:** Bình phương sai lệch làm lỗi lớn bị phạt mạnh.

**Q15. What does `np.allclose(A@x,b)` check? | `np.allclose(A@x,b)` kiểm tra gì?**

A. Ranks of A and its augmented matrix | Hạng của A và ma trận mở rộng

B. Whether a candidate solution approximately satisfies the system | Nghiệm thử có thỏa hệ gần đúng hay không

C. The sum of squared residuals | Tổng bình phương sai số dư

D. Every equation is satisfied | Mọi phương trình đều được thỏa

**Đáp án: B**

**Giải thích:** allclose so kết quả trong ngưỡng sai số số học.

**Q16. What should be compared to diagnose inconsistency of a system? | Để xét hệ vô nghiệm cần so sánh gì?**

A. Whether a candidate solution approximately satisfies the system | Nghiệm thử có thỏa hệ gần đúng hay không

B. The sum of squared residuals | Tổng bình phương sai số dư

C. Every equation is satisfied | Mọi phương trình đều được thỏa

D. Ranks of A and its augmented matrix | Hạng của A và ma trận mở rộng

**Đáp án: D**

**Giải thích:** Hạng A khác hạng [A, b] cho biết hệ vô nghiệm.

**Q17. Why isn't the right-hand side b another unknown? | Vì sao b không phải một ẩn mới?**

A. It contains known target values | Nó chứa giá trị mục tiêu đã biết

B. They add no new independent direction | Chúng không bổ sung hướng độc lập mới

C. When observations outnumber unknowns or do not fit exactly | Khi nhiều quan sát hơn ẩn hoặc không khớp chính xác

D. Prediction is lower than actual | Dự báo thấp hơn thực tế

**Đáp án: A**

**Giải thích:** b là dữ liệu đã biết, x mới là biến chưa biết.

**Q18. What happens when rows of A are multiples of each other? | Nếu các hàng A là bội nhau thì sao?**

A. Prediction is lower than actual | Dự báo thấp hơn thực tế

B. They add no new independent direction | Chúng không bổ sung hướng độc lập mới

C. It contains known target values | Nó chứa giá trị mục tiêu đã biết

D. When observations outnumber unknowns or do not fit exactly | Khi nhiều quan sát hơn ẩn hoặc không khớp chính xác

**Đáp án: B**

**Giải thích:** Hàng tỷ lệ chỉ lặp thông tin tuyến tính.

**Q19. When is `lstsq` useful? | Khi nào `lstsq` hữu ích?**

A. Prediction is lower than actual | Dự báo thấp hơn thực tế

B. When observations outnumber unknowns or do not fit exactly | Khi nhiều quan sát hơn ẩn hoặc không khớp chính xác

C. It contains known target values | Nó chứa giá trị mục tiêu đã biết

D. They add no new independent direction | Chúng không bổ sung hướng độc lập mới

**Đáp án: B**

**Giải thích:** Bình phương tối thiểu tìm cách khớp tốt nhất khi hệ không thỏa hết.

**Q20. What does a negative residual mean under r=prediction−actual? | Sai số dư âm theo r=dự báo−thực tế nghĩa là gì?**

A. When observations outnumber unknowns or do not fit exactly | Khi nhiều quan sát hơn ẩn hoặc không khớp chính xác

B. Prediction is lower than actual | Dự báo thấp hơn thực tế

C. They add no new independent direction | Chúng không bổ sung hướng độc lập mới

D. It contains known target values | Nó chứa giá trị mục tiêu đã biết

**Đáp án: B**

**Giải thích:** Dự báo trừ thực tế là số âm khi dự báo thiếu.

## PY-27 — PY-27 — Eigenvalue, Eigenvector và hướng biến thiên

**Chỉ kiểm tra kiến thức bài học; không kiểm tra ghi nhớ tình huống đánh số.**

**Q1. What defines an eigenvector v of A? | Điều kiện định nghĩa vector riêng v của A là gì?**

A. `A @ v = λ*v` with v nonzero | `A @ v = λ*v` với v khác không

B. A covariance eigenvector with high eigenvalue | Vector riêng hiệp phương sai có trị riêng lớn

C. How two variables vary together | Hai biến cùng biến thiên ra sao

D. Scaling along a corresponding eigenvector | Hệ số co giãn theo vector riêng tương ứng

**Đáp án: A**

**Giải thích:** Vector khác không giữ phương đến hệ số nhân.

**Q2. What does an eigenvalue represent? | Trị riêng biểu thị gì?**

A. `A @ v = λ*v` with v nonzero | `A @ v = λ*v` với v khác không

B. Scaling along a corresponding eigenvector | Hệ số co giãn theo vector riêng tương ứng

C. How two variables vary together | Hai biến cùng biến thiên ra sao

D. A covariance eigenvector with high eigenvalue | Vector riêng hiệp phương sai có trị riêng lớn

**Đáp án: B**

**Giải thích:** Trị riêng là hệ số λ nhân vector riêng.

**Q3. What does covariance describe? | Hiệp phương sai mô tả gì?**

A. How two variables vary together | Hai biến cùng biến thiên ra sao

B. `A @ v = λ*v` with v nonzero | `A @ v = λ*v` với v khác không

C. Scaling along a corresponding eigenvector | Hệ số co giãn theo vector riêng tương ứng

D. A covariance eigenvector with high eigenvalue | Vector riêng hiệp phương sai có trị riêng lớn

**Đáp án: A**

**Giải thích:** Hiệp phương sai đo sự biến thiên cùng nhau.

**Q4. What is a principal direction in PCA? | Hướng chính trong PCA là gì?**

A. A covariance eigenvector with high eigenvalue | Vector riêng hiệp phương sai có trị riêng lớn

B. Scaling along a corresponding eigenvector | Hệ số co giãn theo vector riêng tương ứng

C. `A @ v = λ*v` with v nonzero | `A @ v = λ*v` với v khác không

D. How two variables vary together | Hai biến cùng biến thiên ra sao

**Đáp án: A**

**Giải thích:** Vector riêng hiệp phương sai nổi bật mang phương sai lớn nhất.

**Q5. For A = [[3, 0], [0, 1]], what eigenvalue belongs to v = [1, 0]? | Với A = [[3, 0], [0, 1]], vector riêng v = [1, 0] ứng với trị riêng nào?**

A. 1 | 1

B. 4 | 4

C. 0 | 0

D. 3 | 3

**Đáp án: D**

**Giải thích:** Nhân A với v được [3, 0] = 3v; do đó trị riêng tương ứng bằng 3.

**Q6. A PCA model explains 70% variance with PC1 and 20% with PC2. How much is retained by both? | PCA giữ 70% phương sai ở PC1 và 20% ở PC2. Giữ cả hai thì được bao nhiêu?**

A. 50% | 50%

B. 100% | 100%

C. 70% | 70%

D. 90% | 90%

**Đáp án: D**

**Giải thích:** Tỷ lệ phương sai giải thích được cộng khi chọn các thành phần chính: 70% + 20% = 90%.

**Q7. In a 2-feature dataset, variance along x is 9 and along y is 1, with zero covariance. Which PCA direction comes first? | Dữ liệu hai đặc trưng có phương sai theo x là 9, theo y là 1, hiệp phương sai bằng 0. PCA chọn hướng đầu tiên nào?**

A. The y-axis | Trục y

B. No direction exists | Không có hướng nào

C. The x-axis | Trục x

D. An equal mix of x and y | Pha đều x và y

**Đáp án: C**

**Giải thích:** Khi hiệp phương sai bằng 0, trục có phương sai lớn nhất (trục x, bằng 9) là hướng thành phần chính đầu tiên.

**Q8. If the first principal component retains 80% of total variance, what percentage is not retained by that component? | Nếu thành phần chính đầu tiên giữ 80% tổng phương sai, bao nhiêu phần trăm không được giữ bởi riêng thành phần đó?**

A. 20% | 20%

B. 10% | 10%

C. 0% | 0%

D. 80% | 80%

**Đáp án: A**

**Giải thích:** Phần còn lại là 100% − 80% = 20%, nằm ở các hướng trực giao khác.

**Q9. What is the shape of a covariance matrix for three features? | Ma trận covariance cho ba đặc trưng có shape gì?**

A. Columns of the second returned array | Các cột của mảng trả về thứ hai

B. v and −v describe the same eigendirection | v và −v biểu diễn cùng trục riêng

C. No variance along that direction | Không biến thiên theo hướng đó

D. `(3,3)` | `(3,3)`

**Đáp án: D**

**Giải thích:** Mỗi đặc trưng ghép với từng đặc trưng.

**Q10. Which object contains eigenvectors returned by `eigh`? | Trong kết quả của `eigh`, vector riêng nằm đâu?**

A. v and −v describe the same eigendirection | v và −v biểu diễn cùng trục riêng

B. `(3,3)` | `(3,3)`

C. No variance along that direction | Không biến thiên theo hướng đó

D. Columns of the second returned array | Các cột của mảng trả về thứ hai

**Đáp án: D**

**Giải thích:** eigh lưu mỗi vector riêng ở một cột.

**Q11. Why can an eigenvector's sign change? | Vì sao dấu vector riêng có thể đảo?**

A. v and −v describe the same eigendirection | v và −v biểu diễn cùng trục riêng

B. No variance along that direction | Không biến thiên theo hướng đó

C. `(3,3)` | `(3,3)`

D. Columns of the second returned array | Các cột của mảng trả về thứ hai

**Đáp án: A**

**Giải thích:** Đảo dấu vector riêng vẫn thỏa phương trình.

**Q12. What does a zero covariance eigenvalue suggest? | Trị riêng covariance bằng 0 gợi ý gì?**

A. Columns of the second returned array | Các cột của mảng trả về thứ hai

B. `(3,3)` | `(3,3)`

C. v and −v describe the same eigendirection | v và −v biểu diễn cùng trục riêng

D. No variance along that direction | Không biến thiên theo hướng đó

**Đáp án: D**

**Giải thích:** Trị riêng 0 nghĩa là không có phương sai theo trục đó.

**Q13. How does PCA choose its first component? | PCA chọn thành phần đầu ra sao?**

A. By largest explained variance | Theo phương sai giải thích lớn nhất

B. Variance of one feature | Phương sai của một đặc trưng

C. Two | Hai

D. `A @ v` approximately equals `λ*v` | `A @ v` xấp xỉ `λ*v`

**Đáp án: A**

**Giải thích:** Thành phần đầu tương ứng phương sai cao nhất.

**Q14. What does a covariance diagonal entry represent? | Ô đường chéo covariance biểu thị gì?**

A. `A @ v` approximately equals `λ*v` | `A @ v` xấp xỉ `λ*v`

B. By largest explained variance | Theo phương sai giải thích lớn nhất

C. Variance of one feature | Phương sai của một đặc trưng

D. Two | Hai

**Đáp án: C**

**Giải thích:** Hiệp phương sai của biến với chính nó là phương sai.

**Q15. How many eigenvalues does a 2×2 symmetric matrix have counting multiplicity? | Ma trận đối xứng 2×2 có bao nhiêu trị riêng tính cả bội?**

A. `A @ v` approximately equals `λ*v` | `A @ v` xấp xỉ `λ*v`

B. Two | Hai

C. By largest explained variance | Theo phương sai giải thích lớn nhất

D. Variance of one feature | Phương sai của một đặc trưng

**Đáp án: B**

**Giải thích:** Ma trận 2×2 có hai trị riêng tính bội.

**Q16. Which relation validates an eigenpair? | Quan hệ nào dùng kiểm tra cặp riêng?**

A. `A @ v` approximately equals `λ*v` | `A @ v` xấp xỉ `λ*v`

B. Variance of one feature | Phương sai của một đặc trưng

C. Two | Hai

D. By largest explained variance | Theo phương sai giải thích lớn nhất

**Đáp án: A**

**Giải thích:** Cặp riêng thỏa Av=λv theo sai số số học.

**Q17. Which data layout corresponds to `rowvar=False`? | `rowvar=False` tương ứng bố trí nào?**

A. Only when the matrix is an appropriate covariance matrix | Chỉ khi ma trận là covariance phù hợp

B. One principal-component feature per sample | Một đặc trưng thành phần chính cho mỗi mẫu

C. Rows are samples and columns are features | Hàng là mẫu và cột là đặc trưng

D. Feature scales and units | Thang đo và đơn vị các đặc trưng

**Đáp án: C**

**Giải thích:** Quan sát nằm theo hàng khi rowvar=False.

**Q18. Does an eigenvalue always mean variance? | Trị riêng có luôn mang nghĩa phương sai không?**

A. Feature scales and units | Thang đo và đơn vị các đặc trưng

B. Only when the matrix is an appropriate covariance matrix | Chỉ khi ma trận là covariance phù hợp

C. Rows are samples and columns are features | Hàng là mẫu và cột là đặc trưng

D. One principal-component feature per sample | Một đặc trưng thành phần chính cho mỗi mẫu

**Đáp án: B**

**Giải thích:** Diễn giải phương sai cần ma trận hiệp phương sai.

**Q19. What does `PCA(n_components=1)` preserve? | `PCA(n_components=1)` giữ lại gì?**

A. Feature scales and units | Thang đo và đơn vị các đặc trưng

B. Rows are samples and columns are features | Hàng là mẫu và cột là đặc trưng

C. One principal-component feature per sample | Một đặc trưng thành phần chính cho mỗi mẫu

D. Only when the matrix is an appropriate covariance matrix | Chỉ khi ma trận là covariance phù hợp

**Đáp án: C**

**Giải thích:** Dữ liệu sau chiếu còn một cột, vẫn giữ số hàng.

**Q20. What should be considered before comparing PCA variances across features? | Cần lưu ý gì trước khi so phương sai PCA giữa đặc trưng?**

A. Feature scales and units | Thang đo và đơn vị các đặc trưng

B. One principal-component feature per sample | Một đặc trưng thành phần chính cho mỗi mẫu

C. Rows are samples and columns are features | Hàng là mẫu và cột là đặc trưng

D. Only when the matrix is an appropriate covariance matrix | Chỉ khi ma trận là covariance phù hợp

**Đáp án: A**

**Giải thích:** Đặc trưng có thang lớn có thể lấn át PCA nếu chưa chuẩn hóa.

## PY-28 — PY-28 — Hàm tuyến tính, bậc hai, đa thức và hàm mũ

**Câu hỏi chỉ về nội dung lý thuyết, cú pháp và cách phân biệt hàm.**

**Q1. Which form is a first-degree affine function? | Dạng nào là hàm affine bậc nhất?**

A. `y=a*x**2+b*x+c` with a≠0 | `y=a*x**2+b*x+c` với a≠0

B. A variable appears in the exponent | Biến xuất hiện ở số mũ

C. `y=m*x+b` | `y=m*x+b`

D. Highest nonzero power of x | Lũy thừa cao nhất có hệ số khác 0

**Đáp án: C**

**Giải thích:** Dạng affine gồm hệ số góc và hệ số chặn.

**Q2. Which form contains a nonzero quadratic term? | Dạng nào có hạng bậc hai khác 0?**

A. `y=m*x+b` | `y=m*x+b`

B. A variable appears in the exponent | Biến xuất hiện ở số mũ

C. Highest nonzero power of x | Lũy thừa cao nhất có hệ số khác 0

D. `y=a*x**2+b*x+c` with a≠0 | `y=a*x**2+b*x+c` với a≠0

**Đáp án: D**

**Giải thích:** Hàm bậc hai có hạng x bình phương.

**Q3. What does polynomial degree measure? | Bậc đa thức cho biết gì?**

A. A variable appears in the exponent | Biến xuất hiện ở số mũ

B. `y=m*x+b` | `y=m*x+b`

C. `y=a*x**2+b*x+c` with a≠0 | `y=a*x**2+b*x+c` với a≠0

D. Highest nonzero power of x | Lũy thừa cao nhất có hệ số khác 0

**Đáp án: D**

**Giải thích:** Bậc là số mũ cao nhất có hệ số khác 0.

**Q4. What characterizes an exponential function? | Đặc điểm của hàm mũ là gì?**

A. `y=a*x**2+b*x+c` with a≠0 | `y=a*x**2+b*x+c` với a≠0

B. Highest nonzero power of x | Lũy thừa cao nhất có hệ số khác 0

C. `y=m*x+b` | `y=m*x+b`

D. A variable appears in the exponent | Biến xuất hiện ở số mũ

**Đáp án: D**

**Giải thích:** Hàm mũ có số mũ thay đổi.

**Q5. Given f(x) = 2x + 3, what is f(4)? | Cho f(x) = 2x + 3, f(4) bằng bao nhiêu?**

A. 14 | 14

B. 8 | 8

C. 7 | 7

D. 11 | 11

**Đáp án: D**

**Giải thích:** Thay x = 4: f(4) = 2 × 4 + 3 = 11.

**Q6. At which x is f(x) = (x − 3)² equal to zero? | Hàm f(x) = (x − 3)² bằng 0 tại giá trị x nào?**

A. 6 | 6

B. 3 | 3

C. −3 | −3

D. 0 | 0

**Đáp án: B**

**Giải thích:** Bình phương bằng 0 khi biểu thức bên trong bằng 0: x − 3 = 0, nên x = 3.

**Q7. Which best describes exponential growth compared with linear growth? | Đâu là điểm khác nhau điển hình giữa tăng trưởng hàm mũ và tuyến tính?**

A. Exponential growth always stops | Tăng trưởng mũ luôn dừng

B. Both add the same amount at each step | Cả hai cùng cộng số lượng cố định mỗi bước

C. Linear growth always decreases | Tuyến tính luôn giảm

D. Exponential growth multiplies by a fixed factor in equal steps | Tăng trưởng mũ nhân theo một tỷ lệ cố định qua các bước đều

**Đáp án: D**

**Giải thích:** Hàm tuyến tính có mức tăng tuyệt đối cố định; hàm mũ tăng theo tỷ lệ nhân cố định khi đầu vào tăng đều.

**Q8. What is f(2) if f(x) = (x − 2)²? | Nếu f(x) = (x − 2)², f(2) bằng bao nhiêu?**

A. 2 | 2

B. 0 | 0

C. 8 | 8

D. 4 | 4

**Đáp án: B**

**Giải thích:** Thay x = 2: (2 − 2)² = 0.

**Q9. Which NumPy function evaluates a polynomial? | Hàm NumPy nào tính đa thức?**

A. Highest degree first | Bậc cao nhất trước

B. `np.linspace(start,stop,num)` | `np.linspace(start,stop,num)`

C. `np.exp(x)` | `np.exp(x)`

D. `np.polyval(coefficients,x)` | `np.polyval(coefficients,x)`

**Đáp án: D**

**Giải thích:** polyval tính đa thức theo các hệ số có thứ tự.

**Q10. In what order does `np.polyval` take coefficients? | `np.polyval` nhận hệ số theo thứ tự gì?**

A. `np.linspace(start,stop,num)` | `np.linspace(start,stop,num)`

B. `np.polyval(coefficients,x)` | `np.polyval(coefficients,x)`

C. `np.exp(x)` | `np.exp(x)`

D. Highest degree first | Bậc cao nhất trước

**Đáp án: D**

**Giải thích:** Hệ số bậc cao nhất đứng đầu.

**Q11. Which function computes e raised to x? | Hàm nào tính e mũ x?**

A. Highest degree first | Bậc cao nhất trước

B. `np.linspace(start,stop,num)` | `np.linspace(start,stop,num)`

C. `np.polyval(coefficients,x)` | `np.polyval(coefficients,x)`

D. `np.exp(x)` | `np.exp(x)`

**Đáp án: D**

**Giải thích:** exp tính hàm mũ cơ số e.

**Q12. Which function makes evenly spaced samples? | Hàm nào tạo các điểm cách đều?**

A. Highest degree first | Bậc cao nhất trước

B. `np.polyval(coefficients,x)` | `np.polyval(coefficients,x)`

C. `np.exp(x)` | `np.exp(x)`

D. `np.linspace(start,stop,num)` | `np.linspace(start,stop,num)`

**Đáp án: D**

**Giải thích:** linspace tạo số lượng điểm cách đều yêu cầu.

**Q13. What is the value of y=2x+5 at x=0? | Giá trị y=2x+5 khi x=0 là gì?**

A. 16 | 16

B. 4 | 4

C. 6 | 6

D. 5 | 5

**Đáp án: D**

**Giải thích:** Khi x=0, ta có 2×0+5=5.

**Q14. What is the value of x²+2 at x=2? | Giá trị x²+2 khi x=2 là gì?**

A. 6 | 6

B. 4 | 4

C. 16 | 16

D. 5 | 5

**Đáp án: A**

**Giải thích:** Bình phương 2 rồi cộng 2 bằng 6.

**Q15. What is 2 raised to the fourth power? | 2 mũ 4 bằng gì?**

A. 6 | 6

B. 5 | 5

C. 4 | 4

D. 16 | 16

**Đáp án: D**

**Giải thích:** 2 nhân bốn lần bằng 16.

**Q16. How many intervals are between five evenly spaced points? | Năm điểm cách đều tạo bao nhiêu khoảng?**

A. 5 | 5

B. 16 | 16

C. 6 | 6

D. 4 | 4

**Đáp án: D**

**Giải thích:** n điểm tạo n−1 khoảng.

**Q17. What does `np.exp(0)` equal? | `np.exp(0)` bằng bao nhiêu?**

A. A constant additive increment | Mỗi bước cộng cùng một mức

B. Accuracy on unseen real-world data | Độ chính xác trên dữ liệu thực chưa gặp

C. 1 | 1

D. Its slope changes with x | Độ dốc thay đổi theo x

**Đáp án: C**

**Giải thích:** Cơ số khác 0 mũ 0 bằng 1.

**Q18. How does a quadratic differ from a first-degree affine function? | Hàm bậc hai khác hàm affine bậc nhất ở đâu?**

A. A constant additive increment | Mỗi bước cộng cùng một mức

B. 1 | 1

C. Accuracy on unseen real-world data | Độ chính xác trên dữ liệu thực chưa gặp

D. Its slope changes with x | Độ dốc thay đổi theo x

**Đáp án: D**

**Giải thích:** Mức tăng của hàm bậc hai thay đổi theo x.

**Q19. Which constraint gives a constant-per-step growth model? | Mô hình tăng đều mỗi bước cần điều kiện gì?**

A. A constant additive increment | Mỗi bước cộng cùng một mức

B. 1 | 1

C. Accuracy on unseen real-world data | Độ chính xác trên dữ liệu thực chưa gặp

D. Its slope changes with x | Độ dốc thay đổi theo x

**Đáp án: A**

**Giải thích:** Cộng hằng số tạo mức tăng cố định.

**Q20. What does a fitted function alone not prove? | Một hàm được khớp dữ liệu chưa chứng minh được gì?**

A. A constant additive increment | Mỗi bước cộng cùng một mức

B. 1 | 1

C. Its slope changes with x | Độ dốc thay đổi theo x

D. Accuracy on unseen real-world data | Độ chính xác trên dữ liệu thực chưa gặp

**Đáp án: D**

**Giải thích:** Khả năng dự đoán cần được kiểm chứng ngoài các ví dụ khớp.

## PY-29 — PY-29 — Activation: ReLU, sigmoid, tanh, softmax

**Chỉ hỏi kiến thức, phân biệt hàm và cách đọc đầu ra; không hỏi tình huống đánh số.**

**Q1. What is a ReLU activation? | Hàm kích hoạt ReLU là gì?**

A. `1/(1+exp(-x))` | `1/(1+exp(-x))`

B. A smooth activation mapping into (−1,1) | Hàm trơn đưa giá trị vào (−1,1)

C. Normalization of several class logits to sum one | Chuẩn hóa nhiều logit lớp có tổng bằng một

D. `max(0,x)` | `max(0,x)`

**Đáp án: D**

**Giải thích:** ReLU chặn giá trị âm về không.

**Q2. What is sigmoid? | Sigmoid là gì?**

A. `max(0,x)` | `max(0,x)`

B. Normalization of several class logits to sum one | Chuẩn hóa nhiều logit lớp có tổng bằng một

C. A smooth activation mapping into (−1,1) | Hàm trơn đưa giá trị vào (−1,1)

D. `1/(1+exp(-x))` | `1/(1+exp(-x))`

**Đáp án: D**

**Giải thích:** Sigmoid là phép biến đổi logistic hình chữ S.

**Q3. What is tanh? | Tanh là gì?**

A. `max(0,x)` | `max(0,x)`

B. `1/(1+exp(-x))` | `1/(1+exp(-x))`

C. Normalization of several class logits to sum one | Chuẩn hóa nhiều logit lớp có tổng bằng một

D. A smooth activation mapping into (−1,1) | Hàm trơn đưa giá trị vào (−1,1)

**Đáp án: D**

**Giải thích:** Tanh cân quanh 0 và giới hạn giữa −1 và 1.

**Q4. What is softmax? | Softmax là gì?**

A. `1/(1+exp(-x))` | `1/(1+exp(-x))`

B. `max(0,x)` | `max(0,x)`

C. A smooth activation mapping into (−1,1) | Hàm trơn đưa giá trị vào (−1,1)

D. Normalization of several class logits to sum one | Chuẩn hóa nhiều logit lớp có tổng bằng một

**Đáp án: D**

**Giải thích:** Softmax ràng buộc điểm lớp thành một phân phối chuẩn hóa.

**Q5. What is ReLU(−3) if ReLU(x) = max(0, x)? | ReLU(−3) bằng bao nhiêu nếu ReLU(x) = max(0, x)?**

A. 3 | 3

B. −3 | −3

C. 0 | 0

D. 1 | 1

**Đáp án: C**

**Giải thích:** ReLU chọn giá trị lớn hơn giữa 0 và x. Với −3, giá trị lớn hơn là 0.

**Q6. What is the sigmoid output at input x = 0? | Hàm sigmoid nhận x = 0 thì kết quả là bao nhiêu?**

A. 0 | 0

B. 1 | 1

C. −1 | −1

D. 0.5 | 0.5

**Đáp án: D**

**Giải thích:** Sigmoid(0) = 1/(1 + e⁰) = 1/(1 + 1) = 0.5.

**Q7. A softmax layer outputs probabilities for three classes. What must their sum be (up to rounding)? | Softmax trả về xác suất cho ba lớp. Tổng các xác suất phải gần bằng bao nhiêu?**

A. 0.5 | 0.5

B. 3 | 3

C. 1 | 1

D. 0 | 0

**Đáp án: C**

**Giải thích:** Softmax chuẩn hóa điểm số của tất cả các lớp để các xác suất không âm và cộng lại bằng 1.

**Q8. Which statement about sigmoid is correct for any finite input? | Phát biểu nào đúng về đầu ra sigmoid với mọi đầu vào hữu hạn?**

A. The output always exceeds 1 | Kết quả luôn lớn hơn 1

B. The output lies strictly between 0 and 1 | Kết quả nằm giữa 0 và 1, không chạm hai đầu

C. The output can be negative | Kết quả có thể âm

D. The output is always exactly 0 or 1 | Kết quả luôn chính xác 0 hoặc 1

**Đáp án: B**

**Giải thích:** Với đầu vào hữu hạn, mẫu số 1 + e^(−x) lớn hơn 1, nên đầu ra dương nhưng nhỏ hơn 1.

**Q9. Which NumPy function applies ReLU? | Hàm NumPy nào thực hiện ReLU?**

A. `np.maximum(0,x)` | `np.maximum(0,x)`

B. The largest logit | Logit lớn nhất

C. Tanh | Tanh

D. `np.tanh(x)` | `np.tanh(x)`

**Đáp án: A**

**Giải thích:** maximum chặn từng phần tử.

**Q10. Which NumPy function directly computes tanh? | Hàm NumPy nào tính tanh trực tiếp?**

A. `np.tanh(x)` | `np.tanh(x)`

B. Tanh | Tanh

C. The largest logit | Logit lớn nhất

D. `np.maximum(0,x)` | `np.maximum(0,x)`

**Đáp án: A**

**Giải thích:** NumPy có hàm tanh trực tiếp.

**Q11. Which quantity should be subtracted from logits before stable softmax exponentiation? | Nên trừ gì khỏi logit trước khi tính exp softmax ổn định?**

A. `np.tanh(x)` | `np.tanh(x)`

B. `np.maximum(0,x)` | `np.maximum(0,x)`

C. The largest logit | Logit lớn nhất

D. Tanh | Tanh

**Đáp án: C**

**Giải thích:** Trừ cực đại giữ các số exp không vượt một.

**Q12. Which activation outputs exactly 0 at input 0? | Hàm nào trả đúng 0 với đầu vào 0?**

A. The largest logit | Logit lớn nhất

B. `np.tanh(x)` | `np.tanh(x)`

C. `np.maximum(0,x)` | `np.maximum(0,x)`

D. Tanh | Tanh

**Đáp án: D**

**Giải thích:** Tanh(0)=0, còn sigmoid(0)=0.5.

**Q13. What is sigmoid(0)? | sigmoid(0) bằng gì?**

A. A negative output | Giá trị đầu ra âm

B. It reduces overflow risk without changing the result | Giảm nguy cơ tràn số mà không đổi kết quả

C. 0.5 | 0.5

D. 0 | 0

**Đáp án: C**

**Giải thích:** Sigmoid tại zero bằng một nửa.

**Q14. What is ReLU(−2)? | ReLU(−2) bằng gì?**

A. A negative output | Giá trị đầu ra âm

B. It reduces overflow risk without changing the result | Giảm nguy cơ tràn số mà không đổi kết quả

C. 0.5 | 0.5

D. 0 | 0

**Đáp án: D**

**Giải thích:** ReLU chặn đầu vào âm.

**Q15. What does tanh produce for negative input? | Tanh tạo đầu ra thế nào khi đầu vào âm?**

A. A negative output | Giá trị đầu ra âm

B. 0.5 | 0.5

C. 0 | 0

D. It reduces overflow risk without changing the result | Giảm nguy cơ tràn số mà không đổi kết quả

**Đáp án: A**

**Giải thích:** Tanh giữ dấu của đầu vào hữu hạn khác 0.

**Q16. Why does subtracting max(logits) help softmax? | Vì sao trừ cực đại logit giúp softmax?**

A. 0.5 | 0.5

B. It reduces overflow risk without changing the result | Giảm nguy cơ tràn số mà không đổi kết quả

C. 0 | 0

D. A negative output | Giá trị đầu ra âm

**Đáp án: B**

**Giải thích:** Dịch đều các logit không đổi softmax nhưng giảm tràn số.

**Q17. Which output structure suits mutually exclusive multi-class prediction? | Dạng đầu ra nào phù hợp phân loại nhiều lớp loại trừ nhau?**

A. Their inputs remain in the nonpositive flat region | Đầu vào luôn ở vùng phẳng không dương

B. No, calibration needs checking | Không, cần đánh giá độ hiệu chuẩn

C. Softmax couples scores so they sum to one | Softmax ràng buộc điểm các lớp có tổng một

D. A softmax distribution over classes | Phân phối softmax trên các lớp

**Đáp án: D**

**Giải thích:** Softmax thường dùng cho đầu ra các lớp loại trừ nhau.

**Q18. Why might ReLU neurons stop updating? | Vì sao một số nơ-ron ReLU có thể ngừng cập nhật?**

A. A softmax distribution over classes | Phân phối softmax trên các lớp

B. No, calibration needs checking | Không, cần đánh giá độ hiệu chuẩn

C. Softmax couples scores so they sum to one | Softmax ràng buộc điểm các lớp có tổng một

D. Their inputs remain in the nonpositive flat region | Đầu vào luôn ở vùng phẳng không dương

**Đáp án: D**

**Giải thích:** Độ dốc ReLU bằng không ở đầu vào âm.

**Q19. Do sigmoid outputs automatically prove calibrated probabilities? | Đầu ra sigmoid có mặc nhiên là xác suất đã hiệu chuẩn không?**

A. Softmax couples scores so they sum to one | Softmax ràng buộc điểm các lớp có tổng một

B. No, calibration needs checking | Không, cần đánh giá độ hiệu chuẩn

C. Their inputs remain in the nonpositive flat region | Đầu vào luôn ở vùng phẳng không dương

D. A softmax distribution over classes | Phân phối softmax trên các lớp

**Đáp án: B**

**Giải thích:** Điểm số cần kiểm tra với kết quả thực tế.

**Q20. Which difference distinguishes softmax from independent sigmoid outputs? | Điểm nào phân biệt softmax với sigmoid độc lập?**

A. A softmax distribution over classes | Phân phối softmax trên các lớp

B. Their inputs remain in the nonpositive flat region | Đầu vào luôn ở vùng phẳng không dương

C. No, calibration needs checking | Không, cần đánh giá độ hiệu chuẩn

D. Softmax couples scores so they sum to one | Softmax ràng buộc điểm các lớp có tổng một

**Đáp án: D**

**Giải thích:** Các sigmoid độc lập không bắt buộc có tổng bằng một.

## PY-30 — PY-30 — Loss: MSE, MAE, Huber, cross-entropy và KL

**Chỉ hỏi kiến thức lý thuyết, so sánh loss và đọc công thức, không hỏi dữ liệu tình huống.**

**Q1. What is MSE? | MSE là gì?**

A. Mean absolute prediction error | Trung bình trị tuyệt đối sai số

B. Mean squared prediction error | Trung bình sai số dự báo bình phương

C. Compare two probability distributions in a directed way | So hai phân phối xác suất có phân biệt chiều

D. Quadratic for small errors and linear for large | Bình phương lỗi nhỏ, tuyến tính lỗi lớn

**Đáp án: B**

**Giải thích:** MSE lấy trung bình bình phương sai lệch.

**Q2. What is MAE? | MAE là gì?**

A. Mean squared prediction error | Trung bình sai số dự báo bình phương

B. Quadratic for small errors and linear for large | Bình phương lỗi nhỏ, tuyến tính lỗi lớn

C. Compare two probability distributions in a directed way | So hai phân phối xác suất có phân biệt chiều

D. Mean absolute prediction error | Trung bình trị tuyệt đối sai số

**Đáp án: D**

**Giải thích:** MAE lấy trung bình độ lệch tuyệt đối.

**Q3. What characterizes Huber loss? | Đặc trưng của Huber loss là gì?**

A. Mean absolute prediction error | Trung bình trị tuyệt đối sai số

B. Mean squared prediction error | Trung bình sai số dự báo bình phương

C. Compare two probability distributions in a directed way | So hai phân phối xác suất có phân biệt chiều

D. Quadratic for small errors and linear for large | Bình phương lỗi nhỏ, tuyến tính lỗi lớn

**Đáp án: D**

**Giải thích:** Huber đổi tốc độ tăng mức phạt sau một ngưỡng.

**Q4. What is KL divergence used for? | KL divergence dùng để làm gì?**

A. Mean absolute prediction error | Trung bình trị tuyệt đối sai số

B. Compare two probability distributions in a directed way | So hai phân phối xác suất có phân biệt chiều

C. Mean squared prediction error | Trung bình sai số dự báo bình phương

D. Quadratic for small errors and linear for large | Bình phương lỗi nhỏ, tuyến tính lỗi lớn

**Đáp án: B**

**Giải thích:** KL dùng tỷ số logarit theo một chiều giữa các phân phối.

**Q5. Actual values are [2, 4] and predictions are [3, 2]. What is MSE? | Giá trị thật [2, 4], dự đoán [3, 2]. MSE bằng bao nhiêu?**

A. 1.5 | 1.5

B. 3 | 3

C. 5 | 5

D. 2.5 | 2.5

**Đáp án: D**

**Giải thích:** Sai số là 1 và −2; bình phương là 1 và 4. MSE = (1 + 4)/2 = 2.5.

**Q6. Actual values are [2, 4] and predictions are [3, 2]. What is MAE? | Giá trị thật [2, 4], dự đoán [3, 2]. MAE bằng bao nhiêu?**

A. 0.5 | 0.5

B. 2.5 | 2.5

C. 3 | 3

D. 1.5 | 1.5

**Đáp án: D**

**Giải thích:** Lấy trị tuyệt đối các sai số: |3 − 2| = 1 và |2 − 4| = 2; MAE = (1 + 2)/2 = 1.5.

**Q7. For a correct class, which predicted probability gives the smaller cross-entropy loss? | Với lớp đúng, xác suất dự đoán nào tạo ra cross-entropy nhỏ hơn?**

A. 0.2 | 0.2

B. 0.1 | 0.1

C. 0.9 | 0.9

D. 0.5 | 0.5

**Đáp án: C**

**Giải thích:** Loss của lớp đúng là −log(p). Khi p càng gần 1, loss càng nhỏ; 0.9 là lớn nhất trong bốn giá trị.

**Q8. Which loss penalizes a very large error more strongly than MAE? | Hàm mất mát nào phạt sai số cực lớn mạnh hơn MAE?**

A. Mean squared error | MSE

B. Median absolute deviation | Độ lệch tuyệt đối trung vị

C. Mean absolute error | MAE

D. Zero-one loss | Loss đúng/sai 0–1

**Đáp án: A**

**Giải thích:** MSE bình phương sai số, nên lỗi lớn tăng nhanh hơn so với MAE chỉ lấy trị tuyệt đối.

**Q9. What does `−log(p_true)` represent for one correct class? | `−log(p_true)` biểu thị gì cho một nhãn đúng?**

A. Cross-entropy loss for that sample | Cross-entropy của mẫu đó

B. The distributions are identical | Hai phân phối giống nhau

C. Nonnegative | Không âm

D. No, KL is asymmetric | Không, KL bất đối xứng

**Đáp án: A**

**Giải thích:** Với one-hot, chỉ còn hạng log của lớp đúng.

**Q10. What is the sign of KL divergence for valid distributions? | KL divergence có dấu gì với phân phối hợp lệ?**

A. The distributions are identical | Hai phân phối giống nhau

B. Cross-entropy loss for that sample | Cross-entropy của mẫu đó

C. Nonnegative | Không âm

D. No, KL is asymmetric | Không, KL bất đối xứng

**Đáp án: C**

**Giải thích:** KL không âm theo bất đẳng thức Gibbs.

**Q11. Does swapping P and Q generally preserve KL? | Đổi chỗ P và Q có giữ nguyên KL không?**

A. Nonnegative | Không âm

B. The distributions are identical | Hai phân phối giống nhau

C. No, KL is asymmetric | Không, KL bất đối xứng

D. Cross-entropy loss for that sample | Cross-entropy của mẫu đó

**Đáp án: C**

**Giải thích:** D(P‖Q) và D(Q‖P) có thể khác.

**Q12. What does a zero KL divergence mean for valid finite distributions? | KL bằng 0 nghĩa là gì với các phân phối hữu hạn hợp lệ?**

A. The distributions are identical | Hai phân phối giống nhau

B. Cross-entropy loss for that sample | Cross-entropy của mẫu đó

C. No, KL is asymmetric | Không, KL bất đối xứng

D. Nonnegative | Không âm

**Đáp án: A**

**Giải thích:** KL bằng 0 khi các phân phối trùng nhau trong điều kiện phù hợp.

**Q13. What is the unit of MSE when predictions are in meters? | Dự báo theo mét thì MSE có đơn vị gì?**

A. Meters | Mét

B. MSE | MSE

C. Huber loss | Huber loss

D. Square meters | Mét bình phương

**Đáp án: D**

**Giải thích:** Bình phương sai lệch mét cho đơn vị m².

**Q14. What is the unit of MAE when predictions are in meters? | Dự báo theo mét thì MAE có đơn vị gì?**

A. MSE | MSE

B. Huber loss | Huber loss

C. Square meters | Mét bình phương

D. Meters | Mét

**Đáp án: D**

**Giải thích:** Sai lệch tuyệt đối giữ đơn vị gốc.

**Q15. Which loss increases quadratically with error magnitude? | Loss nào tăng theo bình phương độ lớn lỗi?**

A. Meters | Mét

B. Huber loss | Huber loss

C. MSE | MSE

D. Square meters | Mét bình phương

**Đáp án: C**

**Giải thích:** MSE bình phương độ lớn lỗi.

**Q16. Which regression loss has a threshold between quadratic and linear penalties? | Loss hồi quy nào có ngưỡng chuyển bình phương sang tuyến tính?**

A. Huber loss | Huber loss

B. MSE | MSE

C. Meters | Mét

D. Square meters | Mét bình phương

**Đáp án: A**

**Giải thích:** Huber chuyển miền tại delta.

**Q17. Why clip predicted probabilities before a naive log implementation? | Vì sao clip xác suất trước khi lấy log bằng công thức đơn giản?**

A. To avoid log(0) and numerical infinities | Để tránh log(0) và vô cực số học

B. No, evaluate on held-out data | Không, cần đánh giá trên dữ liệu độc lập

C. Predicted probability assigned to the true class | Xác suất dự báo dành cho lớp đúng

D. MAE | MAE

**Đáp án: A**

**Giải thích:** Xác suất 0 gây kỳ dị log trong công thức số học đơn giản.

**Q18. Which loss is easier to interpret in the original output units? | Loss nào dễ đọc theo đơn vị đầu ra ban đầu?**

A. Predicted probability assigned to the true class | Xác suất dự báo dành cho lớp đúng

B. No, evaluate on held-out data | Không, cần đánh giá trên dữ liệu độc lập

C. To avoid log(0) and numerical infinities | Để tránh log(0) và vô cực số học

D. MAE | MAE

**Đáp án: D**

**Giải thích:** MAE báo sai số trung bình cùng đơn vị đo.

**Q19. Does a lower training loss guarantee better unseen-data performance? | Training loss thấp có bảo đảm dự đoán tốt trên dữ liệu mới?**

A. To avoid log(0) and numerical infinities | Để tránh log(0) và vô cực số học

B. MAE | MAE

C. Predicted probability assigned to the true class | Xác suất dự báo dành cho lớp đúng

D. No, evaluate on held-out data | Không, cần đánh giá trên dữ liệu độc lập

**Đáp án: D**

**Giải thích:** Khả năng tổng quát cần kiểm chứng bằng dữ liệu độc lập.

**Q20. For one-hot labels, what information matters in cross-entropy? | Với nhãn one-hot, điều gì quyết định cross-entropy?**

A. To avoid log(0) and numerical infinities | Để tránh log(0) và vô cực số học

B. Predicted probability assigned to the true class | Xác suất dự báo dành cho lớp đúng

C. MAE | MAE

D. No, evaluate on held-out data | Không, cần đánh giá trên dữ liệu độc lập

**Đáp án: B**

**Giải thích:** Âm log-likelihood dùng xác suất lớp đúng.

## PY-31 — PY-31 — Giới hạn, tính liên tục và đạo hàm



**Q1. What does a limit describe? | Giới hạn mô tả gì?**

A. The two-sided limit exists and equals f(a) | Giới hạn hai phía tồn tại và bằng f(a)

B. Instantaneous rate of change | Tốc độ thay đổi tức thời

C. The derivative evaluated at a | Giá trị đạo hàm tại a

D. What f(x) approaches as x approaches a point | Giá trị f(x) tiến đến khi x tiến gần một điểm

**Đáp án: D**

**Giải thích:** Giới hạn xét đầu vào lân cận điểm.

**Q2. What does continuity at x=a require? | Liên tục tại x=a cần gì?**

A. Instantaneous rate of change | Tốc độ thay đổi tức thời

B. The two-sided limit exists and equals f(a) | Giới hạn hai phía tồn tại và bằng f(a)

C. The derivative evaluated at a | Giá trị đạo hàm tại a

D. What f(x) approaches as x approaches a point | Giá trị f(x) tiến đến khi x tiến gần một điểm

**Đáp án: B**

**Giải thích:** Liên tục đòi hỏi giới hạn bằng giá trị hàm.

**Q3. What does a derivative describe? | Đạo hàm mô tả gì?**

A. What f(x) approaches as x approaches a point | Giá trị f(x) tiến đến khi x tiến gần một điểm

B. Instantaneous rate of change | Tốc độ thay đổi tức thời

C. The two-sided limit exists and equals f(a) | Giới hạn hai phía tồn tại và bằng f(a)

D. The derivative evaluated at a | Giá trị đạo hàm tại a

**Đáp án: B**

**Giải thích:** Đạo hàm đo độ thay đổi tại điểm.

**Q4. What is tangent slope at x=a? | Độ dốc tiếp tuyến tại x=a là gì?**

A. Instantaneous rate of change | Tốc độ thay đổi tức thời

B. The derivative evaluated at a | Giá trị đạo hàm tại a

C. The two-sided limit exists and equals f(a) | Giới hạn hai phía tồn tại và bằng f(a)

D. What f(x) approaches as x approaches a point | Giá trị f(x) tiến đến khi x tiến gần một điểm

**Đáp án: B**

**Giải thích:** Độ dốc tiếp tuyến là f'(a).

**Q5. What is the derivative of f(x) = 4x² − 3x + 1? | Đạo hàm của f(x) = 4x² − 3x + 1 là gì?**

A. 4x − 3 | 4x − 3

B. 8x − 3 | 8x − 3

C. 8x + 1 | 8x + 1

D. 4x² − 3 | 4x² − 3

**Đáp án: B**

**Giải thích:** Đạo hàm từng hạng: 4x² thành 8x, −3x thành −3, hằng số 1 thành 0.

**Q6. If f(x) = x², what is the slope of the tangent at x = 2? | Nếu f(x) = x², độ dốc tiếp tuyến tại x = 2 bằng bao nhiêu?**

A. 8 | 8

B. 4 | 4

C. 2 | 2

D. 0 | 0

**Đáp án: B**

**Giải thích:** Đạo hàm f'(x) = 2x, thay x = 2 được 4.

**Q7. What is the derivative of f(x) = 7? | Đạo hàm của hàm hằng f(x) = 7 bằng bao nhiêu?**

A. x | x

B. 7 | 7

C. 1 | 1

D. 0 | 0

**Đáp án: D**

**Giải thích:** Giá trị hàm hằng không thay đổi theo x nên tốc độ thay đổi, tức đạo hàm, bằng 0.

**Q8. If a function is differentiable at x = a, what must also hold there? | Nếu một hàm có đạo hàm tại x = a thì điều kiện nào chắc chắn đúng?**

A. It has a global minimum | Hàm có cực tiểu toàn cục

B. It is continuous at x = a | Hàm liên tục tại x = a

C. Its derivative is zero | Đạo hàm bằng 0

D. Its value is positive | Giá trị hàm dương

**Đáp án: B**

**Giải thích:** Có đạo hàm tại một điểm là điều kiện mạnh hơn liên tục tại điểm đó; chiều ngược lại không luôn đúng.

**Q9. What is the derivative of x²? | Đạo hàm của x² là gì?**

A. 6 | 6

B. 4 | 4

C. Zero | Bằng 0

D. `2*x` | `2*x`

**Đáp án: D**

**Giải thích:** Quy tắc đạo hàm lũy thừa cho 2x.

**Q10. What is the derivative of a constant? | Đạo hàm của một hằng số là gì?**

A. 6 | 6

B. Zero | Bằng 0

C. `2*x` | `2*x`

D. 4 | 4

**Đáp án: B**

**Giải thích:** Hằng số không đổi theo biến.

**Q11. What is the slope of x² at x=3? | Độ dốc của x² tại x=3 là gì?**

A. 6 | 6

B. `2*x` | `2*x`

C. Zero | Bằng 0

D. 4 | 4

**Đáp án: A**

**Giải thích:** 2 nhân 3 bằng sáu.

**Q12. What is the limit of (x²−4)/(x−2) at x=2? | Giới hạn của (x²−4)/(x−2) khi x→2 là gì?**

A. 4 | 4

B. `2*x` | `2*x`

C. Zero | Bằng 0

D. 6 | 6

**Đáp án: A**

**Giải thích:** Rút gọn gần điểm còn x+2.

**Q13. What may happen if the left and right limits differ? | Nếu giới hạn trái và phải khác nhau thì sao?**

A. Distance per unit time | Khoảng cách trên mỗi đơn vị thời gian

B. The two-sided limit does not exist | Giới hạn hai phía không tồn tại

C. Sampling spacing and numerical scheme | Khoảng cách mẫu và cách lấy sai phân

D. Yes, if nearby values approach one number | Có, nếu giá trị lân cận tiến đến cùng một số

**Đáp án: B**

**Giải thích:** Giới hạn một phía khác nhau khiến giới hạn hai phía không có.

**Q14. What does a derivative unit become for distance over time? | Đạo hàm quãng đường theo thời gian có đơn vị gì?**

A. Sampling spacing and numerical scheme | Khoảng cách mẫu và cách lấy sai phân

B. The two-sided limit does not exist | Giới hạn hai phía không tồn tại

C. Yes, if nearby values approach one number | Có, nếu giá trị lân cận tiến đến cùng một số

D. Distance per unit time | Khoảng cách trên mỗi đơn vị thời gian

**Đáp án: D**

**Giải thích:** Quãng đường chia thời gian cho đơn vị vận tốc.

**Q15. What determines finite-difference accuracy? | Độ chính xác sai phân hữu hạn phụ thuộc gì?**

A. Sampling spacing and numerical scheme | Khoảng cách mẫu và cách lấy sai phân

B. The two-sided limit does not exist | Giới hạn hai phía không tồn tại

C. Distance per unit time | Khoảng cách trên mỗi đơn vị thời gian

D. Yes, if nearby values approach one number | Có, nếu giá trị lân cận tiến đến cùng một số

**Đáp án: A**

**Giải thích:** Khoảng lấy mẫu ảnh hưởng độ dốc ước lượng.

**Q16. Can a function have a finite limit at an undefined point? | Hàm chưa xác định tại một điểm có thể có giới hạn hữu hạn không?**

A. The two-sided limit does not exist | Giới hạn hai phía không tồn tại

B. Distance per unit time | Khoảng cách trên mỗi đơn vị thời gian

C. Yes, if nearby values approach one number | Có, nếu giá trị lân cận tiến đến cùng một số

D. Sampling spacing and numerical scheme | Khoảng cách mẫu và cách lấy sai phân

**Đáp án: C**

**Giải thích:** Giới hạn có thể có dù hàm không xác định ngay điểm đó.

**Q17. How does a derivative differ from an average slope? | Đạo hàm khác độ dốc trung bình thế nào?**

A. 2 | 2

B. It often uses one-sided differences | Nó thường dùng sai phân một phía

C. `sympy.diff` | `sympy.diff`

D. It describes a local infinitesimal change | Nó mô tả độ thay đổi cục bộ rất nhỏ

**Đáp án: D**

**Giải thích:** Độ dốc tức thời là đại lượng giới hạn cục bộ.

**Q18. What is the derivative of 2x+3? | Đạo hàm của 2x+3 là gì?**

A. It describes a local infinitesimal change | Nó mô tả độ thay đổi cục bộ rất nhỏ

B. `sympy.diff` | `sympy.diff`

C. It often uses one-sided differences | Nó thường dùng sai phân một phía

D. 2 | 2

**Đáp án: D**

**Giải thích:** Hệ số của x cho đạo hàm bằng 2.

**Q19. Which tool calculates symbolic derivatives? | Công cụ nào tính đạo hàm ký hiệu?**

A. It describes a local infinitesimal change | Nó mô tả độ thay đổi cục bộ rất nhỏ

B. It often uses one-sided differences | Nó thường dùng sai phân một phía

C. 2 | 2

D. `sympy.diff` | `sympy.diff`

**Đáp án: D**

**Giải thích:** SymPy hỗ trợ đạo hàm ký hiệu bằng diff.

**Q20. Why is a numerical gradient at a boundary less accurate? | Vì sao gradient số ở biên có thể kém chính xác hơn?**

A. `sympy.diff` | `sympy.diff`

B. It describes a local infinitesimal change | Nó mô tả độ thay đổi cục bộ rất nhỏ

C. 2 | 2

D. It often uses one-sided differences | Nó thường dùng sai phân một phía

**Đáp án: D**

**Giải thích:** Ước lượng ở đầu dãy thường dùng dữ liệu một phía.

## PY-32 — PY-32 — Đạo hàm riêng, gradient descent và learning rate



**Q1. What is a partial derivative? | Đạo hàm riêng là gì?**

A. A vector of partial derivatives | Vector gồm các đạo hàm riêng

B. One pass through the training dataset | Một lượt đi qua tập dữ liệu train

C. A factor controlling an optimization update step | Hệ số điều khiển độ lớn bước cập nhật tối ưu

D. Change rate in one variable while others are held fixed | Tốc độ thay đổi theo một biến khi giữ các biến khác cố định

**Đáp án: D**

**Giải thích:** Chỉ thay một biến và giữ biến khác cố định.

**Q2. What is a gradient? | Gradient là gì?**

A. Change rate in one variable while others are held fixed | Tốc độ thay đổi theo một biến khi giữ các biến khác cố định

B. One pass through the training dataset | Một lượt đi qua tập dữ liệu train

C. A factor controlling an optimization update step | Hệ số điều khiển độ lớn bước cập nhật tối ưu

D. A vector of partial derivatives | Vector gồm các đạo hàm riêng

**Đáp án: D**

**Giải thích:** Các đạo hàm riêng hợp thành một vector.

**Q3. What is a learning rate? | Learning rate là gì?**

A. A factor controlling an optimization update step | Hệ số điều khiển độ lớn bước cập nhật tối ưu

B. Change rate in one variable while others are held fixed | Tốc độ thay đổi theo một biến khi giữ các biến khác cố định

C. A vector of partial derivatives | Vector gồm các đạo hàm riêng

D. One pass through the training dataset | Một lượt đi qua tập dữ liệu train

**Đáp án: A**

**Giải thích:** Nó nhân mức độ cập nhật.

**Q4. What is an epoch in training? | Epoch trong huấn luyện là gì?**

A. One pass through the training dataset | Một lượt đi qua tập dữ liệu train

B. Change rate in one variable while others are held fixed | Tốc độ thay đổi theo một biến khi giữ các biến khác cố định

C. A vector of partial derivatives | Vector gồm các đạo hàm riêng

D. A factor controlling an optimization update step | Hệ số điều khiển độ lớn bước cập nhật tối ưu

**Đáp án: A**

**Giải thích:** Một epoch xử lý hết dữ liệu train một lượt.

**Q5. Given L(w) = (w − 2)², what is the gradient at w = 5? | Cho L(w) = (w − 2)², gradient tại w = 5 bằng bao nhiêu?**

A. 4 | 4

B. 6 | 6

C. 2 | 2

D. 10 | 10

**Đáp án: B**

**Giải thích:** Đạo hàm dL/dw = 2(w − 2). Thay w = 5: 2 × (5 − 2) = 6.

**Q6. Gradient descent uses new_w = old_w − rate × gradient. If w = 4, rate = 0.25, gradient = 2, what is new_w? | Gradient Descent cập nhật w mới = w cũ − tốc độ học × gradient. Nếu w = 4, rate = 0.25, gradient = 2, w mới bằng bao nhiêu?**

A. 3.5 | 3.5

B. 2 | 2

C. 4.5 | 4.5

D. 3 | 3

**Đáp án: A**

**Giải thích:** w mới = 4 − 0.25 × 2 = 3.5. Lấy w cũ trừ một bước theo gradient.

**Q7. What may happen when learning rate is excessively large? | Điều gì có thể xảy ra khi tốc độ học quá lớn?**

A. Training data always doubles | Dữ liệu huấn luyện luôn tăng gấp đôi

B. Loss may oscillate or diverge | Loss có thể dao động hoặc phân kỳ

C. Every gradient becomes zero | Mọi gradient đều bằng 0

D. The global optimum is guaranteed | Luôn tìm được cực tiểu toàn cục

**Đáp án: B**

**Giải thích:** Bước nhảy quá lớn có thể vượt qua cực tiểu, khiến hàm mất mát dao động hoặc tăng thay vì giảm.

**Q8. A function has gradient zero at w = 0. Which conclusion is always justified? | Một hàm có gradient bằng 0 tại w = 0. Kết luận nào luôn đúng?**

A. The loss is zero | Loss bằng 0

B. This is a global minimum | Đây là cực tiểu toàn cục

C. The function is constant | Hàm là hằng số

D. It is a stationary point, not necessarily a minimum | Đây là điểm dừng, chưa chắc là cực tiểu

**Đáp án: D**

**Giải thích:** Gradient bằng 0 chỉ cho biết tốc độ thay đổi cục bộ bằng 0. Điểm đó vẫn có thể là cực đại hoặc điểm yên ngựa.

**Q9. What is ∂(x²+3xy)/∂x? | Đạo hàm riêng theo x của x²+3xy là gì?**

A. `2*x+3*y` | `2*x+3*y`

B. `[2*x,2*y]` | `[2*x,2*y]`

C. `2*w` | `2*w`

D. 2.4 | 2.4

**Đáp án: A**

**Giải thích:** Lấy đạo hàm x² và xy theo x.

**Q10. What is the gradient of x²+y²? | Gradient của x²+y² là gì?**

A. 2.4 | 2.4

B. `2*x+3*y` | `2*x+3*y`

C. `2*w` | `2*w`

D. `[2*x,2*y]` | `[2*x,2*y]`

**Đáp án: D**

**Giải thích:** Mỗi đạo hàm bằng hai lần tọa độ.

**Q11. For loss w², what is its derivative? | Đạo hàm loss w² là gì?**

A. `[2*x,2*y]` | `[2*x,2*y]`

B. 2.4 | 2.4

C. `2*w` | `2*w`

D. `2*x+3*y` | `2*x+3*y`

**Đáp án: C**

**Giải thích:** Dùng quy tắc lũy thừa cho w².

**Q12. If w=3, lr=0.1 and grad=6, what is next w? | Nếu w=3, lr=0.1 và gradient=6, w mới là gì?**

A. `[2*x,2*y]` | `[2*x,2*y]`

B. 2.4 | 2.4

C. `2*w` | `2*w`

D. `2*x+3*y` | `2*x+3*y`

**Đáp án: B**

**Giải thích:** 3−0.1×6=2.4.

**Q13. Why might a large learning rate fail? | Vì sao learning rate lớn dễ thất bại?**

A. No, minibatches can cause multiple updates | Không, nhiều minibatch có thể tạo nhiều lần cập nhật

B. Updates can overshoot or diverge | Bước cập nhật có thể vượt cực tiểu hoặc phân kỳ

C. It can make convergence slow | Nó có thể làm hội tụ chậm

D. Locally reduce the objective | Giảm hàm mục tiêu về mặt cục bộ

**Đáp án: B**

**Giải thích:** Bước lớn có thể vượt qua cực tiểu liên tục.

**Q14. Why might a very small learning rate be inefficient? | Vì sao learning rate quá nhỏ kém hiệu quả?**

A. Locally reduce the objective | Giảm hàm mục tiêu về mặt cục bộ

B. It can make convergence slow | Nó có thể làm hội tụ chậm

C. Updates can overshoot or diverge | Bước cập nhật có thể vượt cực tiểu hoặc phân kỳ

D. No, minibatches can cause multiple updates | Không, nhiều minibatch có thể tạo nhiều lần cập nhật

**Đáp án: B**

**Giải thích:** Bước quá nhỏ khiến tối ưu chậm.

**Q15. What does moving opposite the gradient aim to do? | Đi ngược gradient nhằm làm gì?**

A. Updates can overshoot or diverge | Bước cập nhật có thể vượt cực tiểu hoặc phân kỳ

B. No, minibatches can cause multiple updates | Không, nhiều minibatch có thể tạo nhiều lần cập nhật

C. It can make convergence slow | Nó có thể làm hội tụ chậm

D. Locally reduce the objective | Giảm hàm mục tiêu về mặt cục bộ

**Đáp án: D**

**Giải thích:** Gradient âm là hướng giảm với bước đủ nhỏ.

**Q16. Does one epoch always equal one update? | Một epoch luôn bằng một lần cập nhật không?**

A. Locally reduce the objective | Giảm hàm mục tiêu về mặt cục bộ

B. It can make convergence slow | Nó có thể làm hội tụ chậm

C. Updates can overshoot or diverge | Bước cập nhật có thể vượt cực tiểu hoặc phân kỳ

D. No, minibatches can cause multiple updates | Không, nhiều minibatch có thể tạo nhiều lần cập nhật

**Đáp án: D**

**Giải thích:** Một epoch có thể gồm nhiều batch.

**Q17. Why record loss history? | Vì sao lưu lịch sử loss?**

A. Steepest increase | Hướng tăng nhanh nhất

B. No, generalization needs validation | Không, cần kiểm chứng trên dữ liệu mới

C. Each error must use its correct sample | Mỗi sai số cần đúng cặp quan sát

D. To inspect optimization progress | Để xem tiến trình tối ưu

**Đáp án: D**

**Giải thích:** Lịch sử cho thấy xu hướng giảm hoặc bất ổn.

**Q18. Why pair features and targets in the same order? | Vì sao cần ghép x và y cùng thứ tự?**

A. No, generalization needs validation | Không, cần kiểm chứng trên dữ liệu mới

B. Each error must use its correct sample | Mỗi sai số cần đúng cặp quan sát

C. To inspect optimization progress | Để xem tiến trình tối ưu

D. Steepest increase | Hướng tăng nhanh nhất

**Đáp án: B**

**Giải thích:** Hàng ghép sai làm sai số vô nghĩa.

**Q19. Does falling training loss guarantee test accuracy? | Loss train giảm có đảm bảo độ chính xác test?**

A. No, generalization needs validation | Không, cần kiểm chứng trên dữ liệu mới

B. To inspect optimization progress | Để xem tiến trình tối ưu

C. Steepest increase | Hướng tăng nhanh nhất

D. Each error must use its correct sample | Mỗi sai số cần đúng cặp quan sát

**Đáp án: A**

**Giải thích:** Cần dữ liệu độc lập để đo tổng quát hóa.

**Q20. Which direction does a gradient point locally? | Gradient hướng theo phía nào về mặt cục bộ?**

A. No, generalization needs validation | Không, cần kiểm chứng trên dữ liệu mới

B. Steepest increase | Hướng tăng nhanh nhất

C. To inspect optimization progress | Để xem tiến trình tối ưu

D. Each error must use its correct sample | Mỗi sai số cần đúng cặp quan sát

**Đáp án: B**

**Giải thích:** Gradient hướng tăng cục bộ nhanh nhất.

## PY-33 — PY-33 — Jacobian, Hessian và điểm cực trị



**Q1. What does a Jacobian contain? | Jacobian chứa gì?**

A. A differentiable point where the gradient is zero | Điểm khả vi có gradient bằng 0

B. Classifying local behavior near stationary points | Phân loại hành vi cục bộ gần điểm dừng

C. First partial derivatives of vector outputs | Các đạo hàm riêng bậc một của đầu ra vector

D. Second partial derivatives of a scalar output | Các đạo hàm riêng bậc hai của đầu ra vô hướng

**Đáp án: C**

**Giải thích:** Mỗi hàng chứa đạo hàm bậc một của một đầu ra.

**Q2. What does a Hessian contain? | Hessian chứa gì?**

A. Classifying local behavior near stationary points | Phân loại hành vi cục bộ gần điểm dừng

B. First partial derivatives of vector outputs | Các đạo hàm riêng bậc một của đầu ra vector

C. Second partial derivatives of a scalar output | Các đạo hàm riêng bậc hai của đầu ra vô hướng

D. A differentiable point where the gradient is zero | Điểm khả vi có gradient bằng 0

**Đáp án: C**

**Giải thích:** Hessian lấy đạo hàm tiếp của gradient.

**Q3. What is a stationary point? | Điểm dừng là gì?**

A. Classifying local behavior near stationary points | Phân loại hành vi cục bộ gần điểm dừng

B. First partial derivatives of vector outputs | Các đạo hàm riêng bậc một của đầu ra vector

C. Second partial derivatives of a scalar output | Các đạo hàm riêng bậc hai của đầu ra vô hướng

D. A differentiable point where the gradient is zero | Điểm khả vi có gradient bằng 0

**Đáp án: D**

**Giải thích:** Điểm dừng có các đạo hàm riêng bậc một bằng 0.

**Q4. What is curvature information used for? | Thông tin độ cong dùng để làm gì?**

A. Second partial derivatives of a scalar output | Các đạo hàm riêng bậc hai của đầu ra vô hướng

B. A differentiable point where the gradient is zero | Điểm khả vi có gradient bằng 0

C. Classifying local behavior near stationary points | Phân loại hành vi cục bộ gần điểm dừng

D. First partial derivatives of vector outputs | Các đạo hàm riêng bậc một của đầu ra vector

**Đáp án: C**

**Giải thích:** Độ cong giúp phân loại điểm dừng.

**Q5. For f(x, y) = x² + y², what is its Hessian matrix? | Với f(x, y) = x² + y², ma trận Hessian bằng bao nhiêu?**

A. [[1, 0], [0, 1]] | [[1, 0], [0, 1]]

B. [[0, 0], [0, 0]] | [[0, 0], [0, 0]]

C. [[2, 0], [0, 2]] | [[2, 0], [0, 2]]

D. [[0, 2], [2, 0]] | [[0, 2], [2, 0]]

**Đáp án: C**

**Giải thích:** Đạo hàm bậc hai theo x và y đều bằng 2, hai đạo hàm chéo bằng 0.

**Q6. At which x is the derivative of f(x) = (x − 3)² zero? | Đạo hàm của f(x) = (x − 3)² bằng 0 tại x nào?**

A. x = 2 | x = 2

B. x = −3 | x = −3

C. x = 3 | x = 3

D. x = 0 | x = 0

**Đáp án: C**

**Giải thích:** f'(x) = 2(x − 3); đặt bằng 0 được x = 3.

**Q7. At a stationary point, a positive-definite Hessian indicates what? | Tại một điểm dừng, Hessian xác định dương cho biết điều gì?**

A. Always a global maximum | Luôn là cực đại toàn cục

B. A strict local minimum | Một cực tiểu địa phương nghiêm ngặt

C. A strict local maximum | Một cực đại địa phương nghiêm ngặt

D. A saddle point | Một điểm yên ngựa

**Đáp án: B**

**Giải thích:** Hessian xác định dương nghĩa là hàm cong lên theo mọi hướng ở điểm dừng; trong điều kiện trơn phù hợp, đó là cực tiểu địa phương nghiêm ngặt.

**Q8. For f(x, y) = x² − y², how is the stationary point (0, 0) classified? | Với f(x, y) = x² − y², điểm dừng (0, 0) thuộc loại nào?**

A. Neither stationary nor extremum | Không phải điểm dừng hay cực trị

B. Strict local minimum | Cực tiểu địa phương nghiêm ngặt

C. Saddle point | Điểm yên ngựa

D. Strict local maximum | Cực đại địa phương nghiêm ngặt

**Đáp án: C**

**Giải thích:** Theo trục x, f tăng khỏi 0; theo trục y, f giảm khỏi 0. Vì vậy (0, 0) là điểm yên ngựa.

**Q9. What is Hessian of x²+y²? | Hessian của x²+y² là gì?**

A. `[[2,0],[0,-2]]` | `[[2,0],[0,-2]]`

B. `[[1,1],[y,x]]` | `[[1,1],[y,x]]`

C. `[[2,0],[0,2]]` | `[[2,0],[0,2]]`

D. `(3,2)` | `(3,2)`

**Đáp án: C**

**Giải thích:** Đạo hàm bậc hai của mỗi hạng bình phương bằng 2.

**Q10. What is Hessian of x²−y²? | Hessian của x²−y² là gì?**

A. `[[2,0],[0,-2]]` | `[[2,0],[0,-2]]`

B. `(3,2)` | `(3,2)`

C. `[[1,1],[y,x]]` | `[[1,1],[y,x]]`

D. `[[2,0],[0,2]]` | `[[2,0],[0,2]]`

**Đáp án: A**

**Giải thích:** Độ cong theo y bằng âm 2.

**Q11. What are stationary coordinates for (x−3)²+(y−2)²? | Tọa độ dừng của (x−3)²+(y−2)² là gì?**

A. `(3,2)` | `(3,2)`

B. `[[2,0],[0,2]]` | `[[2,0],[0,2]]`

C. `[[2,0],[0,-2]]` | `[[2,0],[0,-2]]`

D. `[[1,1],[y,x]]` | `[[1,1],[y,x]]`

**Đáp án: A**

**Giải thích:** Cả hai bình phương nhỏ nhất khi sai khác bằng 0.

**Q12. What is Jacobian of outputs x+y and xy? | Jacobian của đầu ra x+y và xy là gì?**

A. `[[2,0],[0,2]]` | `[[2,0],[0,2]]`

B. `[[2,0],[0,-2]]` | `[[2,0],[0,-2]]`

C. `(3,2)` | `(3,2)`

D. `[[1,1],[y,x]]` | `[[1,1],[y,x]]`

**Đáp án: D**

**Giải thích:** Lấy đạo hàm mỗi đầu ra theo x và y.

**Q13. What does a positive-definite Hessian at a stationary point indicate? | Hessian xác định dương tại điểm dừng biểu thị gì?**

A. A strict local minimum | Cực tiểu địa phương nghiêm ngặt

B. A saddle point | Điểm yên ngựa

C. The simple second-derivative test is inconclusive | Phép kiểm đạo hàm bậc hai đơn giản chưa kết luận

D. A strict local maximum | Cực đại địa phương nghiêm ngặt

**Đáp án: A**

**Giải thích:** Độ cong dương mọi hướng cho cực tiểu địa phương nghiêm ngặt.

**Q14. What does a negative-definite Hessian at a stationary point indicate? | Hessian xác định âm tại điểm dừng biểu thị gì?**

A. A strict local minimum | Cực tiểu địa phương nghiêm ngặt

B. A strict local maximum | Cực đại địa phương nghiêm ngặt

C. A saddle point | Điểm yên ngựa

D. The simple second-derivative test is inconclusive | Phép kiểm đạo hàm bậc hai đơn giản chưa kết luận

**Đáp án: B**

**Giải thích:** Độ cong âm mọi hướng cho cực đại địa phương nghiêm ngặt.

**Q15. What do mixed-sign Hessian eigenvalues indicate at a stationary point? | Trị riêng Hessian trái dấu ở điểm dừng biểu thị gì?**

A. A saddle point | Điểm yên ngựa

B. A strict local maximum | Cực đại địa phương nghiêm ngặt

C. A strict local minimum | Cực tiểu địa phương nghiêm ngặt

D. The simple second-derivative test is inconclusive | Phép kiểm đạo hàm bậc hai đơn giản chưa kết luận

**Đáp án: A**

**Giải thích:** Một số hướng tăng và hướng khác giảm.

**Q16. What if a Hessian has a zero eigenvalue at a stationary point? | Nếu Hessian có trị riêng 0 tại điểm dừng thì sao?**

A. A saddle point | Điểm yên ngựa

B. The simple second-derivative test is inconclusive | Phép kiểm đạo hàm bậc hai đơn giản chưa kết luận

C. A strict local maximum | Cực đại địa phương nghiêm ngặt

D. A strict local minimum | Cực tiểu địa phương nghiêm ngặt

**Đáp án: B**

**Giải thích:** Trị riêng 0 cần kiểm tra sâu hơn.

**Q17. What is Hessian shape for a scalar function of three inputs? | Hessian hàm vô hướng ba biến có shape nào?**

A. Sensitivities of one output to each input | Độ nhạy của một đầu ra theo từng đầu vào

B. How each output responds to one input | Các đầu ra đáp ứng với một đầu vào

C. `(3,3)` | `(3,3)`

D. It can also occur at a maximum or saddle | Nó còn xuất hiện ở cực đại hoặc yên ngựa

**Đáp án: C**

**Giải thích:** Các đạo hàm riêng bậc hai ghép từng biến với biến khác.

**Q18. What does one Jacobian row represent? | Một hàng Jacobian biểu thị gì?**

A. How each output responds to one input | Các đầu ra đáp ứng với một đầu vào

B. It can also occur at a maximum or saddle | Nó còn xuất hiện ở cực đại hoặc yên ngựa

C. `(3,3)` | `(3,3)`

D. Sensitivities of one output to each input | Độ nhạy của một đầu ra theo từng đầu vào

**Đáp án: D**

**Giải thích:** Hàng cố định đầu ra, cột đổi đầu vào.

**Q19. What does one Jacobian column represent? | Một cột Jacobian biểu thị gì?**

A. Sensitivities of one output to each input | Độ nhạy của một đầu ra theo từng đầu vào

B. It can also occur at a maximum or saddle | Nó còn xuất hiện ở cực đại hoặc yên ngựa

C. `(3,3)` | `(3,3)`

D. How each output responds to one input | Các đầu ra đáp ứng với một đầu vào

**Đáp án: D**

**Giải thích:** Cột cố định một đầu vào qua mọi đầu ra.

**Q20. Why isn't zero gradient alone sufficient to prove a minimum? | Vì sao gradient 0 chưa đủ chứng minh cực tiểu?**

A. Sensitivities of one output to each input | Độ nhạy của một đầu ra theo từng đầu vào

B. `(3,3)` | `(3,3)`

C. It can also occur at a maximum or saddle | Nó còn xuất hiện ở cực đại hoặc yên ngựa

D. How each output responds to one input | Các đầu ra đáp ứng với một đầu vào

**Đáp án: C**

**Giải thích:** Cực đại và yên ngựa cũng có thể có gradient 0.

## PY-34 — PY-34 — Xác suất, không gian mẫu và biến cố



**Q1. What is a random experiment? | Phép thử ngẫu nhiên là gì?**

A. Set of all possible outcomes | Tập tất cả kết quả có thể

B. A subset of the sample space | Một tập con của không gian mẫu

C. A measure between zero and one of an event's chance | Thước đo từ 0 đến 1 cho khả năng biến cố

D. A repeatable procedure with uncertain individual outcome | Thao tác lặp được nhưng kết quả mỗi lần không chắc chắn

**Đáp án: D**

**Giải thích:** Phép thử có thể sinh kết quả khác nhau.

**Q2. What is a sample space? | Không gian mẫu là gì?**

A. A subset of the sample space | Một tập con của không gian mẫu

B. A measure between zero and one of an event's chance | Thước đo từ 0 đến 1 cho khả năng biến cố

C. A repeatable procedure with uncertain individual outcome | Thao tác lặp được nhưng kết quả mỗi lần không chắc chắn

D. Set of all possible outcomes | Tập tất cả kết quả có thể

**Đáp án: D**

**Giải thích:** Không gian mẫu chứa mọi kết quả khả dĩ.

**Q3. What is an event? | Biến cố là gì?**

A. Set of all possible outcomes | Tập tất cả kết quả có thể

B. A measure between zero and one of an event's chance | Thước đo từ 0 đến 1 cho khả năng biến cố

C. A repeatable procedure with uncertain individual outcome | Thao tác lặp được nhưng kết quả mỗi lần không chắc chắn

D. A subset of the sample space | Một tập con của không gian mẫu

**Đáp án: D**

**Giải thích:** Biến cố là một nhóm kết quả.

**Q4. What is probability? | Xác suất là gì?**

A. Set of all possible outcomes | Tập tất cả kết quả có thể

B. A repeatable procedure with uncertain individual outcome | Thao tác lặp được nhưng kết quả mỗi lần không chắc chắn

C. A subset of the sample space | Một tập con của không gian mẫu

D. A measure between zero and one of an event's chance | Thước đo từ 0 đến 1 cho khả năng biến cố

**Đáp án: D**

**Giải thích:** Xác suất trong đoạn 0 đến 1.

**Q5. For a fair coin, what is the probability of heads on one toss? | Với đồng xu công bằng, xác suất được mặt ngửa trong một lần tung là bao nhiêu?**

A. 0 | 0

B. 0.25 | 0.25

C. 1 | 1

D. 0.5 | 0.5

**Đáp án: D**

**Giải thích:** Đồng xu có hai mặt đồng khả năng; xác suất mặt ngửa là 1/2 = 0.5.

**Q6. If P(A) = 0.35, what is P(not A)? | Nếu P(A) = 0.35, xác suất biến cố đối của A bằng bao nhiêu?**

A. 1.35 | 1.35

B. 0.75 | 0.75

C. 0.35 | 0.35

D. 0.65 | 0.65

**Đáp án: D**

**Giải thích:** Tổng xác suất của A và biến cố đối là 1, nên P(không A) = 1 − 0.35 = 0.65.

**Q7. A fair six-sided die is rolled once. What is P(result > 4)? | Tung một xúc xắc sáu mặt công bằng một lần, xác suất ra số lớn hơn 4 là bao nhiêu?**

A. 1/2 | 1/2

B. 1/3 | 1/3

C. 0 | 0

D. 1/6 | 1/6

**Đáp án: B**

**Giải thích:** Hai mặt thuận lợi là 5 và 6 trong tổng 6 mặt đồng khả năng: 2/6 = 1/3.

**Q8. Two fair coin tosses are independent. What is P(both heads)? | Hai lần tung đồng xu công bằng độc lập. Xác suất cả hai đều ra ngửa là bao nhiêu?**

A. 0.75 | 0.75

B. 0.5 | 0.5

C. 1 | 1

D. 0.25 | 0.25

**Đáp án: D**

**Giải thích:** Nhân xác suất hai biến cố độc lập: 0.5 × 0.5 = 0.25.

**Q9. What is P(even) for a fair six-sided die? | Xác suất mặt chẵn của xúc xắc công bằng sáu mặt?**

A. 4 | 4

B. 36 | 36

C. `1/2` | `1/2`

D. Zero | Bằng 0

**Đáp án: C**

**Giải thích:** Ba trong sáu mặt là số chẵn.

**Q10. How many outcomes are possible with two ordered six-sided dice? | Hai xúc xắc sáu mặt theo cặp có thứ tự có bao nhiêu kết quả?**

A. 4 | 4

B. 36 | 36

C. Zero | Bằng 0

D. `1/2` | `1/2`

**Đáp án: B**

**Giải thích:** Hai xúc xắc có 6×6 cặp có thứ tự.

**Q11. How many ordered pairs of dice sum to nine? | Bao nhiêu cặp có thứ tự của hai xúc xắc có tổng 9?**

A. 36 | 36

B. 4 | 4

C. `1/2` | `1/2`

D. Zero | Bằng 0

**Đáp án: B**

**Giải thích:** Bốn cặp là (3,6), (4,5), (5,4), (6,3).

**Q12. What is the probability of the empty event? | Xác suất biến cố rỗng là gì?**

A. 36 | 36

B. `1/2` | `1/2`

C. Zero | Bằng 0

D. 4 | 4

**Đáp án: C**

**Giải thích:** Biến cố không thể có xác suất 0.

**Q13. What is the probability of the entire sample space? | Xác suất của cả không gian mẫu là gì?**

A. No, sampling variation occurs | Không, có dao động do lấy mẫu

B. `1-P(A)` | `1-P(A)`

C. One | Bằng 1

D. One die's result does not change probabilities of the other | Kết quả một xúc xắc không đổi xác suất của xúc xắc kia

**Đáp án: C**

**Giải thích:** Biến cố chắc chắn có xác suất 1.

**Q14. What is P(not A) in terms of P(A)? | P(không A) theo P(A) là gì?**

A. One | Bằng 1

B. `1-P(A)` | `1-P(A)`

C. No, sampling variation occurs | Không, có dao động do lấy mẫu

D. One die's result does not change probabilities of the other | Kết quả một xúc xắc không đổi xác suất của xúc xắc kia

**Đáp án: B**

**Giải thích:** Biến cố và biến cố đối có tổng xác suất 1.

**Q15. Does a simulation always equal the true probability exactly? | Tỷ lệ mô phỏng có luôn bằng xác suất thật?**

A. No, sampling variation occurs | Không, có dao động do lấy mẫu

B. One | Bằng 1

C. One die's result does not change probabilities of the other | Kết quả một xúc xắc không đổi xác suất của xúc xắc kia

D. `1-P(A)` | `1-P(A)`

**Đáp án: A**

**Giải thích:** Mẫu hữu hạn dao động quanh xác suất nền.

**Q16. What does independence of two dice mean? | Hai xúc xắc độc lập nghĩa là gì?**

A. One die's result does not change probabilities of the other | Kết quả một xúc xắc không đổi xác suất của xúc xắc kia

B. `1-P(A)` | `1-P(A)`

C. No, sampling variation occurs | Không, có dao động do lấy mẫu

D. One | Bằng 1

**Đáp án: A**

**Giải thích:** Độc lập nghĩa là một kết quả không đổi xác suất của biến cố còn lại.

**Q17. Why is printing a Set directly fragile for sample output? | Vì sao in trực tiếp Set khó đối chiếu đầu ra mẫu?**

A. Display order is not promised | Thứ tự hiển thị không được đảm bảo

B. That empirical frequency equals theoretical probability | Tần suất thực nghiệm đúng bằng xác suất lý thuyết

C. It tends to reduce sampling variability | Thường làm giảm dao động lấy mẫu

D. Its faces do not have equal probabilities | Các mặt không đồng xác suất

**Đáp án: A**

**Giải thích:** Set không bảo đảm thứ tự in.

**Q18. What does a fixed RNG seed not guarantee? | Seed RNG cố định không bảo đảm điều gì?**

A. Its faces do not have equal probabilities | Các mặt không đồng xác suất

B. It tends to reduce sampling variability | Thường làm giảm dao động lấy mẫu

C. Display order is not promised | Thứ tự hiển thị không được đảm bảo

D. That empirical frequency equals theoretical probability | Tần suất thực nghiệm đúng bằng xác suất lý thuyết

**Đáp án: D**

**Giải thích:** Seed giúp lặp lại mô phỏng nhưng không loại dao động.

**Q19. How does larger sample size generally affect estimate variability? | Tăng số mẫu thường ảnh hưởng độ dao động ước lượng thế nào?**

A. Display order is not promised | Thứ tự hiển thị không được đảm bảo

B. It tends to reduce sampling variability | Thường làm giảm dao động lấy mẫu

C. Its faces do not have equal probabilities | Các mặt không đồng xác suất

D. That empirical frequency equals theoretical probability | Tần suất thực nghiệm đúng bằng xác suất lý thuyết

**Đáp án: B**

**Giải thích:** Mẫu lớn thường ổn định tần suất tương đối hơn.

**Q20. Why can't a biased die use simple favorable-count ratios? | Vì sao xúc xắc lệch không dùng phép đếm mặt đơn giản?**

A. Its faces do not have equal probabilities | Các mặt không đồng xác suất

B. That empirical frequency equals theoretical probability | Tần suất thực nghiệm đúng bằng xác suất lý thuyết

C. It tends to reduce sampling variability | Thường làm giảm dao động lấy mẫu

D. Display order is not promised | Thứ tự hiển thị không được đảm bảo

**Đáp án: A**

**Giải thích:** Xác suất không đều cần cộng theo trọng số.

## PY-35 — PY-35 — Xác suất có điều kiện, Bayes và xác suất toàn phần



**Q1. What is conditional probability? | Xác suất có điều kiện là gì?**

A. One event does not change the probability of the other | Biến cố này không đổi xác suất của biến cố kia

B. A posterior from evidence, likelihood and prior | Xác suất sau bằng chứng từ likelihood và prior

C. Probability of A given B has occurred | Xác suất A khi biết B đã xảy ra

D. Overall chance weighted over a partition | Xác suất chung theo trọng số một phân hoạch

**Đáp án: C**

**Giải thích:** Nó thu hẹp mẫu nền về nhóm B.

**Q2. What is independence of events? | Độc lập giữa hai biến cố là gì?**

A. One event does not change the probability of the other | Biến cố này không đổi xác suất của biến cố kia

B. A posterior from evidence, likelihood and prior | Xác suất sau bằng chứng từ likelihood và prior

C. Overall chance weighted over a partition | Xác suất chung theo trọng số một phân hoạch

D. Probability of A given B has occurred | Xác suất A khi biết B đã xảy ra

**Đáp án: A**

**Giải thích:** Độc lập nghĩa là biến cố này không đổi xác suất biến cố kia.

**Q3. What does Bayes' theorem compute? | Định lý Bayes tính gì?**

A. A posterior from evidence, likelihood and prior | Xác suất sau bằng chứng từ likelihood và prior

B. Probability of A given B has occurred | Xác suất A khi biết B đã xảy ra

C. Overall chance weighted over a partition | Xác suất chung theo trọng số một phân hoạch

D. One event does not change the probability of the other | Biến cố này không đổi xác suất của biến cố kia

**Đáp án: A**

**Giải thích:** Bayes cập nhật tỷ lệ nền từ bằng chứng.

**Q4. What does total probability calculate? | Xác suất toàn phần tính gì?**

A. A posterior from evidence, likelihood and prior | Xác suất sau bằng chứng từ likelihood và prior

B. One event does not change the probability of the other | Biến cố này không đổi xác suất của biến cố kia

C. Overall chance weighted over a partition | Xác suất chung theo trọng số một phân hoạch

D. Probability of A given B has occurred | Xác suất A khi biết B đã xảy ra

**Đáp án: C**

**Giải thích:** Xác suất toàn phần dùng tỷ trọng của từng nhóm.

**Q5. Independent events A and B have P(A) = 0.3, P(B) = 0.6. What is P(A and B)? | Hai biến cố độc lập A và B có P(A) = 0.3, P(B) = 0.6. P(A giao B) bằng bao nhiêu?**

A. 0.3 | 0.3

B. 0.9 | 0.9

C. 0.18 | 0.18

D. 0.6 | 0.6

**Đáp án: C**

**Giải thích:** Độc lập nghĩa là P(A giao B) = P(A) × P(B) = 0.3 × 0.6 = 0.18.

**Q6. If P(A and B) = 0.12 and P(B) = 0.30, what is P(A|B)? | Nếu P(A giao B) = 0.12 và P(B) = 0.30, P(A|B) bằng bao nhiêu?**

A. 0.4 | 0.4

B. 0.12 | 0.12

C. 2.5 | 2.5

D. 0.3 | 0.3

**Đáp án: A**

**Giải thích:** Xác suất có điều kiện P(A|B) = P(A giao B)/P(B) = 0.12/0.30 = 0.4.

**Q7. Which statement about conditional probability is NOT always correct? | Phát biểu nào về xác suất có điều kiện KHÔNG luôn đúng?**

A. P(A|B) uses B as its reference group | P(A|B) dùng B làm nhóm xét

B. P(A|B) needs P(B) > 0 | P(A|B) cần P(B) > 0

C. Independence implies P(A|B) = P(A) when P(B)>0 | Độc lập thì P(A|B) = P(A) nếu P(B)>0

D. P(A|B) always equals P(B|A) | P(A|B) luôn bằng P(B|A)

**Đáp án: D**

**Giải thích:** Đảo A và B làm đổi nhóm điều kiện và mẫu số; hai xác suất có điều kiện nói chung khác nhau.

**Q8. A disease affects 10% of people. A test detects 90% of sick people and flags 10% of healthy people. What is P(sick | positive)? | Tỷ lệ mắc bệnh là 10%. Xét nghiệm báo dương ở 90% người bệnh và 10% người khỏe. Xác suất mắc bệnh khi đã có kết quả dương là bao nhiêu?**

A. 0.09 | 0.09

B. 0.5 | 0.5

C. 0.1 | 0.1

D. 0.9 | 0.9

**Đáp án: B**

**Giải thích:** Trong 100 người: khoảng 10 người bệnh tạo 9 dương thật; 90 người khỏe tạo 9 dương giả. Vậy P(bệnh|dương) = 9/(9+9) = 0.5.

**Q9. What does prior mean? | Prior có nghĩa gì?**

A. Probability of positive signal when no defect exists | Xác suất báo dương khi thực tế không có lỗi

B. Probability before current evidence | Xác suất trước khi có bằng chứng hiện tại

C. Probability of evidence under a hypothesis | Xác suất bằng chứng khi giả thuyết đúng

D. Updated hypothesis probability after evidence | Xác suất giả thuyết được cập nhật sau bằng chứng

**Đáp án: B**

**Giải thích:** Prior là xác suất nền.

**Q10. What does likelihood mean? | Likelihood biểu thị gì?**

A. Updated hypothesis probability after evidence | Xác suất giả thuyết được cập nhật sau bằng chứng

B. Probability before current evidence | Xác suất trước khi có bằng chứng hiện tại

C. Probability of evidence under a hypothesis | Xác suất bằng chứng khi giả thuyết đúng

D. Probability of positive signal when no defect exists | Xác suất báo dương khi thực tế không có lỗi

**Đáp án: C**

**Giải thích:** Likelihood xét bằng chứng khi giả thuyết đúng.

**Q11. What does posterior mean? | Posterior là gì?**

A. Probability of evidence under a hypothesis | Xác suất bằng chứng khi giả thuyết đúng

B. Probability before current evidence | Xác suất trước khi có bằng chứng hiện tại

C. Probability of positive signal when no defect exists | Xác suất báo dương khi thực tế không có lỗi

D. Updated hypothesis probability after evidence | Xác suất giả thuyết được cập nhật sau bằng chứng

**Đáp án: D**

**Giải thích:** Posterior đã tính đến bằng chứng quan sát.

**Q12. What is a false-positive rate? | Tỷ lệ dương giả là gì?**

A. Probability of evidence under a hypothesis | Xác suất bằng chứng khi giả thuyết đúng

B. Updated hypothesis probability after evidence | Xác suất giả thuyết được cập nhật sau bằng chứng

C. Probability of positive signal when no defect exists | Xác suất báo dương khi thực tế không có lỗi

D. Probability before current evidence | Xác suất trước khi có bằng chứng hiện tại

**Đáp án: C**

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

B. 0.3 | 0.3

C. 0.56 | 0.56

D. No; base rate and false positives also matter | Không; còn tỷ lệ nền và dương giả

**Đáp án: C**

**Giải thích:** 0.6×0.8+0.4×0.2 bằng 0.56.

**Q15. If P(A)=0.5 and P(B)=0.6 and they are independent, what is P(A and B)? | Nếu A, B độc lập có xác suất 0.5 và 0.6 thì P(A và B) là gì?**

A. 0.56 | 0.56

B. 0.2 | 0.2

C. 0.3 | 0.3

D. No; base rate and false positives also matter | Không; còn tỷ lệ nền và dương giả

**Đáp án: C**

**Giải thích:** Với biến cố độc lập, 0.5×0.6=0.3.

**Q16. If an alert has 99% sensitivity, does that mean 99% of alerts are true defects? | Độ nhạy 99% có nghĩa 99% cảnh báo là lỗi thật không?**

A. 0.3 | 0.3

B. 0.56 | 0.56

C. 0.2 | 0.2

D. No; base rate and false positives also matter | Không; còn tỷ lệ nền và dương giả

**Đáp án: D**

**Giải thích:** Độ nhạy và posterior xét hai nhóm mẫu nền khác nhau.

**Q17. Why does Bayes need the base rate? | Vì sao Bayes cần tỷ lệ nền?**

A. They condition on different reference groups | Chúng xét trên hai nhóm điều kiện khác nhau

B. That viewing ads caused purchases | Việc xem quảng cáo gây ra hành vi mua

C. The formula divides by P(B) | Vì công thức chia cho P(B)

D. Rare cases can yield many false alarms among positives | Sự kiện hiếm có thể làm dương giả chiếm nhiều trong cảnh báo

**Đáp án: D**

**Giải thích:** Sự kiện hiếm có thể khiến phần lớn cảnh báo là dương giả.

**Q18. Why must P(B)>0 for P(A given B)? | Vì sao cần P(B)>0 khi tính P(A khi B)?**

A. They condition on different reference groups | Chúng xét trên hai nhóm điều kiện khác nhau

B. Rare cases can yield many false alarms among positives | Sự kiện hiếm có thể làm dương giả chiếm nhiều trong cảnh báo

C. The formula divides by P(B) | Vì công thức chia cho P(B)

D. That viewing ads caused purchases | Việc xem quảng cáo gây ra hành vi mua

**Đáp án: C**

**Giải thích:** Chia cho 0 không xác định.

**Q19. What does an observational conditional purchase rate not prove? | Tỷ lệ mua có điều kiện trong quan sát không chứng minh gì?**

A. They condition on different reference groups | Chúng xét trên hai nhóm điều kiện khác nhau

B. That viewing ads caused purchases | Việc xem quảng cáo gây ra hành vi mua

C. Rare cases can yield many false alarms among positives | Sự kiện hiếm có thể làm dương giả chiếm nhiều trong cảnh báo

D. The formula divides by P(B) | Vì công thức chia cho P(B)

**Đáp án: B**

**Giải thích:** Liên hệ quan sát không tự chứng minh nhân quả.

**Q20. What distinguishes P(A given B) from P(B given A)? | P(A khi B) khác P(B khi A) ở đâu?**

A. The formula divides by P(B) | Vì công thức chia cho P(B)

B. Rare cases can yield many false alarms among positives | Sự kiện hiếm có thể làm dương giả chiếm nhiều trong cảnh báo

C. They condition on different reference groups | Chúng xét trên hai nhóm điều kiện khác nhau

D. That viewing ads caused purchases | Việc xem quảng cáo gây ra hành vi mua

**Đáp án: C**

**Giải thích:** Đảo điều kiện làm thay đổi mẫu số.

## PY-36 — PY-36 — Phân phối nhị thức và phân phối chuẩn



**Q1. What is a random variable? | Biến ngẫu nhiên là gì?**

A. A continuous symmetric bell-shaped density | Mật độ liên tục dạng chuông đối xứng

B. A numerical quantity assigned to random outcomes | Đại lượng số gắn với kết quả ngẫu nhiên

C. Probability mass at a discrete value | Xác suất ở một giá trị rời rạc

D. Successes in independent same-p trials | Số thành công trong các lần thử độc lập cùng p

**Đáp án: B**

**Giải thích:** Nó biến kết quả phép thử thành số. Biến ngẫu nhiên không phải toàn bộ kết quả thử; nó gán một con số, chẳng hạn số đơn đúng giờ, cho mỗi kết quả có thể.

**Q2. What does binomial X count? | Biến nhị thức X đếm gì?**

A. A continuous symmetric bell-shaped density | Mật độ liên tục dạng chuông đối xứng

B. Successes in independent same-p trials | Số thành công trong các lần thử độc lập cùng p

C. Probability mass at a discrete value | Xác suất ở một giá trị rời rạc

D. A numerical quantity assigned to random outcomes | Đại lượng số gắn với kết quả ngẫu nhiên

**Đáp án: B**

**Giải thích:** Mỗi lần thử có hai kết quả thành công hoặc thất bại. Biến nhị thức X nhận từ 0 đến n; nó đếm số lần đạt, không đếm số loại kết quả của một phép thử.

**Q3. What characterizes a normal distribution? | Phân phối chuẩn có đặc điểm gì?**

A. A numerical quantity assigned to random outcomes | Đại lượng số gắn với kết quả ngẫu nhiên

B. Probability mass at a discrete value | Xác suất ở một giá trị rời rạc

C. Successes in independent same-p trials | Số thành công trong các lần thử độc lập cùng p

D. A continuous symmetric bell-shaped density | Mật độ liên tục dạng chuông đối xứng

**Đáp án: D**

**Giải thích:** Được xác định bởi trung bình và độ lệch chuẩn. Hai tham số có ý nghĩa khác nhau: mean xác định tâm và độ lệch chuẩn dương quyết định độ phân tán.

**Q4. What is a PMF? | PMF là gì?**

A. A continuous symmetric bell-shaped density | Mật độ liên tục dạng chuông đối xứng

B. Probability mass at a discrete value | Xác suất ở một giá trị rời rạc

C. A numerical quantity assigned to random outcomes | Đại lượng số gắn với kết quả ngẫu nhiên

D. Successes in independent same-p trials | Số thành công trong các lần thử độc lập cùng p

**Đáp án: B**

**Giải thích:** PMF tính xác suất đúng một kết quả rời rạc. Với X nhị thức, PMF tại k trả đúng k lần thành công; CDF tại k tính cả mọi số lần ít hơn k.

**Q5. Two independent fair coins are tossed. What is P(exactly one head)? | Tung hai đồng xu công bằng độc lập. Xác suất có đúng một mặt ngửa là bao nhiêu?**

A. 1 | 1

B. 0.25 | 0.25

C. 0.5 | 0.5

D. 0.75 | 0.75

**Đáp án: C**

**Giải thích:** Bốn kết quả đồng khả năng: NN, NS, SN, SS (N = ngửa, S = sấp). Hai kết quả có đúng một ngửa, nên 2/4 = 0.5.

**Q6. In a standard normal distribution N(0,1), what is P(X ≤ 0)? | Trong phân phối chuẩn tắc N(0,1), P(X ≤ 0) bằng bao nhiêu?**

A. 0 | 0

B. 1 | 1

C. 0.25 | 0.25

D. 0.5 | 0.5

**Đáp án: D**

**Giải thích:** Phân phối chuẩn tắc đối xứng quanh trung bình 0, nên một nửa diện tích nằm bên trái 0.

**Q7. What happens to the spread of a normal distribution if its standard deviation increases while its mean stays fixed? | Nếu độ lệch chuẩn của phân phối chuẩn tăng còn trung bình không đổi, độ phân tán thay đổi thế nào?**

A. It spreads out more | Phân phối trải rộng hơn

B. Its mean becomes zero | Trung bình chuyển thành 0

C. It becomes uniform | Chuyển thành phân phối đều

D. It becomes narrower | Phân phối hẹp lại

**Đáp án: A**

**Giải thích:** Độ lệch chuẩn đo mức phân tán; tăng độ lệch chuẩn làm đường cong rộng và thấp hơn, nhưng vẫn giữ tâm cũ.

**Q8. For a normal distribution, how are mean and median related? | Trong phân phối chuẩn, trung bình và trung vị có quan hệ gì?**

A. The mean is always larger | Trung bình luôn lớn hơn

B. The median is always zero | Trung vị luôn bằng 0

C. The mean is always negative | Trung bình luôn âm

D. They are equal | Hai giá trị bằng nhau

**Đáp án: D**

**Giải thích:** Phân phối chuẩn đối xứng quanh trung bình nên trung bình, trung vị và mode đều trùng nhau.

**Q9. What condition is essential for a simple binomial model? | Điều kiện quan trọng của nhị thức đơn giản là gì?**

A. Independent trials with constant success probability | Các lần thử độc lập cùng xác suất thành công

B. Center and spread | Trung tâm và độ phân tán

C. Zero | Bằng 0

D. Strictly positive standard deviation | Độ lệch chuẩn phải lớn hơn 0

**Đáp án: A**

**Giải thích:** Phụ thuộc giữa lần thử làm sai giả định mô hình. Nếu đơn giao cùng chịu một sự cố hoặc xác suất đúng giờ khác nhau, mô hình nhị thức đơn giản có thể không phù hợp.

**Q10. What do mean and standard deviation determine for normal? | Mean và std xác định gì trong chuẩn?**

A. Center and spread | Trung tâm và độ phân tán

B. Independent trials with constant success probability | Các lần thử độc lập cùng xác suất thành công

C. Zero | Bằng 0

D. Strictly positive standard deviation | Độ lệch chuẩn phải lớn hơn 0

**Đáp án: A**

**Giải thích:** Trung bình định vị và độ lệch chuẩn xác định độ rộng. Đổi độ lệch chuẩn làm chuông rộng/hẹp nhưng không nhất thiết thay tâm của phân phối.

**Q11. What is P(X=x) for a continuous normal variable? | P(X=x) với biến chuẩn liên tục bằng bao nhiêu?**

A. Center and spread | Trung tâm và độ phân tán

B. Zero | Bằng 0

C. Independent trials with constant success probability | Các lần thử độc lập cùng xác suất thành công

D. Strictly positive standard deviation | Độ lệch chuẩn phải lớn hơn 0

**Đáp án: B**

**Giải thích:** Một điểm đơn có xác suất bằng 0. Xác suất trong khoảng là diện tích dưới PDF; một điểm riêng lẻ không có diện tích.

**Q12. Which quantity must be positive for norm.pdf scale? | scale của norm.pdf cần điều kiện nào?**

A. Center and spread | Trung tâm và độ phân tán

B. Independent trials with constant success probability | Các lần thử độc lập cùng xác suất thành công

C. Zero | Bằng 0

D. Strictly positive standard deviation | Độ lệch chuẩn phải lớn hơn 0

**Đáp án: D**

**Giải thích:** Độ lệch chuẩn không dương không hợp lệ. Trong SciPy, `scale` là sigma chứ không phải sigma bình phương; truyền phương sai sẽ làm sai toàn bộ phân phối.

**Q13. What does norm.cdf(0) equal for N(0,1)? | norm.cdf(0) với N(0,1) bằng gì?**

A. No, sampling noise remains | Không, vẫn có dao động lấy mẫu

B. From 0 to 1 inclusive | Từ 0 đến 1 gồm hai đầu

C. CDF(b) minus CDF(a) | CDF(b) trừ CDF(a)

D. 0.5 | 0.5

**Đáp án: D**

**Giải thích:** Chuẩn tắc đối xứng quanh 0. Chuẩn tắc đối xứng quanh trung bình 0 nên mỗi phía chứa một nửa xác suất.

**Q14. How do you calculate normal P(a<X≤b)? | Tính P(a<X≤b) cho chuẩn bằng gì?**

A. 0.5 | 0.5

B. CDF(b) minus CDF(a) | CDF(b) trừ CDF(a)

C. From 0 to 1 inclusive | Từ 0 đến 1 gồm hai đầu

D. No, sampling noise remains | Không, vẫn có dao động lấy mẫu

**Đáp án: B**

**Giải thích:** Hiệu xác suất tích lũy cho xác suất đoạn. Ví dụ P(−1<X≤1) bằng `norm.cdf(1)-norm.cdf(-1)`, xấp xỉ 0,6827.

**Q15. Does fixed RNG seed force sample mean to equal μ? | Seed cố định có buộc mean mẫu bằng μ?**

A. No, sampling noise remains | Không, vẫn có dao động lấy mẫu

B. From 0 to 1 inclusive | Từ 0 đến 1 gồm hai đầu

C. CDF(b) minus CDF(a) | CDF(b) trừ CDF(a)

D. 0.5 | 0.5

**Đáp án: A**

**Giải thích:** Seed lặp được mẫu, không đảm bảo đúng moment lý thuyết. Mô phỏng cố định seed có thể lặp lại nhưng trung bình mẫu vẫn lệch so với kỳ vọng lý thuyết.

**Q16. What is the range of probabilities? | Xác suất nằm trong đoạn nào?**

A. No, sampling noise remains | Không, vẫn có dao động lấy mẫu

B. CDF(b) minus CDF(a) | CDF(b) trừ CDF(a)

C. From 0 to 1 inclusive | Từ 0 đến 1 gồm hai đầu

D. 0.5 | 0.5

**Đáp án: C**

**Giải thích:** Xác suất không âm và không vượt một. Hai đầu 0 và 1 tương ứng biến cố không thể và chắc chắn.

**Q17. Can a continuous PDF exceed 1 at a point? | PDF liên tục có thể lớn hơn 1 tại một điểm không?**

A. The distribution becomes wider | Phân phối trải rộng hơn

B. Yes; only its total integral must be one | Có; chỉ tích phân toàn miền phải bằng một

C. Cumulative probability up to x | Xác suất tích lũy tới x

D. Point probabilities behave differently | Xác suất tại một điểm có ý nghĩa khác nhau

**Đáp án: B**

**Giải thích:** Chiều cao mật độ không phải xác suất. Đường chuẩn có độ lệch chuẩn nhỏ có thể có đỉnh PDF cao hơn 1 nhưng tổng diện tích vẫn bằng 1.

**Q18. What happens when standard deviation of normal increases? | Std phân phối chuẩn tăng sẽ thế nào?**

A. Yes; only its total integral must be one | Có; chỉ tích phân toàn miền phải bằng một

B. Point probabilities behave differently | Xác suất tại một điểm có ý nghĩa khác nhau

C. The distribution becomes wider | Phân phối trải rộng hơn

D. Cumulative probability up to x | Xác suất tích lũy tới x

**Đáp án: C**

**Giải thích:** Cùng tổng diện tích được trải ra trên miền rộng hơn. Sigma lớn hơn không tự làm dịch mean; nó khiến số đo phân tán xa hơn quanh cùng tâm.

**Q19. Why distinguish discrete and continuous variables? | Vì sao phân biệt biến rời rạc và liên tục?**

A. The distribution becomes wider | Phân phối trải rộng hơn

B. Cumulative probability up to x | Xác suất tích lũy tới x

C. Point probabilities behave differently | Xác suất tại một điểm có ý nghĩa khác nhau

D. Yes; only its total integral must be one | Có; chỉ tích phân toàn miền phải bằng một

**Đáp án: C**

**Giải thích:** PMF là xác suất còn PDF là mật độ. Số đếm như X=3 có xác suất tại điểm dương, còn biến đo liên tục có xác suất bằng đúng một giá trị là 0.

**Q20. What does norm.cdf(x,loc,scale) return? | norm.cdf(x,loc,scale) trả gì?**

A. Cumulative probability up to x | Xác suất tích lũy tới x

B. Point probabilities behave differently | Xác suất tại một điểm có ý nghĩa khác nhau

C. Yes; only its total integral must be one | Có; chỉ tích phân toàn miền phải bằng một

D. The distribution becomes wider | Phân phối trải rộng hơn

**Đáp án: A**

**Giải thích:** Nó là P(X≤x) theo phân phối chuẩn. Không lấy chiều cao PDF nếu câu hỏi là P(X≤x); cần dùng `cdf` để tính xác suất tích lũy.

## PY-37 — PY-37 — Thống kê mô tả: mean, median, mode, variance và std



**Q1. What does mean calculate? | Mean tính gì?**

A. Squared dispersion around the mean | Độ phân tán bình phương quanh mean

B. Middle ranked value after sorting | Giá trị ở giữa sau khi sắp

C. Spread in original measurement units | Độ phân tán cùng đơn vị gốc

D. Sum divided by observation count | Tổng chia số quan sát

**Đáp án: D**

**Giải thích:** Mọi quan sát góp vào trung bình.

**Q2. What is median? | Median là gì?**

A. Spread in original measurement units | Độ phân tán cùng đơn vị gốc

B. Sum divided by observation count | Tổng chia số quan sát

C. Squared dispersion around the mean | Độ phân tán bình phương quanh mean

D. Middle ranked value after sorting | Giá trị ở giữa sau khi sắp

**Đáp án: D**

**Giải thích:** Trung vị dựa trên thứ tự, không dựa trên tổng độ lớn.

**Q3. What does variance measure? | Variance đo gì?**

A. Middle ranked value after sorting | Giá trị ở giữa sau khi sắp

B. Spread in original measurement units | Độ phân tán cùng đơn vị gốc

C. Sum divided by observation count | Tổng chia số quan sát

D. Squared dispersion around the mean | Độ phân tán bình phương quanh mean

**Đáp án: D**

**Giải thích:** Nó lấy trung bình bình phương độ lệch.

**Q4. What does standard deviation measure? | Std đo gì?**

A. Middle ranked value after sorting | Giá trị ở giữa sau khi sắp

B. Squared dispersion around the mean | Độ phân tán bình phương quanh mean

C. Sum divided by observation count | Tổng chia số quan sát

D. Spread in original measurement units | Độ phân tán cùng đơn vị gốc

**Đáp án: D**

**Giải thích:** Std là căn bậc hai phương sai.

**Q5. What is the median of [1, 2, 3, 10, 10]? | Trung vị của [1, 2, 3, 10, 10] bằng bao nhiêu?**

A. 3 | 3

B. 10 | 10

C. 5 | 5

D. 2 | 2

**Đáp án: A**

**Giải thích:** Dữ liệu đã tăng dần, có 5 số nên trung vị là số thứ ba: 3.

**Q6. A score is 80, the mean is 60, and standard deviation is 10. What is the z-score? | Điểm số là 80, trung bình 60, độ lệch chuẩn 10. Điểm z là bao nhiêu?**

A. 4 | 4

B. 2 | 2

C. 1 | 1

D. 20 | 20

**Đáp án: B**

**Giải thích:** z = (80 − 60)/10 = 2, nghĩa là cao hơn trung bình hai độ lệch chuẩn.

**Q7. What is the mean of [2, 4, 9]? | Giá trị trung bình của [2, 4, 9] là bao nhiêu?**

A. 5 | 5

B. 15 | 15

C. 6 | 6

D. 4 | 4

**Đáp án: A**

**Giải thích:** Cộng các giá trị 2 + 4 + 9 = 15 rồi chia cho 3 quan sát: mean = 5.

**Q8. When is the population standard deviation equal to zero? | Khi nào độ lệch chuẩn của tổng thể bằng 0?**

A. When the mean is zero | Khi trung bình bằng 0

B. When the sample is large | Khi mẫu lớn

C. When all values are positive | Khi tất cả số đều dương

D. When all observations are equal | Khi tất cả quan sát bằng nhau

**Đáp án: D**

**Giải thích:** Nếu tất cả giá trị giống nhau, không có độ lệch khỏi trung bình, nên phương sai và độ lệch chuẩn đều bằng 0.

**Q9. What is mean of 2,3,4? | Mean của 2,3,4 là bao nhiêu?**

A. 2/3 | 2/3

B. 4 | 4

C. 1 | 1

D. 3 | 3

**Đáp án: D**

**Giải thích:** Tổng 9 chia 3 bằng 3.

**Q10. What is median of 2,4,100? | Median của 2,4,100 là bao nhiêu?**

A. 1 | 1

B. 4 | 4

C. 2/3 | 2/3

D. 3 | 3

**Đáp án: B**

**Giải thích:** Bốn nằm giữa dãy đã sắp.

**Q11. What is population variance of 1,2,3? | Phương sai quần thể của 1,2,3 là gì?**

A. 3 | 3

B. 2/3 | 2/3

C. 4 | 4

D. 1 | 1

**Đáp án: B**

**Giải thích:** Bình phương lệch là 1,0,1 rồi chia ba.

**Q12. What is sample variance of 1,2,3? | Phương sai mẫu của 1,2,3 là gì?**

A. 4 | 4

B. 2/3 | 2/3

C. 1 | 1

D. 3 | 3

**Đáp án: C**

**Giải thích:** Tổng bình phương 2 chia n−1=2.

**Q13. What unit does variance have? | Variance có đơn vị gì?**

A. Original input units | Đơn vị gốc của dữ liệu

B. Median | Trung vị

C. Squared input units | Bình phương đơn vị dữ liệu

D. Mode | Yếu vị

**Đáp án: C**

**Giải thích:** Bình phương lệch làm bình phương đơn vị.

**Q14. What unit does std have? | Std có đơn vị gì?**

A. Median | Trung vị

B. Original input units | Đơn vị gốc của dữ liệu

C. Mode | Yếu vị

D. Squared input units | Bình phương đơn vị dữ liệu

**Đáp án: B**

**Giải thích:** Lấy căn đưa về đơn vị ban đầu.

**Q15. Which statistic resists large outliers better? | Thống kê nào ít nhạy với ngoại lệ cực lớn hơn?**

A. Squared input units | Bình phương đơn vị dữ liệu

B. Original input units | Đơn vị gốc của dữ liệu

C. Median | Trung vị

D. Mode | Yếu vị

**Đáp án: C**

**Giải thích:** Giá trị cực lớn ít tác động vị trí giữa.

**Q16. Which statistic is useful for categorical labels? | Thống kê nào phù hợp nhãn phân loại?**

A. Original input units | Đơn vị gốc của dữ liệu

B. Mode | Yếu vị

C. Squared input units | Bình phương đơn vị dữ liệu

D. Median | Trung vị

**Đáp án: B**

**Giải thích:** Lấy trung bình mã chữ không có ý nghĩa số học.

**Q17. Does std equal standard error? | Std có giống sai số chuẩn không?**

A. Summary statistics can lose meaning | Thống kê tổng hợp có thể mất ý nghĩa

B. No, std measures spread of individual values | Không, std đo độ phân tán quan sát

C. Different denominators give different results | Mẫu số khác nhau cho kết quả khác

D. Yes, large outliers can pull it up | Có, ngoại lệ lớn kéo mean lên

**Đáp án: B**

**Giải thích:** SE đo độ biến thiên của thống kê ước lượng.

**Q18. Can mean lie above most observations? | Mean có thể lớn hơn phần lớn quan sát không?**

A. No, std measures spread of individual values | Không, std đo độ phân tán quan sát

B. Yes, large outliers can pull it up | Có, ngoại lệ lớn kéo mean lên

C. Summary statistics can lose meaning | Thống kê tổng hợp có thể mất ý nghĩa

D. Different denominators give different results | Mẫu số khác nhau cho kết quả khác

**Đáp án: B**

**Giải thích:** Mean phụ thuộc tổng các giá trị.

**Q19. Why state ddof when reporting variance? | Vì sao báo ddof khi trình bày phương sai?**

A. Yes, large outliers can pull it up | Có, ngoại lệ lớn kéo mean lên

B. Different denominators give different results | Mẫu số khác nhau cho kết quả khác

C. Summary statistics can lose meaning | Thống kê tổng hợp có thể mất ý nghĩa

D. No, std measures spread of individual values | Không, std đo độ phân tán quan sát

**Đáp án: B**

**Giải thích:** Quy ước mẫu và quần thể khác nhau.

**Q20. What happens if values use mismatched units? | Nếu số liệu dùng đơn vị không thống nhất thì sao?**

A. Yes, large outliers can pull it up | Có, ngoại lệ lớn kéo mean lên

B. Different denominators give different results | Mẫu số khác nhau cho kết quả khác

C. No, std measures spread of individual values | Không, std đo độ phân tán quan sát

D. Summary statistics can lose meaning | Thống kê tổng hợp có thể mất ý nghĩa

**Đáp án: D**

**Giải thích:** Cần thống nhất đơn vị trước khi tính.

## PY-38 — PY-38 — Quantile, IQR, outlier, skewness và kurtosis



**Q1. What is a quantile? | Phân vị là gì?**

A. Fourth-moment tail behavior relative to normal | Đặc trưng moment bậc bốn/đuôi so với chuẩn

B. The difference Q3−Q1 | Hiệu Q3−Q1

C. A value associated with a cumulative rank | Giá trị gắn với một mức thứ hạng tích lũy

D. Distribution asymmetry | Mức bất đối xứng phân phối

**Đáp án: C**

**Giải thích:** Phân vị chia dữ liệu sắp thứ tự theo tỷ lệ.

**Q2. What is IQR? | IQR là gì?**

A. The difference Q3−Q1 | Hiệu Q3−Q1

B. A value associated with a cumulative rank | Giá trị gắn với một mức thứ hạng tích lũy

C. Fourth-moment tail behavior relative to normal | Đặc trưng moment bậc bốn/đuôi so với chuẩn

D. Distribution asymmetry | Mức bất đối xứng phân phối

**Đáp án: A**

**Giải thích:** Nó đo độ rộng nửa giữa dữ liệu.

**Q3. What does skewness measure? | Skewness đo gì?**

A. Fourth-moment tail behavior relative to normal | Đặc trưng moment bậc bốn/đuôi so với chuẩn

B. Distribution asymmetry | Mức bất đối xứng phân phối

C. A value associated with a cumulative rank | Giá trị gắn với một mức thứ hạng tích lũy

D. The difference Q3−Q1 | Hiệu Q3−Q1

**Đáp án: B**

**Giải thích:** Dấu gợi ý phía đuôi dài.

**Q4. What does excess kurtosis measure? | Excess kurtosis mô tả gì?**

A. A value associated with a cumulative rank | Giá trị gắn với một mức thứ hạng tích lũy

B. Distribution asymmetry | Mức bất đối xứng phân phối

C. The difference Q3−Q1 | Hiệu Q3−Q1

D. Fourth-moment tail behavior relative to normal | Đặc trưng moment bậc bốn/đuôi so với chuẩn

**Đáp án: D**

**Giải thích:** Pandas dùng mốc 0 cho chuẩn.

**Q5. If Q1 = 4 and Q3 = 10, what is the interquartile range (IQR)? | Nếu Q1 = 4, Q3 = 10, khoảng tứ phân vị IQR là bao nhiêu?**

A. 6 | 6

B. 4 | 4

C. 2.5 | 2.5

D. 14 | 14

**Đáp án: A**

**Giải thích:** IQR = Q3 − Q1 = 10 − 4 = 6.

**Q6. If Q1 = 4 and Q3 = 10, what is the upper outlier fence using 1.5 × IQR? | Nếu Q1 = 4 và Q3 = 10, ngưỡng ngoại lệ trên theo quy tắc 1.5 × IQR bằng bao nhiêu?**

A. 19 | 19

B. 15 | 15

C. 21 | 21

D. 16 | 16

**Đáp án: A**

**Giải thích:** IQR = 6, nên ngưỡng trên = Q3 + 1.5 × IQR = 10 + 9 = 19.

**Q7. A value is flagged as an outlier by the IQR rule. What can we conclude? | Một giá trị bị đánh dấu ngoại lệ theo quy tắc IQR. Kết luận nào hợp lý?**

A. It must equal the median | Nó bằng trung vị

B. It must be deleted | Bắt buộc phải xóa

C. It needs checking, but is not necessarily wrong | Nên kiểm tra, nhưng chưa chắc là dữ liệu sai

D. It proves a sensor failed | Chứng minh cảm biến bị lỗi

**Đáp án: C**

**Giải thích:** Quy tắc IQR chỉ đánh dấu giá trị nằm xa vùng giữa dữ liệu. Ngoại lệ có thể là giá trị thật.

**Q8. In a typically right-skewed distribution, which comparison is often observed? | Trong phân phối lệch phải điển hình, mối quan hệ nào thường gặp?**

A. Mean = median always | Trung bình luôn bằng trung vị

B. Mean < median always | Trung bình luôn nhỏ hơn trung vị

C. Mean > median often | Trung bình thường lớn hơn trung vị

D. Standard deviation is zero | Độ lệch chuẩn bằng 0

**Đáp án: C**

**Giải thích:** Đuôi kéo dài về bên phải thường làm trung bình bị kéo lên mạnh hơn trung vị; đây không phải quy tắc bắt buộc cho mọi bộ dữ liệu.

**Q9. What does positive skew suggest? | Skew dương gợi ý gì?**

A. A longer left tail | Đuôi trái dài hơn

B. Excess kurtosis | Kurtosis dư

C. A skewness statistic | Hệ số độ lệch phân phối

D. A longer right tail | Đuôi phải dài hơn

**Đáp án: D**

**Giải thích:** Giá trị lớn kéo đuôi sang phải.

**Q10. What does negative skew suggest? | Skew âm gợi ý gì?**

A. Excess kurtosis | Kurtosis dư

B. A longer right tail | Đuôi phải dài hơn

C. A skewness statistic | Hệ số độ lệch phân phối

D. A longer left tail | Đuôi trái dài hơn

**Đáp án: D**

**Giải thích:** Giá trị nhỏ kéo đuôi về trái.

**Q11. What does Series.kurt() return? | Series.kurt() trả gì?**

A. A longer right tail | Đuôi phải dài hơn

B. A longer left tail | Đuôi trái dài hơn

C. A skewness statistic | Hệ số độ lệch phân phối

D. Excess kurtosis | Kurtosis dư

**Đáp án: D**

**Giải thích:** Pandas dùng quy ước kurtosis dư.

**Q12. What does Series.skew() return? | Series.skew() trả gì?**

A. A skewness statistic | Hệ số độ lệch phân phối

B. Excess kurtosis | Kurtosis dư

C. A longer left tail | Đuôi trái dài hơn

D. A longer right tail | Đuôi phải dài hơn

**Đáp án: A**

**Giải thích:** Nó ước lượng bất đối xứng từ mẫu.

**Q13. What is Q3−Q1 called? | Q3−Q1 gọi là gì?**

A. 5 | 5

B. No; legitimate extremes may be flagged | Không; giá trị cực lớn hợp lệ vẫn có thể bị gắn cờ

C. Interquartile range | Khoảng tứ phân vị

D. 3 | 3

**Đáp án: C**

**Giải thích:** Hiệu này chính là IQR.

**Q14. What is median of 1,3,5? | Median của 1,3,5 bằng gì?**

A. 3 | 3

B. No; legitimate extremes may be flagged | Không; giá trị cực lớn hợp lệ vẫn có thể bị gắn cờ

C. Interquartile range | Khoảng tứ phân vị

D. 5 | 5

**Đáp án: A**

**Giải thích:** Giá trị đứng giữa là ba.

**Q15. What is IQR if Q1=2 and Q3=7? | IQR nếu Q1=2, Q3=7 bằng bao nhiêu?**

A. No; legitimate extremes may be flagged | Không; giá trị cực lớn hợp lệ vẫn có thể bị gắn cờ

B. 5 | 5

C. Interquartile range | Khoảng tứ phân vị

D. 3 | 3

**Đáp án: B**

**Giải thích:** Bảy trừ hai bằng năm.

**Q16. Does an IQR outlier flag prove a measurement error? | Gắn cờ outlier theo IQR có chứng minh số đo sai không?**

A. Interquartile range | Khoảng tứ phân vị

B. 5 | 5

C. No; legitimate extremes may be flagged | Không; giá trị cực lớn hợp lệ vẫn có thể bị gắn cờ

D. 3 | 3

**Đáp án: C**

**Giải thích:** Ngưỡng chỉ là quy tắc sàng lọc.

**Q17. Why can quantile values differ between software packages? | Vì sao phân vị có thể khác giữa các phần mềm?**

A. Fit the imputation value on train only | Tính giá trị điền chỉ từ train

B. Median | Trung vị

C. Different interpolation conventions | Quy ước nội suy khác nhau

D. It concerns fourth moments and tails | Nó liên quan moment bậc bốn và đuôi

**Đáp án: C**

**Giải thích:** Mẫu nhỏ dễ cho thấy sự khác biệt quy ước.

**Q18. Why should you avoid interpreting high kurtosis only as a tall peak? | Vì sao không nên hiểu kurtosis cao chỉ là đỉnh cao?**

A. Fit the imputation value on train only | Tính giá trị điền chỉ từ train

B. Different interpolation conventions | Quy ước nội suy khác nhau

C. It concerns fourth moments and tails | Nó liên quan moment bậc bốn và đuôi

D. Median | Trung vị

**Đáp án: C**

**Giải thích:** Chỉ độ cao đỉnh không đủ diễn giải.

**Q19. What statistic is often robust for imputation with extreme values? | Thống kê nào thường phù hợp điền thiếu khi có ngoại lệ lớn?**

A. Different interpolation conventions | Quy ước nội suy khác nhau

B. It concerns fourth moments and tails | Nó liên quan moment bậc bốn và đuôi

C. Fit the imputation value on train only | Tính giá trị điền chỉ từ train

D. Median | Trung vị

**Đáp án: D**

**Giải thích:** Thứ tự khiến trung vị ít nhạy với cực trị.

**Q20. What is a crucial train/test rule when imputing missing values? | Quy tắc train/test quan trọng khi điền khuyết là gì?**

A. It concerns fourth moments and tails | Nó liên quan moment bậc bốn và đuôi

B. Different interpolation conventions | Quy ước nội suy khác nhau

C. Median | Trung vị

D. Fit the imputation value on train only | Tính giá trị điền chỉ từ train

**Đáp án: D**

**Giải thích:** Dữ liệu test không tham gia học tham số tiền xử lý.

## PY-39 — PY-39 — Lấy mẫu, CLT và sai số chuẩn



**Q1. What is a population? | Tổng thể là gì?**

A. Sampling variability of an estimator | Độ biến thiên của thống kê ước lượng qua các mẫu

B. A selected subset of the population | Một nhóm con được chọn từ tổng thể

C. All units in the target group | Toàn bộ đơn vị của nhóm cần nghiên cứu

D. Approximate sampling distribution of sample means | Phân phối gần đúng của các trung bình mẫu

**Đáp án: C**

**Giải thích:** Kết luận dự kiến hướng đến tổng thể.

**Q2. What is a sample? | Mẫu là gì?**

A. Approximate sampling distribution of sample means | Phân phối gần đúng của các trung bình mẫu

B. A selected subset of the population | Một nhóm con được chọn từ tổng thể

C. Sampling variability of an estimator | Độ biến thiên của thống kê ước lượng qua các mẫu

D. All units in the target group | Toàn bộ đơn vị của nhóm cần nghiên cứu

**Đáp án: B**

**Giải thích:** Mẫu chứa một phần quan sát.

**Q3. What does CLT describe? | CLT mô tả gì?**

A. Approximate sampling distribution of sample means | Phân phối gần đúng của các trung bình mẫu

B. All units in the target group | Toàn bộ đơn vị của nhóm cần nghiên cứu

C. A selected subset of the population | Một nhóm con được chọn từ tổng thể

D. Sampling variability of an estimator | Độ biến thiên của thống kê ước lượng qua các mẫu

**Đáp án: A**

**Giải thích:** CLT nói về mean qua nhiều mẫu, không nói mọi giá trị gốc thành chuẩn.

**Q4. What is standard error? | SE là gì?**

A. Sampling variability of an estimator | Độ biến thiên của thống kê ước lượng qua các mẫu

B. A selected subset of the population | Một nhóm con được chọn từ tổng thể

C. All units in the target group | Toàn bộ đơn vị của nhóm cần nghiên cứu

D. Approximate sampling distribution of sample means | Phân phối gần đúng của các trung bình mẫu

**Đáp án: A**

**Giải thích:** SE mô tả độ bất định của thống kê.

**Q5. A random sample contains [3, 5, 7]. What is its sample mean? | Một mẫu ngẫu nhiên có các giá trị [3, 5, 7]. Trung bình mẫu bằng bao nhiêu?**

A. 7 | 7

B. 3 | 3

C. 5 | 5

D. 15 | 15

**Đáp án: C**

**Giải thích:** Trung bình mẫu = (3 + 5 + 7)/3 = 5.

**Q6. If the sample size rises from 25 to 100 and the population standard deviation stays constant, how does the standard error of the mean change? | Nếu cỡ mẫu tăng từ 25 lên 100 và độ lệch chuẩn tổng thể không đổi, sai số chuẩn của trung bình thay đổi thế nào?**

A. It doubles | Tăng gấp đôi

B. It stays unchanged | Không đổi

C. It halves | Giảm một nửa

D. It becomes zero | Bằng 0

**Đáp án: C**

**Giải thích:** SE = độ lệch chuẩn / căn(cỡ mẫu). Cỡ mẫu tăng 4 lần nên căn cỡ mẫu tăng 2 lần, vì vậy SE giảm một nửa.

**Q7. Does setting a random seed guarantee a representative sample? | Đặt seed ngẫu nhiên có bảo đảm lấy được mẫu đại diện không?**

A. Yes, for large populations | Có, nếu tổng thể lớn

B. Yes, if seed = 42 | Có, nếu seed = 42

C. No; it only helps reproduce the random draw | Không; seed chỉ giúp tái lập lượt lấy mẫu

D. Yes, always | Có, luôn luôn

**Đáp án: C**

**Giải thích:** Seed giúp lặp lại các số ngẫu nhiên, không khắc phục thiên lệch chọn mẫu hay bảo đảm đại diện.

**Q8. What does the Central Limit Theorem mainly describe under suitable conditions and increasing sample size? | Định lý giới hạn trung tâm chủ yếu mô tả điều gì khi các điều kiện phù hợp và cỡ mẫu tăng?**

A. Individual observations become equal | Các quan sát trở nên bằng nhau

B. The population mean becomes zero | Trung bình tổng thể trở về 0

C. All raw data become normal | Mọi dữ liệu gốc trở thành chuẩn

D. The distribution of sample means tends toward normal | Phân phối trung bình mẫu tiến gần phân phối chuẩn

**Đáp án: D**

**Giải thích:** CLT nói về phân phối của trung bình qua nhiều mẫu, không bắt buộc phân phối của từng quan sát chuyển thành chuẩn.

**Q9. What does sample SD measure? | SD mẫu đo gì?**

A. It halves | Giảm một nửa

B. s/sqrt(n) | s/sqrt(n)

C. Spread of individual values | Độ phân tán giá trị từng quan sát

D. Spread among hypothetical sample means | Độ phân tán giữa các mean mẫu giả định

**Đáp án: C**

**Giải thích:** SD khác bất định của mean mẫu.

**Q10. What does the SE of a mean measure? | SE của mean đo gì?**

A. s/sqrt(n) | s/sqrt(n)

B. It halves | Giảm một nửa

C. Spread among hypothetical sample means | Độ phân tán giữa các mean mẫu giả định

D. Spread of individual values | Độ phân tán giá trị từng quan sát

**Đáp án: C**

**Giải thích:** Lấy mẫu lặp gây biến thiên trung bình.

**Q11. What is a common estimated SE formula? | Công thức ước lượng SE thường dùng?**

A. s/sqrt(n) | s/sqrt(n)

B. Spread among hypothetical sample means | Độ phân tán giữa các mean mẫu giả định

C. Spread of individual values | Độ phân tán giá trị từng quan sát

D. It halves | Giảm một nửa

**Đáp án: A**

**Giải thích:** Công thức phù hợp trong các giả định lấy mẫu độc lập thường gặp.

**Q12. How does SE change when n quadruples and sigma is fixed? | SE đổi sao khi n gấp bốn, sigma giữ nguyên?**

A. s/sqrt(n) | s/sqrt(n)

B. It halves | Giảm một nửa

C. Spread among hypothetical sample means | Độ phân tán giữa các mean mẫu giả định

D. Spread of individual values | Độ phân tán giá trị từng quan sát

**Đáp án: B**

**Giải thích:** Căn bậc hai của bốn là hai.

**Q13. Does CLT assert that raw data become normally distributed? | CLT có nói dữ liệu gốc thành phân phối chuẩn không?**

A. It decreases for the sample mean under assumptions | Giảm đối với mean mẫu nếu giả định phù hợp

B. No, it concerns standardized sample means | Không, nói về mean mẫu được chuẩn hóa

C. No; sampling design matters | Không; thiết kế lấy mẫu mới quan trọng

D. A systematically unrepresentative sample | Mẫu không đại diện một cách có hệ thống

**Đáp án: B**

**Giải thích:** Tổng thể lệch vẫn có thể lệch.

**Q14. Is a sample necessarily representative because a seed is fixed? | Có seed cố định thì mẫu chắc chắn đại diện không?**

A. A systematically unrepresentative sample | Mẫu không đại diện một cách có hệ thống

B. No; sampling design matters | Không; thiết kế lấy mẫu mới quan trọng

C. No, it concerns standardized sample means | Không, nói về mean mẫu được chuẩn hóa

D. It decreases for the sample mean under assumptions | Giảm đối với mean mẫu nếu giả định phù hợp

**Đáp án: B**

**Giải thích:** Seed chỉ lặp cách chọn.

**Q15. What often happens to sampling variability as n grows? | n tăng thì dao động lấy mẫu thường thế nào?**

A. A systematically unrepresentative sample | Mẫu không đại diện một cách có hệ thống

B. It decreases for the sample mean under assumptions | Giảm đối với mean mẫu nếu giả định phù hợp

C. No; sampling design matters | Không; thiết kế lấy mẫu mới quan trọng

D. No, it concerns standardized sample means | Không, nói về mean mẫu được chuẩn hóa

**Đáp án: B**

**Giải thích:** SE thường tỷ lệ nghịch căn n.

**Q16. What is the impact of selection bias? | Thiên lệch chọn mẫu gây gì?**

A. It decreases for the sample mean under assumptions | Giảm đối với mean mẫu nếu giả định phù hợp

B. A systematically unrepresentative sample | Mẫu không đại diện một cách có hệ thống

C. No, it concerns standardized sample means | Không, nói về mean mẫu được chuẩn hóa

D. No; sampling design matters | Không; thiết kế lấy mẫu mới quan trọng

**Đáp án: B**

**Giải thích:** Tăng mẫu không tự sửa cách chọn sai.

**Q17. Does n=40 guarantee a good normal approximation in every problem? | n=40 có bảo đảm xấp xỉ chuẩn tốt ở mọi bài toán không?**

A. Clearly defined sampling assumptions | Giả định lấy mẫu được xác định rõ

B. No, underlying assumptions and tails matter | Không, còn phụ thuộc giả định và đuôi phân phối

C. Standard deviation | Độ lệch chuẩn

D. Uses n−1 in variance denominator | Dùng n−1 ở mẫu số phương sai

**Đáp án: B**

**Giải thích:** Không có ngưỡng cỡ mẫu đúng cho mọi trường hợp.

**Q18. What does `ddof=1` change in SD? | `ddof=1` đổi gì trong SD?**

A. No, underlying assumptions and tails matter | Không, còn phụ thuộc giả định và đuôi phân phối

B. Standard deviation | Độ lệch chuẩn

C. Uses n−1 in variance denominator | Dùng n−1 ở mẫu số phương sai

D. Clearly defined sampling assumptions | Giả định lấy mẫu được xác định rõ

**Đáp án: C**

**Giải thích:** Đây là quy ước cho ước lượng phương sai mẫu.

**Q19. Which quantity stays in original units, SD or variance? | Đại lượng nào giữ đơn vị gốc, SD hay variance?**

A. Uses n−1 in variance denominator | Dùng n−1 ở mẫu số phương sai

B. Clearly defined sampling assumptions | Giả định lấy mẫu được xác định rõ

C. Standard deviation | Độ lệch chuẩn

D. No, underlying assumptions and tails matter | Không, còn phụ thuộc giả định và đuôi phân phối

**Đáp án: C**

**Giải thích:** Phương sai có đơn vị bình phương.

**Q20. What is a prerequisite for repeated-sampling inference? | Điều kiện quan trọng của suy luận từ lấy mẫu lặp?**

A. No, underlying assumptions and tails matter | Không, còn phụ thuộc giả định và đuôi phân phối

B. Standard deviation | Độ lệch chuẩn

C. Clearly defined sampling assumptions | Giả định lấy mẫu được xác định rõ

D. Uses n−1 in variance denominator | Dùng n−1 ở mẫu số phương sai

**Đáp án: C**

**Giải thích:** Sự phụ thuộc và cách chọn mẫu ảnh hưởng SE.

## PY-40 — PY-40 — Kiểm định giả thuyết, p-value và khoảng tin cậy



**Q1. What is H0? | H₀ là gì?**

A. A null hypothesis subjected to statistical testing | Giả thuyết không được đem kiểm định

B. An interval from a procedure with 95% long-run coverage | Khoảng từ quy trình có mức bao phủ dài hạn 95%

C. Probability of equally or more extreme test results under H0 | Xác suất thống kê cực đoan bằng hoặc hơn khi H₀ đúng

D. Test a population mean against a specified value | Kiểm định trung bình quần thể với một mốc

**Đáp án: A**

**Giải thích:** Đó là giả định gốc của kiểm định. Ví dụ H₀: μ=50 nói về mean quần thể; không đòi mean mẫu quan sát phải đúng 50.

**Q2. What does p-value mean? | p-value nghĩa là gì?**

A. Probability of equally or more extreme test results under H0 | Xác suất thống kê cực đoan bằng hoặc hơn khi H₀ đúng

B. Test a population mean against a specified value | Kiểm định trung bình quần thể với một mốc

C. An interval from a procedure with 95% long-run coverage | Khoảng từ quy trình có mức bao phủ dài hạn 95%

D. A null hypothesis subjected to statistical testing | Giả thuyết không được đem kiểm định

**Đáp án: A**

**Giải thích:** Nó được tính với điều kiện mô hình H₀ đúng. p-value được tính từ thống kê kiểm định và phân phối dưới H₀, chứ không trực tiếp gán xác suất cho H₀.

**Q3. What is a one-sample t-test for? | T-test một mẫu dùng để làm gì?**

A. A null hypothesis subjected to statistical testing | Giả thuyết không được đem kiểm định

B. Test a population mean against a specified value | Kiểm định trung bình quần thể với một mốc

C. Probability of equally or more extreme test results under H0 | Xác suất thống kê cực đoan bằng hoặc hơn khi H₀ đúng

D. An interval from a procedure with 95% long-run coverage | Khoảng từ quy trình có mức bao phủ dài hạn 95%

**Đáp án: B**

**Giải thích:** Nó dùng trung bình và ước lượng phương sai mẫu. Khác kiểm định hai mẫu, t-test một mẫu so trung bình một mẫu với mốc cố định.

**Q4. What is a 95% confidence interval? | Khoảng tin cậy 95% là gì?**

A. A null hypothesis subjected to statistical testing | Giả thuyết không được đem kiểm định

B. Test a population mean against a specified value | Kiểm định trung bình quần thể với một mốc

C. An interval from a procedure with 95% long-run coverage | Khoảng từ quy trình có mức bao phủ dài hạn 95%

D. Probability of equally or more extreme test results under H0 | Xác suất thống kê cực đoan bằng hoặc hơn khi H₀ đúng

**Đáp án: C**

**Giải thích:** Bao phủ được hiểu qua những lần lấy mẫu lặp. Mức bao phủ 95% thuộc quy trình qua nhiều mẫu; một CI đã tính cần báo hai đầu mút và giả định đi kèm.

**Q5. A hypothesis test has p-value = 0.03 and significance level α = 0.05. What is the usual decision? | Kiểm định có p-value = 0.03 và mức ý nghĩa α = 0.05. Thường đưa ra quyết định nào?**

A. Set p-value to zero | Đặt p-value bằng 0

B. Accept H0 as proven | Chứng minh H0 đúng

C. Double the sample size automatically | Tự động tăng gấp đôi mẫu

D. Reject H0 | Bác bỏ H0

**Đáp án: D**

**Giải thích:** Vì 0.03 < 0.05, dữ liệu đủ bằng chứng để bác bỏ H0 ở mức ý nghĩa đã chọn; không chứng minh H1 chắc chắn đúng.

**Q6. A hypothesis test has p-value = 0.15 and α = 0.05. Which statement is appropriate? | Kiểm định có p-value = 0.15 và α = 0.05. Phát biểu nào phù hợp?**

A. Reject H0 | Bác bỏ H0

B. H0 is proven true | H0 đã được chứng minh đúng

C. Fail to reject H0 | Chưa đủ bằng chứng để bác bỏ H0

D. The sample mean must equal zero | Trung bình mẫu phải bằng 0

**Đáp án: C**

**Giải thích:** 0.15 ≥ 0.05 nên chưa đủ bằng chứng bác bỏ H0. Điều này không có nghĩa đã chứng minh H0 đúng.

**Q7. A 95% two-sided confidence interval contains the null value. What normally happens in the matching two-sided test at α = 0.05? | Khoảng tin cậy 95% hai phía chứa giá trị giả thuyết H0. Trong kiểm định hai phía tương ứng với α = 0.05, thường kết luận gì?**

A. H0 is definitely true | H0 chắc chắn đúng

B. Reject H0 | Bác bỏ H0

C. Fail to reject H0 | Chưa bác bỏ H0

D. The p-value is exactly 0 | p-value chính xác bằng 0

**Đáp án: C**

**Giải thích:** Với cùng mô hình và giả định, khi giá trị H0 nằm trong khoảng tin cậy 95% thì kiểm định hai phía tương ứng ở mức 5% không bác bỏ H0.

**Q8. Which description of a p-value is correct? | Mô tả nào đúng về p-value?**

A. Probability of observing results this extreme or more if H0 were true | Xác suất gặp kết quả cực đoan bằng hoặc hơn nếu H0 đúng

B. Probability H0 is true | Xác suất H0 đúng

C. Probability H1 is true | Xác suất H1 đúng

D. Probability the data were measured correctly | Xác suất dữ liệu được đo đúng

**Đáp án: A**

**Giải thích:** p-value xét mức độ bất thường của dữ liệu theo giả định H0 đúng, không phải xác suất H0 đúng.

**Q9. How is a one-sample t statistic formed? | Thống kê t một mẫu có dạng gì?**

A. n−1 | n−1

B. Lower and upper endpoints of a t interval | Hai đầu dưới/trên của khoảng t

C. (sample mean−mu0)/SE | (mean mẫu−mu0)/SE

D. Standard error of the mean | Sai số chuẩn của trung bình

**Đáp án: C**

**Giải thích:** Nó chuẩn hóa độ lệch của mean so với mốc. Chênh hai điểm chỉ có ý nghĩa kiểm định khi so với độ bất định lấy mẫu của mean.

**Q10. What does `scipy.stats.sem` estimate? | `scipy.stats.sem` ước lượng gì?**

A. n−1 | n−1

B. Lower and upper endpoints of a t interval | Hai đầu dưới/trên của khoảng t

C. (sample mean−mu0)/SE | (mean mẫu−mu0)/SE

D. Standard error of the mean | Sai số chuẩn của trung bình

**Đáp án: D**

**Giải thích:** Nó ước lượng độ dao động của mean mẫu. SE có xu hướng giảm khi n tăng dưới giả định phù hợp, còn SD của từng điểm không nhất thiết giảm.

**Q11. What does t.interval return? | t.interval trả gì?**

A. Lower and upper endpoints of a t interval | Hai đầu dưới/trên của khoảng t

B. (sample mean−mu0)/SE | (mean mẫu−mu0)/SE

C. Standard error of the mean | Sai số chuẩn của trung bình

D. n−1 | n−1

**Đáp án: A**

**Giải thích:** Khoảng phụ thuộc mức tin cậy, df, vị trí và độ rộng. Scale lớn làm khoảng rộng; loc là ước lượng trung tâm chứ không phải phần trăm tin cậy.

**Q12. What degrees of freedom are usual for one-sample t inference? | Bậc tự do thông dụng của t một mẫu là gì?**

A. n−1 | n−1

B. (sample mean−mu0)/SE | (mean mẫu−mu0)/SE

C. Lower and upper endpoints of a t interval | Hai đầu dưới/trên của khoảng t

D. Standard error of the mean | Sai số chuẩn của trung bình

**Đáp án: A**

**Giải thích:** Ước lượng phương sai mẫu làm mất một bậc tự do. Thống kê t ước lượng phương sai từ mẫu nên thường còn n−1 bậc tự do.

**Q13. Is p-value equal to P(H0 is true)? | p-value có bằng P(H₀ đúng) không?**

A. No; p is conditional on H0 | Không; p được tính khi giả định H₀ đúng

B. Failing to reject a false H0 | Không bác bỏ H₀ khi H₀ sai

C. It does not reject at the matching alpha | Không bác bỏ với alpha tương ứng

D. Rejecting a true null hypothesis | Bác bỏ H₀ khi H₀ thực sự đúng

**Đáp án: A**

**Giải thích:** p theo tần suất không phải posterior. Nhầm p với P(H₀|dữ liệu) là đảo chiều điều kiện; kiểm định tần suất xét mức cực đoan của dữ liệu khi H₀ đúng.

**Q14. If a confidence interval covers a null value, what often happens in a matching two-sided test? | Nếu CI chứa mốc H₀ thì kiểm định hai phía tương ứng thường thế nào?**

A. Rejecting a true null hypothesis | Bác bỏ H₀ khi H₀ thực sự đúng

B. No; p is conditional on H0 | Không; p được tính khi giả định H₀ đúng

C. Failing to reject a false H0 | Không bác bỏ H₀ khi H₀ sai

D. It does not reject at the matching alpha | Không bác bỏ với alpha tương ứng

**Đáp án: D**

**Giải thích:** Các quy trình tương ứng thường thống nhất dưới cùng giả định. Sự tương ứng cần kiểm định hai phía, mức tin cậy và giả định phù hợp; không đúng với mọi loại kiểm định và khoảng.

**Q15. What is a type I error? | Sai lầm loại I là gì?**

A. Rejecting a true null hypothesis | Bác bỏ H₀ khi H₀ thực sự đúng

B. No; p is conditional on H0 | Không; p được tính khi giả định H₀ đúng

C. Failing to reject a false H0 | Không bác bỏ H₀ khi H₀ sai

D. It does not reject at the matching alpha | Không bác bỏ với alpha tương ứng

**Đáp án: A**

**Giải thích:** Alpha kiểm soát lỗi loại I dưới giả định kiểm định. Sai lầm loại I là báo dương sai; alpha được chọn trước để kiểm soát xác suất lỗi này dưới giả định H₀.

**Q16. What is a type II error? | Sai lầm loại II là gì?**

A. It does not reject at the matching alpha | Không bác bỏ với alpha tương ứng

B. Rejecting a true null hypothesis | Bác bỏ H₀ khi H₀ thực sự đúng

C. No; p is conditional on H0 | Không; p được tính khi giả định H₀ đúng

D. Failing to reject a false H0 | Không bác bỏ H₀ khi H₀ sai

**Đáp án: D**

**Giải thích:** Nó khác lỗi bác bỏ H₀ đúng. Power bằng một trừ xác suất sai lầm loại II dưới giả thuyết đối cụ thể, liên quan đến thiết kế cỡ mẫu.

**Q17. Does a 95% CI say the fixed parameter has 95% probability of lying in this realized interval? | CI 95% có nghĩa xác suất tham số cố định trong khoảng đã tính là 95%?**

A. No; 95% describes repeated-interval coverage | Không; 95% mô tả tỷ lệ bao phủ khi lặp

B. No; effect size and context still matter | Không; còn kích thước tác động và bối cảnh

C. Strong dependence or problematic extreme data in small samples | Phụ thuộc mạnh hoặc dữ liệu cực đoan trong mẫu nhỏ

D. It becomes wider | Trở nên rộng hơn

**Đáp án: A**

**Giải thích:** Trong diễn giải tần suất, tham số cố định và khoảng thay đổi theo mẫu. Phát biểu xác suất áp dụng cho quy trình tạo khoảng ngẫu nhiên trước lấy mẫu, không phải μ cố định sau khi quan sát một CI.

**Q18. What can violate simple t-test assumptions? | Điều gì có thể vi phạm giả định t-test đơn giản?**

A. No; 95% describes repeated-interval coverage | Không; 95% mô tả tỷ lệ bao phủ khi lặp

B. No; effect size and context still matter | Không; còn kích thước tác động và bối cảnh

C. It becomes wider | Trở nên rộng hơn

D. Strong dependence or problematic extreme data in small samples | Phụ thuộc mạnh hoặc dữ liệu cực đoan trong mẫu nhỏ

**Đáp án: D**

**Giải thích:** Suy luận cần mô hình lấy mẫu phù hợp. Mẫu rất nhỏ, ngoại lệ nặng hoặc phụ thuộc có thể khiến p-value và CI báo ra thiếu tin cậy.

**Q19. What happens to CI width if SE grows with other inputs fixed? | SE tăng khi yếu tố khác giữ nguyên thì CI rộng ra sao?**

A. Strong dependence or problematic extreme data in small samples | Phụ thuộc mạnh hoặc dữ liệu cực đoan trong mẫu nhỏ

B. No; 95% describes repeated-interval coverage | Không; 95% mô tả tỷ lệ bao phủ khi lặp

C. No; effect size and context still matter | Không; còn kích thước tác động và bối cảnh

D. It becomes wider | Trở nên rộng hơn

**Đáp án: D**

**Giải thích:** Bất định cao làm khoảng rộng hơn. Trong khoảng t, SE tăng làm biên `t_critical × SE` tăng, khiến hai đầu mút cách mean xa hơn.

**Q20. Is statistical significance identical to practical importance? | Ý nghĩa thống kê có giống giá trị thực tiễn không?**

A. No; 95% describes repeated-interval coverage | Không; 95% mô tả tỷ lệ bao phủ khi lặp

B. Strong dependence or problematic extreme data in small samples | Phụ thuộc mạnh hoặc dữ liệu cực đoan trong mẫu nhỏ

C. No; effect size and context still matter | Không; còn kích thước tác động và bối cảnh

D. It becomes wider | Trở nên rộng hơn

**Đáp án: C**

**Giải thích:** p nhỏ không chứng minh hiệu quả thực tế lớn. Ngoài p-value cần báo kích thước tác động và độ bất định; tác động rất nhỏ có thể có ý nghĩa thống kê nhưng không hữu ích thực tế.

## PY-41 — PY-41 — Phân hoạch dữ liệu, classification và clustering



**Q1. What is a train set? | Train set là gì?**

A. Data used for fitting model parameters | Dữ liệu để fit tham số mô hình

B. Held-out data for final evaluation | Dữ liệu giữ lại để đánh giá cuối

C. Supervised prediction of discrete labels | Dự đoán nhãn rời rạc có giám sát

D. Grouping unlabeled observations by similarity | Nhóm quan sát chưa có nhãn theo độ tương đồng

**Đáp án: A**

**Giải thích:** Mô hình học tham số từ mẫu train, không cập nhật bằng bản ghi test. Đơn vị học là hàng train với đặc trưng và nhãn, không phải hàng test để chấm điểm.

**Q2. What is a test set? | Test set là gì?**

A. Data used for fitting model parameters | Dữ liệu để fit tham số mô hình

B. Held-out data for final evaluation | Dữ liệu giữ lại để đánh giá cuối

C. Supervised prediction of discrete labels | Dự đoán nhãn rời rạc có giám sát

D. Grouping unlabeled observations by similarity | Nhóm quan sát chưa có nhãn theo độ tương đồng

**Đáp án: B**

**Giải thích:** Test đo hiệu quả trên dữ liệu chưa học; chỉnh đi chỉnh lại theo test làm đánh giá thiên lệch. Điểm cốt lõi là test độc lập với quá trình học; điều chỉnh lặp dựa trên test sẽ làm mất tính độc lập ấy.

**Q3. What is classification? | Classification là gì?**

A. Data used for fitting model parameters | Dữ liệu để fit tham số mô hình

B. Held-out data for final evaluation | Dữ liệu giữ lại để đánh giá cuối

C. Supervised prediction of discrete labels | Dự đoán nhãn rời rạc có giám sát

D. Grouping unlabeled observations by similarity | Nhóm quan sát chưa có nhãn theo độ tương đồng

**Đáp án: C**

**Giải thích:** Lúc train phải có nhãn; đầu ra dự đoán là loại/phân lớp. Khác phân cụm, bài phân loại có nhãn mục tiêu rõ ràng khi học.

**Q4. What is clustering? | Clustering là gì?**

A. Data used for fitting model parameters | Dữ liệu để fit tham số mô hình

B. Held-out data for final evaluation | Dữ liệu giữ lại để đánh giá cuối

C. Supervised prediction of discrete labels | Dự đoán nhãn rời rạc có giám sát

D. Grouping unlabeled observations by similarity | Nhóm quan sát chưa có nhãn theo độ tương đồng

**Đáp án: D**

**Giải thích:** Phân cụm dựa vào X mà không fit nhãn lớp có sẵn. Khác classifier, KMeans không tự hiểu ý nghĩa đời thực của số hiệu cụm.

**Q5. What does stratify=y help preserve? | stratify=y giúp giữ gì?**

A. Approximate label proportions in train and test | Tỷ lệ nhãn xấp xỉ giữa train và test

B. Training features only | Chỉ các đặc trưng train

C. Preprocessing and estimator fitting/prediction | Tiền xử lý và các bước fit/dự đoán

D. Arbitrary cluster identifiers | Định danh cụm tùy ý

**Đáp án: A**

**Giải thích:** Nó chia các lớp theo tỷ lệ gần tương ứng khi số mẫu cho phép. Nó chỉ giữ tỷ lệ lớp xấp xỉ, không bảo đảm mọi nhóm nhỏ đều đại diện.

**Q6. What does StandardScaler fit on? | StandardScaler phải fit trên dữ liệu nào?**

A. Approximate label proportions in train and test | Tỷ lệ nhãn xấp xỉ giữa train và test

B. Training features only | Chỉ các đặc trưng train

C. Preprocessing and estimator fitting/prediction | Tiền xử lý và các bước fit/dự đoán

D. Arbitrary cluster identifiers | Định danh cụm tùy ý

**Đáp án: B**

**Giải thích:** Fit từ test làm rò rỉ phân phối đánh giá vào tiền xử lý. Được áp thống kê đã học từ train lên test, nhưng không được học lại thống kê từ test.

**Q7. What does Pipeline combine? | Pipeline gộp gì?**

A. Approximate label proportions in train and test | Tỷ lệ nhãn xấp xỉ giữa train và test

B. Training features only | Chỉ các đặc trưng train

C. Preprocessing and estimator fitting/prediction | Tiền xử lý và các bước fit/dự đoán

D. Arbitrary cluster identifiers | Định danh cụm tùy ý

**Đáp án: C**

**Giải thích:** Các phép đổi đã học được áp nhất quán khi dự đoán. Vì thế tiền xử lý phải nằm trong quy trình train, không fit trước trên toàn bộ dữ liệu.

**Q8. What do KMeans cluster IDs mean? | Mã cụm KMeans có nghĩa gì?**

A. Approximate label proportions in train and test | Tỷ lệ nhãn xấp xỉ giữa train và test

B. Training features only | Chỉ các đặc trưng train

C. Preprocessing and estimator fitting/prediction | Tiền xử lý và các bước fit/dự đoán

D. Arbitrary cluster identifiers | Định danh cụm tùy ý

**Đáp án: D**

**Giải thích:** Mã có thể đổi 0↔1 dù cách chia hình học không đổi. Hãy đánh giá theo thành viên nhóm hoặc ánh xạ có căn cứ, không mặc định mã 0 là một loài cụ thể.

**Q9. What is a feature? | Feature là gì?**

A. Input measurement used to predict | Số đo đầu vào dùng để dự đoán

B. The desired discrete output class | Lớp đầu ra muốn dự đoán

C. One predicted label per input row | Một nhãn dự đoán cho mỗi hàng đầu vào

D. Prediction accuracy on test labels | Tỷ lệ dự đoán đúng trên nhãn test

**Đáp án: A**

**Giải thích:** Đặc trưng nằm ở cột X, không phải nhãn đích. Mỗi cột cần có ý nghĩa và đơn vị đo rõ ràng trước khi đưa vào classifier.

**Q10. What is a target label? | Target label là gì?**

A. Input measurement used to predict | Số đo đầu vào dùng để dự đoán

B. The desired discrete output class | Lớp đầu ra muốn dự đoán

C. One predicted label per input row | Một nhãn dự đoán cho mỗi hàng đầu vào

D. Prediction accuracy on test labels | Tỷ lệ dự đoán đúng trên nhãn test

**Đáp án: B**

**Giải thích:** Classifier học ánh xạ từ X sang y. Nhãn là mục tiêu dự đoán, không phải đặc trưng được đưa sẵn khi dự đoán.

**Q11. What does `model.predict(X_test)` return? | `model.predict(X_test)` trả gì?**

A. Input measurement used to predict | Số đo đầu vào dùng để dự đoán

B. The desired discrete output class | Lớp đầu ra muốn dự đoán

C. One predicted label per input row | Một nhãn dự đoán cho mỗi hàng đầu vào

D. Prediction accuracy on test labels | Tỷ lệ dự đoán đúng trên nhãn test

**Đáp án: C**

**Giải thích:** Mỗi hàng test có một dự đoán lớp. Số nhãn dự đoán phải bằng số hàng đầu vào, nếu không sẽ thiếu kết quả cho một số mẫu.

**Q12. What does `model.score(X_test,y_test)` mean for a standard classifier? | `model.score` cho classifier thông dụng đo gì?**

A. Input measurement used to predict | Số đo đầu vào dùng để dự đoán

B. The desired discrete output class | Lớp đầu ra muốn dự đoán

C. One predicted label per input row | Một nhãn dự đoán cho mỗi hàng đầu vào

D. Prediction accuracy on test labels | Tỷ lệ dự đoán đúng trên nhãn test

**Đáp án: D**

**Giải thích:** Score so dự đoán với nhãn thật; không phải loss train. Nếu nhãn mất cân bằng, cần đọc thêm precision/recall theo lớp hoặc confusion matrix.

**Q13. Which check detects overlapping IDs across train and test? | Phép kiểm tra nào phát hiện ID xuất hiện ở cả train và test?**

A. `train_ids.isdisjoint(test_ids)` | `train_ids.isdisjoint(test_ids)`

B. No, correlated records or future information may leak | Không, bản ghi liên quan hoặc thông tin tương lai vẫn rò rỉ

C. No, it fits features X | Không, nó fit đặc trưng X

D. Cluster numbers have arbitrary permutations | Số hiệu cụm có thể hoán đổi tùy ý

**Đáp án: A**

**Giải thích:** isdisjoint xác nhận không có cùng mã ở cả hai tập. Kiểm tra này bắt trùng mã đơn giản, không phát hiện phép đo liên quan mang mã khác nhau.

**Q14. Does disjoint ID imply zero leakage? | Không trùng ID có chắc không rò rỉ?**

A. `train_ids.isdisjoint(test_ids)` | `train_ids.isdisjoint(test_ids)`

B. No, correlated records or future information may leak | Không, bản ghi liên quan hoặc thông tin tương lai vẫn rò rỉ

C. No, it fits features X | Không, nó fit đặc trưng X

D. Cluster numbers have arbitrary permutations | Số hiệu cụm có thể hoán đổi tùy ý

**Đáp án: B**

**Giải thích:** Rò rỉ có thể qua dữ liệu liên quan, phép đổi hoặc thông tin thời gian. Rò rỉ là thông tin đáng lẽ chưa biết lọt vào train, không chỉ là vấn đề trùng mã.

**Q15. Does KMeans need y labels to fit? | KMeans cần nhãn y khi fit không?**

A. `train_ids.isdisjoint(test_ids)` | `train_ids.isdisjoint(test_ids)`

B. No, correlated records or future information may leak | Không, bản ghi liên quan hoặc thông tin tương lai vẫn rò rỉ

C. No, it fits features X | Không, nó fit đặc trưng X

D. Cluster numbers have arbitrary permutations | Số hiệu cụm có thể hoán đổi tùy ý

**Đáp án: C**

**Giải thích:** Phân cụm không giám sát và không tối ưu accuracy theo nhãn thật. KMeans chỉ cần tọa độ đặc trưng và số cụm muốn tìm.

**Q16. Why not directly compare KMeans IDs to true classes for accuracy? | Vì sao không so trực tiếp mã KMeans với lớp thật để tính accuracy?**

A. `train_ids.isdisjoint(test_ids)` | `train_ids.isdisjoint(test_ids)`

B. No, correlated records or future information may leak | Không, bản ghi liên quan hoặc thông tin tương lai vẫn rò rỉ

C. No, it fits features X | Không, nó fit đặc trưng X

D. Cluster numbers have arbitrary permutations | Số hiệu cụm có thể hoán đổi tùy ý

**Đáp án: D**

**Giải thích:** Cùng nhóm có thể gắn mã đảo ngược mà chất lượng không đổi. Nếu đổi nhãn số của hai cụm, accuracy kiểu phân loại có thể đổi dù cách chia nhóm vẫn y hệt.

**Q17. What shape does a 150-row four-feature table have? | Bảng 150 hàng, bốn đặc trưng có shape nào?**

A. (150,4) | (150,4)

B. Allocate about a quarter to test | Dành khoảng một phần tư cho test

C. Held-out final test set | Tập test cuối cùng đã giữ lại

D. Predicted known class names | Tên lớp đã biết từ dữ liệu nhãn

**Đáp án: A**

**Giải thích:** Hàng là hoa, cột là bốn đặc trưng. Chiều thứ nhất đếm số hoa, chiều thứ hai đếm số đo trên mỗi hoa.

**Q18. What does test_size=0.25 mean? | test_size=0.25 nghĩa là gì?**

A. (150,4) | (150,4)

B. Allocate about a quarter to test | Dành khoảng một phần tư cho test

C. Held-out final test set | Tập test cuối cùng đã giữ lại

D. Predicted known class names | Tên lớp đã biết từ dữ liệu nhãn

**Đáp án: B**

**Giải thích:** Làm tròn quyết định số nguyên mẫu chính xác. Với số mẫu hữu hạn, thư viện phải làm tròn tỷ lệ yêu cầu thành số lượng nguyên.

**Q19. Which dataset must be excluded from hyperparameter tuning? | Không được dùng tập nào để điều chỉnh siêu tham số?**

A. (150,4) | (150,4)

B. Allocate about a quarter to test | Dành khoảng một phần tư cho test

C. Held-out final test set | Tập test cuối cùng đã giữ lại

D. Predicted known class names | Tên lớp đã biết từ dữ liệu nhãn

**Đáp án: C**

**Giải thích:** Chọn siêu tham số bằng validation/CV thuộc phần train. Hãy chọn siêu tham số bằng validation hoặc cross-validation trên phần train, sau đó đánh giá test cuối.

**Q20. What can a classification model output that KMeans does not inherently provide? | Classifier có đầu ra gì mà KMeans không tự bảo đảm?**

A. (150,4) | (150,4)

B. Allocate about a quarter to test | Dành khoảng một phần tư cho test

C. Held-out final test set | Tập test cuối cùng đã giữ lại

D. Predicted known class names | Tên lớp đã biết từ dữ liệu nhãn

**Đáp án: D**

**Giải thích:** KMeans tạo cụm chứ không tự gán ý nghĩa lớp thật. Mã lớp là nhãn đã xác định; mã cụm chỉ đánh dấu một nhóm vừa phát hiện.

## PY-42 — PY-42 — Tiền xử lý văn bản, token và Jaccard trong NLP



**Q1. What is a token? | Token là gì?**

A. A unit produced by a text-splitting rule | Đơn vị do quy tắc tách văn bản tạo

B. A collection of distinct tokens | Tập các token khác nhau

C. Applying consistent text representations | Đưa văn bản về dạng biểu diễn nhất quán

D. Intersection size divided by union size | Số phần tử giao chia số phần tử hợp

**Đáp án: A**

**Giải thích:** Token có thể là từ, mảnh từ hoặc dấu câu tùy bộ tách. Đơn vị cụ thể phụ thuộc quy tắc tokenizer; token không nhất thiết là một từ hoàn chỉnh.

**Q2. What is a vocabulary? | Vocabulary là gì?**

A. A unit produced by a text-splitting rule | Đơn vị do quy tắc tách văn bản tạo

B. A collection of distinct tokens | Tập các token khác nhau

C. Applying consistent text representations | Đưa văn bản về dạng biểu diễn nhất quán

D. Intersection size divided by union size | Số phần tử giao chia số phần tử hợp

**Đáp án: B**

**Giải thích:** Tập từ vựng bỏ trùng danh tính token, khác bảng tần suất. Nó trả lời có những token nào, chứ không trả lời mỗi token xuất hiện bao nhiêu lần.

**Q3. What is text normalization? | Chuẩn hóa văn bản là gì?**

A. A unit produced by a text-splitting rule | Đơn vị do quy tắc tách văn bản tạo

B. A collection of distinct tokens | Tập các token khác nhau

C. Applying consistent text representations | Đưa văn bản về dạng biểu diễn nhất quán

D. Intersection size divided by union size | Số phần tử giao chia số phần tử hợp

**Đáp án: C**

**Giải thích:** Chữ thường và cắt khoảng trắng giúp khớp dạng văn bản. Chuẩn hóa đổi cách biểu diễn; quy tắc phải nhất quán giữa các văn bản đem so.

**Q4. What is set-based Jaccard similarity? | Jaccard trên Set là gì?**

A. A unit produced by a text-splitting rule | Đơn vị do quy tắc tách văn bản tạo

B. A collection of distinct tokens | Tập các token khác nhau

C. Applying consistent text representations | Đưa văn bản về dạng biểu diễn nhất quán

D. Intersection size divided by union size | Số phần tử giao chia số phần tử hợp

**Đáp án: D**

**Giải thích:** Nó đo từ khác nhau chung so với tổng số từ khác nhau. Một từ chung trong năm từ khác nhau cho 1/5, không phải lấy độ dài một câu làm mẫu số.

**Q5. What does `str.split()` do without arguments? | `str.split()` không đối số làm gì?**

A. Splits on runs of whitespace | Tách theo chuỗi khoảng trắng liên tiếp

B. Converts letters to lowercase | Chuyển chữ thành chữ thường

C. Removes leading and trailing whitespace | Bỏ khoảng trắng hai đầu

D. To deduplicate and display consistently | Để bỏ token trùng và hiển thị ổn định

**Đáp án: A**

**Giải thích:** Tách bằng khoảng trắng không hiểu mọi ranh giới từ. Đây là quy tắc tách chuỗi, không phải thuật toán phân đoạn từ tiếng Việt về mặt ngôn ngữ.

**Q6. What does `lower()` do? | `lower()` làm gì?**

A. Splits on runs of whitespace | Tách theo chuỗi khoảng trắng liên tiếp

B. Converts letters to lowercase | Chuyển chữ thành chữ thường

C. Removes leading and trailing whitespace | Bỏ khoảng trắng hai đầu

D. To deduplicate and display consistently | Để bỏ token trùng và hiển thị ổn định

**Đáp án: B**

**Giải thích:** Giúp so biến thể chữ hoa/thường nhưng không bỏ dấu câu. `lower` chỉ đổi chữ hoa/thường, không tự xóa khoảng trắng hoặc tách token.

**Q7. What does `strip()` do? | `strip()` làm gì?**

A. Splits on runs of whitespace | Tách theo chuỗi khoảng trắng liên tiếp

B. Converts letters to lowercase | Chuyển chữ thành chữ thường

C. Removes leading and trailing whitespace | Bỏ khoảng trắng hai đầu

D. To deduplicate and display consistently | Để bỏ token trùng và hiển thị ổn định

**Đáp án: C**

**Giải thích:** strip không xóa khoảng trắng giữa câu. Muốn xử lý khoảng trắng giữa câu cần `split` hoặc bước khác, không thể chỉ dùng `strip`.

**Q8. Why use `sorted(set(tokens))` for examples? | Vì sao dùng `sorted(set(tokens))`?**

A. Splits on runs of whitespace | Tách theo chuỗi khoảng trắng liên tiếp

B. Converts letters to lowercase | Chuyển chữ thành chữ thường

C. Removes leading and trailing whitespace | Bỏ khoảng trắng hai đầu

D. To deduplicate and display consistently | Để bỏ token trùng và hiển thị ổn định

**Đáp án: D**

**Giải thích:** Set không bảo đảm thứ tự; sorted tạo List có thứ tự. Set loại phần tử trùng, còn `sorted` tạo List có thứ tự để in ổn định.

**Q9. What does A & B produce for sets? | A & B trên Set tạo gì?**

A. Common tokens | Các token chung

B. All distinct tokens from either set | Mọi token khác nhau thuộc ít nhất một tập

C. It ignores repeated occurrences | Bỏ qua số lần lặp

D. 1.0 | 1.0

**Đáp án: A**

**Giải thích:** Giao chỉ giữ giá trị có ở cả hai tập. Với A={'ai','python'}, B={'ai'}, giao chỉ có 'ai', không chứa toàn bộ A.

**Q10. What does A | B produce for sets? | A | B trên Set tạo gì?**

A. Common tokens | Các token chung

B. All distinct tokens from either set | Mọi token khác nhau thuộc ít nhất một tập

C. It ignores repeated occurrences | Bỏ qua số lần lặp

D. 1.0 | 1.0

**Đáp án: B**

**Giải thích:** Hợp loại token trùng ở cả hai bên. Hợp gồm từ riêng ở mỗi bên lẫn các từ chung giữa hai bên.

**Q11. How does Set Jaccard treat token frequency? | Jaccard Set xử lý tần suất token ra sao?**

A. Common tokens | Các token chung

B. All distinct tokens from either set | Mọi token khác nhau thuộc ít nhất một tập

C. It ignores repeated occurrences | Bỏ qua số lần lặp

D. 1.0 | 1.0

**Đáp án: C**

**Giải thích:** Chuyển sang Set mất số lần và thứ tự từ. Vì vậy Jaccard trên Set không phân biệt từ xuất hiện một lần với mười lần.

**Q12. What happens for identical nonempty token sets? | Hai tập token giống hệt và không rỗng cho Jaccard gì?**

A. Common tokens | Các token chung

B. All distinct tokens from either set | Mọi token khác nhau thuộc ít nhất một tập

C. It ignores repeated occurrences | Bỏ qua số lần lặp

D. 1.0 | 1.0

**Đáp án: D**

**Giải thích:** Giao bằng hợp nên tỷ số bằng một. Kết quả này áp dụng khi hợp không rỗng, đúng điều kiện đã nêu trong câu hỏi.

**Q13. What happens for disjoint nonempty token sets? | Hai tập token rời không rỗng cho Jaccard gì?**

A. 0.0 | 0.0

B. The formula has zero denominator; choose a convention | Công thức có mẫu số 0; cần quy ước riêng

C. No, multi-syllable words need more care | Không, từ nhiều tiếng cần xử lý thêm

D. No; punctuation remains | Không, dấu câu vẫn còn

**Đáp án: A**

**Giải thích:** Không có token chung nên tử số bằng không. Tử số bằng không nhưng mẫu số vẫn dương.

**Q14. What happens when both sets are empty? | Nếu hai Set đều rỗng thì Jaccard sao?**

A. 0.0 | 0.0

B. The formula has zero denominator; choose a convention | Công thức có mẫu số 0; cần quy ước riêng

C. No, multi-syllable words need more care | Không, từ nhiều tiếng cần xử lý thêm

D. No; punctuation remains | Không, dấu câu vẫn còn

**Đáp án: B**

**Giải thích:** Phép chia 0/0 không xác định; ứng dụng phải tự quy định. Ứng dụng có thể quy ước hai văn bản rỗng giống nhau 1, nhưng hệ khác có thể chọn 0 hoặc không xác định.

**Q15. Does whitespace splitting correctly segment all Vietnamese words? | split theo khoảng trắng có tách đúng mọi từ tiếng Việt không?**

A. 0.0 | 0.0

B. The formula has zero denominator; choose a convention | Công thức có mẫu số 0; cần quy ước riêng

C. No, multi-syllable words need more care | Không, từ nhiều tiếng cần xử lý thêm

D. No; punctuation remains | Không, dấu câu vẫn còn

**Đáp án: C**

**Giải thích:** Các tiếng ngăn bởi khoảng trắng chưa chắc là từ độc lập. Một từ tiếng Việt có thể gồm nhiều tiếng được ngăn bằng khoảng trắng.

**Q16. Can lowercasing alone remove punctuation? | Chỉ lower() có xóa dấu câu không?**

A. 0.0 | 0.0

B. The formula has zero denominator; choose a convention | Công thức có mẫu số 0; cần quy ước riêng

C. No, multi-syllable words need more care | Không, từ nhiều tiếng cần xử lý thêm

D. No; punctuation remains | Không, dấu câu vẫn còn

**Đáp án: D**

**Giải thích:** Đổi chữ thường và xử lý dấu câu là hai bước khác nhau. Dấu câu có thể còn dính vào token cho đến khi có bước làm sạch/tách riêng.

**Q17. Does Jaccard understand semantic synonyms? | Jaccard theo Set có hiểu từ đồng nghĩa không?**

A. No, it compares literal token identities | Không, nó so token theo mặt chữ

B. Number of distinct tokens in either document | Số token khác nhau ở ít nhất một tài liệu

C. Word order and term frequencies | Thứ tự và tần suất từ

D. For complex punctuation or multilingual segmentation | Khi có dấu câu phức tạp hoặc phân đoạn đa ngôn ngữ

**Đáp án: A**

**Giải thích:** Hai từ khác chữ dù đồng nghĩa vẫn có thể không chung token. Jaccard đo trùng mặt chữ; muốn so ý nghĩa cần biểu diễn ngôn ngữ phong phú hơn.

**Q18. What does len(A|B) represent? | len(A|B) biểu thị gì?**

A. No, it compares literal token identities | Không, nó so token theo mặt chữ

B. Number of distinct tokens in either document | Số token khác nhau ở ít nhất một tài liệu

C. Word order and term frequencies | Thứ tự và tần suất từ

D. For complex punctuation or multilingual segmentation | Khi có dấu câu phức tạp hoặc phân đoạn đa ngôn ngữ

**Đáp án: B**

**Giải thích:** Hợp là mẫu số của Jaccard trên Set. Khi hợp khác rỗng, đây là mẫu số; chỉ dùng len(A) có thể khiến điểm sai.

**Q19. What is lost when building a vocabulary as a Set? | Tạo vocabulary bằng Set mất thông tin nào?**

A. No, it compares literal token identities | Không, nó so token theo mặt chữ

B. Number of distinct tokens in either document | Số token khác nhau ở ít nhất một tài liệu

C. Word order and term frequencies | Thứ tự và tần suất từ

D. For complex punctuation or multilingual segmentation | Khi có dấu câu phức tạp hoặc phân đoạn đa ngôn ngữ

**Đáp án: C**

**Giải thích:** Set chỉ lưu sự có mặt, không lưu vị trí hay lượt xuất hiện. Khi cần đếm số lần hoặc giữ thứ tự, hãy dùng Counter hoặc List token.

**Q20. When should a specialized tokenizer be considered? | Khi nào nên xem bộ tách từ chuyên biệt?**

A. No, it compares literal token identities | Không, nó so token theo mặt chữ

B. Number of distinct tokens in either document | Số token khác nhau ở ít nhất một tài liệu

C. Word order and term frequencies | Thứ tự và tần suất từ

D. For complex punctuation or multilingual segmentation | Khi có dấu câu phức tạp hoặc phân đoạn đa ngôn ngữ

**Đáp án: D**

**Giải thích:** Tokenizer theo ngôn ngữ xử lý ranh giới vượt quá khoảng trắng. Chọn bộ tách phù hợp ngôn ngữ và dùng thống nhất lúc lập chỉ mục lẫn lúc truy vấn.

## PY-43 — PY-43 — Git: quản lý phiên bản và hợp tác trên mã nguồn



**Q1. What does a Git repository contain? | Repository Git chứa gì?**

A. Project content and version history metadata | Nội dung dự án và siêu dữ liệu lịch sử phiên bản

B. A recorded snapshot of staged content | Bản ghi trạng thái từ nội dung đã stage

C. A movable reference to a commit | Tham chiếu di chuyển trỏ đến commit

D. A named reference to another repository URL | Tên tham chiếu đến URL repository khác

**Đáp án: A**

**Giải thích:** Git lưu trạng thái và tham chiếu trong `.git`, không chỉ gom file vào thư mục. Nó là phạm vi quản lý lịch sử dự án, không phải một commit hay nhánh riêng lẻ.

**Q2. What is a commit? | Commit là gì?**

A. Project content and version history metadata | Nội dung dự án và siêu dữ liệu lịch sử phiên bản

B. A recorded snapshot of staged content | Bản ghi trạng thái từ nội dung đã stage

C. A movable reference to a commit | Tham chiếu di chuyển trỏ đến commit

D. A named reference to another repository URL | Tên tham chiếu đến URL repository khác

**Đáp án: B**

**Giải thích:** Commit lưu nội dung đã stage cùng mã định danh và thông điệp. Chỉnh file mà chưa stage không tự làm thay đổi nội dung của commit kế.

**Q3. What is a branch? | Nhánh Git là gì?**

A. Project content and version history metadata | Nội dung dự án và siêu dữ liệu lịch sử phiên bản

B. A recorded snapshot of staged content | Bản ghi trạng thái từ nội dung đã stage

C. A movable reference to a commit | Tham chiếu di chuyển trỏ đến commit

D. A named reference to another repository URL | Tên tham chiếu đến URL repository khác

**Đáp án: C**

**Giải thích:** Tạo nhánh không sao chép vật lý toàn bộ file sang thư mục khác. Nhánh dịch chuyển khi có commit mới, còn commit đã tạo là một bản ghi bất biến.

**Q4. What is a remote? | Remote là gì?**

A. Project content and version history metadata | Nội dung dự án và siêu dữ liệu lịch sử phiên bản

B. A recorded snapshot of staged content | Bản ghi trạng thái từ nội dung đã stage

C. A movable reference to a commit | Tham chiếu di chuyển trỏ đến commit

D. A named reference to another repository URL | Tên tham chiếu đến URL repository khác

**Đáp án: D**

**Giải thích:** Remote chỉ định địa chỉ đồng bộ; quyền truy cập được kiểm riêng. Đổi URL origin không tự xác thực người dùng hay tạo commit ở remote.

**Q5. What does `git status` show? | `git status` hiển thị gì?**

A. Untracked, staged and working changes | File chưa theo dõi, đã stage và đang sửa

B. Stages current changes to that path | Stage thay đổi hiện tại của đường dẫn đó

C. Records staged state with a message | Lưu phần đã stage thành commit có thông điệp

D. Compact commit history | Lịch sử commit rút gọn

**Đáp án: A**

**Giải thích:** Lệnh chỉ báo trạng thái, không tạo commit. Hãy xem status trước add/commit để phát hiện file chưa theo dõi hoặc chưa stage.

**Q6. What does `git add file.py` do? | `git add file.py` làm gì?**

A. Untracked, staged and working changes | File chưa theo dõi, đã stage và đang sửa

B. Stages current changes to that path | Stage thay đổi hiện tại của đường dẫn đó

C. Records staged state with a message | Lưu phần đã stage thành commit có thông điệp

D. Compact commit history | Lịch sử commit rút gọn

**Đáp án: B**

**Giải thích:** Stage chuẩn bị cho commit, không phải tải lên remote. Sau `git add`, xem `git diff --cached` để chắc chỉ những phần mong muốn được đưa vào stage.

**Q7. What does `git commit -m ...` do? | `git commit -m ...` làm gì?**

A. Untracked, staged and working changes | File chưa theo dõi, đã stage và đang sửa

B. Stages current changes to that path | Stage thay đổi hiện tại của đường dẫn đó

C. Records staged state with a message | Lưu phần đã stage thành commit có thông điệp

D. Compact commit history | Lịch sử commit rút gọn

**Đáp án: C**

**Giải thích:** Sau commit vẫn có thể còn sửa đổi chưa stage. Sửa đổi không nằm trong index sẽ không thuộc commit cho tới khi stage lại.

**Q8. What does `git log --oneline` show? | `git log --oneline` hiển thị gì?**

A. Untracked, staged and working changes | File chưa theo dõi, đã stage và đang sửa

B. Stages current changes to that path | Stage thay đổi hiện tại của đường dẫn đó

C. Records staged state with a message | Lưu phần đã stage thành commit có thông điệp

D. Compact commit history | Lịch sử commit rút gọn

**Đáp án: D**

**Giải thích:** Hiển thị hash và tiêu đề, không phải diff chi tiết. Muốn xem thay đổi từng dòng phải dùng diff hoặc show, không chỉ đọc tiêu đề log.

**Q9. What does `git switch -c name` do? | `git switch -c name` làm gì?**

A. Creates and checks out a new branch | Tạo và chuyển sang nhánh mới

B. Name of current branch | Tên nhánh hiện tại

C. Unstaged differences for that path | Khác biệt chưa stage của đường dẫn đó

D. Staged differences against last commit | Khác biệt đã stage so với commit gần nhất

**Đáp án: A**

**Giải thích:** Nhánh bắt đầu từ commit hiện tại nếu không chỉ định mốc khác. Nếu tên đã tồn tại thì tạo nhánh mới sẽ báo lỗi; khi đó cần chuyển nhánh thay vì tạo tiếp.

**Q10. What does `git branch --show-current` return? | `git branch --show-current` trả gì?**

A. Creates and checks out a new branch | Tạo và chuyển sang nhánh mới

B. Name of current branch | Tên nhánh hiện tại

C. Unstaged differences for that path | Khác biệt chưa stage của đường dẫn đó

D. Staged differences against last commit | Khác biệt đã stage so với commit gần nhất

**Đáp án: B**

**Giải thích:** Giúp tránh commit trên nhánh không mong muốn. Nếu đang ở detached HEAD, có thể không có tên nhánh hiện tại để in.

**Q11. What does `git diff -- file` show? | `git diff -- file` hiển thị gì?**

A. Creates and checks out a new branch | Tạo và chuyển sang nhánh mới

B. Name of current branch | Tên nhánh hiện tại

C. Unstaged differences for that path | Khác biệt chưa stage của đường dẫn đó

D. Staged differences against last commit | Khác biệt đã stage so với commit gần nhất

**Đáp án: C**

**Giải thích:** diff thường so working tree với staging area. Với nội dung đã stage, `git diff` thường không hiện; phải xem diff cached.

**Q12. What does `git diff --cached` show? | `git diff --cached` hiển thị gì?**

A. Creates and checks out a new branch | Tạo và chuyển sang nhánh mới

B. Name of current branch | Tên nhánh hiện tại

C. Unstaged differences for that path | Khác biệt chưa stage của đường dẫn đó

D. Staged differences against last commit | Khác biệt đã stage so với commit gần nhất

**Đáp án: D**

**Giải thích:** Giúp xem nội dung đã stage trước khi commit. Nó cho biết nội dung sẽ vào commit, khác phần mới chỉ đang sửa ngoài working tree.

**Q13. What does `git fetch` do? | `git fetch` làm gì?**

A. Downloads remote refs and objects without merging | Tải tham chiếu/dữ liệu remote nhưng chưa merge

B. Sends local refs and commits to remote if permitted | Gửi tham chiếu/commit lên remote nếu có quyền

C. To isolate work before integration | Để tách công việc trước khi tích hợp

D. The index of content selected for next commit | Chỉ mục nội dung được chọn cho commit kế

**Đáp án: A**

**Giải thích:** Fetch cập nhật thông tin remote nhưng chưa nhập vào nhánh đang làm. Fetch có thể cập nhật nhánh theo dõi remote nhưng không nhập chúng vào nhánh local đang đứng.

**Q14. What does `git push` do? | `git push` làm gì?**

A. Downloads remote refs and objects without merging | Tải tham chiếu/dữ liệu remote nhưng chưa merge

B. Sends local refs and commits to remote if permitted | Gửi tham chiếu/commit lên remote nếu có quyền

C. To isolate work before integration | Để tách công việc trước khi tích hợp

D. The index of content selected for next commit | Chỉ mục nội dung được chọn cho commit kế

**Đáp án: B**

**Giải thích:** Push không tự stage hoặc commit thay đổi chưa lưu. Các sửa đổi chưa commit phải được ghi vào lịch sử trước khi push chia sẻ bình thường.

**Q15. Why use a feature branch? | Vì sao dùng nhánh tính năng?**

A. Downloads remote refs and objects without merging | Tải tham chiếu/dữ liệu remote nhưng chưa merge

B. Sends local refs and commits to remote if permitted | Gửi tham chiếu/commit lên remote nếu có quyền

C. To isolate work before integration | Để tách công việc trước khi tích hợp

D. The index of content selected for next commit | Chỉ mục nội dung được chọn cho commit kế

**Đáp án: C**

**Giải thích:** Tách nhánh cho phép xem thử trước khi ảnh hưởng main. Chỉ nên merge nhánh tính năng sau khi kiểm tra đúng phần thay đổi dự định.

**Q16. What is staging area? | Staging area là gì?**

A. Downloads remote refs and objects without merging | Tải tham chiếu/dữ liệu remote nhưng chưa merge

B. Sends local refs and commits to remote if permitted | Gửi tham chiếu/commit lên remote nếu có quyền

C. To isolate work before integration | Để tách công việc trước khi tích hợp

D. The index of content selected for next commit | Chỉ mục nội dung được chọn cho commit kế

**Đáp án: D**

**Giải thích:** Nội dung đã stage có thể khác sửa đổi mới trong working tree. Index tách phần được ghi vào commit với những sửa đổi khác vẫn còn ở máy.

**Q17. What does `git pull --ff-only` require? | `git pull --ff-only` đòi hỏi gì?**

A. A fast-forward update without a merge commit | Có thể tiến thẳng lịch sử mà không tạo merge commit

B. No; authentication and permissions are separate | Không; xác thực và quyền là chuyện khác

C. No, they need to be staged again | Không, cần stage lại phần sửa mới

D. Review status and staged diff | Xem status và diff đã stage

**Đáp án: A**

**Giải thích:** Nó từ chối lịch sử cần tích hợp kiểu không fast-forward. Lịch sử đã phân nhánh cần quyết định tích hợp riêng; ff-only không tự xóa commit.

**Q18. Does setting origin grant push permissions? | Đặt origin có tự cấp quyền push không?**

A. A fast-forward update without a merge commit | Có thể tiến thẳng lịch sử mà không tạo merge commit

B. No; authentication and permissions are separate | Không; xác thực và quyền là chuyện khác

C. No, they need to be staged again | Không, cần stage lại phần sửa mới

D. Review status and staged diff | Xem status và diff đã stage

**Đáp án: B**

**Giải thích:** Có thể cấu hình URL dù không có quyền ghi. Quyền do máy chủ và thông tin đăng nhập quyết định, không phải do tên remote trên máy.

**Q19. Can git commit include edits made after the last git add automatically? | git commit có tự chứa sửa đổi sau lần git add cuối không?**

A. A fast-forward update without a merge commit | Có thể tiến thẳng lịch sử mà không tạo merge commit

B. No; authentication and permissions are separate | Không; xác thực và quyền là chuyện khác

C. No, they need to be staged again | Không, cần stage lại phần sửa mới

D. Review status and staged diff | Xem status và diff đã stage

**Đáp án: C**

**Giải thích:** Commit lưu trạng thái index, có thể cũ hơn nội dung đang sửa. Stage lại sẽ chụp phiên bản mới; nếu không commit dùng bản đã stage cũ.

**Q20. How should a developer check changes before committing? | Nên kiểm thay đổi trước commit bằng cách nào?**

A. A fast-forward update without a merge commit | Có thể tiến thẳng lịch sử mà không tạo merge commit

B. No; authentication and permissions are separate | Không; xác thực và quyền là chuyện khác

C. No, they need to be staged again | Không, cần stage lại phần sửa mới

D. Review status and staged diff | Xem status và diff đã stage

**Đáp án: D**

**Giải thích:** Kiểm tra giúp phát hiện file hoặc dòng thay đổi ngoài ý muốn. Nếu diff đã stage có bí mật hoặc file ngoài phạm vi, hãy bỏ stage hoặc sửa trước khi commit.

## PY-44 — PY-44 — Ứng dụng CLI: CRUD, kiểm tra dữ liệu và thống kê hồ sơ



**Q1. What are the four CRUD operations? | Bốn thao tác CRUD là gì?**

A. Create, Read, Update, Delete | Tạo, đọc, sửa, xóa

B. Checking constraints before processing or storing | Kiểm ràng buộc trước khi xử lý hoặc lưu

C. A field identifying the desired record | Trường xác định bản ghi cần tìm

D. Computing summaries from multiple records | Tính chỉ số tổng hợp từ nhiều bản ghi

**Đáp án: A**

**Giải thích:** CRUD mô tả vòng đời bản ghi, không phải một lệnh cơ sở dữ liệu. Nếu coi thêm mới như ghi đè mà không có chính sách, dữ liệu sinh viên cũ có thể bị mất.

**Q2. What is input validation? | Kiểm tra dữ liệu đầu vào là gì?**

A. Create, Read, Update, Delete | Tạo, đọc, sửa, xóa

B. Checking constraints before processing or storing | Kiểm ràng buộc trước khi xử lý hoặc lưu

C. A field identifying the desired record | Trường xác định bản ghi cần tìm

D. Computing summaries from multiple records | Tính chỉ số tổng hợp từ nhiều bản ghi

**Đáp án: B**

**Giải thích:** Validation chặn điểm sai hoặc mã trùng trước khi ghi. Validation kiểm cả kiểu dữ liệu và giới hạn nghiệp vụ, không chỉ kiểm code chạy được.

**Q3. What is a lookup key? | Khóa tra cứu là gì?**

A. Create, Read, Update, Delete | Tạo, đọc, sửa, xóa

B. Checking constraints before processing or storing | Kiểm ràng buộc trước khi xử lý hoặc lưu

C. A field identifying the desired record | Trường xác định bản ghi cần tìm

D. Computing summaries from multiple records | Tính chỉ số tổng hợp từ nhiều bản ghi

**Đáp án: C**

**Giải thích:** Mã sinh viên dùng làm khóa duy nhất, còn điểm là giá trị bản ghi. Nên dùng mã sinh viên duy nhất và ổn định làm khóa, không dùng điểm có thể thay đổi.

**Q4. What is aggregation? | Aggregate là gì?**

A. Create, Read, Update, Delete | Tạo, đọc, sửa, xóa

B. Checking constraints before processing or storing | Kiểm ràng buộc trước khi xử lý hoặc lưu

C. A field identifying the desired record | Trường xác định bản ghi cần tìm

D. Computing summaries from multiple records | Tính chỉ số tổng hợp từ nhiều bản ghi

**Đáp án: D**

**Giải thích:** Trung bình và cực đại tổng hợp trường số qua nhiều học viên. Với lớp rỗng, cần quy định kết quả 'không có dữ liệu' trước khi tính thống kê số.

**Q5. What does `db.get('S1')` do? | `db.get('S1')` làm gì?**

A. Returns S1 value or None if missing | Trả giá trị S1 hoặc None nếu thiếu

B. Inserts or overwrites the key's value | Thêm hoặc ghi đè giá trị của khóa

C. Removes S2 or returns None if absent | Xóa S2 hoặc trả None nếu thiếu

D. Number of scores in the list | Số điểm trong danh sách

**Đáp án: A**

**Giải thích:** get cho phép tra thiếu khóa mà không ném KeyError. `get` chỉ đọc; việc nhận giá trị mặc định không làm tạo hồ sơ còn thiếu.

**Q6. What does `db['S1']=record` do? | `db['S1']=record` làm gì?**

A. Returns S1 value or None if missing | Trả giá trị S1 hoặc None nếu thiếu

B. Inserts or overwrites the key's value | Thêm hoặc ghi đè giá trị của khóa

C. Removes S2 or returns None if absent | Xóa S2 hoặc trả None nếu thiếu

D. Number of scores in the list | Số điểm trong danh sách

**Đáp án: B**

**Giải thích:** Không kiểm khóa tồn tại, phép gán có thể ghi đè hồ sơ. Hàm thêm mới nên từ chối mã đã tồn tại, không chỉ dùng phép gán.

**Q7. What does `db.pop('S2',None)` do? | `db.pop('S2',None)` làm gì?**

A. Returns S1 value or None if missing | Trả giá trị S1 hoặc None nếu thiếu

B. Inserts or overwrites the key's value | Thêm hoặc ghi đè giá trị của khóa

C. Removes S2 or returns None if absent | Xóa S2 hoặc trả None nếu thiếu

D. Number of scores in the list | Số điểm trong danh sách

**Đáp án: C**

**Giải thích:** Giá trị mặc định tránh lỗi KeyError khi khóa vắng mặt. Nếu không có giá trị mặc định, pop khóa S2 còn thiếu sẽ ném KeyError.

**Q8. What does `len(scores)` provide? | `len(scores)` cung cấp gì?**

A. Returns S1 value or None if missing | Trả giá trị S1 hoặc None nếu thiếu

B. Inserts or overwrites the key's value | Thêm hoặc ghi đè giá trị của khóa

C. Removes S2 or returns None if absent | Xóa S2 hoặc trả None nếu thiếu

D. Number of scores in the list | Số điểm trong danh sách

**Đáp án: D**

**Giải thích:** Mean chia tổng cho số phần tử khi số lượng lớn hơn 0. Số lượng bằng 0 là ca biên, cần kiểm trước khi chia tổng.

**Q9. What is a safe score validation for integer score 8? | Kiểm tra điểm 8 hợp lệ trên thang 0–10 thế nào?**

A. `0 <= score <= 10` | `0 <= score <= 10`

B. Confirm the key does not exist | Xác nhận khóa chưa tồn tại

C. Confirm the key exists and new values are valid | Xác nhận khóa có và giá trị mới hợp lệ

D. KeyError | Lỗi KeyError

**Đáp án: A**

**Giải thích:** Cần kiểm cả cận dưới và cận trên. Nếu điểm đến từ chuỗi CLI bất kỳ, cần xác minh/đổi kiểu trước khi so sánh.

**Q10. What is required before adding a unique student ID? | Trước khi thêm mã sinh viên duy nhất cần gì?**

A. `0 <= score <= 10` | `0 <= score <= 10`

B. Confirm the key does not exist | Xác nhận khóa chưa tồn tại

C. Confirm the key exists and new values are valid | Xác nhận khóa có và giá trị mới hợp lệ

D. KeyError | Lỗi KeyError

**Đáp án: B**

**Giải thích:** Nhờ đó tránh ghi đè âm thầm hồ sơ khác. Kiểm khóa trước khi ghi; ghi đè rồi mới phát hiện có thể không khôi phục tự động được.

**Q11. What is required before updating a student record? | Trước khi sửa hồ sơ cần gì?**

A. `0 <= score <= 10` | `0 <= score <= 10`

B. Confirm the key does not exist | Xác nhận khóa chưa tồn tại

C. Confirm the key exists and new values are valid | Xác nhận khóa có và giá trị mới hợp lệ

D. KeyError | Lỗi KeyError

**Đáp án: C**

**Giải thích:** Sửa không nên vô tình tạo khóa mới. Nhờ đó vừa cập nhật đúng người vừa giữ điểm trong thang hợp lệ.

**Q12. What happens with `db['missing']` for an absent key? | Truy cập `db['missing']` khi thiếu khóa sẽ sao?**

A. `0 <= score <= 10` | `0 <= score <= 10`

B. Confirm the key does not exist | Xác nhận khóa chưa tồn tại

C. Confirm the key exists and new values are valid | Xác nhận khóa có và giá trị mới hợp lệ

D. KeyError | Lỗi KeyError

**Đáp án: D**

**Giải thích:** Truy cập trực tiếp gây lỗi khi khóa không tồn tại. Cần phân biệt khóa không tồn tại với học viên tồn tại nhưng điểm bằng 0.

**Q13. What does `sum([7,8,9])/3` equal? | `sum([7,8,9])/3` bằng gì?**

A. 8.0 | 8.0

B. 9 | 9

C. Check length before dividing | Kiểm số phần tử trước khi chia

D. No, not across process restarts by itself | Không, tự nó không giữ qua lúc khởi động lại

**Đáp án: A**

**Giải thích:** Tổng bằng 24 chia ba bằng 8. Cả ba điểm có trọng số bằng nhau; kết quả không phải điểm cao nhất hay tổng điểm.

**Q14. What does `max([7,8,9])` return? | `max([7,8,9])` trả gì?**

A. 8.0 | 8.0

B. 9 | 9

C. Check length before dividing | Kiểm số phần tử trước khi chia

D. No, not across process restarts by itself | Không, tự nó không giữ qua lúc khởi động lại

**Đáp án: B**

**Giải thích:** max chọn điểm lớn nhất. Phép này chọn điểm cao nhất, chưa tự xác định mã sinh viên nếu không giữ liên hệ bản ghi.

**Q15. How should an empty score list be handled before mean? | Trước khi tính mean với List điểm rỗng cần gì?**

A. 8.0 | 8.0

B. 9 | 9

C. Check length before dividing | Kiểm số phần tử trước khi chia

D. No, not across process restarts by itself | Không, tự nó không giữ qua lúc khởi động lại

**Đáp án: C**

**Giải thích:** Nếu không kiểm, chia cho len=0 sẽ gây lỗi. Chương trình cần nêu cách xử lý lớp rỗng, không bịa ra một điểm trung bình.

**Q16. What does a Python Dictionary persist automatically? | Dictionary Python tự lưu bền dữ liệu không?**

A. 8.0 | 8.0

B. 9 | 9

C. Check length before dividing | Kiểm số phần tử trước khi chia

D. No, not across process restarts by itself | Không, tự nó không giữ qua lúc khởi động lại

**Đáp án: D**

**Giải thích:** Hồ sơ trong RAM cần lưu ra file hoặc database để tồn tại lâu dài. Muốn dữ liệu còn sau khi mở lại, phải lưu bằng JSON, SQLite hoặc cơ chế lưu bền khác.

**Q17. What is a duplicate ID risk in CRUD? | Nguy cơ mã trùng trong CRUD là gì?**

A. Existing data may be overwritten | Dữ liệu cũ có thể bị ghi đè

B. Reject or safely parse with error handling | Từ chối hoặc đổi kiểu có xử lý lỗi

C. When missing keys are expected and handled | Khi dự kiến thiếu khóa và cần xử lý

D. Numeric score values | Các giá trị điểm dạng số

**Đáp án: A**

**Giải thích:** Kiểm tra khóa duy nhất tránh thay nhầm. Nên từ chối mã trùng hoặc dùng lệnh Update riêng nếu chủ ý sửa.

**Q18. What should CLI do with a non-numeric score input? | CLI nên làm gì với điểm nhập chữ thay vì số?**

A. Existing data may be overwritten | Dữ liệu cũ có thể bị ghi đè

B. Reject or safely parse with error handling | Từ chối hoặc đổi kiểu có xử lý lỗi

C. When missing keys are expected and handled | Khi dự kiến thiếu khóa và cần xử lý

D. Numeric score values | Các giá trị điểm dạng số

**Đáp án: B**

**Giải thích:** Chuỗi nhập từ terminal cần đổi số trước khi so ngưỡng. Hãy đổi kiểu an toàn, xử lý ValueError rồi mới kiểm tra thang điểm.

**Q19. When is `dict.get` preferable to square indexing? | Khi nào dùng `dict.get` thay `dict[key]`?**

A. Existing data may be overwritten | Dữ liệu cũ có thể bị ghi đè

B. Reject or safely parse with error handling | Từ chối hoặc đổi kiểu có xử lý lỗi

C. When missing keys are expected and handled | Khi dự kiến thiếu khóa và cần xử lý

D. Numeric score values | Các giá trị điểm dạng số

**Đáp án: C**

**Giải thích:** get trả mặc định thay cho ném KeyError. Khi chắc chắn mọi khóa đều có, truy cập [] phù hợp; nếu có thể thiếu thì `get` an toàn hơn.

**Q20. Which fields should an average score computation use? | Tính điểm trung bình nên dùng trường nào?**

A. Existing data may be overwritten | Dữ liệu cũ có thể bị ghi đè

B. Reject or safely parse with error handling | Từ chối hoặc đổi kiểu có xử lý lỗi

C. When missing keys are expected and handled | Khi dự kiến thiếu khóa và cần xử lý

D. Numeric score values | Các giá trị điểm dạng số

**Đáp án: D**

**Giải thích:** ID và tên để nhận diện, không đưa vào phép trung bình. Chỉ tổng hợp trường điểm dạng số, thống nhất thang đo và cách xử lý ô thiếu.

## PY-45 — PY-45 — Matplotlib: biểu đồ line, scatter và histogram



**Q1. What is a line chart best suited for? | Biểu đồ đường phù hợp gì?**

A. Showing changes across ordered positions | Thể hiện thay đổi theo các mốc có thứ tự

B. Individual paired x-y observations | Từng quan sát theo cặp x-y

C. Counts of numeric values within bins | Số quan sát số học trong từng khoảng

D. Naming variables and their units | Đặt tên đại lượng và đơn vị đo

**Đáp án: A**

**Giải thích:** Nối các mốc cho xu hướng, không đảm bảo có số đo giữa các mốc. Nếu dữ liệu là các loại không có thứ tự, biểu đồ cột phù hợp hơn việc nối đường.

**Q2. What does a scatter plot represent? | Scatter plot biểu diễn gì?**

A. Showing changes across ordered positions | Thể hiện thay đổi theo các mốc có thứ tự

B. Individual paired x-y observations | Từng quan sát theo cặp x-y

C. Counts of numeric values within bins | Số quan sát số học trong từng khoảng

D. Naming variables and their units | Đặt tên đại lượng và đơn vị đo

**Đáp án: B**

**Giải thích:** Mỗi điểm là x và y của cùng một bản ghi. Mảng x và y phải cùng thứ tự bản ghi, nếu không các điểm ghép sẽ sai.

**Q3. What does a histogram represent? | Histogram biểu diễn gì?**

A. Showing changes across ordered positions | Thể hiện thay đổi theo các mốc có thứ tự

B. Individual paired x-y observations | Từng quan sát theo cặp x-y

C. Counts of numeric values within bins | Số quan sát số học trong từng khoảng

D. Naming variables and their units | Đặt tên đại lượng và đơn vị đo

**Đáp án: C**

**Giải thích:** Histogram chia khoảng giá trị số, không giống biểu đồ cột loại. Đổi biên bins sẽ đổi số đếm; khi so histogram cần nêu rõ khoảng chia.

**Q4. What are axis labels for? | Nhãn trục để làm gì?**

A. Showing changes across ordered positions | Thể hiện thay đổi theo các mốc có thứ tự

B. Individual paired x-y observations | Từng quan sát theo cặp x-y

C. Counts of numeric values within bins | Số quan sát số học trong từng khoảng

D. Naming variables and their units | Đặt tên đại lượng và đơn vị đo

**Đáp án: D**

**Giải thích:** Nhãn tránh nhầm đơn vị thời gian, nhiệt độ hay tiền. Con số trên trục thiếu đơn vị khiến người xem không rõ ý nghĩa đo lường.

**Q5. Which function draws a line? | Hàm nào vẽ đường?**

A. `plt.plot(x,y)` | `plt.plot(x,y)`

B. `plt.scatter(x,y)` | `plt.scatter(x,y)`

C. `plt.hist(values,bins=...)` | `plt.hist(values,bins=...)`

D. `plt.savefig(path)` | `plt.savefig(path)`

**Đáp án: A**

**Giải thích:** plot nối điểm theo thứ tự đầu vào mặc định. Hàm vẽ đòi x,y tương ứng nhưng không tự kiểm dữ liệu có đúng ý nghĩa thực tế.

**Q6. Which function draws separate x-y points? | Hàm nào vẽ các điểm x-y riêng?**

A. `plt.plot(x,y)` | `plt.plot(x,y)`

B. `plt.scatter(x,y)` | `plt.scatter(x,y)`

C. `plt.hist(values,bins=...)` | `plt.hist(values,bins=...)`

D. `plt.savefig(path)` | `plt.savefig(path)`

**Đáp án: B**

**Giải thích:** scatter tạo dấu chấm riêng cho từng cặp quan sát. Đây là lựa chọn phù hợp khi các điểm là quan sát rời, không phải chuỗi thời gian cần nối.

**Q7. Which function draws histograms? | Hàm nào vẽ histogram?**

A. `plt.plot(x,y)` | `plt.plot(x,y)`

B. `plt.scatter(x,y)` | `plt.scatter(x,y)`

C. `plt.hist(values,bins=...)` | `plt.hist(values,bins=...)`

D. `plt.savefig(path)` | `plt.savefig(path)`

**Đáp án: C**

**Giải thích:** hist đếm trong từng khoảng rồi vẽ cột các khoảng số. `bins` xác định biên hoặc số khoảng; thay đổi tham số này làm thay đổi bản tóm tắt phân bố.

**Q8. Which function saves a figure? | Hàm nào lưu hình?**

A. `plt.plot(x,y)` | `plt.plot(x,y)`

B. `plt.scatter(x,y)` | `plt.scatter(x,y)`

C. `plt.hist(values,bins=...)` | `plt.hist(values,bins=...)`

D. `plt.savefig(path)` | `plt.savefig(path)`

**Đáp án: D**

**Giải thích:** savefig ghi hình đã vẽ ra tệp PNG. Phải lưu trước khi đóng Figure và kiểm đường dẫn cùng quyền ghi.

**Q9. Why should x and y have matching observation counts? | Vì sao x và y phải có số quan sát tương ứng?**

A. Each x needs its matching y | Mỗi x cần y tương ứng

B. Closes the current Figure | Đóng Figure hiện tại

C. Horizontal-axis label | Nhãn trục ngang

D. Vertical-axis label | Nhãn trục dọc

**Đáp án: A**

**Giải thích:** Không ghép được cặp khi thiếu phần tử tương ứng. Dãy lệch chiều có thể gây lỗi hoặc ghép sai đối tượng quan sát.

**Q10. What does `plt.close()` do? | `plt.close()` làm gì?**

A. Each x needs its matching y | Mỗi x cần y tương ứng

B. Closes the current Figure | Đóng Figure hiện tại

C. Horizontal-axis label | Nhãn trục ngang

D. Vertical-axis label | Nhãn trục dọc

**Đáp án: B**

**Giải thích:** Đóng giúp giải phóng tài nguyên và tránh mở nhiều hình. Nên đóng Figure sau khi xuất, nhất là trong vòng lặp tạo nhiều tệp.

**Q11. What does `plt.xlabel()` set? | `plt.xlabel()` đặt gì?**

A. Each x needs its matching y | Mỗi x cần y tương ứng

B. Closes the current Figure | Đóng Figure hiện tại

C. Horizontal-axis label | Nhãn trục ngang

D. Vertical-axis label | Nhãn trục dọc

**Đáp án: C**

**Giải thích:** Nó chỉ đổi chữ, không tự đổi dữ liệu hoặc đơn vị. Nhãn có ích nên ghi cả đại lượng và đơn vị như ngày hay giờ.

**Q12. What does `plt.ylabel()` set? | `plt.ylabel()` đặt gì?**

A. Each x needs its matching y | Mỗi x cần y tương ứng

B. Closes the current Figure | Đóng Figure hiện tại

C. Horizontal-axis label | Nhãn trục ngang

D. Vertical-axis label | Nhãn trục dọc

**Đáp án: D**

**Giải thích:** Nó mô tả y và nên kèm đơn vị. Trục nhiệt độ nên ghi rõ Celsius hoặc Fahrenheit, không chỉ ghi 'value'.

**Q13. How many markers represent three scatter records? | Ba bản ghi scatter tạo mấy điểm?**

A. Three | Ba

B. Yes, changing bins changes counts per interval | Có, đổi bins sẽ đổi số đếm theo khoảng

C. No, a categorical bar chart is clearer | Không, biểu đồ cột theo nhãn rõ hơn

D. No, association alone is insufficient | Không, chỉ liên hệ chưa đủ

**Đáp án: A**

**Giải thích:** Mỗi hàng tạo một điểm. Mỗi điểm tương ứng một sinh viên, không phải mỗi cột đặc trưng tạo một điểm.

**Q14. Do histogram counts depend on bin boundaries? | Số đếm histogram có phụ thuộc biên bins không?**

A. Three | Ba

B. Yes, changing bins changes counts per interval | Có, đổi bins sẽ đổi số đếm theo khoảng

C. No, a categorical bar chart is clearer | Không, biểu đồ cột theo nhãn rõ hơn

D. No, association alone is insufficient | Không, chỉ liên hệ chưa đủ

**Đáp án: B**

**Giải thích:** Cùng dữ liệu có thể được nhóm khác nhau. Chiều cao histogram thường là số lượng mẫu, không mặc nhiên là xác suất nếu chưa chuẩn hóa.

**Q15. Is a histogram appropriate for names A, B, C as categories? | Histogram có thích hợp trực tiếp cho nhãn A,B,C không?**

A. Three | Ba

B. Yes, changing bins changes counts per interval | Có, đổi bins sẽ đổi số đếm theo khoảng

C. No, a categorical bar chart is clearer | Không, biểu đồ cột theo nhãn rõ hơn

D. No, association alone is insufficient | Không, chỉ liên hệ chưa đủ

**Đáp án: C**

**Giải thích:** Histogram cần khoảng số thay vì tên loại. Cột phân loại so các nhóm tên; histogram dùng khoảng liên tục trên trục số.

**Q16. Can scatter points establish causation? | Scatter có chứng minh quan hệ nhân quả không?**

A. Three | Ba

B. Yes, changing bins changes counts per interval | Có, đổi bins sẽ đổi số đếm theo khoảng

C. No, a categorical bar chart is clearer | Không, biểu đồ cột theo nhãn rõ hơn

D. No, association alone is insufficient | Không, chỉ liên hệ chưa đủ

**Đáp án: D**

**Giải thích:** Biến khác hoặc cách lấy mẫu có thể tạo cùng xu hướng. Cần xem cách thiết kế nghiên cứu và yếu tố gây nhiễu trước khi nói một biến gây ra biến kia.

**Q17. What does backend Agg help with? | Backend Agg giúp gì?**

A. Rendering images without a GUI window | Kết xuất hình không cần cửa sổ GUI

B. Order and units of the time axis | Thứ tự và đơn vị trục thời gian

C. Array of bin counts | Mảng số lượng theo mỗi bin

D. No, it is a rendered image | Không, nó là ảnh được kết xuất

**Đáp án: A**

**Giải thích:** Agg phù hợp chạy script hàng loạt hoặc lưu hình trên server. Agg đặc biệt hữu ích cho kiểm thử tự động không cần màn hình đồ họa.

**Q18. What should be checked before interpreting a time plot? | Trước khi đọc biểu đồ thời gian cần kiểm gì?**

A. Rendering images without a GUI window | Kết xuất hình không cần cửa sổ GUI

B. Order and units of the time axis | Thứ tự và đơn vị trục thời gian

C. Array of bin counts | Mảng số lượng theo mỗi bin

D. No, it is a rendered image | Không, nó là ảnh được kết xuất

**Đáp án: B**

**Giải thích:** Sai thứ tự hoặc đơn vị khiến xu hướng bị hiểu sai. Nếu ngày bị xếp sai, đường nối có thể khiến người xem tưởng thời gian đi ngược.

**Q19. What does `plt.hist` return first? | `plt.hist` trả gì ở vị trí đầu?**

A. Rendering images without a GUI window | Kết xuất hình không cần cửa sổ GUI

B. Order and units of the time axis | Thứ tự và đơn vị trục thời gian

C. Array of bin counts | Mảng số lượng theo mỗi bin

D. No, it is a rendered image | Không, nó là ảnh được kết xuất

**Đáp án: C**

**Giải thích:** Giá trị trả về đầu là tần suất, phần sau là biên và đối tượng vẽ. Mảng biên trả về giúp xác định giá trị nào đóng góp vào từng khoảng đếm.

**Q20. Does a saved PNG retain an editable dataset automatically? | PNG lưu hình có tự chứa bảng dữ liệu có thể sửa không?**

A. Rendering images without a GUI window | Kết xuất hình không cần cửa sổ GUI

B. Order and units of the time axis | Thứ tự và đơn vị trục thời gian

C. Array of bin counts | Mảng số lượng theo mỗi bin

D. No, it is a rendered image | Không, nó là ảnh được kết xuất

**Đáp án: D**

**Giải thích:** Muốn tính lại và sửa biểu đồ cần lưu dữ liệu gốc riêng. Cần lưu script, nhãn và bảng số gốc để tái tạo lại biểu đồ khi cần.

## PY-46 — PY-46 — Mini project: dữ liệu → làm sạch → mô hình → đánh giá



**Q1. What is a feature in supervised learning? | Feature trong học có giám sát là gì?**

A. An input measurement used by the predictor | Đại lượng đo đầu vào mô hình sử dụng

B. A target value the model should predict | Giá trị đích mô hình cần dự đoán

C. An ordered chain of preprocessing and model steps | Chuỗi tiền xử lý và mô hình có thứ tự

D. Checking predictions against held-out targets | So dự đoán với nhãn thật giữ riêng

**Đáp án: A**

**Giải thích:** Trong Iris, bốn số đo cm nằm ở X, không phải nhãn y. Nếu đưa kết quả tương lai hoặc mã lớp vào X, đánh giá sẽ dễ giả tạo do rò rỉ.

**Q2. What is a label? | Label là gì?**

A. An input measurement used by the predictor | Đại lượng đo đầu vào mô hình sử dụng

B. A target value the model should predict | Giá trị đích mô hình cần dự đoán

C. An ordered chain of preprocessing and model steps | Chuỗi tiền xử lý và mô hình có thứ tự

D. Checking predictions against held-out targets | So dự đoán với nhãn thật giữ riêng

**Đáp án: B**

**Giải thích:** Classifier có giám sát học từ nhãn thật ghép với từng hàng train. Mỗi trong 150 hàng đặc trưng cần có nhãn tương ứng khi train.

**Q3. What is a pipeline? | Pipeline là gì?**

A. An input measurement used by the predictor | Đại lượng đo đầu vào mô hình sử dụng

B. A target value the model should predict | Giá trị đích mô hình cần dự đoán

C. An ordered chain of preprocessing and model steps | Chuỗi tiền xử lý và mô hình có thứ tự

D. Checking predictions against held-out targets | So dự đoán với nhãn thật giữ riêng

**Đáp án: C**

**Giải thích:** Nó fit bộ biến đổi trên train rồi tái sử dụng cho dữ liệu sau. Thứ tự rất quan trọng: điền thiếu và chuẩn hóa trước dự đoán, nhưng tham số chỉ học từ train.

**Q4. What is evaluation? | Evaluation là gì?**

A. An input measurement used by the predictor | Đại lượng đo đầu vào mô hình sử dụng

B. A target value the model should predict | Giá trị đích mô hình cần dự đoán

C. An ordered chain of preprocessing and model steps | Chuỗi tiền xử lý và mô hình có thứ tự

D. Checking predictions against held-out targets | So dự đoán với nhãn thật giữ riêng

**Đáp án: D**

**Giải thích:** Test cuối đánh giá dữ liệu chưa fit, không dùng lại mẫu học. Hãy dùng test giữ riêng không thay đổi; điểm train cao có thể chỉ là ghi nhớ dữ liệu.

**Q5. What does an Iris feature row represent? | Một hàng feature Iris biểu diễn gì?**

A. Four measurements for one flower | Bốn số đo của một bông hoa

B. The target class per sample | Lớp mục tiêu cho từng mẫu

C. Unavailable evaluation information entering fitting | Thông tin đánh giá đáng lẽ chưa biết lọt vào fit

D. To check sample/feature dimensions and alignment | Để kiểm chiều mẫu/đặc trưng và sự khớp nhãn

**Đáp án: A**

**Giải thích:** Hàng là một mẫu hoa, cột là số đo như chiều dài cánh. Với shape (150,4), 150 là mẫu, bốn là biến đo theo cm.

**Q6. What does y represent in classification? | y biểu diễn gì khi phân loại?**

A. Four measurements for one flower | Bốn số đo của một bông hoa

B. The target class per sample | Lớp mục tiêu cho từng mẫu

C. Unavailable evaluation information entering fitting | Thông tin đánh giá đáng lẽ chưa biết lọt vào fit

D. To check sample/feature dimensions and alignment | Để kiểm chiều mẫu/đặc trưng và sự khớp nhãn

**Đáp án: B**

**Giải thích:** Nhãn y phải ghép một-một với các hàng X. Nếu X và y sai thứ tự, thuật toán đúng vẫn học sai mối quan hệ dữ liệu–nhãn.

**Q7. What is data leakage? | Rò rỉ dữ liệu là gì?**

A. Four measurements for one flower | Bốn số đo của một bông hoa

B. The target class per sample | Lớp mục tiêu cho từng mẫu

C. Unavailable evaluation information entering fitting | Thông tin đánh giá đáng lẽ chưa biết lọt vào fit

D. To check sample/feature dimensions and alignment | Để kiểm chiều mẫu/đặc trưng và sự khớp nhãn

**Đáp án: C**

**Giải thích:** Fit tiền xử lý trên test hoặc dùng kết quả tương lai có thể làm chỉ số ảo. Rò rỉ còn xảy ra nếu chọn đặc trưng từ toàn bộ dữ liệu trước khi chia.

**Q8. Why inspect X.shape and y.shape first? | Vì sao kiểm X.shape và y.shape đầu tiên?**

A. Four measurements for one flower | Bốn số đo của một bông hoa

B. The target class per sample | Lớp mục tiêu cho từng mẫu

C. Unavailable evaluation information entering fitting | Thông tin đánh giá đáng lẽ chưa biết lọt vào fit

D. To check sample/feature dimensions and alignment | Để kiểm chiều mẫu/đặc trưng và sự khớp nhãn

**Đáp án: D**

**Giải thích:** Số hàng X lệch số nhãn y khiến việc fit sai. Hàng và nhãn lệch nhau phải được sửa trước khi fit hoặc tính điểm.

**Q9. What does train_test_split do? | train_test_split làm gì?**

A. Separates data into fitting and held-out portions | Chia dữ liệu thành phần học và phần giữ riêng

B. To preserve approximate class ratios in split parts | Để giữ tương đối tỷ lệ lớp trong các tập

C. Training features | Các đặc trưng train

D. Training features only | Chỉ đặc trưng train

**Đáp án: A**

**Giải thích:** Hàm chia dữ liệu, không tự học mô hình hay đo accuracy. Phải giữ cả X và y train/test; chia dữ liệu không tự tương đương huấn luyện.

**Q10. Why use stratify=y? | Vì sao dùng stratify=y?**

A. Separates data into fitting and held-out portions | Chia dữ liệu thành phần học và phần giữ riêng

B. To preserve approximate class ratios in split parts | Để giữ tương đối tỷ lệ lớp trong các tập

C. Training features | Các đặc trưng train

D. Training features only | Chỉ đặc trưng train

**Đáp án: B**

**Giải thích:** Giúp giảm lệch lớp khi mỗi lớp có đủ mẫu. Phân tầng hữu ích khi lớp ít mẫu có nguy cơ vắng khỏi tập test.

**Q11. What should SimpleImputer learn from? | SimpleImputer nên học từ đâu?**

A. Separates data into fitting and held-out portions | Chia dữ liệu thành phần học và phần giữ riêng

B. To preserve approximate class ratios in split parts | Để giữ tương đối tỷ lệ lớp trong các tập

C. Training features | Các đặc trưng train

D. Training features only | Chỉ đặc trưng train

**Đáp án: C**

**Giải thích:** Median tính từ toàn bộ dữ liệu làm lộ thống kê test. Hàng test không được tác động đến giá trị điền học được, kể cả khi hàng ấy thiếu dữ liệu.

**Q12. What should StandardScaler learn from? | StandardScaler nên fit từ đâu?**

A. Separates data into fitting and held-out portions | Chia dữ liệu thành phần học và phần giữ riêng

B. To preserve approximate class ratios in split parts | Để giữ tương đối tỷ lệ lớp trong các tập

C. Training features | Các đặc trưng train

D. Training features only | Chỉ đặc trưng train

**Đáp án: D**

**Giải thích:** Biến đổi test bằng mean/std train, không fit từ test. Mean và variance từ train phải được áp nhất quán lên mọi mẫu mới.

**Q13. What does LogisticRegression produce in Iris? | LogisticRegression trên Iris dự đoán gì?**

A. One of three discrete flower classes | Một trong ba loài hoa rời rạc

B. Correct predictions divided by total predictions | Số dự đoán đúng chia tổng số dự đoán

C. Actual labels | Các nhãn thật

D. Predicted labels | Các nhãn dự đoán

**Đáp án: A**

**Giải thích:** Dù có chữ Regression, LogisticRegression dùng để phân loại. Mô hình có thể xuất xác suất lớp, nhưng nhiệm vụ đang xét chọn một nhãn rời rạc.

**Q14. What does accuracy count? | Accuracy đếm gì?**

A. One of three discrete flower classes | Một trong ba loài hoa rời rạc

B. Correct predictions divided by total predictions | Số dự đoán đúng chia tổng số dự đoán

C. Actual labels | Các nhãn thật

D. Predicted labels | Các nhãn dự đoán

**Đáp án: B**

**Giải thích:** Accuracy hữu ích nhưng có thể che lỗi lớp hiếm. Với tập lệch lớp, accuracy cao có thể đến từ việc chỉ đoán lớp đông nhất.

**Q15. What do confusion matrix rows mean? | Hàng của confusion matrix nghĩa là gì?**

A. One of three discrete flower classes | Một trong ba loài hoa rời rạc

B. Correct predictions divided by total predictions | Số dự đoán đúng chia tổng số dự đoán

C. Actual labels | Các nhãn thật

D. Predicted labels | Các nhãn dự đoán

**Đáp án: C**

**Giải thích:** Mỗi hàng đếm mẫu thuộc lớp thật tương ứng. Hàng đại diện nhãn thật; ô ngoài đường chéo là lỗi xuất phát từ lớp thật ở hàng đó.

**Q16. What do confusion matrix columns mean? | Cột của confusion matrix nghĩa là gì?**

A. One of three discrete flower classes | Một trong ba loài hoa rời rạc

B. Correct predictions divided by total predictions | Số dự đoán đúng chia tổng số dự đoán

C. Actual labels | Các nhãn thật

D. Predicted labels | Các nhãn dự đoán

**Đáp án: D**

**Giải thích:** Ô ngoài đường chéo là trường hợp dự đoán sang lớp khác. Cột cho biết lớp dự đoán nào nhận các mẫu bị gán nhầm.

**Q17. What does PCA reduce? | PCA giảm gì?**

A. Feature dimensionality while retaining sample rows | Số chiều đặc trưng nhưng giữ số hàng mẫu

B. To avoid using test distribution to learn axes | Tránh lấy phân phối test để học các trục

C. On the same held-out split and metric | Trên cùng tập test và chỉ số đánh giá

D. No, held-out evaluation is needed | Không, phải đánh giá dữ liệu giữ riêng

**Đáp án: A**

**Giải thích:** Thành phần PCA là trục đặc trưng mới, không phải nhãn. Trục PCA là tổ hợp đặc trưng ban đầu được học, không làm đổi số mẫu.

**Q18. Why fit PCA on train only? | Vì sao chỉ fit PCA trên train?**

A. Feature dimensionality while retaining sample rows | Số chiều đặc trưng nhưng giữ số hàng mẫu

B. To avoid using test distribution to learn axes | Tránh lấy phân phối test để học các trục

C. On the same held-out split and metric | Trên cùng tập test và chỉ số đánh giá

D. No, held-out evaluation is needed | Không, phải đánh giá dữ liệu giữ riêng

**Đáp án: B**

**Giải thích:** Test chỉ được transform bằng PCA đã fit từ train. Nếu không, thông tin phân phối test đã lọt vào biểu diễn đặc trưng.

**Q19. How should baseline and PCA models be compared? | So baseline và mô hình PCA thế nào?**

A. Feature dimensionality while retaining sample rows | Số chiều đặc trưng nhưng giữ số hàng mẫu

B. To avoid using test distribution to learn axes | Tránh lấy phân phối test để học các trục

C. On the same held-out split and metric | Trên cùng tập test và chỉ số đánh giá

D. No, held-out evaluation is needed | Không, phải đánh giá dữ liệu giữ riêng

**Đáp án: C**

**Giải thích:** Khác split hoặc metric không tách được ảnh hưởng của PCA. Train/test phải giống nhau giữa hai cách để chênh lệch metric phản ánh thay đổi mô hình.

**Q20. Does a high train score prove model generalization? | Train score cao có chứng minh tổng quát hóa?**

A. Feature dimensionality while retaining sample rows | Số chiều đặc trưng nhưng giữ số hàng mẫu

B. To avoid using test distribution to learn axes | Tránh lấy phân phối test để học các trục

C. On the same held-out split and metric | Trên cùng tập test và chỉ số đánh giá

D. No, held-out evaluation is needed | Không, phải đánh giá dữ liệu giữ riêng

**Đáp án: D**

**Giải thích:** Mô hình có thể nhớ train nhưng dự đoán kém trên mẫu mới. Cần báo metric test và lỗi theo lớp trước khi đánh giá khả năng ứng dụng thực tế.
