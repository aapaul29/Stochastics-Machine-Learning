import sys, argparse, traceback, random, math
from solution import perceptron_predict, perceptron_update

def approx(a, b, tol=1e-5):
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
    ("predict +1 at zero",
     lambda: perceptron_predict([0.,0.],0.,[1.,2.])==1),
    ("predict -1 negative",
     lambda: perceptron_predict([1.,1.],-5.,[1.,1.])==-1),
    ("predict +1 positive",
     lambda: perceptron_predict([1.,0.],0.,[2.,0.])==1),
    ("update on misclassified (y=-1, predict=+1)",
     # predict([0,0],0,[-1,-1])=+1≠-1 → update: w+=0.1*(-1)*[-1,-1]=[0.1,0.1], b+=0.1*(-1)=-0.1
     lambda: (lambda r: approx(r[0],[0.1,0.1]) and approx(r[1],-0.1))(
         perceptron_update([0.,0.],0.,[-1.,-1.],-1,0.1))),
    ("no update if correct",
     lambda: (lambda r: approx(r[0],[0.,0.]) and approx(r[1],0.0))(
         perceptron_update([0.,0.],0.,[1.,1.],1,0.1))),
    ("returns +1 or -1 only",
     lambda: perceptron_predict([1.],0.,[0.]) in (1,-1)),
]

HIDDEN_TESTS = [
    ("update misclassified (y=+1, predict=-1)",
     # w=[0,0], b=-1.0, x=[1,1]: pred=-1, y=+1 → update
     # w+=[0.1*1*1,0.1*1*1]=[0.1,0.1], b+=-1+0.1=-0.9
     lambda: (lambda r: approx(r[0],[0.1,0.1]) and approx(r[1],-0.9))(
         perceptron_update([0.,0.],-1.,[1.,1.],+1,0.1))),
    ("update + then predict correct",
     lambda: (lambda r: perceptron_predict(r[0],r[1],[-1.,-1.])==-1)(
         perceptron_update([0.,0.],0.,[-1.,-1.],-1,0.1))),
    ("alpha=0 → no change even if wrong",
     lambda: (lambda r: approx(r[0],[0.,0.]) and approx(r[1],0.))(
         perceptron_update([0.,0.],0.,[1.,1.],-1,0.0))),
    ("stress: predict matches sign",
     lambda: (random.seed(33), all(
         perceptron_predict(w,b,x)==(1 if sum(w[i]*x[i] for i in range(2))+b>=0 else -1)
         for w,b,x in [([random.uniform(-2,2),random.uniform(-2,2)],
                         random.uniform(-2,2),[random.uniform(-2,2),random.uniform(-2,2)])
                        for _ in range(30)]))[1]),
    ("stress: after update, correct",
     lambda: all(
         (lambda r: perceptron_predict(r[0],r[1],[1.,0.])== -1)(
             perceptron_update([0.,0.],b,[1.,0.],-1,0.5))
         for b in [0.0, 0.1, 0.5])),
]

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--all",action="store_true")
    args=parser.parse_args()
    print("\n"+"="*55+"\n  CODE EXPERT — Perceptron Learning Rule\n"+"="*55)
    passed=0; total=0
    print("\n── Public Tests ──────────────────────────────────────")
    for name,fn in PUBLIC_TESTS:
        ok=run_test(name,fn); passed+=ok; total+=1
    if args.all:
        print("\n── Hidden Tests ──────────────────────────────────────")
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
