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

A. An unordered collection of unique values only — Tập không thứ tự chỉ gồm giá trị duy nhất

B. An immutable pair of numbers — Cặp số bất biến

C. A mapping from hashable keys to values — Ánh xạ từ khóa có thể băm sang giá trị

D. A sequence with numeric positions only — Dãy chỉ truy cập bằng vị trí số


**Q2. What does a dictionary key do? — Khóa Dictionary có vai trò gì?**

A. Specifies the dictionary's length — Xác định độ dài Dictionary

B. Stores all keys as values — Lưu mọi khóa thành giá trị

C. Sorts the stored values — Sắp xếp các giá trị đã lưu

D. Identifies an entry for lookup — Xác định mục để tra cứu


**Q3. What is a dictionary value? — Giá trị Dictionary là gì?**

A. The key's index position — Vị trí chỉ số của khóa

B. Data associated with a key — Dữ liệu gắn với khóa

C. Always a second dictionary — Luôn là Dictionary thứ hai

D. A name used only in a `for` loop — Tên chỉ dùng trong vòng `for`


**Q4. What is a nested dictionary? — Dictionary lồng nhau là gì?**

A. A dictionary stored inside another dictionary — Dictionary được lưu trong Dictionary khác

B. A list nested inside a set — List lồng trong Set

C. A set of duplicate keys — Set gồm khóa trùng

D. A dictionary with only numeric keys — Dictionary chỉ có khóa số


**Q5. What does `d['x']` do when x exists? — `d['x']` làm gì khi khóa x tồn tại?**

A. Always returns `None` — Luôn trả `None`

B. Retrieves the value stored under `'x'` — Lấy giá trị lưu dưới khóa `'x'`

C. Returns `'x'` as a string — Trả chuỗi `'x'`

D. Deletes the entry for `'x'` — Xóa mục có khóa `'x'`


**Q6. What does `d.get('x')` return if x is absent? — `d.get('x')` trả về gì nếu thiếu khóa x?**

A. `KeyError` — `KeyError`

B. `None` by default — Mặc định là `None`

C. The empty dictionary `{}` — Dictionary rỗng `{}`

D. The string `'x'` — Chuỗi `'x'`


**Q7. What does `d.get('x', 0)` return if x is absent? — `d.get('x', 0)` trả về gì nếu thiếu x?**

A. The integer `0` — Số nguyên `0`

B. A newly inserted entry — Một mục mới được thêm

C. The string `'0'` — Chuỗi `'0'`

D. `None` — `None`


**Q8. What does `d['missing']` raise? — `d['missing']` phát sinh gì khi thiếu khóa?**

A. `0` — `0`

B. An empty list — List rỗng

C. `KeyError` — `KeyError`

D. `None` — `None`


**Q9. What does `d.items()` provide? — `d.items()` cung cấp gì?**

A. A sorted list of keys — List khóa đã sắp

B. A view of key-value pairs — View của các cặp khóa–giá trị

C. Only a view of values — Chỉ view các giá trị

D. Only a view of keys — Chỉ view các khóa


**Q10. What does `d.keys()` provide? — `d.keys()` cung cấp gì?**

A. A view of values — View các giá trị

B. A list of keys sorted automatically — List khóa tự sắp

C. A view of pairs — View các cặp khóa–giá trị

D. A view of dictionary keys — View của các khóa Dictionary


**Q11. What does `d.values()` provide? — `d.values()` cung cấp gì?**

A. A view of dictionary values — View các giá trị Dictionary

B. A dictionary copy — Bản sao Dictionary

C. A view of keys — View các khóa

D. A view of key-value pairs — View các cặp khóa–giá trị


**Q12. What does `d.pop('x', None)` do if x is present? — `d.pop('x', None)` làm gì nếu x tồn tại?**

A. Returns the value without deletion — Trả giá trị nhưng không xóa

B. Removes the key but always returns `None` — Xóa khóa nhưng luôn trả `None`

C. Deletes every dictionary entry — Xóa mọi mục Dictionary

D. Removes `'x'` and returns its former value — Xóa `'x'` và trả giá trị cũ


