# PY-07 — Tuple, Set và các phép toán tập hợp


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Tuple** — bộ giá trị; **Set** — tập hợp.

`List → Tuple và Set → Tập hợp/Jaccard`

Sau List, ta học hai cách lưu dữ liệu khác: Tuple giữ thứ tự và không cho sửa phần tử; Set chỉ giữ các phần tử khác nhau, giúp tìm phần chung hoặc gộp hai nhóm.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích dễ nhớ |
|---|---|---|
| Tuple | bộ giá trị | Dãy có thứ tự không sửa phần tử được |
| Set | tập hợp | Nhóm phần tử không trùng lặp |
| Union | phép hợp | Mọi phần tử có trong ít nhất một tập |
| Intersection | phép giao | Phần tử chung của hai tập |

## 3. Hàm và cú pháp Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cú pháp | Mục đích và lựa chọn liên quan |
|---|---|
| `tuple(items)` | Lưu một bộ dữ liệu có thứ tự và cố định |
| `set(items)` | Khử giá trị trùng, không giữ thứ tự đáng tin |
| `a.union(b)`, `a.intersection(b)` | Lấy toàn bộ phần tử của hai tập (hợp), hoặc chỉ phần tử chung (giao); tương đương `a \| b` và `a & b` |
| `a - b, a ^ b` | Tìm phần tử còn thiếu hoặc khác nhau |

## 4. Khái niệm liên quan

Sau List, có hai nhu cầu khác nhau: **giữ một bộ dữ liệu có thứ tự nhưng không sửa trực tiếp** (Tuple), hoặc **chỉ lưu các giá trị không trùng và so sánh hai nhóm** (Set). Hai cấu trúc không thay thế lẫn nhau: tọa độ `(3, 4)` phù hợp với Tuple, còn danh sách kỹ năng không trùng phù hợp với Set. Từ Set, bài học mở rộng sang phép hợp và phép giao.

### 4.1. Tuple — Bộ giá trị cố định

**Từ vựng trong mục:** **Tuple** — bộ giá trị; **Coordinate** — tọa độ.

Tuple chứa các phần tử **có thứ tự**, thường dùng cho một cặp thông tin gắn với nhau như tọa độ `(x, y)`. Với điểm ở vị trí `x = 3`, `y = 4` mét, ta viết `point = (3, 4)`; `point[0]` là x và `point[1]` là y. Không thể gán `point[0] = 5` như List; nếu cần vị trí mới, tạo Tuple mới.

```python
point = (3, 4)
print(point)
```

**Kết quả khi chạy:**

```text
(3, 4)
```

Dấu ngoặc tròn biểu thị Tuple gồm hai tọa độ, khác dấu ngoặc vuông của List.

### 4.2. Set — Tập hợp không trùng

**Từ vựng trong mục:** **Set** — tập hợp; **Duplicate** — giá trị lặp.

Set giúp lưu **những giá trị khác nhau** mà không cần ghi cùng một giá trị nhiều lần. Một nhóm học ghi ba nhãn `Python`, `AI`, `Python`; khi chuyển sang Set, nhãn `Python` bị trùng chỉ còn một lần. Set không có chỉ số vị trí như `set[0]` và không đảm bảo thứ tự in. `set()` tạo tập rỗng, còn `{}` tạo Dictionary rỗng.

```python
skills = set(['Python', 'AI', 'Python'])
print(len(skills))
```

**Kết quả khi chạy:**

```text
2
```

Có hai kỹ năng khác nhau: Python và AI. Ta in **số lượng** để không phụ thuộc thứ tự hiển thị của Set.

### 4.3. Union — Gộp hai nhóm

**Từ vựng trong mục:** **Union** — phép hợp; **Set** — tập hợp.

Giả sử nhóm A học `{Python, AI}`, nhóm B học `{AI, SQL}`. Cửa hàng khóa học muốn biết **tất cả kỹ năng có trong ít nhất một nhóm**. Phép hợp `a | b` giữ Python, AI và SQL nhưng chỉ giữ AI một lần. Với Set, ký hiệu `|` là phép hợp tập hợp, không phải toán tử `or` nối điều kiện Boolean.

```python
a = {'Python', 'AI'}
b = {'AI', 'SQL'}
print(len(a | b))
```

**Kết quả khi chạy:**

```text
3
```

