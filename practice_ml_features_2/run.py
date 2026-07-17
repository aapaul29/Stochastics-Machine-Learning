import sys, argparse, traceback, random, math
from solution import fit_standardizer, apply_standardizer

def approx(a, b, tol=1e-4):
    if isinstance(a,(list,tuple)) and isinstance(b,(list,tuple)):
        if len(a)!=len(b): return False
        return all(approx(x,y,tol) for x,y in zip(a,b))
    return abs(a-b)<=tol

def run_test(name, fn, public=True):
    tag="PUBLIC" if public else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except Exception:
        print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

X3 = [[1.,2.],[3.,4.],[5.,6.]]

PUBLIC_TESTS = [
    ("fit mu",
     lambda: approx(fit_standardizer(X3)[0],[3.0,4.0])),
    ("fit sigma",
     lambda: approx(fit_standardizer(X3)[1],[round(math.sqrt(8/3),6)]*2)),
    ("apply standardize",
     lambda: (lambda mu,sg: approx(apply_standardizer([[1.,2.]],mu,sg),
                                    [[round((1-3)/math.sqrt(8/3),6)]*2]))(
         *fit_standardizer(X3))),
    ("apply: mean → [0,0]",
     lambda: (lambda mu,sg: approx(apply_standardizer([[3.,4.]],mu,sg),[[0.0,0.0]]))(
         *fit_standardizer(X3))),
    ("zero sigma → 0.0",
     lambda: approx(apply_standardizer([[5.0]],[5.0],[0.0]),[[0.0]])),
    ("shape preserved",
     lambda: len(apply_standardizer(X3,*fit_standardizer(X3)))==3),
]

HIDDEN_TESTS = [
    ("standardized mean ≈ 0",
     lambda: all(abs(sum(r[j] for r in apply_standardizer(X3,*fit_standardizer(X3)))/3)<1e-5
                 for j in range(2))),
    ("standardized std ≈ 1",
     lambda: (lambda Xs: all(
         abs(math.sqrt(sum(r[j]**2 for r in Xs)/len(Xs))-1.0)<1e-4 for j in range(2)))(
         apply_standardizer(X3,*fit_standardizer(X3)))),
    ("1D features",
     lambda: approx(apply_standardizer([[0.],[2.],[4.]],*fit_standardizer([[0.],[2.],[4.]])),
                    [[-1.224745],[0.0],[1.224745]])),
    ("stress: standardized mean≈0",
     lambda: (random.seed(17),
              all(abs(sum(r[0] for r in apply_standardizer(X,*fit_standardizer(X)))/len(X))<1e-5
                  for X in [[[random.gauss(m,s)] for _ in range(30)]
                             for m,s in [(2,1),(5,3),(-1,2)]]))[1]),
]

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--all",action="store_true")
    args=parser.parse_args()
    print("\n"+"="*55+"\n  CODE EXPERT — Feature Standardization\n"+"="*55)
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