**Q13. What does `d['x'] = 5` do if x already exists? — `d['x'] = 5` làm gì khi x đã tồn tại?**

A. Replaces the value associated with `'x'` — Thay giá trị gắn với `'x'`

B. Adds a second duplicate `'x'` key — Thêm khóa `'x'` trùng thứ hai

C. Deletes the key `'x'` — Xóa khóa `'x'`

D. Tests whether `'x'` exists — Kiểm tra `'x'` tồn tại không


**Q14. What does `d['new'] = 5` do if new is absent? — `d['new'] = 5` làm gì khi khóa new chưa có?**

A. Deletes an absent key — Xóa một khóa không tồn tại

B. Returns the total dictionary length — Trả tổng độ dài Dictionary

C. Replaces an unrelated existing key — Thay một khóa cũ không liên quan

D. Inserts a new key-value entry — Thêm một mục khóa–giá trị mới


**Q15. What does `del d['x']` do for an existing key? — `del d['x']` làm gì với khóa đang tồn tại?**

A. Deletes that key and its value — Xóa khóa đó cùng giá trị

B. Deletes the entire dictionary — Xóa toàn bộ Dictionary

C. Leaves the entry intact and returns its value — Giữ nguyên mục và trả giá trị

D. Replaces its value with `None` — Thay giá trị bằng `None`


**Q16. What does `'x' in d` test? — `'x' in d` kiểm tra gì?**

A. Whether `'x'` is a numeric index — `'x'` có phải chỉ số số hay không

B. Whether any key maps to `'x'` — Có khóa nào ánh xạ tới `'x'` không

C. Whether `'x'` is a dictionary key — `'x'` có là khóa Dictionary không

D. Whether `'x'` appears in values only — `'x'` có nằm trong các giá trị hay không


**Q17. May a List be a normal dictionary key? — Có thể dùng List làm khóa Dictionary thông thường không?**

A. Yes, if the list has two elements — Có, nếu List có hai phần tử

B. Yes, if list values are distinct — Có, nếu các giá trị List khác nhau

C. No, lists are unhashable — Không, List không thể băm

D. Yes, every list is hashable — Có, mọi List đều có thể băm


**Q18. Can a tuple of integers be a dictionary key? — Tuple chứa số nguyên có thể làm khóa Dictionary không?**

A. No, all tuples are unhashable — Không, mọi Tuple đều không thể băm

B. Yes, a tuple of integers is hashable — Có, Tuple chứa số nguyên có thể băm

C. Only if the tuple has one element — Chỉ nếu Tuple có một phần tử

D. Only if the tuple is empty — Chỉ nếu Tuple rỗng


**Q19. How do you access the score in `d['A']` when it is a nested dictionary? — Lấy điểm trong Dictionary con `d['A']` thế nào?**

A. `d['A', 'score']` — `d['A', 'score']`

B. `d['score']['A']` — `d['score']['A']`

C. `d.get('A', 'score')` — `d.get('A', 'score')`

D. `d['A']['score']` — `d['A']['score']`


**Q20. What must be unique within one dictionary? — Điều gì phải duy nhất trong một Dictionary?**

A. Dictionary values — Các giá trị Dictionary

B. Both all keys and all values must be unique — Cả khóa và giá trị đều phải duy nhất

C. Dictionary keys — Các khóa Dictionary

