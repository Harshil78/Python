class OptOvrld:
    def __init__(self, name):
        self.name = name
        self.sum2 = 0
        self.i = 0
        self.ans = ""
        self.sum = 0

    def __add__(self, temp):
        while (self.i < len(self.name) or self.i < len(temp.name)):
            if (self.i < len(self.name)):
                self.ans += self.name[self.i]
            if (self.i < len(temp.name)):
                self.ans += temp.name[self.i]
            self.i = self.i + 1
        return self.ans

    def con1(self):
        self.i = 0
        while self.i < len(self.name):
            self.sum = self.sum + ord(self.name[self.i])
            self.i = self.i + 1
        return self.sum

    def con2(self, temp):
        self.i = 0
        while self.i < len(temp.name):
            self.sum2 = self.sum2 + ord(temp.name[self.i])
            self.i = self.i + 1
        return self.sum2

    def __eq__(self, temp):
        if (self.con1() == self.con2(temp)):
            return True
        else:
            return False

    def __lt__(self, temp):
        if (self.con1() < self.con2(temp)):
            return True
        else:
            return False

    def __le__(self, temp):
        if (self.con1() <= self.con2(temp)):
            return True
        else:
            return False

    def __gt__(self, temp):
        if (self.con1() > self.con2(temp)):
            return True
        else:
            return False

    def __ge__(self, temp):
        if (self.con1() >= self.con2(temp)):
            return True
        else:
            return False


while True:
    print("*" * 30)
    str1 = input("Enter the String 1:")
    str2 = input("Enter the String 2:")
    obj1 = OptOvrld(str1)
    obj2 = OptOvrld(str2)
    print(f'Concate String : {obj1 + obj2}')
    if (obj1 == obj2):
        print(f'{str1} and {str2} are same')

    if (obj1 < obj2):
        print(f'{str1} is less than {str2}')

    if (obj1 > obj2):
        print(f'{str1} is greater than {str2}')

    if (obj1 <= obj2):
        print(f'{str1} is less than or Equal To {str2}')

    if (obj1 >= obj2):
        print(f'{str1} is greater than or Equal To {str2}')

    ch = input("Do you want to contious ? Y-Yes /N-No : ")
    if (ch.upper() == "N"):
        break
    elif (ch.upper() == "Y"):
        continue


