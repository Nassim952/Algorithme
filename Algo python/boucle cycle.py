n=int(input("entrez une valeur naturel non nul avec au maximum 3 chiffres"))

u = n%10
d, c = ((n-u)/10)%10, n//100
p = u**2 + d**2 + c**2

while p!=1 or n not in liste:
    liste = [p]
    return(int(p))
if p!=1:
    print("vous êtes dans un puit")
elif n not in

    