Phép hợp gồm ba kỹ năng khác nhau; ký hiệu `|` gộp hai Set và tự loại phần trùng.

### 4.4. Intersection — Tìm phần chung

**Từ vựng trong mục:** **Intersection** — phép giao; **Set** — tập hợp.

Vẫn với hai nhóm A có `{Python, AI}` và B có `{AI, SQL}`, ta muốn tìm **kỹ năng cả hai nhóm đều học**. Phép giao `a & b` chỉ giữ AI, vì Python không có ở B và SQL không có ở A. Phép giao khác phép hợp: hợp trả ba kỹ năng, giao chỉ một kỹ năng.

```python
a = {'Python', 'AI'}
b = {'AI', 'SQL'}
print(a & b)
```

**Kết quả khi chạy:**

```text
{'AI'}
```

Chỉ có AI xuất hiện trong cả hai nhóm; tập chỉ có một phần tử nên thứ tự hiển thị không gây nhầm lẫn.
### 4.5. Difference — Phần tử còn thiếu trong Set

**Từ vựng trong mục:** **Difference** — hiệu tập hợp; **Set** — tập hợp.

Ngoài phép hợp và phép giao, ta còn cần biết **phần tử chỉ có ở nhóm A nhưng chưa có ở nhóm B**. Ví dụ khóa học yêu cầu `Python`, `SQL`, `AI`, còn học viên đã hoàn thành `Python`; hiệu `required - done` giữ `SQL` và `AI`. Dùng `sorted()` nếu muốn in các kỹ năng theo một thứ tự rõ ràng. Hiệu `a - b` khác **hiệu đối xứng** `a ^ b`, vốn lấy các phần tử chỉ thuộc một trong hai nhóm.

```python
required = {'Python', 'SQL', 'AI'}
done = {'Python'}
print(sorted(required - done))
```

**Kết quả khi chạy:**

```text
['AI', 'SQL']
```

Kết quả là một **List đã sắp xếp**, gồm hai kỹ năng cần học tiếp. Set gốc không bị thay đổi.

## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Khử email trùng

**Từ vựng trong mục:** **Set** — tập hợp; **Duplicate** — trùng lặp.

**Tình huống thực tế:** Ứng dụng gửi thông báo đang có bốn email `a@x.vn`, `b@x.vn`, `a@x.vn`, `c@x.vn`. Địa chỉ `a@x.vn` bị nhập hai lần.

**Yêu cầu:** Đếm có bao nhiêu địa chỉ email khác nhau.

**Vì sao chọn cách giải này?** `set()` bỏ bản ghi giống hệt nhau, `len()` đếm số email còn lại. Cách này chưa xử lý khác biệt chữ hoa/chữ thường.

**Quy trình giải:**

1. Lưu bốn email vào list.
2. Chuyển list thành set để bỏ email bị lặp.
3. Dùng `len()` đếm số email khác nhau.

```python
emails=["a@x.vn","b@x.vn","a@x.vn","c@x.vn"]
print(len(set(emails)))
```

**Kết quả khi chạy:**

```text
3
```

**Kết quả:** `3` — có ba địa chỉ email khác nhau.

### Tình huống 2 — Lưu tọa độ

**Từ vựng trong mục:** **Tuple** — bộ giá trị; **Coordinate** — tọa độ.

**Tình huống thực tế:** Một phần mềm bản đồ lưu điểm có tọa độ `(3, 4)` mét, tính từ gốc `(0, 0)`. Hai giá trị lần lượt là vị trí x và y.

**Yêu cầu:** Lấy x, y từ tuple và tính bình phương khoảng cách đến gốc tọa độ.

**Vì sao chọn cách giải này?** Tuple lưu gọn cặp tọa độ có thứ tự. Công thức `x*x + y*y` tính bình phương khoảng cách, không phải khoảng cách thực.

**Quy trình giải:**

1. Lưu tọa độ vào tuple `point`.
2. Tách tuple thành `x` và `y`.
3. Tính `x*x + y*y` rồi in kết quả.

```python
point=(3,4)
x,y=point
print(x*x+y*y)
```

**Kết quả khi chạy:**

```text
25
```

**Kết quả:** `25` m² — bình phương khoảng cách; khoảng cách thật bằng 5 mét.

### Tình huống 3 — Tìm kỹ năng chung

