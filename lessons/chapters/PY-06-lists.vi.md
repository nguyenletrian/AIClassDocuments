# PY-06 — List, chỉ số, cắt danh sách và sắp xếp


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **List** — danh sách; **Index** — chỉ số.

`Vòng lặp → List → Vector/Array`

Sau khi học vòng lặp, ta dùng List để lưu nhiều giá trị trong cùng một biến. Có thể thêm, xóa, sửa, sắp xếp và duyệt từng phần tử.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích dễ nhớ |
|---|---|---|
| List | danh sách | Tập hợp có thứ tự, có thể thay đổi |
| Index | chỉ số | Vị trí tính từ 0 để lấy phần tử |
| Slice | cắt lát | Lấy đoạn phần tử theo start:stop |
| Mutability | khả năng sửa | Có thể cập nhật phần tử của danh sách |

## 3. Hàm và cú pháp Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cú pháp | Mục đích và lựa chọn liên quan |
|---|---|
| `append(), extend(), insert()` | Thêm từng phần tử hoặc nhiều phần tử vào danh sách |
| `pop(), remove(), del` | Xóa theo vị trí hoặc giá trị |
| `sort(), sorted()` | Sắp xếp tại chỗ hoặc tạo danh sách mới |
| `items[start:stop]` | Lấy vùng con không bao gồm stop |

## 4. Khái niệm liên quan

Một cửa hàng cần ghi các món trong giỏ theo đúng thứ tự khách thêm vào. **List** là cấu trúc Python lưu nhiều giá trị trong một biến, được viết bằng dấu ngoặc vuông `[]`. Từ giỏ hàng này, ta lần lượt học cách tạo danh sách, tìm theo vị trí, lấy một đoạn và thay đổi một món; đó cũng là nền tảng để duyệt dữ liệu bằng vòng `for`.

### 4.1. List — Danh sách

**Từ vựng trong mục:** **List** — danh sách; **Element** — phần tử.

List giữ các phần tử theo thứ tự, và mỗi phần tử có thể là tên món hàng, số hoặc một kiểu dữ liệu khác. Giỏ hàng ban đầu gồm `milk` (sữa) và `bread` (bánh mì); ta đặt cả hai vào biến `basket` để xử lý cùng nhau. Dùng dấu `[]` để tạo danh sách, dấu phẩy ngăn cách các phần tử.

```python
basket = ['milk', 'bread']
print(basket)
```

**Kết quả khi chạy:**

```text
['milk', 'bread']
```

Danh sách có hai phần tử theo thứ tự sữa trước, bánh mì sau. Khác với một chuỗi dài, từng món có thể được truy cập và thay đổi riêng.

### 4.2. Index — Vị trí phần tử

**Từ vựng trong mục:** **Index** — chỉ số; **Element** — phần tử.

Khi biết món cần lấy nằm ở vị trí nào, ta dùng **chỉ số**. Python bắt đầu đếm từ `0`: với `['milk', 'bread']`, `basket[0]` là `milk`, còn `basket[1]` là `bread`; `basket[-1]` cũng chỉ phần tử cuối. Chỉ số nằm ngoài giới hạn danh sách sẽ gây `IndexError`.

```python
basket = ['milk', 'bread']
print(basket[0])
```

**Kết quả khi chạy:**

```text
milk
```

Chỉ số `0` lấy đúng món sữa ở vị trí đầu tiên, không phải phần tử thứ hai.

### 4.3. Slice — Lấy một đoạn danh sách

**Từ vựng trong mục:** **Slice** — cắt lát; **Start/stop** — vị trí bắt đầu/kết thúc.

Nếu giỏ có ba món `milk`, `bread`, `rice` và chỉ muốn lấy hai món đầu, ta dùng `basket[:2]`. Với lát cắt `[start:stop]`, vị trí `start` được lấy, còn `stop` **không được lấy**. Bỏ trống `start` nghĩa là bắt đầu từ đầu danh sách. Lát cắt tạo list mới, không xóa phần tử khỏi giỏ gốc.

```python
basket = ['milk', 'bread', 'rice']
print(basket[:2])
```

**Kết quả khi chạy:**

```text
['milk', 'bread']
```

