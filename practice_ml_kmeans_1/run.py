import sys, argparse, traceback, random, math
from solution import assign_clusters

def run_test(name, fn, public=True):
    tag="PUBLIC" if public else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except Exception:
        print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

PUBLIC_TESTS = [
    ("Basic 1D, k=2",
     lambda: assign_clusters([[0.],[1.],[3.],[4.]],[[0.],[3.]])==[0,0,1,1]),
    ("All same centroid",
     lambda: assign_clusters([[1.,1.],[2.,2.],[3.,3.]],[[0.,0.]])==[0,0,0]),
    ("k=3 2D",
     lambda: assign_clusters([[0.,0.],[5.,0.],[0.,5.]],
                              [[0.,0.],[5.,0.],[0.,5.]])==[0,1,2]),
    ("Tie → smallest index",
     lambda: assign_clusters([[2.0]],[[1.0],[3.0]])[0]==0),
    ("Returns list of ints",
     lambda: all(isinstance(v,int) for v in assign_clusters([[1.0]],[[0.0],[2.0]]))),
    ("Length = n",
     lambda: len(assign_clusters([[1.],[2.],[3.]],[[0.],[10.]]))==3),
]

HIDDEN_TESTS = [
    ("2D, k=2",
     lambda: assign_clusters([[1.,1.],[4.,4.],[1.,0.],[5.,5.]],
                              [[0.,0.],[5.,5.]])==[0,1,0,1]),
    ("Point on centroid",
     lambda: assign_clusters([[3.,3.]],[[3.,3.],[10.,10.]])==[0]),
    ("k=1 → all 0",
     lambda: assign_clusters([[i] for i in range(10)],[[5.]])==[0]*10),
    ("Stress: matches brute force",
     lambda: (random.seed(23), all(
         assign_clusters(X,C)==[min(range(len(C)),
             key=lambda j:sum((x[d]-C[j][d])**2 for d in range(2)))
             for x in X]
         for X,C in [([[random.uniform(-5,5),random.uniform(-5,5)] for _ in range(20)],
                       [[random.uniform(-5,5),random.uniform(-5,5)] for _ in range(3)])
                      for _ in range(10)]))[1]),
]

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--all",action="store_true")
    args=parser.parse_args()
    print("\n"+"="*55+"\n  CODE EXPERT — k-Means Assignment\n"+"="*55)
    passed=0; total=0
    print("\n── Public Tests ──────────────────────────────────────")
    for name,fn in PUBLIC_TESTS:
        ok=run_test(name,fn); passed+=ok; total+=1
    if args.all:
        print("\n── Hidden Tests ──────────────────────────────────────")
        for name,fn in HIDDEN_TESTS:
            ok=run_test(name,fn,public=False); passed+=ok; total+=1
    print("\n"+"="*55)
    pct=round(100*passed/total) if total else 0
    print(f"  SCORE: {passed}/{total}  ({pct}%)")
    if pct==100: print("  ✓ Full marks!")
    elif pct>=70: print("  ~ Good — check the failing cases above.")
    else: print("  ✗ Keep going — re-read the problem statement.")
    print("="*55+"\n")

if __name__=="__main__": main()
