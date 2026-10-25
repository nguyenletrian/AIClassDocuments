# PY-10 — Class, Object, constructor và đóng gói


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Class** — lớp; **Object** — đối tượng.

`Hàm / Dictionary → OOP → Kế thừa`

**Học xong dùng để làm gì?** Thiết kế đối tượng học viên hoặc tài khoản với thuộc tính, phương thức và kiểm tra đầu vào.

**Kết nối kiến thức tiếp theo:** PY-11 mở rộng các loại đối tượng bằng kế thừa và ghi đè phương thức.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| Class | lớp | Khuôn mô tả dữ liệu và cách xử lý |
| Object | đối tượng | Một thể hiện cụ thể của lớp |
| Constructor | hàm khởi tạo | Thiết lập thuộc tính lúc tạo instance |
| Encapsulation | đóng gói | Đặt dữ liệu và hành vi bên trong đối tượng |

## 3. Thư viện, hàm và tham số

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm/cú pháp | Giải thích và lý do dùng |
|---|---|
| `class Name:` | Định nghĩa kiểu đối tượng và các phương thức |
| `__init__(self, ...)` | Khởi tạo trạng thái của từng instance |
| `self.attribute` | Truy cập thuộc tính thuộc về chính đối tượng |
| `__str__/set_*/get_*` | Hiển thị và kiểm tra thao tác thay đổi giá trị |


## 4. Khái niệm liên quan

**Lập trình hướng đối tượng (OOP)** giúp gom **dữ liệu của một đối tượng** và **những thao tác dùng dữ liệu ấy** vào cùng một cấu trúc. Ví dụ một học viên có tên, điểm và cách hiển thị hồ sơ; thay vì đặt các biến rời rạc, ta tạo một lớp `Student`. Từ lớp này, bài học lần lượt giải thích class, object, `__init__`, `self` và cách đóng gói thao tác thay đổi dữ liệu.

### 4.1. Class — Khuôn mẫu đối tượng

**Từ vựng trong mục:** **Class** — lớp; **Method** — phương thức.

**Class** giống bản thiết kế: định nghĩa những việc các đối tượng cùng loại có thể thực hiện. Ví dụ lớp `Student` có phương thức `greet()` trả một lời chào. Dòng `class Student:` tạo bản thiết kế, `def greet(self)` định nghĩa hành động; `self` đại diện cho đối tượng cụ thể đang gọi phương thức. Chỉ viết class chưa tạo hồ sơ học viên nào; `Student()` ở cuối mới tạo một đối tượng để gọi `greet()`.

```python
# Mục đích: Định nghĩa class Student như khuôn tạo đối tượng và gọi phương thức greet.
# Dữ liệu: class Student mô tả kiểu đối tượng; phương thức có self truy cập đối tượng hiện tại.
# class khai báo khuôn mẫu Student; Student() tạo một đối tượng mới.
class Student:
    # self tham chiếu đối tượng hiện tại; greet là phương thức của lớp.
    def greet(self):
        # return trả giá trị cho nơi gọi và kết thúc hàm.
        return 'Xin chào'

student = Student()
# Dấu chấm gọi phương thức greet() của chính instance student.
print(student.greet())
```

**Kết quả khi chạy:**

```text
Xin chào
```

Đối tượng `student` gọi phương thức được định nghĩa bên trong lớp `Student`.

### 4.2. Object — Mỗi học viên là một đối tượng

**Từ vựng trong mục:** **Object** — đối tượng; **Attribute** — thuộc tính.

**Object** là một thể hiện được tạo từ class. Cùng một mẫu `Student`, ta có thể tạo hai học viên An và Lan, mỗi người có tên riêng. Thuộc tính `self.name` lưu tên **trên từng đối tượng**, vì vậy thay tên của An không tự thay tên của Lan. Ta dùng dấu chấm `student.name` để lấy một thuộc tính.

