from solution import update

def stochastic_gradient_descent(n, X, Y):
  """
  This function takes as input X, Y as above and tries to estimate the w's using stochastic gradient descent

  Args:
    n: Degree of the polynomial
    X: A list of m floats between -10 and 10
    Y: A list of m floats, where Y[i] is the result of applying an unknown polynomial of degree n to X[i]

  Returns:
    A list of length n, representing the estimated w's
  """

  n_iter = 200
  w = [0.0 for _ in range(n)]
  for _ in range(n_iter):
    for i in range(len(X)):
      update(w, X[i], Y[i])
  return w