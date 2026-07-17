import sys, argparse, traceback, random, math
from solution import q_update

def approx(a, b, tol=1e-5):
    return abs(a-b)<=tol

def run_test(name, fn, public=True):
    tag="PUBLIC" if public else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except Exception:
        print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

PUBLIC_TESTS = [
    ("basic example",
     # target=1+0.9*5=5.5, delta=5.5-0=5.5, q_new=0+0.1*5.5=0.55
     lambda: approx(q_update(0.0,1.0,5.0,0.1,0.9), 0.55)),
    ("alpha=1 → full target",
     # target=2+0.5*3=3.5, q_new=0+1*(3.5-0)=3.5
     lambda: approx(q_update(0.0,2.0,3.0,1.0,0.5), 3.5)),
    ("gamma=0 ignores future",
     # target=5+0=5, q_new=0+0.1*5=0.5
     lambda: approx(q_update(0.0,5.0,100.0,0.1,0.0), 0.5)),
    ("already at target → no change",
     # target=1+1*9=10, q_new=10+0.5*(10-10)=10
     lambda: approx(q_update(10.0,1.0,9.0,0.5,1.0), 10.0)),
    ("negative reward",
     # target=-1+0.9*0=-1, delta=-1-5=-6, q_new=5+0.2*(-6)=3.8
     lambda: approx(q_update(5.0,-1.0,0.0,0.2,0.9), 3.8)),
    ("returns float",
     lambda: isinstance(q_update(0.0,1.0,1.0,0.1,0.9),float)),
]

HIDDEN_TESTS = [
    ("terminal state (max_q_next=0)",
     # target=10, q_new=2+0.5*(10-2)=6
     lambda: approx(q_update(2.0,10.0,0.0,0.5,0.9), 6.0)),
    ("alpha=0 → no update",
     lambda: approx(q_update(3.14,10.0,5.0,0.0,0.9), 3.14)),
    ("formula check",
     lambda: all(approx(q_update(q,r,m,a,g), round(q+a*(r+g*m-q),6))
                 for q,r,m,a,g in [(1.,2.,3.,0.1,0.9),(0.5,0.,1.,0.5,0.8),
                                     (2.,1.,4.,0.3,0.95)])),
    ("stress",
     lambda: (random.seed(41), all(
         approx(q_update(q,r,m,a,g),round(q+a*(r+g*m-q),6))
         for q,r,m,a,g in [(random.uniform(-5,5),random.uniform(-2,10),
                             random.uniform(0,10),random.uniform(0,1),
                             random.uniform(0,1)) for _ in range(30)]))[1]),
]

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--all",action="store_true")
    args=parser.parse_args()
    print("\n"+"="*55+"\n  CODE EXPERT — Q-Learning Bellman Update\n"+"="*55)
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
