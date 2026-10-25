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
# Mục đích: Chọn sản phẩm có giá từ 800 trở lên bằng .loc với điều kiện Boolean.
# Dữ liệu: Ba hàng sản phẩm A/B/C và giá 300/900/1200 (đơn vị minh họa).
# Pandas hỗ trợ lọc hàng DataFrame theo điều kiện.
import pandas as pd

# Tạo bảng name và price theo từng hàng sản phẩm.
products = pd.DataFrame({'name': ['A', 'B', 'C'], 'price': [300, 900, 1200]})
# So từng giá với 800, tạo Series Boolean True/False.
# .loc[điều_kiện_hàng, tên_cột] chọn tên ở hàng True; ở đây B và C.
selected = products.loc[products['price'] >= 800, 'name']
# .tolist() chuyển Series tên đã lọc thành list Python để in.
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
# Mục đích: Dùng .iloc đọc ô theo vị trí hàng 1, cột 0 của DataFrame.
# Dữ liệu: Ba mã A, B, C; thứ tự hàng bắt đầu từ vị trí 0.
# Pandas DataFrame có thể tra theo nhãn .loc hoặc vị trí .iloc.
import pandas as pd

# Tạo bảng một cột id và ba hàng A,B,C.
people = pd.DataFrame({'id': ['A', 'B', 'C']})
# .iloc[1,0] đọc hàng thứ hai và cột đầu tiên theo VỊ TRÍ, trả B; khác .loc tra nhãn.
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
# Mục đích: Gộp các đơn theo city rồi cộng cột sale riêng từng thành phố.
# Dữ liệu: Ba hàng: city A có hai sale 10,20; B một sale 8.
# DataFrame.groupby() tập hợp hàng cùng giá trị của khóa nhóm.
import pandas as pd

# Tạo bảng 3 giao dịch với cột city và sale.
sales = pd.DataFrame({'city': ['A', 'A', 'B'], 'sale': [10, 20, 8]})
# groupby('city') tạo các nhóm hàng cùng tên city, không phải nối bảng.
# Chọn cột sale trong từng nhóm rồi sum() cộng từng nhóm A=30, B=8.
# .to_dict() đổi Series kết quả thành dictionary {city: tổng}, tiện xem bằng print().
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
# Mục đích: Ghép bảng đơn với bảng khách theo id, giữ tất cả đơn và xác minh mỗi id chỉ có một khách.
# Dữ liệu: Hai đơn id 1,2 và hai khách id 1,2, trường sale của đơn và name của khách.
# Pandas merge() là phép nối bảng theo khóa chung.
import pandas as pd

