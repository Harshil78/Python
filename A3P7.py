x = []
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
    print(Dict)
except Exception as e:
    print(e)