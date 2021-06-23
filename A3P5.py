n = int(input("Enter number of students: "))
result = {}
for i in range(n):
    print("Enter Details of student No.", i+1)
    rno = int(input("Roll No :- "))
    m1 = int(input("Marks 1 :- "))
    m2 = int(input("Marks 2 :- "))
    m3 = int(input("Marks 3 :- "))
    total=m1+m2+m3

    result[rno] = [m1,m2,m3,total]
print(result)