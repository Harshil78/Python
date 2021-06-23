str1 = input("enter any string::")
i = 0
j = -1
while i < len(str1):
    if str1[i] != str1[j]:
        print("String not palindrome")
        break
    i += 1
    j -= 1
else:
    print("String is palindrome")
