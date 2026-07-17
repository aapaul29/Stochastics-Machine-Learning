import sys, argparse, traceback
import numpy as np
from solution import build_pipeline

def run_test(name, fn, public=True):
    tag="PUBLIC" if public else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except Exception:
        print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

def make_dataset(seed=0, n=300, noise=0.3, missing_frac=0.1):
    rng = np.random.default_rng(seed)
    X = rng.normal(size=(n, 3))
    y = 2*X[:,0] - X[:,1] + 0.5*X[:,2] + rng.normal(scale=noise, size=n)
    mask = rng.random(size=X.shape) < missing_frac
    X[mask] = np.nan
    return X, y

def r2(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred)**2)
    ss_tot = np.sum((y_true - np.mean(y_true))**2)
    return 1 - ss_res/ss_tot if ss_tot>0 else 0.0

PUBLIC_TESTS = [
    ("Pipeline has 3 steps",
     lambda: len(build_pipeline().steps)==3),
    ("Step 1 is SimpleImputer",
     lambda: "SimpleImputer" in type(build_pipeline().steps[0][1]).__name__),
    ("Step 2 is StandardScaler",
     lambda: "StandardScaler" in type(build_pipeline().steps[1][1]).__name__),
    ("Step 3 is LinearRegression",
     lambda: "LinearRegression" in type(build_pipeline().steps[2][1]).__name__),
    ("Pipeline fits and predicts",
     lambda: (lambda X,y: build_pipeline().fit(X,y).predict(X).shape[0]==len(y))(
         *make_dataset())),
]

HIDDEN_TESTS = [
    ("R² ≥ 0.80 on clean data",
     lambda: (lambda X,y,p: (p.fit(X[:200],y[:200]), r2(y[200:],p.predict(X[200:])))[1]>=0.80)(
         *make_dataset(seed=1,noise=0.2), build_pipeline())),
    ("R² ≥ 0.75 with missing values",
     lambda: (lambda X,y,p: (p.fit(X[:200],y[:200]), r2(y[200:],p.predict(X[200:])))[1]>=0.75)(
         *make_dataset(seed=2,noise=0.3,missing_frac=0.15), build_pipeline())),
    ("Handles NaN without error",
     lambda: (lambda X,y: not np.any(np.isnan(build_pipeline().fit(X,y).predict(X))))(
         *make_dataset(seed=3))),
    ("R² > 0 (better than mean)",
     lambda: (lambda X,y,p: (p.fit(X[:200],y[:200]), r2(y[200:],p.predict(X[200:])))[1]>0)(
         *make_dataset(seed=4), build_pipeline())),
]

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--all",action="store_true")
    args=parser.parse_args()
    print("\n"+"="*55+"\n  CODE EXPERT — Regression Pipeline\n"+"="*55)
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
