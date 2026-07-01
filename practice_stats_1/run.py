import sys,argparse,traceback,random,statistics
try: from solution import sample_mean,sample_variance,sample_median,sample_iqr
except ImportError as e: print(f"[ERROR] {e}"); sys.exit(1)

def approx(a,b,tol=1e-4): return abs(a-b)<=tol
def run_test(name,fn,pub=True):
    tag="PUBLIC" if pub else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except: print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

D=[2,4,4,4,5,5,7,9]
PUBLIC=[
    ("Mean=5",              lambda: approx(sample_mean(D),5.0)),
    ("Variance",            lambda: approx(sample_variance(D),32/7,1e-3)),
    ("Median even",         lambda: approx(sample_median([1,2,3,4]),2.5)),
    ("Median odd",          lambda: approx(sample_median([1,2,3]),2.0)),
    ("Variance n=1 → 0",    lambda: sample_variance([5])==0.0),
    ("IQR",                 lambda: approx(sample_iqr(D),2.5,0.1)),
    ("Mean constant",       lambda: approx(sample_mean([3,3,3]),3.0)),
]
HIDDEN=[
    ("Large sample mean",   lambda: (random.seed(42) or True) and abs(sample_mean([random.gauss(10,2) for _ in range(10000)])-10)<0.1),
    ("Sorted median",       lambda: approx(sample_median([1,2,3,4,5]),3.0)),
    ("Rounding 4dp",        lambda: (lambda r:r==round(r,4))(sample_mean([1,2,3]))),
    ("Stress 10 mean",      lambda: (random.seed(7) or True) and all(
        approx(sample_mean(d),statistics.mean(d),1e-3)
        for d in [[random.gauss(0,3) for _ in range(random.randint(2,500))] for _ in range(10)])),
    ("Stress 10 median",    lambda: (random.seed(7) or True) and all(
        approx(sample_median(d),statistics.median(d),1e-3)
        for d in [[random.gauss(0,3) for _ in range(random.randint(2,500))] for _ in range(10)])),
]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--all",action="store_true"); args=ap.parse_args()
    random.seed(42)
    print("\n"+"="*55+"\n  CODE EXPERT — Summary Statistics\n"+"="*55)
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
