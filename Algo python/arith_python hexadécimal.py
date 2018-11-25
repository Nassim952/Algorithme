n=int(input("Saisissez un nombre binaire afin de le convertir en hexadecimal"))
alph, hex = 'ABCDEF', ''
k=0

while n:
    if n%16 >= 10:
        hex = alph[(n%16)%10] + hex
    else:
        hex = str(n%16)+hex
    n = n//16
print("Le nombre est :", hex)     
