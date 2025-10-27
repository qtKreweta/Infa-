def liczba(n):
    if n == 1:
        return 1
    return liczba(n - 1) + 2 * n - 1
  
n = int(input("Podaj n: "))
print(f"Liczba to {liczba(n)}")

