#This was an early version of the last exercise
#The original exercises used a Word custom object that held a vale
#The functions written were then methods on the word. This proved
#far more cumbersome, so I dropped it in favour of functions

class Word:

    def __init__(self, string):
        self.value = string

    def charCount(self, char):
        length = len(self.value)
        n = 0
        count = 0

        while n < length:
            if self.value[n] == char:
                count += 1
            n += 1
            
        return count

    def isPalindrome(self):
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



