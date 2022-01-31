"""Load the iris dataset with the code snippet below. Train a DecisionTreeClassifier with random_state=42
 and pick the optimal value in range from 1 to 7 for the max_depth parameter. Insert the value in the answer field."""


from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris


X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

clf = DecisionTreeClassifier(random_state=34)
clf.fit(X_train, y_train)

'''clf = tree.DecisionTreeClassifier(random_state=34, max_depth=3)
clf.fit(X_train, y_train)
'''

# For training data:
print(clf.score(X_train, y_train))
# >>> 1

# For test set:
print(clf.score(X_test, y_test))
# >>> 1

print(clf.get_depth())
# >>> 6
