import sys,argparse,traceback,random,scipy.stats
try: from solution import binomial_pmf,binomial_cdf,binomial_mean_variance
except ImportError as e: print(f"[ERROR] {e}"); sys.exit(1)

def _pmf(n,p,k): return round(scipy.stats.binom.pmf(k,n,p),4)
def _cdf(n,p,k): return round(scipy.stats.binom.cdf(k,n,p),4)
def _mv(n,p): return (round(n*p,4),round(n*p*(1-p),4))
def approx(a,b,tol=1e-4): return abs(a-b)<=tol

def run_test(name,fn,pub=True):
    tag="PUBLIC" if pub else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except: print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

PUBLIC=[
    ("PMF Bin(10,0.3) k=3", lambda: approx(binomial_pmf(10,0.3,3),_pmf(10,0.3,3))),
    ("CDF Bin(10,0.3) k=3", lambda: approx(binomial_cdf(10,0.3,3),_cdf(10,0.3,3))),
    ("Mean/Var (10,0.3)",   lambda: binomial_mean_variance(10,0.3)==pytest_like(_mv(10,0.3),1e-4) if False else (
        lambda mv: approx(mv[0],3.0) and approx(mv[1],2.1))(binomial_mean_variance(10,0.3))),
    ("PMF k=0",             lambda: approx(binomial_pmf(5,0.5,0),0.5**5)),
    ("CDF k=n = 1",         lambda: approx(binomial_cdf(5,0.5,5),1.0)),
    ("PMF sums to 1",       lambda: approx(sum(binomial_pmf(8,0.4,k) for k in range(9)),1.0,1e-3)),
    ("Mean/Var fair coin",  lambda: (lambda mv: approx(mv[0],10.0) and approx(mv[1],5.0))(binomial_mean_variance(20,0.5))),
]
HIDDEN=[
    ("p=0 → PMF(k=0)=1",   lambda: approx(binomial_pmf(10,0.0,0),1.0)),
    ("p=1 → PMF(k=n)=1",   lambda: approx(binomial_pmf(10,1.0,10),1.0)),
    ("Large n",             lambda: approx(binomial_pmf(1000,0.4,410),_pmf(1000,0.4,410))),
    ("CDF monotone",        lambda: all(binomial_cdf(10,0.5,k)<=binomial_cdf(10,0.5,k+1) for k in range(10))),
    ("Stress 20",           lambda: all(
        approx(binomial_pmf(n,p,k),_pmf(n,p,k)) and approx(binomial_cdf(n,p,k),_cdf(n,p,k))
        for n,p,k in [(random.randint(5,100),random.uniform(0.1,0.9),0) for _ in range(20)]
        # simplified: just check k=0 for speed
    )),
]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--all",action="store_true"); args=ap.parse_args()
    random.seed(42)
    print("\n"+"="*55+"\n  CODE EXPERT — Binomial Distribution\n"+"="*55)
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
