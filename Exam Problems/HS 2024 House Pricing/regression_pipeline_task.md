# Regression

The file `main.py` loads the housing price data (which you know from the exercises) and tries to train a regression model on it. For this, it builds a Pipeline, then it adds a linear regression model at the end of it and trains it using the housing price data. Unfortunately, the trained model does not work. Modify `train.py` so that the resulting pipeline yields an acceptable R2 score.

We already did one-hot encoding on this data, so you may assume that all data is numeric. However, there are missing values on the data.

**Scoring:** The number of points you get in this question depends on the R2 score your solution attains on the test data. The number of points is computed with a linear interpolation between (0.65, 0) and (0.8, 6). That is, to get 6 points, you must get an R2 score of at least 0.8. To get at least any amount of points, you must get an R2 score of at least 0.65.

**Remark:** Make sure that your data is reproducible by setting `random_state=0` in the constructor of all relevant classes. We do not give any guarantee on the amount of points obtained without this.

Below you find a list of imports that might be useful for this task:

```python
# Imputation and Missing Value Handling
from sklearn.impute import SimpleImputer
from sklearn.impute import KNNImputer
from sklearn.impute import MissingIndicator

# Preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Binarizer
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import PowerTransformer

# Feature Selection
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import RFE
from sklearn.feature_selection import SelectFromModel
from sklearn.feature_selection import VarianceThreshold

# Dimensionality Reduction
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA
from sklearn.decomposition import TruncatedSVD

# Model Selection
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold

# Regression Models
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import BayesianRidge
from sklearn.linear_model import SGDRegressor

# Classification Models
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

# Clustering
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.cluster import AgglomerativeClustering

# Ensemble Methods
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import VotingRegressor
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import BaggingRegressor

# Metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.metrics import classification_report
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import plot_roc_curve

# Pipelines
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
```
