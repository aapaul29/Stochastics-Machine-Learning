def inner_product(u: list[float], v: list[float]):
    ip = 0
    for i in range(len(u)):
        ip += u[i] * v[i]
    return ip

def scalar_vector_product(lam: float, v: list[float]):
    v_new = [lam * v[i] for i in range(len(v))]
    return v_new

def vector_addition(u: list[float], v: list[float]):
    w = []
    for i in range(len(u)):
        w.append(u[i] + v[i])
    return w

def vector_subtraction(u: list[float], v: list[float]):
    w = []
    for i in range(len(u)):
        w.append(u[i] - v[i])
    return w

def w_step(w : list[float], b: float, X_batch:list[list[float]], y_batch: list[float], alpha: float):
    m = len(X_batch)
    gradient = [0] * len(w)
    for i in range(m):
        gradient =vector_addition(gradient, scalar_vector_product(2 / m * (inner_product(w, X_batch[i]) + b - y_batch[i]), X_batch[i]))
        w_new = vector_subtraction(w, scalar_vector_product(alpha, gradient))
    return w_new
    
    
    

def b_step(w : list[float], b: float, X_batch:list[list[float]], y_batch: list[float], alpha: float) -> float:
    m = len(X_batch)
    gradient = 0
    for i in range(m):
        gradient += 2 / m * (inner_product(w, X_batch[i]) + b - y_batch[i])
        b_new =  b - alpha * gradient
    return b_new

def minibatch_sgd_step(w: list[float], b: float,
                       X_batch: list[list[float]], y_batch: list[float],
                       alpha: float) -> tuple[list[float], float]:
    """One mini-batch gradient descent step. Return (w_new, b_new), rounded to 6 dp."""
    # TODO
    w_new = w_step(w, b, X_batch, y_batch, alpha)
    b_new = b_step(w, b, X_batch, y_batch, alpha)
    return w_new, b_new


