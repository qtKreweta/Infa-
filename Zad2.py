def sprawdzaniebinarne(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False

A = [1, 3, 5, 7, 9, 11]
x = int(input("Podaj liczbę: "))

if sprawdzaniebinarne(A, x):
    print("Znajduje się")
else:
    print("Nie znajduje się")