# Tạo hai bảng có cột id trùng tên; sale là giá đơn, name là tên khách.
orders = pd.DataFrame({'id': [1, 2], 'sale': [10, 20]})
# Tạo hai bảng có cột id trùng tên; sale là giá đơn, name là tên khách.
customers = pd.DataFrame({'id': [1, 2], 'name': ['An', 'Lan']})
# on='id' chọn khóa ghép; how='left' giữ mọi đơn dù thiếu khách; validate='many_to_one' yêu cầu khóa id của BẢNG KHÁCH không trùng (nhiều đơn được phép cùng khách).
merged = orders.merge(customers, on='id', how='left', validate='many_to_one')
# Sau ghép, ['name'] lấy tên khách theo thứ tự đơn; tolist() đổi sang list Python.
print(merged['name'].tolist())
```

**Kết quả khi chạy:**

```text
['An', 'Lan']
```

Hai tên khách được ghép đúng theo id, không phải dựa vào vị trí hàng ngẫu nhiên.

## 5. Năm tình huống Pandas — từ lọc hàng đến ghép và tổng hợp nhiều bảng

### Tình huống 1 — Cấp 1: Lọc 10 sản phẩm bằng loc theo ngưỡng

**Từ vựng trong mục:** **Filter** — lọc; **loc** — chọn hàng theo nhãn.

**Tình huống thực tế:** Cửa hàng có danh mục **10 sản phẩm P01–P10**, mỗi sản phẩm ghi một đơn giá tính bằng **nghìn đồng/món**. Chủ cửa hàng muốn chọn những món có giá **từ 800 nghìn đồng trở lên**, rồi in đúng **mã và giá** của chúng để nhân viên đối chiếu bảng hàng. Mã P01 không phải là vị trí hàng và cũng không phải số tiền.

**Vì sao chọn cách này?** `DataFrame` là bảng có cột được đặt tên, giúp phân biệt rõ **mã sản phẩm** và **giá tiền**. Chương trình kiểm tra từng giá có `>= 800` hay không để tạo một **mặt nạ Boolean** (dãy đúng/sai). `df.loc[mask, ['id', 'price_thousand']]` chỉ lấy những hàng đúng điều kiện, đồng thời chỉ giữ hai cột cần xem. `loc` chọn dựa trên nhãn hoặc điều kiện, không phải so sánh mã P01 với con số 800. Cách lọc này còn giữ nguyên dữ liệu gốc; đổi thứ tự bảng không làm ngưỡng giá thay đổi.

**Quy trình:**
1. Tạo bảng mã/giá của 10 sản phẩm.
2. Lọc bằng `price_thousand >= 800` và chọn cột mã.
3. In số sản phẩm phù hợp và danh sách mã.

```python
# Mục đích: Lọc 10 sản phẩm có giá từ 800 nghìn đồng bằng .loc và in mã.
# Dữ liệu: 10 hàng sản phẩm P01..P10, price_thousand là nghìn đồng/món.
# Pandas dùng Series Boolean để chọn đúng hàng quan tâm.
import pandas as pd
prices = [300,900,1200,400,850,2000,500,700,1500,650]
ids = []
# range(1,11) sinh 10 số thứ tự mã sản phẩm, không lấy 11.
for i in range(1, 11):
    # append() giữ mã P01..P10, f-string :02d thêm 0 đầu.
    ids.append(f"P{i:02d}")
# Ghép id và price_thousand thành 10 hàng theo thứ tự tương ứng.
df = pd.DataFrame({"id": ids, "price_thousand": prices})
# So ngưỡng 800 với từng giá để tạo mask Boolean.
# loc[mask, [cột...]] lọc hàng đạt giá và chỉ lấy hai cột id/price_thousand.
selected = df.loc[df["price_thousand"] >= 800, ["id", "price_thousand"]]
if len(df) != 10:
    # ValueError báo số bản ghi/khóa không hợp lệ rồi dừng, tránh công bố kết quả ghép sai.
    raise ValueError("Cần đủ 10 sản phẩm trong bảng giá.")
print("Sản phẩm:", len(df))
# len() trả số sản phẩm đạt ngưỡng sau lọc.
print("Giá cao:", len(selected))
# join() ghép danh sách mã từ Series id bằng dấu phẩy và khoảng trắng.
print("Mã:", ", ".join(selected["id"]))
```

**Kết quả khi chạy:**

```text
Sản phẩm: 10
Giá cao: 5
Mã: P02, P03, P05, P06, P09
```

Ngưỡng **bao gồm** 800 do dùng `>=`. Mã hàng được giữ riêng để biết chính xác những sản phẩm nào cần rà soát.

### Tình huống 2 — Cấp 2: Phân biệt vị trí iloc với mã giao dịch ở 12 phiếu

**Từ vựng trong mục:** **iloc** — chọn theo vị trí; **Slice** — lát cắt; **Index label** — nhãn hàng.

**Tình huống thực tế:** Kho nhận **12 phiếu xuất K01–K12**, theo đúng thứ tự ghi nhận; mỗi phiếu có số món đã xuất. Trưởng kho yêu cầu xem **phiếu thứ 4 đến phiếu thứ 7**, tức bốn phiếu liên tiếp, và cộng tổng số món của bốn phiếu này. Nhân viên cần ghi lại mã phiếu đầu và cuối trong đoạn đã chọn để không chọn lệch một hàng.

**Vì sao chọn cách này?** `iloc` chọn theo **vị trí hàng tính từ 0**, khác `loc` chọn theo nhãn hàng hoặc điều kiện. Phiếu thứ tư có vị trí 3, nên `df.iloc[3:7]` lấy các vị trí **3, 4, 5, 6**, tương ứng K04 đến K07; số 7 ở cuối lát cắt **không được lấy**. Sau đó cộng cột `quantity` của đúng bốn dòng này để ra số món xuất. Nếu dùng `[4:7]` vì thấy chữ 'phiếu thứ 4', chương trình sẽ bỏ K04 và chỉ còn ba phiếu khác với yêu cầu.

**Quy trình:**
1. Ghi 12 phiếu theo thứ tự phát sinh.
2. Cắt các vị trí 3–6 bằng `iloc[3:7]`.
3. In mã đầu/cuối, số dòng và tổng món của lát cắt.

```python
# Mục đích: Dùng .iloc chọn đúng bốn phiếu liên tiếp trong 12 phiếu và tính số món.
# Dữ liệu: 12 dòng K01..K12, quantity là số món cần xuất trên mỗi phiếu.
# Pandas .iloc chọn hàng theo vị trí số nguyên.
import pandas as pd
quantities = [1,2,3,4,1,2,3,4,1,2,3,4]
ids = []
# range(1,13) tạo mã thứ tự 1..12, không lấy 13.
for i in range(1, 13):
    # f-string :02d tạo mã K01..K12 và append() giữ theo thứ tự.
    ids.append(f"K{i:02d}")
