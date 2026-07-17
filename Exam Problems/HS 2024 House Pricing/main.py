import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from train import make_pipeline_list
from utils import load_data
from sklearn.metrics import r2_score

random_seed = 42

def main():
  
  X_train, X_test, y_train, y_test = load_data()
  
  pipe_list = make_pipeline_list()
  pipe_list += [("lr", LinearRegression())]
  pipe = Pipeline(pipe_list)
  pipe.fit(X_train, y_train)
  y_pred = pipe.predict(X_test)
  
  r2 = r2_score(y_test, y_pred)
  
  print(f"R2 score on test data: {r2:.2f}")
  return r2