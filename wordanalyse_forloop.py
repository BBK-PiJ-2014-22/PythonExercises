def charCount(word, char):
    '''Counts the number of times a character appears. Not case sensitive'''
    char = char.lower()
    count = 0

    for i in word.lower():
        if i == char:
            count += 1
    return count
            
   

def isPalindrome(word):
    '''Returns True if word is palindrome, false otherwise. Not case sensitive'''
    if len(word)<= 1:
        return True

    word = word.lower()
    letter = 0
    while letter < len(word)/2:
        if word[letter] != word[-1-letter]:
            return False
        letter += 1
    
    #Other code goes here



