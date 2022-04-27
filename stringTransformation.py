def transformSentence(sentence):
    first = sentence[0]

    for i in range(1, len(sentence)):
        if sentence[i] != ' ':
            if ord(sentence[i+1]) < ord(sentence[i]):
                sentence[i].upper()
            elif ord(sentence[i+1]) > ord(sentence[i]):
                sentence[i].upper()
            
    return sentence





n = ord('') 

print(n)

sentence = "coOL dog"



# print(transformSentence(sentence))