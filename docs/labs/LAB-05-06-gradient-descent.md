# Lab Session 5 & 6 — Gradient Descent, đạo hàm và Hessian

**Word gốc:** `LAB SESSION 5_6.docx`; bản sao trong `MON 2` không tính thành lab thứ hai. Mọi phần dưới là trích từ `labs/pythoclass/LAB-05-06-gradient-descent/LAB.md`, `DEMO.py` và các hàm đã kiểm tra của `SOLUTION.py` (kiến thức PY-24, PY-28, PY-30..PY-33). **Không phát minh dữ liệu hay thuật toán mới.** Đoạn code là các hàm của *cùng một script*, cần chạy với import/bộ dữ liệu và hàm phụ trợ bên dưới.

## English — Original problem and dataset

## Problem Description
In this project, you will build a simple machine learning model to predict students' exam scores based on their study hours.

You will use Python, NumPy, Matplotlib, and SymPy to explore mathematical concepts used in machine learning, including **partial derivatives, gradients, gradient descent, and the Hessian matrix**.

## Dataset

| Study Hours (X) | Exam Score (y) |
|---:|---:|
| 1 | 35 |
| 2 | 40 |
| 3 | 50 |
| 4 | 55 |
| 5 | 65 |
| 6 | 70 |
| 7 | 80 |
| 8 | 85 |

## Tiếng Việt — Tổng quan và dữ liệu

Mục tiêu là xây dựng mô hình học máy tuyến tính đơn giản để dự đoán điểm kiểm tra từ số giờ học, tìm hiểu **đạo hàm riêng, gradient, Gradient Descent và Hessian** bằng Python, NumPy, Matplotlib, SymPy. Dữ liệu đề Word gồm **8 cặp** giờ học–điểm: (1,35), (2,40), (3,50), (4,55), (5,65), (6,70), (7,80), (8,85). Giờ học tính theo giờ; điểm theo đơn vị điểm bài thi.

**Mã và dữ liệu nền trích từ `SOLUTION.py`:**

```python
import numpy as np  # NumPy thao tác với mảng và phép tính số.
import sympy as sp  # SymPy đạo hàm biểu thức chính xác.
from pathlib import Path  # Đường dẫn lưu biểu đồ.
X = np.array([1,2,3,4,5,6,7,8], dtype=float)
Y = np.array([35,40,50,55,65,70,80,85], dtype=float)
```

## Bài 1 — Create and Visualize the Dataset

### English — Original Word requirement

- Create two NumPy arrays: `X` (students' study hours) and `y` (students' exam scores).
- Use Matplotlib to create a scatter plot of study hours versus exam scores.
- Add an appropriate title, axis labels, and grid.

### Tiếng Việt — Bản dịch

**Tạo và vẽ dữ liệu:** Dùng NumPy tạo hai mảng `X` (giờ học) và `y` (điểm kiểm tra) theo đúng 8 hàng; vẽ đồ thị scatter bằng Matplotlib, thêm tiêu đề, nhãn trục và lưới. Không tự thay bộ dữ liệu gốc.

### Bài giải — Code đã có trong demo/giáo trình

Hàm từ `labs/pythoclass/LAB-05-06-gradient-descent/SOLUTION.py`: `task01_dataset()`, `save_plots()`. Code nguồn `DEMO.py` chỉ là bản thực hành ban đầu; hàm lời giải tham chiếu được phân biệt rõ, **không nhận là trích nguyên demo**.

