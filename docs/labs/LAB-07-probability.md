# Lab 7 — Xác suất

## Đề bài tiếng Anh

### LAB SESSION 7

#### Problem Description
Probability, Simulation, Conditional Probability, Bayes’ Theorem and Probability Distributions.

#### Requirements

##### Task 1 – Sample Space and Basic Probability
A box contains 10 cards numbered from 1 to 10. One card is randomly selected.

Define the sample space and events:
- A: The selected number is even.
- B: The selected number is greater than 6.

Calculate theoretical probabilities `P(A)`, `P(B)`, `P(A ∩ B)`, and `P(A ∪ B)`.

##### Task 2 – Probability Simulation
A basketball player has a 70% probability of successfully making a free throw.

- Use NumPy to simulate **5,000 free throws** and calculate experimental probability of success.
- Simulate two independent players with success probabilities 0.7 and 0.6.
- Calculate probability both succeed and probability at least one succeeds.
- Compare simulation with theoretical probabilities.

##### Task 3 – Conditional Probability
A day is randomly selected from a seven-day week.
- Event A: The selected day is a weekday (Monday to Friday).
- Event B: The selected day is Monday, Tuesday, Wednesday or Thursday.

Calculate theoretical conditional probability `P(A | B)`. Simulate 5,000 selections using Python and NumPy, then compare the experimental result.

##### Task 4 – Bayes’ Theorem
An email filtering system has these characteristics:
- 30% of emails are spam.
- 90% of spam emails are correctly identified as spam.
- 5% of non-spam emails are incorrectly classified as spam.

Calculate overall probability an email is classified as spam, then use Bayes' theorem to calculate probability an email is actually spam when classified as spam.

##### Task 5 – Probability Distributions
A customer service team receives 8 independent requests. Each has a 75% probability of successful resolution.

- Use `scipy.stats.binom.pmf()` to calculate probability of **exactly 6** resolved requests and **at least 6** requests.
- Plot the Binomial probability distribution using Matplotlib.

*Chuyển từ `LAB SESSION 7.docx` sang Markdown.*

## Đề bài tiếng Việt

### LAB SESSION 7 — Xác suất

Một chuỗi bài thực hành về **xác suất cơ bản, mô phỏng, xác suất có điều kiện, định lý Bayes và phân phối xác suất**.

#### Toàn bộ yêu cầu

**Bài 1**

Một hộp có 10 thẻ đánh số từ 1 đến 10, lấy ngẫu nhiên một thẻ. Xác định không gian mẫu, biến cố A (số chẵn), B (số lớn hơn 6). Tính xác suất của A, B, đồng thời A và B, và ít nhất A hoặc B.

**Bài 2**

Một người chơi bóng rổ ném phạt thành công với xác suất 70%. Dùng NumPy (thư viện tính toán mảng) mô phỏng **5.000** lần để tính tỉ lệ thực nghiệm. Tiếp theo mô phỏng hai người độc lập với xác suất thành công 0,7 và 0,6; tính cả hai thành công và ít nhất một người thành công; so sánh với lý thuyết.

**Bài 3**

Chọn ngẫu nhiên một ngày trong tuần gồm 7 ngày. A là ngày thường từ thứ Hai đến thứ Sáu, B là thứ Hai đến thứ Năm. Tính `P(A|B)`, mô phỏng 5.000 lần bằng Python/NumPy (thư viện tính toán mảng) và so sánh với kết quả lý thuyết.

**Bài 4**

Hệ thống lọc email có 30% email spam, phát hiện đúng 90% spam, và báo nhầm 5% email không spam thành spam. Tính xác suất một email được đánh dấu spam và xác suất email thực sự spam khi đã bị đánh dấu.

**Bài 5**

Nhóm hỗ trợ nhận 8 yêu cầu độc lập, mỗi yêu cầu có khả năng giải quyết thành công 75%. Dùng `scipy.stats.binom.pmf()` tính xác suất giải quyết **đúng 6** và **ít nhất 6**, vẽ phân phối nhị thức bằng Matplotlib (thư viện vẽ đồ thị).

## Giải thích từng câu

### Câu 1

