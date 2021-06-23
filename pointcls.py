class point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print(self.__class__.__name__, "destroyed")

    def __str__(self):
        return 'x=%d,%d' % (self.x, self.y)


p = point()
print(id(p))
print(str(p))
del p
print(id(p))
