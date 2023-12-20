import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

# Load dataset
dataset = pd.read_csv('iris.csv')

# Prepare data
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

# Split data
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.10)

# Train the KNN classifier
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(Xtrain, ytrain)

# Make predictions
ypred = classifier.predict(Xtest)

# Evaluate and print results
print('\n-------------------------------------')
print(f"Accuracy of the classifier is {metrics.accuracy_score(ytest, ypred)}")
print('---------------------------------------')
print('\nConfusion Matrix:\n', metrics.confusion_matrix(ytest, ypred))
print('---------------------------------------')
print('\nClassification Report:\n', metrics.classification_report(ytest, ypred))
print('---------------------------------------')
