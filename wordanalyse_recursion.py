def charCount(word, char):
    '''Counts the number of times a character appears. Not case sensitive'''
    word = word.lower()
    char = char.lower()
    firstMatch = 0

    if len(word) == 0:
        return 0
    elif word[0] == char:
        firstMatch = 1

    if len(word) == 1:
        return firstMatch
    else:
        return firstMatch + charCount(word[1:],char)
            
   

def isPalindrome(word):
    '''Returns True if word is palindrome, false otherwise. Not case sensitive'''
    word = word.lower()
        
    if len(word) <= 1:
       return True
    elif word[0] != word[-1]:
        return False
    else:
        return isPalindrome(word[1:-1])
                    


    #Other code goes here



