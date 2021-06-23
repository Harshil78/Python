# from goto import goto, label
# label .start
# n = int(input("enter N::"))
# i = 2
# if n<=0:
#     goto .start
# else:
#     while i <= n/2:
#         if n % i == 0:
#             print("no is not prime")
#             break
#         else :
#             i+=1
#     else:
#         print("No is  Prime")

while True:
    try:
        n = int(input("enter N::"))
        i = 2
        if n <= 0:
             print("Please Enter Positive Value")
        else:
            while i <= n / 2:
                if n % i == 0:
                    print("no is not prime")
                    break
                else :
                    i+=1

            else:
                print("No is  Prime")
            break
    except Exception as e:
        print(e)
