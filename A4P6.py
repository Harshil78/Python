x = []
f1 = open("E:/PythonFile/A4P6.txt", "w")
n=int(input("Enter Value Of N:-"))
try:
    for i in range(0,n):
        x.append(input("Enter Value In List:- "))
    l=list(x)
    Dict={}
    for i in l:
        if i not in Dict.keys():
            Dict[i]=1
        else:
            Dict[i]+=1
    f1.write(str(Dict) + "\n")
    f1.close()
    f1=open("E:/PythonFile/A4P6.txt", "r")
    print(f1.readline())
except Exception as e:
    print(e)