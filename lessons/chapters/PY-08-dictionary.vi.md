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

### 4.1. Dictionary

**Từ vựng trong mục:** **Dictionary** — từ điển.

Dictionary lưu thông tin thành từng cặp khóa và giá trị. Ví dụ `{'id': 'O1'}` có khóa `id` và giá trị `O1`. Ta dùng `{}` để tạo Dictionary.

```python
print({'id':'O1'})
```

### 4.2. Key

**Từ vựng trong mục:** **Key** — khóa.

Khóa là tên dùng để lấy dữ liệu, ví dụ `'id'`. `{'id': 'O1'}['id']` cho kết quả `O1`. Khóa trong cùng một Dictionary phải duy nhất.

```python
print({'id':'O1'}['id'])
```

### 4.3. Value

**Từ vựng trong mục:** **Value** — giá trị.

Giá trị là thông tin nằm sau khóa, có thể là chữ, số hoặc một Dictionary khác. `{'x': 5}.get('x')` trả về `5`; với khóa không tồn tại, `get()` mặc định trả về `None`.

```python
print({'x':5}.get('x'))
```

### 4.4. Nested dict

**Từ vựng trong mục:** **Nested dict** — từ điển lồng.

Dictionary lồng nhau là Dictionary chứa Dictionary khác. Ví dụ mã học viên `A` chứa `{'score': 8}`; dùng `['A']['score']` để lấy điểm `8`.

```python
print({'A':{'score':8}}['A']['score'])
```

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
for x in labels: count[x]=count.get(x,0)+1
print(count)
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

**Kết quả:** `None` — không có mã `P02` để xóa; `P01` vẫn còn trong Dictionary.

## 6. Nhầm lẫn dễ gặp

- `obj[key]` gây `KeyError` nếu khóa chưa tồn tại; `obj.get(key)` trả về `None` hoặc giá trị mặc định đã truyền vào.
- Gán `obj[key] = value` sẽ thêm khóa mới hoặc ghi đè giá trị đang có.
- `pop(key)` lấy và xóa giá trị; nếu khóa không tồn tại, nên truyền giá trị mặc định khi phù hợp.
- Khóa Dictionary phải là kiểu có thể băm (hashable), như chuỗi hoặc số; không dùng List làm khóa.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What does a dictionary store? — Dictionary lưu thông tin như thế nào?**

A. Key–value pairs — Các cặp khóa và giá trị

B. Only numbers — Chỉ số

C. Only list indexes — Chỉ chỉ số list

D. Only unique words — Chỉ từ không trùng

**Q2. What is a key in a dictionary? — Khóa trong Dictionary là gì?**

A. The largest number — Số lớn nhất

B. An identifier used to look up a value — Tên hoặc mã để tìm giá trị

C. An automatic sort rule — Quy tắc sắp xếp

D. Always a list — Luôn là list

**Q3. What is a dictionary value? — Giá trị của Dictionary là gì?**

A. Always a filename — Luôn là tên file

B. Always a Boolean — Luôn là đúng sai

C. Information stored under a key — Thông tin được lưu theo một khóa

D. The number of keys — Số lượng khóa

**Q4. What is a nested dictionary? — Dictionary lồng nhau là gì?**

A. A sorted list — List đã sắp xếp

B. A set of numbers — Tập hợp số

C. A text file — File văn bản

D. A dictionary containing another dictionary — Dictionary chứa Dictionary con

**Q5. What does obj.get('x') return if x is absent? — get('x') trả về gì nếu thiếu khóa x?**

A. None by default — Mặc định là None

B. Always 0 — Luôn là 0

C. A KeyError — Lỗi KeyError

D. The first value — Giá trị đầu

**Q6. What does obj.items() provide? — obj.items() cung cấp gì?**

A. Only keys — Chỉ khóa

B. Key–value pairs — Các cặp khóa và giá trị

C. Only values — Chỉ giá trị

D. The last item — Phần tử cuối

**Q7. What does obj['x'] = 5 do? — obj['x'] = 5 làm gì?**

A. Deletes x — Xóa khóa x

B. Sorts all keys — Sắp xếp mọi khóa

C. Adds or updates x — Thêm hoặc cập nhật khóa x

D. Returns a list — Trả về list

**Q8. What does obj.pop('x', None) do when x is missing? — pop('x', None) làm gì khi thiếu x?**

A. Creates x — Tạo khóa x

B. Deletes every key — Xóa mọi khóa

C. Always raises KeyError — Luôn báo KeyError

D. Returns None — Trả về None

**Q9. What is returned for unknown order O3? — Tra cứu đơn O3 chưa có trả về gì?**

A. Not found — Not found

B. paid — paid

C. pending — pending

D. O1 — O1

**Q10. How many SKU01 items remain after selling two? — SKU01 còn bao nhiêu món sau khi bán hai?**

A. 5 — 5

B. 3 — 3

C. 2 — 2

