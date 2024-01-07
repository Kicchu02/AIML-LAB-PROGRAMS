import pandas as pd
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt

# read the dataset
dataset = pd.read_csv('iris.csv',header=None ,names=['slength','swidth','plength','pwidth','species'])

# prepare the data
X = dataset.iloc[:,:-1].values

colormap = {'Iris-setosa': 'red', 'Iris-versicolor': 'green', 'Iris-virginica': 'blue'}

# perform both clustering algorithms
kmeans = KMeans(n_clusters=3)
kmeans_labels = kmeans.fit_predict(X)

em = GaussianMixture(n_components=3)
em_labels = em.fit_predict(X)

plt.subplot(1,3,1)
plt.scatter(X[:, 2], X[:,3], c=dataset['species'].map(colormap))

plt.subplot(1,3,2)
plt.scatter(X[:,2], X[:,3], c=kmeans_labels)
plt.title('K Means Clustering')

plt.subplot(1,3,3)
plt.scatter(X[:,2], X[:,3], c=em_labels)
plt.title('EM Clustering')

plt.show()