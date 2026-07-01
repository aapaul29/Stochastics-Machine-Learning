import sys,argparse,traceback,random,math,scipy.stats
try: from solution import t_statistic,p_value,reject_null
except ImportError as e: print(f"[ERROR] {e}"); sys.exit(1)

def _t(s,mu0):
    n=len(s); xbar=sum(s)/n; std=math.sqrt(sum((x-xbar)**2 for x in s)/(n-1))
    return round((xbar-mu0)/(std/math.sqrt(n)),4)
def _p(s,mu0): return round(2*scipy.stats.t.sf(abs(_t(s,mu0)),df=len(s)-1),4)
def approx(a,b,tol=1e-4): return abs(a-b)<=tol
def run_test(name,fn,pub=True):
    tag="PUBLIC" if pub else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except: print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

S=[2.5,3.1,2.8,3.2,2.9]
PUBLIC=[
    ("t < 0 when mean < mu0",   lambda: t_statistic(S,3.0)<0),
    ("p-value in (0,1)",        lambda: 0<p_value(S,3.0)<1),
    ("No reject H0",            lambda: reject_null(S,3.0,0.05)==False),
    ("Reject obvious diff",     lambda: reject_null([10.0]*20,0.0,0.05)==True),
    ("t=0 when mean=mu0",       lambda: approx(t_statistic([1,2,3],2.0),0.0)),
    ("p=1 when t=0",            lambda: approx(p_value([1,2,3],2.0),1.0)),
    ("Rounding 4dp",            lambda: (lambda r:r==round(r,4))(t_statistic(S,3.0))),
]
HIDDEN=[
    ("Exact t",                 lambda: approx(t_statistic([2.5,3.1,2.8,3.2,2.9],3.0),_t([2.5,3.1,2.8,3.2,2.9],3.0))),
    ("Large effect reject",     lambda: reject_null([100.0]*30,0.0,0.01)==True),
    ("Stress 15",               lambda: (random.seed(7) or True) and all(
        approx(t_statistic(s,mu0),_t(s,mu0)) and approx(p_value(s,mu0),_p(s,mu0)) and reject_null(s,mu0,0.05)==(_p(s,mu0)<0.05)
        for s,mu0 in [([random.gauss(random.uniform(-5,5),1) for _ in range(random.randint(5,200))],random.uniform(-5,5)) for _ in range(15)])),
]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--all",action="store_true"); args=ap.parse_args()
    random.seed(42)
    print("\n"+"="*55+"\n  CODE EXPERT — One-Sample t-Test\n"+"="*55)
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
