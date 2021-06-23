words_Dict={}
while 1:
    List = input('Enter String (Enter 0 For Exit) :')
    if List == '0':
        break
    else:
        List = List.lower()
        word_List=List.split(',');
        for word in word_List:
            if word in words_Dict:
                words_Dict[word] += 1
            else:
                words_Dict[word] = 1
print(words_Dict)