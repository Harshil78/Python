ad = lambda a: a + 10
print(ad(5))

p = lambda a, b: pow(a, b)
print(p(2, 3))


def multi(n):
    return lambda a: a * n


double = multi(2)  # pass n ,call lembda  ,call lambda a:a*2
triple = multi(3)
print(double(5))
print(triple(3))
