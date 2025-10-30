def suma_cyfr(liczba):
    return sum(int(c) for c in str(liczba))

def max_suma_cyfr(tab):
    max_liczba = tab[0]
    max_suma = suma_cyfr(tab[0])

    for x in tab:
        s = suma_cyfr(x)
        if s > max_suma:
            max_suma = s
            max_liczba = x

    return max_liczba, max_suma

tab = [123, 999, 50505, 6789, 870]
liczba, suma = max_suma_cyfr(tab)

print("Liczba o największej sumie cyfr:", liczba)
print("Suma jej cyfr:", suma)
