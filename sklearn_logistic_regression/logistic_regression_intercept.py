"""find and write the intercept of the Iris versicolor class, label 1"""

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

data = load_iris()
X = data.data
y = data.target

model = LogisticRegression()
model.fit(X, y)

print(model.intercept_[1])
