lista = []
n = int(input("Podaj liczbę wyrazów: "))
def sortowanie_tekstow_po_dlugosci(lista, n):
    for i in range(1, n):
        pom = lista[i]
        j = i - 1
        while j >= 0 and len(lista[j]) > len(pom):
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = pom

for _ in range(n):
    lista.append(input("Podaj wyraz: "))

sortowanie_tekstow_po_dlugosci(lista, n)

print("Posortowana lista wg długości:", lista)
