import sys, argparse, traceback, random, math
import numpy as np
from solution import ridge_regression

def approx(a, b, tol=1e-2):
    if isinstance(a,(list,tuple)) and isinstance(b,(list,tuple)):
        return len(a)==len(b) and all(abs(x-y)<=tol for x,y in zip(a,b))
    return abs(a-b)<=tol

def run_test(name, fn, public=True):
    tag="PUBLIC" if public else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except Exception:
        print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

PUBLIC_TESTS = [
    ("lam=0 recovers OLS",
     lambda: approx(ridge_regression([[0.],[1.],[2.],[3.]],[1.,3.,5.,7.],0.0),[1.0,2.0])),
    ("Returns d+1 weights",
     lambda: len(ridge_regression([[1.,2.],[3.,4.]],[1.,2.],1.0))==3),
    ("Large lam shrinks weights",
     lambda: all(abs(w)<2.0 for w in ridge_regression([[0.],[1.],[2.],[3.]],[1.,3.,5.,7.],100.0))),
    ("Larger lam → smaller norm",
     lambda: (lambda w1,w2: sum(x**2 for x in w1)>sum(x**2 for x in w2))(
         ridge_regression([[0.],[1.],[2.],[3.]],[1.,3.,5.,7.],0.1),
         ridge_regression([[0.],[1.],[2.],[3.]],[1.,3.,5.,7.],100.0))),
    ("2D features, lam=0",
     lambda: approx(ridge_regression([[1.,0.],[0.,1.],[1.,1.]],[2.,3.,5.],0.0),[0.,2.,3.])),
]

HIDDEN_TESTS = [
    ("lam=0 vs lam=1 differ",
     lambda: not approx(
         ridge_regression([[0.],[1.],[2.],[3.]],[1.,3.,5.,7.],0.0),
         ridge_regression([[0.],[1.],[2.],[3.]],[1.,3.,5.,7.],1.0))),
    ("Intercept-only problem",
     lambda: approx(ridge_regression([[0.],[1.],[2.]],[3.,3.,3.],0.0),[3.0,0.0])),
    ("Stress: matches numpy formula",
     lambda: (random.seed(3), all(
         (lambda X,y,lam:
             approx(ridge_regression(X,y,lam),
                    (lambda Xb,yv: [round(float(w),4) for w in
                        np.linalg.solve(Xb.T@Xb+lam*np.eye(Xb.shape[1]),Xb.T@yv)])(
                        np.column_stack([np.ones(len(X)),np.array(X)]),np.array(y))))(
             [[random.gauss(0,1)] for _ in range(10)],
             [random.gauss(0,1) for _ in range(10)],
             random.uniform(0.1,5.0))
         for _ in range(10)))[1]),
]

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--all",action="store_true")
    args=parser.parse_args()
    print("\n"+"="*55+"\n  CODE EXPERT — Ridge Regression\n"+"="*55)
    passed=0; total=0
    print("\n── Public Tests ──────────────────────────────────────")
    for name,fn in PUBLIC_TESTS:
        ok=run_test(name,fn); passed+=ok; total+=1
    if args.all:
        print("\n── Hidden Tests ──────────────────────────────────────")
        random.seed(42)
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
