class person:
    cnt = 0

    def __init__(self, fname, lname):
        self.__firstname = fname
        self.lastname = lname
        person.cnt += 1

    def disp(self):
        print("Name=", self.firstname, self.lastname)


class student(person):
    def __init__(self, fname, lname, per):
        person.__init__(self, fname, lname)
        self.percantage = per

    def display(self):
        person.disp(self)
        print("Percantage=", self.percantage, person.cnt)


s = student("Harshil", "Dalal", 80.0)
s1 = student("Velcy", "Shah", 70.0)
s.display()
s1.display()
s1.firstname = "Mehul"
s1.display()
print(issubclass(person, object))
print(issubclass(student, object))
print(issubclass(student, person))
print(issubclass(person, student))
print(isinstance(5, person))
print(isinstance(5, object))
print(isinstance("PCC", object))
print(isinstance(s, object))
