import sys, argparse, traceback
import numpy as np
from sklearn.datasets import make_classification
from sklearn.svm import SVC
from solution import find_best_svc

def run_test(name, fn, public=True):
    tag="PUBLIC" if public else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except Exception:
        print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

def make_data(seed=0, n=300):
    X, y = make_classification(n_samples=n, n_features=5, n_informative=3,
                                 n_redundant=1, random_state=seed)
    return X[:200], y[:200], X[200:], y[200:]

X_tr, y_tr, X_te, y_te = make_data()

PUBLIC_TESTS = [
    ("Returns SVC",
     lambda: isinstance(find_best_svc(X_tr,y_tr), SVC)),
    ("Fitted (has support_vectors_)",
     lambda: hasattr(find_best_svc(X_tr,y_tr),"support_vectors_")),
    ("Predicts correct shape",
     lambda: find_best_svc(X_tr,y_tr).predict(X_te).shape==(len(y_te),)),
    ("Accuracy > 0.5 (better than random)",
     lambda: (find_best_svc(X_tr,y_tr).predict(X_te)==y_te).mean()>0.5),
]

HIDDEN_TESTS = [
    ("Accuracy ≥ 0.70 on test",
     lambda: (find_best_svc(X_tr,y_tr).predict(X_te)==y_te).mean()>=0.70),
    ("Accuracy ≥ 0.70 on second dataset",
     lambda: (lambda X2tr,y2tr,X2te,y2te:
         (find_best_svc(X2tr,y2tr).predict(X2te)==y2te).mean()>=0.70)(
         *make_data(seed=7))),
    ("Uses C in {0.1,1,10,...}",
     lambda: find_best_svc(X_tr,y_tr).C in (0.1,1,10,100,0.01,1000)),
    ("Kernel is linear or rbf",
     lambda: find_best_svc(X_tr,y_tr).kernel in ("linear","rbf","poly","sigmoid")),
]

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--all",action="store_true")
    args=parser.parse_args()
    print("\n"+"="*55+"\n  CODE EXPERT — SVC Grid Search\n"+"="*55)
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
