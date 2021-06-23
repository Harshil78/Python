x=[]
vowel=0
con=0
dt=0
sc=0
n=int(input("Enter Number That You Want to Insert In Array:-"))
for i in range(1,n+1):
    x.append(input("Enter Array Value:-"))


for i in range(len(x)):
    if x[i] in ("a","e","i","o","u"):
        vowel=vowel+1
    elif x[i]>='0' and x[i]<='9':
        dt=dt+1
    elif x[i]>='a' and x[i]<='z':
        con=con+1
    else:
        sc=sc+1
print("========================================")
print("List:-", x)
print("Length Of List:-", len(x))
print("Total Number Of Vowels Are :-",vowel)
print("Total Number Of consonants Are :-",con)
print("Total Number Of Digits Are :-",dt)
print("Total Number Of Special Characters Are :-",sc)
print("========================================")
