def charCount(word,letter):
    word = word.lower()
    letter = letter.lower()
    modifier = 0
    if len(word) == 0:
        return 0
    if word[0] == letter:
        modifier = 1
    return modifier + charCount(word[1:], letter)
            
    
   
def isPalindrome(word):
    word = word.lower()
    if len(word) <= 1:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return isPalindrome(word[1:-1])
               

        
