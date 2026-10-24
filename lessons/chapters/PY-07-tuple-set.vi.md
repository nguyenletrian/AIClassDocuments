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

A. An ordered mutable sequence — Dãy có thứ tự và có thể sửa

B. An unordered collection of unique items — Tập hợp không thứ tự của phần tử duy nhất

C. A key-to-value mapping — Ánh xạ khóa–giá trị

D. An ordered immutable collection — Tập hợp có thứ tự và bất biến

**Q2. What is a set? — Set là gì?**

A. An ordered collection of key-value entries — Tập hợp có thứ tự các cặp khóa–giá trị

B. A collection that always keeps duplicates — Tập hợp luôn giữ giá trị trùng

C. A collection of unique hashable members — Tập hợp gồm phần tử có thể băm và không trùng

D. A sequence accessed by positional indexes — Dãy truy cập bằng chỉ số vị trí

**Q3. What does set union collect? — Phép hợp Set lấy gì?**

A. Only members of the first set not in the second — Chỉ phần tử tập đầu mà không thuộc tập sau

B. Distinct members appearing in either set — Phần tử khác nhau thuộc ít nhất một tập

C. Only members appearing in exactly one set — Chỉ phần tử thuộc đúng một tập

D. Only members common to both sets — Chỉ phần tử chung của hai tập

**Q4. What does set intersection collect? — Phép giao Set lấy gì?**

A. Only members of the first set — Chỉ phần tử tập đầu

B. Members occurring in exactly one set — Phần tử xuất hiện đúng một tập

C. Only members shared by both sets — Chỉ phần tử chung của cả hai tập

D. All distinct members of either set — Mọi phần tử khác nhau thuộc ít nhất một tập

**Q5. Which expression constructs a two-element tuple? — Biểu thức nào tạo Tuple có hai phần tử?**

A. `(2, 3)` — `(2, 3)`

B. `[2, 3]` — `[2, 3]`

C. `{2, 3}` — `{2, 3}`

D. `{2: 3}` — `{2: 3}`

**Q6. Which expression constructs a nonempty set? — Biểu thức nào tạo Set không rỗng?**

A. `[2, 3]` — `[2, 3]`

B. `{2: 3}` — `{2: 3}`

C. `(2, 3)` — `(2, 3)`

D. `{2, 3}` — `{2, 3}`

**Q7. Which expression constructs an empty set? — Biểu thức nào tạo Set rỗng?**

A. `[]` — `[]`

B. `set()` — `set()`

C. `()` — `()`

D. `{}` — `{}`

**Q8. Which expression constructs an empty dictionary? — Biểu thức nào tạo Dictionary rỗng?**

A. `set()` — `set()`

B. `[]` — `[]`

C. `()` — `()`

D. `{}` — `{}`

**Q9. What does `a | b` do for sets? — `a | b` làm gì với hai Set?**

A. Set difference from `a` to `b` — Hiệu Set từ `a` trừ `b`

B. Symmetric difference — Hiệu đối xứng

C. Set union — Phép hợp Set

D. Set intersection — Phép giao Set

**Q10. What does `a & b` do for sets? — `a & b` làm gì với hai Set?**

A. Set intersection — Phép giao Set

B. Set difference — Phép hiệu Set

C. Symmetric difference — Hiệu đối xứng

D. Set union — Phép hợp Set

**Q11. What does `a - b` do for sets? — `a - b` làm gì với hai Set?**

A. Members in `a` but not in `b` — Phần tử thuộc `a` nhưng không thuộc `b`

B. Members in exactly one input — Phần tử thuộc đúng một tập

C. Set union — Phép hợp Set

D. Set intersection — Phép giao Set

**Q12. What does `a ^ b` do for sets? — `a ^ b` làm gì với hai Set?**

A. Set union — Phép hợp Set

B. Set intersection — Phép giao Set

C. Members of `a` only — Chỉ phần tử của `a`

