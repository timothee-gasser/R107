i=0
x=0
y=0
z=0
while i < 10:
    n = int(input("Entrez un entier: "))
    while not(0 <= n <= 20 ):
        n = int(input("Entrez un autre entier: "))
    i = i+1
    if n<10:
        x = x+1
    else :
        if n>=15:
            y = y +1

        else:
            z=z+1

print("Il y a {} nombre d'une valeurs inférieur strictement à 10\nIl y a {} nombre d'une valeurs supérieur ou égale à 10 et inférieur strictement à 15\nIl y a {} nombre d'une valeurs supérieur ou égale à 15 ".format(x,z,y))


