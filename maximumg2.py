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
    

addOne(2)
addOne(1)


