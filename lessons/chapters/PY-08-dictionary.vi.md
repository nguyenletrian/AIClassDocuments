# PY-08 — Dictionary: khóa, giá trị và thêm sửa xóa


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Dictionary** — từ điển; **Key** — khóa.

`List/Set → Dictionary → JSON/CSV → DataFrame`

**Học xong dùng để làm gì?** Tra cứu hồ sơ học viên theo mã và biểu diễn bản ghi có nhiều trường bằng khóa–giá trị.

**Kết nối kiến thức tiếp theo:** PY-09 viết hàm tái sử dụng các bước xử lý những bản ghi đó.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích dễ nhớ |
|---|---|---|
| Dictionary | từ điển | Ánh xạ khóa sang giá trị |
| Key | khóa | Tên hoặc mã để truy tìm giá trị |
| Value | giá trị | Thông tin được lưu theo một khóa |
| Nested dict | từ điển lồng | Một từ điển có từ điển con |

## 3. Hàm và cú pháp Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cú pháp | Mục đích và lựa chọn liên quan |
|---|---|
| `obj[key], obj.get(key)` | Tra cứu khóa hoặc nhận giá trị mặc định |
| `obj.items(), obj.values()` | Duyệt cặp khóa/giá trị hay riêng giá trị |
| `obj[key] = value` | Thêm hoặc cập nhật dữ liệu |
| `del, pop(key)` | Xóa thông tin bằng khóa |

## 4. Khái niệm liên quan

List lấy dữ liệu theo **vị trí**, còn **Dictionary** lấy theo **khóa có ý nghĩa** như mã đơn hàng hoặc tên trường. Mỗi khóa gắn với một giá trị để tra cứu, thêm, sửa hoặc xóa thông tin. Bài dùng hồ sơ đơn hàng làm ví dụ xuyên suốt, từ một mã đơn đơn giản tới hồ sơ có nhiều thuộc tính.

### 4.1. Dictionary — Dữ liệu dạng khóa và giá trị

**Từ vựng trong mục:** **Dictionary** — từ điển; **Key–value pair** — cặp khóa–giá trị.

Một cửa hàng lưu đơn hàng mã `O1` có trạng thái `paid` (đã thanh toán). Trong Dictionary `order = {'id': 'O1', 'status': 'paid'}`, **`id` và `status` là hai khóa**; `O1` và `paid` là các giá trị tương ứng. Dấu `{}` bao các cặp `khóa: giá trị`. Dùng Dictionary khi cần đọc thông tin theo tên trường thay vì phải nhớ chỉ số trong List.

```python
# Mục đích: Tạo dictionary lưu trạng thái đơn theo khóa và giá trị.
# Dữ liệu: Khóa id là mã đơn và status là chuỗi trạng thái.
# Dictionary dùng khóa dạng chuỗi để truy cập giá trị tương ứng.
order = {'id': 'O1', 'status': 'paid'}
print(order)
```

**Kết quả khi chạy:**

```text
{'id': 'O1', 'status': 'paid'}
```

Một đơn hàng có hai trường. Mỗi cặp khóa–giá trị mô tả một thông tin riêng.

### 4.2. Key — Khóa để tra cứu

**Từ vựng trong mục:** **Key** — khóa; **Lookup** — tra cứu.

Khóa là tên hoặc mã duy nhất **trong cùng một Dictionary**, được dùng để lấy giá trị đúng trường. Với hồ sơ `order`, biểu thức `order['id']` lấy mã O1; còn `order['status']` lấy trạng thái. Nếu dùng dấu `[]` với khóa không tồn tại, Python báo `KeyError`; có thể dùng `get()` khi cần giá trị mặc định.

```python
# Mục đích: Tra cứu mã đơn trực tiếp theo khóa id.
# Dữ liệu: Dictionary có hai khóa id/status; truy cập qua tên khóa, không phải chỉ số.
order = {'id': 'O1', 'status': 'paid'}
# ['id'] tra đúng khóa id và lấy giá trị O1; khóa không có sẽ gây KeyError.
print(order['id'])
```

**Kết quả khi chạy:**

```text
O1
```

Python tra theo khóa `id`; không cần duyệt qua các trường bằng vòng lặp.

