# LAB-05-06-gradient-descent — nguyên đề tiếng Anh, bản dịch Việt, hướng giải và code đầy đủ

**Nguồn:** đề gốc chuyển sang `labs/pythoclass/LAB-05-06-gradient-descent/LAB.md` từ Word; code hoàn chỉnh từ `labs/pythoclass/LAB-05-06-gradient-descent/SOLUTION.py`, đối chiếu `DEMO.py` và các bài giáo trình đã học. Các chú thích bổ sung giải thích code hiện hữu; không thay đổi công thức, dữ liệu hay thuật toán. **Một lab = một tài liệu duy nhất.**

---

## PART 1 — COMPLETE ORIGINAL ENGLISH ASSIGNMENT

# LAB SESSION 5 & 6

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

## Requirements

### Task 1: Create and Visualize the Dataset
- Create two NumPy arrays: `X` (students' study hours) and `y` (students' exam scores).
- Use Matplotlib to create a scatter plot of study hours versus exam scores.
- Add an appropriate title, axis labels, and grid.

### Task 2: Build a Simple Linear Prediction Model
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

### Task 3: Calculate Partial Derivatives and the Hessian
Consider the loss function for one sample:

$$
L(w,b)=(2w+b-5)^2.
$$

- Calculate the partial derivative of `L` with respect to `w`.
- Calculate the partial derivative of `L` with respect to `b`.
- Construct the gradient vector.
- Calculate/display the Hessian matrix using SymPy.

### Task 4: Implement Gradient Descent
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

### Task 5: Analyze the Gradient and Hessian of the Full Dataset Loss
Apply the full-dataset loss:

$$
L(w,b)=\frac{1}{n}\sum_i(y_i-wX_i-b)^2.
$$

- Calculate/display the gradient vector and Hessian matrix.
- Evaluate the gradient at the trained `w` and `b`.
- Calculate Hessian eigenvalues using NumPy.
- Briefly explain what gradient and Hessian tell us about optimization.

---

## PHẦN 2 — BẢN DỊCH TIẾNG VIỆT TOÀN BỘ ĐỀ

# LAB SESSION 5 & 6 — Hồi quy tuyến tính và Gradient Descent

## Mô tả bài toán
Xây dựng một mô hình học máy đơn giản để dự đoán **điểm thi của sinh viên** dựa vào **số giờ học**. Dùng Python, NumPy, Matplotlib và SymPy để tìm hiểu đạo hàm riêng, gradient, thuật toán Gradient Descent và ma trận Hessian.

## Dữ liệu

| Số giờ học (X, giờ) | Điểm thi (y, điểm) |
|---:|---:|
| 1 | 35 |
| 2 | 40 |
| 3 | 50 |
| 4 | 55 |
| 5 | 65 |
| 6 | 70 |
| 7 | 80 |
| 8 | 85 |

## Yêu cầu

### Bài 1 — Tạo và trực quan hóa dữ liệu
Tạo hai mảng NumPy `X` và `y` chứa số giờ học và điểm. Dùng Matplotlib vẽ scatter plot giờ học so với điểm thi; đặt tiêu đề, nhãn hai trục và lưới.

### Bài 2 — Xây dựng mô hình dự đoán tuyến tính
Sử dụng mô hình **ŷ = wX + b**, trong đó `w` là trọng số, `b` là hệ số chệch, `ŷ` là điểm dự đoán. Viết `predict(X,w,b)` và `compute_loss(y_true,y_pred)` dùng MSE (trung bình bình phương sai số):

\[
\mathrm{MSE}=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat y_i)^2.
\]

Khởi tạo `w=0`, `b=0`, hiển thị dự đoán đầu tiên và MSE ban đầu.

### Bài 3 — Đạo hàm riêng và Hessian
Với hàm một mẫu **L(w,b)=(2w+b−5)²**, tính đạo hàm riêng theo `w`, theo `b`, ghép vector gradient và tính ma trận Hessian bằng SymPy.

### Bài 4 — Cài đặt Gradient Descent
Tự huấn luyện mô hình theo MSE trên dữ liệu đã cho. Dùng **learning rate = 0,01**, **epochs = 1000**, khởi tạo `w=b=0`. Mỗi epoch tính gradient:

\[
\frac{\partial L}{\partial w}=\frac2n\sum_i X_i(wX_i+b-y_i),\qquad
\frac{\partial L}{\partial b}=\frac2n\sum_i(wX_i+b-y_i).
\]

Sau đó trừ learning rate nhân gradient để cập nhật hai tham số, ghi lại MSE qua mỗi epoch. Hiển thị `w`, `b`, MSE cuối cùng.

