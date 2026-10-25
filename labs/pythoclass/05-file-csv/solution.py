"""Read 15 CSV transactions; do not modify the input file."""
import csv
from collections import defaultdict
from pathlib import Path
DATA=Path(__file__).resolve().parents[1]/"data/sales_sample.csv"
def load(path=DATA):
    with Path(path).open(encoding="utf-8",newline="") as stream:
        reader=csv.DictReader(stream)
        required={"order_id","category","quantity","unit_price"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError("Missing CSV columns")
        rows=list(reader)
    for r in rows:
        r["quantity"]=int(r["quantity"])
        r["unit_price"]=float(r["unit_price"])
        if r["quantity"]<=0 or r["unit_price"]<0: raise ValueError("Invalid transaction")
    return rows
def main():
    records=load()
    assert len(records)==15
    revenue=defaultdict(float)
    for r in records: revenue[r["category"]]+=r["quantity"]*r["unit_price"]
    for category,value in sorted(revenue.items()): print(category,round(value,2),"thousand VND")
    print("Total:",round(sum(revenue.values()),2))
if __name__ == "__main__":
    main()
