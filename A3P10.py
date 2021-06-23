movie={}
rateav=0
movies =["Where Eagle’s Dare", "Enter the Dragon", "Iron Fist", "Fist of Fury"]
dareratings = [ 9, 10, 9.5, 8.5, 3, 7.5, 8]
dragonratings = [ 10, 10, 0, 9, 1, 8, 7.5, 8, 6, 9 ]
fistratings = [ 7, 6, 5 ]
furyratings = [ 6, 5, 6, 6 ]
for i in movies:
    if i=="Where Eagle’s Dare":
        movie[i]=dareratings
    elif i=="Enter the Dragon":
        movie[i]=dragonratings
    elif i=="Iron Fist":
        movie[i]=fistratings
    elif i=="Fist of Fury":
        movie[i]=furyratings
for i in movie:
    rate=0
    n=0
    for j in movie[i]:
        rate=rate+j
        n=n+1
    rateav=round(rate/n,1)
    print('Average ratings of the movie "',i,'" is :-' , rateav)