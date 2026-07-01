import sys,argparse,traceback,random
try: from solution import running_average,lln_converges,convergence_index
except ImportError as e: print(f"[ERROR] {e}"); sys.exit(1)

def _ra(s):
    out=[]; total=0
    for i,x in enumerate(s,1): total+=x; out.append(round(total/i,4))
    return out
def approx_list(a,b,tol=1e-4): return len(a)==len(b) and all(abs(x-y)<=tol for x,y in zip(a,b))
def run_test(name,fn,pub=True):
    tag="PUBLIC" if pub else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except: print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

PUBLIC=[
    ("RA length",           lambda: len(running_average([1,2,3,4]))==4),
    ("RA values [2,4,6]",   lambda: approx_list(running_average([2,4,6]),[2.0,3.0,4.0])),
    ("RA single element",   lambda: approx_list(running_average([5]),[5.0])),
    ("Converges true",      lambda: lln_converges([1.0]*100+[1.05]*100,1.025,0.1)==True),
    ("Converges false",     lambda: lln_converges([100.0]*10,0.0,0.1)==False),
    ("RA rounding",         lambda: all(x==round(x,4) for x in running_average([1,2]))),
    ("Conv index constant", lambda: convergence_index([1.0]*1000,1.0,0.01)==1),
]
HIDDEN=[
    ("Exact RA",            lambda: approx_list(running_average([1.0,3.0,2.0,4.0]),_ra([1.0,3.0,2.0,4.0]))),
    ("Large normal sample", lambda: (random.seed(42) or True) and lln_converges([random.gauss(5,1) for _ in range(10000)],5.0,0.05)),
    ("Rounding 4dp",        lambda: all(x==round(x,4) for x in running_average([1,2,3]))),
    ("Stress 5",            lambda: (random.seed(7) or True) and all(
        approx_list(running_average(s),_ra(s),1e-3)
        for s in [[random.gauss(0,1) for _ in range(1000)] for _ in range(5)])),
]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--all",action="store_true"); args=ap.parse_args()
    random.seed(42)
    print("\n"+"="*55+"\n  CODE EXPERT — Law of Large Numbers\n"+"="*55)
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
