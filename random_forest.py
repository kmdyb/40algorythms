from sklearn.ensemble import RandomForestClassifier


classifier = RandomForestClassifier(n_estimators=10, max_depth=4, criterion='entropy', random_state=0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
cm = metrics.confusion_matrix(y_test, y_pred)
print(cm)

accuracy = metrics.accuracy_score(y_test, y_pred)
recall = metrics.recall_score(Y_test, y_pred)
print(accuracy, recall, precision)