```python
# Hàm task01_dataset() trích từ script lời giải tham chiếu hiện có.
def task01_dataset():
    assert X.shape == Y.shape == (8,)
    return {"hours":X.tolist(),"scores":Y.tolist()}

# Hàm save_plots() trích từ script lời giải tham chiếu hiện có.
def save_plots(w,b,losses):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    root=Path(__file__).resolve().parent/"outputs"
    root.mkdir(exist_ok=True)
    fig,ax=plt.subplots()
    ax.scatter(X,Y,label="Observed scores")
    ax.plot(X,predict(X,w,b),label="Fitted prediction")
    ax.set(xlabel="Study hours",ylabel="Exam score (points)",title="Hours vs. exam scores")
    ax.grid(True)
    ax.legend()
    fig.savefig(root/"hours_vs_scores.png",dpi=140,bbox_inches="tight")
    plt.close(fig)
    fig,ax=plt.subplots()
    ax.plot(np.arange(1,len(losses)+1),losses)
    ax.set(xlabel="Epoch",ylabel="MSE (squared score units)",title="Gradient Descent Training")
    ax.grid(True)
    fig.savefig(root/"loss_curve.png",dpi=140,bbox_inches="tight")
    plt.close(fig)
    print("Wrote",root/"hours_vs_scores.png","and",root/"loss_curve.png")
```

### Giải thích quy trình giải và công thức

Mô hình dữ liệu: `X=[1,2,3,4,5,6,7,8]` giờ; `y=[35,40,50,55,65,70,80,85]` điểm. Biểu đồ scatter vẽ `X` theo trục ngang và `y` theo trục đứng.

**Công thức liên quan:** Không dùng công thức học mô hình ở bước chỉ trực quan hóa; `plt.scatter(X,Y)` hiển thị từng cặp giờ/điểm.

## Bài 2 — Build a Simple Linear Prediction Model

### English — Original Word requirement

Use the following model:

$$
\hat{y} = wX+b
$$

where `w` is the weight, `b` is the bias, and `ŷ` is the predicted exam score.

- Implement a `predict(X, w, b)` function.
- Implement a `compute_loss(y_true, y_pred)` function using Mean Squared Error (MSE):

$$
\mathrm{MSE}=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat y_i)^2.
$$

- Initialize `w = 0` and `b = 0`. Calculate/display initial predictions and MSE.

### Tiếng Việt — Bản dịch

**Mô hình tuyến tính và sai số:** Dự đoán điểm bằng `ŷ = wX+b`, với `w` là hệ số thay đổi theo mỗi giờ học, `b` là độ lệch gốc. Viết `predict(X,w,b)` và `compute_loss(y_true,y_pred)` dùng MSE. Khởi tạo `w=b=0`, tính dự đoán và MSE ban đầu.

### Bài giải — Code đã có trong demo/giáo trình

Hàm từ `labs/pythoclass/LAB-05-06-gradient-descent/SOLUTION.py`: `predict()`, `compute_loss()`, `task02_initial_model()`. Code nguồn `DEMO.py` chỉ là bản thực hành ban đầu; hàm lời giải tham chiếu được phân biệt rõ, **không nhận là trích nguyên demo**.

```python
# Hàm predict() trích từ script lời giải tham chiếu hiện có.
def predict(x,w,b):
    return w*x+b

# Hàm compute_loss() trích từ script lời giải tham chiếu hiện có.
def compute_loss(y_true,y_pred):
    return float(np.mean((y_true-y_pred)**2))

# Hàm task02_initial_model() trích từ script lời giải tham chiếu hiện có.
def task02_initial_model():
    guesses = predict(X,0.0,0.0)
    initial_loss = compute_loss(Y,guesses)
    return guesses,initial_loss
```

### Giải thích quy trình giải và công thức

`predict()` nhân từng số giờ với `w`, cộng `b`; `compute_loss()` tính từng hiệu điểm thật-dự đoán, bình phương, lấy trung bình. Khởi tạo cả hai bằng 0 để có đường chuẩn trước khi học.

**Công thức liên quan:** \(\hat y_i=wX_i+b\), \(\mathrm{MSE}=\frac{1}{n}\sum_{i=1}^n(y_i-\hat y_i)^2\). Đơn vị MSE là bình phương đơn vị điểm.

## Bài 3 — Calculate Partial Derivatives and the Hessian

### English — Original Word requirement

Consider the loss function for one sample:

$$
L(w,b)=(2w+b-5)^2.
$$

- Calculate the partial derivative of `L` with respect to `w`.
- Calculate the partial derivative of `L` with respect to `b`.
- Construct the gradient vector.
- Calculate/display the Hessian matrix using SymPy.