### 4.3. Value và thao tác thêm, sửa, xóa

**Từ vựng trong mục:** **Value** — giá trị; **Update** — cập nhật.

**Giá trị** là dữ liệu gắn với từng khóa; có thể là chuỗi, số, List hoặc Dictionary khác. Ví dụ đơn `O1` đang có trạng thái `pending` (đang chờ). Lệnh `order['status'] = 'paid'` **sửa** giá trị của khóa đã có. Lệnh `order['amount'] = 100` **thêm** trường số tiền mới; `order.pop('amount')` **xóa** trường ấy. Trong bài này, ta in Dictionary trước và sau khi xóa để nhìn thấy thay đổi; nếu xóa khóa không tồn tại mà không truyền giá trị mặc định cho `pop`, Python báo `KeyError`.

```python
# Mục đích: Thêm, sửa và xóa một mục dữ liệu trong dictionary.
# Dữ liệu: Cùng một khóa status bị ghi đè; khóa amount mới được thêm, rồi xóa.
order = {'id': 'O1', 'status': 'pending'}
# Gán lại giá trị cho khóa tồn tại status từ pending thành paid.
order['status'] = 'paid'
# Gán cho khóa mới amount để thêm một trường vào dictionary.
order['amount'] = 100
print(order)
# pop('amount') lấy ra và xóa khóa amount, làm dictionary chỉ còn các khóa khác.
order.pop('amount')
print(order)
```

**Kết quả khi chạy:**

```text
{'id': 'O1', 'status': 'paid', 'amount': 100}
{'id': 'O1', 'status': 'paid'}
```

Dòng đầu có thêm trường `amount` giá trị 100; dòng thứ hai không còn trường này sau `pop()`. Mã đơn O1 và trạng thái `paid` vẫn giữ nguyên.

### 4.4. Nested dictionary — Hồ sơ có thông tin con

**Từ vựng trong mục:** **Nested dictionary** — từ điển lồng; **Field** — trường dữ liệu.

Nếu quản lý nhiều đơn hàng, ta có thể dùng **Dictionary ngoài** với khóa là mã đơn (`O1`, `O2`), và **Dictionary trong** lưu thông tin riêng như `status`, `amount`. Khi cần lấy số tiền đơn `O2`, tra trước `orders['O2']` để lấy hồ sơ con, sau đó tra `['amount']`. Cách này giữ các thuộc tính của từng đơn bên nhau.

```python
# Mục đích: Đọc số tiền ở dictionary con của đơn O2.
# Dữ liệu: Mỗi mã đơn ánh xạ sang một dictionary con có status và amount.
orders = {
    'O1': {'status': 'paid', 'amount': 100},
    'O2': {'status': 'pending', 'amount': 200},
}
# Truy cập hai tầng: lấy dict của mã O2 rồi lấy khóa amount, giá trị 200.
print(orders['O2']['amount'])
```

**Kết quả khi chạy:**

```text
200
```

Kết quả `200` là số tiền của đơn O2 (đơn vị tiền theo quy định của cửa hàng), không phải mã đơn hay chỉ số dòng.
## 5. Năm tình huống Dictionary — từ tra cứu đến nhập/xuất có kiểm chứng

### Tình huống 1 — Cấp 1: Tra cứu 10 đơn không phát sinh KeyError

**Từ vựng trong mục:** **Dictionary** — từ điển; **Key** — khóa; **Get** — tra cứu.

**Tình huống thực tế:** Một cửa hàng quản lý **10 đơn hàng O01 đến O10**. Mỗi mã gắn với một trạng thái: `paid` nghĩa là đã trả tiền, `pending` đang chờ và `cancelled` đã hủy. Nhân viên cần xem trạng thái O04, thử tra O11 là mã chưa có trong bảng, rồi đếm số đơn đã thanh toán; việc tra mã lạ không được làm cả báo cáo dừng lại.

