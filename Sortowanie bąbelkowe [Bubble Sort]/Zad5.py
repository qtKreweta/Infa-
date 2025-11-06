lista = [123, 'ala', 'kotek', 23, 'si', 34565, 'dom', 1, 'kot', 999, 'a']
liczby = []
wyrazy = []
for el in lista:
    if type(el) == int:
        liczby.append(el)
    elif type(el) == str:
        wyrazy.append(el)
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
liczby = bubble_sort(liczby)
wyrazy = bubble_sort(wyrazy)
print("Liczby po sortowaniu:", liczby)
print("Wyrazy po sortowaniu:", wyrazy)
nowy_ciag = []
for slowo in wyrazy:
    for liczba in liczby:
        if len(slowo) == len(str(liczba)):
            nowy_ciag.append(slowo + str(liczba))
print("Nowy ciąg:", nowy_ciag)

