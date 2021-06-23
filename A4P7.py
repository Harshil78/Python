n=int(input("Enter Number Of Line That You Want To Inserted In File:-"))
f1=open("E:/PythonFile/Search.txt", "a")
for i in range(n):
    print("Enter Line:-", i + 1)
    l=input("Enter Sentence:-")
    f1.write(str(l) + "\n")
f1.close()
str=input("Word To Find:")
f1=open("E:/PythonFile/Search.txt", "r")
con=f1.readlines()
line=0
for s in con:
    s=s.replace("\n","").replace("\t","")
    count=0
    for f in s.split(" "):
        if(f==str):
            count+=1
    line+=1
    print("{} Found in line{}, {} Times".format(str,line,count))
f1.close()