**Vì sao chọn cách này?** **Dictionary** là bảng ghép **khóa** với **giá trị**: ở đây khóa là mã đơn O01, O02..., giá trị là trạng thái thanh toán. Từ mã có thể tra đúng trạng thái mà không cần dò từng hàng. `orders.get('O11', 'unknown')` trả về giá trị dự phòng khi mã chưa có, nên chương trình không bị lỗi `KeyError`. Truy cập thẳng `orders['O11']` chỉ phù hợp khi chắc chắn khóa tồn tại; trường hợp này không chắc. Muốn đếm đơn `paid`, duyệt các trạng thái và tăng bộ đếm chỉ khi trạng thái bằng `paid`.

**Quy trình:**
1. Tạo Dictionary 10 mã và trạng thái.
2. Tra cứu O04 và O11 bằng `get`.
3. Đếm trạng thái paid và kiểm tra số khóa.

```python
# Mục đích: Tra trạng thái 10 đơn, kể cả mã không có, và đếm đã thanh toán.
# Dữ liệu: 10 mã đơn có các trạng thái paid/pending/cancelled.
orders = {"O01":"paid","O02":"pending","O03":"paid","O04":"cancelled","O05":"pending","O06":"paid","O07":"pending","O08":"paid","O09":"cancelled","O10":"paid"}
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
if len(orders) != 10:
    # raise báo lỗi rồi dừng luồng hiện tại nếu dữ liệu không đáp ứng yêu cầu.
    raise ValueError("Cần đủ 10 đơn hàng.")
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Số đơn:", len(orders))
# dict.get(khóa, mặc_định) đọc giá trị; nếu thiếu khóa trả 'Not found' thay vì KeyError.
print("O04:", orders.get("O04", "Not found"))
# dict.get(khóa, mặc_định) đọc giá trị; nếu thiếu khóa trả 'Not found' thay vì KeyError.
print("O11:", orders.get("O11", "Not found"))
paid_count = 0
# values() lấy toàn bộ trạng thái đơn để duyệt; không lấy mã khóa.
for value in orders.values():
    # == so với chuỗi paid để đếm đơn đã trả.
    if value == "paid":
        paid_count += 1
print("Đã trả:", paid_count)
```

**Kết quả khi chạy:**

```text
Số đơn: 10
O04: cancelled
O11: Not found
Đã trả: 5
```

O11 không có khóa trong bảng, nên `Not found` là thông báo tra cứu, không phải một trạng thái đơn hàng thật.

### Tình huống 2 — Cấp 2: Cập nhật tồn của 12 SKU theo số đã bán

**Từ vựng trong mục:** **Key-value** — cặp khóa–giá trị; **Update** — cập nhật.

**Tình huống thực tế:** Kho có **12 loại hàng P01 đến P12**. Với mỗi mã, bảng ghi số món đang còn và số món vừa bán; các con số đều là **số lượng món**, không phải tiền. Nhân viên muốn trừ đúng lượng đã bán ở từng mã, báo tồn cuối của P05 và tổng số món còn lại trên cả 12 mã. Nếu ai đó bán nhiều hơn tồn thì không được tạo số tồn âm.

**Vì sao chọn cách này?** **SKU** là mã nhận biết một loại hàng, chẳng hạn P05. Dictionary lưu tồn kho theo khóa là SKU, nên `stock[sku]` luôn tham chiếu đúng loại hàng đó. Với mỗi lượt bán, trước tiên kiểm tra số món có đủ không; nếu đủ mới trừ và lưu tồn còn lại. Dấu `-=` nghĩa là lấy giá trị đang có trừ số đã bán rồi cập nhật lại cùng khóa. Nếu trừ mà không kiểm tra, một loại có thể còn -2 món, vốn không phải tồn kho thực tế. Sau khi xử lý, cộng tồn của 12 khóa và đọc riêng khóa P05.

**Quy trình:**
1. Khởi tạo 12 mã và số tồn đầu ngày.
2. Duyệt đúng cặp mã–số bán; kiểm tra rồi trừ vào từng khóa.
3. In số SKU, tồn tổng cộng, số tồn P05.

