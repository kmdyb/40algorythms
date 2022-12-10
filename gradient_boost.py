from xgboost import XGBClassifier
import sklearn.metrics as metrics


classifier = XGBClassifier()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
cm - metrics.confusion_matrix(y_test, y_pred)
print(cm)

accuracy = metrics.accuracy_score(y_test, y_pred)
recall = metrics.recall_score(y_test, y_pred)
precision = metrics.precision_score(y_test, y_pred)
print(accuracy, recall, precision)
