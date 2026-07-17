import sys, argparse, traceback, random
from solution import accuracy, precision, recall, f1_score

def approx(a, b, tol=1e-3):
    return abs(a-b)<=tol

def run_test(name, fn, public=True):
    tag="PUBLIC" if public else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except Exception:
        print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

yt = [1,0,1,1,0,1]; yp = [1,0,1,0,1,1]

PUBLIC_TESTS = [
    ("accuracy example",  lambda: approx(accuracy(yt,yp),  2/3)),
    ("precision example", lambda: approx(precision(yt,yp), 0.75)),
    ("recall example",    lambda: approx(recall(yt,yp),    0.75)),
    ("f1 example",        lambda: approx(f1_score(yt,yp),  0.75)),
    ("perfect predictions",
     lambda: accuracy([1,0,1],[1,0,1])==1.0 and f1_score([1,0,1],[1,0,1])==1.0),
    ("no positives predicted → precision=0",
     lambda: precision([1,1,0],[0,0,0])==0.0),
    ("no positive labels → recall=0",
     lambda: recall([0,0,0],[1,0,1])==0.0),
]

HIDDEN_TESTS = [
    ("all wrong",
     lambda: approx(accuracy([1,1,0,0],[0,0,1,1]), 0.0)),
    ("precision: only TPs",
     lambda: approx(precision([1,1,1],[1,1,1]), 1.0)),
    ("f1 zero denom → 0",
     lambda: f1_score([0,0,0],[0,0,0])==0.0),
    ("stress: accuracy matches manual",
     lambda: (random.seed(43), all(
         approx(accuracy(yt,yp), sum(a==b for a,b in zip(yt,yp))/len(yt))
         for yt,yp in [([random.randint(0,1) for _ in range(20)],
                         [random.randint(0,1) for _ in range(20)]) for _ in range(10)]))[1]),
    ("stress: f1 = 2pr/(p+r)",
     lambda: (random.seed(45), all(
         (lambda p,r,f: approx(f, 2*p*r/(p+r) if p+r>0 else 0.0))(
             precision(yt,yp),recall(yt,yp),f1_score(yt,yp))
         for yt,yp in [([random.randint(0,1) for _ in range(15)],
                         [random.randint(0,1) for _ in range(15)]) for _ in range(10)]))[1]),
]

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--all",action="store_true")
    args=parser.parse_args()
    print("\n"+"="*55+"\n  CODE EXPERT — Classification Metrics\n"+"="*55)
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
