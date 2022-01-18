import numpy as np
import pandas as pd
from scipy.stats import linregress

"""
Stage 2 of 4
Task: Calculate multiple linear regression for the dataset and print the coefficients.
https://hyperskill.org/projects/195/stages/972/implement"""

df = pd.DataFrame({'y': [33, 42, 45, 51, 53, 61, 62],
                   'x': [4, 4.5, 5, 5.5, 6, 6.5, 7],
                   'w': [1, -3, 2, 5, 0, 3, 6],
                   'z': [11, 15, 12, 9, 18, 13, 16]})


class CustomLinearRegression:

    def __init__(self, *, fit_intercept=True):

        self.fit_intercept = True
        self.coefficient = None
        self.intercept = None

    def fit(self, X, y):
        if self.fit_intercept:

            self.X = X
            self.y = y
            res = linregress(X, y)
            self.coefficient = res[0]  # np.array(res[0])
            self.intercept = res[1]
            print(f"{{'Intercept': {self.intercept}, 'Coefficient': array([{self.coefficient}])}}")
        else:
            pass  # todo


    def predict(self, X):
        pass

regCustom = CustomLinearRegression(fit_intercept=False)
regCustom.fit(df[['x', 'w', 'z']], df['y'])
y_pred = regCustom.predict(df[['x', 'w', 'z']])
