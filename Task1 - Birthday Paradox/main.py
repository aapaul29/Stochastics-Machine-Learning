from solution import simulated_prob, analytical_prob, graph_comparison
import math
import os

def is_interactive():
  return os.environ['ACTION'] in("run", "debug")

def main():
  # input
  try:
    # mountain = [int(x) for x in input('Enter a mountain profile: ').split()]
    npeople, nrepeats, ndays,  ntrials = [int(x) for x in input('Enter npeople, nrepeats, ndays, ntrials: ').split()]
  except:
    print('Error: Input does not seem to be of the correct format.')
    return

  sim_prob = simulated_prob(npeople,ndays, nrepeats, ntrials)

  if nrepeats != 2:
    print(f'\Simulated probability prob: {sim_prob}')
    print('We only compute analytical probability for nrepeats=2.')
  else:
    th_prob = analytical_prob(npeople, ndays)
    print(f'\nSimulated probability: {sim_prob},  vs Analytical probability: {th_prob}')

  if is_interactive() and nrepeats==2:
    graph_comparison(ndays, ntrials)


  if not is_interactive():
    failed = False
    test,min_value,max_value = input().split()
    min_value = float(min_value)
    max_value = float(max_value)
    if test == "theory":
      if not (min_value <= th_prob <= max_value):
        print("Analytical result out of bounds")
        failed = True
    elif test == "estimate":
      if not (min_value <= sim_prob <= max_value):
        print("Estimated result out of bounds")
        failed = True
    if not failed:
      print("OK")
