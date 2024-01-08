import pandas as pd
from pprint import pprint
from collections import Counter
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import mutual_info_classif

def id3(data, target_attribute, attribute_names, default_class=None):
  # if the target contains only yes or only no, return corresponding yes or no
  count = Counter(data[target_attribute])
  if len(count) == 1:
    return next(iter(count))
  # else if the data is empty or no attribute names are present, return the parent class
  elif data.empty or not attribute_names:
    return default_class
  
  # split the data into input and output columns
  X = data[attribute_names]
  Y = data[target_attribute]
  
  # calculate gains using the inbuilt function
  gains = mutual_info_classif(X, Y, discrete_features=True)

  # take the attribute with max gain as the best attribute
  best_attribute = attribute_names[gains.argmax()]

  # construct tree with best attribute as root node
  tree = {best_attribute: {}}

  # reduce the attribute names and recursively call the id3 to construct the subtree
  remaining_attribute_names = [i for i in attribute_names if i != best_attribute]
  tree[best_attribute] = {
    val : id3(data_subset, target_attribute, remaining_attribute_names, default_class) for val, data_subset in data.groupby(best_attribute)
  }

  return tree

# read the dataset
data = pd.read_csv('tennisdata.csv')

# get the attribute names as list and remove the target column
attribute_names = data.columns.tolist()
attribute_names.remove(attribute_names[-1])

# convert string data to numerical values
label_encoder = LabelEncoder()
for attr in attribute_names:
  data[attr] = label_encoder.fit_transform(data[attr])

# get the tree from id3 algorithm and print it
tree = id3(data, 'PlayTennis', attribute_names)
pprint(tree)