### Tiếng Việt — Bản dịch

**Đạo hàm riêng và Hessian:** Với `L(w,b)=(2w+b−5)²`, tính đạo hàm theo `w`, theo `b`, ghép vector gradient và lập ma trận Hessian bằng SymPy. Đây là ví dụ một điểm, chưa phải loss trên toàn bộ 8 quan sát.

### Bài giải — Code đã có trong demo/giáo trình

Hàm từ `labs/pythoclass/LAB-05-06-gradient-descent/SOLUTION.py`: `task03_symbolic_single()`. Code nguồn `DEMO.py` chỉ là bản thực hành ban đầu; hàm lời giải tham chiếu được phân biệt rõ, **không nhận là trích nguyên demo**.

```python
# Hàm task03_symbolic_single() trích từ script lời giải tham chiếu hiện có.
def task03_symbolic_single():
    w,b=sp.symbols("w b",real=True)
    loss=(2*w+b-5)**2
    variables=(w,b)
    gradient=sp.Matrix([sp.diff(loss,v) for v in variables])
    hessian=sp.hessian(loss,variables)
    return loss,gradient,hessian
```

### Giải thích quy trình giải và công thức

Dùng `sp.symbols` tạo biến biểu thức, `sp.diff` lấy đạo hàm, `sp.hessian` trả ma trận đạo hàm bậc hai. Kiểm chứng: gradient của biểu thức mẫu có thành phần theo w và b lần lượt bằng `4(2w+b−5)` và `2(2w+b−5)`.

**Công thức liên quan:** \(\nabla L=[4(2w+b-5),\;2(2w+b-5)]^T\); \(H=\begin{bmatrix}8&4\\4&2\end{bmatrix}\).

## Bài 4 — Implement Gradient Descent

### English — Original Word requirement

Implement Gradient Descent from scratch to train the model on the dataset above.

For MSE, use:

$$
\frac{\partial L}{\partial w}=\frac{2}{n}\sum_i X_i(wX_i+b-y_i),\qquad
\frac{\partial L}{\partial b}=\frac{2}{n}\sum_i(wX_i+b-y_i).
$$

Update parameters by subtracting the learning rate multiplied by each gradient component.

- Initialize `w = 0`, `b = 0`.
- Set the learning rate to `0.01` and the number of epochs to `1000`.
- Calculate gradients and update `w`, `b` each epoch.
- Record MSE during training.
- Display final `w`, `b`, and MSE.

### Tiếng Việt — Bản dịch

**Gradient Descent:** Tự cài cập nhật `w,b` cho hàm MSE trên 8 điểm, ban đầu đều 0, learning rate `0.01`, `1000` epoch. Mỗi epoch tính hai gradient, cập nhật bằng cách trừ learning rate × gradient, ghi lại MSE và hiển thị kết quả cuối.

### Bài giải — Code đã có trong demo/giáo trình

Hàm từ `labs/pythoclass/LAB-05-06-gradient-descent/SOLUTION.py`: `task04_train()`. Code nguồn `DEMO.py` chỉ là bản thực hành ban đầu; hàm lời giải tham chiếu được phân biệt rõ, **không nhận là trích nguyên demo**.

```python
# Hàm task04_train() trích từ script lời giải tham chiếu hiện có.
def task04_train(learning_rate=0.01,epochs=1000):
    w=b=0.0
    history=[]
    n=X.size
    for _ in range(epochs):
        residual=predict(X,w,b)-Y
        dw=(2/n)*np.dot(X,residual)
        db=(2/n)*residual.sum()
        w-=learning_rate*dw
        b-=learning_rate*db
        history.append(compute_loss(Y,predict(X,w,b)))
    return w,b,np.array(history)
```

### Giải thích quy trình giải và công thức

Mỗi vòng dự đoán điểm, lấy phần dư `predict(X,w,b)-Y`, tính gradient `dw`,`db`, trừ learning_rate nhân gradient, lưu MSE mới; không tạo thuật toán khác với script tham khảo.

