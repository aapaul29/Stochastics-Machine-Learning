import sys, argparse, traceback, random, math
from solution import knn_predict

def approx(a, b, tol=1e-3):
    return abs(a-b)<=tol

def run_test(name, fn, public=True):
    tag="PUBLIC" if public else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except Exception:
        print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

Xr = [[0.],[1.],[2.],[3.]]
yr = [0., 1., 2., 3.]

PUBLIC_TESTS = [
    ("k=2 midpoint", lambda: approx(knn_predict(Xr,yr,[1.5],2), 1.5)),
    ("k=3 left",     lambda: approx(knn_predict(Xr,yr,[0.0],3), 1.0)),
    ("k=1 exact",    lambda: approx(knn_predict(Xr,yr,[2.0],1), 2.0)),
    ("k=4 all",      lambda: approx(knn_predict(Xr,yr,[1.5],4), 1.5)),
    ("returns float", lambda: isinstance(knn_predict(Xr,yr,[1.0],1),float)),
    ("rounding to 4 dp",
     lambda: len(str(knn_predict([[0.],[1.],[2.]],[1.,2.,3.],[0.5],2)).split('.')[-1])<=4),
]

HIDDEN_TESTS = [
    ("2D query",
     lambda: approx(knn_predict([[0.,0.],[1.,1.],[2.,2.]],[0.,10.,20.],[1.,1.],1), 10.0)),
    ("k=1 nearest", lambda: approx(knn_predict(Xr,yr,[2.9],1), 3.0)),
    ("k=n → global mean",
     lambda: approx(knn_predict(Xr,yr,[50.],4), 1.5)),
    ("constant targets",
     lambda: approx(knn_predict([[float(i)] for i in range(5)],[7.0]*5,[2.5],3), 7.0)),
    ("stress",
     lambda: (random.seed(19), all(
         approx(knn_predict([[float(i)] for i in range(10)],
                             [float(i)*2 for i in range(10)],[float(q)],3),
                round(sum(sorted([abs(i-q) for i in range(10)])[:3]
                          and [float(i)*2 for i in sorted(range(10),key=lambda i:abs(i-q))[:3]])/3,4))
         for q in range(10)))[1]),
]

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--all",action="store_true")
    args=parser.parse_args()
    print("\n"+"="*55+"\n  CODE EXPERT — k-NN Regression\n"+"="*55)
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
