def charCount(word, letter):

    word = word.lower()
    letter = letter.lower()
    
    count = 0
    for i in word:
        if i == letter:
            count += 1
    return count

def isPalindrome(word):
    word = word.lower()
    reverse = ""

    for i in range(len(word)):
        reverse += word[-1-i]

    if word == reverse:
        return True
    else:
        return False

