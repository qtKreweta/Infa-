def babelkowe(lista):
    n=len(lista)
    for i in range(n):
        for j in range(n-i-1):
            if len(lista[j])>len(lista[j+1]):
                lista[j], lista[j+1]=lista[j+1], lista[j]
    return lista
lista=[]
for i in range(15):
    wyraz=input("podaj wyraz:")
    lista.append(wyraz)
posortowana=babelkowe(lista)
print("posortowana lista:",posortowana)
