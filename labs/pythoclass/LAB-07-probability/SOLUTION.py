"""LAB SESSION 7 — Sample space, simulation, conditional probability, Bayes and binomial.

Run with --no-plot for console-only evaluation.
Dependencies: numpy, scipy, matplotlib (plotting only).
"""
from pathlib import Path
import sys
import numpy as np
from scipy.stats import binom

SEED=2026
TRIALS=5000

def task01_cards():
    space=set(range(1,11))
    a={x for x in space if x%2==0}
    b={x for x in space if x>6}
    return {
        "space":sorted(space),"A":sorted(a),"B":sorted(b),
        "P(A)":len(a)/len(space),
        "P(B)":len(b)/len(space),
        "P(A and B)":len(a&b)/len(space),
        "P(A or B)":len(a|b)/len(space),
    }

def task02_free_throws():
    rng=np.random.default_rng(SEED)
    single=rng.random(TRIALS)<0.7
    first=rng.random(TRIALS)<0.7
    second=rng.random(TRIALS)<0.6
    both=first & second
    either=first | second
    return {
        "experimental_single":single.mean(),
        "experimental_both":both.mean(),
        "experimental_either":either.mean(),
        "theoretical_single":0.7,
        "theoretical_both":0.7*0.6,
        "theoretical_either":1-(1-0.7)*(1-0.6),
    }

def task03_conditional_days():
    # Mon=0, ..., Sun=6; A weekdays Mon–Fri, B Mon–Thu.
    A=set(range(5))
    B=set(range(4))
    theoretical=len(A&B)/len(B)
    rng=np.random.default_rng(SEED+1)
    drawn=rng.integers(0,7,size=TRIALS)
    given_b=np.isin(drawn,list(B))
    joint=np.isin(drawn,list(A&B))
    experimental=float(joint.sum()/given_b.sum())
    return theoretical,experimental

def task04_bayes():
    p_spam=0.30
    p_flag_given_spam=0.90
    p_flag_given_clean=0.05
    p_flag=p_spam*p_flag_given_spam+(1-p_spam)*p_flag_given_clean
    posterior=p_spam*p_flag_given_spam/p_flag
    return p_flag,posterior

def task05_binomial():
    k=np.arange(0,9)
    probs=binom.pmf(k,n=8,p=0.75)
    return k,probs,float(binom.pmf(6,n=8,p=0.75)),float(probs[6:].sum())

def save_plot(k,probs):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    folder=Path(__file__).resolve().parent/"outputs"
    folder.mkdir(exist_ok=True)
    fig,ax=plt.subplots()
    ax.bar(k,probs)
    ax.set(xlabel="Number of resolved requests (k)",ylabel="P(X=k)",title="Binomial(n=8, p=0.75)")
    ax.set_xticks(k)
    ax.grid(True,axis="y")
    target=folder/"binomial_distribution.png"
    fig.savefig(target,dpi=140,bbox_inches="tight")
    plt.close(fig)
    print("Saved:",target)

def main():
    cards=task01_cards()
    simulated=task02_free_throws()
    cond_theory,cond_exp=task03_conditional_days()
    p_flag,p_actual_spam=task04_bayes()
    k,prob,p_exact,p_at_least=task05_binomial()
    assert cards["P(A)"]==0.5
    assert cards["P(B)"]==0.4
    assert cards["P(A and B)"]==0.2
    assert cards["P(A or B)"]==0.7
    assert cond_theory==1.0
    assert abs(simulated["experimental_single"]-0.7)<0.04
    assert np.isclose(p_flag,0.305)
    assert np.isclose(prob.sum(),1)
    print("Task 1:",cards)
    print("Task 2:",simulated)
    print("Task 3 P(A|B), theoretical/experimental:",cond_theory,cond_exp)
    print("Task 4 P(flag), P(spam|flag):",round(p_flag,5),round(p_actual_spam,5))
    print("Task 5 P(X=6), P(X>=6):",round(p_exact,6),round(p_at_least,6))
    if "--no-plot" not in sys.argv:
        save_plot(k,prob)
if __name__=="__main__":
    main()
