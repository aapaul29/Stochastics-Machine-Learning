import sys, argparse, traceback, random, math
import numpy as np
from solution import add_bias_column, normal_equations

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
    ("add_bias_column basic",
     lambda: add_bias_column([[1.0,2.0],[3.0,4.0]])==[[1.0,1.0,2.0],[1.0,3.0,4.0]]),
    ("add_bias_column length",
     lambda: all(len(r)==3 for r in add_bias_column([[1.0,2.0],[3.0,4.0]]))),
    ("Perfect linear fit (y=1+2x)",
     lambda: approx(normal_equations([[0.],[1.],[2.],[3.]],[1.,3.,5.,7.]),[1.0,2.0])),
    ("Intercept only",
     lambda: approx(normal_equations([[0.],[1.],[2.]],[3.,3.,3.]),[3.0,0.0])),
    ("Returns list of length d+1",
     lambda: len(normal_equations([[1.,2.],[3.,4.],[5.,6.]],[1.,2.,3.]))==3),
]

HIDDEN_TESTS = [
    ("2D features",
     lambda: approx(normal_equations([[1.,0.],[0.,1.],[1.,1.]],[2.,3.,5.]),[0.,2.,3.])),
    ("Noisy linear — bias in range",
     lambda: (random.seed(5),
              abs(normal_equations([[float(i)] for i in range(50)],
                                    [2.0*i+1.0+random.gauss(0,0.1) for i in range(50)])[0]-1.0)<0.3 and
              abs(normal_equations([[float(i)] for i in range(50)],
                                    [2.0*i+1.0+random.gauss(0,0.1) for i in range(50)])[1]-2.0)<0.3
              )[1]),
    ("Normal eqs solve MSE",
     lambda: (lambda w,X,y:
         (lambda Xb,wn: float(np.linalg.norm(Xb@wn-np.array(y)))<0.5)(
             np.column_stack([np.ones(len(X)),np.array(X)]),
             np.array(normal_equations(X,y))))(
         normal_equations([[float(i)] for i in range(10)],[float(i)*3+2 for i in range(10)]),
         [[float(i)] for i in range(10)],[float(i)*3+2 for i in range(10)])),
]

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--all",action="store_true")
    args=parser.parse_args()
    print("\n"+"="*55+"\n  CODE EXPERT — Normal Equations (OLS)\n"+"="*55)
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
