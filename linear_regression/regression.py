import numpy as np
import pandas as pd

"""
Stage 2/4: Multiple linear regression and predictions.
In the previous stage, we assumed that our system of equations has an intercept. 
In this stage, we need to modify our fit method to account for no intercept.
predict() method takes a pandas DataFrame XX and returns a numpy array of predictions.
"""

df = pd.DataFrame({'y': [33, 42, 45, 51, 53, 61, 62],
                   'x': [4, 4.5, 5, 5.5, 6, 6.5, 7],
                   'w': [1, -3, 2, 5, 0, 3, 6],
                   'z': [11, 15, 12, 9, 18, 13, 16]})


class CustomLinearRegression:

    def __init__(self, *, fit_intercept=True):

        self.fit_intercept = fit_intercept
        self.coefficient = None
        self.intercept = None

    def fit(self, X, y):
        X, y = np.asarray(X), np.asarray(y)
        if self.fit_intercept:
            X = np.c_[(np.ones_like(y), X)]
            res = np.linalg.inv(X.T @ X) @ X.T @ y
            self.intercept = res[0]
            self.coefficient = res[1:]
            print(f"{{'Intercept': {self.intercept}, 'Coefficient': array({self.coefficient})}}")
        else:
            self.coefficient = np.linalg.inv(X.T @ X) @ X.T @ y


    def predict(self, X):
        self.X = X
        y = np.array(X @ self.coefficient)
        print(y)

regCustom = CustomLinearRegression(fit_intercept=False)
regCustom.fit(df[['x', 'w', 'z']], df['y'])
y_pred = regCustom.predict(df[['x', 'w', 'z']])