```python
# Mục đích: Tạo hai đối tượng Student với thuộc tính name độc lập.
# Dữ liệu: a và b là hai đối tượng riêng biệt, mỗi đối tượng giữ thuộc tính name riêng.
# class định nghĩa mẫu có thuộc tính và phương thức; các instance được tạo bằng cách gọi tên lớp.
class Student:
    # __init__ chạy khi Student(name) được tạo; self là instance và name là đối số nhập.
    def __init__(self, name):
        # Thuộc tính self.name thuộc từng instance, nên hai học viên lưu tên độc lập.
        self.name = name

a = Student('An')
b = Student('Lan')
# Dấu chấm truy cập thuộc tính name của từng đối tượng.
print(a.name, b.name)
```

**Kết quả khi chạy:**

```text
An Lan
```

Cả `a` và `b` đều thuộc lớp Student, nhưng chứa dữ liệu tên riêng.

### 4.3. Constructor và self — Khởi tạo trạng thái

**Từ vựng trong mục:** **Constructor** — bước khởi tạo; **__init__** — phương thức khởi tạo; **self** — chính đối tượng.

Khi tạo `Student('An', 8)`, Python tạo đối tượng mới rồi tự gọi `__init__` để thiết lập tên và điểm ban đầu. Tham số `self` là đối tượng vừa được tạo; `name` và `score` nhận đối số truyền khi gọi. Lệnh `self.score = score` lưu điểm bên trong học viên, không chỉ trong biến tạm của hàm. Điểm ở đây tính trên thang 10.

```python
# Mục đích: Khởi tạo đối tượng Student có name và score qua __init__.
# Dữ liệu: Hàm khởi tạo nhận tên và điểm để lưu trên đúng instance.
# class định nghĩa mẫu có thuộc tính và phương thức; các instance được tạo bằng cách gọi tên lớp.
class Student:
    # __init__ nhận hai giá trị và khởi tạo trạng thái của đối tượng.
    def __init__(self, name, score):
        # Gắn tên lên thuộc tính instance self.name.
        self.name = name
        # Gắn điểm lên thuộc tính instance self.score.
        self.score = score

student = Student('An', 8)
# Đọc hai thuộc tính từ instance student.
print(student.name, student.score)
```

**Kết quả khi chạy:**

```text
An 8
```

Phương thức `__init__` đưa dữ liệu đầu vào thành hai thuộc tính của cùng hồ sơ học viên.

### 4.4. Encapsulation — Đóng gói dữ liệu và quy tắc xử lý

**Từ vựng trong mục:** **Encapsulation** — đóng gói; **Method** — phương thức; **Validation** — kiểm tra hợp lệ.

**Đóng gói** nghĩa là quản lý dữ liệu cùng các thao tác tác động lên nó trong lớp. Ví dụ điểm chỉ được phép trong khoảng 0–10: lớp `Score` lưu số hiện tại tại `self._value` và có phương thức `set_value()` kiểm tra trước khi cập nhật. Dấu `_` là **quy ước** nhắc người lập trình không nên sửa trực tiếp, không phải cơ chế cấm truy cập tuyệt đối. Đọc điểm qua `get_value()` giúp giữ cùng một cách sử dụng.

```python
# Mục đích: Đóng gói điểm trong Score, chỉ đổi qua setter có kiểm tra.
# Dữ liệu: Giá trị _value quy ước nội bộ, không phải thuộc tính private tuyệt đối.
# class định nghĩa mẫu có thuộc tính và phương thức; các instance được tạo bằng cách gọi tên lớp.
class Score:
    # __init__ tự chạy khi tạo object; self là instance hiện tại.
    def __init__(self):
        # Dấu _ quy ước thuộc tính nội bộ; khởi tạo điểm bằng 0.
        self._value = 0

    # Setter nhận điểm mới x để kiểm tra trước khi cập nhật trạng thái.
    def set_value(self, x):
        # not phủ định điều kiện 0..10; ngoài thang sẽ báo ValueError.
        if not 0 <= x <= 10:
            # raise ValueError chặn điểm sai thang và dừng setter.
            raise ValueError('Điểm ngoài khoảng 0–10')
        # Chỉ gán giá trị mới khi đã vượt qua kiểm tra.
        self._value = x

    # Getter trả điểm nội bộ, không cho bên gọi tự sửa trong phương thức.
    def get_value(self):
        # return trả giá trị cho nơi gọi và kết thúc hàm.
        return self._value

score = Score()
# Gọi setter trên đối tượng score với điểm 9.
score.set_value(9)
# Gọi getter để lấy số đã được lưu.
print(score.get_value())
```

