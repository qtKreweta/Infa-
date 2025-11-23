n = int(input("Podaj liczbę elementów: "))
tab = []
def selection_sort_numbers(tab):
    size = len(tab)
    for i in range(size):
        pmin = i
        for j in range(i + 1, size):
            if tab[j] < tab[pmin]:
                pmin = j
        tab[i], tab[pmin] = tab[pmin], tab[i]


print("Podaj", n, "liczb:")
for _ in range(n):
    tab.append(int(input()))

selection_sort_numbers(tab)

print("Posortowany ciąg:", tab)


