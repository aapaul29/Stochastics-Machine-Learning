import sys, argparse, traceback, random, math
from solution import sigmoid, sigmoid_derivative, softmax

def approx(a, b, tol=1e-4):
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
    ("sigmoid(0)=0.5",        lambda: approx(sigmoid(0.0), 0.5)),
    ("sigmoid large pos ≈ 1", lambda: approx(sigmoid(100.0), 1.0)),
    ("sigmoid large neg ≈ 0", lambda: approx(sigmoid(-100.0), 0.0)),
    ("sigmoid_deriv(0)=0.25", lambda: approx(sigmoid_derivative(0.0), 0.25)),
    ("softmax sums to 1",     lambda: abs(sum(softmax([1.,2.,3.]))-1.0)<1e-5),
    ("softmax example",       lambda: approx(softmax([1.,2.,3.]),
                                              [0.090031,0.244728,0.665241])),
    ("softmax uniform",       lambda: approx(softmax([0.,0.,0.]),
                                              [1/3,1/3,1/3])),
]

HIDDEN_TESTS = [
    ("sigmoid(1)",  lambda: approx(sigmoid(1.0), 0.731059)),
    ("sigmoid(-1)", lambda: approx(sigmoid(-1.0), 0.268941)),
    ("sigmoid_deriv(-1)", lambda: approx(sigmoid_derivative(-1.0),
                                          round(sigmoid(-1.0)*(1-sigmoid(-1.0)),6))),
    ("softmax max shift stable",
     lambda: approx(softmax([1000.,1001.,1002.]), softmax([0.,1.,2.]))),
    ("softmax single → [1.0]",
     lambda: approx(softmax([5.0]), [1.0])),
    ("softmax stress: sums to 1",
     lambda: (random.seed(37), all(
         abs(sum(softmax([random.gauss(0,2) for _ in range(5)]))-1.0)<1e-5
         for _ in range(20)))[1]),
]

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--all",action="store_true")
    args=parser.parse_args()
    print("\n"+"="*55+"\n  CODE EXPERT — Activation Functions\n"+"="*55)
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
