def charCount(word,letter):
    word = word.lower()
    letter = letter.lower()
    count = 0
    for i in word:
        if i == letter:
            count += 1
    return count



def isPalindrome(word):
    word = word.lower()
    i = 0
    while i  < len(word):
        if word[i] != word[-1-i]:
            return False
        else:
            i += 1
    return True
