class Word:

    def __init__(self, string):
        '''Creates a word object with string as it's value'''
        self.value = string

    def charCount(self, char):
        '''Counts the number of times a character appears. Not case sensitive'''
        count = 0
        char = char.lower()
        
        for i in self.value.lower():
            if i == char:
                count += 1
        return count
   

    def isPalindrome(self):
        '''Returns True if word is palindrome, false otherwise. Not case sensitive'''
        word = self.value.lower()

        for i in range(len(word)//2):
            if word[i] != word[-1-i]:
                return False
        return True

        



    #Other code goes here



