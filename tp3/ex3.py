from random import *
x = randint(0,100)
y=0
a=0
while True:
    y = int(input("Deviner la valeur :"))
    if y == x:
        a=a+1
        print("vous avez trouver en {} tour ".format(a))
        break
    else:
        if y<x :
            a = a + 1
            print("La valeur est plus grande")

        else:
            if y>x :
                a = a + 1
                print("La valeur est plus petit")