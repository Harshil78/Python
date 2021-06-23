x=[]

oddsum=0
evensum=0

n=int(input("Enter Number That You Want to Insert In Array:-"))
for i in range(1,n+1):
    x.append(int(input("Enter Array Value:-")))
high = x[0]
low = x[0]
totalsum = x[0]
for i in range(1,len(x)):
    if high<x[i]:
        high=x[i]
    if low>x[i]:
        low=x[i]
for i in range(len(x)):
    if x[i]%2==0:
        evensum+=x[i]
    else:
        oddsum+=x[i]
    totalsum = oddsum+evensum
print("===========================================")
print(x)
print("Total Number In List:-", len(x))
print("Sum Of Total Number Of List:-", totalsum)
print("Average Of Total Number Of List:-", totalsum/len(x))
print("Total Even Number Sum:-", evensum)
print("Total Odd Number Sum:-", oddsum)
print("Largest Number In List:-", high)
print("Smallest Number In List:-", low)
print("===========================================")