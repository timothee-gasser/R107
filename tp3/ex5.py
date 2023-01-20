debut = int(input("Donnez l'heure de début de la location (un entier) : "))
fin = int(input("Donnez l'heure de fin de la location (un entier) : "))
x = 0
tarifstandard = 0
tarifmajore = 0

while debut == fin or debut>fin or debut<0 or debut>24 or fin>24 or fin<0:

    if debut>fin:
        print("Attention ! le début de la location est après la fin ...")
        print("\n")
        debut = int(input("Donnez l’heure de début de la location (un entier) :"))
        fin = int(input("Donnez l’heure de fin de la location (un entier) :"))

    if debut==fin:
        print("Attention ! l’heure de fin est identique à l’heure de début. ")
        print("\n")
        debut = int(input("Donnez l’heure de début de la location (un entier) :"))
        fin = int(input("Donnez l’heure de fin de la location (un entier) :"))

    if (debut > 24 or debut < 0) or (fin > 24 or fin < 0):
        print("Les heures doivent être comprises entre 0 et 24 !")
        print("\n")
        debut = int(input("Donnez l’heure de début de la location (un entier) :"))
        fin = int(input("Donnez l’heure de fin de la location (un entier) :"))



for i in range(debut,fin):

    if i>=7 and i<17:
        x += 2
        tarifmajore += 1

    if i<=7 and i>0 or i>=17 and i<24:
        x += 1
        tarifstandard+=1

print("Vous avez loué votre vélo pendant")
print(tarifstandard,"heure(s) au tarif horaire de 1.0 euro(s)")

if tarifmajore > 0:

    print(tarifmajore,"heure(s) au tarif horaire de 2.0 euro(s)")

print("Le montant total à payer est de", x ,"euro(s).")



