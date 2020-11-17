
#importing the libraries
import numpy as np
import pandas as pd

#Read the data
header_names = ['cast_name', 'bio', 'season', 'winner']
df = pd.read_csv("Survivor_Cast.csv",header=None,names=header_names)

#Clean the data
df.drop(df.index[:2], inplace=True)
df = df[df.cast_name != 'Adam Klein']
df = df[df.cast_name != 'Ethan Zohn']
df = df[df.cast_name != 'Jeff Probst']



#Text Preprocessing
import re
import nltk

nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus = []
for i in range(0, len(df.index)):
    contestant = re.sub('[^a-zA-Z]', ' ', df.iloc[i, 1])
    contestant = contestant.lower()
    contestant = contestant.split()
    ps = PorterStemmer()
    contestant = [ps.stem(word) for word in contestant if not word in set(stopwords.words('english'))]
    contestant = ' '.join(contestant)
    corpus.append(contestant)

#Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = df.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Evaluating the model
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
accuracy_score(y_test, y_pred)
cm
