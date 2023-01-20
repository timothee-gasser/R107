def table_multiplication(nombre):
    table = []
    for i in range(10):
        resultat = nombre * i
        table.append(resultat)
    return table

nombre = float(input("Vous cherchez la table de multiplication de quel nombre ? "))
resultats = table_multiplication(nombre)

for i, resultat in enumerate(resultats):
    print(f"{nombre} * {i} = {round(resultat, 2)}")