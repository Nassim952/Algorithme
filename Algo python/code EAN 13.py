def conversion_tableau(c):
    code= 13*[0]
    for k in range(12,-1,-1):
        code[k] = c%10
        c = (c-code[k])//10
    return (code)

c=int(input("saisir l'INSEE 13"))
print(conversion_tableau(c))
