from random import*
n = int(input("choisir le maximum n au max 100"))
nbHasard = randrange(1, n)
chance = 10
i = 1
while i<=10:
    i = i + 1
    choix = int(input("proposer une valeur afin de deviner le chiffre"))
    if choix > nbHasard:
        print("le nombre est plus petit!")
        chance = chance - 1;
        print("dommage c'est pas ça il vous reste,", chance,"essai(s)")
    elif choix < nbHasard:
        print("le nombre est plus grand!")
        chance = chance - 1;
        print("dommage c'est pas ça il vous reste," ,chance,"essai(s)")
if choix == nbHasard:
    print("félicitations!")
       
        
        