Kết quả gồm sữa và bánh mì; `rice` ở chỉ số `2` nằm ngoài đoạn được lấy.

### 4.4. Mutability — Thay đổi nội dung danh sách

**Từ vựng trong mục:** **Mutability** — khả năng thay đổi; **Assignment** — phép gán.

Khác với tuple ở bài kế tiếp, **List là kiểu có thể sửa** sau khi tạo. Nếu cửa hàng đổi món thứ hai từ `bread` thành `rice`, ta gán trực tiếp `basket[1] = 'rice'`. Danh sách vẫn có hai phần tử, chỉ giá trị tại vị trí 1 được thay. Muốn thêm món mới vào cuối thì dùng `append()`, không phải phép gán này.

```python
basket = ['milk', 'bread']
basket[1] = 'rice'
print(basket)
```

**Kết quả khi chạy:**

```text
['milk', 'rice']
```

Món thứ hai đổi thành gạo; món sữa đầu tiên vẫn giữ nguyên.
### 4.5. Sorting — Sắp xếp List

**Từ vựng trong mục:** **Sorting** — sắp xếp; **Ascending/descending** — tăng dần/giảm dần.

Khi có điểm ưu tiên `[7, 9, 4]`, ta thường muốn xem điểm cao trước. Hàm `sorted(scores, reverse=True)` tạo **List mới** theo thứ tự giảm dần; `reverse=False` (mặc định) cho thứ tự tăng dần. List ban đầu không bị sửa bởi `sorted()`, khác với phương thức `scores.sort()` vốn sắp xếp trực tiếp List gốc. Với ví dụ này, điểm 9 đứng đầu, rồi 7 và 4.

```python
scores = [7, 9, 4]
ranked = sorted(scores, reverse=True)
print(ranked)
```

**Kết quả khi chạy:**

```text
[9, 7, 4]
```

Danh sách kết quả được sắp theo điểm giảm dần. Các điểm số không bị thay đổi, chỉ thứ tự của chúng khác đi.

## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Giỏ hàng

**Từ vựng trong mục:** **List** — danh sách.

**Tình huống thực tế:** Một cửa hàng đang có giỏ hàng gồm `milk` (sữa) và `bread` (bánh mì). Khách muốn thêm `rice` (gạo) vào cuối giỏ.

**Yêu cầu:** In danh sách hàng sau khi thêm gạo.

**Vì sao chọn cách giải này?** `append()` thêm một phần tử vào cuối list mà vẫn giữ các món trước đó.

**Quy trình giải:**

1. Tạo list `basket` gồm sữa và bánh mì.
2. Gọi `basket.append("rice")`.
3. In toàn bộ giỏ hàng.

```python
basket=["milk","bread"]
basket.append("rice")
print(basket)
```

**Kết quả khi chạy:**

```text
['milk', 'bread', 'rice']
```

**Kết quả:** `['milk', 'bread', 'rice']` — giỏ có ba món theo đúng thứ tự.

### Tình huống 2 — Lấy hai ưu tiên cao

**Từ vựng trong mục:** **Index** — chỉ số.

**Tình huống thực tế:** Một đội hỗ trợ nhận điểm ưu tiên của bốn yêu cầu là `[2, 9, 4, 7]`; điểm càng lớn thì yêu cầu càng cần xử lý trước.

**Yêu cầu:** In hai điểm ưu tiên cao nhất mà không thay đổi list gốc.

**Vì sao chọn cách giải này?** `sorted(..., reverse=True)` tạo danh sách mới từ cao xuống thấp, rồi `[:2]` lấy hai giá trị đầu.

**Quy trình giải:**

1. Lưu bốn điểm vào `scores`.
2. Sắp xếp giảm dần bằng `sorted(scores, reverse=True)`.
3. Cắt `[:2]` và in kết quả.

```python
scores=[2,9,4,7]
print(sorted(scores,reverse=True)[:2])
```

**Kết quả khi chạy:**

```text
[9, 7]
```

**Kết quả:** `[9, 7]` — hai mức ưu tiên cao nhất. List `scores` gốc không bị thay đổi.

### Tình huống 3 — Lọc điểm đạt

**Từ vựng trong mục:** **Slice** — cắt lát.

