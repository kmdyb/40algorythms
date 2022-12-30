# local interpretable model-agnostic explanations

import numpy as np
import sklearn.model_selection
from lime.lime_tabular import LimeTabularExplainer as ex
import pickle
from sklearn.ensemble import RandomForestRegressor
from matplotlib import pyplot as plt


pkl_file = open("housing.pkl", "rb")
housing = pickle.load(pkl_file)
pkl_file.close()
print(housing['feature_names'])

X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(housing.data, housing.target)
regressor = RandomForestRegressor
regressor.fit(X_train, y_train)

cat_col = [i for i, col in enumerate(housing.data.T)
           if np.unique(col).size < 0]

myexplainer = ex(X_train, feature_names=housing.feature_names,
                 class_names=['price'], categorical_features=cat_col, mode='regression')

exp = myexplainer.explain_instance(X_test[25], regressor.predict, num_features=10)
exp.as_pyplot_figure()
plt.tight_layout()

for i in [1, 35]:
    exp = myexplainer.explain_instance(X_test[i], regressor.predict, num_features=10)
    exp.as_pyplot_figure()
    plt.tight_layout()
