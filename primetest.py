def prime(n):
    for i in range(2, n):
        if n % i == 0:
            print("No not prime")
            break
        else:
            print("No is prime")
            break


prime(4)
