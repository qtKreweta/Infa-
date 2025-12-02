def quicksort_len(tab, lewy, prawy):
    i = lewy
    j = prawy
    pivot = len(tab[(lewy + prawy) // 2])
    while i <= j:
        while len(tab[i]) < pivot:
            i += 1
        while len(tab[j]) > pivot:
            j -= 1
        if i <= j:
            tab[i], tab[j] = tab[j], tab[i]
            i += 1
            j -= 1
    if lewy < j:
        quicksort_len(tab, lewy, j)
    if i < prawy:
        quicksort_len(tab, i, prawy)
n = int(input("Podaj liczbe napisów: "))
d = [input(f"Napis {i+1}: ") for i in range(n)]
quicksort_len(d, 0, n - 1) 
print("\nPosortowane napisy wg długości:")
print(d)

