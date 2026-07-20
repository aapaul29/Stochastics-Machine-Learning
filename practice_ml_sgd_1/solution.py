def inner_product(w : list[float], x: list[float]) -> float:
    ip = 0
    for i in range(len(w)):
        ip += w[i] * x[i]
    return ip
    


def w_step(w: list[float], x: list[float], b: float, alpha: float, y: float, i: float) -> float:
    gradient = 2 * (inner_product(w, x) + b - y) * x[i]
    w_i = w[i] - alpha * gradient
    return round(w_i, 6)


def b_step(w: list[float], x: list[float], b: float, alpha: float, y: float) -> float:
    gradient = 2 * (inner_product(w, x) + b - y)
    b = b - alpha * gradient
    return round(b, 6)



def sgd_update(w: list[float], b: float, x: list[float],
               y: float, alpha: float) -> tuple[list[float], float]:
    """Return (w_new, b_new) after one SGD step on sample (x, y).
    Each value rounded to 6 decimal places."""
    # TODO
    w_new = []
    b_new = b_step(w, x, b, alpha, y)
    for i in range(len(w)):
        w_i = w_step(w, x, b, alpha, y, i)
        w_new.append(w_i)
        

    return (w_new, b_new)
