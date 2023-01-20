def taille_chaine(T):
    compteur = 0
    for i in T:
        if i == "":
            break
        compteur += 1
    return compteur

def pourcentage_voyelles(T):
    compteur_voyelles = 0
    compteur_total = 0
    for i in T:
        if i == "":
            break
        compteur_total += 1
        if i in "aeiouAEIOU":
            compteur_voyelles += 1
    return (compteur_voyelles / compteur_total) * 100

def sous_chaine(T, sous_chaine):
    for i in range(len(T)):
        if T[i:i+len(sous_chaine)] == sous_chaine:
            return i
    return -1

def nombre_occurrences(T, sous_chaine):
    compteur = 0
    index = T.find(sous_chaine)
    while index != -1:
        compteur += 1
        index = T.find(sous_chaine, index+1)
    return compteur

def menu():
    T = input("Entrez la chaine à traiter: ")
    print("Que voulez-vous faire avec cette chaine? ")
    print("1 - Calculez la taille de la chaine")
    print("2 - Calculer le pourcentage de voyelles dans la chaine")
    print("3 - Tester si 'wagon' est une sous-chaine de T")
    print("4 - Calculer le nombre d'occurrences de 'wagon' dans T")
    choice = int(input())
    if choice == 1:
        print("La taille de la chaine est:", taille_chaine(T))
    elif choice == 2:
        print("Le pourcentage de voyelles dans la chaine est:", pourcentage_voyelles(T), "%")
    elif choice == 3:
        result = sous_chaine(T, "wagon")
        if result != -1:
            print("'wagon' est une sous-chaine de T et débute à l'index", result)
        else:
            print("'wagon' n'est pas une sous-chaine de T")
    elif choice == 4:
        print("Le nombre d'occurrences de 'wagon' dans T est:", nombre_occurrences(T, "wagon"))
    else:
        print("Entrée invalide. Veuillez sélectionner une option valide.")

menu()
