x = []
n=int(input("Enter Value Of N:-"))
try:
    for i in range(0,n):
        x.append(input("Enter Value In List:- "))
    f1=open("E:/PythonFile/integer.txt","w")
    f2=open("E:/PythonFile/float.txt","w")
    f3=open("E:/PythonFile/string.txt","w")
    input_list = x
    for i in input_list:
        value = None
        try:
            value = int(i)
        except ValueError:
            try:
                value = float(i)
            except ValueError:
                f3.write(str(i)+",")
            else:
                f2.write(str(value)+",")
        else:
            f1.write(str(value) + ",")
    f1.close()
    f2.close()
    f3.close()
    f1 = open("E:/PythonFile/integer.txt", "r")
    print(f1.readline())
    f2 = open("E:/PythonFile/float.txt", "r")
    print(f2.readline())
    f3 = open("E:/PythonFile/string.txt", "r")
    print(f3.readline())
    f1.close()
    f2.close()
    f3.close()
except Exception as e:
    print(e)