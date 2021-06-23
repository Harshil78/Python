try:
    x = []
    while True:
        a = input('Please enter an integer (0 to exit):-')
        a = int(a)
        if a!=0:
            x.append(a)
        else:
            break
    dup_items = []
    uniq_items = []
    for a in x:
        if a not in dup_items:
            uniq_items.append(a)
            dup_items.append(a)
    print("Original List:-",x)
    print("After Delete Duplicate List Value :-", dup_items)
except Exception as e:
    print(e)