```python
# Mục đích: Theo dõi tồn kho 12 SKU từ số đầu kỳ và số đã bán.
# Dữ liệu: 12 tồn đầu kỳ và 12 lượng bán (món), các phần tử cùng vị trí thuộc một SKU.
starting = [10,8,12,5,20,9,13,6,7,11,14,4]
sold = [2,1,3,0,4,1,2,2,1,3,4,0]
stock = {}
# enumerate(...,1) đặt mã SKU P01..P12 tương ứng từng số tồn.
for i, amount in enumerate(starting, 1):
    # Định dạng f-string :02d cho số thứ tự thành 2 chữ số với số 0 bổ sung.
    sku = f"P{i:02d}"
    # Dictionary stock ánh xạ mã SKU thành số món đầu kỳ.
    stock[sku] = amount
# Duyệt lượng bán cùng thứ tự mã P01..P12.
for i, quantity in enumerate(sold, 1):
    # Định dạng f-string :02d cho số thứ tự thành 2 chữ số với số 0 bổ sung.
    sku = f"P{i:02d}"
    # Không trừ lượng bán vượt số tồn hiện tại, tránh âm kho.
    if quantity > stock[sku]:
        # raise báo lỗi rồi dừng luồng hiện tại nếu dữ liệu không đáp ứng yêu cầu.
        raise ValueError(f"SKU {sku}: số bán vượt quá tồn kho.")
    # -= trừ số bán khỏi lượng hàng của SKU tương ứng.
    stock[sku] -= quantity
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
if len(stock) != 12:
    # raise báo lỗi rồi dừng luồng hiện tại nếu dữ liệu không đáp ứng yêu cầu.
    raise ValueError("Cần đủ 12 mã sản phẩm trong kho.")
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("SKU:", len(stock))
# values() trả các lượng tồn sau bán; sum() cộng thành tổng món còn.
print("Tồn tổng:", sum(stock.values()))
print("P05 còn:", stock["P05"])
```

**Kết quả khi chạy:**

```text
SKU: 12
Tồn tổng: 96
P05 còn: 16
```

Dictionary được cập nhật theo mã thay vì dựa vào vị trí số khi xử lý các lần nhập dữ liệu sau.

### Tình huống 3 — Cấp 3: Đếm 15 nhãn và xếp thứ hạng bằng Dictionary

**Từ vựng trong mục:** **Frequency** — tần suất; **Items** — cặp khóa và giá trị; **Ranking** — xếp hạng.

**Tình huống thực tế:** Trung tâm nhận **15 yêu cầu học tập**, mỗi lượt được gắn một nhãn môn trong các môn **AI, Python, SQL và Math**. Người điều phối muốn biết mỗi môn được yêu cầu bao nhiêu lượt và hai môn phổ biến nhất. Nếu hai môn bằng số lượt thì xếp theo tên môn để báo cáo luôn có thứ tự giống nhau.

**Vì sao chọn cách này?** **Đếm tần suất** nghĩa là tính một nhãn xuất hiện bao nhiêu lần. Dictionary `counts` ghi số lượt theo tên nhãn; `get(label, 0)` lấy số đếm cũ hoặc 0 nếu chưa thấy môn đó, rồi cộng 1 cho lượt mới. Nhờ vậy, 15 lượt được đếm đủ mà không phải chuẩn bị riêng biến cho từng môn. Để chọn hai môn phổ biến nhất, sắp các cặp `(tên môn, số lượt)` theo số lượt **giảm dần**, nếu bằng nhau theo tên môn **tăng dần**; chỉ lấy hai cặp đầu. Không lấy nhãn xuất hiện đầu tiên vì thứ tự tiếp nhận không cho biết môn phổ biến.

**Quy trình:**
1. Tạo Dictionary đếm ban đầu rỗng.
2. Duyệt 15 nhãn, tăng bộ đếm theo khóa.
3. Sắp danh sách cặp số đếm và in hai nhãn đứng đầu.

