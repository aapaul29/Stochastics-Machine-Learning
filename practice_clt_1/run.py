import sys,argparse,traceback,random,math,scipy.stats
try: from solution import clt_mean,clt_variance,clt_prob
except ImportError as e: print(f"[ERROR] {e}"); sys.exit(1)

def _prob(d,n,a,b):
    mu=d.mean(); sig=math.sqrt(d.var()*n)
    return round(scipy.stats.norm.cdf(b,n*mu,sig)-scipy.stats.norm.cdf(a,n*mu,sig),4)
def approx(a,b,tol=1e-4): return abs(a-b)<=tol
def run_test(name,fn,pub=True):
    tag="PUBLIC" if pub else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except: print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

p3=scipy.stats.poisson(mu=3); n01=scipy.stats.norm(0,1); u=scipy.stats.uniform(0,1)
PUBLIC=[
    ("Mean Poisson(3)*10=30",  lambda: approx(clt_mean(p3,10),30.0)),
    ("Var Poisson(3)*10=30",   lambda: approx(clt_variance(p3,10),30.0)),
    ("Mean N(0,1)*5=0",        lambda: approx(clt_mean(n01,5),0.0)),
    ("Var U(0,1)*12=1",        lambda: approx(clt_variance(u,12),1.0,1e-3)),
    ("P(wide)≈1",              lambda: approx(clt_prob(n01,100,-1000,1000),1.0)),
    ("P(Poisson) in (0,1)",    lambda: 0<clt_prob(p3,100,270,330)<1),
]
HIDDEN=[
    ("Exp mean",               lambda: approx(clt_mean(scipy.stats.expon(scale=2),10),20.0)),
    ("Exp prob",               lambda: (lambda d,n: approx(clt_prob(d,n,40,60),_prob(d,n,40,60)))(scipy.stats.expon(scale=1),50)),
    ("Binomial approx",        lambda: approx(clt_prob(scipy.stats.binom(n=10,p=0.3),50,100,160),
                                              _prob(scipy.stats.binom(n=10,p=0.3),50,100,160),1e-3)),
    ("Point interval=0",       lambda: approx(clt_prob(n01,10,0,0),0.0)),
    ("Rounding 4dp",           lambda: (lambda r:r==round(r,4))(clt_mean(p3,10))),
]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--all",action="store_true"); args=ap.parse_args()
    random.seed(42)
    print("\n"+"="*55+"\n  CODE EXPERT — CLT Approximation\n"+"="*55)
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
