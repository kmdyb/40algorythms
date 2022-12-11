from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from math import sqrt


regressor = DecisionTreeRegressor(max_depth=3)
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
print(sqrt(mean_squared_error(y_test, y_pred)))