**Kết quả khi chạy:**

```text
9
```

Điểm 9 hợp lệ nên được lưu và đọc lại. Với điểm 11, `set_value` sẽ báo `ValueError` thay vì ghi dữ liệu sai.
## 5. Năm tình huống OOP — từ đối tượng đến quản lý trạng thái

### Tình huống 1 — Cấp 1: Tạo 10 đối tượng học viên có trạng thái riêng

**Từ vựng trong mục:** **Class** — lớp; **Object** — đối tượng; **Constructor** — hàm khởi tạo.

**Tình huống thực tế:** Một lớp có **10 học viên S01 đến S10**, mỗi người có một điểm kiểm tra theo thang **10 điểm**. Giáo viên cần lưu mã và điểm gắn với đúng từng người, rồi xem điểm của S01 và S10. Họ không muốn phải tạo 10 cặp biến rời rạc dễ nhập nhầm giữa học viên này với học viên khác.

**Vì sao chọn cách này?** **OOP** (lập trình hướng đối tượng) là cách tổ chức thông tin cùng hành động của một sự vật vào một chỗ. **Class** `Student` giống một mẫu để tạo học viên, còn **object** là học viên cụ thể được tạo từ mẫu ấy. Trong `__init__`, `self.id` và `self.score` giữ mã và điểm thuộc **đúng đối tượng đang tạo**. Vì thế sửa điểm một học viên không tự làm đổi điểm học viên khác. Chương trình tạo 10 đối tượng từ các cặp mã–điểm, rồi đọc thuộc tính của S01 và S10; bài này chưa cần những kỹ thuật OOP phức tạp hơn.

**Quy trình:**
1. Định nghĩa lớp có hàm `__init__` lưu mã và điểm.
2. Tạo 10 đối tượng từ bảng điểm, mỗi hàng là một người.
3. In số đối tượng và điểm đầu/cuối.

```python
# Mục đích: Tạo 10 đối tượng Student từ dữ liệu điểm bằng vòng lặp.
# Dữ liệu: 10 điểm từng học viên; class Student chứa code và score trên từng đối tượng.
scores = [8,7,9,6,8.5,10,4,7.5,6.5,9.5]
# class định nghĩa mẫu có thuộc tính và phương thức; các instance được tạo bằng cách gọi tên lớp.
class Student:
    # Mỗi object Student nhận mã riêng và điểm riêng.
    def __init__(self, code, score):
        # self.code lưu mã trên instance.
        self.code = code
        # self.score lưu điểm trên instance.
        self.score = score

students = []
# enumerate(...,1) tạo thứ tự học viên từ 1.
for i, score in enumerate(scores, 1):
    # f-string :02d tạo mã S01..S10, sau đó tạo instance Student.
    students.append(Student(f"S{i:02d}", score))
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
if len(students) != 10:
    # raise báo lỗi rồi dừng luồng hiện tại nếu dữ liệu không đáp ứng yêu cầu.
    raise ValueError("Cần tạo đủ 10 đối tượng học viên.")
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Học viên:", len(students))
# [0] truy cập đối tượng đầu để đọc thuộc tính score.
print("S01:", students[0].score)
# [-1] truy cập đối tượng cuối.
print("S10:", students[-1].score)
```

**Kết quả khi chạy:**

```text
Học viên: 10
S01: 8
S10: 9.5
```

Thuộc tính `self.score` thuộc về từng đối tượng, không phải biến dùng chung cho toàn bộ lớp.

### Tình huống 2 — Cấp 2: Giỏ hàng có phương thức add và total cho 12 món

**Từ vựng trong mục:** **Method** — phương thức; **Self** — đối tượng hiện tại; **Encapsulation** — đóng gói.

**Tình huống thực tế:** Một khách hàng mua **12 mặt hàng**; danh sách có giá một món của từng loại, đơn vị **nghìn đồng** và mỗi loại mua một món. Thu ngân muốn lưu các món đã chọn trong một **giỏ hàng riêng** và nhờ chính giỏ ấy tính tổng số tiền, để lần sau có thể làm thêm giỏ khác mà không bị trộn giá của hai khách.