**Tình huống thực tế:** Trung tâm đào tạo có điểm của bốn học viên là `[4, 7, 9, 3]` trên thang 10. Điểm đạt yêu cầu là từ 5 trở lên.

**Yêu cầu:** Tạo list mới chỉ chứa điểm đạt.

**Vì sao chọn cách giải này?** List comprehension `[x for x in scores if x >= 5]` duyệt từng điểm và chỉ giữ giá trị đạt ngưỡng.

**Quy trình giải:**

1. Lưu điểm vào `scores`.
2. Với mỗi `x`, kiểm tra `x >= 5`.
3. Thêm các điểm đạt vào `passed` và in list mới.

```python
scores=[4,7,9,3]
passed=[x for x in scores if x>=5]
print(passed)
```

**Kết quả khi chạy:**

```text
[7, 9]
```

**Kết quả:** `[7, 9]` — hai điểm đạt, vẫn giữ thứ tự xuất hiện ban đầu.

### Tình huống 4 — Sửa tồn kho

**Từ vựng trong mục:** **Mutability** — khả năng sửa.

**Tình huống thực tế:** Kho lưu số lượng ba mặt hàng trong list `[8, 6, 9]`. Sau kiểm kê, mặt hàng thứ hai thực tế còn 4 sản phẩm, không phải 6.

**Yêu cầu:** Sửa lại số lượng mặt hàng thứ hai rồi in danh sách tồn kho mới.

**Vì sao chọn cách giải này?** List có thể chỉnh trực tiếp theo chỉ số; mặt hàng thứ hai nằm ở chỉ số `1`.

**Quy trình giải:**

1. Lưu `[8, 6, 9]` vào `stock`.
2. Gán `stock[1] = 4`.
3. In danh sách sau khi sửa.

```python
stock=[8,6,9]
stock[1]=4
print(stock)
```

**Kết quả khi chạy:**

```text
[8, 4, 9]
```

**Kết quả:** `[8, 4, 9]` — chỉ số lượng mặt hàng thứ hai được cập nhật.

### Tình huống 5 — Hàng đợi yêu cầu

**Từ vựng trong mục:** **List** — danh sách.

**Tình huống thực tế:** Bộ phận hỗ trợ đang xử lý ba yêu cầu theo thứ tự `REQ01`, `REQ02`, `REQ03`. Yêu cầu đến trước phải được xử lý trước.

**Yêu cầu:** Lấy yêu cầu đầu hàng đợi ra để xử lý và in danh sách còn lại.

**Vì sao chọn cách giải này?** `pop(0)` lấy và xóa phần tử đầu list; phù hợp để minh họa hàng đợi nhỏ. Với hàng đợi lớn hoặc thường xuyên lấy đầu, `collections.deque` phù hợp hơn.

**Quy trình giải:**

1. Tạo list `queue` theo thứ tự yêu cầu đến.
2. Dùng `pop(0)` lấy yêu cầu đầu vào biến `done`.
3. In mã đã xử lý và list còn lại.

```python
queue=["REQ01","REQ02","REQ03"]
done=queue.pop(0)
print(done,queue)
```

**Kết quả khi chạy:**

```text
REQ01 ['REQ02', 'REQ03']
```

**Kết quả:** `REQ01 ['REQ02', 'REQ03']` — yêu cầu đầu đã được lấy ra, hai yêu cầu còn lại giữ nguyên thứ tự.

## 6. Nhầm lẫn dễ gặp

- Chỉ số list bắt đầu từ `0`; truy cập vượt ngoài list gây `IndexError`.
- `append([3,4])` thêm cả list như một phần tử, còn `extend([3,4])` thêm lần lượt `3` và `4`.
- `list.sort()` sửa list gốc và trả về `None`; `sorted(list)` tạo list mới.
- `pop(0)` sẽ lỗi nếu list rỗng. Với hàng đợi lớn, nên dùng `collections.deque`.
- Cắt list bằng `[:2]` không lấy phần tử có chỉ số `2`.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a Python List? — List trong Python là gì?**

A. A mapping of keys to values — Ánh xạ từ khóa sang giá trị

B. An ordered, mutable collection — Tập hợp có thứ tự và có thể sửa

