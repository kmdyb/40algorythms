from sklearn.svm import SVC
import sklearn.metrics as metrics


classifier = SVC(kernel='linear', random_state=0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
cm = metrics.confusion_matrix(y_test, y_pred)
print(cm)

accuracy = metrics.accuracy_score(y_test, y_pred)
recall = metrics.recall_score(y_test, y_pred)
precision = metrics.precision_score(y_test, y_pred)
print(accuracy, recall, precision)
