import sys
import os
from solution import compute_conditional_probability

def is_interactive():
  return os.environ['ACTION'] in("run", "debug")

def main():
  # Only display extra instructions if running in an interactive terminal
  if sys.stdin.isatty():
      print("Computing conditional probability")
      print("Please enter a list of (xi, yi), in one line, according to Python syntax")
  try:
      samples = eval(input())
      result = float(compute_conditional_probability(samples))
      result = round(result, 2)
      if is_interactive(): 
        print(f"P(X=0|Y=1) = {result}")
      else:
        print("|",result,"|")
  except Exception as e:
      print(f"Error: {e}")