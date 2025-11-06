lista = []
for i in range(1,11):
    lista.append(int(input("Podaj lliczbę: ")))
def bambl(lista):
     n = len(lista)
     for i in range(n):
         for j in range(n-i-1):
             if lista[j]<lista[j+1]:
                 lista[j],lista[j+1]=lista[j+1],lista[j]
     return lista
print(bambl(lista))
