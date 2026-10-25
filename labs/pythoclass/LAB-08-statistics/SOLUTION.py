"""LAB SESSION 8 — descriptive statistics, 6 bins, IQR, sample and t-test."""
from pathlib import Path
import sys
import numpy as np
import pandas as pd
from scipy import stats

USAGE_MINUTES=np.array([
    35,45,50,55,60,65,70,75,80,85,
    90,95,100,105,110,115,120,120,125,130,
    135,140,145,150,155,160,165,170,175,180,
    185,190,195,200,205,210,215,220,225,230,
    240,250,260,270,280,290,300,320,350,480
],dtype=float)

def task01_descriptive(values):
    # ddof=1: SAMPLE variance/std rather than population versions.
    return {
        "mean":float(values.mean()),"median":float(np.median(values)),
        "mode":float(pd.Series(values).mode().iloc[0]),
        "minimum":float(values.min()),"maximum":float(values.max()),
        "range":float(np.ptp(values)),
        "sample_variance":float(values.var(ddof=1)),
        "sample_std":float(values.std(ddof=1)),
    }

def task02_frequency(values):
    # Half-open bins [0,60), [60,120), ... so boundary values count exactly once.
    bins=[0,60,120,180,240,360,500]
    labels=["0–<60","60–<120","120–<180","180–<240","240–<360","360–<500"]
    groups=pd.cut(values,bins=bins,labels=labels,right=False,include_lowest=True)
    freq=groups.value_counts(sort=False)
    frame=pd.DataFrame({"frequency":freq})
    frame["cumulative"]=frame["frequency"].cumsum()
    assert frame["frequency"].sum()==len(values)
    return bins,frame

def task03_outliers(values):
    q1,q2,q3=np.percentile(values,[25,50,75])
    iqr=q3-q1
    low,high=q1-1.5*iqr,q3+1.5*iqr
    unusual=values[(values<low)|(values>high)]
    return q1,q2,q3,iqr,low,high,unusual

def task04_sample_and_test(values):
    rng=np.random.default_rng(2026)
    sample=rng.choice(values,size=10,replace=False)
    result=stats.ttest_1samp(values,popmean=120.0)
    return sample,float(sample.mean()),float(result.statistic),float(result.pvalue)

def task05_conclusion(descriptive,outliers,pvalue):
    typical=descriptive["median"]
    decision="reject H0" if pvalue<0.05 else "fail to reject H0"
    print(f"Typical use is around median {typical:.1f} minutes/day.")
    print(f"Sample SD is {descriptive['sample_std']:.1f} minutes, with {len(outliers)} IQR outlier(s).")
    print(f"One-sample t-test vs 120 min/day: p={pvalue:.6g}; {decision} at alpha=0.05.")
    print("Recommendation: study long-duration sessions separately and design user-friendly break reminders.")

def save_plot(values,bins):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    output=Path(__file__).resolve().parent/"outputs"
    output.mkdir(exist_ok=True)
    fig,ax=plt.subplots()
    ax.hist(values,bins=bins,edgecolor="black")
    ax.set(xlabel="Daily app usage (minutes)",ylabel="Users",title="Daily usage of 50 users")
    ax.grid(True,axis="y")
    target=output/"usage_histogram.png"
    fig.savefig(target,dpi=140,bbox_inches="tight")
    plt.close(fig)
    print("Saved:",target)

def main():
    assert USAGE_MINUTES.shape==(50,)
    desc=task01_descriptive(USAGE_MINUTES)
    bins,freq=task02_frequency(USAGE_MINUTES)
    q1,q2,q3,iqr,lo,hi,outliers=task03_outliers(USAGE_MINUTES)
    sample,sample_mean,t,p=task04_sample_and_test(USAGE_MINUTES)
    assert len(sample)==10
    assert 0<=p<=1
    print("Descriptive:",desc)
    print("Frequency:\n",freq.to_string())
    print(f"Q1={q1:.2f}, Q2={q2:.2f}, Q3={q3:.2f}, IQR={iqr:.2f}")
    print(f"Outlier limits [{lo:.2f},{hi:.2f}], values:",outliers.tolist())
    print("Sample of 10:",sample.tolist(),"sample mean:",round(sample_mean,2))
    print("t:",round(t,4),"p:",round(p,6))
    task05_conclusion(desc,outliers,p)
    if "--no-plot" not in sys.argv:
        save_plot(USAGE_MINUTES,bins)
if __name__=="__main__":
    main()