# Ghép hai cột id và quantity với 12 hàng.
df = pd.DataFrame({"id": ids,
                   "quantity": quantities})
# iloc[3:7] lấy chỉ số 3,4,5,6 (K04..K07); không lấy vị trí 7.
portion = df.iloc[3:7]
if len(df) != 12 or len(portion) != 4:
    # ValueError báo số bản ghi/khóa không hợp lệ rồi dừng, tránh công bố kết quả ghép sai.
    raise ValueError("Cần 12 phiếu và đúng 4 phiếu được chọn.")
print("Phiếu:", len(df))
print("Đã chọn:", len(portion))
# Lấy mã đầu ở vị trí 0 của phần đã cắt; iloc[-1] là mã cuối.
print("Mã đầu/cuối:", portion["id"].iloc[0], portion["id"].iloc[-1])
# sum() cộng số món của đúng bốn phiếu đã chọn, int() hiển thị số nguyên.
print("Món xuất:", int(portion["quantity"].sum()))
```

**Kết quả khi chạy:**

```text
Phiếu: 12
Đã chọn: 4
Mã đầu/cuối: K04 K07
Món xuất: 10
```

Lát cắt vẫn là bốn dòng thật từ bảng 12 phiếu; không tạo thêm hay loại ngẫu nhiên dữ liệu.

### Tình huống 3 — Cấp 3: Nhóm 15 giao dịch theo vùng và sắp doanh số

**Từ vựng trong mục:** **groupby** — nhóm theo khóa; **agg** — tổng hợp; **sort_values** — sắp xếp.

**Tình huống thực tế:** Một đại lý có **15 giao dịch** bán hàng; mỗi dòng gồm tên vùng **Bắc, Nam hoặc Trung** và tiền giao dịch tính bằng **triệu đồng**. Chủ đại lý cần biết từng vùng có **bao nhiêu giao dịch**, tổng doanh thu từng vùng, rồi trình bày vùng có tổng tiền cao hơn trước. Đếm 15 dòng chung không trả lời được vùng nào đang hoạt động mạnh nhất.

**Vì sao chọn cách này?** **Groupby** nghĩa là gom các hàng có chung một thông tin, ở đây là tên vùng. `groupby('area')` tách 15 giao dịch thành ba nhóm Bắc, Nam, Trung; `agg` yêu cầu hai phép thống kê cho mỗi nhóm: `size` đếm **số giao dịch**, `sum` cộng **tiền giao dịch**. Hai kết quả không thay thế nhau: vùng ít giao dịch có thể vẫn có doanh thu lớn. `sort_values` sắp theo tổng doanh thu **giảm dần** và tên vùng để có thứ tự nhất quán khi hòa tiền. Không cộng tất cả 15 giao dịch rồi gán cùng một tổng cho mỗi vùng.

**Quy trình:**
1. Tạo 15 dòng với đơn vị doanh thu rõ ràng.
2. Nhóm theo vùng, đếm số giao dịch và cộng doanh thu.
3. Sắp theo doanh thu giảm rồi theo tên vùng để khi hòa điểm vẫn ổn định.

```python
# Mục đích: GroupBy 15 giao dịch theo ba vùng, đếm phiếu và cộng tiền rồi xếp hạng.
# Dữ liệu: 15 giao dịch; mỗi hàng area Bắc/Nam/Trung, amount tính triệu đồng.
# Pandas groupby() và agg() tổng hợp theo nhóm.
import pandas as pd
# 15 dict, mỗi dict là một phiếu theo vùng với số tiền triệu đồng.
rows = [{"area":"Bắc","amount":10},{"area":"Nam","amount":15},{"area":"Trung","amount":20},{"area":"Bắc","amount":25},{"area":"Nam","amount":30},{"area":"Trung","amount":10},{"area":"Bắc","amount":15},{"area":"Nam","amount":20},{"area":"Trung","amount":25},{"area":"Bắc","amount":30},{"area":"Nam","amount":10},{"area":"Trung","amount":15},{"area":"Bắc","amount":20},{"area":"Nam","amount":25},{"area":"Trung","amount":30}]
# Tạo bảng với hai cột area và amount.
df = pd.DataFrame(rows)
# groupby('area') gom dòng cùng vùng; as_index=False giữ area thành CỘT thay vì đưa vào index.
grouped = df.groupby("area", as_index=False).agg(
    # agg() dạng đặt tên: size đếm SỐ HÀNG trong vùng, bao gồm cả giá trị thiếu nếu có.
    # agg() sum cộng tiền mỗi vùng, tạo cột total_million (triệu đồng).
    orders=("amount", "size"), total_million=("amount", "sum"))
