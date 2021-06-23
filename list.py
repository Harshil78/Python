l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(l1[2: 6:2])
print(l1[::3])
print(l1[:6:3])
print(l1[::-1])

l1[0:2] = [11, 12]
print(l1)
l1[50:70] = [17, 18, 19, 15]
print(l1)
l1[50:70] = 'Harshil'
print(l1)
l1.append('dalal')
print(l1)
del l1[2:5]
print(l1)
l1.pop()
print(l1)
l1.pop(0)
print(l1)
l1.pop(2)
print(l1)

print(l1.index(80))
l1.append([10, 20])
print(l1)
l1.extend([10, 20])
print(l1)
print(l1.count(90))
print(len(l1))

l1.reverse()
print(l1)
l2 = [10, 50, 60, 80, 5, 110]
l2.sort()
print(l2)
l2.sort(reverse=True)
print(l2)