D. Members in exactly one of the sets — Phần tử thuộc đúng một trong hai tập

**Q13. What is the length of `set([1,1,2])`? — `set([1,1,2])` có bao nhiêu phần tử?**

A. `2` — `2`

B. `3` — `3`

C. `1` — `1`

D. `ValueError` — `ValueError`

**Q14. What happens when assigning `t[0] = 9` on a tuple? — Gán `t[0] = 9` trên Tuple sẽ thế nào?**

A. A `TypeError` is raised — Phát sinh `TypeError`

B. A new tuple is created automatically — Tự động tạo Tuple mới

C. An `IndexError` is always raised — Luôn phát sinh `IndexError`

D. The tuple's first item changes to 9 — Phần tử đầu Tuple đổi thành 9

**Q15. How do you test membership in a set? — Làm sao kiểm tra một giá trị thuộc Set?**

A. `s[x]` — `s[x]`

B. `x in s` — `x in s`

C. `x == s` — `x == s`

D. `s.index(x)` — `s.index(x)`

**Q16. Is order of printed set elements guaranteed? — Thứ tự phần tử in từ Set có được bảo đảm không?**

A. Always sorted in ascending order — Luôn theo thứ tự tăng dần

B. Always insertion order — Luôn theo thứ tự thêm vào

C. Always a new random permutation — Luôn tạo hoán vị ngẫu nhiên mới

D. No fixed display order is guaranteed — Không bảo đảm thứ tự hiển thị cố định

**Q17. Which built-in immutable ordered sequence best represents a fixed coordinate pair `(x, y)`? — Kiểu dãy có thứ tự và bất biến nào phù hợp nhất biểu diễn cặp tọa độ cố định `(x, y)`?**

A. Dictionary — Dictionary

B. Tuple — Tuple

C. List — List

D. Set — Set

**Q18. Which built-in collection directly keeps only distinct tags? — Kiểu tập hợp nào trực tiếp chỉ giữ những nhãn khác nhau?**

A. String, which holds one sequence of characters — String lưu dãy ký tự

B. Tuple, which retains duplicates — Tuple giữ nguyên các phần tử trùng

C. Set, which retains distinct tags — Set chỉ giữ nhãn khác nhau

D. List, which retains duplicates — List giữ nguyên các phần tử trùng

**Q19. Which method checks whether sets share no elements? — Phương thức nào kiểm tra hai Set không có phần tử chung?**

A. `union()` — `union()`

B. `isdisjoint()` — `isdisjoint()`

C. `intersection()` — `intersection()`

D. `issubset()` — `issubset()`

**Q20. Which function creates a sorted list from a set? — Hàm nào tạo List đã sắp từ một Set?**

A. `list(s)` without ordering — `list(s)` không sắp xếp

B. `reversed(s)` — `reversed(s)`

C. `sorted(s)` — `sorted(s)`

