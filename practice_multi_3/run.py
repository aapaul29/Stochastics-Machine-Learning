import sys,argparse,traceback,random,math,scipy.stats
try: from solution import mixture_pdf,mixture_mean,mixture_variance
except ImportError as e: print(f"[ERROR] {e}"); sys.exit(1)

def _phi(x,mu,sig): return scipy.stats.norm.pdf(x,mu,sig)
def _pdf(x,w,m,s): return round(sum(wi*_phi(x,mi,si) for wi,mi,si in zip(w,m,s)),4)
def _mean(w,m): return round(sum(wi*mi for wi,mi in zip(w,m)),4)
def _var(w,m,s): return round(sum(wi*(si**2+mi**2) for wi,mi,si in zip(w,m,s))-_mean(w,m)**2,4)
def approx(a,b,tol=1e-4): return abs(a-b)<=tol
def run_test(name,fn,pub=True):
    tag="PUBLIC" if pub else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except: print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

W=[0.5,0.5]; M=[-1.0,1.0]; S=[0.5,0.5]
PUBLIC=[
    ("Mean symmetric=0",   lambda: approx(mixture_mean(W,M),0.0)),
    ("Variance=1.25",      lambda: approx(mixture_variance(W,M,S),1.25)),
    ("PDF positive",       lambda: mixture_pdf(0.0,W,M,S)>0),
    ("Single component",   lambda: approx(mixture_pdf(2.0,[1.0],[2.0],[1.0]),round(scipy.stats.norm.pdf(2.0,2.0,1.0),4))),
    ("Single mean",        lambda: approx(mixture_mean([1.0],[2.0]),2.0)),
    ("Single variance",    lambda: approx(mixture_variance([1.0],[2.0],[1.0]),1.0)),
]
HIDDEN=[
    ("3 components",       lambda: approx(mixture_pdf(2.0,[0.3,0.4,0.3],[0,2,4],[1,1,1]),_pdf(2.0,[0.3,0.4,0.3],[0,2,4],[1,1,1]))),
    ("PDF non-negative",   lambda: all(mixture_pdf(x,[0.5,0.5],[-5,5],[1,1])>=0 for x in range(-10,11))),
    ("Rounding 4dp",       lambda: (lambda r:r==round(r,4))(mixture_mean([0.5,0.5],[-1.0,1.0]))),
    ("Stress 10",          lambda: (random.seed(7) or True) and all(
        approx(mixture_pdf(x,w,m,s2),_pdf(x,w,m,s2)) and approx(mixture_mean(w,m),_mean(w,m))
        for x,w,m,s2 in [(random.uniform(-5,5),
                          (lambda r:[v/sum(r) for v in r])([random.random() for _ in range(3)]),
                          [random.uniform(-3,3) for _ in range(3)],
                          [random.uniform(0.5,2) for _ in range(3)]) for _ in range(10)])),
]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--all",action="store_true"); args=ap.parse_args()
    random.seed(42)
    print("\n"+"="*55+"\n  CODE EXPERT — Gaussian Mixture\n"+"="*55)
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
