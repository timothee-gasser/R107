binome = ("Timothée", "Ela")
print("L'étudiant " + binome[0] + " est en binome avec l'étudiante " + binome[1])

n = input("voulez vous changer de binôme? y|n :")
if n == "y":
    new = input("Entrez le nouveau login de votre binôme: ")
    binome = (binome[0], new)
    print("L'étudiant", binome[0], "est maintenant en binome avec l'étudiant", binome[1])

s = input("voulez vous suprimer votre binôme? y|n :")
if s == "y":
    binome = list(binome)
    del binome[1]
    binome = tuple(binome)
    print(binome)

else:
    x = input("voulez vous vous metre en trinôme? y|n :")

    if x == "y":
        new3 = input("Entrez le nouveau login de votre trinôme: ")
        binome = (binome[0],binome[1], new3)
        print(binome)
    else:
        exit()
