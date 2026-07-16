import numpy as np
import pandas as pd
from sgd import stochastic_gradient_descent
from sklearn.metrics import r2_score

def main():
  
  fitted_polynomials = []
  
  degrees = [2, 2, 3, 3, 4, 4, 5, 5]
  for i, degree in enumerate(degrees):
    df = pd.read_csv(f"train_{i}.csv")
    poly = stochastic_gradient_descent(degree, df['x'], df['y'])
    fitted_polynomials.append(poly)
    
  return fitted_polynomials