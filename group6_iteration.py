def charCount(word,letter):
    word = word.upper()
    letter = letter.upper()
    count = 0
    for i in range(len(word)):
        if word[i] == letter:
            count += 1
    return count
   


def isPalindrome(word):
    word = word.upper()
    times = int(len(word)/2)
    start = 0
    end = -1
    for i in range(times):
        if word[start] == word[end]:
            start += 1
            end -= 1
        else:
            return False
    return True


        
