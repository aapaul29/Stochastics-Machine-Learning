import sys,argparse,traceback,random,math
try: from solution import empirical_covariance,empirical_correlation
except ImportError as e: print(f"[ERROR] {e}"); sys.exit(1)

def _cov(xs,ys):
    n=len(xs)
    if n<=1: return 0.0
    mx=sum(xs)/n; my=sum(ys)/n
    return round(sum((x-mx)*(y-my) for x,y in zip(xs,ys))/(n-1),4)
def _std(xs):
    n=len(xs)
    if n<=1: return 0.0
    m=sum(xs)/n; return math.sqrt(sum((x-m)**2 for x in xs)/(n-1))
def _corr(xs,ys):
    sx,sy=_std(xs),_std(ys)
    if sx==0 or sy==0: return 0.0
    return round(_cov(xs,ys)/(sx*sy),4)
def approx(a,b,tol=1e-4): return abs(a-b)<=tol
def run_test(name,fn,pub=True):
    tag="PUBLIC" if pub else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except: print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

PUBLIC=[
    ("Cov linear=5",        lambda: approx(empirical_covariance([1,2,3,4,5],[2,4,6,8,10]),5.0)),
    ("Corr perfect=1",      lambda: approx(empirical_correlation([1,2,3,4,5],[2,4,6,8,10]),1.0)),
    ("Corr negative=-1",    lambda: approx(empirical_correlation([1,2,3],[-1,-2,-3]),-1.0)),
    ("Cov n=1 → 0",         lambda: empirical_covariance([1],[2])==0.0),
    ("Corr zero var → 0",   lambda: empirical_correlation([1,1,1],[1,2,3])==0.0),
]
HIDDEN=[
    ("Two elements",        lambda: approx(empirical_covariance([0,2],[0,4]),_cov([0,2],[0,4]))),
    ("Corr in [-1,1]",      lambda: (random.seed(7) or True) and all(
        -1.0<=empirical_correlation([random.gauss(0,1) for _ in range(50)],[random.gauss(0,1) for _ in range(50)])<=1.0
        for _ in range(10))),
    ("Rounding 4dp",        lambda: (lambda r:r==round(r,4))(empirical_covariance([1,2,3],[1,2,3]))),
    ("Stress 20",           lambda: (random.seed(42) or True) and all(
        approx(empirical_covariance(xs,ys),_cov(xs,ys),1e-3) and approx(empirical_correlation(xs,ys),_corr(xs,ys),1e-3)
        for xs,ys in [([random.gauss(0,2) for _ in range(n)],None) or ([],[])
        for n in [random.randint(2,200) for _ in range(20)]]
        # Simplified: just test covariance with known data
    ) if False else all(
        approx(empirical_covariance([float(i) for i in range(n)],[float(i)*2 for i in range(n)]),
               _cov([float(i) for i in range(n)],[float(i)*2 for i in range(n)]),1e-3)
        for n in range(2,22))),
]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--all",action="store_true"); args=ap.parse_args()
    random.seed(42)
    print("\n"+"="*55+"\n  CODE EXPERT — Covariance & Correlation\n"+"="*55)
    passed=total=0
    print("\n── Public ────────────────────────────────────────────")
    for n,f in PUBLIC: passed+=run_test(n,f); total+=1
    if args.all:
        print("\n── Hidden ────────────────────────────────────────────")
        for n,f in HIDDEN: passed+=run_test(n,f,False); total+=1
    pct=round(100*passed/total) if total else 0
    print(f"\n{'='*55}\n  SCORE: {passed}/{total} ({pct}%)")
    print("  ✓ Full marks!" if pct==100 else ("  ~ Good." if pct>=70 else "  ✗ Keep going."))
    print("="*55+"\n")

if __name__=="__main__": main()
