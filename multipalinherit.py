class calcs:
    def Add(self, a, b):
        return a + b


class calcm:
    def Multi(self, a, b):
        return a * b

    def Add(self, a, b):
        return a - b


class calcd:
    def Divde(self, a, b):
        return a / b


class calc(calcs, calcm, calcd):
    pass


c = calc()
print(c.Add(10, 20))
print(c.Multi(10, 20))
print(c.Divde(10, 20))