```python
# Mục đích: Đếm 15 nhãn trong dictionary và xếp loại theo tần suất.
# Dữ liệu: 15 tên nhãn với các loại AI/Python/SQL/Math.
labels = ["AI","Python","SQL","AI","Math","Python","AI","SQL","Python","Math","SQL","AI","Python","Math","AI"]
counts = {}
for label in labels:
    # get(label,0) đọc bộ đếm hiện tại hoặc 0 nếu nhãn mới; +1 ghi nhận thêm một lượt.
    counts[label] = counts.get(label, 0) + 1
# Hàm key quyết định thứ tự xếp một cặp (tên nhãn, số lần).
def ranking_key(item):
    # item[1] là số lần: đổi âm để xếp nhiều trước; item[0] là tên để phá hòa theo ABC.
    return (-item[1], item[0])
# items() lấy các cặp (nhãn, số); sorted(...,key=...) dùng khóa tùy chỉnh, tạo list mới.
ranking = sorted(counts.items(), key=ranking_key)
# values() lấy các giá trị dictionary, không lấy khóa.
# sum() cộng tất cả số trong đối tượng được đưa vào.
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
if len(labels) != 15 or sum(counts.values()) != 15:
    # raise báo lỗi rồi dừng luồng hiện tại nếu dữ liệu không đáp ứng yêu cầu.
    raise ValueError("Cần đối chiếu đủ 15 nhãn được đếm.")
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Lượt:", len(labels))
count_labels = []
# sorted(counts) sắp xếp tên khóa để bảng số đếm nhất quán.
for name in sorted(counts):
    # append() thêm một phần tử vào cuối danh sách và cập nhật danh sách gốc.
    count_labels.append(f"{name}={counts[name]}")
top_names = []
# [:2] lấy hai nhãn có thứ hạng cao nhất.
for name, count in ranking[:2]:
    # append() thêm một phần tử vào cuối danh sách và cập nhật danh sách gốc.
    top_names.append(name)
# join() nối các chuỗi bằng ký tự phân cách, ở đây là dấu phẩy và khoảng trắng.
print("Đếm:", ", ".join(count_labels))
# join() nối các chuỗi bằng ký tự phân cách, ở đây là dấu phẩy và khoảng trắng.
print("Top 2:", ", ".join(top_names))
```

**Kết quả khi chạy:**

```text
Lượt: 15
Đếm: AI=5, Math=3, Python=4, SQL=3
Top 2: AI, Python
```

Mỗi nhãn là một khóa. Việc có hai nhãn cùng tần suất chỉ ảnh hưởng thứ tự in; số đếm từng nhãn vẫn phải đúng.

### Tình huống 4 — Cấp 4: Kiểm tra 18 hồ sơ học viên lồng nhau

**Từ vựng trong mục:** **Nested dictionary** — Dictionary lồng nhau; **Missing** — thiếu điểm; **Validation** — kiểm tra hợp lệ.

**Tình huống thực tế:** Phòng đào tạo có **18 hồ sơ S01 đến S18**. Mỗi hồ sơ gồm mã, tên giả lập và điểm của học viên trên thang **0 đến 10**. Hai học viên chưa được nhập điểm nên để `None`; một học viên có điểm 11 là sai thang. Giáo vụ cần đếm riêng số hồ sơ có điểm hợp lệ, số chưa có điểm và số nhập sai, mà không dừng khi gặp dữ liệu thiếu.

**Vì sao chọn cách này?** Một hồ sơ có nhiều thông tin đi với cùng mã học viên nên lưu thành **dictionary bên trong dictionary**: tìm đúng mã trước rồi mới đọc trường điểm. `None` nghĩa là chưa nhập điểm, khác với 0 điểm là bài làm đã có kết quả. Chương trình phải kiểm tra `None` trước khi so với khoảng 0–10, vì không thể so sánh trực tiếp số với `None`. Điểm 11 phải đếm vào nhóm sai chứ không cho vào nhóm hợp lệ hay tự sửa thành 10. Cuối cùng ba nhóm hợp lệ, thiếu và sai phải khớp tổng 18 hồ sơ.

**Quy trình:**
1. Tạo 18 mã và các thuộc tính có ý nghĩa.
2. Kiểm tra giá trị thiếu trước, sau đó kiểm tra khoảng điểm hợp lệ.
3. Thống kê ba nhóm và xác minh tổng số hồ sơ.

