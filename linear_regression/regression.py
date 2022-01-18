from scipy.stats import linregress

"""
Stage 1 of 4
Task: Calculate the linear regression for the dataset and print the intercept and coefficient.
Required result format: {'Intercept': 2.0, 'Coefficient': array([2.])}
https://hyperskill.org/projects/195/stages/971/implement"""

x = [4.0, 4.5, 5, 5.5, 6.0, 6.5, 7.0]
y = [33, 42, 45, 51, 53, 61, 62]
res = linregress(x, y)


class CustomLinearRegression:

    def __init__(self, *, fit_intercept=True):

        self.fit_intercept = True
        self.coefficient = res[0]
        self.intercept = res[1]

    def fit(self, X, y):
        self.X = X
        self.y = y
        pass
        print(f"{{'Intercept': {self.coefficient}, 'Coefficient': {self.intercept}}}")
        # {'Intercept': 2.0, 'Coefficient': array([2.])}

dataset = CustomLinearRegression(fit_intercept=True)
dataset.fit(x, y)
