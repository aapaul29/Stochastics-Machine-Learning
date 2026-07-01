import sys,argparse,traceback,random,math
try: from solution import simulate_exponential,simulate_uniform
except ImportError as e: print(f"[ERROR] {e}"); sys.exit(1)

def ref_exp(lam,n,seed):
    random.seed(seed); return [round(-math.log(1-random.random())/lam,4) for _ in range(n)]
def ref_unif(a,b,n,seed):
    random.seed(seed); return [round(a+(b-a)*random.random(),4) for _ in range(n)]
def approx(a,b,tol=0.05): return abs(a-b)<=tol
def run_test(name,fn,pub=True):
    tag="PUBLIC" if pub else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except: print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

PUBLIC=[
    ("Exp length",         lambda: len(simulate_exponential(1.0,10,42))==10),
    ("Unif length",        lambda: len(simulate_uniform(0,1,10,42))==10),
    ("Exp all positive",   lambda: all(x>=0 for x in simulate_exponential(2.0,100,0))),
    ("Unif in [0,5]",      lambda: all(0<=x<=5 for x in simulate_uniform(0,5,100,0))),
    ("Exp seed repro",     lambda: simulate_exponential(1.0,5,42)==simulate_exponential(1.0,5,42)),
    ("Exp mean ≈ 0.5",     lambda: approx(sum(simulate_exponential(2.0,10000,99))/10000,0.5)),
    ("Unif mean ≈ 3",      lambda: approx(sum(simulate_uniform(2,4,10000,99))/10000,3.0)),
]
HIDDEN=[
    ("Exp exact match",    lambda: simulate_exponential(1.0,5,42)==ref_exp(1.0,5,42)),
    ("Unif exact match",   lambda: simulate_uniform(0,1,5,42)==ref_unif(0,1,5,42)),
    ("Exp lam=2",          lambda: simulate_exponential(2.0,5,7)==ref_exp(2.0,5,7)),
    ("Unif shifted",       lambda: simulate_uniform(3,7,5,7)==ref_unif(3,7,5,7)),
    ("Exp large n",        lambda: simulate_exponential(0.5,1000,1)==ref_exp(0.5,1000,1)),
    ("Rounding 4dp",       lambda: all(x==round(x,4) for x in simulate_exponential(1.0,5,42))),
]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--all",action="store_true"); args=ap.parse_args()
    print("\n"+"="*55+"\n  CODE EXPERT — Inverse CDF Simulation\n"+"="*55)
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
