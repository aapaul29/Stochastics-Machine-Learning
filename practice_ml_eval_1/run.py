import sys, argparse, traceback, random
from solution import kfold_indices

def run_test(name, fn, public=True):
    tag="PUBLIC" if public else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except Exception:
        print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

PUBLIC_TESTS = [
    ("n=6, k=3 structure",
     lambda: kfold_indices(6,3)==[([2,3,4,5],[0,1]),([0,1,4,5],[2,3]),([0,1,2,3],[4,5])]),
    ("returns k tuples",
     lambda: len(kfold_indices(10,5))==5),
    ("val+train = all indices",
     lambda: all(sorted(tr+val)==list(range(10))
                 for tr,val in kfold_indices(10,5))),
    ("val sizes ~= n/k",
     lambda: all(abs(len(val)-2)<=1 for _,val in kfold_indices(10,5))),
    ("k=1 → all train, empty val (or all val)",
     lambda: len(kfold_indices(5,1))==1),
    ("k=n → LOO (each val is 1 sample)",
     lambda: all(len(val)==1 for _,val in kfold_indices(5,5))),
]

HIDDEN_TESTS = [
    ("n=10, k=3 sizes",
     lambda: sorted([len(v) for _,v in kfold_indices(10,3)])==[3,3,4]),
    ("no overlap between folds",
     lambda: (lambda folds: all(
         len(set(folds[i][1]) & set(folds[j][1]))==0
         for i in range(4) for j in range(4) if i!=j))(kfold_indices(12,4))),
    ("train+val disjoint",
     lambda: all(len(set(tr) & set(val))==0 for tr,val in kfold_indices(8,4))),
    ("n=7, k=3 → sizes 3,2,2",
     lambda: sorted([len(v) for _,v in kfold_indices(7,3)])==[2,2,3]),
    ("stress: all indices covered in each fold",
     lambda: all(all(sorted(tr+val)==list(range(n))
                     for tr,val in kfold_indices(n,k))
                 for n,k in [(15,5),(20,4),(9,3)])),
]

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--all",action="store_true")
    args=parser.parse_args()
    print("\n"+"="*55+"\n  CODE EXPERT — k-Fold Cross-Validation\n"+"="*55)
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