### Bài 5 — Gradient/Hessian cho toàn bộ dữ liệu
Với **L(w,b) = (1/n) Σᵢ (yᵢ−wXᵢ−b)²**, tính và hiển thị gradient vector, Hessian. Thay hai giá trị `w,b` đã học vào gradient và tính các eigenvalue của Hessian bằng NumPy. Giải thích gradient và Hessian cho biết điều gì về quá trình tối ưu.

---

## Quy trình giải chi tiết và các công thức liên quan

Các bước bám theo file Word, code mẫu và lời giải đã có; không tự nghĩ thuật toán mới. Đọc dữ liệu → kiểm tra kích thước/tham số → tính toán hoặc mô phỏng → đối chiếu kết quả với điều kiện lý thuyết → trình bày/biểu đồ. Các hàm đã tách trong code chỉ để tổ chức chương trình; **nguyên code đầy đủ** nằm ở phần cuối.

### Bài 1 — Cách giải và đối chiếu

Mô hình dữ liệu: `X=[1,2,3,4,5,6,7,8]` giờ; `y=[35,40,50,55,65,70,80,85]` điểm. Biểu đồ scatter vẽ `X` theo trục ngang và `y` theo trục đứng.

**Công thức liên quan:** Không dùng công thức học mô hình ở bước chỉ trực quan hóa; `plt.scatter(X,Y)` hiển thị từng cặp giờ/điểm.

**Kiến thức/công thức trọng tâm:** giữ nguyên 8 dòng dữ liệu X=1..8 và điểm tương ứng; vẽ scatter và đường hồi quy theo giờ/điểm.

### Bài 2 — Cách giải và đối chiếu

`predict()` nhân từng số giờ với `w`, cộng `b`; `compute_loss()` tính từng hiệu điểm thật-dự đoán, bình phương, lấy trung bình. Khởi tạo cả hai bằng 0 để có đường chuẩn trước khi học.

**Công thức liên quan:** \(\hat y_i=wX_i+b\), \(\mathrm{MSE}=\frac{1}{n}\sum_{i=1}^n(y_i-\hat y_i)^2\). Đơn vị MSE là bình phương đơn vị điểm.

**Kiến thức/công thức trọng tâm:** MSE = (1/n)∑(y−ŷ)²; ŷ=wX+b; đơn vị MSE là điểm².

### Bài 3 — Cách giải và đối chiếu

Dùng `sp.symbols` tạo biến biểu thức, `sp.diff` lấy đạo hàm, `sp.hessian` trả ma trận đạo hàm bậc hai. Kiểm chứng: gradient của biểu thức mẫu có thành phần theo w và b lần lượt bằng `4(2w+b−5)` và `2(2w+b−5)`.

**Công thức liên quan:** \(\nabla L=[4(2w+b-5),\;2(2w+b-5)]^T\); \(H=\begin{bmatrix}8&4\\4&2\end{bmatrix}\).

**Kiến thức/công thức trọng tâm:** đạo hàm riêng SymPy `diff`; Hessian ví dụ một điểm L=(2w+b−5)² có gradient [4(2w+b−5),2(2w+b−5)], Hessian [[8,4],[4,2]].

### Bài 4 — Cách giải và đối chiếu

Mỗi vòng dự đoán điểm, lấy phần dư `predict(X,w,b)-Y`, tính gradient `dw`,`db`, trừ learning_rate nhân gradient, lưu MSE mới; không tạo thuật toán khác với script tham khảo.

**Công thức liên quan:** \(\partial_w L=\frac2n\sum_i X_i(wX_i+b-y_i)\), \(\partial_b L=\frac2n\sum_i(wX_i+b-y_i)\). Cập nhật \(w\leftarrow w-0.01\,\partial_wL\) và \(b\leftarrow b-0.01\,\partial_bL\).

**Kiến thức/công thức trọng tâm:** mỗi epoch cập nhật w,b trừ 0.01×gradient; tính lại MSE, lưu đủ 1000 epoch; gradient w=(2/n) Σ X(wX+b−y), b=(2/n) Σ(wX+b−y).

### Bài 5 — Cách giải và đối chiếu

Biểu thức loss tổng được tạo từ 8 giá trị gốc trong `X`,`Y`; SymPy tự tính gradient và Hessian. `subs` thay tham số học được, `np.linalg.eigvalsh` cho trị riêng ma trận đối xứng. Không lẫn với Hessian một điểm ở bài 3.

**Công thức liên quan:** \(L(w,b)=\frac1n\sum_i(y_i-wX_i-b)^2\). Hessian mô tả độ cong; trị riêng dương cho biết độ cong theo hướng tương ứng không âm/định hướng cực tiểu đối với bài toán này.

**Kiến thức/công thức trọng tâm:** hàm loss đầy đủ 8 mẫu khác Hessian một mẫu; tính eigenvalue bằng `eigvalsh` vì Hessian đối xứng; so gradient ở nghiệm đã học.

---

