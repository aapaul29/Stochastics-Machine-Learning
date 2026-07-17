import sys, argparse, traceback, random, math
from solution import mse, r_squared

def approx(a, b, tol=1e-3):
    return abs(a - b) <= tol

def run_test(name, fn, public=True):
    tag="PUBLIC" if public else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except Exception:
        print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

PUBLIC_TESTS = [
    ("MSE basic example",
     lambda: approx(mse([3.,-0.5,2.,7.],[2.5,0.,2.,8.]), 0.375)),
    ("R² basic example",
     lambda: approx(r_squared([3.,-0.5,2.,7.],[2.5,0.,2.,8.]), 0.9486)),
    ("Perfect prediction MSE=0",
     lambda: approx(mse([1.,2.,3.],[1.,2.,3.]), 0.0)),
    ("Perfect prediction R²=1",
     lambda: approx(r_squared([1.,2.,3.],[1.,2.,3.]), 1.0)),
    ("Constant prediction R²≤0",
     lambda: r_squared([1.,2.,3.],[2.,2.,2.]) <= 0.0),
    ("MSE single element",
     lambda: approx(mse([5.],[3.]), 4.0)),
    ("R² constant targets all same → 1.0",
     lambda: approx(r_squared([3.,3.,3.],[3.,3.,3.]), 1.0)),
]

HIDDEN_TESTS = [
    ("MSE larger example",
     lambda: approx(mse([1.,2.,3.,4.],[1.,1.,1.,1.]), 3.5/1, 1e-3) or
             approx(mse([1.,2.,3.,4.],[1.,1.,1.,1.]), (0+1+4+9)/4, 1e-3)),
    ("R² matches formula",
     lambda: (lambda yt,yp,yb:
         approx(r_squared(yt,yp), 1 - sum((a-b)**2 for a,b in zip(yt,yp)) /
                sum((a-yb)**2 for a in yt), 1e-3))(
         [2.,4.,5.,4.,5.],[2.8,3.4,4.,5.,5.],sum([2.,4.,5.,4.,5.])/5)),
    ("MSE stress",
     lambda: (random.seed(11), all(
         approx(mse(yt,yp), sum((a-b)**2 for a,b in zip(yt,yp))/len(yt), 1e-3)
         for yt,yp in [([random.gauss(0,1) for _ in range(20)],
                         [random.gauss(0,1) for _ in range(20)]) for _ in range(10)]))[1]),
    ("R² constant targets mismatch → 0.0",
     lambda: approx(r_squared([3.,3.,3.],[1.,2.,3.]), 0.0)),
    ("R² negative possible",
     lambda: r_squared([1.,2.,3.],[5.,5.,5.]) < 0),
]

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--all",action="store_true")
    args=parser.parse_args()
    print("\n"+"="*55+"\n  CODE EXPERT — MSE and R²\n"+"="*55)
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
