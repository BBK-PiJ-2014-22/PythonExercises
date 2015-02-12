def removeWordByLetter(sentence, letter):
    tokenList = []
    removeList = []
    token = ""
    result = ""

    for i in sentence:
        if i != " ":
            token += i
        else:
            tokenList.append(token)
            token = ""

    tokenList.append(token)
    
    for j in range(0,len(tokenList)):
        contains = False
        for k in tokenList[j]:
            if k == letter:
               contains = True
        if contains:
            removeList.append(j)

    for p in range(0, len(removeList)):
        index = removeList[-1-p]
        tokenList.pop(index)


    for l in tokenList:
        result += l + " "

    return result

print(removeWordByLetter("what a turd",'u'))
print(removeWordByLetter("what a tard",'a'))
print(removeWordByLetter("what a turd",'q'))
