import sys,argparse,traceback,random
try: from solution import empirical_cdf,empirical_quantile
except ImportError as e: print(f"[ERROR] {e}"); sys.exit(1)

def _cdf(s,x): return round(sum(1 for xi in s if xi<=x)/len(s),4)
def _q(s,p):
    for x in sorted(s):
        if _cdf(s,x)>=p: return x
    return sorted(s)[-1]
def approx(a,b,tol=1e-4): return abs(a-b)<=tol
def run_test(name,fn,pub=True):
    tag="PUBLIC" if pub else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except: print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

S=[1,3,2,5,4]
PUBLIC=[
    ("CDF at 3 = 0.6",   lambda: approx(empirical_cdf(S,3),0.6)),
    ("CDF at 2.5 = 0.4", lambda: approx(empirical_cdf(S,2.5),0.4)),
    ("CDF below min = 0",lambda: approx(empirical_cdf(S,0),0.0)),
    ("CDF above max = 1",lambda: approx(empirical_cdf(S,10),1.0)),
    ("Quantile 0.5 = 3", lambda: empirical_quantile(S,0.5)==3),
    ("Quantile 0.0 = 1", lambda: empirical_quantile(S,0.0)==1),
    ("Quantile 1.0 = 5", lambda: empirical_quantile(S,1.0)==5),
    ("CDF monotone",     lambda: all(empirical_cdf(S,x)<=empirical_cdf(S,x+1) for x in range(5))),
]
HIDDEN=[
    ("Duplicates",       lambda: approx(empirical_cdf([1,1,2,2,3],1),0.4)),
    ("Single element",   lambda: approx(empirical_cdf([5.0],5),1.0)),
    ("Stress 15",        lambda: (random.seed(7) or True) and all(
        approx(empirical_cdf(s,x),_cdf(s,x)) and empirical_quantile(s,p)==_q(s,p)
        for s,x,p in [([random.randint(0,20) for _ in range(random.randint(5,200))],
                       random.uniform(0,20),random.uniform(0,1)) for _ in range(15)])),
]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--all",action="store_true"); args=ap.parse_args()
    random.seed(42)
    print("\n"+"="*55+"\n  CODE EXPERT — Empirical CDF & Quantiles\n"+"="*55)
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
