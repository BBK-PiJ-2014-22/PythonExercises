#JM - most classes did not do the Dancer exercise due to time constraints
class Dancer:
    '''Put in tdocstring here'''

    def __init__(self, name, other = None):
        self.name = name
        self.partner = other    
        if other != None:
            other.partner = self

    def pair(self, other):
        '''Pairs two dancers together if they have no partner'''
        if other.partner == None:
            self.partner = other
            other.partner = self
            return True
        else:
            return False

    def dance(self):
        if self.partner == None:
            print(self.name,"dances on their own")
        else:
            print(self.name,"dances with", self.partner.name)

#These are the iterative solutions
def charCount(string, letter):
    string = string.lower()
    letter = letter.lower()
    count = 0
    for i in string:
        if i == letter:
            count += 1
    return count

def isPalindrome(string):
    string = string.lower()
    n = 0
    if len(string) == 0:
        return True
    while n <= len(string)//2:
        if string[n] != string[-1-n]:
            return False
        n += 1
    return True
        
