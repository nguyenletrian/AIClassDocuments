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

## 5. Năm tình huống Pandas — từ lọc hàng đến ghép và tổng hợp nhiều bảng

### Tình huống 1 — Cấp 1: Lọc 10 sản phẩm bằng loc theo ngưỡng

**Từ vựng trong mục:** **Filter** — lọc; **loc** — chọn hàng theo nhãn.

**Tình huống thực tế:** Cửa hàng có **10 sản phẩm** P01…P10, mỗi dòng là giá bán (nghìn đồng/món). Người quản lý cần danh sách những sản phẩm có giá **ít nhất 800 nghìn đồng**, giữ đúng mã để đưa vào bảng đối chiếu.

**Vì sao chọn cách này?** `df.loc[mask, columns]` chọn các hàng đúng điều kiện và chỉ hai cột cần xem. Chỉ số hàng trong DataFrame không phải giá sản phẩm; dùng `loc` giúp tách điều kiện và thông tin hiển thị.

**Quy trình:**
1. Tạo bảng mã/giá của 10 sản phẩm.
2. Lọc bằng `price_thousand >= 800` và chọn cột mã.
3. In số sản phẩm phù hợp và danh sách mã.

```python
import pandas as pd
prices = [300,900,1200,400,850,2000,500,700,1500,650]
df = pd.DataFrame({"id": [f"P{i:02d}" for i in range(1, 11)], "price_thousand": prices})
selected = df.loc[df["price_thousand"] >= 800, ["id", "price_thousand"]]
assert len(df) == 10
print("Sản phẩm:", len(df))
print("Giá cao:", len(selected))
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

**Tình huống thực tế:** Kho ghi **12 phiếu xuất** K01…K12 với số lượng món xuất mỗi phiếu. Để kiểm tra lô được nhập từ thứ tự **phiếu thứ 4 đến phiếu thứ 7**, nhân viên muốn lấy đúng bốn hàng trong DataFrame và tính tổng món của bốn phiếu.

**Vì sao chọn cách này?** `iloc[3:7]` chọn các vị trí 3,4,5,6 tương ứng phiếu thứ 4–7; số 7 là giới hạn không bao gồm. Khác `loc`, `iloc` dùng vị trí chứ không dùng mã K04.

**Quy trình:**
1. Ghi 12 phiếu theo thứ tự phát sinh.
2. Cắt các vị trí 3–6 bằng `iloc[3:7]`.
3. In mã đầu/cuối, số dòng và tổng món của lát cắt.

```python
import pandas as pd
quantities = [1,2,3,4,1,2,3,4,1,2,3,4]
df = pd.DataFrame({"id": [f"K{i:02d}" for i in range(1, 13)],
                   "quantity": quantities})
portion = df.iloc[3:7]
assert len(df) == 12 and len(portion) == 4
print("Phiếu:", len(df))
print("Đã chọn:", len(portion))
print("Mã đầu/cuối:", portion["id"].iloc[0], portion["id"].iloc[-1])
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

**Tình huống thực tế:** Một đại lý có **15 giao dịch**, mỗi hàng gắn vùng `Bắc`, `Nam`, `Trung` và số doanh thu (triệu đồng/giao dịch). Chủ cửa hàng muốn biết số giao dịch và tổng doanh thu **riêng từng vùng**, sau đó sắp vùng có doanh số lớn nhất lên đầu.

**Vì sao chọn cách này?** `groupby('area').agg(...)` gom hàng có cùng vùng và tạo hai chỉ số đếm/tổng; `sort_values` tổ chức bảng kết quả, không làm thay đổi doanh thu thực tế.

**Quy trình:**
1. Tạo 15 dòng với đơn vị doanh thu rõ ràng.
2. Nhóm theo vùng, đếm số giao dịch và cộng doanh thu.
3. Sắp theo doanh thu giảm rồi theo tên vùng để khi hòa điểm vẫn ổn định.

