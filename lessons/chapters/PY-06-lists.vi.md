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

A. An ordered mutable collection — Tập hợp có thứ tự và thay đổi được

B. 0 — 0

C. A list of the first two items — List gồm hai phần tử đầu

D. Its contents can be changed after creation — Có thể đổi nội dung sau khi tạo

**Q2. What is the index of the first list element? — Chỉ số của phần tử List đầu tiên là gì?**

A. An ordered mutable collection — Tập hợp có thứ tự và thay đổi được

B. 0 — 0

C. A list of the first two items — List gồm hai phần tử đầu

D. Its contents can be changed after creation — Có thể đổi nội dung sau khi tạo

**Q3. What does `a[:2]` return? — `a[:2]` trả về gì?**

A. An ordered mutable collection — Tập hợp có thứ tự và thay đổi được

B. 0 — 0

C. A list of the first two items — List gồm hai phần tử đầu

D. Its contents can be changed after creation — Có thể đổi nội dung sau khi tạo

**Q4. What does 'mutable' mean for a list? — List có tính mutable nghĩa là gì?**

A. An ordered mutable collection — Tập hợp có thứ tự và thay đổi được

B. 0 — 0

C. A list of the first two items — List gồm hai phần tử đầu

D. Its contents can be changed after creation — Có thể đổi nội dung sau khi tạo

**Q5. What does `append(x)` do? — `append(x)` làm gì?**

A. Adds x as one item at the end — Thêm x thành một phần tử ở cuối

B. Adds each item from an iterable — Thêm từng phần tử của dữ liệu duyệt được

C. Inserts x at the front — Chèn x vào đầu List

D. Removes and returns the first item — Xóa và trả lại phần tử đầu

**Q6. What does `extend(items)` do? — `extend(items)` làm gì?**

A. Adds x as one item at the end — Thêm x thành một phần tử ở cuối

B. Adds each item from an iterable — Thêm từng phần tử của dữ liệu duyệt được

C. Inserts x at the front — Chèn x vào đầu List

D. Removes and returns the first item — Xóa và trả lại phần tử đầu

**Q7. What does `insert(0, x)` do? — `insert(0, x)` làm gì?**

A. Adds x as one item at the end — Thêm x thành một phần tử ở cuối

B. Adds each item from an iterable — Thêm từng phần tử của dữ liệu duyệt được

C. Inserts x at the front — Chèn x vào đầu List

D. Removes and returns the first item — Xóa và trả lại phần tử đầu

**Q8. What does `pop(0)` do on a nonempty list? — `pop(0)` làm gì với List không rỗng?**

A. Adds x as one item at the end — Thêm x thành một phần tử ở cuối

B. Adds each item from an iterable — Thêm từng phần tử của dữ liệu duyệt được

C. Inserts x at the front — Chèn x vào đầu List

D. Removes and returns the first item — Xóa và trả lại phần tử đầu

**Q9. What does `remove(x)` do? — `remove(x)` dùng để làm gì?**

A. Deletes the first matching value — Xóa giá trị khớp đầu tiên

B. Deletes the second indexed item — Xóa phần tử ở chỉ số 1

C. `None` — `None`

D. Creates a new sorted list — Tạo List mới đã sắp xếp

**Q10. What does `del a[1]` do? — `del a[1]` có tác dụng gì?**

A. Deletes the first matching value — Xóa giá trị khớp đầu tiên

B. Deletes the second indexed item — Xóa phần tử ở chỉ số 1

C. `None` — `None`

D. Creates a new sorted list — Tạo List mới đã sắp xếp

**Q11. What does `a.sort()` return? — `a.sort()` trả về gì?**

A. Deletes the first matching value — Xóa giá trị khớp đầu tiên

B. Deletes the second indexed item — Xóa phần tử ở chỉ số 1

C. `None` — `None`

D. Creates a new sorted list — Tạo List mới đã sắp xếp

**Q12. What does `sorted(a)` do? — `sorted(a)` làm gì?**

A. Deletes the first matching value — Xóa giá trị khớp đầu tiên

B. Deletes the second indexed item — Xóa phần tử ở chỉ số 1

C. `None` — `None`

D. Creates a new sorted list — Tạo List mới đã sắp xếp

**Q13. What does `a[-1]` read from a nonempty list? — `a[-1]` lấy gì từ List không rỗng?**

A. The last element — Phần tử cuối

B. The number of items — Số lượng phần tử

C. `IndexError` — `IndexError`

D. Replaces the second element — Thay phần tử thứ hai

**Q14. What does `len(a)` report? — `len(a)` cho biết gì?**

A. The last element — Phần tử cuối

