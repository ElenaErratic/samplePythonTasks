import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score


"""
Stage 3/4: Multiple linear regression: intercept and 
coefficient(s) predictions and metrics (R^2 and RMSE).

"""

df = pd.DataFrame({'y': [21.95, 27.18, 16.9, 15.37, 16.03, 18.15, 14.22, 18.72, 15.4, 14.69],
                   'x': [11, 11, 9, 8, 7, 7, 6, 5, 5, 4],
                   'w': [0.9, 0.5, 1.75, 2.0, 1.4, 1.5, 3.0, 1.1, 2.6, 1.9]})


class CustomLinearRegression:

    def __init__(self, *, fit_intercept=True):

        self.fit_intercept = fit_intercept
        self.coefficient = None
        self.intercept = None
        self.RMSE = None
        self.R2 = None

    def fit(self, X, y):
        X, y = np.asarray(X), np.asarray(y)
        if self.fit_intercept:
            X = np.c_[(np.ones_like(y), X)]
            res = np.linalg.inv(X.T @ X) @ X.T @ y
            # print(res[1:])
            self.intercept = res[0]
            self.coefficient = res[2:0:-1]
            yhat = np.array(X @ res)
            self.RMSE = np.sqrt(mean_squared_error(y, yhat))
            self.R2 = r2_score(y, yhat)
            dict = {'Intercept': self.intercept,
                    'Coefficient': self.coefficient,
                    'R2': self.R2,
                    'RMSE': self.RMSE}
            print(dict)
        else:
            self.coefficient = np.linalg.inv(X.T @ X) @ X.T @ y
        return None

regCustom = CustomLinearRegression(fit_intercept=True)
regCustom.fit(df[['x', 'w']], df['y'])