```python
import pandas as pd
rows = [{"area":"Bắc","amount":10},{"area":"Nam","amount":15},{"area":"Trung","amount":20},{"area":"Bắc","amount":25},{"area":"Nam","amount":30},{"area":"Trung","amount":10},{"area":"Bắc","amount":15},{"area":"Nam","amount":20},{"area":"Trung","amount":25},{"area":"Bắc","amount":30},{"area":"Nam","amount":10},{"area":"Trung","amount":15},{"area":"Bắc","amount":20},{"area":"Nam","amount":25},{"area":"Trung","amount":30}]
df = pd.DataFrame(rows)
grouped = df.groupby("area", as_index=False).agg(
    orders=("amount", "size"), total_million=("amount", "sum"))
grouped = grouped.sort_values(["total_million", "area"], ascending=[False, True])
assert len(df) == 15 and grouped["orders"].sum() == 15
print("Giao dịch:", len(df))
print("Số vùng:", len(grouped))
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

**Tình huống thực tế:** Ứng dụng có **18 đơn hàng** O01…O18 và bảng thông tin 12 khách C01…C12. Mỗi đơn có mã khách và số tiền (nghìn đồng); riêng O17 trỏ nhầm tới C99 không có trong danh mục. Cần giữ **đủ 18 đơn**, bổ sung thành phố khách khi tìm được và báo mã đơn chưa khớp để nhân viên sửa.

**Vì sao chọn cách này?** `merge(..., how='left', validate='many_to_one', indicator=True)` giữ mỗi đơn bảng trái, chỉ bổ sung thông tin khi mã khách tồn tại ở danh mục **duy nhất**. `inner` sẽ làm O17 biến mất âm thầm, không phù hợp đối soát.

**Quy trình:**
1. Tạo bảng 18 đơn và danh mục 12 khách không trùng mã.
2. Left-merge theo khóa `customer_id`; kiểm tra quan hệ nhiều–một.
3. Đếm số dòng không khớp và xác nhận không mất đơn hàng.

```python
import pandas as pd
orders = pd.DataFrame([{"id":"O01","customer_id":"C01","amount":100},{"id":"O02","customer_id":"C02","amount":125},{"id":"O03","customer_id":"C03","amount":150},{"id":"O04","customer_id":"C04","amount":175},{"id":"O05","customer_id":"C05","amount":200},{"id":"O06","customer_id":"C06","amount":100},{"id":"O07","customer_id":"C07","amount":125},{"id":"O08","customer_id":"C08","amount":150},{"id":"O09","customer_id":"C09","amount":175},{"id":"O10","customer_id":"C10","amount":200},{"id":"O11","customer_id":"C11","amount":100},{"id":"O12","customer_id":"C12","amount":125},{"id":"O13","customer_id":"C01","amount":150},{"id":"O14","customer_id":"C02","amount":175},{"id":"O15","customer_id":"C03","amount":200},{"id":"O16","customer_id":"C04","amount":100},{"id":"O17","customer_id":"C99","amount":125},{"id":"O18","customer_id":"C06","amount":150}])
customers = pd.DataFrame([{"customer_id":"C01","city":"Hà Nội"},{"customer_id":"C02","city":"Đà Nẵng"},{"customer_id":"C03","city":"TP.HCM"},{"customer_id":"C04","city":"Hà Nội"},{"customer_id":"C05","city":"Đà Nẵng"},{"customer_id":"C06","city":"TP.HCM"},{"customer_id":"C07","city":"Hà Nội"},{"customer_id":"C08","city":"Đà Nẵng"},{"customer_id":"C09","city":"TP.HCM"},{"customer_id":"C10","city":"Hà Nội"},{"customer_id":"C11","city":"Đà Nẵng"},{"customer_id":"C12","city":"TP.HCM"}])
merged = orders.merge(customers, on="customer_id", how="left",
                      validate="many_to_one", indicator=True)
unmatched = merged.loc[merged["_merge"] == "left_only", "id"].tolist()
assert len(orders) == len(merged) == 18 and customers["customer_id"].is_unique
print("Đơn:", len(orders))
print("Khách danh mục:", len(customers))
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

**Tình huống thực tế:** Kế toán có **20 dòng bán hàng** O01…O20, mỗi dòng chứa mã SKU và số món; danh mục có **5 giá sản phẩm** P01…P05 (nghìn đồng/món). Dòng O19 mang mã P99 chưa được cấp giá. Cần ghép giá theo SKU, tách một dòng cần bổ sung, tính doanh thu **chỉ từ các dòng có giá hợp lệ** và xác định SKU có doanh thu cao nhất. Không nhân số lượng với giá rỗng hoặc làm mất hàng O19.

**Vì sao chọn cách này?** Left-merge kèm `validate='many_to_one'` ngăn giá nhân lên do mã sản phẩm trùng trong danh mục; sau đó `groupby().sum()` cộng theo SKU. Báo rõ khóa không khớp trước khi tổng hợp để không coi doanh thu thiếu như 0.

**Quy trình:**
1. Tạo 20 dòng bán và bảng giá 5 SKU duy nhất.
2. Left-merge theo `sku`, tách các dòng có giá thiếu để báo lỗi.
3. Tính doanh thu theo dòng `price * qty`, groupby theo SKU, sắp top; xác nhận 19 + 1 = 20.

```python
import pandas as pd
sales = pd.DataFrame([{"invoice_id":"O01","sku":"P01","qty":1},{"invoice_id":"O02","sku":"P02","qty":2},{"invoice_id":"O03","sku":"P03","qty":3},{"invoice_id":"O04","sku":"P04","qty":4},{"invoice_id":"O05","sku":"P05","qty":1},{"invoice_id":"O06","sku":"P01","qty":2},{"invoice_id":"O07","sku":"P02","qty":3},{"invoice_id":"O08","sku":"P03","qty":4},{"invoice_id":"O09","sku":"P04","qty":1},{"invoice_id":"O10","sku":"P05","qty":2},{"invoice_id":"O11","sku":"P01","qty":3},{"invoice_id":"O12","sku":"P02","qty":4},{"invoice_id":"O13","sku":"P03","qty":1},{"invoice_id":"O14","sku":"P04","qty":2},{"invoice_id":"O15","sku":"P05","qty":3},{"invoice_id":"O16","sku":"P01","qty":4},{"invoice_id":"O17","sku":"P02","qty":1},{"invoice_id":"O18","sku":"P03","qty":2},{"invoice_id":"O19","sku":"P99","qty":3},{"invoice_id":"O20","sku":"P05","qty":4}])
prices = pd.DataFrame([["P01",10],["P02",20],["P03",30],["P04",15],["P05",25]], columns=["sku", "price_thousand"])
merged = sales.merge(prices, on="sku", how="left", validate="many_to_one")
missing = merged.loc[merged["price_thousand"].isna(), "invoice_id"].tolist()
valid = merged.loc[merged["price_thousand"].notna()].copy()
valid["revenue_thousand"] = valid["qty"] * valid["price_thousand"]
by_sku = valid.groupby("sku", as_index=False)["revenue_thousand"].sum()
ranking = by_sku.sort_values(["revenue_thousand", "sku"], ascending=[False, True])
assert len(sales) == len(merged) == len(valid) + len(missing) == 20
print("Dòng bán:", len(sales))
print("Có giá:", len(valid))
print("Chưa có giá:", ", ".join(missing))
print("Doanh thu (nghìn đồng):", int(valid["revenue_thousand"].sum()))
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
