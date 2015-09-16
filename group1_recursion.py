class Word:

    def __init__(self, string):
        '''Creates a word object with string as it's value'''
        self.value = string

    def charCount(self, char):
        '''Counts the number of times a character appears. Not case sensitive'''
        word = self.value.lower()
        char = char.lower()
        firstMatch = 0

        if len(word) == 0:
            return 0
        elif word[0] == char:
            firstMatch = 1

        if len(word) == 1:
            return firstMatch
        else:
            return firstMatch + Word(word[1:]).charCount(char)
            
   

    def isPalindrome(self):
        '''Returns True if word is palindrome, false otherwise. Not case sensitive'''
        word = self.value.lower()
            
        if len(word) <= 1:
           return True
        elif word[0] != word[-1]:
            return False
        else:
            return Word(word[1:-1]).isPalindrome()
                        


    #Other code goes here



