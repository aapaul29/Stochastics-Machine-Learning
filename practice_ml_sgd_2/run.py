import sys, argparse, traceback, random, math
from solution import poly_sgd_update

def approx(a, b, tol=1e-4):
    if isinstance(a,(list,tuple)) and isinstance(b,(list,tuple)):
        return len(a)==len(b) and all(abs(x-y)<=tol for x,y in zip(a,b))
    return abs(a-b)<=tol

def run_test(name, fn, public=True):
    tag="PUBLIC" if public else "HIDDEN"
    try:
        ok=fn(); print(f"  {'[PASS]' if ok else '[FAIL]'} [{tag}] {name}"); return bool(ok)
    except Exception:
        print(f"  [ERROR] [{tag}] {name}"); traceback.print_exc(); return False

PUBLIC_TESTS = [
    ("Degree-2 basic example",
     # p(2)=0, err=-3, grads=[-6,-12,-24], w_new=[0.06,0.12,0.24]
     lambda: approx(poly_sgd_update([0.0,0.0,0.0],2.0,3.0,0.01),[0.06,0.12,0.24])),
    ("Degree-1 (linear)",
     # p(1)=0, err=-2, grad=[−4,−4], w_new=[0.4,0.4]
     lambda: approx(poly_sgd_update([0.0,0.0],1.0,2.0,0.1),[0.4,0.4])),
    ("No error → no update",
     # p(1)=1+1=2, err=0
     lambda: approx(poly_sgd_update([1.0,1.0],1.0,2.0,0.1),[1.0,1.0])),
    ("Degree-0 (constant)",
     # p(5)=0, err=-3, grad_w0=2*(-3)*1=-6, w_new=0-0.1*(-6)=0.6
     lambda: approx(poly_sgd_update([0.0],5.0,3.0,0.1),[0.6])),
    ("Returns new list",
     lambda: (lambda w: (poly_sgd_update(w,1.0,2.0,0.1), w[0]==0.0)[1])([0.0,0.0])),
]

HIDDEN_TESTS = [
    ("Degree-3 all zeros → [1,1,1,1]",
     # p(1)=0, err=-1, grad_i=2*(-1)*1^i=-2 each, w_new=0-0.5*(-2)=1 each
     lambda: approx(poly_sgd_update([0.0,0.0,0.0,0.0],1.0,1.0,0.5),[1.0,1.0,1.0,1.0])),
    ("Negative x",
     # p(-1)=0, err=-1, grad=[2*(-1)*1, 2*(-1)*(-1), 2*(-1)*1]=[-2,2,-2]
     # w_new=[0-0.1*(-2), 0-0.1*2, 0-0.1*(-2)]=[0.2,-0.2,0.2]
     lambda: approx(poly_sgd_update([0.0,0.0,0.0],-1.0,1.0,0.1),[0.2,-0.2,0.2])),
    ("Large alpha",
     # p(2)=0+0=0, err=0-4=-4, grad=[2*(-4)*1,2*(-4)*2]=[-8,-16]
     # w_new=[0-0.25*(-8), 0-0.25*(-16)]=[2.0,4.0]
     lambda: approx(poly_sgd_update([0.0,0.0],2.0,4.0,0.25),[2.0,4.0])),
    ("Stress: random",
     lambda: (random.seed(7), all(
         (lambda args: (lambda w,x,y,a:
             approx(poly_sgd_update(w,x,y,a),
                    [round(w[i]-a*2*(sum(w[j]*x**j for j in range(len(w)))-y)*x**i,6)
                     for i in range(len(w))]))(args[0],args[1],args[2],args[3]))(
             [[random.uniform(-1,1) for _ in range(3)],
              random.uniform(-2,2), random.uniform(-3,3), random.uniform(0.001,0.05)])
         for _ in range(20)))[1]),
]

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--all",action="store_true")
    args=parser.parse_args()
    print("\n"+"="*55+"\n  CODE EXPERT — Polynomial SGD Update\n"+"="*55)
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
