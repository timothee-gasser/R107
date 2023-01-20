f=input("saisiser votre prenom:")
n=input("saisiser votre nom:")
p=input("saisiser votre promo:")
g=input("saisiser votre group : ")
my_dict = {
    "name": n,
    "firstname": f,
    "promo": p,
    "group": g
}

print("Votre nom est '" + my_dict["name"] + "', prénom est '" + my_dict["firstname"] + "', vous faites partie de la promo '" + my_dict["promo"] + "' et votre groupe est '" + my_dict["group"] + "'.")

print("Les clés du dictionnaire sont :")
for key in my_dict.keys():
    print("-" + key)

print("Les valeurs du dictionnaire sont :")
for value in my_dict.values():
    print("-" + str(value))

print("Les tuplets du dictionnaire sont :")
for item in my_dict.items():
    print("-(" + item[0] + ", " + str(item[1]) + ")")

x = input("avez vous un binome? y|n :")

if x=="y":
    f2 = input("saisiser sont prenom:")
    n2 = input("saisiser sont nom:")
    p2 = input("saisiser sont promo:")
    g2 = input("saisiser sont group : ")
    partner_dict = {
        "name": n2,
        "firstname": f2,
        "promo": p2,
        "group": g2
    }
    print("Le nom de votre binome est '" + my_dict["name"] + "', prénom est '" + my_dict["firstname"] + "', il faites partie de la promo '" + my_dict["promo"] + "' et est dans le groupe '" + my_dict["group"] + "'.")

    print("Informations sur mon binôme :")
    print("Les clés du dictionnaire sont :")
    for key in partner_dict.keys():
        print("-" + key)

    print("Les valeurs du dictionnaire sont :")
    for value in partner_dict.values():
        print("-" + str(value))

    print("Les tuplets du dictionnaire sont :")
    for item in partner_dict.items():
        print("-(" + item[0] + ", " + str(item[1]) + ")")

    id1 = input("Saisissez votre numéro de poste en tant qu'identifiant:")
    id2 = input("Saisissez le numéro de poste de votre binôme en tant qu'identifiant:")

    binôme = {
        id1: my_dict,
        id2: partner_dict
    }

    print("Les identifiants et les informations des membres du binôme sont:")
    for key, value in binôme.items():
        print("Identifiant: " + key)
        for key2, value2 in value.items():
            print("-" + key2 + ": " + str(value2))
    print("Les étudiants formant le binôme sont :")
    for key, value in binôme.items():
        print("- L'étudiant " + value["firstname"] + " " + value["name"] + " du groupe " + value["group"])