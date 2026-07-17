import sys, argparse, traceback, random, math
from solution import minibatch_sgd_step

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
    ("Perfect prediction → no update",
     lambda: (lambda r: approx(r[0],[1.0]) and approx(r[1],0.0))(
         minibatch_sgd_step([1.0],0.0,[[1.0],[2.0],[3.0]],[1.0,2.0,3.0],0.01))),
    ("Single sample = SGD",
     # m=1, pred=1*2+0=2, err=-3, avg_grad_b=2*(-3)/1=-6, b_new=0-0.01*(-6)=0.06
     lambda: (lambda r: approx(r[0],[1.12]) and approx(r[1],0.06))(
         minibatch_sgd_step([1.0],0.0,[[2.0]],[5.0],0.01))),
    ("Batch of 2, same error → same as single",
     # both samples: x=1, y=1, pred=0, err=-1
     # avg_grad_b = (2*(-1)+2*(-1))/2 = -2, b_new=0-0.1*(-2)=0.2
     lambda: (lambda r: approx(r[0],[0.2]) and approx(r[1],0.2))(
         minibatch_sgd_step([0.0],0.0,[[1.0],[1.0]],[1.0,1.0],0.1))),
    ("Returns new list",
     lambda: (lambda w: (minibatch_sgd_step(w,0.0,[[1.0]],[2.0],0.1), w[0]==0.0)[1])([0.0])),
    ("2D weights output length",
     lambda: (lambda r: len(r[0])==2)(
         minibatch_sgd_step([0.0,0.0],0.0,[[1.0,2.0]],[3.0],0.01))),
]

HIDDEN_TESTS = [
    ("Averaging halves gradient vs single",
     # w=[0], b=0, X=[[1],[1]], y=[1,3]: errors=-1,-3, avg=(-2+-6)/2=-4/2=-2? 
     # Wait: err1=0-1=-1, err2=0-3=-3. avg_grad_b=(2*(-1)+2*(-3))/2=-4. b_new=0-0.1*(-4)=0.4
     # Single with x=1,y=1: err=-1, grad_b=2*(-1)=-2. b_new=0-0.1*(-2)=0.2
     # These are different, confirming averaging matters
     lambda: (lambda r1,r2: not approx(r1[1],r2[1]))(
         minibatch_sgd_step([0.0],0.0,[[1.0],[1.0]],[1.0,3.0],0.1),
         minibatch_sgd_step([0.0],0.0,[[1.0]],[1.0],0.1))),
    ("Batch of 3, 2D",
     # all err=-1, avg_grad_w=[2*(-1)*1/3*3, same]... wait
     # Actually: 3 samples of x=[1,1],y=1, pred=0, err=-1
     # grad_w = sum(2*(-1)*[1,1])/3 = -2*3/3 = -2 each
     # grad_b = sum(2*(-1))/3 = -2
     # w_new=[0-0.1*(-2),...], b_new=0-0.1*(-2)=0.2
     lambda: (lambda r: approx(r[0],[0.2,0.2]) and approx(r[1],0.2))(
         minibatch_sgd_step([0.0,0.0],0.0,[[1.0,1.0],[1.0,1.0],[1.0,1.0]],
                             [1.0,1.0,1.0],0.1))),
    ("Stress: random",
     lambda: (random.seed(9), all(
         (lambda params: (lambda w,b,X,y,a:
             (lambda r: approx(r[1], round(b-a*(2.0/len(X))*
                 sum(sum(w[j]*X[i][j] for j in range(1))+b-y[i] for i in range(len(X))),4)))(
                 minibatch_sgd_step(list(w),b,X,y,a)))(
             params[0],params[1],params[2],params[3],params[4]))(
             [[random.uniform(-1,1)], random.uniform(-1,1),
              [[random.uniform(-2,2)] for _ in range(4)],
              [random.uniform(-2,2) for _ in range(4)],
              random.uniform(0.001,0.05)])
         for _ in range(15)))[1]),
]

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--all",action="store_true")
    args=parser.parse_args()
    print("\n"+"="*55+"\n  CODE EXPERT — Mini-Batch SGD\n"+"="*55)
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
