L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
x = 0
y = 0

for i in range(len(L1)):
    current = L1[i]
    count = 0
    for j in range(i, len(L1)):
        if L1[j] == current:
            count +=1
    if count > y:
        y = count
        x = current
print("Le nombre le plus frequent dans la liste est le : {} ({} x)".format(x, y))



""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
