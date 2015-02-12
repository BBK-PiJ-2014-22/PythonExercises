def removeWordByLetter(sentence, letter):
    tokenlist = tokenise(sentence)
    print(tokenlist)
    tokenlist = removeTokensByLetter(tokenlist, letter)
    return concatenate(tokenlist)


def tokenise(sentence):
    token = ""

    tokenList = []
    for i in sentence:
        if i != " ":
            token += i
        else:
            tokenList.append(token)
            token = ""
    tokenList.append(token)
    print(tokenList)
    return tokenList

def removeTokensByLetter(tokenList, letter):

    removeList = []
    
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

    return tokenList

def concatenate(tokenList):
    result = ""
    for l in tokenList:
        result += l + " "
    return result


print(removeWordByLetter("What a turd", "a"))
