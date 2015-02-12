class Word:

    def __init__(self, string):
        '''Creates a word object with string as it's value'''
        self.value = string

    def charCount(self, char):
        '''Counts the number of times a character appears. Not case sensitive'''
        length = len(self.value)
        n = 0
        count = 0

        while n < length:
            if self.value[n] == char:
                count += 1
            n += 1
            
        return count

    def isPalindrome(self):
        '''Returns True if word is palindrome, false otherwise. Not case sensitive'''
        iterations = len(self.value)/2
        n = 0

        if len(self.value) == 0:
            return False

        while n <= iterations:
            counter = (n+1) * -1
            if self.value[n] != self.value[counter]:
                return False
            n += 1

        return True


        



    #Other code goes here