**Vì sao chọn cách này?** **Phương thức** là một hàm thuộc về đối tượng. Với `Cart`, `add()` thêm giá một món vào danh sách của giỏ, còn `total()` cộng các giá đã nằm trong chính giỏ đó. `__init__` tạo danh sách rỗng **mỗi lần tạo giỏ mới**, thay vì để mọi giỏ dùng chung một danh sách. Nếu dùng dữ liệu chung, thêm món của khách B có thể làm tổng tiền khách A tăng sai. Giữ cách tính tổng trong `Cart` giúp người dùng giỏ chỉ cần gọi `cart.total()` mà không viết phép cộng bên ngoài.

**Quy trình:**
1. Tạo lớp `Cart` với thuộc tính `prices` khởi tạo riêng.
2. Lần lượt gọi `add()` với 12 đơn giá.
3. Gọi `total()` và kiểm tra một giỏ mới không chứa hàng cũ.

```python
# Mục đích: Tạo mỗi giỏ Cart có list giá riêng và phương thức cộng tổng.
# Dữ liệu: 12 giá mặt hàng tính nghìn đồng, mỗi Cart tự có list prices.
prices = [20,30,10,15,40,25,35,20,30,10,50,45]
# class định nghĩa mẫu có thuộc tính và phương thức; các instance được tạo bằng cách gọi tên lớp.
class Cart:
    # Mỗi lần Cart() gọi __init__, tạo list prices mới riêng cho giỏ.
    def __init__(self):
        # List lưu đơn giá theo nghìn đồng của chính giỏ này.
        self.prices = []
    # Phương thức thêm một giá vào giỏ.
    def add(self, price):
        # append() thêm giá vào cuối list của instance.
        self.prices.append(price)
    # Phương thức cộng toàn bộ giá đang có.
    def total(self):
        # sum() cộng giá mỗi món trong giỏ, vẫn tính bằng nghìn đồng.
        return sum(self.prices)

cart = Cart()
for price in prices:
    # Gọi method add của giỏ hiện tại cho từng món.
    cart.add(price)
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
if len(cart.prices) != 12:
    # raise báo lỗi rồi dừng luồng hiện tại nếu dữ liệu không đáp ứng yêu cầu.
    raise ValueError("Giỏ hàng phải chứa đủ 12 món.")
# Cart() tạo giỏ mới, rồi total() phải bằng 0; kiểm không chia sẻ list giữa các object.
if Cart().total() != 0:
    # raise báo lỗi rồi dừng luồng hiện tại nếu dữ liệu không đáp ứng yêu cầu.
    raise ValueError("Giỏ hàng mới phải rỗng, không chia sẻ danh sách cũ.")
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Mặt hàng:", len(cart.prices))
print("Tổng (nghìn đồng):", cart.total())
# Cart() tạo giỏ mới, rồi total() phải bằng 0; kiểm không chia sẻ list giữa các object.
print("Giỏ mới (nghìn đồng):", Cart().total())
```

**Kết quả khi chạy:**

```text
Mặt hàng: 12
Tổng (nghìn đồng): 330
Giỏ mới (nghìn đồng): 0
```

Phương thức được gọi trên một đối tượng cụ thể; việc tạo giỏ mới không kéo theo các mặt hàng của giỏ cũ.

### Tình huống 3 — Cấp 3: Đóng gói quy tắc lưu điểm cho 15 hồ sơ

**Từ vựng trong mục:** **Setter** — phương thức gán; **Validation** — kiểm tra; **Exception** — ngoại lệ.

**Tình huống thực tế:** Phòng đào tạo tiếp nhận **15 điểm của học viên S01 đến S15**, theo thang **0 đến 10**. Trong danh sách có S06 ghi 11 và S10 ghi -1, đều ngoài thang điểm hợp lệ. Giáo viên muốn lưu điểm riêng cho từng hồ sơ, biết những mã nào không thể ghi điểm và tránh đưa điểm sai vào kết quả học tập.

