"""24 synthetic weeks: leakage-safe train/test modeling."""
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
def main():
    rng=np.random.default_rng(2026)
    marketing=np.linspace(3,17,24) # million VND/week
    visitors=np.arange(130,130+24*12,12) # visitors/week
    revenue=12+1.8*marketing+0.09*visitors+rng.normal(0,2,24) # million VND/week
    X=np.column_stack([marketing,visitors])
    assert X.shape==(24,2)
    Xtr,Xte,ytr,yte=train_test_split(X,revenue,test_size=0.25,random_state=2026)
    model=make_pipeline(StandardScaler(),LinearRegression()) # scaler fitted on train only
    model.fit(Xtr,ytr)
    prediction=model.predict(Xte)
    baseline=np.full_like(yte,ytr.mean())
    print("Train/test:",len(ytr),len(yte))
    print("Baseline MAE:",round(mean_absolute_error(yte,baseline),3))
    print("Model MAE:",round(mean_absolute_error(yte,prediction),3))
if __name__ == "__main__":
    main()
