def charCount(word, letter):
    word = word.lower()
    letter = letter.lower()

    count = 0
    if len(word) < 1:
        return 0
    if word[0] == letter:
        count = 1
    if len(word) == 1:
        return count
    return  count + charCount(word[1:], letter)
        

def isPalindrome(word):
    word = word.lower()

    if len(word) <= 1:
        return True
    elif word[0] == word[-1]:
        return isPalindrome(word[1:-1])
    return False
