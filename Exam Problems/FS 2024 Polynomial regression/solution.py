
def evaluate_polynomial(w, x):
  """
  This function takes as input a list w of floats, a float x, and outputs sum([w[i] * x^i for i in range(len(w))])

  Args:
    w: A list of floats
    x: A float

  Returns:
    The sum of w[i] * x^i for i in range(len(w))
  """

  result = 0
  for i in range(len(w)):
    result += w[i] * x**i
  return result

def update(w, x, y):
  """
  This function takes as input the current estimates for the coefficients of the polynomial and a point (x, y). It must
  update w with the information from (x, y).
  
  Args:
    w: A list of floats containing the current estimates of the polynomial.
    x: A float between -10 and 10
    y: A float that is the result of applying a polynomial to x plus some random noise.
    
  Returns:
    None. Update the coefficients directly in w, using the information from (x, y)
  """
  # TODO
  pass