C. An unordered collection of unique items — Tập hợp không thứ tự gồm phần tử duy nhất

D. An immutable sequence of items — Dãy phần tử bất biến

**Q2. What is the index of the first list element? — Chỉ số của phần tử List đầu tiên là gì?**

A. `0` — `0`

B. `-1` — `-1`

C. `len(a)` — `len(a)`

D. `1` — `1`

**Q3. For a List `a`, what does `a[:2]` return? — Với `a` là một List, `a[:2]` trả về gì?**

A. Items from index 2 to the end — Các phần tử từ chỉ số 2 đến cuối

B. A new list of the first two items — List mới gồm hai phần tử đầu

C. A new list of the last two items — List mới gồm hai phần tử cuối

D. Only item at index 2 — Chỉ phần tử tại chỉ số 2

**Q4. What does 'mutable' mean for a list? — List có tính mutable nghĩa là gì?**

A. Its contents can be changed after creation — Có thể sửa nội dung sau khi tạo

B. Its elements cannot be changed — Không thể sửa các phần tử

C. Every element must have the same type — Mọi phần tử phải cùng kiểu

D. Its elements sort automatically — Các phần tử được tự động sắp xếp

**Q5. What does `append(x)` do? — `append(x)` làm gì?**

A. Inserts `x` before the first item — Chèn `x` trước phần tử đầu

B. Removes the final element and returns it — Xóa phần tử cuối và trả về

C. Adds `x` as a single final item — Thêm `x` thành một phần tử cuối

D. Adds every element of `x` separately — Thêm riêng từng phần tử của `x`

**Q6. What does `extend(items)` do? — `extend(items)` làm gì?**

A. Deletes items matching `items` — Xóa phần tử khớp `items`

B. Appends the iterable as one nested item — Thêm cả iterable thành một phần tử lồng

C. Adds the individual elements from `items` — Thêm từng phần tử từ `items`

D. Replaces the first element with `items` — Thay phần tử đầu bằng `items`

**Q7. What does `insert(0, x)` do? — `insert(0, x)` làm gì?**

A. Replaces the first element with `x` — Thay phần tử đầu bằng `x`

B. Inserts `x` at the front, shifting the others — Chèn `x` vào đầu, đẩy các phần tử khác sang phải

C. Removes the first element — Xóa phần tử đầu

D. Adds `x` at the end — Thêm `x` vào cuối

**Q8. What does `pop(0)` do on a nonempty list? — `pop(0)` làm gì với List không rỗng?**

A. Removes and returns the last item — Xóa và trả phần tử cuối

B. Returns the first item without removing it — Trả phần tử đầu nhưng không xóa

C. Deletes the first occurrence of the value zero — Xóa lần xuất hiện đầu của giá trị không

D. Removes and returns the first item — Xóa và trả phần tử đầu

**Q9. What does `remove(x)` do? — `remove(x)` dùng để làm gì?**

A. Deletes every matching value — Xóa tất cả giá trị khớp

B. Returns a sorted copy — Trả bản sao đã sắp xếp

C. Deletes the first matching value — Xóa giá trị khớp đầu tiên

D. Deletes the item at index `x` — Xóa phần tử tại chỉ số `x`

**Q10. What does `del a[1]` do? — `del a[1]` có tác dụng gì?**

A. Returns the removed item — Trả về phần tử đã xóa

B. Deletes the item whose value is `1` — Xóa phần tử có giá trị bằng `1`

C. Deletes the item at index one — Xóa phần tử có chỉ số 1

D. Replaces the item at index one with `None` — Thay phần tử chỉ số 1 bằng `None`

**Q11. What does `a.sort()` return? — `a.sort()` trả về gì?**

A. The sorted indexes — Các chỉ số đã sắp xếp

B. A new sorted list — List mới đã sắp xếp

C. The same list as a return value — Trả về chính List đó

D. `None` — `None`

**Q12. What does `sorted(a)` do? — `sorted(a)` làm gì?**

A. Reverses the original list in place — Đảo List gốc tại chỗ

B. Produces a set of unique items — Tạo Set các phần tử duy nhất

C. Creates a new sorted list — Tạo List mới đã sắp xếp

