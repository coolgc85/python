__author__ = 'galo javier'


class Dog:

    # tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)                # unexpectedly shared by all dogs

#flag = True
flag = bool(input("Y N")=="Y")
print(flag)

