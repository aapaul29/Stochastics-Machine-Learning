import sys,argparse,traceback,random,scipy.stats
try: from solution import welch_t_statistic,welch_p_value,reject_null
except ImportError as e: print(f"[ERROR] {e}"); sys.exit(1)

def _t(xs,ys): return round(scipy.stats.ttest_ind(xs,ys,equal_var=False).statistic,4)
def _p(xs,ys): return round(scipy.stats.ttest_ind(xs,ys,equal_var=False).pvalue,4)
def approx(a,b,tol=1e-3): return abs(a-b)<=tol
def run_test(name,fn,pub=True):
    tag="PUBLIC" if pub else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except: print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

XS=[2.1,2.5,2.3,2.8]; YS=[1.9,1.7,2.0,1.8]
PUBLIC=[
    ("t > 0",               lambda: welch_t_statistic(XS,YS)>0),
    ("p in (0,1)",          lambda: 0<welch_p_value(XS,YS)<1),
    ("Same means → t=0",    lambda: approx(welch_t_statistic([1,2,3],[1,2,3]),0.0)),
    ("Reject large diff",   lambda: reject_null([10.0]*20,[0.0]*20,0.05)==True),
    ("No reject identical", lambda: reject_null([1,2,3],[1,2,3],0.05)==False),
    ("Agrees with scipy",   lambda: approx(welch_t_statistic(XS,YS),_t(XS,YS)) and approx(welch_p_value(XS,YS),_p(XS,YS))),
]
HIDDEN=[
    ("Exact t",             lambda: approx(welch_t_statistic(XS,YS),_t(XS,YS))),
    ("Unequal sizes",       lambda: reject_null([1,2,3,4,5],[10,11,12],0.05)==(_p([1,2,3,4,5],[10,11,12])<0.05)),
    ("Stress 15",           lambda: (random.seed(7) or True) and all(
        approx(welch_t_statistic(xs,ys),_t(xs,ys)) and approx(welch_p_value(xs,ys),_p(xs,ys)) and
        reject_null(xs,ys,0.05)==(_p(xs,ys)<0.05)
        for xs,ys in [([random.gauss(random.uniform(0,2),1) for _ in range(random.randint(5,100))],
                       [random.gauss(random.uniform(0,2),1) for _ in range(random.randint(5,100))]) for _ in range(15)])),
]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--all",action="store_true"); args=ap.parse_args()
    random.seed(42)
    print("\n"+"="*55+"\n  CODE EXPERT — Two-Sample t-Test\n"+"="*55)
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