# sort_values theo tổng giảm dần (False), nếu hòa xếp tên vùng tăng dần (True), cho kết quả ổn định.
grouped = grouped.sort_values(["total_million", "area"], ascending=[False, True])
# sum() cộng số phiếu của các nhóm; phải bằng 15 giao dịch đầu vào.
if len(df) != 15 or grouped["orders"].sum() != 15:
    # ValueError báo số bản ghi/khóa không hợp lệ rồi dừng, tránh công bố kết quả ghép sai.
    raise ValueError("Cần tổng hợp đủ 15 phiếu theo vùng.")
print("Giao dịch:", len(df))
print("Số vùng:", len(grouped))
# to_dict('records') biến DataFrame thành list dict, mỗi dict chứa một vùng để in trường area/orders/total_million.
for record in grouped.to_dict("records"):
    print(f"{record['area']}: {record['orders']} phiếu, {record['total_million']} triệu")
```

**Kết quả khi chạy:**

```text
Giao dịch: 15
Số vùng: 3
Bắc: 5 phiếu, 100 triệu
Nam: 5 phiếu, 100 triệu
Trung: 5 phiếu, 100 triệu
```

Từng giá trị là **doanh thu tổng** trong một vùng, không phải doanh thu trung bình mỗi đơn; muốn trung bình phải yêu cầu phép tính khác.

### Tình huống 4 — Cấp 4: Ghép 18 đơn với 12 khách mà không đánh mất đơn lạ

**Từ vựng trong mục:** **merge** — ghép bảng; **Left join** — giữ bảng trái; **Unmatched key** — khóa không khớp.

**Tình huống thực tế:** Ứng dụng có bảng **18 đơn hàng O01–O18** và bảng thông tin **12 khách C01–C12**. Mỗi đơn ghi mã khách và tiền hàng (**nghìn đồng**); bảng khách ghi **thành phố** của mỗi người. Riêng đơn **O17** tham chiếu mã khách **C99**, chưa có trong danh mục. Nhân viên cần bổ sung thành phố cho những đơn tìm được khách, nhưng vẫn phải giữ đủ **18 đơn** và báo chính xác mã đơn không khớp để sửa.

**Vì sao chọn cách này?** **Ghép bảng (merge)** là tìm dòng thuộc bảng khách bằng **mã khách** trên từng đơn hàng, rồi bổ sung thông tin như thành phố. Một khách có thể đặt **nhiều đơn**, còn mã khách trong danh mục chỉ được xuất hiện **một lần**: `validate='many_to_one'` kiểm tra đúng kiểu quan hệ này để tránh nhân đôi đơn khi bảng khách bị trùng mã. `how='left'` giữ **tất cả 18 đơn** của bảng bên trái, kể cả O17 không tìm thấy C99; `indicator=True` đánh dấu dòng đã ghép được hay còn thiếu, nhờ đó in ra O17 để sửa. Nếu dùng `inner` merge, O17 có thể biến mất khỏi báo cáo mà không có cảnh báo.

**Quy trình:**
1. Tạo bảng 18 đơn và danh mục 12 khách không trùng mã.
2. Left-merge theo khóa `customer_id`; kiểm tra quan hệ nhiều–một.
3. Đếm số dòng không khớp và xác nhận không mất đơn hàng.

```python
# Mục đích: Ghép 18 đơn với danh mục 12 khách, giữ đơn thiếu khách và phát hiện mã C99.
# Dữ liệu: 18 đơn có id/customer_id/amount và danh mục 12 khách customer_id/city; C99 không tồn tại ở bảng khách.
# Pandas merge() kết hợp hai bảng theo khóa chung.
import pandas as pd
# Bảng trái gồm 18 đơn; customer_id trỏ vào mã khách, mỗi khách có thể nhiều đơn.
orders = pd.DataFrame([{"id":"O01","customer_id":"C01","amount":100},{"id":"O02","customer_id":"C02","amount":125},{"id":"O03","customer_id":"C03","amount":150},{"id":"O04","customer_id":"C04","amount":175},{"id":"O05","customer_id":"C05","amount":200},{"id":"O06","customer_id":"C06","amount":100},{"id":"O07","customer_id":"C07","amount":125},{"id":"O08","customer_id":"C08","amount":150},{"id":"O09","customer_id":"C09","amount":175},{"id":"O10","customer_id":"C10","amount":200},{"id":"O11","customer_id":"C11","amount":100},{"id":"O12","customer_id":"C12","amount":125},{"id":"O13","customer_id":"C01","amount":150},{"id":"O14","customer_id":"C02","amount":175},{"id":"O15","customer_id":"C03","amount":200},{"id":"O16","customer_id":"C04","amount":100},{"id":"O17","customer_id":"C99","amount":125},{"id":"O18","customer_id":"C06","amount":150}])
# Bảng phải có 12 mã khách duy nhất và thành phố tương ứng.
customers = pd.DataFrame([{"customer_id":"C01","city":"Hà Nội"},{"customer_id":"C02","city":"Đà Nẵng"},{"customer_id":"C03","city":"TP.HCM"},{"customer_id":"C04","city":"Hà Nội"},{"customer_id":"C05","city":"Đà Nẵng"},{"customer_id":"C06","city":"TP.HCM"},{"customer_id":"C07","city":"Hà Nội"},{"customer_id":"C08","city":"Đà Nẵng"},{"customer_id":"C09","city":"TP.HCM"},{"customer_id":"C10","city":"Hà Nội"},{"customer_id":"C11","city":"Đà Nẵng"},{"customer_id":"C12","city":"TP.HCM"}])
# on='customer_id' chọn khóa; how='left' giữ mọi đơn, kể cả khách C99 chưa có danh mục.
merged = orders.merge(customers, on="customer_id", how="left",
                      # validate='many_to_one' buộc bảng khách có mã duy nhất; indicator=True tạo cột _merge nêu nguồn khớp.
                      validate="many_to_one", indicator=True)
