n = int(input("Enter number of students: "))
f1 = open("E:/PythonFile/stud.txt", "a")
result = []
for i in range(n):
    print("Enter Details of student No.", i+1)
    rno = int(input("Roll No :- "))
    m1 = int(input("Marks 1 :- "))
    m2 = int(input("Marks 2 :- "))
    m3 = int(input("Marks 3 :- "))
    total=m1+m2+m3
    result = [rno,m1,m2,m3,total]
    f1.write(str(result)+"\n")
f1.close()
f1 = open("E:/PythonFile/stud.txt", "r")
con=f1.readlines()
print(" RollNo.    Mark1   Mark2   Mark3   Total")
for s in con:
    s=s.replace("[","").replace("]","")
    stud=s.split(",")
    total=int(stud[1].strip())+int(stud[2].strip())+int(stud[3].strip())
    print(" {:^6}     {:^5}   {:^5}   {:^5}   {:^5}".format(stud[0].strip(),stud[1].strip(),stud[2].strip(),stud[3].strip(),total))
f1.close()