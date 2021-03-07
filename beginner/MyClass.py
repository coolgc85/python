__author__ = 'galo javier'


class MyClass:

    def __init__(self, b):
        self.b = b

    def do_something(self):
        print("do Something")

    def do_sum(self, a, b):
        i = a + b
        return i
       ## print("sum = "+i)

    def do_sum(self, a):
        i = self.b + a
        return i

x = MyClass(8)
print(x.b)
x.do_something()
y = x.do_sum(1)
print("function object")
print(y)