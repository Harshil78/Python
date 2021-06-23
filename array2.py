l1 = [10, 20, 30, 40, 50, 60, 70]
l2 = [11, 12, 13, 14, 15]
print(id(l1))
l1.extend(l2)
print(id(l1))

t1 = (10, 20, 30, 40, 50, 60, 70)
t2 = (11, 12, 13, 14, 15)
print(id(t1))
t1 = t1 + t2
print(id(t1))

for a in t1:
    print(t1)

t1 = (10, 20, 30, 40)
a, b, c, d = t1
print(a)
print(b)
print(c)
print(d)

print(len(t1))
print(max(t1))
print(min(t1))
print(t1.index(20))
print(t1.count(20))

t1 = tuple(l1)
print(t1)
# print(l1)
# print(l1[2: 10:2])
# print(l1[::3])
# print(l1[:6:3])
# print(l1[::-1])
