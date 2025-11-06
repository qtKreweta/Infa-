lista = ["ola","maciek","polak","super","jurek","marek","pociag","aszfaganda","aleksander","krokodyl","franciszkanin","manekin","porosty","prostak","niziolek"]
def bambl(lista):
     n = len(lista)
     for i in range(n):
         for j in range(n-i-1):
             if lista[j]<lista[j+1]:
                 lista[j],lista[j+1]=lista[j+1],lista[j]
     return lista
print(bambl(lista))
