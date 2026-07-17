import sys, argparse, traceback, random
from solution import epsilon_greedy

def run_test(name, fn, public=True):
    tag="PUBLIC" if public else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except Exception:
        print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

PUBLIC_TESTS = [
    ("epsilon=0 → greedy",
     lambda: epsilon_greedy([1.,3.,2.],0.0,0)==1),
    ("epsilon=0 tie → smallest index",
     lambda: epsilon_greedy([5.,5.,1.],0.0,0)==0),
    ("epsilon=1 → random (in range)",
     lambda: epsilon_greedy([1.,3.,2.],1.0,0) in (0,1,2)),
    ("returns int",
     lambda: isinstance(epsilon_greedy([0.,1.],0.0,0),int)),
    ("epsilon=0 always best",
     lambda: all(epsilon_greedy([0.,1.,0.],0.0,s)==1 for s in range(20))),
    ("seeded reproducibility",
     lambda: epsilon_greedy([1.,2.,3.],0.5,7)==epsilon_greedy([1.,2.,3.],0.5,7)),
]

HIDDEN_TESTS = [
    ("epsilon=1 seed=0 deterministic",
     lambda: epsilon_greedy([0.,0.,0.],1.0,0)==(random.seed(0) or None or random.random() and random.randint(0,2))),
    ("greedy 3 actions",
     lambda: epsilon_greedy([10.,-5.,3.],0.0,99)==0),
    ("explore then exploit pattern",
     lambda: (lambda results: sum(r==2 for r in results)>8)(
         [epsilon_greedy([0.,0.,10.],0.1,s) for s in range(100)])),
    ("stress: epsilon=0 always best",
     lambda: all(epsilon_greedy([float(i%3==j) for j in range(3)],0.0,s)==i%3
                 for i,s in enumerate(range(30)))),
    ("stress: epsilon=1 all actions seen",
     lambda: len(set(epsilon_greedy([1.,2.,3.],1.0,s) for s in range(50)))==3),
]

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--all",action="store_true")
    args=parser.parse_args()
    print("\n"+"="*55+"\n  CODE EXPERT — Epsilon-Greedy Selection\n"+"="*55)
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