**Vì sao chọn cách này?** **Đóng gói** ở đây có nghĩa là đặt quy tắc kiểm tra ngay nơi dữ liệu được thay đổi. Đối tượng `ScoreRecord` giữ điểm của một học viên; khi `set_score()` được gọi, nó kiểm tra điểm phải là số nằm từ 0 đến 10 rồi mới lưu. `ValueError` là thông báo lỗi khi giá trị nhập không được chấp nhận; chương trình xử lý lỗi theo từng học viên nên điểm sai của S06, S10 không khiến 13 hồ sơ còn lại bị bỏ qua. Không nên gán thẳng điểm sai vào thuộc tính rồi mới kiểm tra sau, vì lúc đó đối tượng đã giữ thông tin không hợp lệ.

**Quy trình:**
1. Tạo lớp với trạng thái điểm ban đầu `None`.
2. Gọi setter với mỗi trong 15 điểm, bắt lỗi cho đúng mã hồ sơ.
3. Đếm số hồ sơ lưu được và mã cần sửa.

```python
# Mục đích: Lưu 15 điểm qua object setter, bắt ngoại lệ khi điểm sai thang.
# Dữ liệu: 15 điểm thang 0..10, gồm điểm vượt thang cần báo sai.
raw_scores = [4,8,7,10,6,11,9,5,7.5,-1,0,8.5,3,9,10]
# class định nghĩa mẫu có thuộc tính và phương thức; các instance được tạo bằng cách gọi tên lớp.
class ScoreRecord:
    # __init__ tự chạy khi tạo object; self là instance hiện tại.
    def __init__(self, code):
        self.code = code
        # Điểm ban đầu chưa có, dấu _ đánh dấu thuộc tính nội bộ theo quy ước.
        self._score = None
    # Setter kiểm tra thang điểm 0..10 trước khi lưu.
    def set_score(self, value):
        # Ngoài thang 0..10 báo ValueError; cả -1 và 11 đều bị từ chối.
        if not (0 <= value <= 10):
            # raise báo lỗi rồi dừng luồng hiện tại nếu dữ liệu không đáp ứng yêu cầu.
            raise ValueError("score must be within 0..10")
        # Lưu điểm sau khi xét hợp lệ.
        self._score = value
    # Getter trả lại điểm đã lưu hoặc None nếu chưa lưu.
    def get_score(self):
        # return trả giá trị cho nơi gọi và kết thúc hàm.
        return self._score

records, errors = [], []
# enumerate(...,1) đặt mã S01..S15 theo thứ tự nhận.
for index, score in enumerate(raw_scores, 1):
    # Định dạng f-string :02d cho số thứ tự thành 2 chữ số với số 0 bổ sung.
    record = ScoreRecord(f"S{index:02d}")
    # try bắt đầu khối có thể phát sinh ValueError từ setter.
    try:
        # Gọi setter thay vì gán trực tiếp để sử dụng quy tắc kiểm tra.
        record.set_score(score)
    # except ValueError đón điểm sai và tiếp tục duyệt, không dừng toàn chương trình.
    except ValueError:
        # append() giữ mã hồ sơ sai.
        errors.append(record.code)
    # append() thêm một phần tử vào cuối danh sách và cập nhật danh sách gốc.
    records.append(record)
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
if len(records) != 15:
    # raise báo lỗi rồi dừng luồng hiện tại nếu dữ liệu không đáp ứng yêu cầu.
    raise ValueError("Cần lưu đủ 15 hồ sơ.")
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Hồ sơ:", len(records))
saved_count = 0
for rec in records:
    # is not None xác nhận có giá trị thực, khác giá trị thiếu.
    if rec.get_score() is not None:
        saved_count += 1
print("Đã lưu điểm:", saved_count)
# join() nối các chuỗi bằng ký tự phân cách, ở đây là dấu phẩy và khoảng trắng.
print("Sai:", ", ".join(errors))
```

**Kết quả khi chạy:**

```text
Hồ sơ: 15
Đã lưu điểm: 13
Sai: S06, S10
```

Điểm 0 là hợp lệ, khác với điểm chưa nhập (`None`). Cấp này thêm ràng buộc và xử lý lỗi mà không kết thúc toàn bộ lượt nhập.

### Tình huống 4 — Cấp 4: Định dạng 18 hóa đơn qua __str__ và xử lý tiền thiếu

