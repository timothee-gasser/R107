entre = int(input("Entrez un nombre entier:"))

if entre > 0 :
    x = 'positif'
    if entre % 2 == 0 :
        y = 'pair'
    else :
        y = 'impair'
    print("Le nombre est {} et {}".format(x, y))

else :
    if entre < 0:
        x = 'negatif'
        if entre % 2 == 0:
            y = 'pair'
        else:
            y = 'impair'
        print("Le nombre est {} et {}".format(x,y))

    else:
        print("Le nombre est zéro (et il est pair)")


