teachers = {"Harshil": "Python", "velcy": ".VB", "Mann": "Java"}
print(teachers['Harshil'])  # call by key
print(teachers['velcy'])
for key in teachers:
    print(key, " ", teachers[key])

print(teachers.keys())
print(teachers.values())

teachers['Mann'] = 'PHP'
print(teachers)
teachers['Harsh'] = 'C++'
print(teachers)
teachers['Abhi'] = 'OOP'
print(teachers)
del teachers['Abhi']
print(teachers)

teachers.pop('Harsh')
print(teachers)

teachers.pop('Abhi', print("harkhu nakh topa"))
print(teachers.pop('Abhi', "harkhu nakh topa"))

print("Harshil" in teachers)
print("Harshil" not in teachers)
print("Python" in teachers.values())

print(len(teachers))
print(teachers.get('Abhi', "pachhu jo"))

teachers.clear()
print(teachers)

h1 = {"Harshil": "Python", "velcy": ".VB", "Mann": "Java"}
h2 = {"Harshil": "Python", "velcy": "Php", "Dhruv": "Oop"}

print(h1, h2)
h1.update(h2)
print(h1)
