# PY-19 — Pandas: lọc, groupby, merge và sắp xếp


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **loc** — chọn theo nhãn; **iloc** — chọn theo vị trí.

`DataFrame → lọc → nhóm → ghép bảng → AI`

**Học xong dùng để làm gì?** Gộp doanh thu theo thành phố và ghép thông tin khách hàng với đơn hàng theo khóa.

**Kết nối kiến thức tiếp theo:** PY-20 dùng logic và nguyên lý đếm để diễn đạt điều kiện và số trường hợp.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích |
|---|---|---|
| loc | chọn theo nhãn | Chọn hàng/cột theo tên |
| iloc | chọn theo vị trí | Chọn hàng/cột theo số nguyên tính từ 0 |
| groupby | nhóm dữ liệu | Gom các hàng cùng giá trị để tổng hợp |
| merge | ghép bảng | Nối bảng qua khóa chung |

## 3. Hàm Python và tham số

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm / cú pháp | Vì sao dùng |
|---|---|
| `df.loc[label]` | Chọn theo nhãn dòng/cột; slicing theo nhãn có thể gồm điểm cuối |
| `df.iloc[position]` | Chọn theo vị trí; stop của slice không bao gồm |
| `df.groupby(key).agg()` | Gộp nhóm rồi tính tổng/trung bình/số dòng |
| `pd.merge(left,right,on=,how=)` | Ghép theo khóa, cách inner/left/right/outer khác nhau |

## 4. Khái niệm liên quan

**Phân tích bảng với Pandas** thường gồm ba thao tác nối tiếp: **lọc** để giữ dòng đúng điều kiện, **nhóm** để tính thống kê theo loại, rồi **ghép** để bổ sung thông tin từ bảng khác; muốn chọn hàng chính xác cần phân biệt `.loc` theo nhãn và `.iloc` theo vị trí. Ví dụ hàng sản phẩm, giao dịch và khách hàng sẽ cho thấy vì sao cách tổ chức bảng quyết định phép xử lý.

### 4.1. Filtering, loc — Lọc hàng theo điều kiện hoặc nhãn

**Từ vựng trong mục:** **Filter** — lọc; **loc** — chọn theo nhãn.

**Lọc dữ liệu** là giữ các hàng thỏa một điều kiện. Ví dụ bảng có ba mặt hàng A, B, C, giá lần lượt 300, 900, 1200 (nghìn đồng). **Mỗi hàng** là một sản phẩm, **cột price** là giá. `df['price'] >= 800` tạo một Series Boolean; `df.loc[mask, ['name','price']]` chỉ giữ các hàng có giá từ 800 và hai cột muốn xem. `.loc` cũng chọn trực tiếp theo **nhãn index**, khác chọn vị trí số.

```python
# Mục đích: Lọc hàng theo điều kiện hoặc nhãn.
import pandas as pd

products = pd.DataFrame({'name': ['A', 'B', 'C'], 'price': [300, 900, 1200]})
selected = products.loc[products['price'] >= 800, 'name']
print(selected.tolist())
```

**Kết quả khi chạy:**

```text
['B', 'C']
```

Sản phẩm B, C thỏa mức giá; A giá 300 thấp hơn 800 nên bị loại. Kết quả chuyển sang List để tập trung vào tên.

### 4.2. iloc — Chọn theo vị trí hàng và cột

**Từ vựng trong mục:** **iloc** — chọn theo vị trí; **Index** — chỉ số.

`.iloc` chọn **vị trí số nguyên**, tính từ 0, bất kể nhãn index của bảng. Với ba khách A, B, C theo thứ tự hàng, `df.iloc[1]` là khách ở **hàng thứ hai**. Cú pháp `df.iloc[row, col]` lấy một ô, ví dụ `[1, 0]` là cột đầu của hàng hai. Trái lại `.loc['B']` chỉ hoạt động khi **nhãn index thực sự là B**, không phải chỉ vì cột `id` có chữ B.

```python
# Mục đích: Chọn theo vị trí hàng và cột.
import pandas as pd

people = pd.DataFrame({'id': ['A', 'B', 'C']})
print(people.iloc[1, 0])
```

**Kết quả khi chạy:**

```text
B
```

Chỉ số 1 lấy hàng thứ hai và chỉ số cột 0 lấy trường `id`, nên in B.

### 4.3. GroupBy — Tổng hợp trong từng nhóm

