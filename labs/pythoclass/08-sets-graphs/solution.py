"""12 synthetic learners: set operations, Jaccard and adjacency."""
from itertools import combinations
SUBJECTS={
"HV001":{"Python","AI","Math"},"HV002":{"Python","AI","SQL"},
"HV003":{"Python","SQL"},"HV004":{"Java","Web"},
"HV005":{"Python","AI","Math"},"HV006":{"AI","Math"},
"HV007":{"Web","SQL"},"HV008":{"Python","AI"},
"HV009":{"Python","Math"},"HV010":{"Python","AI","SQL"},
"HV011":{"Math","Statistics"},"HV012":{"AI","Math","Statistics"}}
def jaccard(a,b):
    both=a|b
    return len(a&b)/len(both) if both else 1.0
def graph(threshold=0.5):
    adj={key:set() for key in SUBJECTS}
    for a,b in combinations(SUBJECTS,2):
        if jaccard(SUBJECTS[a],SUBJECTS[b])>=threshold:
            adj[a].add(b); adj[b].add(a)
    return adj
def main():
    assert len(SUBJECTS)==12
    print("Subjects:",sorted(set().union(*SUBJECTS.values())))
    print("Jaccard HV001-HV005:",jaccard(SUBJECTS["HV001"],SUBJECTS["HV005"]))
    adj=graph()
    print("Vertices:",len(adj),"edges:",sum(len(x) for x in adj.values())//2)
    for key,values in adj.items(): print(key,sorted(values))
if __name__ == "__main__":
    main()
