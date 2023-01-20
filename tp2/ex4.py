BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400
convives = int(input("Entrez le nombre de personne(s) conviées à la fondue :"))

fromage = fromage * convives / BASE
eau = eau * convives / BASE
ail = ail * convives / BASE
pain = pain * convives / BASE

print("Pour faire une fondue fribourgeoise pour {} personnes, il vous faut :\n- {} gr fromage\n- {} dl d'eau\n- {} gousse(s) d'ail\n- {} gr de pain".format(convives,fromage,eau,ail,pain))