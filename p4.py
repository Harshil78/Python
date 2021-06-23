evenSum=0
oddSum=0
totalsum=0
while True:
    try:
        n = int(input("enter N::"))
        if n <= 0:
             print("Please Enter Positive Value")
        else:
            for i in range(1,n+1):
                if i%2==0:
                    evenSum+=i
                else:
                    oddSum+=i
                totalsum+=i
            print("=======================================")
            print("Total Even Number Sum=", evenSum)
            print("Total Odd Number Sum=", oddSum)
            print("Total Odd And Even Number Sum=", totalsum)
            print("=========================================")
            break
    except Exception as e:
        print(e)