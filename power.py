def power(number,indice):
    if indice == 1:
        return number
    else:
        return number*power(number,indice-1)

print(power(5,-2))