D. Sorts `a` in place and returns `None` — Sắp `a` tại chỗ và trả `None`

**Q13. What does `a[-1]` read from a nonempty list? — `a[-1]` lấy gì từ List không rỗng?**

A. The last element — Phần tử cuối

B. The first element — Phần tử đầu

C. The number of elements — Số phần tử

D. An `IndexError` for every nonempty list — Luôn có `IndexError` với List không rỗng

**Q14. What does `len(a)` report? — `len(a)` cho biết gì?**

A. The number of distinct values — Số giá trị khác nhau

B. The list's memory size in bytes — Kích thước List tính theo byte

C. The final valid index — Chỉ số hợp lệ cuối

D. The number of elements — Số phần tử

**Q15. What happens for `a[10]` on a two-item list? — `a[10]` sẽ thế nào nếu List có hai phần tử?**

A. The last list element — Phần tử cuối List

B. `None` — `None`

C. The integer `0` — Số nguyên `0`

D. `IndexError` — `IndexError`

**Q16. What does `a[1] = 5` do? — `a[1] = 5` làm gì?**

A. Changes the first item to `5` — Thay phần tử đầu thành `5`

B. Replaces the second element with `5` — Thay phần tử thứ hai bằng `5`

C. Inserts a new element at index 1 — Chèn phần tử mới tại chỉ số 1

D. Adds `5` to the end — Thêm `5` vào cuối

**Q17. Which operation sorts a list in place? — Thao tác nào sắp xếp ngay List gốc?**

A. `a.sort()` — `a.sort()`

B. `sorted(a)` — `sorted(a)`

C. `a.reverse()` — `a.reverse()`

D. `reversed(a)` — `reversed(a)`

**Q18. Which expression sorts without mutating the original? — Biểu thức nào sắp xếp mà không sửa List gốc?**

A. `sorted(a)` — `sorted(a)`

B. `a.reverse()` — `a.reverse()`

C. `a.extend(sorted(a))` — `a.extend(sorted(a))`

D. `a.sort()` — `a.sort()`

**Q19. What does `reverse=True` mean in a numeric sort? — `reverse=True` có ý nghĩa gì khi sắp xếp số?**

A. Reverse each number's digits — Đảo chữ số trong từng số

B. Ascending order — Thứ tự tăng dần

C. Random element order — Thứ tự phần tử ngẫu nhiên

D. Descending numeric order — Thứ tự số giảm dần

**Q20. How do `append([3,4])` and `extend([3,4])` differ? — `append([3,4])` và `extend([3,4])` khác gì?**

A. Both operations sort the existing list — Cả hai đều sắp xếp List

B. `append` adds one nested list; `extend` adds two elements — `append` thêm một List con; `extend` thêm hai phần tử

C. Both operations create the same flat list — Cả hai tạo cùng List phẳng