## PHẦN 4 — TOÀN BỘ CODE PYTHON CÙNG CHÚ THÍCH

**Script hoàn chỉnh lấy từ lời giải tham khảo trong repo;** các dòng `#` giải thích mục đích các bước. Đặt nguyên khối vào `lab_solution.py`. Phụ thuộc: numpy, matplotlib, sympy. Có thể chạy `python lab_solution.py --no-plot` để chỉ in kết quả và chạy kiểm tra, hoặc bỏ flag để dùng hàm vẽ của code nguồn. Nguồn demo học viên có thể chỉ minh họa một phần, nên đây là bản `SOLUTION.py` đã tồn tại, không tự nhận là code viết tay nguyên gốc.

```python
"""LAB 5&6 — linear regression, MSE, SymPy gradient/Hessian and plots.

Run: python SOLUTION.py --no-plot
For figures: python SOLUTION.py (saves two PNGs to outputs/).
Requires: numpy matplotlib sympy
"""
import sys
from pathlib import Path
import numpy as np
import sympy as sp

# Eight observations from the source Word brief, X in study hours, y in exam points.
X = np.array([1,2,3,4,5,6,7,8], dtype=float)
Y = np.array([35,40,50,55,65,70,80,85], dtype=float)

# Hàm tính y_hat = w*x + b.
def predict(x,w,b):
    return w*x+b

# Hàm tính trung bình bình phương sai số.
def compute_loss(y_true,y_pred):
    return float(np.mean((y_true-y_pred)**2))

# Đối chiếu đủ tám cặp giờ học và điểm từ đề.
def task01_dataset():
    assert X.shape == Y.shape == (8,)
    return {"hours":X.tolist(),"scores":Y.tolist()}

# Tính điểm dự đoán lúc w=b=0 và MSE trước học.
def task02_initial_model():
    guesses = predict(X,0.0,0.0)
    initial_loss = compute_loss(Y,guesses)
    return guesses,initial_loss

# Dùng đạo hàm SymPy cho loss một mẫu, không lẫn toàn bộ dữ liệu.
def task03_symbolic_single():
    w,b=sp.symbols("w b",real=True)
    loss=(2*w+b-5)**2
    variables=(w,b)
    gradient=sp.Matrix([sp.diff(loss,v) for v in variables])
    hessian=sp.hessian(loss,variables)
    return loss,gradient,hessian

# Cập nhật w,b qua đúng 1000 epoch với learning rate 0.01.
def task04_train(learning_rate=0.01,epochs=1000):
    w=b=0.0
    history=[]
    n=X.size
    for _ in range(epochs):
        # Phần dư là dự đoán trừ điểm thật, dùng để tính đạo hàm MSE.
        residual=predict(X,w,b)-Y
        # Gradient theo w lấy tổng có trọng số số giờ học.
        dw=(2/n)*np.dot(X,residual)
        # Gradient theo b lấy trung bình tổng phần dư.
        db=(2/n)*residual.sum()
        w-=learning_rate*dw
        b-=learning_rate*db
        # Lưu MSE sau mỗi epoch để so tốc độ hội tụ.
        history.append(compute_loss(Y,predict(X,w,b)))
    return w,b,np.array(history)

# Tính gradient, Hessian cho loss của tám quan sát.
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

# Vẽ scatter, đường hồi quy và lịch sử MSE; lưu hình thay vì mở GUI.
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

# Hàm phụ trợ từ lời giải hiện có; giữ nguyên logic.
def main():
    task01_dataset()
    initial_preds,initial_mse=task02_initial_model()
    example_loss,example_grad,example_hessian=task03_symbolic_single()
    w,b,history=task04_train(learning_rate=0.01,epochs=1000)
    full_grad,full_hessian,at_final,eigenvalues=task05_symbolic_full(w,b)
    final_mse=compute_loss(Y,predict(X,w,b))
    assert history.shape==(1000,)
    assert final_mse < initial_mse
    assert all(eigenvalues > 0)
    assert np.isclose(final_mse,history[-1])
    print("Initial predictions:",initial_preds)
    print("Initial MSE:",round(initial_mse,3))
    print("Single-sample symbolic loss:",example_loss)
    print("Single-sample gradient:",example_grad,"Hessian:",example_hessian)
    print(f"Trained w={w:.6f}, b={b:.6f}, final MSE={final_mse:.6f}")
    print("Full gradient:",full_grad)
    print("Full Hessian:",full_hessian)
    print("Gradient evaluated at trained parameters:",at_final)
    print("Hessian eigenvalues:",eigenvalues)
    if "--no-plot" not in sys.argv:
        save_plots(w,b,history)
if __name__=="__main__":
    main()
```

**Chú ý:** Tất cả dữ liệu gốc, giá trị tham số, công thức và hàm thực thi đều nằm trong một script ở trên; không cần chắp nối lời giải rời từng câu.
