
somme = int(input("Entrez une somme d'argent : "))
somme_initiale = somme

billets_100 = somme // 100
somme = somme % 100


billets_50 = somme // 50
somme = somme % 50


billets_10 = somme // 10
somme = somme % 10


pieces_2 = somme // 2
somme = somme % 2


pieces_1 = somme


print("{} euros, c'est donc {} billets de 100, {} de 50, {} de 10, {} pièces de 2 et {} pièce 1.".format(somme_initiale, billets_100, billets_50, billets_10, pieces_2, pieces_1))