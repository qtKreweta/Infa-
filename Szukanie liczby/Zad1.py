A = [1,2,3,4,5,6,7,8,9]
def SzukajLin(A,x):
    for i in A:
        if x==i:
            return True
    return False
x = int(input("Podaj liczbę całkowitą: "))
print(SzukajLin(A,x))