**Công thức liên quan:** \(\partial_w L=\frac2n\sum_i X_i(wX_i+b-y_i)\), \(\partial_b L=\frac2n\sum_i(wX_i+b-y_i)\). Cập nhật \(w\leftarrow w-0.01\,\partial_wL\) và \(b\leftarrow b-0.01\,\partial_bL\).

## Bài 5 — Analyze the Gradient and Hessian of the Full Dataset Loss

### English — Original Word requirement

Apply the full-dataset loss:

$$
L(w,b)=\frac{1}{n}\sum_i(y_i-wX_i-b)^2.
$$

- Calculate/display the gradient vector and Hessian matrix.
- Evaluate the gradient at the trained `w` and `b`.
- Calculate Hessian eigenvalues using NumPy.
- Briefly explain what gradient and Hessian tell us about optimization.

### Tiếng Việt — Bản dịch

**Gradient/Hessian của cả dataset:** Lập loss trung bình trên 8 quan sát, tính gradient và Hessian của cả tập, thay `w,b` đã huấn luyện vào gradient, tính eigenvalue của Hessian bằng NumPy và giải thích ý nghĩa hướng giảm/độ cong.

### Bài giải — Code đã có trong demo/giáo trình

Hàm từ `labs/pythoclass/LAB-05-06-gradient-descent/SOLUTION.py`: `task05_symbolic_full()`. Code nguồn `DEMO.py` chỉ là bản thực hành ban đầu; hàm lời giải tham chiếu được phân biệt rõ, **không nhận là trích nguyên demo**.

```python
# Hàm task05_symbolic_full() trích từ script lời giải tham chiếu hiện có.
def task05_symbolic_full(trained_w,trained_b):
    w,b=sp.symbols("w b",real=True)
    values=[sp.Integer(int(x)) for x in X]
    targets=[sp.Integer(int(y)) for y in Y]
    n=len(values)
    full_loss=sum((yi-w*xi-b)**2 for xi,yi in zip(values,targets))/n
    gradient=sp.Matrix([sp.diff(full_loss,w),sp.diff(full_loss,b)])
    hessian=sp.hessian(full_loss,(w,b))
    gradient_at=gradient.subs({w:trained_w,b:trained_b}).evalf()
    eigvals=np.linalg.eigvalsh(np.asarray(hessian,dtype=float))
    return gradient,hessian,gradient_at,eigvals
```

### Giải thích quy trình giải và công thức

Biểu thức loss tổng được tạo từ 8 giá trị gốc trong `X`,`Y`; SymPy tự tính gradient và Hessian. `subs` thay tham số học được, `np.linalg.eigvalsh` cho trị riêng ma trận đối xứng. Không lẫn với Hessian một điểm ở bài 3.

**Công thức liên quan:** \(L(w,b)=\frac1n\sum_i(y_i-wX_i-b)^2\). Hessian mô tả độ cong; trị riêng dương cho biết độ cong theo hướng tương ứng không âm/định hướng cực tiểu đối với bài toán này.

## Cách kiểm tra theo code đã học

- `SOLUTION.py` chứa `main()` kiểm tra MSE sau khi học nhỏ hơn MSE ban đầu, lưu 1000 giá trị loss và kiểm tra eigenvalue Hessian dương. Có thể chạy bản tham khảo từ thư mục `labs/pythoclass/LAB-05-06-gradient-descent` bằng `python SOLUTION.py --no-plot`.
- Muốn vẽ hình dùng `python SOLUTION.py`; hàm đã có `save_plots()` ghi đồ thị scatter/đường dự đoán và MSE theo epoch vào thư mục output của mã tham khảo. Không tạo ảnh/đoạn code mới trong tài liệu Word giải.
- Nguồn kiến thức: bài PY-30 (loss), PY-31 (đạo hàm), PY-32 (gradient descent), PY-33 (Hessian). Tổng hợp chỉ là *một file* `LAB-05-06-gradient-descent.md`.
