"""Fit the model on all the data from the Iris dataset. Get the OOB score."""
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

model = RandomForestClassifier(n_estimators=17,
                               max_features='sqrt',
                               oob_score=True,
                               random_state=774)
model.fit(X, y)

print(model.oob_score_)