**Từ vựng trong mục:** **Intersection** — phép giao; **Set** — tập hợp.

**Tình huống thực tế:** Hai nhóm học viên có kỹ năng lần lượt là `{'Python', 'AI', 'SQL'}` và `{'Python', 'Math', 'AI'}`.

**Yêu cầu:** Tìm những kỹ năng có ở cả hai nhóm.

**Vì sao chọn cách giải này?** Phép giao `&` chỉ giữ các phần tử chung giữa hai set.

**Quy trình giải:**

1. Lưu kỹ năng của mỗi nhóm thành một set.
2. Dùng `a & b` để tìm phần tử chung.
3. In tập kỹ năng tìm được.

```python
a={"Python","AI","SQL"}
b={"Python","Math","AI"}
print(a&b)
```

**Kết quả khi chạy:**

```text
{'Python', 'AI'}
```

*Thứ tự các phần tử trong Set khi in có thể khác nhau.*

**Kết quả:** Tập chứa `Python` và `AI`; thứ tự hiển thị của set có thể thay đổi.

### Tình huống 4 — Gộp nhóm chủ đề

**Từ vựng trong mục:** **Union** — phép hợp; **Set** — tập hợp.

**Tình huống thực tế:** Hai nhóm tài liệu được gắn nhãn `{'Python', 'Math'}` và `{'Math', 'AI'}`. Nhân viên cần danh sách chủ đề của cả hai nhóm mà không lặp lại `Math`.

**Yêu cầu:** Gộp các nhãn thành một set chỉ chứa các chủ đề khác nhau.

**Vì sao chọn cách giải này?** Phép hợp `|` lấy tất cả phần tử thuộc một trong hai set và bỏ phần trùng.

**Quy trình giải:**

1. Lưu nhãn của từng nhóm thành set.
2. Dùng `a | b` để gộp.
3. In các nhãn sau khi gộp.

```python
a={"Python","Math"}
b={"Math","AI"}
print(a|b)
```

**Kết quả khi chạy:**

```text
{'Python', 'Math', 'AI'}
```

*Thứ tự các phần tử trong Set khi in có thể khác nhau.*

**Kết quả:** Tập chứa `Python`, `Math`, `AI`; thứ tự in không cố định.

### Tình huống 5 — Liệt kê bài còn thiếu

**Từ vựng trong mục:** **Difference** — hiệu tập hợp; **Set** — tập hợp.

**Tình huống thực tế:** Khóa học yêu cầu ba kỹ năng `Python`, `SQL`, `AI`. Một học viên đã học xong `Python`.

**Yêu cầu:** Liệt kê các kỹ năng học viên còn phải học.

**Vì sao chọn cách giải này?** Hiệu tập hợp `required - done` giữ những kỹ năng bắt buộc chưa có trong tập đã hoàn thành.

**Quy trình giải:**

1. Lưu tập kỹ năng bắt buộc.
2. Lưu tập kỹ năng đã học.
3. Lấy hiệu hai tập và in kết quả.

```python
required={"Python","SQL","AI"}
done={"Python"}
print(required-done)
```

**Kết quả khi chạy:**

```text
{'SQL', 'AI'}
```

*Thứ tự các phần tử trong Set khi in có thể khác nhau.*

**Kết quả:** Tập chứa `SQL` và `AI`; thứ tự in không cố định.

## 6. Nhầm lẫn dễ gặp

- Tuple không cho gán lại từng phần tử như `point[0] = 5`; nếu cần sửa tọa độ, tạo tuple mới.
- Set không có thứ tự cố định, không dùng `my_set[0]` và không dựa vào thứ tự khi in.
- Set chỉ giữ phần tử có thể băm được (hashable); không thể đặt list trực tiếp làm phần tử của set.
- Phép hợp `|` lấy tất cả phần tử; phép giao `&` chỉ lấy phần tử chung; phép trừ `-` tìm phần tử còn thiếu.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a tuple? — Tuple là gì?**

A. An ordered immutable collection — Bộ giá trị có thứ tự, không thể sửa trực tiếp

B. A collection of unique elements — Tập hợp các phần tử không trùng

C. Elements in either set — Phần tử thuộc ít nhất một trong hai tập

D. Elements common to both sets — Phần tử chung của cả hai tập

**Q2. What is a set? — Set là gì?**