D. `append` adds both separately and `extend` nests them — `append` thêm riêng còn `extend` lồng List

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | A Python list is an ordered, mutable collection, so elements have positions and can be changed after creation. For example `[10, 20]` stores two items whose order matters; a set does not provide positional indexing. | List trong Python là tập hợp có thứ tự và có thể thay đổi, nên mỗi phần tử có vị trí và có thể được sửa sau khi tạo. Ví dụ `[10, 20]` chứa hai phần tử theo thứ tự xác định; set không hỗ trợ chỉ số vị trí. |
| Q2 | **A** | List indexes start from `0`, so `a[0]` selects the first item and `a[1]` the second. Negative index `-1` has a different meaning: the last item. | Chỉ số List bắt đầu từ `0`, vì vậy `a[0]` lấy phần tử đầu và `a[1]` lấy phần tử thứ hai. Chỉ số âm `-1` mang nghĩa khác: phần tử cuối. |
| Q3 | **B** | The slice `a[:2]` starts at index zero by default and stops before index two, yielding a new list of the first two items. For `[4, 5, 6]`, the result is `[4, 5]`, not the single item at index two. | Lát cắt `a[:2]` mặc định bắt đầu tại chỉ số 0 và dừng trước chỉ số 2, tạo List mới gồm hai phần tử đầu. Với `[4, 5, 6]`, kết quả là `[4, 5]`, không phải phần tử tại chỉ số 2. |
| Q4 | **A** | Mutable means elements may be replaced, inserted, or deleted without creating an entirely new list. For instance, assigning `a = [1, 2]` followed by `a[0] = 9` makes `a` contain `[9, 2]`; a tuple does not allow that item assignment. | Mutable nghĩa là có thể thay, thêm hoặc xóa phần tử trên List hiện có. Ví dụ gán `a = [1, 2]` rồi thực hiện `a[0] = 9` làm `a` thành `[9, 2]`; tuple không cho phép gán phần tử như vậy. |
| Q5 | **C** | `append(x)` adds `x` as exactly one item at the end and mutates the list. For example, if `a = [1]`, calling `a.append([2, 3])` changes `a` into `[1, [2, 3]]`; `extend()` instead adds the numbers separately. | `append(x)` thêm toàn bộ `x` thành đúng một phần tử cuối List và sửa List tại chỗ. Vì vậy thêm `[2, 3]` bằng `append` vào `[1]` tạo phần tử List lồng nhau, không thêm từng số; muốn thêm từng số thì dùng `extend()`. |
| Q6 | **C** | `extend(items)` iterates over its argument and adds each item individually to the existing list. For `a = [1]`, `a.extend([2, 3])` makes `[1, 2, 3]`, while `append([2, 3])` would create `[1, [2, 3]]`. | `extend(items)` duyệt đối số và thêm từng phần tử riêng vào List hiện có. Với `a = [1]`, `a.extend([2, 3])` tạo `[1, 2, 3]`, còn `append([2, 3])` sẽ tạo `[1, [2, 3]]`. |
| Q7 | **B** | `insert(0, x)` places `x` before the current first element and shifts existing positions to the right. For example, inserting `9` into `[1, 2]` at index zero gives `[9, 1, 2]`, not a replacement of `1`. | `insert(0, x)` chèn `x` trước phần tử đầu tiên và đẩy các phần tử cũ sang phải. Ví dụ chèn `9` vào đầu `[1, 2]` cho `[9, 1, 2]`, không ghi đè số `1`. |
| Q8 | **D** | `pop(0)` removes the first item of a nonempty list and returns that removed value. For `[7, 8]`, the returned value is `7` and the remaining list is `[8]`; indexing `a[0]` alone would not remove anything. | `pop(0)` xóa phần tử đầu của List không rỗng và trả chính phần tử đã xóa. Với `[7, 8]`, kết quả trả về là `7` và List còn `[8]`; chỉ đọc `a[0]` thì không xóa phần tử nào. |
| Q9 | **C** | `remove(x)` deletes the first occurrence equal to `x`; it searches by value rather than treating `x` as an index. For `[2, 3, 2]`, `remove(2)` leaves `[3, 2]`, and a missing value raises `ValueError`. | `remove(x)` xóa lần xuất hiện đầu tiên có giá trị bằng `x`; nó tìm theo giá trị chứ không xem `x` là chỉ số. Với `[2, 3, 2]`, `remove(2)` còn `[3, 2]`, và giá trị không tồn tại sẽ gây `ValueError`. |
| Q10 | **C** | `del a[1]` removes the item at index one, which is the second item because indexing starts at zero. Unlike `remove(1)`, it uses a position; unlike `pop(1)`, the `del` statement does not return the deleted value. | `del a[1]` xóa phần tử tại chỉ số 1, tức phần tử thứ hai vì chỉ số bắt đầu từ 0. Khác `remove(1)`, lệnh này dùng vị trí; khác `pop(1)`, câu lệnh `del` không trả về giá trị bị xóa. |
| Q11 | **D** | `a.sort()` sorts the list in place and returns `None`, allowing the same list object to keep its new order. Saving `result = a.sort()` therefore gives `None`, not a newly sorted list; use `sorted(a)` to obtain a separate list. | `a.sort()` sắp List tại chỗ và trả về `None`, nên chính List cũ nhận thứ tự mới. Gán `result = a.sort()` sẽ cho `None`, không phải List mới đã sắp; muốn List riêng thì dùng `sorted(a)`. |
| Q12 | **C** | `sorted(a)` returns a new sorted list and does not reorder the original list. If `a = [3, 1]`, then `sorted(a)` is `[1, 3]` while `a` remains `[3, 1]`, unlike `a.sort()`. | `sorted(a)` trả về List mới đã sắp xếp và không đổi thứ tự List gốc. Nếu `a = [3, 1]`, `sorted(a)` là `[1, 3]` còn `a` vẫn `[3, 1]`, khác `a.sort()`. |
| Q13 | **A** | Index `-1` refers to the final element of a nonempty list, regardless of its length. For `[4, 7, 9]`, `a[-1]` yields `9`; `len(a)` instead counts all three elements. | Chỉ số `-1` chỉ phần tử cuối của List không rỗng, bất kể List dài bao nhiêu. Với `[4, 7, 9]`, `a[-1]` là `9`; còn `len(a)` đếm đủ ba phần tử. |
| Q14 | **D** | `len(a)` returns the number of top-level elements in a list, including any nested list as one element. For `[1, [2, 3]]`, the length is `2`, not `3` and not the last index `1`. | `len(a)` trả về số phần tử ở cấp ngoài của List; một List lồng trong được tính là một phần tử. Với `[1, [2, 3]]`, độ dài là `2`, không phải `3` và không phải chỉ số cuối `1`. |
| Q15 | **D** | A two-item list has valid positive indexes `0` and `1`; reading `a[10]` is out of range and raises `IndexError`. Python does not automatically return `None` or grow the list for a missing index. | List gồm hai phần tử chỉ có chỉ số dương hợp lệ `0` và `1`; đọc `a[10]` vượt giới hạn nên gây `IndexError`. Python không tự trả `None` hoặc mở rộng List khi đọc chỉ số không có. |
| Q16 | **B** | `a[1] = 5` changes the existing item at index one to `5`, provided that index exists. For `[8, 9]`, the result is `[8, 5]`; it does not insert another item or modify index zero. | `a[1] = 5` thay phần tử hiện có tại chỉ số 1 thành `5`, miễn chỉ số đó tồn tại. Với `[8, 9]`, kết quả là `[8, 5]`; lệnh không chèn thêm phần tử hay sửa chỉ số 0. |
| Q17 | **A** | `a.sort()` orders a list in place, so later reads of `a` see the sorted order. `sorted(a)` returns another list instead, while `reverse()` merely reverses existing positions without computing sort order. | `a.sort()` sắp xếp ngay trên List gốc nên đọc `a` sau đó thấy thứ tự mới. `sorted(a)` trả List khác, còn `reverse()` chỉ đảo vị trí hiện có, không tính thứ tự sắp xếp. |
| Q18 | **A** | `sorted(a)` constructs a new list in sorted order while leaving `a` unchanged. By contrast `a.sort()` modifies `a` and returns `None`, so the two should not be used interchangeably when retaining the original matters. | `sorted(a)` tạo List mới theo thứ tự sắp xếp và giữ nguyên `a`. Ngược lại `a.sort()` sửa trực tiếp `a` và trả `None`, nên không thể dùng thay nhau khi cần giữ dữ liệu gốc. |
| Q19 | **D** | In a normal numeric ascending sort, `reverse=True` reverses the comparison order to descending. For `[3, 1, 2]`, `sorted(a, reverse=True)` yields `[3, 2, 1]`, not the original reversed position order. | Trong phép sắp số mặc định tăng dần, `reverse=True` đảo thứ tự thành giảm dần. Với `[3, 1, 2]`, `sorted(a, reverse=True)` cho `[3, 2, 1]`, không đơn thuần đảo thứ tự vị trí gốc. |
| Q20 | **B** | `append([3, 4])` adds the entire inner list as one element, whereas `extend([3, 4])` adds two individual integers. Starting with `[1, 2]`, the results are `[1, 2, [3, 4]]` versus `[1, 2, 3, 4]`. | `append([3, 4])` thêm nguyên List con thành một phần tử, còn `extend([3, 4])` thêm riêng hai số nguyên. Bắt đầu từ `[1, 2]`, hai kết quả lần lượt là `[1, 2, [3, 4]]` và `[1, 2, 3, 4]`. |

## 8. Nối sang bài tiếp theo

`Vòng lặp → List → Vector/Array`.
