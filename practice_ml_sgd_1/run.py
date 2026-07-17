import sys, argparse, traceback, random, math
from solution import sgd_update

def approx(a, b, tol=1e-4):
    if isinstance(a, (list,tuple)) and isinstance(b,(list,tuple)):
        return len(a)==len(b) and all(abs(x-y)<=tol for x,y in zip(a,b))
    return abs(a-b)<=tol

def run_test(name, fn, public=True):
    tag="PUBLIC" if public else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except Exception:
        print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

PUBLIC_TESTS = [
    ("Basic 2D example",
     lambda: (lambda r: approx(r[0],[1.12,0.18]) and approx(r[1],0.06))(
         sgd_update([1.0,0.0],0.0,[2.0,3.0],5.0,0.01))),
    ("No error → no update",
     lambda: (lambda r: approx(r[0],[1.0,2.0]) and approx(r[1],0.5))(
         sgd_update([1.0,2.0],0.5,[1.0,0.0],1.5,0.1))),
    ("Returns new list, does not mutate w",
     lambda: (lambda w: (sgd_update(w,0.0,[1.0],2.0,0.1), w[0]==0.0)[1])([0.0])),
    ("Scalar (1D) update",
     # pred=0, err=-3, w_new=0+0.04*2*3*1=0.24, b_new=0+0.04*2*3=0.24
     lambda: (lambda r: approx(r[0],[0.24]) and approx(r[1],0.24))(
         sgd_update([0.0],0.0,[1.0],3.0,0.04))),
    ("Rounding to 6 dp",
     lambda: all(len(str(v).split('.')[-1])<=6
                 for v in sgd_update([0.1],0.1,[0.3],1.0,0.001)[0])),
]

HIDDEN_TESTS = [
    ("Large learning rate",
     # pred=0, err=-3, w_new=0+0.5*2*3=3.0, b_new=3.0
     lambda: (lambda r: approx(r[0],[3.0],1e-4) and approx(r[1],3.0,1e-4))(
         sgd_update([0.0],0.0,[1.0],3.0,0.5))),
    ("3D weights",
     # pred=3, err=-3, each w_i: 1 + 0.01*2*3*1 = 1.06
     lambda: (lambda r: approx(r[0],[1.06,1.06,1.06],1e-4))(
         sgd_update([1.0,1.0,1.0],0.0,[1.0,1.0,1.0],6.0,0.01))),
    ("Negative target",
     # pred=0, err=0-(-1)=1, b_new=0-0.01*2*1=-0.02
     lambda: (lambda r: approx(r[1],-0.02,1e-4))(
         sgd_update([0.0],0.0,[1.0],-1.0,0.01))),
    ("Alpha=0 → no change",
     lambda: (lambda r: approx(r[0],[2.0]) and approx(r[1],3.0))(
         sgd_update([2.0],3.0,[5.0],1.0,0.0))),
    ("Stress: random samples",
     lambda: (random.seed(7), all(
         (lambda args: (lambda w,b,x,y,a:
             (lambda r: approx(r[0][0], round(w-a*2*(w*x+b-y)*x,6)) and
                        approx(r[1],    round(b-a*2*(w*x+b-y),6)))(
                 sgd_update([w],b,[x],y,a)))(*args))(
             [random.uniform(-2,2), random.uniform(-1,1),
              random.uniform(-3,3), random.uniform(-3,3),
              random.uniform(0.001,0.05)])
         for _ in range(20)))[1]),
]

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--all",action="store_true")
    args=parser.parse_args()
    print("\n"+"="*55+"\n  CODE EXPERT — Linear SGD Update\n"+"="*55)
    passed=0; total=0
    print("\n── Public Tests ──────────────────────────────────────")
    for name,fn in PUBLIC_TESTS:
        ok=run_test(name,fn); passed+=ok; total+=1
    if args.all:
        print("\n── Hidden Tests ──────────────────────────────────────")
        random.seed(42)
        for name,fn in HIDDEN_TESTS:
            ok=run_test(name,fn,public=False); passed+=ok; total+=1
    print("\n"+"="*55)
    pct=round(100*passed/total) if total else 0
    print(f"  SCORE: {passed}/{total}  ({pct}%)")
    if pct==100: print("  ✓ Full marks!")
    elif pct>=70: print("  ~ Good — check the failing cases above.")
    else: print("  ✗ Keep going — re-read the problem statement.")
    print("="*55+"\n")

if __name__=="__main__": main()
