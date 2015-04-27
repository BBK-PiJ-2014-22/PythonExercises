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
    for i in range(len(word)//2):
        if word[i] != word[-1-i]:
            return False
    return True
        


print(charCount("thing","t"))