D. `s.sort()` — `s.sort()`

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **D** | A tuple is an ordered, immutable sequence: `(2, 3)` keeps the first coordinate before the second, but item assignment is not allowed. A list is also ordered, yet its elements can be changed. | Tuple là dãy có thứ tự và bất biến: `(2, 3)` giữ tọa độ đầu trước tọa độ sau, nhưng không cho phép gán lại từng phần tử. List cũng có thứ tự nhưng có thể sửa các phần tử. |
| Q2 | **C** | A set stores distinct hashable members and does not support positional indexing. Creating `set([1, 1, 2])` leaves the two distinct members `1` and `2`, unlike a list that preserves duplicates. | Set chứa các phần tử có thể băm và không trùng nhau, đồng thời không hỗ trợ truy cập theo chỉ số vị trí. Tạo `set([1, 1, 2])` chỉ còn hai phần tử `1` và `2`, khác List vốn giữ phần tử lặp. |
| Q3 | **B** | Union contains every distinct element appearing in at least one of the two sets. For `{1, 2}` and `{2, 3}`, union contains `{1, 2, 3}`; intersection would keep only the common member `2`. | Phép hợp lấy mỗi phần tử khác nhau xuất hiện trong ít nhất một tập. Với `{1, 2}` và `{2, 3}`, hợp chứa `{1, 2, 3}`; phép giao chỉ giữ phần tử chung `2`. |
| Q4 | **C** | Intersection keeps only the members common to both inputs. For `{1, 2}` and `{2, 3}`, the intersection is `{2}`; this is narrower than the union `{1, 2, 3}`. | Phép giao chỉ giữ phần tử có mặt ở cả hai tập. Với `{1, 2}` và `{2, 3}`, giao là `{2}`; tập này nhỏ hơn phép hợp `{1, 2, 3}`. |
| Q5 | **A** | `(2, 3)` is a tuple with two ordered elements because of the comma-separated expression. By contrast, `{2, 3}` is a set and `[2, 3]` is a mutable list. | `(2, 3)` là Tuple gồm hai phần tử có thứ tự với các giá trị phân cách bằng dấu phẩy. Ngược lại, `{2, 3}` là Set và `[2, 3]` là List có thể sửa. |
| Q6 | **D** | `{2, 3}` constructs a nonempty set of two unique integers. Parentheses create a tuple and square brackets create a list, whereas empty braces `{}` create a dictionary. | `{2, 3}` tạo Set không rỗng gồm hai số nguyên khác nhau. Dấu ngoặc tròn tạo Tuple và ngoặc vuông tạo List, còn ngoặc nhọn rỗng `{}` tạo Dictionary. |
| Q7 | **B** | `set()` constructs the empty set. The visually similar `{}` is an empty dictionary, so using braces alone will not create a set with zero members. | `set()` tạo Set rỗng. Ký hiệu gần giống `{}` lại là Dictionary rỗng, vì vậy không thể dùng cặp ngoặc nhọn trống để tạo Set không có phần tử. |
| Q8 | **D** | `{}` denotes an empty dictionary, a key-to-value mapping with no entries. For an empty set use `set()` instead; for an empty list or tuple use `[]` or `()`. | `{}` biểu diễn Dictionary rỗng, tức ánh xạ khóa–giá trị chưa có mục nào. Muốn tạo Set rỗng phải dùng `set()`; List và Tuple rỗng lần lượt là `[]` và `()`. |
| Q9 | **C** | For sets, `a &#124; b` computes union, retaining distinct elements found in `a`, `b`, or both. With `a={1,2}` and `b={2,3}`, the result contains 1, 2 and 3, unlike intersection which retains only 2. | Với Set, `a &#124; b` thực hiện phép hợp, giữ phần tử khác nhau thuộc `a`, `b` hoặc cả hai. Nếu `a={1,2}` và `b={2,3}`, kết quả chứa 1, 2, 3, khác giao vốn chỉ giữ 2. |
| Q10 | **A** | `a & b` is set intersection, keeping only values present in both sets. For `{1,2}` and `{2,3}`, it returns `{2}`; it does not collect every distinct member as union does. | `a & b` là phép giao Set, chỉ giữ giá trị xuất hiện ở cả hai tập. Với `{1,2}` và `{2,3}`, kết quả là `{2}`; nó không lấy mọi phần tử khác nhau như phép hợp. |
| Q11 | **A** | `a - b` keeps members in `a` that are absent from `b`, so order matters: `{1,2} - {2,3}` is `{1}`. Reversing operands instead gives `{3}`, unlike symmetric difference which retains both 1 and 3. | `a - b` chỉ giữ phần tử thuộc `a` mà không thuộc `b`, nên thứ tự hai vế quan trọng: `{1,2} - {2,3}` cho `{1}`. Đảo hai vế lại được `{3}`, khác hiệu đối xứng giữ cả 1 và 3. |
| Q12 | **D** | `a ^ b` computes symmetric difference: members found in exactly one of the two sets. For `{1,2}` and `{2,3}`, the result contains 1 and 3 but excludes shared member 2. | `a ^ b` tính hiệu đối xứng: lấy phần tử có mặt đúng ở một trong hai tập. Với `{1,2}` và `{2,3}`, kết quả chứa 1 và 3 nhưng loại phần tử chung 2. |
| Q13 | **A** | Building a set removes duplicates, so `set([1,1,2])` has only members 1 and 2. Its length is therefore integer `2`, not the three positions of the original list. | Tạo Set sẽ loại giá trị trùng, vì vậy `set([1,1,2])` chỉ còn phần tử 1 và 2. Độ dài do đó bằng số nguyên `2`, không phải ba vị trí của List gốc. |
| Q14 | **A** | Tuples disallow item assignment, so trying `t[0] = 9` on a tuple raises `TypeError`. This differs from a list, where replacing an existing indexed item is allowed. | Tuple không cho phép gán lại từng phần tử nên `t[0] = 9` trên Tuple gây `TypeError`. Khác với List, việc gán vào một chỉ số hợp lệ được cho phép. |
| Q15 | **B** | Membership is tested with `x in s`, which produces a Boolean. For `s={1,3}`, `3 in s` is `True` and `2 in s` is `False`; sets do not have a positional `.index()` method. | Dùng `x in s` để kiểm tra phần tử, kết quả là Boolean. Với `s={1,3}`, `3 in s` là `True` và `2 in s` là `False`; Set không có phương thức `.index()` theo vị trí. |
| Q16 | **D** | A set does not guarantee the order used when displaying or iterating its elements. Even if a particular example prints `{1, 2, 3}`, do not rely on that order in later runs; sorting the set is a separate operation. | Set không bảo đảm thứ tự khi hiển thị hay duyệt các phần tử. Dù một lần chạy in `{1, 2, 3}`, không nên phụ thuộc thứ tự đó ở các lần sau; sắp xếp Set là thao tác riêng. |
| Q17 | **B** | An immutable ordered pair such as `(x, y)` fits a fixed coordinate because the first and second positions retain their meanings. A set would lose positional access and a list would permit item reassignment. | Một cặp có thứ tự và bất biến như `(x, y)` phù hợp tọa độ cố định vì vị trí thứ nhất và thứ hai có ý nghĩa riêng. Set không truy cập theo vị trí, còn List cho phép gán lại phần tử. |
| Q18 | **C** | A set directly removes duplicate tags because each equal member can appear only once. For tags `['red', 'red', 'blue']`, creating a set retains the distinct labels `red` and `blue`, although their order is not guaranteed. | Set trực tiếp loại nhãn trùng vì mỗi giá trị chỉ xuất hiện một lần. Với nhãn `['red', 'red', 'blue']`, tạo Set giữ hai nhãn khác nhau `red` và `blue`, nhưng không bảo đảm thứ tự. |
| Q19 | **B** | `a.isdisjoint(b)` returns `True` exactly when the two sets share no elements. For `{1,2}` and `{3}`, it is `True`, whereas `{1,2}` and `{2,4}` yield `False`. | `a.isdisjoint(b)` trả `True` khi và chỉ khi hai Set không có phần tử chung. Với `{1,2}` và `{3}`, kết quả là `True`, còn `{1,2}` và `{2,4}` cho `False`. |
| Q20 | **C** | `sorted(s)` returns a new list whose items are ordered, for example `sorted({3,1,2})` yields `[1,2,3]`. It does not impose lasting order on the original set, which remains unordered. | `sorted(s)` trả về List mới đã sắp xếp, ví dụ `sorted({3,1,2})` cho `[1,2,3]`. Nó không tạo thứ tự cố định cho Set gốc, vốn vẫn là tập không có thứ tự vị trí. |

## 8. Nối sang bài tiếp theo

`List → Tuple và Set → Tập hợp/Jaccard`.
