import random

def generer_et_combien(nbr=100, vmin=0, vmax=100, seuil=30):
    tab = [random.randint(vmin, vmax) for _ in range(nbr)]
    tab.sort()
    print(tab)
    total = len([x for x in tab if x < seuil])
    print(f"Il y en a {total} inférieurs à {seuil}")

nb = int(input("Combien de nombres voulez-vous générer ? "))
vmin = int(input("Valeur minimale : "))
vmax = int(input("Valeur maximale : "))
reponse = input("Voulez-vous préciser le seuil ? O|N : ")
seuil = int(input("Valeur du seuil : ")) if reponse in ['O', 'Oui', 'o'] else 30

generer_et_combien(nb, vmin, vmax, seuil)