Tạo `set(range(1,11))`, lọc từng biến cố bằng set comprehension. Dùng `&` cho giao và `|` cho hợp, rồi chia số phần tử cho kích thước không gian mẫu 10.

**Công thức / kết quả đối chiếu:** P(A)=5/10=0,5; P(B)=4/10=0,4; P(A∩B)=2/10=0,2; P(A∪B)=0,5+0,4−0,2=0,7.

**Công thức/đối chiếu:** P(A)=5/10=0,5; P(B)=4/10=0,4; P(A∩B)=2/10=0,2; P(A∪B)=0,7.

**Ví dụ và lỗi thường gặp:** A gồm năm thẻ chẵn, B gồm bốn thẻ lớn hơn 6, giao gồm 8 và 10. P(A∩B)=2/10, P(A∪B)=7/10.

**Thuật ngữ cần nhớ:** Sample space (không gian mẫu).

### Câu 2

`np.random.default_rng(SEED)` tạo bộ sinh số có thể lặp; mỗi lần so ngẫu nhiên với ngưỡng 0,7/0,6 được một kết quả True/False. `mean()` cho tần suất thành công; dùng `&` và `|` trên hai mảng bool.

**Công thức / kết quả đối chiếu:** Độc lập: P(cả hai)=0,7×0,6=0,42; P(ít nhất một)=1−(1−0,7)(1−0,6)=0,88. Mô phỏng 5.000 lượt chỉ **xấp xỉ**, không bắt buộc trùng lý thuyết.

**Công thức/đối chiếu:** P(cả hai)=0,7×0,6=0,42; P(ít nhất một)=1−(1−0,7)(1−0,6)=0,88. Mô phỏng 5.000 lượt xấp xỉ giá trị này.

**Ví dụ và lỗi thường gặp:** Tần suất trong 5.000 lượt rút là kết quả mô phỏng, có thể lệch lý thuyết. Với hai người độc lập, P(cả hai)=0,7×0,6=0,42.

**Thuật ngữ cần nhớ:** Simulation (mô phỏng).

### Câu 3

Đặt thứ Hai đến Chủ nhật ứng với mã 0–6; B={0,1,2,3} là tập con của A={0..4}. Trong mô phỏng, đếm số lượt chọn vào B rồi kiểm tra đồng thời A∩B để được xác suất có điều kiện.

**Công thức / kết quả đối chiếu:** P(A|B)=P(A∩B)/P(B)=4/4=1 (vì mọi ngày trong B đều là ngày thường).

**Công thức/đối chiếu:** B={thứ Hai..Năm} nằm trong A={thứ Hai..Sáu}; P(A|B)=1.

**Ví dụ và lỗi thường gặp:** Biến cố B (thứ Hai–thứ Năm) nằm hoàn toàn trong biến cố A (thứ Hai–thứ Sáu), nên P(A|B)=1.

**Thuật ngữ cần nhớ:** Conditional probability (xác suất có điều kiện).

### Câu 4

Tính tổng hai cách bị hệ thống gắn cờ spam: spam thật bị phát hiện và email sạch bị báo nhầm. Sau đó dùng Bayes đổi chiều điều kiện từ P(flag|spam) sang P(spam|flag).

**Công thức / kết quả đối chiếu:** P(flag)=0,3×0,9+0,7×0,05=0,305. P(spam|flag)=0,27/0,305≈0,8852459, **không** phải 90%.

**Công thức/đối chiếu:** P(flag)=0,3×0,9+0,7×0,05=0,305; P(spam|flag)=0,27/0,305≈0,88525.

**Ví dụ và lỗi thường gặp:** P(flag)=0,3×0,9+0,7×0,05=0,305. P(spam|flag)=0,27/0,305, không đánh đồng với P(flag|spam)=0,9.

**Thuật ngữ cần nhớ:** Bayes (định lý Bayes).

### Câu 5

Số thành công tuân theo nhị thức vì có 8 phép thử độc lập cùng xác suất p=0,75. Hàm pmf trả xác suất đúng k; cộng pmf cho k=6,7,8 để lấy ít nhất 6. Hàm `save_plot` trong code tham khảo dùng `plt.bar`.

