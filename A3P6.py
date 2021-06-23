s=input("Enter String :-")
l=list(s)
Dict={}
for i in l:
    if i not in Dict.keys():
        Dict[i]=1
    else:
        Dict[i]+=1
print(Dict)