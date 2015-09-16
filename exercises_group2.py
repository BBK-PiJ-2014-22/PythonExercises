def maximum(number1, number2):
    if number1 > number2:
        return number1
    else:
        return number2

def maxdouble(number1, number2):
    return 2*maximum(number1, number2)

def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False

def addOne(number):
    print(number+1)

class Pair:

    def __init__(self, value, pair=None):
        self.value = value
        self.pair = pair

    def link(self, newpair):
        '''Links to pairs together

           OTHER INFORMATION

           '''
        self.pair = newpair
        newpair.pair = self
        #Asigns pair to self.pair and vice ersa



    

addOne(2)
addOne(1)


a = Pair(14)
b = Pair(12)

a.link(b)

print(a.pair.value)
