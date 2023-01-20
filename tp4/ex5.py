date = input("Entrez la date (jjmmaaaa): ")

if len(date) != 8:
    print("La date n'est pas au bon format. Veuillez corriger votre saisie.")
    exit()

jour = int(date[:2])
mois = int(date[2:4])
annee = int(date[4:])

if mois not in range(1, 13):
    print("Le mois est invalide. Veuillez corriger votre saisie.")
    exit()


if mois in [4, 6, 9, 11] and jour not in range(1, 31):
    print("Le jour est invalide pour ce mois. Veuillez corriger votre saisie.")
    exit()
elif mois == 2:
    if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
        if jour not in range(1, 30):
            print("Le jour est invalide pour ce mois. Veuillez corriger votre saisie.")
            exit()
    else:
        if jour not in range(1, 29):
            print("Le jour est invalide pour ce mois. Veuillez corriger votre saisie.")
            exit()
elif jour not in range(1, 32):
    print("Le jour est invalide pour ce mois. Veuillez corriger votre saisie.")
    exit()

print("La date est valide.")