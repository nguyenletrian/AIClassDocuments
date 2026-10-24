# PY-08 — Dictionary: khóa, giá trị và thêm sửa xóa


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Dictionary** — từ điển; **Key** — khóa.

`List/Set → Dictionary → JSON/CSV → DataFrame`

Sau List, Tuple và Set, ta học Dictionary để tìm thông tin qua một tên hoặc mã riêng. Thay vì nhớ số thứ tự, ta lấy thông tin theo khóa như `id`, `name` hoặc mã sản phẩm.

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
order = {'id': 'O1', 'status': 'paid'}
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
order = {'id': 'O1', 'status': 'pending'}
order['status'] = 'paid'
order['amount'] = 100
print(order)
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
orders = {
    'O1': {'status': 'paid', 'amount': 100},
    'O2': {'status': 'pending', 'amount': 200},
}
print(orders['O2']['amount'])
```

**Kết quả khi chạy:**

```text
200
```

Kết quả `200` là số tiền của đơn O2 (đơn vị tiền theo quy định của cửa hàng), không phải mã đơn hay chỉ số dòng.
## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Tra cứu đơn theo mã

**Từ vựng trong mục:** **Dictionary** — từ điển; **Key** — khóa.

**Tình huống thực tế:** Cửa hàng đang lưu trạng thái hai đơn hàng: `O1` đã thanh toán (`paid`) và `O2` đang chờ (`pending`). Khách nhập mã `O3`, chưa có trong hệ thống.

**Yêu cầu:** Tra cứu mã `O3` và in thông báo nếu không tìm thấy.

**Vì sao chọn cách giải này?** `get(key, default)` tìm theo mã đơn và trả về `Not found` khi khóa chưa tồn tại, thay vì phát sinh `KeyError`.

**Quy trình giải:**

1. Lưu trạng thái đơn theo từng mã.
2. Tra `O3` bằng `get()` và truyền vào câu báo `Not found`.
3. In kết quả.

```python
orders={"O1":"paid","O2":"pending"}
print(orders.get("O3","Not found"))
```

**Kết quả khi chạy:**

```text
Not found
```

**Kết quả:** `Not found` — không có mã đơn `O3` trong dữ liệu.

### Tình huống 2 — Cập nhật tồn kho

**Từ vựng trong mục:** **Key** — khóa; **Value** — giá trị.

**Tình huống thực tế:** Kho có sản phẩm mã `SKU01` với 5 món. Sau khi bán 2 món, nhân viên cần cập nhật số lượng còn lại.

**Yêu cầu:** Trừ 2 khỏi tồn kho của `SKU01` rồi in Dictionary.

**Vì sao chọn cách giải này?** Mã SKU là khóa của sản phẩm; `stock['SKU01'] -= 2` thay đổi số lượng ngay tại khóa tương ứng.

**Quy trình giải:**

1. Lưu số lượng ban đầu theo mã SKU.
2. Lấy số lượng ở khóa `SKU01` và trừ 2.
3. In tồn kho đã cập nhật.

```python
stock={"SKU01":5}
stock["SKU01"]-=2
print(stock)
```

**Kết quả khi chạy:**

```text
{'SKU01': 3}
```

**Kết quả:** `{'SKU01': 3}` — sản phẩm còn 3 món.

### Tình huống 3 — Đếm nhãn

**Từ vựng trong mục:** **Dictionary** — từ điển; **Count** — số lần.

**Tình huống thực tế:** Một hệ thống phân loại ghi ba nhãn theo thứ tự `AI`, `Math`, `AI`. Người quản lý muốn biết mỗi nhãn xuất hiện bao nhiêu lần.

**Yêu cầu:** Tạo Dictionary đếm số lượt của từng nhãn.

**Vì sao chọn cách giải này?** `get(x, 0)` lấy số đếm cũ hoặc 0 nếu nhãn mới xuất hiện, sau đó cộng thêm 1.

**Quy trình giải:**

1. Tạo list nhãn và Dictionary `count` rỗng.
2. Duyệt từng nhãn bằng `for`.
3. Tăng bộ đếm của nhãn và in kết quả.

```python
labels=["AI","Math","AI"]
count={}
for x in labels:
    count[x]=count.get(x,0)+1
