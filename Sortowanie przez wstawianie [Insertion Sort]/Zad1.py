lista = []
for _ in range(n):
    lista.append(int(input("Podaj liczbę: ")))
n = int(input("Podaj liczbę elementów: "))
def sortowanie_przez_wstawianie(lista, n):
    for i in range(1, n):
        pom = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > pom:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = pom

sortowanie_przez_wstawianie(lista, n)

print("Posortowana lista:", lista)

