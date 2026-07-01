import sys,argparse,traceback,random,scipy.stats
try: from solution import standardize,normal_prob,normal_quantile
except ImportError as e: print(f"[ERROR] {e}"); sys.exit(1)

def approx(a,b,tol=1e-4): return abs(a-b)<=tol
def run_test(name,fn,pub=True):
    tag="PUBLIC" if pub else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except: print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

PUBLIC=[
    ("Standardize basic",  lambda: approx(standardize(1.5,1.0,0.5),1.0)),
    ("Standardize zero",   lambda: approx(standardize(2.0,2.0,1.0),0.0)),
    ("P(-1<Z<1) ≈ 68%",    lambda: approx(normal_prob(0,1,-1,1),0.6827,1e-3)),
    ("P(-1.96<Z<1.96)≈95%",lambda: approx(normal_prob(0,1,-1.96,1.96),0.95,1e-2)),
    ("P(-10<Z<10) ≈ 1",    lambda: approx(normal_prob(0,1,-10,10),1.0)),
    ("Quantile 97.5%≈1.96",lambda: approx(normal_quantile(0,1,0.975),1.96,1e-2)),
    ("Quantile median=mu", lambda: approx(normal_quantile(5,2,0.5),5.0)),
]
HIDDEN=[
    ("Shifted normal",     lambda: approx(normal_prob(3,2,1,5),round(scipy.stats.norm.cdf(5,3,2)-scipy.stats.norm.cdf(1,3,2),4))),
    ("Quantile-CDF inv",   lambda: all(approx(scipy.stats.norm.cdf(normal_quantile(2,3,p),2,3),p,1e-3) for p in [0.1,0.5,0.9])),
    ("Point interval=0",   lambda: approx(normal_prob(0,1,0,0),0.0)),
    ("Symmetry",           lambda: approx(normal_prob(0,1,-1,0),normal_prob(0,1,0,1))),
    ("Rounding 4dp",       lambda: (lambda r:r==round(r,4))(normal_prob(0,1,-1,1))),
    ("Stress 20",          lambda: (random.seed(7) or True) and all(
        approx(normal_prob(mu,sig,a,b),round(scipy.stats.norm.cdf(b,mu,sig)-scipy.stats.norm.cdf(a,mu,sig),4))
        for mu,sig,a,b in [(random.uniform(-5,5),random.uniform(0.5,5),random.uniform(-10,0),random.uniform(0,10)) for _ in range(20)])),
]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--all",action="store_true"); args=ap.parse_args()
    random.seed(42)
    print("\n"+"="*55+"\n  CODE EXPERT — Normal Distribution\n"+"="*55)
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
