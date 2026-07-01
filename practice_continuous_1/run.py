import sys,argparse,traceback,random,math,scipy.stats
try: from solution import exp_pdf,exp_cdf,exp_quantile
except ImportError as e: print(f"[ERROR] {e}"); sys.exit(1)

def approx(a,b,tol=1e-4): return abs(a-b)<=tol
def run_test(name,fn,pub=True):
    tag="PUBLIC" if pub else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except: print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

PUBLIC=[
    ("PDF Exp(2) x=1",      lambda: approx(exp_pdf(2.0,1.0),round(2*math.exp(-2),4))),
    ("CDF Exp(2) x=1",      lambda: approx(exp_cdf(2.0,1.0),round(1-math.exp(-2),4))),
    ("Quantile median",     lambda: approx(exp_quantile(2.0,0.5),round(math.log(2)/2,4))),
    ("PDF x<0 = 0",         lambda: exp_pdf(1.0,-1.0)==0.0),
    ("CDF x<0 = 0",         lambda: exp_cdf(1.0,-1.0)==0.0),
    ("CDF x=0 = 0",         lambda: approx(exp_cdf(1.0,0.0),0.0)),
]
HIDDEN=[
    ("PDF at x=0 = lam",    lambda: approx(exp_pdf(3.0,0.0),3.0)),
    ("CDF large x ≈ 1",     lambda: approx(exp_cdf(1.0,20),1.0)),
    ("Quantile-CDF inverse",lambda: all(approx(exp_cdf(2.5,exp_quantile(2.5,p)),p,1e-3) for p in [0.1,0.5,0.9])),
    ("Rounding 4dp",        lambda: (lambda r:r==round(r,4))(exp_pdf(1.0,1.0))),
    ("Stress 20",           lambda: (random.seed(42) or True) and all(
        approx(exp_pdf(lam,x),round(scipy.stats.expon.pdf(x,scale=1/lam),4))
        for lam,x in [(random.uniform(0.5,5),random.uniform(0,5)) for _ in range(20)])),
]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--all",action="store_true"); args=ap.parse_args()
    random.seed(42)
    print("\n"+"="*55+"\n  CODE EXPERT — Exponential Distribution\n"+"="*55)
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
