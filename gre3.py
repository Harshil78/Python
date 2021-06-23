x=int(input("Enter X::"))
y=int(input("Enter Y::"))
z=int(input("Enter Z::"))
if x>y and x>z :
    print("x is Greater")
elif y>x and y>z:
    print("y is Greater")
elif z>x and z>y :
    print("Z is Greater")
else :
    print("two or more values are equal")
print(type(x))    