**Công thức / kết quả đối chiếu:** P(X=k)=C(8,k)(0,75)^k(0,25)^(8−k); P(X≥6)=P(X=6)+P(X=7)+P(X=8).

**Công thức/đối chiếu:** X~Binom(n=8,p=0,75); P(X=k)=C(8,k)×p^k×(1−p)^(8−k); P(X≥6)=Σ P(X=k), k=6..8.

**Ví dụ và lỗi thường gặp:** Với tám yêu cầu độc lập, dùng phân phối nhị thức. Đúng sáu dùng pmf(6); ít nhất sáu cộng pmf(6)+pmf(7)+pmf(8).

**Thuật ngữ cần nhớ:** Binomial distribution (phân phối nhị thức).


## Code Python

```python
from pathlib import Path  # Nạp thư viện (import: nạp vào) để sử dụng hàm sẵn có.
import sys  # Nạp thư viện (import: nạp vào) để sử dụng hàm sẵn có.
import numpy as np  # Nạp thư viện (import: nạp vào) để sử dụng hàm sẵn có.
from scipy.stats import binom  # Nạp thư viện (import: nạp vào) để sử dụng hàm sẵn có.

SEED=2026  # Tính hoặc cập nhật biến SEED theo công thức của bài.
TRIALS=5000  # Tính hoặc cập nhật biến TRIALS theo công thức của bài.

def task01_cards():  # Khai báo hàm (function: hàm) để gom và gọi lại những bước này.
    space=set(range(1,11))  # Tính hoặc cập nhật biến space theo công thức của bài.
    a={x for x in space if x%2==0}  # Tính hoặc cập nhật biến a theo công thức của bài.
    b={x for x in space if x>6}  # Tính hoặc cập nhật biến b theo công thức của bài.
    return {  # Trả kết quả (return: trả về) cho nơi gọi hàm.
        "space":sorted(space),"A":sorted(a),"B":sorted(b),  # Gắn tên trường (key: khóa) với giá trị trong từ điển.
        "P(A)":len(a)/len(space),  # Gắn tên trường (key: khóa) với giá trị trong từ điển.
        "P(B)":len(b)/len(space),  # Gắn tên trường (key: khóa) với giá trị trong từ điển.
        "P(A and B)":len(a&b)/len(space),  # Gắn tên trường (key: khóa) với giá trị trong từ điển.
        "P(A or B)":len(a|b)/len(space),  # Gắn tên trường (key: khóa) với giá trị trong từ điển.
    }  # Đóng danh sách, mảng hoặc nhóm tham số đang xây dựng.

def task02_free_throws():  # Khai báo hàm (function: hàm) để gom và gọi lại những bước này.
    rng=np.random.default_rng(SEED)  # Tạo hoặc sử dụng số ngẫu nhiên; seed giúp lặp lại phép thử.
    single=rng.random(TRIALS)<0.7  # Tạo hoặc sử dụng số ngẫu nhiên; seed giúp lặp lại phép thử.
    first=rng.random(TRIALS)<0.7  # Tạo hoặc sử dụng số ngẫu nhiên; seed giúp lặp lại phép thử.
    second=rng.random(TRIALS)<0.6  # Tạo hoặc sử dụng số ngẫu nhiên; seed giúp lặp lại phép thử.
    both=first & second  # Tính hoặc cập nhật biến both theo công thức của bài.
    either=first | second  # Tính hoặc cập nhật biến either theo công thức của bài.
    return {  # Trả kết quả (return: trả về) cho nơi gọi hàm.
        "experimental_single":single.mean(),  # Gắn tên trường (key: khóa) với giá trị trong từ điển.
        "experimental_both":both.mean(),  # Gắn tên trường (key: khóa) với giá trị trong từ điển.
        "experimental_either":either.mean(),  # Gắn tên trường (key: khóa) với giá trị trong từ điển.
        "theoretical_single":0.7,  # Gắn tên trường (key: khóa) với giá trị trong từ điển.
        "theoretical_both":0.7*0.6,  # Gắn tên trường (key: khóa) với giá trị trong từ điển.
        "theoretical_either":1-(1-0.7)*(1-0.6),  # Gắn tên trường (key: khóa) với giá trị trong từ điển.
    }  # Đóng danh sách, mảng hoặc nhóm tham số đang xây dựng.

def task03_conditional_days():  # Khai báo hàm (function: hàm) để gom và gọi lại những bước này.
    A=set(range(5))  # Tính hoặc cập nhật biến A theo công thức của bài.
    B=set(range(4))  # Tính hoặc cập nhật biến B theo công thức của bài.
    theoretical=len(A&B)/len(B)  # Tính hoặc cập nhật biến theoretical theo công thức của bài.
    rng=np.random.default_rng(SEED+1)  # Tạo hoặc sử dụng số ngẫu nhiên; seed giúp lặp lại phép thử.
    drawn=rng.integers(0,7,size=TRIALS)  # Tạo hoặc sử dụng số ngẫu nhiên; seed giúp lặp lại phép thử.
    given_b=np.isin(drawn,list(B))  # Tính hoặc cập nhật biến given_b theo công thức của bài.
    joint=np.isin(drawn,list(A&B))  # Tính hoặc cập nhật biến joint theo công thức của bài.
    experimental=float(joint.sum()/given_b.sum())  # Đếm hoặc cộng phần tử để tính tổng/tỷ lệ.
    return theoretical,experimental  # Trả kết quả (return: trả về) cho nơi gọi hàm.

def task04_bayes():  # Khai báo hàm (function: hàm) để gom và gọi lại những bước này.
    p_spam=0.30  # Tính hoặc cập nhật biến p_spam theo công thức của bài.
    p_flag_given_spam=0.90  # Tính hoặc cập nhật biến p_flag_given_spam theo công thức của bài.
    p_flag_given_clean=0.05  # Tính hoặc cập nhật biến p_flag_given_clean theo công thức của bài.
    p_flag=p_spam*p_flag_given_spam+(1-p_spam)*p_flag_given_clean  # Tính hoặc cập nhật biến p_flag theo công thức của bài.
    posterior=p_spam*p_flag_given_spam/p_flag  # Tính hoặc cập nhật biến posterior theo công thức của bài.
    return p_flag,posterior  # Trả kết quả (return: trả về) cho nơi gọi hàm.

def task05_binomial():  # Khai báo hàm (function: hàm) để gom và gọi lại những bước này.
    k=np.arange(0,9)  # Tính hoặc cập nhật biến k theo công thức của bài.
    probs=binom.pmf(k,n=8,p=0.75)  # Dùng hàm xác suất/kiểm định đúng tham số của đề.
    return k,probs,float(binom.pmf(6,n=8,p=0.75)),float(probs[6:].sum())  # Trả kết quả (return: trả về) cho nơi gọi hàm.

def save_plot(k,probs):  # Khai báo hàm (function: hàm) để gom và gọi lại những bước này.
    import matplotlib  # Nạp thư viện (import: nạp vào) để sử dụng hàm sẵn có.
    matplotlib.use("Agg")  # Thực hiện bước xử lý, giữ nguyên cấu trúc và thứ tự code mẫu.
    import matplotlib.pyplot as plt  # Nạp thư viện (import: nạp vào) để sử dụng hàm sẵn có.
    folder=Path(__file__).resolve().parent/"outputs"  # Tính hoặc cập nhật biến folder theo công thức của bài.
    folder.mkdir(exist_ok=True)  # Thực hiện bước xử lý, giữ nguyên cấu trúc và thứ tự code mẫu.
    fig,ax=plt.subplots()  # Thực hiện bước xử lý, giữ nguyên cấu trúc và thứ tự code mẫu.
    ax.bar(k,probs)  # Vẽ hoặc lưu biểu đồ (plot: đồ thị) để trình bày kết quả.
    ax.set(xlabel="Number of resolved requests (k)",ylabel="P(X=k)",title="Binomial(n=8, p=0.75)")  # Đặt nhãn, chú giải hoặc lưới cho hình vẽ.
    ax.set_xticks(k)  # Thực hiện bước xử lý, giữ nguyên cấu trúc và thứ tự code mẫu.
    ax.grid(True,axis="y")  # Đặt nhãn, chú giải hoặc lưới cho hình vẽ.
    target=folder/"binomial_distribution.png"  # Tính hoặc cập nhật biến target theo công thức của bài.
    fig.savefig(target,dpi=140,bbox_inches="tight")  # Vẽ hoặc lưu biểu đồ (plot: đồ thị) để trình bày kết quả.
    plt.close(fig)  # Đóng biểu đồ sau khi dùng để giải phóng bộ nhớ.
    print("Saved:",target)  # In kết quả (output: kết quả) để người học đối chiếu.

def main():  # Khai báo hàm (function: hàm) để gom và gọi lại những bước này.
    cards=task01_cards()  # Tính hoặc cập nhật biến cards theo công thức của bài.
    simulated=task02_free_throws()  # Tính hoặc cập nhật biến simulated theo công thức của bài.
    cond_theory,cond_exp=task03_conditional_days()  # Thực hiện bước xử lý, giữ nguyên cấu trúc và thứ tự code mẫu.
    p_flag,p_actual_spam=task04_bayes()  # Thực hiện bước xử lý, giữ nguyên cấu trúc và thứ tự code mẫu.
    k,prob,p_exact,p_at_least=task05_binomial()  # Thực hiện bước xử lý, giữ nguyên cấu trúc và thứ tự code mẫu.
    if not (cards["P(A)"]==0.5): raise ValueError("Kiểm tra dữ liệu không đạt")  # Kiểm tra bằng if (nếu); khi điều kiện sai sẽ báo lỗi rõ ràng.
    if not (cards["P(B)"]==0.4): raise ValueError("Kiểm tra dữ liệu không đạt")  # Kiểm tra bằng if (nếu); khi điều kiện sai sẽ báo lỗi rõ ràng.
    if not (cards["P(A and B)"]==0.2): raise ValueError("Kiểm tra dữ liệu không đạt")  # Kiểm tra bằng if (nếu); khi điều kiện sai sẽ báo lỗi rõ ràng.
    if not (cards["P(A or B)"]==0.7): raise ValueError("Kiểm tra dữ liệu không đạt")  # Kiểm tra bằng if (nếu); khi điều kiện sai sẽ báo lỗi rõ ràng.
    if not (cond_theory==1.0): raise ValueError("Kiểm tra dữ liệu không đạt")  # Kiểm tra bằng if (nếu); khi điều kiện sai sẽ báo lỗi rõ ràng.
    if not (abs(simulated["experimental_single"]-0.7)<0.04): raise ValueError("Kiểm tra dữ liệu không đạt")  # Kiểm tra bằng if (nếu); khi điều kiện sai sẽ báo lỗi rõ ràng.
    if not (np.isclose(p_flag,0.305)): raise ValueError("Kiểm tra dữ liệu không đạt")  # Kiểm tra bằng if (nếu); khi điều kiện sai sẽ báo lỗi rõ ràng.
    if not (np.isclose(prob.sum(),1)): raise ValueError("Kiểm tra dữ liệu không đạt")  # Kiểm tra bằng if (nếu); khi điều kiện sai sẽ báo lỗi rõ ràng.
    print("Task 1:",cards)  # In kết quả (output: kết quả) để người học đối chiếu.
    print("Task 2:",simulated)  # In kết quả (output: kết quả) để người học đối chiếu.
    print("Task 3 P(A|B), theoretical/experimental:",cond_theory,cond_exp)  # In kết quả (output: kết quả) để người học đối chiếu.
    print("Task 4 P(flag), P(spam|flag):",round(p_flag,5),round(p_actual_spam,5))  # In kết quả (output: kết quả) để người học đối chiếu.
    print("Task 5 P(X=6), P(X>=6):",round(p_exact,6),round(p_at_least,6))  # In kết quả (output: kết quả) để người học đối chiếu.
    if "--no-plot" not in sys.argv:  # Kiểm tra điều kiện; nhánh sau chỉ chạy khi điều kiện đúng.
        save_plot(k,prob)  # Thực hiện bước xử lý, giữ nguyên cấu trúc và thứ tự code mẫu.
if __name__=="__main__":  # Kiểm tra điều kiện; nhánh sau chỉ chạy khi điều kiện đúng.
    main()  # Thực hiện bước xử lý, giữ nguyên cấu trúc và thứ tự code mẫu.
```
