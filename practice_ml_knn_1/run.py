import sys, argparse, traceback, random, math
from collections import Counter
from solution import euclidean_distance, knn_classify

def run_test(name, fn, public=True):
    tag="PUBLIC" if public else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except Exception:
        print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

X4 = [[0.,0.],[1.,0.],[0.,1.],[1.,1.]]
y4 = [0, 0, 1, 1]

PUBLIC_TESTS = [
    ("distance basic", lambda: abs(euclidean_distance([0.,0.],[3.,4.])-5.0)<1e-5),
    ("distance same point", lambda: euclidean_distance([1.,2.],[1.,2.])==0.0),
    ("knn k=1 near [0,0]", lambda: knn_classify(X4,y4,[0.1,0.1],1)==0),
    ("knn k=1 near [1,1]", lambda: knn_classify(X4,y4,[0.9,0.9],1)==1),
    ("knn k=3 near [0.1,0.1]", lambda: knn_classify(X4,y4,[0.1,0.1],3)==0),
    ("returns int", lambda: isinstance(knn_classify(X4,y4,[0.5,0.5],1),int)),
]

HIDDEN_TESTS = [
    ("distance 1D", lambda: abs(euclidean_distance([3.],[7.])-4.0)<1e-5),
    ("distance 3D", lambda: abs(euclidean_distance([1.,2.,3.],[4.,6.,3.])-5.0)<1e-5),
    ("knn k=3 near [0.9,0.1] → class 0",
     lambda: knn_classify(X4,y4,[0.9,0.1],3)==0),
    ("tie in votes → smallest label",
     lambda: knn_classify([[0.],[1.],[2.],[3.]],[0,1,0,1],[1.5],2) in (0,1)),
    ("k=n → majority class overall",
     lambda: knn_classify([[float(i)] for i in range(10)],
                           [0]*7+[1]*3,[999.],10)==0),
    ("stress",
     lambda: (random.seed(21), all(
         knn_classify([[float(i)] for i in range(10)],
                       [i%2 for i in range(10)],[float(q)],1)==q%2
         for q in range(10)))[1]),
]

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--all",action="store_true")
    args=parser.parse_args()
    print("\n"+"="*55+"\n  CODE EXPERT — k-NN Classification\n"+"="*55)
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
