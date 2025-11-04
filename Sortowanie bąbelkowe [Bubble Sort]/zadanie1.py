lista =[2,1,3,5,4,6,8,7,9,11,10,13,12,15,14,17,16,18,19,20]
def babelkowe(lista):
    n=len(lista)
    for i in range(n):
        for j in range(n-i-1):
            if lista[j]>lista[j+1]:
                lista[j], lista[j+1]=lista[j+1], lista[j]
    return lista
posortowana=babelkowe(lista)
print("posortowana lista:",posortowana)
