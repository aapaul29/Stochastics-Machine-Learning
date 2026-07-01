import sys,argparse,traceback,random,math,scipy.stats
try: from solution import confidence_interval
except ImportError as e: print(f"[ERROR] {e}"); sys.exit(1)

def _ci(s,sig,alpha):
    n=len(s); xbar=sum(s)/n; z=scipy.stats.norm.ppf(1-alpha/2); m=z*sig/math.sqrt(n)
    return round(xbar-m,4),round(xbar+m,4)
def approx(a,b,tol=1e-4): return abs(a-b)<=tol
def run_test(name,fn,pub=True):
    tag="PUBLIC" if pub else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except: print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

S=[2.1,1.9,2.0,2.2,1.8]
PUBLIC=[
    ("Basic CI bounds",     lambda: (lambda lo,hi: approx(lo,2.0-1.96*0.5/math.sqrt(5),1e-2) and approx(hi,2.0+1.96*0.5/math.sqrt(5),1e-2))(*confidence_interval(S,0.5,0.05))),
    ("Symmetric at 0",      lambda: (lambda lo,hi: approx(lo,-hi))(*confidence_interval([0]*10,1.0,0.05))),
    ("99% wider than 95%",  lambda: (lambda a,b: (b[1]-b[0])>(a[1]-a[0]))(confidence_interval(S,1.0,0.05),confidence_interval(S,1.0,0.01))),
    ("Mean in CI",          lambda: (lambda lo,hi: lo<2.0<hi)(*confidence_interval(S,0.5,0.05))),
    ("Rounding 4dp",        lambda: (lambda lo,hi: lo==round(lo,4) and hi==round(hi,4))(*confidence_interval(S,0.5,0.05))),
]
HIDDEN=[
    ("Exact match",         lambda: (lambda r,e: approx(r[0],e[0]) and approx(r[1],e[1]))(
        confidence_interval([1,2,3,4,5],2.0,0.05),_ci([1,2,3,4,5],2.0,0.05))),
    ("lo < hi",             lambda: (lambda lo,hi:lo<hi)(*confidence_interval([1,2,3],0.5,0.05))),
    ("Stress 15",           lambda: (random.seed(7) or True) and all(
        approx(confidence_interval(s,sig,alpha)[0],_ci(s,sig,alpha)[0]) and
        approx(confidence_interval(s,sig,alpha)[1],_ci(s,sig,alpha)[1])
        for s,sig,alpha in [([random.gauss(0,1) for _ in range(random.randint(2,200))],
                              random.uniform(0.5,3),random.choice([0.01,0.05,0.1])) for _ in range(15)])),
]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--all",action="store_true"); args=ap.parse_args()
    random.seed(42)
    print("\n"+"="*55+"\n  CODE EXPERT — Confidence Interval\n"+"="*55)
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
