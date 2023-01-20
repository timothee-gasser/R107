nMax = 3
v1 = []
v2 = []

n = int(input("Quelle est la taille de vos vecteurs [entre 1 et {}] ? ".format(nMax)))
while n < 1 or n > nMax:
    n = int(input("La taille doit être comprise entre 1 et {}. Quelle est la taille de vos vecteurs ? ".format(nMax)))

print("Saisie du premier vecteur :")
for i in range(n):
    v1.append(int(input("v1[{}] = ".format(i))))

print("Saisie du second vecteur :")
for i in range(n):
    v2.append(int(input("v2[{}] = ".format(i))))

produit_scalaire = sum(v1[i] * v2[i] for i in range(n))

print("Le produit scalaire de v1 par v2 vaut {}".format(produit_scalaire))