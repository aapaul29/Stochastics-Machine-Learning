import sys,argparse,traceback,random
try: from solution import empirical_joint,empirical_marginal_x,empirical_marginal_y,are_independent
except ImportError as e: print(f"[ERROR] {e}"); sys.exit(1)

def _j(s,x,y): return round(sum(1 for a,b in s if a==x and b==y)/len(s),4)
def _mx(s,x):  return round(sum(1 for a,_ in s if a==x)/len(s),4)
def _my(s,y):  return round(sum(1 for _,b in s if b==y)/len(s),4)
def approx(a,b,tol=1e-4): return abs(a-b)<=tol
def run_test(name,fn,pub=True):
    tag="PUBLIC" if pub else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except: print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

S=[(0,0),(0,1),(1,0),(1,1)]
PUBLIC=[
    ("Joint (0,0)=0.25",    lambda: approx(empirical_joint(S,0,0),0.25)),
    ("Marginal X=0 = 0.5",  lambda: approx(empirical_marginal_x(S,0),0.5)),
    ("Marginal Y=1 = 0.5",  lambda: approx(empirical_marginal_y(S,1),0.5)),
    ("Independent sample",  lambda: are_independent(S,[0,1],[0,1],0.01)==True),
    ("Dependent sample",    lambda: are_independent([(0,0),(0,0),(1,1),(1,1)],[0,1],[0,1],0.01)==False),
    ("Joint unseen = 0",    lambda: approx(empirical_joint(S,0,9),0.0)),
    ("Marginal X sums to 1",lambda: approx(sum(empirical_marginal_x(S,x) for x in [0,1]),1.0,1e-3)),
]
HIDDEN=[
    ("Three classes",       lambda: approx(empirical_joint([(i%3,i%2) for i in range(30)],0,0),
                                           _j([(i%3,i%2) for i in range(30)],0,0))),
    ("Fully dependent",     lambda: are_independent([(k,k) for k in range(4)]*100,[0,1,2,3],[0,1,2,3],0.01)==False),
    ("Stress 10 cases",     lambda: (random.seed(7) or True) and all(
        approx(empirical_joint(s,x,y),_j(s,x,y))
        for s,x,y in [([( random.randint(0,2),random.randint(0,2)) for _ in range(200)],
                       random.randint(0,2),random.randint(0,2)) for _ in range(10)])),
]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--all",action="store_true"); args=ap.parse_args()
    random.seed(42)
    print("\n"+"="*55+"\n  CODE EXPERT — Joint PMF & Independence\n"+"="*55)
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
