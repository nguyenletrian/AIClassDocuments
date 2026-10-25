"""12 marketing observations: linear model, MSE and gradient descent."""
X=list(range(1,13)) # marketing million VND
Y=[5.2,7,9.3,10.7,13.1,14.9,17.4,19.2,20.8,23.2,25.1,26.9] # revenue million VND
def mse(w,b):
    return sum((w*x+b-y)**2 for x,y in zip(X,Y))/len(X)
def train(lr=0.01,steps=3500):
    w=b=0.0
    for _ in range(steps):
        dw=2*sum((w*x+b-y)*x for x,y in zip(X,Y))/len(X)
        db=2*sum(w*x+b-y for x,y in zip(X,Y))/len(X)
        w-=lr*dw
        b-=lr*db
    return w,b
def main():
    assert len(X)==len(Y)==12
    start=mse(0,0)
    w,b=train()
    end=mse(w,b)
    print(f"Before MSE={start:.3f}; after={end:.3f}; weight={w:.3f}; bias={b:.3f}")
    assert end<start
if __name__ == "__main__":
    main()
