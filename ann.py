import numpy as np

# initial the dataset and target
X = np.array(([2,9],[1,5],[3,6]), dtype=float)
Y = np.array(([92],[86],[89]), dtype=float)

# squish the dataset values to between 0 and 1
X /= 10
Y /= 100

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

# variable initialisation
number_of_iterations = 10000
learning_rate = 0.1
input_nodes = 2
output_nodes = 1
hidden_nodes = 3

# weights and bias initialisation
wh = np.random.uniform(size=(input_nodes, hidden_nodes))
wout = np.random.uniform(size=(hidden_nodes, output_nodes))
bh = np.random.uniform(size=(1, hidden_nodes))
bout = np.random.uniform(size=(1, output_nodes))

# start algorithm
for i in range(number_of_iterations):
  # forward propogation
  hout = sigmoid(X @ wh + bh)
  out = sigmoid(hout @ wout + bout)

  # backpropogation
  d_out = out * (1 - out) * (Y - out)
  d_hidden = hout * (1 - hout) * (d_out @ wout.T)

  # modify the weights
  wout += learning_rate * hout.T @ d_out
  wh += learning_rate * X.T @ d_hidden

print('input:\n' + str(X))
print('target:\n' + str(Y))
print('predicted:\n' + str(out))