A. An ordered immutable collection — Bộ giá trị có thứ tự, không thể sửa trực tiếp

B. A collection of unique elements — Tập hợp các phần tử không trùng

C. Elements in either set — Phần tử thuộc ít nhất một trong hai tập

D. Elements common to both sets — Phần tử chung của cả hai tập

**Q3. What does set union collect? — Phép hợp Set lấy gì?**

A. An ordered immutable collection — Bộ giá trị có thứ tự, không thể sửa trực tiếp

B. A collection of unique elements — Tập hợp các phần tử không trùng

C. Elements in either set — Phần tử thuộc ít nhất một trong hai tập

D. Elements common to both sets — Phần tử chung của cả hai tập

**Q4. What does set intersection collect? — Phép giao Set lấy gì?**

A. An ordered immutable collection — Bộ giá trị có thứ tự, không thể sửa trực tiếp

B. A collection of unique elements — Tập hợp các phần tử không trùng

C. Elements in either set — Phần tử thuộc ít nhất một trong hai tập

D. Elements common to both sets — Phần tử chung của cả hai tập

**Q5. Which expression constructs a two-element tuple? — Biểu thức nào tạo Tuple có hai phần tử?**

A. `(2, 3)` — `(2, 3)`

B. `{2, 3}` — `{2, 3}`

C. `set()` — `set()`

D. `{}` — `{}`

**Q6. Which expression constructs a nonempty set? — Biểu thức nào tạo Set không rỗng?**

A. `(2, 3)` — `(2, 3)`

B. `{2, 3}` — `{2, 3}`

C. `set()` — `set()`

D. `{}` — `{}`

**Q7. Which expression constructs an empty set? — Biểu thức nào tạo Set rỗng?**

A. `(2, 3)` — `(2, 3)`

B. `{2, 3}` — `{2, 3}`

C. `set()` — `set()`

D. `{}` — `{}`

**Q8. Which expression constructs an empty dictionary? — Biểu thức nào tạo Dictionary rỗng?**

A. `(2, 3)` — `(2, 3)`

B. `{2, 3}` — `{2, 3}`

C. `set()` — `set()`

D. `{}` — `{}`

**Q9. What does `a | b` do for sets? — `a | b` làm gì với hai Set?**

A. Set union — Phép hợp tập hợp

B. Set intersection — Phép giao tập hợp

C. Elements in a but not b — Các phần tử thuộc a nhưng không thuộc b

D. Symmetric difference — Hiệu đối xứng

**Q10. What does `a & b` do for sets? — `a & b` làm gì với hai Set?**

A. Set union — Phép hợp tập hợp

B. Set intersection — Phép giao tập hợp

C. Elements in a but not b — Các phần tử thuộc a nhưng không thuộc b

D. Symmetric difference — Hiệu đối xứng

**Q11. What does `a - b` do for sets? — `a - b` làm gì với hai Set?**

A. Set union — Phép hợp tập hợp

B. Set intersection — Phép giao tập hợp

C. Elements in a but not b — Các phần tử thuộc a nhưng không thuộc b

D. Symmetric difference — Hiệu đối xứng

**Q12. What does `a ^ b` do for sets? — `a ^ b` làm gì với hai Set?**

A. Set union — Phép hợp tập hợp

B. Set intersection — Phép giao tập hợp

C. Elements in a but not b — Các phần tử thuộc a nhưng không thuộc b

D. Symmetric difference — Hiệu đối xứng

**Q13. What is the length of `set([1,1,2])`? — `set([1,1,2])` có bao nhiêu phần tử?**

A. `2` — `2`

B. `TypeError` — `TypeError`

C. `x in s` — `x in s`

D. No fixed order is guaranteed — Không bảo đảm thứ tự cố định

**Q14. What happens when assigning `t[0] = 9` on a tuple? — Gán `t[0] = 9` trên Tuple sẽ thế nào?**

A. `2` — `2`

B. `TypeError` — `TypeError`

C. `x in s` — `x in s`

D. No fixed order is guaranteed — Không bảo đảm thứ tự cố định

**Q15. How do you test membership in a set? — Làm sao kiểm tra một giá trị thuộc Set?**

A. `2` — `2`

B. `TypeError` — `TypeError`

C. `x in s` — `x in s`

D. No fixed order is guaranteed — Không bảo đảm thứ tự cố định

