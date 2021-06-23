english_to_dutch={"last" : "laatst", "week" : "week", "the" : "de", "royal" : "koninklijk",
"festival" : "feest", "hall" : "hal", "saw" : "zaag", "first" : "eerst", "performance" : "optreden",
"of" : "van", "a" : "een", "new" : "nieuw", "symphony" : "symphonie", "by" : "bij", "one" : "een",
"world" : "wereld", "leading" : "leidend", "modern" : "modern", "composer" : "componist",
"composers" : "componisten", "two" : "twee", "shed" : "schuur", "sheds" : "schuren"}


Sentence=input("Enter Sentence which you want to Convert into dutch:")
dutch_Sentence=""
words = list(Sentence.split(' '))
for word in words:
    word = word.lower()
    if word in english_to_dutch.keys():
        dutch_Sentence = dutch_Sentence + english_to_dutch[word] + ' '
    else:
        dutch_Sentence = dutch_Sentence + word + ' '
print('English Sentence Is :',Sentence)
print('English To Dutch Convert Sentence Is :',dutch_Sentence)