**Từ vựng trong mục:** **Dunder method** — phương thức đặc biệt; **__str__** — chuỗi hiển thị; **Missing value** — giá trị thiếu.

**Tình huống thực tế:** Ứng dụng kế toán có **18 hóa đơn O01 đến O18**, mỗi hóa đơn cần lưu số tiền thanh toán tính bằng **đồng**. Hai hóa đơn O06 và O15 chưa được nhập tiền nên có giá trị `None`. Nhân viên muốn in hóa đơn theo mẫu dễ đọc, đồng thời báo tổng tiền của những hóa đơn đã có số và mã hai hóa đơn còn thiếu; không được hiển thị thiếu tiền như 0 đồng.

**Vì sao chọn cách này?** `__str__()` là phương thức cho biết **đối tượng được hiển thị thành dòng chữ như thế nào**, chẳng hạn khi in một hóa đơn. Còn `is_ready()` kiểm tra hóa đơn đã có số tiền để tính tổng chưa. Hai việc khác nhau: hóa đơn thiếu tiền vẫn có mã nhưng chưa đủ dữ liệu để tính doanh thu; `None` không đồng nghĩa 0 đồng. Chương trình tạo đối tượng cho 18 hóa đơn, chỉ cộng tiền của các đối tượng sẵn sàng và ghi riêng mã thiếu. Đặt quy tắc hiển thị và kiểm tra trong đối tượng giúp mọi nơi in hóa đơn theo cùng một cách.

**Quy trình:**
1. Tạo đối tượng `Invoice` cho đủ 18 dòng và lưu mã/số tiền.
2. Định nghĩa `is_ready()` và `__str__()` theo trạng thái có/thiếu tiền.
3. In hóa đơn mẫu, thống kê số hợp lệ, số thiếu và tổng giá trị.

```python
# Mục đích: Tạo 18 Invoice có cách hiển thị riêng qua __str__ và tính tổng hóa đơn hợp lệ.
# Dữ liệu: 18 khoản tiền đồng, None là hóa đơn chưa có số tiền.
amounts = [100000,125000,150000,175000,200000,None,125000,150000,175000,200000,100000,125000,150000,175000,None,100000,125000,150000]
# class định nghĩa mẫu có thuộc tính và phương thức; các instance được tạo bằng cách gọi tên lớp.
class Invoice:
    # __init__ tự chạy khi tạo object; self là instance hiện tại.
    def __init__(self, code, amount):
        # Gán đồng thời hai thuộc tính instance từ mã và tiền.
        self.code, self.amount = code, amount
    # Phương thức kiểm tra tiền hóa đơn đã là số không âm hay chưa.
    def is_ready(self):
        # isinstance() xác nhận số int/float, tránh so sánh >=0 với None.
        return isinstance(self.amount, (int, float)) and self.amount >= 0
    # __str__ quy định chuỗi khi gọi str(invoice) hoặc in object.
    def __str__(self):
        # Dùng quy tắc kiểm tra đã định nghĩa trong class trước khi định dạng.
        if self.is_ready():
            # f-string :, thêm dấu phân nhóm nghìn khi in số tiền đồng.
            value = f"{self.amount:,} đồng"
        else:
            value = "Chưa có số tiền"
        # return trả giá trị cho nơi gọi và kết thúc hàm.
        return f"{self.code}: {value}"

invoices = []
# enumerate() trả (số thứ tự, phần tử); start=1 khi truyền 1, mặc định bắt đầu 0.
for i, amount in enumerate(amounts, 1):
    # append() thêm object Invoice mới; f-string :02d tạo mã O01..O18.
    invoices.append(Invoice(f"O{i:02d}", amount))
ready = []
missing = []
for order in invoices:
    # Gọi kiểm tra hóa đơn ngay trên từng instance.
    if order.is_ready():
        # append() thêm một phần tử vào cuối danh sách và cập nhật danh sách gốc.
        ready.append(order)
    else:
        # append() thêm một phần tử vào cuối danh sách và cập nhật danh sách gốc.
        missing.append(order.code)
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
if len(invoices) != 18:
    # raise báo lỗi rồi dừng luồng hiện tại nếu dữ liệu không đáp ứng yêu cầu.
    raise ValueError("Cần đủ 18 hóa đơn.")
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Số hóa đơn:", len(invoices))
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Sẵn sàng:", len(ready))
# join() nối các chuỗi bằng ký tự phân cách, ở đây là dấu phẩy và khoảng trắng.
print("Thiếu:", ", ".join(missing))
total_amount = 0
for order in ready:
    # += cộng chỉ các hóa đơn hợp lệ, đơn vị đồng.
    total_amount += order.amount
print("Tổng (đồng):", total_amount)
# str() gọi Invoice.__str__ của phần tử đầu [0] để tạo chuỗi dễ đọc.
print("Mẫu:", str(invoices[0]))
```

