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

def predict(x,w,b):
    return w*x+b

def compute_loss(y_true,y_pred):
    return float(np.mean((y_true-y_pred)**2))

def task01_dataset():
    assert X.shape == Y.shape == (8,)
    return {"hours":X.tolist(),"scores":Y.tolist()}

def task02_initial_model():
    guesses = predict(X,0.0,0.0)
    initial_loss = compute_loss(Y,guesses)
    return guesses,initial_loss

def task03_symbolic_single():
    w,b=sp.symbols("w b",real=True)
    loss=(2*w+b-5)**2
    variables=(w,b)
    gradient=sp.Matrix([sp.diff(loss,v) for v in variables])
    hessian=sp.hessian(loss,variables)
    return loss,gradient,hessian

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