# _merge='left_only' nghĩa đơn ở bảng trái không tìm được khách bên phải.
# .loc[mask,'id'] lấy mã đơn không khớp; tolist() chuyển Series sang list để báo cáo.
unmatched = merged.loc[merged["_merge"] == "left_only", "id"].tolist()
# .is_unique xác minh không có trùng khóa khách, tránh một đơn bị nhân bản khi merge.
# Kiểm số dòng sau ghép vẫn là 18 (left join với khóa phía phải duy nhất).
if len(orders) != 18 or len(merged) != 18 or not customers["customer_id"].is_unique:
    # ValueError báo số bản ghi/khóa không hợp lệ rồi dừng, tránh công bố kết quả ghép sai.
    raise ValueError("Cần đủ 18 đơn sau ghép và mã khách hàng duy nhất.")
print("Đơn:", len(orders))
print("Khách danh mục:", len(customers))
# Kiểm số dòng sau ghép vẫn là 18 (left join với khóa phía phải duy nhất).
print("Đơn sau ghép:", len(merged))
print("Chưa tìm thấy khách:", ", ".join(unmatched))
```

**Kết quả khi chạy:**

```text
Đơn: 18
Khách danh mục: 12
Đơn sau ghép: 18
Chưa tìm thấy khách: O17
```

O17 vẫn ở bảng kết quả với thành phố thiếu, nhờ đó lỗi khóa còn nhìn thấy để sửa. Không gán thành phố giả cho C99.

### Tình huống 5 — Cấp 5: Ghép 20 dòng bán hàng với giá và phân nhóm doanh thu

**Từ vựng trong mục:** **Merge validation** — kiểm quan hệ khóa; **Groupby** — nhóm; **Data quality** — chất lượng dữ liệu.

**Tình huống thực tế:** Kế toán nhận **20 dòng bán hàng O01–O20**, mỗi dòng ghi **SKU** (mã loại hàng) và **số món bán**. Một bảng giá riêng chỉ có năm SKU **P01–P05**, đơn giá tương ứng tính bằng **nghìn đồng/món**. Dòng O19 ghi **P99** nên chưa tìm được đơn giá. Cần ghép bảng để tính tiền cho các dòng có giá, giữ riêng mã hóa đơn cần bổ sung giá, tổng hợp doanh thu theo SKU và xác định SKU doanh thu cao nhất; không tự tính P99 bằng 0 đồng.

**Vì sao chọn cách này?** **SKU** là mã nhận diện loại sản phẩm, dùng để tìm **đơn giá** tương ứng trong bảng giá. Chương trình ghép 20 dòng bán với năm giá theo SKU bằng `how='left'`, tức vẫn giữ dòng O19 dù P99 chưa có giá. `validate='many_to_one'` bảo đảm mỗi SKU chỉ có **một giá** trong danh mục để không tạo thêm dòng bán giả. `isna()` xác định các dòng thiếu giá; chỉ lấy những dòng `notna()` rồi nhân **số món × giá một món** để có doanh thu từng dòng. `groupby('sku').sum()` cộng các dòng của cùng một sản phẩm và `sort_values` xếp SKU doanh thu cao nhất trước. O19 được báo cần sửa, không được đổi thành doanh thu 0 vì số tiền thực tế chưa biết.

**Quy trình:**
1. Tạo 20 dòng bán và bảng giá 5 SKU duy nhất.
2. Left-merge theo `sku`, tách các dòng có giá thiếu để báo lỗi.
3. Tính doanh thu theo dòng `price * qty`, groupby theo SKU, sắp top; xác nhận 19 + 1 = 20.

```python
# Mục đích: Ghép 20 lượt bán với bảng giá theo SKU, bỏ dòng thiếu giá và xếp doanh thu theo mặt hàng.
# Dữ liệu: 20 lượt bán (invoice_id, sku, qty món), bảng giá 5 SKU (nghìn đồng/món); P99 chưa có giá.
# Pandas xử lý merge, lọc NaN và groupby để tính doanh thu.
import pandas as pd
# 20 hàng: mỗi hóa đơn một SKU và số món bán.
sales = pd.DataFrame([{"invoice_id":"O01","sku":"P01","qty":1},{"invoice_id":"O02","sku":"P02","qty":2},{"invoice_id":"O03","sku":"P03","qty":3},{"invoice_id":"O04","sku":"P04","qty":4},{"invoice_id":"O05","sku":"P05","qty":1},{"invoice_id":"O06","sku":"P01","qty":2},{"invoice_id":"O07","sku":"P02","qty":3},{"invoice_id":"O08","sku":"P03","qty":4},{"invoice_id":"O09","sku":"P04","qty":1},{"invoice_id":"O10","sku":"P05","qty":2},{"invoice_id":"O11","sku":"P01","qty":3},{"invoice_id":"O12","sku":"P02","qty":4},{"invoice_id":"O13","sku":"P03","qty":1},{"invoice_id":"O14","sku":"P04","qty":2},{"invoice_id":"O15","sku":"P05","qty":3},{"invoice_id":"O16","sku":"P01","qty":4},{"invoice_id":"O17","sku":"P02","qty":1},{"invoice_id":"O18","sku":"P03","qty":2},{"invoice_id":"O19","sku":"P99","qty":3},{"invoice_id":"O20","sku":"P05","qty":4}])
# Danh mục có một mức giá nghìn đồng/món cho mỗi SKU P01..P05.
prices = pd.DataFrame([["P01",10],["P02",20],["P03",30],["P04",15],["P05",25]], columns=["sku", "price_thousand"])
# merge theo SKU; left giữ tất cả 20 giao dịch; many_to_one bảo đảm mỗi SKU có tối đa một hàng giá, không nhân doanh thu.
merged = sales.merge(prices, on="sku", how="left", validate="many_to_one")
# isna() tạo mask nơi SKU không có giá sau khi nối (ví dụ P99).
# .loc[mask,'invoice_id'] ghi hóa đơn thiếu giá, không ngầm coi là giá 0.
missing = merged.loc[merged["price_thousand"].isna(), "invoice_id"].tolist()
# notna() nhận dòng có giá; .copy() tạo bảng hợp lệ độc lập.
valid = merged.loc[merged["price_thousand"].notna()].copy()
# Tạo cột doanh thu nghìn đồng = số món × giá nghìn đồng/món, theo từng hàng.
valid["revenue_thousand"] = valid["qty"] * valid["price_thousand"]
# groupby('sku') gom dòng bán cùng mặt hàng, as_index=False giữ SKU thành cột; sum() cộng doanh thu từng SKU.
by_sku = valid.groupby("sku", as_index=False)["revenue_thousand"].sum()
# Xếp doanh thu giảm dần, nếu bằng tiền thì tên SKU tăng dần để giải quyết hòa.
ranking = by_sku.sort_values(["revenue_thousand", "sku"], ascending=[False, True])
# Đối chiếu 20 dòng = có giá + chưa có giá, không đánh mất giao dịch.
if len(sales) != 20 or len(merged) != 20 or len(valid) + len(missing) != 20:
    # ValueError báo số bản ghi/khóa không hợp lệ rồi dừng, tránh công bố kết quả ghép sai.
    raise ValueError("Cần đối chiếu đủ 20 dòng bán, gồm cả SKU chưa có giá.")
print("Dòng bán:", len(sales))
print("Có giá:", len(valid))
print("Chưa có giá:", ", ".join(missing))
# sum() tổng doanh thu hợp lệ theo nghìn đồng, không cộng hàng chưa có giá.
print("Doanh thu (nghìn đồng):", int(valid["revenue_thousand"].sum()))
# iloc[0] là hàng đầu của bảng xếp hạng, ['sku'] trả mã SKU có doanh thu cao nhất.
print("SKU cao nhất:", ranking.iloc[0]["sku"])
```

**Kết quả khi chạy:**

```text
Dòng bán: 20
Có giá: 19
Chưa có giá: O19
Doanh thu (nghìn đồng): 955
SKU cao nhất: P03
```

Doanh thu tổng hợp ở đây chỉ gồm 19 dòng có giá; O19 cần bổ sung SKU thật trước khi có thể hoàn thiện báo cáo.

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