D. 7 — 7

**Q11. How many AI labels are counted? — Nhãn AI xuất hiện bao nhiêu lần?**

A. 1 — 1

B. 3 — 3

C. 2 — 2

D. 0 — 0

**Q12. What score belongs to SV2? — Điểm của SV2 là bao nhiêu?**

A. 8 — 8

B. 10 — 10

C. 0 — 0

D. 9 — 9

**Q13. What is printed when P02 is not present? — In gì khi không có P02?**

A. None — None

B. P01 — P01

C. 10 — 10

D. KeyError — KeyError

**Q14. Which expression safely looks up an optional key? — Cách nào tra khóa có thể không tồn tại?**

A. obj['x'] always — Luôn dùng obj['x']

B. obj.get('x') — obj.get('x')

C. obj.remove('x') — obj.remove('x')

D. obj.sort() — obj.sort()

**Q15. What does count.get(x, 0) provide for a new label? — count.get(x, 0) cho gì khi gặp nhãn mới?**

A. A string — Một chuỗi

B. A list — Một list

C. 0 — 0

D. An exception — Một lỗi

**Q16. What happens when you assign an existing key? — Gán vào khóa đã tồn tại sẽ thế nào?**

A. Nothing changes — Không thay đổi

B. It creates a duplicate key — Tạo khóa trùng

C. It always fails — Luôn lỗi

D. Its value is replaced — Giá trị được thay thế

**Q17. How do you access a score inside students['SV2']? — Lấy điểm trong students['SV2'] bằng cách nào?**

A. students['SV2']['score'] — students['SV2']['score']

B. students[2] — students[2]

C. students.score only — Chỉ students.score

D. students.pop() — students.pop()

**Q18. What does obj.values() give? — obj.values() cho kết quả gì?**

A. Only keys — Chỉ khóa

B. The stored values — Các giá trị đã lưu

C. Key/value pairs — Các cặp khóa và giá trị

D. Sorted keys — Khóa đã sắp

**Q19. Can a list normally be used as a dictionary key? — Có thể dùng List làm khóa Dictionary không?**

A. Yes, always — Có, luôn được

B. Only if empty — Chỉ khi rỗng

C. No, lists are unhashable — Không, List không thể băm

D. Only with pop — Chỉ khi dùng pop

**Q20. Which object is best for looking up stock by SKU? — Nên dùng gì để tìm tồn kho theo mã SKU?**

A. A single float — Một số thực

B. A bare Boolean — Một giá trị đúng sai

C. An unrelated tuple — Tuple không liên quan

D. A dictionary mapping SKU to quantity — Dictionary nối mã SKU với số lượng

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | A dictionary maps keys to values. | Dictionary nối mỗi khóa với một giá trị. |
| Q2 | **B** | Keys identify stored values. | Khóa dùng để tìm thông tin đã lưu. |
| Q3 | **C** | Values are associated with keys. | Mỗi giá trị gắn với một khóa. |
| Q4 | **D** | Nested dictionaries group related details. | Dictionary lồng giúp gom thông tin liên quan. |
| Q5 | **A** | get returns None when no default is specified. | get trả về None nếu không truyền giá trị mặc định. |
| Q6 | **B** | items yields pairs for iteration. | items cung cấp các cặp khi duyệt. |
| Q7 | **C** | Assignment creates or replaces the value. | Phép gán tạo hoặc sửa giá trị. |
| Q8 | **D** | The default prevents KeyError for a missing key. | Giá trị mặc định giúp tránh KeyError. |
| Q9 | **A** | O3 is absent, so get returns the default. | O3 không tồn tại nên get trả về câu mặc định. |
| Q10 | **B** | Five minus two equals three. | Năm trừ hai còn ba. |
| Q11 | **C** | AI appears twice in the input list. | AI xuất hiện hai lần trong list. |
| Q12 | **D** | SV2 has score 9. | SV2 có điểm 9. |
| Q13 | **A** | pop uses None as the fallback. | pop trả về None khi không có khóa. |
| Q14 | **B** | get can handle a missing key. | get xử lý được khóa không tồn tại. |
| Q15 | **C** | The fallback starts counting at zero. | Giá trị mặc định giúp bắt đầu đếm từ 0. |
| Q16 | **D** | Dictionary keys are unique. | Các khóa của Dictionary là duy nhất. |
| Q17 | **A** | Two key lookups reach the nested value. | Hai lần tra khóa lấy được giá trị bên trong. |
| Q18 | **B** | values exposes the dictionary's values. | values cho phép duyệt các giá trị. |
| Q19 | **C** | Mutable lists are unhashable. | List có thể thay đổi nên không dùng làm khóa. |
| Q20 | **D** | Dictionary keys enable SKU-based lookups. | Khóa Dictionary giúp tra mã SKU. |

## 8. Nối sang bài tiếp theo

`List/Set → Dictionary → JSON/CSV → DataFrame`.
