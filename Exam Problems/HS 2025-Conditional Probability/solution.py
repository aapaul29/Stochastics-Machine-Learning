import numpy as np

# given pairs of observations samples[i] (0 <= i < N)
# where samples[i][0] stands for an observation of X and
# samples[i][1] stands for an observation of Y
# return the exmpirical conditional probability P(X=0|Y=1)
def compute_conditional_probability(samples: list[tuple[int, int]]) -> float:

  N = len(samples)
  X0Y1 = 0
  Y1 = 0
  
  for i in range(N):
    sample = samples[i]
    if sample[1] == 1:
      Y1 += 1
      if sample[0] == 0:
        X0Y1 += 1
  
  if Y1 == 0:
    return 0
  else:
    return X0Y1 / Y1