B. The number of items — Số lượng phần tử

C. `IndexError` — `IndexError`

D. Replaces the second element — Thay phần tử thứ hai

**Q15. What happens for `a[10]` on a two-item list? — `a[10]` sẽ thế nào nếu List có hai phần tử?**

A. The last element — Phần tử cuối

B. The number of items — Số lượng phần tử

C. `IndexError` — `IndexError`

D. Replaces the second element — Thay phần tử thứ hai

**Q16. What does `a[1] = 5` do? — `a[1] = 5` làm gì?**

A. The last element — Phần tử cuối

B. The number of items — Số lượng phần tử

C. `IndexError` — `IndexError`

D. Replaces the second element — Thay phần tử thứ hai

**Q17. Which operation sorts a list in place? — Thao tác nào sắp xếp ngay List gốc?**

A. `a.sort()` — `a.sort()`

B. `sorted(a)` — `sorted(a)`

C. Descending order — Thứ tự giảm dần

D. One nested item versus two separate items — Một phần tử List con so với hai phần tử riêng

**Q18. Which expression sorts without mutating the original? — Biểu thức nào sắp xếp mà không sửa List gốc?**

A. `a.sort()` — `a.sort()`

B. `sorted(a)` — `sorted(a)`

C. Descending order — Thứ tự giảm dần

D. One nested item versus two separate items — Một phần tử List con so với hai phần tử riêng

**Q19. What does `reverse=True` mean in a numeric sort? — `reverse=True` có ý nghĩa gì khi sắp xếp số?**

A. `a.sort()` — `a.sort()`

B. `sorted(a)` — `sorted(a)`

C. Descending order — Thứ tự giảm dần

D. One nested item versus two separate items — Một phần tử List con so với hai phần tử riêng

**Q20. How do `append([3,4])` and `extend([3,4])` differ? — `append([3,4])` và `extend([3,4])` khác gì?**

A. `a.sort()` — `a.sort()`

B. `sorted(a)` — `sorted(a)`

C. Descending order — Thứ tự giảm dần

D. One nested item versus two separate items — Một phần tử List con so với hai phần tử riêng

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | A list keeps elements in sequence and permits edits. | List lưu phần tử theo thứ tự và có thể sửa. |
| Q2 | **B** | Python uses zero-based indexing. | Python đánh chỉ số bắt đầu từ 0. |
| Q3 | **C** | A slice starts at zero and stops before index two. | Lát cắt bắt đầu từ 0, dừng trước vị trí 2. |
| Q4 | **D** | Mutable lists allow item replacement or insertion. | List có thể thay phần tử hoặc chèn phần tử mới. |
| Q5 | **A** | append adds a single element to the list's end. | append thêm một phần tử ở cuối list. |
| Q6 | **B** | extend inserts elements individually from the iterable. | extend thêm lần lượt các phần tử của dãy. |
| Q7 | **C** | Inserting at index zero shifts existing items to the right. | Chèn ở chỉ số 0 đẩy các phần tử cũ sang phải. |
| Q8 | **D** | pop uses an index, unlike remove which uses a value. | pop xóa theo chỉ số, khác remove xóa theo giá trị. |
| Q9 | **A** | remove searches by value, not by index. | remove tìm theo giá trị chứ không theo chỉ số. |
| Q10 | **B** | del can delete the item at a specified index. | del xóa phần tử tại chỉ số đã chỉ định. |
| Q11 | **C** | sort modifies a list in place and returns None. | sort sắp xếp list gốc và trả về None. |
| Q12 | **D** | sorted leaves the original list unchanged. | sorted không sửa List ban đầu. |
| Q13 | **A** | Negative indices count from the end. | Chỉ số âm đếm từ cuối. |
| Q14 | **B** | len counts the elements in the list. | len đếm các phần tử có trong List. |
| Q15 | **C** | Index 10 is outside the available indices. | Chỉ số 10 vượt quá giới hạn List. |
| Q16 | **D** | A list supports assignment at valid indices. | List cho phép gán lại giá trị ở chỉ số hợp lệ. |
| Q17 | **A** | sort changes the list itself. | sort thay đổi trực tiếp List. |
| Q18 | **B** | sorted returns a separate ordered list. | sorted trả về một List mới đã sắp xếp. |
| Q19 | **C** | reverse True reverses the normal ascending sort order. | reverse True đảo thứ tự sắp xếp tăng dần mặc định. |
| Q20 | **D** | append adds the list as one value, while extend adds its contents. | append thêm cả List như một phần tử, extend thêm các phần tử bên trong. |

## 8. Nối sang bài tiếp theo

`Vòng lặp → List → Vector/Array`.
