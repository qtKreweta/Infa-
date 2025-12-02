def szybkie_sortowanie(tab, left, right):
    i = left
    j = right
    x = tab[(left + right) // 2]
    while i <= j:
        while tab[i] < x:
            i += 1
        while tab[j] > x:
            j -= 1

        if i <= j:
            tab[i], tab[j] = tab[j], tab[i]
            i += 1
            j -= 1

    if left < j:
        szybkie_sortowanie(tab, left, j)
    if i < right:
        szybkie_sortowanie(tab, i, right)


tablica = list(map(int, input("Podaj liczby po spacji: ").split()))
szybkie_sortowanie(tablica, 0, len(tablica) - 1)
print("Lista:", tablica)