**Q16. Is order of printed set elements guaranteed? — Thứ tự phần tử in từ Set có được bảo đảm không?**

A. `2` — `2`

B. `TypeError` — `TypeError`

C. `x in s` — `x in s`

D. No fixed order is guaranteed — Không bảo đảm thứ tự cố định

**Q17. Which type best fits a fixed coordinate pair? — Kiểu nào phù hợp cho cặp tọa độ cố định?**

A. Tuple — Tuple

B. Set — Set

C. `isdisjoint()` — `isdisjoint()`

D. `sorted()` — `sorted()`

**Q18. Which type is suitable for deduplicating tags? — Kiểu nào phù hợp để loại nhãn trùng?**

A. Tuple — Tuple

B. Set — Set

C. `isdisjoint()` — `isdisjoint()`

D. `sorted()` — `sorted()`

**Q19. Which method checks whether sets share no elements? — Phương thức nào kiểm tra hai Set không có phần tử chung?**

A. Tuple — Tuple

B. Set — Set

C. `isdisjoint()` — `isdisjoint()`

D. `sorted()` — `sorted()`

**Q20. Which function creates a sorted list from a set? — Hàm nào tạo List đã sắp từ một Set?**

A. Tuple — Tuple

B. Set — Set

C. `isdisjoint()` — `isdisjoint()`

D. `sorted()` — `sorted()`

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | A tuple preserves order while preventing reassignment of its elements. | Tuple giữ thứ tự nhưng không cho gán lại từng phần tử. |
| Q2 | **B** | A set contains distinct values and has no positional indexing. | Set giữ giá trị không trùng và không truy cập theo chỉ số vị trí. |
| Q3 | **C** | Union includes all distinct members found in either set. | Phép hợp chứa các phần tử khác nhau có trong ít nhất một tập. |
| Q4 | **D** | Intersection contains only elements shared by both inputs. | Phép giao chỉ lấy phần tử có ở cả hai tập. |
| Q5 | **A** | Parentheses with two comma-separated values represent a tuple. | Hai giá trị phân cách bởi dấu phẩy trong ngoặc tròn tạo Tuple. |
| Q6 | **B** | Curly braces around plain distinct values form a set. | Ngoặc nhọn bao các giá trị riêng lẻ tạo Set. |
| Q7 | **C** | Empty braces create a dictionary, not a set. | Ngoặc nhọn rỗng tạo Dictionary, không phải Set. |
| Q8 | **D** | Empty curly braces denote a dictionary. | Cặp ngoặc nhọn rỗng biểu thị Dictionary. |
| Q9 | **A** | The | operator includes elements present in either set. | Toán tử | lấy các phần tử thuộc ít nhất một tập. |
| Q10 | **B** | The & operator keeps elements present in both sets. | Toán tử & chỉ lấy phần tử chung. |
| Q11 | **C** | Set difference subtracts members of b from a. | Hiệu tập hợp loại khỏi a những phần tử đã có trong b. |
| Q12 | **D** | Symmetric difference keeps values present in exactly one set. | Hiệu đối xứng lấy phần tử chỉ có ở đúng một tập. |
| Q13 | **A** | Duplicate ones collapse to one value. | Hai giá trị 1 trùng nhau chỉ còn một phần tử. |
| Q14 | **B** | Tuples disallow item assignment. | Tuple không cho phép gán lại phần tử theo chỉ số. |
| Q15 | **C** | The `in` operator tests whether a value belongs to a set. | Toán tử `in` kiểm tra giá trị có thuộc Set hay không. |
| Q16 | **D** | Sets do not promise an iteration or display order. | Set không cam kết thứ tự duyệt hoặc hiển thị cố định. |
| Q17 | **A** | Ordered coordinates can be packaged as an immutable pair. | Hai tọa độ theo thứ tự có thể lưu bằng Tuple không sửa trực tiếp. |
| Q18 | **B** | Sets preserve distinct values automatically. | Set tự giữ các giá trị khác nhau. |
| Q19 | **C** | isdisjoint returns True when the intersection is empty. | isdisjoint trả True khi phép giao rỗng. |
| Q20 | **D** | sorted returns an ordered list without changing the set. | sorted trả List có thứ tự mà không sửa Set. |

## 8. Nối sang bài tiếp theo

`List → Tuple và Set → Tập hợp/Jaccard`.
