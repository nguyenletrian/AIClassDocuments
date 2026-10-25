"""20 observations: descriptive statistics, sample ratio, bootstrap."""
import random
from statistics import mean,median,pstdev,quantiles
MINUTES=[8,12,10,14,9,11,16,18,13,15,11,12,20,14,17,9,10,13,15,19]
def interval(values,n=1500):
    rng=random.Random(2026)
    estimates=sorted(mean(rng.choices(values,k=len(values))) for _ in range(n))
    return estimates[int(.025*n)],estimates[int(.975*n)-1]
def main():
    assert len(MINUTES)==20
    q1,q2,q3=quantiles(MINUTES,n=4,method="inclusive")
    print("Count:",len(MINUTES),"Mean:",round(mean(MINUTES),2),"Median:",median(MINUTES))
    print("Std:",round(pstdev(MINUTES),2),"Q1/Q2/Q3:",q1,q2,q3)
    print("On time within 15 min:",sum(x<=15 for x in MINUTES)/len(MINUTES))
    print("Bootstrap mean interval:",interval(MINUTES))
if __name__ == "__main__":
    main()
