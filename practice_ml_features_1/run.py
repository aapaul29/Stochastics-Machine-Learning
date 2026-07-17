import sys, argparse, traceback, random, math
from solution import poly_features

def approx(a, b, tol=1e-5):
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
    ("degree 3",  lambda: approx(poly_features(2.0,3),[1.0,2.0,4.0,8.0])),
    ("degree 2",  lambda: approx(poly_features(0.5,2),[1.0,0.5,0.25])),
    ("degree 0",  lambda: approx(poly_features(3.0,0),[1.0])),
    ("degree 1",  lambda: approx(poly_features(5.0,1),[1.0,5.0])),
    ("length = degree+1", lambda: len(poly_features(2.0,5))==6),
    ("first element always 1", lambda: poly_features(99.0,4)[0]==1.0),
]

HIDDEN_TESTS = [
    ("negative x", lambda: approx(poly_features(-2.0,3),[1.0,-2.0,4.0,-8.0])),
    ("x=0",        lambda: approx(poly_features(0.0,3),[1.0,0.0,0.0,0.0])),
    ("x=1",        lambda: all(v==1.0 for v in poly_features(1.0,5))),
    ("fractional", lambda: approx(poly_features(0.1,4),[1.0,0.1,0.01,0.001,0.0001])),
    ("stress",
     lambda: (random.seed(13), all(
         approx(poly_features(x,d), [round(x**i,6) for i in range(d+1)])
         for x,d in [(random.uniform(-3,3), random.randint(0,6)) for _ in range(20)]))[1]),
]

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--all",action="store_true")
    args=parser.parse_args()
    print("\n"+"="*55+"\n  CODE EXPERT — Polynomial Features\n"+"="*55)
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
