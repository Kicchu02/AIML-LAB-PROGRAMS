import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the tennis dataset
tennis_data = pd.read_csv('tennisdata.csv')

# Convert categorical variables to numerical values
tennis_data = pd.get_dummies(tennis_data, columns=['Outlook', 'Temperature', 'Humidity', 'Windy', 'PlayTennis'], drop_first=True)

# Split the dataset into features (X) and target variable (y)
X = tennis_data.drop('PlayTennis_Yes', axis=1)
y = tennis_data['PlayTennis_Yes']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create and train the Decision Tree model
dt_model = DecisionTreeClassifier(criterion='entropy')
dt_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = dt_model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Display the Decision Tree
tree_rules = export_text(dt_model, feature_names=X.columns.tolist())
print("\nDecision Tree Rules:")
print(tree_rules)