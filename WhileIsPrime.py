def isPrime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2,number//2):
            if number % i == 0:
                return False
        return True
        
n = 0
while n <= 1000:
    if isPrime(n):
        print(n)
    n += 1
