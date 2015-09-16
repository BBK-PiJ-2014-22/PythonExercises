def minimum(number1, number2):
    '''Returns the lowest of two numbers'''
    if number1 < number2:
        return number1
    else:
        return number2

def doubleminimum(number1, number2):
    '''Returns double of the lowest of two number'''
    return minimum(number1, number2) * 2

def isEven(number):
    '''Returns if number is even'''
    if number % 2 == 0:
        return True
    else:
        return False

def isEven2(number):
    '''Returns if number is even'''
    return number % 2 == 0

def printoutntimes(string, n=2):
    print(string*n)
    
printoutntimes("str",5)
printoutntimes("str")
printoutntimes("str",n=2)
printoutntimes(string = "str",n=5)

printoutntimes(n=5, "str")
 
