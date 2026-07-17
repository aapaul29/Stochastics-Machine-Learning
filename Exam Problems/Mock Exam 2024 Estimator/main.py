import numpy as np
from solution import estimator


def make_noisy_sin(zero):
  def noisy_sin(x):
    return np.sin(x - zero) + np.random.normal(0, 0.01)
  return noisy_sin
    

def main():
  np.random.seed(42)
  
  penalties = []
  num_tests = 10
  for i in range(num_tests):
    zero = np.random.uniform(-5, 5)
    noisy_sin = make_noisy_sin(zero)
    
    x = estimator(noisy_sin)
    penalty = np.sin(x - zero)
    if i <= 4:
      print(f"The function is sin(x - {zero:.2f}).", end=" ")
      print(f"Prediction: {x:.2f}", end=" ")
    else:
      print(f"The function is sin(x - ???)", end=" ")
      print(f"Prediction: ???", end=" ")
    print(f"Penalty = {penalty:.2f}")
    penalties.append(abs(penalty))
  return abs(sum(penalties) / num_tests)