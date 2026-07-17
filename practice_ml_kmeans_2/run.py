import sys, argparse, traceback, random, math
from solution import update_centroids, kmeans_converged

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

PUBLIC_TESTS = [
    ("update 1D k=2",
     lambda: approx(update_centroids([[0.],[2.],[4.],[6.]],[0,0,1,1],2),[[1.0],[5.0]])),
    ("update 2D k=2",
     lambda: approx(update_centroids([[0.,0.],[2.,2.],[4.,0.],[6.,2.]],[0,0,1,1],2),
                    [[1.0,1.0],[5.0,1.0]])),
    ("converged True (same)",
     lambda: kmeans_converged([[1.0],[5.0]],[[1.0],[5.0]],1e-4)==True),
    ("converged False (moved)",
     lambda: kmeans_converged([[1.0],[5.0]],[[1.1],[5.0]],1e-4)==False),
    ("converged with tol",
     lambda: kmeans_converged([[0.0]],[[0.05]],0.1)==True),
    ("empty cluster → zeros",
     lambda: approx(update_centroids([[1.],[2.]],[0,0],2),[[1.5],[0.0]])),
]

HIDDEN_TESTS = [
    ("k=3",
     lambda: approx(update_centroids([[0.],[3.],[6.],[1.],[4.],[7.]],[0,1,2,0,1,2],3),
                    [[0.5],[3.5],[6.5]])),
    ("all same cluster",
     lambda: approx(update_centroids([[1.],[2.],[3.]],[0,0,0],1),[[2.0]])),
    ("converged boundary",
     lambda: kmeans_converged([[0.0]],[[1e-6]],1e-4)==True and
             kmeans_converged([[0.0]],[[0.5]],1e-4)==False),
    ("stress update matches mean",
     lambda: (random.seed(29), all(
         all(abs(update_centroids(X,A,2)[j][0] -
                 (sum(X[i][0] for i in range(len(X)) if A[i]==j)/max(1,sum(1 for a in A if a==j))))<1e-4
             for j in range(2))
         for X,A in [([[random.uniform(0,10)] for _ in range(20)],
                       [random.randint(0,1) for _ in range(20)]) for _ in range(10)]))[1]),
]

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--all",action="store_true")
    args=parser.parse_args()
    print("\n"+"="*55+"\n  CODE EXPERT — k-Means Update & Convergence\n"+"="*55)
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
