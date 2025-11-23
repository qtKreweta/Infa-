n = int(input("Podaj liczbę elementów: "))

lista = []
for _ in range(n):
    lista.append(int(input("Podaj liczbę: ")))

def sortowanie_przez_wstawianie(lista):
    for i in range(1, len(lista)):
        pom = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > pom:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = pom

sortowanie_przez_wstawianie(lista)
print("Posortowana lista:", lista)

