from machinable import Component

from sklearn.linear_model import Ridge


class RidgeRegression(Component):
    def on_create(self):
        model = Ridge(alpha=self.config.alpha)
        model.fit([[0, 0], [0, 1], [1, 1]], [0, 0.1, 1])
        print(model.intercept_)
