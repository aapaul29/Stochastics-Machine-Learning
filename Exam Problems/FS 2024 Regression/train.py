import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def train_model():
    train_df = pd.read_csv("data.csv")

    train_X = train_df.drop("y", axis=1)
    train_y = train_df["y"]

    model = LinearRegression()
    model.fit(train_X, train_y)
    
    return model