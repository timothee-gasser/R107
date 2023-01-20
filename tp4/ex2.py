nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
notes = []

for i in range(nombreEtudiants):
    note = float(input(f"Note etudiant {i} : "))
    while note < 0 or note > 20:
        note = float(input(f"Note doit être entre 0 et 20. Note etudiant {i} : "))
    notes.append(note)
    moyenne += note

moyenne /= nombreEtudiants
print("Moyenne de classe :",round(moyenne,2))
print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i, note in enumerate(notes):
    ecart = round(note - moyenne,2)
    print(f"{i} | {note} | {ecart}")

