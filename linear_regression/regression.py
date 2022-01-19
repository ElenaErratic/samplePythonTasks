import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


"""
Stage 4/4: Multiple linear regression: comparing the 'hand-made' model and
sklearn LinearRegression.
"""


df = pd.read_csv("data/data_stage4.csv")
X = df[['f1', 'f2', 'f3']]
y = df['y']

def custom_rmse(y, yhat):
    return np.sqrt(np.mean((y - yhat) ** 2))


def custom_r2_score(y, yhat):
    return 1 - np.sum((y - yhat) ** 2) / np.sum((y - np.mean(y)) ** 2)

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
            self.coefficient = res[1:]
            yhat = np.array(X @ res)
            self.RMSE = custom_rmse(y, yhat)
            self.R2 = custom_r2_score(y, yhat)
        else:
            self.coefficient = np.linalg.inv(X.T @ X) @ X.T @ y
        return None

regCustom = CustomLinearRegression(fit_intercept=True)
regCustom.fit(df[['f1', 'f2', 'f3']], df['y'])

regSci = LinearRegression(fit_intercept=True)
regSci.fit(X, y)
Y_predict = regSci.predict(X)


i = np.float64(regSci.intercept_ - regCustom.intercept)
c = (regSci.coef_ - regCustom.coefficient).astype(float)
r = np.longdouble(r2_score(y, Y_predict) - regCustom.R2)
rm = (np.sqrt(mean_squared_error(y, Y_predict)) - regCustom.RMSE)

print(f"{{'Intercept': {i}, 'Coefficient': {c}, 'R2': {r}, 'RMSE': {rm}}}")
# currently there's the float subtraction problem, so visual comparing the value
# pairs works better than subracting them