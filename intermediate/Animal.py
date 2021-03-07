__author__ = 'galo javier'


class Animal:
    def __init__(self, name):
        self.name = name

    def description(self):
        print(self.name)


hippo = Animal("Barney")
hippo.description()