**Kết quả khi chạy:**

```text
Số hóa đơn: 18
Sẵn sàng: 16
Thiếu: O06, O15
Tổng (đồng): 2325000
Mẫu: O01: 100,000 đồng
```

Chỉ tính tổng trên các đối tượng `is_ready() == True`. Giá trị `None` là một trạng thái thiếu cần sửa, không phải số tiền 0.

### Tình huống 5 — Cấp 5: Xây đối tượng tồn kho độc lập và xử lý 20 lượt xuất

**Từ vựng trong mục:** **State** — trạng thái; **Encapsulation** — đóng gói; **Instance method** — phương thức đối tượng.

**Tình huống thực tế:** Một kho có **5 loại sản phẩm P01 đến P05**, tồn đầu ngày lần lượt là **10, 9, 8, 7, 5 món**. Trong ngày có **20 lượt yêu cầu xuất hàng**; mỗi lượt chứa mã sản phẩm và số món muốn lấy. Có yêu cầu lấy quá số đang còn, một yêu cầu chưa nhập số lượng (`None`) và một yêu cầu lấy 0 món. Nhân viên cần biết yêu cầu nào bị từ chối và số tồn cuối của từng loại, bảo đảm không loại nào bị trừ xuống số âm.

**Vì sao chọn cách này?** **Trạng thái của đối tượng** là dữ liệu hiện tại được giữ bên trong nó; ở đây `StockItem` giữ số món còn của **một mã sản phẩm**. Phương thức `reserve()` kiểm tra số muốn xuất có phải lượng hợp lệ và có vượt tồn không. Chỉ khi yêu cầu được chấp nhận mới trừ vào `self.quantity`; nếu thiếu số lượng, lấy 0 món hoặc lấy nhiều hơn tồn thì từ chối và **giữ nguyên số tồn**. Cần xử lý 20 lượt **đúng thứ tự** vì sau khi xuất một lượt, số còn lại cho lượt tiếp theo đã khác. Mỗi SKU có đối tượng riêng nên xuất P01 không thể vô tình trừ tồn của P02.

**Quy trình:**
1. Khởi tạo 5 đối tượng độc lập từ tồn đầu ngày.
2. Duyệt 20 yêu cầu theo thứ tự; `reserve()` trả True/False thay vì trừ vô điều kiện.
3. Đếm số yêu cầu thành công, ghi mã lỗi và đối chiếu tồn không âm.