```python
# Mục đích: Phân loại 18 hồ sơ học viên thành điểm hợp lệ, thiếu và ngoài thang.
# Dữ liệu: 18 điểm học viên, None là thiếu; điểm hợp lệ thuộc đoạn 0..10.
scores = [8,7,9,None,6.5,10,4,7.5,8.5,9,5,6,8,11,7,None,4.5,9]
students = {}
# enumerate(...,1) gán mã S01..S18 theo thứ tự điểm.
for i, value in enumerate(scores, 1):
    # Định dạng f-string :02d cho số thứ tự thành 2 chữ số với số 0 bổ sung.
    student_code = f"S{i:02d}"
    # Dictionary con lưu hai trường name và score của từng học viên.
    students[student_code] = {"name": f"Học viên {i:02d}", "score": value}
valid, missing, invalid = [], [], []
# items() duyệt từng cặp (mã học viên, hồ sơ dict).
for code, info in students.items():
    score = info["score"]
    # is None nhận diện điểm chưa có, không nhầm với số 0.
    if score is None:
        # append() lưu mã chưa có điểm.
        missing.append(code)
    # Chuỗi so sánh kiểm tra ngoài khoảng 0..10, kể cả điểm 11.
    elif not (0 <= score <= 10):
        # append() lưu mã điểm hợp lệ.
        # append() lưu mã điểm ngoài thang.
        invalid.append(code)
    else:
        # append() lưu mã điểm hợp lệ.
        valid.append(code)
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
if len(students) != 18 or len(valid) + len(missing) + len(invalid) != 18:
    # raise báo lỗi rồi dừng luồng hiện tại nếu dữ liệu không đáp ứng yêu cầu.
    raise ValueError("Cần phân loại đủ 18 hồ sơ học viên.")
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Hồ sơ:", len(students))
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Hợp lệ:", len(valid))
# join() nối các chuỗi bằng ký tự phân cách, ở đây là dấu phẩy và khoảng trắng.
print("Thiếu:", ", ".join(missing))
# join() nối các chuỗi bằng ký tự phân cách, ở đây là dấu phẩy và khoảng trắng.
print("Sai thang:", ", ".join(invalid))
```

**Kết quả khi chạy:**

```text
Hồ sơ: 18
Hợp lệ: 15
Thiếu: S04, S16
Sai thang: S14
```

Một giá trị 11 không phải thiếu nhưng vẫn không hợp lệ. Hai nguyên nhân cần được phân biệt để hướng dẫn nhân viên sửa đúng hồ sơ.

### Tình huống 5 — Cấp 5: Xử lý 20 giao dịch nhập/xuất kho có kiểm chứng

**Từ vựng trong mục:** **CRUD** — thêm/đọc/sửa/xóa; **Dictionary get** — tra cứu mặc định; **Transaction** — giao dịch.

**Tình huống thực tế:** Một cửa hàng ghi lại **20 giao dịch kho** theo đúng thứ tự xảy ra. Mỗi dòng có mã sản phẩm, thao tác `add` (nhập thêm) hoặc `sell` (bán/xuất), và số món muốn nhập hoặc xuất. Có lượt bán vượt số lượng hiện có, lượt bán một mã chưa từng nhập và lượt thiếu số món. Người quản lý muốn biết giao dịch nào được chấp nhận hay bị từ chối, tổng số lần thành công/thất bại và tồn cuối của từng loại hàng.

**Vì sao chọn cách này?** Tồn kho là **trạng thái thay đổi theo từng giao dịch**, vì thế thứ tự 20 lượt rất quan trọng: một lượt nhập trước có thể giúp lượt bán sau đủ hàng. Dictionary giữ số món hiện tại của mỗi mã. Với `add`, kiểm tra mã và lượng nhập rồi cộng; với `sell`, chỉ trừ khi mã đã có và còn đủ món. Dòng thiếu số lượng, bán SKU chưa tồn tại hay bán quá số tồn đều bị **từ chối và không làm thay đổi kho**. Sau mỗi lượt tăng bộ đếm thành công hoặc thất bại, rồi đọc dictionary để có tồn cuối. Không thể cộng tất cả lượt nhập rồi trừ tất cả lượt bán trước, vì cách đó bỏ qua những giao dịch bị từ chối ở thời điểm chúng xảy ra.

**Quy trình:**
1. Khởi tạo kho rỗng, duyệt lần lượt 20 tuple giao dịch.
2. Với nhập, cộng tồn; với xuất, kiểm tra số dương, SKU tồn tại và đủ số món.
3. Ghi lại số thứ tự giao dịch lỗi, đối chiếu số lượt và in bảng tồn đã sắp mã.

