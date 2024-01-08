# import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB

# Load Data from CSV
data = pd.read_csv('tennisdata.csv')

# obtain train data and train output
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# convert them in numbers
label_encoder = LabelEncoder()
for col in X.columns.tolist():
  X.loc[:,col] = label_encoder.fit_transform(X[col])
y = label_encoder.fit_transform(y)

# split the data into test and train
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.10)

# train the Naive Bayesian classifier
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# make predictions
y_pred = classifier.predict(X_test)

# print the results
print('Test data:', y_test)
print('Predicted data:', y_pred)
print("Accuracy is:", metrics.accuracy_score(y_pred, y_test))