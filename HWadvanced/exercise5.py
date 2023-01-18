def reverseWord(Sentence):
    words = Sentence.split(" ")
    newSentence = ' '.join(reversed(words))
    return ' '.join(reversed(words))

Sentence = "Python is good language to learn"
print(reverseWord(Sentence))