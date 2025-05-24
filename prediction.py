import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor

data = pd.read_csv("mtcars.csv")

labels = data['mpg']
train1 = data.drop(['model', 'mpg'],axis=1)

col_imp = ["cyl", "disp", "hp", "drat", "wt", "qsec"]

clf = GradientBoostingRegressor(n_estimators = 400, max_depth = 5, min_samples_split = 2)
clf.fit(train1[col_imp], labels)

def predict(dict_values, col_imp=col_imp, clf=clf):
    x = np.array([float(dict_values[col]) for col in col_imp])
    x = x.reshape(1,-1)
    y_pred = clf.predict(x)[0]
    return y_pred
