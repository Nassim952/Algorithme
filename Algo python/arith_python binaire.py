nombre=int(input("Saisissez un nombre afin de le convertir en binaire: "))
quotient = nombre
resultat = ''
while nombre!=0:
    if quotient>=64:
        quotient=nombre//2
        reste=nombre%2
        resultat = resultat+str(reste)
        nombre=quotient
    elif quotient>=32:
        quotient=nombre//2
        reste=nombre%2
        resultat = resultat+str(reste)
        nombre=quotient
    elif quotient>=16:
        quotient=nombre//2
        reste=nombre%2
        resultat = resultat+str(reste)
        nombre=quotient
    elif quotient>=8:
        quotient=nombre//2
        reste=nombre%2
        resultat = resultat+str(reste)
        nombre=quotient
    elif quotient>=4:
        quotient=nombre//2
        reste=nombre%2
        resultat = resultat+str(reste)
        nombre=quotient
    elif quotient>=2:
        quotient=nombre//2
        reste=nombre%2
        resultat = resultat+str(reste)
        nombre=quotient
    elif quotient>=1:
        quotient=nombre//2
        reste=nombre%2
        resultat = resultat+str(reste)
        nombre=quotient
        
res = ''
for i in range(len(resultat)-1, -1, -1):
    res += resultat[i]
 
print("\nLe nombre", res,"en base 10 équivaut à la suite de 0 et de 1 en bibaire.")