D. Neither keys nor values must be unique — Cả khóa lẫn giá trị đều không cần duy nhất

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **C** | A dictionary maps unique hashable keys to associated values, for example `{'name':'An', 'score':9}`. You retrieve a value through its key instead of a numeric list position. | Dictionary ánh xạ các khóa khác nhau, có thể băm, tới giá trị tương ứng, ví dụ `{'name':'An', 'score':9}`. Bạn truy cập giá trị qua khóa thay vì chỉ số vị trí như List. |
| Q2 | **D** | A key identifies an entry and is used to look up, update, or remove its value. For `{'age': 20}`, the key `'age'` leads to value `20`; it is not itself the associated value. | Khóa xác định một mục để tra cứu, cập nhật hoặc xóa giá trị. Trong `{'age': 20}`, khóa `'age'` dẫn đến giá trị `20`; khóa không đồng nghĩa với giá trị đi kèm. |
| Q3 | **B** | A dictionary value is the data stored under a key, such as number `20` under key `'age'`. Values can be many types, including lists or dictionaries, while keys must be hashable. | Giá trị Dictionary là dữ liệu lưu dưới một khóa, chẳng hạn số `20` dưới khóa `'age'`. Giá trị có thể thuộc nhiều kiểu kể cả List hoặc Dictionary, trong khi khóa phải là đối tượng có thể băm. |
| Q4 | **A** | A nested dictionary is a dictionary used as a value inside another mapping. For example `{'A': {'score': 9}}` groups the `score` field under key `'A'`, and two bracket lookups reach the number. | Dictionary lồng nhau là Dictionary được lưu làm giá trị trong Dictionary khác. Ví dụ `{'A': {'score': 9}}` gom trường `score` dưới khóa `'A'`, và hai lần truy cập ngoặc vuông sẽ lấy được con số. |
| Q5 | **B** | When key `'x'` exists, `d['x']` returns the value associated with it. Unlike `d.get('x')`, direct bracket lookup raises `KeyError` if the key is missing. | Khi khóa `'x'` tồn tại, `d['x']` lấy giá trị gắn với khóa đó. Khác `d.get('x')`, truy cập ngoặc vuông sẽ gây `KeyError` nếu khóa không tồn tại. |
| Q6 | **B** | Without an explicit default, `d.get('x')` returns `None` for a missing key instead of raising `KeyError`. This lets the caller handle missing data, but `None` might also be a legitimate stored value. | Khi không cung cấp mặc định, `d.get('x')` trả `None` nếu thiếu khóa thay vì gây `KeyError`. Cách này giúp xử lý dữ liệu thiếu, nhưng bản thân `None` cũng có thể là giá trị được lưu thật. |
| Q7 | **A** | The second argument of `get` is the fallback for a missing key, so `d.get('x', 0)` returns integer `0` when `'x'` is absent. It does not create that key or overwrite existing values. | Đối số thứ hai của `get` là giá trị dự phòng khi không tìm thấy khóa, nên `d.get('x', 0)` trả số nguyên `0` nếu thiếu `'x'`. Lệnh không tạo khóa đó và không ghi đè giá trị đang có. |
| Q8 | **C** | Direct access with `d['missing']` raises `KeyError` when the key is absent. For optional entries, `get` can return a fallback; this difference matters when deciding whether absence should be an error. | Truy cập trực tiếp `d['missing']` gây `KeyError` khi không có khóa. Với dữ liệu tùy chọn, `get` có thể trả giá trị dự phòng; sự khác biệt này quyết định có xem việc thiếu khóa là lỗi hay không. |
| Q9 | **B** | `d.items()` returns a dynamic view of key-value pairs used in loops such as `for key, value in d.items()`. It is not the same as `keys()`, which exposes only keys, or `values()`, which exposes only values. | `d.items()` trả một view động của các cặp khóa–giá trị, thường duyệt bằng `for key, value in d.items()`. Nó khác `keys()` chỉ đưa ra khóa và `values()` chỉ đưa ra giá trị. |
| Q10 | **D** | `d.keys()` provides a dynamic view of dictionary keys. With `{'a': 1}`, iterating that view yields `'a'`, not value `1` or the entire key-value pair. | `d.keys()` cung cấp view động của các khóa Dictionary. Với `{'a': 1}`, khi duyệt view này nhận `'a'`, không phải giá trị `1` hay cả cặp khóa–giá trị. |
| Q11 | **A** | `d.values()` provides a dynamic view of the values stored in a dictionary. For `{'a': 1, 'b': 2}`, iteration yields 1 and 2; to retain their associated keys, use `items()` instead. | `d.values()` trả view động của các giá trị đang lưu. Với `{'a': 1, 'b': 2}`, khi duyệt thu được 1 và 2; muốn kèm khóa tương ứng thì dùng `items()`. |
| Q12 | **D** | When `'x'` is present, `d.pop('x', None)` removes its entry and returns its former value. The optional `None` is a fallback only if the key is absent; it does not force the return value to be `None`. | Khi `'x'` tồn tại, `d.pop('x', None)` xóa mục tương ứng và trả về giá trị cũ. Đối số `None` chỉ là giá trị dự phòng nếu không có khóa; nó không ép kết quả luôn thành `None`. |
| Q13 | **A** | Assigning `d['x'] = 5` when `'x'` is already a key replaces that entry's value with `5`. It does not insert a second duplicate key because each dictionary key is unique. | Gán `d['x'] = 5` khi khóa `'x'` đã tồn tại sẽ thay giá trị của mục đó thành `5`. Lệnh không tạo thêm một khóa `'x'` thứ hai vì mỗi khóa Dictionary là duy nhất. |
| Q14 | **D** | Assigning `d['new'] = 5` when the key is absent inserts a new mapping from `'new'` to 5. The same assignment syntax updates an existing key if it was already present. | Gán `d['new'] = 5` khi chưa có khóa sẽ thêm cặp `'new'` ánh xạ tới 5. Cùng cú pháp gán này lại cập nhật giá trị nếu khóa đã tồn tại. |
| Q15 | **A** | `del d['x']` removes an existing key and its associated value from the dictionary. Unlike `pop`, the `del` statement does not produce the removed value as a return result. | `del d['x']` xóa khóa có sẵn cùng giá trị tương ứng khỏi Dictionary. Khác `pop`, câu lệnh `del` không trả về giá trị đã xóa. |
| Q16 | **C** | For dictionaries, `in` tests keys by default: `'x' in {'x': 3}` is `True`, but `3 in {'x': 3}` is `False`. To inspect values rather than keys, check membership in `d.values()`. | Với Dictionary, `in` mặc định kiểm tra khóa: `'x' in {'x': 3}` là `True`, còn `3 in {'x': 3}` là `False`. Muốn kiểm tra giá trị thay vì khóa, hãy xét thành viên trong `d.values()`. |
| Q17 | **C** | A list is mutable and therefore unhashable, so it cannot be an ordinary dictionary key. Trying `{[1,2]: 'x'}` raises `TypeError`; a tuple of hashable numbers can be used instead. | List có thể thay đổi nên không thể băm và không dùng làm khóa Dictionary thông thường. Thử `{[1,2]: 'x'}` gây `TypeError`; một Tuple chứa các số có thể băm thì dùng được. |
| Q18 | **B** | A tuple consisting solely of integers is hashable and can serve as a dictionary key, such as `{(1,2): 'point'}`. Not every tuple works: one containing a list is unhashable because a nested member is unhashable. | Tuple chỉ chứa số nguyên có thể băm nên dùng làm khóa Dictionary, ví dụ `{(1,2): 'point'}`. Không phải mọi Tuple đều dùng được: Tuple chứa List cũng không thể băm vì một phần tử bên trong không thể băm. |
| Q19 | **D** | `d['A']['score']` first retrieves the nested dictionary stored under `'A'`, then looks up its `'score'` entry. With `d={'A':{'score':9}}`, the expression returns 9; the nested keys must exist or direct access raises `KeyError`. | `d['A']['score']` trước tiên lấy Dictionary con dưới khóa `'A'`, rồi tra mục `'score'` trong đó. Với `d={'A':{'score':9}}`, biểu thức trả 9; nếu thiếu một trong các khóa thì cách truy cập trực tiếp gây `KeyError`. |
| Q20 | **C** | Keys are unique within a dictionary; assigning the same key again updates the existing entry rather than adding another copy. Values may repeat across multiple keys, so uniqueness applies to keys, not values. | Các khóa là duy nhất trong một Dictionary; gán lại cùng một khóa sẽ cập nhật mục cũ thay vì tạo thêm bản sao. Giá trị có thể lặp ở nhiều khóa nên tính duy nhất áp dụng cho khóa chứ không phải giá trị. |

## 8. Nối sang bài tiếp theo

`List/Set → Dictionary → JSON/CSV → DataFrame`.