print(count)
```

**Kết quả khi chạy:**

```text
{'AI': 2, 'Math': 1}
```

**Kết quả:** `{'AI': 2, 'Math': 1}` — AI xuất hiện hai lần, Math một lần.

### Tình huống 4 — Hồ sơ lồng nhau

**Từ vựng trong mục:** **Nested dict** — từ điển lồng; **Key** — khóa.

**Tình huống thực tế:** Trung tâm có hồ sơ `SV1` tên An, điểm 8 và `SV2` tên Lan, điểm 9. Hồ sơ lưu theo mã sinh viên, bên trong chứa tên và điểm.

**Yêu cầu:** Lấy điểm của `SV2` và in kết quả.

**Vì sao chọn cách giải này?** Dictionary lồng nhau giúp tìm sinh viên bằng mã rồi lấy đúng trường `score` của người đó.

**Quy trình giải:**

1. Lưu hai hồ sơ trong `students`.
2. Chọn sinh viên bằng khóa `SV2`.
3. Lấy khóa `score` trong hồ sơ con và in điểm.

```python
students={"SV1":{"name":"An","score":8},"SV2":{"name":"Lan","score":9}}
print(students["SV2"]["score"])
```

**Kết quả khi chạy:**

```text
9
```

**Kết quả:** `9` — điểm của học viên Lan (`SV2`).

### Tình huống 5 — Xóa SKU không có

**Từ vựng trong mục:** **Dictionary** — từ điển; **Pop** — lấy và xóa.

**Tình huống thực tế:** Kho đang có sản phẩm `P01` với 10 món. Nhân viên muốn xóa mã `P02`, nhưng mã này không có trong Dictionary.

**Yêu cầu:** Thử xóa `P02` và in kết quả thao tác, không làm chương trình lỗi.

**Vì sao chọn cách giải này?** `pop('P02', None)` trả về `None` nếu không có mã, thay vì gây `KeyError`. Không có phần tử nào bị xóa.

**Quy trình giải:**

1. Lưu mã hàng đang có.
2. Gọi `pop()` với mã `P02` và giá trị mặc định `None`.
3. In biến `removed`.

```python
items={"P01":10}
removed=items.pop("P02",None)
print(removed)
```

**Kết quả khi chạy:**

```text
None
```

**Kết quả:** `None` — không có mã `P02` để xóa; `P01` vẫn còn trong Dictionary.

## 6. Nhầm lẫn dễ gặp

- `obj[key]` gây `KeyError` nếu khóa chưa tồn tại; `obj.get(key)` trả về `None` hoặc giá trị mặc định đã truyền vào.
- Gán `obj[key] = value` sẽ thêm khóa mới hoặc ghi đè giá trị đang có.
- `pop(key)` lấy và xóa giá trị; nếu khóa không tồn tại, nên truyền giá trị mặc định khi phù hợp.
- Khóa Dictionary phải là kiểu có thể băm (hashable), như chuỗi hoặc số; không dùng List làm khóa.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a dictionary? — Dictionary là gì?**

A. A mapping from keys to values — Ánh xạ từ khóa sang giá trị

B. Identifies a value for lookup — Xác định giá trị để tra cứu

C. Data associated with a key — Dữ liệu gắn với một khóa

D. A dictionary holding another dictionary — Dictionary chứa một Dictionary khác

**Q2. What does a dictionary key do? — Khóa Dictionary có vai trò gì?**

A. A mapping from keys to values — Ánh xạ từ khóa sang giá trị

B. Identifies a value for lookup — Xác định giá trị để tra cứu

C. Data associated with a key — Dữ liệu gắn với một khóa

D. A dictionary holding another dictionary — Dictionary chứa một Dictionary khác

**Q3. What is a dictionary value? — Giá trị Dictionary là gì?**

A. A mapping from keys to values — Ánh xạ từ khóa sang giá trị

B. Identifies a value for lookup — Xác định giá trị để tra cứu

C. Data associated with a key — Dữ liệu gắn với một khóa

D. A dictionary holding another dictionary — Dictionary chứa một Dictionary khác

**Q4. What is a nested dictionary? — Dictionary lồng nhau là gì?**

A. A mapping from keys to values — Ánh xạ từ khóa sang giá trị

B. Identifies a value for lookup — Xác định giá trị để tra cứu

C. Data associated with a key — Dữ liệu gắn với một khóa

D. A dictionary holding another dictionary — Dictionary chứa một Dictionary khác

**Q5. What does `d['x']` do when x exists? — `d['x']` làm gì khi khóa x tồn tại?**

A. Retrieves the value of x — Lấy giá trị gắn với x

B. `None` by default — Mặc định là `None`

C. `0` — `0`

D. `KeyError` — `KeyError`

**Q6. What does `d.get('x')` return if x is absent? — `d.get('x')` trả về gì nếu thiếu khóa x?**

A. Retrieves the value of x — Lấy giá trị gắn với x

B. `None` by default — Mặc định là `None`

C. `0` — `0`

D. `KeyError` — `KeyError`

**Q7. What does `d.get('x', 0)` return if x is absent? — `d.get('x', 0)` trả về gì nếu thiếu x?**

A. Retrieves the value of x — Lấy giá trị gắn với x

B. `None` by default — Mặc định là `None`

C. `0` — `0`

D. `KeyError` — `KeyError`

**Q8. What does `d['missing']` raise? — `d['missing']` phát sinh gì khi thiếu khóa?**

A. Retrieves the value of x — Lấy giá trị gắn với x

B. `None` by default — Mặc định là `None`

C. `0` — `0`

D. `KeyError` — `KeyError`

**Q9. What does `d.items()` provide? — `d.items()` cung cấp gì?**

A. Key-value pairs — Các cặp khóa và giá trị

B. Dictionary keys — Các khóa Dictionary

C. Dictionary values — Các giá trị Dictionary

D. Removes x and returns its value — Xóa khóa x và trả giá trị của nó

**Q10. What does `d.keys()` provide? — `d.keys()` cung cấp gì?**

A. Key-value pairs — Các cặp khóa và giá trị

B. Dictionary keys — Các khóa Dictionary

C. Dictionary values — Các giá trị Dictionary

D. Removes x and returns its value — Xóa khóa x và trả giá trị của nó

**Q11. What does `d.values()` provide? — `d.values()` cung cấp gì?**

A. Key-value pairs — Các cặp khóa và giá trị

B. Dictionary keys — Các khóa Dictionary

C. Dictionary values — Các giá trị Dictionary

D. Removes x and returns its value — Xóa khóa x và trả giá trị của nó

**Q12. What does `d.pop('x', None)` do if x is present? — `d.pop('x', None)` làm gì nếu x tồn tại?**

A. Key-value pairs — Các cặp khóa và giá trị

B. Dictionary keys — Các khóa Dictionary

C. Dictionary values — Các giá trị Dictionary

D. Removes x and returns its value — Xóa khóa x và trả giá trị của nó

**Q13. What does `d['x'] = 5` do if x already exists? — `d['x'] = 5` làm gì khi x đã tồn tại?**

A. Replaces the value mapped to x — Thay giá trị của khóa x

B. Adds a new key-value pair — Thêm một cặp khóa–giá trị mới

C. Deletes the entry — Xóa mục dữ liệu

D. Whether x is a key — x có phải khóa của Dictionary không

**Q14. What does `d['new'] = 5` do if new is absent? — `d['new'] = 5` làm gì khi khóa new chưa có?**

A. Replaces the value mapped to x — Thay giá trị của khóa x

B. Adds a new key-value pair — Thêm một cặp khóa–giá trị mới

C. Deletes the entry — Xóa mục dữ liệu

D. Whether x is a key — x có phải khóa của Dictionary không

**Q15. What does `del d['x']` do for an existing key? — `del d['x']` làm gì với khóa đang tồn tại?**

A. Replaces the value mapped to x — Thay giá trị của khóa x

B. Adds a new key-value pair — Thêm một cặp khóa–giá trị mới

C. Deletes the entry — Xóa mục dữ liệu

D. Whether x is a key — x có phải khóa của Dictionary không

**Q16. What does `'x' in d` test? — `'x' in d` kiểm tra gì?**

A. Replaces the value mapped to x — Thay giá trị của khóa x

B. Adds a new key-value pair — Thêm một cặp khóa–giá trị mới

C. Deletes the entry — Xóa mục dữ liệu

D. Whether x is a key — x có phải khóa của Dictionary không

**Q17. May a List be a normal dictionary key? — Có thể dùng List làm khóa Dictionary thông thường không?**

A. No, Lists are unhashable — Không, List không hash được

B. Yes, it is hashable — Có, Tuple này hash được

C. `d['A']['score']` — `d['A']['score']`

D. Keys — Các khóa

**Q18. Can a tuple of integers be a dictionary key? — Tuple chứa số nguyên có thể làm khóa Dictionary không?**

A. No, Lists are unhashable — Không, List không hash được

B. Yes, it is hashable — Có, Tuple này hash được

C. `d['A']['score']` — `d['A']['score']`

D. Keys — Các khóa

**Q19. How do you access the score in `d['A']` when it is a nested dictionary? — Lấy điểm trong Dictionary con `d['A']` thế nào?**

A. No, Lists are unhashable — Không, List không hash được

B. Yes, it is hashable — Có, Tuple này hash được

C. `d['A']['score']` — `d['A']['score']`

D. Keys — Các khóa

**Q20. What must be unique within one dictionary? — Điều gì phải duy nhất trong một Dictionary?**

A. No, Lists are unhashable — Không, List không hash được

B. Yes, it is hashable — Có, Tuple này hash được

C. `d['A']['score']` — `d['A']['score']`

D. Keys — Các khóa

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | A dictionary associates each unique key with one value. | Dictionary liên kết mỗi khóa duy nhất với một giá trị. |
| Q2 | **B** | Keys identify entries to read, update, or remove. | Khóa chỉ ra mục dữ liệu cần đọc, sửa hoặc xóa. |
| Q3 | **C** | Values can be text, numbers, lists or nested dictionaries. | Giá trị có thể là chuỗi, số, List hoặc Dictionary con. |
| Q4 | **D** | Nested mappings group related subfields under a parent key. | Dictionary lồng gom các trường con theo khóa cha. |
| Q5 | **A** | Bracket lookup accesses the mapped value directly. | Tra cứu bằng ngoặc vuông lấy trực tiếp giá trị của khóa. |
| Q6 | **B** | get avoids KeyError for absent keys unless different behavior is requested. | get trả None khi thiếu khóa nếu không đặt giá trị mặc định khác. |
| Q7 | **C** | The second argument supplies the fallback value. | Đối số thứ hai là giá trị thay thế khi thiếu khóa. |
| Q8 | **D** | Direct bracket access to a missing key raises KeyError. | Truy cập ngoặc vuông với khóa không tồn tại gây KeyError. |
| Q9 | **A** | items supports iterating over keys together with their values. | items cho phép duyệt đồng thời khóa và giá trị. |
| Q10 | **B** | keys exposes the keys for iteration or membership checks. | keys cho phép duyệt hoặc kiểm tra các khóa. |
| Q11 | **C** | values exposes the stored values without their keys. | values cho phép duyệt các giá trị mà không kèm khóa. |
| Q12 | **D** | pop removes an entry while returning the removed value. | pop vừa xóa mục dữ liệu vừa trả lại giá trị đã xóa. |
| Q13 | **A** | Assigning an existing key updates its value. | Gán khóa đã có sẽ cập nhật giá trị. |
| Q14 | **B** | Assignment to an absent key inserts a new entry. | Gán vào khóa chưa có sẽ thêm mục dữ liệu mới. |
| Q15 | **C** | del removes the key and its associated value. | del xóa khóa và giá trị gắn với nó. |
| Q16 | **D** | Membership tests dictionary keys rather than values by default. | Toán tử in trên Dictionary mặc định kiểm tra khóa. |
| Q17 | **A** | Mutable Lists cannot be hashed for dictionary keys. | List có thể thay đổi nên không dùng trực tiếp làm khóa. |
| Q18 | **B** | A tuple of hashable elements can act as a key. | Tuple gồm phần tử hash được có thể làm khóa. |
| Q19 | **C** | The first lookup retrieves the nested mapping and the second retrieves a field. | Lần tra đầu lấy Dictionary con, lần tra sau lấy trường điểm. |
| Q20 | **D** | A dictionary cannot contain duplicate keys as separate entries. | Một Dictionary không thể giữ các khóa trùng thành các mục độc lập. |

## 8. Nối sang bài tiếp theo

`List/Set → Dictionary → JSON/CSV → DataFrame`.
