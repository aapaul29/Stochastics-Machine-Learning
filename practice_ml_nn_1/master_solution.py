import math

def sigmoid(z: float) -> float:
    """Sigmoid activation, rounded to 6 dp."""
    return round(1.0 / (1.0 + math.exp(-z)), 6)

def sigmoid_derivative(z: float) -> float:
    """Derivative of sigmoid, rounded to 6 dp."""
    s = sigmoid(z)
    return round(s * (1 - s), 6)

def softmax(z: list[float]) -> list[float]:
    """Softmax of vector z, each value rounded to 6 dp."""
    m = max(z)
    exps = [math.exp(zi - m) for zi in z]
    s = sum(exps)
    return [round(e / s, 6) for e in exps]
