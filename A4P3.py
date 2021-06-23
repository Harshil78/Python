try:
    x = []
    while True:
        a = input('Please enter an integer (0 to exit):-')
        a = int(a)
        if a!=0:
            x.append(a)
        else:
            break
    for a in x:
        if a%2==0:
            e = open("E:/PythonFile/Even.txt", "a+")
            e.write(str(a))
            e.write(",")
            e.close()
        else:
            f = open("E:/PythonFile/Odd.txt", "a+")
            f.write(str(a))
            f.write(",")
            f.close()
    print("List:-",x)
    e = open("E:/PythonFile/Even.txt", "r")
    print("Even Number File:-",e.read())
    f = open("E:/PythonFile/Odd.txt", "r")
    print("Odd Number File:-",f.read())
except Exception as e:
    print(e)


