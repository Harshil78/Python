# + __add__
# - __sub__
# * __mul__
# / __truediv__
# // __floordiv__
# % __mod__
# > __gt__
# < __lt__
# >= __ge__
# <= __le__
# == __eq__
# == __eq__
# != __nq__
# [] __getitem__(self,index)


class point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "x=" + str(self.__x) + ",y=" + str(self.__y)

    def __add__(self, p):
        temp = point()
        temp.__x = self.__x + p.__x
        temp.__y = self.__y + p.__y
        return temp

    def __sub__(self, p):
        temp = point()
        temp.__x = self.__x - p.__x
        temp.__y = self.__y - p.__y
        return temp

    def __mul__(self, p):
        temp = point()
        temp.__x = self.__x * p.__x
        temp.__y = self.__y * p.__y
        return temp

    def __truediv__(self, p):
        temp = point()
        if p.__x == 0 or p.__y == 0:
            print("not possible")
        else:
            temp.__x = self.__x / p.__x
            temp.__y = self.__y / p.__y
        return temp


p1 = point(10, 0)
p2 = point(12, 24)
p3 = p1 + p2
print(str(p3))
p3 = p2 - p1
print(str(p3))
p3 = p1 * p2
print(str(p3))
p3 = p2 / p1
print(str(p3))
