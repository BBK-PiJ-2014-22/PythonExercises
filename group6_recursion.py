def charCount(word,letter):
    word = word.lower()
    letter = letter.lower()
    if len(word) == 0:
        return 0
    else:
        if word[len(word)-1] == letter:
            return 1  + charCount(word[0:-1], letter)
        else:
            return charCount(word[0:-1], letter)
   


def isPalindrome(word):
    word = word.lower()
    if len(word) < 2:
        return True
    if word[0] == word[-1]:
        if isPalindrome(word[1:-1]):
            return True
        else:
            return False
    else:
        return False
