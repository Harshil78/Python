class person:
    "common person class"
    cnt = 0

    def __init__(self, fname, lname):
        self.__firstname = fname
        self.lastname = lname
        person.cnt += 1

    def disp(self):
        print("Name=", self.firstname, self.lastname)


class student(person):
    'common student class inheritby by person'

    def __init__(self, fname, lname, per):
        person.__init__(self, fname, lname)
        self.percantage = per

    def display(self):
        person.disp(self)
        print("Percantage=", self.percantage, person.cnt)


print("Doc", person.__doc__)
print("Name", person.__name__)
print("Module", person.__module__)
print("Bases", person.__bases__)
print("Dict", person.__dict__)

print("Doc", student.__doc__)
print("Name", student.__name__)
print("Module", student.__module__)
print("Bases", student.__bases__)
print("Dict", student.__dict__)
