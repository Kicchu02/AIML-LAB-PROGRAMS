import numpy as np
import matplotlib.pyplot as plt

def local_regression(x0, X, Y, tau):
    x0 = [1, x0]
    X = [[1, i] for i in X]
    X = np.asarray(X)
    xw = (X.T) * np.exp(np.sum((X - x0) ** 2, axis=1) / (-2 * tau))
    beta = np.linalg.pinv(xw @ X) @ xw @ Y @ x0
    return beta

def draw(tau):
    prediction = [local_regression(x0, X, Y, tau) for x0 in X]
    plt.scatter(X, Y, color='black')
    plt.scatter(X, prediction, color='red')

X = np.linspace(-3, 3, num=1000)
Y = np.abs(X ** 2 - 2)

plt.subplot(2,2,1)
draw(10)
plt.subplot(2,2,2)
draw(1)
plt.subplot(2,2,3)
draw(0.1)
plt.subplot(2,2,4)
draw(0.01)

plt.show()