**Từ vựng trong mục:** **GroupBy** — nhóm theo khóa; **Aggregation** — phép tổng hợp.

`groupby` gom những hàng có **cùng giá trị ở một cột khóa**, rồi tính thống kê riêng cho từng nhóm. Giả sử ba giao dịch có `city = A,A,B` và `sale = 10,20,8` nghìn đồng. **Mỗi hàng** là một giao dịch; **cột city** là vùng, **sale** là tiền. `groupby('city')['sale'].sum()` cộng doanh thu của A thành 30 và B thành 8. Không nhầm GroupBy với lọc: lọc loại hàng, còn groupby kết hợp các hàng thành thống kê nhóm.

```python
# Mục đích: Tổng hợp trong từng nhóm.
import pandas as pd

sales = pd.DataFrame({'city': ['A', 'A', 'B'], 'sale': [10, 20, 8]})
print(sales.groupby('city')['sale'].sum().to_dict())
```

**Kết quả khi chạy:**

```text
{'A': 30, 'B': 8}
```

Vùng A có hai giao dịch nên tổng 30 nghìn đồng; vùng B chỉ có một giao dịch 8 nghìn đồng.

### 4.4. Merge — Ghép bảng theo khóa

**Từ vựng trong mục:** **Merge** — ghép bảng; **Join key** — khóa ghép.

Khi thông tin nằm trong hai bảng, `merge` dùng cột **khóa chung** để ghép các hàng liên quan. Bảng `orders` có đơn của khách `id=1` và `id=2`, cột `sale` là giá trị đơn; bảng `customers` có tên An, Lan theo cùng id. `merge(on='id', how='left')` giữ mọi dòng bên trái và bổ sung tên nếu tìm thấy. Nếu bảng bên phải có nhiều dòng trùng khóa, một dòng đơn hàng có thể bị nhân bản; dùng `validate='many_to_one'` để kiểm tra mỗi id bên phải là duy nhất.

```python
# Mục đích: Ghép bảng theo khóa.
import pandas as pd

orders = pd.DataFrame({'id': [1, 2], 'sale': [10, 20]})
customers = pd.DataFrame({'id': [1, 2], 'name': ['An', 'Lan']})
merged = orders.merge(customers, on='id', how='left', validate='many_to_one')
print(merged['name'].tolist())
```

**Kết quả khi chạy:**

```text
['An', 'Lan']
```

Hai tên khách được ghép đúng theo id, không phải dựa vào vị trí hàng ngẫu nhiên.

## 5. Năm vấn đề thực tế

### Tình huống 1 — Đơn hàng giá cao

**Từ vựng trong mục:** **loc** — chọn theo nhãn.

**Tình huống thực tế:** Cửa hàng có ba sản phẩm A, B, C với giá 300, 900 và 1.200 đơn vị tiền. In các sản phẩm có giá từ 800 trở lên.

**Vì sao chọn cách giải này?** Điều kiện `df.price >= 800` chọn hai hàng phù hợp.

**Quy trình giải:**

1. Tạo bảng gồm tên và giá của ba sản phẩm.
2. Tạo mặt nạ `price >= 800` để giữ sản phẩm đạt ngưỡng.
3. In bảng đã lọc, giữ B và C cùng giá tương ứng.

```python
# Mục đích: Đơn hàng giá cao.
import pandas as pd
df = pd.DataFrame({"name":["A", "B", "C"], "price":[300, 900, 1200]})
print(df[df.price>=800])
```

**Kết quả khi chạy:**

```text
  name  price
1    B    900
2    C   1200
```

### Tình huống 2 — Tra dòng thứ hai

**Từ vựng trong mục:** **iloc** — chọn theo vị trí.

**Tình huống thực tế:** Bảng mã khách theo thứ tự A, B, C. Lấy dòng thứ hai của bảng.

**Vì sao chọn cách giải này?** `iloc[1]` lấy vị trí thứ hai do chỉ số bắt đầu từ 0.

**Quy trình giải:**

1. Tạo bảng mã khách A, B, C theo đúng thứ tự hàng.
2. Gọi `.iloc[1]` để lấy hàng ở chỉ số 1.
3. In dữ liệu của khách thứ hai, không nhầm nhãn với vị trí.

```python
# Mục đích: Tra dòng thứ hai.
import pandas as pd
df = pd.DataFrame({"id":["A", "B", "C"]})
print(df.iloc[1])
```

