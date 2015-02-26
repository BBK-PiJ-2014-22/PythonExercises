def power(number, indice):
    if indice == 1:
        return number
    else:
        return number*power(number, indice-1)

print(power(1,1))
print(power(2,2))
print(power(2,1))
print(power(2,6))
