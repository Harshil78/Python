class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, data):
        self.items.append(data)

    def display(self):
        print(self.items)

    def dequeue(self):
        return self.items.pop(0)


q = Queue()
while True:
    print()
    print("Enter your choice as per given -")
    print("1 = For insert data In Queue press 1 ")
    print("2 = For delete data Form Queue press 2 ")
    print("3 = For Display Data of Queue press 3 ")

    print("0 = For Exit enter 0 ")
    print()
    operation = input("Enter your choice :- ")
    if operation == '1':
        data = int(input("Enter your Data :- "))
        q.enqueue(data)
    elif operation == '2':
        if q.is_empty():
            print('Queue is empty.')
        else:
            print('Delete queued value: ', q.dequeue())
    elif operation == '3':
        if q.is_empty():
            print('queue is empty.')
        else:
            q.display()
    elif operation == '0':
        break