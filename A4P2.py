n=int(input("Enter Number Of Line That You Want To Inserted In File:-"))
f=open("E:/PythonFile/Prog-2.txt", "a")
for i in range(n):
    print("Enter Line:-", i + 1)
    l=input("Enter Sentence:-")
    f.write(str(l) + "\n")
f.close()
f=open("E:/PythonFile/Prog-2.txt", "r")
print(f.readline())
f.seek(0)
print(f.readlines())
f.seek(0)
print("Consider 0 As First Line")
n=int(input("Enter Starting Line Number :-"))
m=int(input("Enter Ending Line Number :-"))
print(f.readlines()[n:n+m])
f.seek(0)
con=f.readlines()
for s in con:
    print("\n")
    print("Line-", s,"Number Words :-",len(s.split()))
f.close()