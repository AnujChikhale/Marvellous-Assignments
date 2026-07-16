class Demo:
    Value = 0

    def __init__(self, a, b):
        self.no1 = a
        self.no2 = b

    def fun(self):
        print(self.no1)
        print(self.no2)

    def gun(self):
        print(self.no1)
        print(self.no2)

dobj1 = Demo(11,12)
dobj2 = Demo(51,101)
dobj1.fun()
dobj2.fun()
dobj1.gun()
dobj2.gun()

    