**Kết quả khi chạy:**

```text
id    B
Name: 1, dtype: object
```

### Tình huống 3 — Doanh thu từng vùng

**Từ vựng trong mục:** **groupby** — nhóm dữ liệu.

**Tình huống thực tế:** Bảng doanh thu có ba giao dịch: vùng A được 10 và 20, vùng B được 8 đơn vị tiền. Tính tổng doanh thu theo từng vùng.

**Vì sao chọn cách giải này?** `groupby('city')['sale'].sum()` cộng các dòng có cùng vùng.

**Quy trình giải:**

1. Tạo ba dòng doanh thu và gắn khóa vùng A, A, B.
2. Nhóm theo cột `city` và cộng `sale` cho từng nhóm.
3. In tổng của vùng A và B, đơn vị tiền giữ nguyên.

```python
# Mục đích: Doanh thu từng vùng.
import pandas as pd
df = pd.DataFrame({"city":["A", "A", "B"], "sale":[10, 20, 8]})
print(df.groupby("city")["sale"].sum())
```

**Kết quả khi chạy:**

```text
city
A    30
B     8
Name: sale, dtype: int64
```

### Tình huống 4 — Đơn hàng và khách

**Từ vựng trong mục:** **merge** — ghép bảng.

**Tình huống thực tế:** Bảng bán hàng có ID 1,2 với doanh thu 10,20. Bảng khách có ID 1 là An, ID 2 là Lan. Ghép tên khách vào từng dòng doanh thu theo ID.

**Vì sao chọn cách giải này?** `merge(..., on='id', how='left')` giữ các dòng bán hàng bên trái và lấy tên tương ứng.

**Quy trình giải:**

1. Tạo bảng đơn hàng với khóa `id` và bảng khách cũng có `id`.
2. Ghép từ bảng đơn bằng `merge(on='id', how='left')`.
3. In tên sau khi ghép và kiểm tra số hàng vẫn là hai.

```python
# Mục đích: Đơn hàng và khách.
import pandas as pd
a = pd.DataFrame({"id":[1, 2], "sale":[10, 20]})
b = pd.DataFrame({"id":[1, 2], "name":["An", "Lan"]})
print(a.merge(b, on="id", how="left"))
```

**Kết quả khi chạy:**

```text
   id  sale name
0   1    10   An
1   2    20  Lan
```

### Tình huống 5 — Top doanh số

**Từ vựng trong mục:** **sort_values** — sắp xếp theo giá trị.

**Tình huống thực tế:** Bốn nhân viên A, B, C, D có doanh số 30,80,20,60 đơn vị tiền. In hai người có doanh số cao nhất.

**Vì sao chọn cách giải này?** `sort_values(ascending=False).head(2)` sắp giảm dần và lấy hai dòng đầu.

**Quy trình giải:**

1. Tạo bảng bốn nhân viên với doanh số tương ứng.
2. Sắp xếp theo `sale` giảm dần.
3. Dùng `head(2)` để lấy hai nhân viên đứng đầu và in bảng.

```python
# Mục đích: Top doanh số.
import pandas as pd
df = pd.DataFrame({"id":["A", "B", "C", "D"], "sale":[30, 80, 20, 60]})
print(df.sort_values("sale", ascending=False).head(2))
```

**Kết quả khi chạy:**

```text
  id  sale
1  B    80
3  D    60
```

## 6. Sai lầm thường gặp

- `.loc` dùng **nhãn**, `.iloc` dùng **vị trí số**; không nhầm nhãn cột `id` với index của DataFrame.
- Với lọc Boolean, phải dùng điều kiện trên đúng cột; `df.loc[mask, columns]` khác `.iloc`.
- `groupby('city').sum()` chỉ có ý nghĩa khi hiểu **mỗi hàng là giao dịch**, cột `city` là khóa phân nhóm và `sale` là lượng cần tổng hợp.
- `merge` dùng khóa; nếu bảng phụ có **khóa trùng**, số hàng sau ghép có thể tăng. Có thể dùng `validate='many_to_one'` khi bảng phải phải duy nhất.
- `sort_values()` mặc định tăng dần; để lấy nhóm doanh thu cao nhất cần `ascending=False` trước `head()`.

## 7. Trắc nghiệm

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

## 8. Nối sang bài tiếp

`DataFrame → lọc → nhóm → ghép bảng → AI`.
