def babelkowe(lista):
    n=len(lista)
    for i in range(n):
        for j in range(n-i-1):
            if lista[j]<lista[j+1]:
                lista[j], lista[j+1]=lista[j+1], lista[j]
    return lista
lista=[]
for i in range(10):
    liczba=int(input("podaj liczbe:"))
    lista.append(liczba)
posortowana=babelkowe(lista)
print("posortowana lista:",posortowana)
