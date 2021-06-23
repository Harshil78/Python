try:
    x = []
    while True:
        a = input('Please enter an integer (0 to exit):-')
        a = int(a)
        if a!=0:
            x.append(a)
        else:
            break
    odd = []
    even = []
    for a in x:
        if a%2==0:
            even.append(a)
        else:
            odd.append(a)
    print("Odd Number List :-",odd)
    print("Even Number List :-",even)
except Exception as e:
    print(e)
