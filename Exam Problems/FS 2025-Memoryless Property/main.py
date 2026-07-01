import sys
import os
import solution
import random


def is_interactive():
  return os.environ['ACTION'] in("run", "debug")

def main():
  # Only display extra instructions if running in an interactive terminal
  my_input = input('Enter <n> <s> <t> <eps> <dist> <dist_param_0> <dist_param_1>: \n').split()
  #print(my_input) # TODO: remove
  
  n = int(my_input[0])
  s = float(my_input[1])
  t = float(my_input[2])
  eps = float(my_input[3])
  distr=my_input[4]
  
  samples = []
  test_param_id = 6
  random.seed(10)
  if distr == 'exp':
    lambda_ = float(my_input[5]) #1 or 2
    samples = [random.expovariate(lambda_) for _ in range(n)]
  elif distr == 'normal':  
    mu = float(my_input[5]) # 0.35
    sigma = float(my_input[6]) # 0.25
    samples = [random.gauss(mu, sigma) for _ in range(n)]
    test_param_id = 7
  else:
    a = float(my_input[5]) #0
    b = float(my_input[6]) #1.2
    test_param_id = 7
    samples = [random.uniform(a,b) for _ in range(n)]
  
  if is_interactive():
    p_larger_than_t = solution.prob_larger_than_t(samples, t)
    cond_prob = solution.prob_larger_than_s_plus_t(samples, s, t)
    is_memoryless = solution.has_memoryless_property(samples, s, t, eps)
  
    print("P(X>",t,")=",p_larger_than_t)
    print("P(X>",s,"+",t,"| X>",s,")=",cond_prob)
    print("||P(X>",s,"+",t,"| X>",s,") - P(X>",t,")|| < eps=",is_memoryless)
  else:
    test_type = my_input[test_param_id]
    
    
    if test_type == 'prob':
      result = solution.prob_larger_than_t(samples, t)
      print("P(X>",t,")=",result)
      value = float(my_input[test_param_id+1])
      delta = float(my_input[test_param_id+2])
      print("Expected result in [",value-delta,",",value+delta,"]")
      assert(value - delta <= result <= value + delta)
    elif test_type == 'cond':
      result = solution.prob_larger_than_s_plus_t(samples, s, t)
      print("P(X>",s,"+",t,"| X>",s,")=",result)
      value = float(my_input[test_param_id+1])
      delta = float(my_input[test_param_id+2])
      print("Expected result in [",value-delta,",",value+delta,"]")
      assert(value - delta <= result <= value + delta)
    elif test_type == 'memory':
      result = solution.has_memoryless_property(samples, s, t, eps)
      print("||P(X>",s,"+",t,"| X>",s,") - P(X>",t,")|| < eps=",result)
      value = my_input[test_param_id+1] == 'True'
      print("Expected result:", value)
      assert( result == value)

  print("ok")