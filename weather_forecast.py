import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


df = pd.read_csv("weather.csv")
print(df.columns)
print(df.iloc[:, 0:12].head())
print(df.iloc[:, 12:25].head())

x = df.drop(['Date', 'RainTomorrow'], axis=1)
y = df['RainTomorrow']

train_x, train_y, test_x, test_y = train_test_split(x, y, test_size=0.2, random_state=2)

model = LogisticRegression()
model.fit(train_x, test_x)
predict = model.predict(train_y)

print(accuracy_score(predict, test_y))
