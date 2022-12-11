from sklearn import ensemble
from sklearn.metrics import mean_squared_error
from math import sqrt


params = {'n_estimators': 500, 'max_depth': 4, 'min_samples_split': 2, 'learning_rate': 0.01, 'loss': 'ls'}
regressor = ensemble.GradientBoostingRegressor(**params)
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
print(sqrt(mean_squared_error(y_test, y_pred)))
