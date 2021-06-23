class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peep(self,search):
       if search in self.items:
           print("Found Value :-",search)
       else:
           print("Not Fount Value")


    def display(self):
        print(self.items)

s = Stack()
while True:
    print()
    print("Enter your choise as per given -")
    print("1 = For insert data Enter 1 ")
    print("2 = For delete data enter 2 ")
    print("3 = For Print data enter 3 ")
    print("4 = For Peep data enter 4 ")
    print("0 = For Exit enter 0 ")
    print()
    operation = input("Enter your choice :- ")
    if operation == '1':
        data=int(input("Enter your Data :- "))
        s.push(data)
    elif operation == '2':
        if s.is_empty():
            print('Stack is empty.')
        else:
            print('Popped value: ', s.pop())
    elif operation == '3':
        if s.is_empty():
            print('Stack is empty.')
        else:
            s.display()
    elif operation == '4':
        if s.is_empty():
            print('Stack is empty.')
        else:
            search=int(input("Enter Search Element:-"))
            s.peep(search)
    elif operation == '0':
        break