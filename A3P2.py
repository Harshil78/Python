
my_list=[]
temp_list=[]
cnum=[]
c=0
n=int(input('Enter the size of list:- '))

try:
    for i in range(n):
        for j in range(0,10000):
            a = input('Please enter an integer (0 to exit):-')
            a = int(a)
            if a!=0:
                temp_list.append(a)

            else:
                c=0
                break
        c=len(temp_list)
        cnum.append(c)
        my_list.append(temp_list)
        temp_list=[]  #set temp_list to null

    print("Nested List:-",my_list)
    print("Count Of Each Nested List:-",cnum)
except Exception as e:
    print(e)