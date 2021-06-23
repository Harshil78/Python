try:
    x = []
    while True:
        a = input('Please enter an integer (0 to exit):-')

        if a!="0":
            f = open("E:/PythonFile/Velcy.txt", "a+")
            f.write(a+",")
            f.close()
        else:
            break

    f = open("E:/Velcy.txt", "r")
    print(f.read())

except Exception as e:
    print(e)