def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

for i in range(2000):
    print(fibonacci(i))