```python
# Mục đích: Áp dụng 20 giao dịch kho qua dictionary, từ chối giao dịch sai.
# Dữ liệu: 20 tuple (SKU, hành động add/sell, số lượng), None nghĩa chưa có số lượng.
events = [("P01","add",12),("P02","add",9),("P03","add",8),("P01","sell",2),("P02","sell",3),("P04","add",5),("P05","add",7),("P03","sell",1),("P01","sell",20),("P06","add",15),("P04","sell",2),("P02","sell",1),("P07","add",4),("P05","sell",2),("P08","add",6),("P03","sell",3),("P02","add",5),("P09","sell",1),("P06","sell",4),("P07","sell",None)]
stock, rejected = {}, []
# enumerate(...,1) đánh số giao dịch kho 1..20 để báo dòng lỗi.
for index, (sku, action, quantity) in enumerate(events, 1):
    # or từ chối số lượng thiếu hoặc không dương ngay từ đầu.
    if quantity is None or quantity <= 0:
        # append() lưu số thứ tự giao dịch từ chối.
        rejected.append(index)
    # Nhánh add tăng tồn kho của SKU.
    elif action == "add":
        # get(sku,0) lấy tồn hiện có hoặc 0 khi SKU mới, rồi cộng số nhập.
        stock[sku] = stock.get(sku, 0) + quantity
    # and buộc hành động sell, SKU đã tồn tại và lượng kho đủ xuất.
    elif action == "sell" and sku in stock and stock[sku] >= quantity:
        # -= giảm tồn của chính SKU sau khi kiểm đủ.
        stock[sku] -= quantity
    else:
        # append() lưu số thứ tự giao dịch từ chối.
        rejected.append(index)
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
if len(events) != 20:
    # raise báo lỗi rồi dừng luồng hiện tại nếu dữ liệu không đáp ứng yêu cầu.
    raise ValueError("Cần kiểm tra đủ 20 giao dịch kho.")
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Giao dịch:", len(events))
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Đã nhận:", len(events) - len(rejected))
rejected_labels = []
for index in rejected:
    # str() chuyển số thứ tự giao dịch thành chuỗi cho join().
    rejected_labels.append(str(index))
stock_labels = []
# sorted(stock) xếp tên các SKU trước khi in.
for sku in sorted(stock):
    # append() thêm một phần tử vào cuối danh sách và cập nhật danh sách gốc.
    stock_labels.append(f"{sku}={stock[sku]}")
# join() nối các chuỗi bằng ký tự phân cách, ở đây là dấu phẩy và khoảng trắng.
print("Từ chối lượt:", ", ".join(rejected_labels))
# join() nối các chuỗi bằng ký tự phân cách, ở đây là dấu phẩy và khoảng trắng.
print("Tồn cuối:", ", ".join(stock_labels))
```

**Kết quả khi chạy:**

```text
Giao dịch: 20
Đã nhận: 17
Từ chối lượt: 9, 18, 20
Tồn cuối: P01=10, P02=10, P03=4, P04=3, P05=5, P06=11, P07=4, P08=6
```

Phiếu bị từ chối giữ nguyên số tồn trước đó. Không được âm thầm tạo SKU P09 tồn 0 rồi trừ thành -1, vì kho chưa hề nhận mặt hàng này.

## 6. Nhầm lẫn dễ gặp

- `obj[key]` gây `KeyError` nếu khóa chưa tồn tại; `obj.get(key)` trả về `None` hoặc giá trị mặc định đã truyền vào.
- Gán `obj[key] = value` sẽ thêm khóa mới hoặc ghi đè giá trị đang có.
- `pop(key)` lấy và xóa giá trị; nếu khóa không tồn tại, nên truyền giá trị mặc định khi phù hợp.
- Khóa Dictionary phải là kiểu có thể băm (hashable), như chuỗi hoặc số; không dùng List làm khóa.

## 7. Trắc nghiệm

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

## 8. Nối sang bài tiếp theo

`List/Set → Dictionary → JSON/CSV → DataFrame`.
