import sys
import os
import solution
import scipy

def is_interactive():
  return os.environ['ACTION'] in("run", "debug")

def main():
  # Only display extra instructions if running in an interactive terminal
  my_input = input('Enter <dist> <a> <b> <n> <low> <high>: \n').split()
  distr = my_input[0]
  a = float(my_input[1])
  b = float(my_input[2])
  if distr == 'beta':
    distribution = scipy.stats.beta(a,b)
  elif distr == 'uniform':
    distribution = scipy.stats.uniform(a,b)
  else:
    distribution = scipy.stats.norm(a,b)
  n = int(my_input[3])
  low = float(my_input[4])
  high = float(my_input[5])
  
  if is_interactive():
    mean = solution.mean(distribution,n)
    variance = solution.variance(distribution,n)
    probability = solution.approximate(distribution,n,low,high)
  
    print("E(Sn)=",mean)
    print("Var(Sn)=",variance)
    print("P(Sn in [",low,",",high,"])=",probability)
  else:
    value = float(my_input[7])
    delta = float(my_input[8])
    if my_input[6] == 'mean':
      result = solution.mean(distribution,n)
      print("E(Sn)=",result)
    elif my_input[6] == 'var':
      result = solution.variance(distribution,n)
      print("Var(Sn)=",result)
    elif my_input[6] == 'prob':
      result = solution.approximate(distribution,n,low,high)
      print("P(Sn in [",low,",",high,"])=",result)
    print("Expected result in [",value-delta,",",value+delta,"]")
    assert(value - delta <= result <= value + delta)

  print("ok")