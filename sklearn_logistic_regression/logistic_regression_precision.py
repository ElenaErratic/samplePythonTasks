"""Get the predictions for test set and evaluate the quality of the model with PrecisionPrecision metric and parameter average='macro'"""
from sklearn.metrics import precision_score
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = load_iris()
X = data.data
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=92)

model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

precision = precision_score(y_test, y_pred, average='macro')
print(precision)
