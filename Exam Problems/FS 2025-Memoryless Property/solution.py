import numpy as np

# return an approximation of the probability P(X > t)
def prob_larger_than_t(samples, t):
  n = len(samples)
  count_t = sum(1 for x in samples if x > t)
  prob_t = count_t / n
  return prob_t

# return an approximation of  conditional probability P(X>s+t | x>s)
def prob_larger_than_s_plus_t(samples, s, t):
  count_s = sum(1 for x in samples if x > s)
  #print(f"count_s: {count_s}")  # TODO: remove line
  count_s_plus_t = sum(1 for x in samples if x > s + t)
  cond_prob = count_s_plus_t / count_s
  return cond_prob

# return True iff the absolute difference between the probability P(X > t)
# and the conditional probability P(X>s+t | x>s) is below eps
def has_memoryless_property(samples, s, t, eps):
  prob_t = prob_larger_than_t(samples, t)
  cond_prob = prob_larger_than_s_plus_t(samples, s, t)
  #print(f"prob_t: {prob_t}")  # TODO: remove
  #print(f"cond_prob: {cond_prob}")  # TODO: remove
  return abs(cond_prob - prob_t) < eps