```python
# Mục đích: Tạo đối tượng StockItem để từ chối yêu cầu xuất kho không hợp lệ.
# Dữ liệu: initial là tồn kho 5 SKU theo món; requests gồm 20 bộ (SKU, lượng xin xuất), None/0/vượt tồn bị từ chối.
initial = {"P01":10,"P02":9,"P03":8,"P04":7,"P05":5}
requests = [("P01",2),("P02",1),("P03",3),("P01",4),("P02",5),("P03",2),("P04",1),("P01",3),("P03",6),("P04",3),("P02",2),("P01",7),("P05",1),("P03",1),("P04",4),("P05",2),("P01",None),("P02",0),("P04",2),("P05",8)]
# Mỗi instance StockItem lưu tồn của một SKU và cung cấp phương thức xuất.
class StockItem:
    # __init__ tự chạy khi tạo object; self là instance hiện tại.
    def __init__(self, code, quantity):
        # Gán mã SKU và số món hiện còn lên object.
        self.code, self.quantity = code, quantity
    # Phương thức cố gắng dành hàng, trả True nếu đủ điều kiện.
    def reserve(self, requested):
        # isinstance(...,int) loại None/kiểu sai; or loại lượng <=0 hoặc lớn hơn tồn.
        if not isinstance(requested, int) or requested <= 0 or requested > self.quantity:
            # False nghĩa yêu cầu bị từ chối, không trừ tồn.
            return False
        # -= trừ món đã cấp, chỉ sau kiểm tra an toàn.
        self.quantity -= requested
        # True báo xuất thành công.
        return True

items = {}
# items() duyệt các cặp (SKU, số lượng tồn đầu kỳ) để tạo object.
for code, qty in initial.items():
    # Dictionary ánh xạ SKU sang object giữ trạng thái tồn riêng.
    items[code] = StockItem(code, qty)
rejected = []
# enumerate(...,1) gắn số thứ tự yêu cầu 1..20.
for index, (code, requested) in enumerate(requests, 1):
    # Gọi phương thức trên đúng SKU; not tìm các lần từ chối để ghi mã.
    if not items[code].reserve(requested):
        # append() thêm một phần tử vào cuối danh sách và cập nhật danh sách gốc.
        # Định dạng f-string :02d cho số thứ tự thành 2 chữ số với số 0 bổ sung.
        rejected.append(f"T{index:02d}")
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
if len(requests) != 20:
    # raise báo lỗi rồi dừng luồng hiện tại nếu dữ liệu không đáp ứng yêu cầu.
    raise ValueError("Cần xử lý đủ 20 yêu cầu xuất kho.")
# values() lấy các giá trị dictionary, không lấy khóa.
for item in items.values():
    # Kiểm tra cuối không có số tồn âm.
    if item.quantity < 0:
        # raise báo lỗi rồi dừng luồng hiện tại nếu dữ liệu không đáp ứng yêu cầu.
        raise ValueError("Tồn kho của sản phẩm không được âm.")
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Yêu cầu:", len(requests))
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Chấp nhận:", len(requests) - len(rejected))
# join() nối các chuỗi bằng ký tự phân cách, ở đây là dấu phẩy và khoảng trắng.
print("Từ chối:", ", ".join(rejected))
stock_labels = []
# sorted() xếp các khóa SKU theo ABC trước khi in.
for code in sorted(items):
    # append() thêm một phần tử vào cuối danh sách và cập nhật danh sách gốc.
    stock_labels.append(f"{code}={items[code].quantity}")
# join() nối các chuỗi bằng ký tự phân cách, ở đây là dấu phẩy và khoảng trắng.
print("Tồn cuối:", ", ".join(stock_labels))
```

**Kết quả khi chạy:**

```text
Yêu cầu: 20
Chấp nhận: 14
Từ chối: T09, T12, T15, T17, T18, T20
Tồn cuối: P01=1, P02=1, P03=2, P04=1, P05=2
```

Người học cần theo dõi trạng thái thay đổi **qua 20 yêu cầu nối tiếp**, không chỉ tính một đơn hàng. Khi một yêu cầu bị từ chối, tồn kho phải giữ nguyên trước khi xét yêu cầu tiếp theo.

## 6. Sai lầm thường gặp

- `class` là khuôn mẫu; đối tượng chỉ xuất hiện khi gọi lớp như `Student('An', 8)`.
- `self.name` là thuộc tính của đối tượng, không phải biến dùng chung giữa mọi học viên. Mỗi đối tượng có trạng thái riêng.
- `__init__` chuẩn bị dữ liệu ban đầu, còn `__str__` quy định cách hiển thị; hai phương thức có mục đích khác nhau.
- `self._value` dùng dấu gạch dưới theo quy ước, không tự tạo thuộc tính hoàn toàn riêng tư. Muốn bảo vệ dữ liệu cần kiểm soát cách cập nhật và kiểm tra hợp lệ.
- Điểm vượt 0–10 sẽ phát sinh `ValueError` trong ví dụ `Score`; không bỏ qua xử lý lỗi ở chương trình thực tế.

## 7. Trắc nghiệm

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

## 8. Nối sang bài tiếp theo

`Hàm / Dictionary → OOP → Kế thừa`.
