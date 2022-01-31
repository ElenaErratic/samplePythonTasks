"""
1. Load the iris dataset with the code snippet below. You don't need to split the data into training and test sets.

2. Train a DecisionTreeClassifier with random_state=42.

3. Download a dataset below.

4. Make predictions for the downloaded dataset.

5. Find out how many setosa species according to your model must be in the dataset.

6. Insert the number of setosa species in the answer field.

[ALERT] Keep in mind, that the values 0, 1, 2 in the prediction array correspond to the setosa, versicolor and virginica species respectively.

"""
import collections
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

clf = DecisionTreeClassifier(random_state=42)
clf.fit(X, y)

dataset = pd.read_csv("dataset/input.txt", header=None)
X_dataset = dataset.drop(0, axis=0)

prediction = clf.predict(X_dataset)
counts = collections.Counter(prediction)
print(counts[0])
