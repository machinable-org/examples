from machinable import Component


class BaselineModel(Component):

    def on_create(self):
        print('Hello World', self.config)
