import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix


dataset = pd.read_csv("Restaurant_Reviews.tsv", delimeter='\t', quoting=3)
dataset.head()

# oczyszczenie
nltk.download('stopwords')
corpus = []
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if word not in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

# definicja cech i etykiety
cv = CountVectorizer(max_features=1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

# podzial test i train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# trenowanie, naiwny bayesowski klasyfikator
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# przewidywanie
y_pred = classifier.predict(X_test)

# macierz pomylek
cm = confusion_matrix(y_test, y_pred)
print(cm)
