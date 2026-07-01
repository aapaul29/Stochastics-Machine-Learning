import sys,argparse,traceback,random,scipy.stats
try: from solution import poisson_pmf,poisson_cdf,poisson_approx_binomial
except ImportError as e: print(f"[ERROR] {e}"); sys.exit(1)

def approx(a,b,tol=1e-4): return abs(a-b)<=tol
def run_test(name,fn,pub=True):
    tag="PUBLIC" if pub else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except: print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

PUBLIC=[
    ("PMF Poisson(3) k=2",     lambda: approx(poisson_pmf(3.0,2),round(scipy.stats.poisson.pmf(2,3.0),4))),
    ("CDF Poisson(3) k=2",     lambda: approx(poisson_cdf(3.0,2),round(scipy.stats.poisson.cdf(2,3.0),4))),
    ("PMF k=0",                lambda: approx(poisson_pmf(2.0,0),round(scipy.stats.poisson.pmf(0,2.0),4))),
    ("Approx Bin(1000,0.003)",  lambda: approx(poisson_approx_binomial(1000,0.003,2),round(scipy.stats.poisson.pmf(2,3.0),4))),
    ("PMF sums to 1",          lambda: approx(sum(poisson_pmf(2.0,k) for k in range(20)),1.0,1e-3)),
    ("CDF large k = 1",        lambda: approx(poisson_cdf(1.0,50),1.0)),
]
HIDDEN=[
    ("Small lambda",           lambda: approx(poisson_pmf(0.1,0),round(scipy.stats.poisson.pmf(0,0.1),4))),
    ("Large lambda",           lambda: approx(poisson_pmf(50,50),round(scipy.stats.poisson.pmf(50,50),4))),
    ("CDF monotone",           lambda: all(poisson_cdf(5,k)<=poisson_cdf(5,k+1) for k in range(14))),
    ("Approx accuracy <5%",    lambda: all(
        abs(poisson_approx_binomial(500,0.01,k)-scipy.stats.binom.pmf(k,500,0.01))/max(scipy.stats.binom.pmf(k,500,0.01),1e-6)<0.05
        for k in range(10))),
    ("Stress 20",              lambda: (random.seed(7) or True) and all(
        approx(poisson_pmf(lam,k),round(scipy.stats.poisson.pmf(k,lam),4))
        for lam,k in [(random.uniform(0.5,20),random.randint(0,30)) for _ in range(20)])),
]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--all",action="store_true"); args=ap.parse_args()
    random.seed(42)
    print("\n"+"="*55+"\n  CODE EXPERT — Poisson Distribution\n"+"="*55)
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
