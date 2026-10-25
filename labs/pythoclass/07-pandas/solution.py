"""15 transactions: DataFrame, missing values, groupby."""
from pathlib import Path
import pandas as pd
DATA=Path(__file__).resolve().parents[1]/"data/sales_sample.csv"
def main():
    df=pd.read_csv(DATA)
    assert len(df)==15
    print("Shape:",df.shape,"\nMissing:",df.isna().sum().to_dict())
    print("Duplicate order IDs:",df["order_id"].duplicated().sum())
    if (df["quantity"]<=0).any() or (df["unit_price"]<0).any(): raise ValueError("Invalid transaction")
    df=df.copy()
    df["revenue"]=df["quantity"]*df["unit_price"]
    result=df.groupby("category",as_index=False)["revenue"].sum().sort_values("revenue",ascending=False)
    print(result.to_string(index=False))
    print("Total (thousand VND):",df["revenue"].sum())
if __name__ == "__main__":
    main()
