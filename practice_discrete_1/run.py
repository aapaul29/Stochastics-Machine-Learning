import sys,argparse,traceback,random
try: from solution import empirical_pmf,empirical_mean,empirical_variance
except ImportError as e: print(f"[ERROR] {e}"); sys.exit(1)

def _pmf(s,k): return round(s.count(k)/len(s),4)
def _mean(s):  return round(sum(s)/len(s),4)
def _var(s):
    if len(s)==1: return 0.0
    m=sum(s)/len(s); return round(sum((x-m)**2 for x in s)/(len(s)-1),4)
def approx(a,b,tol=1e-4): return abs(a-b)<=tol

def run_test(name,fn,pub=True):
    tag="PUBLIC" if pub else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except: print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

S=[0,1,0,2,1,0]
PUBLIC=[
    ("PMF k=0",         lambda: approx(empirical_pmf(S,0),0.5)),
    ("PMF k=1",         lambda: approx(empirical_pmf(S,1),2/6)),
    ("PMF unseen=0",    lambda: approx(empirical_pmf(S,9),0.0)),
    ("PMF sums to 1",   lambda: approx(sum(empirical_pmf(S,k) for k in {0,1,2}),1.0,1e-3)),
    ("Mean",            lambda: approx(empirical_mean(S),4/6)),
    ("Variance",        lambda: approx(empirical_variance(S),0.6667,1e-3)),
    ("Variance n=1",    lambda: empirical_variance([5])==0.0),
]
HIDDEN=[
    ("All same",        lambda: approx(empirical_variance([3]*10),0.0)),
    ("Two elements",    lambda: approx(empirical_variance([0,1]),0.5)),
    ("Large input",     lambda: (random.seed(42) or True) and approx(
        empirical_mean([random.randint(0,5) for _ in range(100_000)]),
        _mean([random.randint(0,5) for _ in (random.seed(42) or range(100_000))]),1e-2)),
    ("Rounding 4dp",    lambda: (lambda r:r==round(r,4))(empirical_mean([0,1,2]))),
    ("Stress 20",       lambda: all(
        approx(empirical_pmf(s,k),_pmf(s,k)) and approx(empirical_mean(s),_mean(s)) and approx(empirical_variance(s),_var(s))
        for s,k in [([random.randint(0,9) for _ in range(random.randint(2,200))],random.randint(0,9)) for _ in range(20)])),
]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--all",action="store_true"); args=ap.parse_args()
    random.seed(7)
    print("\n"+"="*55+"\n  CODE EXPERT — Empirical PMF, Mean, Variance\n"+"="*55)
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
