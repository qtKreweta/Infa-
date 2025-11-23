n = int(input("Podaj liczbę wyrazów: "))
words = []
def selection_sort_by_length(tab):
    size = len(tab)
    for i in range(size):
        pmin = i
        for j in range(i + 1, size):
            if len(tab[j]) < len(tab[pmin]):
                pmin = j
        tab[i], tab[pmin] = tab[pmin], tab[i]

print("Podaj", n, "wyrazów:")
for _ in range(n):
    words.append(input())

selection_sort_by_length(words)

print("Posortowane wyrazy:", words)

