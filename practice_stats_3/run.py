import sys,argparse,traceback,random,math
try: from solution import mle_exponential,mle_normal
except ImportError as e: print(f"[ERROR] {e}"); sys.exit(1)

def _exp(s): return round(1/(sum(s)/len(s)),4)
def _norm(s):
    mu=sum(s)/len(s); sig=math.sqrt(sum((x-mu)**2 for x in s)/len(s))
    return round(mu,4),round(sig,4)
def approx(a,b,tol=1e-4): return abs(a-b)<=tol
def run_test(name,fn,pub=True):
    tag="PUBLIC" if pub else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except: print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

PUBLIC=[
    ("Exp basic = 0.5",     lambda: approx(mle_exponential([1,2,3]),0.5)),
    ("Exp constant",        lambda: approx(mle_exponential([2,2,2]),0.5)),
    ("Normal mu",           lambda: approx(mle_normal([1,2,3])[0],2.0)),
    ("Normal sigma biased", lambda: approx(mle_normal([1,2,3])[1],math.sqrt(2/3))),
    ("Normal constant",     lambda: (lambda r: approx(r[0],5.0) and approx(r[1],0.0))(mle_normal([5,5,5]))),
    ("Biased sigma n=2",    lambda: approx(mle_normal([0,2])[1],1.0)),
]
HIDDEN=[
    ("Large Exp ≈ 2",       lambda: (random.seed(42) or True) and abs(mle_exponential([random.expovariate(2) for _ in range(10000)])-2)<0.1),
    ("Large Normal",        lambda: (random.seed(42) or True) and abs(mle_normal([random.gauss(3,1.5) for _ in range(10000)])[0]-3)<0.05),
    ("Rounding 4dp",        lambda: (lambda r:r==round(r,4))(mle_exponential([1,2,3]))),
    ("Stress 20",           lambda: (random.seed(7) or True) and all(
        approx(mle_exponential(s),_exp(s)) and (lambda ab,ef: approx(ab[0],ef[0]) and approx(ab[1],ef[1]))(mle_normal(s),_norm(s))
        for s in [[random.expovariate(random.uniform(0.5,3)) for _ in range(random.randint(2,200))] for _ in range(20)])),
]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--all",action="store_true"); args=ap.parse_args()
    random.seed(42)
    print("\n"+"="*55+"\n  CODE EXPERT — MLE\n"+"="*55)
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
