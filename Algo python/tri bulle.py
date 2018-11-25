from random import*
n=int(input("nombre d'élément à trier"))
liste_initiale = [randrange(1,100) for i in range (n)]
print("liste a trier:", liste_initiale)

for k in range (n-1,0,-1):
    m = max(liste_initiale[:k+1])
    i = liste_initiale.index(m)
    if(liste_initiale[i] > liste_initiale[k]):
        liste_initiale[k], liste_initiale[i] = liste_initiale[i], liste_initiale[k]

print("liste finale:", liste_initiale)
                
