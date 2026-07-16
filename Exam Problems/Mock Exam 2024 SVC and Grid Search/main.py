from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
import pandas as pd
import pickle
import warnings
warnings.filterwarnings("ignore", message="X does not have valid feature names, but SVC was fitted with feature names", category=UserWarning)

def main():
    # read data
    train_data = pd.read_csv('data.csv')
    x_train, y_train = train_data.drop(['y'], axis=1), train_data['y']

    model = SVC(random_state=0)
    model.fit(x_train, y_train)

    return model